#!/usr/bin/env python3
"""The sign character of the Bring chiral fibre's monodromy is non-trivial.

`prop:baryon-product-from-alt` currently says the quark-colour content
of the baryon *selects* the totally antisymmetric isotype `Alt^3`. That
is an input. This probe supplies the half of a derivation that is
purely a fact about the Bring fibre, and states plainly the half that
is still missing.

**What is at issue.** Item 4 of `eightfold-open-problems` asks what
separates the octonionic (colour) `SU(3)` from the eightfold-way
(flavour) `SU(3)`. `docs/audits/2026-08-26-flavour-colour-discriminator-search.md`
proves no *object-level* gate can (`no_object_gate_separates`): the two
triples carry equal dimension, equal Frobenius-Schur type, equal
triality. What does separate them is the Young-symmetry **channel** of
`V (x) V (x) V` that the physical state occupies -- colour sits in
`lambda = (1^3)`, the sign representation of `S_3`; both flavour
channels sit elsewhere. So a derivation of colour antisymmetry would
settle item 4 as well as item 7. The obstacle is that the sign
representation has to come from somewhere.

**What this probe establishes -- exactly, no floating point.** The
canonical Bring chiral cubic from the invariant ring,

    f(X, z) = X^3 + (z+1) X^2 + (z^2+z+1) X + (z^3+z^2+z+1),

has a monodromy representation `pi_1(P^1 - Delta) -> S_3` permuting its
three sheets, and the composite with `sgn` is **surjective onto {+1,-1}**.
Four facts, all in exact rational arithmetic over `QQ[z]`:

  A1. `Delta(z) = -(16z^6 + 24z^5 + 35z^4 + 50z^3 + 35z^2 + 24z + 16)`
      has degree 6 and `gcd(Delta, Delta') = 1`, so the six branch
      points are distinct and each is a *simple* zero. (These are the
      six points `bring-chiral-fibre-figure.witness.json` locates
      numerically, at residuals ~1e-15.)

  A2. `f` has no root in `C(z)`. A monic cubic over the integrally
      closed ring `C[z]` can only have a root in `C(z)` that is
      already in `C[z]`, and comparing leading terms forces that root
      to have degree 1; substituting `X = az + b` and clearing gives
      an inconsistent system. Hence `f` is irreducible over `C(z)`
      and the monodromy is **transitive**.

  A3. The depressed-cubic coefficient `p(z) = (2z^2 + z + 2)/3`
      satisfies `gcd(p, Delta) = 1`. A triple root needs `p = q = 0`,
      so no branch point carries one: at every branch point the fibre
      degenerates to a *double* root plus a simple one, and the local
      monodromy is a **transposition**.

  A4. `Delta` is squarefree of positive degree, hence not a square in
      `C(z)`, so `C(z)(sqrt(Delta))` is a genuine quadratic extension.

  A5. Substituting `X = zY` and taking the leading form at `z = infinity`
      gives `Y^3 + Y^2 + Y + 1`, which is squarefree, so the covering is
      unramified there and all the branching is the six finite points.
      Riemann-Hurwitz then gives `2g - 2 = -2*3 + 6 = 0`: the fibre is a
      genus-1 curve. This confirms `rem:brings-qou-4tuple`'s own words
      ("the elliptic cubic", "chiral elliptic fibre") and pins down an
      inconsistency in the same remark -- see below.

A2 + A3 give the monodromy group: a transitive subgroup of `S_3`
containing a transposition is `S_3` itself. A4 gives the same
conclusion by a second, independent route and identifies the character
concretely -- `sgn` is cut out by the Vandermonde `sqrt(Delta)`, and a
loop has `sgn = -1` exactly when it exchanges the two sheets of that
double cover.

**A5 settles which object `rem:brings-qou-4tuple` is talking about.**
That remark writes "the branched covering `pi: S -> P^1(C)` (degree 4,
six branch points)" two sentences above "the `S_3` permutation of the
three sheets", and a degree-4 covering does not have three sheets.
Riemann-Hurwitz decides it. A degree-4 cover of `P^1` with six simple
branch points has genus 0, not 4; and Bring's genus-4 surface would need
12 branch points at degree 3, or 14 at degree 4 -- never 6. The only
reading consistent with "six branch points" AND "three sheets" is the
degree-3, genus-1 cover computed here, which is exactly what the remark
elsewhere calls "the elliptic cubic" and whose three roots it says
parametrise colour. So "degree 4" does not describe the colour-carrying
fibre; it belongs to a different map, or is simply wrong. Recorded, not
silently repaired: the fix belongs in the content block, by its author.

**The numerical cross-check** (mpmath, 50 dps -- no float64 anywhere)
transports the three roots along a closed path from a base point out to
each branch point, once around it, and back, and reads the resulting
permutation in a *common* basis at the base point. All six come back
transpositions, and the six generate `S_3`. Every continuation step
carries a guard: the distance a root moves must be small compared with
the separation between roots, so the nearest-neighbour matching is
never a coin flip. The worst guard ratio over the whole run is
reported.

**Scope, per the (a)/(b) discipline.** This is a positive result about
the fibre, not a refutation. What it does *not* establish is the step
that would close item 7:

  - that the three sheets of this cubic **are** the three colour tubes
    of the baryon, rather than merely a set of three objects carrying
    an `S_3` action, and
  - that the physical state is the class in `Alt^3` rather than in one
    of the other two isotypes.

The first is plausible from the corpus's own framing -- the same `S_3`
is said to permute `(r, g, b)` -- but "plausible" is not "derived", and
the identification is exactly what item 4 says is open. So the honest
statement is: **the sign line exists and is non-trivial; whether the
baryon lives in it is still an input.** Section "The gap" of
`docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md`
tracks the same gap from the Milnor side.

Cross-references:
  - `prop:baryon-product-from-alt`         (the block that currently selects Alt)
  - `computations/bring_chiral_fibre_figure.py`  (the six branch points, F3)
  - `docs/audits/2026-08-26-flavour-colour-discriminator-search.md` (item 4/7)
  - `docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md`
"""

