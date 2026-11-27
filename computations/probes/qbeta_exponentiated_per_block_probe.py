#!/usr/bin/env python3
"""qbeta_exponentiated_per_block_probe.py — PROBE 6a: the EXPONENTIATED
per-block decomposition (U1), the never-run PR #1585 queue item 2.

QUESTION (docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md
§1 U1 + §3.G). C13 (PR #2465, `habiro_mode_to_ladder_bridge.py`) refuted the
LINEAR / bar-even Δtr_M-seeded f: seed `1 + N·Σ_k G_k u_L^k` with the scale N
fixing c_2 = −1 gives a constant c_3 ≈ −1.4…−1.5, far from the empirical
c_3 ≈ −2.01 (muon) / −2.07 (proton). U1 asks: does the EXPONENTIATED
per-block seeding

    F = exp( N · Σ_λ g_λ(u_L) ),   λ ∈ {(3), (2,1), (1,1,1)},  UNIFORM N

do better? Here g_λ is the even-in-ℏ_q (integer-u_L ladder) part of the
per-Wedderburn-block Δtr_M closed form (paper closed forms, PR #1764 /
`qbeta-per-block-paper-closed-forms.witness.json`; leading ε-coefficients
−2 / −1 / −2 per `qbeta_multiblock_order_audit.py`, PR #1593). The change
of variable is the C13 bridge's: u_L = b·ℏ_q², ℏ_q = (q−1)/q, so
q = 1/(1−ℏ); even-in-ℏ coefficients a_{2k} feed integer rungs G_k =
a_{2k}/b^k; odd-in-ℏ coefficients are the half-integer bar-odd remainder
(excluded, exactly as in C13).

NON-TRIVIALITY CHECK (verified before writing this probe): the per-block
sum Σ_λ f_λ(q) is NOT proportional to the atomic Δtr_M(√q) used by C13 —
their ratio is q-dependent (equals 4 only at q = 1). The per-block object
is the y_λ-rational-surrogate Δτ_M (PR #1764, non-canonical y_λ), so this
probe genuinely tests different seed data as well as a different (exp vs
linear) functional form.

STRUCTURAL FACTS the probe also records (independent of the numbers):
  1. With UNIFORM weights, exp(N·Σ_λ g_λ) = exp(N·g_total) — the per-block
     structure collapses; it could only matter with per-block weights,
     which would be a fit (forbidden).
  2. When the seed starts at k = 2 (ladder convention: no c_1 rung),
     log[exp(N·Σ_{k≥2} G_k u^k)] = N·Σ G_k u^k exactly, and
     log[1 + N·Σ_{k≥2} G_k u^k] agrees with it through u³. So the
     exponentiated and linear seedings of the SAME data share c_2 and c_3
     identically; exponentiation first differentiates at c_4 (by +½·c_2²).
     U1's exp-vs-linear distinction is therefore a c_4-and-higher effect.

NORMALIZATION (mirrors C13 exactly): the single scale d.o.f. N is fixed by
c_2 = −1 (the one PROVED rung, Lean `N2_factor`); c_3, c_4 are then read
off with product-form bookkeeping (log ∏(1+c_k u^k) = Σ[c_k u^k − ½c_k²u^{2k}
+ …] ⇒ c_2 = L_2, c_3 = L_3, c_4 = L_4 + ½L_2²).

KILL CRITERION (pre-stated in the task, before running):
  • anchor-CONSTANT and far from empirical (the C13 failure mode), OR
    anchor-unstable in the wrong direction  ⇒ verdict NEGATIVE — extend
    C13 to "exponentiated per-block seeding also refuted", scope-limited
    (a) per AGENTS.md §Before declaring "refuted".
  • within ~1% of empirical at BOTH anchors ⇒ GATE-PASSED near-match
    (report only; no wiring, no derivation claim).

DISCIPLINE: exact sympy symbolics for all series; mpmath 60 dps for the
final numerics; no fitting (uniform weights, one scale d.o.f. = c_2);
TIERED reporting; no production wiring; witness JSON per the
qbeta_root_of_unity_probe.py pattern.
"""

import json
import os
import subprocess
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp

mp.mp.dps = 60

HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.dirname(HERE)

