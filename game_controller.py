class game_controller:

    def game_play(self,players,board):
        current_player=0
        while(True):
            piece,cell=players[current_player].make_move()
            #players[current_player].move(player,cell,board,)
               current_player=(current_player+1)%len(players)

PRINT(

    "HI")