# Fungsi untuk membuat papan catur
def create_chess_board(width, height):
    """
    Membuat papan catur dengan pola menggunakan list comprehension
    Args:
        width: lebar papan
        height: tinggi papan
    Returns:
        nested list berupa papan catur
    """
    return [[('#' if (i + j) % 2 == 0 else '*') for j in range(width)] for i in range(height)]

# Fungsi untuk mengubah pola papan catur
def convert_pattern(row):
    """
    Mengubah pola papan catur dengan mengganti simbol
    Args:
        row: baris papan catur
    Returns:
        list baris dengan pola baru
    """
    return ['O' if cell == '#' else 'X' for cell in row]

# Test Soal 1
board = create_chess_board(8, 8)
print("Papan Catur Original:")
for row in board:
    print(' '.join(row))

print("\nPapan Catur dengan Pola Baru:")
# Test Soal 2 menggunakan map
new_board = list(map(convert_pattern, board))
for row in new_board:
    print(' '.join(row))