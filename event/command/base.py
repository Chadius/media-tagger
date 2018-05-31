class UnknownCommandException(Exception):
    pass

class Command(object):
    """Encapsulate an request that acts upon an object.
    """

    def __init__(self, *args, **kwargs):
        # Track the object that will act.
        self.actor = kwargs['actor']

        # Did the actor start executing?
        self.started_execution = False

        # Did the actor finish executing?
        self.finished_execution = False

    def has_started(self):
        """Returns True if the Command started execution.
        """
        return self.started_execution == True

    def has_finished(self):
        """Returns True if the Command finished execution.
        """
        return self.finished_execution == True
    def execute(self):
        """Perform the command on the actor.
        """
        self.started_execution = True

    def undo(self):
        """Reverse the effects of the execute command.
        """
        pass

class CommandController(object):
    """Base class that accepts a bunch of Command objects.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        # A list of Command objects
        self.command_queue = []

    def add_command(self, new_command):
        """Adds a Command to the queue.
        """
        self.command_queue.append(new_command)

    def process_commands(self):
        """Tries to process commands.
        """
        # If there are no commands, we're done.
        if len(self.command_queue) == 0:
            return

        # If the current command has started but not finished, wait for it to finish.
        current_command = self.command_queue[0]
        if current_command.has_started() and not current_command.has_finished():
            return

        # Collect a list to remove after execution.
        commands_to_delete = []

        # For each command in the queue,
        for command in self.command_queue:
            # Get the command and try to execute it unless it is already running.
            if not command.has_started():
                self.handle_command(command)
                # If it did not start, then it means we don't recognize this command. Raise an Exception.
                if not command.has_started():
                    raise UnknownCommandException("Base CommandController cannot handle commands of type {command_type}.".format(command_type=type(current_command)))
            # If it finished, mark the command for removal.
            if command.has_finished():
                commands_to_delete.append(command)
        # Remove all commands in the queue.
        for command in commands_to_delete:
            self.command_queue.remove(command)

    def handle_command(self, command):
        """Subclasses will inspect and handle commands.
        They should mark the command has started execution.
        """
        pass
