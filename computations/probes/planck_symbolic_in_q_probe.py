#!/usr/bin/env python3
"""
The Planck quantities are symbolic in `q` — and at least three distinct objects
in this corpus wear the name "Planck length".

Bean `qou-plck`, issue #6941. This session first framed the Planck length as
FORBIDDEN — "a fourth calibration" — on the strength of
`meridian-exceptional-divisor-note.md`. **That was wrong as a general statement,
and the owner corrected it: "plank length is not a calibration.. written
symbolic in q".** The corpus already writes it symbolically, in two places, and
`g-q-closed-form.md` states explicitly that the SI value of `G` "functions
strictly as the human-scale rescaling ... enters as a unit-system datum, not as
a fit parameter on `q`".

What the note actually forbids is narrower: pinning the SUBSTRATE at
`m_Planck`, i.e. importing SI `G` as an input that fixes `q₀`. Writing `ℓ_P(q)`
as a `q`-expression is a different move, it is already done, and it introduces
no calibration at all.

WHAT THIS PROBE ESTABLISHES.

1. The corpus's own `q`-forms are mutually consistent: with `ħ_q = (q−1)/q`,
   `c_q = 1/(q−1)` and `G_q = q²/(q−1)⁴`, Newton's constant in Planck units is
   `G_Planck = G_q·(ħ_q/c_q)² = 1` IDENTICALLY as a rational function — matching
   the claim in `g-q-closed-form.md` §"In `q`-natural units".

2. The dimensional Planck triple follows in closed form, exactly:
       ℓ_P = √(ħ_q G_q / c_q³) = √q
       m_P = √(ħ_q c_q / G_q)  = (q−1)²/q^{3/2}
       t_P = √(ħ_q G_q / c_q⁵) = √q·|q−1|   (= √q·(q−1) on q > 1)
   No calibration enters: each is a function of `q` alone.

3. **At least three distinct objects are called "the Planck length" here, and
   they are not equal.** The corpus itself already separates two of them
   (`discrete-planck-step.md`: "This is the normalised total ... It is not the
   same object as the local `ℓ_P^step ~ ħ_q`"); the third is the dimensional
   one derived above, which no corpus block currently carries:

   | name | expression | at proton `q₀` |
   |---|---|---|
   | normalised total (`discrete-planck-step`) | `ħ_q · t_P^Reeb = 1` | `1` |
   | per-step share (`p5-counterexample`, `ℓ_q`) | `(q−1)/q = ħ_q` | `0.0991` |
   | dimensional (derived here) | `√(ħ_q G_q/c_q³) = √q` | `1.0536` |

   The share and the dimensional form differ by a factor of **10.63** at `q₀`.
   That is a notation collision of exactly the kind the register exists to
   catch, and it is recorded rather than resolved: which object the framework
   MEANS by "Planck length" in a given block is a question for the author, not
   something a probe should decide.

SCOPE. This probe derives and compares; it settles no physics. It does not claim
the dimensional `√q` is the "right" Planck length, nor that either corpus form
is wrong — only that three inequivalent expressions currently carry one name,
and that none of them is a calibration.

Precision: everything is exact symbolic algebra in `sympy` over `ℚ(q)`; the two
numerical columns are `mpmath` at the corpus compute precision from the exact
forms. No float64, no fit.

-- Ref: [manuscript] folio/quantum-observable-universe/information-theory/g-q-closed-form.md
-- Ref: [manuscript] folio/quantum-observable-universe/information-theory/discrete-planck-step.md
-- Ref: [manuscript] folio/quantum-observable-universe/fluid-dynamics/p5-counterexample.md
-- Ref: [manuscript] folio/quantum-observable-universe/braids-and-knots/meridian-exceptional-divisor-note.md
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import COMPUTE_DPS  # noqa: E402
from q_parameter import q_at  # noqa: E402  (proton pin — the standing default)


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q = sp.symbols("q", positive=True)

    hbar_q = (q - 1) / q
    c_q = 1 / (q - 1)
    G_q = q**2 / (q - 1)**4

    G_planck = sp.simplify(G_q * (hbar_q / c_q)**2)
    ell_P = sp.simplify(sp.sqrt(sp.simplify(hbar_q * G_q / c_q**3)))
    m_P = sp.simplify(sp.sqrt(sp.simplify(hbar_q * c_q / G_q)))
    t_P = sp.simplify(sp.sqrt(sp.simplify(hbar_q * G_q / c_q**5)))

    # The three objects called "Planck length".
    ell_total = sp.simplify(hbar_q * (q / (q - 1)))   # discrete-planck-step
    ell_share = sp.simplify(hbar_q)                   # p5-counterexample: ell_q
    ell_dim = ell_P                                   # derived above

    q0 = q_at(mp.mp.dps)
    def at0(e):
        return mp.mpf(str(sp.N(e.subs(q, sp.Float(str(q_at(40)), 40)), 40)))

    v_total, v_share, v_dim = at0(ell_total), at0(ell_share), at0(ell_dim)
    ratio = v_dim / v_share

    checks = [
        ("G_in_planck_units_is_identically_one",
         sp.simplify(G_planck - 1) == 0,
         "G_q*(hbar_q/c_q)^2 = 1 as a rational function of q, matching "
         "g-q-closed-form.md — the corpus's q-forms are mutually consistent"),
        ("ell_P_dimensional_equals_sqrt_q",
         sp.simplify(ell_P - sp.sqrt(q)) == 0,
         "sqrt(hbar_q G_q / c_q^3) = sqrt(q) exactly"),
        ("m_P_dimensional_closed_form",
         sp.simplify(m_P - (q - 1)**2 / q**sp.Rational(3, 2)) == 0,
         "sqrt(hbar_q c_q / G_q) = (q-1)^2 / q^(3/2) exactly"),
        ("t_P_dimensional_closed_form",
         sp.simplify(t_P - sp.sqrt(q) * sp.Abs(q - 1)) == 0,
         "sqrt(hbar_q G_q / c_q^5) = sqrt(q)*|q-1| exactly. The Abs survives "
         "because `q` is declared positive but not >1; on the framework's own "
         "domain q0 > 1 it reads sqrt(q)*(q-1). Stated with the Abs rather "
         "than assuming the domain into the identity"),
        ("planck_triple_is_free_of_calibration",
         all(e.free_symbols <= {q} for e in (ell_P, m_P, t_P)),
         "each of ell_P, m_P, t_P is a function of q ALONE — no m_e, no "
         "CODATA, no SI G, so none of them is a calibration"),
        ("normalised_total_is_one",
         sp.simplify(ell_total - 1) == 0,
         "discrete-planck-step's ell_P(q) = hbar_q * q/(q-1) = 1 identically"),
        ("three_planck_lengths_are_pairwise_distinct",
         sp.simplify(ell_total - ell_share) != 0
         and sp.simplify(ell_total - ell_dim) != 0
         and sp.simplify(ell_share - ell_dim) != 0,
         "the normalised total, the per-step share and the dimensional form "
         "are three inequivalent expressions carrying one name"),
        ("share_and_dimensional_differ_by_more_than_ten_at_q0",
         ratio > 10,
         f"at the proton q0 they differ by a factor {mp.nstr(ratio, 6)}"),
    ]

    print(f"hbar_q = {hbar_q}    c_q = {c_q}    G_q = {G_q}")
    print(f"G_Planck = G_q*(hbar_q/c_q)^2 = {G_planck}")
    print()
    print(f"ell_P = sqrt(hbar_q G_q / c_q^3) = {ell_P}")
    print(f"m_P   = sqrt(hbar_q c_q / G_q)   = {m_P}")
    print(f"t_P   = sqrt(hbar_q G_q / c_q^5) = {t_P}")
    print()
    print(f"THREE objects named 'Planck length'   (proton q0 = {mp.nstr(q0, 12)})")
    print(f"  normalised total  {str(ell_total):22} = {mp.nstr(v_total, 12)}")
    print(f"  per-step share    {str(ell_share):22} = {mp.nstr(v_share, 12)}")
    print(f"  dimensional       {str(ell_dim):22} = {mp.nstr(v_dim, 12)}")
    print(f"  dimensional / share = {mp.nstr(ratio, 12)}")
    print()

    ok = 0
    for name, cond, desc in checks:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}: {desc}")
        ok += 1 if cond else 0
    print(f"\n{ok}/{len(checks)} assertions")

    try:
        from qou_substrate.witness import WitnessBuilder
    except Exception as e:  # noqa: BLE001
        print(f"(witness not emitted: {e!r})")
        return 0 if ok == len(checks) else 1

    wb = WitnessBuilder("planck-symbolic-in-q", engine="sympy+mpmath",
                        _script_path=__file__)
    for name, cond, desc in checks:
        wb.add_assertion(name, computed="1" if cond else "0", expected="1",
                         tolerance="0.5", source=desc)
    wb.add_data("hbar_q", str(hbar_q))
    wb.add_data("c_q", str(c_q))
    wb.add_data("G_q", str(G_q))
    wb.add_data("G_planck_units", str(G_planck))
    wb.add_data("ell_P_dimensional", str(ell_P))
    wb.add_data("m_P_dimensional", str(m_P))
    wb.add_data("t_P_dimensional", str(t_P))
    wb.add_data("ell_normalised_total", str(ell_total))
    wb.add_data("ell_per_step_share", str(ell_share))
    wb.add_data("ell_share_at_q0", mp.nstr(v_share, 30))
    wb.add_data("ell_dimensional_at_q0", mp.nstr(v_dim, 30))
    wb.add_data("dimensional_over_share_at_q0", mp.nstr(ratio, 30))
    wb.add_data("corrects",
                "This session's own audit §5, which framed the Planck length "
                "as forbidden / a fourth calibration. Owner correction: it is "
                "not a calibration, it is written symbolically in q. What the "
                "corpus forbids is pinning the SUBSTRATE at m_Planck (importing "
                "SI G as an input fixing q0), which is a different move.")
    wb.add_data("scope",
                "Derives and compares; settles no physics. Does not claim the "
                "dimensional sqrt(q) is the 'right' Planck length nor that "
                "either corpus form is wrong — only that three inequivalent "
                "expressions carry one name, and that none is a calibration. "
                "Which one a given block MEANS is an author question.")
    wb.save({"q0Anchor": "proton",
             "q0AnchorReason": "the numeric column is evaluated at the standing "
                               "proton default; the algebra is anchor-free"})
    print("witness written")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