from __future__ import annotations

import itertools
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# Path bridge (subdirectory refactor): keeps flat-namespace imports
# (`from witness_base import …`) resolving from the `probes/` cluster.
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

WITNESS_OUT = HERE / "bring-cubic-monodromy-probe.witness.json"

# 50 significant digits: the branch points are separated by ~1.2e-1 and
# the closest approach of a transported root to its neighbour is ~1e-2,
# so this is ~48 digits of headroom on every comparison the run makes.
mp.dps = 50

# Continuation resolution. The guard below reports the worst
# (step displacement) / (root separation) ratio actually attained; if
# it ever approached 1/2 the nearest-neighbour matching would be
# unreliable and these would need raising.
N_CIRCLE = 2000
N_SEGMENT = 800

# Base point for the common-basis monodromy. Real, outside the disc
# containing every branch point (all six have |z| < 1.1).
Z_BASE_STR = "2"


# ── Part A: exact algebra over QQ[z] ─────────────────────────────


def exact_facts() -> dict:
    """A1-A4, in exact rational arithmetic. No floating point."""
    X, z = sp.symbols("X z")
    c_sym = sp.Symbol("c")
    b = z + 1
    c = z**2 + z + 1
    d = z**3 + z**2 + z + 1
    f = X**3 + b * X**2 + c * X + d

    delta = sp.Poly(sp.expand(sp.discriminant(sp.Poly(f, X))), z)
    delta_prime = delta.diff(z)
    gcd_dd = sp.Poly(sp.gcd(delta, delta_prime), z)

    # A1 — six distinct simple branch points.
    a1 = {
        "discriminant": sp.sstr(delta.as_expr()),
        "degree": int(delta.degree()),
        "gcd_with_derivative": sp.sstr(gcd_dd.as_expr()),
        "squarefree": gcd_dd.degree() == 0,
        "n_branch_points": int(delta.degree()),
    }

    # A2 — no root in C(z), hence irreducible over C(z), hence the
    # monodromy is transitive. A monic cubic over the integrally closed
    # ring C[z] has any C(z)-root already in C[z]; matching leading
    # terms (X^3 ~ -z^3) forces degree 1, so X = a*z + e exhausts the
    # possibilities.
    a_sym, e_sym = sp.symbols("a e")
    subst = sp.Poly(sp.expand(f.subs(X, a_sym * z + e_sym)), z)
    system = [sp.simplify(co) for co in subst.all_coeffs()]
    sols = sp.solve(system, [a_sym, e_sym], dict=True)
    a2 = {
        "ansatz": "X = a*z + e (forced: monic over the integrally closed "
                  "C[z], leading terms give deg X = 1)",
        "coefficient_equations": [sp.sstr(s) for s in system],
        "solutions_over_C": [
            {str(k): sp.sstr(v) for k, v in s.items()} for s in sols
        ],
        "has_root_in_C_of_z": len(sols) > 0,
        "irreducible_over_C_of_z": len(sols) == 0,
        "monodromy_transitive": len(sols) == 0,
    }

    # A3 — no branch point carries a triple root, so every local
    # monodromy is a transposition. Triple root <=> p = q = 0 for the
    # depressed cubic; it suffices that p and Delta are coprime.
    p_expr = sp.together(sp.expand(c - b**2 / 3))
    p_num = sp.Poly(sp.numer(p_expr), z)
    q_expr = sp.together(sp.expand(2 * b**3 / 27 - b * c / 3 + d))
    q_num = sp.Poly(sp.numer(q_expr), z)
    gcd_p_delta = sp.Poly(sp.gcd(p_num, delta), z)
    a3 = {
        "depressed_p": sp.sstr(sp.factor(p_expr)),
        "depressed_q": sp.sstr(sp.factor(q_expr)),
        "gcd_numer_p_with_discriminant": sp.sstr(gcd_p_delta.as_expr()),
        "coprime": gcd_p_delta.degree() == 0,
        "triple_root_possible": gcd_p_delta.degree() > 0,
        "local_monodromy_is_transposition": gcd_p_delta.degree() == 0,
        "_q_numer_degree": int(q_num.degree()),
    }

    # A4 — Delta is not a square in C(z), so C(z)(sqrt(Delta)) is a
    # genuine quadratic extension: the sign line is non-trivial.
    # Squarefreeness is preserved under the field extension QQ -> C,
    # and a square would need every multiplicity even.
    a4 = {
        "discriminant_squarefree": a1["squarefree"],
        "discriminant_degree_positive": a1["degree"] > 0,
        "is_square_in_C_of_z": not (a1["squarefree"] and a1["degree"] > 0),
        "quadratic_extension_nontrivial": a1["squarefree"] and a1["degree"] > 0,
    }

    # A5 — the genus of the fibre curve, by Riemann-Hurwitz. Needed
    # because rem:brings-qou-4tuple describes the covering as "degree 4,
    # six branch points" two sentences above "the S_3 permutation of the
    # three sheets", and those cannot both describe one map.
    #
    # Behaviour over z = infinity: substituting X = z*Y and taking the
    # leading form gives Y^3 + Y^2 + Y + 1. If that is squarefree the
    # three sheets stay distinct at infinity, so the covering is
    # unramified there and ALL the branching is the six finite points.
    Y = sp.symbols("Y")
    leading = sp.Poly(Y**3 + Y**2 + Y + 1, Y)
    disc_leading = sp.discriminant(leading)
    unramified_at_infinity = disc_leading != 0

    degree = 3
    n_branch = int(delta.degree())
    # Each branch point carries a double root (A3), i.e. one point of
    # ramification index 2, contributing (2-1) = 1 to the RH sum.
    ramification = n_branch if a3["local_monodromy_is_transposition"] else None
    two_g_minus_2 = -2 * degree + ramification if ramification is not None else None
    genus = (two_g_minus_2 + 2) // 2 if two_g_minus_2 is not None else None

    def rh_genus(d: int, b: int):
        """Genus forced by Riemann-Hurwitz for a degree-d cover of P^1
        with b simple branch points, or None if b has the wrong parity."""
        val = -2 * d + b + 2
        return val // 2 if val % 2 == 0 else None

    a5 = {
        "leading_form_at_infinity": sp.sstr(leading.as_expr()),
        "leading_form_discriminant": sp.sstr(disc_leading),
        "unramified_at_infinity": bool(unramified_at_infinity),
        "degree": degree,
        "n_simple_branch_points": n_branch,
        "riemann_hurwitz_2g_minus_2": int(two_g_minus_2),
        "genus": int(genus),
        "fibre_is_elliptic": genus == 1,
        # The two readings rem:brings-qou-4tuple cannot both hold.
        "genus_if_degree_4_with_6_branch_points": rh_genus(4, 6),
        "branch_points_needed_for_genus_4_at_degree_3": 6 + 2 * 3,
        "branch_points_needed_for_genus_4_at_degree_4": 6 + 2 * 4,
    }

    # A6 — the three sheets ARE the corpus's three colour tubes.
    #
    # `prop:color-elliptic` states the colour elliptic equation is exactly
    # this cubic, with `X = (x_2, x_3, x_4)` named as THE COLOUR VARIABLE.
    # `def:color-tube-fibers` then defines the colour tubes (r_z, g_z, b_z)
    # as the roots of a DIFFERENT-LOOKING cubic,
    #     c^3 + (4z+1)c^2 + (6z^2+3z+1)c + (4z^3+3z^2+2z+1),
    # obtained "by substituting X = c + z". Verify that, rather than take
    # it on trust: a translation of the fibre coordinate is an isomorphism
    # at every z, so if it holds then the two cubics have the same
    # discriminant, the same branch points and the SAME monodromy.
    tube = (c_sym**3 + (4*z + 1)*c_sym**2 + (6*z**2 + 3*z + 1)*c_sym
            + (4*z**3 + 3*z**2 + 2*z + 1))
    shifted = sp.expand(f.subs(X, c_sym + z))
    identity_holds = sp.expand(shifted - tube) == 0
    disc_tube = sp.Poly(sp.expand(sp.discriminant(sp.Poly(tube, c_sym))), z)
    disc_equal = (delta - disc_tube).is_zero

    a6 = {
        "corpus_colour_tube_cubic": sp.sstr(tube),
        "substitution": "X = c + z",
        "chiral_cubic_shifted": sp.sstr(sp.Poly(shifted, c_sym).as_expr()),
        "identity_holds": bool(identity_holds),
        "discriminant_of_tube_cubic": sp.sstr(disc_tube.as_expr()),
        "discriminants_identical": bool(disc_equal),
        "consequence": (
            "the three sheets whose monodromy is computed here are the "
            "corpus's own colour tubes (r_z, g_z, b_z) = (w_2 - z, w_3 - z, "
            "w_4 - z), not an abstract triple: same curve, same six branch "
            "points, same monodromy"
        ),
    }

    monodromy_group = (
        "S_3" if (a2["monodromy_transitive"]
                  and a3["local_monodromy_is_transposition"]) else "undetermined"
    )
    return {
        "A1_discriminant_squarefree": a1,
        "A2_irreducible_transitive": a2,
        "A3_no_triple_root": a3,
        "A4_sign_line_nontrivial": a4,
        "A5_fibre_genus": a5,
        "A6_sheets_are_the_colour_tubes": a6,
        "monodromy_group": monodromy_group,
        "sgn_character_surjective": monodromy_group == "S_3",
    }


