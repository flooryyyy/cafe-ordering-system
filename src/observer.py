# define a class for order observer
class OrderObserver:
    # this is a base class
    # subclasses override update() to do something when order changes
    def update(self, order):
        pass

# this class lets Order notify observers when it changes
class OrderSubject:
    def __init__(self):
        self._observers = [] # list of observers watching this order
    
    # add an observer to the list
    def add_observer(self, observer):
        self._observers.append(observer)
    
    # remove an observer from the list
    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    # tell all observers that something changed
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)