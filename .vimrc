set runtimepath+=~/.vim_runtime

source ~/.vim_runtime/vimrcs/basic.vim
source ~/.vim_runtime/vimrcs/filetypes.vim
source ~/.vim_runtime/vimrcs/plugins_config.vim
source ~/.vim_runtime/vimrcs/extended.vim
"line number
set number relativenumber
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END
set encoding=utf-8
try
source ~/.vim_runtime/my_configs.vim
catch
endtry

call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree'
Plug 'junegunn/vim-easy-align'
Plug 'tmhedberg/SimpylFold'
Plug 'vim-scripts/indentpython.vim'
"plug 'vim-syntastic/syntastic'
Plug 'nvie/vim-flake8'
Plug 'jnurmine/Zenburn'
Plug 'altercation/vim-colors-solarized'
Plug 'kien/ctrlp.vim'
"Plug 'ycm-core/YouCompleteMe', { 'do': './install.py' }
call plug#end()
syntax on
" Enable folding
set foldmethod=indent
set foldlevel=99
" Enable folding with the spacebar
nnoremap <space> za
"show the matching part of the pair for [] {} and ()
set showmatch
" enable syntax highlighting
syntax enable
set mouse=a