def discriminant_int_coeffs() -> list[int]:
    """Integer coefficients of Delta(z), highest power first."""
    z = sp.symbols("z")
    X = sp.symbols("X")
    f = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)
    delta = sp.Poly(sp.expand(sp.discriminant(sp.Poly(f, X))), z)
    return [int(co) for co in delta.all_coeffs()]


# ── Part B: high-precision monodromy transport (mpmath, no float64) ──


def cubic_roots(z):
    """The three sheets X_1, X_2, X_3 over z, at mp.dps precision."""
    b = z + 1
    c = z**2 + z + 1
    d = z**3 + z**2 + z + 1
    return list(mp.polyroots([mp.mpc(1), b, c, d], maxsteps=200, extraprec=200))


def min_separation(roots) -> "mp.mpf":
    return min(abs(roots[i] - roots[j]) for i, j in itertools.combinations(range(3), 2))


def _best_matching(prev, curr):
    """Assign each label of `prev` to a distinct root of `curr`,
    minimising the total displacement over all 3! assignments.

    Returns (matched, max_step) where `matched[k]` continues `prev[k]`.
    Exhaustive rather than greedy: with three sheets the full search is
    six comparisons, and greedy can mis-assign near a close approach.
    """
    best = None
    for perm in itertools.permutations(range(3)):
        total = sum(abs(curr[perm[k]] - prev[k]) for k in range(3))
        if best is None or total < best[0]:
            best = (total, perm)
    perm = best[1]
    matched = [curr[perm[k]] for k in range(3)]
    max_step = max(abs(matched[k] - prev[k]) for k in range(3))
    return matched, max_step


