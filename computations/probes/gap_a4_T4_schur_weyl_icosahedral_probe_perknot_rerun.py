#!/usr/bin/env python3
"""GAP-A-4 T4 probe — PER-KNOT-RETARGETED RE-RUN (bean x5az, artifact audit).

Re-runs the T4 Schur-Weyl icosahedral character-bridge probe with the
derivation attempt RETARGETED, per the protocol of
[`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`](../../docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md).
The audit's verdict on the original: it "*tries to derive* λ_A from a
weighted A₄-irrep sum" — but λ_A ≈ 2.533 is a FIT (the CODATA-implied
near-match), so deriving it is deriving a fit; there is no categorical
object to recover.

Retarget mapping (λ_A target → per-knot / round-trip targets):

  | original target | retargeted comparison set |
  |---|---|
  | λ_A = (1/4)·Σ_{λ⊢4} dim_q(V_λ) ≈ 2.533 (checked at q=1 → 5/2) | tr_M(p) ≈ 1.0653, tr_M(n) ≈ 0.9232 — canonical per-knot chi-cache Markov traces |
  |   | ρ_rt(p/n) = m_{p/n}·ℏ_q²/(m_e·Vol(𝓑₃)) ≈ 2.46 — the round-trip density target |

The construction itself is UNCHANGED: the same S₄ → A₄ and S₅ → A₅
branching tables, the same dim_q(V_λ) Wedderburn weights at the same
canonical muon-q₀ (matches computations/q-pinning-50-digit.witness.json),
the same character-orthogonality machinery imported from the original
probe module.  What changes is the QUESTION: instead of "does a
weighted A₄-irrep sum reproduce λ_A?", we enumerate the construction's
natural (pre-registered, parameter-free) irrep-sum aggregates and ask
whether ANY of them lands on the canonical per-knot densities
tr_M(p), tr_M(n) or on the round-trip ρ ≈ 2.46 — to stated tolerance
(MATCH < 0.5 % rel, NEAR < 5 % rel).

Pre-registered variant list per group G ∈ {A₄ (n=4), A₅ (n=5)} — all
canonical normalizations arising in the Schur-Weyl/branching
construction, NO tunable parameter, NO scan:

  V1  (1/n)·Σ_{λ⊢n} dim_q(V_λ)          — the original λ_A form
  V2  Σ_{λ⊢n} dim_q(V_λ) / #partitions   — partition average
  V3  Σ_i D_i / #irreps                  — irrep average of branched totals
  V4  D_i                                — per-irrep branched dim_q total
  V5  D_i / d_i                          — per-irrep, per-dimension
  V6  D_i·d_i / |G|                      — Plancherel-weighted per irrep
  V7  Σ_i D_i·d_i / |G|                  — Plancherel total

where D_i = Σ_{λ⊢n} mult(λ → irrep_i)·dim_q(V_λ) is the branched
dim_q total the original probe computes, and d_i = dim(irrep_i).

Look-elsewhere honesty: ~15 variants × 4 targets ≈ 60 comparisons —
an isolated NEAR (<5 %) is weak evidence; only a MATCH (<0.5 %) with a
structural reason would count as a lead.

Three-calibration discipline: NO new fitted constants, NO rescalers,
NO new ansatz families — only the original construction's natural
aggregates compared against the canonical per-knot base.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits
`gap-a4-T4-schur-weyl-icosahedral-probe-perknot-rerun.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import json
from pathlib import Path

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from _gap_a4_qsafe import Q_0_50DPS, dim_q_partition  # noqa: E402

# Import the ORIGINAL probe module (unmodified) for the like-for-like
# character tables + branching machinery.  Import does not execute main().
from gap_a4_T4_schur_weyl_icosahedral_probe import (  # noqa: E402
    A4_CHAR_TABLE, A4_CLASS_SIZES, A4_DIMS, A4_IRREPS,
    A5_CHAR_TABLE, A5_CLASS_SIZES, A5_DIMS, A5_IRREPS,
    S4_PARTITIONS_4, S4_TO_A4_CHAR,
    S5_PARTITIONS_5, S5_TO_A5_CHAR,
    character_inner_product, is_nonneg_integer_multiplicity,
)
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION as M_P_MEV,
    M_N_MEV_VALIDATION as M_N_MEV,
)

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

# Vol(𝓑₃) = 8·G (same 50-dps literal as the T2 probe / knot_volumes).
VOL_BORROMEAN_8G = mp.mpf(
    "7.32772475341775212043682811945907288619319499425")

MATCH_TOL = mp.mpf("0.005")   # 0.5 % relative
NEAR_TOL = mp.mpf("0.05")     # 5 % relative


def load_chi_cache_tr_M(atom: str, n: int) -> mp.mpf:
    path = COMPUTE_DIR / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"
    return mp.mpf(json.loads(path.read_text())["tr_M_at_q0"])


def branched_dimq_totals(partitions, restr_char, group_char_table,
                         class_sizes, group_order, q_0):
    """Reproduce the original probe's per-irrep branched dim_q totals
    D_i = Σ_λ mult(λ→i)·dim_q(V_λ), plus Σ_λ dim_q(V_λ)."""
    n_irreps = len(group_char_table)
    totals = [mp.mpf(0)] * n_irreps
    sum_dimq = mp.mpf(0)
    tol = mp.mpf("1e-8")
    all_int = True
    for lam in partitions:
        chi_lam = restr_char[lam]
        dq = dim_q_partition(lam, q_0)
        sum_dimq += dq
        for i, chi_i in enumerate(group_char_table):
            m = character_inner_product(chi_lam, chi_i, class_sizes,
                                        group_order)
            ok, nn = is_nonneg_integer_multiplicity(m, tol)
            if not ok:
                all_int = False
            totals[i] += dq * mp.mpf(nn)
    return totals, sum_dimq, all_int


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-T4-schur-weyl-icosahedral-probe-perknot-rerun",
        engine="mpmath",
    )
    w.set_audit_only(
        "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md"
    )
    w.set_description(
        "GAP-A-4 T4 per-knot RETARGETED re-run (bean x5az): the original "
        "Schur-Weyl A₄/A₅ branched dim_q construction, unchanged, with the "
        "derivation target swapped from the fitted λ_A ≈ 2.533 to the "
        "canonical per-knot densities tr_M(p) ≈ 1.0653 / tr_M(n) ≈ 0.9232 "
        "and the round-trip ρ_rt ≈ 2.46.  Enumerates pre-registered "
        "parameter-free irrep-sum aggregates; MATCH < 0.5 %, NEAR < 5 %. "
        "EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    hbar2 = hbar * hbar

    # ── Retargeted comparison set ──────────────────────────────────
    tr_M_p = load_chi_cache_tr_M("proton", 3)
    tr_M_n = load_chi_cache_tr_M("neutron", 3)
    rho_rt_p = mp.mpf(M_P_MEV) * hbar2 / (mp.mpf(M_E_MEV) * VOL_BORROMEAN_8G)
    rho_rt_n = mp.mpf(M_N_MEV) * hbar2 / (mp.mpf(M_E_MEV) * VOL_BORROMEAN_8G)
    targets = {
        "tr_M_proton_chi_cache": tr_M_p,
        "tr_M_neutron_chi_cache": tr_M_n,
        "rho_roundtrip_proton": rho_rt_p,
        "rho_roundtrip_neutron": rho_rt_n,
    }

    print("=" * 78)
    print("GAP-A-4 T4 — PER-KNOT-RETARGETED RE-RUN (Schur-Weyl irrep sums)")
    print("=" * 78)
    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print("  targets:")
    for k, v in targets.items():
        print(f"    {k:<28s} = {float(v):.10f}")

    # ── The construction's aggregates (unchanged from original) ────
    groups = []
    a4_totals, a4_sum_dimq, a4_int = branched_dimq_totals(
        S4_PARTITIONS_4, S4_TO_A4_CHAR, A4_CHAR_TABLE,
        A4_CLASS_SIZES, 12, q_0)
    groups.append(("A4", 4, A4_IRREPS, A4_DIMS, 12,
                   a4_totals, a4_sum_dimq, a4_int))
    a5_totals, a5_sum_dimq, a5_int = branched_dimq_totals(
        S5_PARTITIONS_5, S5_TO_A5_CHAR, A5_CHAR_TABLE,
        A5_CLASS_SIZES, 60, q_0)
    groups.append(("A5", 5, A5_IRREPS, A5_DIMS, 60,
                   a5_totals, a5_sum_dimq, a5_int))

    # ── Pre-registered variant enumeration ─────────────────────────
    variants: list[tuple[str, mp.mpf]] = []
    for (gname, n, irreps, dims, order, totals, sum_dimq, _ok) in groups:
        n_parts = len(S4_PARTITIONS_4 if n == 4 else S5_PARTITIONS_5)
        variants.append((f"{gname}: V1 (1/{n})·Σ_λ dim_q  [orig λ_A form]",
                         sum_dimq / n))
        variants.append((f"{gname}: V2 Σ_λ dim_q / #partitions({n_parts})",
                         sum_dimq / n_parts))
        variants.append((f"{gname}: V3 Σ_i D_i / #irreps({len(irreps)})",
                         sum(totals, mp.mpf(0)) / len(irreps)))
        plancherel_total = mp.mpf(0)
        for i, name in enumerate(irreps):
            variants.append((f"{gname}: V4 D[{name}]", totals[i]))
            variants.append((f"{gname}: V5 D[{name}]/dim({dims[i]})",
                             totals[i] / dims[i]))
            pw = totals[i] * dims[i] / order
            variants.append((f"{gname}: V6 D[{name}]·dim/|G|", pw))
            plancherel_total += pw
        variants.append((f"{gname}: V7 Σ_i D_i·dim_i/|G|", plancherel_total))

    print()
    print(f"  {'variant':<38s} {'value':>12s} "
          f"{'best target':>26s} {'rel err':>10s} {'class':>7s}")
    print("-" * 100)

    results = []
    matches, nears = [], []
    for name, val in variants:
        best_t, best_err = None, None
        for tname, tval in targets.items():
            err = abs(val / tval - 1)
            if best_err is None or err < best_err:
                best_t, best_err = tname, err
        if best_err < MATCH_TOL:
            klass = "MATCH"
            matches.append((name, best_t, float(best_err)))
        elif best_err < NEAR_TOL:
            klass = "NEAR"
            nears.append((name, best_t, float(best_err)))
        else:
            klass = "—"
        rec = {
            "variant": name,
            "value": str(val),
            "best_target": best_t,
            "best_rel_err": str(best_err),
            "class": klass,
            "rel_err_all_targets": {
                tname: str(abs(val / tval - 1))
                for tname, tval in targets.items()
            },
        }
        results.append(rec)
        print(f"  {name:<38s} {float(val):>12.6f} "
              f"{best_t:>26s} {float(best_err):>10.4%} {klass:>7s}")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data(
        "retarget",
        "original target λ_A = (1/4)Σ_λ dim_q ≈ 2.533 (a FIT — audit "
        "2026-06-24) replaced by canonical per-knot tr_M(p/n) chi-cache "
        "traces + round-trip ρ_rt(p/n) = m·ℏ_q²/(m_e·8G) ≈ 2.46",
    )
    w.add_data("targets", {k: str(v) for k, v in targets.items()})
    w.add_data("match_tol_rel", str(MATCH_TOL))
    w.add_data("near_tol_rel", str(NEAR_TOL))
    w.add_data("variant_results", results)
    w.add_data("branching_multiplicities_integer_ok",
               bool(a4_int and a5_int))
    w.add_data("n_comparisons", len(variants) * len(targets))

    # ── Synthesis (scope-limited (a) phrasing only) ────────────────
    if matches:
        synthesis = (
            f"{len(matches)} variant(s) MATCH (<0.5 % rel) a per-knot / "
            f"round-trip target: {matches}.  Candidate lead ONLY — with "
            f"{len(variants) * len(targets)} comparisons a structural "
            f"reason is required before this counts as a derivation; do "
            f"NOT wire anything (three-calibration discipline)."
        )
    elif nears:
        synthesis = (
            f"No variant MATCHes (<0.5 %); {len(nears)} NEAR (<5 %): "
            f"{nears}.  With {len(variants) * len(targets)} comparisons "
            f"these are within look-elsewhere noise.  Scope-limited "
            f"negative (a): the Schur-Weyl A₄/A₅ branched dim_q "
            f"construction's natural parameter-free aggregates land on "
            f"neither the canonical per-knot tr_M(p/n) nor the "
            f"round-trip ρ ≈ 2.46 to MATCH tolerance."
        )
    else:
        synthesis = (
            f"No variant lands within 5 % of any target.  Scope-limited "
            f"negative (a): the same weighted-irrep-sum construction that "
            f"reproduced the fitted λ_A form does NOT reproduce the "
            f"canonical per-knot densities tr_M(p) ≈ 1.0653 / tr_M(n) ≈ "
            f"0.9232, nor the round-trip ρ ≈ 2.46, under any of its "
            f"pre-registered parameter-free aggregates.  This constrains "
            f"these specific aggregates only — not the ingredient "
            f"'A₄/A₅ branching' inside richer closures."
        )
    w.add_data("synthesis_verdict", synthesis)
    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Reproduction anchors.
    w.add_assertion(
        "original_lambda_A_form_reproduced",
        computed=float(a4_sum_dimq / 4),
        expected=2.5328,
        tolerance=5e-4,
        source="(1/4)·Σ_{λ⊢4} dim_q(V_λ) at q₀ — the original T4 target "
               "quantity (= linking_weight_family_a(q₀) ≈ 2.5328); "
               "reproduced here as a baseline cross-check, NOT a target.",
    )
    w.add_assertion(
        "branching_multiplicities_all_integer",
        computed=1.0 if (a4_int and a5_int) else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="Original probe's claim α/β integrality — must reproduce "
               "(construction unchanged; only the target moved).",
    )
    w.add_assertion(
        "rho_roundtrip_proton_near_2_46",
        computed=float(rho_rt_p),
        expected=2.460,
        tolerance=2e-3,
        source="Round-trip density target m_p·ℏ_q²/(m_e·Vol(𝓑₃)) — the "
               "≈2.46 the audit doc cites as the value that round-trips "
               "m_p (reported, not fitted).",
    )

    out_path = w.save()
    repo_root = COMPUTE_DIR.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