# ---------------------------------------------------------------------------
# Anchors (two documented q₀ pins — AGENTS.md §q₀ anchor convention)
# ---------------------------------------------------------------------------
# Proton pin: live from the qou-substrate package (task instruction).
import sys
sys.path.insert(0, os.path.join(os.path.dirname(COMP), "tools", "qou-substrate", "python"))
# `q_parameter` lives in computations/substrate/ (bean qou-9ugp); the anchor
# must be read from it so the witness resolves its stamp. Idempotent.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from qou_substrate.witness import apply_q0_comparison  # noqa: E402

# Both pins read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). The
# muon leg was the literal 1.1099785955573... -- the RETIRED self-certified
# pin A, superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. A
# mu-vs-p comparison whose muon leg is a retired literal compares live proton
# against yesterday's muon, which is the failure it exists to measure.
# Exception E1 of the 2026-08-30 ruling: both pins are read here on purpose.
# The proton leg additionally had a silent `except` fallback to a hand-typed
# copy of the same value. Same number today, and a second place for it to go
# stale; a pin that cannot be established is an error, not a default.
Q0_PROTON = Q_MP
Q0_MUON = q_muon_at(50)

# Empirical c_3 targets (registry ≈ −2.02 muon / −2.07 proton):
#   proton: qbeta_root_of_unity_probe.py / c3-rigidity audit (proton-pinned)
#   muon:   extracted AT this file's own Q0_MUON (:85) — see below
#
# 🛑 THE MUON VALUE WAS -2.0097 (corrected 2026-08-29, bean `qou-t39x`), taken
# from `qbeta_multiblock_order_audit.py C3_EMP_MUON` per the old comment here.
# Two things were wrong with that provenance:
#
#   1. -2.0097 is the pre-#1422 value and matches NO anchor now in use.
#   2. The file it was copied from defines `Q0_MUON_PIN = Q_50_DIGIT_STR`,
#      which is the PROTON pin — so it could not have been a muon readout.
#
# There is no single "muon c_3". Re-running c_3 = (Q_codata/Q_N2 - 1)/u^3:
#
#     frozen pin  (…5557…)   -2.02018813   <- this file's Q0_MUON
#     CODATA-2018 (…5554…)   -2.02020024
#     CODATA-2022 (…5642…)   -2.01986031
#
# `Q0_MUON` above is 1.10997859555733471…, the frozen pin, so the value below is
# the one extracted there. Verified by reproducing the corpus PROTON value
# -2.06934257712 to 12 digits with the same routine.
C3_EMP_PROTON = mp.mpf("-2.06934257711516783787971951725")
C3_EMP_MUON = mp.mpf("-2.02018812814")

# Exactness tolerance for the c_2 = -1 assertion. An mpf, not the bare `1e-35`
# float literal it replaces — the literal was serialized into the witness as a
# raw float64.
C2_TOL = mp.mpf("1e-35")

# C13 reference values (habiro-mode-to-ladder-bridge.witness.json) for the
# extends-C13 comparison: linear seed of the ATOMIC Δtr_M even-in-ℏ data.
C13_C3_NUM = mp.mpf("-1.49691695322654196968759384677")  # = -100/(77b)

ORDER_H = 12          # ℏ-series depth → integer rungs up to u_L^5
K_MAX = 5             # highest ladder rung peeled (c_2..c_4 reported)


def b_of_q0(q0: mp.mpf) -> mp.mpf:
    """Hoefsmit ladder constant b(q₀): b² = (h²+3)/(h²+4), h = q₀ − 1/q₀."""
    h = q0 - 1 / q0
    return mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))


