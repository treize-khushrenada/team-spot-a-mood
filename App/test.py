from pathlib import Path
#print(Path(__file__).parent.parent)
import os

DIR_ABS_PATH = os.path.dirname(__file__)

parent = Path(__file__).parent.parent

abs = os.path.join(parent, '/pickle_objects/sample_song_lyrics_set.obj')
print(abs)
