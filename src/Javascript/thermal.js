console.log("Hello World");


const DEPOSIT_T = 543.15;
const ENVELOP_T = 343.15;
const RHO = 1050.0;
const C = 2080.0;
const k = 0.177;
const h = 75
const e = 0.95;
const S_B = 5.67e-8;

const DIAMETER = 0.004;
const LENGTH = 0.005;
const dt = 0.2;
const N = 40000;

function computeConv(T, D, L)
{
	var area = Math.PI * D * L;
	return h * area * (T - ENVELOP_T);
}

function computeRadi(T, D, L)
{
	var area = Math.PI * D * L;
	return e * S_B * area * (Math.pow(T, 4) - Math.pow(ENVELOP_T, 4));
}


function computeInter(T1, T2, D, L)
{
	var area = Math.PI * D * D / 4.0;
	return k * area / L * (T1 - T2)
}


function thermal()
{
	console.log("Thermal analysis starts: ");
	maxTemp = 0;
	var Ts = new Array(N);
	for (var i = 0; i < N; i++)
	{
		Ts[i] = DEPOSIT_T;
	}
	var tempTs = new Array(N);
	for(var i = 0; i < N; i++)
	{
		for(var j = 0; j < i + 1; j++)
		{
			var Q_conv = computeConv(Ts[j], DIAMETER, LENGTH);
			var Q_radi = computeRadi(Ts[j], DIAMETER, LENGTH);
			var Q_pre = j > 0 ? computeInter(Ts[j], Ts[j - 1], DIAMETER, LENGTH) : 0.0;
			var Q_suc = j < i ? computeInter(Ts[j], Ts[j + 1], DIAMETER, LENGTH) : 0.0;
			var m = RHO * Math.PI * DIAMETER * DIAMETER / 4.0 * LENGTH;
			tempTs[j] = Ts[j] - (Q_conv + Q_radi + Q_pre + Q_suc) * dt / (m * C);
		}
		for(var j = 0; j < i + 1; j++)
		{
			Ts[j] = tempTs[j];
		}
		if(Ts[0] > maxTemp) maxTemp = Ts[0];
	}
	console.log(maxTemp);
	console.log("Thermal analysis ends.");
}


var t0 = performance.now()
thermal()
var t1 = performance.now()
console.log((t1 - t0) / 1000.0 + " s")

