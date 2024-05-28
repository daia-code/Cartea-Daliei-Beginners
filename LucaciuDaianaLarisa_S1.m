% Procesare Digitală a Imaginilor EE368/CS232
% Bernd Girod
% Departamentul de Inginerie Electrică, Universitatea Stanford
% Script realizat de Qiyuan Tian și David Chen

clear, clc, close all;

%% Modificare imagine doar pe jumătate sau într-o anumită regiune

% Încărcarea imaginii de test
img = imread('C:\Users\daian\Documents\MATLAB\testare1\parrot.jpg');

% Convertirea imaginii la tipul double pentru procesare
img = im2double(img);

% Determinarea dimensiunilor imaginii
[rows, cols, ~] = size(img);

% Definirea regiunii de modificat (în acest caz, jumătatea dreaptă a imaginii)
regiune_de_modificat = [cols/2 + 1, 1, cols/2, rows]; % [x, y, lățime, înălțime]

% Crearea unei măști pentru a specifica regiunea de modificat
masca = zeros(rows, cols);
masca(regiune_de_modificat(2):regiune_de_modificat(2)+regiune_de_modificat(4)-1, regiune_de_modificat(1):regiune_de_modificat(1)+regiune_de_modificat(3)-1) = 1;

% Modificarea imaginii doar în regiunea specificată
img_modificata = img;
img_modificata(repmat(masca, [1, 1, size(img, 3)]) == 1) = 0;

% Afișarea imaginilor originală și modificate
figure;
subplot(1, 2, 1);
imshow(img);
title('Imaginea Originală');
subplot(1, 2, 2);
imshow(img_modificata);
title('Imaginea Modificată');

% Salvarea imaginii modificate
imwrite(img_modificata, 'C:\Users\daian\Documents\MATLAB\testare1\parrot_modificat.jpg');

%% Construcție "sintetică" a imaginii: crearea de linii sau cercuri sau alte forme geometrice completând valorile în matricea de bază

% Crearea unei matrice de bază
matrice_de_baza = zeros(200, 200);

% Adăugarea unei linii în matricea de bază
matrice_de_baza(50:60, :) = 255; % Adăugăm o linie albă pe rândurile 50-60

% Afișarea imaginii sintetice
figure;
imshow(matrice_de_baza);
title('Imagine Sintetică (Linie)');

% Salvarea imaginii sintetice
imwrite(matrice_de_baza, 'C:\Users\daian\Documents\MATLAB\testare1\imagine_sintetica.png');

%% Adăugare formă geometrică în matricea de bază

% Adăugarea unui cerc în matricea de bază
centru = [100, 100];
raza = 40;
[X, Y] = meshgrid(1:size(matrice_de_baza, 2), 1:size(matrice_de_baza, 1));
cerc = (X - centru(1)).^2 + (Y - centru(2)).^2 <= raza^2;
matrice_de_baza(cerc) = 255; % Setăm valorile din cerc la 255 (alb)

% Afișarea imaginii sintetice cu cerc adăugat
figure;
imshow(matrice_de_baza);
title('Imagine Sintetică cu Cerc');

% Salvarea imaginii sintetice cu cerc adăugat
imwrite(matrice_de_baza, 'C:\Users\daian\Documents\MATLAB\testare1\imagine_sintetica_cerc.png');

