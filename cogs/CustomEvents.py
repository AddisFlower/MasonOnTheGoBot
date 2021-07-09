from discord.ext import commands


class CustomEvents(commands.Cog):
    event_list = []

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='createEvent', aliases=['createEvents'],
                      description='Command that creates a custom event with a unique key ands adds it to the event list created by the members of the discord server. Each argument needs to be seperated by a |.')
    async def create_event(self, ctx, *, args):
        arg_list = args.split(" | ")
        name = arg_list[0]
        start_date = arg_list[1]
        end_date = arg_list[2]
        start_time = arg_list[3]
        end_time = arg_list[4]
        location = arg_list[5]
        description = arg_list[6]

        event = Event(name, start_date, end_date, start_time, end_time, location, description)
        self.event_list.append(event)
        event.set_event_id(len(self.event_list))
        response = "Event " + event.name + " with id " + str(event.get_event_id()) + " added!"
        await ctx.send(response)

    @commands.command(name='setEventLocation', description='Command that sets the location of an event in the event list with the given id.')
    async def set_event_location(self, ctx, event_id, *, location):
        for event in self.event_list:
            if str(event.event_id) == str(event_id):
                event.set_location(location)
                print(event.get_location())

    @commands.command(name='setEventDescription', description='Command that sets the description of the an event in the event list with the given id.')
    async def set_event_description(self, ctx, event_id, *, description):
        for event in self.event_list:
            if str(event.event_id) == str(event_id):
                event.set_description(description)
                print(event.get_description())

    @commands.command(name='displayEvents', description='Command that lists all the events that have been created.')
    async def display_events(self, ctx):
        for event in self.event_list:
            response = "**Event " + str(event.get_event_id()) + ": " + event.get_name() + "**\n"
            response += " `From " + event.get_start_date() + " to " + event.get_end_date() + "\n"
            response += " From " + event.get_start_time() + " to " + event.get_end_time() + "\n"
            response += " Location: " + event.get_location() + "\n"
            response += " Description: " + event.get_description() + "`\n"
            await ctx.send(response)


class Event:
    name = ""
    event_id = ""
    start_date = ""
    end_date = ""
    start_time = ""
    end_time = ""
    location = ""
    description = ""

    def __init__(self, name, start_date, end_date, start_time, end_time, location, description):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.description = description

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_event_id(self, event_id):
        self.event_id = event_id

    def get_event_id(self):
        return self.event_id

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description


def setup(bot):
    """Necessary setup function"""
    bot.add_cog(CustomEvents(bot))
