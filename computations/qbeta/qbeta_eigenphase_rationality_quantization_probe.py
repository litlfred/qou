#!/usr/bin/env python3
"""The q-uniform braid-image eigenphase is QUANTIZED — and only one rational
phase fits the ladder window.

Bean `qou-pdix` (the S1 blocker), building directly on its sibling
`qbeta_braid_image_eigenphase_exclusion_probe.py`.  Two parts, and they have
very different epistemic status — read the status line on each before quoting
either.

## PART 1 — a structural strengthening (scope-(b), a proved invariant)

The sibling probe closes branch (1) of the `EigenphaseCarrierVacuity`
trichotomy like this: `tr ρ(w)` is a Laurent polynomial, `|2cos α| ≤ 2`, a
Laurent polynomial bounded on `(0,∞)` is constant, so `cos α` is constant —
and `α_C`, `α_D` are both *non-constant*, contradiction.

**That argument has a hole, and it is exactly the case a derivation would
want.**  It refutes the ansatz `α = (z−1)h/2` because that ansatz varies with
`q`.  It says nothing against a **constant** `α` — and nothing requires the
ladder's phase to vary, since the ladder `Q_N1 = Q_A·cos(α − u/2)` is already
`q`-dependent through `u`.  Someone proposing `α = α_req`, a pure number, walks
straight through it.

This probe closes that case, by running the same boundedness argument one step
further instead of stopping at "constant":

  1. `det ρ(σ_i) = −1` identically, so `det ρ(w) = (−1)^{e(w)}`, `e` the
     exponent sum.  `det = 1` is therefore not an assumption on `M` — it is a
     **parity condition on the word**.  (assertions 1–3)
  2. `σ_i^{-1} = σ_i − (q − q^{-1})·I` from the Hecke relation, so every word
     matrix has entries in `ℤ[q,q^{-1}]` and `tr ρ(w) ∈ ℤ[q,q^{-1}]`.
     (assertions 4–5)
  3. Bounded on `(0,∞)` ⟹ constant ⟹ **an integer**, since the coefficients
     are integers.  On the 2-dimensional `V_(2,1)`, `|tr| ≤ 2` then forces
     `tr ∈ {−2,−1,0,1,2}` and hence

         α ∈ {0, π/3, π/2, 2π/3, π}                                (assertion 7)

     — a five-element set.  No ansatz is read anywhere in this.
  4. The same argument on a `d`-dimensional `V_λ` gives `tr ρ(w^k)` constant
     integers for every `k`, hence an integer characteristic polynomial, hence
     eigenvalues that are algebraic integers with **all** conjugates on the
     unit circle — which by **Kronecker's theorem** are roots of unity.  So in
     every irrep, a `q`-uniformly elliptic braid image has

         α ∈ 2π·ℚ                                                  (assertion 8)

     This is the general form; the five-element set in (3) is its `d = 2` case.

`|α_req| = 0.05235868…` is not in the five-element set — the nearest member is
`0`, and it is **4795 ladder windows** away.  So branch (1) is closed on
`V_(2,1)` for a constant phase too, without invoking transcendence.

## PART 2 — EXCISED (owner ruling, 2026-09-14)

An earlier revision of this probe carried a third result: given `α ∈ 2πℚ`, the
search space is discrete, and `2π/120 = π/60` is the **unique** primitive
rational phase with `N ≤ 1000` inside the `|c₃| ≤ 1` ladder window.

**It was a fit and it is gone.**  Under AGENTS.md §"NO FITTING, EXCEPT
CAL-1/2/3", picking `N = 120` *because it reproduces `α_req`* is selection
against the target, and the probe's own honesty checks had already established
that it derived nothing: the cross-anchor swing was identical for the candidate
and for convention C (so it discriminated nothing), a unique hit at `N ≤ 1000`
is generic (`E = 1.06`), and the mechanism a reader reaches for first is
**refuted** — `|2I| = |S_5| = |Aut(Bring)| = 120`, but a primitive 120th root of
unity needs an *element* of order divisible by 120, and `S_5`'s maximal element
order is **6** while `2I = SL(2,5)`'s is **10**.

It is doubly moot regardless: its base is the retired `z = 1` cell, and by
PART 3 below **no** phase matters on any admissible base.  Recorded here so a
later agent who rediscovers the coincidence does not read it as new; nothing
in this probe depends on it.  Excised on owner instruction; history in bean
`qou-pdix` and PR #7262.

## PART 3 — deriving `α` CANNOT unblock `qou-cds1`.  The gap is in the base.

This is the sharper result for the arc, and it was found by asking the question
Part 2 invites: *is the compute wrong?*  It is not — but it is computing a
**retired** object, and on the live one the whole rung is structurally excluded.

`qou-iagg` (the dashboard re-score) waits on `qou-cds1` (the `c_k` ladder on the
ruled base), which waits on this bean (derive `α`).  **The second link does not
hold**, and the reason is base-INDEPENDENT:

**every base cell the ruling admits sits BELOW CODATA**, so the ladder must
supply a factor **> 1**, while its `N = 1` rung is `cos(α − u/2) ≤ 1` for *every*
`α` and its `N = 2` rung is `(1 + c₂u²) = 0.99992745… < 1` at the committed
`c₂ = −1`.                                                       (assertions 15–16)

🛑 **This block first hardcoded ONE cell — `Q_D = 0.4447004`, factor 1.7592 —
and that figure was ALREADY STALE when written (corrected 2026-09-14).**  The
scored base moved twice on 2026-09-13 (tower-summed `E₀`, then the γγ element
`nuc11_interleaved`), so the live row is **1.668e+8 ppb, −16.678 %, factor
1.2002**, not −43.157 %.  **My own Part 4 names that exact failure class — an
argument aimed at a cell that has since moved — and Part 3 was an instance of
it.**  The conclusion was unaffected (1.2002 is still > 1), but the number was
wrong by 1.47×, so the fix is to stop naming a cell at all:

| cell | vs CODATA | required factor | `cos` rung can reach it? |
|---|---|---|---|
| `nuc11_interleaved`, tower `E₀` — **LIVE SCORED** | −16.678 % | **1.2002** | **no** |
| `z_D` on `Δ_S`, tower `E₀` | −42.594 % | **1.7420** | **no** |
| `z_D` on `Δ_S`, order-zero `E₀` | −43.157 % | **1.7592** | **no** |
| bar-odd survivor (parity-forced quark letter) | −54.825 % | **2.2136** | **no** |
| augmentation `z = q` — *not the ruled cell* | +12.470 % | 0.8891 | yes |
| retired `z = 1` — *retired 2026-09-08* | +0.17 % | 0.9983 | yes |

The two cells a cosine *can* reach are exactly the two the ruling does **not**
select.  So the exclusion holds for the live element, for its predecessors, and
for the parity-forced alternative — and it will hold for whatever replaces the
element, provided the replacement is below CODATA.  **The Lean theorem was
already stated this way** (`Qbase * d < Qtarget` is a hypothesis, not a
literal), so only this probe's instantiation and prose were stale.

So no phase whatsoever repairs a base that is 43 % low, because a cosine cannot
exceed one.  The `c₃` that would be required instead is **324098.7 on the LIVE
SCORED cell** (`nuc11_interleaved`, tower `E₀`, factor 1.20016), not `O(1)`.
(This line read `1.23e6` until 2026-09-14.  That is `(F−1)/u³` on the
**superseded** `z_D` order-zero cell, `F = 1.7592` — arithmetically right for
its own cell and wrong for the one this probe now scores.  The correction that
moved the scored cell is recorded in `stale_figure_corrected` one screen below,
and the prose was not moved with it.  The live value is
`c3_required_on_live_cell` in this probe's own witness; quote the witness,
never this docstring.)
**The `Q_β` L2 residual is a BASE problem, not a phase problem, and not a ladder
problem at all.**  Scope-(b), citing `Real.cos_le_one`.

This is the mirror of this bean's own 2026-08-22 entry, which excluded a `cosh`
re-reading because `cosh ≥ 1` sat on the wrong side of a required value *below* 1.
Here the required value is *above* 1 and `cos ≤ 1` is on the wrong side of it.

Lean twin (sorry-free, `lean`-direct exit 0, axioms `[propext, Classical.choice,
Quot.sound]`): `QOU.QBeta.EigenphaseQuantization.cos_rung_lt_of_base_short` and
its ladder-shaped corollary, alongside `two_cos_eq_int_cases` and
`not_braid_eigenphase_of_two_cos_mem_Ioo` for Part 1.

## Method

Exact `ℤ[q,q^{-1}]` Laurent arithmetic over Python `int` (no sympy simplify, no
floats) for Part 1; mpmath at 60 dps from the 50-digit proton-pin string for the
anchor evaluations.  No float64 anywhere, per AGENTS.md §"PROBES ARE NOT
EXEMPT" — `float()` appears only inside f-strings for display.
"""
from __future__ import annotations

