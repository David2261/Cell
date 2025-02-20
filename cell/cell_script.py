from typing import List


class Cell:
	def __init__(
			self,
			dna_intact: bool = True,
			resources: int = 100,
			contact_inhibition: bool = False) -> None:
		# Проверка на повреждение ДНК
		self.dna_intact: bool = dna_intact
		# Количество доступных ресурсов
		self.resources: int = resources
		# Контактное ингибирование
		self.contact_inhibition: bool = contact_inhibition
		self.alive: bool = True  # Статус клетки

	def check_division_signal(self) -> bool:
		# Проверка сигналов на деление
		if self.dna_intact and self.resources > 50 and not self.contact_inhibition:
			return True
		return False

	def check_stop_signal(self) -> bool:
		# Проверка сигналов на остановку деления
		if not self.dna_intact or self.resources < 20:
			return True
		return False

	def apoptosis(self) -> None:
		# Апоптоз (запрограммированная клеточная смерть)
		self.alive = False
		print("Клетка уничтожена из-за повреждений или нехватки ресурсов.")

	def divide(self) -> List['Cell']:
		if self.check_division_signal():
			self.resources -= 50  # Расход ресурсов на деление
			print("Клетка поделилась.")
			return [
				Cell(
					dna_intact=self.dna_intact,
					resources=self.resources // 2) for _ in range(2)]
		else:
			print("Клетка не может делиться.")
			return [self]

	def process(self) -> List['Cell']:
		if self.check_stop_signal():
			self.apoptosis()
			return []
		else:
			return self.divide()


# Симуляция работы клеток
initial_cells: List[Cell] = [Cell()]
new_cells: List[Cell] = []

for _ in range(10):  # Симулируем 10 циклов деления
	temp_cells: List[Cell] = []
	for cell in initial_cells:
		temp_cells.extend(cell.process())
	# Убираем мертвые клетки
	initial_cells = [cell for cell in temp_cells if cell.alive]
	print(f"Количество клеток: {len(initial_cells)}")
