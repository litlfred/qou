#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only calibration across counterfactual q.
"""
q ↔ ρ calibration — pinning the metallic ladder to physical densities.

The metallic-q phase ladder (silver = Borromean→CFL, φ² = CFL→gCFL/CCS
bar-mirror, …) is algebraically proved
(QOU.AlgebraicSubstrate.MetallicLPIdentities / MetallicHierarchy) but
the synthesis audit (2026-06-09-metallic-q-csc-phase-synthesis.md §3)
left the q ↔ baryon-density map unpinned.  This script computes the
THREE candidate calibrations the corpus supports, with no fitting —
each map is anchored by structures already in the corpus:

  Map A — kinetic / ℏ_q² scaling.  The EOS blocks
    (prop:eos-borromean-cfl) carry the compression energy
    E_comp ∝ ℏ_q² ρ^{2/3}.  Attributing the density dependence of the
    kinetic scale to the running deformation gives
        ℏ_q(ρ) = ℏ_{q0} · (ρ/ρ0)^{1/3},   q(ρ) = 1/(1 − ℏ_q(ρ)),
    anchored at q(ρ0) = q0 (nuclear saturation = substrate).

  Map B — energy-crossover anchor.  The corpus's own ρ_c criterion
    (prop:borromean-hopf-energy-crossover part 4): compression energy
    closes the Borromean−Hopf binding gap
        E_comp(ρ_c) = V_B/ℏ_{q0}² − (3/2)(q0 + q0⁻¹)   [Skein units].
    Converting to MeV via the m_p anchor and solving with the
    (relativistic and non-relativistic) Fermi gas gives ρ_c; a power
    law q(ρ) = q0 (ρ/ρ0)^α anchored by q(ρ_c) = δ_silver fixes α.

  Map C — geometric / coral-tube overlap.  The CFL conjecture's
    trigger (conj:color-superconductivity-borromean): tubes overlap
    when the inter-baryon spacing ρ^{-1/3} reaches the tube transverse
    scale |c_r| ~ r_p.  ρ_c^geom = |c_r|^{-3}; same power-law anchor.

Output: per-map predicted densities for every rung (φ, δ_silver, φ²,
δ_bronze, δ_4) in ρ0 and g/cm³, the consistency comparison (Map A vs
Map B both place silver deep, ~10²ρ0; Map C places it at ~10 ρ0),
and the observational classification (inside neutron-star reach
ρ ≲ 8 ρ0, proto-NS reach ≲ 12 ρ0, or black-hole-formation only).

No fits: every number is a consequence of corpus formulas + CODATA
constants.  The maps are alternative *identifications*, reported
side by side (tiered, not wired).
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50
HERE = Path(__file__).parent

# ── constants ──────────────────────────────────────────────────────────

try:  # canonical substrate pin
    from qou_substrate import Q0 as _Q0  # type: ignore

    Q0 = mp.mpf(str(_Q0))
except Exception:
    # same literal as the sibling metallic probes (two_quark_*, three_quark_*)
    Q0 = mp.mpf("1.1099785955541805")

V_B = mp.mpf("7.32772")  # Borromean volume (SnapPy), corpus value
M_P_MEV = mp.mpf("938.27208816")  # CODATA proton mass
HBARC_MEV_FM = mp.mpf("197.3269804")
RHO_0_FM3 = mp.mpf("0.16")  # nuclear saturation baryon density [fm^-3]
RHO_0_GCM3 = mp.mpf("2.7e14")  # the same in g/cm^3 (standard)
R_P_FM = mp.mpf("0.8414")  # CODATA proton charge radius
M_SUN_G = mp.mpf("1.98892e33")
M_B_G = mp.mpf("1.67262192e-24")  # proton mass [g]
MEV_TO_ERG = mp.mpf("1.602176634e-6")

# density reach classification (standard NS structure literature)
NS_CORE_MAX = mp.mpf(8)  # max central density of stable NS [ρ0]
PROTO_NS_MAX = mp.mpf(12)  # transient proto-NS central density [ρ0]


def hbar_q(q: mp.mpf) -> mp.mpf:
    return (q - 1) / q


def q_of_hbar(h: mp.mpf) -> mp.mpf:
    return 1 / (1 - h)


def delta_n(n: int) -> mp.mpf:
    return (mp.mpf(n) + mp.sqrt(n * n + 4)) / 2


PHI = delta_n(1)
RUNGS: list[tuple[str, mp.mpf]] = [
    ("φ", PHI),
    ("δ_silver", delta_n(2)),
    ("φ²", PHI * PHI),  # bar-mirror of q_gold = 1/φ²
    ("δ_bronze", delta_n(3)),
    ("δ_4", delta_n(4)),
]

# Skein → MeV conversion at the m_p anchor (mass formula at q0):
M_B_SKEIN = V_B / hbar_q(Q0) ** 2  # Borromean baryon mass in Skein units
SKEIN_TO_MEV = M_P_MEV / M_B_SKEIN


# ── Map A: kinetic ℏ_q² scaling ────────────────────────────────────────


def map_a_rho(q: mp.mpf) -> mp.mpf:
    """ρ/ρ0 at which Map A's running ℏ_q reaches ℏ_q(q)."""
    return (hbar_q(q) / hbar_q(Q0)) ** 3


