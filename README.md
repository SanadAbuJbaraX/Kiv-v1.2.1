# Kiv-v1.2.1 🔥
source code of dynamic Kiv programming language v1.1.0 (finale version of v1)
# If your os supports .exe
- add builds folder to enviroment variables then
# Run 🕹️
- First time only
- run setup.exe or python setup.py 
If os supports .exe
- kiv file.kiv
else
- ```python PATH/To/repositry/kiv file.kiv```
# Shell 🐢
If os supports .exe
- kivshell
else
- ```python PATH/To/repositry/kiv/kivshell.py```
# Future 🔮
this is sll a beta version meaning not all binaries are found very few buildin functions and libraries and bad perfermonce hopefully all if this will be fixed in kiv v2
# Syntax
# Comments
Can be at start of line or end
startwith '//'
``` 
// Comment here
```
# Functions
```
function name(param1,param2) do
  "CODE HERE"
   return "OPTIONAL AND ANY TYPE"
end
// One line
function x(a,b) -> a+b // returns auto a + b
```
# Lambda 
```
function() -> print("F")
```
# Variables
```
// var variable_name = variable_value
var age = 13
var name = "Sanad:
```
# For Loops
```
for i=0 until 5 do 
  print(i)
end
``` 
this will from 0 to 5 (not included the 5)
# while loops
```
while true do
  break
end
```
break breaks the loop (exit)
continue stops the operation restarts the loop (cuts)
# if elseif and else
```
  if 1==1 do
    print("OK")
  elseif 1 > 3 do
    print("NOT OK")
  else
    print("HUH")
  end // end is after the whole condition block
  if not false do
    print("THIS WILL PRINT")
  end
  if !false do
    print("THIS WILL ALSO PRINT")
  end
  ```
  use '!' or 'not' to say that if the condition is false then do 
# Builtin
- true Bool
- false Bool
- null
- GLOBALS returns all the defined variables and functions in the file
- print() :params text any type prints into terminal
- input() : params text takes input from use
- cls() : no params clears the terminal (works on every os)
- len() : params any object and returns the length of it
- index() : params object and index returns the char or elements with index passed in the object
- type() : no params returns the type of the object
- toInt() : params string or float and converts it to int
- toFloat() : params string or int converts to float
- toString() : params int,float,string,bool converts to string
- in() : params object and element checks if elem is found in object
- range() : params start and end (must be int) returns a list contating numbers between start and end
- open() : param filename returns the content of a file
- round : params number to digists (ints) rounds the number to digits (param)
# Builtin Modulesa
# Time
- sleep() : params secs (int or float) pauses the program to specific amout of secends
- counter() : no params capture time taken starts time when first called and pauses it and returns the secs takend at the the second call
# Random
- random_int() : params range start (int) , range end (int) returns a random int between range start and range end
# OS
- system_execute() : param command (str) executes the command like cmd for e.g.
# Keyboard and Mouse
- press() : param key(str) presses the key
- write() : params text(str) interval(int) writes text if interval is 0 it immediatly writes the text
- moveMouse() : params x(int) y(int) moves mouse to x and y
- size() : no params return the size of the computer as a list
- leftClick() : no params clicks the left Click
- rightClick() : no params clicks the right Click
- doubleClick() : no params double clicks
  
    
  
  
