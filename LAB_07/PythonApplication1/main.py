# -*- coding: cp1251 -*-

import matrix_module

# �������� � ����������� ����� ������� �� ������-����������
rows_num = int(input("������ ����� ��������� �������: "))
filler = input("������ ������-����������: ")

# ��������� ������� ��� ��������� ��������� ������� ����������
matrix_module.print_upper_right_triangle(rows_num, filler)
