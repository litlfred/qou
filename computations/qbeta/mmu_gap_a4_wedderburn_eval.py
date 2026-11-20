import sympy as sp
import mpmath as mp

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This held the RETIRED
# self-certified pin A as a literal -- retired 2026-08-22 for the CODATA-2022
# derivation, so the value was stale AND could not follow the anchor.
#
# MIGRATED TO PROTON on the owner ruling of 2026-08-30: proton is the default,
# and the burden is on the exception. Neither exception applies here -- this
# probe makes no explicit proton-vs-muon comparison (E1), and it is not about
# the CAL-1/2/3 triple as mathematics (E2). "It has always been muon" is
# expressly not a reason. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR`
# resolves to the proton pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

def main():
    mp.mp.dps = 60
    
    q_val = Q_MP
    
    # Let's compute the (2,1) representation matrices of sigma_1, sigma_2
    q = sp.Symbol('q')
    
    # Standard Iwahori-Hecke algebra H_3(q) matrices for lambda=(2,1)
    # Using the standard Hoefsmit / Wenzl representation
    # sigma_1 = [[q, 0], [1, -1]]
    # sigma_2 = [[-1, q], [0, q]]
    
    s1 = sp.Matrix([[q, 0], [1, -1]])
    s2 = sp.Matrix([[-1, q], [0, q]])
    s1_inv = sp.simplify(s1.inv())
    s2_inv = sp.simplify(s2.inv())
    
    # 4_1 knot braid word: (s1 * s2_inv)^2
    braid = s1 * s2_inv
    braid_sq = sp.simplify(braid * braid)
    
    chi_21 = sp.trace(braid_sq)
    print(f"chi_21(q) = {chi_21}")
    
    # Wenzl weights:
    # y_(3) = [4]_q / [2]_q^3
    # y_(2,1) = 1 / [2]_q^2
    # y_(1,1,1) = 0
    # where [k]_q = (q^k - 1) / (q - 1) (Wait, standard quantum integer is (q^k - q^-k)/(q - q^-1) or (1-q^k)/(1-q)?)
    # Let's use hbar_q definition [2]_q = 1 + q
    
    # Evaluate chi_21 at q_0
    chi_21_val = chi_21.subs(q, sp.Float(str(q_val), 60))
    print(f"chi_21(q_0) = {chi_21_val}")
    
    # We want to see if chi_21 or something similar provides a factor of (1 + 210e-9)
    # The discrepancy is 209.75 ppb.
    # What is the deviation of chi_21 from something?
    # chi_21 is a polynomial in q.
    
    chi_21_eval = float(chi_21_val)
    print(f"Numeric chi_21: {chi_21_eval}")
    
    # What if the mass correction is exactly chi_21 / 2 ?
    # 2 is the classical dimension of (2,1)
    print(f"chi_21 / 2: {chi_21_eval / 2}")
    
    # What is the exact 209.75 ppb factor?
    target_factor = 1.0 - 209.75e-9
    print(f"Target factor: {target_factor}")

if __name__ == "__main__":
    main()
