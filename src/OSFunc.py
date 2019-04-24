import os


def make_sound_listing(sound):
    sound_dir = "../bin/sounds/{sound}".format(sound=sound)
    sound_listing = {
        "key": sound,
        "imgExt": get_img_ext_from_dir(sound_dir)
    }
    return sound_listing


def get_sound_ext_from_dir(sound_dir):
    return get_ext_from_dir(sound_dir, "sound.")


def get_img_ext_from_dir(sound_dir):
    return get_ext_from_dir(sound_dir, "img.")


def get_ext_from_dir(sound_dir, key):
    files = os.listdir(sound_dir)
    return list(filter(lambda x: key in x, files))[0].split(".")[-1]