def map_a_q(rho_ratio: mp.mpf) -> mp.mpf:
    h = hbar_q(Q0) * rho_ratio ** mp.mpf("1/3")
    return q_of_hbar(h) if h < 1 else mp.inf


# ── Map B: energy-crossover anchor ─────────────────────────────────────


def crossover_gap_mev() -> mp.mpf:
    """Binding gap the compression energy must close (Skein → MeV)."""
    gap_skein = V_B / hbar_q(Q0) ** 2 - mp.mpf(3) / 2 * (Q0 + 1 / Q0)
    return gap_skein * SKEIN_TO_MEV


def k_fermi_mev(rho_ratio: mp.mpf) -> mp.mpf:
    """ℏc·k_F [MeV] for baryon density ρ = rho_ratio·ρ0 (degeneracy 2,
    matching the (3π²n)^{1/3} convention of the EOS block)."""
    k_fm = (3 * mp.pi**2 * RHO_0_FM3 * rho_ratio) ** mp.mpf("1/3")
    return HBARC_MEV_FM * k_fm


def map_b_rho_c(relativistic: bool) -> mp.mpf:
    """ρ_c/ρ0 where E_comp closes the gap."""
    gap = crossover_gap_mev()
    if relativistic:
        kc = mp.sqrt((M_P_MEV + gap) ** 2 - M_P_MEV**2)
    else:
        kc = mp.sqrt(2 * M_P_MEV * gap)
    return (kc / k_fermi_mev(mp.mpf(1))) ** 3


# ── Map C: coral-tube overlap ──────────────────────────────────────────


def map_c_rho_c(c_r_fm: mp.mpf) -> mp.mpf:
    """ρ_c/ρ0 where inter-baryon spacing ρ^{-1/3} = |c_r|."""
    spacing_0 = RHO_0_FM3 ** mp.mpf("-1/3")
    return (spacing_0 / c_r_fm) ** 3


# ── power-law maps anchored at (ρ_c, δ_silver) ─────────────────────────


def alpha_for(rho_c_ratio: mp.mpf) -> mp.mpf:
    return mp.log(delta_n(2) / Q0) / mp.log(rho_c_ratio)


def powerlaw_rho(q: mp.mpf, alpha: mp.mpf) -> mp.mpf:
    return (q / Q0) ** (1 / alpha)


def reach(rho_ratio: mp.mpf) -> str:
    if rho_ratio <= NS_CORE_MAX:
        return "NS core"
    if rho_ratio <= PROTO_NS_MAX:
        return "proto-NS (transient)"
    return "BH-formation only"


