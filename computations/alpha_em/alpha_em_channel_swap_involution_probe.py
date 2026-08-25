#!/usr/bin/env python3
"""alpha_em_channel_swap_involution_probe.py

Which involution swaps the two Hecke channels `e₊/e₋` — refining the α_EM
per-loop-measure "unification of the 2" hypothesis.

Bounded ALGEBRAIC probe (scope-(a); NOT a fit, NOT a closure). Extends the
same-day sibling conjecture-statement audit
(`2026-07-18-alpha-em-perloop-conjecture-statement.md`, landed on main), which
NAMED — but did not derive — a unification hypothesis for the three readings of
the `2` in `8π = 2·(4π)`:

  > "the bar involution `q ↔ q⁻¹` swaps `e₊/e₋` exactly as complex conjugation
  >  swaps `H^{1,0} ⊕ H^{0,1}`" (Hodge doubling, #3920 `484c86462`),

so that a τ-functor correspondence would identify the Hecke channel pair with
the Hodge conjugate pair and reduce all three `2`-readings to one object.

This probe VERIFIES the algebraic core of that hypothesis exactly (sympy over
`ℚ(q)`), and finds it must be CORRECTED:

  * the Hecke bar involution `q ↦ q⁻¹`, `σ ↦ σ⁻¹` (with `σ⁻¹ = σ − (q − q⁻¹)`)
    **FIXES** each idempotent — `bar(e₊) = e₊`, `bar(e₋) = e₋` — it does NOT
    swap them. So the hypothesis as literally stated is refuted;
  * the involution that DOES swap `e₊ ↔ e₋` is the **eigenvalue-exchange**
    substitution `q ↦ −q⁻¹` (exchanging the two Hecke eigenvalues `q`, `−q⁻¹`).
    It also sends `[2]_q ↦ −[2]_q` — the sign flip is exactly the derivability
    map's separately-underived **global "−" alternation**, so the channel-swap
    involution ties the multiplicity-`2` and the global sign to ONE operation.

Corrected bridge (scope-(a), sharper than the named hypothesis): a τ-functor
unifying the Hodge `2` (complex conjugation `H^{1,0} ↔ H^{0,1}`, #3920) with the
Hecke `2` (`e₊ ↔ e₋`) must map complex conjugation to `q ↦ −q⁻¹`, NOT to the bar
involution `q ↦ q⁻¹`. Because `q ↦ −q⁻¹` sends the real substrate `q₀ ≈ 1.11` to
`≈ −0.90` (real-negative — NOT a conjugation of a real number), the
identification is necessarily a **fibre-level** statement (formal/complex `q`,
`Im q` unconstrained per the AGENTS.md fibre-vs-observable banner); at the
observable anchor `q₀` (`Im q₀ = 0`) it is not conjugation.

WHAT THIS DOES AND DOES NOT ESTABLISH
-------------------------------------
DOES (scope-(a), exact): refutes the literal "bar swaps the channels" (bar FIXES
     them); identifies the channel-swap as `q ↦ −q⁻¹`; shows it carries
     `[2]_q ↦ −[2]_q` (the global sign); places the unification at fibre level.
DOES NOT: derive the unification, close the wall, or wire anything. The
     correspondence "complex conjugation ≙ `q ↦ −q⁻¹` under τ" remains the open
     conjecture — this probe only fixes WHICH involution it must be.

ANTI-LAUNDERING: no CODATA read; no convention tuned to `8π`; the involutions are
exact `ℚ(q)` algebra, machine-checked; the correspondence is stated OPEN. No
`α_k` wired; no fit; no tier change; `1/(8π)` stays a phase-4 identification.

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


def main() -> int:
    q, sigma = sp.symbols("q sigma")
    br2 = q + 1 / q  # [2]_q
    ep = (sigma + 1 / q) / br2  # e₊ (projector onto eigenvalue q)
    em = (q - sigma) / br2  # e₋ (projector onto eigenvalue −q⁻¹)

    controls: list[dict] = []
    assertions: list[dict] = []

    def check(name: str, ok: bool, detail: str, bucket: list) -> None:
        bucket.append({"name": name, "pass": bool(ok), "detail": detail})

    # ---- CONTROLS: e₊, e₋ are the two Hecke idempotents -------------------
    check("idempotents_sum_to_one", sp.simplify(ep + em - 1) == 0,
          "e₊ + e₋ = 1", controls)
    # e₊ projects onto eigenvalue q: σ·e₊ = q·e₊  (mod σ² = (q−q⁻¹)σ + 1)
    sig2 = (q - 1 / q) * sigma + 1
    def reduce_sig(expr):
        # reduce any σ² to (q−q⁻¹)σ+1 (single reduction suffices for degree-2 terms here)
        e = sp.expand(expr)
        e = e.subs(sigma**2, sig2)
        return sp.simplify(e)
    check("e_plus_eigen_q", reduce_sig(sigma * ep - q * ep) == 0,
          "σ·e₊ = q·e₊ (eigenvalue q)", controls)
    check("e_minus_eigen_negqinv", reduce_sig(sigma * em - (-1 / q) * em) == 0,
          "σ·e₋ = −q⁻¹·e₋ (eigenvalue −q⁻¹)", controls)

    # ---- bar involution q↦q⁻¹, σ↦σ⁻¹ : FIXES the idempotents --------------
    def bar(expr):
        e = expr.subs(q, 1 / q)                        # coefficients q ↦ q⁻¹
        e = e.subs(sigma, sigma - (q - 1 / q))         # σ ↦ σ⁻¹ (original q)
        return sp.simplify(e)
    check("bar_fixes_e_plus", sp.simplify(bar(ep) - ep) == 0,
          "bar(e₊) = e₊ — the bar involution q↦q⁻¹ FIXES e₊ (does NOT swap)", assertions)
    check("bar_fixes_e_minus", sp.simplify(bar(em) - em) == 0,
          "bar(e₋) = e₋ — bar FIXES e₋ too", assertions)
    check("bar_does_not_swap", sp.simplify(bar(ep) - em) != 0,
          "bar(e₊) ≠ e₋ — the NAMED hypothesis ('bar swaps the channels') is REFUTED", assertions)

    # ---- eigenvalue-exchange q↦−q⁻¹ : SWAPS the idempotents ---------------
    swap = lambda e: sp.simplify(e.subs(q, -1 / q))
    check("eigswap_swaps_plus_to_minus", sp.simplify(swap(ep) - em) == 0,
          "under q↦−q⁻¹: e₊ ↦ e₋  (SWAPS the channels — this is the correct involution)", assertions)
    check("eigswap_swaps_minus_to_plus", sp.simplify(swap(em) - ep) == 0,
          "under q↦−q⁻¹: e₋ ↦ e₊", assertions)
    check("eigswap_flips_bracket_sign", sp.simplify(br2.subs(q, -1 / q) + br2) == 0,
          "under q↦−q⁻¹: [2]_q ↦ −[2]_q — the sign flip IS the global '−' alternation "
          "(derivability map's separate underived global dressing sign)", assertions)

    # ---- fibre-level: q↦−q⁻¹ at real q₀ is real-negative, not conjugation --
    q0 = mpf("1.10997859555733471")  # muon-q₀ canonical (computations/ layer)
    swapped = -1 / q0
    check("eigswap_real_q0_is_real_negative",
          swapped < 0 and abs(swapped.imag if hasattr(swapped, "imag") else 0) < mpf(10) ** -40,
          f"q₀ ≈ {mp.nstr(q0,6)} ↦ −q₀⁻¹ ≈ {mp.nstr(swapped,4)} (real-negative) ⇒ at the "
          "observable anchor (Im q₀ = 0) the swap is NOT conjugation; the unification is a "
          "FIBRE-level statement (formal/complex q, per the Im(q) banner)", assertions)

    all_pass = all(c["pass"] for c in controls) and all(a["pass"] for a in assertions)

    verdict = (
        "Unification hypothesis for the '2' CORRECTED (scope-(a), exact ℚ(q) algebra) — the "
        "wall is NOT closed. The sibling conjecture-statement audit named 'the bar involution "
        "q↦q⁻¹ swaps e₊/e₋ as conjugation swaps H^{1,0}/H^{0,1}'. Machine-checked result: the "
        "Hecke bar involution (q↦q⁻¹, σ↦σ⁻¹) FIXES each idempotent — bar(e₊)=e₊, bar(e₋)=e₋ — "
        "it does NOT swap them, so the literal hypothesis is REFUTED. The involution that DOES "
        "swap e₊↔e₋ is the eigenvalue-exchange q↦−q⁻¹; it also sends [2]_q↦−[2]_q, so the same "
        "operation carries the derivability map's separate underived global '−' alternation. "
        "CORRECTED bridge: a τ-functor unifying the Hodge 2 (conjugation on H^{1,0}⊕H^{0,1}, "
        "#3920) with the Hecke 2 (e₊↔e₋) must map complex conjugation to q↦−q⁻¹, NOT the bar "
        "involution. Since q↦−q⁻¹ sends real q₀≈1.11 to ≈−0.90 (real-negative, not a "
        "conjugation of a real), the identification is FIBRE-level (complex/formal q, Im q "
        "unconstrained per the AGENTS.md banner); at observable q₀ it is not conjugation. This "
        "sharpens WHICH involution the correspondence must implement; it does NOT derive it. No "
        "CODATA read; no fit; no α_k wired; 1/(8π) stays a phase-4 identification."
    )

    script_path = Path(__file__).resolve()
    witness = {
        "$schema": "https://litlfred.github.io/witness-schema/witness.schema.json",
        "witnessVersion": "1.0",
        "id": "alpha-em-channel-swap-involution",
        "description": (
            "α_EM per-loop '2' unification: which involution swaps the Hecke channels e₊/e₋. "
            "bar (q↦q⁻¹) FIXES them (refutes the named hypothesis); q↦−q⁻¹ SWAPS them and "
            "flips [2]_q (the global sign). Corrected τ-bridge is fibre-level. scope-(a), auditOnly."
        ),
        "auditOnly": True,
        "computation": {
            "script": "computations/alpha_em/alpha_em_channel_swap_involution_probe.py",
            "scriptCommitSha": git("log", "-1", "--format=%H", "--", str(script_path)) or git("rev-parse", "HEAD"),
            "scriptHash": script_sha256_prefix(script_path),
        },
        "controls": controls,
        "assertions": assertions,
        "allPass": all_pass,
        "verdict": verdict,
        "scope": "(a) scope-limited — refutes the literal bar-swap; identifies q↦−q⁻¹ as the channel-swap; unification stays open (fibre-level)",
        "antiLaundering": "exact ℚ(q) algebra, machine-checked; no CODATA read; no convention tuned to 8π; correspondence stated open",
    }
    out = REPO / "computations" / "alpha_em" / "alpha-em-channel-swap-involution.witness.json"
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
    print("α_EM per-loop '2' — which involution swaps the Hecke channels e₊/e₋")
    print("=" * 78)
    print("  CONTROLS:")
    for c in controls:
        print(f"    [{'PASS' if c['pass'] else 'FAIL'}] {c['name']}: {c['detail']}")
    print("  ASSERTIONS:")
    for a in assertions:
        print(f"    [{'PASS' if a['pass'] else 'FAIL'}] {a['name']}: {a['detail']}")
    print("-" * 78)
    print(f"  bar (q↦q⁻¹): FIXES e₊,e₋ (named hypothesis refuted)")
    print(f"  q↦−q⁻¹     : SWAPS e₊↔e₋ AND flips [2]_q↦−[2]_q (the global sign)")
    print(f"  ALL PASS: {all_pass}")
    print(f"  wrote {out.relative_to(REPO)}")
    print("=" * 78)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
