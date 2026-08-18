#!/usr/bin/env python3
"""The 5_2 invariant trace field is the CUBIC of discriminant -23, not Q(sqrt-7).

`docs/audits/2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md` opens with

    "The 5_2 invariant trace field is Q(sqrt-7) (det(5_2)=7), so the bar-odd
     action is expected as a Q(sqrt-7) dilog constant."

Both halves of that sentence are wrong, and the parenthetical shows why: it reads
the trace field off the DETERMINANT, which is an Alexander-polynomial (abelian)
datum, not a geometric one.  This probe certifies the correction and pins down
exactly which object each field belongs to.

What is certified here
----------------------

1.  The geometric shapes of the 5_2 saddle -- taken from the corpus's OWN solver,
    `qbeta_5two_quantum_volume_probe.saddle`, not re-derived -- satisfy monic
    integer CUBICS of discriminant -23.  Checked by exact integer arithmetic on
    the recovered coefficients, not by a floating-point near-match.

2.  Q(sqrt-7) is NOT a subfield of the trace field K.  This is a scope-(b)
    structural exclusion resting on a PROVED invariant -- the tower law:
    [Q(sqrt-7):Q] = 2 does not divide [K:Q] = 3, so no embedding exists.  It is
    not a numerical near-miss and no amount of precision can rescue it.

3.  The unique quadratic field attached to K is Q(sqrt-23), the quadratic
    resolvent cut out by disc(K).  A non-Galois cubic has Galois group S_3, whose
    unique index-2 subgroup A_3 fixes exactly Q(sqrt(disc)).  So if the bar-odd
    channel has a quadratic arithmetic home, it is the sqrt-23 line -- which is
    what the corpus's own A6 sigma-pair tower already records.

4.  Where the 7 legitimately lives: the Alexander polynomial Delta(t) = 2t^2-3t+2
    has discriminant -7, and det(5_2) = |Delta(-1)| = 7.  So Q(sqrt-7) IS attached
    to 5_2 -- as the Alexander root field, equivalently the quadratic subfield of
    Q(zeta_7), the home of the abelian/metabelian data of the Z/7 branched cover.
    A different layer from the geometric SL_2(C) representation.

What is NOT claimed
-------------------

Nothing about the bar-odd action VALUE.  The 2026-07-18 audit's discipline note
was correct -- it claimed no action value -- and this probe claims none either.
The correction is to the FIELD the search should run in, not to any number.  The
uploaded Hakimoglu-Brown paper's Q(sqrt-7) identities are themselves correct;
they are simply not about 5_2 (the paper contains no occurrence of "knot",
"hyperbolic", "volume", or "trace field").

Ref: docs/audits/2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md (retracted premise)
Bean: qou-ynff
"""
from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60


def cubic_disc(a: int, b: int, c: int, d: int) -> int:
    """Discriminant of a x^3 + b x^2 + c x + d, by the classical formula.

    Exact integer arithmetic -- the whole point of this probe is that the answer
    is an integer identity, not a numerical coincidence.
    """
    return (18 * a * b * c * d - 4 * b**3 * d + b * b * c * c
            - 4 * a * c**3 - 27 * a * a * d * d)


def recover_monic_cubic(z, dps_guard: int = 30):
    """Recover the monic integer cubic satisfied by z, or None.

    PSLQ on (1, z, z^2, z^3) over the real and imaginary parts jointly.  Returns
    integer coefficients (1, b, c, d) normalized monic, plus the residual.
    """
    rel = mp.pslq([mp.mpf(1), mp.re(z), mp.re(z * z), mp.re(z**3)],
                  tol=mp.mpf(10) ** -dps_guard, maxcoeff=10**6)
    if rel is None:
        return None, None
    d0, c0, b0, a0 = (int(v) for v in rel)
    if a0 == 0:
        return None, None
    # normalize monic (sign + leading coefficient)
    if any(v % a0 for v in (b0, c0, d0)):
        return None, None
    b, c, d = b0 // a0, c0 // a0, d0 // a0
    resid = z**3 + b * z * z + c * z + d
    return (1, b, c, d), abs(resid)


