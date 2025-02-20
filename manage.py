import sys
import subprocess
import os

# Добавляем текущую директорию в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
	if len(sys.argv) < 2:
		print("Usage: python manage.py [cell|tests]")
		sys.exit(1)

	command = sys.argv[1]

	if command == "cell":
		from cell.cell_script import Cell  # Правильный путь к файлу
		initial_cells = [Cell()]

		for _ in range(10):  # Симуляция 10 циклов деления
			temp_cells = []
			for cell in initial_cells:
				temp_cells.extend(cell.process())
			initial_cells = [cell for cell in temp_cells if cell.alive]
			print(f"Количество клеток: {len(initial_cells)}")

	elif command == "tests":
		subprocess.run(["pytest", "tests/test_cell.py"])  # Указываем путь к тестам

	else:
		print("Invalid command. Use 'cell' or 'tests'.")
		sys.exit(1)


if __name__ == "__main__":
	main()
