#!/usr/bin/env python3
"""binding_functional_extensivity_probe.py — the binding functional IS derived,
the 2026-08-25 audit's grep missed it, and its figure is convention-C frame.

THE CORPUS-STATE CORRECTION.  `docs/audits/2026-08-25-deuteron-attack-c-convergence.md`
runs a five-path corpus-grep for a derivation of `B = -alpha*ln|tr_M|` and concludes:

    "So B = -alpha*ln|tr_M| is posited.  Scope (a) -- it is not derived *in this
     corpus*."

its table recording, for the first path searched:

    | docs/audits/ | files that **use** the form; none derives it |

**That is wrong.**  `docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
carries a section whose heading is literally

    ## 10a. The functional is DERIVED, not chosen -- and it is the log form

dated **seventeen days earlier**, in `docs/audits/` -- the very path the table
reports as containing no derivation.  Its argument: `tr_M` is multiplicative over
independent subsystems (`tr_atom = tr_free * PROD mu_k`, measured there to
1.2e-31), energy is extensive, so the trace-to-energy map obeys Cauchy's
`f(xy) = f(x) + f(y)` on `(R_+, x)` and the log form is forced.

The `qou-d5e8` bean repeats the "posited" verdict, and
`ursell_alternation_sign_identity_probe.py` had already cited 10a as a derivation
-- so the corpus disagreed with itself in three places.

WHAT THIS PROBE ESTABLISHES, and it is deliberately narrow:

 1. **10a's extensivity comparison, exactly.**  The log form is extensive; the
    linear rival is not; and the defect has a CLOSED FORM,

        a(1-xy) - [a(1-x) + a(1-y)]  =  -a(1-x)(1-y)

    which 10a reports only as a measured number.  Now Lean:
    `QOU.QBeta.InterfaceScalar.linearForm_extensivity_defect` (sorry-free, an
    identity, so no positivity hypothesis and no anchor).

 2. **10a's number is convention-C frame.**  The audit predates the 2026-08-09
    convention-D excision by one day.  With `mu_pp = z`, `mu_nn = z - h` at the
    proton pin:

        convention C   z = sqrt(q)/(q+1)   defect = 1.487498   <- the audit's 1.4875
        convention D   z = q^3/(q^2+1)     defect = 0.966887

    The conclusion survives in both -- the closed form vanishes only at `x = 1`
    or `y = 1` -- but the figure needs its scope, exactly as the c_k ladder does.

 3. **The linear form's ceiling is convention-INDEPENDENT.**  `t_atom > 0` gives
    `B_lin < alpha * t_free` outright, so with `t_free ~ 1` the linear form cannot
    reach `B_AME` at 3H (8.48), 4He (28.30) or 7Li (39.24) under any convention.
    A second, independent reason to reject it.
    Lean: `linearForm_ceiling`.

WHAT IS STILL NOT FORMALISED.  The uniqueness step -- that the only continuous
solutions of Cauchy's equation are `c*log x` -- is classical and is NOT in Lean
here.  So "forced" continues to rest on it, and the Lean section says so.  What
IS mechanically checked is the comparison the corpus actually runs.

Run:  python3 -u computations/probes/binding_functional_extensivity_probe.py \
        2>&1 | tee /tmp/binding_functional_extensivity.log
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

LEAN_DECLS = (
    "QOU.QBeta.InterfaceScalar.logForm_extensive",
    "QOU.QBeta.InterfaceScalar.linearForm_extensivity_defect",
    "QOU.QBeta.InterfaceScalar.linearForm_not_extensive",
    "QOU.QBeta.InterfaceScalar.linearForm_ceiling",
)

# The audit's own figure, and the AME bindings its ceiling table uses.
AUDIT_QUOTED_LINEAR_DEFECT = "1.4875"
B_AME = {"2H": "2.224566", "3H": "8.481798", "4He": "28.295673", "7Li": "39.244524"}


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - mp.mpf(1) / q
    alpha = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    z_C = mp.sqrt(q) / (q + 1)
    z_D = q ** 3 / (q ** 2 + 1)

    print("=" * 82)
    print("the binding functional: extensivity, and which convention 10a's number is")
    print("=" * 82)
    print(f"\n  q_0 (proton) = {mp.nstr(q, 40)}")
    print(f"  alpha        = {mp.nstr(alpha, 16)} MeV")

    def log_defect(x, y):
        return (-alpha * mp.log(x * y)) - ((-alpha * mp.log(x)) + (-alpha * mp.log(y)))

    def lin_defect(x, y):
        return (alpha * (1 - x * y)) - ((alpha * (1 - x)) + (alpha * (1 - y)))

    def closed(x, y):
        return -(alpha * ((1 - x) * (1 - y)))

    rows = {}
    print(f"\n  {'convention':<14}{'z':>20}{'log defect':>16}{'lin defect':>18}"
          f"{'closed form':>18}")
    for name, z in (("C", z_C), ("D", z_D)):
        x, y = z, z - h
        ld, nd, cf = log_defect(x, y), lin_defect(x, y), closed(x, y)
        rows[name] = {
            "z": mp.nstr(z, 40), "mu_pp": mp.nstr(x, 40), "mu_nn": mp.nstr(y, 40),
            "log_form_defect": mp.nstr(ld, 20),
            "linear_form_defect": mp.nstr(nd, 30),
            "closed_form": mp.nstr(cf, 30),
        }
        print(f"  {name:<14}{mp.nstr(z, 14):>20}{mp.nstr(abs(ld), 6):>16}"
              f"{mp.nstr(nd, 12):>18}{mp.nstr(cf, 12):>18}")

    quoted = mp.mpf(AUDIT_QUOTED_LINEAR_DEFECT)
    matchC = abs(abs(mp.mpf(rows["C"]["linear_form_defect"])) - quoted)
    matchD = abs(abs(mp.mpf(rows["D"]["linear_form_defect"])) - quoted)
    print(f"\n  10a quotes {AUDIT_QUOTED_LINEAR_DEFECT}: |C - quoted| = {mp.nstr(matchC, 6)}"
          f"   |D - quoted| = {mp.nstr(matchD, 6)}")
    print(f"  -> the audit's figure is CONVENTION-C frame")

    # The ceiling, convention-independent.
    print(f"\n  linear-form ceiling  B_lin < alpha * t_free, with t_free ~ 1:")
    ceiling = alpha
    over = []
    for atom, b in B_AME.items():
        bv = mp.mpf(b)
        flag = "EXCEEDS" if bv > ceiling else "under"
        if bv > ceiling:
            over.append(atom)
        print(f"    {atom:<5} B_AME = {mp.nstr(bv, 10):>14}   vs ceiling "
              f"{mp.nstr(ceiling, 8)}   {flag}")

    w = WitnessBuilder("binding-functional-extensivity", engine="python")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("alpha_MeV", mp.nstr(alpha, 30))
    w.add_data("lean_declarations", list(LEAN_DECLS))
    w.add_data("by_convention", rows)
    w.add_data("audit_10a_quoted_linear_defect", AUDIT_QUOTED_LINEAR_DEFECT)
    w.add_data("audit_10a_figure_is_convention", "C")
    w.add_data("atoms_exceeding_linear_ceiling", over)
    w.add_data("derivation_location",
               "docs/audits/2026-08-08-binding-functional-attack-vectors-"
               "and-li2q-guard.md 10a")
    w.add_data("audit_that_missed_it",
               "docs/audits/2026-08-25-deuteron-attack-c-convergence.md")

    w.add_assertion(
        "the log form is extensive (defect exactly zero, convention D)",
        computed=mp.nstr(abs(mp.mpf(rows["D"]["log_form_defect"])), 30),
        expected="0", tolerance="1e-40",
        source="-alpha ln(xy) vs -alpha ln x + -alpha ln y at mu_pp, mu_nn",
    )
    w.add_assertion(
        "the linear form's defect equals the closed form -alpha(1-x)(1-y)",
        computed=mp.nstr(abs(mp.mpf(rows["D"]["linear_form_defect"])
                             - mp.mpf(rows["D"]["closed_form"])), 30),
        expected="0", tolerance="1e-40",
        source="Lean linearForm_extensivity_defect, checked numerically",
    )
    w.add_assertion(
        "10a's quoted 1.4875 is the CONVENTION-C value, not convention D",
        computed=mp.nstr(matchC, 30), expected="0", tolerance="1e-4",
        source=f"convention D gives {rows['D']['linear_form_defect'][:12]}, "
               f"|D - quoted| = {mp.nstr(matchD, 6)}",
    )
    w.add_assertion(
        "three of the four AME atoms exceed the linear form's ceiling",
        computed=str(len(over)), expected="3", tolerance="0",
        source=f"ceiling alpha = {mp.nstr(alpha, 10)} MeV with t_free ~ 1; "
               f"exceeded by {', '.join(over)}",
    )

    w.add_caveat(
        "The uniqueness step of 10a -- that the only continuous solutions of "
        "Cauchy's equation f(xy) = f(x) + f(y) are c*log x -- is classical and is "
        "NOT formalised in this corpus. 'The log form is forced' still rests on "
        "it. What is proved in Lean is the comparison the corpus actually runs: "
        "log extensive, linear not, with the defect in closed form and a "
        "convention-independent ceiling."
    )
    w.add_caveat(
        "The ceiling row uses t_free ~ 1, which 10a establishes separately "
        "(tr_M(nucleon) ~ 1 at every A). It is quoted here, not re-derived."
    )
    w.add_caveat(
        "Corpus-state finding, not a physics result: the 2026-08-25 audit and "
        "bean qou-d5e8 both record the functional as posited with no derivation "
        "anywhere. The derivation is in docs/audits/, the first path that audit's "
        "own grep table lists. Both should be corrected rather than the finding "
        "being left to a third reader to rediscover."
    )

    out = w.save()
    print(f"\n  witness -> {out}")
    failed = [a for a in w.assertions if not a.passed]
    print(f"  assertions: {len(w.assertions) - len(failed)}/{len(w.assertions)} pass")
    for a in failed:
        print(f"    FAIL  {a.name}: computed={a.computed} expected={a.expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
