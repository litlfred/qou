#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""c_knot_nonuniversal_pinned_weight_probe.py — the clean cross-isotope C_knot test, run with the
NOW-PINNED Markov weight y_λ (PR #4543). Verdict: C_knot is NOT a universal derivable factor — it
varies 59.1× across the four lightest isotopes (D/T/³He/⁴He), and two knots at the SAME strand count
(T, ³He at H₉) require C_knot differing by a factor 1.37. So "derive C_knot as one geometric/scale
factor" is REFUTED (scope-a); the mirror-pair inequality further gives a scope-(b) exclusion of any
level-only rescale g(n, q₀). The Δ_λ magnitude derivation itself stays OPEN (bean qou-3q7t).

CONVENTION-D REFRESH (2026-08-11, bean qou-4jut). Every figure above and below was re-derived after
`70d1ade383` ("excise C tiers 2+3: 176 producer sites to convention D") — a deliberate repo-wide
migration that this file's committed witness PRE-DATED, so HEAD could not reproduce its own witness
(scriptHash fcc009c4ce2802cd vs sha256(HEAD) 32fdfcc3ed1c4342). Convention D is right by an
independent, experiment-free argument: it gives QR = Q² EXACTLY, hence r = log_Q(QR) = 2, and r is
the number of variables in the Wenzl principal specialisation s_λ(1,Q,…,Q^{r−1}) — it must be a
positive integer, and the mass chapter forces 2 (the fundamental of SU_q(2)). The pre-migration
convention returns a non-integer r and therefore was never a fibre dimension at all.
BOTH VERDICTS SURVIVE and in fact strengthen: spread 2.83× → 59.12× (scope-a), mirror ratio
1.35 → 1.367 (scope-b), and f^λ remains the tightest dim convention. Nothing that was claimed
becomes false; the magnitudes move. The witness's own description now INTERPOLATES every figure from
the run, so it can no longer drift from its payload the way this docstring did.

Context — why this supersedes c_knot_not_universal_probe.py
----------------------------------------------------------
The master binding formula is
    B(K) = m_e · |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|,     Σ_λ y_λ f^λ = tr_M(1) = 1,
and C_knot(K) = B_AME(K) / (m_e · |Σ|) is the FITTED deficit ratio = the open Δ_λ gate
(binding_energy_categorical_deuteron.py). The PRIOR prune (c_knot_not_universal_probe.py, PR #4491)
found a "41× convention spread" (5.85 vs 240) for the deuteron — but PR #4543 showed that 41× was
RIGHT-weight (Markov y_λ) vs WRONG-weight (signed dim_q, not the Markov trace): a category error, not
a genuine ambiguity. With the weight now PINNED to the derived Wenzl y_λ (BindingWeightMarkovPinning),
C_knot is well-posed, and the honest universality question can finally be asked cleanly. THIS
probe asks it: with the ONE derived weight and the SAME conventions as the master formula, is C_knot
universal across isotopes?

THE MEASUREMENT (all four caches interface-inclusive, χ^λ from the Rust Hoefsmit engine)
--------------------------------------------------------------------------------------
For each K ∈ {D(H₆), T(H₉), ³He(H₉), ⁴He(H₁₂)}: S(K) = |Σ_λ y_λ χ^λ(β_K) sgn f^λ| (y_λ the pinned
Wenzl weight, Σ y_λ f^λ = 1 verified), then C_knot(K) = B_AME(K)/(m_e S(K)):

    C_knot(D)=6.068  C_knot(T)=6.706  C_knot(³He)=4.905  C_knot(⁴He)=290.01  → spread 59.12×

Three independent kills of the single-factor hypothesis, all 0-fit:
  1. NON-UNIVERSAL: spread 59.12× (min ³He 4.905, max ⁴He 290.01) with the pinned weight + best dim.
  2. DIM CONVENTION doesn't fix it: f^λ (hook SYT) is still the TIGHTEST (spread 59.12×) vs dim_q
     (219.8×) and no-dim (73.98×) — the master formula's f^λ choice is the good one, yet still 59×.
  3. NO SCALE fixes it: the spread is invariant under any global scale (m_e → E₀/μ₀); C_knot/A and
     C_knot/(A−1) are non-constant; log C / log A ∈ {2.60,1.73,1.45,4.09} is not a clean power. A
     deuteron-pinned scale (0-fit CAL on B(²H)) PREDICTS T/³He/⁴He at −9.5% / +23.7% / −97.9% — far
     outside the isospin ±8% band (ROUTE 5, docs/audits/2026-08-01-mu3-target-robustness-audit.md).

The MIRROR-PAIR invariant (the Lean-provable core): T and ³He sit at the SAME strand count H₉ but
require C_knot(T)=6.706 ≠ 4.905=C_knot(³He) (ratio 1.367, robust across all three dim conventions). Therefore C_knot cannot be a function of (n, q₀) alone — it carries genuine per-knot
(isospin/mirror) content. Lean `CKnotNonUniversal.no_level_only_closure` proves the cross-
multiplied inequality B_AME(T)·S(³He) ≠ B_AME(³He)·S(T) (sorry-free, norm_num on rationals).

VERDICT
-------
scope-(a): the single-universal-C_knot / single-scale derivation route is REFUTED with the pinned
weight — C_knot ≡ the full per-isotope Δ_λ magnitude, not a constant and not any (global/A-power)
rescale. This CONFIRMS + SHARPENS the E₀-options audit (docs/audits/2026-06-01-e0-lambda-substrate-
derivation-options.md): the χ^λ→M_λ absolute per-block scale is not a single derivable object.
scope-(b) (narrow): the level-only closure class g(n, q₀)·m_e·S(K) is structurally excluded by the
T/³He mirror inequality (cited invariant: no_level_only_closure). The Δ_λ magnitude itself
remains OPEN (bean qou-3q7t) — this narrows the attack, it does not close the gate.

STRICT anti-fit: y_λ is the derived Wenzl weight (recomputed here, Σ y_λ f^λ = 1 asserted); χ^λ read
from committed interface-inclusive caches; B_AME are experimental validation targets used ONLY as a
diagnostic ratio, NEVER inverted into a canonical weight; free_parameters = 0; nothing wired. Exact
(mpmath, 50 dps). audit_only.
"""
from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMP = ROOT / "computations"
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401,E402 — substrate path bridge
from mpmath import mp, mpf, fabs, sqrt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

q0 = mpf(Q_50_DIGIT_STR)
qi = 1 / q0
h = q0 - qi
m_e = mpf("0.51099895069")

# Wenzl Schur-principal parameters (Q = q², Markov z pinned) — the CANONICAL y_λ (markov module).
Q = q0 ** 2
z_mark = q0**3 / (q0**2 + 1)
z_w = q0 * z_mark
QR = z_w / (1 - Q + z_w)


def _hooks_contents(lam):
    hs, cs = [], []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def f_lambda(lam):
    """SYT count = classical dim of the S_n irrep, via the hook-length formula."""
    hs, _ = _hooks_contents(lam)
    p = 1
    for x in hs:
        p *= x
    return math.factorial(sum(lam)) // p


def n_stat(lam):
    return sum(i * lam[i] for i in range(len(lam)))


def _q_int(k):
    if k == 0:
        return mpf(0)
    return (q0 ** k - qi ** k) / h


def _q_fac(n):
    r = mpf(1)
    for k in range(1, n + 1):
        r *= _q_int(k)
    return r


def dim_q(lam, n):
    """Quantum dimension s_λ(1, q, …, q^{n-1}) / [n]_q! (alternative dim convention, tested)."""
    r = q0 ** n_stat(lam)
    for i in range(len(lam)):
        for j in range(lam[i]):
            c = j - i
            arm = lam[i] - j - 1
            leg = sum(1 for rr in range(i + 1, len(lam)) if lam[rr] > j)
            hk = arm + leg + 1
            r *= _q_int(n + c) / _q_int(hk)
    return r / _q_fac(n)


def schur_principal(lam):
    """s_λ(1, Q, …, Q^{r-1}) closed form (Wenzl), Q = q², Q^r = QR."""
    hs, cs = _hooks_contents(lam)
    num = mpf(1)
    den = mpf(1)
    for hh, c in zip(hs, cs):
        num *= (1 - QR * Q ** c)
        den *= (1 - Q ** hh)
    return Q ** n_stat(lam) * num / den


def _load(fn):
    p = COMP / fn
    if not p.exists():
        raise FileNotFoundError(f"required interface-inclusive χ cache missing: {p}")
    a = json.loads(p.read_text())["data"]["atom"]
    parts = [tuple(e["partition"]) for e in a["by_partition"]]
    chis = [mpf(str(e["chi_lambda"])) for e in a["by_partition"]]
    return a["n_strands"], parts, chis


def sum_and_cknot(fn, B_ame, dimconv="f"):
    n, parts, chis = _load(fn)
    Z = mpf(0)
    sp_cache = {}
    for lam in parts:
        s = schur_principal(list(lam))
        sp_cache[lam] = s
        Z += s * f_lambda(list(lam))  # Σ s_λ f_λ = normaliser (⇒ Σ y_λ f_λ = 1)
    S = mpf(0)
    Snorm = mpf(0)
    for lam, chi in zip(parts, chis):
        y = sp_cache[lam] / Z
        sgn = (-1) ** n_stat(list(lam))
        if dimconv == "f":
            D = mpf(f_lambda(list(lam)))
        elif dimconv == "dimq":
            D = dim_q(list(lam), n)
        else:  # 'none'
            D = mpf(1)
        S += y * chi * sgn * D
        Snorm += y * f_lambda(list(lam))
    absS = fabs(S)
    return {
        "n_strands": n,
        "n_partitions": len(parts),
        "S_signed": S,
        "absS": absS,
        "markov_norm_sum_yf": Snorm,  # must be 1
        "B_naive_MeV": m_e * absS,
        "C_knot": B_ame / (m_e * absS),
    }


def main() -> int:
    # AME binding energies (experimental validation targets — diagnostic ratio only, never inverted).
    from codata_constants import (  # noqa: E402
        AME_B_DEUTERON_MEV_VALIDATION as B_D,
        AME_B_TRITIUM_MEV_VALIDATION as B_T,
        AME_B_HE3_MEV_VALIDATION as B_HE3,
        AME_B_HE4_MEV_VALIDATION as B_HE4,
    )
    isotopes = [
        ("D", "atom-chi-rust-d.witness.json", mpf(str(B_D)), 2),
        ("T", "atom-chi-rust-t.witness.json", mpf(str(B_T)), 3),
        ("3He", "atom-chi-rust-3he.witness.json", mpf(str(B_HE3)), 3),
        ("4He", "atom-chi-rust-4he.witness.json", mpf(str(B_HE4)), 4),
    ]

    print("=" * 78)
    print("  C_knot cross-isotope universality — pinned Wenzl y_λ, master-formula conventions")
    print("=" * 78)
    per = {}
    for name, fn, B, A in isotopes:
        r = sum_and_cknot(fn, B, "f")
        per[name] = {
            "A": A,
            "n_strands": r["n_strands"],
            "absS": mp.nstr(r["absS"], 8),
            "markov_norm_sum_yf": mp.nstr(r["markov_norm_sum_yf"], 6),
            "B_naive_MeV": mp.nstr(r["B_naive_MeV"], 8),
            "B_AME_MeV": mp.nstr(B, 8),
            "C_knot": mp.nstr(r["C_knot"], 8),
        }
        print(f"  {name:>4} H_{r['n_strands']:<2} |S|={float(r['absS']):9.5f} "
              f"Σyf={float(r['markov_norm_sum_yf']):.4f} "
              f"B_naive={float(r['B_naive_MeV']):8.4f} B_AME={float(B):8.4f} "
              f"C_knot={float(r['C_knot']):8.4f}")

    cvals = {k: mpf(per[k]["C_knot"]) for k in per}
    spread = max(cvals.values()) / min(cvals.values())

    # Mirror pair T / ³He at the SAME strand count H₉ — the level-only exclusion invariant.
    cT, cHe = cvals["T"], cvals["3He"]
    mirror_ratio = cT / cHe
    same_n = per["T"]["n_strands"] == per["3He"]["n_strands"]

    # Dim-convention robustness of the mirror ratio.
    dim_rows = {}
    for dc in ("f", "dimq", "none"):
        cvs = {name: sum_and_cknot(fn, B, dc)["C_knot"] for name, fn, B, _A in isotopes}
        dim_rows[dc] = {
            "C_knot": {k: mp.nstr(cvs[k], 6) for k in cvs},
            "spread": mp.nstr(max(cvs.values()) / min(cvs.values()), 5),
            "T_over_3He_sameH9": mp.nstr(cvs["T"] / cvs["3He"], 5),
        }

    # Deuteron-pinned scale prediction test (0-fit CAL on B(²H), predict the rest).
    SD = sum_and_cknot(isotopes[0][1], isotopes[0][2], "f")["absS"]
    alpha = mpf(str(isotopes[0][2])) / SD  # per-|S| scale calibrated to the deuteron
    pin_pred = {}
    for name, fn, B, _A in isotopes:
        SK = sum_and_cknot(fn, B, "f")["absS"]
        Bpred = alpha * SK
        pin_pred[name] = {
            "B_pred_MeV": mp.nstr(Bpred, 8),
            "B_AME_MeV": mp.nstr(B, 8),
            "err_pct": mp.nstr((Bpred - B) / B * 100, 4),
        }

    # Framing / writhe test (0-fit): does the omitted Jones/HOMFLY framing factor q₀^{c·w(K)} account
    # for C_knot? Writhe w(K) = (#σ − #σ⁻¹) of the canonical word (averaged interface crossings are
    # writhe-neutral). If framing closes it, c = ln(C_knot)/(w·ln q₀) is CONSTANT across isotopes.
    #
    # LEVEL OF DEFINITION (framing note; nothing below changes). The writhe is a property of the
    # BRAID WORD, not of its closure — Markov-I (conjugation) invariant, but Markov-II stabilisation
    # β ∈ B_n ↦ βσ_n^{±1} ∈ B_{n+1} shifts it by ±1 while presenting the same link. The four rows sit
    # at n(K) = 3(Z+N) strands, already recorded as `n_strands` above, and they are NOT all equal:
    #     D  n=6  w=4      T  n=9  w=4      ³He n=9  w=8      ⁴He n=12 w=8
    # n(K) is the braid index (atom-knot.md), i.e. the lowest level of the substrate tower. Under the
    # owner ruling (states are Gröbner–Shirshov normal forms; the observable is the trace at the
    # lowest level) these canonical words ARE the states, so the cross-isotope comparison compares
    # states, not two presentations of one state — it stands as written.
    # This probe's result is moreover a NEGATIVE and is level-proof either way: D and T share w=4 yet
    # have different C_knot, so no writhe-ONLY factor q₀^{c·w} (a hypothesis with no n-dependence by
    # construction) can close C_knot, whatever level each row sits at. The separate scope-(b) mirror
    # exclusion is already a SAME-level comparison (T and ³He both at n=9; `same_n` asserted below).
    # Ref: docs/audits/2026-08-10-writhe-level-of-definition.md §5d.
    framing = {}
    try:
        from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
        zn = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
        lnq = mp.log(q0)
        for name in per:
            Z, N = zn[name]
            cr = atom_canonical_crossings(Z, N, include_inter=True)
            npos = sum(1 for _g, t in cr if t == "sigma")
            nneg = sum(1 for _g, t in cr if t == "sigma_inv")
            w = npos - nneg
            C = mpf(per[name]["C_knot"])
            c = (mp.log(C) / (w * lnq)) if w != 0 else mpf("nan")
            framing[name] = {"writhe": w, "n_sigma": npos, "n_sigma_inv": nneg,
                             "C_knot": per[name]["C_knot"], "framing_c": mp.nstr(c, 6)}
        # D & T share writhe 4; ³He & ⁴He share writhe 8 — yet C_knot differs in BOTH pairs.
        wD, wT = framing["D"]["writhe"], framing["T"]["writhe"]
        framing_excluded = bool(wD == wT and mpf(per["D"]["C_knot"]) != mpf(per["T"]["C_knot"]))
    except Exception as e:  # canonical_braid_crossings unavailable — record, do not fake
        framing = {"error": f"writhe test skipped: {e}"}
        framing_excluded = None

    single_factor_refuted = bool(spread > mpf("1.2"))
    level_only_excluded = bool(same_n and mirror_ratio > mpf("1.1"))

    print(f"\n  spread(C_knot) = {float(spread):.3f}×   "
          f"T/³He (both H₉) = {float(mirror_ratio):.3f}  same_n={same_n}")
    print(f"  deuteron-pinned scale α = {float(alpha):.4f} MeV (= {float(alpha/m_e):.3f} m_e); "
          f"predicts T {pin_pred['T']['err_pct']}%, ³He {pin_pred['3He']['err_pct']}%, "
          f"⁴He {pin_pred['4He']['err_pct']}%")
    print(f"\n  VERDICT scope-(a): single-universal-C_knot REFUTED (spread {float(spread):.2f}×). "
          f"scope-(b): level-only rescale g(n,q₀) excluded by T/³He mirror. Δ_λ OPEN (qou-3q7t).")

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),
        "computation": "c-knot-nonuniversal-pinned-weight",
        "description": (
            "The clean cross-isotope C_knot universality test, run with the NOW-PINNED Markov weight "
            "y_λ (PR #4543, Σ y_λ f^λ = 1 verified). Master-formula conventions "
            "(binding_energy_categorical_deuteron): B(K) = m_e·|Σ_λ y_λ χ^λ(β_K) sgn f^λ|, χ^λ from the "
            f"interface-inclusive Rust Hoefsmit caches. Result: C_knot = {per['D']['C_knot']}/"
            f"{per['T']['C_knot']}/{per['3He']['C_knot']}/{per['4He']['C_knot']} for "
            f"D/T/³He/⁴He → spread {mp.nstr(spread, 5)}×, NON-UNIVERSAL. f^λ (hook SYT) is the tightest "
            f"dim convention ({dim_rows['f']['spread']}× vs dim_q {dim_rows['dimq']['spread']}×, "
            f"none {dim_rows['none']['spread']}×); no global/A-power scale fixes it (log C/log A non-"
            f"constant); a deuteron-pinned 0-fit scale mispredicts T/³He/⁴He by "
            f"{pin_pred['T']['err_pct']}%/{pin_pred['3He']['err_pct']}%/{pin_pred['4He']['err_pct']}% "
            f"(≫ isospin ±8%). Mirror pair T & ³He at the SAME H₉ need C_knot differing by a factor "
            f"{mp.nstr(mirror_ratio, 5)} (robust across dim conventions: "
            f"{dim_rows['f']['T_over_3He_sameH9']}/{dim_rows['dimq']['T_over_3He_sameH9']}/"
            f"{dim_rows['none']['T_over_3He_sameH9']}) ⇒ C_knot is NOT a function of (n,q₀); it is "
            "per-knot Δ_λ. "
            "scope-(a): single-universal-C_knot derivation route REFUTED; scope-(b): level-only rescale "
            "g(n,q₀) excluded by the mirror inequality (Lean no_level_only_closure). Δ_λ magnitude "
            "stays OPEN (bean qou-3q7t). Supersedes c_knot_not_universal_probe.py (whose 41× was right-"
            "vs-wrong weight, now resolved). No fit; B_AME diagnostic-only (never inverted); nothing "
            "wired; exact mpmath. NOTE: every figure in this description is INTERPOLATED from the "
            "values computed in this run — it cannot go stale against its own payload."),
        "audit_only": True,
        "tier": "scope-(a) refutation of single-universal-C_knot + scope-(b) level-only exclusion; no fit",
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": {
            "master_formula": "B(K) = m_e·|Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|,  Σ_λ y_λ f^λ = 1",
            "weight": "Wenzl Schur-principal y_λ (pinned, PR #4543) — recomputed, Σ y_λ f^λ = 1 asserted",
            "per_isotope": per,
            "spread_factor": mp.nstr(spread, 5),
            "mirror_pair_T_3He": {
                "same_strand_count_H9": same_n,
                "C_knot_T": mp.nstr(cT, 6),
                "C_knot_3He": mp.nstr(cHe, 6),
                "ratio": mp.nstr(mirror_ratio, 5),
                "note": (f"same H₉ ⇒ any g(n,q₀) closure would force C_knot(T)=C_knot(³He); they "
                         f"differ by a factor {mp.nstr(mirror_ratio, 5)}."),
            },
            "dim_convention_scan": dim_rows,
            "framing_writhe_test": {
                "per_isotope": framing,
                "framing_excluded": framing_excluded,
                "note": (
                    "Writhe w(K)=#σ−#σ⁻¹ of the canonical word (averaged interface crossings "
                    "writhe-neutral): w(D)=w(T)=4, w(³He)=w(⁴He)=8. The omitted Jones/HOMFLY "
                    "framing factor q₀^{c·w} would need CONSTANT c to close C_knot. The per-isotope "
                    "c is recorded in `per_isotope.framing_c` above and is not constant; and — "
                    "decisively, and independently of those values — D&T (same writhe 4) and ³He&⁴He "
                    "(same writhe 8) have DIFFERENT C_knot, so no writhe-only factor closes it. "
                    "That pair argument is what carries the exclusion; the c-spread is corroboration. "
                    "Framing RULED OUT (scope-b)."),
            },
            "deuteron_pinned_scale_prediction": {
                "alpha_MeV": mp.nstr(alpha, 6),
                "alpha_over_m_e": mp.nstr(alpha / m_e, 6),
                "predictions": pin_pred,
                "note": (f"0-fit CAL on B(²H); errors {pin_pred['T']['err_pct']}/"
                         f"{pin_pred['3He']['err_pct']}/{pin_pred['4He']['err_pct']}% ≫ isospin ±8% "
                         f"⇒ single scale fails."),
            },
            "verdict": {
                "single_universal_C_knot_refuted": single_factor_refuted,
                "level_only_rescale_excluded": level_only_excluded,
                "classification": (
                    f"scope-(a): C_knot is non-universal ({mp.nstr(spread, 5)}× with the pinned "
                    "weight + best dim), so "
                    "'derive C_knot as one geometric/scale factor' is refuted. scope-(b): the level-only "
                    "rescale class g(n,q₀)·m_e·S(K) is structurally excluded by the T/³He mirror "
                    "inequality (cited invariant no_level_only_closure). NOT an exclusion of a per-"
                    "knot Δ_λ derivation — that remains OPEN (bean qou-3q7t)."),
                "anti_fit": (
                    "y_λ derived (Wenzl, Σ y_λ f^λ = 1 asserted); χ^λ from committed caches; B_AME used "
                    "only as a diagnostic ratio, never inverted into a weight; free_parameters = 0."),
            },
            "free_parameters": 0,
        },
        "context": {
            "axis": "Δ_λ / C_knot derivation — is the deficit one universal factor? (pinned weight)",
            "bean": "qou-3q7t",
            "supersedes": "c_knot_not_universal_probe.py (41× was right-vs-wrong weight, resolved #4543)",
            "builds_on": "PR #4491 (C_knot gate), PR #4543 (weight pinned), "
                         "docs/audits/2026-06-01-e0-lambda-substrate-derivation-options.md",
            "no_fit": True,
        },
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)], cwd=this.parent, text=True
        ).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "c-knot-nonuniversal-pinned-weight.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")
    print(f"\nwitness -> {out.name}")

    # Assertions (fail-fast — the negative must be reproducible).
    assert abs(float(per["D"]["markov_norm_sum_yf"]) - 1.0) < 1e-6, "Markov normalisation Σ y_λ f^λ = 1 broken"
    assert single_factor_refuted, "spread must refute a single universal C_knot"
    assert level_only_excluded, "mirror pair must exclude a level-only rescale"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