def transport(path, start):
    """Analytically continue the three sheets along `path`.

    `path` is a sequence of z values beginning at the point where
    `start` was computed. Returns (final_sheets, worst_guard) where
    `worst_guard` is the largest ratio

        (distance a sheet moved in one step) / (separation of the
         sheets at that step)

    attained anywhere on the path. A value well below 1/2 means the
    nearest-neighbour matching was never a close call.
    """
    current = list(start)
    worst = mp.mpf(0)
    for zk in path[1:]:
        curr = cubic_roots(zk)
        matched, max_step = _best_matching(current, curr)
        sep = min_separation(curr)
        ratio = max_step / sep
        if ratio > worst:
            worst = ratio
        current = matched
    return current, worst


def _circle(centre, radius, n, start_unit):
    """`n`-step counterclockwise circle of the given radius about
    `centre`, beginning (and ending) at `centre + radius*start_unit` so
    it joins the incoming segment without a jump."""
    pts = [centre + radius * start_unit * mp.expjpi(2 * mp.mpf(k) / n)
           for k in range(n)]
    pts.append(pts[0])
    return pts


def _segment(z_from, z_to, n):
    return [z_from + (z_to - z_from) * (mp.mpf(k) / n) for k in range(n + 1)]


def numeric_monodromy(exact: dict) -> dict:
    """Six loops from a common base point; read the permutations off."""
    coeffs = [mp.mpf(c) for c in discriminant_int_coeffs()]
    bps = list(mp.polyroots(coeffs, maxsteps=200, extraprec=300))
    bps.sort(key=lambda w: (mp.nstr(w.real, 20), mp.nstr(w.imag, 20)))

    sep_bp = min(abs(bps[i] - bps[j])
                 for i, j in itertools.combinations(range(len(bps)), 2))
    # A third of the closest approach: each circle then encloses exactly
    # one branch point, with the nearest other one a full radius away.
    radius = sep_bp / 3

    z_base = mp.mpc(mp.mpf(Z_BASE_STR), 0)
    base_roots = cubic_roots(z_base)

    # Every segment must stay clear of every branch point it is not
    # aimed at, or the "loop around exactly one" reading is wrong.
    def segment_clearance(z_j):
        u = (z_base - z_j) / abs(z_base - z_j)
        s_j = z_j + radius * u
        worst = None
        for other in bps:
            if abs(other - z_j) < radius / 2:
                continue
            # distance from `other` to the segment [z_base, s_j]
            v = s_j - z_base
            t = ((other - z_base) * mp.conj(v)).real / (abs(v) ** 2)
            t = max(mp.mpf(0), min(mp.mpf(1), t))
            dist = abs(other - (z_base + t * v))
            if worst is None or dist < worst:
                worst = dist
        return s_j, worst

    loops = []
    worst_guard = mp.mpf(0)
    min_clearance = None
    for idx, z_j in enumerate(bps):
        s_j, clearance = segment_clearance(z_j)
        if min_clearance is None or clearance < min_clearance:
            min_clearance = clearance
        u_j = (z_base - z_j) / abs(z_base - z_j)
        path = (_segment(z_base, s_j, N_SEGMENT)
                + _circle(z_j, radius, N_CIRCLE, u_j)[1:]
                + _segment(s_j, z_base, N_SEGMENT)[1:])
        final, guard = transport(path, base_roots)
        if guard > worst_guard:
            worst_guard = guard
        # Read the permutation in the common basis at z_base.
        perm = []
        for k in range(3):
            dists = [abs(final[k] - base_roots[m]) for m in range(3)]
            perm.append(int(min(range(3), key=lambda m: dists[m])))
        # The path ends AT the base point, so the transported sheets and
        # the base sheets are two orderings of one recomputed root set.
        # This residual therefore checks that the identification is a
        # permutation with nothing left over -- not that the transport
        # itself was accurate; the guard ratio is what covers that.
        closure = max(abs(final[k] - base_roots[perm[k]]) for k in range(3))
        cyc = _cycle_type(tuple(perm))
        loops.append({
            "branch_point": {"re": mp.nstr(z_j.real, 20),
                             "im": mp.nstr(z_j.imag, 20)},
            "discriminant_residual": mp.nstr(
                abs(sum(coeffs[i] * z_j ** (len(coeffs) - 1 - i)
                        for i in range(len(coeffs)))), 8),
            "segment_clearance": mp.nstr(clearance, 12),
            "permutation": perm,
            "cycle_type": cyc,
            "is_transposition": cyc == "transposition",
            "sgn": -1 if cyc == "transposition" else 1,
            "identification_residual": mp.nstr(closure, 8),
            "worst_guard_ratio": mp.nstr(guard, 8),
        })

    perms = [tuple(L["permutation"]) for L in loops]
    generated = _generate(perms)

    # A7 — the corpus's own H_1 H_2 claim, checked against these numbers.
    # `rem:holonomy-trefoil` says H_1, H_2 are the holonomies around two
    # DISTINCT branch points and that their composite "acts as a 3-cycle in
    # the symmetric-group holonomy S_3", with (H_1 H_2)^3 = id. Each loop
    # here IS such a holonomy, so composing two distinct ones tests that
    # claim directly rather than taking it on trust.
    distinct = sorted(set(perms))
    composites = []
    for a, b in itertools.permutations(distinct, 2):
        pr = _compose(a, b)
        composites.append({
            "left": list(a), "right": list(b), "product": list(pr),
            "cycle_type": _cycle_type(pr), "order": _order(pr),
        })
    a7 = {
        "distinct_local_monodromies": [list(x) for x in distinct],
        "composites_of_two_distinct": composites,
        "all_composites_are_3_cycles": bool(
            composites and all(c["cycle_type"] == "3-cycle" for c in composites)),
        "all_composites_have_order_3": bool(
            composites and all(c["order"] == 3 for c in composites)),
        "corroborates_corpus_claim": (
            "rem:holonomy-trefoil (as reverted on main by 7adab17a3d) states "
            "H_1 H_2 acts as a 3-cycle in S_3 with (H_1 H_2)^3 = id. Two "
            "distinct transpositions sharing a letter compose to a 3-cycle, "
            "and these do."
        ),
    }
    return {
        "base_point": Z_BASE_STR,
        "dps": mp.dps,
        "n_circle_steps": N_CIRCLE,
        "n_segment_steps": N_SEGMENT,
        "branch_point_min_separation": mp.nstr(sep_bp, 12),
        "loop_radius": mp.nstr(radius, 12),
        "min_segment_clearance": mp.nstr(min_clearance, 12),
        "worst_guard_ratio_over_all_loops": mp.nstr(worst_guard, 8),
        "guard_is_safe": worst_guard < mp.mpf("0.25"),
        "loops": loops,
        "all_transpositions": all(L["is_transposition"] for L in loops),
        "group_order_generated": len(generated),
        "group_generated": "S_3" if len(generated) == 6 else (
            "A_3" if len(generated) == 3 else f"order-{len(generated)}"),
        "A7_composite_is_a_3_cycle": a7,
        "sgn_of_the_six_generators": sorted({L["sgn"] for L in loops}),
        "sgn_image_of_the_group": (
            [-1, 1] if any(L["sgn"] == -1 for L in loops) else [1]),
    }


