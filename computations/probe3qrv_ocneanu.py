"""Bean qou-3qrv, part 2: is convention D forced *given* the TL condition?

Two exact tests, as rational functions of t = sqrt(q):

  TEST 1.  D  ==  y_(3)^J * chi_(3) + y_(2,1)^J * chi_(2,1)
           with the Jones-closure weights of prop:h3-markov-wenzl-weights,
             y_(3)^J = [4]_q/[2]_q^3,  y_(2,1)^J = 1/[2]_q^2,  y_(1^3)^J = 0.
           If exact, D is a genuine normalised Markov trace on H_3, namely
           the one that kills the 3-row block.

  TEST 2.  Both D and C are normalised:  sum_lambda y_lambda * dim_lambda = 1.
           If both are, then D and C are two members of the Ocneanu
           1-parameter family at different z -- i.e. the production choice
           is a choice of Ocneanu parameter, and the TL condition
           y_(1^3) = 0 is what pins it.
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
q_of_t = t**2
h_of_t = t**2 - 1/t**2
t0 = sp.sqrt(sp.Float(str(Q0), 50))

BOR = [(0, "sigma"), (1, "sigma_inv")] * 3
PARTS = [(3,), (2, 1), (1, 1, 1)]
DIMS = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}


def qint(n, q):
    return (q**n - q**(-n)) / (q - q**(-1))


chi = {}
for lam in PARTS:
    chi[lam] = sp.cancel(sp.together(
        sp.sympify(q_character_on_braid_word(lam, BOR, qs)).subs(qs, q_of_t)))

q = q_of_t
b2 = qint(2, q)
b4 = qint(4, q)
yJ = {(3,): sp.cancel(b4 / b2**3),
      (2, 1): sp.cancel(1 / b2**2),
      (1, 1, 1): sp.Integer(0)}
yW = {lam: sp.cancel(sp.together(
    sp.sympify(y_lambda_wenzl_bridge_symbolic(lam)).subs(qs, q_of_t)))
    for lam in PARTS}

D_sym = sp.cancel((4 + h_of_t**2 - 3*h_of_t**4 - h_of_t**6) / (h_of_t**2 + 4))
J_sym = sp.cancel(sp.together(sum(yJ[l] * chi[l] for l in PARTS)))
C_sym = sp.cancel(sp.together(sum(yW[l] * chi[l] for l in PARTS)))

print("TEST 1 -- D vs the Jones-closure weight vector")
diff = sp.cancel(sp.together(D_sym - J_sym))
print("  sp.cancel(D - sum_lambda y^J_lambda chi^lambda) = %s" % diff)
print("  => D IS the Markov trace with y_(1^3)=0 : %s"
      % ("YES (exact)" if sp.simplify(diff) == 0 else "NO"))
print("  numeric at q0:  D = %s" % sp.N(D_sym.subs(t, t0), 25))
print("                  J = %s" % sp.N(J_sym.subs(t, t0), 25))
print("                  C = %s" % sp.N(C_sym.subs(t, t0), 25))

print("\nTEST 2 -- normalisation  sum_lambda y_lambda * dim_lambda == 1")
for name, yv in (("Jones-closure (D)", yJ), ("Wenzl-bridge (C)", yW)):
    s = sp.cancel(sp.together(sum(yv[l] * DIMS[l] for l in PARTS)))
    print("  %-20s sum y*dim = %s   (numeric %s)"
          % (name, sp.simplify(s), sp.N(s.subs(t, t0), 20)))

print("\nWeights at q0:")
for lam in PARTS:
    print("  %-9s  y^J = %-24s  y^W = %s"
          % (str(lam), sp.N(yJ[lam].subs(t, t0), 18),
             sp.N(yW[lam].subs(t, t0), 18)))
