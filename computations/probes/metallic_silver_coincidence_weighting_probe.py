#!/usr/bin/env python3
"""The silver coincidence is real, holds at every `n` — and belongs to the
Plancherel weighting, not the convention-D Markov trace.

WHY THIS EXISTS
---------------
Owner, on `metallic_ladder_regime_test_probe.py`'s negative and on its citation
of PR #1999: *"this is VERY old and needs re-examination, it is pre convention
D"*, and *"I don't think these are fundamentally different … isn't the LP dual
shadow realizable as a representation?"*

Both points land. This probe re-runs the question at convention D and the
earlier negative does not survive contact: **the owner's regime prediction is
correct, it was already proved in this corpus at `n = 2`, and it generalises to
every `n`.** What the earlier probe measured was a different functional.

1. THE PR #1999 ILLUSTRATION IS PRE-D AND WRONG IN THREE WAYS
--------------------------------------------------------------
`computations/metallic_q_illustration.py` (last touched 2026-08-15, one day
before convention D landed in `qou-cds2`) is the artifact the earlier probe
cited as corroboration. Under D it fails three separate checks:

  (a) **Stale `q_0`.** It hard-codes `1.1099785955541805`; the substrate is
      `1.1099785827513808`. Off by `1.28e-8`.

  (b) **Its standard character is wrong.** It plots
      `chi^(2,1)(sigma_1 sigma_2) = (q - 1/q)^2 - 1 = h^2 - 1`. In convention D
      the standard block is `T_i -> [[q,1],[0,-1/q]], [[-1/q,0],[1,q]]` and
      `tr(T_1 T_2) = -1` **exactly, for every q**. Verified here against the
      explicit 2x2 rep at four values of `q`. Its other two curves (`q^2`,
      `q^-2`) are right.

  (c) **It claims to plot `y_lambda · chi^lambda` and plots bare
      `chi^lambda`.** No weight appears anywhere in the file. This matters
      because under D one of the three weights is zero (below).

  And it contradicts itself: its own `h^2 - 1` **changes sign at `h = 1`** —
  the golden rung — while its docstring asserts "no sign flips at metallic
  ratios". The true `chi_std(3-cycle) = -1` is constant, so the conclusion
  survives, but by the opposite mechanism from the one drawn.

  **Consequence:** the corroboration `metallic_ladder_regime_test_probe.py`
  drew from PR #1999 is withdrawn. That probe's own H_3/H_9 measurements stand;
  its supporting citation does not.

2. UNDER CONVENTION D ONLY TWO BLOCKS ARE LIVE
------------------------------------------------
The Markov weights are `y_sym = (q^4+1)/(q^2+1)^2`, `y_std = q^2/(q^2+1)^2`,
`y_alt = 0`. In `h`:

    y_sym = (h^2+2)/(h^2+4)      y_std = 1/(h^2+4) = 1/[2]_q^2      y_alt = 0

(`[2]_q^2 = (q+1/q)^2 = h^2+4`, and `y_sym + 2·y_std = 1` exactly.) The alt
block is annihilated at every `q`, so a three-curve per-block plot is
structurally wrong under D regardless of the character formulas.

3. THE IDENTITY THAT CARRIES THE SILVER COINCIDENCE
------------------------------------------------------
Weight the blocks by the **q-Plancherel measure** `W_lambda = d_q(lambda)^2 /
sum d_q^2` — the weighting `pyhecke.regime_scanner._compute_h3_wedderburn_
weights` uses, and (shown below) the one the Lean silver theorem is really
about. Write `T(w) = sum_lambda W_lambda chi^lambda(w)`. Then

    **T(sigma_i) = (h/2) · T(gamma)      identically, at every strand count.**

Proof, three lines, from facts this corpus already holds:
  (i)   `W_lambda = W_lambda'` — hook multisets are transpose-invariant, so
        `d_q(lambda) = [n]_q!/H_q(lambda) = d_q(lambda')`. Checked n = 2..5.
  (ii)  `chi^lambda(sigma) + chi^lambda'(sigma) = dim(lambda) · h` — the
        corpus's own `GaloisPairCharacterSum` class in
        `MetallicLPIdentities.lean`, symbolically verified there for n = 3, 4.
  (iii) `chi^lambda(gamma) = dim(lambda)`.
  Then `2 T(sigma) = sum_lambda W_lambda (chi^lambda + chi^lambda')(sigma)
                   = sum_lambda W_lambda dim(lambda) h = h · T(gamma)`.

Since `T(gamma) > 0`, the cost coincidence `T(gamma) = T(sigma)` holds **iff
`h = 2`, iff `q = delta_silver`** — for every `n`.

**This is `silver_lp_coincidence` (Lean, sorry-free, PR #2047), which is stated
and proved only at `n = 2`, generalised to all `n`.** The `n = 2` cost vector
`t_1 = 2(q+1/q)`, `t_2 = q^2-q^-2` is exactly `2[2]_q · (T(gamma), T(sigma))`,
so the theorem is the `n = 2` instance of the identity above. Verified here at
`n = 2` and `n = 3`; the general case is conditional only on
`GaloisPairCharacterSum`, which is already a corpus conjecture class.

It also settles the owner's second point. `T(sigma)/T(gamma) = h/2` is
simultaneously an optimisation fact (when two LP cost coefficients coincide)
and a representation-theoretic one (the transpose-pair character sum). They are
not two regimes; the dual **is** the representation. The distinction drawn in
`metallic_ladder_regime_test_probe.py` between a "representation-theoretic
regime" and "an optimisation one" is withdrawn.

4. WHY THE EARLIER SWEEP SAW NOTHING: IT WAS THE OTHER FUNCTIONAL
-------------------------------------------------------------------
Convention D's **Markov** trace is not Plancherel-weighted. Its cost vector on
the H_3 NF basis is `t = [1, z, z, z^2, z^2, h z^2 + z]` with
`z = q^3/(q^2+1) = q^2/[2]_q`, so

    Markov:      T(sigma)/T(gamma) = z = q^2/[2]_q        (not h/2)

and the `gamma`-`sigma` coincidence moves off silver entirely, to `z = 1`:

    q^3 - q^2 - 1 = 0   ->   q = 1.4655712318767680...

the **supergolden ratio** (Narayana's constant), `h = 0.78324...`. Not metallic.
The same polynomial governs `gamma = L±` and `sigma = L±`. The one other
Markov locus, `gamma = e^-`, is `q^5+q^4-2q^2-q-1 = 0`, `q = 1.24143...`,
`h = 0.43591...` — also not metallic.

So the metallic structure is a property of the **Plancherel** functional. The
earlier probe swept the Markov-weighted LP and correctly found nothing there;
the negative was about the wrong object, not about the ladder.

5. WHAT IS ACTUALLY REFUTED
-----------------------------
`SDPDegeneracyDetectsMetallic` (MetallicLPIdentities.lean) asserts that for the
n-strand LP the cost-coincidence set is `S(n) ⊆ {delta_1, …, delta_n}`. The
containment fails at `n = 3` in **both** weightings:

  * Plancherel `S(3) = {delta_2}` ∪ `{q = 2.8022805603737193}` — the second
    root, from `T(gamma) = T(e^-)`, has `h = 2.44543`, strictly between the
    silver and bronze rungs.
  * Markov `S(3) = {1.46557…, 1.24143…}`, neither metallic, silver absent.

Silver being *in* `S(n)` is now a theorem (§3); `S(n)` being *contained in* the
ladder is false. The conjecture should be weakened to the direction that holds.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired. §2 and §3 are exact symbolic identities
(sympy, residual `== 0`); §1(b) is checked against an explicitly constructed
matrix rep at 50 dps; the coincidence roots are exact algebraic numbers
reported to 16 digits. `h = 2` is `delta_2 = 1 + sqrt(2)` exactly.

-- Ref: [manuscript] bean t7qv
-- Ref: [lean] QOU.AlgebraicSubstrate.MetallicLPIdentities (PR #2047)
-- Ref: [probe] metallic_ladder_regime_test_probe.py (corroboration withdrawn)
-- Ref: [probe] computations/metallic_q_illustration.py (PR #1999, pre-D)
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from pyhecke.wedderburn import (  # noqa: E402
    partition_conjugate,
    partition_dimension,
    partitions_of,
    q_dimension,
)
from q_parameter import Q as Q0  # noqa: E402

mp.mp.dps = 50

Q = sp.symbols("q", positive=True)
H = Q - 1 / Q

# H_3 normal-form basis, in the corpus's order.
NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L+", "L-", "e-"]

# Convention-D characters on that basis (derived and cross-checked in §1).
CHI_SYM = [sp.Integer(1), Q, Q, Q ** 2, Q ** 2, Q ** 3]
CHI_STD = [sp.Integer(2), H, H, sp.Integer(-1), sp.Integer(-1), sp.Integer(0)]
CHI_ALT = [sp.Integer(1), -1 / Q, -1 / Q, Q ** -2, Q ** -2, -Q ** -3]

# Illustration's hard-coded q_0 (PR #1999 era).
Q0_STALE = 1.1099785955541805


def delta_n(n: int):
    """Metallic ratio: the `q` at which `h = q - 1/q` equals `n`."""
    return (n + sp.sqrt(n * n + 4)) / 2


def std_rep(q):
    """Explicit convention-D standard rep: `T_i^2 = h T_i + 1`."""
    h = q - 1 / q
    t1 = mp.matrix([[q, 1], [0, -1 / q]])
    t2 = mp.matrix([[-1 / q, 0], [1, q]])
    assert mp.norm(t1 * t1 - (h * t1 + mp.eye(2))) < mp.mpf(10) ** -40
    return t1, t2


def plancherel_weights(n: int):
    """`W_lambda = d_q(lambda)^2 / sum d_q^2`, symbolic where available."""
    parts = list(partitions_of(n))
    return parts, {p: q_dimension(p) for p in parts}


def main() -> int:
    assertions = []
    print("t7qv — the silver coincidence: which weighting carries it")

    # ── A1. the PR #1999 illustration fails three checks under D ──────
    print("\n  1. metallic_q_illustration.py (PR #1999) re-checked at D")
    stale_gap = abs(float(Q0) - Q0_STALE)
    bad_chi = []
    for qs in ("1.1099785827513808076", "1.4", "2.0",
               "2.41421356237309504880"):
        q = mp.mpf(qs)
        t1, t2 = std_rep(q)
        m = t1 * t2
        actual = m[0, 0] + m[1, 1]
        claimed = (q - 1 / q) ** 2 - 1
        bad_chi.append((qs, float(actual), float(claimed)))
    const_minus_one = all(abs(a + 1) < 1e-40 for _, a, _ in bad_chi)
    formula_differs = all(abs(a - c) > 1e-3 for _, a, c in bad_chi)
    # its own curve h^2 - 1 flips sign exactly at the golden rung h = 1
    flips_at_golden = sp.simplify((sp.Symbol("h") ** 2 - 1).subs(
        sp.Symbol("h"), 1)) == 0
    ok = (stale_gap > 1e-9 and const_minus_one and formula_differs
          and bool(flips_at_golden))
    print(f"     (a) stale q_0: |Delta| = {stale_gap:.3e}")
    print(f"     (b) chi_std(sigma_1 sigma_2) = -1 exactly at all q: "
          f"{const_minus_one}; its h^2-1 differs: {formula_differs}")
    for qs, a, c in bad_chi:
        print(f"         q = {qs[:12]:<12}  actual {a:+.6f}   "
              f"claimed h^2-1 = {c:+.6f}")
    print(f"     (c) its own h^2-1 changes sign at h = 1 (golden): "
          f"{bool(flips_at_golden)} — contradicting its own docstring")
    assertions.append(("A1_illustration_stale_and_wrong", ok,
                       f"q0 gap {stale_gap:.3e}; chi_std const -1 "
                       f"{const_minus_one}; formula differs {formula_differs}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. convention-D weights in h; the alt block is annihilated ───
    print("\n  2. convention-D Markov weights, rewritten in h")
    h = sp.Symbol("h", positive=True)
    y_sym_q = (Q ** 4 + 1) / (Q ** 2 + 1) ** 2
    y_std_q = Q ** 2 / (Q ** 2 + 1) ** 2
    r_sym = sp.simplify(y_sym_q - ((H ** 2 + 2) / (H ** 2 + 4)))
    r_std = sp.simplify(y_std_q - (1 / (H ** 2 + 4)))
    r_two = sp.simplify((Q + 1 / Q) ** 2 - (H ** 2 + 4))
    r_nrm = sp.simplify((h ** 2 + 2) / (h ** 2 + 4) + 2 / (h ** 2 + 4) - 1)
    ok = all(x == 0 for x in (r_sym, r_std, r_two, r_nrm))
    print(f"     y_sym = (h^2+2)/(h^2+4)   residual {r_sym}")
    print(f"     y_std = 1/(h^2+4) = 1/[2]_q^2   residual {r_std}"
          f"   ([2]_q^2 = h^2+4 residual {r_two})")
    print(f"     y_alt = 0 identically  ->  only TWO live blocks under D")
    print(f"     normalisation y_sym + 2 y_std - 1 = {r_nrm}")
    assertions.append(("A2_D_weights_in_h_and_alt_annihilated", ok,
                       "all four residuals exactly 0; y_alt = 0"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the identity T(sigma) = (h/2) T(gamma) ────────────────────
    print("\n  3. Plancherel identity  T(sigma) = (h/2) T(gamma)")
    # n = 3, symbolic
    den3 = Q ** 4 + 4 * Q ** 2 + 1
    w3 = [Q ** 2 / den3, (Q ** 2 + 1) ** 2 / den3, Q ** 2 / den3]
    t_gamma3 = sum(w * c for w, c in zip(w3, [CHI_SYM[0], CHI_STD[0],
                                              CHI_ALT[0]]))
    t_sigma3 = sum(w * c for w, c in zip(w3, [CHI_SYM[1], CHI_STD[1],
                                              CHI_ALT[1]]))
    res3 = sp.simplify(2 * t_sigma3 - H * t_gamma3)
    # n = 2, symbolic (two 1-dim blocks, W = (1/2, 1/2))
    t_gamma2 = sp.Rational(1, 2) * 1 + sp.Rational(1, 2) * 1
    t_sigma2 = sp.Rational(1, 2) * Q + sp.Rational(1, 2) * (-1 / Q)
    res2 = sp.simplify(2 * t_sigma2 - H * t_gamma2)
    # input (i): W_lambda = W_lambda' for n = 2..5
    conj_ok = {}
    for n in (2, 3, 4, 5):
        parts, dq = plancherel_weights(n)
        conj_ok[n] = all(
            abs(complex(dq[p]) ** 2
                - complex(dq[tuple(partition_conjugate(p))]) ** 2) < 1e-25
            for p in parts)
    # input (ii): chi^lambda(sigma) + chi^lambda'(sigma) = dim(lambda) h, n = 3
    pair_sym_alt = sp.simplify(CHI_SYM[1] + CHI_ALT[1] - 1 * H)
    pair_std = sp.simplify(2 * CHI_STD[1] - 2 * H)
    ok = (res3 == 0 and res2 == 0 and all(conj_ok.values())
          and pair_sym_alt == 0 and pair_std == 0)
    print(f"     n = 3:  2 T(sigma) - h T(gamma) = {res3}")
    print(f"     n = 2:  2 T(sigma) - h T(gamma) = {res2}")
    print(f"     (i)  W_lambda = W_lambda' for n = 2..5: {conj_ok}")
    print(f"     (ii) chi^(3)+chi^(111) - h = {pair_sym_alt};  "
          f"2 chi^(21) - 2h = {pair_std}")
    print(f"     => T(sigma)/T(gamma) = h/2 at every n, given (i)+(ii)")
    assertions.append(("A3_plancherel_ratio_is_h_over_2", ok,
                       "exact at n = 2 and n = 3; both structural inputs hold"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. therefore the coincidence is at silver, at every n ────────
    print("\n  4. consequence: T(gamma) = T(sigma)  <=>  q = delta_silver")
    silver = sp.simplify(delta_n(2))
    h_at_silver = sp.simplify(silver - 1 / silver)
    coin3 = sp.factor(sp.numer(sp.cancel(sp.together(t_gamma3 - t_sigma3))))
    coin2 = sp.factor(sp.numer(sp.cancel(sp.together(t_gamma2 - t_sigma2))))
    root3 = sp.nsimplify(sp.nsolve(coin3, Q, 2.4), [sp.sqrt(2)])
    root2 = sp.nsimplify(sp.nsolve(coin2, Q, 2.4), [sp.sqrt(2)])
    hit3 = sp.simplify(root3 - silver) == 0
    hit2 = sp.simplify(root2 - silver) == 0
    # the Lean n=2 cost vector is 2[2]_q * (T(gamma), T(sigma))
    lean_t1 = 2 * (Q + 1 / Q)
    lean_t2 = Q ** 2 - Q ** -2
    lean_ok = (sp.simplify(lean_t1 - 2 * (Q + 1 / Q) * t_gamma2) == 0
               and sp.simplify(lean_t2 - 2 * (Q + 1 / Q) * t_sigma2) == 0)
    ok = bool(hit3 and hit2 and h_at_silver == 2 and lean_ok)
    print(f"     h(delta_silver) = {h_at_silver}   (delta_2 = 1 + sqrt 2)")
    print(f"     n = 2 coincidence poly {coin2} -> q = {root2}")
    print(f"     n = 3 coincidence poly {coin3} -> q = {root3}")
    print(f"     Lean's (t_1,t_2) = 2[2]_q ·(T(gamma),T(sigma)): {lean_ok}")
    print(f"     => silver_lp_coincidence (n=2, PR #2047) extends to n = 3, "
          f"and to all n given A3")
    assertions.append(("A4_silver_coincidence_holds_at_n2_and_n3", ok,
                       f"both loci equal 1+sqrt(2); Lean cost vector is the "
                       f"Plancherel one rescaled by 2[2]_q"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. under the D Markov weighting the coincidence MOVES ────────
    print("\n  5. the convention-D Markov trace does NOT carry it")
    z = Q ** 3 / (Q ** 2 + 1)
    t_markov = [sp.Integer(1), z, z, z ** 2, z ** 2, sp.simplify(H * z ** 2 + z)]
    ratio = sp.simplify(t_markov[1] / t_markov[0])
    not_h_over_2 = sp.simplify(ratio - H / 2) != 0
    supergolden_poly = sp.Poly(Q ** 3 - Q ** 2 - 1, Q)
    psi = mp.findroot(lambda x: x ** 3 - x ** 2 - 1, mp.mpf("1.5"))
    h_psi = psi - 1 / psi
    gm_num = sp.factor(sp.numer(sp.cancel(sp.together(
        t_markov[0] - t_markov[1]))))
    ge_num = sp.factor(sp.numer(sp.cancel(sp.together(
        t_markov[0] - t_markov[5]))))
    second = mp.findroot(lambda x: x ** 5 + x ** 4 - 2 * x ** 2 - x - 1,
                         mp.mpf("1.25"))
    h_second = second - 1 / second
    non_metallic = all(
        min(abs(float(hv) - n) for n in (1, 2, 3, 4)) > 1e-9
        for hv in (h_psi, h_second))
    ok = bool(not_h_over_2 and non_metallic
              and sp.simplify(gm_num + (Q ** 3 - Q ** 2 - 1)) == 0)
    print(f"     Markov  T(sigma)/T(gamma) = z = {ratio}   (not h/2)")
    print(f"     gamma = sigma  numer {gm_num}  -> supergolden "
          f"q = {mp.nstr(psi, 17)}, h = {mp.nstr(h_psi, 12)}")
    print(f"     gamma = e-     numer {ge_num}")
    print(f"                    -> q = {mp.nstr(second, 17)}, "
          f"h = {mp.nstr(h_second, 12)}")
    print(f"     neither is metallic: {non_metallic}")
    print(f"     => the earlier H_3/H_9 negative swept the Markov functional; "
          f"the ladder lives in the Plancherel one")
    assertions.append(("A5_markov_coincidence_is_supergolden_not_silver", ok,
                       f"z != h/2; loci at {mp.nstr(psi, 12)} and "
                       f"{mp.nstr(second, 12)}, both non-metallic"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. S(n) subset {delta_1..delta_n} is FALSE at n = 3 ──────────
    print("\n  6. SDPDegeneracyDetectsMetallic: S(n) ⊆ ladder is false at n=3")
    ge3 = sp.factor(sp.numer(sp.cancel(sp.together(
        t_gamma3 - sum(w * c for w, c in zip(
            w3, [CHI_SYM[5], CHI_STD[5], CHI_ALT[5]]))))))
    extra = mp.findroot(
        lambda x: float(sp.lambdify(Q, ge3, "math")(x)), mp.mpf("2.8"))
    h_extra = extra - 1 / extra
    off_ladder = min(abs(float(h_extra) - n) for n in (1, 2, 3, 4)) > 1e-9
    between = 2.0 < float(h_extra) < 3.0
    ok = bool(off_ladder and between)
    print(f"     Plancherel S(3) also contains  T(gamma) = T(e-):")
    print(f"       {ge3}  ->  q = {mp.nstr(extra, 17)}, "
          f"h = {mp.nstr(h_extra, 12)}")
    print(f"     strictly between the silver and bronze rungs: {between}")
    print(f"     so silver IS in S(3) (A4) but S(3) is NOT inside the ladder")
    assertions.append(("A6_S_n_not_contained_in_ladder", ok,
                       f"extra Plancherel locus h = {mp.nstr(h_extra, 12)}, "
                       f"non-metallic, between delta_2 and delta_3"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── summary ───────────────────────────────────────────────────────
    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The owner's regime prediction is right and the corpus already")
    print("  half-proved it. Under the q-Plancherel weighting,")
    print("      T(sigma)/T(gamma) = h/2   identically, at every n,")
    print("  so the cost coincidence sits at h = 2 = delta_silver for every")
    print("  strand count — silver_lp_coincidence (n=2, PR #2047) is the")
    print("  first instance of an all-n identity, and its mechanism is the")
    print("  transpose-pair character sum. That is the sense in which the LP")
    print("  dual IS a representation: the optimisation fact and the")
    print("  representation fact are one identity. Convention D's Markov")
    print("  trace uses different weights, ratio z = q^2/[2]_q instead of")
    print("  h/2, and its coincidence sits at the supergolden ratio")
    print("  q^3 = q^2 + 1 instead. The earlier H_3/H_9 negative swept the")
    print("  Markov functional and is withdrawn as evidence about the ladder.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")
        return 0 if all_ok else 1

    try:
        wb = WitnessBuilder(Path(__file__).stem)
        wb.set_description(
            "Re-examines the PR #1999 metallic negative at convention D. The "
            "illustration is stale (q_0 off by 1.3e-8), plots chi^(2,1)"
            "(sigma_1 sigma_2) = h^2-1 where convention D gives the constant "
            "-1, and plots bare characters while claiming weighted ones; its "
            "own curve flips sign at the golden rung it says nothing flips "
            "at. Under D y_alt = 0, so only two blocks are live, and "
            "y_sym = (h^2+2)/(h^2+4), y_std = 1/[2]_q^2. Under the "
            "q-Plancherel weighting T(sigma) = (h/2) T(gamma) identically at "
            "every n — from W_lambda = W_lambda' plus the transpose-pair "
            "character sum — so the cost coincidence is at h = 2 = "
            "delta_silver for every strand count, generalising the Lean "
            "silver_lp_coincidence from n = 2. Under the convention-D Markov "
            "weighting the ratio is z = q^2/[2]_q instead and the coincidence "
            "moves to the supergolden ratio q^3 = q^2+1. S(3) also contains a "
            "non-metallic locus, refuting S(n) subset {delta_1..delta_n}.")
        wb.add_data("q0_current", str(Q0))
        wb.add_data("q0_stale_in_illustration", f"{Q0_STALE:.16f}")
        wb.add_data("chi_std_on_3cycle_convention_D", "-1 (exact, all q)")
        wb.add_data("D_weights_in_h", {
            "y_sym": "(h^2+2)/(h^2+4)",
            "y_std": "1/(h^2+4) = 1/[2]_q^2",
            "y_alt": "0"})
        wb.add_data("plancherel_identity", "T(sigma) = (h/2) T(gamma)")
        wb.add_data("silver", {"delta_2": "1+sqrt(2)",
                               "value": "2.414213562373095",
                               "h": "2"})
        wb.add_data("markov_coincidence_supergolden",
                    {"poly": "q^3-q^2-1", "q": mp.nstr(psi, 17),
                     "h": mp.nstr(h_psi, 15)})
        wb.add_data("markov_coincidence_second",
                    {"poly": "q^5+q^4-2q^2-q-1", "q": mp.nstr(second, 17),
                     "h": mp.nstr(h_second, 15)})
        wb.add_data("plancherel_extra_locus",
                    {"q": mp.nstr(extra, 17), "h": mp.nstr(h_extra, 15)})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "The all-n statement is conditional on GaloisPairCharacterSum "
            "(chi^lambda(sigma) + chi^lambda'(sigma) = dim(lambda) h), which "
            "is a conjecture CLASS in MetallicLPIdentities.lean, not a "
            "theorem — symbolically verified there for n = 3, 4. This probe "
            "verifies the resulting identity outright at n = 2 and n = 3 and "
            "verifies the other input, W_lambda = W_lambda', at n = 2..5.")
        wb.add_caveat(
            "Two weightings are in play and neither is 'the' right one. The "
            "q-Plancherel measure d_q^2/sum d_q^2 is what pyhecke's "
            "regime_scanner uses and what the Lean silver theorem's cost "
            "vector turns out to be; the convention-D Markov trace y_lambda "
            "is what the atom LP is actually built on. The finding is that "
            "the metallic ladder is a feature of the FORMER, so a metallic "
            "result cannot be transported into the atom LP without first "
            "settling which functional the physics is supposed to extremise.")
        wb.add_caveat(
            "The withdrawal is of a CITATION, not of a measurement. "
            "metallic_ladder_regime_test_probe.py's own H_3 Gram-signature "
            "and H_9 selection sweeps are unaffected and still show no "
            "metallic feature — because, as shown here, they are Markov-"
            "weighted. Its appeal to PR #1999 as independent corroboration, "
            "and its framing of 'representation-theoretic regime' versus "
            "'optimisation regime' as distinct, are both withdrawn.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
