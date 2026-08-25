"""Is the D-vs-C convention split EXACTLY the Temperley-Lieb truncation?

Bean qou-3qrv. Tests, as rational functions of t = sqrt(q) (exact):

    C  = sum_{lambda |- 3} y_lambda^W * chi^lambda(beta_Bor)   (full H_3)
    TL = C  -  y_(1,1,1) * chi^(1,1,1)(beta_Bor)               (drop 3-row)
    D  = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4),  h = q - 1/q        (Lean form)

If  D - TL  cancels to 0 identically, the 195 ppm D-C gap IS exactly the
3-row Wedderburn block, and the convention question reduces to a purely
categorical one: does the mass fibre functor land in Rep(SU_q(2)) ~ TL
(no 3-row image) or in the full H_3(q)?
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401
import sympy as sp

HERE = Path(__file__).resolve().parent
for sub in ("markov", "substrate", "hecke"):
    sys.path.insert(0, str(HERE / sub))

from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic
from hecke_character_symbolic import q_character_on_braid_word
from q_parameter import Q as Q0

t = sp.symbols("t", positive=True)
qs = sp.symbols("q", positive=True)
h_of_t = t**2 - 1/t**2

BOR_CROSSINGS = [(0, "sigma"), (1, "sigma_inv")] * 3   # (s_0 s_1^-1)^3
PARTS = [(3,), (2, 1), (1, 1, 1)]

t0 = sp.sqrt(sp.Float(str(Q0), 50))

print("Wedderburn decomposition of tr_M(beta_Bor) over lambda |- 3")
print("(exact rational functions in t = sqrt(q); q0 = %s)\n" % Q0)

terms = {}
for lam in PARTS:
    y_l = y_lambda_wenzl_bridge_symbolic(lam)
    chi_l = q_character_on_braid_word(lam, BOR_CROSSINGS, qs)
    term = sp.cancel(sp.together(sp.sympify(y_l * chi_l).subs(qs, t**2)))
    terms[lam] = term
    yv = sp.N(sp.sympify(y_l).subs(qs, sp.Float(str(Q0), 50)), 20)
    cv = sp.N(sp.sympify(chi_l).subs(qs, sp.Float(str(Q0), 50)), 20)
    print("  lambda = %-9s  y = %-24s chi = %-24s y*chi = %s"
          % (str(lam), yv, cv, sp.N(term.subs(t, t0), 20)))

C_sym = sp.cancel(sp.together(sum(terms.values())))
TL_sym = sp.cancel(sp.together(terms[(3,)] + terms[(2, 1)]))
D_sym = sp.cancel((4 + h_of_t**2 - 3*h_of_t**4 - h_of_t**6) / (h_of_t**2 + 4))

print("\nValues at q0:")
print("  C  (full H_3, 3 blocks)      = %s" % sp.N(C_sym.subs(t, t0), 25))
print("  TL (drop the (1^3) block)    = %s" % sp.N(TL_sym.subs(t, t0), 25))
print("  D  (Lean closed form)        = %s" % sp.N(D_sym.subs(t, t0), 25))

print("\nEXACT identity tests (cancel to 0 <=> identical rational functions):")
d_minus_c = sp.cancel(sp.together(D_sym - C_sym))
d_minus_tl = sp.cancel(sp.together(D_sym - TL_sym))
print("  D - C   = %s" % d_minus_c)
print("  D - TL  = %s" % d_minus_tl)

print("\nNumeric at q0:")
print("  D - C            = %s" % sp.N(d_minus_c.subs(t, t0), 12))
print("  D - TL           = %s" % sp.N(d_minus_tl.subs(t, t0), 12))
print("  -y*chi at (1^3)  = %s" % sp.N(-terms[(1, 1, 1)].subs(t, t0), 12))
print("\nVERDICT: D == TL-truncation of C ?  %s"
      % ("YES (exact)" if d_minus_tl == 0 else "NO"))
