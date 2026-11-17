---
# qou-gba1
title: 'Magnus Omega2 option E: derive the Omega2 pairing from what Omega2 is'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T11:44:24Z
updated_at: 2026-10-04T15:13:17Z
parent: qou-v2om
---

# The only option that ANSWERS the question rather than choosing

Derive the correct contraction from what Ω₂ is, instead of picking a weight
family and defending it.

## For

Ω₂ = ½ Σ_{i<j} [A_i, A_j] is a curvature-like object built from germs
`A_g = q(∂_q σ_g)σ_g⁻¹`. The right pairing should fall out of whatever
variational principle produces a binding energy — and if it does, it settles the
row-cap objection to option A **on principle** rather than by convention, which
no other option can do.

## Against

Open-ended research with no bounded cost. The arc already has a usable sign
result, and the sign does not depend on the choice, so this blocks nothing.

🛑 **THAT "AGAINST" IS VOID AS OF 2026-09-13.** The sign DOES depend on the
choice — see the corrected measured context below. The one argument for
deferring option E was that it decided only a label; it decides whether the
phenomenon exists. E is now the only option that answers the question.

## Work

- [ ] Identify the functional whose stationarity gives the binding correction.
      **Not done.** The step below reaches the same weight from a weaker premise
      (link-invariance) without needing the variational principle, so this is no
      longer the only route — but it is still the one that would make the
      premise a theorem.
- [x] Read off the induced pairing on `H_n(q)` and compare with both families.
      **DONE 2026-09-13** — see below. The pairing has an exact, parameter-free
      stabilisation law under Wenzl (residual 4e-141) and none under Plancherel.
- [x] Should NOT block option A; if it lands, it supersedes whichever was chosen.
      It does not supersede A — it **derives** A's choice from a principle
      instead of a convention, which is what A's "Against" said could not be
      done.

Option from the decision analysis in [`docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md`](../docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md).
Parent question: `qou-za3q`. Sibling options: `qou-q2q7` (A), `qou-94yt` (B),
`qou-smvw` (C), `qou-ia4w` (D), `qou-gba1` (E).

**Shared measured context** (none of this is fitted):

- `tr(1) = Σ_λ w(λ)·d_λ` — Wenzl gives exactly **1.0** at n = 6, 9, 12;
  Plancherel gives **11.139 / 184.233 / 6751.541**. Plancherel is not a
  normalised trace and its scale grows ~600× from A=2 to A=4.
- Plancherel puts **81.8 %** of its H₆ mass on ≥3-row shapes; the Wenzl row cap
  (level r = 2, `qou-fq0f`) puts **0 %** there. **62.4 %** of the Plancherel
  |contribution| at A=2 comes from shapes Wenzl annihilates.
- 🛑 **CORRECTED 2026-09-13. This block said "the **sign is robust**: P_total
  < 0 under both, on all three atoms". THAT IS FALSE**, and it is the premise
  every option below was weighed against. It was measured on 2026-09-07 from a
  robustness run whose triton and ⁴He sources predated the 2026-09-05 ordering
  ruling (`qou-hu1f`). Regenerated on the canonical borromean word:

      atom      Plancherel      Wenzl (headline)     agree?
      deuteron   -15.095          -6.921              yes
      triton      +2.470         -13.931              NO
      ⁴He        +34.126         -20.466              NO

      Plancherel  -, +, +   one sign change, deuteron -> triton
      Wenzl       -, -, -   no sign change anywhere in A = 2,3,4

  So the two families do not merely disagree on a number: **they disagree on
  whether the programme's target A-dependent sign change is present at all.**
  Per-λ traces are mixed-sign at every A (+4/−5, +14/−14, +33/−42), so the sum
  is a genuine cancellation and the sign was free to move.
- **Magnitude is not robust** either, and not monotone. The figures that stood
  here (triton −108.1 → −60.0, ⁴He −57.8 → −100.8) were the same pre-ruling
  run; the canonical values are in the table above.
- The probes' stated control (`ρ=I ⇒ tr(Ω₂)=0`) holds **blockwise** — every
  per-λ control trace is exactly 0 — so it is weight-blind and provides no
  evidence either way.

🛑 **CORRECTED 2026-09-13.** This read *"No published conclusion depends on the
choice, so this is a correctness-of-object question, not an emergency."* Both
halves are now false. The choice of weight family decides whether the
A-dependent sign change — the programme's target — is exhibited, so a published
sign statement DOES depend on it. Choosing the family because it yields the
wanted sign would be selection against the target (AGENTS.md), which is why the
honest reading is that under the production Markov weight the sign change is
**not** exhibited in A = 2, 3, 4.

