#!/usr/bin/env python3
"""The deuteron bar-even/bar-odd split is the H₆ partition-conjugation parity — DERIVED and verified
against the canonical characters/weights. Two exact categorical identities pin the parity of the
binding correction; the Δ_λ magnitudes remain the Track-A gate. Forward, exact, no fit.

CONTEXT (owner steer "push from categorical side"): #4369 reduced the deuteron correction C to the
Δ_λ closure. This probe pushes it through the canonical categorical object — the Frobenius-paired
Markov trace tr_M(β_D) = Σ_{λ⊢6} w_λ(q) χ^λ_q(β_D) over the 11 Wedderburn blocks of H₆(q)
(build_markov_trace_assembly_deuteron_chain.py) — and derives the PARITY structure of the correction.

TWO EXACT IDENTITIES (verified to 30 dps against the committed derived caches):
  I1. WEIGHT conjugation-invariance:  w_λ(q) = w_{λ'}(q).
      The Ocneanu/Jones Markov weight is w_λ = (q−q⁻¹)^{n-1} / ∏_{cells}[hook]_q; conjugation λ→λ'
      transposes the Young diagram, which PERMUTES the hook multiset, so ∏[hook]_q — hence w_λ — is
      conjugation-invariant. (Verified for all 11 partitions of 6.)
  I2. CHARACTER conjugation = bar:  χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹).
      Partition conjugation on the character is EXACTLY the bar involution q→q⁻¹ (verified: the ratio
      χ^{λ'}(q₀)/χ^λ(q₀⁻¹) = 1.0000000000 for every λ, from the committed
      chi-deuteron-free-h6-at-q0 / at-qinv 50-dps caches).

CONSEQUENCE — the parity map (grounds ConjugationParitySplit.lean's abstract involution c):
  The per-block term T_λ(q) = w_λ(q)χ^λ(q) satisfies, under bar q→q⁻¹,
      T_λ(q⁻¹) = w_λ(q⁻¹) χ^λ(q⁻¹) = (−1)^{n-1} w_λ(q) · χ^{λ'}(q) = (−1)^{n-1} T_{λ'}(q),
  using I1+I2 and (q−q⁻¹)^{n-1} bar-parity. So bar maps the λ-block to (±) the λ'-block: conjugate
  PAIRS interchange, and the SELF-CONJUGATE block sits on the diagonal. For n=6 the 11 partitions are
  5 conjugate pairs + the single self-conjugate (3,2,1).

THE KEY CATEGORICAL FACT (Lean barOdd_selfConj_zero, verified): the self-conjugate (3,2,1) has a
BAR-EVEN character, χ^{(3,2,1)}(q₀) = χ^{(3,2,1)}(q₀⁻¹) = 7.6256 (ratio 1.0) — so its Wedderburn
contribution is purely bar-even: it feeds the bar-even coefficient g₂ and NEVER the bar-odd impurity t.

SCOPE (honest, scope-(a)): DERIVED — the PARITY structure of the deuteron correction is the H₆
partition-conjugation parity (two exact identities + the self-conjugate→bar-even fact, Lean-proved
backbone). NOT derived — the Δ_λ per-partition MAGNITUDES (the Track-A gate) and the exact
tr_M→binding normalization (a separate convention: β_D word, sign-only crossings; this probe does not
reproduce the 0.3883 tr_M value or C from the parity structure alone). Nothing wired; no fit.

EXPLORATORY — audit + witness only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
PARTS = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
         (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]


def conj(p):
    m = max(p)
    return tuple(sum(1 for x in p if x >= k) for k in range(1, m + 1))


def hooks(p):
    pc = conj(p)
    return [(row - j - 1) + (pc[j] - i - 1) + 1 for i, row in enumerate(p) for j in range(row)]


def main() -> int:
    q0 = mp.mpf('1.1099785827513808075916690956107688798744991218736')

    def qn(n):
        return (q0 ** n - q0 ** (-n)) / (q0 - 1 / q0)

    def w(p):
        den = mp.mpf(1)
        for hh in hooks(p):
            den *= qn(hh)
        return (q0 - 1 / q0) ** (sum(p) - 1) / den

    c0 = {tuple(r['partition']): mp.mpf(r['chi_lambda'])
          for r in json.load(open(_COMP / 'chi-deuteron-free-h6-at-q0-50dps.witness.json'))['by_partition']}
    ci = {tuple(r['partition']): mp.mpf(r['chi_lambda'])
          for r in json.load(open(_COMP / 'chi-deuteron-free-h6-at-qinv-50dps.witness.json'))['by_partition']}

    # I1: weight conjugation-invariance
    i1 = all(abs(w(p) - w(conj(p))) < mp.mpf('1e-30') for p in PARTS)
    # I2: character conjugation = bar
    i2_ratios = [c0[conj(p)] / ci[p] for p in PARTS]
    i2 = all(abs(r - 1) < mp.mpf('1e-30') for r in i2_ratios)

    self_conj = [p for p in PARTS if conj(p) == p]
    pairs = []
    seen = set()
    for p in PARTS:
        if p in seen:
            continue
        c = conj(p)
        seen.add(p)
        if c != p:
            pairs.append((p, c))
            seen.add(c)
    # self-conjugate character bar-parity
    sc = self_conj[0]
    sc_bar_even = abs(c0[sc] - ci[sc]) < mp.mpf('1e-30')

    result = {
        "I1_weight_conjugation_invariance": {
            "w_lambda_eq_w_lambda_prime": bool(i1),
            "reason": "w_λ = (q−q⁻¹)^{n-1}/∏[hook]_q; conjugation transposes the diagram → permutes "
                      "the hook multiset → ∏[hook]_q invariant.",
        },
        "I2_character_conjugation_is_bar": {
            "chi_lambda_prime_q0_over_chi_lambda_qinv": mp.nstr(i2_ratios[0], 12) + " (all = 1)",
            "holds_all_11": bool(i2),
            "identity": "χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹) — partition conjugation IS the bar involution.",
        },
        "parity_map": {
            "T_lambda_bar_image": "T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q)  (from I1+I2 and (q−q⁻¹)^{n-1} parity)",
            "meaning": "bar maps the λ-block to ±the λ'-block: conjugate pairs interchange, "
                       "self-conjugate sits on the diagonal — the concrete realisation of "
                       "ConjugationParitySplit.lean's involution c.",
        },
        "structure_n6": {
            "conjugate_pairs": [[list(a), list(b)] for a, b in pairs],
            "n_pairs": len(pairs),
            "self_conjugate": [list(p) for p in self_conj],
        },
        "key_fact_self_conjugate_bar_even": {
            "partition": list(sc),
            "chi_q0": mp.nstr(c0[sc], 10),
            "chi_qinv": mp.nstr(ci[sc], 10),
            "bar_even_character": bool(sc_bar_even),
            "meaning": "the self-conjugate (3,2,1) has a BAR-EVEN character (χ(q0)=χ(1/q0)); its "
                       "Wedderburn contribution is purely bar-even — it feeds g₂, never the bar-odd t "
                       "(Lean barOdd_selfConj_zero).",
        },
        "scope": {
            "derived": "the PARITY structure of the deuteron correction = H₆ partition-conjugation "
                       "parity (I1 + I2 + self-conjugate→bar-even; Lean backbone).",
            "not_derived": "the Δ_λ per-partition magnitudes (Track-A gate) and the tr_M→binding "
                           "normalization (β_D word / sign convention); the parity structure alone "
                           "does not reproduce tr_M=0.3883 or C.",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "deuteron-conjugation-parity-categorical",
        "description": ("The deuteron bar-even/bar-odd split is the H₆ partition-conjugation parity, "
                        "derived and verified against the canonical derived caches. Two exact "
                        "identities (30 dps): I1 weight conjugation-invariance w_λ=w_{λ'} (hook "
                        "multiset preserved under transpose); I2 character conjugation = bar "
                        "χ^{λ'}(β_D;q)=χ^λ(β_D;q⁻¹) (ratio 1.0 for all 11 partitions). Consequence: the "
                        "per-block term obeys T_λ(q⁻¹)=(−1)^{n-1}T_{λ'}(q), so bar interchanges "
                        "conjugate pairs and fixes the self-conjugate — 5 pairs + (3,2,1) for n=6. Key "
                        "fact: (3,2,1) has a bar-even character (χ(q0)=χ(1/q0)=7.6256), so it feeds g₂ "
                        "and never the bar-odd t (Lean barOdd_selfConj_zero). DERIVED: the parity "
                        "structure; NOT derived: the Δ_λ magnitudes (Track-A gate) or the tr_M→binding "
                        "normalization. scope-(a), audit-only, nothing wired; no fit."),
        "audit_only": True,
        "tier": "two exact categorical identities (30 dps, derived caches) + parity map + "
                "self-conjugate→bar-even; Lean-proved backbone; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, categorical parity of the deuteron correction",
            "lean": "QOU/MassTheory/ConjugationParitySplit.lean",
            "caches": "chi-deuteron-free-h6-at-{q0,qinv}-50dps.witness.json; schur-weyl-weight-*.json",
            "builds_on": "#4369 (frame-independent C = Δ_λ closure), "
                         "build_markov_trace_assembly_deuteron_chain.py (tr_M=Σ w_λ χ^λ)",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "deuteron-conjugation-parity-categorical", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("weight_conj_invariance", computed=str(bool(i1)), expected="True")
    wb.add_assertion("character_conj_is_bar", computed=str(bool(i2)), expected="True")
    wb.add_assertion("self_conjugate_3_2_1_bar_even", computed=str(bool(sc_bar_even)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Deuteron bar-parity = H₆ partition-conjugation parity (categorical) ===")
    print(f"I1  w_λ = w_{{λ'}} (hook conjugation-invariance): {i1}")
    print(f"I2  χ^{{λ'}}(β_D;q) = χ^λ(β_D;q⁻¹) (conjugation = bar), all 11: {i2}")
    print(f"    parity map: T_λ(q⁻¹) = (−1)^(n-1) T_{{λ'}}(q) ⇒ bar interchanges conjugate pairs")
    print(f"    n=6 structure: {len(pairs)} conjugate pairs + self-conjugate {[list(p) for p in self_conj]}")
    print(f"KEY  self-conjugate (3,2,1): χ(q0)={mp.nstr(c0[sc],8)} = χ(1/q0)={mp.nstr(ci[sc],8)} "
          f"(bar-even: {sc_bar_even}) ⇒ feeds g₂, never t (Lean barOdd_selfConj_zero)")
    print("SCOPE: DERIVED the parity structure (categorical, verified); the Δ_λ magnitudes + "
          "tr_M→binding normalization remain the Track-A gate. scope-(a), no fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
