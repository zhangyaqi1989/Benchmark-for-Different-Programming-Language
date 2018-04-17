import java.lang.Math;

public class Thermal
{
  public static double DEPOSIT_T = 543.15;
  public static double ENVELOP_T = 343.15;
  public static double RHO = 1050.0;
  public static double C = 2080.0;
  public static double k = 0.177;
  public static double h = 75;
  public static double e = 0.95;
  public static double S_B = 5.67e-8;

  public static double DIAMETER = 0.004;
  public static double LENGTH = 0.005;
  public static double dt = 0.2;
  public static int N = 40000;

  public static void main(String[] args)
  {
    double[] Ts = new double[N];
    for(int i = 0; i < N; i++)
    {
      Ts[i] = DEPOSIT_T;
    }
    double[] tempTs = new double[N];
    double maxTemp = 0.0;
    for(int i = 0; i < N; i++)
    {
      for(int j = 0; j < i + 1; j++)
      {
        double QConv = computeConv(Ts[j], DIAMETER, LENGTH);
        double QRadi = computeRadi(Ts[j], DIAMETER, LENGTH);
        double QPre = j > 0 ? computeInter(Ts[j], Ts[j - 1], DIAMETER, LENGTH) : 0.0;
        double QSuc = j < i ? computeInter(Ts[j], Ts[j + 1], DIAMETER, LENGTH) : 0.0;
        double m = RHO * Math.PI * DIAMETER * DIAMETER / 4.0 * LENGTH;
        tempTs[j] = Ts[j] - (QConv + QRadi + QPre + QSuc) * dt / (m * C);
      }
      for(int j = 0; j < i + 1; j++)
      {
        Ts[j] = tempTs[j];
      }
      if (Ts[0] > maxTemp) maxTemp = Ts[0];
    }
    System.out.printf("%f\n", maxTemp);
  }


  public static double computeConv(double T, double D, double L)
  {
    double area = Math.PI * D * L;
    return h * area * (T - ENVELOP_T);
  }


  public static double computeRadi(double T, double D, double L)
  {
    double area = Math.PI * D * L;
    return e * S_B * area *
      (T * T * T * T - ENVELOP_T * ENVELOP_T * ENVELOP_T * ENVELOP_T);
  }

  public static double computeInter(double T1, double T2, double D, double L)
  {
    double area = Math.PI * D * D / 4;
    return k * area / L * (T1 - T2);
  }
}
