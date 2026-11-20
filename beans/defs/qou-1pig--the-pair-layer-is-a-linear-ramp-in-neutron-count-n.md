---
# qou-1pig
title: The pair layer is a LINEAR RAMP in neutron count, not an isospin structure — B_nn > B_pn > B_pp is backwards
status: todo
pr: 8205
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T10:05:43Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## The question that provoked it

Owner, 2026-08-30: *"do we need to split in the model? where issue?"* — on the
27% b3 gap being the 3H-3He splitting with 'nowhere to live but b3'.

**The model already splits.** The issue is not a missing split; it is that the
split it has is the wrong SHAPE.

## Measured (convention D, proton pin, alpha = m_e/(q0(q0-1)) = 4.18598 MeV)

    h    = q0 - 1/q0                = 0.20906029879563931543
    f_pp = z                        = 0.6126880371464652516
    f_pn = z - h(1/2 - delta/4)     = 0.50822978937673896258
    f_nn = z - h                    = 0.40362773835082593616

Sec.10a log form, pair energies B = -alpha ln f:

    B_pp = 2.0507 MeV      B_pn = 2.8332 MeV      B_nn = 3.7978 MeV

## Defect 1 — the ordering is backwards

Charge symmetry says the two LIKE pairs are nearly degenerate (equal up to EM
and a small CSB residual) and the UNLIKE pair is the distinguished one: the
deuteron is bound, the diproton and dineutron are **not bound at all**. So the
physical ordering is `B_pn > B_pp ~ B_nn`.

The model gives a **monotone ladder** `B_pp < B_pn < B_nn`, with the two like
pairs **1.747 MeV apart** where charge symmetry wants them nearly equal, and
`B_nn` — the unbound one — as the MOST bound.

## Defect 2 — it is a linear ramp, and exactly so

    midpoint of f_pp and f_nn  =  z - h/2
    f_pn                       =  z - h/2 + h*delta/4

so `f_pn` is the ARITHMETIC MEAN of `f_pp` and `f_nn` up to `h*delta/4`,
measured at **7.19e-5**, i.e. **1.4e-4 relative**. The bond factor is therefore
linear in the neutron count of the pair (0, 1, 2 neutrons -> z, z-h/2, z-h).

A linear ramp in neutron count is **odd in T_z**. Charge symmetry demands the
strong part be **even** in T_z, with the asymmetry supplied by an EM term the
framework does not have (qou-9v7t: *"the framework has no EM term in any
per-bond factor"*). So the typing is not an isospin structure at all.

## Consequence — this is where the 27% goes

The model's pair-layer mirror asymmetry is

    B(3H) - B(3He) = alpha * ln(f_pp/f_nn) = 1.74707324276 MeV

against the observed 0.763755 MeV: **right sign, 2.287x too large**.

Re-typing the AME Ursell inversion with the model's own pair layer instead of
`3*B(2H)` therefore OVER-subtracts and eats the whole 3-body term:

    b3 untyped   3H  1.8081        3He  1.044345      split +0.763755
    b3 retyped   3H -0.98231       3He +0.00100816    split -0.98332

The split flips sign. So the answer to *"do we need to split in the model?"* is:
the model splits already, and the split is 2.3x too strong and of the wrong
parity — strong enough that using it destroys b3 rather than cleaning it.

**Why the AME inversion cannot type its pairs.** It subtracts `3*B(2H)` from
both nuclei, typing every pair as pn, because `B(pp)` and `B(nn)` are **not
measurable** — the diproton and dineutron are unbound. So the untyped inversion
charges the entire p/n asymmetry, strong AND EM, to b3 by construction. That is
correct bookkeeping given the data; it is not an error, and it is why b3 carries
the 27%.

## Flag — a suspicious near-zero, do NOT build on it

Retyped `b3(3He) = +0.00100816` MeV, i.e. the model's 3He pair layer 7.717035
against AME 7.718043 — a 0.013% match. With a 2.3x-wrong asymmetry elsewhere in
the same table this is almost certainly coincidence. Recorded so nobody
rediscovers it as a result.

## Next

Ask whether the corpus's own p/n convention (`bring_color_weighted`, canonical
per owner ruling R3 2026-08-15) gives an even-in-T_z typing, and if not, what
would. Cross-reference qou-9v7t, which found 9 of 10 chirality candidates get
the mirror asymmetry backwards and named the missing EM channel.



