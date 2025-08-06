# ExtendedLangtonLanguage
ExtendedLangtonLanguage is a programming language operating on a black-and-white board with three instructions and one „operator” moving through it. An implementation has been written in Python, however, because of performance reasons, I shall write a C one. In order to use the implementation, clone, then run basic_frontend.py and enter the commands. The only dependency is Python.

The operator starts from [0,0], turning towards [1,0]. When it leaves a field, if tha field has been white, turns black, and vice versa. There are threee commands: l, r and c. „l” turns left and moves forward; „r” turns right and moves forward; „c” turns left if the actually occupied field is black, right otherwise. An initial board can be given arbitrarily. As Langton's ant is Turing-complete, and this can emulate Langton's ant, with ccc... ExtendedLangtonLanguage is Turing-complete as well.

# The PHP implementation

The PHP implementation is located at el_implementation.php. It requests one POST argument, command, the output format is:
```
[x position at the end];[y position at the end]
(direction like (1;0))
[board in x,y,value format]
```
You can try it with a simple form at https://harizalan.hu/extendedlangton/index.php
Also, at https://harizalan.hu/extendedlangton/el.php, you can use it as an API, without the need of installing anything.