## 2026-09-13 — E's first bounded result: the Wenzl weight is DERIVED, not chosen

`computations/deltalambda/magnus_omega2_markov_stabilisation_probe.py`,
witness `magnus-omega2-markov-stabilisation.witness.json`, 6/6 assertions.

### The argument, before any arithmetic

A nucleus is a **link**; a braid word only presents it. So a functional of the
nucleus must respect the moves relating different words for the same link. The
Markov trace on ⋃ₙ Hₙ(q) is *characterised* (Jones–Ocneanu) by three axioms:

    (1) trₙ(1) = 1
    (2) trₙ(xy) = trₙ(yx)
    (3) tr_{n+1}(x·σ_{n-1}) = z·trₙ(x),  x ∈ Hₙ        ← stabilisation

Wenzl y_λ realises all three, with z = q³/(q²+1) under convention D. Plancherel
satisfies **neither (1)** — tr(1) = 11.1 / 26.3 / 66.3 at n = 6 / 7 / 8 —
**nor (3)**, having no z at all. Axiom (3) is the relevant one because
stabilisation is the move that changes n, and **n = 3A**: a cross-A statement
*is* a statement across stabilisations.

Now the pairing. For β' = β·σ_{n-1}, far-commutativity leaves

    ΔΩ₂ = ½·m·[A_{n-2}, A_{n-1}],   m = multiplicity of σ_{n-2} in β

