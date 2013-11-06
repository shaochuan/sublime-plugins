import sublime, sublime_plugin

class NewLayoutCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):
    self.view.window().run_command("set_layout", args)
    self.view.window().run_command("focus_group", { "group": 0 })
    self.view.window().run_command("move_to_group", { "group": 1 } )
