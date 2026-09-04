#!/usr/bin/env python3
"""The atom LP as an n-fold IP: binding is the aggregation gap — and it is
exactly zero at `q_0`.

WHAT WAS ASKED
--------------
Owner: *"Reformulate the atom LP as an n-fold IP and measure binding as the
coupling duality gap."* Following De Loera-Hemmecke-Onn-Weismantel,
**N-Fold Integer Programming** (`math/0605242`), from the owner's paper drop
`5bbd4b33`. An n-fold IP has constraint matrix

    A^(n)  =  (1_n (x) I_q) (+) (I_n (x) A)

— `n` independent copies of a fixed block `A x_k = b_k`, coupled by one global
row block `sum_k x_k = b_0`. Their words: the programs are almost separable,
*"the constraint sum x_k = b_0 **binds** these programs together."*

THE REFORMULATION
-----------------
Take the corpus's own positive-sector LP, unchanged
(`positive_sector_operator_selection_probe.py`):
`phi(v) = min { t . x : G x >= G v, x >= 0 }` on the `H_3` NF basis, with `G`
the convention-D Gram and `t` the Markov cost. Then

    free(Z,N)  =  Z phi(v_p) + N phi(v_n)
                  = sum_k min { t . x_k : G x_k >= G v_k, x_k >= 0 }
                  ^ n SEPARATE local blocks, no coupling

    atom(Z,N)  =  min { sum_k t . x_k : sum_k G x_k >= sum_k G v_k, x >= 0 }
                  ^ the SAME constraints AGGREGATED into one coupling block

    E_bind     =  free - atom

Nothing is put in by hand: `atom` is `free` with the `n` local constraint
blocks replaced by their sum, which is the textbook aggregation relaxation, so
every free-feasible point is atom-feasible and **`E_bind >= 0` structurally**.
Concretely `x_p + x_n` is aggregate-feasible with cost exactly `free`, which is
the one-line proof of the sign. The mass defect comes out with the right sign
from the relaxation alone.

TWO THINGS THIS BUYS
--------------------
**(1) The `6^A` blowup disappears.** Substituting `X = sum_k x_k`, the atom
program is a single **6-variable** LP, `atom = phi(Z v_p + N v_n)`. The whole
`A`-dependence sits in the right-hand side. Verified here against the explicit
`6A`-variable block LP at `A = 2, 3, 4`: identical to `1e-12`. That is the
n-fold theorem's payoff realised on this program.

**(2) Binding is exactly the non-additivity of the LP value function.** `phi`
is positively homogeneous and convex in its right-hand side, hence subadditive,
and

    E_bind = Z phi(v_p) + N phi(v_n) - phi(Z v_p + N v_n)

is precisely its **cone-crossing defect**: zero when `v_p` and `v_n` lie in one
linearity cone of `phi`, positive when the aggregate optimum crosses to another
vertex. So "what binds a nucleus" becomes "do the proton and the neutron sit in
different pieces of the value function", which is a finite, decidable question.

THE ANSWER AT `q_0`: ZERO
---------------------------
They do not. At `q_0` the optimal supports are `(2,3,4)` for the proton and
`(2,3)` for the neutron — **nested**, so both sit in the closure of one cone,
`phi` is linear along the whole ray, and

    E_bind = 0   to machine epsilon, for every isotope tested
             (2H, 3H, 3He, 4He, 6Li, 12C, 16O, and pure-p / pure-n systems)

The largest residual over the whole table is `5.3e-15` on a value of order 10.
This is not a small binding; it is an exact algebraic zero.

BUT THE MECHANISM IS REAL, AND IT HAS A WINDOW
------------------------------------------------
Sweeping `h = q - 1/q` from 0.05 to 4.2, the gap is zero everywhere except one
interval, whose edges bisect to

    h in (0.47718474189158, 0.56984029056366)
    q in (1.26666159014921, 1.32471795696803)          peak 0.0687 at h = 0.534

`q_0` has `h = 0.20906`, **56.2 % below the lower edge**. Everything outside
that window is float noise (`|gap| < 1e-9`, and rising with the magnitude of
the values, as noise does).

Inside the window the gap obeys an exact law across `0 <= Z, N <= 4`:

    E_bind(Z, N)  =  min(Z, N) . kappa            kappa = 0.069590  (Z >= N)
                                                        = 0.070191  (Z <  N)

with `E_bind = 0` identically whenever `Z = 0` or `N = 0`. Two remarks, one
encouraging and one disciplining:

  * **No binding without both species.** No bound dineutron, no bound diproton,
    for a structural reason rather than a fitted one. That is the correct
    qualitative physics and nothing here was tuned to produce it.
  * `min(Z,N) = (A - |N - Z|)/2`, so the law is a volume term and an asymmetry
    term with their coefficients **locked at ratio 1**. It is *not* the
    semi-empirical mass formula: the SEMF asymmetry term goes as `(N-Z)^2 / A`,
    not `|N-Z|`. Do not read this as a derivation of the SEMF.

WHAT THIS SETTLES AND WHAT IT DOES NOT
----------------------------------------
Settled: the n-fold reformulation is correct, it collapses the exponential, it
produces a binding-shaped quantity with the right sign and the right pairing
structure from a relaxation with nothing fitted — and **at the physical
substrate point that quantity is identically zero.** So the coupling
aggregation gap is not the source of nuclear binding at `q_0`. The `4He` L2
miss (`qou-1nvh`: 8 meV wanted out of 28.3 MeV) is not repaired by this route.

Not settled, and this is the live question: the reformulation replaces the
multiplicative cost `t^(x)A . x` with the additive `sum_k t . x_k`. Those are
different functionals, not two spellings of one — the additive one is what the
n-fold form requires. Combined with the previous turn's finding that the
metallic structure lives in the Plancherel functional and not the Markov one
(`metallic_silver_coincidence_weighting_probe.py`), the same question is now
blocking from two directions: **which functional is the physics supposed to
extremise?** Until that is settled, a zero here is a zero for the Markov-cost
additive program specifically, not for the reformulation as such.

WHAT IS BUILT HERE IS THE **LP RELAXATION**
---------------------------------------------
Everything below runs `scipy.linprog` — continuous, not integer. The n-fold
*aggregation* structure is fully exercised (that is what produces the gap, the
collapse and the pairing law), but Theorem 1.1's actual content — poly-time
solvability of the **integer** program via Graver-basis stabilisation — is not.
For this program the LP collapse to 6 variables makes the relaxation trivially
tractable, so the interesting complexity question lives entirely in the
integrality that is *not* built here. That is the honest boundary of this
probe, and where a follow-up belongs.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired. The LP is the corpus's existing
positive-sector program with its Gram, cost and nucleon chains unchanged. The
peak gap is verified three ways: `highs`, `highs-ds` and `highs-ipm` agree to
9 digits; the separate problems carry valid dual certificates (`y >= 0`,
`G^T y <= t`, dual objective equal to primal); and an explicit feasible point
strictly cheaper than `free` is exhibited. Window edges are 50-step bisections.

-- Ref: [manuscript] bean t7qv
-- Ref: [paper] De Loera, Hemmecke, Onn, Weismantel, N-Fold Integer
   Programming, math/0605242 (owner drop 5bbd4b33)
-- Ref: [probe] positive_sector_operator_selection_probe.py (the LP reused here)
-- Ref: [probe] h3a_frobenius_gram_offdiagonal_probe.py (t = G e_1)
-- Ref: [bean] qou-1nvh (L2 light-isotope error attribution)
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
from scipy.optimize import linprog  # noqa: E402

from pyhecke.gram import _hm_mp, gram_matrix_mp  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 30
H_Q0 = float(q_at(mp.mp.dps) - 1 / q_at(mp.mp.dps))
ZERO_TOL = 1e-9


def build(q_val):
    """Gram, Markov cost and both nucleon NF vectors at this `q`.

    Accepts an `mpf` or a decimal string.  The anchored call passes the `mpf`
    from `q_at` directly: routing the substrate `q0` through `str()` would go
    via the float64 Newton solve and carry a ~1e-17 error into a 30-dps solve.
    The h-sweep call sites pass a `repr()` of a float64 `q_of_h` on purpose --
    those points ARE float64, and say so.
    """
    q = mp.mpf(q_val)
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


def q_of_h(hv: float) -> float:
    return (hv + (hv * hv + 4) ** 0.5) / 2


def phi(gram, cost, v, method: str = "highs"):
    """`min { t.x : G x >= G v, x >= 0 }` — the corpus's positive-sector LP."""
    r = linprog(cost, A_ub=-gram, b_ub=-(gram @ v),
                bounds=[(0, None)] * 6, method=method)
    if not r.success:
        return None, None, None
    supp = tuple(i for i in range(6) if r.x[i] > 1e-11)
    return float(r.fun), supp, r.x


