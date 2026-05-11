clc;
clear all;
close all;

fc = 100;
fm = 10;
t = 0:0.001:1;

carrier = sin(2*pi*fc*t);
message = sin(2*pi*fm*t);

am = (1 + message).*carrier;

plot(t, am);
title('AM Modulation');
