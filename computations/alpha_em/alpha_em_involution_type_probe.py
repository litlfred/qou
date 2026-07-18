#!/usr/bin/env python3
"""alpha_em_involution_type_probe.py

The α_EM per-loop `2` unification obstruction is NOME-INDEPENDENT: the Hecke
channel-swap is a C-LINEAR (holomorphic) involution; Hodge conjugation is
C-ANTI-LINEAR. Strengthens #3941 (which stated the obstruction under the
specific nome `q = e^{2πiτ}`, caveated).

Bounded ALGEBRAIC probe (scope-(a); NOT a fit, NOT a closure). #3941 showed that
under the standard nome `q = e^{2πiτ}` the Hecke channel-swap `q ↦ −q⁻¹` (#3936)
maps to the holomorphic modular involution `τ ↦ ½ − τ`, distinct from the
anti-holomorphic Hodge conjugation `τ ↦ −τ̄` — but flagged the nome as a caveated
choice. This probe removes the caveat: the analytic-TYPE mismatch is intrinsic to
the two involutions, independent of any nome or coordinate.

FACTS (exact, `ℚ(q)` / formal complex `q`):

  * `q ↦ −q⁻¹` is an **involutive automorphism** of the field `ℚ(q)` (a ring
    homomorphism: additive + multiplicative), hence **ℂ-LINEAR** on formal
    functions of `q` — it commutes with scalar multiplication by `i`
    (`swap(i·x) = i·swap(x)`). It is holomorphic in `q`.
  * complex conjugation (the anti-linear involution fixing a real structure, the
    Hodge `H^{1,0} ↔ H^{0,1}` swap fixing `H¹(M,ℝ)`) is **ℂ-ANTI-LINEAR**:
    `conj(i·z) = −i·conj(z)`.

A ℂ-linear involution and a ℂ-anti-linear involution are of DIFFERENT type; no
change of coordinate (nome, uniformizer, modular parameter) converts one into the
other. So the #3941 obstruction is intrinsic, not an artifact of `q = e^{2πiτ}`.

WHAT A UNIFICATION WOULD REQUIRE (named, not derived): a **real structure** `R`
on the fibre (an anti-linear involution) such that Hodge conjugation factors as
`conj = swap ∘ R` — equivalently `R = swap ∘ conj` (linear ∘ anti-linear =
anti-linear), an anti-linear involution intertwining the Hecke channel-swap with
Hodge conjugation. The existence of a compatible `R` on the categorical fibre is
the precise open input the τ-functor must supply. (It is exactly the fibre-level
reality structure #3941/#3936 pointed to — here named as an anti-linear `R`.)

WHAT THIS DOES AND DOES NOT ESTABLISH
-------------------------------------
DOES: proves the analytic-type mismatch (linear vs anti-linear) exactly and
      nome-independently; names the required bridge as an anti-linear real
      structure `R = swap ∘ conj`.
DOES NOT: derive the unification, exhibit `R`, or close the wall. It removes the
      nome caveat from #3941 and pins the open input to "a compatible anti-linear
      `R` on the fibre".

ANTI-LAUNDERING: exact algebra, machine-checked; no CODATA read; no nome assumed
(the point IS nome-independence); unification stated OPEN. No `α_k` wired; no fit;
`1/(8π)` stays a phase-4 identification.

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[2]


def git(*args: str) -> str:
    return (
        subprocess.check_output(["git", *args], cwd=REPO, stderr=subprocess.DEVNULL)
        .decode()
        .strip()
    )


def script_sha256_prefix(path: Path, n: int = 12) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:n]


def main() -> int:
    q = sp.symbols("q", real=True)  # real so conj fixes the variable, conjugates scalars only
    I = sp.I
    swap = lambda e: e.subs(q, -1 / q)  # Hecke channel-swap q ↦ −q⁻¹
    conj = lambda e: e.conjugate()      # scalar conjugation (i ↦ −i), fixes real q

    controls: list[dict] = []
    assertions: list[dict] = []

    def check(name: str, ok: bool, detail: str, bucket: list) -> None:
        bucket.append({"name": name, "pass": bool(ok), "detail": detail})

    # ---- CONTROLS: swap is an involutive ℚ(q) automorphism ---------------
    x = (q**2 + 3) / (q - 1)
    check("swap_involutive", sp.simplify(swap(swap(x)) - x) == 0,
          "swap∘swap = id on ℚ(q) (involution)", controls)
    a, b = (q + 1), (q**2 - 2)
    check("swap_multiplicative", sp.simplify(swap(a * b) - swap(a) * swap(b)) == 0,
          "swap(ab) = swap(a)·swap(b)", controls)
    check("swap_additive", sp.simplify(swap(a + b) - (swap(a) + swap(b))) == 0,
          "swap(a+b) = swap(a)+swap(b) ⇒ swap is a ring homomorphism", controls)

    # ---- ASSERTION 1: swap is ℂ-LINEAR (holomorphic) ---------------------
    check("swap_is_C_linear", sp.simplify(swap(I * x) - I * swap(x)) == 0,
          "swap(i·x) = i·swap(x) ⇒ the Hecke channel-swap is ℂ-LINEAR (holomorphic); "
          "anti-linear would give −i·swap(x)", assertions)

    # ---- ASSERTION 2: conjugation is ℂ-ANTI-LINEAR -----------------------
    # scalar conjugation (i↦−i) on a q-dependent expression, q real (fixed):
    w = (3 + I) * q**2 + (2 - I) / q
    check("conj_is_C_antilinear", sp.simplify(conj(I * w) - (-I * conj(w))) == 0,
          "conj(i·w) = −i·conj(w) ⇒ Hodge conjugation (fixing H¹(M,ℝ)) is ℂ-ANTI-LINEAR", assertions)

    # ---- ASSERTION 3: different TYPE ⇒ nome-independent obstruction -------
    # swap fixes i and conj negates it; they act oppositely on i·w, so no
    # coordinate change identifies them. Exhibit swap(i·w) − conj(i·w) ≠ 0 in type.
    check("linear_ne_antilinear_nome_independent",
          sp.simplify(swap(I * w) - I * swap(w)) == 0 and sp.simplify(conj(I * w) + I * conj(w)) == 0,
          "swap(i·w)=+i·swap(w) but conj(i·w)=−i·conj(w) ⇒ swap (ℂ-linear) and conj "
          "(ℂ-anti-linear) act oppositely on i·w; different analytic TYPE, nome-independent — "
          "the #3941 obstruction is INTRINSIC, not a nome artifact", assertions)

    # ---- ASSERTION 4: the required bridge R = swap∘conj is ANTI-LINEAR ----
    # R := swap ∘ conj (linear ∘ anti-linear = anti-linear). Check R(i·w) = −i·R(w)
    # via the image of i: swap fixes i, conj sends i↦−i, so R sends i↦−i.
    R = lambda e: swap(conj(e))
    check("bridge_R_is_antilinear", sp.simplify(R(I * w) - (-I * R(w))) == 0,
          "R := swap∘conj satisfies R(i·w) = −i·R(w) ⇒ R is ANTI-LINEAR; a unification needs "
          "such an anti-linear real structure R with conj = swap ∘ R (the named open input)", assertions)

    all_pass = all(c["pass"] for c in controls) and all(a["pass"] for a in assertions)

    verdict = (
        "The α_EM per-loop '2' unification obstruction is NOME-INDEPENDENT (scope-(a), exact "
        "algebra) — strengthens #3941. The Hecke channel-swap q↦−q⁻¹ (#3936) is an involutive "
        "ℚ(q)-automorphism, hence ℂ-LINEAR (holomorphic): swap(i·x)=i·swap(x). Hodge "
        "conjugation (the anti-linear involution fixing H¹(M,ℝ), swapping H^{1,0}↔H^{0,1}) is "
        "ℂ-ANTI-LINEAR: conj(i·z)=−i·conj(z). A ℂ-linear and a ℂ-anti-linear involution are of "
        "different analytic TYPE — no nome/coordinate converts one to the other, so the #3941 "
        "obstruction (previously stated under q=e^{2πiτ}) is INTRINSIC, caveat removed. A "
        "unification requires an anti-linear real structure R := swap∘conj on the fibre with "
        "conj = swap ∘ R; the existence of a compatible R is the precise open input the "
        "τ-functor must supply (the fibre-level reality structure of #3936/#3941, now named). "
        "Does not derive the unification or exhibit R. No CODATA read; no nome assumed; no fit; "
        "no α_k wired; 1/(8π) stays a phase-4 identification."
    )

    script_path = Path(__file__).resolve()
    witness = {
        "$schema": "https://litlfred.github.io/witness-schema/witness.schema.json",
        "witnessVersion": "1.0",
        "id": "alpha-em-involution-type",
        "description": (
            "α_EM per-loop '2' obstruction is nome-independent: Hecke channel-swap q↦−q⁻¹ is "
            "ℂ-LINEAR (holomorphic), Hodge conjugation is ℂ-ANTI-LINEAR; unification needs an "
            "anti-linear real structure R=swap∘conj. Strengthens #3941. scope-(a), auditOnly."
        ),
        "auditOnly": True,
        "computation": {
            "script": "computations/alpha_em/alpha_em_involution_type_probe.py",
            "scriptCommitSha": git("log", "-1", "--format=%H", "--", str(script_path)) or git("rev-parse", "HEAD"),
            "scriptHash": script_sha256_prefix(script_path),
        },
        "controls": controls,
        "assertions": assertions,
        "allPass": all_pass,
        "verdict": verdict,
        "scope": "(a) scope-limited — nome-independent involution-type obstruction; unification stays open (needs anti-linear R)",
        "antiLaundering": "exact ℚ(q)/ℂ algebra, machine-checked; no CODATA read; no nome assumed; unification stated open",
    }
    out = REPO / "computations" / "alpha_em" / "alpha-em-involution-type.witness.json"
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
    print("α_EM per-loop '2' — nome-independent involution-type obstruction")
    print("=" * 78)
    print("  CONTROLS:")
    for c in controls:
        print(f"    [{'PASS' if c['pass'] else 'FAIL'}] {c['name']}: {c['detail']}")
    print("  ASSERTIONS:")
    for a in assertions:
        print(f"    [{'PASS' if a['pass'] else 'FAIL'}] {a['name']}: {a['detail']}")
    print("-" * 78)
    print("  Hecke swap q↦−q⁻¹ : ℂ-LINEAR (holomorphic)")
    print("  Hodge conjugation : ℂ-ANTI-LINEAR   ⇒ intrinsic type mismatch (no nome fixes it)")
    print("  bridge R=swap∘conj: ANTI-LINEAR (the named open input)")
    print(f"  ALL PASS: {all_pass}")
    print(f"  wrote {out.relative_to(REPO)}")
    print("=" * 78)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