def block_lp(gram, cost, vs):
    """The explicit `6A`-variable n-fold program, coupling block and all."""
    n = len(vs)
    big_c = np.tile(cost, n)
    big_a = np.hstack([-gram] * n)                      # one coupling block
    big_b = -(gram @ sum(vs))
    r = linprog(big_c, A_ub=big_a, b_ub=big_b,
                bounds=[(0, None)] * (6 * n), method="highs")
    return float(r.fun) if r.success else None


def gap(gram, cost, vp, vn, Z: int, N: int):
    pp, _, _ = phi(gram, cost, vp)
    nn, _, _ = phi(gram, cost, vn)
    if pp is None or nn is None:
        return None, None, None
    free = Z * pp + N * nn
    if Z == 0 and N == 0:
        return 0.0, 0.0, 0.0
    atom, _, _ = phi(gram, cost, Z * vp + N * vn)
    if atom is None:
        return None, None, None
    return free, atom, free - atom


def gap_at_h(hv: float, Z: int = 1, N: int = 1):
    gram, cost, vp, vn = build(repr(q_of_h(hv)))
    _, _, g = gap(gram, cost, vp, vn, Z, N)
    return g


def bisect_edge(a: float, b: float) -> float:
    """`a` and `b` straddle the gap>0 threshold; 50 steps."""
    fa = gap_at_h(a) > ZERO_TOL
    for _ in range(50):
        m = 0.5 * (a + b)
        if (gap_at_h(m) > ZERO_TOL) == fa:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
            ("6Li", 3, 3), ("12C", 6, 6), ("16O", 8, 8),
            ("2n", 0, 2), ("2p", 2, 0), ("4n", 0, 4)]


