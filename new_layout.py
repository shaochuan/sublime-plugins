import sublime, sublime_plugin

class NewLayoutCommand(sublime_plugin.WindowCommand):
  def run(self, **args):
    print(dir(self))
    self.window.run_command("set_layout", args)
    self.window.run_command("focus_group", { "group": 0 })
    self.window.run_command("move_to_group", { "group": 1 } )
