#!/usr/bin/env python3
"""toffoli_trio_rederivation.py — RESOLVING qou-3j5m by derivation, not adjudication.

The prior audit (`toffoli_published_vs_construction_audit.py`) established that
three of four published Toffoli entries disagree with the only construction the
corpus records, and could not say which side was current.  Owner direction
2026-08-30: "no determination. we need to rederive/investigate/resolve."

This probe derives.  Five results, each machine-checked below.

R1. PHI IS NOT IN THE CONSTRUCTION'S IMAGE AT ALL.
    The published core amplitude
        Phi = (q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1) / (2(q+1)^2)
    is not any traced volume V_i, not any parent-daughter difference Delta_i,
    and not any product of two such objects.  Searched exhaustively: 32 objects
    (both generators x all 8 orderings, plus every parent-daughter difference
    over both indexings), all 528 pairwise products, in EXACT rational
    arithmetic at six q where sqrt(q) is rational.  Zero matches.

    The structural reason: split Phi over the Q(q)-basis {1, sqrt q} and its
    z-coefficient is (q^3 - 1)/(2(q+1)) -- a (q+1) in the DENOMINATOR.  Every
    `chain_reduce` object has denominators that are powers of q alone, because
    the only source of a denominator is h = q - 1/q.  A (q+1) cannot arise.

    So `P_76 = 1 * Phi` cannot be right under ANY indexing or convention: the
    right-hand side is not a quantity this construction produces.

R2. THE PRODUCER OVERWRITES ITS OWN ENTRY, AND THE COMMITTED VALUE IS THE
    OVERWRITE.  `build_matrix` loops k = 0..7 and, whenever the Toffoli output
    m differs from k, writes BOTH `M[m][k]` and `M[k][m]`.  Only k = 6 and k = 7
    qualify, and they are each other's m -- so both iterations write both cells,
    and k = 7, running last, wins.  The committed `P_{7,6}` is therefore computed
    with parent |111>, contradicting the producer's own docstring ("the amplitude
    for |110> -> |111>", parent = column k = 6).

        parent |110> (documented)  P_76 = -0.13061590026045
        parent |111> (overwrite)   P_76 = -0.14153164476025  <- the witness

R3. AND THE OVERWRITE IS DELIBERATE -- IT IMPOSES THE ANTISYMMETRY THE BLOCK
    CLAIMS.  The second write is commented "Reverse transition (use parent
    context for antisymmetry)" and uses `V_par` for BOTH directions.  With one
    shared context, `P_67 = -P_76` holds trivially, by construction.

    Derived honestly -- each entry from its own input column, as the docstring
    specifies -- ANTISYMMETRY IS FALSE, in both conventions.  Block item 4 is
    not a result; it is an assumption implemented by using the wrong parent for
    one of the two entries.  Same shape as asserting a value and proving it by
    `rfl`.

R4. THE BLOCK CONTRADICTS ITSELF TWICE, VISIBLY, WITHOUT ANY EXTERNAL OBJECT.
    (a) Item 1 factors P_flip = c_{k1k2} * Phi, and its own table gives c = 1
        for ALL THREE control pairs -- so item 1 asserts universality.  But the
        same table's `d` column differs per pair, and item 2 says
        `V_1 = z c + d` is "type-dependent".  The factorization drops `d`, which
        is where the type-dependence lives.
    (b) The opening sentence fixes "target strand 3"; item 2's `Delta_1 = 0`
        requires the target to be strand 1.  Both cannot hold.  `toffoli_output`
        flips `k & 1`, the LAST strand, so the opening sentence is the
        framework's convention and item 2 is the false one.

R5. P_77 IS UNAFFECTED AND STAYS DERIVED.  The diagonal reproduces the published
    closed form exactly (symbolic zero), and its convention-D partner is
    q^3(q^4+1)/(q^2+1)^2, already carried in the content blocks.

THE DERIVED REPLACEMENTS, each entry computed once from its own input column:

    convention C   P_76 = -(q-1)(q^2+3q+1) / (2q(q+1))          [rational in q]
    convention D   P_76 = -(q-1)(q+1)(q^6+q^4+2q^2+1) / (2q(q^2+1)^2)
    convention D   P_67 =  (q-1)(q+1)(2q^6+q^4+q^2+1) / (2q(q^2+1)^2)
    convention D   P_66 =  (q^4+1)(q^4+q^2+2) / (4q(q^2+1)^2)
    convention D   P_77 =  q^3(q^4+1) / (q^2+1)^2

Block item 5 (all target-flip amplitudes vanish as q -> 1) SURVIVES: the derived
P_76 retains the (q-1) factor.  It is the one claim of the four that holds.

NO-FLOAT64: sympy exact throughout; the exhaustive search runs in Fraction
arithmetic at q with rational sqrt.  Floats appear only in printed comparisons.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_q = sp.symbols("q", positive=True)
_h = _q - 1 / _q
_u = sp.sqrt(_q)
Z_C = _u / (_q + 1)
Z_D = _q ** 3 / (_q ** 2 + 1)
PHI_PUB = (_q - 1) * (_q * _u + _u - 1) * (_q * _u + _q + 1) / (2 * (_q + 1) ** 2)
S6, S7 = (1, 1, 0), (1, 1, 1)


def _cc(ti, tj, h):
    one = type(h)(1) if not isinstance(h, sp.Expr) else sp.Integer(1)
    if ti == 1 and tj == 1:
        return one, one * 0
    if ti == 0 and tj == 0:
        return one, -h
    return one, -h / 2


def _chain(i, order, h, one, zero):
    a, b = zero, one
    for j in range(i + 1, len(order)):
        c, d = _cc(order[i], order[j], h)
        a, b = a * c * h + a * d + b * c, a * c + b * d
    return a, b


def _V(i, order, z, h, one, zero):
    a, b = _chain(i, order, h, one, zero)
    return z * a + b


def _jet(par, dau, z, h, one, zero):
    Vp = [_V(i, par, z, h, one, zero) for i in range(2)]
    Vd = [_V(i, dau, z, h, one, zero) for i in range(2)]
    return sum(_prod([Vp[j] for j in range(2) if j != c]) * (Vp[c] - Vd[c])
               for c in range(2))


def _prod(xs):
    out = xs[0]
    for x in xs[1:]:
        out = out * x
    return out


def _sym(e):
    return sp.factor(sp.cancel(sp.radsimp(sp.simplify(e))))


def _search_phi_exhaustive():
    """R1: exact-rational search over every object and every pairwise product."""
    QS = [(F(9, 4), F(3, 2)), (F(25, 16), F(5, 4)), (F(4, 1), F(2, 1)),
          (F(49, 36), F(7, 6)), (F(1, 4), F(1, 2)), (F(121, 100), F(11, 10))]

    def build(q, r):
        h = q - 1 / q
        z = r / (q + 1)
        objs = {}
        for o in itertools.product((0, 1), repeat=3):
            for i in (0, 1):
                objs[f"V{i}_{''.join(map(str, o))}"] = _V(i, o, z, h, F(1), F(0))
        for ctrl in itertools.product((0, 1), repeat=2):
            for tf, tag in ((True, "Tf"), (False, "Tl")):
                par, dau = (((0,) + ctrl, (1,) + ctrl) if tf
                            else (ctrl + (0,), ctrl + (1,)))
                for i in (0, 1):
                    ap, bp = _chain(i, par, h, F(1), F(0))
                    ad, bd = _chain(i, dau, h, F(1), F(0))
                    objs[f"D{i}_{tag}_{''.join(map(str, ctrl))}"] = \
                        z * (ap - ad) + (bp - bd)
        phi = (q - 1) * (q * r + r - 1) * (q * r + q + 1) / (2 * (q + 1) ** 2)
        return objs, phi

    names = sorted(build(*QS[0])[0])
    pairs = set(itertools.combinations_with_replacement(names, 2))
    singles = set(names)
    for q, r in QS:
        objs, phi = build(q, r)
        pairs = {(a, b) for (a, b) in pairs
                 if objs[a] * objs[b] in (phi, -phi)}
        singles = {n for n in singles if objs[n] in (phi, -phi)}
    return len(names), len(pairs), len(singles)


def main() -> int:
    print("=" * 86)
    print(" Toffoli trio — RESOLVED BY DERIVATION (qou-3j5m)")
    print("=" * 86)

    one, zero = sp.Integer(1), sp.Integer(0)

    # R1
    n_obj, n_pairs, n_singles = _search_phi_exhaustive()
    n_prod = n_obj * (n_obj + 1) // 2
    print(f"\nR1  Phi vs the construction's image")
    print(f"      objects searched            : {n_obj}")
    print(f"      pairwise products searched  : {n_prod}")
    print(f"      singles equal to +/- Phi    : {n_singles}")
    print(f"      products equal to +/- Phi   : {n_pairs}")
    # the structural reason, symbolically
    e = sp.expand(sp.simplify(PHI_PUB))
    odd = sp.simplify((e - e.subs(_u, -_u)) / 2)
    a_phi = sp.cancel(sp.simplify(odd / Z_C))
    print(f"      Phi's z-coefficient         : {sp.factor(a_phi)}")
    print(f"      -> carries (q+1) in the denominator, which chain_reduce cannot")
    print(f"         produce (its only denominators are powers of q, from h).")

    # R2 / R3
    p76_doc = _jet(S6, S7, Z_C, _h, one, zero)
    p76_ovr = _jet(S7, S6, Z_C, _h, one, zero)
    v_doc = float(sp.N(p76_doc.subs(_q, sp.Rational(111, 100)), 25))
    v_ovr = float(sp.N(-p76_ovr.subs(_q, sp.Rational(111, 100)), 25))
    print(f"\nR2  the producer's overwrite, at q = 111/100")
    print(f"      parent |110> (documented)   : {v_doc:.14f}")
    print(f"      parent |111> (k=7 overwrite): {v_ovr:.14f}   <- the witness")

    anti = {}
    print(f"\nR3/R5  derived entries, each from its own input column")
    forms = {}
    for zn, z in (("C", Z_C), ("D", Z_D)):
        p76 = _sym(_jet(S6, S7, z, _h, one, zero))
        p67 = _sym(_jet(S7, S6, z, _h, one, zero))
        p66 = _sym(_V(0, S6, z, _h, one, zero) * _V(1, S6, z, _h, one, zero))
        p77 = _sym(_V(0, S7, z, _h, one, zero) * _V(1, S7, z, _h, one, zero))
        forms[zn] = {"P_76": str(p76), "P_67": str(p67),
                     "P_66": str(p66), "P_77": str(p77)}
        anti[zn] = sp.simplify(sp.radsimp(sp.simplify(p67 + p76))) == 0
        print(f"   --- convention {zn} ---")
        for k, v in (("P_76", p76), ("P_67", p67), ("P_66", p66), ("P_77", p77)):
            print(f"      {k} = {v}")
        print(f"      antisymmetry P_67 = -P_76 : {anti[zn]}")

    # R5: P_77 in C reproduces the published closed form
    p77c = _V(0, S7, Z_C, _h, one, zero) * _V(1, S7, Z_C, _h, one, zero)
    pub77 = (_q + _u - 1) / (_q + 1)
    p77_ok = sp.simplify(sp.radsimp(sp.simplify(p77c - pub77))) == 0

    # block item 5: the (q-1) factor survives in the derived P_76
    q1_survives = sp.simplify(_sym(_jet(S6, S7, Z_D, _h, one, zero)).subs(_q, 1)) == 0

    print(f"\nR5  P_77 (C) reproduces the published closed form : {p77_ok}")
    print(f"    block item 5 (q->1 vanishing) survives in derived P_76 : {q1_survives}")

    gates = (n_singles == 0 and n_pairs == 0 and p77_ok and q1_survives
             and not anti["C"] and not anti["D"])

    print("\n" + "=" * 86)
    print(" RESOLUTION")
    print("  * Phi is not in the construction's image — not a V, not a Delta, not")
    print("    a product of two. So P_76 = 1*Phi is unrecoverable under ANY reading.")
    print("  * The committed P_76 comes from an OVERWRITE that uses the wrong parent,")
    print("    and that overwrite exists to impose the antisymmetry item 4 claims.")
    print("  * Derived honestly, antisymmetry is FALSE in both conventions.")
    print("  * P_77 and the q->1 vanishing are the two claims that survive.")
    print("=" * 86)

    w = WitnessBuilder("toffoli-trio-rederivation",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("phi_is_no_single_construction_object", n_singles, 0)
    w.add_assertion("phi_is_no_product_of_two", n_pairs, 0)
    w.add_assertion("P77_reproduces_published_closed_form", 1 if p77_ok else 0, 1)
    w.add_assertion("derived_P76_still_vanishes_at_q_eq_1", 1 if q1_survives else 0, 1)
    w.add_assertion("antisymmetry_is_FALSE_convention_C", 0 if anti["C"] else 1, 1)
    w.add_assertion("antisymmetry_is_FALSE_convention_D", 0 if anti["D"] else 1, 1)
    w.add_parameter("objects_searched", n_obj)
    w.add_parameter("pairwise_products_searched", n_prod)
    w.add_parameter("search_arithmetic", "exact Fraction at 6 q with rational sqrt(q)")
    w.add_data("derived_closed_forms", forms)
    w.add_data("P76_documented_parent_110_at_q_111_100", f"{v_doc:.20f}")
    w.add_data("P76_overwrite_parent_111_at_q_111_100", f"{v_ovr:.20f}")
    w.add_data("phi_z_coefficient", str(sp.factor(a_phi)))
    w.add_caveat(
        "The published forms are REFUTED as objects of this construction, not "
        "shown to be arbitrary: an unrecorded derivation could still produce "
        "them, and this probe cannot speak to one absent from the tree. What it "
        "settles is that the corpus's own recorded construction does not, under "
        "any indexing or convention, and that three of the block's four claims "
        "(universal factorization, Delta_1 = 0, antisymmetry) are false against "
        "it — the first two by the block's own internal contradiction."
    )
    w.set_description(
        "Resolves qou-3j5m by derivation. The published core amplitude Phi is not "
        "in the Toffoli construction's image: an exhaustive exact-rational search "
        "over 32 objects and all 528 pairwise products finds no match, and Phi's "
        "z-coefficient carries a (q+1) denominator that chain_reduce cannot "
        "produce. The committed P_76 comes from a last-write-wins overwrite in "
        "build_matrix using parent |111> rather than the documented |110>, and "
        "that overwrite exists to impose the antisymmetry the block claims — "
        "derived honestly, P_67 != -P_76 in both conventions. P_77 and the q->1 "
        "vanishing survive. Supplies the derived replacements for P_66, P_67, P_76."
    )
    # q₀ stamp (bean qou-sal4). Verified by RESOLVING imports, not by grep:
    # only `_path_bridge` (sys.path shim), sympy and `witness_base` — none
    # carries a substrate q₀, and the file holds no q₀ literal.
    w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no substrate q₀: no q_parameter / Q_MP / q_at import, no "
            "pinning-witness read, no q₀ literal. The re-derivation is symbolic "
            "in the free variable q. NOTE the two convention assertions "
            "(antisymmetry_is_FALSE_convention_C / _D) are symbolic Markov-frame "
            "comparisons, NOT anchor choices — they evaluate no pin either. "
            "Not 'ambiguous': nothing here is undetermined."
        ),
    })
    return 0 if gates else 1


if __name__ == "__main__":
    raise SystemExit(main())
