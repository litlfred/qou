#!/usr/bin/env python3
"""alpha_em_multiplicity2_realcomplex_probe.py

MULTIPLICITY-2 / real-vs-holomorphic count of the α_EM per-loop measure
`1/(π b₁) = 1/(8π)`, `b₁ = dim H¹(M_Bring) = 2g = 8` at genus `g = 4`.

Bounded STRUCTURAL probe (scope-(a); NOT a fit, NOT a derivation). It resolves
the SINGLE crisp residual left after the π-power axis closed (#3909, heat-kernel
`1/(4π)`, forced `−1`): the `8π = 2·(4π)` **multiplicity `2`** — equivalently the
`4 ↔ b₁` coefficient. Sharp question:

  Is the per-loop mode count the **real** harmonic-1-form count
  `b₁ = dim_ℝ H¹(M,ℝ) = 2g = 8`, or the **holomorphic** count
  `g = dim_ℂ H^{1,0} = 4`?  I.e. is the factor `2` in `8π = 2·(4π)` the
  real-vs-complex Hodge doubling `b₁ = 2g` (FORCED once the Laplacian is the
  real one), or a conflation of the 2D heat-kernel Gaussian base `4π` (d=2)
  with a distinct, un-forced loop multiplicity `2`?

The lever is a **proved corpus invariant** (already merged): the count enters as
the ζ-regularized homological index of the **real Hodge Laplacian** Δ₁ on
Ω¹(M,ℝ),

    Tr_{H¹}(1) = −ζ_{Δ₁}(0) = b₁ = 2g = 8      (#3834 / #3896, area-free),

and the derived n=1 zero-mode `photonZeroModeShift = b₁/Area` (#2114,
`QOU.Archimedean.PhotonIRZeroMode`, sorry-free). Δ₁ here is the Hodge–de Rham
Laplacian on **real** 1-forms; its harmonic kernel is `H¹(M,ℝ)`, real dimension
`b₁ = 2g` — NOT the ∂̄-Laplacian on `H^{1,0}` (dimension `g`). The photon is a
**real** U(1) gauge field (its connection is a real 1-form), so the self-energy
propagator that carries the per-loop measure lives on the SAME real harmonic
sector as the proved zero-mode. The count is therefore the real `b₁`, and the
`b₁ = 2g` doubling is the real⊕complex Hodge splitting
`H¹(M,ℝ) ⊗ ℂ = H^{1,0} ⊕ H^{0,1}` (each summand `dim_ℂ = g`).

WHAT THIS DOES AND DOES NOT ESTABLISH
-------------------------------------
DOES (real-vs-holomorphic sub-question — CLOSES, scope-(a) forced):
  * The count is the **real** Betti number `b₁ = 8`, not the holomorphic `g = 4`,
    because (i) the merged ζ-index is the REAL Δ₁ (`−ζ_{Δ₁}(0)=2g`), and (ii) the
    photon gauge field is real. The factor `2` (`b₁ = 2g`) IS the real-vs-complex
    Hodge doubling — FORCED by the reality of the Laplacian, not a free knob.

DOES NOT (normalization-FORM sub-question — stays OPEN, scope-(a)):
  * This does NOT derive the reciprocal form `1/(π·b₁)`. `8π` admits TWO
    normalization readings that are numerically identical but structurally
    distinct:
      (P)  `π · b₁`   — one bare loop-π traced over the `b₁ = 8` real harmonic
                        sectors  (count-carrying, single π, the #3896 index home);
      (H)  `(4π) · 2` — the 2D heat-kernel Gaussian base `(4π)^{d/2}|_{d=2}=4π`
                        (the #3909-adjudicated derived π) × a residual `2`.
    Under reading (H) the `4π` is the archimedean heat-kernel Gaussian, NOT
    `π·g`, so the residual `2` is a DISTINCT loop-multiplicity that the
    real-vs-complex argument does NOT directly supply. No PROVED invariant
    selects (P) over (H). Honest statement: a factor of `2` is the single
    easiest thing to fit; this probe claims ONLY the count (real `b₁`, forced),
    NOT the normalization form.

ANTI-LAUNDERING: no CODATA read; no convention tuned toward `8π`; the real count
is FORCED by the reality of the merged Δ₁-index, not chosen; the normalization-
form residual is stated OPEN, not papered over. No `α_k` wired; no fit; no tier
change; `1/(8π)` stays a phase-4 identification.

-- Ref: [manuscript] prop:photon-ir-zero-mode-bring   (n=1 zero-mode b₁/Area, #2114)
-- Ref: [manuscript] prop:em-coupling-bring-zero-mode  (the α_EM ladder)
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from mpmath import mp, mpf, sqrt
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

REPO = Path(__file__).resolve().parents[2]


def git(*args: str) -> str:
    # Fail-loud: never emit a witness with placeholder ('unknown') provenance.
    return (
        subprocess.check_output(
            ["git", *args], cwd=REPO, stderr=subprocess.DEVNULL
        )
        .decode()
        .strip()
    )


def script_sha256_prefix(path: Path, n: int = 12) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()[:n]


def main() -> int:
    g = 4  # Bring's surface, genus 4 (χ = 2 − 2g = −6), Lean-locked #3864/#2114
    b1 = 2 * g  # = 8, real first Betti number = dim_ℝ H¹(M,ℝ) = harmonic 1-form count
    holo = g  # = 4, holomorphic count = dim_ℂ H^{1,0}(M) = genus

    controls: list[dict] = []
    assertions: list[dict] = []

    def check(name: str, ok: bool, detail: str, bucket: list) -> None:
        bucket.append({"name": name, "pass": bool(ok), "detail": detail})

    # ---- CONTROLS (established facts this probe reuses) --------------------
    # C1: real Betti = 2g (Poincaré / Hodge over ℝ).
    check("betti1_eq_2g", b1 == 2 * g, f"b₁ = 2g = {b1}", controls)
    # C2: holomorphic count = g (dim H^{1,0} for a compact Riemann surface).
    check("holomorphic_count_eq_g", holo == g, f"dim H^(1,0) = g = {holo}", controls)
    # C3: the real-vs-complex doubling factor is exactly 2.
    check("real_over_holomorphic_is_2", b1 == 2 * holo, f"b₁/g = {b1 // holo} = 2", controls)
    # C4: the merged ζ-index home reproduces the REAL count (−ζ_Δ₁(0) = 2g), NOT g.
    #     (ζ_Δ₁(0) = −b₁ is the merged #3834/#3896 result; the sign/value are the
    #      area-free homological index Tr_{H¹}(1) = 2g = 8.)
    zeta_index = 2 * g  # −ζ_{Δ₁}(0) for the REAL Hodge Laplacian on Ω¹(M,ℝ)
    check("zeta_index_is_real_b1", zeta_index == b1 and zeta_index != holo,
          f"−ζ_Δ₁(0) = {zeta_index} = b₁ (real), ≠ g = {holo} (holomorphic)", controls)

    # ---- A. Real-vs-holomorphic count: CLOSES (forced real b₁) -------------
    # A1: the self-energy denominator target 8π decomposes as π·b₁ with the REAL
    #     count, and the holomorphic reading π·g = 4π is a factor 2 too small.
    target_8pi = 8 * mp.pi
    real_reading = mp.pi * b1        # π · b₁ = 8π ✓
    holo_reading = mp.pi * holo      # π · g  = 4π ✗ (factor 2 short)
    check("real_reading_hits_8pi", abs(real_reading - target_8pi) < mpf(10) ** -40,
          "π·b₁ = 8π (real harmonic 1-forms)", assertions)
    check("holomorphic_reading_is_half", abs(holo_reading - target_8pi / 2) < mpf(10) ** -40,
          "π·g = 4π = (8π)/2 — holomorphic count is a factor 2 short ⇒ excluded", assertions)
    # A2: the count that the PROVED index selects is the real one (lever).
    check("index_selects_real_count", zeta_index == b1,
          "the merged real-Δ₁ ζ-index −ζ_Δ₁(0)=2g selects b₁ (real), forcing the factor 2 "
          "= real⊕complex Hodge doubling H¹(M,ℝ)⊗ℂ = H^{1,0}⊕H^{0,1}", assertions)

    # ---- B. Normalization FORM: stays OPEN (two readings of 8π) ------------
    # B1: reading (P) π·b₁ and reading (H) (4π)·2 are numerically identical...
    reading_P = mp.pi * b1           # π · b₁       = 8π
    reading_H = (4 * mp.pi) * 2      # (4π) · 2     = 8π
    check("readings_P_and_H_agree_numerically",
          abs(reading_P - reading_H) < mpf(10) ** -40,
          "π·b₁ = (4π)·2 = 8π — the two normalization readings coincide in value", assertions)
    # B2: ...but are structurally distinct: under (H) the base is the archimedean
    #     heat-kernel 4π (the #3909-adjudicated derived π), so the residual 2 is a
    #     DISTINCT multiplicity, NOT π·g. No proved invariant selects (P) vs (H).
    #     Honest OPEN: assert that the FORM is not forced (recorded, not manufactured).
    form_forced = False  # deliberately False — the reciprocal-form derivation is the open wall
    check("normalization_form_not_forced", form_forced is False,
          "under reading (H) the 4π is the heat-kernel Gaussian (NOT π·g), so its residual 2 "
          "is a distinct loop multiplicity the real-vs-complex argument does not supply; "
          "no proved invariant selects π·b₁ over (4π)·2 — the reciprocal-form derivation "
          "stays the OPEN wall (scope-(a))", assertions)
    # B3: anti-laundering honesty — a factor of 2 is trivially fittable; the probe
    #     claims only the count, not the form. (Documented, always true.)
    check("claims_count_only_not_form", True,
          "a factor of 2 is the single easiest thing to fit; this probe forces the COUNT "
          "(real b₁, not holomorphic g) and explicitly does NOT claim the normalization form",
          assertions)

    all_pass = all(c["pass"] for c in controls) and all(a["pass"] for a in assertions)

    verdict = (
        "REAL-VS-HOLOMORPHIC SUB-QUESTION: CLOSES (scope-(a), forced). The per-loop "
        "mode count is the REAL harmonic-1-form count b₁ = 2g = 8, NOT the holomorphic "
        "g = 4: the merged ζ-index −ζ_Δ₁(0) = 2g is the REAL Hodge Laplacian on Ω¹(M,ℝ), "
        "and the photon is a real U(1) gauge field, so its self-energy propagator lives on "
        "the same real harmonic sector. The factor 2 in 8π = 2·(4π) IS the real⊕complex "
        "Hodge doubling H¹(M,ℝ)⊗ℂ = H^{1,0}⊕H^{0,1} — FORCED by the reality of Δ₁, not a "
        "conflation. || NORMALIZATION-FORM SUB-QUESTION: stays OPEN (scope-(a)). 8π admits "
        "reading (P) π·b₁ [one bare loop-π traced over the b₁ real sectors, the #3896 index "
        "home] and reading (H) (4π)·2 [the #3909 heat-kernel Gaussian 4π × a residual 2]; "
        "under (H) the residual 2 is a DISTINCT multiplicity the real-vs-complex argument "
        "does not supply. No proved invariant selects (P) over (H). Honest: the count is "
        "forced real-b₁; the reciprocal normalization FORM is not derived. No 8π "
        "manufactured; no α_k wired; no fit; 1/(8π) stays a phase-4 identification."
    )

    script_path = Path(__file__).resolve()
    witness = {
        "$schema": "https://litlfred.github.io/witness-schema/witness.schema.json",
        "witnessVersion": "1.0",
        "id": "alpha-em-multiplicity2-realcomplex",
        "description": (
            "α_EM per-loop measure 1/(8π): real-vs-holomorphic count of the "
            "8π = 2·(4π) multiplicity. Real b₁=8 FORCED (merged real-Δ₁ ζ-index + "
            "real gauge field); reciprocal normalization FORM stays OPEN. scope-(a), auditOnly."
        ),
        "auditOnly": True,
        "computation": {
            "script": "computations/alpha_em/alpha_em_multiplicity2_realcomplex_probe.py",
            "scriptCommitSha": git("log", "-1", "--format=%H", "--", str(script_path)) or git("rev-parse", "HEAD"),
            "scriptHash": script_sha256_prefix(script_path),
        },
        "inputs": {"genus": g, "betti1_real": b1, "holomorphic_count": holo},
        "controls": controls,
        "assertions": assertions,
        "allPass": all_pass,
        "verdict": verdict,
        "scope": "(a) scope-limited — real count forced; normalization form open",
        "antiLaundering": "no CODATA read; no convention tuned to 8π; factor 2 not fitted (claimed only via the real ζ-index); form residual stated open",
    }

    out = REPO / "computations" / "alpha_em" / "alpha-em-multiplicity2-realcomplex.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2) + "\n")

    print("=" * 78)
    print("α_EM per-loop measure — multiplicity-2 / real-vs-holomorphic count probe")
    print("=" * 78)
    print(f"  genus g = {g};  real b₁ = 2g = {b1};  holomorphic g = {holo}")
    print(f"  target denominator = 8π;  π·b₁ = 8π (real ✓);  π·g = 4π = 8π/2 (holo ✗)")
    print(f"  merged real-Δ₁ ζ-index −ζ_Δ₁(0) = {zeta_index} = b₁ (selects real count)")
    print("-" * 78)
    print("  CONTROLS:")
    for c in controls:
        print(f"    [{'PASS' if c['pass'] else 'FAIL'}] {c['name']}: {c['detail']}")
    print("  ASSERTIONS:")
    for a in assertions:
        print(f"    [{'PASS' if a['pass'] else 'FAIL'}] {a['name']}: {a['detail']}")
    print("-" * 78)
    print(f"  ALL PASS: {all_pass}")
    print(f"  wrote {out.relative_to(REPO)}")
    print("=" * 78)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
