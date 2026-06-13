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
    "D": 2.22452, "T": 8.481821, "3He": 7.71804,
    "4He": 28.2957, "6Li": 31.994, "7Li": 39.2445,
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

# ALL stable isotopes from H through Fe (63 isotopes).
# Source: NUBASE2020 (Kondev et al., Chinese Physics C 45, 2021).
# Per user direction 2026-05-24: "do all nucleotides".
ISOTOPES = [
    # Z=1 Hydrogen
    ("p",     1,  0), ("n",     0,  1), ("D",     1,  1), ("T",     1,  2),
    # Z=2 Helium
    ("3He",   2,  1), ("4He",   2,  2),
    # Z=3 Lithium
    ("6Li",   3,  3), ("7Li",   3,  4),
    # Z=4 Beryllium
    ("9Be",   4,  5),
    # Z=5 Boron
    ("10B",   5,  5), ("11B",   5,  6),
    # Z=6 Carbon
    ("12C",   6,  6), ("13C",   6,  7),
    # Z=7 Nitrogen
    ("14N",   7,  7), ("15N",   7,  8),
    # Z=8 Oxygen
    ("16O",   8,  8), ("17O",   8,  9), ("18O",   8, 10),
    # Z=9 Fluorine
    ("19F",   9, 10),
    # Z=10 Neon
    ("20Ne", 10, 10), ("21Ne", 10, 11), ("22Ne", 10, 12),
    # Z=11 Sodium
    ("23Na", 11, 12),
    # Z=12 Magnesium
    ("24Mg", 12, 12), ("25Mg", 12, 13), ("26Mg", 12, 14),
    # Z=13 Aluminum
    ("27Al", 13, 14),
    # Z=14 Silicon
    ("28Si", 14, 14), ("29Si", 14, 15), ("30Si", 14, 16),
    # Z=15 Phosphorus
    ("31P",  15, 16),
    # Z=16 Sulfur
    ("32S",  16, 16), ("33S",  16, 17), ("34S",  16, 18), ("36S",  16, 20),
    # Z=17 Chlorine
    ("35Cl", 17, 18), ("37Cl", 17, 20),
    # Z=18 Argon
    ("36Ar", 18, 18), ("38Ar", 18, 20), ("40Ar", 18, 22),
    # Z=19 Potassium
    ("39K",  19, 20), ("41K",  19, 22),
    # Z=20 Calcium
    ("40Ca", 20, 20), ("42Ca", 20, 22), ("43Ca", 20, 23),
    ("44Ca", 20, 24), ("46Ca", 20, 26), ("48Ca", 20, 28),
    # Z=21 Scandium
    ("45Sc", 21, 24),
    # Z=22 Titanium
    ("46Ti", 22, 24), ("47Ti", 22, 25), ("48Ti", 22, 26),
    ("49Ti", 22, 27), ("50Ti", 22, 28),
    # Z=23 Vanadium
    ("50V",  23, 27), ("51V",  23, 28),
    # Z=24 Chromium
    ("50Cr", 24, 26), ("52Cr", 24, 28), ("53Cr", 24, 29), ("54Cr", 24, 30),
    # Z=25 Manganese
    ("55Mn", 25, 30),
    # Z=26 Iron
    ("54Fe", 26, 28), ("56Fe", 26, 30), ("57Fe", 26, 31), ("58Fe", 26, 32),
]


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

    # Nucleus mass (before binding): Z protons + N neutrons
    m_nucleus_unbound = Z * m_p_pred + N * m_n_pred

    # TRUTH-TRACKING OVERRIDE (per-knot VolDensity)
    m_pb = None
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
                    m_nucleus_unbound = m_pb
                    _source += " [OVERRIDE: per-knot VolDensity]"
                else:
                    m_nucleus_unbound = None
                    _source += " [ERROR: missing Vol(K)]"
            else:
                m_nucleus_unbound = None
                _source += " [ERROR: missing per-atom-hyperbolic-volume.witness.json]"
        except Exception as e:
            m_nucleus_unbound = None
            _source += f" [ERROR: {e}]"

    m_avg = (m_p_pred + m_n_pred) / 2
    return {
        "linking_weight_family_a": float(linking_weight),
        "source": _source,
        "m_avg_MeV": float(m_avg),
        "m_p_pred_MeV": float(m_p_pred),
        "m_n_pred_MeV": float(m_n_pred),
        "m_nucleus_unbound_MeV": float(m_nucleus_unbound) if m_nucleus_unbound is not None else None,
        "vol_K": float(vol_K_used) if vol_K_used else None,
        "is_per_knot": m_pb is not None,
    }


