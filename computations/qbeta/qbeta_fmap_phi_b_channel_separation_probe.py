#!/usr/bin/env python3
"""qbeta_fmap_phi_b_channel_separation_probe.py — magnitude vs phase channel on Φ_b.

Fibre-side spec for the z→c_k f-map keystone (handed to PR #3458). NOT a c_3
construction — a structural confirmation, on the VALIDATED Faddeev Φ_b
(phi_b_evaluator.py, literature-verified against library/arxiv-math-0604094v1/0604094v1.pdf, Hikami
math/0604094), that the fibre-saddle object separates cleanly into a FLAT
magnitude channel and a VARYING phase channel.

## Why this matters for c_3

The cross-anchor c_3 swing (c_3(q_p) = −2.0693 proton vs −2.0097 muon over
Δq = 1.28×10⁻⁸) forces a slope dc_3/dq ≈ 4.66×10⁶, which for a SMOOTH REAL
function of q needs a singularity within ≈ 4.4×10⁻⁷ of q_0 (the real-q
impossibility, PR #1821 — no categorical object supplies such a pole; the
prior cross-anchor probe's candidates A/B/C/D all fail without a fitted pole).

That bound is a MAGNITUDE-channel bound. The fibre-saddle Φ_b is a pure phase
(|Φ_b| = 1), so its magnitude derivative is identically zero and ALL variation
lives in the phase (bar-odd / Im 𝔙 / decay) channel — on which the smooth-real
magnitude bound is silent. This probe confirms that separation numerically and
witnesses the Lean fact QOU.QBeta.IsSigmaUnitary.crossFactor (the cross-anchor
connecting factor of two σ-unitaries is itself σ-unitary — a pure phase) with
σ = complex conjugation.

## Pre-stated gates (non-fishing)

  G1  magnitude channel FLAT   : |Φ_b(z)| = 1 and |d|Φ_b|/dz| ≈ 0  (≤ 1e-20)
  G2  phase channel VARIES     : |d arg Φ_b / dz| is nonzero        (≥ 1e-3)
  G3  cross-point factor phase : |Φ_b(z₂)·conj Φ_b(z₁)| = 1         (≤ 1e-20)

C14 anti-fitting: nothing here is compared to c_k, Φ₁, the residue A, dc_3/dq,
or any physical constant. The z-grid and fibre points are fixed by corpus
structure (the merged root-of-unity reference set), not by numerical matching.
The 4.66e6 observable-q slope is a SEPARATE (magnitude) channel and is
deliberately NOT reproduced here — this probe is fibre-side only.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from phi_b_evaluator import phi_b  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Repo precision discipline: use the shared COMPUTE_DPS (not a hardcoded dps) so
# the run precision matches the witness precisionMetadata.compute_dps.
DPS = set_compute_dps()

# Fibre points fixed by corpus structure (subset of the merged reference set).
# Evaluate the b² literals inside an explicit precision context (unary `+`
# forces re-rounding to the working dps) so no import-time default truncates.
with mp.workdps(DPS):
    POINTS = [
        ("zeta_4 (b^2 = 1/4, q = i)", +(mp.mpf(1) / 4)),
        ("zeta_6 (b^2 = 1/6, q = e^{iπ/3})", +(mp.mpf(1) / 6)),
    ]
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# Small real base points + a finite-difference step for the z-derivatives.
Z_BASE = [mp.mpf("0.10"), mp.mpf("0.20")]
DZ = mp.mpf("1e-6")


def main() -> int:
    print("=" * 78)
    print(" Φ_b channel separation — magnitude FLAT vs phase VARYING (fibre saddle)")
    print("=" * 78)
    wb = WitnessBuilder("qbeta-fmap-phi-b-channel-separation", engine="mpmath")
    wb.set_description(
        "Fibre-side spec for the z→c_k f-map keystone (PR #3458). On the "
        "validated Faddeev Φ_b (phi_b_evaluator.py), confirms the fibre-saddle "
        "object separates into a FLAT magnitude channel (d|Φ_b|/dz ≈ 0) and a "
        "VARYING phase channel (d arg Φ_b/dz ≠ 0), and witnesses "
        "QOU.QBeta.IsSigmaUnitary.crossFactor (cross-point connecting factor of "
        "two σ-unitaries is σ-unitary) with σ = conjugation. Records the "
        "channel classification of the c_3 cross-anchor swing: PR #1821's "
        "dc_3/dq ≈ 4.66e6 impossibility is a MAGNITUDE-channel bound; the "
        "bar-odd c_3 source lives in the phase channel, which the bound does "
        "not touch. C14 anti-fitting: no comparison to c_k / Φ₁ / residue A / "
        "dc_3/dq / any physical constant; the 4.66e6 observable-q slope is a "
        "separate channel and is NOT reproduced here."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    rows = []
    max_mag_deriv = 0.0            # G1: want ~ 0
    max_unimod_err = 0.0          # G1: |Φ_b| = 1
    min_phase_deriv = mp.inf      # G2: want nonzero (report the min over the grid)
    max_crossfactor_err = 0.0     # G3: connecting-factor unimodularity

    for label, b2 in POINTS:
        b = mp.sqrt(b2)
        q = mp.exp(2 * mp.pi * mp.j * b2)
        print(f"\n  {label}:  b = {mp.nstr(b, 10)},  q = {mp.nstr(q, 8)}")
        pts = []
        for z in Z_BASE:
            v = phi_b(z, b)
            vp = phi_b(z + DZ, b)
            # magnitude channel
            mag = mp.fabs(v)
            magp = mp.fabs(vp)
            unimod = float(mp.fabs(mag - 1))
            dmag = float(mp.fabs((magp - mag) / DZ))
            # phase channel — local phase increment arg(vp/v) is branch-cut
            # robust (the ratio's argument is the principal-branch increment).
            dphase = float(mp.fabs(mp.arg(vp / v)) / DZ)
            # G3: cross-point connecting factor w = Φ_b(z+DZ)·conj Φ_b(z) — σ-unitary?
            w = vp * mp.conj(v)
            crossfac = float(mp.fabs(mp.fabs(w) - 1))

            max_unimod_err = max(max_unimod_err, unimod)
            max_mag_deriv = max(max_mag_deriv, dmag)
            min_phase_deriv = min(min_phase_deriv, mp.mpf(dphase))
            max_crossfactor_err = max(max_crossfactor_err, crossfac)

            print(f"     z = {mp.nstr(z, 4)}:  |Φ_b| = {mp.nstr(mag, 14)}  "
                  f"d|Φ|/dz = {dmag:.2e}   d(arg)/dz = {dphase:.4f}   "
                  f"|cross| − 1 = {crossfac:.2e}")
            pts.append({
                "z": mp.nstr(mp.mpf(z), 6),
                "abs_Phi_b_minus_1": f"{unimod:.3e}",
                "d_abs_dz": f"{dmag:.3e}",
                "d_arg_dz": f"{dphase:.6f}",
                "crossfactor_abs_minus_1": f"{crossfac:.3e}",
            })
        rows.append({"point": label, "b_sq": mp.nstr(mp.mpf(b2), 12),
                     "q": mp.nstr(q, 20), "points": pts})

    min_phase = float(min_phase_deriv)
    print()
    print("  READING:")
    print(f"    magnitude channel FLAT :  max d|Φ_b|/dz = {max_mag_deriv:.2e}  "
          f"(want ≈ 0)")
    print(f"    phase channel VARIES   :  min |d arg Φ_b/dz| = {min_phase:.4f}  "
          f"(want ≠ 0)")
    print(f"    cross-factor σ-unitary :  max ||w| − 1| = {max_crossfactor_err:.2e}")
    print()
    print("  SCOPE (a): fibre-side structural confirmation only. The c_3 swing")
    print("  is thereby classified as a PHASE-channel (bar-odd) quantity; the")
    print("  PR #1821 magnitude bound does not constrain it. NOT a c_3 build.")

    wb.add_data("fibre_points", rows)
    wb.add_data("dz_step", mp.nstr(DZ, 6))
    wb.add_data("evaluator", "computations/qbeta/phi_b_evaluator.py (battery-gated)")
    wb.add_data("lean_witnessed", "QOU.QBeta.IsSigmaUnitary.crossFactor "
                "(FaddeevModularDouble.lean, sorry-free)")
    wb.add_data("channel_classification_of_c3_swing",
                "phase (bar-odd / Im 𝔙 / decay); PR #1821 dc_3/dq≈4.66e6 is a "
                "magnitude-channel bound, silent on the phase channel")

    # G1 — magnitude channel flat (two facets)
    wb.add_assertion(
        "G1a_unimodular_magnitude",
        computed=max_unimod_err, expected=0.0, tolerance=1e-25,
        source="|Φ_b(z)| = 1 at real b, real z (pure phase; prop:phi-b-unitary-bar-odd)",
    )
    wb.add_assertion(
        "G1b_magnitude_derivative_flat",
        computed=max_mag_deriv, expected=0.0, tolerance=1e-20,
        source="d|Φ_b|/dz ≈ 0 — magnitude channel carries no variation",
    )
    # G2 — phase channel varies (nonzero lower bound), boolean-as-float gate.
    wb.add_data("min_phase_derivative", f"{min_phase:.6f}")
    wb.add_assertion(
        "G2_phase_derivative_nonzero",
        computed=1.0 if min_phase > 1e-3 else 0.0, expected=1.0, tolerance=0.5,
        source=f"|d arg Φ_b/dz| ≥ 1e-3 (min observed {min_phase:.4f}) — "
               "phase channel carries the variation",
    )
    # G3 — cross-anchor connecting factor is σ-unitary (Lean crossFactor)
    wb.add_assertion(
        "G3_crossfactor_sigma_unitary",
        computed=max_crossfactor_err, expected=0.0, tolerance=1e-20,
        source="|Φ_b(z₂)·conj Φ_b(z₁)| = 1 — witnesses IsSigmaUnitary.crossFactor",
    )

    ok = (max_unimod_err < 1e-25 and max_mag_deriv < 1e-20
          and min_phase > 1e-3 and max_crossfactor_err < 1e-20)
    print(f"\n  ALL GATES: {'OK' if ok else 'FAILURES'}")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
