import cherrypy
import os
import json
from playsound import playsound
import socket
from src.OSFunc import make_sound_listing, get_sound_ext_from_dir


class Root:

    def __init__(self):
        pass

    @cherrypy.expose()
    def index(self):
        return open("../bin/html/index.html")

    @cherrypy.expose()
    def get_sounds(self):
        sounds = os.listdir("../bin/sounds")
        sound_map = list(map(lambda x: make_sound_listing(x), sounds))
        return json.dumps(sound_map)

    @cherrypy.expose()
    def play_sound(self, sound):
        sound_dir = "../bin/sounds/{sound}".format(sound=sound)
        ext = get_sound_ext_from_dir(sound_dir)
        sound_file = "{dir}/sound.{ext}".format(
            dir=sound_dir,
            ext=ext
        )
        playsound(sound_file)
        return json.dumps({"sound": sound})


if __name__ == "__main__":

    cherrypy.config.update({
        'server.socket_port': 8080,
        'server.socket_host': socket.gethostbyname(socket.gethostname()),
        'response.timeout': 1600000
    })

    conf = {
        "/bin": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.abspath("../bin"),
        },
    }

    cherrypy.quickstart(Root(), config=conf)
