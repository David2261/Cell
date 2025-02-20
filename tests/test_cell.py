import pytest
from cell.cell_script import Cell


def test_cell_division():
	cell = Cell()
	new_cells = cell.divide()
	assert len(new_cells) == 2
	assert all(isinstance(c, Cell) for c in new_cells)

def test_cell_apoptosis():
	cell = Cell(dna_intact=False)
	cell.process()
	assert not cell.alive

def test_cell_no_division_low_resources():
	cell = Cell(resources=10)
	new_cells = cell.process()
	assert len(new_cells) == 0
	assert all(not cell.alive for cell in new_cells)

def test_cell_no_division_contact_inhibition():
	cell = Cell(contact_inhibition=True)
	new_cells = cell.process()
	assert len(new_cells) == 1
	assert new_cells[0].alive == True
