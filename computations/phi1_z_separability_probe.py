"""Is Phi_1's z-dependence separable from its combinatorial minimisation?

Bean qou-1jw9. Kills or confirms the queued `xzrj` lead: main's qou-xzrj arc
factorised mu's convention-dependence into named block invariants, leaving a
z-free residue. I recorded the lead with the objection that it cannot transfer
because "Phi_1 is a minimum over arrangements and min() is what a factorisation
does not close".

Reading the producer, that objection is WRONG about the mechanism. In
wedderburn_mass_table_convention_d.py::V the transfer recursion builds (a, b)
from the crossing content ALONE, and z enters exactly once, at the end:

    V(chain) = z * a + b

So V is AFFINE in z with z-FREE coefficients, and

    Phi_1(seq) = sum_i log |z * a_i + b_i|.

The min is therefore over a finite set of z-free (a_i, b_i) multisets. Whether
it obstructs a closed form reduces to ONE empirical question:

    does the argmin arrangement MOVE when z moves?

If it does not, the minimisation is a z-independent combinatorial selection and
Phi_1 has a closed form in z given the selected multiset -- the lead survives.
If it does, the selection genuinely couples to the convention and the lead dies.

NO FLOAT64 anywhere: mpmath end to end, per AGENTS.md.
"""
import sys
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

from qou_substrate.constants import q_at  # noqa: E402

Q = q_at(50)
H = Q - 1 / Q
Z_C = mp.sqrt(Q) / (Q + 1)          # excised, used ONLY as a second z probe point
Z_D = Q ** 3 / (Q ** 2 + 1)         # canonical

TBL = {("p", "p"): (1, mp.mpf(0)), ("n", "n"): (1, -H), ("p", "n"): (1, -H / 2),
       ("e", "e"): (1, mp.mpf(0)), ("p", "e"): (1, -H), ("n", "e"): (0, mp.mpf(1))}


def cr(x, y):
    return TBL[(x, y)] if (x, y) in TBL else TBL[(y, x)]


def ab(chain):
    """The z-FREE coefficients (a, b) of the affine form V = z*a + b."""
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        c = mp.mpf(c)
        a, b = a * (c * H + d) + b * c, a * c + b * d
    return a, b


def phi1_at(seq, z):
    t = mp.mpf(0)
    for i in range(len(seq)):
        ch = [cr(seq[i], seq[j]) for j in range(i + 1, len(seq))]
        if ch:
            a, b = ab(ch)
            t += mp.log(abs(z * a + b))
    return t


def nuc_to_seq(nuc):
    s = []
    for c in nuc:
        s.extend(["e", "p"]) if c == "p" else s.append("n")
    return s


def arrangements(Z, N):
    return sorted(set(permutations("p" * Z + "n" * N)))


print("=" * 74)
print("Phi_1 z-separability probe (bean qou-1jw9)")
print("=" * 74)
print(f"  q0   = {mp.nstr(Q, 20)}   (proton pin)")
print(f"  z_D  = {mp.nstr(Z_D, 20)}   canonical")
print(f"  z_C  = {mp.nstr(Z_C, 20)}   excised; second probe point only")

# --- TEST 1: is V exactly affine in z? second difference must vanish ---------
print("\nTEST 1 -- V affine in z (second difference over 3 z points)")
seq = nuc_to_seq(list("pnn"))
ch = [cr(seq[0], seq[j]) for j in range(1, len(seq))]
a, b = ab(ch)
zs = [mp.mpf(1) / 4, mp.mpf(1) / 3, mp.mpf(1) / 2]
vs = [z * a + b for z in zs]
# affine <=> divided second difference is 0
d2 = ((vs[2] - vs[1]) / (zs[2] - zs[1])) - ((vs[1] - vs[0]) / (zs[1] - zs[0]))
print(f"    a = {mp.nstr(a, 20)}   (z-free)")
print(f"    b = {mp.nstr(b, 20)}   (z-free)")
print(f"    second difference = {mp.nstr(d2, 5)}   -> affine: {abs(d2) < mp.mpf(10) ** -45}")

# --- TEST 2: does the argmin arrangement move with z? -----------------------
print("\nTEST 2 -- does the argmin arrangement MOVE between z_D and z_C?")
print(f"    {'atom':>5} {'Z':>3} {'N':>3} {'#arr':>7}  {'argmin same?':>13}   "
      f"{'Phi_1(z_D)':>14} {'Phi_1(z_C)':>14}")
CASES = [("He", 2, 2), ("Li", 3, 4), ("Be", 4, 5), ("B", 5, 6), ("C", 6, 6)]
moved = 0
for name, Z, N in CASES:
    arrs = arrangements(Z, N)
    best_d = min(arrs, key=lambda A: phi1_at(nuc_to_seq(A), Z_D))
    best_c = min(arrs, key=lambda A: phi1_at(nuc_to_seq(A), Z_C))
    same = phi1_at(nuc_to_seq(best_d), Z_D) == phi1_at(nuc_to_seq(best_c), Z_D)
    if not same:
        moved += 1
    print(f"    {name:>5} {Z:>3} {N:>3} {len(arrs):>7}  {str(same):>13}   "
          f"{mp.nstr(phi1_at(nuc_to_seq(best_d), Z_D), 12):>14} "
          f"{mp.nstr(phi1_at(nuc_to_seq(best_c), Z_C), 12):>14}")

print(f"\n    argmin MOVED on {moved} of {len(CASES)} atoms")
print()
print("=" * 74)
if moved == 0:
    print("VERDICT: the minimisation is z-INDEPENDENT on this sample.")
    print("  Phi_1 = sum_i log|z*a_i + b_i| over a FIXED, z-free (a_i,b_i) multiset.")
    print("  So min() is NOT the obstacle I recorded. The lead SURVIVES this test:")
    print("  whether it closes now turns on whether the a_i, b_i are themselves")
    print("  named block invariants -- the actual xzrj question.")
else:
    print("VERDICT: the argmin MOVES with z, so the combinatorial selection is")
    print("  convention-coupled and no fixed multiset exists. The lead DIES, though")
    print("  for a different reason than I recorded (coupling, not the min itself).")
print("=" * 74)
print("\nSCOPE (a): five light atoms, exhaustive over arrangements, two z points.")
print("Not a claim about all Z, nor about all z.")