---

## ANSWER to the owner's follow-up: "check bring_color_weighted parity" (2026-08-30)

**`bring_color_weighted` is parity-blind. It cannot fix this, and the reason is
structural.**

Producer: `computations/probes/pair_layer_isospin_parity_probe.py`, 8/8.

### The decomposition

Charge conjugation p<->n maps pp<->nn and FIXES pn. On the like-pair channel:

    E = (f_pp + f_nn)/2 = 0.50815788774864559388     charge-symmetric (isoscalar)
    O = (f_pp - f_nn)/2 = 0.10453014939781965772     charge-ANTIsymmetric (isovector)
    |O|/|E|             = 0.205704077252

and the T=0-vs-T=1 splitting -- what makes the deuteron special -- is `f_pn - E`:

    strict_averaged      f_pn - E = 0            EXACTLY zero
    bring_color_weighted f_pn - E = 7.19016e-5   = h*delta/4

    isovector / isoscalar-splitting = **1453.79**

### Root cause: it is the HECKE SKEIN RELATION, not a convention

`interface_factor`'s own docstring maps `positive: sigma -> z` (p-p) and
`negative: sigma^-1 -> z - h` (n-n). So

    f_pp - f_nn = z - (z - h) = h = q - 1/q = sigma - sigma^-1

**exactly** (residual 0.0). Given the identification `p |-> positive crossing,
n |-> negative crossing`, the skein relation fixes the isovector term with **no
free coefficient**. It is not tunable by any `pn_convention`.

### What bring_color_weighted actually does

It modifies **only** the p-n factor, by `h*delta/4 = 7.19e-5`. `f_pp` and
`f_nn` are untouched, so `O` is **identical under all three conventions**.
It is a correction on the channel that is already charge-even (pn is
self-conjugate) and leaves the 0.1045 term on the channel where the parity
problem lives.

It is still strictly better than `strict_averaged`, which sets the T=0/T=1
splitting to exactly zero -- better by 1/1454 of what is needed.

### In energy terms (Sec.10a log map, alpha = 4.18598 MeV)

    B_pp = 2.0507   B_pn = 2.8332   B_nn = 3.7978 MeV
    model mirror asymmetry = 1.74707 MeV   vs AME 0.763755   ratio 2.2875

Physics wants the reverse ordering: charge symmetry makes pp and nn nearly
degenerate (the strong CSB contribution to the A=3 splitting is ~70 keV of
764 keV) with the T=0 pn channel distinguished -- the deuteron binds, the
diproton and dineutron do not. The model has B_nn, the UNBOUND channel, as the
most bound.

### Scope

**(a)** for the physics judgement -- charge symmetry is an empirical
near-symmetry, not a theorem about this model. **Exact and unconditional** for
the algebra: `f_pp - f_nn = h` identically and `bring_color_weighted` leaves it
unchanged. Those two are what constrain any repair.

### Consequence for the repair

The isovector term cannot be reduced by choosing a different `pn_convention`.
It can only be changed by changing **the p/n-to-crossing-sign identification
itself** -- i.e. `p |-> sigma, n |-> sigma^-1` is the thing to revisit, not the
p-n averaging rule. Any candidate replacement has to make the LIKE pairs
near-degenerate while distinguishing the unlike one, which is the opposite of
what a crossing-sign assignment naturally produces.


## The alpha-free part of the same measurement is 19.0% — 2026-09-14