def main():
    print("=" * 74)
    print(" PROBE 6a (U1) — EXPONENTIATED per-block Δtr_M seeding of the Q_β f")
    print("=" * 74)

    q = sp.Symbol("q", positive=True)
    hbar = sp.Symbol("hbar")
    b = sp.Symbol("b", positive=True)
    uL = sp.Symbol("u_L", positive=True)
    Nrm = sp.Symbol("N")

    # ---- 1. load the per-block closed forms (reuse, do not re-derive) ----
    wpath = os.path.join(COMP, "qbeta", "qbeta-per-block-paper-closed-forms.witness.json")
    w = json.load(open(wpath))
    forms = {lam: sp.sympify(expr, locals={"q": q})
             for lam, expr in w["data"]["paper_closed_forms"].items()}
    blocks = ["(3)", "(2,1)", "(1,1,1)"]
    print("\n  Per-block Δtr_M closed forms f_λ(q) "
          "(qbeta-per-block-paper-closed-forms.witness.json):")
    for blk in blocks:
        print(f"    {blk:>8s}: {forms[blk]}")

    # sanity: leading ε-coefficients must be −2 / −1 / −2 (PR #1593)
    eps = sp.Symbol("eps")
    lead = {}
    for blk in blocks:
        ser = sp.expand(sp.series(forms[blk].subs(q, 1 + eps), eps, 0, 3).removeO())
        lp = min(m[0] for m in sp.Poly(ser, eps).monoms())
        lead[blk] = sp.nsimplify(ser.coeff(eps, lp))
    lead_ok = (lead["(3)"] == -2 and lead["(2,1)"] == -1 and lead["(1,1,1)"] == -2)
    print(f"\n  sanity — leading ε-coefficients (−2/−1/−2 expected): "
          f"{[str(lead[b_]) for b_ in blocks]}  →  {'PASS' if lead_ok else 'FAIL'}")

    # ---- 2. per-block ℏ-series; even-in-ℏ = integer-u_L ladder data ------
    # q = 1/(1−ℏ)  (ℏ_q = (q−1)/q inverted), exactly as the C13 bridge.
    q_of_h = 1 / (1 - hbar)
    a_blk: dict[str, dict[int, sp.Rational]] = {}
    print(f"\n  ℏ_q-Taylor series per block (q = 1/(1−ℏ)), to ℏ^{ORDER_H - 1}:")
    for blk in blocks:
        ser = sp.expand(sp.series(forms[blk].subs(q, q_of_h), hbar, 0, ORDER_H).removeO())
        a_blk[blk] = {n: sp.nsimplify(ser.coeff(hbar, n)) for n in range(ORDER_H)}
        even = {n: v for n, v in a_blk[blk].items() if n % 2 == 0 and v != 0}
        odd1 = a_blk[blk].get(1, 0)
        print(f"    {blk:>8s}: a_1 = {odd1} (bar-odd, excluded);  even "
              + "  ".join(f"a_{n}={v}" for n, v in sorted(even.items())))

    # totals (uniform weights ⇒ only the sum enters the exponent)
    a_tot = {n: sum(a_blk[blk][n] for blk in blocks) for n in range(ORDER_H)}
    print("\n  Uniform-weight total (Σ_λ):  "
          + "  ".join(f"a_{n}={a_tot[n]}" for n in range(ORDER_H) if a_tot[n] != 0))

    # integer-ladder data G_k = a_{2k}/b^k  (b symbolic; C13 convention)
    G = {k: a_tot[2 * k] / b ** k for k in range(0, ORDER_H // 2)}
    print("\n  Integer-ladder G_k = a_2k/b^k (uniform per-block sum):")
    for k in range(2, K_MAX + 1):
        print(f"    G_{k} = {G[k]}")

    # ---- 3. EXPONENTIATED seed, scale fixed ONLY by c_2 = −1 -------------
    #   F = exp(N·Σ_{k≥2} G_k u_L^k)   ⇒   log F = N·Σ G_k u_L^k exactly.
    logF = sp.expand(Nrm * sum(G[k] * uL ** k for k in range(2, K_MAX + 1)))
    L = {k: sp.expand(logF).coeff(uL, k) for k in range(2, K_MAX + 1)}
    Nsol = sp.solve(sp.Eq(L[2], -1), Nrm)
    if not Nsol:
        raise SystemExit("scale-fix c_2 = −1 unsolvable — G_2 vanished")
    Nval = Nsol[0]
    # product-form bookkeeping: log ∏(1+c_k u^k) = Σ[c_k u^k − ½c_k² u^{2k} + …]
    c_sym = {
        2: sp.simplify(L[2].subs(Nrm, Nval)),
        3: sp.simplify(L[3].subs(Nrm, Nval)),
        4: sp.simplify((L[4] + sp.Rational(1, 2) * L[2] ** 2).subs(Nrm, Nval)),
    }
    print(f"\n  Scale fix c_2 = −1  ⇒  N = {Nval}")
    print("  Peeled ladder coefficients (symbolic in b):")
    for k in (2, 3, 4):
        print(f"    c_{k} = {c_sym[k]}")

    # structural identity: linear seed of the SAME data shares c_3
    seed_lin = sp.expand(1 + Nrm * sum(G[k] * uL ** k for k in range(2, K_MAX + 1)))
    log_lin = sp.expand(sp.series(sp.log(seed_lin), uL, 0, K_MAX + 1).removeO())
    Llin = {k: log_lin.coeff(uL, k) for k in range(2, K_MAX + 1)}
    Nlin = sp.solve(sp.Eq(Llin[2], -1), Nrm)[0]
    c3_lin = sp.simplify(Llin[3].subs(Nrm, Nlin))
    c4_lin = sp.simplify((Llin[4] + sp.Rational(1, 2) * Llin[2] ** 2).subs(Nrm, Nlin))
    c3_same = sp.simplify(c3_lin - c_sym[3]) == 0
    c4_shift = sp.simplify(c_sym[4] - c4_lin)
    print(f"\n  exp-vs-linear seeding of the same data: c_3 identical: {c3_same}; "
          f"c_4(exp) − c_4(linear) = {c4_shift}")

    # ---- 4. numerics at BOTH anchors (60 dps) ----------------------------
    results = {}
    print("\n  " + "-" * 70)
    print("  Numeric c_k at the two anchors (b = b(q₀); 60 dps):")
    for tag, q0 in (("proton", Q0_PROTON), ("muon", Q0_MUON)):
        bval = b_of_q0(q0)
        b_sp = sp.Float(mp.nstr(bval, 55), 55)
        cnum = {k: mp.mpf(str(sp.N(c_sym[k].subs(b, b_sp), 40))) for k in (2, 3, 4)}
        results[tag] = {"q0": q0, "b": bval, "c": cnum}
        print(f"    [{tag:6s}] q₀ = {mp.nstr(q0, 20)}   b = {mp.nstr(bval, 20)}")
        for k in (2, 3, 4):
            print(f"             c_{k} = {mp.nstr(cnum[k], 25)}")

    c3_p, c3_m = results["proton"]["c"][3], results["muon"]["c"][3]
    err_p = abs((c3_p - C3_EMP_PROTON) / C3_EMP_PROTON)
    err_m = abs((c3_m - C3_EMP_MUON) / C3_EMP_MUON)
    pred_swing = abs((c3_p - c3_m) / c3_p)
    emp_swing = abs((C3_EMP_PROTON - C3_EMP_MUON) / C3_EMP_PROTON)
    print("\n  Predicted vs empirical c_3:")
    print(f"    proton:  pred {mp.nstr(c3_p, 20)}   emp {mp.nstr(C3_EMP_PROTON, 20)}"
          f"   |rel err| = {float(err_p) * 100:.2f}%")
    print(f"    muon:    pred {mp.nstr(c3_m, 20)}   emp {mp.nstr(C3_EMP_MUON, 20)}"
          f"   |rel err| = {float(err_m) * 100:.2f}%")
    print(f"    predicted cross-anchor swing: {mp.nstr(pred_swing, 8)} "
          f"({float(pred_swing) * 100:.2e}%)   empirical swing: "
          f"{float(emp_swing) * 100:.2f}%")
    # mpf comparisons, not float64 ones (AGENTS.md §PROBES ARE NOT EXEMPT: a
    # `float(x)` outside an f-string is a computation, not a display).
    anchor_constant = pred_swing < mp.mpf("1e-4")  # ≪ the empirical swing
    within_1pct_both = err_p < mp.mpf("0.01") and err_m < mp.mpf("0.01")
    # The empirical swing, spelled once and interpolated everywhere below. It
    # was hardcoded "2.9%" at three sites — the pre-#1422 stale-c_3 figure,
    # which no longer matched the value this very function computes two lines
    # up (2.38%). Deriving it means the number cannot go stale again.
    emp_swing_pct = f"{mp.nstr(emp_swing * 100, 3)}%"
    print(f"    ⇒ prediction is anchor-{'CONSTANT' if anchor_constant else 'VARYING'} "
          f"(C13's was anchor-constant)")

    # C13 comparison (extends-C13 framing)
    d_c13 = abs((c3_p - C13_C3_NUM) / C13_C3_NUM)
    print(f"\n  vs C13 linear-atomic seed c_3 = {mp.nstr(C13_C3_NUM, 20)}: "
          f"rel diff {float(d_c13) * 100:.2f}% (different seed data, same regime)")

    # ---- 5. verdict per the pre-stated kill criterion --------------------
    if within_1pct_both:
        overall = "GATE-PASSED (near-match — report only; no wiring)"
    else:
        overall = "NEGATIVE"
    summary = (
        f"Exponentiated per-block seeding (U1) gives c_3 ≈ {mp.nstr(c3_p, 8)} at both "
        f"anchors — anchor-constant (swing {float(pred_swing):.1e} vs empirical "
        f"{emp_swing_pct}) and "
        f"{float(err_p) * 100:.1f}% (proton) / {float(err_m) * 100:.1f}% (muon) from the "
        "empirical c_3 — exactly the C13 failure mode. Two structural collapses make this "
        "unsurprising: (i) uniform weights collapse exp(Σ_λ g_λ) to exp(g_total); "
        "(ii) with the ladder-convention seed starting at u_L², the exponentiated and "
        "linear seedings share c_3 identically — exponentiation only moves c_4 (by +½). "
        "Scope-limited refutation (a): the exponentiated per-block Δtr_M seeding, ALONE "
        "and with uniform weights, does not reproduce c_3; it does not exclude per-block "
        "data inside a non-linear or non-uniform closure (which would need a derived, "
        "not fitted, weight rule). Extends C13: 'linear / bar-even' → 'linear, bar-even, "
        "AND exponentiated-uniform' Δtr_M-seeded f all refuted."
    ) if overall == "NEGATIVE" else (
        "Within 1% of empirical c_3 at both anchors — gate-passed near-match; "
        "report only, no wiring, no derivation claim."
    )
    print("\n" + "=" * 74)
    print(f"  VERDICT: {overall}")
    print(f"  {summary}")

    # ---- witness emission (qbeta_root_of_unity_probe.py pattern) ---------
    out = {
        "engine": "mpmath+sympy",
        "engineVersion": f"mpmath {mp.__version__}; sympy {sp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-exponentiated-per-block",
        "scriptFile": "qbeta_exponentiated_per_block_probe.py",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            check=True).stdout.strip(),
        "description": (
            "PROBE 6a (U1, PR #1585 queue item 2, never previously run): seeds the "
            "Q_beta scaling map as F = exp(N*Sum_lambda g_lambda(u_L)) with the "
            "per-Wedderburn-block Delta tr_M closed forms (paper closed forms, "
            "PR #1764; leading eps-coefficients -2/-1/-2), even-in-hbar projection "
            "onto the integer u_L = b*hbar_q^2 ladder (C13 bridge change of variable), "
            "UNIFORM weights, scale fixed ONLY by the proved c_2 = -1. Reads off c_3, "
            "c_4 symbolically (constants over b) and numerically at both q0 anchors "
            "(proton-pinned from qou_substrate.constants; muon canonical). Records the "
            "anchor-stability diagnostic and two structural collapses: uniform-weight "
            "exp(Sum per-block) = exp(total), and exp-vs-linear seeding share c_3 when "
            "the seed starts at u_L^2. NOT a fit; no scan; no wiring."
        ),
        "precisionMetadata": {"compute_dps": 60},
        "data": {
            "per_block_closed_forms": {blk: str(forms[blk]) for blk in blocks},
            "per_block_leading_eps": {blk: str(lead[blk]) for blk in blocks},
            "per_block_hbar_series": {
                blk: {f"a_{n}": str(v) for n, v in a_blk[blk].items() if v != 0}
                for blk in blocks},
            "uniform_total_hbar_series": {
                f"a_{n}": str(a_tot[n]) for n in range(ORDER_H) if a_tot[n] != 0},
            "ladder_G_k": {f"G_{k}": str(G[k]) for k in range(2, K_MAX + 1)},
            "scale_N": str(Nval),
            "c_symbolic": {f"c_{k}": str(c_sym[k]) for k in (2, 3, 4)},
            "c_numeric": {
                tag: {f"c_{k}": mp.nstr(results[tag]["c"][k], 40) for k in (2, 3, 4)}
                for tag in ("proton", "muon")},
            "anchors": {
                "proton_q0": mp.nstr(Q0_PROTON, 50),
                "muon_q0": mp.nstr(Q0_MUON, 50),
                "b_proton": mp.nstr(results["proton"]["b"], 50),
                "b_muon": mp.nstr(results["muon"]["b"], 50),
            },
            "empirical_c3": {"proton": mp.nstr(C3_EMP_PROTON, 30),
                             "muon": mp.nstr(C3_EMP_MUON, 10)},
            "c3_rel_err": {"proton": mp.nstr(err_p, 10), "muon": mp.nstr(err_m, 10)},
            "anchor_stability": {
                "predicted_c3_cross_anchor_swing": mp.nstr(pred_swing, 10),
                "empirical_c3_cross_anchor_swing": mp.nstr(emp_swing, 10),
                "prediction_is_anchor_constant": bool(anchor_constant),
                "note": ("b(q0) differs only at ~1e-8 relative between the two pins, "
                         "so any c_k = rational/b^m prediction is anchor-constant to "
                         f"~1e-8 — it cannot track the {emp_swing_pct} empirical swing "
                         "(the C13 diagnostic, reproduced here for the exponentiated "
                         "seed)."),
            },
            "structural_collapses": {
                "uniform_weights_collapse": (
                    "exp(N*Sum_lambda g_lambda) = exp(N*g_total): per-block structure "
                    "is invisible under uniform weights; per-block weights would be a "
                    "fit (forbidden without a derived weight rule)"),
                "exp_vs_linear_c3_identical": bool(c3_same),
                "c4_exp_minus_c4_linear": str(c4_shift),
            },
            "c13_reference": {
                "c3_linear_atomic_seed": mp.nstr(C13_C3_NUM, 30),
                "rel_diff_to_this_probe": mp.nstr(d_c13, 10),
                "note": ("Per-block sum is NOT proportional to the atomic Delta tr_M "
                         "(q-dependent ratio, = 4 only at q = 1), so this probe tests "
                         "genuinely different seed data as well as the exp form."),
            },
        },
        "assertions": [
            {
                "name": "per_block_leading_eps_coefficients_are_minus2_minus1_minus2",
                "computed": 1.0 if lead_ok else 0.0,
                "expected": 1.0,
                "passed": bool(lead_ok),
                "tolerance": 0.0,
                "source": "qbeta_multiblock_order_audit.py (PR #1593) per-block leading data",
            },
            {
                "name": "scale_fix_c2_minus1_solvable_and_exact",
                # mpmath.mpf carried end-to-end and serialized as a decimal
                # string. `float(...)` here truncated a 35-digit agreement to a
                # double, and the bare `1e-35` tolerance literal put a raw
                # float64 into the witness (AGENTS.md §PROBES ARE NOT EXEMPT;
                # caught by witness_raw_float64_audit, bean qou-t39x).
                "computed": mp.nstr(results["proton"]["c"][2], 40),
                "expected": "-1",
                "passed": bool(abs(results["proton"]["c"][2] + 1) < C2_TOL),
                "tolerance": mp.nstr(C2_TOL, 5),
                "source": "c_2 = -1 is the one proved rung (Lean N2_factor); the single scale d.o.f.",
            },
            {
                "name": "kill_criterion_hit_exponentiated_seed_misses_c3_gate",
                "computed": 0.0 if within_1pct_both else 1.0,
                "expected": 1.0,  # kill criterion fires => probe verdict NEGATIVE
                "passed": bool(not within_1pct_both),
                "tolerance": 0.0,
                "source": ("Pre-stated kill criterion: anchor-constant and far from "
                           "empirical (C13 failure mode) => NEGATIVE, extend C13 "
                           "scope-limited (a)."),
            },
        ],
        "verdict": {
            "overall": overall,
            "predicted_c3_proton": mp.nstr(c3_p, 30),
            "predicted_c3_muon": mp.nstr(c3_m, 30),
            "anchor_constant": bool(anchor_constant),
            "summary": summary,
        },
    }
    out["allPassed"] = all(a["passed"] for a in out["assertions"])

    wout = os.path.join(HERE, "qbeta-exponentiated-per-block.witness.json")
    with open(wout, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        out.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            out, script_path=__file__, engine=None, q0_anchor=None)
        # Explicit `comparison` stamp (bean qou-9ugp): this producer reads BOTH
        # pins deliberately, so no anchor list can classify it and it was going
        # out unstamped. The reason string is kept ASCII on purpose: this
        # witness is written with json.dump, whose ensure_ascii=True turns any
        # non-ASCII into a \\uXXXX escape and collapses the shape guard.
        apply_q0_comparison(out,
            muon=Q0_MUON, proton=Q0_PROTON,
            reason='compares the exponentiated per-block c_3 against the empirical target at BOTH pins; both pins are read on purpose and each has its own target',
        )
        json.dump(out, f, indent=2)
    print(f"\n  witness -> {wout}")
    return out


if __name__ == "__main__":
    main()
