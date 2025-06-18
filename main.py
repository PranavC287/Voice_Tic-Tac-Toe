# main.py

import pygame
import sys
import random
from board import create_board, make_move, check_winner, is_full, PLAYER, AI, EMPTY
from ai import get_best_move
from voice import get_move_from_voice

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 900
CELL_SIZE = 540 // 3  # Match actual grid cell size (180)
GRID_TOP = (HEIGHT - WIDTH) // 2 + 30
X_OFFSET = 130  # Manual adjustment for grid alignment (left padding)
Y_OFFSET = 155  # Manual adjustment for grid alignment (top padding)

# Colors
BG_COLOR = (8, 12, 20)
X_COLOR = (255, 60, 200)
O_COLOR = (0, 255, 255)
GLOW_COLOR_X = (255, 160, 255)
GLOW_COLOR_O = (100, 255, 255)

# Font
TITLE_FONT = pygame.font.Font("assets/Orbitron-VariableFont_wght.ttf", 50)
SUB_FONT = pygame.font.Font("assets/Orbitron-VariableFont_wght.ttf", 26)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Load and scale glow background image
background_grid = pygame.image.load("assets/background_grid.png").convert_alpha()
background_grid = pygame.transform.smoothscale(background_grid, (WIDTH, WIDTH))

# Game state
board = create_board()
current_player = PLAYER
ai_thinking = False
ai_start_time = 0
winner = None

# Draw grid
def draw_grid():
    screen.blit(background_grid, (0, GRID_TOP))

# Draw X
def draw_x(center):
    x, y = center
    offset = CELL_SIZE // 6.5
    pygame.draw.line(screen, GLOW_COLOR_X, (x - offset - 3, y - offset - 3), (x + offset + 3, y + offset + 3), 10)
    pygame.draw.line(screen, GLOW_COLOR_X, (x + offset + 3, y - offset - 3), (x - offset - 3, y + offset + 3), 10)
    pygame.draw.line(screen, X_COLOR, (x - offset, y - offset), (x + offset, y + offset), 4)
    pygame.draw.line(screen, X_COLOR, (x + offset, y - offset), (x - offset, y + offset), 4)

# Draw O
def draw_o(center):
    x, y = center
    radius = CELL_SIZE // 6.5
    pygame.draw.circle(screen, GLOW_COLOR_O, (x, y), radius + 6, 10)
    pygame.draw.circle(screen, O_COLOR, (x, y), radius, 4)

# Draw moves
def draw_moves():
    for row in range(3):
        for col in range(3):
            extra_y = 0
            if row == 0:
                extra_y = 40  # Extra offset for top row alignment
            elif row == 1:
                extra_y = 25  # Extra offset for middle row alignment
            center = (
                col * CELL_SIZE + CELL_SIZE // 2 + X_OFFSET,
                row * CELL_SIZE + CELL_SIZE // 2 + GRID_TOP + Y_OFFSET + extra_y
            )
            if board[row][col] == PLAYER:
                draw_x(center)
            elif board[row][col] == AI:
                draw_o(center)

# Draw status and instruction text
def draw_status_text():
    if winner:
        message = f"{winner} WINS!" if winner in [PLAYER, AI] else "DRAW!"
    else:
        message = "PLAYER TURN" if current_player == PLAYER else "AI THINKING..."
    label = TITLE_FONT.render(message, True, (0, 255, 255))
    screen.blit(label, (WIDTH // 2 - label.get_width() // 2, 50))
    instructions = SUB_FONT.render("🎤 Press V to speak your move (e.g. 'top left')", True, (0, 255, 255))
    screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, 120))
    instructions2 = SUB_FONT.render("🤖 This AI is unbeatable. Good luck!", True, (0, 255, 255))
    screen.blit(instructions2, (WIDTH // 2 - instructions2.get_width() // 2, 155))

# Game loop
running = True
while running:
    screen.fill(BG_COLOR)
    draw_grid()
    draw_moves()
    draw_status_text()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and current_player == PLAYER and not winner:
            if event.key == pygame.K_v:
                move = get_move_from_voice()
                if move:
                    row, col = move
                    if make_move(board, row, col, PLAYER):
                        winner = check_winner(board)
                        if winner or is_full(board):
                            if not winner:
                                winner = "DRAW"
                        else:
                            current_player = AI
    if current_player == AI and running and not winner:
        if not ai_thinking:
            ai_thinking = True
            ai_start_time = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - ai_start_time >= 500:
            row, col = get_best_move(board)
            make_move(board, row, col, AI)
            winner = check_winner(board)
            if winner or is_full(board):
                if not winner:
                    winner = "DRAW"
            else:
                current_player = PLAYER
            ai_thinking = False

pygame.quit()
sys.exit()
