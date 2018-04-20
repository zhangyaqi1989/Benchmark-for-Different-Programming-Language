##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# simple thermal simulation
##################################

module Thermal

const DEPOSIT_T = 543.15
const ENVELOP_T = 343.15
const RHO = 1050.0
const C = 2080.0
const k = 0.177
const h = 75
const e = 0.95
const S_B = 5.67e-8
const DIAMETER = 0.004
const LENGTH = 0.005
const dt = 0.2
const N = 40000
const PI = 3.1415926

function computeConv(T::Float64, D::Float64, L::Float64)
area = PI * D * L
return h * area * (T - ENVELOP_T)
end

function computeRadi(T::Float64, D::Float64, L::Float64)
area = PI * D * L
return e * S_B * area * (T * T * T * T - ENVELOP_T * ENVELOP_T * ENVELOP_T * ENVELOP_T);
end


function computeInter(T1::Float64, T2::Float64, D::Float64, L::Float64)
area = PI * D * D / 4.0
return k * area / L * (T1 - T2)
end


function main(N::Int64)
Ts = DEPOSIT_T * ones(N);
tempTs = zeros(N);
maxTemp = 0.0
for i = 1:N
  for j = 1:i
    Q_conv = computeConv(Ts[j], DIAMETER, LENGTH)
    Q_radi = computeRadi(Ts[j], DIAMETER, LENGTH)
    if j > 1
      Q_pre = computeInter(Ts[j], Ts[j - 1], DIAMETER, LENGTH)
    else
      Q_pre = 0.0
    end
    if j < i
      Q_suc = computeInter(Ts[j], Ts[j + 1], DIAMETER, LENGTH)
    else
      Q_suc = 0.0
    end
    m = RHO * PI * DIAMETER * DIAMETER / 4.0 * LENGTH
    tempTs[j] = Ts[j] - (Q_conv + Q_radi + Q_pre + Q_suc) * dt / (m * C)
  end
  for j = 1:i
    Ts[j] = tempTs[j]
  end
  if Ts[1] > maxTemp
    maxTemp = Ts[1]
  end
end
@printf("%0.6f\n", maxTemp)
# println(maxTemp)
end

# @time main(N)
main(N)

end