def main() -> None:
    maps: dict[str, dict] = {}

    # Map A
    rows_a = []
    for name, q in RUNGS:
        rr = map_a_rho(q)
        rows_a.append({
            "rung": name, "q": mp.nstr(q, 12),
            "rho_over_rho0": mp.nstr(rr, 8),
            "rho_gcm3": mp.nstr(rr * RHO_0_GCM3, 6),
            "reach": reach(rr),
        })
    maps["A_kinetic_hbar_q"] = {
        "form": "hbar_q(rho) = hbar_q(q0)·(rho/rho0)^(1/3); q = 1/(1−hbar_q)",
        "anchor": "q(rho0) = q0 (saturation = substrate)",
        "rungs": rows_a,
    }

    # Map B
    gap = crossover_gap_mev()
    for tag, rel in (("relativistic", True), ("non_relativistic", False)):
        rc = map_b_rho_c(rel)
        al = alpha_for(rc)
        rows = []
        for name, q in RUNGS:
            rr = powerlaw_rho(q, al)
            rows.append({
                "rung": name, "q": mp.nstr(q, 12),
                "rho_over_rho0": mp.nstr(rr, 8),
                "rho_gcm3": mp.nstr(rr * RHO_0_GCM3, 6),
                "reach": reach(rr),
            })
        maps[f"B_energy_crossover_{tag}"] = {
            "form": "q(rho) = q0·(rho/rho0)^alpha",
            "anchor": (
                "E_comp(rho_c) closes the Borromean−Hopf gap "
                f"({mp.nstr(gap, 6)} MeV/baryon); q(rho_c) = δ_silver"
            ),
            "rho_c_over_rho0": mp.nstr(rc, 8),
            "alpha": mp.nstr(al, 8),
            "rungs": rows,
        }

    # Map C (central r_p + honest bracket)
    for tag, cr in (("rp", R_P_FM), ("0p6fm", mp.mpf("0.6")),
                    ("1p0fm", mp.mpf("1.0"))):
        rc = map_c_rho_c(cr)
        al = alpha_for(rc)
        rows = []
        for name, q in RUNGS:
            rr = powerlaw_rho(q, al)
            rows.append({
                "rung": name, "q": mp.nstr(q, 12),
                "rho_over_rho0": mp.nstr(rr, 8),
                "rho_gcm3": mp.nstr(rr * RHO_0_GCM3, 6),
                "reach": reach(rr),
            })
        maps[f"C_coral_tube_{tag}"] = {
            "form": "q(rho) = q0·(rho/rho0)^alpha",
            "anchor": (
                f"tube overlap: rho_c^(-1/3) = |c_r| = {mp.nstr(cr, 5)} fm; "
                "q(rho_c) = δ_silver"
            ),
            "rho_c_over_rho0": mp.nstr(rc, 8),
            "alpha": mp.nstr(al, 8),
            "rungs": rows,
        }

    # consistency + classification summary
    silver_a = map_a_rho(delta_n(2))
    silver_b_rel = map_b_rho_c(True)
    silver_b_nr = map_b_rho_c(False)
    silver_c = map_c_rho_c(R_P_FM)
    summary = {
        "silver_placement_rho0": {
            "A_kinetic": mp.nstr(silver_a, 6),
            "B_crossover_rel": mp.nstr(silver_b_rel, 6),
            "B_crossover_nonrel": mp.nstr(silver_b_nr, 6),
            "C_coral_tube_rp": mp.nstr(silver_c, 6),
        },
        "deep_vs_shallow": (
            "Maps A and B (independent routes: running-ℏ_q kinetic scale "
            "vs corpus gap-closure criterion) BOTH place silver deep, "
            "O(10²)·ρ0 — beyond any neutron-star central density: no CFL "
            "core in stable NS, no NICER kink, cascade only inside "
            "BH-forming collapse.  Map C (the conjecture's own geometric "
            "trigger) places silver at ~10 ρ0 — reachable in the heaviest "
            "proto-NS: NICER kink + delayed second neutrino burst become "
            "live predictions.  The two placements are observationally "
            "distinguishable; neither is wired as canonical."
        ),
        "map_c_golden_rung_note": (
            "Under Map C the FIRST rung φ lands at "
            f"{mp.nstr(powerlaw_rho(PHI, alpha_for(silver_c)), 5)} ρ0 — "
            "the density band where hyperons appear in standard NS "
            "physics and in the corpus's own layered table "
            "(conj:color-superconductivity-borromean §phase sequence: "
            "outer core ρ0..2ρ0 hyperonic).  Structural echo, not a fit."
        ),
    }

    # assertions (internal identities, not physics)
    assert abs(PHI * PHI + 1 / (PHI * PHI) - 3) < mp.mpf(10) ** -40, \
        "φ² + φ⁻² = 3 (Lucas) failed"
    assert abs(hbar_q(PHI) - 1 / PHI**2) < mp.mpf(10) ** -40, \
        "ℏ_q(φ) = 1/φ² = q_gold failed"
    a_check = abs(map_a_q(map_a_rho(delta_n(3))) - delta_n(3))
    assert a_check < mp.mpf(10) ** -40, "Map A roundtrip failed"

    witness = {
        "description": (
            "q ↔ ρ calibration for the metallic phase ladder: three "
            "corpus-anchored maps (A kinetic ℏ_q² scaling, B energy-"
            "crossover gap closure, C coral-tube geometric overlap), "
            "each pinning ρ(δ_silver) and predicting the densities of "
            "every rung (φ, δ_silver, φ², δ_bronze, δ_4).  Tiered "
            "alternative identifications — none wired as canonical."
        ),
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "script": "metallic_q_rho_calibration.py",
        "constants": {
            "q0": mp.nstr(Q0, 17),
            "hbar_q0": mp.nstr(hbar_q(Q0), 12),
            "V_B": mp.nstr(V_B, 8),
            "M_B_skein": mp.nstr(M_B_SKEIN, 8),
            "skein_to_MeV": mp.nstr(SKEIN_TO_MEV, 8),
            "rho0_fm3": mp.nstr(RHO_0_FM3, 4),
            "rho0_gcm3": mp.nstr(RHO_0_GCM3, 4),
            "crossover_gap_MeV": mp.nstr(crossover_gap_mev(), 8),
        },
        "structural_identities": {
            "hbar_q(φ) = 1/φ² = q_gold": True,
            "φ² + φ⁻² = 3": True,
            "note": (
                "ℏ_q at the golden rung equals the corpus deconfinement "
                "boundary q_gold = 1/φ² exactly; the φ² rung's Hecke "
                "scalar sum is the integer 3 (Lucas L_2).  Both verified "
                "at 40+ dps."
            ),
        },
        "maps": maps,
        "summary": summary,
        "limitations": [
            "Map A attributes ALL density dependence of the kinetic "
            "scale to a running ℏ_q — an identification, not a "
            "derivation; the EOS blocks treat ℏ_q as fixed at q0.",
            "Map B inherits the corpus crossover criterion's Fermi-gas "
            "form; relativistic vs non-relativistic bracket spans "
            "~×1.8 in ρ_c.",
            "Map C's |c_r| (coral-tube transverse scale) is bracketed "
            "0.6–1.0 fm around r_p; the corpus does not pin it.",
            "ρ0 reach thresholds (8 ρ0 stable NS, 12 ρ0 proto-NS) are "
            "standard-literature round numbers, not corpus outputs.",
        ],
    }
    out = HERE / "metallic-q-rho-calibration.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Saved witness: {out}", file=sys.stderr)

    # console table
    for mname, m in maps.items():
        print(f"\n── {mname}  (anchor: {m['anchor']})")
        for r in m["rungs"]:
            print(f"  {r['rung']:9s} q={float(mp.mpf(r['q'])):8.4f}  "
                  f"ρ={float(mp.mpf(r['rho_over_rho0'])):10.3f} ρ0  "
                  f"[{r['reach']}]")
    print("\nSilver placement (ρ0):", json.dumps(
        summary["silver_placement_rho0"], indent=2))


if __name__ == "__main__":
    main()
