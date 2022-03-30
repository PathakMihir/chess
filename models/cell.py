class cell:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.current_piece=None

    def current_piece_setter(self,piece):
    	self.current_piece=piece
 
    def is_free(self):
        self.current_piece=None