def try_binding_canonical(Z: int, N: int, q_str: str) -> dict | None:
    """Try to compute binding energy via binding_canonical with
    closed-form path. Returns None if the atom is too heavy (A > 4)
    or if the computation fails.

    Computes BOTH Q_β-scaled (legacy) and E₀×q⁻¹-scaled (PR #1361)
    results for comparison."""
    A = Z + N
    if A < 2:
        return {"B_pred_MeV": 0.0, "B_E0_MeV": 0.0, "method": "no binding (single nucleon)"}
    if A > 12:
        # H_{3A} kernel gated for non-α-cluster atoms; but the
        # `recursive-on-⁴He` atlas methodology covers Z=N, A%4==0
        # via B(nα) = n·B(⁴He) + C(n,2)·c_αα. Wire it in here
        # for the A>12 α-cluster atoms — ¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si,
        # ³²S, ³⁶Ar, ⁴⁰Ca (⁸Be / ¹²C are A≤12 so they go through
        # the existing binding_canonical branch below, not here).
        # User request 2026-06-03: "wire up ALL isotopes properly".
        # Closure is zero-fit: B(⁴He) from magic-A formula,
        # c_αα = m_e · Vol(7²_1) (Whitehead link).
        if Z == N and A % 4 == 0:
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
                # Surface the failure to stderr so regressions don't go
                # silent in production runs; still return None to keep
                # the gated-isotope contract intact.
                print(
                    f"WARN: alpha_cluster_binding failed for "
                    f"(Z={Z}, N={N}, A={A}): {e!s}",
                    file=sys.stderr,
                )
                return None
        return None  # gated on H_{3A} kernel availability

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
    print(f"{'Atom':>5s} {'Z':>2s} {'N':>2s} {'A':>2s}  "
          f"{'m_pred (MeV)':>14s} {'m_CODATA (MeV)':>14s} {'Δm/m %':>9s}  "
          f"{'B_pred (MeV)':>12s} {'B_AME (MeV)':>11s} {'ΔB/B %':>9s}  "
          f"{'atlas_tag':>30s}  caveats")
    print("-" * 175)

    rows = []
    for i, (name, Z, N) in enumerate(ISOTOPES):
        A = Z + N
        t0 = time.monotonic()

        # Absolute mass prediction
        m_nucleus_unbound = borromean_mass_prediction(q, Z, N, name)["m_nucleus_unbound_MeV"]

        # Binding energy
        binding = try_binding_canonical(Z, N, Q_50_DIGIT_STR)

        B_pred = 0.0
        B_method = "n/a"
        if binding is not None:
            B_pred = binding.get("B_pred_MeV") or 0.0
            B_method = binding.get("method", "?")

        m_pred = (m_nucleus_unbound - B_pred) if m_nucleus_unbound is not None else None
        B_AME = AME_BINDING.get(name, 0.0)

        # CODATA/AME mass for comparison
        m_codata = CODATA_MASS.get(name)
        if m_codata is None and B_AME > 0:
            # Derive from AME: m = Z·m_p + N·m_n - B_AME (using CODATA nucleon masses)
            m_codata = (
                Z * float(M_P_MEV_VALIDATION)
                + N * float(M_N_MEV_VALIDATION)
                - B_AME
            )

        # Errors
        m_err_pct = ((m_pred - m_codata) / m_codata * 100) if (m_codata and m_pred is not None) else None
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
            "m_pred_MeV": round(m_pred, 6) if m_pred else None,
            "m_codata_MeV": round(m_codata, 6) if m_codata else None,
            "m_err_pct": round(m_err_pct, 4) if m_err_pct is not None else None,
            "B_pred_MeV": round(B_pred, 6) if B_pred else None,
            "B_AME_MeV": round(B_AME, 6),
            "B_err_pct": round(B_err_pct, 4) if B_err_pct is not None else None,
            "binding_method": B_method,
            "atlas_methodology_tag": atlas_tag,
            "caveats": caveats,
        }
        rows.append(row)

        # Print row
        m_pred_s = f"{m_pred:14.6f}" if m_pred else "           n/a"
        m_codata_s = f"{m_codata:14.6f}" if m_codata else "           n/a"
        m_err_s = f"{m_err_pct:+8.4f}%" if m_err_pct is not None else "      n/a"
        B_pred_s = f"{B_pred:12.6f}" if B_pred else "         n/a"
        B_AME_s = f"{B_AME:11.6f}"
        B_err_s = f"{B_err_pct:+8.4f}%" if B_err_pct is not None else "      n/a"

        elapsed = time.monotonic() - t0
        print(f"{name:>5s} {Z:>2d} {N:>2d} {A:>2d}  "
              f"{m_pred_s} {m_codata_s} {m_err_s}  "
              f"{B_pred_s} {B_AME_s} {B_err_s}  "
              f"{atlas_tag:>30s}  "
              f"{'|'.join(caveats[:2])}"
              f"  [{elapsed:.1f}s]")

    # Summary
    print()
    n_computed = sum(1 for r in rows if r["m_pred_MeV"] is not None)
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
            r["m_pred_MeV"] is not None
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
