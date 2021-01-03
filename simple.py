
from translate import Translator

while True:
   words = input('What words you want to translate ?  ')
   from_lang = input('\nwhat language you translate from？ ')
   to_lang = input('\nLanguage you want translate to? ')

   translator= Translator(from_lang ,to_lang)
   translation = translator.translate(words)
   print (translation)