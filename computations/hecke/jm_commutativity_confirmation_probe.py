"""Independent confirmation of what the Lean now claims -- and the control it needs.

The Lean file `HeckeTranspositionExpansion.lean` proves three things this probe
re-measures in a FAITHFUL model, because a machine-checked proof establishes that the
STATEMENT follows, not that the statement says what its docstring says it says:

  (1) L_k = 1 + A_k   at   d = q - 1/q          jmRaw_eq_one_add_addJM
  (2) [A_i, A_k] = 0  for every d               addJM_comm
  (3) [L_i, L_k] = 0                            jmRaw_comm

Method: regular representation of H_n(q) (faithful), exact fractions.Fraction, no
float64 anywhere. Every object here is a linear combination of GENERATOR WORDS -- the
JM elements, the transpositions, and their products alike -- so products are word
concatenations and nothing needs a general multiplication routine.

CONTROLS (a probe testing a claimed identity without a control measures itself):

  C1  [L_i, sigma_j] = 0 must FAIL for some (i,j) -- the JM elements are not central,
      so an all-True sweep would mean the comparison is broken rather than that the
      theorem is strong.
  C2  L_k = 1 + A_k must FAIL at d != q - 1/q. The identifying value is forced by the
      recursion; if the identity held for every d the probe would not be seeing d.

Emits no witness: this checks a proof, not a physical quantity.
"""
from fractions import Fraction as F
import os
_src = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "jm_adjacent_widen_q_and_n.py")
exec(open(_src).read().split('print("jm words')[0])


def add(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, F(0)) + v
        if r[k] == 0:
            del r[k]
    return r


def smul(c, a):
    return {k: c * v for k, v in a.items() if c * v != 0}


def jm_word(k):
    """L_k as a generator word: L_0 = 1, L_{j+1} = s_j L_j s_j."""
    w = []
    for j in range(k):
        w = [j] + w + [j]
    return w


def transp_word(l, k):
    """T_(l,k) = s_{k-1} ... s_{l+1} s_l s_{l+1} ... s_{k-1}, for l < k."""
    w = [l]
    for j in range(l + 1, k):
        w = [j] + w + [j]
    return w


def addJM(word, k, d):
    """A_k = d * sum_{l<k} T_(l,k), as an element."""
    r = {}
    for l in range(k):
        r = add(r, smul(d, word(transp_word(l, k))))
    return r


def one(word):
    return word([])


rows = []
for n in (4, 5):
    for q in (F(2), F(3), F(5, 2)):
        word = build(n, q)
        h = q - 1 / q

        # (1) L_k = 1 + A_k at d = h
        ok1 = all(word(jm_word(k)) == add(one(word), addJM(word, k, h))
                  for k in range(n))

        # (2) [A_i, A_k] = 0 for several d, including d = 1 (not the identifying value).
        # A_i A_k = d^2 * sum_{a<i} sum_{b<k} T_(a,i) T_(b,k), and each term is a word.
        def addJM_prod(i, k, d):
            r = {}
            for a in range(i):
                for b in range(k):
                    r = add(r, smul(d * d,
                                    word(transp_word(a, i) + transp_word(b, k))))
            return r

        ok2 = all(addJM_prod(i, k, d) == addJM_prod(k, i, d)
                  for d in (h, F(1), F(1, 2), F(-3))
                  for i in range(n) for k in range(n))

        # (3) [L_i, L_k] = 0
        ok3 = all(word(jm_word(i) + jm_word(k)) == word(jm_word(k) + jm_word(i))
                  for i in range(n) for k in range(n))

        # C1: L_i must NOT commute with every generator
        c1_fail = any(word(jm_word(i) + [j]) != word([j] + jm_word(i))
                      for i in range(n) for j in range(n - 1))

        # C2: the identification must fail at a wrong d
        c2_fail = any(word(jm_word(k)) != add(one(word), addJM(word, k, F(1)))
                      for k in range(2, n))

        rows.append((n, q, ok1, ok2, ok3, c1_fail, c2_fail))

print(f"{'n':>2} {'q':>5} | L=1+A  [A,A]=0  [L,L]=0 | C1 noncentral  C2 d-sensitive")
allok = True
for (n, q, ok1, ok2, ok3, c1, c2) in rows:
    print(f"{n:>2} {str(q):>5} | {str(ok1):>5}  {str(ok2):>7}  {str(ok3):>7} |"
          f" {str(c1):>13}  {str(c2):>14}")
    allok &= ok1 and ok2 and ok3 and c1 and c2

print()
print("ALL CHECKS AND CONTROLS PASS" if allok else "*** SOMETHING FAILED ***")
