/*
 * written by Yaqi Zhang (zhang623@wisc.edu)
 * University of Wisconsin-Madison
 * March 2018
 */
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

const double DEPOSIT_T = 543.15;
const double ENVELOP_T = 343.15;
const double RHO = 1050.0;
const double C = 2080.0;
const double k = 0.177;
const double h = 75;
const double e = 0.95;
const double S_B = 5.67e-8;
const double DIAMETER = 0.004;
const double LENGTH = 0.005;
const double dt = 0.2;
const int N = 40000;

double computeConv(double T, double D, double L);
double computeRadi(double T, double D, double L);
double computeInter(double T1, double T2, double D, double L);


int main()
{
  double * Ts = new double[N];
  for(int i = 0; i < N; i++)
  {
    Ts[i] = DEPOSIT_T;
  }
  double * tempTs = new double[N];
  double maxTemp = 0.0;
  for(int i = 0; i < N; i++)
  {
    for(int j = 0; j < i + 1; j++)
    {
      double Q_conv = computeConv(Ts[j], DIAMETER, LENGTH);
      double Q_radi = computeRadi(Ts[j], DIAMETER, LENGTH);
      double Q_pre = j > 0 ? computeInter(Ts[j], Ts[j - 1], DIAMETER, LENGTH) : 0.0;
      double Q_suc = j < i ? computeInter(Ts[j], Ts[j + 1], DIAMETER, LENGTH) : 0.0;
      double m = RHO * M_PI * DIAMETER * DIAMETER / 4.0 * LENGTH;
      tempTs[j] = Ts[j] - (Q_conv + Q_radi + Q_pre + Q_suc) * dt / (m * C);
    }
    for(int j = 0; j < i + 1; j++)
    {
      Ts[j] = tempTs[j];
    }
    if (Ts[0] > maxTemp) maxTemp = Ts[0];
  }
  delete[] Ts;
  delete[] tempTs;
  printf("%f\n", maxTemp);
  return 0;
}


double computeConv(double T, double D, double L)
{
  double area = M_PI * D * L;
  return h * area * (T - ENVELOP_T);
}


double computeRadi(double T, double D, double L)
{
  double area = M_PI * D * L;
  return e * S_B * area *
    (T * T * T * T - ENVELOP_T * ENVELOP_T * ENVELOP_T * ENVELOP_T);
}

double computeInter(double T1, double T2, double D, double L)
{
  double area = M_PI * D * D / 4;
  return k * area / L * (T1 - T2);
}

