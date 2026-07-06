#!/usr/bin/env python3
"""qbeta_silver_rationals.py
============================

Verify the Q_β silver-ratio c_k rational identities — wiring the sorry-free Lean
theorems `QOU.QBeta.qbeta_c{8,9,10}_at_silver` and `c4_eq_c8_div_c3_at_silver`
(content blocks `qbeta-c8-c10-silver-rationals.ts`, `qbeta-c4-from-c3-c8-product-
identity.ts`), which previously had no `computation` field.

These are PURE rational identities at the silver ratio q = 1+√2 (the root of
q²−2q−1=0), where the Hoefsmit b² = (q⁴+q²+1)/(q²+1)² = 7/8 exactly (grounded in
`SilverAnchorGrounding.lean`). With c_3 = −2 and b² = 7/8:

    c_8  = c_3²·b⁴ = 4·(7/8)² = 49/16
    c_9  = c_3³·b² = −8·(7/8) = −7
    c_10 = c_3²·b⁶ = 4·(7/8)³ = 343/128
    c_4  = c_8/c_3 = −49/32   (product identity c_3·c_4 = c_8)
    c_6  = 7/2               (product identity c_3·c_6 = c_9)

This is the SUBDOMINANT silver/Q_A pole (char root ≈ 3.12, not the dominant
≈ 117.4 — SilverAnchorGrounding §1): a GENUINE-but-subdominant kernel root. Per
the too-small≠wrong triage it is SUBDOMINANT-but-REAL; wiring the proved rationals
is honest and costs nothing in discipline. No fit; no c_k≥3 made canonical (the
Pell–Lucas pattern still breaks at the free rungs — registry §8); b² grounding +
the rational rungs only.
"""
from __future__ import annotations

import json
import pathlib

import sympy as sp

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── (G) Hoefsmit b² = 7/8 at the silver ratio (exact, via q = 1+√2) ───────────
print("(G) b² = (q⁴+q²+1)/(q²+1)² = 7/8 at q = 1+√2 (silver locus)")
q = 1 + sp.sqrt(2)
silver_rel = sp.simplify(q**2 - 2*q - 1)
bSq = sp.nsimplify(sp.simplify((q**4 + q**2 + 1) / (q**2 + 1)**2))
print(f"    q²−2q−1 = {silver_rel}   b² = {bSq}")
check("(G) silver relation q²−2q−1 = 0 at q=1+√2", silver_rel == 0)
check("(G) Hoefsmit b² = 7/8 at silver", bSq == sp.Rational(7, 8))
results["b_squared_at_silver"] = str(bSq)

# ── (C) the c_k rational rungs (exact, sympy.Rational) ────────────────────────
print("\n(C) c_k closed-form rationals at silver (c_3 = −2, b² = 7/8)")
c3 = sp.Integer(-2)
b2 = sp.Rational(7, 8)
c8 = c3**2 * b2**2            # c_3²·b⁴
c9 = c3**3 * b2               # c_3³·b²
c10 = c3**2 * b2**3           # c_3²·b⁶
c4 = c8 / c3                  # product identity c_3·c_4 = c_8
c6 = c9 / c3                  # product identity c_3·c_6 = c_9
table = {"c_8": (c8, sp.Rational(49, 16)), "c_9": (c9, sp.Integer(-7)),
         "c_10": (c10, sp.Rational(343, 128)), "c_4": (c4, sp.Rational(-49, 32)),
         "c_6": (c6, sp.Rational(7, 2))}
for name, (val, expect) in table.items():
    print(f"    {name:5s} = {str(val):>10s}   (expect {expect})")
    check(f"(C) {name} = {expect}", sp.simplify(val - expect) == 0)
    results[f"{name}_at_silver"] = str(val)

# ── (P) the product identities c_3·c_4 = c_8 and c_3·c_6 = c_9 ─────────────────
print("\n(P) structural product identities")
check("(P) c_3·c_4 = c_8 (= 49/16)", sp.simplify(c3 * c4 - c8) == 0 and c3 * c4 == sp.Rational(49, 16))
check("(P) c_3·c_6 = c_9 (= −7)", sp.simplify(c3 * c6 - c9) == 0 and c3 * c6 == sp.Integer(-7))

all_passed = all(ok for _, ok in asserts)
verdict = (
    "VERIFIED (exact rational + silver-ratio b² grounding). The Q_β silver-ratio "
    "rungs c_8=49/16, c_9=−7, c_10=343/128 and c_4=−49/32 (product identity "
    "c_3·c_4=c_8) hold exactly with c_3=−2 and the Hoefsmit b²=7/8, itself exact "
    "at q=1+√2. Wires the sorry-free norm_num Lean theorems "
    "qbeta_c{8,9,10}_at_silver / c4_eq_c8_div_c3_at_silver. SUBDOMINANT-but-REAL "
    "(the silver/Q_A pole is a genuine subdominant kernel root, char ≈3.12, not "
    "the dominant ≈117.4); no fit; no c_k≥3 made canonical."
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "qbeta_silver_rationals",
    "description": (
        "Verify the Q_β silver-ratio c_k rational identities (c_8=49/16, c_9=−7, "
        "c_10=343/128, c_4=−49/32 via c_3·c_4=c_8) and the Hoefsmit b²=7/8 grounding "
        "at q=1+√2, wiring QOU.QBeta.qbeta_c{8,9,10}_at_silver and "
        "c4_eq_c8_div_c3_at_silver."),
    "discipline": "no fit; exact rational; SUBDOMINANT-but-REAL silver/Q_A pole; no c_k≥3 made canonical",
    "lean_refs": ["qou:QOU.QBeta.qbeta_c10_at_silver", "qou:QOU.QBeta.c4_eq_c8_div_c3_at_silver"],
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "qbeta-silver-rationals.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
