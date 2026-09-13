#!/usr/bin/env python3
"""Per-knot additive S(K) structure vs the derived k(A) extensivity gap.

Bean qou-cqqs — salvage of PR #3205 verdict #5.

The per-knot re-run
(`gap-a4-S-K-additive-probe-perknot-rerun.witness.json`) showed the
PR #1876 additive-S(K) refutation is partly a λ_A artifact: on the
canonical per-knot base tr_M(K), S_emp(K) > 0 for all six atoms and
S/(A·m_e) is uniform to ×1.73 (vs sign-flipping/unbounded on λ_A).

Honest test now: does that per-knot additive structure INFORM the
single open Δ_λ gate gap — the DERIVED extensivity multiplier
k(A) = μ_ext(K) = B_AME / B_base
(`deltalambda-extensivity-gap-synthesis.witness.json`)?

Targets (D/T/³He/⁴He):  μ_ext = 5.853 / 4.444 / 3.292 / 9.313.
The DEFINING feature is NON-MONOTONE: 4He is the max (doubly-magic),
D is the SECOND-largest (tiny B_base), 3He < T though same A.

Decisive structural fact (formalize-first): a quantity UNIFORM in A
(like S/(A·m_e) ~ ×1.73) CANNOT supply a non-monotone μ_ext (×2.83
range, D-2nd). So the probe FIRST tests explicitly whether each
per-knot candidate is monotone/uniform (→ PRUNE) or actually tracks
the μ_ext non-monotone SHAPE (→ LEAD).

Candidates are parameter-free readings of the per-knot S(K)/tr_M
structure. Junk controls (A, C(A,2) bonds) calibrate any "match"
against look-elsewhere. Shape is judged by (i) rank ordering,
(ii) Spearman rank-correlation with μ_ext, (iii) per-isotope rel-err
after a SINGLE global mean-aligning scale (a shape DIAGNOSTIC, NOT a
per-point fit, NOT a rescaler-as-closure). No Breit-Wigner / BW fit,
no reverse-engineering a constant to a target (adhb gate respected).

EXPLORATORY — scope-(a). No production wiring; no content changes.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _bridge

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps, fmt
from witness_base import WitnessBuilder, record_upstream


def _serialise(obj):
    """Render mpf leaves with `_precision.fmt`; leave everything else alone."""
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()
                if not k.startswith("_")}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
set_compute_dps()

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO_ROOT = COMPUTE_DIR.parent

SYNTH = COMPUTE_DIR / "deltalambda" / \
    "deltalambda-extensivity-gap-synthesis.witness.json"
RERUN = HERE / "gap-a4-S-K-additive-probe-perknot-rerun.witness.json"

M_E = mp.mpf("0.51099895069")
ATOMS = ["D", "T", "3He", "4He"]   # the four extensivity-gap isotopes


def spearman(a: list[mp.mpf], b: list[mp.mpf]) -> mp.mpf:
    """Spearman rank-correlation with average-rank tie handling.

    EXACT up to the two square roots.  Ranks are half-integers, so every
    quantity here except the final radicals is a RATIONAL, and it is carried
    as `Fraction` rather than as `float`.  This returned a `float` built with
    `math.sqrt` over float ranks until 2026-09-13 — the case AGENTS.md names
    directly ("never aggregate with `statistics` / `math` over floats"), and
    not a cosmetic one here: the probe's PRUNE verdict is decided by
    `rho_real > rho_junk + 0.25`, so this function's return value IS the
    conclusion.
    """
    def ranks(xs):
        order = sorted(range(len(xs)), key=lambda i: xs[i])
        rk = [Fraction(0)] * len(xs)
        i = 0
        while i < len(xs):
            j = i
            while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
                j += 1
            avg = Fraction(i + j, 2) + 1
            for k in range(i, j + 1):
                rk[order[k]] = avg
            i = j + 1
        return rk
    ra, rb = ranks(a), ranks(b)
    n = len(a)
    mean_a = sum(ra, Fraction(0)) / n
    mean_b = sum(rb, Fraction(0)) / n
    num = sum(((ra[i] - mean_a) * (rb[i] - mean_b) for i in range(n)),
              Fraction(0))
    va = sum(((ra[i] - mean_a) ** 2 for i in range(n)), Fraction(0))
    vb = sum(((rb[i] - mean_b) ** 2 for i in range(n)), Fraction(0))
    if va <= 0 or vb <= 0:
        return mp.mpf(0)
    da = mp.sqrt(mp.mpf(va.numerator) / va.denominator)
    db = mp.sqrt(mp.mpf(vb.numerator) / vb.denominator)
    return (mp.mpf(num.numerator) / num.denominator) / (da * db)


def order_desc(vals: dict[str, mp.mpf]) -> list[str]:
    return sorted(vals, key=lambda k: vals[k], reverse=True)


def main() -> int:
    synth = record_upstream(SYNTH, _UPSTREAM_RECORDS)
    rerun = record_upstream(RERUN, _UPSTREAM_RECORDS)

    # ── 1. cross-check: reproduce B_base and μ_ext from the synthesis witness
    B_base, B_AME, mu_target = {}, {}, {}
    for a in ATOMS:
        row = synth["rows"][a]
        B_base[a] = mp.mpf(str(row["B_base_MeV"]))
        B_AME[a] = mp.mpf(str(row["B_AME_MeV"]))
        mu_target[a] = mp.mpf(str(row["mu_ext_target"]))
    mu_recomputed = {a: B_AME[a] / B_base[a] for a in ATOMS}
    xcheck_ok = all(
        abs(mu_recomputed[a] - mu_target[a]) < mp.mpf("1e-9") for a in ATOMS
    )

    # ── per-knot S(K)/tr_M structure from the rerun witness
    trM = {a: mp.mpf(rerun["data"]["tr_M_per_atom"][a]) for a in ATOMS}
    trM["p"] = mp.mpf(rerun["data"]["tr_M_per_atom"]["p"])
    trM["n"] = mp.mpf(rerun["data"]["tr_M_per_atom"]["n"])
    pk_rows = {r["label"]: r for r in rerun["data"]["perknot_trM"]["rows"]}
    S_emp = {a: mp.mpf(pk_rows[a]["S_emp_MeV"]) for a in ATOMS}
    ZN = {a: (int(pk_rows[a]["Z"]), int(pk_rows[a]["N"])) for a in ATOMS}
    Aof = {a: sum(ZN[a]) for a in ATOMS}

    # ── 2. candidate parameter-free multipliers ─────────────────────────────
    cand: dict[str, dict[str, mp.mpf]] = {}

    # per-knot additive S(K) normalisations (the "uniform to ×1.73" family)
    cand["S/(A*m_e)"] = {a: S_emp[a] / (Aof[a] * M_E) for a in ATOMS}
    cand["S/m_e"] = {a: S_emp[a] / M_E for a in ATOMS}
    # per-knot trace and its inverse (leading-term carrier)
    cand["tr_M(K)"] = {a: trM[a] for a in ATOMS}
    cand["1/tr_M(K)"] = {a: 1 / trM[a] for a in ATOMS}
    # tr_M(K) vs constituent sum — a per-knot "binding-like" additive reading
    cand["constit_sum/tr_M"] = {
        a: (ZN[a][0] * trM["p"] + ZN[a][1] * trM["n"]) / trM[a] for a in ATOMS
    }
    # tr_M-bond-product Σ_{bonds} tr_M(K): C(A,2) identical per-knot bonds
    cand["C(A,2)*tr_M(K)"] = {
        a: len(list(combinations(range(Aof[a]), 2))) * trM[a] for a in ATOMS
    }
    # ── 3. junk controls (deliberately meaningless) ─────────────────────────
    cand["JUNK:A"] = {a: mp.mpf(Aof[a]) for a in ATOMS}
    cand["JUNK:C(A,2)"] = {
        a: mp.mpf(len(list(combinations(range(Aof[a]), 2)))) for a in ATOMS
    }

    mu_vec = [mu_target[a] for a in ATOMS]
    mu_order = order_desc(mu_target)
    mu_spread = max(mu_vec) / min(mu_vec)

    # ── evaluate each candidate: shape (order, Spearman) + mean-aligned rel-err
    results = {}
    for name, cm in cand.items():
        cvec = [cm[a] for a in ATOMS]
        cspread = max(abs(v) for v in cvec) / min(abs(v) for v in cvec)
        rho = spearman(cvec, mu_vec)
        # single global mean-aligning scale (geometric mean) — DIAGNOSTIC only
        gm_c = mp.e ** (sum(mp.log(abs(v)) for v in cvec) / len(cvec))
        gm_mu = mp.e ** (sum(mp.log(v) for v in mu_vec) / len(mu_vec))
        scale = gm_mu / gm_c
        per_iso = {}
        for a in ATOMS:
            scaled = cm[a] * scale
            rel = abs(scaled - mu_target[a]) / mu_target[a]
            per_iso[a] = {
                "candidate_raw": cm[a],
                "candidate_scaled": scaled,
                "mu_ext_target": mu_target[a],
                "rel_err": rel,
            }
        max_rel = max(per_iso[a]["rel_err"] for a in ATOMS)
        c_order = order_desc(cm)
        order_match = c_order == mu_order
        # deuteron tell: is D the 2nd-largest (as in μ_ext), or the smallest?
        d_rank_cand = c_order.index("D") + 1       # 1 = largest
        results[name] = {
            "order_desc": c_order,
            "order_matches_mu": order_match,
            "D_rank_in_candidate": d_rank_cand,     # μ_ext has D at rank 2
            "spearman_vs_mu": rho,
            "spread_max_over_min": cspread,
            "monotone_or_uniform_note": (
                "uniform (spread<1.3)" if cspread < mp.mpf("1.3")
                else "non-uniform"),
            "max_rel_err_mean_aligned": max_rel,
            "per_isotope": per_iso,
        }

    # ── junk-control calibration: best real candidate vs best junk ───────────
    real_names = [n for n in cand if not n.startswith("JUNK")]
    junk_names = [n for n in cand if n.startswith("JUNK")]
    best_real = max(real_names, key=lambda n: results[n]["spearman_vs_mu"])
    best_junk = max(junk_names, key=lambda n: results[n]["spearman_vs_mu"])
    rho_real = results[best_real]["spearman_vs_mu"]
    rho_junk = results[best_junk]["spearman_vs_mu"]
    beats_junk = rho_real > rho_junk + 0.25   # meaningful margin for n=4

    # decisive prune criterion: no real candidate reproduces μ_ext's SHAPE
    any_order_match = any(
        results[n]["order_matches_mu"] for n in real_names)
    any_d_second = any(
        results[n]["D_rank_in_candidate"] == 2 for n in real_names)

    if any_order_match and beats_junk:
        verdict_tag = "LEAD"
    else:
        verdict_tag = "PRUNE"

    # ── console report ───────────────────────────────────────────────────────
    print("=" * 92)
    print("Per-knot additive S(K) vs derived k(A) extensivity gap (bean qou-cqqs)")
    print("=" * 92)
    print(f"  cross-check B_AME/B_base == mu_ext_target : {xcheck_ok}")
    print(f"  mu_ext order (desc): {mu_order}  spread ×{float(mu_spread):.2f} "
          f"(D at rank {mu_order.index('D')+1})")
    print("-" * 92)
    hdr = f"  {'candidate':<20}{'order(desc)':<26}{'Drank':>6}{'spear':>7}" \
          f"{'spread':>8}{'maxRelErr':>10}"
    print(hdr)
    for name in real_names + junk_names:
        r = results[name]
        print(f"  {name:<20}{'/'.join(r['order_desc']):<26}"
              f"{r['D_rank_in_candidate']:>6}{r['spearman_vs_mu']:>7.2f}"
              f"{r['spread_max_over_min']:>8.2f}"
              f"{r['max_rel_err_mean_aligned']:>10.2f}")
    print("-" * 92)
    print("  per-isotope candidate(scaled) vs mu_ext  [rel-err]:")
    for name in real_names:
        r = results[name]
        cells = "  ".join(
            f"{a}:{r['per_isotope'][a]['candidate_scaled']:.2f}/"
            f"{r['per_isotope'][a]['mu_ext_target']:.2f}"
            f"[{r['per_isotope'][a]['rel_err']*100:.0f}%]" for a in ATOMS)
        print(f"    {name:<20} {cells}")
    print("-" * 92)
    print(f"  best real candidate : {best_real} (Spearman {rho_real:+.2f})")
    print(f"  best junk control   : {best_junk} (Spearman {rho_junk:+.2f})")
    print(f"  real beats junk by >0.25 ? {beats_junk}")
    print(f"  any real order == mu order ? {any_order_match}")
    print(f"  any real puts D at rank 2 (as mu_ext) ? {any_d_second}")
    print(f"\n  VERDICT: {verdict_tag}")

    verdict = (
        f"{verdict_tag} (scope-(a)). Cross-check: B_AME/B_base reproduces "
        f"mu_ext_target for all four isotopes ({xcheck_ok}). mu_ext is "
        f"NON-MONOTONE (order {'/'.join(mu_order)}, spread "
        f"×{float(mu_spread):.2f}, {mu_order[1]} 2nd-largest). NO "
        f"parameter-free per-knot reading of the additive "
        f"S(K)/tr_M structure reproduces that shape: every candidate that "
        f"has 4He as the max (S/m_e, S/(A m_e), 1/tr_M, constit_sum/tr_M) "
        f"puts the DEUTERON SMALLEST (rank 4) against mu_ext's "
        f"D-at-rank-{mu_order.index('D') + 1} — the per-knot "
        f"S/(A m_e) family is monotone/compressed (spread "
        f"×{float(results['S/(A*m_e)']['spread_max_over_min']):.2f} across "
        f"the four) and cannot supply mu_ext's ×{float(mu_spread):.2f} "
        f"non-monotone range, as the formalize-first "
        f"uniformity argument predicts. tr_M(K) itself is anti-shaped "
        f"(4He MIN, not max). JUNK CONTROL: the best real candidate "
        f"({best_real}, Spearman {rho_real:+.2f}) does NOT beat the best "
        f"junk control ({best_junk}, Spearman {rho_junk:+.2f}) by a "
        f"meaningful n=4 margin (beats_by_>0.25={beats_junk}) — so any "
        f"apparent partial match is within look-elsewhere noise. "
        f"CONCLUSION: the per-knot additive S(K) structure does NOT inform "
        f"the derived k(A) extensivity multiplier; it is pruned as a "
        f"source of the non-monotone k(A). Scope-limited negative (a): "
        f"constrains the per-knot S(K)/tr_M single-quantity reading only; "
        f"NOT a structural exclusion of tr_M in a richer multi-term / "
        f"operator-valued branching combiner (GAP-A-3/GAP-A-4 remain the "
        f"open derived directions). No fit, no BW, no rescaler-as-closure."
    )

    w = WitnessBuilder(
        "perknot-additive-sk-vs-kA-extensivity", engine="mpmath")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_audit_only(
        "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md")
    w.set_description(
        "Bean qou-cqqs (PR #3205 verdict #5 salvage). Tests whether the "
        "per-knot additive S(K)/tr_M structure — regularised on the "
        "canonical base (S/(A m_e) uniform to ×1.73, no sign flip) — "
        "informs the single open Delta_lambda gate gap: the DERIVED "
        "extensivity multiplier k(A)=mu_ext=B_AME/B_base "
        "(5.853/4.444/3.292/9.313 for D/T/3He/4He, NON-MONOTONE, 4He max, "
        "D 2nd). Parameter-free candidates vs mu_ext by rank order, "
        "Spearman, and mean-aligned rel-err, calibrated against junk "
        "controls (A, C(A,2)). No fit, no BW, no rescaler-as-closure. "
        "EXPLORATORY, scope-(a).")

    w.add_parameter("m_e_MeV", str(M_E))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("bean", "qou-cqqs")
    w.add_data("cross_check_B_AME_over_B_base_equals_mu_target", bool(xcheck_ok))
    w.add_data("targets", {
        a: {
            "B_base_MeV": fmt(B_base[a]),
            "B_AME_MeV": fmt(B_AME[a]),
            "mu_ext_target": fmt(mu_target[a]),
            "mu_ext_recomputed": fmt(mu_recomputed[a]),
            "A": Aof[a],
        } for a in ATOMS
    })
    w.add_data("mu_ext_order_desc", mu_order)
    w.add_data("mu_ext_spread_max_over_min", fmt(mu_spread))
    w.add_data("candidates", _serialise(results))
    w.add_data("junk_control", {
        "best_real_candidate": best_real,
        "best_real_spearman": fmt(rho_real),
        "best_junk_candidate": best_junk,
        "best_junk_spearman": fmt(rho_junk),
        "real_beats_junk_by_0p25": bool(beats_junk),
        "any_real_order_matches_mu": bool(any_order_match),
        "any_real_D_at_rank2": bool(any_d_second),
    })
    w.add_data("verdict_tag", verdict_tag)
    w.add_data("verdict", verdict)

    w.add_assertion(
        "cross_check_mu_ext_reproduced",
        computed=str(bool(xcheck_ok)), expected="True", tolerance=0,
        source="B_AME/B_base recomputed from synthesis witness rows equals "
               "mu_ext_target to <1e-9 for D/T/3He/4He.")
    w.add_assertion(
        "perknot_sk_does_not_beat_junk_on_mu_shape",
        computed=str(bool(not beats_junk)), expected="True", tolerance=0,
        source=f"best real per-knot candidate {best_real} Spearman "
               f"{rho_real:+.2f} vs best junk {best_junk} {rho_junk:+.2f}; "
               f"margin < 0.25 ⇒ no meaningful shape match (n=4).")
    w.add_assertion(
        "no_perknot_candidate_reproduces_mu_ext_order",
        computed=str(bool(not any_order_match)), expected="True", tolerance=0,
        source=f"No parameter-free per-knot S(K)/tr_M candidate matches the "
               f"non-monotone mu_ext desc order ({mu_order[1]} 2nd, "
               f"{mu_order[0]} max); the S/(A m_e) family puts D smallest.")

    print("\n  RERUN VERDICT:")
    for chunk in verdict.split(". "):
        print(f"    {chunk.strip()}")

    out = w.save()
    try:
        rel = out.relative_to(REPO_ROOT)
    except ValueError:
        rel = out
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
