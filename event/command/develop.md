# How to use Commands
Commands encapsulate an object and an action to apply to it. This helps you delay the action and decouple the caller at a later time.

If you look in base.py, you'll see the basic classes: Command and CommandController.

# Command class
When constructing a Command, set the actor parameter. Set the actor parameter to the object that will perform an action.

Subclasses may require different parameters, you'll have to look at the definitions there.

## Functions
### has_started(self)
Returns True if the Command started executed. This still returns True if it finishes execution.
### has_finished(self)
Returns True if the Command finished execution.
### is_undoable(self)
Returns True if the Command can be reversed. Defaults to False.
Override this function if you want to make reversible Commands.
### undo(self)
Calling undo will actually reverse the Command's effects.
Override this function if to actually undo the effects.
### execute(self)
Actually perform the action upon Command.actor .
Override this function when making a subclass.

# CommandController
Command Controllers actually processes Command objects.
## Functions
### add_command(self, new_command)
Adds a new Command object to be processed later.
### process_commands(self)
Calling this will try to trigger Command objects in FIFO (First In First Out) order.

This will process Command objects until a Command is still executing. Call process_commands again when the Command completes.

### handle_command(self, command)
This function processes the given command immediately.

process_commands() will call this to do the actual execution.

Subclass this function to handle different types of Commands. This function should start executing the given command.

If command.has_started() returns False, process_commands will raise an UnknownCommandException.
### can_undo_last_command(self)
Returns True if the previously executed Command can be undone.
If no Commands have been executed, this returns False.
### undo_last_command(self)
Call this function to undo the last executed Command.
You can call this multiple times to undo the previous executed Command. If a command cannot be undone, executing this will clear the history.