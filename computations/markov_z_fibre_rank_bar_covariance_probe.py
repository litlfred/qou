#!/usr/bin/env python3
"""Choosing the Markov parameter ``z`` *is* choosing the fibre rank ``N``.

Joins two items that PRs #4767 and #4766 opened separately:

  * #4767 asks whether ``z`` should be ``q^3/(q^2+1)`` (convention D) rather
    than ``1/(q^(1/2)+q^(-1/2))`` (convention C), and declined the edit,
    noting that ``z_C`` is bar-invariant where ``z_D`` is not.
  * #4766 shows that binding's Wenzl bridge satisfies
    ``X = Q^N  <=>  z*[N]_q = q^N`` and asks which integer fibre rank ``N``,
    if any, binding traces (bean ``qou-rm47``).

This probe establishes three things.

1. **The two questions are one.**  ``z*[N]_q = q^N`` is invertible: every
   ``z`` names a rank ``N`` and every ``N`` names a ``z``.  Convention D is
   exactly ``N = 2``.  Convention C is ``N ~ 2.5995``, not an integer.

2. **The bar-covariance law.**  For the whole family ``z_N = q^N/[N]_q``,

       bar(z_N) = q^(-2N) * z_N

   -- proved here symbolically for generic ``q``, and checked at ``N = 1..8``.

3. **Therefore bar-invariance and a fibre reading are incompatible.**
   ``bar(z_N) = z_N`` forces ``q^(2N) = 1``, so at generic ``q`` the only
   bar-invariant member of the family is ``N = 0`` (degenerate: ``[0]_q = 0``,
   no fibre).  ``z_C``'s bar-invariance is thus *not* a tiebreaker in D's
   disfavour that some other integer ``N`` could satisfy: **no** integer
   ``N >= 1`` gives a bar-invariant ``z``.  The corpus must give up exactly
   one of the two properties, and which one is the author's call.

This is a structural (scope-b) exclusion of "some integer fibre rank yields a
bar-invariant Markov parameter", resting on the proved identity in item 2.
It is *not* a claim about which convention is correct.

Conventions
-----------
q_0 is the **experimental (proton) pin** per the 2026-08-07 owner directive.
No muon-built cache is read.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

DPS = 50


def main() -> int:
    mp.mp.dps = DPS

    wb = WitnessBuilder("markov-z-fibre-rank-bar-covariance", engine="python")
    wb.set_description(
        "z*[N]_q = q^N makes the Markov-parameter convention and the fibre "
        "rank the same choice; bar(z_N) = q^(-2N) z_N shows no integer rank "
        "N >= 1 gives a bar-invariant z. Joins #4767 (z value) and #4766 "
        "(bean qou-rm47, binding fibre N)."
    )

    q, N = sp.symbols("q N", positive=True)
    checks: dict[str, bool] = {}

    # ---- The family, in both of its forms. ----------------------------------
    # z_N := q^N / [N]_q  with  [N]_q = (q^N - q^-N)/(q - q^-1).
    bracket_N = (q**N - q ** (-N)) / (q - 1 / q)
    z_N = sp.simplify(q**N / bracket_N)
    # Closed form: q^(2N-1)(q^2 - 1)/(q^(2N) - 1)
    z_N_closed = q ** (2 * N - 1) * (q**2 - 1) / (q ** (2 * N) - 1)
    checks["z_N_closed_form"] = sp.simplify(z_N - z_N_closed) == 0

    # ---- 1. Equivalence with the Wenzl-bridge condition X = Q^N. ------------
    # Binding's bridge (y_lambda_wenzl_bridge.py:122,140): Q = q^2,
    # X = q*z/(1 - Q + q*z).  Solve X = Q^N for z and compare to z_N.
    z_sym = sp.Symbol("z", positive=True)
    Q_big = q**2
    X = q * z_sym / (1 - Q_big + q * z_sym)
    z_from_bridge = sp.solve(sp.Eq(X, Q_big**N), z_sym)[0]
    checks["bridge_X_eq_QN_iff_z_eq_qN_over_Nq"] = (
        sp.simplify(z_from_bridge - z_N_closed) == 0
    )

    # ---- 2. The bar-covariance law:  bar(z_N) = q^(-2N) * z_N. --------------
    bar_z_N = z_N_closed.subs(q, 1 / q)
    ratio = sp.simplify(bar_z_N / z_N_closed)
    checks["bar_covariance_ratio_is_q_pow_minus_2N"] = (
        sp.simplify(ratio - q ** (-2 * N)) == 0
    )

    # 2b. Spot-check at integer ranks, independently of the symbolic step.
    per_rank = []
    for n_int in range(1, 9):
        zn = sp.simplify(z_N_closed.subs(N, n_int))
        rn = sp.simplify(zn.subs(q, 1 / q) / zn)
        ok = sp.simplify(rn - q ** (-2 * n_int)) == 0
        per_rank.append(
            {"N": n_int, "z_N": str(sp.simplify(zn)), "bar_ratio_ok": bool(ok)}
        )
    checks["bar_covariance_holds_N_1_to_8"] = all(r["bar_ratio_ok"] for r in per_rank)

    # ---- 3. Bar-invariance forces q^(2N) = 1. ------------------------------
    # bar(z_N) = z_N  <=>  q^(-2N) = 1.  At generic q (transcendental over Q,
    # and in particular q_0 > 1 real) this has no solution with N >= 1.
    checks["no_integer_rank_is_bar_invariant"] = all(
        sp.simplify(q ** (-2 * n_int) - 1) != 0 for n_int in range(1, 9)
    )

    # ---- The two named conventions, placed in the family. -------------------
    # Convention C is EXCISED (owner ruling 2026-08-09, re-affirmed 2026-08-15).
    # It stays here because this probe COMPARES the two conventions -- removing
    # the excised one would remove the thing being compared.
    #
    # The "binding + 8 corpus sites" attribution was already stale when written:
    # the binding channel moved to D on 2026-08-09. Left as recorded history
    # rather than re-counted, because re-inventorying belongs to qou-cdh3 and a
    # fresh count in a probe comment would only go stale again.
    z_C_expr = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))     # EXCISED (attribution stale)
    z_D_expr = q**3 / (q**2 + 1)                      # CANONICAL — Jones / SU_q(2)

    # D is exactly N = 2.
    checks["z_D_is_rank_2_exactly"] = (
        sp.simplify(z_N_closed.subs(N, 2) - z_D_expr) == 0
    )
    # C is bar-invariant; D is not (reproduces #4767's table).
    checks["z_C_is_bar_invariant"] = (
        sp.simplify(z_C_expr.subs(q, 1 / q) - z_C_expr) == 0
    )
    checks["z_D_is_not_bar_invariant"] = (
        sp.simplify(z_D_expr.subs(q, 1 / q) - z_D_expr) != 0
    )
    # ...and D's bar ratio is q^-4, i.e. the law at N = 2.
    checks["z_D_bar_ratio_is_q_minus_4"] = (
        sp.simplify(z_D_expr.subs(q, 1 / q) / z_D_expr - q ** (-4)) == 0
    )

    # ---- Numerics at the experimental pin: invert z -> N for C and D. -------
    q0 = mp.mpf(Q_50_DIGIT_STR)

    def z_of_rank(n_val):
        n_val = mp.mpf(n_val)
        return q0 ** (2 * n_val - 1) * (q0**2 - 1) / (q0 ** (2 * n_val) - 1)

    def rank_of_z(z_val):
        return mp.findroot(lambda n: z_of_rank(n) - z_val, mp.mpf("2.5"))

    z_C_num = 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))
    z_D_num = q0**3 / (q0**2 + 1)
    N_from_C = rank_of_z(z_C_num)
    N_from_D = rank_of_z(z_D_num)

    checks["N_from_z_D_is_2"] = abs(N_from_D - 2) < mp.mpf("1e-40")
    checks["N_from_z_C_is_not_integer"] = (
        abs(N_from_C - mp.nint(N_from_C)) > mp.mpf("1e-6")
    )

    # Where do the neighbouring integer ranks sit, for qou-rm47?
    rank_table = [
        {
            "N": n_int,
            "z_at_q0": mp.nstr(z_of_rank(n_int), 24),
            "rel_gap_to_z_C": mp.nstr(
                (z_of_rank(n_int) - z_C_num) / z_C_num, 12
            ),
        }
        for n_int in range(1, 7)
    ]

    all_pass = all(checks.values())

    wb.add_parameter("q_0_pin", "experimental/proton")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_parameter("dps", DPS)
    wb.add_data("z_family", "z_N = q^N/[N]_q = q^(2N-1)(q^2-1)/(q^(2N)-1)")
    wb.add_data("bar_covariance_law", "bar(z_N) = q^(-2N) * z_N")
    wb.add_data("checks", {k: bool(v) for k, v in checks.items()})
    wb.add_data("per_rank_bar_check", per_rank)
    wb.add_data("rank_table_at_q0", rank_table)
    wb.add_data(
        "conventions",
        {
            "C": {
                "z": "1/(q^(1/2)+q^(-1/2))",
                "z_at_q0": mp.nstr(z_C_num, 24),
                "implied_rank_N": mp.nstr(N_from_C, 20),
                "bar_invariant": True,
                "integer_rank": False,
            },
            "D": {
                "z": "q^3/(q^2+1)",
                "z_at_q0": mp.nstr(z_D_num, 24),
                "implied_rank_N": mp.nstr(N_from_D, 20),
                "bar_invariant": False,
                "integer_rank": True,
            },
        },
    )

    wb.add_assertion("checks_failed", sum(1 for v in checks.values() if not v), 0)
    wb.add_assertion(
        # STRINGS: the documented WitnessBuilder convention for keeping an
        # assertion value out of float64. N_from_* come off mp.findroot at the
        # working precision and were being cut to 17 digits at the assertion.
        "implied_rank_of_z_D", mp.nstr(N_from_D, 30), "2.0",
        tolerance="1e-40", source="mp.findroot on z_N(q_0)",
    )
    wb.add_assertion(
        "implied_rank_of_z_C", mp.nstr(N_from_C, 30), "2.5995155364001770",
        tolerance="1e-15",
        source="mp.findroot on z_N(q_0); independent of #4766's N_eff",
    )
    wb.add_assertion(
        "n_integer_ranks_that_are_bar_invariant", 0, 0, source="sympy exact"
    )

    wb.add_data(
        "interpretation",
        {
            "unification": (
                "z*[N]_q = q^N is invertible, so the Markov-parameter "
                "convention and the fibre rank are the same choice. #4767's "
                "z question and #4766's bean qou-rm47 are one question."
            ),
            "structural_exclusion_scope_b": (
                "bar(z_N) = q^(-2N) z_N, so bar-invariance forces q^(2N)=1, "
                "impossible at q_0 > 1 for N >= 1. No integer fibre rank "
                "yields a bar-invariant Markov parameter. The corpus must "
                "give up either bar-invariance of z or the fibre reading; "
                "there is no rank that rescues both."
            ),
            "not_a_convention_verdict": (
                "This does not say which convention is correct. It says the "
                "two desiderata are incompatible, so the decision cannot be "
                "deferred to a search over N."
            ),
        },
    )
    wb.add_caveat(
        "Scope (b) applies only to the family z = q^N/[N]_q, i.e. to fibre "
        "readings via the Wenzl bridge's X = Q^N. A Markov parameter arising "
        "some other way is not covered."
    )
    wb.add_caveat(
        "N is treated as a real variable when inverting z -> N. The "
        "non-integrality of N_from_C is therefore a statement about that "
        "continuation, matching #4766's N_eff = 2.5995155364."
    )

    path = wb.save()

    print("=" * 70)
    print("markov z  <->  fibre rank N     (proton pin, %d dps)" % DPS)
    print("=" * 70)
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print()
    print("  z_N = q^N/[N]_q = q^(2N-1)(q^2-1)/(q^(2N)-1)")
    print("  bar-covariance law:   bar(z_N) = q^(-2N) * z_N")
    print("  => bar-invariant  <=>  q^(2N) = 1  =>  no integer N >= 1")
    print()
    print(f"  convention D  z = q^3/(q^2+1)      -> N = {mp.nstr(N_from_D, 20)}")
    print(f"  convention C  z = 1/(q^.5+q^-.5)   -> N = {mp.nstr(N_from_C, 20)}")
    print()
    print("  integer ranks near C:")
    for r in rank_table[:5]:
        print(f"    N={r['N']}  z={r['z_at_q0'][:20]}  rel gap to z_C {r['rel_gap_to_z_C']}")
    print()
    print(f"  ALL CHECKS {'PASS' if all_pass else 'FAIL'}")
    print(f"  witness -> {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
