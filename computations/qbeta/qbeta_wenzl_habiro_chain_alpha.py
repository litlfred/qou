#!/usr/bin/env python3
"""qbeta_wenzl_habiro_chain_alpha.py — Family α first-test at u_substrate.

Chain 1 of the user-approved Q_β Habiro element search (2026-06-03, PR #1760).
Family α premise (per scope doc 2026-06-03):

    F_α(u) = Π_k (1 + tr_M(p_k) · u^k)

where `p_k` is a Wenzl-class projector in H_n(q). If the residue-A
categorical identification at u_substrate is a literal Wenzl-projector
Markov trace, then `tr_M(p_2) = c_2 = -1` and `tr_M(p_3) = c_3 ≈ -2.069`.

This is a FIRST-TEST: compute `tr_M(p_k)` for k=2..4 in FOUR standard
projector conventions and compare to (c_2, c_3, c_4) targets. The Δ_λ
gate is respected (closed-form formulas, no fits).

Projector conventions tested:
  1. **JW (Jones-Wenzl)**: tr_M(p_n^{JW}) = (-1)^{n-1} / [n]_q
  2. **Symmetric (Schur-Weyl)**: tr_M(s_n) via q-dim of symmetric rep
  3. **Antisymmetric**: tr_M(a_n) via q-dim of anti-symmetric rep
  4. **Adjoint-like**: tr_M(adj_n) via q-dim of adjoint at level n

Note (informed by c_2 Lean proof): c_2 = -1 comes from Kashiwara f̃₁²
(crystal operator eigenvalue), NOT a Markov trace of a projector. If
none of the 4 conventions reproduces (-1, -2.069), the Family α
literal-Wenzl-Markov-trace formulation is refuted; the residue A must
involve a Kashiwara crystal operator (Family β-adjacent) or a different
categorical object.

Verdict: this is a STRUCTURAL TEST — NEGATIVE is informative (sharpens
the search), POSITIVE would close a 4-day open question.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# Path bridge (subdirectory refactor, Phase 5).
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


REASON_TEXT = "target below the 1e-30 precision floor — relative error undefined"


def quantum_int(n: int, q: mpf) -> mpf:
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def quantum_factorial(n: int, q: mpf) -> mpf:
    result = mpf(1)
    for k in range(1, n + 1):
        result = result * quantum_int(k, q)
    return result


def tr_M_jones_wenzl(n: int, q: mpf) -> mpf:
    """Markov trace of the Jones-Wenzl idempotent at strand-count n.

    Standard formula (Kauffman normalization):
      tr_M(p_n^{JW}) = (-1)^(n-1) · [n]_q⁻¹

    The (-1)^(n-1) sign is from the alternating Markov-trace closure.
    """
    sign = mpf(-1) ** (n - 1)
    return sign / quantum_int(n, q)


def tr_M_symmetric(n: int, q: mpf) -> mpf:
    """Markov trace of the symmetric Schur-Weyl idempotent.

    Markov-normalized q-dimension of the symmetric rep S^{(n)}:
      tr_M(s_n) = q^{n(n-1)/2} / [n]_q!

    Reference: Wenzl 1988 §2 (representation dimension); Jones 1985
    eq. 4.3 (Markov-trace normalization).
    """
    return q ** (n * (n - 1) // 2) / quantum_factorial(n, q)


def tr_M_antisymmetric(n: int, q: mpf) -> mpf:
    """Markov trace of the antisymmetric Schur-Weyl idempotent.

    q-dim of anti-symmetric rep at level n: q^{-n(n-1)/2} / [n]_q!
    """
    return q ** (-(n * (n - 1) // 2)) / quantum_factorial(n, q)


def tr_M_adjoint_like(n: int, q: mpf) -> mpf:
    """Markov trace of the adjoint-like rep (formal q-character variant).

    [n]_q - [n]_q^(-1) — a self-conjugate combination that can be negative.
    """
    qn = quantum_int(n, q)
    return qn - 1 / qn


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-wenzl-habiro-chain-alpha", engine="mpmath")

    q = Q_MP

    # Targets: (c_2, c_3, c_4...) from cache
    targets = {
        2: mpf("-1"),  # Lean-proved (Kashiwara f̃₁²)
        3: mpf("-2.06934257711516783787971951725"),  # cal-anchored
        4: mpf("0"),  # below numerical floor at this anchor
    }

    print("=" * 76)
    print(" Family α first-test — Wenzl-projector Markov traces vs (c_2, c_3, c_4)")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q, 14)}")
    print(f"  Targets:")
    print(f"    c_2 = {mp.nstr(targets[2], 14):>20}  (Lean-proved, Kashiwara f̃₁²)")
    print(f"    c_3 = {mp.nstr(targets[3], 14):>20}  (cal-anchored)")
    print(f"    c_4 = {mp.nstr(targets[4], 14):>20}  (below numerical floor)")
    print()

    conventions = {
        "JW (Jones-Wenzl)": tr_M_jones_wenzl,
        "Symmetric (Schur-Weyl)": tr_M_symmetric,
        "Antisymmetric": tr_M_antisymmetric,
        "Adjoint-like [n]_q − [n]_q⁻¹": tr_M_adjoint_like,
    }

    results = {}
    tolerance_ppm = 10.0  # 10 ppm = 1e-5 relative
    any_pass = False

    for name, formula in conventions.items():
        print("─" * 76)
        print(f"  Convention: {name}")
        print("─" * 76)
        row = {"convention": name, "k_results": {}}
        max_err_ppm = 0.0
        passed_all = True
        for k in [2, 3, 4]:
            value = formula(k, q)
            target = targets[k]
            if abs(target) < mpf("1e-30"):
                # A RELATIVE error against a target of zero is undefined, which
                # the code already knew — hence ok_str "n/a". It recorded that
                # as float("nan"), which json.dump writes as a bare NaN token;
                # JSON has none, so this witness did not parse under a strict
                # loader. null, not an "nan" marker: undefined-by-construction
                # is a MISSING value, not a pole.
                err_ppm = None
                ok = True  # target is below precision floor — any value OK
                ok_str = "n/a"
            else:
                err_ppm = float(abs(value - target) / abs(target) * 1e6)
                ok = err_ppm <= tolerance_ppm
                ok_str = "PASS" if ok else "FAIL"
                if not ok:
                    passed_all = False
                if err_ppm > max_err_ppm:
                    max_err_ppm = err_ppm
            print(f"    k={k}: tr_M(p_k) = {mp.nstr(value, 14):>20}  "
                  f"target = {mp.nstr(target, 14):>14}  "
                  f"err = {'         n/a' if err_ppm is None else f'{err_ppm:>12.2f}'} ppm  {ok_str}")
            row["k_results"][str(k)] = {
                "computed": mp.nstr(value, 30),
                "target": mp.nstr(target, 30),
                "err_ppm": err_ppm,
                "err_ppm_undefined_reason": (None if err_ppm is not None
                                             else "%s" % REASON_TEXT),
                "passed": ok,
            }
        row["all_passed"] = passed_all
        row["max_err_ppm"] = max_err_ppm
        if passed_all:
            any_pass = True
            print(f"    → ALL PASS (max err {max_err_ppm:.2f} ppm) — candidate Habiro element!")
        else:
            print(f"    → FAIL (max err {max_err_ppm:.2f} ppm)")
        print()
        results[name] = row

    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    if any_pass:
        print("  POSITIVE — one or more Wenzl-projector conventions matches (c_2, c_3)")
        print("  within 10 ppm. This is a Family α residue-A categorical-ID candidate.")
    else:
        print("  NEGATIVE — no literal Wenzl-projector Markov trace reproduces")
        print("  (c_2, c_3) = (-1, -2.069). Consistent with the Lean proof of c_2 = -1")
        print("  coming from Kashiwara f̃₁² (crystal operator), NOT a Markov trace.")
        print()
        print("  Implication: residue A categorical-ID likely lives in the Kashiwara")
        print("  crystal layer (Family β-adjacent / Option-E intended path), not in")
        print("  the literal Wenzl-projector Markov trace. Family α as written above")
        print("  is REFUTED; the search narrows to formulas involving crystal operators.")

    # Assertions
    wb.add_assertion(
        "family_alpha_literal_wenzl_markov_trace_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,  # expected NEGATIVE based on c_2 = Kashiwara crystal eigenvalue
        source="If c_2 = -1 came from a Wenzl-projector Markov trace, this would PASS; "
               "the Lean proof says c_2 = -1 comes from Kashiwara f̃₁² (crystal), so we "
               "expect this to FAIL — confirming the residue A categorical-ID is NOT a "
               "literal Wenzl trace.",
    )

    wb.add_data("targets", {str(k): mp.nstr(v, 30) for k, v in targets.items()})
    wb.add_data("conventions_tested", list(conventions.keys()))
    wb.add_data("per_convention_results", results)
    wb.add_data("any_convention_passes_10_ppm", any_pass)
    wb.add_data("interpretation", (
        "Family α first-test: 4 literal Wenzl-projector Markov trace conventions tested "
        "at proton-pinned q₀ against (c_2, c_3) = (-1, -2.069). "
        + ("POSITIVE — at least one convention matches, candidate residue-A categorical-ID."
           if any_pass else
           "NEGATIVE — no literal Wenzl trace matches, consistent with c_2 = Kashiwara f̃₁² "
           "categorical origin. Search narrows to crystal-operator formulas (Family β-adjacent).")
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
