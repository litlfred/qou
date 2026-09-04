#!/usr/bin/env python3
"""The two-nucleon sector is not mis-parameterised, it is UNREACHABLE: the bond
trace ratio is exactly `mu(d) = z + d`, affine in `d`, and the physical
bound/unbound pattern is non-monotonic in `d`.

WHAT IS BEING CHECKED
---------------------
Nature binds **one** of the three two-nucleon systems:

    pp  (diproton)    UNBOUND
    pn  (deuteron)    BOUND, 2.2245 MeV
    nn  (dineutron)   UNBOUND

This construction binds **all three** — and in the worst possible order.
Measured here from the same machinery the rest of the arc uses, with
`L = -log(mu)` and `L > 0` meaning bound:

    bond   d               mu = z + d     L
    pp     0.0000000000    0.612688037    0.4898993843    BOUND
    pn    -0.1044582478    0.508229789    0.6768215924    BOUND
    nn    -0.2090602988    0.403627738    0.9072622655    BOUND

`L_nn > L_pn > L_pp`: **the model makes the dineutron the most bound of the
three.** That is not a small quantitative miss; it is the wrong answer to the
simplest question the theory can be asked, and everything at higher `A` is built
out of these same bonds.

WHY NO PARAMETER CHOICE FIXES IT
--------------------------------
A bond is `(1, d)` with `d = -beta h` and `beta in [0,1]`, so `d in [-h, 0]` and
`d <= 0` always. Hence

    mu  =  z + d  <=  z  =  0.612688037  <  1     =>   L = -log(mu) > 0

**every single crossing binds, structurally.** Unbinding needs `mu > 1`, i.e.
`z > 1`, i.e. `q^3 > q^2 + 1` — threshold at the supergolden ratio
`q* = 1.4655712318767680`, and `q0 = 1.1099785828` sits `24.3 %` below it. No
choice of `beta`, colour convention, framing, or writhe normalisation moves this,
because every one of them only moves `d`.

THE IMPOSSIBILITY
-----------------
Stronger than "the numbers are off". Measured: `mu(d) = z + d` **exactly** —
slope `1` with spread `5.3e-15`, and `|mu(d) - (z+d)| <= 8.9e-16` (machine
epsilon) using the exact Wenzl `r = 2` weights — independent of which nucleons
sit at the ends. Routed through `load_cost` instead it is `3.1e-9`, which is
that path's documented stored-f64 floor rather than a defect. It is affine
because the bond crossing occurs exactly once, so
`tr(W(M + dI)) = tr(WM) + d tr(W)`; and the constant is the **Markov parameter**
`z` itself.

Nature requires, with bound `<=> mu < 1`:

    mu(d_pp = 0)  > 1        and      mu(d_nn = -h) > 1
    but            mu(d_pn)  < 1      for an interior d_pn

so `{d : mu(d) > 1}` must contain **both endpoints** of `[-h, 0]` while
**excluding an interior point**. For an affine `mu` that set is a half-line. It
cannot. **Therefore no assignment of bond offsets — in any Wedderburn block, or
any weighted combination of them — reproduces the physical pattern.**

This is the uncomfortable part: affineness in `d` is not an accident of the
parameterisation. `z` is the Markov parameter, the very thing that makes this
trace a link invariant. The property that makes the construction topological is
the same property that forbids the two-nucleon pattern.

UNBINDING DOES EXIST IN THE ALGEBRA — WITH THE WRONG PATTERN
------------------------------------------------------------
Per-block `mu_lambda` on the four live `H_6` blocks is not uniformly `< 1`:

    block     dim       y       mu_pp      mu_pn      mu_nn
    (3,3)      5    0.015124   0.370566   0.431211   0.457700
    (4,2)      9    0.046032   0.208466   0.398117   0.035035
    (5,1)      5    0.078953  -0.276707  -0.944701  -1.500687   <- NEGATIVE
    (6,)       1    0.115324   1.109979   1.005520   0.900918   <- >1 twice

The trivial block gives `mu = q + d` exactly (`q0`, `q0 + D_PN`, `1/q0`), so it
**does** unbind `pp` and `pn` — but binds `nn`, which is the wrong pattern, and
it is still affine in `d`, so it is subject to the same impossibility. And the
`(5,1)` block has a **negative** ratio, so per-block "binding" is not even
well-defined there; only the total is physical.

WHAT NATURE ACTUALLY GRADES BY
------------------------------
The `NN` scattering lengths say the distinction is not flavour at all:

    a_pp(1S0)  = -17.3      unbound
    a_nn(1S0)  = -18.9      unbound
    a_np(1S0)  = -23.740    unbound     <- np is ALSO unbound in 1S0
    a_np(3S1)  =  +5.419    BOUND       <- the only bound channel

**All three `T = 1` states are unbound.** The single bound two-nucleon state is
the `T = 0` spin-triplet, which only `np` can form because Pauli forbids it for
`pp` and `nn`. So the flavour pair is the wrong label; `(T, S)` is the right one,
and a construction that assigns one scalar per flavour pair is answering a
question nature does not ask.

THE THREE ESCAPE ROUTES, AND WHICH IS LIVE
------------------------------------------
* **(a) More than one crossing per bond.** `mu` becomes polynomial in `d` of
  degree = the crossing count, and degree `>= 2` can be non-monotone. This is the
  minimal structural change that removes the impossibility.
* **(b) A grading that selects a different OPERATOR per channel**, not a
  different offset — genuine `(T, S)` labels. The `n = 2` Wedderburn split
  `mu_+/mu_-` is already the symmetric/antisymmetric decomposition, so the
  labels exist; nothing currently uses them to choose an operator.
* **(c) `q > 1.4656`.** Excluded: `q0` is fixed by other physics and sits `24.3 %`
  below.

(a) and (b) are both live and are not exclusive. (c) is closed.

DISCIPLINE
----------
No fit; nothing wired. Every number is measured with the same seminormal
machinery as the rest of the arc; `mu = z + d` is verified numerically rather
than assumed. Scattering lengths are quoted as an external comparison target and
nothing is tuned to them.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] the_alpha_spike_is_an_inverted_stagger_probe.py (same gap, A>=3)
-- Ref: [data] CD-Bonn NN scattering lengths, Machleidt nucl-th/0006014 Tbl. XI
"""
from __future__ import annotations

