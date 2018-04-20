##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# Thermal analysis
##################################


main <- function()
{
  DEPOSIT_T = 543.15
  ENVELOP_T = 343.15
  RHO = 1050.0
  C = 2080.0
  k = 0.177
  h = 75
  e = 0.95
  S_B = 5.67e-8

  DIAMETER = 0.004
  LENGTH = 0.005
  dt = 0.2
  N = 40000

  Ts = rep(DEPOSIT_T, N);
  Q_convs = rep(0, N);
  Q_radis = rep(0, N);
  Q_pres = rep(0, N);
  Q_sucs = rep(0, N);
  free_area = pi * DIAMETER * LENGTH
  cross_area = pi * DIAMETER * DIAMETER / 4.0
  max_temp = 0.0
  for (i in 1:N)
  {
    Q_convs[1:i] = (Ts[1:i] - ENVELOP_T) * free_area * h;
    Q_radis[1:i] = (Ts[1:i] ^ 4 - ENVELOP_T ^ 4) * e * S_B * free_area
    if (i > 1)
    {
      Q_pres[2:i] = (Ts[2:i] - Ts[1:i-1]) * k * cross_area / LENGTH
      Q_sucs[1:i-1] = (Ts[1:i-1] - Ts[2:i]) * k * cross_area / LENGTH
    }
    m = RHO * pi * DIAMETER * DIAMETER / 4.0 * LENGTH
    Ts[1:i] = Ts[1:i] - (Q_convs[1:i] + Q_radis[1:i] + Q_pres[1:i] + Q_sucs[1:i]) * dt / (m * C)
    if (Ts[1] > max_temp)
      max_temp = Ts[1]
  }
  sprintf("max temp = %f", max_temp)

}


system.time(main())
