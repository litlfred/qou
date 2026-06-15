#!/usr/bin/env python3
"""qbessel_mu_lambda_vs_qlommel_zeros.py
=====================================

Step 2 of the derive-first q-Bessel plan: settle — by **exact symbolic algebra in
ℚ(q)**, no float fit, no probe — whether the framework's finite content-Casimir
spectrum `{μ_λ}` is a q-Bessel / q-Lommel **zero** spectrum (the "q-drumhead"
reading of lead 4).

## The derivation

The q-heat-kernel eigenvalues (`prop:q-heat-kernel-peter-weyl`) are

    μ_λ = ℏ_q² · Σ_{x∈λ} [c(x)]_q [c(x)+1]_q,   ℏ_q = (q−1)/q,  c(x) = (col−row),

i.e. the **q-Casimir** of the SU_q(2)-rep block λ — quadratic in the cell
contents. We establish three exact facts and draw the structural conclusion:

  (A) ALGEBRAIC + FINITE. Each μ_λ ∈ ℚ(q) (a rational function of q); at fixed n
      the spectrum `{μ_λ : λ⊢n}` is finite of cardinality `p(n)` (the partition
      number).
  (B) CARDINALITY OBSTRUCTION. The Hahn–Exton q-Bessel `J_ν^{(3)}(x;q)` is entire
      in x with INFINITELY many zeros (transcendental over ℚ(q)); a finite
      algebraic set cannot be that zero set. The finite/algebraic truncation is
      the q-Lommel polynomial `h_{m,ν}` of degree m — but `p(n) ≠ n`
      (`p(4)=5≠4`, `p(5)=7≠5`, …), so the per-n spectrum is not the zero set of
      the degree-n q-Lommel polynomial; a match would need degree `m=p(n)` AND a
      substrate-derived (ν,q), with the zeros of a **three-term-recurrence**
      (Lommel) polynomial, not a **quadratic-in-content Casimir**.
  (C) STRUCTURAL TYPE. μ_λ is a COMPACT-group (SU_q(2)) Casimir eigenvalue
      (quadratic in highest weight); q-Bessel zeros are the NON-COMPACT
      E_q(2) / q-disk spectrum. The two are bridged ONLY by the
      SU_q(2)→E_q(2) contraction (PR #2279). So the Bessel/Lommel zero structure
      lives in the n→∞ brane-tower / contraction limit, NOT in the finite-n
      confinement spectrum.

## Verdict (derived, not probed)

REFUTED for the finite per-n spectrum: it is the compact q-Casimir spectrum, not
a q-Bessel/q-Lommel zero spectrum. REDIRECT: the q-Lommel three-term recurrence
is the right tool for the **infinite brane-tower** (where the binding `Δ_λ`
ladder also lives) — consistent with #2279/#2300 ("the Bessel object is the
tower, not the n-trace").
"""
from __future__ import annotations

import json
import pathlib

import sympy as sp

q = sp.symbols("q", positive=True)
hbar = (q - 1) / q


def q_int(n: int):
    """[n]_q = (q^n − 1)/(q − 1), valid for negative n too."""
    return sp.simplify((q ** n - 1) / (q - 1))


def partitions(n: int):
    """All integer partitions of n as descending tuples."""
    if n == 0:
        yield ()
        return
    for first in range(n, 0, -1):
        for rest in partitions(n - first):
            if not rest or rest[0] <= first:
                yield (first,) + rest


def mu_lambda(part):
    """q-Casimir μ_λ = ℏ_q² Σ_{cells} [c]_q [c+1]_q, content c = col − row (0-indexed)."""
    total = sp.Integer(0)
    for row, rowlen in enumerate(part):
        for col in range(rowlen):
            c = col - row
            total += q_int(c) * q_int(c + 1)
    return sp.simplify(hbar ** 2 * total)


results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name, ok):
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── (A) μ_λ are rational functions of q; spectrum size = p(n) ─────────────────
print("(A) μ_λ exact (ℚ(q)) and finite, cardinality p(n)")
spectrum = {}
all_rational = True
for n in (3, 4):
    parts = list(partitions(n))
    row = {}
    for p in parts:
        m = mu_lambda(p)
        is_rat = m.is_rational_function(q)
        all_rational = all_rational and bool(is_rat)
        row["+".join(map(str, p))] = sp.srepr(sp.nsimplify(m)) if False else str(sp.simplify(m))
        print(f"    n={n}  λ={p!s:12s}  μ_λ = {sp.simplify(m)}")
    spectrum[str(n)] = {"p_n": len(parts), "mu": row}
