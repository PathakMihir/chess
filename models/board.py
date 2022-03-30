class board:

    def __init__(self,board_size,cells):
        self.board_size=board_size
        self.cells=cells

    def get_left_cell(self,cell):
    	return self.get_cell_at_location(cell.x,cell.y-1)

    def get_right_cell(self,cell):
        return self.get_cell_at_location(cell.x,cell.y+1)

    def get_top_cell(self,cell):
        return self.get_cell_at_location(cell.x+1,cell.y)

    def get_down_cell(self,cell): 
        return self.get_cell_at_location(cell.x-1,cell.y)

    def get_cell_at_location(self,x,y):

    	if(x>self.board_size or y>self.board_size or x<0 or y<0):
    		return None
    	else:
    	    return self.cells[x][y]	

    
    def is_player_on_check(self,player):
    	return self.check_if_piece_can_be_killed()


    def check_if_piece_can_be_killed(self):
        pass 	
