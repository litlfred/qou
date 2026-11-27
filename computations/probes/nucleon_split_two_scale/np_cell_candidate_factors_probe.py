"""Can a q-NS or combinatorial factor supply the n - p flavour cell's ~4x, or its sign?

Bean qou-mbfv. Pre-stated structure (nothing here is tuned):
  * the cell is E * log(tau_p/tau_n), with tau_p/tau_n = q^2 forced on every tower level
    (NucleonSplitFullTower.markov_forces_K, strandWeight_flip, spectator_ratio);
  * a factor g common to tau_p and tau_n cancels from the ratio (spectator_ratio);
  * the sign theorem of #9767: log chart E_0 = m_e*L_X/L_e and mass chart
    E_1 = m_e*w_X/w_e agree in sign iff L_X*w_X < 0 (L_e < 0 < w_e).
    A candidate factor g can enter in only three places:
      (i)   on tau_p and tau_n jointly: it cancels from the ratio (spectator_ratio);
      (ii)  on the scale E: both charts scale by g > 0, so no sign changes, size x g;
      (iii) on the ratio itself, tau_p/tau_n -> g*q^2: this changes the exponent, which
            markov_forces_K forbids for one block. Even then the mass-chart weight of the
            cell becomes 2 + q*d(log g)/dq, so the sign flips only if q*d(log g)/dq < -2.
Candidates (from the q-NS and combinatorics threads), each with its exponent q*d(log g)/dq:
  f^(2,1) = 2 (block multiplicity)        constant        exponent 0
  Molien Plancherel sum (ruled Phi_k)      = 1 exactly     exponent 0
  writhe ratio e/(N(N-1)), #9747           in [0, 1]       exponent 0  (e = 0 for A = 1 chain)
  Haar budget factor q^2, #9752            q0^2            exponent +2
mpmath 50 dps, proton pin.
"""
import sys
from pathlib import Path
from mpmath import mp, mpf, log

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 50
q = mpf(Q_50_DIGIT_STR)
b = log(q)
tau_e = q**3 * (q**4 + 1) / (q**2 + 1)**2
L_e = log(tau_e)
w_e = 3 + 4 * q**2 * (q**2 - 1) / ((q**4 + 1) * (q**2 + 1))
L_X, w_X = 2 * b, mpf(2)
cell_log = L_X / L_e * -1          # in m_e, orientation of #9718 (|c| > 0): +2 ln q |c|
cell_mass = -w_X / w_e            # CAL-1 orientation, #9767
assert L_e < 0 < w_e

cands = [("f^(2,1) multiplicity", mpf(2), mpf(0)),
         ("Molien Plancherel sum", mpf(1), mpf(0)),
         ("writhe ratio, chain A=1", mpf(0), mpf(0)),
         ("writhe ratio, full twist", mpf(1), mpf(0)),
         ("Haar budget q^2", q**2, mpf(2))]
print("model cells / m_e: log chart", mp.nstr(cell_log, 12), " mass chart", mp.nstr(cell_mass, 12))
print("mass-chart sign flip needs q d(log g)/dq <", mp.nstr(-w_X, 6))
for name, g, gam in cands:
    w_new = w_X + gam
    flips = w_new < 0
    print(f"{name:26s} g = {mp.nstr(g, 8):>10s}  (i) cancels  (ii) size x{mp.nstr(g, 4)}, sign kept"
          f"  (iii) exponent {mp.nstr(gam, 3)}, flips sign: {flips}")
    assert not flips
print()
print("-- comparison boundary (data enter only here) --")
me = mpf("0.51099895069")
target = mpf("1.29333205") / me
print("measured / log-chart cell", mp.nstr(target / cell_log, 8))
print("measured / |mass-chart cell|", mp.nstr(target / -cell_mass, 8))
print("largest candidate on the scale E (q-NS q0^2):", mp.nstr(q**2, 8))
