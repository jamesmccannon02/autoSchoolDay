# Automatically open your applications for school (Under development)

This is designed to open a number of applications on startup using a simple ```school``` command within the command prompt

# Installation

```
git clone https://github.com/jamesmccannon02/autoSchoolDay.git
```

This will install the files into your current directory

Then you need to add your application to the path. On mad do the following:

1. ```nano ~/.zshrc```
2. Add the following
    ```
   function school(){
    python ~/[path to file] $1
    }
    ```
3. Exit and save
4. Now in terminal run ```. ~/.zshrc```
5. Then all you have to do is run ```school``` to run the python script