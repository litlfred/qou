#!/usr/bin/env python3
"""The deuteron bar-even/bar-odd split is the SIGNED H₆ partition-conjugation parity — derived and
verified against the canonical characters/weights. CORRECTS an earlier draft that dropped the weight's
(−1)^{n-1} bar-sign and therefore assigned the self-conjugate (3,2,1) to the WRONG channel.

CONTEXT (owner steer "push from categorical side"): #4369 reduced the deuteron correction C to the
Δ_λ closure. This probe pushes it through the canonical categorical object — the Frobenius-paired
Markov trace tr_M(β_D) = Σ_{λ⊢6} w_λ(q) χ^λ_q(β_D) over the 11 Wedderburn blocks of H₆(q) — and derives
the PARITY structure of the correction.

THREE EXACT FACTS (verified to 25 dps against the committed derived caches):
  I1. WEIGHT conjugation-invariance:  w_λ(q) = w_{λ'}(q)  (transpose permutes the hook multiset).
  I2. CHARACTER conjugation = bar:  χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹)  (ratio 1.0 for all 11 partitions).
  I3. WEIGHT bar-sign:  w_λ(q⁻¹) = (−1)^{n-1} w_λ(q)  (from the (q−q⁻¹)^{n-1} prefactor). For n=6 the
      sign is (−1)^5 = −1.

THE SIGNED PARITY MAP (grounds ConjugationParitySplit.lean). The per-block term T_λ = w_λ χ^λ obeys
    T_λ(q⁻¹) = w_λ(q⁻¹) χ^λ(q⁻¹) = (−1)^{n-1} w_λ(q) · χ^{λ'}(q) = (−1)^{n-1} T_{λ'}(q).
Verified numerically: T_λ(q₀⁻¹) = −T_{λ'}(q₀) for all 11 (n=6 ⇒ sign −1).

CORRECTED KEY FACT (the earlier draft had this BACKWARDS): under the PHYSICAL bar the self-conjugate
(3,2,1) is BAR-ODD, T_{(3,2,1)}(q₀⁻¹) = −T_{(3,2,1)}(q₀) (ratio −1) — because for n=6 the sign is −1
and (3,2,1)=(3,2,1)'. So the self-conjugate feeds the bar-ODD impurity t and NEVER the bar-even
coefficient g₂. Consequently:
  • the BAR-EVEN g₂ is carried ENTIRELY by the conjugate-pair ASYMMETRIES (Δ_λ − Δ_{λ'}, which vanish
    on the self-conjugate);
  • the BAR-ODD t is carried by the conjugate-pair SYMMETRIC parts PLUS the whole self-conjugate.
(The sign is load-bearing: for a hypothetical odd-n atom, sign=+1, the roles would swap.)

SCOPE (honest, scope-(a)): DERIVED — the PARITY structure of the deuteron correction is the SIGNED H₆
partition-conjugation parity (I1+I2+I3, the parity map, and the corrected self-conjugate→t fact; Lean
backbone ConjugationParitySplit.lean sorry-free). NOT derived — the Δ_λ per-partition MAGNITUDES
(Track-A gate) and the tr_M→binding normalization (β_D word / sign convention); the parity structure
alone does not reproduce a binding number. Nothing wired; no fit.

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
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
PARTS = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
         (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]


def conj(p):
    m = max(p)
    return tuple(sum(1 for x in p if x >= k) for k in range(1, m + 1))


def hooks(p):
    pc = conj(p)
    return [(row - j - 1) + (pc[j] - i - 1) + 1 for i, row in enumerate(p) for j in range(row)]


def main() -> int:
    # Source q₀ from the SAME pinning the character caches were computed at (its `q_str`), so q₀ and
    # χ^λ(q₀) can never drift apart — the identities below (I2: χ^{λ'}(q)=χ^λ(q⁻¹)) hold only when q₀
    # matches the cache exactly. (NOT qou_substrate.q_at / Q_50_DIGIT_STR: those are a different pin —
    # ~11.7 ppb muon↔proton — and would break consistency with these caches.)
    _q0cache = json.load(open(_COMP / 'chi-deuteron-free-h6-at-q0-50dps.witness.json'))
    q0 = mp.mpf(_q0cache['q_str'])
    qi = 1 / q0

    def qn(x, n):
        return (x ** n - x ** (-n)) / (x - 1 / x)

    def w(x, p):
        den = mp.mpf(1)
        for hh in hooks(p):
            den *= qn(x, hh)
        return (x - 1 / x) ** (sum(p) - 1) / den

    c0 = {tuple(r['partition']): mp.mpf(r['chi_lambda']) for r in _q0cache['by_partition']}
    ci = {tuple(r['partition']): mp.mpf(r['chi_lambda'])
          for r in json.load(open(_COMP / 'chi-deuteron-free-h6-at-qinv-50dps.witness.json'))['by_partition']}

    tol = mp.mpf('1e-25')
    i1 = all(abs(w(q0, p) - w(q0, conj(p))) < tol for p in PARTS)                     # weight conj-inv
    i2 = all(abs(c0[conj(p)] - ci[p]) < tol for p in PARTS)                           # char conj = bar
    i3 = all(abs(w(qi, p) - (-1) ** (sum(p) - 1) * w(q0, p)) < tol for p in PARTS)    # weight bar-sign

    T0 = {p: w(q0, p) * c0[p] for p in PARTS}
    Ti = {p: w(qi, p) * ci[p] for p in PARTS}
    # signed parity map: T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q); n=6 ⇒ = −T_{λ'}(q)
    parity_map = all(abs(Ti[p] + T0[conj(p)]) < tol for p in PARTS)

    sc = (3, 2, 1)
    sc_ratio = Ti[sc] / T0[sc]                      # = −1 ⇒ bar-ODD ⇒ feeds t
    sc_bar_odd = abs(sc_ratio + 1) < mp.mpf('1e-6')

    pairs, seen = [], set()
    for p in PARTS:
        if p in seen:
            continue
        seen.add(p)
        c = conj(p)
        if c != p:
            pairs.append((p, c))
            seen.add(c)

    result = {
        "I1_weight_conjugation_invariance": {"w_lambda_eq_w_lambda_prime": bool(i1)},
        "I2_character_conjugation_is_bar": {"chi_lambda_prime_q_eq_chi_lambda_qinv": bool(i2)},
        "I3_weight_bar_sign": {
            "w_lambda_qinv_eq_minus1_pow_n_minus_1": bool(i3),
            "sign_for_n6": "(−1)^5 = −1",
        },
        "signed_parity_map": {
            "T_lambda_qinv_eq_signed_T_lambda_prime": bool(parity_map),
            "identity": "T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q); for n=6, = −T_{λ'}(q). Verified all 11.",
            "grounds_lean": "ConjugationParitySplit.lean barImage sgn=(−1)^{n-1}",
        },
        "CORRECTED_self_conjugate_is_bar_odd": {
            "partition": list(sc),
            "T_q0": mp.nstr(T0[sc], 8),
            "T_qinv": mp.nstr(Ti[sc], 8),
            "ratio": mp.nstr(sc_ratio, 6),
            "bar_odd": bool(sc_bar_odd),
            "correction_note": "EARLIER DRAFT WAS BACKWARDS. With the weight's (−1)^{n-1} sign, the "
                               "self-conjugate (3,2,1) is BAR-ODD (ratio −1) ⇒ it feeds the bar-odd "
                               "impurity t, NEVER the bar-even g₂ (Lean selfConj_barEven_zero_deuteron).",
        },
        "channel_assignment": {
            "bar_even_g2": "conjugate-pair ASYMMETRIES Δ_λ − Δ_{λ'} (vanish on the self-conjugate)",
            "bar_odd_t": "conjugate-pair SYMMETRIC parts + the whole self-conjugate (3,2,1)",
            "n6_structure": {"conjugate_pairs": len(pairs), "self_conjugate": [list(sc)]},
        },
        "scope": {
            "derived": "the SIGNED parity structure of the deuteron correction = H₆ partition-"
                       "conjugation parity with the weight's (−1)^{n-1} sign (Lean backbone).",
            "not_derived": "the Δ_λ magnitudes (Track-A gate) + tr_M→binding normalization.",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "deuteron-conjugation-parity-categorical",
        "description": ("The deuteron bar-even/bar-odd split is the SIGNED H₆ partition-conjugation "
                        "parity, verified against the derived caches (25 dps). CORRECTS an earlier "
                        "draft that dropped the weight bar-sign. Three facts: I1 w_λ=w_{λ'}; I2 "
                        "χ^{λ'}(q)=χ^λ(q⁻¹); I3 w_λ(q⁻¹)=(−1)^{n-1}w_λ(q) (=−1 for n=6). Parity map "
                        "T_λ(q⁻¹)=(−1)^{n-1}T_{λ'}(q)=−T_{λ'}(q) (all 11). CORRECTED key fact: the "
                        "self-conjugate (3,2,1) is BAR-ODD (T(q⁻¹)=−T(q), ratio −1) ⇒ feeds the bar-odd "
                        "impurity t, NEVER g₂ (opposite of the earlier draft). So the bar-even g₂ is "
                        "carried by conjugate-pair ASYMMETRIES Δ_λ−Δ_{λ'}, and the bar-odd t by the "
                        "symmetric parts + the self-conjugate. DERIVED: the signed parity structure "
                        "(Lean ConjugationParitySplit sorry-free). NOT derived: the Δ_λ magnitudes "
                        "(Track-A gate) + tr_M→binding normalization. scope-(a), audit-only, nothing "
                        "wired; no fit."),
        "audit_only": True,
        "tier": "three exact identities + signed parity map + CORRECTED self-conjugate→t; Lean-proved "
                "backbone; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, categorical parity of the deuteron correction",
            "lean": "QOU/MassTheory/ConjugationParitySplit.lean (selfConj_barEven_zero_deuteron)",
            "caches": "chi-deuteron-free-h6-at-{q0,qinv}-50dps.witness.json",
            "correction": "supersedes the earlier sign-dropped draft (self-conjugate channel reversed)",
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
    wb.add_assertion("weight_bar_sign", computed=str(bool(i3)), expected="True")
    wb.add_assertion("signed_parity_map", computed=str(bool(parity_map)), expected="True")
    wb.add_assertion("self_conjugate_3_2_1_bar_ODD", computed=str(bool(sc_bar_odd)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Deuteron bar-parity = SIGNED H₆ partition-conjugation parity (categorical, CORRECTED) ===")
    print(f"I1 w_λ=w_{{λ'}}: {i1}   I2 χ^{{λ'}}(q)=χ^λ(q⁻¹): {i2}   I3 w_λ(q⁻¹)=(−1)^{{n-1}}w_λ(q): {i3}")
    print(f"signed parity map T_λ(q⁻¹)=(−1)^(n-1)T_{{λ'}}(q)=−T_{{λ'}}(q) (n=6), all 11: {parity_map}")
    print(f"CORRECTED: self-conjugate (3,2,1) ratio T(1/q0)/T(q0) = {mp.nstr(sc_ratio,4)} ⇒ BAR-ODD: "
          f"{sc_bar_odd} ⇒ feeds t, NEVER g₂ (earlier draft had this backwards)")
    print(f"channel: bar-even g₂ = conjugate-pair asymmetries Δ_λ−Δ_{{λ'}}; bar-odd t = symmetric parts "
          f"+ self-conjugate (3,2,1)")
    print("SCOPE: DERIVED the signed parity structure; Δ_λ magnitudes + tr_M→binding remain the "
          "Track-A gate. scope-(a), no fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
