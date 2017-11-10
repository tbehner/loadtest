import neovim
import os
from os import path

@neovim.plugin
class TestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    def search_test_file(self, filename):
        wd = self.nvim.command_output('pwd').strip()
        test_filename = 'test_' + path.basename(filename)
        for dirpath, dirnames, filenames in os.walk(wd):
            for fn in filenames:
                if test_filename == fn:
                    return path.join(dirpath, fn)

    def _open_test_file(self, filename):
        test_file = self.search_test_file(filename)
        if test_file:
            self.nvim.command('badd ' + test_file)

    @neovim.autocmd('BufAdd', pattern='*.py', eval='expand("<afile>")', sync=True)
    def on_bufadd(self, filename):
        self._open_test_file(filename)
        self.nvim.out_write("Loaded test file for " + filename + "\n")
