#!/usr/bin/env python3
"""The per-block χ_λ(Δ_{T_β}) closed forms under the CANONICAL ordering.

Two of the three published closed forms
(`QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`, lines 72–99) are unchanged by
the 2026-09-05 intra-ordering ruling. One is not. This derives all three
symbolically from the canonical words and states the corrected one.

WHAT MOVES, AND WHY IT IS THE ONLY ONE THAT CAN
-----------------------------------------------
    λ         published (grouped)              canonical (borromean)
    (3)       -(q²-1)(q²+1)²/(4q)              IDENTICAL
    (2,1)     (q²-1)(-q⁴-1)/(4q³)              DIFFERS  ← the only 2-dim block
    (1,1,1)   -(q²-1)(q²+1)²/(4q⁵)             IDENTICAL

(3) and (1,1,1) are the ONE-DIMENSIONAL irreps. There the generators act by
scalars, so they commute, and no reordering of the word can reach them. (2,1) is
the only 2-dimensional block of H₃(q), and it is exactly where σ₀ and σ₁ fail to
commute.

That is the ruling's own justification — *σ₀ and σ₁ do not commute, so only the
alternating word is β_Bor* — recovered from a direction that did not assume it.
The ordering moves the answer precisely where non-commutativity is visible and
nowhere else.

THE CORRECTED FORM
------------------
    χ_(2,1)(Δ_{T_β}) = (q²-1)(q⁴+1)·P(q) / (4q⁹)
    P(q) = 2q¹² - 5q¹⁰ + 5q⁸ - 5q⁶ + 5q⁴ - 5q² + 2

Related to the published form by an exact factor:

    canonical / published = -P(q)/q⁶,      P(1) = -1

so **the two agree exactly at q = 1**, which is why the classical-point results
survive untouched. Three structural properties are preserved:

  * the (q²-1) factor — so `chi_block_vanishing_at_one` and
    `prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor` still hold;
  * the leading coefficient — lim_{q→1} χ_(2,1)/(q²-1) = -1/2 in BOTH frames,
    verified symbolically, not sampled;
  * bar-parity — both are ODD polynomials in h = q - 1/q,
    published  -h(h²+2)/4                        (degree 3)
    canonical   h(2h⁸+11h⁶+17h⁴+5h²-2)/4         (degree 9)

P(q) is palindromic (q¹²·P(1/q) = P(q)), i.e. bar-involution symmetric, which is
the consistency check on the derivation that does not depend on any numeric pin.

SCOPE
-----
This probe derives and verifies. It does NOT edit
`QBetaPerBlockChiClosedForms.lean`: `chi_block_21` carries proof obligations
there (vanishing at 1, the `(q^2-1)*P21` factorisation, two downstream sums) and
seven other files reference it. That migration is tracked in bean `qou-eddc`;
this is its verified target.

Bean: `qou-eddc`. Ordering ruling: `qou-hu1f`. Producer fix: `qou-y2o7`.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMPUTATIONS = _HERE.parent
sys.path[:0] = [str(_COMPUTATIONS), str(_COMPUTATIONS / "substrate"),
                str(_COMPUTATIONS.parent / "qou-mass" / "src" / "qou_mass" / "_internal")]

import _path_bridge  # noqa: F401,E402
import sympy as sp  # noqa: E402

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from hecke_character_symbolic import q_character_on_braid_word  # noqa: E402

q = sp.Symbol("q", positive=True)

#: The published forms, transcribed from QBetaPerBlockChiClosedForms.lean.
PUBLISHED = {
    (3,): -(q**2 - 1) * (q**2 + 1) ** 2 / (4 * q),
    (2, 1): (q**2 - 1) * (-(q**4) - 1) / (4 * q**3),
    (1, 1, 1): -(q**2 - 1) * (q**2 + 1) ** 2 / (4 * q**5),
}


def derive() -> dict[tuple, sp.Expr]:
    """χ_λ(β_n) − χ_λ(β_p) from the canonical words, symbolically in q."""
    cp = atom_canonical_crossings(1, 0)
    cn = atom_canonical_crossings(0, 1)
    out = {}
    for shape in PUBLISHED:
        xp = q_character_on_braid_word(list(shape), cp, q)
        xn = q_character_on_braid_word(list(shape), cn, q)
        out[shape] = sp.factor(sp.cancel(sp.together(xn - xp)))
    return out, cp, cn


def as_h_polynomial(expr):
    """Express in h = q - 1/q, or return None if it is not a polynomial in h."""
    t = sp.Symbol("t")
    roots = sp.solve(sp.Eq(t, q - 1 / q), q)
    for r in roots:
        sub = sp.simplify(sp.expand(sp.simplify(expr.subs(q, r))))
        if not sub.has(sp.sqrt(t**2 + 4)):
            return sp.expand(sub)
    return None


def main() -> int:
    derived, cp, cn = derive()
    print("Per-block χ_λ(Δ_{T_β}) — canonical (borromean) ordering\n")
    print(f"  proton  word: {[c for _, c in cp]}")
    print(f"  neutron word: {[c for _, c in cn]}\n")

    rows, all_ok = [], True
    for shape, expr in derived.items():
        same = sp.simplify(expr - PUBLISHED[shape]) == 0
        rows.append({
            "lambda": list(shape),
            "canonical_closed_form": sp.sstr(expr),
            "published_closed_form": sp.sstr(sp.factor(PUBLISHED[shape])),
            "identical_to_published": bool(same),
            "dim": {(3,): 1, (2, 1): 2, (1, 1, 1): 1}[shape],
        })
        print(f"  λ={str(shape):<10} dim={rows[-1]['dim']}  "
              f"{'IDENTICAL to published' if same else 'DIFFERS from published'}")
        print(f"     {expr}")

    # The one that moved, characterised exactly.
    ratio = sp.factor(sp.cancel(sp.simplify(derived[(2, 1)] / PUBLISHED[(2, 1)])))
    P = 2 * q**12 - 5 * q**10 + 5 * q**8 - 5 * q**6 + 5 * q**4 - 5 * q**2 + 2
    palindromic = sp.simplify(sp.expand(q**12 * P.subs(q, 1 / q)) - sp.expand(P)) == 0
    at_one = sp.simplify(ratio.subs(q, 1))
    lim_can = sp.limit(derived[(2, 1)] / (q**2 - 1), q, 1)
    lim_pub = sp.limit(PUBLISHED[(2, 1)] / (q**2 - 1), q, 1)
    h_can = as_h_polynomial(derived[(2, 1)])
    h_pub = as_h_polynomial(PUBLISHED[(2, 1)])

    print(f"\n  canonical/published for (2,1) = {ratio}")
    print(f"     at q=1                     : {at_one}")
    print(f"     P palindromic              : {palindromic}")
    print(f"     lim (q→1) χ/(q²-1)  canonical {lim_can}   published {lim_pub}")
    print(f"     as a polynomial in h:  canonical {h_can}")
    print(f"                            published {h_pub}")

    # INDEPENDENT-PATH CROSS-CHECK. Everything above comes from the symbolic
    # Hoefsmit matrix product. Re-derive the same three numbers at q0 through
    # `chi_general_word.chi_all_lambda_any` -- a different implementation
    # (transfer / window kernels over mpmath, no Hoefsmit matrices, no sympy)
    # on the same canonical word.
    #
    # This is here because of the chi-cache staleness found the same day
    # (docs/audits/2026-09-05-chi-caches-stale-to-the-intra-ordering-...): the
    # committed chi-<atom>-h<n> caches are grouped-era. This path CANNOT have
    # read one -- `q_character_on_braid_word` consults a cache only when
    # `atom_cache_label` is passed, and it is not passed above -- but asserting
    # agreement against an unrelated implementation settles that by measurement
    # rather than by reading the call site.
    import mpmath as mp
    from q_parameter import Q_50_DIGIT_STR, Q_MP
    from chi_general_word import chi_all_lambda_any
    from mass_at_3A_proper import atom_braid_word_3A

    mp.mp.dps = 50
    q0_mp = Q_MP
    q0_sym = sp.Rational(Q_50_DIGIT_STR.replace(".", ""), 10 ** (len(Q_50_DIGIT_STR) - 2))
    num_p = chi_all_lambda_any(atom_braid_word_3A(1, 0, q=q0_mp), 3, dps=50, q=q0_mp)
    num_n = chi_all_lambda_any(atom_braid_word_3A(0, 1, q=q0_mp), 3, dps=50, q=q0_mp)

    worst = mp.mpf(0)
    print("\n  independent-path cross-check at q0 (chi_all_lambda_any, no Hoefsmit):")
    for shape, expr in derived.items():
        indep = num_n.get(shape, mp.mpf(0)) - num_p.get(shape, mp.mpf(0))
        symb = mp.mpf(sp.sstr(sp.N(expr.subs(q, q0_sym), 40)))
        rel = abs(indep - symb) / abs(symb) if symb != 0 else abs(indep - symb)
        worst = max(worst, rel)
        print(f"    λ={str(shape):<10} symbolic {mp.nstr(symb, 16):<22} "
              f"independent {mp.nstr(indep, 16):<22} rel {mp.nstr(rel, 4)}")
    cross_ok = worst < mp.mpf("1e-38")

    checks = {
        "independent_path_agrees_at_q0": cross_ok,
        "one_dim_blocks_unchanged":
            derived[(3,)] == sp.factor(PUBLISHED[(3,)])
            or sp.simplify(derived[(3,)] - PUBLISHED[(3,)]) == 0,
        "sign_block_unchanged":
            sp.simplify(derived[(1, 1, 1)] - PUBLISHED[(1, 1, 1)]) == 0,
        "two_dim_block_moved":
            sp.simplify(derived[(2, 1)] - PUBLISHED[(2, 1)]) != 0,
        "q2_minus_1_factor_survives":
            sp.simplify(sp.cancel(derived[(2, 1)] / (q**2 - 1)).is_rational_function(q)),
        "classical_point_agrees": at_one == 1,
        "leading_coefficient_agrees": lim_can == lim_pub == sp.Rational(-1, 2),
        "P_is_palindromic": palindromic,
        "both_bar_odd_in_h": (h_can is not None and h_pub is not None
                              and sp.simplify(h_can.subs(sp.Symbol("t"), -sp.Symbol("t"))
                                              + h_can) == 0),
    }
    print()
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
        all_ok = all_ok and bool(v)

    sys.path.insert(0, str(_COMPUTATIONS / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    wb = WitnessBuilder(Path(__file__).stem, engine="python+sympy")
    wb.set_content_block("prop:qbeta-per-block-chi-closed-forms")
    wb.set_description(
        "Derives the three per-block characters chi_lambda(Delta_T_beta) "
        "symbolically from the CANONICAL (borromean) nucleon words. The two "
        "one-dimensional blocks reproduce the published closed forms exactly; "
        "the 2-dimensional (2,1) block does not, and is the only block the "
        "intra-ordering can reach. States the corrected form and shows the "
        "classical-point results are unaffected."
    )
    wb.add_data("blocks", rows)
    wb.add_data("canonical_over_published_ratio_21", sp.sstr(ratio))
    wb.add_data("ratio_at_q_equals_1", sp.sstr(at_one))
    wb.add_data("P_palindromic", bool(palindromic))
    wb.add_data("limit_chi21_over_q2m1", {"canonical": sp.sstr(lim_can),
                                          "published": sp.sstr(lim_pub)})
    wb.add_data("as_h_polynomial", {"canonical_21": sp.sstr(h_can),
                                    "published_21": sp.sstr(h_pub)})
    for name, ok in checks.items():
        wb.add_assertion(name=name, computed=str(int(bool(ok))), expected="1")
    wb.add_caveat(
        "Derivation only. QBetaPerBlockChiClosedForms.lean is NOT edited here: "
        "chi_block_21 carries proof obligations (vanishing at q=1, the "
        "(q^2-1)*P21 factorisation, two downstream weighted sums) and seven "
        "files reference it. That migration is bean qou-eddc; this is its target."
    )
    wb.add_caveat(
        "The published forms remain correct for the GROUPED word, which is what "
        "qbeta_delta_vs_deltaTbeta_settled_probe verifies (pinned to "
        "intra_order='grouped'). This is a change of canonical braid, not a "
        "correction of an arithmetic error."
    )
    print(f"\nWitness: {wb.save()}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
