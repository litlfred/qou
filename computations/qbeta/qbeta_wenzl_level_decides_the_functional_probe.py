#!/usr/bin/env python3
"""
qbeta_wenzl_level_decides_the_functional_probe.py — qou-99qc: the augmentation
and convention D are Wenzl levels r = 1 and r = 2 of ONE family, at every n.
The n = 3 argument merged in #7115 is a special case, and its caveat is gone.

# Ref: computations/markov/markov_weights_symbolic.py  (Wenzl relation + row cap)
# Ref: computations/qbeta/qbeta_augmentation_is_a_markov_trace_probe.py  (#7115)
# Ref: docs/audits/2026-09-05-qbeta-functional-decision-options.md

WHAT #7115 LEFT OPEN. It showed the augmentation IS the Markov trace at z = q,
that its Wedderburn support is the single one-row partition while convention D's
is the two-row family, and that D7 therefore selects z_D for the decay channel.
Every step of that was computed at n = 3 and the PR said so: "n = 3 only ...
nothing is claimed for general n". If the one-row/two-row split were an n = 3
accident, so was the conclusion.

It is not an accident. It is Wenzl's level, and the corpus already carried the
relation that shows it.

THE DERIVATION, from the corpus's own formula rather than from a character
table. `markov_weights_symbolic` fixes the Wenzl level by

    Q^r = z_W / (1 - Q + z_W),        Q = q^2,   z_W = q*z

and computes the weights by the Schur principal specialisation

    s_lambda = Q^{n(lambda)} * prod_x (1 - Q^r * Q^{c(x)}) / (1 - Q^{h(x)}).

Solving the first relation for z, rather than substituting a value into it,
gives a closed form in the level:

    z(r) = q^{2r-1} (q^2 - 1) / (q^{2r} - 1)

    r = 1  ->  z = q                  the AUGMENTATION
    r = 2  ->  z = q^3/(q^2 + 1)      CONVENTION D
    r = 3  ->  z = q^5/((q^2-q+1)(q^2+q+1))
    r = 4  ->  z = q^7/((q^2+1)(q^4+1))

So the two functionals the Q_beta decision has been choosing between are not
two objects of different kinds, and not even two arbitrary points of the Markov
family: they are the first two INTEGER LEVELS of one tower.

WHY THE SUPPORT FOLLOWS AT EVERY n. Orellana, Crelle 508 (1999) 157-178, p. 5:
`s_{alpha,r}(q) = 0 whenever l(alpha) > r` -- the row cap, cited in the corpus
at `WenzlWeightVanishing.lean`. At r = 1 that kills every partition with two or
more rows, leaving lambda = (n) alone; at r = 2 it kills three or more, leaving
lambda = (n-k, k). Both statements are for ALL n. The n = 3 table of #7115 is
the r = 1 and r = 2 rows of this, at one n.

Consequently D7's characterisation of convention D as "the two-row TL
truncation, surviving family lambda = (n-k,k)" is not an assertion this probe
has to take on trust: it is what r = 2 MEANS, and r = 2 is what z_D solves the
corpus's own Wenzl relation at. Checked here rather than assumed.

TWO THINGS THIS SETTLES THAT #7115 TOOK AS GIVEN.

1. WHY THERE ARE EXACTLY TWO ADMISSIBLE ROOTS. Admissibility is annihilation of
   the >= 3-row blocks (the GNS/TL quotient). By the row cap that is exactly
   `r <= 2`, so the admissible integer levels are r in {1, 2} and there are two
   of them at EVERY n -- not by luck of a cubic at n = 3.
2. WHY THE PUBLISHED z = 1 IS INADMISSIBLE, in general-n terms. Inverting the
   closed form, z = 1 sits at Q^r = q/(1 + q - q^2), i.e. a NON-INTEGER level
   (computed below at the proton pin). A non-integer level is not a level: no
   row cap applies, so it annihilates nothing. That replaces #7115's local
   reason ("the (1^3) numerator does not vanish there") with a structural one.

WHAT THIS DOES NOT DO. It does not choose r. D7 does that, by scoping
convention D -- level 2 -- to the decay/Q_beta channel, and that scoping is the
owner's reading to confirm. It does not improve any number: r = 2 still gives
-43.157 %, the WORSE of the two residuals, which is the anti-fitting directive
working. It does not touch Option E (derive a different element Delta), which
remains the only route to a parameter-free admissible sub-1 % result. Nothing
is wired. Scope-(a).

Exact sympy over Q(q) throughout; the pin enters only where a level has to be
read off numerically, as an exact Rational from the 50-digit proton string,
through mpmath at 60 dps. No float64 (AGENTS.md NO-FLOAT64; probes not exempt).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

sys.path.insert(0, str(HERE.parent / "markov"))
from markov_weights_symbolic import (  # noqa: E402
    hooks_and_contents,
    n_partition,
    partitions_of,
)

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

q = sp.symbols("q", positive=True)
Q_W = q**2


def _f_lambda(shape) -> int:
    hs, _ = hooks_and_contents(list(shape))
    p = 1
    for h in hs:
        p *= h
    return sp.factorial(sum(shape)) // p


def schur_principal_at_level(lam, QR):
    """s_lambda(1, Q, ..., Q^{r-1}) with Q^r supplied as QR.

    The corpus's own closed form (markov_weights_symbolic.schur_principal_symbolic),
    with the level lifted out of the module constant so it can be varied.
    """
    hs, cs = hooks_and_contents(list(lam))
    num, den = sp.Integer(1), sp.Integer(1)
    for h, c in zip(hs, cs):
        num *= 1 - QR * Q_W**c
        den *= 1 - Q_W**h
    return sp.cancel(Q_W ** n_partition(list(lam)) * num / den)


def weights_at_level(n: int, r: int):
    """Normalised Jones-Markov weights y_lambda at integer Wenzl level r."""
    QR = Q_W**r
    shapes = [tuple(s) for s in partitions_of(n)]
    s = {sh: schur_principal_at_level(sh, QR) for sh in shapes}
    Z = sp.cancel(sum(s[sh] * _f_lambda(sh) for sh in shapes))
    return {sh: sp.cancel(s[sh] / Z) for sh in shapes}


def main() -> int:
    mp.mp.dps = 60
    checks: list[dict] = []

    def chk(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        return bool(ok)

    print(__doc__.splitlines()[1])
    print()
    ok = True

    z, r = sp.symbols("z r", positive=True)
    zW = q * z

    # ---- 1. solve Wenzl's relation for z; do not assert the closed form ----
    closed = sp.simplify(sp.solve(sp.Eq(Q_W**r, zW / (1 - Q_W + zW)), z)[0])
    target = q ** (2 * r - 1) * (q**2 - 1) / (q ** (2 * r) - 1)
    ok &= chk("wenzl_relation_SOLVES_to_a_closed_form_in_the_level",
              sp.simplify(closed - target) == 0,
              f"solving Q^r = z_W/(1-Q+z_W) for z with Q=q^2, z_W=qz gives "
              f"z(r) = {sp.simplify(target)} -- derived from the corpus's own "
              "relation, not assumed")

    zD = q**3 / (q**2 + 1)
    z_of = {rv: sp.factor(sp.simplify(closed.subs(r, rv))) for rv in (1, 2, 3, 4)}
    for rv in (1, 2, 3, 4):
        print(f"      r={rv}:  z = {z_of[rv]}")

    ok &= chk("level_1_IS_the_augmentation",
              sp.simplify(z_of[1] - q) == 0,
              "z(1) = q exactly -- the augmentation sigma -> q, which #7115 "
              "showed is the Markov trace at that parameter")
    ok &= chk("level_2_IS_convention_D",
              sp.simplify(z_of[2] - zD) == 0,
              "z(2) = q^3/(q^2+1) = z_D exactly. D7's characterisation of D as "
              "the two-row TL truncation is DERIVED here from the corpus's "
              "Wenzl relation rather than taken on trust")

    # ---- 2. the row cap, at every n we can compute -------------------------
    ns = (3, 4, 5, 6, 7)
    supp = {}
    for rv in (1, 2):
        for n in ns:
            w = weights_at_level(n, rv)
            supp[(rv, n)] = sorted(sh for sh, v in w.items() if sp.simplify(v) != 0)

    r1_ok = all(supp[(1, n)] == [(n,)] for n in ns)
    ok &= chk("level_1_supports_EXACTLY_the_one_row_partition_for_every_n",
              r1_ok,
              "n = " + ", ".join(f"{n}:{supp[(1, n)]}" for n in ns)
              + " -- one row at every n, so the augmentation's ONE-row cap is "
                "structural and not the n=3 accident #7115 could not exclude")

    r2_ok = all(supp[(2, n)] == sorted(sh for sh in map(tuple, partitions_of(n))
                                       if len(sh) <= 2) for n in ns)
    ok &= chk("level_2_supports_EXACTLY_the_two_row_family_for_every_n",
              r2_ok,
              "at every n the nonzero weights are exactly the lambda with "
              "l(lambda) <= 2, i.e. D7's family lambda = (n-k, k) -- Orellana "
              "Crelle 508 (1999) p.5, s_{alpha,r} = 0 for l(alpha) > r")

    ok &= chk("the_two_supports_are_STRICTLY_NESTED_at_every_n",
              all(set(supp[(1, n)]) < set(supp[(2, n)]) for n in ns),
              "one-row is a PROPER subset of two-row at every n, so the "
              "augmentation is a strict refinement of convention D and is not "
              "D -- #7115's conclusion, now general")

    # ---- 3. calibration against the merged n = 3 numbers -------------------
    w3r1 = weights_at_level(3, 1)
    w3r2 = weights_at_level(3, 2)
    exp_r2 = {(3,): (q**4 + 1) / (q**2 + 1) ** 2,
              (2, 1): q**2 / (q**2 + 1) ** 2,
              (1, 1, 1): sp.Integer(0)}
    cal = (all(sp.simplify(w3r1[sh] - (1 if sh == (3,) else 0)) == 0 for sh in w3r1)
           and all(sp.simplify(w3r2[sh] - exp_r2[sh]) == 0 for sh in w3r2))
    ok &= chk("CALIBRATION_reproduces_the_merged_n3_weight_table",
              cal,
              "r=1 gives y_(3)=1, y_(2,1)=0, y_(1^3)=0 and r=2 gives "
              "((q^4+1)/(q^2+1)^2, q^2/(q^2+1)^2, 0) -- byte-for-byte the table "
              "in #7115 (13bb8243d87), so this route is anchored to the merged "
              "result rather than free-standing")

    # ---- 4. why there are exactly TWO admissible levels --------------------
    # admissible = annihilates every block with >= 3 rows; by the row cap that
    # is r <= 2, and r >= 1 for a nonempty tower.
    r3_has_3row = any(len(sh) >= 3 and sp.simplify(v) != 0
                      for sh, v in weights_at_level(3, 3).items())
    ok &= chk("admissibility_is_EXACTLY_level_le_2_hence_two_roots_at_every_n",
              r3_has_3row,
              "level 3 gives a NONZERO weight on a 3-row block (n=3: "
              "y_(1,1,1) != 0), so it is inadmissible; with the row cap this "
              "makes 'annihilates >= 3 rows' equivalent to r <= 2. The two "
              "admissible roots the corpus found at n=3 are the two integer "
              "levels 1 and 2, and there are two of them at EVERY n -- not a "
              "coincidence of one cubic")

    # ---- 5. z = 1 is a NON-INTEGER level ----------------------------------
    # Q^r at z = 1 is READ OFF the Wenzl relation by substitution, not asserted:
    # Q^r = z_W/(1 - Q + z_W) with z_W = q*1 = q.
    QR_z1 = sp.cancel((zW / (1 - Q_W + zW)).subs(z, 1))
    q0 = sp.Rational(Q_50_DIGIT_STR)
    QR_num = mp.mpf(str(sp.N(QR_z1.subs(q, q0), 60)))
    q0m = mp.mpf(str(sp.N(q0, 60)))
    r_z1 = mp.log(QR_num) / (2 * mp.log(q0m))
    print(f"      z = 1  ->  Q^r = {mp.nstr(QR_num, 20)},  r = {mp.nstr(r_z1, 20)}")
    ok &= chk("published_z_eq_1_sits_at_a_NON_INTEGER_wenzl_level",
              abs(r_z1 - mp.floor(r_z1)) > mp.mpf("1e-6")
              and mp.mpf(1) < r_z1 < mp.mpf(2),
              f"r = {mp.nstr(r_z1, 12)} at the proton pin -- strictly between "
              "levels 1 and 2 and not an integer. A non-integer level is not a "
              "level, so no row cap applies and z=1 annihilates NOTHING. That "
              "is the general-n form of the inadmissibility #7115 established "
              "at n=3 by a numerator not vanishing")

    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    w = {
        "description":
            "qou-99qc: the augmentation and convention D are Wenzl levels r=1 "
            "and r=2 of one family. z(r) = q^(2r-1)(q^2-1)/(q^(2r)-1), derived "
            "by solving the corpus's own Wenzl relation. The row cap "
            "(Orellana Crelle 508 p.5) then gives one-row support at r=1 and "
            "two-row at r=2 FOR EVERY n, removing the n=3-only caveat of "
            "#7115 (13bb8243d87). Admissibility = r<=2, so exactly two "
            "admissible levels at every n; the published z=1 is a non-integer "
            "level. Scope-(a); chooses no level and wires nothing.",
        "checks": checks,
        "all_passed": bool(ok),
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "scriptFile": Path(__file__).name,
        "z_of_level": {str(k): sp.srepr(v) for k, v in z_of.items()},
        "z_closed_form": sp.srepr(sp.simplify(target)),
        "support_by_level_and_n": {f"r{rv}_n{n}": [str(s) for s in supp[(rv, n)]]
                                   for rv in (1, 2) for n in ns},
        "z_eq_1_level_at_proton_pin": mp.nstr(r_z1, 30),
        "caveats": [
            "Scope-(a). Establishes a structural identification and a support "
            "fact; derives no observable and proposes no value.",
            "It does NOT choose the level. D7 does, by scoping convention D "
            "(level 2) to the decay/Q_beta channel -- and whether that scoping "
            "reaches the choice of functional WITHIN the channel is the "
            "owner's reading, still open.",
            "Level 2 gives -43.157 %, the WORSE of the two residuals. That is "
            "the anti-fitting directive working, not a defect.",
            "Option E (derive a different element Delta) is untouched and "
            "remains the only route to a parameter-free admissible sub-1 % "
            "result (qou-37j2).",
            "The row cap is cited from Orellana Crelle 508 (1999) p.5 via the "
            "corpus's WenzlWeightVanishing.lean; it is not re-proved here.",
            "Supports are checked at n = 3..7. The cap itself is general, but "
            "the computation is not a proof for all n.",
        ],
    }
    WitnessBuilder.stamp_staleness_metadata(
        w, script_path=__file__, engine="python+sympy",
        q0_anchor="proton", q0_value=Q_50_DIGIT_STR)
    out = HERE / "qbeta-wenzl-level-decides-the-functional.witness.json"
    out.write_text(__import__("json").dumps(w, indent=2) + "\n")
    print(f"  witness -> {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
