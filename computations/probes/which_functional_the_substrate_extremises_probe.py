#!/usr/bin/env python3
"""Which functional the physics extremises: the Markov trace, decisively — and
why binding is zero at `q_0` anyway.

WHAT WAS ASKED
--------------
Two turns left a functional ambiguity open, and I claimed it was blocking from
two directions:

  * **Axis 1.** `metallic_silver_coincidence_weighting_probe.py` found the
    metallic ladder lives in the **q-Plancherel** weighting
    `W_lambda = d_q^2 / sum d_q^2`, not the convention-D **Markov** weighting
    `y_lambda`.
  * **Axis 2.** `nfold_ip_coupling_duality_gap_probe.py` needed an **additive**
    cost `sum_k t.x_k` where the corpus's atom construction uses a
    **multiplicative** `t^(x)A . x`.

Both are settled here, and one of them was never actually a fork. **I withdraw
"blocking from two directions"**: Axis 2 makes no difference to anything.

AXIS 1 — MARKOV, ON THREE INDEPENDENT GROUNDS
------------------------------------------------
The question is not a preference. Three properties the corpus already *demands*
each pick out the Markov trace and each reject Plancherel:

**(1) The Markov property.** `tr(x . T_n) = z . tr(x)` for `x` in `H_{n-1}` is
what makes the trace a link invariant, and it is what the whole closure/arity
apparatus rests on (`c_free = 2A`, `c_atom = A+1`, Lean
`QOU.MassTheory.ClassicalTraceFloor`). Testing on the two `H_2` basis elements:

    Markov      T(gamma.s1)/T(gamma) = z        T(s0.s1)/T(s0) = z       SAME
    Plancherel  T(gamma.s1)/T(gamma) = h/2      T(s0.s1)/T(s0) =
                                          -2q^3/(q^6+2q^4-2q^2-1)        DIFFERENT

Plancherel is **not a Markov trace**. Its ratio is not even a constant, so it
carries no Markov parameter at all.

**(2) The Gram radical.** Convention D's defining fact is that the Gram is
singular, `det G = 0`, with radical exactly the three-strand q-antisymmetriser
— which is the statement `y_alt = 0`. Plancherel has `W_alt = q^2/D != 0`, so a
Plancherel Gram is **nonsingular**: a different cone from the one every SDP in
this corpus is posed over.

**(3) Multiplicativity on disjoint strand blocks.** This is the property that
gives `t^(A) = t^(x)A` and hence makes the entire atom construction possible
(`h3a_frobenius_gram_offdiagonal_probe` verified it for the Markov trace at
`H_6`). Running the *same* test with Plancherel weights: **36 of 36 basis pairs
fail**, worst relative error `1.09e+01`. And it is not a normalisation problem —
`gamma(x)gamma`, `gamma(x)s0`, `s0(x)gamma` all miss by the same factor 4.0346,
but `s0(x)s0` misses by `-2.056`, **with a sign flip**. No rescaling repairs it.

**Verdict: the substrate extremises the Markov functional.** Consequently the
silver coincidence `T(sigma) = (h/2) T(gamma)` — which is a true theorem, and
still is — is a theorem about a functional that is not a link invariant, does
not carry the corpus's cone, and cannot build an atom. **The metallic ladder is
a property of a functional the substrate does not use.** That retires it as a
physical mechanism rather than leaving it open.

AXIS 2 — A NON-ISSUE: BOTH COSTS GIVE EXACTLY ZERO
-----------------------------------------------------
The additive/multiplicative choice changes nothing. Running the full
multiplicative program at its true dimension —

    min { t^(x)A . x  :  G^(x)A x >= G^(x)A v_(x),  x >= 0 }

with no collapse, `6^A` variables (1296 for `4He`) — the gap is again exactly
zero, for `2H`, `3H`, `3He` and `4He`, at `1.4e-16`. The tensor of the
per-nucleon optima is *already* globally optimal for the coupled program.

WHY: THE VALUE FUNCTION IS LINEAR, NOT MERELY PIECEWISE LINEAR
-----------------------------------------------------------------
The dual is `phi(v) = max { y.(Gv) : G^T y <= t, y >= 0 }`, and at `q_0` its
optimum is **rank one and identical for both nucleons**:

    y*_p  =  y*_n  =  0.54312042 . e_3          (a single active row, sigma_1)

so `phi(v) = 0.54312042 . (G v)_2` — **exactly linear in `v`**, to a residual
of exactly 0.0, verified on `v_p`, `v_n`, `v_p+v_n` and `2v_p+2v_n`. A linear value function is exactly
additive, so the aggregation gap vanishes identically: for every `(Z,N)`, every
isotope, and either cost convention. That single fact is the whole explanation
of the zero, and it subsumes the earlier "nested supports" observation.

Note this is `t = G e_1` biting again (`h3a_frobenius_gram_offdiagonal_probe`).
`y = e_1` is dual-feasible with *all six* dual constraints tight — a maximally
degenerate vertex — though it is not the optimum (`phi(v_p) = 0.694056` against
`t.v_p = 0.629328`).

AND IT IS A CRITICAL CONFIGURATION, NOT A ROBUST ONE
-------------------------------------------------------
The obstruction is **not** geometric — the feasible set is perfectly capable of
producing binding. Of 300 random nonnegative costs, **86 open a strictly
positive gap** (worst 1.65 % relative). What is special is the Markov cost
specifically. And it is special in the sharpest possible way: along directions
that do open a gap, `gap/eps` is **constant to six significant figures across
six decades** of `eps` (1e-1 down to 1e-6; three directions shown, constants
0.0309, 0.0289, 0.0174, each flat to < 5e-8). A gap growing exactly linearly
from zero means the Markov cost lies **exactly on the boundary** of the no-gap region — a critical
point, not an interior one. 5 of 24 random directions cross it; the rest stay
at exact zero, so the boundary is a face rather than a point.

WHAT THIS MEANS FOR L2 1PPQ
------------------------------
Binding is zero at `q_0` because the substrate sits precisely on the critical
face where the LP value function degenerates to rank one. It is not zero
because the wrong cost was chosen (both give zero), nor because the geometry
forbids it (28.7 % of costs give binding). So the live question is no longer
"which functional" — it is **why the substrate sits exactly on that face**, and
whether the physical binding is the linear response `C.eps` to whatever breaks
the degeneracy. That is a well-posed follow-up with a measured coefficient
already in hand.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired. `H_6` multiplicativity reuses the corpus's
own `hecke_characters.build_seminormal_matrices`, the same routine
`h3a_frobenius_gram_offdiagonal_probe` used for the Markov check. Axis-1 tests
1 and 2 are exact symbolic identities. A correction against my own earlier
draft of this probe: a first pass detected gap-opening with `abs(gap) > 1e-9`
and reported a knife-edge radius of `3e-8`; those were *negative* gaps, which
are structurally impossible since aggregation is a relaxation, i.e. solver
noise. Every gap measurement here is sign-aware with a relative threshold, and
the boundary claim rests on the linear scaling, not on a radius.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] metallic_silver_coincidence_weighting_probe.py (Axis 1)
-- Ref: [probe] nfold_ip_coupling_duality_gap_probe.py (Axis 2)
-- Ref: [probe] h3a_frobenius_gram_offdiagonal_probe.py (t = G e_1; the Markov
   multiplicativity check reused here)
-- Ref: [lean] QOU.MassTheory.ClassicalTraceFloor (c_atom = A + 1)
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
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402
from scipy.optimize import linprog  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from pyhecke.gram import _hm_mp, gram_matrix_mp  # noqa: E402
from pyhecke.wedderburn import partitions_of, q_dimension  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 30
NF = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NAMES = ["gamma", "s0", "s1", "L+", "L-", "e-"]


def substrate():
    q = mp.mpf(str(Q0))
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    gram = np.array([[float(x) for x in row] for row in gram_matrix_mp(30, q=q)])
    cost = np.array([float(x) for x in
                     [mp.mpf(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]])

    def nucleon(kind: str) -> np.ndarray:
        nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
        for _ in range(3):
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
        if kind == "p":
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 1, h)
        else:
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        return np.array([float(x) for x in nf])

    return gram, cost, nucleon("p"), nucleon("n")


def plancherel_h3():
    """Symbolic Plancherel functional on the H_3 NF basis."""
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    den = q ** 4 + 4 * q ** 2 + 1
    w = [q ** 2 / den, (q ** 2 + 1) ** 2 / den, q ** 2 / den]
    chi = [[1, q, q, q ** 2, q ** 2, q ** 3],
           [2, h, h, -1, -1, 0],
           [1, -1 / q, -1 / q, q ** -2, q ** -2, -q ** -3]]
    return q, h, w, [sp.simplify(sum(w[b] * chi[b][i] for b in range(3)))
                     for i in range(6)]


def kron_all(mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def solve(gram, cost, v):
    r = linprog(cost, A_ub=-gram, b_ub=-(gram @ v),
                bounds=[(0, None)] * 6, method="highs")
    if not r.success:
        return None, None
    return float(r.fun), -r.ineqlin.marginals


def relgap(gram, cost, vp, vn):
    a, _ = solve(gram, cost, vp)
    b, _ = solve(gram, cost, vn)
    ab, _ = solve(gram, cost, vp + vn)
    if None in (a, b, ab):
        return None
    return (a + b - ab) / max(abs(a + b), 1e-30)


def main() -> int:
    assertions = []
    print("t7qv — which functional the substrate extremises")
    gram, cost, vp, vn = substrate()
    qs, hs, w3, tP = plancherel_h3()
    z_sym = qs ** 3 / (qs ** 2 + 1)
    tM = [sp.Integer(1), z_sym, z_sym, z_sym ** 2, z_sym ** 2,
          sp.simplify(hs * z_sym ** 2 + z_sym)]

    # ── A1. the Markov property ───────────────────────────────────────
    print("\n  1. the Markov property  tr(x . T_n) = z tr(x)")
    m1 = sp.simplify(tM[2] / tM[0])
    m2 = sp.simplify(tM[3] / tM[1])
    p1 = sp.simplify(tP[2] / tP[0])
    p2 = sp.simplify(tP[3] / tP[1])
    markov_const = sp.simplify(m1 - m2) == 0
    planch_const = sp.simplify(p1 - p2) == 0
    ok = bool(markov_const and not planch_const)
    print(f"     Markov      gamma->s1: {m1}     s0->L+: {m2}   same: "
          f"{markov_const}")
    print(f"     Plancherel  gamma->s1: {p1}     s0->L+: {p2}")
    print(f"                 same: {planch_const}   -> NOT a Markov trace")
    assertions.append(("A1_plancherel_is_not_a_markov_trace", ok,
                       "Markov ratio is z on both; Plancherel gives h/2 and "
                       "-2q^3/(q^6+2q^4-2q^2-1)"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the Gram radical / annihilated block ──────────────────────
    print("\n  2. the Gram radical (convention D: det G = 0, radical = e_alt)")
    w_alt = sp.simplify(w3[2])
    y_alt_zero = True                      # convention D, established
    ok = bool(w_alt != 0 and y_alt_zero)
    detG = float(np.linalg.det(gram))
    rank = int(np.linalg.matrix_rank(gram, tol=1e-9))
    print(f"     Markov     y_alt = 0            -> Gram singular: "
          f"det = {detG:.3e}, rank {rank} of 6")
    print(f"     Plancherel W_alt = {w_alt} != 0  -> Gram would be NONSINGULAR")
    print(f"     so Plancherel poses the SDP over a different cone")
    assertions.append(("A2_plancherel_does_not_annihilate_antisymmetriser", ok,
                       f"W_alt = q^2/D != 0 while y_alt = 0; Markov Gram rank "
                       f"{rank}/6, det {detG:.2e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. multiplicativity on disjoint strand blocks (H_6) ──────────
    print("\n  3. multiplicativity on disjoint blocks — what gives t^(A) = "
          "t^(x)A")
    parts6 = list(partitions_of(6))
    dq6 = [float(q_dimension(p)) for p in parts6]
    ssq = sum(d * d for d in dq6)
    w6 = [d * d / ssq for d in dq6]
    sig = {tuple(p): [np.asarray(m, dtype=float)
                      for m in build_seminormal_matrices(list(p))[0]]
           for p in parts6}

    def tr6(word):
        tot = 0.0
        for i, p in enumerate(parts6):
            s = sig[tuple(p)]
            mtx = np.eye(s[0].shape[0])
            for g in word:
                mtx = mtx @ s[g]
            tot += w6[i] * float(np.trace(mtx))
        return tot

    tP_num = [float(sp.N(x.subs(qs, sp.Float(str(Q0), 30)), 30)) for x in tP]
    bad, worst, factors = 0, 0.0, {}
    for i, wi in enumerate(NF):
        for j, wj in enumerate(NF):
            lhs = tr6(list(wi) + [g + 3 for g in wj])
            rhs = tP_num[i] * tP_num[j]
            rel = abs(lhs - rhs) / max(abs(rhs), 1e-30)
            worst = max(worst, rel)
            if rel > 1e-6:
                bad += 1
            if (i, j) in ((0, 0), (0, 1), (1, 0), (1, 1)):
                factors[f"{NAMES[i]}x{NAMES[j]}"] = lhs / rhs
    ok = bad == 36 and worst > 1.0
    print(f"     Plancherel: {bad} of 36 pairs fail at 1e-6; "
          f"worst relative error {worst:.4e}")
    print(f"     and no rescaling repairs it — lhs/rhs by pair:")
    for k, v in factors.items():
        print(f"        {k:<16s} {v:+.6f}")
    print(f"     (three agree at +4.0346 but s0xs0 is -2.0556, a SIGN FLIP)")
    assertions.append(("A3_plancherel_not_multiplicative_on_blocks", ok,
                       f"{bad}/36 pairs fail, worst rel err {worst:.3e}, "
                       f"sign flip on s0xs0 rules out a normalisation fix"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")
    print("\n     ==> VERDICT: the substrate extremises the MARKOV functional.")
    print("         The metallic ladder belongs to a functional that is not a")
    print("         link invariant, has a different cone, and cannot build an")
    print("         atom. Retired as a physical mechanism.")

    # ── A4. Axis 2 is a non-issue: both costs give exactly zero ───────
    print("\n  4. additive vs multiplicative: both exactly zero at q_0")
    pp, _ = solve(gram, cost, vp)
    nn, _ = solve(gram, cost, vn)
    _, xp = solve(gram, cost, vp), None
    rp = linprog(cost, A_ub=-gram, b_ub=-(gram @ vp),
                 bounds=[(0, None)] * 6, method="highs")
    rn = linprog(cost, A_ub=-gram, b_ub=-(gram @ vn),
                 bounds=[(0, None)] * 6, method="highs")
    worst_mult = 0.0
    print(f"     {'atom':5s} {'dim':>5s} {'free = prod phi':>18s} "
          f"{'atom_mult':>16s} {'gap':>13s}")
    for lbl, Z, N in [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]:
        A = Z + N
        vs = [vp] * Z + [vn] * N
        big_g = kron_all([gram] * A)
        big_t = kron_all([cost.reshape(1, -1)] * A).ravel()
        v_t = kron_all([v.reshape(-1, 1) for v in vs]).ravel()
        free = (pp ** Z) * (nn ** N)
        r = linprog(big_t, A_ub=-big_g, b_ub=-(big_g @ v_t),
                    bounds=[(0, None)] * (6 ** A), method="highs")
        g = free - float(r.fun)
        worst_mult = max(worst_mult, abs(g))
        print(f"     {lbl:5s} {6 ** A:5d} {free:18.12f} {float(r.fun):16.12f} "
              f"{g:+13.3e}")
    ok = worst_mult < 1e-12
    print(f"     largest |gap| over the multiplicative programs = "
          f"{worst_mult:.3e}")
    print(f"     the tensor of per-nucleon optima is ALREADY globally optimal")
    assertions.append(("A4_both_costs_give_zero", ok,
                       f"multiplicative gap max {worst_mult:.2e} at full 6^A "
                       f"(1296 vars at 4He); additive zero already shown"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. the mechanism: a rank-one, shared dual ────────────────────
    print("\n  5. why: the dual is rank one and SHARED by both nucleons")
    yp = -rp.ineqlin.marginals
    yn = -rn.ineqlin.marginals
    same = bool(np.allclose(yp, yn, atol=1e-9))
    supp_p = int((np.abs(yp) > 1e-11).sum())
    lam = float(yp[np.argmax(np.abs(yp))])
    row = int(np.argmax(np.abs(yp)))
    lin_err = 0.0
    for v in (vp, vn, vp + vn, 2 * vp + 2 * vn):
        val, _ = solve(gram, cost, v)
        lin_err = max(lin_err, abs(val - lam * float((gram @ v)[row])))
    ok = bool(same and supp_p == 1 and lin_err < 1e-7)
    print(f"     y*_p = {np.round(yp, 9)}")
    print(f"     y*_n = {np.round(yn, 9)}   identical: {same}")
    print(f"     support size {supp_p} — a single active row, index {row} "
          f"({NAMES[row]})")
    print(f"     so phi(v) = {lam:.8f} * (G v)_{row}, EXACTLY LINEAR in v")
    print(f"     max |phi(v) - lam (Gv)_{row}| over 4 vectors = {lin_err:.2e}")
    print(f"     a linear value function is exactly additive => gap == 0 for")
    print(f"     every (Z,N) and either cost convention. That is the whole zero.")
    assertions.append(("A5_rank_one_shared_dual_makes_phi_linear", ok,
                       f"y*_p = y*_n = {lam:.8f} e_{row}; linearity residual "
                       f"{lin_err:.2e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. critical, not geometric ───────────────────────────────────
    print("\n  6. the obstruction is CRITICAL, not geometric")
    rng = np.random.default_rng(7)
    pos, spurious, worst_rel = 0, 0, 0.0
    for _ in range(300):
        c = rng.random(6) + 0.05
        g = relgap(gram, cost=c, vp=vp, vn=vn)
        if g is None:
            continue
        if g > 1e-8:
            pos += 1
            worst_rel = max(worst_rel, g)
        elif g < -1e-8:
            spurious += 1
    print(f"     random nonnegative costs opening a POSITIVE gap: {pos}/300 "
          f"(worst {100 * worst_rel:.4f}%)")
    print(f"     structurally impossible negatives seen: {spurious}")
    rng = np.random.default_rng(11)
    slopes, shown = [], 0
    for _ in range(24):
        d = rng.normal(size=6)
        d /= np.linalg.norm(d)
        g0 = relgap(gram, cost + 1e-2 * d, vp, vn)
        if g0 is None or g0 < 1e-8:
            continue
        ratios = []
        for e in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
            c = cost + e * d
            if np.any(c <= 0):
                continue
            a, _ = solve(gram, c, vp)
            b, _ = solve(gram, c, vn)
            ab, _ = solve(gram, c, vp + vn)
            ratios.append((a + b - ab) / e)
        spread = (max(ratios) - min(ratios)) / max(ratios)
        slopes.append((ratios[0], spread))
        if shown < 3:
            print(f"     direction: gap/eps over 1e-1..1e-6 = "
                  f"{ratios[0]:.6f} (spread {spread:.2e})")
            shown += 1
    linear = bool(slopes) and all(s < 1e-6 for _, s in slopes)
    ok = bool(pos > 50 and spurious == 0 and linear)
    print(f"     {len(slopes)} of 24 directions open a gap; in every one "
          f"gap/eps is constant to {max((s for _, s in slopes), default=0):.1e}")
    print(f"     gap grows EXACTLY linearly from zero => the Markov cost lies")
    print(f"     ON the boundary of the no-gap region, not inside it.")
    assertions.append(("A6_critical_not_geometric", ok,
                       f"{pos}/300 random costs bind; gap/eps constant over "
                       f"6 decades in {len(slopes)}/24 directions"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Axis 1 is settled three ways over: the substrate extremises the")
    print("  MARKOV trace. Plancherel is not a Markov trace, does not")
    print("  annihilate the antisymmetriser, and is not multiplicative on")
    print("  disjoint blocks (36/36 fail). So the metallic ladder is a")
    print("  property of a functional the substrate cannot use — retired.")
    print("  Axis 2 was never a fork and I withdraw the claim that it was:")
    print("  additive and multiplicative both give exactly zero, the latter")
    print("  verified at full 6^A. The reason is one fact — at q_0 the dual")
    print("  optimum is rank one and shared, so phi is exactly LINEAR and")
    print("  therefore exactly additive.")
    print("  And that zero is critical, not structural: 86 of 300 random")
    print("  costs do bind, and the gap opens exactly linearly in the")
    print("  perturbation, so the substrate sits ON the boundary face.")
    print("  The open question is no longer 'which functional' but why the")
    print("  substrate sits exactly there, and whether physical binding is")
    print("  the linear response to whatever breaks the degeneracy.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="scipy")
        wb.set_description(
            "Settles which functional the substrate extremises. Three "
            "independent properties the corpus already demands each reject the "
            "q-Plancherel weighting and select the convention-D Markov trace: "
            "Plancherel is not a Markov trace (tr(x.T_n)/tr(x) is h/2 on gamma "
            "but -2q^3/(q^6+2q^4-2q^2-1) on s0, not constant); it does not "
            "annihilate the q-antisymmetriser (W_alt = q^2/D != 0 against "
            "y_alt = 0), so its Gram is nonsingular and its cone is not the "
            "corpus's; and it is not multiplicative on disjoint strand blocks "
            "at H_6 (36/36 pairs fail, worst rel err 10.9, with a sign flip on "
            "s0xs0 ruling out a normalisation fix), which is the property that "
            "gives t^(A) = t^(x)A. So the metallic ladder is a property of a "
            "functional the substrate cannot use. The additive/multiplicative "
            "question is a non-issue: both give exactly zero binding at q_0, "
            "the multiplicative verified at full 6^A (1296 vars at 4He), "
            "because the dual optimum is rank one and shared by both nucleons "
            "(y* = 0.54312042 e_2), making phi(v) = lam (Gv)_2 exactly linear "
            "and hence exactly additive. The zero is critical rather than "
            "geometric: 86 of 300 random nonnegative costs open a positive "
            "gap, and where a gap opens it grows exactly linearly in the "
            "perturbation (gap/eps constant over six decades), so the Markov "
            "cost lies on the boundary of the no-gap region.")
        wb.add_data("verdict", "Markov trace, on three independent grounds")
        wb.add_data("plancherel_markov_ratio",
                    {"gamma": "h/2", "s0": "-2q^3/(q^6+2q^4-2q^2-1)"})
        wb.add_data("plancherel_multiplicativity",
                    {"failed_pairs": f"{bad}/36",
                     "worst_rel_err": f"{worst:.4e}",
                     "lhs_over_rhs": {k: f"{v:+.6f}"
                                      for k, v in factors.items()}})
        wb.add_data("dual_at_q0", {"y_star": [f"{x:.9f}" for x in yp],
                                   "support": supp_p, "row": row,
                                   "lambda": f"{lam:.9f}"})
        wb.add_data("phi_linearity_residual", f"{lin_err:.3e}")
        wb.add_data("multiplicative_gap_max", f"{worst_mult:.3e}")
        wb.add_data("random_costs_that_bind", f"{pos}/300")
        wb.add_data("gap_slopes", [f"{s:.6f}" for s, _ in slopes])
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "RETIRING THE METALLIC LADDER IS A RE-SCOPING, NOT A REFUTATION. "
            "The silver coincidence T(sigma) = (h/2) T(gamma) at every n, and "
            "the Lean silver_lp_coincidence it generalises, remain true "
            "theorems about the Plancherel functional. What is established "
            "here is that the substrate's own dynamics cannot be posed over "
            "that functional, so the ladder is not available as a physical "
            "mechanism. If a future construction finds a legitimate role for "
            "the Plancherel weighting, the metallic results come back with it.")
        wb.add_caveat(
            "CORRECTION AGAINST AN EARLIER DRAFT OF THIS PROBE. A first pass "
            "detected gap-opening with abs(gap) > 1e-9 and reported a "
            "knife-edge radius of 3e-8; those were NEGATIVE gaps, which are "
            "structurally impossible since aggregation is a relaxation — i.e. "
            "solver noise, not signal. All measurements here are sign-aware "
            "with a relative threshold, zero spurious negatives are observed, "
            "and the boundary claim rests on the linear scaling of the gap "
            "over six decades rather than on any radius.")
        wb.add_caveat(
            "The Markov multiplicativity leg is asserted from "
            "h3a_frobenius_gram_offdiagonal_probe (max rel err 1.1e-8 over the "
            "same 36 pairs), not re-run here; only the Plancherel side is "
            "recomputed. The two use the same build_seminormal_matrices "
            "routine and the same basis pairs, so the comparison is "
            "like-for-like.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
