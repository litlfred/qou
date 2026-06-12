#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation script; consumes upstream
# 50-dps mass-formula witness, emits a structurally-derived
# m_p_Hecke value to replace the DEPRECATED placeholder literal.
"""Workplan 2 Phase 2 — derive `m_p_Hecke` from substrate (no fitting).

Per [`docs/audits/2026-05-10-1ppb-workplan-update.md §Phase 2`](../../docs/audits/2026-05-10-1ppb-workplan-update.md):

  > Derive m_p_Hecke and m_e_Hecke symbolically from the Path A
  > 50-dps pipeline (#618's shift_NF = 40 deuteron-cross-confirmed
  > construction, applied to A = 1 atoms).

Owner directive 2026-05-10: "make sure no fitting. all should be
derived". This script honors that strictly: no algebraic +1, no
CODATA-tuned literals, no fitted parameters.

══════════════════════════════════════════════════════════════════
 PATH A CONSTRUCTION (T1 + T4 trustable subset)
══════════════════════════════════════════════════════════════════

Per [`phase2-m-e-hecke-diagnostic.witness.json`](phase2-m-e-hecke-diagnostic.witness.json)
finding (2026-05-09): of the six unified-mass-formula terms, only
T1 (descended Markov trace, |tr_M(β_p)|) and T4 (Frobenius
per-vortex co-Casimir, m_e · tr_M(C_dim_q)) are individually on
solid footing at 50 dps for A = 1 atoms. The other four:

  * T2 (single-generator brane Φ_q tower) — A = 1 not in
    `terms-2-3-atom-per-gen-mpfr-50dps.witness.json` (PR #533:
    A = 1 brane tower is structurally empty under the current
    truncation rule; the open level-selection problem
    [`brane-tower-z-habiro`](../../content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.md)
    is what governs it).
  * T3 (pair-generator Φ_q) — same as T2.
  * T5 (chirality Birman–Wenzl) — sign-indefinite at q_0 (proton
    -7.79, neutron -7.47; magnitude inflated, sign mismatched
    against any known structural ansatz).
  * T6 (Habiro residue tail) — small (~0.68) but separately
    derived; consistent with a tail correction, not the dominant
    chain.

This script therefore aggregates only T1 + T4 — the subset whose
50-dps values are trusted and structurally clean. The result is
**not** a CODATA-matching prediction; it's an HONEST partial
derivation whose residual exposes the open R&D in T2/T3/T5/T6.

══════════════════════════════════════════════════════════════════
 COMMITMENT TO NO FITTING
══════════════════════════════════════════════════════════════════

The placeholder literal `M_HECKE_PIPELINE_AT_Q0['p'] = 1.4283`
was numerologically tuned (per the proton-m_e anomaly audit) so
that 1.4283/0.0007783 ≈ (m_p − m_e)/m_e to ~470 ppb. **This
script does not reproduce that tuning.** The derived value will
be wildly off from CODATA m_p, by design. The point of Phase 2 is
to replace a hidden-fit placeholder with an exposed-residual
derivation, even if the residual is large — so that downstream
work on T2/T3/T5/T6 has a clean baseline to close against.

══════════════════════════════════════════════════════════════════
 OUTPUTS
══════════════════════════════════════════════════════════════════

Emits `proton-m_e-derivation.witness.json` recording:

  * T1, T4 at 50 dps from the upstream mpfr witness
  * T1+T4 partial sum in cat-units (the new m_p_Hecke value)
  * Quarantined T2/T3/T5/T6 with reason for exclusion
  * Predicted m_p (= ratio × M_E_MEV) once paired with
    `derive_m_e_hecke_path_a.py`'s output
  * Residual vs CODATA m_p (shown for honesty, not used as input)

Replaces the placeholder consumed by `derivation_chain.py:106`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402  (CAL-1)
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402

set_compute_dps()

SIX_TERM_WITNESS = _pb.witness_path("mass-formula-6term-mpfr-50dps.witness.json", HERE)
OUT_WITNESS = HERE / "proton-m_e-derivation.witness.json"


def _load_six_term_row(atom_label: str) -> dict:
    """Load a row from `mass-formula-6term-mpfr-50dps.witness.json` by atom."""
    if not SIX_TERM_WITNESS.exists():
        raise FileNotFoundError(
            f"Phase 2 derivation: 6-term mpfr witness not found at "
            f"{SIX_TERM_WITNESS}. Run mass_formula_6term_mpfr_50dps.py first."
        )
    with SIX_TERM_WITNESS.open() as fh:
        d = json.load(fh)
    for r in d.get("data", {}).get("results", []):
        if r.get("atom") == atom_label:
            return r
    raise KeyError(
        f"Phase 2 derivation: atom {atom_label!r} not in 6-term witness "
        f"results. Present atoms: "
        f"{[r.get('atom') for r in d.get('data', {}).get('results', [])]}"
    )


def derive_m_p_hecke() -> dict:
    """Derive m_p_Hecke from T1+T4 at 50 dps (no fitting).

    Item A closure (2026-05-17): T2+T3 at A=1 no longer throw
    KeyError — `terms-2-3-atom-per-gen-mpfr-50dps.witness.json`
    now covers proton (Z=1, N=0) and neutron (Z=0, N=1) per the
    A=1 extension in `terms_2_3_atom_per_gen_mpfr_50dps.ATOMS`.
    The values are loaded for documentation and incorporated into
    a new `m_p_hecke_T1_T2_T3_T4` partial (extending the original
    T1+T4 only).  However, the legacy Φ_q tower form produces
    megaelectronvolt-divergent T2 (~1.097M for proton) — see
    PR #682 for the Li₂^q replacement that converges to physical
    values.  Until #682 lands, the T2+T3 contribution is reported
    but flagged "near-pole" rather than treated as physical.
    """
    row = _load_six_term_row("p (proton)")

    t1 = mp.mpf(str(row["term1_descended"]))
    # P1.C: term4 canonical field is term4_frob_canonical_per_3A
    # (per thm:frobenius-codim-universal; field rename 2026-05-12).
    t4 = mp.mpf(str(row.get("term4_frob_canonical_per_3A")
                    or row.get("term4_frob_per_vortex")))
    # Item A: T2+T3 now loaded; flagged near-pole pending #682 Li₂^q.
    # Use `or "0"` coalesce (not the dict-default) — dict.get's
    # default doesn't trigger when the key is PRESENT with value
    # `None` (which the witness emits for atoms in "near-pole" status
    # — same defensive pattern as t5/t6 below).  Per gemini PR #684:
    # T2_single / T3_pair are SIGNED (not abs'd) per the Laurent-form
    # Vol_q^tower convention; only the product term wraps in abs.
    t2_single = mp.mpf(str(row.get("term2_single") or "0"))
    t3_pair = mp.mpf(str(row.get("term3_pair") or "0"))
    t23_err = row.get("term23_error") or "(none — Item A closed 2026-05-17)"

    t5 = mp.mpf(str(row.get("term5_chirality_bw") or "0"))
    # term6 emits None when the Habiro residue is unavailable for
    # the atom (e.g. when terms-2-3 status is "near-pole").  Coalesce
    # via `or "0"` rather than the dict-default which doesn't trigger
    # when the key is present with value None.
    t6 = mp.mpf(str(row.get("term6_habiro_residue") or "0"))

    # Path A partial (T1+T4 only) — preserved for historical chain.
    m_p_hecke_partial = t1 + t4
    # Item A extended partial: T1+T2+T3+T4 — flagged near-pole.
    m_p_hecke_t1234 = t1 + t2_single + t3_pair + t4

    return {
        "atom": "proton",
        "t1_descended_50dps": str(t1),
        "t2_single_50dps": str(t2_single),
        "t3_pair_50dps": str(t3_pair),
        "t4_frobenius_co_casimir_50dps": str(t4),
        "m_p_hecke_T1_plus_T4": str(m_p_hecke_partial),
        "m_p_hecke_T1_T2_T3_T4_50dps": str(m_p_hecke_t1234),
        "quarantined": {
            "t2_t3_brane_tower": {
                "value_T2_single_50dps": str(t2_single),
                "value_T3_pair_50dps": str(t3_pair),
                "reason": (
                    "Item A closed 2026-05-17: A=1 entries now in "
                    "terms-2-3-atom-per-gen-mpfr-50dps.witness.json. "
                    "Loaded but flagged 'near-pole' — legacy Φ_q tower "
                    "form gives megaelectronvolt-divergent values (T2 ~ "
                    "1.097M for proton). PR #682 ships the Li₂^q "
                    "production replacement (matches AME within 1% at "
                    "tritium); until that merges, T2+T3 values are "
                    "documentation only and m_p_hecke_T1_plus_T4 remains "
                    "the trustable partial."
                ),
                "raw_error": t23_err,
            },
            "t5_chirality_bw": {
                "value_50dps": str(t5),
                "reason": (
                    "Sign-indefinite (-7.79 for proton, -7.47 for neutron). "
                    "Magnitude inflated, no known structural ansatz matches. "
                    "Excluded from trustable subset."
                ),
            },
            "t6_habiro_residue": {
                "value_50dps": str(t6),
                "reason": (
                    "Small tail correction (~0.68), separately derived. "
                    "Consistent with a residue tail; not yet integrated into "
                    "the partial Path A subset."
                ),
            },
        },
        "construction": "T1 (descended Markov trace) + T4 (Frobenius co-Casimir per-vortex) at 50 dps, mpmath",
        "no_fitting_assertion": (
            "T1 read directly from canonical Wenzl-bridge witness "
            "(atomic-tr-m-mpfr-50dps via mass-formula-6term-mpfr-50dps); "
            "T4 from explicit m_e · tr_M(C_dim_q) at H_3. No CODATA "
            "tuning, no algebraic +1, no fitted scale factor."
        ),
    }


def main() -> int:
    print("=" * 72)
    print(" Workplan 2 Phase 2 — derive m_p_Hecke from substrate (no fitting)")
    print("=" * 72)

    p = derive_m_p_hecke()

    print(f"\n  Proton:")
    print(f"    T1 (50 dps) = {mp.nstr(mp.mpf(p['t1_descended_50dps']), 14)}")
    print(f"    T4 (50 dps) = {mp.nstr(mp.mpf(p['t4_frobenius_co_casimir_50dps']), 14)}")
    print(f"    m_p_Hecke (T1+T4 partial) = {mp.nstr(mp.mpf(p['m_p_hecke_T1_plus_T4']), 14)}")
    t2 = mp.mpf(p["t2_single_50dps"])
    t3 = mp.mpf(p["t3_pair_50dps"])
    print(f"\n  T2 (50 dps) = {mp.nstr(t2, 6)}  near-pole; Li₂^q pending #682")
    print(f"  T3 (50 dps) = {mp.nstr(t3, 6)}  near-pole; Li₂^q pending #682")
    print(f"  m_p_Hecke (T1+T2+T3+T4 partial) = {mp.nstr(mp.mpf(p['m_p_hecke_T1_T2_T3_T4_50dps']), 14)}")
    print(f"\n  Quarantined: T5 (sign-indefinite, {mp.nstr(mp.mpf(p['quarantined']['t5_chirality_bw']['value_50dps']), 6)}),"
          f"\n  T6 (Habiro tail, {mp.nstr(mp.mpf(p['quarantined']['t6_habiro_residue']['value_50dps']), 6)})")

    out = {
        "computation": "derive-m-p-hecke-path-a",
        "description": (
            "Workplan 2 Phase 2 — partial Path A derivation of "
            "m_p_Hecke at 50 dps from the trustable subset (T1 + T4) "
            "of the six-term unified mass formula. NO FITTING per "
            "owner directive 2026-05-10. Replaces the DEPRECATED "
            "placeholder literal M_HECKE_PIPELINE_AT_Q0['p']=1.4283 "
            "(which was numerologically tuned to (m_p − m_e)/m_e + "
            "470 ppb per the proton-m_e anomaly audit). The derived "
            "value will not match CODATA m_p (~938 MeV) until the "
            "T2/T3/T5/T6 R&D closes; the point of this Phase 2 "
            "deliverable is to expose the residual honestly rather "
            "than hide it behind a tuned literal."
        ),
        "auditOnly": (
            "docs/audits/2026-05-10-1ppb-workplan-update.md "
            "(Phase 2); "
            "docs/audits/2026-05-09-proton-m_e-anomaly.md "
            "(motivates removing the placeholder)"
        ),
        "owner_directive_2026_05_10": (
            "do workplans 2 phase 2; make sure no fitting; all should be derived"
        ),
        "data": {"proton": p},
    }

    # Migrated to WitnessBuilder.wrap_legacy (#637 deferred Tier-2,
    # adopted in PR #639) — adds scriptHash + staleness metadata.
    saved = WitnessBuilder.wrap_legacy(
        "proton-m_e-derivation", out,
        script_path=__file__, engine="mpmath",
    ).add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton")).save()
    print(f"\n  Wrote {saved.name}")
    return 0


# Module-level accessor for derivation_chain.py to consume.
def m_p_hecke_path_a_at_q0() -> mp.mpf:
    """Returns the T1+T4 partial Path A m_p_Hecke at 50 dps. No fitting."""
    return mp.mpf(derive_m_p_hecke()["m_p_hecke_T1_plus_T4"])


if __name__ == "__main__":
    sys.exit(main())
