#!/usr/bin/env python3


# polynomial_q_not_applicable: assembly script — consumes upstream
# hecke_core canonical chain at H_{3A}.
"""Phase 3 — Triton binding via convention B (hecke_core._canon at H_9).

Per `docs/audits/2026-05-10-1ppb-workplan-update.md §Phase 3`: extend
the deuteron H_6 binding chain (PR #618 / #621) to Triton at H_9.
Per `docs/audits/2026-05-10-hbar-q-scaling-audit.md`: atom binding
uses **convention B** (E_0 = Q_β^CODATA ≈ 0.7823 MeV) at H_{3A},
NOT convention A (β-decay single-tick). Naively reusing A would
miss the 1/ℏ_q² factor (≈ 102× error).

Per owner directive 2026-05-10 ("no fitting; all should be derived"):
this script does NOT introduce new fitting. It consumes the already-
derived `hecke_core.binding_from_frobenius_pairing` chain at the
canonical strand count 3A (= 9 for Triton). The residual vs AME
exposes the open R&D in T2/T3 brane-tower closure, NOT a scaling
choice.

══════════════════════════════════════════════════════════════════
 CONSTRUCTION (NO FITTING)
══════════════════════════════════════════════════════════════════

Per `prop:categorical-mass-markov`:

    B_bulk(Z, N) = E_0 · ( |tr_M(W_free)| - |tr_M(W_atom)| )

at H_{3A}(q), where:

  * E_0 = E_0_CALIBRATION_MEV from hecke_core (convention B; CAL-3
    Q_β = 0.7823 MeV, with ℏ_q² absorbed via |Δ(net)|=1 convention).
  * W_free  = nucleon-product braid (no inter-nucleon crossings)
  * W_atom  = full atomic braid (with inter-nucleon σ crossings)
  * |tr_M(·)| from the canonical Jones–Markov trace
    (canonical=True path via `binding_canonical.binding_canonical`),
    falling back to Plancherel-weighted form if the canonical solver
    hits NotImplementedError on heavy atoms.

For Triton (Z=1, N=2, A=3) the braid is at H_9. Atoms in scope:

  * Deuteron (D, Z=1, N=1, A=2)  → H_6
  * Triton (T, Z=1, N=2, A=3)    → H_9
  * Helium-3 (³He, Z=2, N=1)     → H_9
  * Helium-4 (⁴He, Z=2, N=2)     → H_12

══════════════════════════════════════════════════════════════════
 EXPECTED RESIDUAL
══════════════════════════════════════════════════════════════════

The canonical convention-B chain has known residuals vs AME 2020
binding energies. These are NOT scaling errors (the ℏ_q² scaling is
already correct via |tr_M| difference) — they're the open
brane-tower closure problem at H_{3A}. Phase 3 deliverable here is
to **record** the residuals at H_9 and H_12 honestly, exposing the
size of the gap that subsequent Phase 4 (³He sign) and Phase 5
(⁴He H_12) work must close.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from hecke_core import E_0_CALIBRATION_MEV  # noqa: E402
# NOTE: `binding_from_frobenius_pairing` is the Phase-5 EXPLORATORY
# binding entry point (line 2991-2992 of the original hecke_core.py
# self-documented it as "Legacy Plancherel path (default)"). It lives
# in _deprecated/hecke_core_legacy.py per the canonical-vs-exploratory
# carve-out (docs/audits/2026-05-24-hecke-core-canonical-audit.md).
# Canonical binding entries are `binding_canonical.binding_canonical`
# or `mass_formula_6term_mpfr_50dps.py`.  This convention-B comparison
# script intentionally probes the legacy path; do not promote.
from hecke_core_legacy import (  # noqa: E402
    binding_from_frobenius_pairing,
)
from derivation_chain import E_0_CONVENTIONS  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

OUT = HERE / "phase3-triton-binding-convention-b.witness.json"

AME_2020_BINDING_MEV = {
    "D":    2.22456612,
    "T":    8.481798,
    "3He":  7.71810,
    "4He": 28.29567,
}


def main() -> int:
    print("=" * 80)
    print(" Phase 3 — Atom binding via convention B (hecke_core._canon at H_{3A})")
    print("=" * 80)
    print(f"\n  E_0 (convention B) = {float(E_0_CALIBRATION_MEV):.6f} MeV")
    print("  Operator: B_bulk = E_0 · (|tr_M(W_free)| - |tr_M(W_atom)|) at H_{3A}")
    print()
    print(f"  {'Atom':>6} {'(Z,N)':>8} {'H_{3A}':>8} {'B_pred (MeV)':>15} {'B_AME (MeV)':>14} {'residual':>12}")
    print("  " + "─" * 72)

    rows = []
    for label, (Z, N) in [("D", (1, 1)), ("T", (1, 2)),
                           ("3He", (2, 1)), ("4He", (2, 2))]:
        A = Z + N
        h_level = f"H_{3 * A}"
        ame = AME_2020_BINDING_MEV[label]
        try:
            t0 = time.time()
            # `canonical=True` already has internal Plancherel fallback
            # on NotImplementedError in hecke_core._canon — relying on
            # that rather than catching here masks real bugs (per
            # Copilot review). Only catch NotImplementedError narrowly.
            try:
                b_pred = binding_from_frobenius_pairing(Z, N, canonical=True)
                trace_kind = "canonical_jones_markov"
            except NotImplementedError as e:
                b_pred = binding_from_frobenius_pairing(Z, N, canonical=False)
                trace_kind = f"plancherel_fallback ({type(e).__name__})"
            dt = time.time() - t0
            b_pred_f = float(b_pred)
            err_pct = (b_pred_f - ame) / ame * 100 if ame else float("nan")
            err_kev = (b_pred_f - ame) * 1000
            print(f"  {label:>6} {f'({Z},{N})':>8} {h_level:>8} "
                  f"{b_pred_f:>+15.6f} {ame:>+14.6f} {err_pct:>+10.2f}%")
            rows.append({
                "atom": label,
                "Z": Z, "N": N, "A": A,
                "hecke_level": h_level,
                "trace_kind": trace_kind,
                "E_0_MeV": float(E_0_CALIBRATION_MEV),
                "B_pred_MeV": b_pred_f,
                "B_ame_MeV": ame,
                "residual_pct": err_pct,
                "residual_keV": err_kev,
                "compute_time_s": dt,
            })
        except Exception as e:
            print(f"  {label}: ERROR {type(e).__name__}: {str(e)[:60]}")
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": A,
                "hecke_level": h_level,
                "error": f"{type(e).__name__}: {str(e)[:200]}",
            })

    out = {
        "engine": "mpmath",
        "computation": "phase3-triton-binding-convention-b",
        "scriptFile": "phase3_triton_binding_convention_b.py",
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "description": (
            "Phase 3 of the 1ppb workplan: atom binding at H_{3A} via "
            "the canonical hecke_core._canon chain (convention B, "
            "E_0 = Q_β^CODATA). NO FITTING per owner directive "
            "2026-05-10. The residuals vs AME 2020 are the honest "
            "exposure of the brane-tower closure problem — the ℏ_q² "
            "scaling is structurally correct (via |tr_M| difference); "
            "the gap is in the T2/T3 brane-tower terms, not in E_0."
        ),
        "auditOnly": (
            "docs/audits/2026-05-10-1ppb-workplan-update.md (Phase 3); "
            "docs/audits/2026-05-10-hbar-q-scaling-audit.md (convention B)"
        ),
        "convention_used": "B_q_value_absorbed",
        "convention_metadata": E_0_CONVENTIONS["B_q_value_absorbed"],
        "owner_directive_2026_05_10": (
            "do workplans 2 phase 2 / Phase 3; no fitting/guessing; "
            "all should be derived"
        ),
        "data": {
            "E_0_MeV": float(E_0_CALIBRATION_MEV),
            "E_0_source": "hecke_core.E_0_CALIBRATION_MEV = Q_β CODATA",
            "rows": rows,
        },
    }
    saved = WitnessBuilder.wrap_legacy(
        "phase3-triton-binding-convention-b", out,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Wrote {saved.name}")

    # Surface the Triton row prominently
    triton_row = next((r for r in rows if r["atom"] == "T"), None)
    if triton_row and "B_pred_MeV" in triton_row:
        print(f"\n  TRITON (Phase 3 deliverable):")
        print(f"    B_pred = {triton_row['B_pred_MeV']:.6f} MeV")
        print(f"    B_AME  = {triton_row['B_ame_MeV']:.6f} MeV")
        print(f"    residual = {triton_row['residual_pct']:+.2f} %  ({triton_row['residual_keV']:+.1f} keV)")
        print(f"    convention B at H_9 (canonical hecke_core chain)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
