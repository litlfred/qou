"""The cusp factor's bar-anomaly equals the Ocneanu framing quantum at N = 2 only
-- plus the naming bridge between two corpus theorems that are the same number.

WHAT THIS IS, AND WHAT IT IS NOT.  An earlier version of this probe claimed five
results.  A six-path corpus-grep established that THREE OF THEM ARE ALREADY
CORPUS THEOREMS and that a fourth "refutation" is likewise already proved.  This
version keeps only what survived, credits every prior-art site, and records the
retractions as checks so they cannot be re-derived a third time.

NOTATION.  bar : q -> 1/q.  For a Laurent-type X, the BAR ANOMALY is

    omega(X) := X / bar(X).

omega = 1 is bar-even, omega = -1 is bar-odd, and a monomial omega = q^k is
framing weight k.  h = q - 1/q.  hbar_q = 1 - 1/q is the CAL-2 cusp factor.
z_D = q^3/(q^2+1) is the convention-D Markov parameter; z_- = z - h is the
negative-crossing loop value; a is the Ocneanu framing quantum, a^2 = z/z_-.

===============================================================================
RETRACTED -- already in the corpus, do not re-derive a third time
===============================================================================

R1.  bar(z_D) = z_- EXACTLY.  Held at three sites:
     * `QOU.MassTheory.barZ`, content/.../lean/QOU/MassTheory/PnInterfaceBarStructure.lean:95
       `markovZ q^-1 = markovZ q - heckeH q`, over [Field K] [CharZero K], sorry-free.
     * content/.../mass-theory/interface-knot-markov-z-proof.md:49-69, the section
       "The three factors are one bar-orbit".
     * probes/pn_interface_bar_structure_probe.py, 17 assertions.

R2.  a^2 = z/bar(z), i.e. the framing ratio IS the bar-anomaly.  Held as
     `markovZ_bar_weight` in content/.../lean/QOU/Hecke/ClosedFormInterfaceFactors.lean:310,
     whose own docstring says the two readings are the same statement:
         "This is the fact that reconciles `markovZ_bar_weight` ('bar scales z by
          q^-4') with `QOU.MassTheory.barZ` ('bar sends z to z - h'): the two
          statements are the same statement."
     Also QOU/QBeta/LadderParityReflection.lean:37 as bar(z_D) = q^-4 z_D.

R3.  z_N - bar(z_N) = h for EVERY N of the Ocneanu family z_N = q^N/[N]_q.
     Held in content/.../lean/QOU/QBeta/MarkovZFullBarCondition.lean, verified
     "symbolically in N" by computations/markov_z_full_bar_condition_probe.py
     (2026-08-08).  The condition is named as a Prop: `FullBar` in
     QOU/QBeta/DecayFibreBarParity.lean:62.

R4.  Convention C is bar-even and therefore fails the full-bar condition.  Held
     and Lean-proved: `barEven_fullBar_forces_classical`, `zC_fails_fullBar`
     (MarkovZFullBarCondition.lean), `barEven_not_fullBar`
     (DecayFibreBarParity.lean:165), `QOU.QBeta.z_bar_invariant`.  The earlier
     version of this probe asserted that the corpus's only structural argument
     against C was the log-derivative one in markov-z-reconciliation.md.  THAT
     WAS WRONG: the bar-involution argument has been on main since 2026-08-08.

R5.  The writhe route to the mass/binding asymmetry is refuted.  Already proved,
     and more strongly than the earlier version of this probe managed --
     QOU.MassTheory.PoincareCenteringOfQ3 (lean-direct exit 0, 8 decls):
     `borromean_writhe_zero`, `writhe_prefactor_is_one` (a^writhe = 1 for ANY a),
     `no_writhe_prefactor_yields_inv_cube`.  Quantified over ALL writhe
     prefactors, not just the one word.  Scope (b), invariant: a writhe
     prefactor is multiplicative in the writhe, so at w = 0 every one is 1.

R6.  lw carries no framing, as a TYPE fact.  computations/lw_is_framing_independent_probe.py
     (3/3): `linking_weight_family_a` has signature (q, q_inv=None) -> mpf and
     "takes NO knot, NO diagram, NO framing".  It is a function of the crossing
     number alone, so two knots of equal crossing number and opposite writhe get
     the same lw.  CONSEQUENCE, and it retracts the earlier framing of this arc:
     whatever the extra q-power is, IT CANNOT LIVE ON lw.

===============================================================================
CORRECTED -- a row of the earlier bar-anomaly table contradicted the corpus
===============================================================================

C1.  omega(M) = 1 was WRONG for the corpus's DERIVED binding channel.
     QOU.Mass.BrunnianBindingChannel.countChannel is the count TIMES h,
         countChannel np nn q = (np + nn) * (q - q^-1) / 2,
     and `countChannel_barOdd` (BrunnianBindingChannel.lean:241) proves it
     BAR-ODD, so omega = -1, not +1.  The bare integer M of the earlier table
     comes from BindingMassRung, where M, lw, hbar are FREE REAL PARAMETERS
     carrying no parity content at all.  The two objects differ by exactly one
     bar-odd factor.  What survives the correction is the FRAMING-WEIGHT
     contrast, not the parity one:
         mass multiplier   omega = q^2   -- a monomial, framing weight 2
         binding channel   omega = -1    -- a sign,     framing weight 0
     Framing weight is the exponent of q; a sign is not a framing weight.

C2.  tr_M(K, q) is NOT bar-even in general, so the "one framing quantum" figure
     is right for the DEPRECATED global-scalar form and wrong for the canonical
     per-block one.  With per_knot_density_per_block = [Vol(K)/hbar_q^2]*tr_M
     (_li_2_q_util.py:649), omega(mass) = q^2 * omega(tr_M), and the corpus
     MEASURED omega(tr_M) /= 1: shifts of +13.2 % / +11.8 % under q -> 1/q
     (docs/coordination/2026-07-18-ka-additive-cluster-negative-structural-findings.md,
     bean qou-7uxa), i.e. omega ~ 0.883 / 0.894 -- not a monomial in q at all.
     The Borromean case IS bar-even (`trM_borromean_bar_invariant`,
     BorromeanMarkovTrace.lean:262) because the Borromean link is AMPHICHIRAL,
     which is an A-family fact and not a general one.

C3.  hbar_q^2 -> q^2 is already in the corpus, in different vocabulary:
     interface-knot-markov-z-proof.md:119-126 localises the same factor and
     calls it "the two quanta of substrate Planck action".  Same number,
     different interpretive frame.

===============================================================================
WHAT IS NEW -- the only two things this probe lands
===============================================================================

N1.  omega(1/hbar_q^2) = a holds at N = 2 AND AT NO OTHER N.  With the Ocneanu
     family's framing quantum a_N = q^N, omega(1/hbar_q^2) = q^2 matches a_N
     exactly when N = 2 -- and N = 2 is convention D, the sl_2 point of the
     family (`QOU.QBeta.WenzlWeight.level_eq_two_of_conventionD`).  The
     six-path grep found NO corpus artifact evaluating hbar_q's bar-anomaly
     against the family index N: the two halves each exist and nothing composes
     them.  (Path 0, corpus_search, was DOWN -- the paper-assistant MCP server
     failed ENOENT -- so this is grep-open, not graph-open.)

N2.  THE NAMING BRIDGE.  `markovZ_bar_weight`'s q^-4 and `markov_framing_ratio_eq`'s
     a^2 = q^4 are the same number, in two files, with no cross-reference
     between them.  `markov_framing_ratio_eq` (information-theory/toffoli-lp-stability.lean:792)
     has exactly four citation sites corpus-wide and NONE is in the mass or
     binding chain.  So the corpus knows "bar scales z by q^-4" and knows "the
     Ocneanu framing ratio is q^4" and does not record that these are one fact.

WHAT THIS DOES NOT DO.  It does not close residual (ii) of bean qou-brng, and it
does not reach it.  The corpus's own 2026-08-30 entry in that bean declares the
self-vs-mutual FRAMING of residual (ii) mis-posed -- lw is a representation-
theoretic Wedderburn q-dimension sum, M a topological coordination count, so
the question "why does one linking notion split two ways" is not the situation.
The live carrier for the mass channel's extra q-power is bean qou-24w9, which is
further along: it identifies /q^3 as 1/y^Schur_(3), the q-Schur Plancherel
weight at the content sum c((3)) = 0+1+2 = 3, and explains the bar-asymmetry by
bar sending lambda -> lambda' with c(lambda') = -c(lambda) -- a single-block
weight picking the chirality-extremal block.  That is a different mechanism from
framing, and the bar-symmetrised repair of hbar_q was already TESTED AND REFUTED
there (q re-solves to 1.12303, m_mu/m_e misses by -27.16 %, 1,286,334x worse;
qbeta/fbor_normalisation_barsymmetry_probe.py).

TERMINOLOGY HAZARD, recorded.  "framing quantum" is overloaded in this corpus,
a markovZ/markovZc-class collision: the RIBBON twist theta = q^{1/2} gives a
framing ladder q^{T/2} (bean qou-gzs0), while the OCNEANU framing ratio gives
a = q^2.  These differ by a = theta^4.  N1 is about the Ocneanu one.

PRECISION.  Exact symbolic sympy over the ring generated by s = sqrt(q).  No
floats, no numerics, no anchor read, no witness emitted, nothing re-scored, no
convention adopted or retired.  The exit code is the verdict, matching the
sibling markov_loop_value_product_and_framing_ratio.py.
"""