import sys
import warnings
from math import comb
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
import scipy.sparse as sps  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from pyhecke.atom import D_PN  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
_Zp = _Q ** 3 / (_Q ** 2 + 1)
HF, DPN, ZF = float(_H), float(D_PN), float(_Zp)
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
BONDS = {"pp": 0.0, "pn": DPN, "nn": -HF}
NATURE = {"pp": ("UNBOUND", "diproton"), "pn": ("bound", "deuteron 2.2245 MeV"),
          "nn": ("UNBOUND", "dineutron")}
SCATT = [("a_pp(1S0)", -17.3, "unbound"), ("a_nn(1S0)", -18.9, "unbound"),
         ("a_np(1S0)", -23.740, "unbound"), ("a_np(3S1)", +5.419, "BOUND")]


def nucleon_word(betas, g0, g1):
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -betas[0] * HF, g0), (1, -betas[1] * HF, g0),
          (1, -betas[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def main() -> int:
    assertions = []
    print("t7qv — the two-nucleon pattern is unreachable, not mis-fitted")

    parts, y, _c, _d, _m = load_cost("deuteron")
    live = [(tuple(p), float(w)) for p, w in zip(parts, y)
            if abs(float(w)) > 1e-30]
    BLK = {p: (w, [sps.csr_matrix(m, dtype=float)
                   for m in build_seminormal_matrices(list(p))[0]])
           for p, w in live}

    def blocktr(p, word):
        _w, S = BLK[p]
        n = S[0].shape[0]
        M = sps.identity(n, format="csr")
        for c, dd, g in word:
            M = M @ (c * S[g] + dd * sps.identity(n, format="csr"))
        return float(M.diagonal().sum())

    def pair_words(fl, d=None):
        base = (nucleon_word(B_P if fl[0] == "p" else B_N, 0, 1)
                + nucleon_word(B_P if fl[1] == "p" else B_N, 3, 4))
        return base if d is None else base + [(1, d, 2)]

    def qint(m):
        return sum(_Q ** (m - 1 - 2 * i) for i in range(m))

    # exact Wenzl r=2 weights: y_(n-k,k) ~ [n-2k+1]_q, normalised sum(y.dim)=1
    def exact_weights(n=6):
        ks = list(range(n // 2 + 1))
        ps = [((n - k, k) if k else (n,)) for k in ks]
        dims = [comb(n, k) - comb(n, k - 1) if k else 1 for k in ks]
        raw = [qint(n - 2 * k + 1) for k in ks]
        Z = sum(r * dd for r, dd in zip(raw, dims))
        return {pp: float(r / Z) for pp, r in zip(ps, raw)}

    YEX = exact_weights()

    def mu_total(fl, d, exact=False):
        a = b = 0.0
        for p, w in live:
            ww = YEX[p] if exact else w
            a += ww * blocktr(p, pair_words(fl, d))
            b += ww * blocktr(p, pair_words(fl))
        return a / b

    # ── A1. all three bind, and in the worst order ─────────────────────
    print("\n  1. the model binds all three two-nucleon systems")
    print(f"     {'bond':<5s} {'d':>14s} {'mu':>12s} {'L':>14s} "
          f"{'model':>8s}   nature")
    L = {}
    for k, d in BONDS.items():
        mu = ZF + d
        L[k] = -np.log(mu)
        print(f"     {k:<5s} {d:14.10f} {mu:12.9f} {L[k]:14.10f} "
              f"{'BOUND':>8s}   {NATURE[k][0]:<8s} ({NATURE[k][1]})")
    order = sorted(L, key=lambda k: -L[k])
    ok = all(v > 0 for v in L.values()) and order[0] == "nn"
    print(f"     model ordering by binding: {' > '.join(order)}")
    print(f"     nature binds 1 of 3; the model binds 3 of 3, and makes the")
    print(f"     DINEUTRON the most bound. Everything at higher A is built out")
    print(f"     of these same bonds.")
    assertions.append(("A1_model_binds_all_three_dineutron_most", ok,
                       f"L_pp {L['pp']:.6f}, L_pn {L['pn']:.6f}, "
                       f"L_nn {L['nn']:.6f}; all > 0, nn largest"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. it is structural, not parametric ───────────────────────────
    print("\n  2. no parameter choice can unbind a single crossing")
    qs = float(mp.findroot(lambda q: q ** 3 - q ** 2 - 1, mp.mpf("1.5")))
    print(f"     d = -beta h with beta in [0,1] => d in [{-HF:.6f}, 0], d <= 0")
    print(f"     so mu = z + d <= z = {ZF:.9f} < 1, so L > 0 ALWAYS")
    print(f"     unbinding needs z > 1, i.e. q^3 > q^2 + 1")
    print(f"     threshold q* = {qs:.16f} (supergolden ratio)")
    print(f"     q0 = {float(_Q):.10f}, which is {100 * (1 - float(_Q) / qs):.1f} % below")
    print(f"     beta, colour convention, framing and writhe all only move d.")
    ok = ZF < 1 and float(_Q) < qs and abs(qs ** 3 - qs ** 2 - 1) < 1e-12
    assertions.append(("A2_binding_is_structural_not_parametric", ok,
                       f"z = {ZF:.9f} < 1 with d <= 0; threshold q* = {qs:.12f}, "
                       f"q0 is {100 * (1 - float(_Q) / qs):.1f}% below"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. mu(d) = z + d exactly, and flavour-blind ───────────────────
    print("\n  3. mu(d) is EXACTLY z + d — affine, and independent of flavour")
    ds = [0.0, -0.05, -0.1, -0.15, -HF]
    slopes, devs, devs_lc = [], [], []
    for fl in ("pp", "pn", "nn"):
        vex = [mu_total(fl, d, exact=True) for d in ds]
        vlc = [mu_total(fl, d) for d in ds]
        sl = [(vex[i + 1] - vex[i]) / (ds[i + 1] - ds[i])
              for i in range(len(ds) - 1)]
        slopes += sl
        devs.append(max(abs(v - (ZF + d)) for v, d in zip(vex, ds)))
        devs_lc.append(max(abs(v - (ZF + d)) for v, d in zip(vlc, ds)))
        print(f"     {fl}: mu(0) = {vex[0]:.12f}   |mu(d)-(z+d)| exact-y "
              f"{devs[-1]:.2e}   load_cost-y {devs_lc[-1]:.2e}")
    spread = max(slopes) - min(slopes)
    ok = spread < 1e-12 and max(devs) < 1e-12 and abs(np.mean(slopes) - 1) < 1e-12
    print(f"     slope is 1 across all flavours, spread {spread:.2e}")
    print(f"     with the EXACT Wenzl r=2 weights mu(d) = z + d to "
          f"{max(devs):.1e} (machine epsilon); routed through load_cost it is")
    print(f"     {max(devs_lc):.1e}, which is that path's documented stored-f64")
    print(f"     floor, not a defect — the identity is exact.")
    print(f"     affine because the bond crossing occurs exactly once:")
    print(f"     tr(W(M + dI)) = tr(WM) + d tr(W). And the constant is z, the")
    print(f"     MARKOV PARAMETER — the same object that makes this trace a")
    print(f"     link invariant.")
    assertions.append(("A3_mu_is_exactly_z_plus_d", ok,
                       f"slope 1 to {spread:.1e}; |mu-(z+d)| <= {max(devs):.1e} "
                       f"with exact weights ({max(devs_lc):.1e} via load_cost, "
                       f"its f64 floor); flavour-independent"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. the impossibility ──────────────────────────────────────────
    print("\n  4. THE IMPOSSIBILITY")
    need_hi = [0.0, -HF]
    need_lo = DPN
    viol = [d for d in need_hi if (ZF + d) > 1]
    print(f"     nature requires (bound <=> mu < 1):")
    print(f"       mu(d_pp = {0.0:.4f})  > 1   diproton  UNBOUND")
    print(f"       mu(d_pn = {DPN:.4f}) < 1   deuteron  BOUND")
    print(f"       mu(d_nn = {-HF:.4f}) > 1   dineutron UNBOUND")
    print(f"     so the set {{d : mu(d) > 1}} must contain BOTH endpoints of")
    print(f"     [{-HF:.4f}, 0] and EXCLUDE the interior point {DPN:.4f}.")
    print(f"     mu is affine, so that set is a HALF-LINE. It cannot.")
    print(f"     => no assignment of offsets d, in any Wedderburn block or any")
    print(f"        weighted combination, reproduces the physical pattern.")
    print(f"     (currently neither endpoint even exceeds 1: {len(viol)}/2)")
    print(f"     Affineness is not an accident of the parameterisation — the")
    print(f"     constant IS the Markov parameter. The property that makes the")
    print(f"     construction topological is what forbids the physics.")
    ok = len(viol) == 0 and (ZF + DPN) < 1
    assertions.append(("A4_physical_pattern_needs_a_non_monotone_mu", ok,
                       "affine mu has half-line superlevel sets; the pattern "
                       "needs both endpoints above 1 and an interior point "
                       "below"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. unbinding exists per block, with the wrong pattern ─────────
    print("\n  5. unbinding DOES exist in the algebra — wrongly patterned")
    print(f"     {'block':<8s} {'dim':>4s} {'y':>10s} {'mu_pp':>11s} "
          f"{'mu_pn':>11s} {'mu_nn':>11s}")
    unb, neg = [], []
    triv = {}
    for p, w in live:
        dim = BLK[p][1][0].shape[0]
        row = f"     {str(p):<8s} {dim:4d} {w:10.6f}"
        for k, dd in BONDS.items():
            m = blocktr(p, pair_words(k, dd)) / blocktr(p, pair_words(k))
            if m > 1:
                unb.append((p, k))
            if m < 0:
                neg.append((p, k))
            if p == (6,):
                triv[k] = m
            row += f" {m:11.6f}"
        print(row)
    tq = abs(triv["pp"] - float(_Q)) < 1e-9
    ok = len(unb) >= 2 and len(neg) >= 1 and tq
    print(f"     the trivial block (6,) gives mu = q + d exactly "
          f"(mu_pp = q0 to {abs(triv['pp'] - float(_Q)):.1e}), so it DOES")
    print(f"     unbind pp and pn — but binds nn, the wrong pattern, and it is")
    print(f"     still affine in d so the same impossibility applies.")
    print(f"     the (5,1) block has NEGATIVE ratios, so per-block 'binding' is")
    print(f"     not well defined there; only the total is physical.")
    assertions.append(("A5_unbinding_exists_but_wrongly_patterned", ok,
                       f"{len(unb)} block/flavour pairs unbind, {len(neg)} have "
                       f"negative ratio; trivial block = q + d"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. what nature actually grades by ─────────────────────────────
    print("\n  6. nature grades by (T, S), not by flavour pair")
    for name, a, st in SCATT:
        print(f"     {name:<12s} {a:+9.3f} fm   {st}")
    t1 = [s for n, a, s in SCATT if "1S0" in n]
    t0 = [s for n, a, s in SCATT if "3S1" in n]
    ok = all(s == "unbound" for s in t1) and t0 == ["BOUND"]
    print(f"     ALL THREE T=1 (1S0) states are unbound, including np. The one")
    print(f"     bound two-nucleon state is the T=0 spin-triplet, which only np")
    print(f"     can form — Pauli forbids it for pp and nn. So the flavour pair")
    print(f"     is the wrong label and a construction assigning one scalar per")
    print(f"     flavour pair is answering a question nature does not ask.")
    print(f"     ESCAPES: (a) >1 crossing per bond makes mu polynomial in d, so")
    print(f"     degree >= 2 can be non-monotone; (b) grade by (T,S), selecting")
    print(f"     a different OPERATOR per channel rather than a different offset")
    print(f"     — the n=2 Wedderburn split IS the sym/antisym decomposition, so")
    print(f"     the labels already exist and nothing uses them; (c) q > q* is")
    print(f"     closed. (a) and (b) are live and not exclusive.")
    assertions.append(("A6_nature_grades_by_T_and_S_not_flavour", ok,
                       "all three 1S0 (T=1) states unbound; only the T=0 3S1 "
                       "np state is bound"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The two-nucleon sector is not mis-parameterised, it is unreachable.")
    print("  The bond trace ratio is exactly mu(d) = z + d — affine, slope 1,")
    print("  flavour-blind — while the physical pattern (pp and nn unbound, pn")
    print("  bound) is non-monotone in d. An affine function's superlevel set is")
    print("  a half-line, so NO offset assignment in any block or combination")
    print("  can produce it. Conventions only move d, so none of them help.")
    print("  And the affineness is not incidental: the constant is the Markov")
    print("  parameter, so the property making this a link invariant is the same")
    print("  one forbidding the physics.")
    print("  Nature's own grading says why: all three T=1 states are unbound and")
    print("  the single bound state is the T=0 spin-triplet, which only np can")
    print("  form. Flavour pair is the wrong label. The live fixes are more than")
    print("  one crossing per bond, or a (T,S) grading that selects an operator")
    print("  rather than an offset; raising q past the supergolden threshold is")
    print("  closed at 24.3 %.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="numpy")
        wb.set_description(
            "Establishes that the two-nucleon sector is unreachable rather than "
            "mis-fitted. Measured with the arc's standard seminormal machinery, "
            "the model binds all three two-nucleon systems (L_pp 0.4899, L_pn "
            "0.6768, L_nn 0.9073, all > 0) where nature binds only the "
            "deuteron, and it makes the DINEUTRON the most bound. This is "
            "structural: a bond is (1, d) with d = -beta h and beta in [0,1], "
            "so d <= 0 and mu = z + d <= z = 0.6127 < 1 always; unbinding needs "
            "q^3 > q^2 + 1, threshold at the supergolden ratio 1.4655712318767680 "
            "with q0 24.3% below. THE IMPOSSIBILITY: mu(d) = z + d exactly — "
            "slope 1 to 4.4e-15, independent of flavour, affine because the bond "
            "crossing occurs once — while the physical pattern needs {d : mu(d) "
            "> 1} to contain both endpoints of [-h, 0] and exclude an interior "
            "point. An affine function's superlevel set is a half-line, so no "
            "offset assignment in any Wedderburn block or weighted combination "
            "reproduces it, and every convention (framing, writhe, colour "
            "weighting) only moves d. The affineness is not incidental: the "
            "constant is the Markov parameter, so the property making the trace "
            "a link invariant is the same one forbidding the pattern. Unbinding "
            "does exist per block — the trivial block gives mu = q + d exactly "
            "and unbinds pp and pn — but binds nn, the wrong pattern, and the "
            "(5,1) block has negative ratios so per-block binding is not well "
            "defined. Nature grades by (T,S): all three T=1 (1S0) states are "
            "unbound including np, and the single bound state is the T=0 "
            "spin-triplet that only np can form.")
        wb.add_data("two_body_bonds",
                    {k: {"d": f"{BONDS[k]:.12f}", "mu": f"{ZF + BONDS[k]:.12f}",
                         "L": f"{L[k]:.12f}", "model": "BOUND",
                         "nature": NATURE[k][0]} for k in BONDS})
        wb.add_data("structural_bound",
                    {"z": f"{ZF:.12f}", "h": f"{HF:.12f}",
                     "supergolden_threshold": f"{qs:.16f}",
                     "q0": f"{float(_Q):.16f}",
                     "pct_below_threshold": f"{100 * (1 - float(_Q) / qs):.2f}"})
        wb.add_data("affineness",
                    {"slope_spread": f"{spread:.3e}",
                     "max_dev_from_z_plus_d": f"{max(devs):.3e}",
                     "max_dev_via_load_cost_f64_floor": f"{max(devs_lc):.3e}",
                     "mean_slope": f"{float(np.mean(slopes)):.12f}"})
        wb.add_data("per_block",
                    {str(p): {k: f"{blocktr(p, pair_words(k, dd)) / blocktr(p, pair_words(k)):.9f}"
                              for k, dd in BONDS.items()} for p, _w in live})
        wb.add_data("scattering_lengths_fm",
                    {n: {"a_fm": f"{a:+.3f}", "state": s} for n, a, s in SCATT})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE IMPOSSIBILITY IS SCOPED TO A SINGLE-CROSSING BOND WITH A REAL "
            "OFFSET. That is what the current construction uses, so the "
            "conclusion applies to it as built and to every convention variant "
            "of it. It does NOT say the substrate cannot describe the two-"
            "nucleon sector at all: escape (a), more than one crossing per bond, "
            "makes mu polynomial in d of degree equal to the crossing count and "
            "removes the obstruction immediately. Neither escape is attempted "
            "here.")
        wb.add_caveat(
            "'BOUND' IS READ AS mu < 1, i.e. L > 0, which is the arc's own "
            "convention for binding throughout. It is a sign convention on a "
            "dimensionless trace ratio, not a physical energy, and the arc has "
            "repeatedly found the magnitudes to be orders off. The claim here "
            "is about SIGN and ORDERING, which is where the convention is "
            "meaningful, and no magnitude is asserted.")
        wb.add_caveat(
            "The scattering lengths are an external comparison target quoted "
            "from CD-Bonn / experiment (Machleidt nucl-th/0006014 Tbl. XI). "
            "Nothing here is fitted or tuned to them; they are used only to "
            "establish WHICH quantum numbers nature's bound/unbound split "
            "follows. As of this probe the corpus's reference set contains no "
            "NN partial-wave data at all, so this is an import, not a "
            "citation of existing corpus material.")
        wb.add_caveat(
            "Per-block ratios are reported for structure, not as physical "
            "channel binding energies. The (5,1) block's ratio is negative, so "
            "-log of it is undefined; only the y-weighted total is a Markov "
            "trace and only it carries the link-invariance that the rest of the "
            "arc relies on.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
