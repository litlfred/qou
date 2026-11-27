"""Volume-order rule for the lepton volume carriers (owner card 2026-11-27), no fitting.

Generation g >= 1 carries the g-th smallest hyperbolic knot volume: 4_1 (Cao-Meyerhoff), then
5_2 (Gabai-Haraway-Meyerhoff-Thurston-Yarmola). These are cited theorems, not computed here.
Volumes are computed exactly from shapes: Vol(4_1) = 2 Cl_2(pi/3), and Vol(5_2) = 3 D(z) with
z the root of z^3 - z^2 + 1 that has Im z > 0 (D the Bloch-Wigner dilogarithm).
Lean: QOU/Observations/VolumeOrderRule.lean (ratio_q_free: m_tau/m_mu = Vol2/Vol1).
Measured ratios enter only in the comparison block.
"""
import sys
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / p))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 30
checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def bloch_wigner(z):
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


VOL41 = 2 * mp.clsin(2, mp.pi / 3)
z52 = [r for r in mp.polyroots([1, -1, 0, 1]) if mp.im(r) > 0][0]
VOL52 = 3 * bloch_wigner(z52)
check("Vol(4_1) = 2.029883212819...", abs(VOL41 - mp.mpf("2.02988321281930725004240510855")) < 1e-25)
check("Vol(5_2) = 2.828122088330...", abs(VOL52 - mp.mpf("2.82812208833078316276389880928")) < 1e-25)
check("order: Vol(4_1) < Vol(5_2)", VOL41 < VOL52)

q0 = mp.mpf(Q_50_DIGIT_STR)
h = 1 - 1 / q0
ratio = VOL52 / VOL41
check("m_tau/m_mu is q-free", abs((VOL52 / h**2) / (VOL41 / h**2) - ratio) < 1e-25)
print()
print("m_mu/m_e  = Vol(4_1)/hbar^2 ", mp.nstr(VOL41 / h**2, 10))
print("m_tau/m_e = Vol(5_2)/hbar^2 ", mp.nstr(VOL52 / h**2, 10))
print("m_tau/m_mu = Vol(5_2)/Vol(4_1)", mp.nstr(ratio, 10))
print()
print("-- comparison boundary (measured values enter only here) --")
print("m_tau/m_e measured 3477.23 ; rule / measured =", mp.nstr(VOL52 / h**2 / mp.mpf("3477.23"), 6))
print("m_tau/m_mu measured 16.8170 ; rule / measured =", mp.nstr(ratio / mp.mpf("16.8170"), 6))
print()
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