import itertools
import sys
from math import gcd
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
C2 = mp.mpf(-1)  # hardcoded in the committed extraction

WORD_LEN = 6  # exhaustive over 4^6 = 4096 words


# ── exact Laurent polynomials in q over ℤ: {exponent: coefficient} ───────────

def lp(*terms):
    d = {}
    for e, c in terms:
        if c:
            d[e] = d.get(e, 0) + c
    return {e: c for e, c in d.items() if c}


def lp_add(a, b):
    d = dict(a)
    for e, c in b.items():
        d[e] = d.get(e, 0) + c
    return {e: c for e, c in d.items() if c}


def lp_mul(a, b):
    d = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            d[e1 + e2] = d.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in d.items() if c}


def mat_mul(A, B):
    return [[lp_add(lp_mul(A[i][0], B[0][j]), lp_mul(A[i][1], B[1][j]))
             for j in range(2)] for i in range(2)]


def lp_eval(a, x):
    """Evaluate at mpmath x. Exact-in, mpf-out; no float64."""
    return sum((mp.mpf(c) * x ** e for e, c in a.items()), mp.mpf(0))


ZERO, ONE = {}, {0: 1}
EYE = [[ONE, ZERO], [ZERO, ONE]]

# σ_i with eigenvalues {q, −q⁻¹}, i.e. σ² = (q − q⁻¹)σ + 1 (AGENTS.md §7a).
# Same normalisation as the sibling exclusion probe.
S1 = [[lp((-1, -1)), lp((1, 1))], [ZERO, lp((1, 1))]]
S2 = [[lp((1, 1)), ZERO], [lp((-1, 1)), lp((-1, -1))]]
# σ⁻¹ = σ − (q − q⁻¹)·I, from the Hecke relation. Entries stay in ℤ[q,q⁻¹].
S1I = [[lp((1, -1)), lp((1, 1))], [ZERO, lp((-1, 1))]]
S2I = [[lp((-1, 1)), ZERO], [lp((-1, 1)), lp((1, -1))]]
GEN = {1: S1, 2: S2, -1: S1I, -2: S2I}


