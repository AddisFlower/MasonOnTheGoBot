from discord.ext import commands


class CustomEvents(commands.Cog):
    event_list = []
    event_num = 0

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='createEvent', aliases=['createEvents'],
                      description='Command that creates a custom event with a unique key ands adds it to the event list created by the members of the discord server. Each argument needs to be separated by a |.')
    async def create_event(self, ctx, *, args):
        arg_list = args.split(" | ")
        if len(arg_list) != 7:
            await ctx.send("Please enter the required arguments when using this command.")
        name = arg_list[0]
        start_date = arg_list[1]
        end_date = arg_list[2]
        start_time = arg_list[3]
        end_time = arg_list[4]
        location = arg_list[5]
        description = arg_list[6]

        event = Event(name, start_date, end_date, start_time, end_time, location, description)
        self.event_list.append(event)
        self.event_num += 1
        event.set_event_id(self.event_num)
        response = "Event " + event.name + " with id " + str(event.get_event_id()) + " added!"
        await ctx.send(response)

    @commands.command(name='setEventName',
                      description='Command that sets the name of an event in the event list with the given id.')
    async def set_event_name(self, ctx, event_id, *, name):
        found = False
        for event in self.event_list:
            if str(event.get_event_id()) == str(event_id):
                found = True
                event.set_name(name)
                await ctx.send("Event " + str(event.get_event_id()) + " name successfully changed to " + name)
        if not found:
            await ctx.send("There is currently no event with the given id.")

    @commands.command(name='setEventStartDate',
                      description='Command that sets the start date of an event in the event list with the given id.')
    async def set_event_start_date(self, ctx, event_id, *, start_date):
        found = False
        for event in self.event_list:
            if str(event.get_event_id()) == str(event_id):
                found = True
                event.set_start_date(start_date)
                await ctx.send("Event " + str(event.get_event_id()) + " start date successfully changed to " + start_date)
        if not found:
            await ctx.send("There is currently no event with the given id.")

    @commands.command(name='setEventEndDate',
                      description='Command that sets the end date of an event in the event list with the given id.')
    async def set_event_end_date(self, ctx, event_id, *, end_date):
        found = False
        for event in self.event_list:
            if str(event.get_event_id()) == str(event_id):
                found = True
                event.set_end_date(end_date)
                await ctx.send("Event " + str(event.get_event_id()) + " end date successfully changed to " + end_date)
        if not found:
            await ctx.send("There is currently no event with the given id.")

    @commands.command(name='setEventStartTime',
                      description='Command that sets the start time of an event in the event list with the given id.')
    async def set_event_start_time(self, ctx, event_id, *, start_time):
        found = False
        for event in self.event_list:
            if str(event.get_event_id()) == str(event_id):
                found = True
                event.set_start_time(start_time)
                await ctx.send("Event " + str(event.get_event_id()) + " start time successfully changed to " + start_time)
        if not found:
            await ctx.send("There is currently no event with the given id.")

    @commands.command(name='setEventEndTime',
                      description='Command that sets the end time of an event in the event list with the given id.')
    async def set_event_end_time(self, ctx, event_id, *, end_time):
        found = False
        for event in self.event_list:
            if str(event.get_event_id()) == str(event_id):
                found = True
                event.set_end_time(end_time)
                await ctx.send("Event " + str(event.get_event_id()) + " end time successfully changed to " + end_time)
        if not found:
            await ctx.send("There is currently no event with the given id.")

    @commands.command(name='setEventLocation', description='Command that sets the location of an event in the event list with the given id.')
    async def set_event_location(self, ctx, event_id, *, location):
        found = False
        for event in self.event_list:
            if str(event.get_event_id()) == str(event_id):
                found = True
                event.set_location(location)
                await ctx.send("Event " + str(event.get_event_id()) + " location successfully changed to " + location)
        if not found:
            await ctx.send("There is currently no event with the given id.")

    @commands.command(name='setEventDescription', description='Command that sets the description of the an event in the event list with the given id.')
    async def set_event_description(self, ctx, event_id, *, description):
        found = False
        for event in self.event_list:
            if str(event.get_event_id()) == str(event_id):
                found = True
                event.set_description(description)
                await ctx.send("Event " + str(event.get_event_id()) + " description successfully changed to " + description)
        if not found:
            await ctx.send("There is currently no event with the given id.")

    @commands.command(name='displayEvents', description='Command that lists all the events that have been created.')
    async def display_events(self, ctx):
        if len(self.event_list) == 0:
            await ctx.send("There are currently no events in this discord server.")
        else:
            for event in self.event_list:
                response = "**Event " + str(event.get_event_id()) + ": " + event.get_name() + "**\n"
                response += " `From " + event.get_start_date() + " to " + event.get_end_date() + "\n"
                response += " From " + event.get_start_time() + " to " + event.get_end_time() + "\n"
                response += " Location: " + event.get_location() + "\n"
                response += " Description: " + event.get_description() + "`\n"
                await ctx.send(response)

    @commands.command(name='clearEvents', description='Command that removes all the events that have been created.')
    async def clear_events(self, ctx):
        if len(self.event_list) == 0:
            await ctx.send("There are no created events already!")
        else:
            self.event_list.clear()
            await ctx.send("All events have been successfully removed!")

    @commands.command(name='removeEvent', description='Command that removes a specific event from the list of events')
    async def remove_event(self, ctx, event_id):
        found = False
        for event in self.event_list:
            if str(event_id) == str(event.event_id):
                found = True
                self.event_list.remove(event)
                await ctx.send("Event " + str(event.get_event_id()) + " has been successfully removed!")
        if not found:
            await ctx.send("There is currently no event with the given id.")


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
