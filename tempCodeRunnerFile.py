import pygame
import sys
from const import * 
from game import Game
from move import Move 

class Main:
    def __init__(self):
      pygame.init()
      
      self.screen= pygame.display.set_mode((WIDTH,HEIGHT))
      pygame.display.set_caption('chess')

      self.game=Game()
      
    def mainloop(self):
       screen = self.screen
       game = self.game
       board= self.game.board
       dragger= self.game.dragger
       while True:
          
          game.show_bg(screen)
          game.show_pieces(screen)
          if dragger.dragging:
             dragger.update_blit(screen)


          for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
               dragger.update_mouse(event.pos)
               #print(event.pos)

               clicked_row = dragger.mouseY// SQSIZE
               clicked_col=dragger.mouseX//SQSIZE

               print(dragger.mouseY,clicked_row)
               print(dragger.mouseX,clicked_col)

               if board.squares[clicked_row][clicked_col].has_piece():
                  piece = board.squares[clicked_row][clicked_col].piece
                  board.calc_moves(piece,clicked_row,clicked_col)
                  dragger.save_initial(event.pos)
                  dragger.drag_piece(piece)

                  game.show_bg(screen)

                  game.show_moves(screen)
                  game.show_pieces(screen)

            elif event.type==pygame.MOUSEMOTION:
               if dragger.dragging :
                  dragger.update_mouse(event.pos)
                  game.show_bg(screen)
                  game.show_moves(screen)
                  game.show_pieces(screen)
                  dragger.update_blit(screen)

            elif event.type==pygame.MOUSEBUTTONUP:
              dragger.undrag_piece()

            elif event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

          pygame.display.update()

main=Main()
main.mainloop() 

