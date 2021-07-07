import datetime
import requests
import bs4
from discord.ext import commands, tasks


class Events(commands.Cog):
    """ This is a cog with the currentEvents command."""

    def __init__(self, bot):
        self.bot = bot

    # Command for current event list
    @commands.command(name='currentEvent', aliases=['currentEvents'],
                      description='Sends the current event list')
    async def today(self, ctx):
        base_url = "https://mason360.gmu.edu/mobile_ws/v17/mobile_events_list"

        limit = 40
        range = 0

        current_date = datetime.datetime.now()
        timestamp = current_date.timestamp()

        while True:
            got_all = False

            # generate request url
            url = "{}?range={}&limit={}&filter4_contains=OR&filter4_notcontains=OR&order=undefined&search_word=&&{}".format(
                base_url, range, limit, timestamp)
            response = requests.get(url)
            events = []

            # if request success
            if response.status_code == 200:
                data = response.json()
                to_skip = False

                # loop for data array
                for item in data:
                    fields = item['fields'].split(',')
                    html_fields = item['htmlFields']
                    listing_separator = item['listingSeparator'] == "true"
                    if listing_separator:
                        # There are listing separators such as "Ongoing", "Wed, Jul 7, 2021" ...
                        # among them, we need "Today" only
                        if item['p1'] == "Ongoing":
                            to_skip = True
                        else:
                            to_skip = False

                    if to_skip:
                        continue

                    # check if this data is event
                    if "eventDates" in fields and "eventName" in fields:
                        date_index = fields.index("eventDates")
                        name_index = fields.index("eventName")
                        event_name = item["p{}".format(name_index)]
                        event_date = item["p{}".format(date_index)]
                        # print(event_date)
                        if "eventDates" in html_fields:
                            try:
                                parsed_html = bs4.BeautifulSoup(event_date, features="lxml")
                                event_date = parsed_html.find('p').text
                            except:
                                print("exception parsing html")
                                continue

                        # print(event_date)
                        event_date = event_date.replace('–', '').strip()
                        # print(event_date)
                        try:
                            event_date = datetime.datetime.strptime(event_date, '%a, %b %d, %Y %I:%M %p')
                        except:
                            try:
                                event_date = datetime.datetime.strptime(event_date, '%a, %b %d, %Y')
                            except:
                                print("exception parsing date")
                                continue

                        # check event's date
                        if event_date.date() == current_date.date():
                            events.append("- {}".format(event_name))

                        # if date is after today...
                        # print(event_date.day, current_date.day)
                        if event_date.day > current_date.day + 0:
                            got_all = True
                            break
            # error
            else:
                await ctx.send("""
                Error getting today event list
                """)
                return

            if got_all:
                break
            range += limit

        if len(events) == 0:
            return await ctx.send("""There are no events today.""")

        await ctx.send("""
        Today Event List:
    ```{}```
        """.format("\n".join(events)))


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(Events(bot))
