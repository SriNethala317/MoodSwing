from mplayer import Player, CmdPrefix
from download_song import *
import os

def play_audio(song):
    Player.cmd_prefix = CmdPrefix.PAUSING_KEEP
    player = Player()
    print(os.getcwd() + "\\" + SONGSFOLDER + "\\" + song.get_filename())
    # player.loadfile()