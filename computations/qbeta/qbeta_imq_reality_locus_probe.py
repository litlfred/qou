#!/usr/bin/env python3
"""Where can Q_beta be real with Im(q) != 0?  Not on the substrate branch --
under EITHER complex extension of the closed form.

WHAT WAS ASKED
--------------
Bean `qou-c66b`, on the author's instruction to chip away at where the
imaginarity comes from (`conj:im-q-physical-role`).  That bean established
that `Q_beta` is Im(q)-SENSITIVE -- unlike the mass formula, whose `|tr_M|`
covers the whole expression -- and then asserted, without proof:

    "Q_beta is experimentally a real Q-value in MeV.  Requiring Im Q_beta = 0
     therefore forces Im q = 0."

That assertion is TOO STRONG as written, and this probe is the correction.
`Im Q_beta = 0` is one real equation on two real unknowns, so its solution set
is a CURVE, not the single point `Im q = 0`.  The real question is whether the
curve's non-real branch passes through the substrate.  It does not -- and that
is what makes the conclusion survive.

`qou-c66b` also flags, correctly and load-bearingly, that the complex
extension of `Q_beta` is the agent's and not the corpus's: the closed form was
derived for real `q`, where the `|.|` is a sign fix.  So this probe does not
pick one extension.  It runs BOTH readings that the corpus's own text
supports, and reports where they agree and where they do not.

THE TWO EXTENSIONS
------------------
E1 -- the PRINTED closed form, which is also the live code
(`qbeta_utils.py:293`, and `neutron-qvalue-symbolic.md`):

    Q_A(q) = m_e * |q^2 - 2q - 1| * (q + 1) / (2 q^3)

E2 -- the DERIVATION the same block gives one line above it, before the
real-q simplification:

    Q_beta = |Delta(net)| * E_0,
    Delta(net) = h(h-2)/2,  h = q - 1/q,  E_0 = m_e / (q(q-1))

E1 is E2 simplified USING `q` real and `q > 1`: only then is
`(q^2-1) = (q-1)(q+1)` positive and pullable out of the modulus.  Extending
E1 past that assumption is therefore extending a formula past the hypothesis
that produced it -- exactly the shape AGENTS.md's "defined residual is not a
derived decomposition" section warns about, one construction over.  Hence
both are run.

RESULT
------
Both reduce to the same shape -- a real non-negative modulus factor times an
unprojected rational function -- so `Im Q_beta = 0` reduces to that rational
function being real.  With `q = x + iy`:

    E1:  Im[(q+1)/q^3] = 0   <=>   y * [ 2x(x^2+y^2) + 3x^2 - y^2 ] = 0
    E2:  Im[1/(q(q-1))] = 0  <=>   y * (2x - 1) = 0

So each has the trivial branch `y = 0` and one non-real branch:

    E1 non-real branch:  y^2 = -x^2 (2x+3) / (2x-1),  real only for -3/2 < x < 1/2
    E2 non-real branch:  x = 1/2 exactly

**The substrate is in neither.**  `Re q = q_0 ~ 1.10998 > 1/2`, so E1's strip
excludes it and E2's line misses it.  On the substrate branch, `Im Q_beta = 0`
forces `Im q = 0` under both readings.

STRONGER, AND IT ANSWERS CANDIDATE (ii) AS LITERALLY POSED
-----------------------------------------------------------
"On the substrate branch" understates it.  Candidate (ii) does not ask about a
point; it posits that CAL-2 alone leaves an APOLLONIUS CIRCLE of admissible
complex `q`, with `Im q` as "the arc coordinate parametrizing the other
admissible q values", and asks whether a second constraint picks a complex one.

Reading CAL-2 with a modulus -- which is what produces a circle at all --
`|hbar_q| = sqrt(k)`, `hbar_q = 1 - 1/q`, `k = Vol(4_1)/(m_mu/m_e)`, gives
`|q-1| = sqrt(k)|q|`: the Apollonius circle with

    centre = 1/(1-k),   radius = sqrt(k)/(1-k)

This probe derives those from the live CODATA-2022 muon ratio and gets
**centre 1.0099145, radius 0.1000641**, reproducing the conjecture's own stated
"centre ~ 1.010, radius ~ 0.100".  So the reading is the conjecture's reading,
not a guess at it.

Its leftmost point is `Re q = 0.909850`, a margin of **0.410 above 1/2**.  The
ENTIRE admissible set therefore lies in the half-plane where both branches are
empty, so `Im Q_beta = 0` kills every non-real point of the circle and leaves
exactly its two real intersections, `0.9098504` and `1.1099785956`.

(The second is the live CODATA-2022 muon `q_0` to every digit shown, as it must
be -- the circle is built from that ratio.  The proton pin sits 1.046e-8 off the
circle in the `|q-1|/|q|` residual, which is the mu-p substrate tension seen in
this coordinate.)

WHY RUNNING BOTH IS THE POINT
-----------------------------
The two loci are DISJOINT: E1's is an open strip `-3/2 < x < 1/2`, E2's is the
single line `x = 1/2` bounding it.  So the extensions disagree about where
imaginarity is admissible *everywhere except on the answer that matters* --
which both corroborates `qou-c66b`'s caveat (the extension choice is genuinely
unfixed and it genuinely changes the answer) and shows the substrate
conclusion does not depend on resolving it.

WHAT THIS CLOSES, AND WHAT IT DOES NOT
--------------------------------------
`conj:im-q-physical-role` candidate (ii) asks whether "another CAL-2-like
independent constraint fixes a unique complex q_0", and states: "If only real
solutions exist, candidate (ii) is closed."  `Q_beta` IS such a constraint --
it is the CAL-2 proxy's partner, `Q_beta = hbar / D_beta` -- and it is already
in the framework in closed form.  On the substrate branch it admits only real
solutions.  Scope (b): a proved algebraic identity forbids the alternative,
not a numerical near-miss.

It does NOT touch candidate (i), chirality.  It does not show `Im q` is
unphysical at the FIBRE level, where `AGENTS.md`'s fibre-vs-observable banner
explicitly leaves `Im(q)` unconstrained; it constrains the ARCHIMEDEAN
evaluation only, which is what `lusztig_q_0_imaginary_part_zero` already
asserts from a different direction.  What is new is that the constraint now
follows from a DECAY observable the framework already has, rather than being
an assumption -- which also corrects candidate (iii)'s stated obstacle ("needs
a categorical formula for decay widths Gamma").

PRECISION.  The algebra is exact sympy over `ZZ[x,y]`; no float enters it.
The spot-checks are mpmath at 50 dps carried from the 50-digit q_0 string.
No float64 anywhere, per AGENTS.md "PROBES ARE NOT EXEMPT".
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]

mp.mp.dps = 50

x, y = sp.symbols("x y", real=True)
q = x + sp.I * y

# The 50-digit PROTON pin (AGENTS.md: proton is the default for all new compute).
Q0_STR = "1.1099785827513808075916690956107688798744991218736"


def im_condition(expr):
    """Exact Im(expr) as a polynomial/rational in (x, y), factored."""
    return sp.factor(sp.simplify(sp.im(sp.expand(expr).rewrite(sp.re))))


def main() -> int:
    print("=" * 78)
    print(" Q_beta real with Im(q) != 0 -- where?  (bean qou-c66b, conj:im-q-physical-role)")
    print("=" * 78)

    # ---- [1] the two extensions, stripped of their real non-negative factors ----
    # Both are (real >= 0 modulus factor) * (unprojected rational function).
    # Im(Q_beta) = 0  <=>  the rational function is real (or the modulus factor is 0).
    g1 = (q + 1) / (2 * q**3)          # E1: printed closed form
    g2 = _qbeta_e0.order_zero_scaled(1, q)             # E2: E_0 / m_e, from the derivation

    im1 = sp.factor(sp.simplify(sp.im(sp.expand(sp.simplify(sp.expand(g1))))))
    im2 = sp.factor(sp.simplify(sp.im(sp.expand(sp.simplify(sp.expand(g2))))))

    print("\n[1] Im of the UNPROJECTED factor, exactly (q = x + iy)")
    print(f"    E1  Im[(q+1)/(2q^3)]  = {im1}")
    print(f"    E2  Im[1/(q(q-1))]    = {im2}")

    # Numerators carry the zero set; denominators are |q|^{2k} > 0.
    n1 = sp.factor(sp.numer(sp.cancel(im1)))
    n2 = sp.factor(sp.numer(sp.cancel(im2)))
    print(f"\n    E1 numerator (the zero set) = {n1}")
    print(f"    E2 numerator (the zero set) = {n2}")

    # ---- [2] both factor as y * (branch) ----
    b1 = sp.factor(sp.cancel(n1 / y))
    b2 = sp.factor(sp.cancel(n2 / y))
    y_divides_1 = sp.simplify(n1 - y * b1) == 0
    y_divides_2 = sp.simplify(n2 - y * b2) == 0
    print("\n[2] each zero set is  y * (non-real branch)")
    print(f"    E1: y * ({b1})     y divides exactly: {y_divides_1}")
    print(f"    E2: y * ({b2})     y divides exactly: {y_divides_2}")

    # ---- [3] solve the non-real branch for y^2 as a function of x ----
    y2_1 = sp.simplify(sp.solve(sp.Eq(b1, 0), y**2)[0])
    print("\n[3] the non-real branch, solved")
    print(f"    E1: y^2 = {sp.factor(y2_1)}   (needs y^2 > 0)")
    print(f"    E2: {sp.solve(sp.Eq(b2, 0), x)}  -- a vertical line, y free")

    # E1 admissible x-interval: y^2 > 0
    ivl = sp.solve_univariate_inequality(y2_1 > 0, x, relational=False)
    print(f"    E1 admissible Re(q): {ivl}")

    # ---- [4] is the substrate in either locus? ----
    q0 = mp.mpf(Q0_STR)
    x0 = sp.Rational(str(q0)[:30].rstrip("0") or "0")   # exact rational proxy for the test
    y2_at_q0 = sp.simplify(y2_1.subs(x, x0))
    e1_hit = bool(y2_at_q0 > 0)
    e2_hit = bool(sp.simplify(x0 - sp.Rational(1, 2)) == 0)
    print("\n[4] the substrate branch,  Re(q) = q_0")
    print(f"    q_0 (50 dps)        = {mp.nstr(q0, 30)}")
    print(f"    E1  y^2 at q_0      = {sp.nsimplify(y2_at_q0, rational=True)}"
          f"  ->  {'IN locus' if e1_hit else 'y^2 < 0, NOT in locus'}")
    print(f"    E2  q_0 == 1/2      = {e2_hit}  ->  {'IN locus' if e2_hit else 'NOT in locus'}")

    # ---- [5] the two loci are disjoint ----
    disjoint = not bool(y2_1.subs(x, sp.Rational(1, 2)).is_positive)
    print("\n[5] do the two extensions agree about WHERE imaginarity is allowed?")
    print(f"    E1 strip = {ivl}   (open, excludes 1/2)")
    print("    E2 line  = {1/2}")
    print(f"    disjoint = {disjoint}  -> they agree only on excluding the substrate")

    # ---- [6] the modulus factor's own zeros are real ----
    quad_roots = sp.solve(sp.Eq(sp.Symbol("t") ** 2 - 2 * sp.Symbol("t") - 1, 0), sp.Symbol("t"))
    all_real = all(r.is_real for r in quad_roots)
    print("\n[6] the other way Im(Q_beta) can vanish: the modulus factor is 0")
    print(f"    q^2 - 2q - 1 = 0 at q = {quad_roots}")
    print(f"    all real: {all_real}  -> supplies no complex solution either")

    # ---- [7] mpmath spot-check at 50 dps: Im(Q_beta) on and off the loci ----
    def qb_e1(qc):
        return abs(qc**2 - 2 * qc - 1) * (qc + 1) / (2 * qc**3)

    def qb_e2(qc):
        h = qc - 1 / qc
        return abs(h * (h - 2) / 2) / (qc * (qc - 1))

    checks = []
    for label, qc in [
        ("substrate, Im q = 0", mp.mpc(q0, 0)),
        ("substrate, Im q = 1e-6", mp.mpc(q0, mp.mpf("1e-6"))),
        ("substrate, Im q = 1e-3", mp.mpc(q0, mp.mpf("1e-3"))),
        ("E2 locus x = 1/2, Im q = 0.3", mp.mpc(mp.mpf("0.5"), mp.mpf("0.3"))),
    ]:
        checks.append({
            "case": label,
            "q": mp.nstr(qc, 20),
            "Im_QA_over_me_E1": mp.nstr(mp.im(qb_e1(qc)), 20),
            "Im_QA_over_me_E2": mp.nstr(mp.im(qb_e2(qc)), 20),
        })
    print("\n[7] mpmath spot-check, 50 dps  (Q_beta/m_e imaginary part)")
    for c in checks:
        print(f"    {c['case']:32s} E1 {c['Im_QA_over_me_E1']:>26s}   E2 {c['Im_QA_over_me_E2']:>26s}")

    e2_locus_row = checks[-1]
    e2_vanishes_on_its_locus = mp.almosteq(
        mp.mpf(e2_locus_row["Im_QA_over_me_E2"]), 0, abs_eps=mp.mpf("1e-40"))
    e1_nonzero_off_locus = not mp.almosteq(
        mp.mpf(checks[2]["Im_QA_over_me_E1"]), 0, abs_eps=mp.mpf("1e-20"))

    # ---- [8] candidate (ii)'s ENTIRE admissible set, not just the substrate ----
    # CAL-2 read with a modulus: |1 - 1/q| = sqrt(k), k = Vol(4_1)/(m_mu/m_e).
    # Equivalently |q-1| = sqrt(k)|q| -- an Apollonius circle.
    vol41 = 2 * mp.clsin(2, mp.pi / 3)
    ratio_mu_e = mp.mpf("206.7682827")            # CODATA 2022, the live muon ratio
    kk = vol41 / ratio_mu_e
    centre = 1 / (1 - kk)
    radius = mp.sqrt(kk) / (1 - kk)
    leftmost = centre - radius
    circle_in_half_plane = bool(leftmost > mp.mpf("0.5"))
    q0m = mp.mpf(Q0_STR)
    off_circle = abs(q0m - 1) / abs(q0m) - mp.sqrt(kk)
    print("\n[8] candidate (ii)'s admissible set: the CAL-2 Apollonius circle")
    print(f"    Vol(4_1)             = {mp.nstr(vol41, 25)}")
    print(f"    k = Vol/(m_mu/m_e)   = {mp.nstr(kk, 25)}")
    print(f"    centre = 1/(1-k)     = {mp.nstr(centre, 20)}   (conjecture: ~1.010)")
    print(f"    radius = sqrt(k)/(1-k) = {mp.nstr(radius, 20)}   (conjecture: ~0.100)")
    print(f"    leftmost Re(q)       = {mp.nstr(leftmost, 20)}"
          f"   margin above 1/2 = {mp.nstr(leftmost - mp.mpf('0.5'), 12)}")
    print(f"    real intersections   = {mp.nstr(leftmost, 20)}, {mp.nstr(centre + radius, 20)}")
    print(f"    proton pin off circle= {mp.nstr(off_circle, 10)}  (the mu-p tension in this coordinate)")
    print(f"    ENTIRE circle in Re(q) > 1/2: {circle_in_half_plane}")

    # ---- assertions ----
    assertions = [
        {"name": "E1_zero_set_factors_as_y_times_branch",
         "passed": bool(y_divides_1),
         "detail": f"Im[(q+1)/(2q^3)] numerator = y*({b1}) exactly"},
        {"name": "E2_zero_set_factors_as_y_times_branch",
         "passed": bool(y_divides_2),
         "detail": f"Im[1/(q(q-1))] numerator = y*({b2}) exactly"},
        {"name": "substrate_not_in_E1_non_real_branch",
         "passed": not e1_hit,
         "detail": f"E1 needs Re(q) in {ivl}; q_0 = 1.10998 > 1/2, so y^2 < 0"},
        {"name": "substrate_not_in_E2_non_real_branch",
         "passed": not e2_hit,
         "detail": "E2 needs Re(q) = 1/2 exactly; q_0 = 1.10998"},
        {"name": "modulus_factor_zeros_are_real",
         "passed": bool(all_real),
         "detail": f"q^2-2q-1 = 0 at {quad_roots}, both real -- no complex escape"},
        {"name": "the_two_extensions_disagree_off_the_substrate",
         "passed": bool(disjoint),
         "detail": "E1's open strip and E2's line x=1/2 are disjoint; they agree "
                   "only that the substrate is excluded -- which is why the "
                   "conclusion survives qou-c66b's unresolved extension choice"},
        {"name": "numeric_control_E2_vanishes_on_its_own_locus",
         "passed": bool(e2_vanishes_on_its_locus),
         "detail": "at q = 1/2 + 0.3i, Im(Q_beta) under E2 is 0 to 1e-40 -- the "
                   "test can see a real Q_beta at complex q when there is one"},
        {"name": "apollonius_circle_reproduces_the_conjectures_own_numbers",
         "passed": bool(abs(centre - mp.mpf("1.010")) < mp.mpf("0.001")
                        and abs(radius - mp.mpf("0.100")) < mp.mpf("0.001")),
         "detail": f"derived centre {mp.nstr(centre, 12)} / radius {mp.nstr(radius, 12)} "
                   f"against the conjecture's stated ~1.010 / ~0.100 -- so the "
                   f"modulus reading of CAL-2 used here IS the conjecture's reading"},
        {"name": "entire_cal2_admissible_set_lies_in_Re_q_gt_half",
         "passed": circle_in_half_plane,
         "detail": f"leftmost point of the circle is Re(q) = {mp.nstr(leftmost, 12)}, "
                   f"a margin of {mp.nstr(leftmost - mp.mpf('0.5'), 8)} above 1/2 -- so "
                   f"both branches are empty on the WHOLE arc, not merely near q_0, "
                   f"and candidate (ii)'s test is answered on its entire admissible set"},
        {"name": "numeric_control_E1_nonzero_off_its_locus",
         "passed": bool(e1_nonzero_off_locus),
         "detail": "at q = q_0 + 1e-3 i, Im(Q_beta) under E1 is not 0 -- the test "
                   "can see a non-real Q_beta too"},
    ]
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
        print(f"           {a['detail']}")
    ok = all(a["passed"] for a in assertions)
    print(f"\n  allPassed: {ok}  ({sum(a['passed'] for a in assertions)}/{len(assertions)})")

    out = HERE / "qbeta-imq-reality-locus.witness.json"
    w = {
        "description": "Where can Q_beta be real with Im(q) != 0? Under BOTH complex "
                       "extensions of the closed form the solution set is y=0 plus one "
                       "non-real branch, and the substrate Re(q)=q_0 lies in neither "
                       "branch -- so on the substrate, Im(Q_beta)=0 forces Im(q)=0. "
                       "Corrects bean qou-c66b's stronger unqualified claim, and closes "
                       "conj:im-q-physical-role candidate (ii) using an observable the "
                       "framework already has -- and not merely at q_0: the CAL-2 "
                       "Apollonius circle that candidate (ii) posits as its admissible "
                       "set lies ENTIRELY in Re(q) > 1/2 (leftmost 0.909850, margin "
                       "0.410), so every non-real point of the arc is excluded and only "
                       "its two real intersections survive.",
        "engine": "sympy (exact symbolic over ZZ[x,y]) + mpmath 50 dps spot-checks; no float64",
        "q0Anchor": "proton",
        "q0AnchorReason": "AGENTS.md 2026-08-07 owner directive: proton is the default "
                          "for all new compute; this probe is neither an explicit "
                          "proton-vs-muon comparison (E1) nor an ideal-CAL statement (E2)",
        "q0Value": Q0_STR,
        "data": {
            "E1_form": "m_e * |q^2 - 2q - 1| * (q + 1) / (2 q^3)   [printed closed form, qbeta_utils.py:293]",
            "E2_form": "|Delta(net)| * E_0,  Delta(net) = h(h-2)/2, h = q - 1/q, E_0 = m_e/(q(q-1))",
            "E1_im_numerator": str(n1),
            "E2_im_numerator": str(n2),
            "E1_non_real_branch_y_squared": str(sp.factor(y2_1)),
            "E1_admissible_Re_q": str(ivl),
            "E2_non_real_branch": "Re(q) = 1/2 exactly, Im(q) free",
            "substrate_in_E1_branch": bool(e1_hit),
            "substrate_in_E2_branch": bool(e2_hit),
            "loci_disjoint": bool(disjoint),
            "modulus_factor_roots": [str(r) for r in quad_roots],
            "spot_checks": checks,
            "cal2_apollonius_circle": {
                "reading": "CAL-2 with a modulus, |1 - 1/q| = sqrt(k), which is what "
                           "produces a circle at all; k = Vol(4_1)/(m_mu/m_e)",
                "Vol_4_1": mp.nstr(vol41, 30),
                "m_mu_over_m_e": "206.7682827 (CODATA 2022)",
                "k": mp.nstr(kk, 30),
                "centre": mp.nstr(centre, 25),
                "radius": mp.nstr(radius, 25),
                "conjecture_states": "centre ~1.010, radius ~0.100",
                "leftmost_Re_q": mp.nstr(leftmost, 25),
                "margin_above_one_half": mp.nstr(leftmost - mp.mpf("0.5"), 20),
                "real_intersections": [mp.nstr(leftmost, 25), mp.nstr(centre + radius, 25)],
                "proton_pin_off_circle_residual": mp.nstr(off_circle, 12),
                "entire_circle_in_substrate_half_plane": circle_in_half_plane,
            },
            "scope": "(b) -- structural exclusion citing a proved algebraic identity "
                     "(the exact factorisation of Im, and the sign of y^2 on the "
                     "substrate branch), not a numerical near-miss. Scoped to the "
                     "ARCHIMEDEAN evaluation; AGENTS.md's fibre-vs-observable banner "
                     "leaves Im(q) unconstrained at the fibre level and this does not "
                     "touch that.",
            "does_not_close": "candidate (i), chirality. Nor does it fix WHICH complex "
                              "extension is canonical -- it shows the substrate answer "
                              "does not depend on that choice.",
            "corrects": "bean qou-c66b asserted 'Requiring Im Q_beta = 0 therefore "
                        "forces Im q = 0' without qualification. One real equation on "
                        "two real unknowns has a curve of solutions, not a point; the "
                        "non-real branch is non-empty under both readings. The claim "
                        "holds on the substrate branch Re(q) > 1/2, and that is where "
                        "it needed to hold.",
        },
        "assertions": assertions,
        "allPassed": ok,
    }
    out.write_text(json.dumps(w, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
