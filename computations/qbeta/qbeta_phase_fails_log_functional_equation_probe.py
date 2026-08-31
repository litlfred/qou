"""Route 5: the ladder phase is NOT a constant-residue holonomy angle, and
entry (7)'s "EXACT -1/4" is a 0.32% approximation.

Bean `qou-pdix` (child of `qou-cds1`), route 5 — the surviving route.

Kohno-Drinfeld FIXES the scale rather than leaving it free: braiding is
`P exp(hbar t/2)` with `t` eigenvalues +-1, matching the Hecke eigenvalues
`{q, -1/q}` exactly when `q = e^{hbar/2}`. So `hbar = 2 ln q` and a
**constant-residue** holonomy angle is `c * ln q` for some constant `c`.

## 1. The exclusion, by the logarithm's FUNCTIONAL EQUATION — no transcendence

The obvious objection is transcendence: `alpha` is algebraic in `q` while
`c ln q` is not. That is correct but needs transcendence theory. **The
elementary substitute needs none.** `ln(q^2) = 2 ln q`, so EVERY function
`c * ln` satisfies `f(q^2) = 2 f(q)`, whatever `c` is. Measured, `alpha` fails
that identity in both conventions:

    C: alpha(q^2) - 2alpha(q)
         = -(2q^{7/2} - 2q^{3/2} + q^5 - 2q^4 - 3q^3 + 3q^2 + 2q - 1)/(2q^2(q+1))
    D: alpha(q^2) - 2alpha(q)
         = (q-1)^2(q+1)(q^9+q^8+2q^6+q^5+3q^4-q^3+q^2-q+1)/(2q^2(q^2+1)(q^4+1))

Both nonzero as functions. **So alpha is not `c ln q` for ANY c, in either
convention** — hence not a constant-residue Kohno-Drinfeld holonomy angle.
Lean-proved in `QOU/QBeta/PhaseFailsLogFunctionalEquation.lean`, where the
witnesses are single points and the doubling lemma is stated for an arbitrary
additive `L`, so the exclusion holds for every `c` at once.

## 2. Entry (7)'s "EXACT" is not exact — measured

Entry (7) records *"EXACT: target / Re(log-gap) = -1/4, with Re(log-gap) =
2 ln q"* and builds acceptance-test part 2 on it (*"account for alpha = -1/4 of
Re(log-gap) AND the discarded i*pi"*). At the proton pin:

    quantity          value          ratio to 2 ln q0     deviation from -1/4
    alpha_C        -0.05233612          -0.25079432            0.32 %
    alpha_D        -0.04048578          -0.19400756           22.4  %
    alpha_required -0.05661728          -0.27130960            8.52 %

`-1/4` is a 0.32 % approximation for `alpha_C`, badly wrong for `alpha_D`, and
8.5 % off the phase the ladder actually needs. And by part 1 it **cannot** be
exact: exactness would make `alpha = -(1/2) ln q`, which fails the doubling
identity.

## Consequence: BOTH discriminating parts of the acceptance test are defective

    part 1  reproduce alpha through t^2       VACUOUS — it is a bar-symmetry
                                              test in disguise (proved in
                                              QOU/QBeta/BarEvenForcesStationarity)
    part 2  account for the -1/4 of Re(log-gap)  RESTS ON A NON-IDENTITY — the
                                              -1/4 is 0.32% off and provably
                                              cannot be exact
    part 3  deliver a value below 1           a sanity check, not a test

So the test that was meant to discriminate a holonomy construction does not
discriminate. That is a finding about the test, not about the hypothesis.

## What route 5 still has

The exclusion is scope-(b) and names its invariant, but it is NARROW: it removes
**constant-residue** connections. A connection whose residues depend on `q`, a
non-flat construction, or a genuinely `q`-dependent-parameter transcendental
object is untouched — and such an object need not satisfy the doubling identity.
What is gone is the specific Kohno-Drinfeld reading the acceptance test encoded.

Run:  python3 -u computations/qbeta/qbeta_phase_fails_log_functional_equation_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in (REPO / "computations", REPO / "computations" / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from q_parameter import q_at  # noqa: E402 — proton pin
from witness_base import WitnessBuilder  # noqa: E402

q = sp.Symbol("q", positive=True)
h = q - 1 / q
zC = sp.sqrt(q) / (q + 1)
zD = q**3 / (q**2 + 1)


def alpha(z):
    return sp.simplify((z - 1) * h / 2)


def main() -> int:
    checks: list[tuple[str, bool, str]] = []
    doubling = {}
    for nm, z in (("C", zC), ("D", zD)):
        a = alpha(z)
        d = sp.simplify(sp.together(a.subs(q, q**2) - 2 * a))
        doubling[nm] = str(sp.factor(d))
        checks.append((
            f"alpha_{nm}_fails_log_doubling_identity",
            sp.simplify(d) != 0,
            f"{nm}: alpha(q^2) - 2 alpha(q) != 0, so alpha != c*ln q for ANY c",
        ))
        # and it fails at a concrete rational point, matching the Lean witnesses
        pt = sp.Integer(2)
        checks.append((
            f"alpha_{nm}_fails_doubling_at_a_point",
            sp.simplify(d.subs(q, pt)) != 0,
            f"{nm}: nonzero at q=2, the witness the Lean proof uses",
        ))

    # entry (7)'s "EXACT -1/4"
    import mpmath as mp
    mp.mp.dps = 50
    q0 = mp.mpf(str(q_at()))
    hm = q0 - 1 / q0
    lg = 2 * mp.log(q0)
    REQ = mp.mpf("0.99839767")
    rows = {}
    for nm, zv in (("alpha_C", mp.sqrt(q0) / (q0 + 1)),
                   ("alpha_D", q0**3 / (q0**2 + 1))):
        av = (zv - 1) * hm / 2
        rows[nm] = {"value": mp.nstr(av, 16),
                    "ratio_to_2lnq": mp.nstr(av / lg, 16),
                    "dev_from_minus_quarter_pct":
                        mp.nstr(100 * abs(av / lg + mp.mpf(1) / 4)
                                / mp.mpf("0.25"), 6)}
    areq = -mp.acos(REQ)
    rows["alpha_required"] = {
        "value": mp.nstr(areq, 16),
        "ratio_to_2lnq": mp.nstr(areq / lg, 16),
        "dev_from_minus_quarter_pct":
            mp.nstr(100 * abs(areq / lg + mp.mpf(1) / 4) / mp.mpf("0.25"), 6)}

    aC = (mp.sqrt(q0) / (q0 + 1) - 1) * hm / 2
    checks.append((
        "entry7_exact_minus_quarter_is_NOT_exact",
        abs(aC / lg + mp.mpf(1) / 4) > mp.mpf("1e-6"),
        "alpha_C/(2 ln q0) = %s, not -1/4; entry (7) records this as EXACT"
        % mp.nstr(aC / lg, 12),
    ))
    checks.append((
        "entry7_deviation_is_about_a_third_of_a_percent",
        mp.mpf("0.3") < 100 * abs(aC / lg + mp.mpf(1) / 4) / mp.mpf("0.25")
        < mp.mpf("0.35"),
        "the -1/4 is a 0.32%% approximation for alpha_C",
    ))
    checks.append((
        "minus_quarter_is_far_worse_for_D_and_for_the_required_phase",
        (mp.mpf(rows["alpha_D"]["dev_from_minus_quarter_pct"]) > 20)
        and (mp.mpf(rows["alpha_required"]["dev_from_minus_quarter_pct"]) > 8),
        "22.4%% off for D, 8.5%% off for the phase the ladder needs",
    ))

    npass = sum(1 for _, ok, _ in checks if ok)
    for n, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}: {why}")
    print(f"\n{npass}/{len(checks)} assertions pass\n")
    print(f"  {'quantity':<16}{'value':>18}{'ratio to 2 ln q0':>20}{'dev from -1/4':>16}")
    for k, v in rows.items():
        print(f"  {k:<16}{v['value']:>18}{v['ratio_to_2lnq']:>20}"
              f"{v['dev_from_minus_quarter_pct'] + ' %':>16}")

    w = WitnessBuilder("qbeta-phase-fails-log-functional-equation",
                       engine="python+sympy+mpmath", output_dir=HERE,
                       _script_path=__file__)
    w.set_description(
        "Route 5, scope-(b): the ladder phase is NOT a constant-residue "
        "Kohno-Drinfeld holonomy angle. Elementary invariant, no transcendence "
        "needed — ln(q^2) = 2 ln q, so every c*ln satisfies f(q^2) = 2f(q), and "
        "alpha fails that identity in BOTH conventions as an explicit nonzero "
        "algebraic function. Separately: bean entry (7)'s 'EXACT: target / "
        "Re(log-gap) = -1/4' is a 0.32%% approximation for alpha_C (22.4%% for "
        "alpha_D, 8.52%% for the required phase) and provably cannot be exact, "
        "since exactness would make alpha = -(1/2) ln q. So BOTH discriminating "
        "parts of the branch-3 acceptance test are defective: part 1 is vacuous "
        "(a bar-symmetry test in disguise) and part 2 rests on a non-identity.")
    w.set_content_block("prop:q-beta-cos-resummation")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why}
                          for n, ok, why in checks])
    w.add_data("doubling_defect", doubling)
    w.add_data("ratio_to_re_log_gap", rows)
    w.add_data("scope", (
        "NARROW scope-(b): removes CONSTANT-RESIDUE connections only. A "
        "connection with q-dependent residues, a non-flat construction, or a "
        "genuinely q-dependent-parameter transcendental object is untouched "
        "and need not satisfy the doubling identity. What is gone is the "
        "specific Kohno-Drinfeld reading the acceptance test encoded."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save()
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
