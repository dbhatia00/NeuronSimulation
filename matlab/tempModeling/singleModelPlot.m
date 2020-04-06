[temp] = xlsread('data.xlsx');
celc = temp(:,1);
time = temp(:,2);
figure(1);
plot(time, celc)

%STAGE 1 - time = [69.62,198.4]
time1 = time(6962:19840);
celc1 = celc(6962:19840);
f=fit(time1,celc1,'poly2')

hold on
x = (69.62:198.4) ;
y = f(x);
plot(x,y);

%STAGE 2 - time = [198.4,698.3]
time2 = time(19800:69900);
celc2 = celc(19800:69900);
g=fit(time2,celc2,'exp2')

hold on
x = (196:699) ;
y = g(x);
plot(x,y);

%STAGE 3 - time = [688.3,1745]
time2 = time(68830:174500);
celc2 = celc(68830:174500);
t=fit(time2,celc2,'exp2')

hold on
x = (688.3:1745);
y = t(x);
plot(x,y);


%scaled g(x)
hold off
figure(2)
y = g(190:700);
y = y*(3.65315*10^-5);
plot((190:700), y);
%G(182) is the starting point??

%scaled t(x)
hold off
figure(3)
y = t(688.3:1745);
y = y*(6.8101*10^-6);
plot((688.3:1745), y);
