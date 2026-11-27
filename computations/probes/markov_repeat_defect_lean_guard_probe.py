#!/usr/bin/env python3
"""markov_repeat_defect_lean_guard_probe.py — numerical guard on the Lean claim
that Markov stabilisation cannot hold at a repeated interface generator.

WHAT IS BEING GUARDED.  `QOU.QBeta.InterfaceScalar` (sorry-free, verified
`lean`-direct exit 0, `#print axioms` showing no `sorryAx`) now carries:

  * `markov_repeat_forces_quadratic` — if `tr(W sigma) = z tr(W)` is assumed at
    `W = sigma`, then `z^2 = h z + 1`.  Axiom-free.
  * `conventionD_markov_defect` — with `z = q^3/(q^2+1)`, `h = q - 1/q`,

        z^2 - h z - 1  =  -(q^2 - q + 1)(q^2 + q + 1) / (q^2 + 1)^2

  * `conventionD_markov_defect_neg` — that quantity is `< 0` for every `q > 0`,
    since both quadratic factors are `(q +- 1/2)^2 + 3/4`.
  * `markov_stabilisation_fails_on_repeat` — hence the stabilisation hypothesis
    is unavailable when the interface generator already occurs in the word.

A proof does not need numerical support to be true.  What this probe supplies is
the thing a proof cannot: a check that the CLOSED FORM in the Lean is the same
function the compute layer evaluates, so a later edit to either side that pulls
them apart is caught.  It is a wiring guard, not evidence.

WHY IT MATTERS HERE.  `interface_scalar` collapses the whole interface to the
single scalar `mu = a z + b`, and every downstream binding number goes through
that collapse.  The collapse is conditional on Markov stabilisation, which that
theorem's own docstring flags as a hypothesis standing in for Jones (1987).  The
new results say when the hypothesis is available: only at a generator the word
does not already use.

MEASURED COUNTERPART.  `colour_weighting_markov_universality_probe.py` (PR #6319)
fits `k` in `tr_M ~ (d + k)` from traces alone and finds `k = z_D` to 1e-48 on
four canonical nuclear words -- each using its interface generator exactly once --
and finds it BREAK (`k - z_D = 1.2285`) on the deuteron word with one extra sigma
on that same generator.  That control was measured before the Lean was written;
the Lean says why it had to come out that way.

Run:  python3 -u computations/probes/markov_repeat_defect_lean_guard_probe.py \
        2>&1 | tee /tmp/markov_repeat_defect_guard.log
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
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

LEAN_DECLS = (
    "QOU.QBeta.InterfaceScalar.markov_repeat_forces_quadratic",
    "QOU.QBeta.InterfaceScalar.conventionD_markov_defect",
    "QOU.QBeta.InterfaceScalar.conventionD_markov_defect_neg",
    "QOU.QBeta.InterfaceScalar.markov_stabilisation_fails_on_repeat",
)


def defect_direct(q):
    """z^2 - h z - 1 evaluated from the definitions, as the compute layer has them."""
    z = q ** 3 / (q ** 2 + 1)
    h = q - mp.mpf(1) / q
    return z * z - h * z - 1


def defect_closed_form(q):
    """The Lean's closed form, transcribed."""
    return -((q ** 2 - q + 1) * (q ** 2 + q + 1)) / (q ** 2 + 1) ** 2


