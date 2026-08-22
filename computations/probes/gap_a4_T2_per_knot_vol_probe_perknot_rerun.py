#!/usr/bin/env python3
"""GAP-A-4 T2 probe — PER-KNOT-DENSITY RE-RUN (bean x5az, artifact audit).

Re-runs the PR #1891 T2 per-knot Vol(K) convention probe with the
canonical PER-KNOT Hecke-trace density substituted for the fitted
global scalar λ_A, per the re-run protocol of
[`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`](../../docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md).
The audit classifies the original as λ_A-bound: it "anchors on the
`per_knot_density_borromean` (λ_A) convention".

Density-swap mapping (λ_A anchor → like-for-like per-knot form):

  | where λ_A entered the original | per-knot re-run |
  |---|---|
  | proton anchor assertion `λ_emp(p) ≈ 2.460` — the CODATA-implied | REMOVED as a target; λ_emp(p) is *reported*, and the |
  | λ_A near-match from the `per_knot_density_borromean` docstring | tested identity is `λ_emp(K) =? tr_M(K)` (ratio → 1) |
  | convention C "uniform Borromean" = the `per_knot_density_borromean` | kept as one of the three Vol conventions (the Vol map |
  | (λ_A) production convention | is under test, not the density scalar) |
  | reference trace `closed_form_tau_M(Z, N, …)` — the closed-form | canonical chi-cache Markov trace `tr_M(K)` from |
  | product approximation (needs the Rust kernel) | `chi-{atom}-h{3A}-at-q0-50dps.witness.json` |

The tested quantity per atom and Vol convention is

    ratio(K) = λ_emp(K) / tr_M(K)
             = m(K) / (m_e · per_knot_density_per_block(Vol(K), tr_M(K), q₀))

i.e. the observed mass over the canonical per-knot volume-density mass
`m_pred(K) = m_e · Vol(K)/ℏ_q² · tr_M(K)`.  The verdict metric is the
original's per-light-series swing max/min − 1 with the original
thresholds (<5 % TIGHT / <25 % NEAR / ≥25 % REFUTED).  A TIGHT swing
with ratio ≈ 1 would mean the per-knot density closes absolute mass; a
TIGHT swing at ratio = c ≠ 1 would mean λ_emp ∝ tr_M with a single
residual global factor c; a wide swing is a scope-limited negative (a)
for the per-knot density under that Vol convention — never a
structural exclusion (b).

Same isotopes {p, n, D, T, ³He, ⁴He}, same CODATA/AME validation
masses (codata_constants registry via the original module's
LIGHT_SERIES), same three Vol conventions (Phase-4 JSJ / Model B
small-knot / uniform Borromean), same canonical muon-q₀ 50-dps string
(matches computations/q-pinning-50-digit.witness.json), same precision
defaults (_precision.set_compute_dps).

Per-knot traces (canonical chi-cache, `tr_M_at_q0`):
  p 1.0653…, n 0.9232…, D 0.3884…, T 0.1041…, ³He 0.2066…, ⁴He 0.0554…
(p ≠ n distinct — the structure the degenerate global λ_A erases).
Note: the ⁴He cache uses the colour-weighted-averaged-crossing
convention; the others use averaged-crossings.

Three-calibration discipline: NO new fitted constants, NO rescalers
presented as closures, NO new ansatz families — only the original T2
test retargeted onto the canonical per-knot density base.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits
`gap-a4-T2-per-knot-vol-probe-perknot-rerun.witness.json`.
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
from _li_2_q_util import per_knot_density_per_block  # noqa: E402

# Import the ORIGINAL probe module (unmodified) for the like-for-like
# fixtures: atoms, masses, the three Vol conventions, λ_emp and the
# swing metric.  Import does not execute the original's main().
from gap_a4_T2_per_knot_vol_probe import (  # noqa: E402
    LIGHT_SERIES,
    Q_0_50DPS,
    hbar_q_sq,
    lambda_empirical,
    per_series_swing,
)
from codata_constants import M_E_MEV  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

# label (original LIGHT_SERIES) → (chi-cache atom name, strand count n)
CHI_CACHE_ATOMS = {
    "p": ("proton", 3),
    "n": ("neutron", 3),
    "D": ("deuteron", 6),
    "T": ("tritium", 9),
    "3He": ("helium-3", 9),
    "4He": ("helium-4", 12),
}


def load_chi_cache_tr_M(label: str) -> tuple[mp.mpf, str]:
    """Canonical per-knot |tr_M(K)| at q₀ from the numerical chi cache.

    Returns (tr_M, convention_tag).  Source witnesses:
    `chi-{atom}-h{n}-at-q0-50dps.witness.json` — the same caches the
    `canonical_tr_m_via_chi_cache.canonical_tr_m` combiner prefers.
    """
    atom, n = CHI_CACHE_ATOMS[label]
    path = COMPUTE_DIR / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"
    d = json.loads(path.read_text())
    return mp.mpf(d["tr_M_at_q0"]), str(d.get("convention", "unknown"))


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-T2-per-knot-vol-probe-perknot-rerun", engine="mpmath"
    )
    w.set_audit_only(
        "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md"
    )
    w.set_description(
        "GAP-A-4 T2 per-knot re-run (bean x5az): the original T2 Vol(K) "
        "convention probe with the canonical chi-cache per-knot Markov "
        "trace tr_M(K) substituted for the fitted global λ_A anchor. "
        "Tests ratio(K) = m(K) / (m_e·Vol(K)/ℏ_q²·tr_M(K)) per Vol "
        "convention; verdict = original swing thresholds. EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    hbar2 = hbar_q_sq(q_0)

    print("=" * 78)
    print("GAP-A-4 T2 — PER-KNOT-DENSITY RE-RUN (canonical tr_M(K), chi caches)")
    print("=" * 78)
    print(f"  q₀   = {Q_0_50DPS[:18]}...")
    print(f"  ℏ_q² = {float(hbar2):.10f}")

    conventions = ["A_phase4_jsj", "B_model_b_small_knot", "C_uniform_borromean"]

    print()
    print(f"  {'atom':<4} {'Z':>2} {'N':>2} {'tr_M(K) chi':>14} ", end="")
    for c in conventions:
        print(f"{'Vol_' + c[:1]:>12s} {'ratio_' + c[:1]:>12s} ", end="")
    print()
    print("-" * 100)

    rows = []
    ratios_by_convention: dict[str, list[mp.mpf]] = {c: [] for c in conventions}
    for label, Z, N, m_K, conv_vols in LIGHT_SERIES:
        tr_M_K, conv_tag = load_chi_cache_tr_M(label)
        per_atom = {
            "label": label, "Z": Z, "N": N, "m_K_MeV": str(m_K),
            "tr_M_chi_cache": str(tr_M_K),
            "chi_cache_convention": conv_tag,
        }
        print(f"  {label:<4} {Z:>2} {N:>2} {float(tr_M_K):>14.10f} ", end="")
        for c in conventions:
            vol = conv_vols[c]
            lam = lambda_empirical(m_K, vol, q_0)
            # Canonical per-knot mass via the paper-faithful helper.
            m_pred = M_E_MEV * per_knot_density_per_block(vol, tr_M_K, q_0)
            ratio = mp.mpf(m_K) / m_pred
            # Internal consistency: λ_emp/tr_M must equal m/m_pred exactly.
            assert abs(ratio - lam / tr_M_K) < mp.mpf("1e-40"), (
                label, c, "per_knot_density_per_block route mismatch"
            )
            ratios_by_convention[c].append(ratio)
            per_atom[f"vol_{c}"] = str(vol)
            per_atom[f"lambda_emp_{c}"] = str(lam)
            per_atom[f"m_pred_perknot_MeV_{c}"] = str(m_pred)
            per_atom[f"ratio_m_over_m_pred_{c}"] = str(ratio)
            print(f"{float(vol):>12.4f} {float(ratio):>12.6f} ", end="")
        print()
        rows.append(per_atom)

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data(
        "density_swap",
        "global λ_A anchor (per_knot_density_borromean ≈ 2.533, p=n degenerate)"
        " → canonical per-knot tr_M(K) from chi-{atom}-h{n}-at-q0-50dps"
        " witnesses via per_knot_density_per_block(Vol(K), tr_M(K), q₀)",
    )
    w.add_data("per_atom_per_convention", rows)

    # Per-convention swing — original verdict metric + thresholds.
    print()
    print("-" * 78)
    print(f"  {'convention':<26s} {'min(ratio)':>10s} {'max(ratio)':>10s} "
          f"{'max/min−1':>12s} {'verdict':>20s}")
    print("-" * 78)

    convention_verdicts = []
    for c in conventions:
        vals = ratios_by_convention[c]
        swing = per_series_swing(vals)
        if abs(swing) < mp.mpf("5e-2"):
            verdict = "TIGHT (<5 % swing)"
        elif abs(swing) < mp.mpf("0.25"):
            verdict = "NEAR (<25 % swing)"
        else:
            verdict = "REFUTED (≥25 %)"
        convention_verdicts.append({
            "convention": c,
            "min_ratio": str(min(vals)),
            "max_ratio": str(max(vals)),
            "swing": str(swing),
            "verdict": verdict,
        })
        print(f"  {c:<26s} {float(min(vals)):>10.4f} {float(max(vals)):>10.4f} "
              f"{float(swing):>+12.2%} {verdict:>20s}")
    w.add_data("convention_verdicts", convention_verdicts)

    # Nucleon-level report: does the per-knot density land absolute mass?
    p_row, n_row = rows[0], rows[1]
    ratio_p = mp.mpf(p_row["ratio_m_over_m_pred_C_uniform_borromean"])
    ratio_n = mp.mpf(n_row["ratio_m_over_m_pred_C_uniform_borromean"])
    print()
    print(f"  nucleon absolute-mass check (Vol = 8·G Borromean):")
    print(f"    m_p / m_pred(p) = {float(ratio_p):.6f}  "
          f"(m_pred = {float(mp.mpf(p_row['m_pred_perknot_MeV_C_uniform_borromean'])):.3f} MeV)")
    print(f"    m_n / m_pred(n) = {float(ratio_n):.6f}  "
          f"(m_pred = {float(mp.mpf(n_row['m_pred_perknot_MeV_C_uniform_borromean'])):.3f} MeV)")
    w.add_data("nucleon_absolute_mass_check", {
        "ratio_p": str(ratio_p),
        "ratio_n": str(ratio_n),
        "m_pred_p_MeV": p_row["m_pred_perknot_MeV_C_uniform_borromean"],
        "m_pred_n_MeV": n_row["m_pred_perknot_MeV_C_uniform_borromean"],
    })

    # Synthesis — scope-limited (a) phrasing only.
    swings = {v["convention"]: float(mp.mpf(v["swing"])) for v in convention_verdicts}
    tight = [v for v in convention_verdicts if v["verdict"].startswith("TIGHT")]
    near = [v for v in convention_verdicts if v["verdict"].startswith("NEAR")]
    swing_summary = ", ".join(f"{k}: {s:.2%}" for k, s in swings.items())
    if tight:
        synthesis = (
            f"Per-knot re-run: convention(s) "
            f"{[v['convention'] for v in tight]} give a TIGHT swing (<5 %) "
            f"of m(K)/(m_e·Vol(K)/ℏ_q²·tr_M(K)) across the light series — "
            f"λ_emp ∝ tr_M(K) up to a single residual factor "
            f"(ratio_p ≈ {float(ratio_p):.4f}).  The original T2 negative "
            f"was a λ_A-anchoring artifact in the tested sense; whether "
            f"the residual factor is categorically derivable remains open "
            f"(do NOT fit it — three-calibration discipline)."
        )
    elif near:
        synthesis = (
            f"Per-knot re-run: convention(s) {[v['convention'] for v in near]} "
            f"give a NEAR swing (<25 %); the rest are wide ({swing_summary}). "
            f"Partial structure only — scope-limited negative (a): the "
            f"per-knot tr_M(K) density with these Vol conventions, alone, "
            f"does not close the light-series mass ratios."
        )
    else:
        synthesis = (
            f"Per-knot re-run: all three Vol conventions give wide swings "
            f"of m(K)/(m_e·Vol(K)/ℏ_q²·tr_M(K)) ({swing_summary}).  "
            f"Scope-limited negative (a): the canonical per-knot tr_M(K) "
            f"density, alone, under any of the three Vol conventions, does "
            f"not collapse the light-series swing either — the original "
            f"T2 negative verdict is ROBUST to the λ_A → per-knot density "
            f"swap (it was not a density artifact in the swing metric), "
            f"while remaining silent on multi-term closures that include "
            f"tr_M(K) as a factor."
        )
    w.add_data("synthesis_verdict", synthesis)
    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Reproduction anchors (canonical chi-cache nucleon traces — these are
    # loaded inputs, not fitted targets).
    tr_p, _ = load_chi_cache_tr_M("p")
    tr_n, _ = load_chi_cache_tr_M("n")
    w.add_assertion(
        "proton_chi_cache_tr_M_matches_documented",
        computed=float(tr_p),
        expected=1.0653062380758782,
        tolerance=1e-12,
        source="chi-proton-h3-at-q0-50dps.witness.json tr_M_at_q0 "
               "(canonical per-knot proton trace, audit doc value 1.0653).",
    )
    w.add_assertion(
        "neutron_chi_cache_tr_M_matches_documented",
        computed=float(tr_n),
        expected=0.9232333051498377,
        tolerance=1e-12,
        source="chi-neutron-h3-at-q0-50dps.witness.json tr_M_at_q0 "
               "(canonical per-knot neutron trace, audit doc value 0.9232).",
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
