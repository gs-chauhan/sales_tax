import pytest
import problem1_sales_tax

class TestClass:
    def test_for_sales_tax1():
        assert s_tax('1 book at 12.49\n1 music CD at 14.99\n1 chocolate bar at 0.85') == '1 book: 12.49\n1 music CD: 16.49\n1 chocolate bar: 0.85\nSales Taxes: 1.5\nTotal: 29.83'

    def test_for_sales_tax2():
        assert s_tax('1 imported box of chocolates at 10.00 1 imported bottle of perfume at 47.50') == '1 imported box of chocolates: 10.5\n1 imported bottle of perfume: 54.65\nSales Taxes: 7.65\nTotal: 65.15'
        
    def test_for_sales_tax3():
        assert s_tax('1 imported bottle of perfume at 27.99 1 bottle of perfume at 18.99\n1 packet of headache pills at 9.75\n1 box of imported chocolates at 11.25') == '1 imported bottle of perfume: 32.19\n1 bottle of perfume: 20.89\n1 packet of headache pills: 9.75\n1 box of imported chocolates: 11.85\nSales Taxes: 6.7\nTotal: 74.68'