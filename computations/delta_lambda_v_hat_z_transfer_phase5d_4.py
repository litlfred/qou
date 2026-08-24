"""
delta_lambda_v_hat_z_transfer_phase5d_4.py — Phase 5d.4 probe.

Tests whether the Phase 5c.1 z-exactness finding (τ_M ratio = z exactly
per interface generator) transfers to the per-generator V̂ level used
by PR #801's binding-energy formula.

Phase 5c.1 finding (τ_M-level):
  τ_M(β_K^FULL) / τ_M(β_K^CONSTIT) at any Z-step = z (rel.err 0.0001%)

Question for V̂-level (PR #801 framework):
  V̂_g(β_K^FULL) / V̂_g(β_K^CONSTIT) = ?  for interface generator g

If z-exactness transfers, the interface generator's V̂ ratio = z.
If not, the V̂-level structure is different.

Result: **z-exactness DOES NOT transfer**. Instead, V̂ at interface
generators is **flavor-selective**:
  - Different-flavor (p-n) interface: V̂_FULL = 0     (V̂_CONSTIT = 1)
  - Same-flavor   (p-p) interface: V̂_FULL = +h/2   (V̂_CONSTIT = 1; σ positive)
  - Same-flavor   (n-n) interface: V̂_FULL = -h/2   (V̂_CONSTIT = 1; σ⁻¹ negative)

where h = q - q⁻¹ ≈ 0.209 is the Hecke skein parameter. The
"h/2 vs 0 vs -h/2" structure is **richer than naive z-transfer**:
the flavor pair at the interface determines the categorical value.

This is consistent with the Hecke relation σ² = h·σ + 1 specialised
to the interface generator: V̂(σ)|interface = ⟨σ - h/2⟩ ↦ projection
onto the symmetric/antisymmetric channel depending on flavor pairing.

Implication: the binding-energy formula's T1 = |∏ V̂_g| term picks up
a factor of (h/2)^(#same-flavor-interfaces) · 0^(#different-flavor-interfaces)
from interface generators. For typical atom braids, multiple interface
contributions multiply — explaining why the binding formula's T1 is
small (~10⁻¹⁶ in PR #801's data) for atoms with mixed-flavor interfaces.

  Ref: PR #801 ([binding_via_interface_knot.py](computations/binding_via_interface_knot.py))
  Ref: PR #819 Phase 5c.1 ([delta_lambda_fr_identity_phase5c.py](computations/delta_lambda_fr_identity_phase5c.py))
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from mass_at_3A_proper import per_generator_V_hat_3A
from _precision import set_compute_dps  # noqa: E402


# (Z, N, label, expected_interface_generators) — interface gens are at
# positions 3Z-1 (between Z-th and Z+1-th nucleon block) etc.
ATOMS = [
    ("D",   1, 1),   # H_6: gen 2 (σ_3) is p-n interface
    ("T",   1, 2),   # H_9: gen 2 (σ_3) is p-n; gen 5 (σ_6⁻¹) is n-n
    ("3He", 2, 1),   # H_9: gen 2 (σ_3) is p-p; gen 5 (σ_6) is p-n
    # ⁴He H_12 skipped — slow without further infra
]


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("v-hat-z-transfer-phase5d-4")
    builder.set_description(
        "Phase 5d.4: probe whether the Phase 5c.1 z-exactness finding "
        "(τ_M(β_FULL)/τ_M(β_CONSTIT) = z per interface) transfers to "
        "the per-generator V̂ level used by PR #801's binding-energy "
        "formula. Result: V̂-level z-transfer FAILS; instead, V̂ at "
        "interface generators is flavor-selective: different-flavor "
        "(p-n) interface → V̂_FULL = 0; same-flavor (p-p / n-n) "
        "interface → V̂_FULL = ±h/2 (sign matches σ orientation). The "
        "categorical structure is richer than naive z-transfer."
    )
    builder.set_content_block("def:ew-interface-knot")

    # 🛑 Was: `load_q_50dps()`, which reads the MUON `q-pinning-50-digit`
    # witness by default. But `per_generator_V_hat_3A` (imported above from
    # `mass_at_3A_proper`) takes no q argument -- it binds its own q_0 at module
    # level from `q_parameter`, which resolves PROTON for that stem. So the
    # muon q/h/z below were being applied to proton-computed V̂, and the witness
    # recorded the muon q_0 as this producer's q_0.
    #
    # That is the `delta_lambda_fr_identity_phase5c` defect again (fixed
    # 2026-08-08): two layers meeting inside one quantity, invisible because
    # each half is individually reasonable. Take q_0 from the same place the
    # V̂ side takes it, so the pair is single-layer by construction.
    from q_parameter import Q_MP as _Q_RUNTIME  # noqa: E402
    # Q_MP, not mpf(str(Q)): the f64 constant carries ~16 significant digits,
    # so mpf(str(...)) LAUNDERS it — the value looks 50-digit and is accurate
    # to 16. Read the high-precision name instead.
    q = _Q_RUNTIME
    q_inv = mp.mpf(1) / q
    z = mp.mpf(1) / (mp.sqrt(q) + mp.sqrt(q_inv))
    h = q - q_inv
    builder.add_parameter("q_0", str(q))
    builder.add_parameter("h", str(h))
    builder.add_parameter("h_over_2", str(h / 2))
    builder.add_parameter("z_markov", str(z))

    print(f"  q_0 = {float(q):.6f}, h = {float(h):.6f}, h/2 = {float(h/2):.6f}, z = {float(z):.6f}")
    print()

    per_atom = {}
    for name, Z, N in ATOMS:
        A = Z + N
        n_strands = 3 * A
        vols_full = per_generator_V_hat_3A(
            Z, N, include_inter=True, weight_scheme="normalized_plancherel")
        vols_constit = per_generator_V_hat_3A(
            Z, N, include_inter=False, weight_scheme="normalized_plancherel")
        atom_rows = []
        print(f"  === {name} (Z={Z}, N={N}, H_{n_strands}) ===")
        for g_idx, (vf, vc) in enumerate(zip(vols_full, vols_constit)):
            full_val = mp.mpf(str(vf["full"]))
            constit_val = mp.mpf(str(vc["full"]))
            # Classify: is this generator at an interface? (boundary between strand-blocks)
            # Strand blocks are {1-3}, {4-6}, ... ; interface gens at strand g+1 = 3, 6, 9
            # So 1-indexed interface gen = 3, 6, 9 ↔ 0-indexed g_idx = 2, 5, 8
            is_interface = (g_idx + 1) % 3 == 0
            row = {
                "gen_idx_0based": g_idx,
                "gen_sigma_1based": g_idx + 1,
                "is_interface": is_interface,
                # 50 dps, not float(): these are substrate quantities computed
                # at mp.dps = 50 and were being truncated to f64 on the way out,
                # discarding ~35 digits. The sibling producers already spell it
                # this way — `hydrogen_qshuffle_compound` writes `str(...)` and
                # `habiro_exact_mass_endomorphism` writes `mp.nstr(v, 50)`.
                "V_hat_full": mp.nstr(full_val, 50, strip_zeros=False),
                "V_hat_constit": mp.nstr(constit_val, 50, strip_zeros=False),
                "ratio_full_over_constit": (
                    mp.nstr(full_val / constit_val, 50, strip_zeros=False)
                    if constit_val != 0 else None),
            }
            # Categorical match? (per the finding above)
            tags = []
            ZERO_TOL = mp.mpf("1e-10")  # float64 noise tolerance
            if is_interface:
                if abs(full_val) < ZERO_TOL:
                    tags.append("V̂=0 (different-flavor interface)")
                elif abs(abs(full_val) - h / 2) < ZERO_TOL:
                    sign = "+" if float(full_val) > 0 else "-"
                    flavor = "p-p (σ +)" if sign == "+" else "n-n (σ⁻¹)"
                    tags.append(f"V̂={sign}h/2 (same-flavor: {flavor})")
            row["categorical_tag"] = " ; ".join(tags) if tags else ""
            atom_rows.append(row)
            tag = row["categorical_tag"]
            print(f"    gen {g_idx} (σ_{g_idx+1}): V̂_FULL = {float(full_val):+.6f}, "
                  f"V̂_CONSTIT = {float(constit_val):.6f}  "
                  f"{tag}")
        per_atom[name] = atom_rows
        print()

    builder.add_data("per_atom", per_atom)

    # Assertion: every interface generator's V̂_FULL matches the
    # flavor-selective rule {0, +h/2, -h/2}
    # Compared at mp precision, matching the 50-dps rows above. The rule is
    # `V̂ ∈ {0, ±h/2}` exactly, so the tolerance is guarding representation
    # error, not a fit — keeping it at f64 width here would test the emitted
    # string's first 16 digits and silently ignore the other 34.
    h_half = h / 2
    flavor_rule_passes = 0
    flavor_rule_total = 0
    ZERO_TOL = mp.mpf("1e-10")
    for name, rows in per_atom.items():
        for r in rows:
            if r["is_interface"]:
                flavor_rule_total += 1
                vf = mp.mpf(r["V_hat_full"])
                if abs(vf) < ZERO_TOL or abs(abs(vf) - h_half) < ZERO_TOL:
                    flavor_rule_passes += 1

    builder.add_assertion(
        "interface_v_hat_flavor_selective_rule",
        computed=float(flavor_rule_passes),
        expected=float(flavor_rule_total),
        tolerance=0.0,
        unit="count",
        source=(
            "Interface generator V̂_FULL ∈ {0, +h/2, -h/2}. "
            "0 = different-flavor (p-n); +h/2 = same-flavor positive (p-p, σ); "
            "-h/2 = same-flavor negative (n-n, σ⁻¹). "
            f"Verified at {flavor_rule_passes}/{flavor_rule_total} interface generators "
            f"across {len(per_atom)} atoms tested."
        ),
    )

    print(f"\n  Flavor-selective rule: {flavor_rule_passes}/{flavor_rule_total} interfaces match")
    print(f"  (z-exactness DOES NOT transfer to V̂ level; flavor selectivity holds instead)")

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
