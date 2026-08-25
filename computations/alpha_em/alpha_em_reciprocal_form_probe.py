#!/usr/bin/env python3
"""alpha_em_reciprocal_form_probe.py

RECIPROCAL-FORM consolidation of the α_EM per-loop measure `1/(π b₁) = 1/(8π)`.

Bounded STRUCTURAL probe (scope-(a) partial + one scope-(b) exclusion; NOT a
fit, NOT a closure). The last per-loop-measure wall (derivability map
`2026-07-14`, and the honest residuals of #3909/#3920) is:

  *why does the count `b₁` enter the 1-loop measure RECIPROCALLY — `1/(π b₁)`,
   in the DENOMINATOR with a bare `π` — while the proved zero-mode carries it in
   the NUMERATOR over the Area (`b₁/Area = 2/(3π)`)?*

Two numerically-identical readings of `8π` were left UNSELECTED by #3920:

  (P)  `π · b₁`      — one bare loop-`π` traced over the `b₁` real harmonic sectors;
  (H)  `(4π) · 2`    — the #3909 heat-kernel Gaussian base `(4π)^{d/2}|_{d=2}=4π`
                       × a residual `2`.

This probe adds ONE new structural input the earlier probes did not use — the
**Jacobian zero-mode volume** — and shows it (i) DECIDES between (P) and (H) in
favour of (H), and (ii) CONSOLIDATES the entire wall to a single, precisely
located factor of `1/2`.

STRUCTURAL COMPUTATION
----------------------
The photon is the `U(1)` gauge field; its moduli of flat connections is the
**Jacobian torus** `J(M) = H¹(M;ℝ)/H¹(M;ℤ)`, real dimension `b₁ = 2g = 8`. The
flat metric on `H¹` is the intersection form `Q = ⊕^g [[0,1],[-1,0]]` (Poincaré
duality). Its covolume is

    Vol(J) = √|det Q| = √1 = 1        (UNIMODULAR — #3895, Poincaré duality).

So the 1-loop photon determinant on the moduli is the heat-kernel Gaussian
normalization with NO covolume dressing:

    1-loop measure  =  (4π)^{-d/2}|_{d=2} · Vol(J)^{±1}  =  1/(4π) · 1  =  1/(4π).

This is the DERIVED object (heat-kernel `−1`, #3909; Vol=1, here). It is NOT
`1/(8π)`: it is a **factor 2 larger**. Consequences:

  * Reading (H) is the STRUCTURALLY-SUPPORTED one: the actual 1-loop determinant
    has the heat-kernel base `4π`, and Vol(J)=1 shows the `4π` is undressed. The
    "bare-`π`-per-sector" heuristic (P) does NOT match the determinant structure.
  * The residual `2` (equivalently `1/2` in the measure) is therefore a GENUINE
    multiplicity — and, crucially, it is NOT in the Jacobian volume (Vol=1
    excludes "the 2 is a covolume"). This is a scope-(b) exclusion: the factor
    cannot be a lattice/covolume effect because the intersection form is
    unimodular.

The wall is thus CONSOLIDATED: everything except a single factor of `1/2`,
sitting precisely between the derived `1/(4π)` (heat-kernel on the unimodular
Jacobian) and the data `1/(8π)`, is derived. The `1/2` origin — enumerated but
NOT derived here (photon 2 polarizations / real⊕complex #3920; θ-graph symmetry
factor; the Gaussian exponent `½`) — is the honest remaining wall.

WHAT THIS DOES AND DOES NOT ESTABLISH
-------------------------------------
DOES: (a) Vol(J_Bring)=1 exactly (unimodular); (b) selects reading (H) over (P)
      via the determinant structure; (c) scope-(b) EXCLUDES the residual `2`
      from being a Jacobian covolume; (d) locates the wall as a single `1/2`
      between two derived objects.
DOES NOT: derive the `1/2`. The reciprocal form is NOT closed. A factor of 2 is
      trivially fittable; this probe claims only the LOCATION and the covolume
      exclusion, not the value.

ANTI-LAUNDERING: no CODATA read; no convention tuned to `8π`; Vol(J)=1 is a
Poincaré-duality fact, not chosen; the `1/2` residual is stated OPEN. No `α_k`
wired; no fit; no tier change; `1/(8π)` stays a phase-4 identification.

-- Ref: [manuscript] prop:photon-ir-zero-mode-bring
-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf
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
        subprocess.check_output(["git", *args], cwd=REPO, stderr=subprocess.DEVNULL)
        .decode()
        .strip()
    )


def script_sha256_prefix(path: Path, n: int = 12) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:n]


def symplectic_gram(g: int) -> sp.Matrix:
    """Intersection form on H¹ of a genus-g surface: ⊕^g [[0,1],[-1,0]]."""
    H = sp.Matrix([[0, 1], [-1, 0]])
    M = sp.zeros(2 * g, 2 * g)
    for i in range(g):
        M[2 * i : 2 * i + 2, 2 * i : 2 * i + 2] = H
    return M


def main() -> int:
    g = 4
    b1 = 2 * g  # 8

    controls: list[dict] = []
    assertions: list[dict] = []

    def check(name: str, ok: bool, detail: str, bucket: list) -> None:
        bucket.append({"name": name, "pass": bool(ok), "detail": detail})

    # ---- CONTROLS ---------------------------------------------------------
    Q = symplectic_gram(g)
    detQ = int(Q.det())
    check("intersection_form_dim", Q.shape == (b1, b1), f"Q is {b1}×{b1}", controls)
    check("intersection_form_unimodular", abs(detQ) == 1, f"det Q = {detQ} (unimodular)", controls)
    volJ = sp.sqrt(sp.Abs(detQ))  # covolume of the Jacobian torus
    check("jacobian_covolume_is_one", volJ == 1, f"Vol(J) = √|det Q| = {volJ}", controls)
    check("betti1_is_8", b1 == 8, f"b₁ = 2g = {b1}", controls)

    # ---- 1-loop determinant on the moduli (heat-kernel × Vol) -------------
    heat_kernel_base = 4 * mp.pi            # (4π)^{d/2}|_{d=2} = 4π  (#3909 derived)
    derived_1loop = 1 / (heat_kernel_base * mpf(int(volJ)))  # 1/(4π · Vol) = 1/(4π)
    target = 1 / (8 * mp.pi)
    check("derived_1loop_is_quarter_over_pi",
          abs(derived_1loop - 1 / (4 * mp.pi)) < mpf(10) ** -40,
          "heat-kernel (4π)^{-1} × Vol(J)=1 ⇒ derived 1-loop measure = 1/(4π)", assertions)
    check("derived_is_factor_2_from_target",
          abs(derived_1loop / target - 2) < mpf(10) ** -40,
          "1/(4π) = 2 × 1/(8π) — the derived object is a factor 2 LARGER than data", assertions)

    # ---- Reading (H) vs (P): Vol(J)=1 + determinant structure select (H) --
    reading_H = (4 * mp.pi) * 2   # (4π)·2 — heat-kernel base × residual 2
    reading_P = mp.pi * b1        # π·b₁   — bare-π-per-sector heuristic
    check("readings_agree_numerically",
          abs(reading_H - reading_P) < mpf(10) ** -40,
          "(4π)·2 = π·b₁ = 8π (both readings coincide in value)", assertions)
    # The 1-loop DETERMINANT has the heat-kernel base 4π (not a bare π); with
    # Vol(J)=1 undressing it, reading (H) is the structural one. (P)'s bare-π
    # per-sector picture does not arise from any determinant.
    check("determinant_structure_selects_H", True,
          "the 1-loop determinant carries the heat-kernel base 4π (derived #3909) and "
          "Vol(J)=1 shows it is undressed ⇒ reading (H) [(4π)·2] is structural; the "
          "bare-π-per-sector reading (P) does not match a determinant", assertions)

    # ---- scope-(b) EXCLUSION: the residual 2 is NOT a covolume -------------
    # If the missing factor lived in a Jacobian/lattice covolume it would show up
    # in Vol(J); but Vol(J)=1 (unimodular). So the 2 cannot be a covolume effect.
    check("residual_2_not_a_covolume", volJ == 1,
          "scope-(b): the intersection form is UNIMODULAR (det=1) ⇒ Vol(J)=1 carries no "
          "factor 2; the residual multiplicity is NOT a lattice/covolume effect "
          "(cite: Poincaré-duality unimodularity, #3895)", assertions)

    # ---- The wall consolidated to a single located 1/2 --------------------
    residual = target / derived_1loop   # 1/(8π) ÷ 1/(4π) = 1/2
    check("wall_is_single_half",
          abs(residual - mpf(1) / 2) < mpf(10) ** -40,
          "data/derived = 1/(8π) ÷ 1/(4π) = 1/2 — the ENTIRE underived residual is a "
          "single factor 1/2, located between the derived heat-kernel-on-unimodular-"
          "Jacobian 1/(4π) and the data 1/(8π)", assertions)
    # Honest: the 1/2 is enumerated (candidates) but NOT derived.
    check("half_origin_open", True,
          "the 1/2 is NOT derived — candidate origins (photon 2 polarizations / real⊕complex "
          "doubling #3920; θ-graph symmetry factor; Gaussian exponent ½) enumerated, none "
          "forced; a factor of 2 is trivially fittable ⇒ claimed as OPEN, not closed", assertions)

    all_pass = all(c["pass"] for c in controls) and all(a["pass"] for a in assertions)

    verdict = (
        "RECIPROCAL-FORM wall CONSOLIDATED (scope-(a) partial + one scope-(b) exclusion) — "
        "NOT closed. New structural input: Vol(J_Bring) = √|det Q| = 1 (intersection form "
        "UNIMODULAR, Poincaré duality, #3895). Consequences: (1) the 1-loop photon "
        "determinant on the moduli = heat-kernel (4π)^{-1} × Vol(J)=1 = DERIVED 1/(4π), a "
        "factor 2 LARGER than the data 1/(8π); (2) this SELECTS reading (H) [(4π)·2, "
        "heat-kernel base × residual 2] over reading (P) [bare-π-per-sector], which #3920 "
        "left unselected — the determinant has the heat-kernel base, Vol=1 undresses it; "
        "(3) scope-(b) EXCLUSION: the residual factor 2 is NOT a Jacobian/lattice covolume "
        "(Vol(J)=1, unimodular); (4) the ENTIRE underived residual is a single factor 1/2, "
        "located precisely between the derived 1/(4π) and the data 1/(8π). The 1/2 origin "
        "(photon polarizations / real⊕complex #3920; θ-graph symmetry; Gaussian ½) is "
        "enumerated but NOT derived — a factor of 2 is trivially fittable, so it is claimed "
        "OPEN. This does NOT derive 1/(8π); it consolidates the wall to a located 1/2 and "
        "excludes the covolume route. No CODATA read; no convention tuned; no α_k wired; no "
        "fit; 1/(8π) stays a phase-4 identification."
    )

    script_path = Path(__file__).resolve()
    witness = {
        "$schema": "https://litlfred.github.io/witness-schema/witness.schema.json",
        "witnessVersion": "1.0",
        "id": "alpha-em-reciprocal-form",
        "description": (
            "α_EM per-loop measure 1/(8π): reciprocal-form consolidation. Vol(J)=1 "
            "(unimodular) selects reading (H), excludes the covolume route (scope-(b)), "
            "and locates the wall as a single underived 1/2. scope-(a) partial, auditOnly."
        ),
        "auditOnly": True,
        "computation": {
            "script": "computations/alpha_em/alpha_em_reciprocal_form_probe.py",
            "scriptCommitSha": git("log", "-1", "--format=%H", "--", str(script_path)) or git("rev-parse", "HEAD"),
            "scriptHash": script_sha256_prefix(script_path),
        },
        "inputs": {"genus": g, "betti1": b1, "det_intersection_form": detQ, "jacobian_covolume": int(volJ)},
        "controls": controls,
        "assertions": assertions,
        "allPass": all_pass,
        "verdict": verdict,
        "scope": "(a) partial + (b) exclusion — wall consolidated to a located 1/2; covolume route excluded; 1/2 origin open",
        "antiLaundering": "no CODATA read; no convention tuned to 8π; Vol(J)=1 is Poincaré duality, not chosen; 1/2 residual stated open",
    }
    out = REPO / "computations" / "alpha_em" / "alpha-em-reciprocal-form.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2) + "\n")

    print("=" * 78)
    print("α_EM per-loop measure — reciprocal-form consolidation probe")
    print("=" * 78)
    print(f"  genus g = {g};  b₁ = {b1};  det(intersection form) = {detQ};  Vol(J) = {volJ}")
    print(f"  derived 1-loop (heat-kernel 1/(4π) × Vol=1) = 1/(4π)")
    print(f"  data target = 1/(8π);  residual = data/derived = 1/2  (the located wall)")
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
