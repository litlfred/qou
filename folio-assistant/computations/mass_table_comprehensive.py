#!/usr/bin/env python3
"""mass_table_comprehensive.py — full mass/binding table at current production tier.

Computes absolute masses AND binding energies for all nuclei from
proton (A=1) through ¹²C (A=12), using the current production
infrastructure:

  ABSOLUTE MASS:
    m(K) = m_e · [Vol(𝓑₃)/ℏ_q²] · λ_A · (1 ± Δm/(2·M_N))

  where λ_A = Family A (PROVED), Δm/M_N = substrate-pure flavor-split
  (PROVED per PR #942). Proton gets −Δm/2, neutron gets +Δm/2.
  Composite nucleus mass = Z·m_p + N·m_n − B(K).

  BINDING ENERGY:
    For A ≤ 3: binding_canonical with use_closed_form=True (PR #921;
    the Phase 5q closed form via tr_M_via_wenzl_bridge_mpfr).
    For A = 4: binding_canonical (H_12 Phase-1 extract wired via
    #944; currently closed-form path uses strict_averaged).
    For A ≥ 5: flagged as "not yet computed" (gated on H_12 Phase-2
    + higher H_{3A} kernels).

  KNOT ATLAS CROSS-REFERENCE:
    Each entry carries the methodology tag from the recursive atom
    knot atlas (prop:recursive-atom-knot-atlas) — principled-derivation,
    manual-historical-volume-match, magic-A-formula, recursive-on-⁴He,
    or not-computed.

Emits: mass-table-comprehensive.witness.json

Per CLAUDE.md "Long-compute logging discipline": periodic progress
lines with wall + ETA.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_E_MEV,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
    Q_BETA_MEV,
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
    AME_B_LI6_MEV_VALIDATION, AME_B_LI7_MEV_VALIDATION,
)
from _li_2_q_util import (  # noqa: E402
    linking_weight_family_a,
    flavor_split_subleading,
    vol_density_borromean,
)
from witness_base import WitnessBuilder  # noqa: E402

# AME 2020 binding energies (MeV) — used for comparison only.
# Source: Wang et al., Chinese Physics C 45 (2021) 030003.
AME_BINDING = {
    "p": 0.0, "n": 0.0,
    "D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION, "6Li": AME_B_LI6_MEV_VALIDATION, "7Li": AME_B_LI7_MEV_VALIDATION,
    "9Be": 58.165, "10B": 64.751, "11B": 76.205,
    "12C": 92.162, "13C": 97.108, "14N": 104.659, "15N": 115.492,
    "16O": 127.619, "17O": 131.763, "18O": 139.808,
    "19F": 147.801, "20Ne": 160.645, "21Ne": 167.406, "22Ne": 177.770,
    "23Na": 186.564, "24Mg": 198.257, "25Mg": 205.588, "26Mg": 216.681,
    "27Al": 224.952, "28Si": 236.537, "29Si": 245.011, "30Si": 255.620,
    "31P": 262.917, "32S": 271.781, "33S": 280.422, "34S": 291.839,
    "36S": 308.714, "35Cl": 298.210, "37Cl": 317.100,
    "36Ar": 306.716, "38Ar": 327.343, "40Ar": 343.810,
    "39K": 333.723, "41K": 351.619,
    "40Ca": 342.052, "42Ca": 361.895, "43Ca": 369.828,
    "44Ca": 380.960, "46Ca": 398.769, "48Ca": 416.001,
    "45Sc": 387.849,
    "46Ti": 398.194, "47Ti": 407.073, "48Ti": 418.699,
    "49Ti": 426.841, "50Ti": 437.780,
    "50V": 434.794, "51V": 445.842,
    "50Cr": 435.049, "52Cr": 456.345, "53Cr": 464.287, "54Cr": 474.008,
    "55Mn": 482.071,
    "54Fe": 471.764, "56Fe": 492.254, "57Fe": 499.900, "58Fe": 509.946,
}

# CODATA masses (MeV) for cross-check
CODATA_MASS = {
    "p": float(M_P_MEV_VALIDATION),
    "n": float(M_N_MEV_VALIDATION),
    "D": float(M_D_MEV_VALIDATION),
    "T": float(M_T_MEV_VALIDATION),
    "3He": None,  # not in codata_constants; derive from AME
    "4He": float(M_HE4_MEV_VALIDATION),
}

# Atlas methodology tags (from recursive-atom-knot-atlas.md)
ATLAS_TAG = {
    "p": "principled-derivation",
    "n": "principled-derivation",
    "D": "manual-historical-volume-match",
    "T": "manual-historical-volume-match",
    "3He": "manual-historical-volume-match",
    "4He": "magic-A-formula",
    "6Li": "deprecated-volume-match",
    "7Li": "deprecated-volume-match",
    "9Be": "recursive-on-4He",
    "10B": "recursive-on-4He",
    "12C": "recursive-on-4He",
}

ELEMENTS = [
    "n", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

ISOTOPES = [("p", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2)]
# Add grid of theoretical isotopes up to Z=118, roughly spanning from proton to neutron drip line
for z in range(2, 119):
    n_min = max(0, int(0.5 * z) - 2)
    n_max = int(2.5 * z) + 5
    for n in range(n_min, n_max + 1):
        a = z + n
        if a > 4:  # Avoid duplicates with explicitly added H, He isotopes
            sym = f"{a}{ELEMENTS[z]}"
            ISOTOPES.append((sym, z, n))


def borromean_mass_prediction(
    q: mp.mpf, Z: int, N: int, atom_name: str = None,
) -> dict:
    """Predict absolute mass of nucleus (Z, N) via the Borromean
    baryon mass formula (Family A + substrate-pure flavor-split).

    m_avg = m_e · Vol(𝓑₃)/ℏ_q² · λ_A
    m_p_pred = m_avg · (1 − Δm/(2·M_N))
    m_n_pred = m_avg · (1 + Δm/(2·M_N))
    m_nucleus = Z · m_p_pred + N · m_n_pred − B(K)

    If Vol(K) is available for the atom, uses the truth-tracking
    per-knot formula: m(K) = m_e · VolDensity(K, q₀)
    """
    m_e = mp.mpf(str(M_E_MEV))

    # Load substrate identity predictions (sub-ppb accuracy)
    # from the canonical witness, falling back to Family A if unavailable.
    sub_witness = _pb.witness_path("m-p-substrate-identity-50dps.witness.json", HERE)
    if sub_witness.exists():
        import json as _json
        sub_data = _json.load(sub_witness.open())
        preds = sub_data["data"]["predictions"]
        m_p_pred = mp.mpf(str(preds["m_p_MeV"]))
        m_n_pred = mp.mpf(str(preds["m_n_MeV"]))
        # Apply Habiro brane-tower correction (PR #1346)
        hbar_q = (q - 1) / q
        b_val = ((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2) ** mp.mpf("0.5")
        u_val = b_val * hbar_q ** 2
        habiro_ratio = (1 + 46 * u_val ** 4) * (1 + 4 * u_val ** 5) * (1 - 29 * u_val ** 6)
        m_p_pred = m_p_pred * habiro_ratio
        m_n_pred = m_n_pred * habiro_ratio
        _source = "substrate-identity + Habiro brane-tower"
    else:
        vol_density = vol_density_borromean(q)
        delta_m_over_M = flavor_split_subleading(q)
        m_avg = m_e * vol_density
        m_p_pred = m_avg * (1 - delta_m_over_M / 2)
        m_n_pred = m_avg * (1 + delta_m_over_M / 2)
        _source = "Family A (fallback)"
    linking_weight = linking_weight_family_a(q)

    # Base definition (q-CLT statistical average)
    m_nucleus_unbound_approx = Z * float(m_p_pred) + N * float(m_n_pred)

    # TRUTH-TRACKING OVERRIDE (per-knot VolDensity, symbolic top-down)
    m_nucleus_unbound_symbolic = None
    vol_K_used = None
    if atom_name is not None:
        try:
            import json as _json
            vol_witness = HERE / "per-atom-hyperbolic-volume.witness.json"
            if vol_witness.exists():
                vol_data = _json.load(vol_witness.open())["data"]
                vol_key = f"Vol_{atom_name}"
                if vol_key in vol_data:
                    from closed_form_tau_M import compute_tau_M_nucleon_H3, closed_form_tau_M
                    from _li_2_q_util import vol_density_per_block
                    tau_p_H3 = compute_tau_M_nucleon_H3("p", q)
                    tau_n_H3 = compute_tau_M_nucleon_H3("n", q)
                    tr_M_K = closed_form_tau_M(Z, N, q, tau_p_H3, tau_n_H3)
                    vol_K_used = mp.mpf(str(vol_data[vol_key]))
                    m_pb = m_e * vol_density_per_block(vol_K_used, tr_M_K, q)
                    m_nucleus_unbound_symbolic = float(m_pb)
                    _source += " [OVERRIDE: per-knot VolDensity]"
                else:
                    _source += " [ERROR: missing Vol(K)]"
            else:
                _source += " [ERROR: missing per-atom-hyperbolic-volume.witness.json]"
        except Exception as e:
            _source += f" [ERROR: {e}]"

    m_avg = (m_p_pred + m_n_pred) / 2
    return {
        "linking_weight_family_a": float(linking_weight),
        "source": _source,
        "m_avg_MeV": float(m_avg),
        "m_p_pred_MeV": float(m_p_pred),
        "m_n_pred_MeV": float(m_n_pred),
        "m_nucleus_unbound_approx_MeV": float(m_nucleus_unbound_approx),
        "m_nucleus_unbound_symbolic_MeV": float(m_nucleus_unbound_symbolic) if m_nucleus_unbound_symbolic is not None else None,
        "vol_K": float(vol_K_used) if vol_K_used else None,
        "is_per_knot": m_nucleus_unbound_symbolic is not None,
    }


def try_binding_canonical(Z: int, N: int, q_str: str) -> dict | None:
    """Try to compute binding energy via binding_canonical with
    closed-form path. Returns None if the computation fails.

    Computes BOTH Q_β-scaled (legacy) and E₀×q⁻¹-scaled (PR #1361)
    results for comparison."""
    A = Z + N
    if A < 2:
        return {"B_pred_MeV": 0.0, "B_E0_MeV": 0.0, "method": "no binding (single nucleon)"}

    # If A>12 and alpha cluster, try alpha_cluster_binding first
    if A > 12 and Z == N and A % 4 == 0:
        try:
            from alpha.alpha_cluster_recursion import alpha_cluster_binding
            r = alpha_cluster_binding(Z, N)
            if r.get("applicable"):
                return {
                    "B_pred_MeV": float(r["B_pred_MeV"]),
                    "B_E0_MeV": float(r["B_pred_MeV"]),  # same scale
                    "method": "alpha_cluster_recursion (recursive-on-⁴He)",
                    "formula": r.get("formula"),
                }
        except Exception as e:
            print(
                f"WARN: alpha_cluster_binding failed for (Z={Z}, N={N}, A={A}): {e!s}",
                file=sys.stderr,
            )

    try:
        from binding_canonical import binding_canonical
        r = binding_canonical(
            Z, N,
            Q_beta_n_mev=float(Q_BETA_MEV),
            use_closed_form=True,
            verbose=False,
        )
        if r.get("status") != "solved":
            return {"B_pred_MeV": None, "method": f"binding_canonical failed: {r.get('status')}", "error": r.get("error")}

        B_qbeta = r.get("B_MeV")

        # E₀×q⁻¹ scale (PR #1361): B = E₀ × Δtr × (1-ℏ_q)
        # where E₀ = m_e/(q₀(q₀-1)), (1-ℏ_q) = q₀⁻¹
        import mpmath as _mp
        q_val = _mp.mpf(q_str)
        E_0 = float(M_E_MEV) / float(q_val * (q_val - 1))
        scale_ratio = E_0 / float(Q_BETA_MEV) * float(1 / q_val)
        B_E0 = B_qbeta * scale_ratio if B_qbeta else None

        return {
            "B_pred_MeV": B_E0,  # use E₀×q⁻¹ as primary
            "B_qbeta_MeV": B_qbeta,
            "tr_M_atom": r.get("tr_M_atom"),
            "tr_M_free": r.get("tr_M_free"),
            "method": "E₀×q⁻¹ (PR #1361)" + (" (closed-form)" if A <= 3 else " (symbolic)"),
        }
    except Exception as e:
        return {"B_pred_MeV": None, "method": f"error: {e}"}


def main() -> int:
    t_start = time.monotonic()
    builder = WitnessBuilder(
        "mass-table-comprehensive",
        engine="mpmath",
        start_time=t_start,
    )
    builder.set_description(
        "Comprehensive mass/binding table for all nuclei from proton "
        "(A=1) through ¹²C (A=12) at the current production tier: "
        "Family A λ_A = 5/2 + (3/4)h² (PROVED) + substrate-pure "
        "flavor-split Δm/M_N (PROVED, PR #942). Binding energies "
        "via binding_canonical with use_closed_form=True for A ≤ 3 "
        "(PR #921). A = 4 uses symbolic path. A ≥ 5 flagged as "
        "'not yet computed'. Each entry cross-references the "
        "recursive atom knot atlas methodology tag."
    )
    builder.set_content_block("prop:recursive-atom-knot-atlas")
    builder.add_parameter("q_str", Q_50_DIGIT_STR)
    # dps is captured authoritatively in precisionMetadata.compute_dps;
    # not duplicated here (see Copilot review #1756, witness-line 23/40).

    q = mp.mpf(Q_50_DIGIT_STR)

    # Compute nucleon masses once
    nucleon = borromean_mass_prediction(q, 1, 0)
    m_p_pred = nucleon["m_p_pred_MeV"]
    m_n_pred = nucleon["m_n_pred_MeV"]

    print("=" * 120)
    print("COMPREHENSIVE MASS TABLE — QOU framework at current production tier")
    print(f"  q₀ = {Q_50_DIGIT_STR[:25]}...")
    print(f"  source: {nucleon.get('source', 'Family A')}")
    print(f"  linking_weight (Family A, PROVED) = {nucleon['linking_weight_family_a']:.10f}")
    print(f"  m_p^pred = {m_p_pred:.6f} MeV   (CODATA: {float(M_P_MEV_VALIDATION):.6f})")
    print(f"  m_n^pred = {m_n_pred:.6f} MeV   (CODATA: {float(M_N_MEV_VALIDATION):.6f})")
    print("=" * 120)
    print()
    print(f"\n{'Atom':>5s} {'Z':>2s} {'N':>2s} {'A':>2s}  "
          f"{'m_symbolic':>14s} {'m_qCLT_approx':>14s} {'m_observed':>14s}  "
          f"{'B_pred':>12s} {'B_AME':>11s}  "
          f"{'Methodology':>30s}  Caveats")
    print("-" * 140)

    rows = []
    mt_ppb_path = _pb.witness_path("mass-table-ppb.witness.json", HERE)
    mt_ppb_data = None
    if mt_ppb_path.exists():
        import json as _json
        mt_ppb_data = _json.load(mt_ppb_path.open())

    for i, (name, Z, N) in enumerate(ISOTOPES):
        A = Z + N
        t0 = time.monotonic()

        nucleon = borromean_mass_prediction(q, Z, N, name)
        m_unbound_approx = nucleon.get("m_nucleus_unbound_approx_MeV")
        m_unbound_symbolic = nucleon.get("m_nucleus_unbound_symbolic_MeV")

        # Binding energy
        binding = try_binding_canonical(Z, N, Q_50_DIGIT_STR)

        B_pred = 0.0
        B_method = "n/a"
        if binding is not None:
            B_pred = binding.get("B_pred_MeV") or 0.0
            B_method = binding.get("method", "?")
            
        # FALLBACK: if canonical binding is not available, use the legacy mass-table-ppb
        if (binding is None or B_pred == 0.0) and A >= 2:
            if mt_ppb_data is not None:
                for r in mt_ppb_data.get("data", {}).get("rows", []):
                    if r.get("Z") == Z and r.get("N") == N:
                        b_val = r.get("B_pred_MeV")
                        if b_val is not None:
                            B_pred = float(b_val)
                            B_method = "legacy (mass-table-ppb)"
                        break

        m_approx = (m_unbound_approx - B_pred) if (m_unbound_approx is not None and (B_pred > 0 or A == 1)) else None
        m_symbolic = (m_unbound_symbolic - B_pred) if (m_unbound_symbolic is not None and (B_pred > 0 or A == 1)) else None
        B_AME = AME_BINDING.get(name, 0.0)

        # CODATA/AME observed mass for comparison
        m_observed = CODATA_MASS.get(name)
        if m_observed is None and B_AME > 0:
            # Derive from AME: m = Z·m_p + N·m_n - B_AME (using CODATA nucleon masses)
            m_observed = (
                Z * float(M_P_MEV_VALIDATION)
                + N * float(M_N_MEV_VALIDATION)
                - B_AME
            )

        # Errors against Observed
        m_err_pct_approx = ((m_approx - m_observed) / m_observed * 100) if (m_observed and m_approx is not None) else None
        m_err_pct_sym = ((m_symbolic - m_observed) / m_observed * 100) if (m_observed and m_symbolic is not None) else None
        B_err_pct = ((B_pred - B_AME) / B_AME * 100) if B_AME > 0 else None

        # Caveats
        caveats = []
        caveats.append("Family A λ_A (PROVED)")
        if Z > 0 and N > 0:
            caveats.append("flavor-split (PROVED)")
        if binding is None:
            caveats.append("B NOT COMPUTED (gated on H_{3A} kernel)")
        elif B_pred == 0 and A > 1:
            caveats.append(f"B computation failed: {B_method}")
        if A > 4:
            caveats.append("H_{3A} kernel not available (Phase-2 gated)")

        atlas_tag = ATLAS_TAG.get(name, "not-in-atlas")

        row = {
            "atom": name,
            "Z": Z, "N": N, "A": A,
            "m_approx_MeV": round(m_approx, 6) if m_approx else None,
            "m_symbolic_MeV": round(m_symbolic, 6) if m_symbolic else None,
            "m_observed_MeV": round(m_observed, 6) if m_observed else None,
            "m_err_pct_approx": round(m_err_pct_approx, 4) if m_err_pct_approx is not None else None,
            "m_err_pct_sym": round(m_err_pct_sym, 4) if m_err_pct_sym is not None else None,
            "B_pred_MeV": round(B_pred, 6) if B_pred else None,
            "B_AME_MeV": round(B_AME, 6),
            "B_err_pct": round(B_err_pct, 4) if B_err_pct is not None else None,
            "binding_method": B_method,
            "atlas_methodology_tag": atlas_tag,
            "caveats": caveats,
        }
        rows.append(row)

        # Print row
        m_sym_s = f"{float(m_symbolic):14.6f}" if m_symbolic else "           n/a"
        m_app_s = f"{float(m_approx):14.6f}" if m_approx else "           n/a"
        m_obs_s = f"{float(m_observed):14.6f}" if m_observed else "           n/a"
        B_pred_s = f"{float(B_pred):12.6f}" if B_pred else "         n/a"
        B_AME_s = f"{float(B_AME):11.6f}"

        elapsed = time.monotonic() - t0
        print(f"{name:>5s} {Z:>2d} {N:>2d} {A:>2d}  "
              f"{m_sym_s} {m_app_s} {m_obs_s}  "
              f"{B_pred_s} {B_AME_s}  "
              f"{atlas_tag:>30s}  "
              f"{'|'.join(caveats[:2])}"
              f"  [{elapsed:.1f}s]")

    # Summary
    print()
    n_computed = sum(1 for r in rows if r["m_approx_MeV"] is not None)
    n_binding = sum(1 for r in rows if r["B_pred_MeV"] and r["B_pred_MeV"] > 0)
    n_gated = sum(1 for r in rows if any("gated" in c for c in r["caveats"]))
    print(f"Summary: {n_computed}/{len(rows)} masses computed; "
          f"{n_binding}/{len(rows)} binding energies computed; "
          f"{n_gated} gated on H_{{3A}} Phase-2.")

    builder.add_data("rows", rows)
    builder.add_data("summary", {
        "total_isotopes": len(rows),
        "masses_computed": n_computed,
        "binding_computed": n_binding,
        "gated_on_phase2": n_gated,
        # NOTE: keys below are populated only when `predict_p_n` returns
        # via the Family-A fallback path; the substrate-identity path
        # (canonical, post-2026-05-23 absorption of λ_scale into
        # VolDensity) does not emit them. Hence .get() — None here means
        # "substrate-identity path was taken", NOT "compute failure".
        # See `nucleon_path` field below for which path was used.
        "nucleon_path": nucleon.get(
            "path",
            "family_a" if "linking_weight_family_a" in nucleon else "substrate_identity",
        ),
        "linking_weight_family_a": nucleon.get("linking_weight_family_a"),
        "vol_density_borromean_q": nucleon.get("vol_density_borromean_q"),
        "delta_m_over_M_N": nucleon.get("delta_m_over_M_N"),
        "m_p_pred_MeV": m_p_pred,
        "m_n_pred_MeV": m_n_pred,
        "production_tier": (
            "VolDensity(𝓑₃, q) via PROVED Family A linking_weight "
            "+ flavor-split (PROVED) — PR #1080 canonical framing"
        ),
        "research_tier_not_used": (
            "Strategy I linking_weight = Family A − G·h² "
            "(conjectural bijection, PURGED 2026-05-24 per PR #985)"
        ),
    })

    builder.add_assertion(
        name="all_A_leq_4_masses_computed",
        computed=float(all(
            r["m_approx_MeV"] is not None
            for r in rows if r["A"] <= 4
        )),
        expected=1.0,
        tolerance=0.0,
        source="All A ≤ 4 isotopes have absolute mass predictions",
    )

    builder.add_caveat(
        "Production tier uses Family A λ_A = 5/2 + (3/4)h² (PROVED, "
        "+2.89% from CODATA on m_p) + substrate-pure flavor-split "
        "(PROVED, 0.03% ratio match). Strategy I (λ_Y = λ_A − G·h², "
        "+1.33%) is NOT used in this mass table — it requires the "
        "Yekutieli bijection proof (research-grade; PR #978 / #991). "
        "Binding energies for A ≥ 5 are NOT computed — gated on H_12 "
        "Phase-2 (≥3500 test words; PR #944 delivered Phase-1 for A ≤ 4). "
        "Atlas methodology tags from prop:recursive-atom-knot-atlas."
    )

    out = builder.save()
    print(f"\n→ Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