from __future__ import annotations

import sys

import sympy as sp

CHECKS: list[tuple[str, bool]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((label, ok))
    mark = "ok  " if ok else "FAIL"
    print(f"  [{mark}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")


s = sp.symbols("s", positive=True)
q = s ** 2


def bar(e):
    return sp.cancel(sp.together(sp.sympify(e).subs(s, 1 / s)))


def omega(e):
    """Bar anomaly omega(X) = X / bar(X)."""
    return sp.cancel(sp.simplify(sp.sympify(e) / bar(e)))


def zero(e) -> bool:
    return sp.simplify(sp.together(sp.cancel(sp.sympify(e)))) == 0


h = q - 1 / q
hbar_q = 1 - 1 / q
zD = q ** 3 / (q ** 2 + 1)
zDneg = zD - h
a = q ** 2


def qint_sym(n: int):
    return sp.cancel((q ** n - q ** (-n)) / (q - 1 / q))


def main() -> int:
    print()
    print("=" * 74)
    print("  cusp-factor bar-anomaly vs the Ocneanu family index -- bean qou-brng")
    print("=" * 74)
    print()

    # ---- N1: the one genuinely new claim ------------------------------------
    print("N1. NEW: omega(1/hbar_q^2) = a_N = q^N at N = 2 and at no other N")
    check("omega(1/hbar_q^2) = q^2",
          zero(omega(1 / hbar_q ** 2) - q ** 2),
          f"omega(1/hbar_q^2) = {omega(1 / hbar_q ** 2)} = q^2")
    matching = [n for n in range(1, 9) if zero(omega(1 / hbar_q ** 2) - q ** n)]
    check("matches the family framing quantum a_N = q^N only at N = 2",
          matching == [2],
          f"matching N over 1..8: {matching}\n"
          "N = 2 is convention D, the sl_2 point (WenzlWeight.level_eq_two_of_conventionD)")
    check("D IS the N = 2 member of z_N = q^N/[N]_q",
          zero(sp.cancel(q ** 2 / qint_sym(2)) - zD),
          f"q^2/[2]_q = {sp.cancel(q ** 2 / qint_sym(2))} = z_D")
    print()

    # ---- N2: the naming bridge ----------------------------------------------
    print("N2. NEW: the naming bridge -- two corpus theorems are one number")
    check("bar(z_D) = q^-4 * z_D   (markovZ_bar_weight, ClosedFormInterfaceFactors)",
          zero(bar(zD) - zD / q ** 4))
    check("z_D/z_- = q^4 = a^2     (markov_framing_ratio_eq, toffoli-lp-stability)",
          zero(sp.cancel(zD / zDneg) - q ** 4))
    check("=> they are the SAME statement: omega(z_D) = a^2",
          zero(omega(zD) - a ** 2) and zero(sp.cancel(zD / zDneg) - omega(zD)),
          "markov_framing_ratio_eq has 4 citation sites corpus-wide and NONE is\n"
          "in the mass or binding chain; no file records that these coincide")
    print()

    # ---- R: the retractions, re-verified so they are not re-derived ---------
    print("R.  RETRACTED -- already corpus theorems (verified here only as credit)")
    check("R1 bar(z_D) = z_-        -- QOU.MassTheory.barZ (PnInterfaceBarStructure.lean:95)",
          zero(bar(zD) - zDneg))
    check("R3 z_N - bar(z_N) = h for N = 1..8  -- MarkovZFullBarCondition.lean",
          all(zero(bar(sp.cancel(q ** n / qint_sym(n)))
                   - (sp.cancel(q ** n / qint_sym(n)) - h)) for n in range(1, 9)),
          "reason, one line: z_N - bar(z_N) = (q^N - q^-N)/[N]_q = [N]_q h/[N]_q = h")
    zC = 1 / (s + 1 / s)
    check("R4 z_C is bar-even, so C fails full-bar -- barEven_fullBar_forces_classical",
          zero(bar(zC) - zC) and not zero(bar(zC) - (zC - h)),
          "the earlier version of this probe wrongly claimed the corpus's only\n"
          "structural argument against C was the log-derivative one; the\n"
          "bar-involution argument has been on main since 2026-08-08")
    print()

    # ---- C1: the correction -------------------------------------------------
    print("C1. CORRECTED: the derived binding channel is BAR-ODD, not bar-even")
    np_, nn_ = sp.symbols("np nn", nonnegative=True)
    count_channel = (np_ + nn_) * (q - 1 / q) / 2      # BrunnianBindingChannel.countChannel
    check("countChannel = (n+ + n-)*h/2 is BAR-ODD (countChannel_barOdd)",
          zero(bar(count_channel) + count_channel),
          f"omega(countChannel) = {omega(count_channel)}, NOT +1")
    check("the bare integer M of BindingMassRung carries no parity content",
          all(zero(omega(sp.Integer(k)) - 1) for k in (1, 2, 3, 7)),
          "M, lw, hbar are free real parameters there, hypothesis only lw /= 0;\n"
          "so omega(M) = 1 is a statement about a free parameter, not a result")
    check("what survives is the FRAMING-WEIGHT contrast, not the parity one",
          zero(omega(1 / hbar_q ** 2) - q ** 2) and zero(omega(count_channel) + 1),
          "mass multiplier  omega = q^2  -- a monomial, framing weight 2\n"
          "binding channel  omega = -1   -- a sign,     framing weight 0\n"
          "a sign is not a framing weight; the exponent of q is")
    print()

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print("=" * 74)
    print(f"  {n_ok}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  Two things are new: omega(1/hbar_q^2) matches the Ocneanu")
    print("  family's framing quantum a_N = q^N at N = 2 and no other N, and the")
    print("  naming bridge between markovZ_bar_weight's q^-4 and")
    print("  markov_framing_ratio_eq's a^2 = q^4, which no file records as one")
    print("  fact.  Everything else this probe once claimed is already a corpus")
    print("  theorem and is retracted above with its site.  Residual (ii) of")
    print("  qou-brng is NOT closed and is NOT reached: the corpus's own")
    print("  2026-08-30 entry in that bean declares the self-vs-mutual framing")
    print("  of it mis-posed, and the live carrier for the mass channel's extra")
    print("  q-power is bean qou-24w9 on a q-Schur Plancherel route, not a")
    print("  framing one.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
