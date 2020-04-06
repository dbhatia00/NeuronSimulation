clear
fID = fopen('030220Patch2_temp_14_smth.txt','r');
x = 1:199999;
x = x';
sizeA = [1 inf];
formatSpec = '%f';
y = fscanf(fID, formatSpec, sizeA);
y = y';
plot(x, y);
title('Potential vs. Time')
xlabel('Time') 
ylabel('Membrane Potential mV') 
clear fID formatSpec sizeA