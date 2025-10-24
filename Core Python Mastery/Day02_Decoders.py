# Decoders - A Function that acts as a wrapper to an existing function:
# Add a starting and ending line to it using decoders - Adding behaviour to this existing function
def new_decorator(func):
  def wrapper():
    print('Start')
    func()
    print('End')
  return wrapper


#  Application
@new_decorator
def greet():
  print('Hello')

greet()
