"""Independent confirmation of `prod L_i = Delta^2` at general n.

`HeckeFullTwistProduct.lean` proves `jmProd H (n+1) = delta H n ^ (n+1)` from the braid
relations alone. The corpus had only n = 2 and n = 3, each by an explicit word
manipulation. This re-measures the general statement in a FAITHFUL model, and -- more
to the point -- checks that the Lean file's `delta`, `run` and `jmProd` DEFINITIONS name
the objects their docstrings say they name. A machine-checked proof cannot establish
that.

Method: regular representation of H_n(q) (faithful), exact fractions.Fraction, no
float64. Every object is a generator word, so products are concatenations.

CHECKED, for n = 3..6 and q in {2, 3, 5/2}:

  L_0 L_1 ... L_{n-1}  =  (sigma_0 sigma_1 ... sigma_{n-2})^n
  L_k                  =  run(0,k) * delta(k)          jmRaw_eq_run_mul_delta
  (delta m)^m          =  (delta (m-1))^m * run(0,m)   delta_twist_step

  Note the exponent on the LEFT is m, not m+1, even though the delta index went up. That
  asymmetry is the whole content of the step -- it is what lets the induction absorb one
  more JM element per level -- and getting it wrong here is what this probe caught on its
  first run.

CONTROLS:

  C1  the SAME product against the WRONG exponent (delta n)^(n+1) at the n-th place must
      FAIL -- the exponent is not free, and a comparison that accepted any exponent would
      be measuring nothing.
  C2  the twist is not the identity -- an all-True sweep against a trivial right-hand
      side would prove only that the harness collapses everything.

Emits no witness: this checks a proof, not a physical quantity.
"""
from fractions import Fraction as F
import os
_src = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "jm_adjacent_widen_q_and_n.py")
exec(open(_src).read().split('print("jm words')[0])


def delta_word(k):
    """delta k = sigma_0 sigma_1 ... sigma_{k-1}."""
    return list(range(k))


def run_word(b, k):
    """run b k = sigma_{b+k-1} ... sigma_b."""
    return list(range(b + k - 1, b - 1, -1))


def jm_word(k):
    """L_k by its own recursion: L_0 = 1, L_{j+1} = s_j L_j s_j."""
    w = []
    for j in range(k):
        w = [j] + w + [j]
    return w


def jmprod_word(n):
    """L_0 L_1 ... L_{n-1}."""
    w = []
    for k in range(n):
        w = w + jm_word(k)
    return w


rows = []
for n in (3, 4, 5, 6):
    for q in (F(2), F(3), F(5, 2)):
        word = build(n, q)
        # prod L_i = (delta (n-1))^n
        twist = delta_word(n - 1) * n
        ok_twist = word(jmprod_word(n)) == word(twist)
        # L_k = run(0,k) * delta(k)
        ok_factor = all(word(jm_word(k)) == word(run_word(0, k) + delta_word(k))
                        for k in range(n))
        # (delta m)^(m+1) = (delta (m-1))^m * run(0,m), for every m the algebra can hold
        ok_step = all(word(delta_word(m) * m)
                      == word(delta_word(m - 1) * m + run_word(0, m))
                      for m in range(1, n))
        # C1: the exponent is not free
        c1_fail = word(jmprod_word(n)) != word(delta_word(n - 1) * (n + 1))
        # C2: the twist is not the identity
        c2_nontrivial = word(twist) != word([])
        rows.append((n, q, ok_twist, ok_factor, ok_step, c1_fail, c2_nontrivial))

print(f"{'n':>2} {'q':>5} | prodL=D^2  L=run*delta  step | C1 exp-tight  C2 nontrivial")
allok = True
for (n, q, a, b, c, c1, c2) in rows:
    print(f"{n:>2} {str(q):>5} | {str(a):>9}  {str(b):>11}  {str(c):>4} |"
          f" {str(c1):>12}  {str(c2):>13}")
    allok &= a and b and c and c1 and c2

print()
print("ALL CHECKS AND CONTROLS PASS" if allok else "*** SOMETHING FAILED ***")