def main() -> int:
    q0 = Q_MP

    print("=" * 80)
    print("guard: the Lean closed form for the Markov-repeat defect")
    print("=" * 80)
    print("\n  Lean declarations guarded:")
    for d in LEAN_DECLS:
        print(f"    {d}")

    # 1. Symbolic identity — the strongest form of the check, and it is exact.
    qs = sp.symbols("q", positive=True)
    lhs = (qs ** 3 / (qs ** 2 + 1)) ** 2 - (qs - 1 / qs) * (qs ** 3 / (qs ** 2 + 1)) - 1
    rhs = -((qs ** 2 - qs + 1) * (qs ** 2 + qs + 1)) / (qs ** 2 + 1) ** 2
    symbolic_zero = sp.simplify(sp.together(lhs - rhs))
    print(f"\n  SYMBOLIC  (direct - closed form) simplifies to: {symbolic_zero}")

    # 2. Numerical sweep, including the substrate pin.
    qs_num = [mp.mpf(s) for s in
              ("0.25", "0.5", "0.9", "1", "1.05")] + [q0] + \
             [mp.mpf(s) for s in ("1.5", "2", "7", "100")]
    worst_rel = mp.mpf(0)
    all_negative = True
    print(f"\n  {'q':>22}{'defect (direct)':>28}{'rel |direct-closed|':>24}")
    for q in qs_num:
        a, b = defect_direct(q), defect_closed_form(q)
        rel = abs(a - b) / abs(b)
        worst_rel = max(worst_rel, rel)
        if a >= 0:
            all_negative = False
        tag = " <- substrate pin" if q == q0 else ""
        print(f"  {mp.nstr(q, 12):>22}{mp.nstr(a, 18):>28}{mp.nstr(rel, 6):>24}{tag}")

    print(f"\n  worst relative disagreement over the sweep: {mp.nstr(worst_rel, 8)}")
    print(f"  defect strictly negative at every sampled q: {all_negative}")

    # 3. The quadratic the Lean extracts, at the pin: z^2 vs h z + 1.
    z0 = q0 ** 3 / (q0 ** 2 + 1)
    h0 = q0 - mp.mpf(1) / q0
    print(f"\n  at the substrate pin:")
    print(f"    z_D          = {mp.nstr(z0, 30)}")
    print(f"    z_D^2        = {mp.nstr(z0 * z0, 30)}")
    print(f"    h z_D + 1    = {mp.nstr(h0 * z0 + 1, 30)}")
    print(f"    difference   = {mp.nstr(z0 * z0 - (h0 * z0 + 1), 20)}")

    w = WitnessBuilder("markov-repeat-defect-lean-guard", engine="python")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("lean_declarations_guarded", list(LEAN_DECLS))
    w.add_data("lean_file",
               "folio/quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean")
    w.add_data("closed_form", "-(q^2 - q + 1)(q^2 + q + 1) / (q^2 + 1)^2")
    w.add_data("symbolic_difference", str(symbolic_zero))
    w.add_data("defect_at_q0", mp.nstr(defect_direct(q0), 40))
    w.add_data("z_D_at_q0", mp.nstr(z0, 40))
    w.add_data("q_values_swept", [mp.nstr(q, 12) for q in qs_num])

    w.add_assertion(
        "the Lean closed form is symbolically identical to the direct expression",
        computed=str(symbolic_zero), expected="0", tolerance="0",
        source="sympy simplify of (direct - closed form) as a rational function in q",
    )
    w.add_assertion(
        "and agrees numerically across a q sweep spanning 0.25 to 100",
        computed=mp.nstr(worst_rel, 30), expected="0", tolerance="1e-40",
        source=f"{len(qs_num)} values of q including the substrate pin",
    )
    w.add_assertion(
        "the defect is strictly negative at every sampled q",
        computed="1" if all_negative else "0", expected="1", tolerance="0",
        source="conventionD_markov_defect_neg, sampled",
    )
    w.add_assertion(
        "so z_D is not a root of x^2 - h x - 1 at the substrate pin",
        computed=mp.nstr(abs(z0 * z0 - (h0 * z0 + 1)), 30),
        expected="0.752702113251965", tolerance="1e-14",
        source="the quantity markov_repeat_forces_quadratic would require to vanish",
    )

    w.add_caveat(
        "This is a WIRING GUARD, not evidence for the theorem. The Lean results "
        "are proved; what is checked here is that the closed form in the Lean and "
        "the expression the compute layer evaluates are the same function, so a "
        "later edit to either side that separates them is caught."
    )
    w.add_caveat(
        "Scope: the negativity assertion is sampled, not proved, here — the proof "
        "is conventionD_markov_defect_neg, which covers every q > 0 via the "
        "positive-definiteness of q^2 +- q + 1. Do not cite the sweep as the "
        "general result."
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
