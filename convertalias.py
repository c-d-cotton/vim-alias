#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

def convert_func(bashfilename, outputfolder):
    with open(bashfilename, 'r', encoding = 'latin-1') as f:
        aliases_bash = f.read().splitlines()
    aliases_bash = [alias.replace('"', '').replace("'",'') for alias in aliases_bash if not alias.startswith('#')]
    aliases = [alias.split('=') for alias in aliases_bash]

    aliases_vim = [':cabbrev ' + ' '.join(alias) for alias in aliases]
    aliases_ultisnips = ['snippet ' + alias[0] + ' "" i\n' + alias[1] + '/' + '\nendsnippet' for alias in aliases]

    with open(outputfolder + 'vimalias.vim', 'w+') as f:
        f.writelines('\n'.join(aliases_vim))

    with open(outputfolder + 'ultisnipsalias.snippets', 'w+') as f:
        f.writelines('\n'.join(aliases_ultisnips))
