! written by Yaqi Zhang (zhang623@wisc.edu)
! University of Wisconsin-Madison
! March 2018

program thermal
  real, parameter :: DEPOSIT_T = 543.15
  real, parameter :: ENVELOP_T = 343.15
  real, parameter :: PI = 3.1415926
  real, parameter :: RHO = 1050.0
  real, parameter :: C = 2080.0
  real, parameter :: k = 0.177
  real, parameter :: h = 75.0
  real, parameter :: e = 0.95
  real, parameter :: S_B = 5.67e-8
  real, parameter :: DIAMETER = 0.004
  real, parameter :: LENGTH = 0.005
  real, parameter :: dt = 0.2
  integer, parameter :: N = 40000
  real, dimension(1:N) ::  Ts, temp_Ts
  real :: maxTemp = 0.0
  integer :: i, j
  real :: Q_conv, Q_radi, Q_pre, Q_suc, m

  do i = 1, N
    Ts(i) = DEPOSIT_T
  end do

  do i = 1, N
    do j = 1, i
      Q_conv = computeConv(Ts(j), DIAMETER, LENGTH)
      Q_radi = computeRadi(Ts(j), DIAMETER, LENGTH)
      if (j > 1) then
        Q_pre = computeInter(Ts(j), Ts(j - 1), DIAMETER, LENGTH)
      else
        Q_pre = 0.0
      end if
      if (j < i) then
        Q_suc = computeInter(Ts(j), Ts(j + 1), DIAMETER, LENGTH)
      else
        Q_suc = 0.0
      end if
      m = RHO * PI * DIAMETER * DIAMETER / 4.0 * LENGTH
      temp_Ts(j) = Ts(j) - (Q_conv + Q_radi + Q_pre + Q_suc) * dt / (m * C)
    end do

    do j = 1, i
      Ts(j) = temp_Ts(j)
    end do
    if (Ts(1) > maxTemp) then 
      maxTemp = Ts(1)
    end if
    ! print *, Ts(1)
  end do

  ! print *, "maxTemp = ", maxTemp
  print *, maxTemp

contains
  function computeConv(T, D, L)
    real :: T, D, L, area, computeConv
    area = PI * D * L
    computeConv = h * area * (T - ENVELOP_T)
  end function computeConv

  function computeRadi(T, D, L)
    real :: T, D, L, area, computeRadi
    area = PI * D * L
    computeRadi = e * S_B * area * (T ** 4 - ENVELOP_T ** 4)
  end function computeRadi

  function computeInter(T1, T2, D, L)
    real :: T1, T2, D, L, area, computeInter
    area = PI * D * D / 4.0
    computeInter = k * area / L * (T1 - T2)
  end function computeInter

end program thermal

