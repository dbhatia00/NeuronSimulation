clear
fID = fopen('030220Patch2_temp_14_smth.txt','r');
sizeA = [1 inf];
formatSpec = '%f';
y = fscanf(fID, formatSpec, sizeA);
y = y';
plot(1:199999, y);