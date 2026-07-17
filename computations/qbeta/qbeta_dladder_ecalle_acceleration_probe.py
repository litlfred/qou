#!/usr/bin/env python3
"""qbeta_dladder_ecalle_acceleration_probe.py

Jackson q-Borel / Écalle ACCELERATION machinery for the bar-odd Q_β D-ladder
`D(ũ) = Σ_k d_k ũ^k` (d_k ∈ ℚ(√3), exact) — the odd-channel singularity
locator. Unowned item #1 of the 2026-07-17 1ppQ path reassessment
(docs/audits/2026-07-17-1ppq-path-reassessment.md §"Non-duplicative next-work
options"): with KC22 closing the whole (q-)holonomic class, the one route left
to a c₃ closure is transcendental/resurgent, and the D-ladder is q-Gevrey with
NO single Gevrey index (the 07-13 finding), so the machinery must be q-Borel /
acceleration — NOT plain Borel (the wrong-transform note of
docs/audits/2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md
§"Resummation note").

## Relation to the running "more terms" arm (do not race)

`qbeta_dladder_extension_singularity_probe.py` (running in a separate session)
extends the exact d_k toward k≈31 at ORD 63. THIS probe builds the acceleration
machinery on the COMMITTED order (ORD 43 → d₁…d₂₁) and exposes core functions
that take an **arbitrary-length exact coefficient list** — (a_k, b_k) ∈ ℚ²
pairs for d_k = a_k + b_k√3 — so the extension's k≈31 terms plug in later with
no edits. The ladder is NOT extended here.

## The three arms

  Arm 1 — **Borel–Leroy + conformal dlog-Padé.** b_k = d_k/(k!)^s on a fine s
    grid (0…0.40 step 0.02) bracketing BOTH prior order estimates — the
    root-test slope-zero s* ≈ 0.20 and the log-fit C ≈ 0.06
    (qbeta-dladder-qborel-leroy-resummation.witness.json: the drifting-index
    q-Gevrey signature). At each s the singularity of the transformed series is
    located in the ACCELERATED plane by the conformal-mapped dlog-Padé core of
    the merged even-channel probe
    (computations/probes/qbeta_borel_conformal_pade_probe.py — ζ = 4A₀w/(1+w)²
    uniformizes the cut, dlog turns the branch point into a simple pole,
    margin-held damped fixed point), imported, not reimplemented.

  Arm 2 — **Jackson q-Borel.** The q-Gevrey transform
    b_k = d_k / q₀^{t·k(k−1)/2} for scanned Ramis order t (q₀ the substrate
    value from q-pinning-50-digit.witness.json — the same source the D-ladder
    generator itself reads), same downstream conformal dlog-Padé + gate. This
    is the transform whose suppression profile (q-factorial ~ q^{k²/2}) matches
    a q-Gevrey class, where (k!)^s cannot (the drifting-index problem).

  Arm 3 — **Parity-split acceleration.** Per the exact 2-adic ℤ/2 grading
    (qbeta-dladder-padic-graded-prime.witness.json: v₂(den b_k)=0 ⟺ k odd; 2
    the unique graded prime = the bar-involution prime), the odd-k and even-k
    subseries are accelerated SEPARATELY in the w = ζ² variable, each at its
    own Borel–Leroy order; per-parity singularity estimates are reported plus
    whether they coincide — the bar-parity structure predicts the odd part is
    the S-carrier.

## The ESTIMATOR-CONSISTENCY GATE (pre-stated, tol 15%)

The 07-13 Leroy scan located ρ_dlog ≈ 0.156 vs root-test radius ≈ 0.32 at
s*, k=21 — a 2× estimator gap, honestly reported as "not resolved". This probe
makes that honesty structural: a singularity is reported as LOCATED only when
the conformal dlog-Padé radius and the root-test radius agree to within the
PRE-STATED tolerance |ρ_dlog/ρ_rt − 1| < 0.15, with ≥ 2 independent (L,M,μ)
conformal configs converged. No gate pass ⇒ no location claim, at any (s,t).

## Pre-stated kill criteria

  K1 — the gate fails at every (s, t) on the committed terms ⇒ verdict
    "finite-k shadow persists at ORD 43 (k=21); machinery ready for the
    extension's terms". Scope-(a): a statement about k=21 resolution power,
    NOT a refutation of resummability or of any singularity candidate.
  K2 — the parity-split estimates diverge from each other beyond tolerance ⇒
    reported as STRUCTURE (the ℤ/2 grading acting on the Borel plane), not as
    failure.

## Candidate comparison (pre-named, no fit)

IFF the gate passes somewhere, the located ρ is compared against PRE-NAMED
candidates only: Vol(4₁)/π, Vol(4₁), π²/6, the substrate u = b·ℏ_q² (= 1/117.4,
computed exactly from q₀ — the KC21 extractor scale), ũ(q₀) = q₀·u (the ladder
variable's substrate value), and the KC21-capstone S-scales |S(muon)| =
0.00968298, the Φ_b volume deficit 0.0094, and t·κ₁ = 0.058
(docs/audits/2026-07-12-c3-wall-resolution-capstone.md). Consistent-within-
spread wording ONLY; no identification claims. NO instanton action is claimed
unless the gate passes; no c_k wired; no fit to QOU observables; no tier
change.

## In-script assertions

  1. exact d_k reproduction: the generator output at ORD 43 matches the
     committed qbeta-dladder-generating-function-structure.witness.json
     (a_k, b_k) strings for every k = 1…21, exactly (ℚ equality);
  2. transform sanity: s = 0 (and t = 0) reproduce the raw series exactly;
  3. gate arithmetic spot-check: the prior 0.156-vs-0.32 pair must FAIL the
     gate arithmetic; a 0.30-vs-0.32 pair must pass it; and the full gate
     machinery (conformal dlog-Padé + root test) must PASS on a synthetic
     branch-point series c_k = √k·2^k (= Li₋₁/₂(2ζ), known singularity at
     ρ₀ = 1/2; a pure geometric would make the high-order Padé Hankel system
     exactly singular, so the branch-type synthetic is the honest plumbing
     test).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import json  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

# COMMITTED order — the extension arm (separate session) owns ORD 63 / k≈31.
ORD = 43
core.ORD = ORD
# The generating-function module reads its ORD from sys.argv at import time;
# pin it explicitly so this probe is deterministic regardless of invocation.
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402

# Conformal-map + dlog-Padé core (merged even-channel probe) — imported, not
# reimplemented: pade / clean_poles / mapped_series / conformal_iterate.
import qbeta_borel_conformal_pade_probe as cpade  # noqa: E402

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
R3 = sp.sqrt(3)

GATE_TOL = mp.mpf("0.15")     # pre-stated estimator-consistency tolerance
PARITY_TOL = mp.mpf("0.25")   # per-parity coincidence tolerance (10-term series)
S_GRID = [mp.mpf(i) / 50 for i in range(0, 21)]      # s = 0.00 … 0.40 step 0.02
T_GRID = [mp.mpf(i) / 20 for i in range(0, 11)]      # t = 0.00 … 0.50 step 0.05
CONFIGS_GRID = [(7, 7, mp.mpf("1.5")), (8, 8, mp.mpf("2.0")), (9, 9, mp.mpf("1.5"))]
CONFIGS_HEADLINE = [(L, M, mu) for (L, M) in [(6, 6), (7, 7), (8, 8), (9, 9)]
                    for mu in (mp.mpf("1.5"), mp.mpf("2.0"))]
CONFIGS_PARITY_ODD = [(3, 3, mp.mpf("1.5")), (4, 4, mp.mpf("2.0")), (4, 5, mp.mpf("1.5"))]
CONFIGS_PARITY_EVEN = [(3, 3, mp.mpf("1.5")), (4, 4, mp.mpf("2.0"))]

# Pre-named KC21-capstone S-scales (docs/audits/2026-07-12-c3-wall-resolution-
# capstone.md results 1 & 5) — fixed BEFORE any singularity is located.
S_MUON_ABS = mp.mpf("0.00968298")
VOL_DEFICIT = mp.mpf("0.0094")
T_KAPPA1 = mp.mpf("0.058")


# ---------------------------------------------------------------------------
# exact-coefficient API — arbitrary-length (a_k, b_k) ∈ ℚ² pair lists
# ---------------------------------------------------------------------------
def load_exact_dk_pairs():
    """Build the exact D-ladder at the committed ORD and return the canonical
    exact representation: pairs[k] = (a_k, b_k) with d_k = a_k + b_k√3,
    a_k, b_k ∈ ℚ (sympy Rational); pairs[0] = (0, 0). Any-length lists in the
    same shape (e.g. the extension arm's k≈31 output) plug into every core
    function below."""
    dk, KMAX, _vt, odd_ok = dlad.build_d_ladder()
    pairs = [(sp.Integer(0), sp.Integer(0))]
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        pairs.append((sp.Rational(e.coeff(R3, 0)), sp.Rational(e.coeff(R3, 1))))
    return pairs, KMAX, odd_ok


def pairs_to_mpf(pairs):
    """Evaluate exact (a, b) pairs to mpf at working dps: d_k = a_k + b_k√3."""
    s3 = mp.sqrt(3)
    out = []
    for (a, b) in pairs:
        out.append(mp.mpf(int(a.p)) / int(a.q) + (mp.mpf(int(b.p)) / int(b.q)) * s3)
    return out


def borel_leroy(d, s):
    """Borel–Leroy transform of order s: b_k = d_k / (k!)^s (any length)."""
    return [d[0]] + [d[k] / mp.factorial(k) ** s for k in range(1, len(d))]


def jackson_qborel(d, q0, t):
    """Jackson q-Borel (Ramis q-Gevrey order t): b_k = d_k / q0^{t·k(k−1)/2}."""
    return [d[0]] + [d[k] / q0 ** (t * mp.mpf(k * (k - 1)) / 2)
                     for k in range(1, len(d))]


def parity_split_pairs(pairs):
    """Split exact pairs into the odd / even k subseries in the w = ζ² plane:
    odd_w[j] = d_{2j+1} (j ≥ 0), even_w[j] = d_{2j} (j ≥ 1, index 0 = (0,0))."""
    odd_w = [pairs[k] for k in range(1, len(pairs), 2)]
    even_w = [(sp.Integer(0), sp.Integer(0))] + [pairs[k]
                                                 for k in range(2, len(pairs), 2)]
    return odd_w, even_w


# ---------------------------------------------------------------------------
# estimators + the gate
# ---------------------------------------------------------------------------
def root_test_radius(vals, ks, tail=5):
    """1 / mean of |c_k|^{1/k} over the last `tail` indices (the extension
    probe's convention). vals indexed by position matching ks."""
    pick = list(zip(ks, vals))[-tail:]
    rt = [abs(v) ** (mp.mpf(1) / k) for (k, v) in pick]
    return 1 / (mp.fsum(rt) / len(rt))


def root_test_slope(vals, ks):
    """Least-squares slope of |c_k|^{1/k} vs k (rising ⇒ divergent)."""
    xs = list(ks)
    ys = [abs(v) ** (mp.mpf(1) / k) for (k, v) in zip(ks, vals)]
    n = len(xs)
    sx = mp.fsum(xs); sy = mp.fsum(ys)
    sxx = mp.fsum(x * x for x in xs)
    sxy = mp.fsum(x * y for x, y in zip(xs, ys))
    return (n * sxy - sx * sy) / (n * sxx - sx * sx)


def slope_zero_bisect(transform, lo, hi, ks_for_slope, iters=36):
    """Bisect the transform order for root-test slope = 0 (the s*/t* locator).
    `transform(order)` returns the full transformed list b (b[0] ignored)."""
    def slope_at(x):
        b = transform(x)
        return root_test_slope([b[k] for k in ks_for_slope], ks_for_slope)
    lo, hi = mp.mpf(lo), mp.mpf(hi)
    if slope_at(lo) <= 0:
        return lo
    if slope_at(hi) >= 0:
        return None  # never flattens on the scanned range
    for _ in range(iters):
        mid = (lo + hi) / 2
        if slope_at(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def gate_eval(fc, rho_rt, configs, max_iter=60):
    """The estimator-consistency gate in the accelerated plane.

    fc — coefficient list of a function f with f(0) = fc[0] ≠ 0 whose
    singularity set equals the transformed series' (for a series with b_0 = 0
    pass fc[n] = b_{n+1}, i.e. f = B(ζ)/ζ). Runs the conformal dlog-Padé core
    seeded at the root-test radius across `configs`; the gate PASSES iff ≥ 2
    configs converge AND |ρ_dlog/ρ_rt − 1| < GATE_TOL."""
    As, details = [], {}
    for (L, M, mu) in configs:
        if L + M + 1 > len(fc) - 1:
            details[f"[{L}/{M}],mu={mp.nstr(mu, 3)}"] = {"skipped": "too few terms"}
            continue
        r = cpade.conformal_iterate(fc, L, M, rho_rt, mu, use_dlog=True,
                                    max_iter=max_iter)
        tag = f"[{L}/{M}],mu={mp.nstr(mu, 3)}"
        if r.get("converged"):
            As.append(r["A"])
            details[tag] = {"A": mp.nstr(r["A"], 10), "iters": r["iters"]}
        else:
            details[tag] = {"converged": False, "why": r.get("why", "?")}
    if not As:
        return {"rho_rt": rho_rt, "rho_dlog": None, "gap": None, "spread": None,
                "n_conv": 0, "gate": False, "details": details}
    rho = mp.fsum(As) / len(As)
    gap = abs(rho / rho_rt - 1)
    spread = ((max(As) - min(As)) / rho) if len(As) > 1 else mp.mpf(0)
    return {"rho_rt": rho_rt, "rho_dlog": rho, "rho_min": min(As),
            "rho_max": max(As), "gap": gap, "spread": spread,
            "n_conv": len(As), "gate": bool(gap < GATE_TOL and len(As) >= 2),
            "details": details}


def gate_on_series(b, configs, kmin=1):
    """Gate a transformed series with b[0] = 0 (full-ladder arms 1-2)."""
    ks = list(range(kmin, len(b)))
    rho_rt = root_test_radius([b[k] for k in ks], ks)
    fc = [b[k] for k in range(1, len(b))]     # f = B(ζ)/ζ, fc[0] = b_1 ≠ 0
    return gate_eval(fc, rho_rt, configs)


def gate_to_json(g):
    """Stringify the mpf fields of a gate_eval result for the witness."""
    if not g:
        return None
    out = {}
    for k, v in g.items():
        if v is None or isinstance(v, (bool, int, str, dict)):
            out[k] = v
        else:
            out[k] = mp.nstr(v, 10)
    return out


# ---------------------------------------------------------------------------
def load_q0():
    """Substrate q₀ from the canonical 50-digit pinning witness — the same
    source the D-ladder generator itself reads."""
    w = json.load(open(_pb.witness_path("q-pinning-50-digit.witness.json", HERE)))
    return mp.mpf(w["derived_50_digit"]["q"])


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" D-ladder Jackson q-Borel / Écalle acceleration — odd-channel locator")
    print(f" committed ORD = {ORD} (k ≤ 21); gate tol = {mp.nstr(GATE_TOL, 3)}")
    print("=" * 78)

    # ---- exact ladder + reproduction assertion ----------------------------
    print("building exact D-ladder at committed ORD (symbolic; ~1-2 min) ...",
          flush=True)
    pairs, KMAX, odd_ok = load_exact_dk_pairs()
    print(f"  d_1..d_{KMAX} exact; over-determination zero: {odd_ok} "
          f"({time.monotonic() - t0:.0f}s)", flush=True)

    wgen = json.load(open(_pb.witness_path(
        "qbeta-dladder-generating-function-structure.witness.json", HERE)))
    repro_ok = (wgen["data"]["ORD"] == ORD and wgen["data"]["n_terms"] == KMAX)
    for k in range(1, KMAX + 1):
        wa = sp.Rational(wgen["data"]["a_k_rational"][str(k)])
        wb_ = sp.Rational(wgen["data"]["b_k_sqrt3_coeff"][str(k)])
        repro_ok = repro_ok and (pairs[k][0] == wa) and (pairs[k][1] == wb_)
    print(f"  exact d_k reproduce the committed witness (k=1..{KMAX}): {repro_ok}")

    d = pairs_to_mpf(pairs)
    q0 = load_q0()
    q0_ok = mp.nstr(q0, 6).startswith("1.1099")
    print(f"  substrate q0 = {mp.nstr(q0, 12)} (prefix ok: {q0_ok})")

    # ---- transform sanity: zero order reproduces the raw series -----------
    bl0 = borel_leroy(d, mp.mpf(0))
    qb0 = jackson_qborel(d, q0, mp.mpf(0))
    sanity_ok = all(bl0[k] == d[k] and qb0[k] == d[k] for k in range(len(d)))
    print(f"  transform sanity (s=0 and t=0 reproduce raw d_k): {sanity_ok}")

    # ---- gate arithmetic spot-checks --------------------------------------
    gap_prior = abs(mp.mpf("0.156") / mp.mpf("0.32") - 1)     # the 07-13 pair
    gap_close = abs(mp.mpf("0.30") / mp.mpf("0.32") - 1)
    arith_ok = (gap_prior > GATE_TOL) and (gap_close < GATE_TOL)
    # Branch-point synthetic c_k = sqrt(k)*2^k (Li_{-1/2}(2*zeta)), rho = 1/2.
    syn = [mp.mpf(0)] + [mp.sqrt(k) * mp.mpf(2) ** k for k in range(1, 22)]
    g_syn = gate_on_series(syn, CONFIGS_GRID)
    syn_ok = bool(g_syn["gate"] and g_syn["rho_dlog"] is not None
                  and abs(g_syn["rho_dlog"] - mp.mpf("0.5")) < mp.mpf("0.02"))
    gate_check_ok = arith_ok and syn_ok
    print(f"  gate arithmetic: prior 0.156/0.32 gap={mp.nstr(gap_prior, 3)} FAILS, "
          f"0.30/0.32 gap={mp.nstr(gap_close, 3)} passes: {arith_ok}")
    print(f"  synthetic branch point (rho=0.5): located "
          f"{mp.nstr(g_syn['rho_dlog'], 8) if g_syn['rho_dlog'] else 'none'}, "
          f"rho_rt={mp.nstr(g_syn['rho_rt'], 6)}, gate={g_syn['gate']}: {syn_ok}")

    # ---- Arm 1: Borel–Leroy scan + conformal dlog-Padé gate ---------------
    print(f"\n== Arm 1: Borel–Leroy s-scan ({len(S_GRID)} pts, "
          f"3 conformal configs each) ==", flush=True)
    ks_slope = list(range(8, KMAX + 1))
    arm1_rows, arm1_pass = [], []
    for i, s in enumerate(S_GRID):
        b = borel_leroy(d, s)
        slope = root_test_slope([b[k] for k in ks_slope], ks_slope)
        g = gate_on_series(b, CONFIGS_GRID)
        arm1_rows.append({
            "s": float(s), "root_slope": mp.nstr(slope, 6),
            "rho_rt": mp.nstr(g["rho_rt"], 8),
            "rho_dlog": (mp.nstr(g["rho_dlog"], 8) if g["rho_dlog"] else None),
            "gap": (mp.nstr(g["gap"], 4) if g["gap"] is not None else None),
            "n_conv": g["n_conv"], "gate": g["gate"],
        })
        if g["gate"]:
            arm1_pass.append((s, g))
        el = time.monotonic() - t0
        eta = el / (i + 1) * (len(S_GRID) - i - 1)
        print(f"  s={float(s):.2f}: slope={mp.nstr(slope, 4):>10}  "
              f"rho_rt={mp.nstr(g['rho_rt'], 6):>9}  "
              f"rho_dlog={mp.nstr(g['rho_dlog'], 6) if g['rho_dlog'] else 'none':>9}  "
              f"gap={mp.nstr(g['gap'], 3) if g['gap'] is not None else 'n/a':>6}  "
              f"conv={g['n_conv']}  gate={'PASS' if g['gate'] else 'fail'}  "
              f"[{el:.0f}s, eta {eta:.0f}s]", flush=True)

    s_star = slope_zero_bisect(lambda s: borel_leroy(d, s), 0, 1, ks_slope)
    g_sstar = (gate_on_series(borel_leroy(d, s_star), CONFIGS_HEADLINE)
               if s_star is not None else None)
    print(f"  s* (slope-zero) = {mp.nstr(s_star, 6) if s_star is not None else 'none'}; "
          f"headline 8-config gate at s*: "
          f"{'PASS' if (g_sstar and g_sstar['gate']) else 'fail'}"
          + (f"  rho_dlog={mp.nstr(g_sstar['rho_dlog'], 8)} vs "
             f"rho_rt={mp.nstr(g_sstar['rho_rt'], 8)} "
             f"(gap {mp.nstr(g_sstar['gap'], 3)}, conv {g_sstar['n_conv']})"
             if g_sstar and g_sstar["rho_dlog"] else ""), flush=True)

    # ---- Arm 2: Jackson q-Borel scan --------------------------------------
    print(f"\n== Arm 2: Jackson q-Borel t-scan ({len(T_GRID)} pts) ==", flush=True)
    arm2_rows, arm2_pass = [], []
    for i, t in enumerate(T_GRID):
        b = jackson_qborel(d, q0, t)
        slope = root_test_slope([b[k] for k in ks_slope], ks_slope)
        g = gate_on_series(b, CONFIGS_GRID)
        arm2_rows.append({
            "t": float(t), "root_slope": mp.nstr(slope, 6),
            "rho_rt": mp.nstr(g["rho_rt"], 8),
            "rho_dlog": (mp.nstr(g["rho_dlog"], 8) if g["rho_dlog"] else None),
            "gap": (mp.nstr(g["gap"], 4) if g["gap"] is not None else None),
            "n_conv": g["n_conv"], "gate": g["gate"],
        })
        if g["gate"]:
            arm2_pass.append((t, g))
        el = time.monotonic() - t0
        print(f"  t={float(t):.2f}: slope={mp.nstr(slope, 4):>10}  "
              f"rho_rt={mp.nstr(g['rho_rt'], 6):>9}  "
              f"rho_dlog={mp.nstr(g['rho_dlog'], 6) if g['rho_dlog'] else 'none':>9}  "
              f"gap={mp.nstr(g['gap'], 3) if g['gap'] is not None else 'n/a':>6}  "
              f"conv={g['n_conv']}  gate={'PASS' if g['gate'] else 'fail'}  "
              f"[{el:.0f}s]", flush=True)

    t_star = slope_zero_bisect(lambda t: jackson_qborel(d, q0, t), 0, 2, ks_slope)
    g_tstar = (gate_on_series(jackson_qborel(d, q0, t_star), CONFIGS_HEADLINE)
               if t_star is not None else None)
    print(f"  t* (slope-zero) = {mp.nstr(t_star, 6) if t_star is not None else 'none'}; "
          f"headline 8-config gate at t*: "
          f"{'PASS' if (g_tstar and g_tstar['gate']) else 'fail'}"
          + (f"  rho_dlog={mp.nstr(g_tstar['rho_dlog'], 8)} vs "
             f"rho_rt={mp.nstr(g_tstar['rho_rt'], 8)} "
             f"(gap {mp.nstr(g_tstar['gap'], 3)}, conv {g_tstar['n_conv']})"
             if g_tstar and g_tstar["rho_dlog"] else ""), flush=True)

    # ---- Arm 3: parity-split acceleration in w = ζ² -----------------------
    print("\n== Arm 3: parity-split acceleration (w = ζ² plane; 2-adic ℤ/2 "
          "grading) ==", flush=True)
    odd_pairs, even_pairs = parity_split_pairs(pairs)
    odd_w = pairs_to_mpf(odd_pairs)        # odd_w[j] = d_{2j+1}, j = 0..10
    even_w = pairs_to_mpf(even_pairs)      # even_w[j] = d_{2j},  j = 1..10
    parity = {}
    for name, coefs, cfgs in (("odd", odd_w, CONFIGS_PARITY_ODD),
                              ("even", even_w, CONFIGS_PARITY_EVEN)):
        jmax = len(coefs) - 1
        js = list(range(3, jmax + 1))
        if name == "odd":
            def tr(s, c=coefs):
                return [c[j] / mp.factorial(j) ** s if j else c[0]
                        for j in range(len(c))]
        else:
            def tr(s, c=coefs):
                return [mp.mpf(0)] + [c[j] / mp.factorial(j) ** s
                                      for j in range(1, len(c))]
        s_par = slope_zero_bisect(tr, 0, mp.mpf("1.5"), js)
        if s_par is None:
            parity[name] = {"s_star": None, "gate": False,
                            "note": "root-test never flattens on s ≤ 1.5"}
            print(f"  {name}: no slope-zero order found (s ≤ 1.5)")
            continue
        b = tr(s_par)
        rho_rt_w = root_test_radius([b[j] for j in range(1, len(b))],
                                    list(range(1, len(b))))
        fc = ([b[j] for j in range(len(b))] if name == "odd" and b[0] != 0
              else [b[j] for j in range(1, len(b))])
        g = gate_eval(fc, rho_rt_w, cfgs, max_iter=60)
        rho_zeta = (mp.sqrt(g["rho_dlog"]) if g["rho_dlog"] else None)
        parity[name] = {
            "s_star": mp.nstr(s_par, 6),
            "rho_rt_w": mp.nstr(rho_rt_w, 8),
            "rho_dlog_w": (mp.nstr(g["rho_dlog"], 8) if g["rho_dlog"] else None),
            "rho_zeta": (mp.nstr(rho_zeta, 8) if rho_zeta else None),
            "gap": (mp.nstr(g["gap"], 4) if g["gap"] is not None else None),
            "n_conv": g["n_conv"], "gate": g["gate"], "_rho_zeta_mp": rho_zeta,
        }
        print(f"  {name}: s*_par={mp.nstr(s_par, 4)}  rho_rt(w)={mp.nstr(rho_rt_w, 6)}  "
              f"rho_dlog(w)={mp.nstr(g['rho_dlog'], 6) if g['rho_dlog'] else 'none'}  "
              f"gap={mp.nstr(g['gap'], 3) if g['gap'] is not None else 'n/a'}  "
              f"gate={'PASS' if g['gate'] else 'fail'}"
              f"  → rho_zeta={mp.nstr(rho_zeta, 6) if rho_zeta else 'n/a'}",
              flush=True)

    par_coincide = None
    if parity.get("odd", {}).get("_rho_zeta_mp") and \
       parity.get("even", {}).get("_rho_zeta_mp"):
        ro, re_ = parity["odd"]["_rho_zeta_mp"], parity["even"]["_rho_zeta_mp"]
        par_gap = abs(ro / re_ - 1)
        par_coincide = bool(par_gap < PARITY_TOL)
        print(f"  parity coincidence |rho_odd/rho_even - 1| = {mp.nstr(par_gap, 4)} "
              f"(tol {mp.nstr(PARITY_TOL, 3)}): "
              f"{'COINCIDE' if par_coincide else 'DIVERGE (K2: structure, not failure)'}")
    for v in parity.values():
        v.pop("_rho_zeta_mp", None)

    # ---- candidate comparison (only if the gate passed anywhere) ----------
    u_sub = (mp.sqrt(q0 ** 4 + q0 ** 2 + 1) / (q0 ** 2 + 1)) * ((q0 - 1) / q0) ** 2
    Vol41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    candidates = {
        "Vol(4_1)/pi": Vol41 / mp.pi,
        "Vol(4_1)": Vol41,
        "pi^2/6": mp.pi ** 2 / 6,
        "u_substrate=b*hbar_q^2": u_sub,
        "u_tilde_substrate=q0*u": q0 * u_sub,
        "abs_S_muon_KC21": S_MUON_ABS,
        "phib_volume_deficit_KC21": VOL_DEFICIT,
        "t_kappa1_KC21": T_KAPPA1,
    }
    gate_rhos = ([g["rho_dlog"] for (_x, g) in arm1_pass + arm2_pass] +
                 ([g_sstar["rho_dlog"]] if g_sstar and g_sstar["gate"] else []) +
                 ([g_tstar["rho_dlog"]] if g_tstar and g_tstar["gate"] else []))
    any_gate = bool(gate_rhos)
    cand_report = {}
    consistent = []
    if any_gate:
        r_lo, r_hi = min(gate_rhos), max(gate_rhos)
        r_mean = mp.fsum(gate_rhos) / len(gate_rhos)
        print(f"\n== Candidates vs gate-passing rho in "
              f"[{mp.nstr(r_lo, 8)}, {mp.nstr(r_hi, 8)}] ==")
        for name, val in candidates.items():
            inside = bool(r_lo * (1 - GATE_TOL) <= val <= r_hi * (1 + GATE_TOL))
            cand_report[name] = {"value": mp.nstr(val, 10),
                                 "rel_to_mean": mp.nstr(abs(r_mean / val - 1), 4),
                                 "consistent_within_spread": inside}
            if inside:
                consistent.append(name)
            print(f"  {name:28s} = {mp.nstr(val, 8):>12}  "
                  f"{'consistent-within-spread' if inside else 'not matched'}")
    else:
        print("\n== Candidates: NOT compared (gate failed everywhere; per the "
              "pre-stated rule no singularity is reported as located) ==")
        for name, val in candidates.items():
            cand_report[name] = {"value": mp.nstr(val, 10),
                                 "consistent_within_spread": None}

    # ---- verdict ----------------------------------------------------------
    if any_gate:
        verdict = (
            f"GATE PASSED at {len(gate_rhos)} accelerated configuration(s): the "
            f"conformal dlog-Padé and root-test radii agree within "
            f"{mp.nstr(GATE_TOL, 3)}; located singularity rho in "
            f"[{mp.nstr(min(gate_rhos), 8)}, {mp.nstr(max(gate_rhos), 8)}] "
            f"(accelerated-plane location; measurement, not identification"
            + (f"; consistent-within-spread: {', '.join(consistent)}"
               if consistent else "; no pre-named candidate inside the spread")
            + "). No instanton action wired; no c_k wired; no tier change.")
    else:
        verdict = (
            f"K1: the estimator-consistency gate (tol {mp.nstr(GATE_TOL, 3)}) "
            f"fails at every Borel–Leroy order s ≤ 0.40, every Jackson q-Borel "
            f"order t ≤ 0.50, and at s*/t* with the 8-config headline set — the "
            f"finite-k shadow persists at the committed ORD {ORD} (k = {KMAX}). "
            "Scope-(a): a statement about k=21 resolution power, NOT a "
            "refutation of resummability or of any singularity candidate. The "
            "machinery (exact-pair API, both transforms, the gate) is ready for "
            "the extension arm's k≈31 terms.")
    if par_coincide is False:
        verdict += (" K2: the parity-split estimates diverge beyond "
                    f"{mp.nstr(PARITY_TOL, 3)} — recorded as bar-parity ℤ/2 "
                    "structure acting on the Borel plane (the odd part as the "
                    "S-carrier), not as failure.")
    elif par_coincide is True:
        verdict += " Parity-split estimates coincide within tolerance."
    print(f"\nVERDICT: {verdict}")
    print(f"total {time.monotonic() - t0:.0f}s")

    # ---- witness ----------------------------------------------------------
    wb = WitnessBuilder("qbeta-dladder-ecalle-acceleration", engine="mpmath")
    wb.set_description(
        "Jackson q-Borel / Ecalle acceleration machinery for the bar-odd Q_beta "
        "D-ladder (odd-channel singularity locator; unowned item #1 of the "
        "2026-07-17 1ppQ reassessment). Arm 1: Borel-Leroy s-scan + conformal "
        "dlog-Pade (core imported from the merged even-channel probe) with a "
        "pre-stated 15% estimator-consistency gate (dlog-Pade vs root-test "
        "radius) — the honest fix for the prior 0.156-vs-0.32 gap. Arm 2: "
        "Jackson q-Borel b_k = d_k/q0^{t k(k-1)/2} at substrate q0, same gate. "
        "Arm 3: parity-split acceleration in w = zeta^2 per the 2-adic Z/2 "
        "grading. Exact d_k at committed ORD 43 (k<=21); core API takes "
        "any-length exact (a_k, b_k) pairs so the extension arm's k~31 terms "
        "plug in. Scope-(a); no instanton action claimed without the gate; no "
        "c_k wired; no fit; no tier change.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_parameter("ORD_committed", ORD)
    wb.add_parameter("KMAX", KMAX)
    wb.add_parameter("gate_tolerance", float(GATE_TOL))
    wb.add_parameter("parity_tolerance", float(PARITY_TOL))
    wb.add_parameter("q0", mp.nstr(q0, 50))
    wb.add_data("arm1_borel_leroy_scan", arm1_rows)
    wb.add_data("arm1_s_star", mp.nstr(s_star, 8) if s_star is not None else None)
    wb.add_data("arm1_headline_gate_at_s_star", gate_to_json(g_sstar))
    wb.add_data("arm2_jackson_qborel_scan", arm2_rows)
    wb.add_data("arm2_t_star", mp.nstr(t_star, 8) if t_star is not None else None)
    wb.add_data("arm2_headline_gate_at_t_star", gate_to_json(g_tstar))
    wb.add_data("arm3_parity_split", parity)
    wb.add_data("arm3_parity_coincide", par_coincide)
    wb.add_data("gate_passed_anywhere", any_gate)
    wb.add_data("candidates_pre_named", cand_report)
    wb.add_data("consistent_within_spread", consistent)
    wb.add_data("verdict", verdict)
    wb.add_caveat(
        "The gate-pass rho values are accelerated-plane singularity locations "
        "(transform-order dependent); consistent-within-spread wording only, "
        "no identification claims, no instanton action wired.")
    wb.add_caveat(
        "Committed-order run (ORD 43, k<=21) — the ORD-63 / k~31 extension is "
        "the running sibling arm; rerun this probe on its exact pairs when it "
        "lands (the core API is any-length).")
    wb.add_assertion("exact_dk_reproduce_committed_witness", bool(repro_ok), True,
                     source="all 21 (a_k, b_k) pairs equal the committed "
                            "qbeta-dladder-generating-function-structure witness "
                            "strings, exact Q equality, plus over-determination "
                            f"zero ({odd_ok})")
    wb.add_assertion("transform_sanity_zero_order_identity", bool(sanity_ok), True,
                     source="borel_leroy(d, 0) and jackson_qborel(d, q0, 0) "
                            "reproduce the raw series elementwise, exactly")
    wb.add_assertion("gate_arithmetic_spot_check", bool(gate_check_ok), True,
                     source="prior 0.156-vs-0.32 pair fails the 15% gate "
                            "(gap 0.51); 0.30-vs-0.32 passes (gap 0.0625); full "
                            "gate machinery locates the synthetic branch-point "
                            "(Li_{-1/2}(2 zeta)) singularity rho=0.5 within 2% "
                            "and passes")
    wb.add_assertion("q0_prefix_sanity", bool(q0_ok), True,
                     source="q0 from q-pinning-50-digit.witness.json starts 1.1099")
    out = wb.save()
    print(f"witness -> {out}")
    return 0 if (repro_ok and sanity_ok and gate_check_ok and q0_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