and since Ω₂(β)·ρ ∈ Hₙ, cyclicity plus axiom (3) give
tr_{n+1}(ρσ_{n-1}·Ω₂(β)) = z·trₙ(ρΩ₂(β)). So the pairing does **not** satisfy a
clean Markov law — the new crossing contributes — but it satisfies an exact one:

    P_y(βσ_{n-1}) = z·P_y(β) + (m/2)·Σ_λ y_λ tr(ρ'_λ [A_{n-2},A_{n-1}]_λ)

with **z fixed, no free parameter**. Under Plancherel there is no z, so there is
no such identity even to state.

### Measured on the deuteron word and two successive stabilisations

    n 6→7 (m=4)                    n 7→8 (m=1)
    tr(1)  Wenzl  1.0 exactly      1.0 exactly
           Planch 26.3135          66.3315
    raw trace, axiom (3):
           Wenzl  resid 7.4e-141   2.4e-141      ← positive control
           Planch resid 1.056      2.427         ← negative control
    z the raw trace implies:
           Wenzl  0.6126880371…    0.6126880371…  (identical)
           Planch −10.8667         +0.1788        (not even the same sign)
    THE PAIRING, derived law:
           Wenzl  resid 4.44e-141  6.18e-141     ← the question
           Planch resid 8.967      0.497

**The Plancherel arm does not merely need a different z — it has none.** The
ratio it would require moves from −10.87 to +0.18 between two stabilisations of
the same word. A family with a stabilisation law has one z.

### The test could have failed, and both terms are load-bearing

Falsification control: re-evaluating the *same* law at the two wrong values a
reader might substitute —

    z = q  (the competing Markov root, degenerate: y_(2,1)=0, not faithful
            on TL₃; named in markov_z's own docstring)   → resid 0.486, 0.691
    z = 1  (no stabilisation scaling)                    → resid 0.378, 0.538

So the identity pins z to 140 digits. And the correction term is not a rounding
detail: it is **40 %** of P at the first step and **15 %** at the second, so the
law is a real cancellation between two large pieces, not bookkeeping.

### What this does and does not settle

**Does**: gives a principled reason to prefer Wenzl that does not mention the
sign — the sign never enters the test — so it is *not* selection against the
target. Answers option A's "Against" (that the row cap is defensible only by
convention): the row cap comes with the trace that has the stabilisation law.

**Does not**: prove the binding functional must be a link invariant. That
premise is stated, not derived, and it is now the whole of what remains in this
bean. The unticked first item — identify the functional whose stationarity gives
the binding correction — would turn the premise into a theorem.

**Untested**: the other Markov move, conjugation β → αβα⁻¹, which needs
negative crossings the germ machinery does not build. Positive stabilisation
only.

### Recommendation to the owner for qou-za3q decision 1

Adopt **Wenzl**, on the stabilisation law rather than on consistency-with-
production. The consequence stands unchanged and must be reported with it: under
that weight the programme's target A-dependent sign change is **not** exhibited
in A = 2, 3, 4 (−, −, −). Deciding the measure and losing the phenomenon is the
honest outcome; keeping Plancherel because it yields −, +, + would be selection
against the target, and Plancherel is now additionally excluded on principle.

### Incidental

The probe's first run died in its own germ check — `y_lambda_wenzl_bridge_
numeric` sets global mpmath dps and never restores it, so a literal `dps=50` at
140 dps destroyed the 1e-50 finite difference. No live victim in the corpus
(measured: 1 of 15 literal-50 callers works above 50, and it already guards with
`workdps`). Warned at the source; fix is bean `qou-p4fr`.

### 2026-09-13 (later) — independent corroboration of `z` from `qou-qqm4`

Found while sweeping `qou-4383`, not while looking for it.
`qbeta_bond_factors_derived_probe.MEASURED["b_pp"] = 0.6126880371464652516`
is `z(q₀) = q₀³/(q₀²+1)` to **all 19 digits it carries**
(z = 0.6126880371464652515958299…). That bean's working title is "the bond
factors ARE the two Markov parameters", and it reached the number from the
qbeta chain expansion — a completely different route from the stabilisation
axiom used above.

Two things follow, one solid and one speculative:

- **Solid.** `z` is not a convention this arc adopted. It shows up
  identically in a derivation that has nothing to do with Ω₂, which is
  additional reason to trust the stabilisation law as structure rather than
  bookkeeping.
- **Speculative, offered to `qou-qqm4` as a lead and not tested here.** If a
  bond factor *is* the stabilisation parameter, adding a nucleon to the chain
  may literally be a Markov stabilisation, which would recast that bean's
  near-additivity question as one about Markov moves. Against it: `b_pn` and
  `b_nn` are **not** `z` (ratios 0.8295 and 0.7942 to their predecessors), so
  it is not one parameter doing all the work.

Cross-cited into `qou-qqm4` as a coordination note. That bean is under active
edit by a sibling today; nothing of theirs was changed.

---

REPLY FROM `qou-qqm4` (2026-09-13, session sleepy-morse, PR #7285).
Reciprocating the cross-citation; nothing of this bean is edited.

**Your `b_pp = z` is stronger than you stated it.** The note you left on
`qou-qqm4` reports it as verified numerically, "agreeing to all 19 digits `b_pp`
carries". `qbeta_bond_factors_derived_probe` — the file the `MEASURED` value
comes from — already establishes it **symbolically**: its docstring lists
`b_pp - z = 0` as identity 1, and the assertion is named
`b_pp_IS_the_markov_parameter`. So the relation is an identity of rational
functions in `q`, not an agreement to 19 digits. Your *independence* argument is
untouched — the stabilisation route and the nuclear-trace extraction really are
different routes to it.

**Your counter-argument does not survive, and the reason may be the lead you
wanted.** You wrote: *"`b_pn` and `b_nn` are not `z` (ratios 0.8295 and 0.7942),
so it is not one parameter doing all the work."* Both ratios reproduce
(0.82950826287, 0.79418355002 at dps=60). But all three bond constants are the
same interior bond factor at three values of one mixing parameter:

    b(t) = z - h*t,  h = q - 1/q,  delta = (q-1)^2 (1 - q^-4)/3

    pp  t = 0              -> z                 = q^3/(q^2+1)
    pn  t = 1/2 - delta/4  -> z - h*(1/2-delta/4) = the deg-10 rational
    nn  t = 1              -> z - h             = 1/(q^3+q)

Each difference simplifies to **exactly 0** over the symbol `q`. So it IS one
parameter — `z` — plus the Hecke quadratic relation, with `t` selecting the
letter. `b_pn` and `b_nn` are not `z` for the same reason `z - h` is not `z`.

Proved in Lean as `QOU.Hecke.BondLetterIdentification.tr_bond_interp` (#7285,
sorry-free) from the Markov property with material on both sides of the bond;
checked symbolically in
`computations/qbeta/qbeta_bond_factors_are_one_interpolation_probe.py` (4/4).

**Where that leaves your speculative lead.** "Adding a nucleon is a Markov
stabilisation" now has no counter-example from the bond factors — but I have not
tested it either, and the `t` values themselves are underived (`qou-qqm4` still
owes the `1/4` and the `(q-1)^2/3`). Note also that `qou-0pzi` reports the
`pp -> sigma` / `nn -> sigma^-1` orientation FALSIFIED on the two-nucleon signs;
the law says what a letter contributes, not which letter a flavour pair gets.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 75 Progress (2026-11-17T11:49:05Z)
- Advanced in PR `litlfred/qou#8329` (branch `feat/round75-blocklen-equilateral-bondletter-descent-framing-43c1`, head `d2c6d3d8e433b1ecf3e00634b44d230b097bc7d3`).
