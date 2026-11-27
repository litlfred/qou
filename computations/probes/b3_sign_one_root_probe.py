#!/usr/bin/env python3
"""The three-way wrong sign on b_3 has ONE root -- and uniform attraction does not escape it.

Bean `qou-q8vl`; parents `qou-brng`, `qou-rwhv`, `qou-ix0x`.
Lean: `QOU/MassTheory/B3SignOneRoot.lean` (13 declarations, sorry-free).

WHAT THIS MEASURES
------------------
Three constructions give the connected three-body channel the wrong sign against
AME2020 -- the count channel (#7193), the Ursell/Mayer cumulant (#7198), the
dominant summand (#7200). This probe establishes that they are ONE failure, and
corrects the escape hatch that the Ursell audit and AGENTS.md currently state.

    A. The three production interface letters are all `sigma + d*1` with d <= 0,
       so every bond factor mu = z + d is confined to (0, 1).
    B. The production A=3 word is a CHAIN, so phi3 collapses to a PRODUCT of two
       Mayer variables -- and a product does not change sign when BOTH factors
       flip. Uniform attraction therefore leaves b_3 < 0.
    C. What the chain needs is SIGN-MIXED bonds: exactly one bond above 1. Both
       A=3 chains impose the SAME pattern (pn opposite to both like-pairs), and
       that pattern is the observed two-nucleon spectrum -- deuteron bound,
       diproton and dineutron unbound.
    D. Neither derived bond family can supply it. The projector family is
       excluded by an IDENTITY (mu+ + mu- = 1), not an inequality.

WHAT IT DOES NOT CLAIM
----------------------
*   NOT that a bond above 1 is the only escape. `b3Agg_nonneg_of_convexOn`
    (bean `qou-82mc`) gives b_3 >= 0 from a convex aggregator with every bond
    still inside (0,1). This probe is about the MULTIPLICATIVE assembly only.
*   NOT that mu(sigma^m) alternates by parity. CHECK 7 below REFUTES that
    reading -- it is a prediction this probe's author made from two data points
    and the corpus's own stacked-bond table contradicts it.
*   NOT a proposal to adopt sigma^2. Choosing a letter because it yields the
    AME sign is selection against the target (AGENTS.md "NO FITTING").

PRECISION. mpmath `mpf` end to end at 60 dps; sympy exact rational functions for
every algebraic identity. `float()` appears nowhere outside an f-string. No
witness is written and nothing is wired.

-- Ref: [manuscript] .beans/qou-q8vl; docs/audits/2026-09-12-ursell-partition-function-for-b3.md
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "tools/pyhecke/python", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import sympy as sp  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from pyhecke.constants import (  # noqa: E402
    PN_CONVENTION,
    flavor_split_leading,
    pn_interface_offset,
)

mp.dps = 60

FAILURES: list[str] = []
PASSES = 0


def check(ok: bool, name: str, detail: str = "") -> None:
    global PASSES
    if ok:
        PASSES += 1
        print(f"[PASS] {name}")
    else:
        FAILURES.append(name)
        print(f"[FAIL] {name}")
    if detail:
        for line in detail.strip().splitlines():
            print(f"        {line}")


# --------------------------------------------------------------------------
# Substrate, convention D, proton pin.
# --------------------------------------------------------------------------
Q = Q_MP
H = Q - 1 / Q                      # Hecke h = q - 1/q
Z_D = Q**3 / (Q**2 + 1)            # convention D Markov parameter

# The three production interface letters, from the live source of truth.
#   pp: (1, 0)     -- bare sigma
#   nn: (1, -h)    -- sigma^-1 via the Hecke relation
#   pn: (1, d_pn)  -- colour-weighted (owner ruling R3)
D_PP = mpf(0)
D_NN = -H
D_PN = pn_interface_offset(Q)

MU = {"pp": Z_D + D_PP, "pn": Z_D + D_PN, "nn": Z_D + D_NN}
G = {k: v - 1 for k, v in MU.items()}          # Mayer variable g = mu - 1

# The production A=3 chains (atom_braid_word_3A lays A-1 interfaces in a LINE).
CHAINS = {"3H": ("pn", "nn"), "3He": ("pp", "pn")}

# AME2020 targets under the corpus's uniform-e2 convention, b3 = B(A=3) - 3*B(2H).
AME_B3 = {"3H": mpf("1.8081"), "3He": mpf("1.0443")}


def phi3_chain(ga, gb):
    """Third Ursell function on a 2-bond chain: ONE connected spanning graph."""
    return ga * gb


def b3_chain(ga, gb):
    return -phi3_chain(ga, gb)


print("=" * 78)
print(f" q0 = {mp.nstr(Q, 25)}   z_D = {mp.nstr(Z_D, 25)}   h = {mp.nstr(H, 25)}")
print(f" p-n convention: {PN_CONVENTION}")
print("=" * 78)

# --------------------------------------------------------------------------
# CHECK 1 -- the production letters, and their confinement to (0,1).
# --------------------------------------------------------------------------
rows = []
for k in ("pp", "pn", "nn"):
    rows.append(f"{k}: d = {mp.nstr(MU[k] - Z_D, 20):>24s}  mu = {mp.nstr(MU[k], 20):>24s}"
                f"  g = {mp.nstr(G[k], 20):>24s}")
check(
    all(mpf(0) < MU[k] < mpf(1) for k in MU) and all(G[k] < 0 for k in G),
    "CHECK 1: every production bond factor lies in (0,1), so every Mayer g < 0",
    "\n".join(rows) + "\n"
    "d <= 0 for all three (sigma at one end, sigma^-1 at the other), so mu <= z_D < 1.\n"
    "Confinement itself is QBeta.SingleCrossingAlwaysBinds.interface_mem_Ioo; measured here.",
)

# nn must be exactly sigma^-1: mu = 1/(q(q^2+1)).
mu_nn_closed = 1 / (Q * (Q**2 + 1))
check(
    abs(MU["nn"] - mu_nn_closed) < mpf(10) ** (-50),
    "CHECK 2: the nn letter IS sigma^-1 -- mu_nn = 1/(q(q^2+1)) to 50 dps",
    f"live {mp.nstr(MU['nn'], 30)}\nclosed {mp.nstr(mu_nn_closed, 30)}\n"
    f"|dev| = {mp.nstr(abs(MU['nn'] - mu_nn_closed), 5)}",
)

# --------------------------------------------------------------------------
# CHECK 3 -- the chain sign, at the live bonds. The three-way wrong sign.
# --------------------------------------------------------------------------
rows = []
ok = True
for atom, (a, b) in CHAINS.items():
    val = b3_chain(G[a], G[b])
    ok &= val < 0
    rows.append(f"{atom:4s} bonds ({a},{b}): phi3 = {mp.nstr(phi3_chain(G[a], G[b]), 12)}"
                f"   b3 = {mp.nstr(val, 12)}   AME wants +{mp.nstr(AME_B3[atom], 6)}")
check(ok, "CHECK 3: at the LIVE bonds both A=3 chains give b3 < 0, AME wants > 0",
      "\n".join(rows))

# --------------------------------------------------------------------------
# CHECK 4 -- THE CORRECTION. Uniform attraction does not escape.
# --------------------------------------------------------------------------
# Flip every bond to attractive (mu > 1) by reflecting g -> -g, magnitudes kept.
rows, ok = [], True
for atom, (a, b) in CHAINS.items():
    ga, gb = -G[a], -G[b]                      # both now > 0, i.e. mu > 1
    val = b3_chain(ga, gb)
    ok &= val < 0
    rows.append(f"{atom:4s} ALL bonds attractive (mu>1): g = ({mp.nstr(ga,10)}, {mp.nstr(gb,10)})"
                f"  ->  b3 = {mp.nstr(val, 12)}  (STILL NEGATIVE)")
check(
    ok,
    "CHECK 4: uniform attraction leaves b3 < 0 -- the escape hatch as written is NOT sufficient",
    "\n".join(rows) + "\n"
    "phi3(chain) = g01*g12 is a PRODUCT, so its sign is invariant under flipping BOTH bonds.\n"
    "The Ursell audit s4 and AGENTS.md say a positive term 'needs a bond factor above 1'.\n"
    "True but NOT sufficient: on a 2-bond chain EXACTLY ONE bond must exceed 1.",
)

# --------------------------------------------------------------------------
# CHECK 5 -- the sharp condition, and that both chains impose the SAME pattern.
# --------------------------------------------------------------------------
# Enumerate the four sign assignments of (g_pn, g_like) and see which give b3>0 on BOTH.
def both_chains_positive(sign_pn: int, sign_like: int) -> bool:
    gg = {"pn": mpf(sign_pn) * abs(G["pn"]),
          "pp": mpf(sign_like) * abs(G["pp"]),
          "nn": mpf(sign_like) * abs(G["nn"])}
    return all(b3_chain(gg[a], gg[b]) > 0 for a, b in CHAINS.values())


grid = {(sp_, sl): both_chains_positive(sp_, sl) for sp_ in (+1, -1) for sl in (+1, -1)}
winners = [k for k, v in grid.items() if v]
check(
    len(winners) == 2 and all(k[0] != k[1] for k in winners),
    "CHECK 5: b3 > 0 on BOTH chains iff g_pn is opposite in sign to both like-pair bonds",
    "\n".join(f"  (sign g_pn, sign g_like) = {k}  ->  both chains positive: {v}"
              for k, v in grid.items())
    + "\nOnly the two SIGN-MIXED assignments work. Uniform sign fails both ways.",
)

# The physical reading: B = -alpha*log(mu) > 0 exactly when mu < 1.
check(
    both_chains_positive(-1, +1),
    "CHECK 6: the working assignment is 'pn binds, like-pairs do not' -- the observed spectrum",
    "g_pn < 0 (mu_pn < 1, pn BOUND: the deuteron) and g_pp, g_nn > 0 (mu > 1, UNBOUND)\n"
    "is exactly the two-nucleon fact: deuteron bound, diproton and dineutron unbound.\n"
    "So b3 > 0 and the correct two-body boundness pattern are ONE condition, not two.\n"
    "The LIVE model instead has all three g < 0 -- it binds the diproton and the\n"
    "dineutron -- and that same defect is what forces b3 < 0.",
)

# --------------------------------------------------------------------------
# CHECK 7 -- REFUTING THIS PROBE AUTHOR'S OWN PREDICTED PATTERN.
# --------------------------------------------------------------------------
# sigma^m = a_m*sigma + b_m; bond factor mu_m = a_m*z + b_m. From the eigenvalues
# q and -1/q of sigma. Computed EXACTLY in sympy, then evaluated at q0.
qs = sp.Symbol("q", positive=True)
zs = qs**3 / (qs**2 + 1)
a_s, b_s = sp.symbols("a_s b_s")
mu_sym = {}
for m in list(range(1, 9)) + [-1, -2]:
    sol = sp.solve([sp.Eq(a_s * qs + b_s, qs**m),
                    sp.Eq(a_s * (-1 / qs) + b_s, (-1 / qs) ** m)], [a_s, b_s], dict=True)[0]
    mu_sym[m] = sp.simplify(sol[a_s] * zs + sol[b_s])

q_exact = sp.Rational(Fraction(Q_50_DIGIT_STR))
mu_num = {m: mpf(str(sp.N(mu_sym[m].subs(qs, q_exact), 60))) for m in mu_sym}
above = sorted(m for m in mu_num if mu_num[m] > 1)
odd_above = [m for m in above if m % 2 != 0]
rows = [f"  m = {m:+d}: mu = {mp.nstr(mu_num[m], 15):>22s}"
        f"  {'ATTRACTIVE (>1)' if mu_num[m] > 1 else ''}" for m in sorted(mu_num)]
check(
    len(odd_above) > 0,
    "CHECK 7: 'even attracts, odd repels' is REFUTED -- odd powers above 1 exist",
    "\n".join(rows) + "\n"
    f"mu > 1 at m = {above}; ODD among them: {odd_above}.\n"
    "This probe's author derived mu(sigma^2) > 1 > mu(sigma^3) symbolically and was one\n"
    "step from asserting a parity law. It is false. Recorded so it is not re-derived.",
)

# sigma^2 closed form, which IS correct and is already in the corpus.
sig2_closed = sp.simplify(mu_sym[2] - (qs**4 + 1) / (qs**2 + 1))
check(
    sig2_closed == 0,
    "CHECK 8: mu(sigma^2) = (q^4+1)/(q^2+1) exactly, and exceeds 1 for every q > 1",
    f"symbolic residual = {sig2_closed}\n"
    f"mu(sigma^2) - 1 = {sp.factor(sp.simplify(mu_sym[2] - 1))}  (positive for q > 1)\n"
    f"at q0: {mp.nstr(mu_num[2], 20)}\n"
    "Already held as QBeta.InterfaceScalar.stacked_crossing_gt_one; measured here to tie\n"
    "the closed form to the corpus value. NOT proposed as a letter -- see the docstring.",
)

# --------------------------------------------------------------------------
# CHECK 9 -- the projector family is excluded by an IDENTITY.
# --------------------------------------------------------------------------
mu_plus = (Z_D + 1 / Q) / (Q + 1 / Q)      # T = 1, isospin symmetric
mu_minus = (Q - Z_D) / (Q + 1 / Q)         # T = 0, antisymmetric
sym_sum = sp.simplify((zs + 1 / qs) / (qs + 1 / qs) + (qs - zs) / (qs + 1 / qs) - 1)
check(
    sym_sum == 0 and abs(mu_plus + mu_minus - 1) < mpf(10) ** (-55)
    and mpf(0) < mu_minus < mu_plus < mpf(1),
    "CHECK 9: mu+ + mu- = 1 IDENTICALLY, so no isospin channel can be attractive",
    f"symbolic residual of (mu+ + mu- - 1) = {sym_sum}  (identically zero, any z and q)\n"
    f"mu+ (T=1) = {mp.nstr(mu_plus, 20)}    mu- (T=0) = {mp.nstr(mu_minus, 20)}\n"
    f"sum - 1 = {mp.nstr(mu_plus + mu_minus - 1, 5)}\n"
    "An attractive channel mu+ > 1 forces mu- < 0, where -alpha*log(mu-) is not real.\n"
    "This is a partition of unity, not an inequality some other q could reverse.",
)

# --------------------------------------------------------------------------
# CHECK 10 -- the chain is covered by NEITHER standing theorem.
# --------------------------------------------------------------------------
# b3corpus_neg needs all three f in (0,1); the chain's absent bond is exactly 1.
# wMult_b3_nonpos is the EQUAL-bond statement; the chain bonds differ.
equal_bonds = all(abs(G[a] - G[b]) > mpf(10) ** (-6) for a, b in CHAINS.values())
check(
    equal_bonds,
    "CHECK 10: the two chain bonds are genuinely DIFFERENT, so wMult_b3_nonpos does not cover it",
    "\n".join(f"  {atom}: |g_{a} - g_{b}| = {mp.nstr(abs(G[a] - G[b]), 12)}"
              for atom, (a, b) in CHAINS.items())
    + "\nb3corpus_neg needs all three bonds strictly inside (0,1); a chain's absent bond\n"
      "sits at exactly f = 1, which that hypothesis excludes. Neither theorem applies.",
)

# --------------------------------------------------------------------------
print()
print("=" * 78)
print(f" {PASSES}/{PASSES + len(FAILURES)} checks pass")
if FAILURES:
    for f in FAILURES:
        print(f"   FAILED: {f}")
print("=" * 78)
sys.exit(1 if FAILURES else 0)