Owner instruction: *"Merge then try derivation"* (after *"Why are we doing a
census?! That's sounds like fitting. We should be in lean deriving"*). The
derivation attempted was whether a `tr_M`-level quantity can carry a
charge-antisymmetric part at all; it lands on this bean's ground, so the result
is recorded here rather than in a new bean.

Probe: `computations/probes/b3_asym_over_sym_is_alpha_free_probe.py`
(3/3 structural assertions, zero raw float64 in the witness).

**This bean already held the numerator.** `B(3H) - B(3He) = alpha*ln(f_pp/f_nn)
= 1.74707324276 MeV` is exactly twice the `b3_asym` of the mirror split, and the
linear-ramp / odd-in-T_z diagnosis above is the better explanation of it. None of
that is re-derived.

**What is new is that a residual survives `alpha`.** Decompose the chain assembly
by the mirror split and `alpha` cancels in the internal ratio:

    b3_sym  = alpha [ 2 ln f_pn - (ln f_pp + ln f_nn)/2 ]
    b3_asym = alpha [ (ln f_pp - ln f_nn) / 2 ]

Verified by recomputing at `7*alpha`: ratio drift `4.5e-72` while the parts
themselves move 7x.

The `2.287479x` this bean reports is **linear in alpha** — an alpha 2.287x
smaller removes it entirely. So is the corresponding symmetric comparison,
`1.922620x`. Their quotient is not:

    (model asym / obs asym) / (model sym / obs sym)
      = 2.287479 / 1.922620
      = 1.189772

so the alpha-free content of the A=3 mirror failure is: **the chain assembly
overshoots the antisymmetric part by 19.0% more than it overshoots the symmetric
part**, and no choice of `alpha` touches that 19.0%. That is the part of this
bean's defect 1 which cannot be argued away as a scale problem.

**The ratio's sign is NOT a second finding.** It comes out `-0.318567` against
AME `+0.267755`, but the numerator is positive and right-signed (this bean
establishes that), and the denominator is negative because `b3_sym` is — the
corpus's own `QOU.MassTheory.B3SignOneRoot.b3corpus_chain_neg` (sorry-free, the
Ursell alternation forcing `b3 < 0` for every bond triple). Grant that repair and
the ratio's sign repairs with it. The probe's first draft claimed the sign
"survives an overall sign flip"; that is true only for flipping both parts and is
withdrawn.

**Ranked against the corpus's ten candidates** on the same alpha-free
discriminant, computed from `b3-charge-decomposition-a3.witness.json` (which
reports sym and asym separately but never their internal ratio — every column it
has carries the candidate's own scale):

    product_beyond_pairwise  +0.054253    chiral_joint_triangle   -0.039168
    product_two_bond_only    +0.068345    chiral_joint_longrange  -0.088559
    product_three_bond_only  +0.140678    abs_joint_triangle      -0.029677
    joint_trace_abs_c3       +0.140678    CHAIN ASSEMBLY          -0.318567
    joint_trace_signed_c3    +0.140678    -- AME2020              +0.267755
    joint_trace_chiral_c3    -0.161850

The ten span `[-0.16185, +0.14068]`; the chain assembly is the first candidate
whose magnitude **exceeds** the target. It is also not among those ten — they are
product models, joint traces and chirality weightings, and the production
assembly is log-additive.

Scope **(a)**, not (b): this excludes the chain assembly's isospin structure as
written, not any ingredient. And the asymmetry is **isospin-labelling**, not
electromagnetic: `f_pp` and `f_nn` differ by the Hecke `h` (measured,
`|f_pp - f_nn| = h` exactly), and the per-bond factors carry no EM term.

Bean stays `todo` — the open question is unchanged.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.


## Progress Update (PR #8205)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`AtomNFQDegreeBondSetDichotomy.lean`, `TwoNucleonChannelSignObstruction.lean`, `PairLayerLinearRampParity.lean`, `ChainMirrorSplittingChargeSymmetry.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact `TL_3` Laurent polynomial probe (`computations/probes/atom_nf_qdegree_pair_ramp_mirror_probe.py`) and stamped witness (`computations/probes/atom-nf-qdegree-pair-ramp-mirror-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8205 (`ready: ed5c0c87c86301f2666c843555cc576831d17a74`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8205, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
