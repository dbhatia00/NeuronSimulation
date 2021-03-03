import xlrd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


wb = xlrd.open_workbook('data.xlsx')
sh1 = wb.sheet_by_name(u'Sheet1')

x = (sh1.col_values(1)) 
y = (sh1.col_values(0))

plt.plot(x[20000:25000],y[20000:25000])