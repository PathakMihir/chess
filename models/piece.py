class piece:

    def __init__(self,piece_type,color,move_providers):
        self.piece_type=piece_type
        self.color=color
        self.move_providers=move_providers
        self.no_of_moves=0
        self.is_killed=False

    def current_cell_setter(self,cell):
        self.current_cell=cell

    def kill_it(self):
        self.is_killed=True

    def move(self,player,to_cell,board,additional_blockers):
        if(self.is_killed):
            raise Exception()
        next_possible_cells=self.next_possible_cells()

        if(to_cell not in next_possible_cells):
            raise Exception()
        self.kill_piece_in_cell()
        self.current_cell.current_piece=None
        self.current_cell=to_cell
        self.current_cell.current_piece=self
        self.no_of_moves+=1

    def next_possible_cells(self,board,additional_blockers,players):
        pass

    def is_piece_from_same_player(self,piece):
        return piece.color==self.color


    def kill_piece_in_cell(self,target_cell):
        if(target_cell.current_piece!=None):
            target_cell.current_piece.kill_it()


