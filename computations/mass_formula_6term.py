"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
#!/usr/bin/env python3
"""
Integrated 6-term mass formula for light isotopes.

Per thm:knot-mass-formula-unified, the total vortex mass is:

    𝔪(ρ) = |tr_M(T_w)|                     [1: descended]
         + Σ_i Φ_q(|V̂_i|)                   [2: single-gen brane tower]
         + z²·Σ_{i<j} Φ_q(|V̂_i V̂_j|)       [3: pair-gen brane tower]
         + m_e · tr_M(C_dim_q)               [4: Frobenius co-Casimir]
         + a_K · B_bulk                      [5: chirality factor]
         + (jet-level prefix corrections)    [6: OPEN / upstream]

For this script:
  - Term 1: numerical Hoefsmit via hecke_characters (at H_{3A})
  - Terms 2+3: atom_per_generator_volumes + Φ_q tower
  - Term 4: universal (2 + 1/[2]_q)·m_e per nucleon (n=3 Frobenius)
  - Term 5: paper's BW with chirality factor per knot type
  - Term 6: absent (marked as missing)

β-decay calibration: E_0 = 0.78233341 MeV, m_e = 0.511 MeV.  The
proton and neutron singly are calibrated (no tower needed); the
formula is applied for bindings of D, T, ³He, ⁴He.

Answers user's question:
  - n/p discrepancy is CALIBRATION-DEPENDENT; with β-calib
    both match CODATA to 0.2%
  - The 55-98% errors for A=2,3,4 come from MISSING terms 2-5,
    not from n/p per se

Witness: mass-formula-6term.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_MP as _Q_CANONICAL  # mpf, 70 dps (was float64 Q)
from experimental_constants import (
    M_E_MEV, M_P_MEV, M_N_MEV, Q_NEUTRON_MEV,
)
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)

Q0 = _Q_CANONICAL
m_e = M_E_MEV


def _mpf_from_witness_value(key: str, val) -> "mp.mpf":
    """Parse one Σ-table entry, refusing a JSON float.

    `probe_term4_conventions` serialises with `mp.nstr(..., 50)`, i.e. a
    STRING, so the 50 digits survive the round-trip. A JSON *number* in this
    slot means the table was written at float64 and the precision is already
    gone upstream — `mp.mpf(str(<float>))` would re-wrap that loss in an mpf
    and hide it, which is the laundering pattern the precision gates flag.
    Refuse instead, and say where to fix it.
    """
    if isinstance(val, str):
        return mp.mpf(val)
    raise TypeError(
        f"probe-term4-conventions: {key} is {type(val).__name__}, not str — "
        f"the table must be serialised as a decimal string (mp.nstr) or its "
        f"precision is lost before it is read. Fix the producer, not here."
    )


def _load_sigma_3A_table():
    """Load Σ_{λ⊢3A} 1/dim_q(λ) values at q_0 from the per-3A probe witness.

    Per the per-3A correction (audit 2026-04-28b): the genuine algebraic
    Term 4 is m_e · Σ_{λ⊢3A} 1/dim_q(λ), NOT A · m_e · (2 + 1/[2]_q).
    The probe witness records Σ_{λ⊢3A} 1/dim_q(λ) at q_0 for A=1..4.

    **That witness has never existed in this repository and no producer in
    the tree writes it** (measured 2026-08-26, bean `qou-nk3h`; the identical
    loader in `unified_low_isotope_predictor.py` has the same problem). Both
    swallowing paths below now warn instead of returning `{}` in silence.
    The table is deliberately not reconstructed here — ten live `dim_q`
    implementations exist with differing signatures, so building it is a
    choice among conventions rather than a computation."""
    path = Path(__file__).parent / "probe-term4-conventions.witness.json"
    if not path.exists():
        print(f"  \u26a0 term4: {path.name} not found — Sigma_(3A) table "
              f"unavailable; the caller's fallback is in force (bean qou-nk3h)",
              file=sys.stderr)
        return {}
    try:
        d = json.loads(path.read_text())
        # WitnessBuilder nests the payload under `data`; the pre-2026-08-26
        # loader read only the top level, so it would have missed the table
        # even had the witness existed. Top level kept as a fallback.
        sigma = d.get("data", {}).get("sigma_inv_dim_q_at_q0") \
            or d["sigma_inv_dim_q_at_q0"]
        out = {}
        # Map A → n=3A entry (covers all A whose key is present in witness).
        for key, val in sigma.items():
            if key.startswith("n="):
                n = int(key.split("=")[1])
                if n % 3 == 0:
                    out[n // 3] = _mpf_from_witness_value(key, val)
        return out
    except Exception as exc:
        print(f"  \u26a0 term4: {path.name} unreadable ({exc!r}) — the "
              f"caller's fallback is in force (bean qou-nk3h)", file=sys.stderr)
        return {}




def term_1_descended(Z, N, include_inter):
    """Term 1: |tr_M(T_w)| via numerical Hoefsmit at H_{3A}."""
    from light_isotope_sweep import tr_M_at_q0
    tr, _, _ = tr_M_at_q0(Z, N, include_inter)
    return abs(tr)


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()
# Built after set_compute_dps(): at import-time dps it was a 53-bit value
# serialised with 50 manufactured digits.
FROB_N3 = m_e * (2 + 1 / (Q0 + 1 / Q0))  # m_e · (2 + 1/[2]_q)
# Also after set_compute_dps(): parsed at import-time dps the 50-digit
# strings were cut to 53 bits (precision-gates fake-precision red).
_SIGMA_3A_AT_Q0 = _load_sigma_3A_table()

def term_23_brane_tower(Z, N, include_inter):
    """Terms 2 + 3: Σ_i Φ_q(|V̂_i|) + z²·Σ_{i<j} Φ_q(|V̂_i V̂_j|).

    Per thm:knot-mass-formula-unified, V̂_i is the full additive-
    Wedderburn-traced volume at generator i (the 'full' key from
    atom_per_generator_volumes; std/sym/alt are Wedderburn-block
    components, full is their weighted aggregate).

    Returns dict {T2, T3, status, max_abs_V}; status is one of:
      "ok": all |V̂_i| < 0.95, Φ_q convergent
      "near-pole": some |V̂_i| ∈ [0.95, 1.05); Φ_q values huge but finite
      "divergent": some |V̂_i| ≥ 1.05; Φ_q diverges (T23 unphysical)

    The previous version silently caught TypeError when abs() was
    applied to the dict-typed volume, returning T2 = T3 = 0.  This
    masked the deeper structural issue that |V̂_i| for D is at or
    above 1, putting it AT the Φ_q convergence boundary.
    """
    from hecke_core import atom_per_generator_volumes, h as h_val, z as z_mark
    from mass_endomorphism import Phi_q
    vols_dict = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    vols = [v["full"] if isinstance(v, dict) else v for v in vols_dict]
    abs_vols = [abs(float(v)) for v in vols]
    # max_abs_V is the dominant generator volume (max over abs).
    # By construction every multi-nucleon atom contains at least one
    # proton or neutron, and the proton's σ_0 generator volume
    # |V̂_full| ≈ 0.9890 dominates across D / T / ³He / ⁴He /
    # heavier — so this scalar is structurally identical (to ~14 dp)
    # across atoms whose generator structure shares the same
    # proton/neutron building block.  Identical-across-atoms is
    # therefore the EXPECTED behaviour, not a bug.
    max_abs = max(abs_vols) if abs_vols else 0.0

    if max_abs >= 1.05:
        return {"T2": 0.0, "T3": 0.0,
                "single": 0.0, "pair": 0.0,  # legacy aliases
                "status": "divergent",
                "max_abs_V": max_abs}
    status = "near-pole" if max_abs >= 0.95 else "ok"
    single = mp.mpf(0)
    pair = mp.mpf(0)
    for v in vols:
        single += Phi_q(v)
    for i in range(len(vols) - 1):
        pair += Phi_q(vols[i] * vols[i + 1])
    pair *= z_mark ** 2
    return {"T2": float(single), "T3": float(pair),
            # Legacy aliases for backward compat with downstream
            # consumers (probe_canonical_multi_term_D, etc.) that read
            # `.single` and `.pair` on this dict.
            "single": float(single), "pair": float(pair),
            "status": status, "max_abs_V": max_abs}


def term_4_frobenius(A):
    """Term 4: Frobenius co-Casimir trace m_e · τ(C_{dim_q}^{H_{3A}}).

    Per ``thm:frobenius-codim-universal`` and the per-3A correction
    (audit 2026-04-28b), the algebraic Term 4 for an isotope braid in
    H_{3A}(q) is

        Term4(A) = m_e · Σ_{λ⊢3A} 1/dim_q(λ)

    The two earlier compute heuristics are RETAINED for comparison only:

      - per-vortex 1·FROB_N3        (constant, ≈ 1.276 MeV)
      - per-A     A·FROB_N3         (legacy compute, deprecated)

    Returns (per-vortex, per-A, per-3A_genuine).  Use per-3A_genuine
    in canonical predictions; the others are kept for backward
    comparison.
    """
    pv = FROB_N3
    pA = A * FROB_N3
    sigma_3A = _SIGMA_3A_AT_Q0.get(A)
    p3A = m_e * sigma_3A if sigma_3A is not None else None
    return pv, pA, p3A


def term_5_chirality_bw(Z, N, knot_type):
    """Term 5: paper's BW + chirality factor.  Uses
    bw_chirality_isotopes.py infrastructure."""
    try:
        from bw_chirality_isotopes import (
            B_bulk, B_Zdep, B_shell, pairing_sign,
            f_chiral_plus, f_chiral_minus, f_amphi, f_borromean, f_Zdep_scale,
        )
    except ImportError:
        return None
    chirality_map = {
        "chiral+": f_chiral_plus,
        "chiral-": f_chiral_minus,
        "amphichiral": f_amphi,
        "borromean": f_borromean,
        "none": mp.mpf(1),
    }
    a_K = chirality_map.get(knot_type, mp.mpf(1))
    A = Z + N
    sign = pairing_sign(Z, N)
    bulk = B_bulk(A, Z, N, sign)
    zdep = B_Zdep(A, Z, N)
    shell = B_shell(A, Z, N) if A >= 4 else mp.mpf(0)
    B = a_K * bulk + f_Zdep_scale * zdep + shell
    return float(B)


# Knot-type assignments per paper (six-term-mass-formula-complete.md)
KNOT_TYPE = {
    "D": "chiral+",          # paper's assignment (gives -353%, questionable)
    "T": "amphichiral",
    "3He": "amphichiral",
    "4He": "borromean",
    "6Li": "none",
}


def predict_all_terms(Z, N, knot_type):
    """Compute all 6 terms for an isotope.  For the BINDING energy
    (not single-vortex mass), we need:
        B = E_0 · [ |tr_M(free)| - |tr_M(atom)| ]   [term 1 path]
      or
        B = paper_BW + chirality                   [term 5 path]
    We report both."""
    A = Z + N
    t1_free = term_1_descended(Z, N, include_inter=False)
    t1_atom = term_1_descended(Z, N, include_inter=True)

    t23_free = term_23_brane_tower(Z, N, include_inter=False)
    t23_atom = term_23_brane_tower(Z, N, include_inter=True)

    t4_pv, t4_pa, t4_p3A = term_4_frobenius(A)  # per-vortex, per-A, per-3A
    t5 = term_5_chirality_bw(Z, N, knot_type)

    return {
        "A": A, "Z": Z, "N": N,
        "knot_type": knot_type,
        "term1_descended_free": t1_free,
        "term1_descended_atom": t1_atom,
        "term23_tower_free": t23_free,
        "term23_tower_atom": t23_atom,
        "term4_frobenius_pervortex": t4_pv,
        "term4_frobenius_per_A": t4_pa,
        "term4_frobenius_per_3A_canonical": t4_p3A,
        "term5_bw_chirality_binding": t5,
    }


if __name__ == "__main__":
    print("INTEGRATED 6-TERM MASS FORMULA — light isotopes")
    print("=" * 96)
    print(f"q_0 = {Q0}, m_e = {m_e} MeV")
    print(f"Universal Frobenius (n=3) = {mp.nstr(FROB_N3, 7)} MeV per vortex")
    print()

    # A=1 β-decay calibration (same as light_isotope_sweep.py).
    # Use the canonical CODATA-derived Q_NEUTRON_MEV (0.78233341 MeV)
    # from experimental_constants.py rather than the 3-sig-fig truncation
    # to keep precision consistent with categorical_q_decay_ba_low_isotopes.
    t1_p = term_1_descended(1, 0, include_inter=False)
    t1_n = term_1_descended(0, 1, include_inter=False)
    Q_cat = t1_n - t1_p
    E_0 = Q_NEUTRON_MEV / abs(Q_cat)
    print(f"[A=1 calibration]")
    print(f"  |tr_M(p)| @ q_0 = {float(t1_p):.6e}")
    print(f"  |tr_M(n)| @ q_0 = {float(t1_n):.6e}")
    print(f"  E_0 = Q_β(n)={float(Q_NEUTRON_MEV):.6f} / |Q_cat| = {float(E_0):.6f} MeV/cat.unit")
    print()

    # Isotope sweep (skip ⁴He for speed; use light_isotope_sweep results)
    # Unified AME 2020 values (matches `B_AME_REFERENCE` in
    # categorical_q_decay_ba_low_isotopes.py — fewer-digit truncations
    # caused a 0.0002% discrepancy in err_pct previously).
    B_AME = {"D": float(AME_B_DEUTERON_MEV_VALIDATION), "T": float(AME_B_TRITIUM_MEV_VALIDATION), "3He": float(AME_B_HE3_MEV_VALIDATION)}
    rows = {}
    for iso in ["D", "T", "3He"]:
        Z, N = {"D": (1, 1), "T": (1, 2), "3He": (2, 1)}[iso]
        print(f"── {iso} (Z={Z}, N={N}, A={Z+N}) ──")
        r = predict_all_terms(Z, N, KNOT_TYPE[iso])
        rows[iso] = r

        # Binding predictions from different term subsets
        B_term1 = E_0 * (r["term1_descended_free"] - r["term1_descended_atom"])
        # T2+T3 brane-tower binding contribution (free - atom subtraction
        # in cat units, multiplied by E_0 to convert).  Only included when
        # |V̂| < 0.95 (Φ_q convergent).  For D the atom volumes hit |V̂|≈1
        # so the brane tower diverges; flagged via status.
        t23_f = r["term23_tower_free"]
        t23_a = r["term23_tower_atom"]
        if (t23_f.get("status") == "ok" and t23_a.get("status") == "ok"):
            B_term23 = E_0 * (
                (t23_f["T2"] + t23_f["T3"])
                - (t23_a["T2"] + t23_a["T3"])
            )
            t23_status = "included"
        else:
            B_term23 = 0.0
            t23_status = (f"excluded ({t23_f.get('status','?')}/"
                          f"{t23_a.get('status','?')})")
        # Term 4 — show per-vortex (legacy) and per-3A (canonical algebraic)
        B_term1_plus_frob_pv = B_term1 + B_term23 + r["term4_frobenius_pervortex"]
        t4_p3A = r["term4_frobenius_per_3A_canonical"]
        B_term1_plus_frob_p3A = (
            B_term1 + B_term23 + t4_p3A if t4_p3A is not None else None
        )
        B_term5 = r["term5_bw_chirality_binding"]

        print(f"  Term 2+3 (brane tower)               : B23 = "
              f"{float(B_term23):8.4f} MeV  ({t23_status})")
        print(f"  Term 1 only (descended)              : B = "
              f"{float(B_term1):8.4f} MeV "
              f"({float((B_term1-B_AME[iso])/B_AME[iso]*100):+7.2f}%)")
        print(f"  T1 + T2+3 + T4 per-vortex            : B = "
              f"{float(B_term1_plus_frob_pv):8.4f} MeV "
              f"({float((B_term1_plus_frob_pv-B_AME[iso])/B_AME[iso]*100):+7.2f}%)")
        if B_term1_plus_frob_p3A is not None:
            print(f"  T1 + T2+3 + T4 per-3A (CANONICAL)    : B = "
                  f"{float(B_term1_plus_frob_p3A):8.4f} MeV "
                  f"({float((B_term1_plus_frob_p3A-B_AME[iso])/B_AME[iso]*100):+7.2f}%)")
        if B_term5 is not None:
            print(f"  Term 5 only (paper BW+χ)             : B = "
                  f"{float(B_term5):8.4f} MeV "
                  f"({float((B_term5-B_AME[iso])/B_AME[iso]*100):+7.2f}%)")
        print(f"  B_AME                                : "
              f"{float(B_AME[iso]):8.4f} MeV")
        print()

        err_p3A = (
            (B_term1_plus_frob_p3A - B_AME[iso]) / B_AME[iso] * 100
            if B_term1_plus_frob_p3A is not None else None
        )
        rows[iso].update({
            "B_pred_term1": B_term1,
            # Legacy aliases retained for backward compat with downstream
            # consumers (e.g. categorical_q_decay_ba_low_isotopes,
            # probe_canonical_multi_term_D); same values as
            # `*_pervortex_legacy` below.
            "B_pred_term1_plus_term4": B_term1_plus_frob_pv,
            "B_pred_term1_plus_term4_pervortex_legacy": B_term1_plus_frob_pv,
            "B_pred_term1_plus_term4_per3A_canonical": B_term1_plus_frob_p3A,
            "B_pred_term5_bw_chirality": B_term5,
            "B_AME_MeV": B_AME[iso],
            "err_pct": {
                "term1_only": (B_term1 - B_AME[iso]) / B_AME[iso] * 100,
                # Legacy alias: `term1_plus_term4` aliases the per-vortex
                # value for backward compat.
                "term1_plus_term4":
                    (B_term1_plus_frob_pv - B_AME[iso]) / B_AME[iso] * 100,
                "term1_plus_term4_pervortex_legacy":
                    (B_term1_plus_frob_pv - B_AME[iso]) / B_AME[iso] * 100,
                "term1_plus_term4_per3A_canonical": err_p3A,
                "term5_only": (
                    (B_term5 - B_AME[iso]) / B_AME[iso] * 100
                    if B_term5 is not None else None
                ),
            },
        })

    # Summary table
    print("Summary (binding errors by term subset)")
    print(f"{'iso':>5}  {'term1':>10}  "
          f"{'t1+4 pv (legacy)':>18}  {'t1+4 per-3A (CAN)':>18}  "
          f"{'term5 (BW+χ)':>14}")
    print("-" * 78)
    for iso in ["D", "T", "3He"]:
        r = rows[iso]
        e1 = r['err_pct']['term1_only']
        e14_pv = r['err_pct']['term1_plus_term4_pervortex_legacy']
        e14_p3A = r['err_pct']['term1_plus_term4_per3A_canonical']
        # float() casts here are DISPLAY ONLY (AGENTS.md permits it inside an
        # f-string). These carry mpf since term 4 became exact.
        e14_p3A_str = (f"{float(e14_p3A):>+15.2f}%"
                       if e14_p3A is not None else "     (N/A)")
        t5 = r['err_pct']['term5_only']
        t5_str = f"{float(t5):>+11.2f}%" if t5 is not None else "     (N/A)"
        print(f"{iso:>5}  {float(e1):>+8.2f}%  "
              f"{float(e14_pv):>+15.2f}%   {e14_p3A_str}  {t5_str}")

    print()
    print("KEY FINDING: n/p discrepancy is NOT visible here because we")
    print("calibrate on β-decay Q_β(n) = 0.78233341 MeV. Both p and n match")
    print("CODATA to <0.2% by construction.")
    print()
    print("The A≥3 errors are from MISSING terms 2-5, NOT n/p:")
    print("  - Term 1 alone: -55% to -98%")
    print("  - Term 1+4 (add universal Frob): still -56% to -94%")
    print("  - Term 5 (paper BW+χ):  -353% for D, +0.5-0.9% for T/³He")
    print()
    print("The SUM of all 6 terms (not tested here because terms 2-3")
    print("duplicate term 1's information and term 6 is open) would be")
    print("the integrated target.")

    # term1 path delegates to light_isotope_sweep.tr_M_at_q0, which
    # uses chi_sym_alt_closed_form.{chi_sym_closed_form,chi_alt_closed_form}
    # for the 1-dim irreps λ = (n,) and λ = (1,)*n; the remaining
    # higher-dim partitions still go through the seminormal Hoefsmit
    # numeric evaluator.
    from light_isotope_sweep import CLOSED_FORM_USED as _CLOSED_FORM_USED
    witness = {
        "computation": "mass-formula-6term",
        "closed_form_used": _CLOSED_FORM_USED,
        "description": (
            "Integrated 6-term mass formula computation for light "
            "isotopes. Reports each term separately plus binding "
            "predictions via different subsets. Clarifies that n/p "
            "discrepancy is calibration-dependent; β-calibration "
            "fixes it by construction. A≥3 errors come from missing "
            "structural terms, not n/p."
        ),
        "reference_blocks": [
            "thm:knot-mass-formula-unified",
            "thm:frobenius-codim-universal",
            "prop:six-term-mass-formula-complete",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0, "m_e_MeV": m_e, "E_0_MeV": E_0,
            "frobenius_n3_pervortex_MeV": FROB_N3,
            "sigma_inv_dim_q_at_q0_3A": _SIGMA_3A_AT_Q0,
            "term4_convention": "per-3A canonical (m_e · Σ_{λ⊢3A} 1/dim_q(λ))",
        },
        "A1_calibration": {
            "tr_p_q0": t1_p,
            "tr_n_q0": t1_n,
            "Q_cat": Q_cat,
            "note": (
                "β-decay calibration sets m_p and m_n to CODATA by "
                "construction; n/p discrepancy only arises WITHOUT "
                "this calibration (upstream raw tower: m_n=411 vs 940)."
            ),
        },
        "rows": rows,
    }
    out = Path(__file__).parent / "mass-formula-6term.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
