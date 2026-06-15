#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation script; consumes upstream
# 50-dps mass-formula witness, emits a structurally-derived
# m_n_Hecke value for downstream consumers (neutron-side counterpart
# of derive_m_p_hecke_path_a.py).
"""Workplan 2 Phase 2 — derive `m_n_Hecke` from substrate (no fitting).

Neutron-side counterpart of
[`derive_m_p_hecke_path_a.py`](derive_m_p_hecke_path_a.py).

Per [`docs/audits/2026-05-10-1ppb-workplan-update.md §Phase 2`](../../docs/audits/2026-05-10-1ppb-workplan-update.md)
and the **three-calibration discipline**
([`calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md);
PR #637): only CAL-1 $m_e$, CAL-2 $m_\\mu/m_e$ (fixes $q_0$), and
CAL-3 $Q_\\beta(n)$ may enter as inputs. $m_p$ and $m_n$ are
**predictions** — consuming them as inputs would violate the
discipline (see
[`docs/audits/2026-05-11-three-calibration-discipline-violations.md`](../../docs/audits/2026-05-11-three-calibration-discipline-violations.md)).

══════════════════════════════════════════════════════════════════
 PATH A CONSTRUCTION (T1 + T4 trustable subset)
══════════════════════════════════════════════════════════════════

Identical structure to the proton:

  * T1 = $|\\mathrm{tr}_M(\\beta_n, q_0)|$ descended-Markov-trace
    value at 50 dps, read from `atomic-tr-m-mpfr-50dps.witness.json`
    via `mass-formula-6term-mpfr-50dps.witness.json`.
  * T4 = Frobenius co-Casimir per-vortex correction at $H_3$ from
    the same witness (the T4 value happens to coincide with the
    proton's at A=1 because the per-vortex co-Casimir is
    atom-independent for A=1 atoms — same vortex structure).
  * Quarantined: T2/T3 (A=1 brane-tower structurally empty under
    current level-selection rule — open R&D
    [`brane-tower-z-habiro`](../../content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.md)),
    T5 (sign-indefinite at $q_0$: −7.466 for neutron), T6 (small
    Habiro tail, +0.681).

══════════════════════════════════════════════════════════════════
 COMMITMENT TO NO FITTING
══════════════════════════════════════════════════════════════════

No CODATA $m_n$ is consumed by this script.  The derived value will
deviate from CODATA $m_n \\approx 939.565$ MeV substantially —
similar to the proton's "wildly off CODATA" deliverable — because
T2/T3/T5/T6 R&D has not closed yet.  The point of Phase 2 is to
**expose** the residual, not to fit it.

══════════════════════════════════════════════════════════════════
 OUTPUTS
══════════════════════════════════════════════════════════════════

Emits `neutron-m_n-derivation.witness.json` recording:

  * T1, T4 at 50 dps from the upstream mpfr witness
  * T1+T4 partial sum in cat-units (the new m_n_Hecke value)
  * Quarantined T2/T3/T5/T6 with reason for exclusion

Consumed by `build_neutron_mass_50dps_chain.py` and (once wired)
by `derivation_chain.M_HECKE_PIPELINE_AT_Q0` for the neutron entry.
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
set_compute_dps()

SIX_TERM_WITNESS = _pb.witness_path("mass-formula-6term-mpfr-50dps.witness.json", HERE)
OUT_WITNESS = HERE / "neutron-m_n-derivation.witness.json"


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


def derive_m_n_hecke() -> dict:
    """Derive m_n_Hecke from T1+T4 at 50 dps (no fitting)."""
    row = _load_six_term_row("n (neutron)")

    t1 = mp.mpf(str(row["term1_descended"]))
    # P1.C HARD BREAK (2026-05-12): `term4_frob_per_vortex` renamed to
    # `term4_frob_canonical_per_3A`. Apply the same fix here that
    # Item A landed for `derive_m_p_hecke_path_a.py`.
    t4 = mp.mpf(str(row["term4_frob_canonical_per_3A"]))

    # Quarantine reasons (loaded for documentation only)
    t2_err = row.get("term23_error") or "(none)"
    # `row.get(k) or "0"` handles None/null values from the 50dps
    # witness (Item A pattern, gemini fix from PR #683).
    t5 = mp.mpf(str(row.get("term5_chirality_bw") or "0"))
    t6 = mp.mpf(str(row.get("term6_habiro_residue") or "0"))

    # Path A partial: T1 + T4 only
    m_n_hecke_partial = t1 + t4

    return {
        "atom": "neutron",
        "t1_descended_50dps": str(t1),
        "t4_frobenius_co_casimir_50dps": str(t4),
        "m_n_hecke_T1_plus_T4": str(m_n_hecke_partial),
        "quarantined": {
            "t2_t3_brane_tower": {
                "value": "0 (KeyError at A=1)",
                "reason": (
                    "A=1 not in terms-2-3-atom-per-gen-mpfr-50dps.witness.json. "
                    "PR #533: A=1 brane tower structurally empty under current "
                    "level-selection rule. Open R&D: brane-tower-z-habiro."
                ),
                "raw_error": t2_err,
            },
            "t5_chirality_bw": {
                "value_50dps": str(t5),
                "reason": (
                    "Sign-indefinite at q_0 (neutron value -7.47). "
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
            "m_n consumed; no algebraic +1; no fitted scale factor."
        ),
    }


def main() -> int:
    print("=" * 72)
    print(" Workplan 2 Phase 2 — derive m_n_Hecke from substrate (no fitting)")
    print("=" * 72)

    n = derive_m_n_hecke()

    print(f"\n  Neutron:")
    print(f"    T1 (50 dps) = {mp.nstr(mp.mpf(n['t1_descended_50dps']), 14)}")
    print(f"    T4 (50 dps) = {mp.nstr(mp.mpf(n['t4_frobenius_co_casimir_50dps']), 14)}")
    print(f"    m_n_Hecke (T1+T4 partial) = {mp.nstr(mp.mpf(n['m_n_hecke_T1_plus_T4']), 14)}")
    print(f"\n  Quarantined: T2+T3 (A=1 KeyError), T5 (sign-indefinite, "
          f"{mp.nstr(mp.mpf(n['quarantined']['t5_chirality_bw']['value_50dps']), 6)}),"
          f"\n  T6 (Habiro tail, "
          f"{mp.nstr(mp.mpf(n['quarantined']['t6_habiro_residue']['value_50dps']), 6)})")

    # Per Copilot PR #640:203 — switch from raw json.dump to
    # WitnessBuilder.wrap_legacy so the emitted witness carries
    # staleness metadata (scriptHash, commitSha, computedAt, etc.)
    # consumed by `run_pipeline.py`.  Preserves the on-disk shape
    # (description, auditOnly, data) bit-for-bit.
    from witness_base import WitnessBuilder
    from lean_uniqueness_refs import lean_uniqueness_ref
    payload = {
        "description": (
            "Workplan 2 Phase 2 — partial Path A derivation of "
            "m_n_Hecke at 50 dps from the trustable subset (T1 + T4) "
            "of the six-term unified mass formula. NO FITTING per "
            "owner directive 2026-05-10. Neutron-side counterpart of "
            "derive_m_p_hecke_path_a.py.  Honors the three-calibration "
            "discipline (CAL-1 m_e, CAL-2 q_0, CAL-3 𝔇_π) — no "
            "CODATA m_n consumed.  The derived value will not match "
            "CODATA m_n (~939.6 MeV) until the T2/T3/T5/T6 R&D closes."
        ),
        "auditOnly": (
            "docs/audits/2026-05-10-1ppb-workplan-update.md "
            "(Phase 2); "
            "docs/audits/2026-05-11-three-calibration-discipline-violations.md "
            "(motivates building this neutron-side counterpart so the "
            "neutron-mass chain consumes a substrate-derived value "
            "instead of the placeholder)"
        ),
        "owner_directive_2026_05_10": (
            "do workplans 2 phase 2; make sure no fitting; all should be derived"
        ),
        "data": {"neutron": n},
    }
    builder = WitnessBuilder.wrap_legacy(
        "neutron-m_n-derivation",
        payload,
        script_path=__file__,
        engine="mpmath",
    )
    builder.add_data("lean_uniqueness_ref", lean_uniqueness_ref("neutron"))
    out_path = builder.save()
    print(f"\n  Wrote {Path(out_path).name}")
    return 0


# Module-level accessor for derivation_chain.py to consume.
def m_n_hecke_path_a_at_q0() -> mp.mpf:
    """Returns the T1+T4 partial Path A m_n_Hecke at 50 dps. No fitting."""
    return mp.mpf(derive_m_n_hecke()["m_n_hecke_T1_plus_T4"])


if __name__ == "__main__":
    sys.exit(main())
