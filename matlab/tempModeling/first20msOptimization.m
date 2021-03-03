[temp] = xlsread('data.xlsx');
celc = temp(:,1);
time = temp(:,2);
figure(1);
plot(time(6962:174500), celc(6962:174500));

time2 = time(19800:69900);
celc2 = celc(19800:69900);
figure(2);
plot(time2,celc2)
g=fit(time2,celc2,'exp2')

hold on
x = (198.4:699);
y = g(x);
plot(x,y);
hold off