def _cycle_type(perm: tuple) -> str:
    if perm == (0, 1, 2):
        return "identity"
    fixed = sum(1 for k in range(3) if perm[k] == k)
    if fixed == 1:
        return "transposition"
    return "3-cycle"


def _order(p: tuple) -> int:
    """Order of a permutation of three letters."""
    n, q = 1, p
    while q != (0, 1, 2):
        q = _compose(q, p)
        n += 1
    return n


def _compose(a: tuple, b: tuple) -> tuple:
    return tuple(a[b[k]] for k in range(3))


def _generate(gens) -> set:
    seen = {(0, 1, 2)}
    frontier = [(0, 1, 2)]
    while frontier:
        g = frontier.pop()
        for h in gens:
            x = _compose(g, h)
            if x not in seen:
                seen.add(x)
                frontier.append(x)
    return seen


# ── Main ─────────────────────────────────────────────────────────


def main() -> int:
    print("A. Exact algebra over QQ[z] (sympy; no floating point)")
    exact = exact_facts()
    a1 = exact["A1_discriminant_squarefree"]
    print(f"   A1  Delta(z) = {a1['discriminant']}")
    print(f"       degree {a1['degree']}, gcd(Delta, Delta') = "
          f"{a1['gcd_with_derivative']}  ->  squarefree: {a1['squarefree']}")
    a2 = exact["A2_irreducible_transitive"]
    print(f"   A2  roots of the form a*z+e over C: "
          f"{a2['solutions_over_C'] or 'none'}  ->  irreducible over C(z): "
          f"{a2['irreducible_over_C_of_z']}  (monodromy transitive)")
    a3 = exact["A3_no_triple_root"]
    print(f"   A3  p(z) = {a3['depressed_p']}, gcd(numer p, Delta) = "
          f"{a3['gcd_numer_p_with_discriminant']}  ->  no triple root: "
          f"{not a3['triple_root_possible']}  (local monodromy is a "
          f"transposition)")
    a4 = exact["A4_sign_line_nontrivial"]
    print(f"   A4  Delta a square in C(z): {a4['is_square_in_C_of_z']}  ->  "
          f"C(z)(sqrt Delta) is a genuine quadratic extension: "
          f"{a4['quadratic_extension_nontrivial']}")
    a5 = exact["A5_fibre_genus"]
    print(f"   A5  leading form at infinity {a5['leading_form_at_infinity']}, "
          f"discriminant {a5['leading_form_discriminant']}  ->  unramified "
          f"there: {a5['unramified_at_infinity']}; Riemann-Hurwitz with "
          f"degree {a5['degree']} and {a5['n_simple_branch_points']} simple "
          f"branch points gives genus {a5['genus']} (elliptic: "
          f"{a5['fibre_is_elliptic']})")
    print(f"       a degree-4 cover with 6 simple branch points would have "
          f"genus {a5['genus_if_degree_4_with_6_branch_points']}; a genus-4 "
          f"cover would need "
          f"{a5['branch_points_needed_for_genus_4_at_degree_3']} of them at "
          f"degree 3, "
          f"{a5['branch_points_needed_for_genus_4_at_degree_4']} at degree 4")
    a6 = exact["A6_sheets_are_the_colour_tubes"]
    print(f"   A6  corpus colour-tube cubic under X = c+z reproduces this "
          f"cubic: {a6['identity_holds']}; discriminants identical: "
          f"{a6['discriminants_identical']}")
    print(f"       => the three sheets ARE (r_z, g_z, b_z), the corpus's own "
          f"colour tubes")
    print(f"   =>  monodromy group {exact['monodromy_group']}; sgn "
          f"surjective onto {{+1,-1}}: {exact['sgn_character_surjective']}")

    print(f"\nB. Transporting the three sheets at {mp.dps} dps "
          f"(mpmath; no float64)")
    numeric = numeric_monodromy(exact)
    print(f"   base point z0 = {numeric['base_point']}, loop radius "
          f"{numeric['loop_radius']} "
          f"(branch points no closer than "
          f"{numeric['branch_point_min_separation']})")
    print(f"   closest a segment comes to a branch point it does not "
          f"encircle: {numeric['min_segment_clearance']}")
    for L in numeric["loops"]:
        print(f"     bp ({L['branch_point']['re']}, {L['branch_point']['im']}i)"
              f"  perm {tuple(L['permutation'])}  {L['cycle_type']:14s}"
              f"  sgn {L['sgn']:+d}  id-residual "
              f"{L['identification_residual']}")
    print(f"   worst (step / separation) guard ratio over every step of "
          f"every loop: {numeric['worst_guard_ratio_over_all_loops']} "
          f"(safe: {numeric['guard_is_safe']})")
    a7 = numeric["A7_composite_is_a_3_cycle"]
    print(f"   A7  distinct local monodromies "
          f"{a7['distinct_local_monodromies']}; composing two distinct ones "
          f"gives a 3-cycle of order 3: "
          f"{a7['all_composites_are_3_cycles'] and a7['all_composites_have_order_3']}"
          f"  -> corroborates rem:holonomy-trefoil's (H_1 H_2)^3 = id")
    print(f"   all six loops are transpositions: "
          f"{numeric['all_transpositions']}; they generate "
          f"{numeric['group_generated']}; sgn on the generators "
          f"{numeric['sgn_of_the_six_generators']}, on the group "
          f"{numeric['sgn_image_of_the_group']}")

    established = bool(
        exact["sgn_character_surjective"]
        and numeric["all_transpositions"]
        and numeric["group_generated"] == "S_3"
        and numeric["guard_is_safe"]
    )
    agrees = (exact["monodromy_group"] == numeric["group_generated"])

    print("\nVERDICT")
    print(f"   exact and numerical routes agree on the monodromy group: "
          f"{agrees}")
    print(f"   the sign character of the Bring fibre's S_3 is non-trivial: "
          f"{established}")
    print("   STILL AN INPUT: that the three sheets ARE the three colour")
    print("   tubes, and that the baryon occupies the Alt^3 isotype rather")
    print("   than one of the other two. The sign line exists; whether the")
    print("   state lives in it is not settled here.")

    out = {
        "schemaVersion": "1.0.0",
        "description": (
            "The monodromy of the canonical Bring chiral cubic "
            "X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1) is the full S_3, so its "
            "sign character is non-trivial and is cut out by the Vandermonde "
            "sqrt(Delta). Establishes the existence of the sign line that "
            "prop:baryon-product-from-alt currently selects by hand; does NOT "
            "establish that the baryon state occupies it."
        ),
        "computation": {
            "script": "computations/probes/bring_cubic_monodromy_probe.py",
            "arithmetic": (
                "Part A exact over QQ[z] (sympy discriminant / gcd / solve); "
                "Part B mpmath at 50 dps. No float64 anywhere: the "
                "discriminant's coefficients are integers and every "
                "continuation step is mpc."
            ),
        },
        "exact": exact,
        "numeric": numeric,
        "summary": {
            "monodromy_group": exact["monodromy_group"],
            "sign_character_nontrivial": established,
            "routes_agree": agrees,
            "scope": (
                "(a) positive result about the fibre. Two independent exact "
                "routes to a non-trivial sgn: transitive + a transposition "
                "gives S_3; and Delta squarefree of degree 6 is not a square "
                "in C(z), so the quadratic extension is genuine."
            ),
            "what_is_still_an_input": (
                "the identification of the three sheets with the three colour "
                "tubes, and the placement of the physical state in Alt^3 "
                "rather than in the trivial or standard isotype. Item 4 of "
                "eightfold-open-problems is exactly the first of these."
            ),
            "consumes": [
                "computations/bring_chiral_fibre_figure.py "
                "(the same six branch points, located numerically at "
                "residuals ~1e-15)",
            ],
            "corpus_inconsistency_flagged": (
                "rem:brings-qou-4tuple describes the covering as 'degree 4, "
                "six branch points' two sentences above 'the S_3 permutation "
                "of the three sheets'. By Riemann-Hurwitz a degree-4 cover of "
                "P^1 with six simple branch points has genus 0, and a genus-4 "
                "cover needs 12 branch points at degree 3 or 14 at degree 4. "
                "The degree-3, genus-1 cover computed here is the only "
                "reading consistent with both 'six branch points' and 'three "
                "sheets', and matches that remark's own 'elliptic cubic'. "
                "Flagged for the block's author; not repaired here."
            ),
            "bears_on": [
                "prop:baryon-product-from-alt",
                "eightfold-open-problems item 4 (flavour vs colour)",
                "eightfold-open-problems item 7 (colour antisymmetry)",
            ],
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote: {WITNESS_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
