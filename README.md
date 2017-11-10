# LoadTest
A toy example for a neovim plugin written in python3.

## Description
If you open a file FN, this plugin will look from your current working directory downwards for a file test_FN and loads it in a buffer.
This happens only for python files, i.e. files having a '.py' extension.

## Installation
Install with vim-plug and do a :UpdateRemotePlugin.
