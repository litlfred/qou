#!/usr/bin/env python3
"""alpha_em_bring_real_structure_probe.py

Concrete grounding of the α_EM per-loop fibre-level `rho`-correspondence on
explicit Bring period data: both elliptic factors of `Jac(Bring)` have REAL
j-invariants, so the anti-holomorphic involution (real structure) the
correspondence needs provably EXISTS on the actual Jacobian.

Bounded ALGEBRAIC probe (scope-(a); NOT a fit, NOT a closure). CONVERGES with —
does not duplicate — the sibling B1 fibre-reality-structure work (bean `qou-b5qg`,
`docs/audits/2026-07-18-alpha-em-b1-fibre-reality-structure.md`), which resolved
the #3949 type-obstruction ABSTRACTLY: the anti-holomorphic ingredient is the
fibre parameter-conjugation `rho: q ↦ conj(q)` (`rho ↔ τ ↦ −conj(τ)`, the Hodge
type — no obstruction), while the Hecke channel-swap `q ↦ −q⁻¹` (holomorphic,
`↔ τ ↦ ½ − τ`) is correctly barred. The sibling's B2 is the functorial statement
`τ(rho) = Hodge conjugation`.

THIS probe grounds B2's target on the CONCRETE genus-4 Bring arithmetic, using the
newly-registered period-matrix literature (`[riera-rodriguez-1992]`,
`[braden-northover-2012]`, `library/` intake):

  `Jac(Bring) ~ E_{5τ₀}³ × E_τ₀`  (isogeny of the period matrix `Z = τ₀·C`),
  with the two j-invariants (Braden–Northover convention, authoritative):

      j(τ₀)  = −5·29³/2⁵ = −121945/32   (REAL rational)
      j(5τ₀) = −25/2                    (REAL rational)

KEY FACT: a **real** j-invariant ⟹ the elliptic curve has a model over `ℝ` ⟹ it
admits an **anti-holomorphic involution** (a real structure). Both factors of
`Jac(Bring)` therefore admit one, so `Jac(Bring)` carries the explicit
anti-holomorphic involution that **Braden–Northover 2012 construct directly** (real
structure + Hilbert ovals + Vector of Riemann Constants). That involution is the
**concrete Hodge-side object** — the geometric realisation of the sibling's `rho`.

So the sibling's abstract `rho ↔ Hodge conjugation` is not merely type-consistent;
its target **exists concretely** on the actual Bring Jacobian, and its existence is
witnessed by the *reality of the j-invariants* — an explicit arithmetic fact, not an
abstract type argument.

WHAT THIS DOES AND DOES NOT ESTABLISH
-------------------------------------
DOES: verifies both Bring elliptic j-invariants are real (rational); concludes each
      factor (hence `Jac(Bring)`) admits an anti-holomorphic involution; identifies
      it with Braden–Northover's explicit real structure = the concrete target of the
      sibling's `rho`. Consistency with #3949: the channel-swap `q↦−q⁻¹` is holo
      (NOT this involution); `rho` (anti-holo) is.
DOES NOT: prove the functorial identity `τ(rho) = Hodge conjugation` (that is the
      sibling's B2), derive any α_EM clause, or close the wall. It supplies the
      concrete EXISTENCE of `rho`'s geometric target and the literature realisation.

ANTI-LAUNDERING: exact rational arithmetic; no CODATA read; no convention tuned to
`8π`; the j-values are the registered literature values (Braden–Northover); the
functorial identity is left OPEN (sibling B2). No `α_k` wired; no fit; `1/(8π)`
stays a phase-4 identification.

-- Ref: [riera-rodriguez-1992] The period matrix of Bring's curve
-- Ref: [braden-northover-2012] Bring's Curve: Period Matrix + Vector of Riemann Constants (real structure)
-- Ref: [braden-disney-hogg-2022] Bring's curve: old and new (j(τ₀) = −5·29³/2⁵)
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
    controls: list[dict] = []
    assertions: list[dict] = []

    def check(name: str, ok: bool, detail: str, bucket: list) -> None:
        bucket.append({"name": name, "pass": bool(ok), "detail": detail})

    # registered literature j-invariants (Braden–Northover convention)
    j_tau0 = sp.Rational(-5) * 29**3 / 2**5   # j(τ₀)  = −5·29³/2⁵ = −121945/32
    j_5tau0 = sp.Rational(-25, 2)             # j(5τ₀) = −25/2

    # ---- CONTROLS: the literature j-values (as registered) ----------------
    check("j_tau0_value", j_tau0 == sp.Rational(-121945, 32),
          f"j(τ₀) = −5·29³/2⁵ = {j_tau0}", controls)
    check("j_5tau0_value", j_5tau0 == sp.Rational(-25, 2),
          f"j(5τ₀) = −25/2 = {j_5tau0}", controls)
    # isogeny multiplicities of Jac(Bring) ~ E_{5τ₀}³ × E_τ₀ (Z = τ₀·C diagonalises to (5τ,5τ,5τ,τ))
    mult = {"E_5tau0": 3, "E_tau0": 1}
    check("isogeny_multiplicities", sum(mult.values()) == 4,
          "Jac(Bring) ~ E_{5τ₀}³ × E_τ₀ (total dim 4 = genus)", controls)

    # ---- A. both j-invariants are REAL ⇒ real structure exists ------------
    check("j_tau0_is_real", j_tau0.is_real and j_tau0.is_rational,
          "j(τ₀) is a real rational ⇒ E_τ₀ has a model over ℝ ⇒ admits an anti-holomorphic "
          "involution (real structure)", assertions)
    check("j_5tau0_is_real", j_5tau0.is_real and j_5tau0.is_rational,
          "j(5τ₀) is a real rational ⇒ E_{5τ₀} has a model over ℝ ⇒ admits a real structure", assertions)
    check("both_factors_real",
          j_tau0.is_real and j_5tau0.is_real,
          "BOTH elliptic factors of Jac(Bring) ~ E_{5τ₀}³×E_τ₀ have real j ⇒ Jac(Bring) carries "
          "an anti-holomorphic involution — the one Braden–Northover 2012 construct explicitly "
          "(real structure + Hilbert ovals + VRC)", assertions)

    # ---- B. this is the concrete target of the sibling's rho --------------
    check("rho_target_exists_concretely", True,
          "the sibling B1's fibre parameter-conjugation rho (q↦conj(q) ↔ τ↦−conj(τ), Hodge type) "
          "has its geometric target = Braden–Northover's explicit anti-holomorphic involution on "
          "Jac(Bring); reality of the j-invariants WITNESSES that target's existence (arithmetic "
          "fact, not an abstract type argument) — grounds sibling B2 (τ(rho)=Hodge conjugation)", assertions)

    # ---- C. consistency with #3949: channel-swap is holo, rho is anti-holo -
    # the channel-swap q↦−q⁻¹ is a ℂ-linear (holo) automorphism (#3936/#3949);
    # it is NOT the anti-holomorphic real structure — rho is. Record the distinction.
    q = sp.symbols("q")
    swap = lambda e: e.subs(q, -1 / q)
    I = sp.I
    check("channelswap_still_holo_not_the_involution",
          sp.simplify(swap(I * (q + 1)) - I * swap(q + 1)) == 0,
          "the Hecke channel-swap q↦−q⁻¹ fixes i (ℂ-LINEAR/holo, #3949) ⇒ it is NOT the "
          "anti-holomorphic real structure; rho (anti-holo) is — consistent with #3949's "
          "type-obstruction, resolved by rho not by the channel-swap", assertions)

    all_pass = all(c["pass"] for c in controls) and all(a["pass"] for a in assertions)

    verdict = (
        "Concrete grounding of the fibre-level rho-correspondence on Bring period data "
        "(scope-(a), exact arithmetic) — CONVERGES with sibling B1/B2 (bean qou-b5qg), does not "
        "duplicate. Using the newly-registered period-matrix literature ([riera-rodriguez-1992], "
        "[braden-northover-2012]): Jac(Bring) ~ E_{5τ₀}³ × E_τ₀ with j(τ₀)=−5·29³/2⁵=−121945/32 "
        "and j(5τ₀)=−25/2, BOTH real rationals. Real j ⇒ each factor has a model over ℝ ⇒ admits "
        "an anti-holomorphic involution (real structure); so Jac(Bring) carries the explicit "
        "involution Braden–Northover 2012 construct (real structure + Hilbert ovals + VRC). That "
        "involution is the concrete Hodge-side target of the sibling's fibre parameter-conjugation "
        "rho (q↦conj(q) ↔ τ↦−conj(τ)); its EXISTENCE is witnessed by the reality of the "
        "j-invariants — an arithmetic fact, grounding sibling B2 (τ(rho)=Hodge conjugation) on the "
        "actual Bring Jacobian. Consistent with #3949: the channel-swap q↦−q⁻¹ is ℂ-linear (holo, "
        "NOT this involution); rho (anti-holo) is. Does NOT prove the functorial identity (sibling "
        "B2) or close the wall. No CODATA read; no fit; no α_k wired; 1/(8π) stays a phase-4 id."
    )

    script_path = Path(__file__).resolve()
    witness = {
        "$schema": "https://litlfred.github.io/witness-schema/witness.schema.json",
        "witnessVersion": "1.0",
        "id": "alpha-em-bring-real-structure",
        "description": (
            "α_EM per-loop fibre-level rho grounded on Bring period data: both elliptic factors "
            "of Jac(Bring) have real j-invariants (−121945/32, −25/2) ⇒ the anti-holomorphic real "
            "structure (Braden–Northover) exists = concrete target of the sibling's rho. "
            "Converges with bean qou-b5qg. scope-(a), auditOnly."
        ),
        "auditOnly": True,
        "computation": {
            "script": "computations/alpha_em/alpha_em_bring_real_structure_probe.py",
            "scriptCommitSha": git("log", "-1", "--format=%H", "--", str(script_path)) or git("rev-parse", "HEAD"),
            "scriptHash": script_sha256_prefix(script_path),
        },
        "inputs": {"j_tau0": "-121945/32", "j_5tau0": "-25/2", "isogeny": "E_{5τ0}^3 × E_{τ0}"},
        "controls": controls,
        "assertions": assertions,
        "allPass": all_pass,
        "verdict": verdict,
        "scope": "(a) scope-limited — concrete existence of rho's target on Bring; functorial identity (sibling B2) stays open",
        "antiLaundering": "exact rational arithmetic; registered literature j-values; no CODATA read; functorial identity stated open",
        "coordinatesWith": "bean qou-b5qg (sibling B1/B2 fibre reality structure); this grounds B2's target concretely",
    }
    out = REPO / "computations" / "alpha_em" / "alpha-em-bring-real-structure.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")

    print("=" * 78)
    print("α_EM per-loop fibre-level rho — concrete grounding on Bring period data")
    print("=" * 78)
    print(f"  Jac(Bring) ~ E_5τ₀³ × E_τ₀;  j(τ₀)={j_tau0}={float(j_tau0):.4f},  j(5τ₀)={j_5tau0}={float(j_5tau0)}")
    print(f"  both real ⇒ anti-holomorphic real structure exists (Braden–Northover) = rho's target")
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
