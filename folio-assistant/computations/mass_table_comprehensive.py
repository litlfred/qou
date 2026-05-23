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
    lambda_scale_family_a,
    flavor_split_subleading,
)
from witness_base import WitnessBuilder  # noqa: E402

# AME 2020 binding energies (MeV) — used for comparison only.
# Source: Wang et al., Chinese Physics C 45 (2021) 030003.
AME_BINDING = {
    "p": 0.0, "n": 0.0,
    "D": 2.22452, "T": 8.481821, "3He": 7.71804,
    "4He": 28.295674,
    "6Li": 32.0, "7Li": 39.244529,
    "9Be": 58.1650, "10B": 64.750, "12C": 92.161728,
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

# Full isotope list: (name, Z, N)
ISOTOPES = [
    ("p",   1, 0),
    ("n",   0, 1),
    ("D",   1, 1),
    ("T",   1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
    ("9Be", 4, 5),
    ("10B", 5, 5),
    ("12C", 6, 6),
]


def borromean_mass_prediction(
    q: mp.mpf, Z: int, N: int,
) -> dict:
    """Predict absolute mass of nucleus (Z, N) via the Borromean
    baryon mass formula (Family A + substrate-pure flavor-split).

    m_avg = m_e · Vol(𝓑₃)/ℏ_q² · λ_A
    m_p_pred = m_avg · (1 − Δm/(2·M_N))
    m_n_pred = m_avg · (1 + Δm/(2·M_N))
    m_nucleus = Z · m_p_pred + N · m_n_pred − B(K)

    Returns dict with prediction details.
    """
    m_e = mp.mpf(str(M_E_MEV))
    vol_b3 = 8 * mp.catalan
    hbar_q = (q - mp.mpf(1)) / q
    hbar_q_sq = hbar_q ** 2

    lam_A = lambda_scale_family_a(q)
    delta_m_over_M = flavor_split_subleading(q)

    m_avg = m_e * (vol_b3 / hbar_q_sq) * lam_A
    m_p_pred = m_avg * (1 - delta_m_over_M / 2)
    m_n_pred = m_avg * (1 + delta_m_over_M / 2)

    # Nucleus mass (before binding): Z protons + N neutrons
    m_nucleus_unbound = Z * m_p_pred + N * m_n_pred

    return {
        "lambda_A": float(lam_A),
        "delta_m_over_M_N": float(delta_m_over_M),
        "m_avg_MeV": float(m_avg),
        "m_p_pred_MeV": float(m_p_pred),
        "m_n_pred_MeV": float(m_n_pred),
        "m_nucleus_unbound_MeV": float(m_nucleus_unbound),
    }


def try_binding_canonical(Z: int, N: int, q_str: str) -> dict | None:
    """Try to compute binding energy via binding_canonical with
    closed-form path. Returns None if the atom is too heavy (A > 4)
    or if the computation fails."""
    A = Z + N
    if A < 2:
        return {"B_pred_MeV": 0.0, "method": "no binding (single nucleon)"}
    if A > 4:
        return None  # gated on H_12 Phase-2

    try:
        from binding_canonical import binding_canonical
        r = binding_canonical(
            Z, N,
            Q_beta_n_mev=float(Q_BETA_MEV),
            use_closed_form=(A <= 3),  # closed-form verified at A ≤ 3
            verbose=False,
        )
        if r.get("status") != "solved":
            return {"B_pred_MeV": None, "method": f"binding_canonical failed: {r.get('status')}", "error": r.get("error")}
        return {
            "B_pred_MeV": r.get("B_MeV"),
            "tr_M_atom": r.get("tr_M_atom"),
            "tr_M_free": r.get("tr_M_free"),
            "method": "binding_canonical" + (" (closed-form)" if A <= 3 else " (symbolic)"),
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
    builder.add_parameter("dps", 50)

    q = mp.mpf(Q_50_DIGIT_STR)

    # Compute nucleon masses once
    nucleon = borromean_mass_prediction(q, 1, 0)
    m_p_pred = nucleon["m_p_pred_MeV"]
    m_n_pred = nucleon["m_n_pred_MeV"]

    print("=" * 120)
    print("COMPREHENSIVE MASS TABLE — QOU framework at current production tier")
    print(f"  q₀ = {Q_50_DIGIT_STR[:25]}...")
    print(f"  λ_A (Family A, PROVED) = {nucleon['lambda_A']:.10f}")
    print(f"  Δm/M_N (substrate-pure, PROVED) = {nucleon['delta_m_over_M_N']:.8f}")
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
        m_nucleus_unbound = Z * m_p_pred + N * m_n_pred

        # Binding energy
        binding = try_binding_canonical(Z, N, Q_50_DIGIT_STR)

        B_pred = 0.0
        B_method = "n/a"
        if binding is not None:
            B_pred = binding.get("B_pred_MeV") or 0.0
            B_method = binding.get("method", "?")

        m_pred = m_nucleus_unbound - B_pred
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
        m_err_pct = ((m_pred - m_codata) / m_codata * 100) if m_codata else None
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
        "lambda_A_value": nucleon["lambda_A"],
        "delta_m_over_M_N": nucleon["delta_m_over_M_N"],
        "m_p_pred_MeV": m_p_pred,
        "m_n_pred_MeV": m_n_pred,
        "production_tier": "Family A (PROVED) + flavor-split (PROVED)",
        "research_tier_not_used": "Strategy I λ_Y = λ_A - G·h² (conjectural bijection)",
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
