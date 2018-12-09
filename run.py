from flaskblog import app

# Every module in python has a special attribute called __name__ .
# The value of __name__  attribute is set to '__main__'  when 
# module run as current program. Otherwise the value of __name__  
# is set to contain the name of the module which is currently running.
if __name__ == "__main__":
    app.run(debug = True)