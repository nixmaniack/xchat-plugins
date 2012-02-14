#!/usr/bin/env python

__module_name__ = "DictBot"
__module_version__ = "0.1"
__module_description__ = "DictBot by Muneeb"

import xchat
import os


print "\0034",__module_name__, __module_version__,"has been loaded\003"

def getDefinition(word, word_eol, userdata):
    if word[0] == 'define':
        cmd = 'dict %s' % (word[1])
        fi, fo, fe = os.popen3(cmd)
        for i in fo.readlines():
            print i,

    return xchat.EAT_ALL

xchat.hook_command('define', getDefinition, help="Usage: /define word")
