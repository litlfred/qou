# All five SDP uniqueness axioms were false — and the triage method could not see it

**Date:** 2026-09-05
**Bean:** `qou-i6u4`
**PR:** [#6882](https://github.com/litlfred/qou/pull/6882)
**Status:** closed — all five deleted, consumers rerouted, refutations landed in-tree

## The finding

Every one of the five SDP axioms under `QOU/MathlibExt/` asserted a **false**
proposition. Each one alone derives `False`, verified `lean`-direct with
`#print axioms` showing no `sorryAx` and the axiom itself as the only
non-standard dependency:

| axiom | file |
|---|---|
| `strict_complementarity_unique_axiom` | `SDP.lean` |
| `slater_strict_complementarity_kernel_axiom` | `SDPRealUniqueness.lean` |
| `SDPRankUniqueness` | `SDPRealUniqueness.lean` |
| `strict_complementarity_kernel_disjoint` | `SDPRankEquality.lean` |
| `affine_slater_rigidity` | `SDPRankEquality.lean` |

Two derived theorems were false with them:
`rank_equality_under_strict_complementarity` and the
`real_strict_complementarity_unique` pair.

## The counterexamples

**`zeroSDP`** — `n = 1`, no constraints, **zero cost**. Every PSD matrix is
feasible, `objAt ≡ 0`, and the dual slack `S = cost − Σ yᵢAᵢ` is the **zero
matrix**. So `Φ⋆ = 0` and `Φ' = 1` are both optimal and the conclusion gives
`1 = 0`.

**`rankSDP`** — `n = 2`, no constraints, `cost = diag(1,0)`, `Φ⋆ = diag(0,1)`,
`D = diag(0,1)`. Needed only for `affine_slater_rigidity`, whose rank guard
`rank Φ⋆ + rank S = n` this one **satisfies** (`1 + 1 = 2`) while still
producing `S · D = 0` with `D ≠ 0`.

Both are Slater-strictly-feasible, so no Slater hypothesis excludes them.

## Why the guards were not guards

The `SDPRealUniqueness` layer *looks* sound where `SDP.lean` looks thin: its
`RealStrongDualityPair` carries genuine `dualSlack_psd` and `obj_eq_dualObj`
fields where `SDP.lean`'s `StrongDualityPair` has `True` placeholders, and its
axioms carry `_h_S_diff` / `_h_constraint_diff` on top. I cleared it on that
basis earlier in the same triage, and **that was wrong.**

Those hypotheses say `Φ' − Φ⋆ ∈ ker S`. When `S = 0` the kernel is everything,
so they hold vacuously — and they fail to constrain precisely in the degenerate
case where uniqueness fails. **Structure is not soundness.**

The sharpest instance: `class SlaterStrictComplementarityKernel`'s single field
*was* the false proposition, so the class was **uninhabitable** and any instance
of it unsound.

## What the true theorem is

Alizadeh–Haeberly–Overton 1997 does not say strict complementarity implies a
unique primal optimum. It says the optimum is unique **iff the dual is
nondegenerate**, given strict complementarity. None of the five axioms carried a
nondegeneracy hypothesis. Every citation was to a real theorem; no Lean
statement was that theorem.

## Why two prior audits cleared them

[`2026-08-26-live-axiom-surface-recheck.md`](2026-08-26-live-axiom-surface-recheck.md)
and [`2026-09-03-axiom-tier-triage.md`](2026-09-03-axiom-tier-triage.md) both
examined this exact five-axiom family, eight days and two days before. Both did
careful work — corpus-greping every name-stem for a proved shadow, measuring
proof terms, reading Mathlib's own TODO list to establish that conic duality is
not yet available. The 2026-09-03 audit concluded the tier is "blocked one level
lower" than the axioms state.

Both asked:

1. *Is the citation real?* — yes, all five.
2. *Can Mathlib close it?* — no, not yet.

Neither asked:

3. **Is the Lean statement the theorem that citation names?**

That third question is the whole finding. An axiom with an impeccable citation
to a true published theorem is still a false Lean proposition when the
formalisation drops a hypothesis the paper requires, and no amount of care on
questions 1 and 2 substitutes.

### 🛑 But this failure mode was NOT new to the corpus, and saying so was my error

The first version of this audit said *"nothing in the axiom-triage tradition
here tests for it"*, framing the method gap as a discovery. **It is not.** One
directory over from the SDP files,
[`QOU/BraidKnot/LpDualityHypothesisClass.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/LpDualityHypothesisClass.lean)
carries a section headed *"No global instance — and why the two that were here
proved `False`"*, recording that `schrijver_strong_duality` and
`schrijver_complementary_slackness` **each independently made the library
inconsistent** — found by the same degenerate-instance method, on the same kind
of object (an LP whose `primal_obj` and `dual_obj` are arbitrary independent
fields), and repaired the same way: delete the axioms, keep the §3b-cond
conditional class, supply no global instance.

So the corpus already knew this failure mode, in the adjacent file, in the same
`BraidKnot` directory. What is true is narrower and worth stating exactly:

- the **precedent existed and was well documented** at the site of its own fix;
- the two 2026-08/09 audits of the SDP family did not carry it across, though
  the SDP axioms sit one directory away and are the same conic-duality subject;
- so the gap is in **propagation** — a lesson recorded at its own site does not
  reach the next audit — not in the corpus ever having lacked the insight.

That distinction matters, because the remedy differs. A novel gap needs a new
idea; a propagation gap needs the check to be *runnable* and *routine*, which is
what the script below is for.

**And the same oversight showed up in the script.** Its first version flagged
`schrijver_strong_duality` as an unexamined candidate — it was matching the
axiom text quoted inside that file's own post-mortem. See the parser note.

## Blast radius — no false consequence landed

Luck, not design. Every live consumer instantiates `cost = 1` (identity), never
`cost = 0`:

- `nucleusEmptySDP` has `cost := 1`, so its objective is `trace Φ` and its
  uniqueness claim (PSD + zero trace ⟹ zero) is **true**. Only the route was
  rotten, and that file already carried a sorry-free alternative.
- The canonical-knot-ID bridge consumes the generic theorem.

## The repair

**`QOU/MathlibExt/SDPUniquenessCounterexamples.lean`** proves the five
**negations** directly rather than deriving `False` from the axioms — so the
results survive their deletion and block the statements from being restated.
`#print axioms` on all five: `[propext, Classical.choice, Quot.sound]`.

All five axioms deleted, each leaving a section comment naming its
counterexample theorem and concrete instance. Consumers rerouted onto the
proven interior case (`dualSlack` positive-definite), which was already
sorry-free and axiom-free in every file. 30/30 files importing the SDP chain
`lean`-direct exit 0.

**Nothing true was lost.** Every live consumer's dual slack is the identity, so
each discharges the interior hypothesis outright. The axioms were supplying a
false *unconditional default* over the top of a correct *conditional* design —
`SDPSlaterUniqueness` already had two proven axiom-free instances.

## The follow-on: what else has this shape?

[`scripts/lean-axiom-degenerate-risk-audit.py`](../../scripts/lean-axiom-degenerate-risk-audit.py)
adds question 3 as a triage aid, ranking axioms by the signature all five
shared: a **collapsing conclusion** (an equality, `= 0`, `Unique`,
`Subsingleton`) reached from hypotheses a degenerate instance satisfies
vacuously. Its `--selftest` reconstructs the five from git and aborts unless all
five score in the flagged band, so a future narrowing cannot silently report a
clean tree.

It earned that on its first run: the conclusion matcher used an ASCII-only
identifier class and could not see `Φ' = sc.Φstar`, scoring the flagship axiom
below threshold.

**Live: 137 axioms, 22 flagged.**

That figure was wrong twice before it was right, both times too high, and both
corrections were mechanical rather than clever:

| count | what it was counting |
|---:|---|
| 364 | included vendored `.lake/packages` — Mathlib's and Aesop's own **test fixtures**, which declare axioms freely |
| 164 | excluded those, but still parsed inside Lean **block comments** |
| **137** | real top-level axioms |

The comment bug was 26 of 163 matches (19 %) and had two distinct causes worth
naming, because neither is obvious from the outside:

- a documented **post-mortem** — the `LpDualityHypothesisClass.lean` section
  above quotes its two deleted axioms in a ```lean fence, so the audit reported
  an already-refuted axiom as an open candidate;
- ordinary **English prose** — a wrapped sentence beginning "axiom is consumed
  only via …" matches `^axiom\s+\w+`, and there are fourteen: `it`, `of`,
  `and`, `with`, `in`, `is`, `for`, `that`, `can`, `to`, `beyond`, `standing`,
  `audit`, `report`.

Quote 137, and re-run rather than quoting any of these.

**A high score is not evidence of falsity and a low one is not evidence of
soundness.** Only a Lean term settles either.

### First flagged axiom worked, and NOT refuted

`markov_trace_unique_axiom` (`QOU/Hecke/MarkovTrace.lean`) scores 6 and is the
sharpest test available, because I had **cleared it earlier in this same triage
by the citation method**. Its own file even names a gap in prose — *"As stated,
two instances with the same `z_param` are not yet shown equal at the linear-map
level by this class alone — the field set is too weak."*

**It survives the degenerate-instance attack**, and the reason is instructive:
`HeckeAlgebra` carries `spans : Algebra.adjoin R (Set.range embed) = ⊤`, which
is a real guard of the kind the SDP five entirely lacked.

- `n ≤ 1`: `Generator n` is empty, so `spans` forces `A` to be generated by `R`
  alone and the trace is determined by `trace 1 = 1`.
- `n = 2`: `A` is spanned by `{1, σ₁}` modulo the quadratic relation, and both
  are pinned (`normalised`, `trace_gen`).
- `n = 3`: the basis element `σ₁σ₂σ₁` is pinned by no field — but cyclicity plus
  the quadratic relation recover it: `tr(σ₁σ₂σ₁) = tr(σ₂σ₁²) = h·z² + z`.

So the file's caveat is a claim about **provability from these fields**, not a
demonstration of falsity, and the two must not be conflated. Recorded as
*attempted and not refuted*; the axiom stays flagged, and a refutation would
need a genuine `HeckeAlgebra` instance rather than a degenerate one.

## Rule to carry forward

Before clearing any axiom, ask all three questions. Question 3 is answered by
writing the most degenerate instance the axiom's own structures admit and trying
to break it — not by reading the citation more carefully.

---

# Corpus-level: this is the FIFTH incident, and all five share one root cause

Added 2026-09-06, after the `LpDualityHypothesisClass.lean` precedent above
prompted a deliberate search rather than an accidental one.

**Eleven false axioms have now been found in this corpus, across five separate
incidents.** Mine are the largest batch but not the first, second, third or
fourth:

| # | site | axioms found false |
|---|---|---|
| 1 | `QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean` | `b1_hyperbolic_rows` |
| 2 | `QOU/BraidKnot/LpDualityHypothesisClass.lean` | `schrijver_strong_duality`, `schrijver_complementary_slackness` |
| 3 | `QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean` | `dressed_mass_split_substrate_closed_form` |
| 4 | `stochastic-mechanics/macroscopic-stability-equivalence.lean` | `macroscopic_iff_rh_axiom`, `rh_iff_persistence_axiom` |
| 5 | `QOU/MathlibExt/SDP*.lean` (this audit) | the five above |

All four prior post-mortems live inside `/- … -/` blocks; none of the `False`
proofs is compiled, so **the library is not currently inconsistent** from any
of them.

## The shared root cause: over-quantification

Every one of the eleven is the same defect — **a binder that should have been
fixed, or tied to another field, is left free** — and the conclusion then
relates things nothing connects:

- **B1** quantified over `n_hyperbolic_rows_verified`, the very count it meant
  to fix, so it asserted `3 ≤ n` for every `n : ℕ`. Instantiate at `0`.
- **Schrijver** quantified over an `OperatorSelectionLP` whose `primal_obj` and
  `dual_obj` are arbitrary independent reals, so strong duality asserted that
  any two reals are equal.
- **Dressed mass** quantified `F`, `M_N` and `q` mutually unrelated — the left
  side fixed by `F` alone, the right side varying freely with `M_N`.
- **Macroscopic stability** quantified `ψ` and `ζ` independently and asserted an
  *iff* between a property of one and a property of the other.
- **SDP** (this audit) quantified over strict-complementarity pairs without the
  nondegeneracy hypothesis that ties the dual's rank to the primal's.

The fourth site says it in as many words: *"The three fields exist to be related
to **each other**. Quantifying over them independently is precisely the defect
that made the removed axioms inconsistent."*

So the corpus has independently rediscovered one nameable class **five times**,
and written it down five times, each at its own fix site. That is the
propagation gap, measured: not a missing insight, a missing *destination*.

## What follows

1. **Prefer live negations to commented `False` proofs.** Every prior incident
   recorded itself as `theorem X_axiom_is_inconsistent : False` **inside a
   comment**. A commented proof cannot be re-run and goes stale silently — and
   it is also what made the risk audit report `schrijver_strong_duality` as an
   open candidate, since the text is still there to match. This audit's
   `SDPUniquenessCounterexamples.lean` instead proves the **negations** as live,
   compiled theorems, which survive deletion of the axiom and re-verify on every
   build. That should be the standard idiom.

2. **The check belongs in the risk audit, not in five docstrings.**
   Over-quantification is mechanically detectable: a binder appearing on only
   one side of the conclusion, or two binders the conclusion relates with
   nothing tying them. The current script approximates this with its
   "no positivity/rank/nondegeneracy guard" and "universally quantified" signals
   — a direct check is the obvious next refinement.

3. **The count is a floor, not a total.** It counts incidents that were found
   and documented. Nothing here establishes that the remaining 137 axioms are
   sound; 22 are flagged and 21 of those are unexamined.