def main() -> int:
    assertions = []
    print("t7qv — the atom LP as an n-fold IP; binding as the coupling gap")

    gram0, cost0, vp0, vn0 = build(q_at(mp.mp.dps))

    # ── A1. aggregation is a relaxation, so the sign is structural ────
    print("\n  1. E_bind >= 0 is structural, not fitted")
    pp, sp_, xp = phi(gram0, cost0, vp0)
    nn, sn, xn = phi(gram0, cost0, vn0)
    xs = xp + xn
    slack = float(np.min(gram0 @ xs - gram0 @ (vp0 + vn0)))
    cost_sum = float(cost0 @ xs)
    ok = slack > -1e-9 and abs(cost_sum - (pp + nn)) < 1e-12
    print(f"     x_p + x_n is aggregate-feasible: min slack = {slack:+.3e}")
    print(f"     its cost = {cost_sum:.12f} = free = {pp + nn:.12f}")
    print(f"     hence atom <= free always  =>  E_bind >= 0, no tuning")
    assertions.append(("A1_gap_nonnegative_structurally", ok,
                       f"x_p+x_n feasible (slack {slack:.2e}), cost = free"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the 6^A blowup collapses to one 6-variable LP ─────────────
    print("\n  2. the atom program collapses: 6^A -> 6 variables")
    coll_ok = True
    for lbl, Z, N in [("2H", 1, 1), ("3H", 1, 2), ("4He", 2, 2)]:
        vs = [vp0] * Z + [vn0] * N
        blk = block_lp(gram0, cost0, vs)
        col, _, _ = phi(gram0, cost0, Z * vp0 + N * vn0)
        d = abs(blk - col)
        coll_ok &= d < 1e-12
        print(f"     {lbl:4s} A={Z + N}  block LP ({6 * (Z + N):2d} vars) = "
              f"{blk:.12f}   collapsed (6 vars) = {col:.12f}   |d| = {d:.2e}")
    print(f"     the whole A-dependence is in the right-hand side")
    assertions.append(("A2_block_program_collapses_to_six_vars", coll_ok,
                       "block and collapsed LPs agree to 1e-12 at A = 2, 3, 4"))
    print(f"     -> {'PASS' if coll_ok else 'FAIL'}")

    # ── A3. at q_0 the gap is exactly zero ────────────────────────────
    print(f"\n  3. at q_0 (h = {H_Q0:.12f}) the gap is zero")
    print(f"     supports: proton {sp_}, neutron {sn}  -> nested: "
          f"{set(sn) <= set(sp_) or set(sp_) <= set(sn)}")
    worst = 0.0
    print(f"     {'atom':6s} {'Z':>2s} {'N':>2s} {'free':>14s} "
          f"{'atom':>14s} {'E_bind':>12s}")
    for lbl, Z, N in ISOTOPES:
        free, atom, g = gap(gram0, cost0, vp0, vn0, Z, N)
        worst = max(worst, abs(g))
        print(f"     {lbl:6s} {Z:2d} {N:2d} {free:14.9f} {atom:14.9f} "
              f"{g:+12.3e}")
    ok = worst < 1e-12
    print(f"     largest |E_bind| over the table = {worst:.3e}  "
          f"(machine epsilon on values of order 10)")
    assertions.append(("A3_gap_exactly_zero_at_q0", ok,
                       f"max |gap| = {worst:.3e} over 10 isotopes"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. there is a window, and q_0 is outside it ──────────────────
    print("\n  4. the mechanism has a window — and q_0 is not in it")
    lo = bisect_edge(0.470, 0.500)
    hi = bisect_edge(0.600, 0.560)
    outside = not (lo < H_Q0 < hi)
    below = 100 * (1 - H_Q0 / lo)
    peak_h, peak_g = max(((0.478 + i * 0.002, gap_at_h(0.478 + i * 0.002))
                          for i in range(46)), key=lambda p: p[1])
    ok = bool(lo < hi and outside and peak_g > 1e-3)
    print(f"     window  h in ({lo:.14f}, {hi:.14f})")
    print(f"             q in ({q_of_h(lo):.14f}, {q_of_h(hi):.14f})")
    print(f"     peak gap {peak_g:.8f} at h = {peak_h:.4f}")
    print(f"     q_0 has h = {H_Q0:.12f}: inside = {not outside}, "
          f"{below:.2f}% below the lower edge")
    assertions.append(("A4_window_exists_and_excludes_q0", ok,
                       f"h in ({lo:.9f}, {hi:.9f}); q_0 is {below:.1f}% below"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. inside the window the law is min(Z,N) * kappa ─────────────
    print("\n  5. inside the window: E_bind = min(Z,N) * kappa, exactly")
    gram_w, cost_w, vp_w, vn_w = build(repr(q_of_h(0.535)))
    kappas, pure_zero = {}, True
    print(f"     {'Z':>2s} {'N':>2s} {'A':>2s} {'E_bind':>13s} "
          f"{'/min(Z,N)':>12s}")
    for Z in range(5):
        for N in range(5):
            if Z + N == 0:
                continue
            _, _, g = gap(gram_w, cost_w, vp_w, vn_w, Z, N)
            g = 0.0 if abs(g) < 1e-12 else g
            m = min(Z, N)
            if m == 0:
                pure_zero &= (g == 0.0)
            else:
                kappas.setdefault(round(g / m, 9), []).append((Z, N))
            if Z <= 2 and N <= 2:
                print(f"     {Z:2d} {N:2d} {Z + N:2d} {g:+13.6e} "
                      f"{('%12.6f' % (g / m)) if m else '         ---'}")
    ks = sorted(kappas)
    spread_k = (max(ks) - min(ks)) / min(ks)
    ok = bool(pure_zero and len(ks) == 2 and spread_k < 0.01)
    print(f"     pure-p and pure-n systems: E_bind = 0 exactly -> {pure_zero}")
    print(f"     distinct kappa values over 0 <= Z,N <= 4: "
          f"{ks}  ({len(ks)} of them, spread {100 * spread_k:.2f}%)")
    print(f"       {kappas[ks[0]][:4]}... all have Z >= N;"
          f" {kappas[ks[1]][:4]}... all have Z < N")
    print(f"     min(Z,N) = (A - |N-Z|)/2, so this is a volume term and an")
    print(f"     asymmetry term locked at ratio 1 — NOT the SEMF, whose")
    print(f"     asymmetry term goes as (N-Z)^2/A rather than |N-Z|.")
    assertions.append(("A5_pairing_law_and_pure_species_zero", ok,
                       f"E_bind/min(Z,N) takes exactly {len(ks)} values "
                       f"{ks} over 0<=Z,N<=4 (spread {100 * spread_k:.2f}%); "
                       f"Z=0 or N=0 gives exactly 0"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the in-window gap is not a solver artefact ────────────────
    print("\n  6. the in-window gap verified three ways")
    vals = {}
    for meth in ("highs", "highs-ds", "highs-ipm"):
        a, _, _ = phi(gram_w, cost_w, vp_w, meth)
        b, _, _ = phi(gram_w, cost_w, vn_w, meth)
        c, _, _ = phi(gram_w, cost_w, vp_w + vn_w, meth)
        vals[meth] = a + b - c
    spread = max(vals.values()) - min(vals.values())
    r_p = linprog(cost_w, A_ub=-gram_w, b_ub=-(gram_w @ vp_w),
                  bounds=[(0, None)] * 6, method="highs")
    r_n = linprog(cost_w, A_ub=-gram_w, b_ub=-(gram_w @ vn_w),
                  bounds=[(0, None)] * 6, method="highs")
    duals_ok = True
    for r, v in ((r_p, vp_w), (r_n, vn_w)):
        y = -r.ineqlin.marginals
        duals_ok &= (bool(np.all(y >= -1e-9))
                     and bool(np.all(gram_w.T @ y <= cost_w + 1e-9))
                     and abs(float(y @ (gram_w @ v)) - float(r.fun)) < 1e-9)
    xw = r_p.x + r_n.x
    aw, _, xa = phi(gram_w, cost_w, vp_w + vn_w)
    cheaper = float(cost_w @ xa) < float(cost_w @ xw) - 1e-6
    ok = bool(spread < 1e-9 and duals_ok and cheaper)
    for meth, g in vals.items():
        print(f"     {meth:<10s} gap = {g:.9f}")
    print(f"     spread across methods = {spread:.2e}")
    print(f"     valid dual certificates (y>=0, G^T y <= t, strong duality): "
          f"{duals_ok}")
    print(f"     explicit witness: cost(x_agg) = {float(cost_w @ xa):.9f} "
          f"< cost(x_p + x_n) = {float(cost_w @ xw):.9f}")
    assertions.append(("A6_in_window_gap_is_real", ok,
                       f"3 methods agree to {spread:.1e}; duals valid; "
                       f"cheaper aggregate point exhibited"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── summary ───────────────────────────────────────────────────────
    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The reformulation works: aggregation gives E_bind >= 0 with")
    print("  nothing fitted, the 6^A blowup collapses to a 6-variable LP, and")
    print("  binding becomes the cone-crossing defect of the LP value")
    print("  function — a finite, decidable question. Inside its window the")
    print("  gap obeys E_bind = min(Z,N)*kappa and vanishes for pure-proton or")
    print("  pure-neutron systems, which is the right qualitative physics from")
    print("  a relaxation rather than a fit.")
    print("  But at q_0 the proton and neutron sit in ONE linearity cone")
    print("  (supports nested), so the gap is an exact algebraic zero for every")
    print("  isotope. The window is h in (0.4772, 0.5698) and q_0 sits 56%")
    print("  below it. So this route does NOT repair the 4He L2 miss.")
    print("  The live question it leaves is the same one the metallic work")
    print("  left: the n-fold form requires an ADDITIVE cost where the corpus")
    print("  uses a multiplicative one. Which functional the physics is")
    print("  supposed to extremise is now blocking from two directions.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="scipy")
        wb.set_description(
            "Reformulates the atom LP as an n-fold integer program (De Loera-"
            "Hemmecke-Onn-Weismantel, math/0605242): free = n separate local "
            "blocks min{t.x_k : G x_k >= G v_k, x_k >= 0}, atom = the same "
            "constraints aggregated into one coupling block. Aggregation is a "
            "relaxation so E_bind = free - atom >= 0 structurally, with "
            "x_p + x_n an explicit aggregate-feasible point of cost exactly "
            "free. The atom program collapses from 6^A to 6 variables "
            "(verified against the explicit block LP at A = 2,3,4), making "
            "binding the cone-crossing defect of the LP value function. At "
            "q_0 the proton and neutron optimal supports are nested ((2,3,4) "
            "and (2,3)), so both lie in one linearity cone and E_bind is an "
            "exact zero (max 5.3e-15 across 2H..16O). The mechanism is real "
            "but windowed: h in (0.47718, 0.56984), peak 0.0687 at h = 0.534, "
            "with q_0 56.2% below the lower edge. Inside the window "
            "E_bind = min(Z,N)*kappa exactly, kappa ~ 0.0696, and zero for "
            "pure-proton or pure-neutron systems. NEGATIVE for the L2 binding "
            "gap: this route does not repair the 4He miss.")
        wb.add_data("h_of_q0", f"{H_Q0:.15f}")
        wb.add_data("supports_at_q0", {"proton": list(sp_), "neutron": list(sn),
                                       "nested": True})
        wb.add_data("max_abs_gap_at_q0", f"{worst:.3e}")
        wb.add_data("window_h", {"lower": f"{lo:.14f}", "upper": f"{hi:.14f}"})
        wb.add_data("window_q", {"lower": f"{q_of_h(lo):.14f}",
                                 "upper": f"{q_of_h(hi):.14f}"})
        wb.add_data("peak", {"h": f"{peak_h:.4f}", "gap": f"{peak_g:.8f}"})
        wb.add_data("q0_below_lower_edge_pct", f"{below:.2f}")
        wb.add_data("kappa_values", [f"{k:.9f}" for k in sorted(kappas)])
        wb.add_data("pairing_law", "E_bind = min(Z,N) * kappa; "
                                   "min(Z,N) = (A - |N-Z|)/2")
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE COST FUNCTIONAL CHANGED. The n-fold form requires an ADDITIVE "
            "cost sum_k t.x_k, where the corpus's atom construction uses the "
            "multiplicative t^(x)A . x. These are different functionals, not "
            "two spellings of one. The Markov trace IS multiplicative on "
            "disjoint strand blocks (h3a_frobenius_gram_offdiagonal_probe), so "
            "the additive cost is its logarithm in spirit but not literally — "
            "log(t.x) is not linear in x, so no exact change of variables "
            "converts one program into the other. The zero reported here is a "
            "zero for the additive-Markov-cost program specifically.")
        wb.add_caveat(
            "The pairing law is NOT the semi-empirical mass formula. "
            "min(Z,N) = (A-|N-Z|)/2 gives a volume term and an asymmetry term "
            "with coefficients locked at ratio 1, and an asymmetry term linear "
            "in |N-Z|; the SEMF's goes as (N-Z)^2/A with an independent "
            "coefficient. The agreement claimed here is qualitative only: "
            "binding proportional to the proton-neutron pair count, and "
            "exactly zero for pure-species systems. Nothing was fitted and no "
            "B_AME value was consulted.")
        wb.add_caveat(
            "THIS IS THE LP RELAXATION, NOT THE IP. Everything measured here "
            "runs scipy.linprog over the continuous relaxation. The n-fold "
            "AGGREGATION structure is fully exercised — it is what produces "
            "the gap, the 6^A collapse and the pairing law — but Theorem "
            "1.1's actual content, poly-time solvability of the INTEGER "
            "program via Graver-basis stabilisation, is untouched. Since the "
            "relaxation collapses to 6 variables it is trivially tractable, so "
            "the entire complexity question lives in the integrality not built "
            "here.")
        wb.add_caveat(
            "Window edges are 50-step bisections on a 1e-9 threshold against a "
            "float64 LP, so the last few digits quoted are the bisection's "
            "precision, not certified algebraic values. The interior gap "
            "(0.0687 at the peak) is 8 orders above the noise floor and is "
            "separately verified by three LP methods, dual certificates, and "
            "an explicit cheaper feasible point; the exact zeros at q_0 are "
            "9 orders below the same floor.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
