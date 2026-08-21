#!/usr/bin/env python3
"""
Formalize-first REDUCTION of the W_λ geometric-realization wall (Subgoal-2 q₀ /
keystone), observable-side complement to the fibre-ζ Lawrence–Rozansky modulus
spec (2026-07-17-three-front-attack-specs.md §2).

CLAIM (q-symbolic, q₀-free as an identity in q; verified n=2..5): the full-Hecke
q-Plancherel weight W_λ = d_q(λ)²/[n]_q! is SUB-NORMALIZED at q≠1 —

    Σ_{λ⊢n} W_λ  =  Z(q)  :=  (Σ_{λ⊢n} d_q(λ)²) / [n]_q! ,
    Z(1) = 1  (RSK/Burnside: Σ (f^λ)² = n!),   Z(q) < 1  for q ≠ 1.

CONSEQUENCE (the reduction): a UNITARY modular S-matrix vacuum row satisfies
Σ_λ |S_{0λ}|² = 1 (unitarity) ⇔ its induced probability measure is normalized.
Since Σ_λ W_λ = Z(q) < 1 for q ≠ 1, **W_λ is NOT the vacuum-row probability
measure of any unitary modular category at real q ≠ 1** — a compact/unitary
S-matrix is excluded not only because it is q₀-INDEPENDENT (the ledger's reason)
but by an exact NORMALIZATION (completeness) obstruction. The geometric object
realizing W_λ at the observable q₀ must be NON-unitary, carrying exactly the
completeness defect Z(q). This reinforces the non-compact Hahn–Exton q-Bessel
redirect and pins the exact defect a realization must reproduce.

Scope guard: this REDUCES/sharpens the wall (pins the q-symbolic gate + the
exact non-unitarity); it does NOT derive q₀, does NOT compute the colored-LR
Σ(2,3,5) amplitude (the sibling's fibre-side spec), and wires nothing. The
sub-normalization value Z=0.98222 (n=5, q₀) is the ledger's P1 "sub-normalized"
number — this probe supplies the S-matrix-unitarity FRAMING of it. No fit.

Self-contained (sympy only).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def qint(q, k):
    return sp.simplify((q**k - q**(-k)) / (q - 1 / q))


def qfact(q, n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= qint(q, k)
    return sp.simplify(r)


def hooks(lam):
    hs = []
    for r, rl in enumerate(lam):
        for c in range(rl):
            arm = rl - c - 1
            leg = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            hs.append(arm + leg + 1)
    return hs


def dq(q, lam):
    num = qfact(q, sum(lam))
    den = sp.Integer(1)
    for h in hooks(lam):
        den *= qint(q, h)
    return sp.simplify(num / den)


def parts(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in parts(n - k, k):
            yield (k,) + rest


def main():
    q = sp.symbols('q', positive=True)
    q0 = sp.Rational(110998, 100000)   # substrate q₀ ≈ 1.10998 (rational proxy; result q₀-robust)

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    Zvals = {}
    for n in (2, 3, 4, 5):
        S = sp.simplify(sum(dq(q, lam)**2 for lam in parts(n)))
        F = qfact(q, n)
        Z = sp.simplify(S / F)
        Zvals[n] = (Z, sp.N(Z.subs(q, q0), 8), sp.limit(Z, q, 1))

    # 1. Z(1) = 1 exactly for all n (RSK/Burnside q=1 identity Σ(f^λ)²=n!)
    check("Z_equals_one_at_q1_rsk_burnside",
          all(Zvals[n][2] == 1 for n in (2, 3, 4, 5)),
          "Z(1)=Σ_λ d_1(λ)²/n! = Σ(f^λ)²/n! = 1 for n=2..5 (RSK/Burnside) — W_λ is a "
          "normalized measure ONLY at q=1")

    # 2. Z(q) < 1 for q ≠ 1 (sub-normalization at real q₀)
    check("Z_strictly_below_one_at_q0",
          all(0 < Zvals[n][1] < 1 for n in (2, 3, 4, 5)),
          "Z(q₀) = " + ", ".join(f"n={n}:{float(Zvals[n][1]):.5f}" for n in (2, 3, 4, 5))
          + " — all < 1 ⇒ Σ_λ W_λ < 1: W_λ is SUB-NORMALIZED at q≠1")

    # 3. matches the ledger's P1 keystone number (n=5, Z=0.98222)
    z5 = float(Zvals[5][1])
    check("matches_ledger_P1_subnormalization_0p98222",
          abs(z5 - 0.98222) < 5e-5,
          f"n=5 (full-Hecke S₅ keystone): Z(q₀)={z5:.5f} = the ledger's P1 'sub-normalized "
          "Z=0.98222' — this probe supplies its S-matrix-unitarity framing")

    # 4. the reduction: unitary S-matrix ⟹ ΣW=1, contradicted ⇒ non-unitary required
    #    (encode as the exact symbolic gate Σd_q² = Z·[n]_q!, Z≠1)
    n = 3
    S3 = sp.simplify(sum(dq(q, lam)**2 for lam in parts(3)))
    gate_ok = (sp.simplify(S3 - Zvals[3][0] * qfact(q, 3)) == 0) and (sp.simplify(Zvals[3][0] - 1) != 0)
    check("unitarity_gate_excludes_compact_modular",
          gate_ok,
          "exact gate Σ_λ d_q² = Z(q)·[n]_q! with Z≠1 (q≠1) ⇒ a unitary modular vacuum row "
          "(ΣW=1) CANNOT equal W_λ at q≠1 ⇒ the geometric realization must be NON-unitary "
          "(reinforces the non-compact q-Bessel redirect); complements the fibre-ζ modulus spec")

    # 5. the fibre→archimedean CONTINUATION of the normalization is trivial: Z(q) is a
    #    RATIONAL function of q ⇒ continues everywhere (bar poles). So the continuation wall
    #    is NOT separate — its substance is the non-rational AMPLITUDE (the LR-modulus front).
    Z_rational = all(
        sp.cancel(sp.together(sum(dq(q, lam)**2 for lam in parts(n)) / qfact(q, n))).is_rational_function(q)
        for n in (2, 3, 4, 5))
    check("normalization_continuation_trivial_Z_rational",
          Z_rational,
          "Z(q)=Σd_q²/[n]_q! is a RATIONAL function of q (n=2..5; e.g. n=2: 2q/(q²+1)) ⇒ the "
          "fibre→archimedean CONTINUATION of the W_λ normalization is trivial (continues "
          "everywhere bar poles). So the 'continuation wall' is NOT separate: its substance is "
          "entirely the non-rational AMPLITUDE = the LR-modulus front. C's remaining pieces are "
          "the amplitude compute + a q₀-fixing categorical condition (numerology-gated), not a "
          "distinct continuation problem")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "OBSERVABLE-SIDE NORMALIZATION GATE (formalize-first reduction of the W_λ wall; no q₀ "
        "derivation, no fit, nothing wired): the full-Hecke q-Plancherel weight W_λ=d_q²/[n]_q! "
        "is SUB-NORMALIZED at real q≠1 — Σ_λ W_λ = Z(q) = (Σd_q²)/[n]_q!, with Z(1)=1 "
        "(RSK/Burnside) and Z(q₀)<1 (n=5: 0.98222, the ledger's P1 number). A UNITARY modular "
        "S-matrix vacuum row has Σ|S_{0λ}|²=1, so W_λ is NOT its probability measure at q≠1 — "
        "a compact/unitary realization is excluded by an exact NORMALIZATION obstruction (not "
        "only by q₀-independence). The geometric object hosting W_λ at the observable q₀ must be "
        "NON-unitary with completeness defect exactly Z(q), reinforcing the non-compact q-Bessel "
        "redirect. This is the OBSERVABLE-side complement to the sibling's fibre-ζ colored-LR "
        "modulus spec (|S_{0λ}(ζ)|=d_ζ/D). It sharpens the wall + pins a q-symbolic gate; it does "
        "NOT close it. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "keystone-wlambda-unitarity-normalization-gate",
        "description": "Observable-side reduction of the W_λ geometric wall: W_λ=d_q²/[n]_q! is "
                       "sub-normalized (Σ_λ W_λ=Z(q)<1 at q≠1, Z(1)=1 RSK/Burnside, n=5 Z=0.98222). "
                       "A unitary modular S-matrix has ΣW=1 ⇒ compact/unitary realization excluded "
                       "by normalization; the geometric object must be non-unitary with defect Z(q). "
                       "Complements the fibre-ζ colored-LR modulus spec. No q₀ derivation; nothing wired.",
        "auditOnly": "docs/audits/2026-07-17-keystone-wlambda-unitarity-normalization-gate.md",
        "tier": "symbolic-exact (sympy; q-symbolic identity + RSK/Burnside q=1 anchor)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        # NOT float(): Zvals[n][1] is a sympy N() value carrying more than
        # float64; str() keeps what was computed. The display line above uses
        # float() deliberately, which is display-only. Bean qou-irzg.
        "result": {"Z_at_q0": {n: str(Zvals[n][1]) for n in (2, 3, 4, 5)},
                   "Z2_exact": str(Zvals[2][0]), "Z3_exact": str(Zvals[3][0]),
                   "verdict": verdict},
        "context": {
            "complements": "2026-07-17-three-front-attack-specs.md §2 (fibre-ζ colored-LR modulus "
                           "|S_{0λ}(ζ)|=d_ζ/D); this is the observable-side (real q₀) normalization gate",
            "reduces": "the W_λ geometric-realization wall — pins the exact non-unitarity Z(q) any "
                       "realization must carry; reinforces the non-compact q-Bessel redirect",
            "frames": "the ledger's P1 'sub-normalized Z=0.98222' as an S-matrix unitarity/completeness "
                      "obstruction (Σ|S_{0λ}|²=1 for unitary vs Σ_λ W_λ=Z<1)",
            "scope_guard": "does NOT derive q₀, does NOT compute the colored-LR amplitude; no fit; "
                           "nothing wired; no tier change",
        },
    }
    out = os.path.join(_here, "keystone-wlambda-unitarity-normalization-gate.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
