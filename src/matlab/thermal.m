tic
% 1. define constants
DEPOSIT_T = 543.15;
ENVELOP_T = 343.15;
RHO = 1050.0;
C = 2080.0;
k = 0.177;
h = 75;
e = 0.95;
S_B = 5.67e-8;
DIAMETER = 0.004;
LENGTH = 0.005;
dt = 0.2;
N = 40000;

% 2. 
Ts = DEPOSIT_T * ones(N, 1);
maxTemp = 0;

QConvs = zeros(N, 1);
QRadis = zeros(N, 1);
QPres = zeros(N, 1);
QSucs = zeros(N, 1);

surfaceArea = pi * DIAMETER * LENGTH;
crossArea = pi * DIAMETER ^ 2 / 4;

for i = 1:N
    QConvs(1:i) = h * surfaceArea * (Ts(1:i) - ENVELOP_T);
    QRadis(1:i) = e * S_B * surfaceArea * (Ts(1:i).^4 - ENVELOP_T^4);
    QPres(2:i)  = crossArea * (Ts(2:i) - Ts(1:i-1)) * k / LENGTH;
    QSucs(1:i-1) = crossArea * (Ts(1:i-1) - Ts(2:i)) * k / LENGTH;
    m = RHO * crossArea * LENGTH;
    Ts(1:i) = Ts(1:i) - (QConvs(1:i) + QRadis(1:i) + QPres(1:i) + QSucs(1:i))...
        * dt / (m * C);
    if Ts(1) > maxTemp
        maxTemp = Ts(1);
    end
end

fprintf("%0.6f\n", maxTemp);
toc