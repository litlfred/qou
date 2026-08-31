#!/usr/bin/env python3
"""Is the mass multiplier `lw` framing-dependent? — the criterion of
`docs/audits/2026-08-30-self-crossing-invariance-gate.md` §4, applied.

Bean `qou-brng`. Scope-(a) probe; emits no witness, wires nothing, moves no number.

BACKGROUND. `QOU.Mass.SelfCrossingInvarianceGate` (PR #6226) shows that
`SelfMutualPartition.binding_eq_neg_mutualEnergy` — the mass=self / binding=mutual assignment —
holds exactly on the slice `selfDefect = 0`, i.e. only if assembling the components changes no
component's own self-crossing content. Calugareanu says that is not automatic: `SL = Wr + Tw` and
only the SUM is the isotopy invariant, while a type-I Reidemeister move (creation/removal of a
SELF-crossing) changes `Wr` alone — and Moffatt & Ricca note ambient isotopies "typically involve
such passage" (Proc. R. Soc. Lond. A 439 (1992) 411-429, sec.1; `library/procrsoclondona92/ocr/`).

The criterion the audit states: a self-energy factoring through `SL` passes the gate; one read off
`Wr` (a bare self-crossing count) does not. THE AUDIT DELIBERATELY DID NOT ANSWER which one the
framework's `lw` is. This probe answers it.

TWO KINDS OF EVIDENCE, kept separate on purpose (AGENTS.md: "absence of a comment is not evidence
of absence of a reason" — say which claim was measured):

  (A) A TYPE/SIGNATURE fact, inspected not measured. `linking_weight_family_a` has signature
      `(q, q_inv=None) -> mpf`. It takes NO knot, NO diagram, NO framing. A function of `q` alone
      cannot be changed by a writhe<->twist reassignment, because it never reads either. This is
      what actually settles the criterion, and it is settled by reading the signature.

  (B) An EXACT algebraic check, measured here. The docstring's two closed forms
      `(3q^2 + 4 + 3q^-2)/4` and `5/2 + (3/4)h^2` (h = q - 1/q) are verified to agree IDENTICALLY,
      over exact rational arithmetic (`fractions.Fraction`) at several rational q -- not "to N
      digits", which would say nothing. The value at the substrate anchor is then reported at
      65 dps for the record.

VERDICT (stated up front so it is not buried): the Calugareanu objection DOES NOT BITE the
framework's `lw`. It is not writhe-valued; it is not self-linking-valued either. It is a normalized
sum of QUANTUM DIMENSIONS over the partitions of 4 -- a representation-theoretic quantity, not a
diagrammatic one. So `selfDefect = 0` holds for it and the mass=self / binding=mutual assignment is
safe from this particular objection. This DEFLATES the audit's own sec.4 criterion, which is the
honest outcome and is reported as such.

THE RESIDUAL THE ANSWER EXPOSES, which is the more interesting half: `lw` is called a "linking
weight" and is not a linking quantity. The bean frames `qou-brng` as "linking (mutual) vs
self-energy (self) amplitudes" -- two readings of one linking notion. They are not that. `M` is a
genuine topological coordination count; `lw` is a q-dimension sum over Wedderburn blocks. A
name-vs-content mismatch of exactly the kind AGENTS.md records for `markovZ`/`markovZc`.

PRECISION. mpmath end to end at 65 dps for the anchor value; `fractions.Fraction` (exact) for the
identity. No float64 anywhere; `float()` appears nowhere. q is read as `+Q_MP`, never
`mp.mpf(str(Q))`.
"""

from __future__ import annotations

import inspect
import os
import sys
from fractions import Fraction

from mpmath import mp

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (_HERE, os.path.join(_HERE, "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

mp.dps = 65

from q_parameter import Q_MP  # noqa: E402
from _li_2_q_util import linking_weight_family_a  # noqa: E402


def lw_closed_form_a(q: Fraction) -> Fraction:
    """`(3q^2 + 4 + 3q^-2) / 4` — the docstring's Wedderburn-sum form, exact over Q."""
    return (3 * q**2 + 4 + 3 / q**2) / 4


def lw_closed_form_b(q: Fraction) -> Fraction:
    """`5/2 + (3/4) h^2`, `h = q - 1/q` — the implemented form, exact over Q."""
    h = q - 1 / q
    return Fraction(5, 2) + Fraction(3, 4) * h**2


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # (A) the signature fact -- inspected, not measured.
    sig = inspect.signature(linking_weight_family_a)
    params = list(sig.parameters)
    diagram_free = params == ["q", "q_inv"]
    checks.append((
        "lw takes no knot / diagram / framing argument",
        diagram_free,
        f"signature = {sig}  params = {params}",
    ))

    # (B) the two closed forms agree EXACTLY over the rationals.
    all_exact = True
    for num, den in ((2, 1), (3, 2), (11, 10), (7, 5), (101, 100)):
        q = Fraction(num, den)
        a, b = lw_closed_form_a(q), lw_closed_form_b(q)
        if a != b:
            all_exact = False
        print(f"  q = {num}/{den:<4}  (3q^2+4+3q^-2)/4 = {a}   5/2+(3/4)h^2 = {b}   equal={a == b}")
    checks.append((
        "the Wedderburn-sum form and the implemented form are IDENTICAL over Q (exact, not 'to N digits')",
        all_exact,
        "fractions.Fraction, 5 rational sample points",
    ))

    # The anchor value, for the record. mpmath at 65 dps; q read as +Q_MP.
    q0 = +Q_MP
    lw0 = linking_weight_family_a(q0)
    h0 = q0 - mp.mpf(1) / q0
    lw0_alt = mp.mpf(5) / 2 + mp.mpf(3) * h0**2 / 4
    print()
    print(f"  q0            = {mp.nstr(q0, 30)}")
    print(f"  lw(q0)        = {mp.nstr(lw0, 30)}")
    print(f"  5/2+(3/4)h^2  = {mp.nstr(lw0_alt, 30)}")
    checks.append((
        "the production callable reproduces its own closed form at the anchor",
        lw0 == lw0_alt,
        "exact mpf equality at 65 dps (same expression, so equality is expected and is a wiring check)",
    ))

    print()
    ok = True
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}")
        ok = ok and passed

    print()
    print("VERDICT")
    print("  lw is a function of q ALONE -- a normalized sum of quantum dimensions over the")
    print("  partitions of 4 -- so it is neither writhe-valued nor self-linking-valued, and the")
    print("  Calugareanu / type-I objection of the self-crossing-invariance gate DOES NOT BITE it.")
    print("  selfDefect = 0 holds for the framework's mass multiplier; the mass=self / binding=mutual")
    print("  assignment is safe from THIS objection. The audit's sec.4 criterion is thereby deflated.")
    print()
    print("  RESIDUAL: 'linking weight' is a misnomer. qou-brng frames the open question as linking")
    print("  (mutual) vs self-energy (self) -- two readings of one linking notion. They are not that:")
    print("  M is a topological coordination count, lw is a representation-theoretic q-dimension sum.")
    print("  Nothing here says lw is WRONG; it says the two multipliers are not the same kind of")
    print("  object, which is a reframing of the question, not an answer to it.")
    print()
    print("  NOT CLAIMED: that the H4 Wedderburn-count interpretation of lw is derived. The producer's")
    print("  own docstring records it as posited -- at q0 the value is a CODATA-implied near-match to")
    print("  the value that round-trips m_p. That is untouched by this probe and stays open.")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
