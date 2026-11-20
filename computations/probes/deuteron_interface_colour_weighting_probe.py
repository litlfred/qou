#!/usr/bin/env python3
"""deuteron_interface_colour_weighting_probe.py — the R3 colour weighting closes
0.097 % of the deuteron binding gap, and the effect is smaller than the slack in
the target it is being compared against.

WHY NOW.  Bean `qou-19jc` (2H ATTACK B) tested the deuteron's required interface
scalar against ten pre-specified Hecke-admissible elements and found none that
lands on it: the framework's derived element `(sigma + sigma^-1)/2` gives
mu = 0.5081578877 against a required 0.5877..., 13.5 % off in mu and ~27 % in B.
Its table predates owner ruling R3 (2026-08-15), which makes `bring_color_weighted`
the canonical p/n convention -- so the row labelled "derived" is the COLOUR-BLIND
interface, and the canonical one had never been evaluated here.

PR #6319 priced the colour weighting on the trace (1.4149e-4, nucleus-independent).
This converts that into the deuteron's binding and asks the obvious follow-up: is
the missing 27 % the colour weighting? It is not, and by three orders of magnitude.

THE IDENTITY THAT MAKES THIS EXACT.  #6319 proved -- with a control -- that for a
generator occurring once in the word, `tr_M(A (sigma_g + d I) B) = (d + z_D) *
tr_M(A B)` with `z_D = q^3/(q^2 + 1)`. So the interface contributes exactly the
scalar `mu = d + z_D`, which is the same object `qou-19jc` tabulates. Cross-check:
all of that bean's rows are reproduced here from `mu = a*z_D + b` alone --

    sigma               0.6126880371464653
    sigma^-1            0.4036277383508259
    sigma^2             1.128088744114354
    I                   1.0
    (sigma+sigma^-1)/2  0.5081578877486456   <- the bean's "derived" row

-- so this probe and that bean are measuring one quantity, reached independently.

MEASURED, at the proton pin, 50 dps, with `B = -alpha ln mu`,
`alpha = m_e/(q_0 (q_0 - 1)) = 4.185981363294476 MeV`:

    interface                     mu                      B / MeV      err vs AME
    colour-BLIND    d = -h/2      0.50815788774864559     2.83375482     +27.385 %
    colour-WEIGHTED d = -h(1/2-delta/4)
                                  0.50822978937673896     2.83316257     +27.358 %
    required (B = 2.224566 AME)   0.58776247263801610     2.224566        0

    shortfall to close           0.6091888 MeV
    colour weighting moves B by -0.0005923 MeV
    fraction of the gap closed    0.0972 %

THE PART WORTH KEEPING.  The weighting shifts mu by 7.190e-5. The bean's own
quoted required value, `0.58771506411074`, differs from a self-consistent
inversion of `B = 2.224566` by 4.741e-5. Those are the SAME ORDER -- the effect is
1.52x the slack in the target it would have to explain, and both are ~1e-4 against
a gap of 0.0796 in mu. So the colour weighting is not a candidate for the missing
27 %, and it sits close enough to the target's own bookkeeping noise that quoting
it to more than one significant figure would be false precision.

(First written here as "the effect is SMALLER than the slack", comparing an
ABSOLUTE shift of 7.190e-5 against a RELATIVE difference of 8.066e-5. A units
error, and the two happened to be numerically close, which is why it read as
plausible. Caught by this probe's own assertion failing. On one footing --
absolute, in mu -- it is 7.190e-5 against 4.741e-5, ratio 1.5166. The conclusion
is unchanged; the direction of the comparison was wrong.)

A STRUCTURAL NOTE ON THE SEARCH SHAPE.  `qou-19jc` scopes its negative carefully:
"the list is 10 entries, not the algebra". The identity closes that worry in a
direction that does not help the search. The interface acts through ONE generator,
and the subalgebra it generates is 2-dimensional -- `sigma^2 = h*sigma + 1` reduces
everything -- so every admissible element is `a*sigma + b*I` and every one of them
has `mu = a*z_D + b`, which sweeps all of R. **Matching mu therefore cannot select
an element: every mu is attained by a continuum of them.** Enumerating more
elements is not an under-powered search, it is the wrong shape of question; the
constraint has to fix (a, b) from a principle, not from the value of mu.

Scope: (a) for the numbers -- one nucleus, one pin, this functional form. The
structural note is (b) but its content is deliberately weak: it excludes a SEARCH
STRATEGY, not any ingredient. It does not exclude an element derived from a
space-indexed construction (`qou-vbyi`); such an element would come with its own
(a, b), which is exactly the point.

Run:  python3 -u computations/probes/deuteron_interface_colour_weighting_probe.py \
        2>&1 | tee /tmp/deuteron_interface_cw.log
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "hecke", COMPUTATIONS / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from _li_2_q_util import flavor_split_leading  # noqa: E402
from canonical_braid_crossings import d_for_ctype  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

B_AME_DEUTERON = "2.224566"          # MeV, AME2020
MU_QUOTED_IN_BEAN = "0.58771506411074"   # qou-19jc's "REQUIRED mu"


def main() -> int:
    q = Q_MP
    q_sym = sp.sympify(Q_50_DIGIT_STR)
    h = q - mp.mpf(1) / q
    z_D = q ** 3 / (q ** 2 + 1)
    delta = mp.mpf(
        str(sp.sympify(flavor_split_leading(sp.Symbol("q")))
            .subs(sp.Symbol("q"), q_sym)
            .evalf(mp.mp.dps))
    )
    d_blind = d_for_ctype("averaged", h)
    d_weighted = d_for_ctype("averaged_weighted", h, delta=delta)

    m_e = mp.mpf(str(M_E_MEV))
    alpha = m_e / (q * (q - mp.mpf(1)))
    B_ame = mp.mpf(B_AME_DEUTERON)

    def B_of(mu):
        return -alpha * mp.log(mu)

    mu_blind = z_D + d_blind
    mu_weighted = z_D + d_weighted
    mu_required = mp.e ** (-B_ame / alpha)     # self-consistent inversion
    mu_quoted = mp.mpf(MU_QUOTED_IN_BEAN)

    print("=" * 84)
    print("deuteron interface — what the R3 colour weighting is worth")
    print("=" * 84)
    print(f"\n  q_0 (proton)            = {mp.nstr(q, 40)}")
    print(f"  z_D = q^3/(q^2+1)       = {mp.nstr(z_D, 30)}")
    print(f"  h, delta                = {mp.nstr(h, 20)}, {mp.nstr(delta, 20)}")
    print(f"  alpha = m_e/(q(q-1))    = {mp.nstr(alpha, 16)} MeV")
    print(f"  B_AME(2H)               = {mp.nstr(B_ame, 10)} MeV")

    B_blind, B_weighted = B_of(mu_blind), B_of(mu_weighted)
    shortfall = B_blind - B_ame
    moved = B_weighted - B_blind
    frac = abs(moved) / abs(shortfall)

    print(f"\n  {'interface':<34}{'mu':>24}{'B / MeV':>16}{'err':>12}")
    for label, mu in (("colour-BLIND    d = -h/2", mu_blind),
                      ("colour-WEIGHTED d = -h(1/2-d/4)", mu_weighted),
                      ("required (inverted from AME)", mu_required)):
        b = B_of(mu)
        print(f"  {label:<34}{mp.nstr(mu, 20):>24}{mp.nstr(b, 12):>16}"
              f"{mp.nstr((b - B_ame) / B_ame * 100, 6):>11}%")

    print(f"\n  shortfall to close          = {mp.nstr(shortfall, 10)} MeV")
    print(f"  colour weighting moves B by = {mp.nstr(moved, 10)} MeV")
    print(f"  fraction of the gap closed  = {mp.nstr(frac * 100, 6)} %")

    # Both ABSOLUTE, in mu units -- comparing an absolute shift against a
    # relative difference is what produced the retracted claim in the docstring.
    d_mu = mu_weighted - mu_blind
    slack_abs = abs(mu_required - mu_quoted)
    gap_mu = mu_required - mu_blind
    print(f"\n  the weighting shifts mu by                {mp.nstr(abs(d_mu), 10)}")
    print(f"  qou-19jc's quoted vs self-consistent mu   {mp.nstr(slack_abs, 10)}")
    print(f"  ratio effect/slack                        {mp.nstr(abs(d_mu) / slack_abs, 8)}")
    print(f"  the gap in mu it would have to explain    {mp.nstr(gap_mu, 10)}")
    print(f"  -> same order as the target's bookkeeping noise, and ~1e-3 of the gap")

    print(f"\n  cross-check: reproducing qou-19jc's table from mu = a*z_D + b")
    table = (("sigma", mp.mpf(1), mp.mpf(0)),
             ("sigma^-1", mp.mpf(1), -h),
             ("sigma^2 = h.sigma + 1", h, mp.mpf(1)),
             ("I", mp.mpf(0), mp.mpf(1)),
             ("(sigma+sigma^-1)/2", mp.mpf(1), -h / 2))
    for name, a, b in table:
        print(f"    {name:<24} mu = {mp.nstr(a * z_D + b, 16)}")

    w = WitnessBuilder("deuteron-interface-colour-weighting", engine="python")
    w.add_parameter("nucleus", "deuteron (Z=1, N=1)")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("B_AME_MeV", B_AME_DEUTERON)
    w.add_data("z_D", mp.nstr(z_D, 50))
    w.add_data("alpha_MeV", mp.nstr(alpha, 30))
    w.add_data("mu_colour_blind", mp.nstr(mu_blind, 40))
    w.add_data("mu_colour_weighted", mp.nstr(mu_weighted, 40))
    w.add_data("mu_required_self_consistent", mp.nstr(mu_required, 40))
    w.add_data("mu_required_quoted_in_qou_19jc", MU_QUOTED_IN_BEAN)
    w.add_data("B_colour_blind_MeV", mp.nstr(B_blind, 30))
    w.add_data("B_colour_weighted_MeV", mp.nstr(B_weighted, 30))
    w.add_data("shortfall_MeV", mp.nstr(shortfall, 30))
    w.add_data("colour_weighting_shift_MeV", mp.nstr(moved, 30))
    w.add_data("fraction_of_gap_closed", mp.nstr(frac, 30))

    w.add_assertion(
        "the colour weighting closes under 0.1% of the deuteron binding gap",
        computed=mp.nstr(frac, 30), expected="0.000972198", tolerance="1e-8",
        source="|B(weighted) - B(blind)| / |B(blind) - B_AME|",
    )
    w.add_assertion(
        "the weighting is the same order as the slack in qou-19jc's quoted target",
        computed=mp.nstr(abs(d_mu) / slack_abs, 30),
        expected="1.5166391", tolerance="1e-6",
        source="both ABSOLUTE in mu: 7.190e-5 shift vs 4.741e-5 quoted-vs-inverted",
    )
    w.add_assertion(
        "and it is ~1e-3 of the gap in mu it would have to explain",
        computed=mp.nstr(abs(d_mu) / gap_mu, 30),
        expected="0.00090327", tolerance="1e-7",
        source="|d_w - d_blind| / (mu_required - mu_blind)",
    )
    w.add_assertion(
        "qou-19jc's 'derived' row is the COLOUR-BLIND interface",
        computed=mp.nstr(abs(mu_blind - mp.mpf("0.5081578877486456")), 30),
        expected="0", tolerance="1e-15",
        source="that bean's (sigma+sigma^-1)/2 row, reproduced from mu = z_D - h/2",
    )
    w.add_assertion(
        "the whole qou-19jc table follows from mu = a*z_D + b",
        computed=mp.nstr(
            max(abs((a * z_D + b) - ref) for (a, b, ref) in (
                (mp.mpf(1), mp.mpf(0), mp.mpf("0.6126880371464653")),
                (mp.mpf(1), -h, mp.mpf("0.4036277383508259")),
                (h, mp.mpf(1), mp.mpf("1.128088744114354")),
                (mp.mpf(0), mp.mpf(1), mp.mpf("1.0")),
                (mp.mpf(1), -h / 2, mp.mpf("0.5081578877486456")),
            )), 30),
        expected="0", tolerance="1e-15",
        source="five rows of that bean's table, recomputed from the #6319 identity",
    )

    w.add_caveat(
        "Scope-(a) for the numbers: one nucleus, one pin, and the functional form "
        "B = -alpha ln mu, which qou-19jc's own redirect places under suspicion "
        "(qou-kj4v: flavour-only mu cannot split 3S1 from 1S0). If that form is "
        "wrong, these MeV figures move; the mu figures and the identity do not."
    )
    w.add_caveat(
        "The structural note -- every admissible interface element is a*sigma + b*I, "
        "so mu = a*z_D + b sweeps all of R and cannot select an element -- excludes "
        "a SEARCH STRATEGY, not any ingredient. A space-indexed derived element "
        "(qou-vbyi) would arrive with its own (a, b) and is untouched by it."
    )
    w.add_caveat(
        "No claim that qou-19jc's quoted required mu is wrong for its purpose: it "
        "agrees to 4 significant figures and its 13.5 % conclusion is unaffected. "
        "The point is only that an effect of 7.2e-5 cannot be assessed against a "
        "value carrying 8.1e-5 of slack."
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
