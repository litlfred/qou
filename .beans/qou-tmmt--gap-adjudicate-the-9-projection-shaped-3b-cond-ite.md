---
# qou-tmmt
title: 'GAP: adjudicate the 9 projection-shaped §3b-cond item-5 candidates'
status: todo
type: task
priority: normal
created_at: 2026-09-04T14:12:30Z
updated_at: 2026-09-04T14:16:58Z
---

Found by `bun run scripts/conditional-on-class-hypothesis-audit.ts --projections`
(added 2026-09-04, PR #6662). NOT yet adjudicated — this bean is the work.

## What the filter does

Flags a block whose proof body is a **bare projection** of a bound hypothesis:
`:= h.field …` or `by exact h.field …`, where `h` is a binder of that very
declaration. That is the shape of the one confirmed item-5 violation
(`prop:explicit-central-idempotent`, found and fixed the same day).

It splits `PROJECTION` from `composition`: applying a class field to arguments
that DISCHARGE ITS HYPOTHESES is composition, which is what §3b-cond item 5
asks for. A bare `h.field`, or one applied only to the theorem's own binders,
discharges nothing — the field already IS the conclusion at that instantiation.

## Current output — 9 PROJECTION, 2 composition, of 78 bound blocks

    PROJECTION  cor:knot-factor-borromean-composite         decouple.decouples
    PROJECTION  cor:lr-tensor-character-bridge              h.bridge ν β
    PROJECTION  prop:archimedean-functor-uniqueness         hD.uniqueness τ_arch h_cont h_anti h_pent
    PROJECTION  prop:atom-knot-mass-derivation              h.atom_knot_mass_derivation cert T_w
    PROJECTION  prop:gb-residue-spectral-sum                s.spectral_decomposition
    PROJECTION  prop:hecke-branching-trace-decomposition    h.decomposition lam I beta1 beta2
    PROJECTION  prop:markov-trace-recursive-reducer         ctx.claim_reducer_correct β
    PROJECTION  prop:rho-k-h3a-refinement                   inst.identity data Δ partitions
    PROJECTION  prop:sigma-shell-from-beta-chain-derivation inst.identity data
    composition prop:b1-soft-sharpness-theorem              ctx.depth_bound_of_nonvanishing ctx.lewin_nonvanishing
    composition prop:b1-torus-knot-rows-theorem             ctx.b1_from_tate_rationality ctx.h_bloch_suslin ctx.h_garoufalidis_le

**All 11 are in `binds_other_carrier`** — blocks that mint their own context
class rather than taking the conjecture's published one. That is the predicted
higher-yield bucket: a locally-minted class is freer to carry its author's own
conclusion. **Zero** candidates in `binds_cone_class` now that
`prop:explicit-central-idempotent` is fixed.

Field names on three of them are self-describing: `claim_reducer_correct`,
`inst.identity`, and `h.atom_knot_mass_derivation` (field name == theorem name).

## Limits — read before quoting the 9

- **Sufficient, NOT necessary.** A class can carry the conclusion in a
  rearranged form reachable by `ring`/`simp` and this filter will not see it.
  `prop:proton-mass-substrate-identity` is exactly that and does not appear.
  So 9 is a **LOWER bound** on item-5 violations — the opposite direction from
  every other count in that script, whose header records four narrowings that
  each INFLATED what they claimed.
- **Not verdicts.** `hD.uniqueness τ_arch h_cont h_anti h_pent` applies a field
  to four arguments; whether those discharge hypotheses or are just the
  theorem's own binders decides projection-vs-composition, and the filter
  answers that syntactically. Read each declaration.

## Two bugs found in the filter itself, both fixed, one worth remembering

1. **`\w` is ASCII-ONLY.** Binder names here are routinely `β`, `ν`, `Δ`,
   `τ_arch`. The first cut's binder set missed every Greek one and mis-filed
   THREE blocks as `composition` that are projections. Note the direction:
   this bug caused **under**-flagging, so fixing it raised the count 6 → 9.
2. The declaration-boundary scan did not stop at a module docstring `/-!`, so
   `prop:atom-knot-mass-derivation`'s proof body swallowed the following
   docstring and its argument list was garbage.

Both are the same family as everything else in that file's header: the pattern
decided what could be seen, and the first answer was about the pattern.

## Next step

Open each of the 9 declarations and its bound class; decide whether a field
carries the block's conclusion. Fix as `prop:explicit-central-idempotent` was
fixed — re-encode the class as genuine sub-hypotheses so the theorem composes
them. That is per-block mathematics, not a sweep.


---

## ADJUDICATED 2026-09-04: 2 of 9 read, both CONFIRMED item-5 violations

### 1. `cor:knot-factor-borromean-composite` — CONFIRMED

`content/quantum-observable-universe/mass-theory/knot-factor-borromean-composite.lean`

    structure BrunnianDecoupling (k : ℕ) (component_factor : ℝ)
        (composite_factor : ℝ) : Prop where
      decouples : composite_factor = component_factor ^ k

    theorem knot_factor_borromean (k : ℕ) (h : ℝ) (composite : ℝ)
        (decouple : BrunnianDecoupling k (1 - h ^ 2) composite) :
        composite = (1 - h ^ 2) ^ k :=
      decouple.decouples

The structure has **exactly one field, and it is the theorem's conclusion**.
Textbook item 5.

Note the file's own comment defending it: *"it genuinely consumes the
`BrunnianDecoupling` hypothesis."* True, and beside the point — consuming a
hypothesis that IS the conclusion is precisely what item 5 forbids. The same
comment records removing a neighbouring vacuity (`∃ a, a = e`), so the author
was auditing for vacuity and this shape passed that filter. **Item 5 is not
visible to a vacuity check.**

### 2. `prop:gb-residue-spectral-sum` — CONFIRMED

    theorem gb_residue_spectral_sum (R) [CommRing R] [LinearOrder R]
        [s : GBResidueSpectralSum R] :
        s.mass = |s.descended| + ∑ ℓ : Fin s.levelBound, s.residue ℓ :=
      s.spectral_decomposition

Field projected directly. And the class's **own docstring already says the
quiet part**: the graded trace is *"supplied freely by the instance … **That
is not encoded here** — no field relates this to `tr_M`, to the filtration, or
to `descended`"*. So the class is documented as asserting nothing structural,
and the theorem projects one of its fields.

### Bonus finding — a same-FQN duplicate, latent not live

`GBResidueSpectralSum` is declared **twice**, both in `namespace QOU.BraidKnot`:

- `content/quantum-observable-universe/mass-theory/gb-residue-spectral-sum.lean` (block sibling)
- `content/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum.lean` (library)

i.e. two declarations of `QOU.BraidKnot.GBResidueSpectralSum`. This is the
sibling/library divergence hazard from `qou-e7xv` / PR #6540 §"A cost of this
sweep", and `lean.ref` resolves **sibling-first by file**, so the sibling wins.

**Compared: the field NAMES and types agree for all seven data fields.** The
one multi-line field, `spectral_decomposition`, was truncated by the comparison
and is **NOT** compared — do not read this as "the two are identical". Latent,
not currently diverged as far as checked.

## Still to adjudicate: 7

    cor:lr-tensor-character-bridge              h.bridge ν β
    prop:archimedean-functor-uniqueness         hD.uniqueness τ_arch h_cont h_anti h_pent
    prop:atom-knot-mass-derivation              h.atom_knot_mass_derivation cert T_w
    prop:hecke-branching-trace-decomposition    h.decomposition lam I beta1 beta2
    prop:markov-trace-recursive-reducer         ctx.claim_reducer_correct β
    prop:rho-k-h3a-refinement                   inst.identity data Δ partitions
    prop:sigma-shell-from-beta-chain-derivation inst.identity data

Hit rate so far is 2/2, but two is not a rate — read each.
