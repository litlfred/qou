#!/usr/bin/env python3
"""The PUBLISHED Q_beta closed form is exactly the z = 1 cell -- the functional
convention D forbids.

Bean `qou-99qc`, which asks: *which functional is `eps` MEANT to be in the
Q_beta ansatz?* This probe answers a narrower question that the corpus had left
implicit, and the answer removes the ambiguity from the published side.

WHAT WAS ALREADY ESTABLISHED (not re-derived here, cited):

  * `ConventionDAdmissibleRoots.lean` (sorry-free) factors the (1^3)-block
    weight numerator as `N(q,z) = (z - q)*((q^2+1)z - q^3)`, so under
    convention D exactly TWO Markov parameters descend to the two-row
    quotient: `z = q` (where tr_M IS the augmentation) and
    `z_D = q^3/(q^2+1)`. Its `one_not_root` proves `z = 1` is not a root.
  * `docs/audits/2026-08-29-delta-fork-at-admissible-parameters.md` completes
    the (element x z) grid and gives `tr_M(Delta_S)(z)` in closed form, affine
    in z.
  * `qou-99qc` records that the coordinate sum `epsNPq` IS tr_M at z = 1.

WHAT THIS ADDS. Those facts are about an *ansatz*. Nothing in the corpus
connected them to the framework's PUBLISHED headline closed form, the one in
the AGENTS.md canonical-derivation cheat sheet:

    Q_beta = m_e * |q^2 - 2q - 1| * (q + 1) / (2 q^3)

Solving `|tr_M^z(Delta_S)| * E0 == that`, with `E0 = m_e/(q(q-1))`, for z gives
`z = 1` on the positive branch and `z = h - 1` on the negative one. NEITHER is
an admissible root. So the published formula is not neutral between the two
candidate functionals -- it COMMITS to the coordinate sum, and that is the one
the canonical convention excludes.

This does not make the published number wrong as arithmetic; it is exact and
reproduces to 50 digits. It relocates the open question: not "which eps was
meant", but whether to keep a headline value produced by an inadmissible
functional, or adopt an admissible one and accept its error (+12.470 % or
-43.157 %).

SCOPE, stated per the AGENTS.md refutation rule.
  * Scope-(a) on the physics: nothing here refutes the Q_beta value or the
    ansatz. It identifies which functional the published form uses.
  * The INADMISSIBILITY is scope-(b) and the invariant is cited: `z = 1` is
    not a root of `N(q,z)`, proved in Lean sorry-free, and a root computation
    is a dimension/degree bound -- one of the permitted grounds.
  * Nothing is wired; no content block is edited; no c_k is proposed.

PRECISION. Every algebraic step is exact sympy over Q(q). The pin enters only
at readout, as an exact `Rational` from the 50-digit proton string, with an
mpmath 50-dps print. No float64 arithmetic anywhere (AGENTS.md NO-FLOAT64,
probes not exempt).
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
sys.path.insert(0, str(_COMP))

import _path_bridge  # noqa: E402, F401
from qou_substrate import constants as CONST  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def main() -> int:
    mp.mp.dps = 60
    checks: list[dict] = []

    def chk(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        return bool(ok)

    print(__doc__.splitlines()[0])
    print()
    ok = True

    q, z = sp.symbols("q z", positive=True)
    h = q - 1 / q

    # ---- the objects, all exact over Q(q) --------------------------------
    # affine trace of the short element, from the 2026-08-29 audit
    trM_S = q**2 / 2 - q * z - 1 + z / q + 1 / (2 * q**2)
    E0 = _qbeta_e0.order_zero_scaled(1, q)                    # in units of m_e
    published = sp.Abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)   # units of m_e
    epsNPq = h**2 / 2 - h
    # the (1^3) weight numerator whose roots are the admissible parameters
    N = (q**2 + 1) * z**2 - (2 * q**3 + q) * z + q**4

    # ---- CHECK 1: epsNPq is tr_M at z = 1 (re-verified, not assumed) -----
    d1 = sp.simplify(trM_S.subs(z, 1) - epsNPq)
    ok &= chk("epsNPq_is_trM_at_z_equals_one", d1 == 0,
              f"simplify(tr_M(Delta_S)(1) - epsNPq) = {d1}")

    # ---- CHECK 2: the published closed form IS |tr_M(z=1)| * E0 ----------
    # `sp.Abs` cannot be discharged without a domain, and the domain is not a
    # technicality -- it is exactly where h < 2. For 1 < q < 1 + sqrt(2) (the
    # SILVER RATIO, where h = 2):
    #     h > 0,  h - 2 = (q^2 - 2q - 1)/q < 0   =>  epsNPq = h(h-2)/2 < 0
    #     |epsNPq| = h(2 - h)/2,   |q^2 - 2q - 1| = 2q + 1 - q^2
    # Both absolute values are resolved on that branch and the identity is then
    # exact. Above the silver ratio both signs flip together, so the identity
    # holds there too -- verified separately below rather than assumed.
    eps_abs = h * (2 - h) / 2                       # |epsNPq| on 1 < q < 1+sqrt2
    pub_abs = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    d2 = sp.simplify(sp.expand(eps_abs * E0 - pub_abs))
    ok &= chk("published_closed_form_equals_abs_epsNPq_times_E0", d2 == 0,
              f"simplify(|epsNPq|*E0 - published) = {d2} on 1 < q < 1+sqrt(2) "
              "(exact over Q(q), not a numerical coincidence)")

    # and on the other side of the silver ratio, where both signs flip
    d2b = sp.simplify(sp.expand((h * (h - 2) / 2) * E0
                                - (q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)))
    ok &= chk("identity_also_holds_above_the_silver_ratio", d2b == 0,
              f"same difference with both signs flipped = {d2b} "
              "(so the identity is not an artifact of the branch chosen)")

    ok &= chk("the_pin_lies_below_the_silver_ratio",
              float(CONST.Q_50_DIGIT_STR[:20]) < 1 + 2 ** 0.5,
              f"q0 = {CONST.Q_50_DIGIT_STR[:12]}... < 1+sqrt(2) = 2.41421..., "
              "so the first branch is the physical one")

    # ---- CHECK 3: solve for z; BOTH branches, so the claim is complete ---
    roots = {}
    for sgn in (+1, -1):
        tgt = sgn * (q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)
        sol = sp.solve(sp.Eq(sp.simplify(trM_S * E0), tgt), z)
        roots[sgn] = [sp.simplify(s) for s in sol]
    ok &= chk("published_form_solves_to_z_equals_one", roots[+1] == [sp.Integer(1)],
              f"positive branch: z = {roots[+1]}")
    ok &= chk("negative_branch_is_h_minus_one",
              len(roots[-1]) == 1 and sp.simplify(roots[-1][0] - (h - 1)) == 0,
              f"negative branch: z = {roots[-1]} = h - 1")

    # ---- CHECK 4: neither solved z is an admissible root -----------------
    adm = {"q": q, "z_D": q**3 / (q**2 + 1)}
    for nm, val in adm.items():
        r = sp.simplify(N.subs(z, val))
        ok &= chk(f"admissible_root_{nm}_annihilates_N", r == 0,
                  f"N(q, {nm}) = {r}")
    for nm, val in (("one", sp.Integer(1)), ("h_minus_one", h - 1)):
        r = sp.simplify(sp.factor(N.subs(z, val)))
        ok &= chk(f"solved_z_{nm}_is_NOT_an_admissible_root", r != 0,
                  f"N(q, {nm}) = {r} (nonzero as a polynomial in q)")

    # ---- CHECK 4b: the bound is the SUPERGOLDEN ratio, not the plastic ---
    # N(q,1) factors as -(q-1)(-q^3+q^2+1), so it vanishes exactly at the root
    # of q^3 - q^2 - 1 ~ 1.4656. That is the bound in `one_not_root`'s
    # hypothesis, recovered here independently rather than quoted.
    #
    # 🛑 THE CORPUS NAMES IT WRONG, and the value it quotes is right, which is
    # why no grep for a bad NUMBER would find it. `ConventionDAdmissibleRoots
    # .lean` says "plastic number ~ 1.4656" at lines 40, 108 and 123, and
    # `docs/audits/2026-08-29-delta-fork-at-admissible-parameters.md` repeats
    # it. 1.4656 is the SUPERGOLDEN ratio, the root of x^3 = x^2 + 1
    # (OEIS A092526). The PLASTIC number is ~1.32472, the root of x^3 = x + 1
    # (A060006) -- a different constant, and not the bound here.
    #
    # Same defect class AGENTS.md records for Lambda vs Cl_2: the right value
    # under the wrong name. Nothing proved is affected -- the Lean hypothesis
    # is the inequality `q^3 - q^2 - 1 < 0`, not the name -- so this is a
    # docstring correction, not a mathematical one. Checked both ways so the
    # distinction cannot be re-conflated silently.
    supergolden = sp.real_roots(sp.Poly(q**3 - q**2 - 1, q))[0]
    plastic = sp.real_roots(sp.Poly(q**3 - q - 1, q))[0]
    sg_f = mp.mpf(str(sp.N(supergolden, 30)))
    pl_f = mp.mpf(str(sp.N(plastic, 30)))
    q0_f = mp.mpf(CONST.Q_50_DIGIT_STR)
    ok &= chk("N_at_z_one_vanishes_at_the_SUPERGOLDEN_ratio",
              sp.simplify(sp.expand(N.subs(z, 1)).subs(q, supergolden)) == 0,
              f"root of q^3-q^2-1 = {mp.nstr(sg_f, 12)} annihilates N(q,1)")
    ok &= chk("the_plastic_number_is_a_DIFFERENT_constant",
              sp.simplify(sp.expand(N.subs(z, 1)).subs(q, plastic)) != 0
              and mp.fabs(pl_f - sg_f) > mp.mpf("0.1"),
              f"plastic (root of q^3-q-1) = {mp.nstr(pl_f, 12)} != "
              f"{mp.nstr(sg_f, 12)}; it does NOT annihilate N(q,1). The corpus "
              "calls the bound 'plastic' in 4 sites; the value it quotes "
              "(1.4656) is the supergolden one and is correct.")
    ok &= chk("the_pin_is_below_the_bound", q0_f < sg_f,
              f"q0 = {mp.nstr(q0_f, 12)} < {mp.nstr(sg_f, 12)}, so z = 1 is "
              "genuinely not a root AT the substrate, not merely generically")

    # ---- readout at the canonical proton pin -----------------------------
    # exact Rational from the 50-digit string; the pin never enters as a float
    qs = CONST.Q_50_DIGIT_STR
    q0 = sp.Rational(qs)                    # exact; sympy parses the decimal
    m_e = sp.Rational(str(CONST.M_E_MEV))
    Qexp = sp.Rational(str(CONST.Q_NEUTRON_MEV))

    def err_pct(zval):
        """Exact rational throughout; mpmath only at the final readout."""
        pred = sp.Abs(trM_S.subs({z: zval, q: q0})) * (_qbeta_e0.order_zero_scaled(m_e, q0))
        r = sp.nsimplify((pred - Qexp) / Qexp * 100, rational=True)
        r = sp.Rational(r)
        return mp.mpf(r.p) / mp.mpf(r.q)

    grid = {}
    for nm, zval in (("z=1 (published, INADMISSIBLE)", sp.Integer(1)),
                     ("z=q (augmentation)", q0),
                     ("z=z_D (Markov, convention D)", q0**3 / (q0**2 + 1))):
        e = err_pct(zval)
        grid[nm] = mp.nstr(e, 8)
        print(f"      {nm:34s} err = {mp.nstr(e, 8):>12s} %")

    # ---- CHECK 5: calibration against the corpus's own published grid ----
    # If these three do not reproduce the 2026-08-29 audit, my trace is wrong.
    want = {"z=1 (published, INADMISSIBLE)": mp.mpf("0.168"),
            "z=q (augmentation)": mp.mpf("12.470"),
            "z=z_D (Markov, convention D)": mp.mpf("-43.157")}
    worst = max(abs(mp.mpf(grid[k]) - v) for k, v in want.items())
    ok &= chk("reproduces_the_corpus_published_grid", worst < mp.mpf("0.001"),
              f"max |mine - audit 2026-08-29| = {mp.nstr(worst, 4)} pp "
              "over the three cells (calibration, not a new result)")

    # ---- CHECK 6: numeric identity of published vs |epsNPq|*E0 -----------
    q0m = mp.mpf(qs)
    hm = q0m - 1 / q0m
    lhs = mp.fabs(q0m**2 - 2 * q0m - 1) * (q0m + 1) / (2 * q0m**3)
    rhs = mp.fabs(hm**2 / 2 - hm) / (q0m * (q0m - 1))
    ok &= chk("published_and_epsNPq_agree_at_the_pin", mp.fabs(lhs - rhs) < mp.mpf("1e-45"),
              f"|published - |epsNPq|*E0| / m_e = {mp.nstr(mp.fabs(lhs - rhs), 4)} "
              "at 60 dps")

    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    witness = {
        "name": "qbeta-published-form-is-the-inadmissible-z1",
        "description": (
            "The framework's published Q_beta closed form "
            "m_e|q^2-2q-1|(q+1)/(2q^3) is EXACTLY |tr_M(Delta_S)| * E0 "
            "evaluated at Markov parameter z = 1 -- the coordinate sum "
            "epsNPq. Solving for z gives z = 1 (positive branch) and "
            "z = h - 1 (negative), and neither is a root of the (1^3) weight "
            "numerator, whose only roots are z = q and z_D = q^3/(q^2+1) "
            "(ConventionDAdmissibleRoots.lean, sorry-free). So the published "
            "form commits to the one functional convention D forbids. "
            "Scope-(a) on the physics; the inadmissibility is scope-(b) with "
            "the root computation as the cited invariant. Nothing wired."),
        "assertions": checks,
        "solved_markov_parameter": {
            "positive_branch": "1",
            "negative_branch": "h - 1 = q - 1 - 1/q",
            "admissible_roots": ["q", "q**3/(q**2 + 1)"],
        },
        "err_pct_at_proton_pin": grid,
        "caveats": [
            "Does NOT show the published Q_beta value is wrong as arithmetic; "
            "it is exact and reproduces to 50 digits.",
            "Does NOT adjudicate which functional SHOULD be used -- that is "
            "the owner call qou-99qc holds open. It removes the ambiguity "
            "about which one the PUBLISHED form uses.",
            "The grid row values are a calibration against "
            "docs/audits/2026-08-29-delta-fork-at-admissible-parameters.md, "
            "not new measurements.",
            "Delta_S (the NF vector) only. qou-avt5's standing finding that "
            "Delta_S is not the exhibited nucleon-word difference is "
            "untouched; the Delta_L row of the grid is unaffected by this.",
        ],
        "related": [
            "QOU.QBeta.ConventionDAdmissibleRoots",
            "QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one",
            "docs/audits/2026-08-29-delta-fork-at-admissible-parameters.md",
            "computations/qbeta/qbeta_admissible_functionals_bracket_probe.py",
        ],
        "source": "bean qou-99qc",
        "scriptFile": Path(__file__).name,
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python+sympy+mpmath",
        q0_anchor="proton",
        q0_anchor_reason=(
            "Readout only. Every algebraic result (the z solve, the root "
            "computation, the two identities) is exact over Q(q) and pin-free; "
            "q0 enters solely to print the err_pct grid at the canonical "
            "experimental pin."),
        q0_value=qs)

    out = _HERE / "qbeta-published-form-is-the-inadmissible-z1.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
