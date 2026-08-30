---
# qou-nial
title: 'ROOT CAUSE: the bond rule is a centred SUM of charges where Coulomb needs a PRODUCT — one substitution explains the whole arc'
status: todo
type: task
priority: normal
created_at: 2026-08-30T13:00:13Z
updated_at: 2026-08-30T13:00:56Z
---

## The finding

Owner, 2026-08-30: *"go ahead on the p->sigma, n->sigma^-1 identification"*.

**The identification is not wrong about protons and neutrons. It is wrong about
how two charges COMBINE.** One substitution explains every failure on this arc.

Producer: `computations/probes/level3_bond_charge_rule_probe.py`, 6/6.
Lean: `QOU/MassTheory/BondChargeRule.lean`, sorry-free, generic CommRing.

## What the corpus assigns

`torus-hopf-stability-proof`: **Q(proton) = +1, Q(neutron) = 0.**
`prop:skein-crossing-asymmetry`: the per-crossing correction is
`delta = q - (q + 1/q)/2 = h/2`, applied *"between composites of the same charge
relative to a mixed-charge baseline"* -- **two-valued**.

## What the implementation computes

`closed_form_tau_M.interface_factor`, relative to the mixed-charge baseline
`f_pn`, measured at the canonical proton pin:

    pair   Qi+Qj  Qi*Qj   implementation            centred SUM               PRODUCT
    pp      2.0    1.0    +0.10453014939781965772   +0.10453014939781965772   +0.10453...
    pn      1.0    0.0     0.0                       0.0                       0.0
    nn      0.0    0.0    -0.10453014939781965772   -0.10453014939781965772    0.0

**The implementation is EXACTLY `(Q_i + Q_j - 1) * h/2`** -- the CENTRED SUM --
to the last digit. Coulomb is `Q_i * Q_j * h/2`. The two **agree on pp and pn**
and **differ ONLY on nn**: the sum rule charges two neutral objects `-h/2`, the
product rule charges them `0`. Two neutrals have no Coulomb interaction, so `0`
is the physical value.

**One bond. That is the entire defect.**

## Why it explains the whole arc

Summed over the complete graph:

    sum rule      SUM_{i<j} (Q_i + Q_j) = (A-1) * Z     LINEAR in Z
    product rule  SUM_{i<j} Q_i * Q_j   = Z(Z-1)/2      QUADRATIC

- **qou-1pig** `f_pp - f_nn = h`: `sumRule_like_pairs_differ` gives `2c = h`.
  Under the product rule `nn` sits ON the `pn` baseline
  (`prodRule_like_pairs_are_strong_baseline`), so the STRONG channel becomes
  charge-symmetric and the only charge dependence left is on `pp` -- which is
  exactly what an electromagnetic term should be.
- **qou-dhsn** the A-only Coulomb channel and the `2Z` strong channel: the
  crossing counts are linear in Z **because the bond rule is a sum**.
- **CrossingCountAffine**'s degree gap: same fact, and this is its source.
- **qou-vudb** the A^0 mirror scaling.

`no_scaling_of_sumRule_is_prodRule` proves no multiple of the sum-rule total is
the product-rule total, quantifying over the coefficient FIRST.

## 🛑 What it does NOT fix — and the numbers say so

Measured mirror exponents over 20 odd-A pairs, A = 3..41:

    sum rule      (A-1)(Z-N)          p = 1.1137411
    product rule  [Z(Z-1)-N(N-1)]/2   p = 1.1137411     <-- IDENTICAL
    Coulomb shape (A-1)/A^(1/3)       p = 0.78040779

**For mirror pairs specifically the two rules have the SAME A-scaling**, because
at `Z - N = 1` both totals are proportional to `A - 1`. So the product rule is
**not** a fix to the mirror exponent. Its gain is structural -- `nn` on the
baseline, charge symmetry of the strong channel, and a `Z(Z-1)` multiplicity
that exists at all -- not numerical.

The remaining gap is the `1/R` of a Coulomb energy with `R ~ A^(1/3)`, a
GEOMETRIC input the bond picture does not carry. **Necessary, not sufficient**,
and do not report the product rule as closing the mirror splitting.

## Scope

Lean identities exact over a generic CommRing, for ANY charges; `Q(p)=1,
Q(n)=0` enter only in the specialised corollaries. Probe scope-(a).

**Nothing refuted.** `prop:skein-crossing-asymmetry`'s own wording is
two-valued and is what the PRODUCT rule realises; it is the three-valued ladder
in the implementation that does not follow from it. Nothing wired -- changing
`interface_factor` moves `tr_M` for every atom with an nn interface, i.e. the
whole binding table, and Phase 5q's 1e-49 closed-form validation is against the
current convention.

Parents: qou-1pig, qou-dhsn, qou-vudb.
