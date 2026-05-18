"""m_p chain closure Item A — T2+T3 at A=1 (single nucleon) probe.

Per docs/audits/2026-05-17-m-p-chain-closure-gap-analysis.md §"Item A":

  Reformulate or instantiate T2+T3 at A=1. The tower term
  `single + cross = Σ_g Φ_q(|V|) + Σ_{i<j} z² Φ_q(|V_i V_j|)`
  relies on generator-pair structure. At A=1 the proton has
  3 strands (2 generators), so the sum has C(2,2) = 1 pair —
  not empty. The "KeyError at A=1" diagnostic suggests the
  *witness* file `terms-2-3-atom-per-gen-mpfr-50dps.witness.json`
  doesn't tabulate A=1, not that the formula is empty.

This probe DIRECTLY computes the T2 (single-gen brane tower) and
T3 (pair-gen brane tower) sums for the proton and neutron — A=1
single nucleons — using the canonical per-generator volumes from
`mass_endomorphism.additive_wedderburn_volumes`.

Finding: at A=1 the volumes `V̂_full` are close to 1
(proton: 0.989, 0.971; neutron: similar), so Φ_q(|V̂|) is large
(~10^5-10^6). The T2+T3 raw sums are O(10^6), enormously larger
than the T1+T4 ~ O(1) currently shipping in the proton-mass chain.

INTERPRETATION OPTIONS for the user to adjudicate:

  (1) **Structural suppression** of T2+T3 at A=1 is intentional.
      The "brane tower" level-selection rule may forbid A=1 brane
      levels structurally, in which case the raw 10^6 Φ_q values
      DON'T contribute to the mass and the T1+T4 = 0.5974 MeV
      gap is real (Items B and C — T5 and T6 — must carry the
      remaining 1571× factor).

  (2) **Witness-coverage gap** as my audit suspected. T2+T3 at
      A=1 ARE structurally non-zero and need a downstream rule
      to filter or scale them. Including the raw values would
      explode the predicted mass by ~10^6×; some normalization
      brings them down.

  (3) **Re-derivation needed** of the level-selection rule.
      The "structurally empty under current level-selection rule"
      claim in derive_m_p_hecke_path_a may be over-strong; the
      generator-pair structure at A=1 exists (proton has 2 gens,
      so C(2,2)=1 pair) and the Φ_q values are real.

This probe is **diagnostic-only**: it surfaces the gap so the
owner can pick between (1)/(2)/(3). Does NOT modify the m_p chain.

Output: t2-t3-proton-neutron-a1.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from mass_endomorphism import (  # noqa: E402
    additive_wedderburn_volumes,
    proton_cross,
    neutron_cross,
    Phi_q,
)
from q_parameter import Q as Q_FLOAT  # noqa: E402


def compute_t2_t3(label: str, n_strands: int, crossings: dict) -> dict:
    """Compute T2 = Σ_g Φ_q(|V̂_g|) and T3 = z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)
    for a single-nucleon braid at A=1 (Z=1, N=0 or Z=0, N=1)."""
    vols = additive_wedderburn_volumes(n_strands, crossings)
    n_gens = len(vols)

    # T2: single-generator brane tower
    t2_per_gen = []
    t2 = 0.0
    for i, v in enumerate(vols):
        magnitude = abs(v["full"])
        phi = Phi_q(magnitude)
        t2_per_gen.append({"gen": i, "V_full": v["full"], "abs_V": magnitude, "phi_q": phi})
        t2 += phi

    # T3: pair brane tower (with z_mark² scaling per mass_endomorphism
    # convention: z_mark = 1/(q^{1/2}+q^{-1/2}))
    z_mark = 1.0 / (Q_FLOAT ** 0.5 + (1.0 / Q_FLOAT) ** 0.5)
    t3_per_pair = []
    t3_raw = 0.0  # before z² scaling
    for i in range(n_gens):
        for j in range(i + 1, n_gens):
            prod = vols[i]["full"] * vols[j]["full"]
            phi = Phi_q(abs(prod))
            t3_per_pair.append({"i": i, "j": j, "prod": prod, "phi_q": phi})
            t3_raw += phi
    t3 = z_mark ** 2 * t3_raw

    return {
        "label": label,
        "n_strands": n_strands,
        "n_generators": n_gens,
        "n_pairs": n_gens * (n_gens - 1) // 2,
        "vols": [{"gen": i, "V_full": v["full"]} for i, v in enumerate(vols)],
        "t2_per_gen": t2_per_gen,
        "t2_total": t2,
        "t3_per_pair": t3_per_pair,
        "t3_raw_sum": t3_raw,
        "z_mark_sq": z_mark ** 2,
        "t3_after_z_sq_scaling": t3,
        "t2_plus_t3": t2 + t3,
    }


def main() -> int:
    print("=" * 90)
    print("  Item A probe — T2+T3 at A=1 (single nucleon)")
    print("=" * 90)
    print()

    proton_result = compute_t2_t3("proton (Z=1, N=0)", 3, proton_cross)
    neutron_result = compute_t2_t3("neutron (Z=0, N=1)", 3, neutron_cross)

    for r in [proton_result, neutron_result]:
        print(f"  --- {r['label']} ---")
        print(f"  strands={r['n_strands']}  generators={r['n_generators']}  pairs={r['n_pairs']}")
        for v in r['vols']:
            print(f"    gen{v['gen']}: V_full = {v['V_full']:+.6f}")
        print(f"  T2 (single-gen tower):")
        for entry in r['t2_per_gen']:
            print(f"    Φ_q(|{entry['V_full']:+.6f}|) = {entry['phi_q']:.3e}")
        print(f"    T2 total = {r['t2_total']:.3e}")
        print(f"  T3 (pair tower):")
        for entry in r['t3_per_pair']:
            print(f"    Φ_q(|V_{entry['i']}·V_{entry['j']}| = |{entry['prod']:+.6f}|) = {entry['phi_q']:.3e}")
        print(f"    T3 raw sum = {r['t3_raw_sum']:.3e}")
        print(f"    z_mark² = {r['z_mark_sq']:.4f}")
        print(f"    T3 after z² scaling = {r['t3_after_z_sq_scaling']:.3e}")
        print(f"  T2 + T3 = {r['t2_plus_t3']:.3e}")
        print()

    print("=" * 90)
    print("  Comparison to T1+T4 (currently shipping in proton-mass chain)")
    print("=" * 90)
    print()
    # Load m_p_Hecke (T1+T4 partial) from the canonical Path A derivation
    # — no magic numbers; this is the single source of truth.
    from derive_m_p_hecke_path_a import m_p_hecke_path_a_at_q0
    m_p_hecke_value = float(m_p_hecke_path_a_at_q0())
    print("  T1 + T4 (proton, from derive_m_p_hecke_path_a, m_p_Hecke):")
    print(f"    m_p_Hecke = {m_p_hecke_value:.6f} (in same units as T1 and T4)")
    print()
    print(f"  T2+T3 (proton, this probe, raw): {proton_result['t2_plus_t3']:.3e}")
    print()
    print("  RATIO T2+T3 / m_p_Hecke ≈ {:.2e}".format(proton_result['t2_plus_t3'] / m_p_hecke_value))
    print()
    print("  Direct interpretation: if T2+T3 at A=1 are added to T1+T4,")
    print("  the resulting m_p_Hecke is ~10^6× the current value, which")
    print("  is far OVER CODATA (1836× would close the gap; 10^6× overshoots).")
    print()
    print("  Three options (see probe docstring + audit doc):")
    print("    (1) STRUCTURAL SUPPRESSION at A=1 is intentional;")
    print("        these volumes don't enter the mass formula by")
    print("        level-selection rule.")
    print("    (2) WITNESS-COVERAGE GAP requires a downstream scale")
    print("        factor that brings T2+T3 from O(10^6) to O(1000).")
    print("    (3) RE-DERIVATION of the level-selection rule needed.")
    print()

    # Witness output
    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder("t2-t3-proton-neutron-a1", engine="python")
        .set_description(
            "m_p chain closure Item A — direct computation of T2+T3 at "
            "A=1 (proton, neutron). Surfaces the previously-`KeyError`d "
            "tower contributions for owner adjudication: structural "
            "suppression vs witness-coverage gap vs level-selection-rule "
            "re-derivation. Diagnostic-only; does not modify m_p chain."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-m-p-chain-closure-gap-analysis.md"
        )
        .add_data("proton_a1", proton_result)
        .add_data("neutron_a1", neutron_result)
        .add_data(
            "interpretation_options",
            "1=structural_suppression, 2=witness_coverage_gap, 3=rederivation"
        )
        .add_data("ratio_t2t3_over_m_p_hecke", float(proton_result['t2_plus_t3'] / m_p_hecke_value))
        .add_data("ratio_t2t3_over_codata", float(proton_result['t2_plus_t3'] / 938.272))
        .add_assertion(
            name="proton_t2_t3_not_structurally_zero",
            computed=float(proton_result['t2_plus_t3']) > 1.0,
            expected=True,
            unit="boolean",
            source=(
                "At A=1 proton has 2 generators, so the pair sum has "
                "C(2,2)=1 entry. Volumes ~0.97-0.99 give Φ_q values "
                "~10^5-10^6. The 'structurally empty' framing in "
                "derive_m_p_hecke_path_a is incorrect at this raw level."
            ),
        )
        .add_caveat(
            "This probe is DIAGNOSTIC. It computes T2+T3 directly using "
            "the same `Phi_q`, `additive_wedderburn_volumes`, and "
            "`{proton,neutron}_cross` infrastructure as the A≥2 path. "
            "It does NOT modify the m_p chain. Closing m_p requires "
            "owner adjudication on which of options (1)/(2)/(3) applies."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