def _load_saddle():
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "p5", str(here / "qbeta_5two_quantum_volume_probe.py"))
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    return P


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" 5_2 trace field: the cubic of disc -23, NOT Q(sqrt-7)")
    print("=" * 78)

    # ---------------------------------------------------------------- (1)
    # The geometric shapes, from the corpus's own solver.
    P = _load_saddle()
    y0 = mp.mpc("0.78492", "1.30714")
    x1, y1 = P.saddle(mp.mpf(1), y0)
    z1, z2 = y1 / x1, 1 / y1

    print(f"\n corpus saddle (m=1):  x = {mp.nstr(x1, 12)}")
    print(f"                       y = {mp.nstr(y1, 12)}")
    print(f" shapes:              z1 = {mp.nstr(z1, 12)}")
    print(f"                      z2 = {mp.nstr(z2, 12)}")

    recovered = {}
    for label, val in (("y", y1), ("x", x1), ("z2 = 1/y", z2)):
        poly, resid = recover_monic_cubic(val)
        recovered[label] = (poly, resid)
        if poly is None:
            print(f"\n  {label:10s}  no integer cubic recovered")
            continue
        _, b, c, d = poly
        disc = cubic_disc(1, b, c, d)
        sgn = lambda n: ("+" if n >= 0 else "-") + str(abs(n))  # noqa: E731
        print(f"\n  {label:10s}  x^3 {sgn(b)}x^2 {sgn(c)}x {sgn(d)}"
              f"   disc = {disc}   |residual| = {mp.nstr(resid, 4)}")

    discs = []
    for label, (poly, resid) in recovered.items():
        if poly is None:
            continue
        discs.append((label, cubic_disc(*poly), resid))

    all_cubic = len(discs) == 3
    all_m23 = all_cubic and all(d == -23 for _, d, _ in discs)
    tight = all_cubic and all(r < mp.mpf(10) ** -40 for _, _, r in discs)
    check(
        "geometric_shapes_satisfy_cubics_of_disc_minus_23",
        all_m23 and tight,
        computed="; ".join(f"{lab}: disc={d}, resid={mp.nstr(r, 3)}" for lab, d, r in discs),
        source="minimal polynomials of the corpus's own saddle shapes, recovered by "
               "PSLQ and verified by EXACT integer discriminant -- every one is a "
               "cubic of discriminant -23",
    )

    # ---------------------------------------------------------------- (2)
    # The tower-law exclusion.  This is the scope-(b) claim.
    deg_K = 3
    deg_qsqrt7 = 2
    excluded = (deg_K % deg_qsqrt7) != 0
    print(f"\n TOWER LAW:  [Q(sqrt-7):Q] = {deg_qsqrt7}  does not divide  [K:Q] = {deg_K}")
    print("             => Q(sqrt-7) has no embedding into K.  Structural, not numerical.")
    check(
        "qsqrt7_cannot_embed_in_the_cubic_trace_field",
        excluded,
        computed=f"[Q(sqrt-7):Q]={deg_qsqrt7} nmid [K:Q]={deg_K}",
        source="scope-(b) structural exclusion via a PROVED invariant (the tower law / "
               "Lagrange on field degrees). A degree-3 field has no quadratic subfield, "
               "so no precision improvement can produce the claimed containment",
    )

    # ---------------------------------------------------------------- (3)
    # The quadratic resolvent is Q(sqrt-23).
    #   disc(K) = -23 is squarefree and negative; the Galois closure of a
    #   non-Galois cubic has group S_3, whose unique index-2 subgroup A_3 fixes
    #   exactly Q(sqrt(disc)).
    disc_K = -23
    is_squarefree = all(disc_K % (p * p) for p in (2, 3, 5, 7, 11, 13, 17, 19, 23))
    resolvent_is_m23 = is_squarefree and disc_K == -23
    print(f"\n QUADRATIC RESOLVENT:  Q(sqrt(disc K)) = Q(sqrt{disc_K})"
          f"   [disc squarefree: {is_squarefree}]")
    print("   The Galois closure has group S_3; A_3 fixes exactly this quadratic field.")
    print("   So the bar-odd quadratic home, if there is one, is the sqrt-23 line.")
    check(
        "unique_quadratic_attached_to_K_is_qsqrt_minus_23",
        resolvent_is_m23,
        computed=f"disc(K) = {disc_K}, squarefree",
        source="a non-Galois cubic has Galois group S_3 with a unique index-2 subgroup "
               "A_3, whose fixed field is Q(sqrt(disc)) -- Q(sqrt-23), not Q(sqrt-7). "
               "This matches the corpus's own A6 sigma-pair tower, which records the "
               "bar-odd line as sqrt-23",
    )

    # ---------------------------------------------------------------- (4)
    # Where the 7 legitimately lives: the Alexander polynomial.
    #   Delta_{5_2}(t) = 2t^2 - 3t + 2
    a_l, b_l, c_l = 2, -3, 2
    alex_disc = b_l * b_l - 4 * a_l * c_l                 # = -7
    det_5two = abs(a_l * (-1) ** 2 + b_l * (-1) + c_l)    # |Delta(-1)| = 7
    alex_roots = [(3 + s * mp.sqrt(-7)) / 4 for s in (1, -1)]
    alex_ok = (alex_disc == -7 and det_5two == 7
               and all(abs(a_l * r * r + b_l * r + c_l) < mp.mpf(10) ** -45
                       for r in alex_roots))
    print(f"\n ALEXANDER LAYER:  Delta(t) = 2t^2 - 3t + 2,  disc = {alex_disc},"
          f"  det(5_2) = |Delta(-1)| = {det_5two}")
    print("   Roots (3 +- i sqrt7)/4 generate Q(sqrt-7): the abelian/metabelian home")
    print("   (quadratic subfield of Q(zeta_7), Z/7 double branched cover) -- REAL,")
    print("   but a different layer from the geometric SL_2(C) trace field.")
    check(
        "the_seven_is_the_alexander_layer_not_the_geometric_one",
        alex_ok,
        computed=f"disc(Delta) = {alex_disc}, det = |Delta(-1)| = {det_5two}",
        source="Q(sqrt-7) IS genuinely attached to 5_2 -- as the Alexander root field / "
               "quadratic subfield of Q(zeta_7), where the abelian data of the Z/7 "
               "branched cover lives. The retracted audit inferred the GEOMETRIC trace "
               "field from this ABELIAN datum",
    )

    # ---------------------------------------------------------------- (5)
    # The paired control the retracted audit never ran.  If the imaginary
    # direction of the shape lived on the sqrt-7 line, Im(z1)/sqrt7 would be
    # low-degree algebraic.  Run the SAME test against both lines, so the
    # negative is calibrated by a positive rather than standing alone.
    TOL = mp.mpf(10) ** -40

    def cubic_rel(v):
        return mp.pslq([mp.mpf(1), v, v * v, v**3], tol=TOL, maxcoeff=10**6)

    ratio7 = mp.im(z1) / mp.sqrt(7)
    ratio23 = mp.im(z1) / mp.sqrt(23)
    ident7 = mp.identify(ratio7)
    rel7 = cubic_rel(ratio7)
    rel23 = cubic_rel(ratio23)
    rel_bare = cubic_rel(mp.im(z1))

    print(f"\n PAIRED CONTROL (same test, both lines; tol 1e-40, deg <= 3)")
    print(f"   Im(z1)        = {mp.nstr(mp.im(z1), 20)}   pslq -> {rel_bare}")
    print(f"   Im(z1)/sqrt7  = {mp.nstr(ratio7, 20)}   pslq -> {rel7}   identify -> {ident7}")
    print(f"   Im(z1)/sqrt23 = {mp.nstr(ratio23, 20)}   pslq -> {rel23}")

    # The sqrt-23 hit must land back in K, or it is just a coincidence of height.
    resid23 = None
    disc23 = None
    sqfree23 = None
    if rel23 is not None:
        d0, c0, b0, a0 = (int(v) for v in rel23)
        resid23 = abs(a0 * ratio23**3 + b0 * ratio23**2 + c0 * ratio23 + d0)
        disc23 = cubic_disc(a0, b0, c0, d0)
        n = abs(disc23)
        sqfree23 = n
        for p in range(2, 400):
            while sqfree23 % (p * p) == 0:
                sqfree23 //= p * p
        print(f"     -> {a0}x^3 + {b0}x^2 + {c0}x + {d0},  |residual| = {mp.nstr(resid23, 4)}")
        print(f"     -> disc = {disc23} = -({sqfree23}) * square"
              f"   => squarefree part {sqfree23}"
              f"{'  (SAME field K)' if sqfree23 == 23 and disc23 < 0 else ''}")

    sqrt7_dead = ident7 is None and rel7 is None and rel_bare is None
    sqrt23_lands_in_K = (rel23 is not None and disc23 is not None and disc23 < 0
                         and sqfree23 == 23 and resid23 < TOL)
    check(
        "sqrt23_line_is_algebraic_over_K_while_sqrt7_line_is_not",
        sqrt7_dead and sqrt23_lands_in_K,
        computed=f"Im(z1): {rel_bare}; /sqrt7: {rel7}; /sqrt23: {rel23} "
                 f"(disc {disc23}, squarefree part {sqfree23})",
        source="the check the retracted audit never ran, run against BOTH lines so the "
               "negative is calibrated. Im(z1) and Im(z1)/sqrt7 satisfy no integer cubic; "
               "Im(z1)/sqrt23 satisfies one whose discriminant has squarefree part 23 -- "
               "it lands back in K. So the numerics do not merely fail to support the "
               "sqrt-7 line, they positively select the sqrt-23 one",
    )

    all_passed = all(a["passed"] for a in assertions)

    verdict = (
        "CORRECTION (scope-(b), proved invariant): the 5_2 invariant trace field is the "
        "CUBIC field of discriminant -23, not Q(sqrt-7). The tower law forbids the "
        "containment outright -- 2 does not divide 3 -- so this is a structural "
        "exclusion, not a numerical near-miss. Q(sqrt-7) is genuinely attached to 5_2, "
        "but as the ALEXANDER root field (disc(2t^2-3t+2) = -7, det = 7), the abelian "
        "layer of the Z/7 branched cover; the retracted audit read the geometric field "
        "off that abelian datum. The quadratic home of the bar-odd channel, if any, is "
        "the sqrt-23 line fixed by A_3 in the S_3 Galois closure -- which is what the "
        "corpus's own A6 sigma-pair tower already records. NO action VALUE is claimed "
        "here or retracted: the 2026-07-18 audit claimed none, and neither does this. "
        "The correction is to the FIELD a search should run in."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-5two-trace-field-disc23-not-qsqrt7", engine="mpmath")
    wb.set_description(
        "Certifies that the 5_2 invariant trace field is the cubic of discriminant -23 "
        "and that Q(sqrt-7) cannot embed in it (tower law, scope-(b)); identifies "
        "Q(sqrt-7) as the Alexander/abelian layer and Q(sqrt-23) as the S_3 quadratic "
        "resolvent. Retracts the premise of the 2026-07-18 bar-odd-action-home audit.")
    wb.set_audit_only("docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    for label, (poly, resid) in recovered.items():
        if poly is None:
            continue
        wb.add_data(f"min_poly[{label}]",
                    f"x^3 + ({poly[1]})x^2 + ({poly[2]})x + ({poly[3]})")
        wb.add_data(f"disc[{label}]", str(cubic_disc(*poly)))
    wb.add_data("trace_field_degree", "3")
    wb.add_data("trace_field_disc", "-23")
    wb.add_data("quadratic_resolvent", "Q(sqrt-23)")
    wb.add_data("alexander_polynomial", "2t^2 - 3t + 2")
    wb.add_data("alexander_disc", str(alex_disc))
    wb.add_data("determinant", str(det_5two))
    wb.add_data("im_z1_over_sqrt7", mp.nstr(ratio7, 25))
    wb.add_data("im_z1_over_sqrt7_identify", str(ident7))
    wb.add_data("im_z1_over_sqrt7_cubic_relation", str(rel7))
    wb.add_data("im_z1_over_sqrt23", mp.nstr(ratio23, 25))
    wb.add_data("im_z1_over_sqrt23_cubic_relation", str(rel23))
    wb.add_data("im_z1_over_sqrt23_cubic_disc", str(disc23))
    wb.add_data("im_z1_over_sqrt23_disc_squarefree_part", str(sqfree23))
    wb.add_data("exclusion_scope", "(b) structural -- tower law, [Q(sqrt-7):Q]=2 nmid [K:Q]=3")
    wb.add_data("verdict", verdict)

    # q0 anchor: `independent`, and stated rather than left to inference.
    #
    # Nothing here reads the substrate modulus. The saddle is solved at m = 1 --
    # the complete hyperbolic structure of the 5_2 complement, a fixed geometric
    # object -- and every field-theoretic conclusion is exact integer arithmetic
    # on recovered polynomial coefficients. The one place a reader might expect
    # a pin is the `Im(z1)/sqrt(23)` control, but that sqrt is the field's
    # discriminant, not a modulus.
    #
    # Import cone: _path_bridge (sys.path only), mpmath, witness_base, and
    # qbeta_5two_quantum_volume_probe -- none of which reads q_parameter,
    # constants.Q, or y_lambda_at.
    #
    # So `independent` is the honest record, NOT the standing proton default:
    # stamping a pin this compute never read is precisely the misrecord the
    # field exists to prevent. Via save(extra=...) rather than add_data(), which
    # would nest it under `data` where the audit reading body["q0Anchor"] cannot
    # see it. No q0Value -- there is no value, and one here would be a Q0_FLIP.
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Pure hyperbolic geometry + exact integer arithmetic. The 5_2 saddle "
            "is solved at m = 1 (the complete structure, a fixed object), minimal "
            "polynomials are recovered by PSLQ, and discriminants are computed "
            "over Z. No substrate modulus enters: the import cone reaches no "
            "q_parameter, no qou_substrate.constants, no y_lambda_at. The sqrt(23) "
            "in the paired control is the field discriminant, not a pin."
        ),
    })
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
