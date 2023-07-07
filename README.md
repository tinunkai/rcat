# rcat

"raw" cat for passthroughing escape characters in tmux.  
Mainly for [sixel protocal], [Kitty Graphics Protocol] and [iTerm2 Graphics Protocol].  
Remember to add
```
set-option -g allow-passthrough on
```
in `.tmux.conf`.

[sixel protocal]: https://en.wikipedia.org/wiki/Sixel
[Kitty Graphics Protocol]: https://sw.kovidgoyal.net/kitty/graphics-protocol
[iTerm2 Graphics Protocol]: https://iterm2.com/documentation-images.html