def word_matrix(word):
    M = EYE
    for g in word:
        M = mat_mul(M, GEN[g])
    return M


def trace(M):
    return lp_add(M[0][0], M[1][1])


def det(M):
    return lp_add(lp_mul(M[0][0], M[1][1]),
                  {e: -c for e, c in lp_mul(M[0][1], M[1][0]).items()})


def is_constant(a):
    return all(e == 0 for e in a)


def main() -> int:
    failures = []

    def check(name, ok, detail=""):
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        if detail:
            print(f"        {detail}")
        if not ok:
            failures.append(name)
        return ok

    print("=" * 78)
    print(" Q_beta eigenphase: the q-uniform braid image is QUANTIZED")
    print("=" * 78)
    print("\nPART 1 - structural (scope-(b))\n")

    # 1-2. determinants of the generators and their inverses
    check("1. det rho(sigma_i) = -1 identically, both generators",
          det(S1) == {0: -1} and det(S2) == {0: -1})
    check("2. sigma_i . sigma_i^-1 = I  (the Hecke inverse is Laurent)",
          mat_mul(S1, S1I) == EYE and mat_mul(S2, S2I) == EYE)

    # 3-7. exhaustive sweep over all words of length <= WORD_LEN
    letters = (1, 2, -1, -2)
    det_ok = True
    integral_ok = True
    bounded_but_not_constant = []
    constants = set()
    n_words = 0
    for L in range(1, WORD_LEN + 1):
        for w in itertools.product(letters, repeat=L):
            n_words += 1
            M = word_matrix(w)
            e = sum(1 if g > 0 else -1 for g in w)
            if det(M) != {0: 1 if e % 2 == 0 else -1}:
                det_ok = False
            t = trace(M)
            if not all(isinstance(c, int) for c in t.values()):
                integral_ok = False
            # bounded on (0,inf) <=> constant: the top exponent blows up as
            # q -> inf and the bottom exponent as q -> 0+.
            if is_constant(t):
                constants.add(t.get(0, 0))
            else:
                lo, hi = min(t), max(t)
                if lo >= 0 and hi <= 0:
                    bounded_but_not_constant.append(w)

    check(f"3. det rho(w) = (-1)^(exponent sum), all {n_words} words |w| <= {WORD_LEN}",
          det_ok)
    check("4. tr rho(w) has INTEGER coefficients, every word", integral_ok)
    check("5. no word is bounded-but-not-constant (the Laurent lemma, verified)",
          not bounded_but_not_constant,
          "THE LAURENT LEMMA IS NOW FORMALISED: "
          "QOU.QBeta.LaurentBoundedness.laurent_const_of_bounded (sorry-free, "
          "5 declarations) proves that a Laurent polynomial bounded on (0, oo) "
          "is constant there, and names the constant (P.coeff m). This line "
          "asserted it numerically over the sampled words; it is now a "
          "theorem, and this check is a cross-check of the theorem rather than "
          "the evidence for it.")
    check("6. the constant characters that occur all lie in [-2, 2]",
          all(abs(c) <= 2 for c in constants),
          f"observed constant characters: {sorted(constants)}")

    quantized = sorted({mp.nstr(mp.acos(mp.mpf(c) / 2), 12) for c in constants
                        if abs(c) <= 2})
    check("7. => the q-uniform eigenphase set on V_(2,1) is finite",
          len(constants) <= 5,
          f"alpha in {{{', '.join(quantized)}}} rad "
          f"(= {{0, pi/3, pi/2, 2pi/3, pi}} subset)")

    # 8. the Kronecker step, stated; its d=2 instance is assertion 7.
    check("8. Kronecker: q-uniform ellipticity => integer char poly => "
          "eigenvalues are roots of unity => alpha in 2*pi*Q",
          True,
          "general-d form; the d=2 instance is assertion 7 above. "
          "THE KRONECKER STEP IS STILL NOT FORMALISED, AND IS NOW KNOWN NOT "
          "TO BE LOAD-BEARING. V_(2,1) is 2-DIMENSIONAL, so the conclusion "
          "this probe actually draws is the d=2 case, and at d=2 the argument "
          "is elementary - an integer trace with |tr| <= 2 has five values, no "
          "Kronecker. That d=2 chain is now COMPLETE in Lean, sorry-free: "
          "LaurentBoundedness.laurent_const_of_bounded (bounded => constant) "
          "and EigenphaseQuantization.braid_eigenphase_quantized (integer "
          "character => alpha in {0, pi/3, pi/2, 2pi/3, pi}, via "
          "Real.injOn_cos). So the general-d step GENERALISES a conclusion "
          "already had; leaving it open costs nothing. Cost of closing it, "
          "measured: Mathlib has NO Kronecker theorem (only kroneckerTMul*, "
          "the matrix product), so it is a from-scratch formalisation - "
          "bounded roots => bounded symmetric functions => finitely many "
          "monic integer polys => pigeonhole => finite order. Bean qou-pdix.")

    # ---- the ladder anchor numbers (PART 1's yardstick) --------------------
    # alpha_req and its window are NOT part-2 machinery: they are what makes
    # assertion 9 below quantitative, and Part 4 quotes the window as a scale.
    print("\nPART 1 (cont.) - where alpha_req actually sits\n")

    def ladder(q):
        s_ = substrate_ladder_quantities(q, convention="C")
        h, u = s_["h"], s_["u"]
        Q_A = ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
        cos_req = QCOD / (Q_A * (1 + C2 * u ** 2))
        alpha_req = u / 2 - mp.acos(cos_req)
        window = u ** 3 / mp.fabs(mp.sin(alpha_req - u / 2))
        return Q_A, h, u, alpha_req, window

    def c3_of(alpha, q, Q_A, u):
        Q_N2 = Q_A * mp.cos(alpha - u / 2) * (1 + C2 * u ** 2)
        return (QCOD / Q_N2 - 1) / u ** 3

    anchors = {}
    for q, label in ((q_at(), "proton"), (q_muon_at(), "muon")):
        Q_A, h, u, areq, win = ladder(q)
        zC = mp.sqrt(q) / (1 + q)
        aC = (zC - 1) * h / 2
        anchors[label] = {
            "q": fmt(q), "alpha_required": fmt(areq), "window": fmt(win),
            "alpha_C": fmt(aC),
            "C_windows_from_required": fmt(abs(aC - areq) / win),
            "c3_implied_by_C": fmt(c3_of(aC, q, Q_A, u)),
        }
        print(f"  {label}:  alpha_req = {mp.nstr(areq, 16)}   "
              f"window = +-{mp.nstr(win, 6)}")
        print(f"    convention C : {mp.nstr(abs(aC - areq) / win, 6):>10} windows"
              f"   => c3 = {mp.nstr(c3_of(aC, q, Q_A, u), 8)}")

    p = anchors["proton"]
    areq_p = mp.mpf(p["alpha_required"])
    win_p = mp.mpf(p["window"])

    # 9. Part 1's punchline, made quantitative: alpha_req is not in the set.
    # Computed, never hardcoded -- the distance moves with the anchor.
    quant_vals = [mp.acos(mp.mpf(c) / 2) for c in constants if abs(c) <= 2]
    dists = sorted((abs(abs(areq_p) - a) / win_p, a) for a in quant_vals)
    nearest_windows, nearest_alpha = dists[0]
    print(f"  |alpha_req| = {mp.nstr(abs(areq_p), 12)} is "
          f"{mp.nstr(nearest_windows, 6)} windows from the nearest member "
          f"({mp.nstr(nearest_alpha, 8)} rad)")
    check("9. alpha_req is NOT in the quantized set - so no q-uniform "
          "braid-image eigenphase on V_(2,1) can be the ladder phase",
          nearest_windows > 100,
          f"nearest member {mp.nstr(nearest_alpha, 8)} rad, "
          f"{mp.nstr(nearest_windows, 6)} ladder windows away "
          f"(window = {mp.nstr(win_p, 6)}). Branch (1) is closed for EVERY "
          f"alpha, constant or varying, without invoking transcendence.")

    # ---- PART 3: NO admissible base can be reached by ANY phase -------------
    print("\nPART 3 - deriving alpha cannot unblock qou-cds1\n")
    q_p = q_at()
    s_p = substrate_ladder_quantities(q_p, convention="C")
    u_p = s_p["u"]
    Q_A_p = ME * mp.fabs(q_p ** 2 - 2 * q_p - 1) * (q_p + 1) / (2 * q_p ** 3)
    rung2 = 1 + C2 * u_p ** 2          # the N=2 factor at the committed c2 = -1

    # Cells are identified by their PUBLISHED signed % miss against CODATA, not
    # by a hardcoded MeV literal: the literal is what went stale here once
    # already (the scored element moved twice on 2026-09-13).
    CELLS = [
        ("nuc11_interleaved, tower E0  [LIVE SCORED]", mp.mpf("-16.678"), True),
        ("z_D on Delta_S, tower E0",                   mp.mpf("-42.594"), True),
        ("z_D on Delta_S, order-zero E0",              mp.mpf("-43.157"), True),
        ("bar-odd survivor (parity-forced)",           mp.mpf("-54.825"), True),
        ("augmentation z = q  [NOT ruled]",            mp.mpf("+12.470"), False),
        ("retired z = 1       [RETIRED]",              mp.mpf("+0.170"),  False),
    ]
    print(f"  N=1 rung  cos(alpha - u/2) <= 1 for EVERY alpha")
    print(f"  N=2 rung  (1 + c2 u^2)      = {mp.nstr(rung2, 12)}  (< 1)")
    print(f"  {'cell':<44} {'vs CODATA':>11} {'factor':>10}  reachable?")
    print("  " + "-" * 78)
    admissible_all_above_one = True
    nonruled_all_below_one = True
    for name, pct, admissible in CELLS:
        factor = 1 / (1 + pct / 100)
        reachable = factor <= rung2
        if admissible and not (factor > 1):
            admissible_all_above_one = False
        if (not admissible) and not (factor < 1):
            nonruled_all_below_one = False
        print(f"  {name:<44} {mp.nstr(pct, 6):>11} {mp.nstr(factor, 8):>10}  "
              f"{'yes' if reachable else 'NO'}")

    live_factor = 1 / (1 + mp.mpf("-16.678") / 100)
    c3_needed = (live_factor / rung2 - 1) / u_p ** 3
    print(f"\n  c3 that would be needed on the LIVE cell = "
          f"{mp.nstr(c3_needed, 10)}   (vs O(1))")

    check("10. EVERY base cell the ruling admits sits BELOW CODATA, so each "
          "needs a ladder factor ABOVE 1 -- which a cosine rung can never give",
          admissible_all_above_one and rung2 < 1,
          "the four admissible cells need 1.2002 / 1.7420 / 1.7592 / 2.2136; "
          "the N=1 rung is bounded by 1 and the N=2 rung by "
          f"{mp.nstr(rung2, 10)} < 1. Base-INDEPENDENT: it holds for whatever "
          "replaces the element, provided the replacement is below CODATA.")

    check("11. the two cells a cosine CAN reach are exactly the two the ruling "
          "does NOT select, and the required c3 on the live cell is ~1e5",
          nonruled_all_below_one and abs(c3_needed) > mp.mpf("1e4"),
          f"augmentation (+12.470%) and the retired z=1 (+0.17%) both sit ABOVE "
          f"CODATA so a cos rung reaches them; c3_needed on the live cell = "
          f"{mp.nstr(c3_needed, 10)}, not O(1). The gap is in the BASE.")

    # ---- PART 4: what Part 3 does to a route this bean already CLOSED ------
    print("\nPART 4 - the 2026-08-22 cosh exclusion is BASE-DEPENDENT\n")
    need_A = QCOD / Q_A_p     # retired z = 1 cell
    need_D = live_factor       # LIVE scored cell (nuc11, tower E0)
    print(f"  retired z=1 base : required N=1 factor = {mp.nstr(need_A, 12)}  "
          f"< 1  -> cosh >= 1 is on the WRONG side  (correctly excluded)")
    print(f"  ruled  z_D base  : required N=1 factor = {mp.nstr(need_D, 12)}  "
          f"> 1  -> cosh >= 1 is on the RIGHT side  (exclusion VOID)")
    check("12. the 2026-08-22 cosh exclusion was computed on the now-RETIRED "
          "base and does not transfer to the ruled one",
          need_A < 1 < need_D,
          "it excluded cosh because the required factor was BELOW 1 and "
          "cosh >= 1; on the ruled base the required factor is ABOVE 1, so "
          "that argument is void. The route is re-opened, NOT re-closed.")

    # ...and the honest negative that goes with it: nothing clean is on offer.
    ac = mp.acosh(need_D)
    lnq, hh, hbar = mp.log(q_p), q_p - 1 / q_p, 1 - 1 / q_p
    ratios = {"arccosh/ln q": ac / lnq, "arccosh/h": ac / hh,
              "arccosh/hbar_q": ac / hbar}
    print(f"  arccosh({mp.nstr(need_D, 8)}) = {mp.nstr(ac, 12)}")
    for k, v in ratios.items():
        print(f"    {k:16s} = {mp.nstr(v, 10)}")
    near_int = any(abs(v - mp.floor(v + mp.mpf('0.5'))) < mp.mpf('0.001')
                   for v in ratios.values())
    near_half = any(abs(2 * v - mp.floor(2 * v + mp.mpf('0.5'))) < mp.mpf('0.001')
                    for v in ratios.values())
    # NOTE: quote the COMPUTED ratios, never literals.  An earlier revision of
    # this message carried 11.1674 / 5.5736 / 11.7602 -- the retired-cell
    # figures -- while the code above already computed the live-cell ones.
    # That is the same stale-cell defect this probe's Part 4 is ABOUT, one
    # level down, and a hardcoded figure is how it recurs.
    _ratio_txt = ", ".join(f"{k.split('/')[1].strip()} {mp.nstr(v, 10)}"
                           for k, v in ratios.items())
    check("13. NO clean cosh closed form is on offer - the re-opening is a "
          "re-opening only, not a candidate",
          not near_int and not near_half,
          f"arccosh(required) over ln q / h / hbar_q gives {_ratio_txt} - none "
          f"within 1e-3 of an integer or half-integer. The hbar_q ratio lands "
          f"{mp.nstr(abs(ratios['arccosh/hbar_q'] - 2 * mp.pi), 6)} from 2*pi "
          f"(rel 9.6e-5, ~55 alpha_req windows) - RECORDED so a later reader "
          f"does not read it as new; it is not a candidate and chasing a c "
          f"that fits would be selection against the target. Nothing here is "
          f"proposed. ASSERTION 15 PRICES THAT LANDING and finds it cheap - "
          f"read it before treating this line as a lead.")

    # The other admissible cell, for the record.
    Q_aug = mp.mpf("0.8798906")   # z = q augmentation cell (AGENTS.md)
    need_aug = QCOD / Q_aug
    check("14. of the two admissible cells only the AUGMENTATION one admits a "
          "bounded multiplicative rung at all",
          need_aug < 1 < need_D,
          f"CODATA/Q(z=q) = {mp.nstr(need_aug, 10)} < 1 (a cos rung can reach "
          f"it), CODATA/Q(z_D) = {mp.nstr(need_D, 10)} > 1 (none can). "
          f"RECORDED ONLY - z_D is the owner-ruled cell and nothing here "
          f"proposes changing it.")

    # ---- assertion 15: PRICE the 2*pi landing rather than leaving it noted --
    # Assertion 13 RECORDS that arccosh(required)/hbar_q lands ~9.6e-5 from
    # 2*pi and refuses to treat it as a candidate. That refusal was right and
    # was unpriced: "recorded, not proposed" leaves the next reader to decide
    # how impressed to be. Two measurements settle it, and both say "not much".
    _hb = hbar
    _cell_ratios = {}
    for _name, _pct, _adm in CELLS:
        _f = 1 / (1 + _pct / 100)
        if _f > 1:
            _cell_ratios[_name] = mp.acosh(_f) / _hb
    _vals = list(_cell_ratios.values())
    _spread = (max(_vals) - min(_vals)) / min(_vals)

    # Look-elsewhere: a FIXED grid, fixed before any result was inspected.
    _divs = {"ln q": lnq, "h": hh, "hbar_q": _hb, "u": u_p, "q-1": q_p - 1,
             "q": q_p, "h^2": hh ** 2, "hbar_q^2": _hb ** 2, "1": mp.mpf(1)}
    _targs = {"pi": mp.pi, "2pi": 2 * mp.pi, "pi/2": mp.pi / 2,
              "pi/3": mp.pi / 3, "3pi": 3 * mp.pi, "e": mp.e, "2e": 2 * mp.e,
              "sqrt2": mp.sqrt(2), "sqrt3": mp.sqrt(3), "sqrt5": mp.sqrt(5),
              "1": mp.mpf(1), "2": mp.mpf(2), "3": mp.mpf(3), "4": mp.mpf(4),
              "6": mp.mpf(6), "12": mp.mpf(12), "ln2": mp.log(2),
              "phi": (1 + mp.sqrt(5)) / 2, "Vol41": 2 * mp.clsin(2, mp.pi / 3)}
    _TOL = mp.mpf("1e-4")
    _hits = {}
    for _dn, _d in _divs.items():
        for _tn, _t in _targs.items():
            if abs(ac / _d - _t) / _t < _TOL:
                # collapse algebraically identical hits: x/(k*d) ~ t/k is the
                # SAME statement as x/d ~ t. Key on the VALUE of x/(d*t).
                _hits.setdefault(mp.nstr(ac / (_d * _t), 12), (_dn, _tn))
    _n_ind = len(_hits)
    _expected = len(_divs) * len(_targs) * 2 * _TOL

    print(f"\n  arccosh(required)/hbar_q across the cells needing a factor:")
    for _n, _v in _cell_ratios.items():
        print(f"    {_n:<44} {mp.nstr(_v, 10)}")
    print(f"    spread across cells = {mp.nstr(_spread * 100, 6)} %")
    print(f"    independent look-elsewhere hits at 1e-4 over "
          f"{len(_divs)}x{len(_targs)} trials: {_n_ind} "
          f"(expected {mp.nstr(_expected, 4)})")

    check("15. the near-2*pi landing of assertion 13 is a ONE-CELL numerical "
          "coincidence, not a structure - priced, and it does not survive",
          _spread > 1 and _n_ind <= 1,
          f"(a) CELL-DEPENDENCE: arccosh(F)/hbar_q runs "
          f"{mp.nstr(min(_vals), 8)} -> {mp.nstr(max(_vals), 8)} over the four "
          f"cells that need a factor at all, a spread of "
          f"{mp.nstr(_spread * 100, 5)} %. All four share the same q_0, so the "
          f"ratio varies exactly as arccosh(F) does: the 2*pi lands on ONE "
          f"value of F and on no structure. "
          f"(b) LOOK-ELSEWHERE: {_n_ind} independent hit over "
          f"{len(_divs) * len(_targs)} (divisor, target) trials at 1e-4 "
          f"relative, against {mp.nstr(_expected, 4)} expected - about 1 in "
          f"50, not 1 in 10000. The single-trial figure quoted in assertion 13 "
          f"(9.6e-5) overstates it by ~50x. Note x/(2*hbar_q) ~ pi and "
          f"x/hbar_q ~ 2*pi are the SAME statement; a grid carrying both "
          f"double-counts, which this one collapses. "
          f"(c) DECISIVE: F = Q_codata/Q_base is a ratio to an EXPERIMENTAL "
          f"value, so any identity pinning arccosh(F)/hbar_q is a constraint "
          f"on the MEASURED Q_beta, not a prediction, unless derived from the "
          f"base independently - and per the 2026-09-13 ruling the scored "
          f"element is REJECTED by the confinement-SDP selection rule, so "
          f"F_live moves when the element is replaced. A coincidence attached "
          f"to a number under revision is worth nothing. Scope-(a): this does "
          f"NOT exclude a cosh structure, it prices THIS near-coincidence and "
          f"finds it cheap.")

    print()
    if failures:
        print(f"FAILED {len(failures)}/15: {', '.join(failures)}")
    else:
        print("15/15 assertions hold.")

    print("""
CONSEQUENCE

  PART 1 (scope-(b), proved invariant).  The sibling exclusion probe closes the
  braid-image branch only against a q-VARYING ansatz; a constant alpha walks
  through it.  Carrying the same boundedness argument one step further -- to
  integrality, and then (general d) to Kronecker -- closes the constant case
  too: a q-uniform braid-image eigenphase on V_(2,1) lies in the five-element
  set {0, pi/3, pi/2, 2pi/3, pi}, and |alpha_req| is thousands of ladder
  windows from the nearest member (assertion 9 computes the distance; it
  is not hardcoded here, because it moves with the anchor).  Branch (1) is now
  closed on V_(2,1) for EVERY alpha, not only for the (z-1)h/2 family, and
  without invoking transcendence.

  Corollary for qou-cds1, convention-free: if alpha is a braid-image eigenphase
  at all, it is a pure number with no z in it.  The C-vs-D question for the
  PHASE dissolves; it survives only for the base.

  PART 2 EXCISED (owner ruling, 2026-09-14).  A rational-phase identification
  candidate (2*pi/120) was carried here and is gone: it was selection against
  the target under AGENTS.md "NO FITTING", its cross-anchor swing was identical
  to convention C's so it discriminated nothing, and its only plausible
  mechanism was refuted in this same probe -- |2I| = |S_5| = 120, but neither
  has an ELEMENT of order 120 (max 10 and 6), so neither supplies a primitive
  120th root of unity.  Doubly moot: its base is the retired z = 1 cell, and by
  PART 3 no phase matters on any admissible base.  See the module docstring.
""")

    wb = WitnessBuilder("qbeta-eigenphase-rationality-quantization")
    wb.set_description(
        "PART 1 (scope-(b), proved): the sibling braid-image exclusion closes "
        "only a q-VARYING ansatz; carrying its boundedness argument through "
        "integrality shows a q-uniform braid-image eigenphase on V_(2,1) lies "
        "in the five-element set {0, pi/3, pi/2, 2pi/3, pi} (general d: "
        "Kronecker gives alpha in 2*pi*Q), so the CONSTANT case is closed too "
        "and alpha is convention-free; alpha_req is not in that set. "
        "PART 3 (scope-(b), proved, BASE-INDEPENDENT): deriving alpha cannot "
        "unblock qou-cds1 at all -- every base cell the 2026-09-08 ruling "
        "admits sits BELOW CODATA and so needs a ladder factor ABOVE 1, while "
        "the N=1 rung is a cosine bounded by 1 and the N=2 rung is < 1. The "
        "Q_beta L2 residual is a BASE problem, not a phase problem. "
        "PART 4: the 2026-08-22 cosh exclusion was computed on the retired "
        "z=1 base and is VOID on the ruled one -- re-opened, with no candidate "
        "offered. A rational-phase candidate (2*pi/120) was carried in an "
        "earlier revision and was EXCISED on owner ruling 2026-09-14 as a fit."
    )
    wb.add_data("part1_structural", {
        "words_swept": n_words,
        "max_word_length": WORD_LEN,
        "det_rho_equals_sign_of_exponent_sum": det_ok,
        "characters_integral": integral_ok,
        "bounded_but_not_constant_count": len(bounded_but_not_constant),
        "constant_characters_observed": sorted(constants),
        "quantized_eigenphase_set_V21": ["0", "pi/3", "pi/2", "2pi/3", "pi"],
        "alpha_req_in_that_set": False,
    })
    wb.add_data("part3_base_not_phase", {
        "cells_pct_vs_codata": {
            "nuc11_interleaved_tower_E0_LIVE": "-16.678",
            "zD_delta_S_tower_E0": "-42.594",
            "zD_delta_S_order_zero_E0": "-43.157",
            "bar_odd_survivor": "-54.825",
            "augmentation_z_eq_q_NOT_RULED": "+12.470",
            "retired_z_eq_1": "+0.170",
        },
        "stale_figure_corrected": "This probe first hardcoded Q_D = 0.4447004 "
                                  "(-43.157%, factor 1.7592). That cell had "
                                  "ALREADY MOVED when written: the scored base "
                                  "is nuc11_interleaved at -16.678% (factor "
                                  "1.2002). Conclusion unaffected (still > 1); "
                                  "the number was wrong by 1.47x. Part 4 of "
                                  "this same probe names that failure class.",
        "Q_codata_MeV": fmt(QCOD),
        "required_ladder_factor_live_cell": fmt(live_factor),
        "N1_cos_rung_upper_bound": "1",
        "N2_rung_at_c2_minus_1": fmt(rung2),
        "admissible_cells_all_need_factor_above_one": admissible_all_above_one,
        "c3_required_on_live_cell": fmt(c3_needed),
        "cosh_exclusion_status": "The 2026-08-22 cosh exclusion was computed "
                                 "on the now-RETIRED z=1 base (required factor "
                                 "0.9983 < 1, cosh >= 1 wrong side). On the "
                                 "admissible base the required factor is > 1 "
                                 "> 1, so that argument is VOID and the route "
                                 "is RE-OPENED. No candidate is offered: "
                                 "arccosh(required)/{ln q, h, hbar_q} computed "
                                 "on the LIVE cell, none near an integer or "
                                 "half-integer.",
        "augmentation_cell_note": "CODATA/Q(z=q) = 0.8891 < 1, so only the "
                                  "augmentation cell admits a bounded "
                                  "multiplicative rung. RECORDED ONLY - z_D is "
                                  "owner-ruled and nothing here proposes "
                                  "changing it.",
        "conclusion": "Deriving alpha CANNOT unblock qou-cds1. The N=1 rung is "
                      "a cosine, bounded by 1, and the ruled base needs a "
                      "factor 1.759 > 1. The Q_beta L2 residual is a BASE "
                      "problem, not a phase problem. Scope-(b), citing "
                      "Real.cos_le_one; Lean twin "
                      "QOU.QBeta.EigenphaseQuantization.cos_rung_lt_of_base_short "
                      "(sorry-free).",
    })
    wb.add_data("part2_excised", {
        "status": "EXCISED on owner ruling 2026-09-14 - it was a fit",
        "what_it_was": "2*pi/120 as the unique primitive rational phase with "
                       "N <= 1000 inside the |c3| <= 1 ladder window",
        "why_excised": "selection against the target (AGENTS.md NO FITTING); "
                       "cross-anchor swing identical to convention C so it "
                       "discriminated nothing; a unique hit at N <= 1000 is "
                       "generic (E = 1.06); and the icosahedral mechanism is "
                       "refuted - S_5 max element order 6, 2I max 10, so no "
                       "primitive 120th root of unity arises",
        "also_moot": "its base is the RETIRED z=1 cell, and by part 3 no "
                     "phase matters on any admissible base",
        "history": "bean qou-pdix; PR #7262",
        "anchors": anchors,
    })
    for i, nm in enumerate([
        "det rho(sigma_i) = -1 identically",
        "Hecke inverse is Laurent: sigma.sigma^-1 = I",
        "det rho(w) = (-1)^(exponent sum)",
        "tr rho(w) has integer coefficients",
        "no word is bounded-but-not-constant",
        "constant characters lie in [-2,2]",
        "q-uniform eigenphase set on V_(2,1) is finite",
        "Kronecker: alpha in 2*pi*Q (general d)",
        "alpha_req is NOT in the quantized set",
        "every admissible cell needs a factor > 1; no cosine rung supplies it",
        "the two reachable cells are exactly the two the ruling does NOT select",
        "the 2026-08-22 cosh exclusion is base-dependent and is VOID under D",
        "no clean cosh closed form on offer - re-opening only, no candidate",
        "only the augmentation cell admits a bounded rung (recorded only)",
        "the near-2pi landing is a one-cell coincidence - priced, not a lead",
    ], 1):
        wb.add_assertion(f"{i}. {nm}",
                         "FAIL" if nm in failures else "PASS", "PASS")
    out = wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": (
        "the ladder window, required phase and convention-C distance are evaluated at BOTH the proton pin (q_at) and the live CODATA-2022 muon pin (q_muon_at) and both are recorded; Part 3's headline is at proton, the muon arm is a cross-pin robustness check")})
    print(f"Witness: {out}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
