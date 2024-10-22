# -*- coding: cp1251 -*-
import sys

def print_upper_right_triangle(rows_num, filler):
    """
    �������� ������ ������ ��������� ������� �������� ������, �������������� ������-����������.

    :param rows_num: ʳ������ ����� (� ��������) ��������� �������.
    :param filler: ������, ���� ��������������� ��� ���������� ����������.
    :raises SystemExit: ���� ������-���������� �� ��������� (�� � ��������� ��������).
    """

    # �������� �� ���������� �������-�����������
    if len(filler) != 1:
        if len(filler) == 0:
            print("�� ������� ������-����������")
            sys.exit(1)
        else:
            print("�������� �������-������������")
            sys.exit(1)
    
    # ��������� ���������� ������
    lst = []
    for i in range(rows_num):
        lst.append([])  # ������ ����� ����� � ��������� ������
        for j in range(rows_num):
            if j < i:
                lst[i].append(" ")  # ������ ������ ����� ��������-������������
            else:
                lst[i].append(filler)  # ������ ������-���������� �� �����

    # ��������� ������
    for row in lst:
        print("".join(row))