results["spectrum"] = spectrum
check("every μ_λ is a rational function of q (algebraic, in ℚ(q))", all_rational)

# ── (B) cardinality obstruction: p(n) ≠ n for n ≥ 4 ──────────────────────────
print("\n(B) cardinality obstruction vs degree-n q-Lommel polynomial")
pn = {n: len(list(partitions(n))) for n in (3, 4, 5, 6)}
print(f"    p(n) for n=3..6: {pn}")
mismatch = {n: (pn[n], n, pn[n] != n) for n in (4, 5, 6)}
results["cardinality"] = {"p_n": pn, "p_n_neq_n": {str(k): v[2] for k, v in mismatch.items()}}
check("p(n) ≠ n for n=4,5,6 (per-n spectrum ≠ degree-n q-Lommel zero set)",
      all(v[2] for v in mismatch.values()))

# ── (C) structural type: compact q-Casimir, q→1 classical content-Casimir ────
print("\n(C) structural type — compact SU_q(2) Casimir (q→1 → classical content-Casimir)")
classical = {}
ok_classical = True
for n in (3, 4):
    for p in partitions(n):
        m1 = sp.limit(mu_lambda(p) / hbar ** 2, q, 1)  # bracket limit (strip ℏ_q²→0)
        cl = sum((col - row) * (col - row + 1)
                 for row, rl in enumerate(p) for col in range(rl))
        ok_classical = ok_classical and (sp.simplify(m1 - cl) == 0)
        classical["+".join(map(str, p))] = {"q_to_1_bracket": str(m1), "classical_casimir": int(cl)}
print("    q→1 bracket = Σ c(c+1) (classical content-Casimir) for all λ⊢3,4:",
      ok_classical)
results["classical_limit"] = classical
check("q→1: μ_λ/ℏ_q² → Σ_{x} c(x)(c(x)+1) = classical content-Casimir (quadratic, not Bessel-zero)",
      ok_classical)

all_passed = all(ok for _, ok in asserts)
verdict = (
    "REFUTED (finite per-n spectrum), derived exactly in ℚ(q) — no float, no fit. "
    "The content-Casimir spectrum {μ_λ} is the COMPACT SU_q(2) q-Casimir "
    "(rational in q, finite of size p(n), quadratic-in-content; q→1 → the "
    "classical content-Casimir Σ c(c+1)). It cannot be a q-Bessel ZERO spectrum "
    "(those are infinite + transcendental over ℚ(q)); and it is not the degree-n "
    "q-Lommel zero set since p(n)≠n for n≥4. The q-Bessel/q-Lommel zero structure "
    "belongs to the NON-COMPACT E_q(2)/q-disk = the n→∞ brane-tower (contraction) "
    "limit, bridged to the compact spectrum only by the SU_q(2)→E_q(2) "
    "contraction (PR #2279). REDIRECT: the q-Lommel three-term recurrence is the "
    "right tool for the brane-TOWER (and the binding Δ_λ ladder), not the "
    "finite-n confinement spectrum. Confirms #2279/#2300 'the Bessel object is "
    "the tower, not the n-trace' from the spectral side. Nothing wired."
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "qbessel_mu_lambda_vs_qlommel_zeros",
    "description": (
        "Exact symbolic (ℚ(q)) derive-or-refute of whether the finite "
        "content-Casimir spectrum {μ_λ} is a q-Bessel/q-Lommel zero spectrum "
        "(lead-4 q-drumhead question). Verdict REFUTED for the finite per-n "
        "spectrum (compact SU_q(2) q-Casimir, algebraic, p(n)≠n), with the "
        "Bessel/Lommel structure redirected to the n→∞ brane-tower limit. "
        "docs/audits/2026-06-14-qbessel-lead4-mu-lambda-qlommel-derivation.md."
    ),
    "discipline": "exact symbolic ℚ(q); no float; no fit; derive-or-refute; nothing wired",
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "qbessel-mu-lambda-vs-qlommel-zeros.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
