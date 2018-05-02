class Song(object):

   def __init__(self, lyrics):
      self.lyrics = lyrics

   def sing_me_a_song(self):
      for line in self.lyrics:
         print(line)
#
happy_bday = Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_and_you_know_it = Song(["If your happy and you know it",
                              "Clap your hands!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

happy_and_you_know_it.sing_me_a_song()

# this is a seperate variable that does the same thing
hsong = Song(happy_bday.lyrics)
hsong.sing_me_a_song()
