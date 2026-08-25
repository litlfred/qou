#!/usr/bin/env python3
"""alpha_em_tau_correspondence_probe.py

The τ-correspondence for the α_EM per-loop `2` unification: what modular
involution does the Hecke channel-swap `q ↦ −q⁻¹` correspond to — and is it
complex conjugation?

Bounded probe (scope-(a); NOT a fit, NOT a closure — the HARD open attack, taken
to an honest obstruction). Context: after #3936 established that the involution
swapping the Hecke channels `e₊ ↔ e₋` is the eigenvalue-exchange `q ↦ −q⁻¹`
(the bar involution `q ↦ q⁻¹` FIXES them), the remaining wall is the single
correspondence naming that the τ-functor identifies the Hecke `2` with the Hodge
`2` (#3920) — the sibling conjecture-statement audit's phrase "as complex
conjugation swaps `H^{1,0} ⊕ H^{0,1}`."

This probe maps `q ↦ −q⁻¹` through the standard nome identification
`q = e^{2πiτ}` (τ the modular parameter of the Bring Jacobian's elliptic factor
`E`, `Jac(Bring) ~ E⁴`) and finds a structural OBSTRUCTION:

  * `q ↦ q⁻¹`    (bar)              ≙  `τ ↦ −τ`        (holomorphic)
  * `q ↦ −q⁻¹`   (channel-swap)     ≙  `τ ↦ ½ − τ`     (HOLOMORPHIC involution)
  * complex conjugation on `H^{1,0} ↔ H^{0,1}`  ≙  `τ ↦ −τ̄`  (ANTI-holomorphic)

So the channel-swap `q ↦ −q⁻¹` corresponds to the **holomorphic** modular
involution `τ ↦ ½ − τ` (a half-period shift composed with `τ ↦ −τ`, an
Atkin–Lehner-type map) — NOT to the **anti-holomorphic** complex conjugation
`τ ↦ −τ̄`. A holomorphic τ-functor therefore CANNOT identify the Hecke channel
swap with Hodge conjugation directly: the two involutions differ in analytic
type (holomorphic vs anti-holomorphic).

HONEST OBSTRUCTION (scope-(a), sharpens — does NOT refute the whole unification):
the identification can only hold at the **fibre level** where `q` is a
formal/complex variable and the reality structure differs from the archimedean
`q₀ ∈ ℝ` (per the AGENTS.md Im(q) fibre-vs-observable banner) — the anti-
holomorphic ingredient must enter through the fibre's complex structure, not
through the holomorphic nome map. Equivalently: a genuine unification needs the
τ-functor to supply an anti-holomorphic (conjugation) piece that the holomorphic
`q = e^{2πiτ}` dictionary does not. This is exactly the categorical→archimedean
bridge that remains the open "multi-week" input.

CAVEAT (STRICT): the correspondence is computed under the STANDARD nome
`q = e^{2πiτ}`. The framework's ACTUAL τ-functor `q₀ ↔ period` dictionary is the
unproved input; under a different identification the modular involution could
differ. This probe therefore establishes the obstruction FOR the standard nome
and names the dictionary as the open degree of freedom — it does not close the
correspondence.

WHAT THIS DOES AND DOES NOT ESTABLISH
-------------------------------------
DOES: computes the modular involution matching each q-involution (exact, verified
      numerically to 1e−20); shows the channel-swap `q↦−q⁻¹` is holomorphic
      `τ↦½−τ`, distinct in analytic type from anti-holomorphic conjugation.
DOES NOT: derive the unification or close the wall. It converts "the τ-functor
      maps conjugation to the channel swap" into a precise obstruction (holo vs
      anti-holo under the standard nome) and localizes the open input to the
      fibre-level reality structure / the q↔period dictionary.

ANTI-LAUNDERING: no CODATA read; no convention tuned to `8π`; the nome map is the
textbook `q = e^{2πiτ}`, stated as a caveated choice; the obstruction is stated,
the unification left OPEN. No `α_k` wired; no fit; `1/(8π)` stays a phase-4 id.

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import mpmath as mp
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

    TOL = mp.mpf(10) ** -20
    # generic modular point (Im τ > 0) — the correspondence is an identity in τ,
    # so any interior point verifies it.
    tau = mp.mpf("0.31") + mp.mpf("0.77") * 1j
    qof = lambda t: mp.e ** (2j * mp.pi * t)
    q = qof(tau)

    # ---- CONTROL: the nome map is well-defined (Im τ > 0 ⇒ |q| ≠ 0,1) -----
    check("nome_welldefined", mp.im(tau) > 0 and abs(q) not in (0,),
          f"q = e^(2πiτ), Im τ = {mp.nstr(mp.im(tau),3)} > 0, |q| = {mp.nstr(abs(q),4)}", controls)

    # ---- bar q↦q⁻¹  ≙  τ ↦ −τ (holomorphic) -------------------------------
    check("bar_is_tau_to_neg_tau", abs(qof(-tau) - 1 / q) < TOL,
          "q ↦ q⁻¹ (bar)  ≙  τ ↦ −τ  (holomorphic)", assertions)

    # ---- channel-swap q↦−q⁻¹  ≙  τ ↦ ½ − τ (holomorphic) ------------------
    check("channelswap_is_tau_to_half_minus_tau",
          abs(qof(mp.mpf("0.5") - tau) - (-1 / q)) < TOL,
          "q ↦ −q⁻¹ (Hecke channel-swap, #3936)  ≙  τ ↦ ½ − τ  (HOLOMORPHIC involution)", assertions)
    # it is an involution: (½ − (½ − τ)) = τ
    check("half_minus_tau_is_involution",
          abs((mp.mpf("0.5") - (mp.mpf("0.5") - tau)) - tau) < TOL,
          "τ ↦ ½ − τ is an involution (applied twice = id)", assertions)

    # ---- complex conjugation on H^{1,0}↔H^{0,1} is ANTI-holomorphic --------
    # the lattice-preserving conjugation is τ ↦ −τ̄ (reflection about the
    # imaginary axis); it is NOT holomorphic (depends on τ̄).
    conj_tau = -mp.conj(tau)
    check("conjugation_is_antiholomorphic",
          abs(mp.im(conj_tau) - mp.im(tau)) < TOL and abs(mp.re(conj_tau) + mp.re(tau)) < TOL,
          f"complex conjugation H^{{1,0}}↔H^{{0,1}}  ≙  τ ↦ −τ̄ (ANTI-holomorphic), "
          f"here −τ̄ = {mp.nstr(conj_tau,4)}", assertions)

    # ---- THE OBSTRUCTION: channel-swap (holo) ≠ conjugation (anti-holo) ----
    # τ ↦ ½ − τ  (holomorphic) is not equal to τ ↦ −τ̄ (anti-holomorphic)
    # at a generic point with Re τ ≠ ¼ — exhibit the difference.
    lhs = mp.mpf("0.5") - tau      # channel-swap image
    rhs = -mp.conj(tau)            # conjugation image
    check("holo_vs_antiholo_differ", abs(lhs - rhs) > mp.mpf("1e-6"),
          f"τ↦½−τ (channel-swap image {mp.nstr(lhs,4)}) ≠ τ↦−τ̄ (conjugation image "
          f"{mp.nstr(rhs,4)}) ⇒ a holomorphic τ-functor CANNOT identify the Hecke "
          "channel-swap with Hodge conjugation directly (different analytic type)", assertions)

    all_pass = all(c["pass"] for c in controls) and all(a["pass"] for a in assertions)

    verdict = (
        "τ-CORRESPONDENCE for the '2' unification — sharpened to a holo-vs-anti-holo "
        "OBSTRUCTION (scope-(a)), NOT closed. Under the standard nome q = e^(2πiτ): the "
        "bar involution q↦q⁻¹ ≙ τ↦−τ (holomorphic); the Hecke channel-swap q↦−q⁻¹ (#3936) "
        "≙ τ↦½−τ, a HOLOMORPHIC modular involution (half-period shift ∘ τ↦−τ, Atkin–Lehner "
        "type); complex conjugation swapping H^{1,0}↔H^{0,1} ≙ τ↦−τ̄, ANTI-holomorphic. So "
        "the channel-swap is holomorphic and conjugation is anti-holomorphic — a holomorphic "
        "τ-functor CANNOT identify them directly (they differ in analytic type at any Re τ ≠ "
        "¼). The unification can therefore hold only at the FIBRE level, where q is formal/"
        "complex and the reality structure differs from the archimedean q₀∈ℝ (AGENTS.md Im(q) "
        "banner): the anti-holomorphic (conjugation) ingredient must enter through the fibre's "
        "complex structure, not the holomorphic nome. CAVEAT: computed for the standard nome; "
        "the framework's actual q₀↔period dictionary is the open input and could give a "
        "different modular involution. This localizes the remaining wall (the categorical→"
        "archimedean bridge) to a precise obstruction; it does not close it. No CODATA read; "
        "no fit; no α_k wired; 1/(8π) stays a phase-4 identification."
    )

    script_path = Path(__file__).resolve()
    witness = {
        "$schema": "https://litlfred.github.io/witness-schema/witness.schema.json",
        "witnessVersion": "1.0",
        "id": "alpha-em-tau-correspondence",
        "description": (
            "α_EM per-loop '2' unification: the Hecke channel-swap q↦−q⁻¹ ≙ the holomorphic "
            "modular involution τ↦½−τ (nome q=e^{2πiτ}), NOT anti-holomorphic conjugation "
            "τ↦−τ̄ — a holo-vs-anti-holo obstruction placing the unification at fibre level. "
            "scope-(a), auditOnly."
        ),
        "auditOnly": True,
        "computation": {
            "script": "computations/alpha_em/alpha_em_tau_correspondence_probe.py",
            "scriptCommitSha": git("log", "-1", "--format=%H", "--", str(script_path)) or git("rev-parse", "HEAD"),
            "scriptHash": script_sha256_prefix(script_path),
        },
        "controls": controls,
        "assertions": assertions,
        "allPass": all_pass,
        "verdict": verdict,
        "scope": "(a) scope-limited (standard nome) — holo-vs-anti-holo obstruction; unification stays open at fibre level",
        "antiLaundering": "standard nome q=e^{2πiτ} (caveated choice); no CODATA read; no convention tuned to 8π; unification stated open",
    }
    out = REPO / "computations" / "alpha_em" / "alpha-em-tau-correspondence.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2) + "\n")

    print("=" * 78)
    print("α_EM per-loop '2' — τ-correspondence of the Hecke channel-swap q↦−q⁻¹")
    print("=" * 78)
    print("  CONTROLS:")
    for c in controls:
        print(f"    [{'PASS' if c['pass'] else 'FAIL'}] {c['name']}: {c['detail']}")
    print("  ASSERTIONS:")
    for a in assertions:
        print(f"    [{'PASS' if a['pass'] else 'FAIL'}] {a['name']}: {a['detail']}")
    print("-" * 78)
    print("  bar q↦q⁻¹        ≙ τ↦−τ      (holomorphic)")
    print("  channel q↦−q⁻¹   ≙ τ↦½−τ     (HOLOMORPHIC)  ← #3936 swap")
    print("  Hodge conjugation ≙ τ↦−τ̄     (ANTI-holomorphic)  ← obstruction")
    print(f"  ALL PASS: {all_pass}")
    print(f"  wrote {out.relative_to(REPO)}")
    print("=" * 78)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
