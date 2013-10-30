import sublime, sublime_plugin
import re

def toggle(pattern, word, transformer):
  for match in pattern.finditer(word):
    substr = match.group()
    word = word.replace(substr, transformer(substr))
  return word

def mixed_to_underscore(word):
  return '_' + word.lower()

def underscore_to_mixed(word):
  return word.replace('_','').capitalize()

def is_letter_type(pattern, word):
  return bool(pattern.search(word))

class ToggleCapLettersCommand(sublime_plugin.TextCommand):
  ''' This plugin transforms the select words from
      setVarName   -> set_var_name or
      set_var_name -> setVarName
  '''
  mixed_cap_letters = re.compile("[A-Z][a-z]+")
  underscore_letters = re.compile("[_][a-z]+")
  def run(self, edit, *args):
    for point in self.view.sel():
      word_region = self.view.word(point)
      word = self.view.substr(word_region)
      new_word = ''
      if is_letter_type(self.mixed_cap_letters, word):
        new_word = toggle(self.mixed_cap_letters, word, mixed_to_underscore)
      elif is_letter_type(self.underscore_letters, word):
        new_word = toggle(self.underscore_letters, word, underscore_to_mixed)
      
      if new_word:
        self.view.erase(edit, word_region)
        self.view.insert(edit, word_region.begin(), new_word)
