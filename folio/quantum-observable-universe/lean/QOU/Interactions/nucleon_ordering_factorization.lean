import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.List.Perm.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.Interactions.nucleon_ordering_factorization

**Proposition** for content block
[`prop:nucleon-ordering-factorization`](../../../nuclear-interactions/nucleon-ordering-factorization.md):
*For a nuclear braid `𝒩(Z, N)` in `H_A(q)` with nucleon ordering
`π = (t₁, …, t_A)`, the Markov trace decomposes by Wedderburn channel:*

  tr_M(𝒩) = W_sym · S(π) + W_std · (z · a_π + b_π) + W_alt · A(π),

*with `S(π) = ∏ₖ(q + d_k)` and `A(π) = ∏ₖ(−q⁻¹ + d_k)` products of
commuting scalars (hence ordering-independent), and `(a_π, b_π)` a `2 × 2`
matrix product over the standard representation.*

## 2026-09-03 — a documented fix that was reverted in bulk

This file's own docstring said, in a dated correction notice:

> *"**Honest `sorry` — and now actually one.**  Until 2026-08-08 this
> docstring said "honest `sorry`" while the body read
> `exact ctx.factorization_ident` … The field is deleted and the body is a
> real `sorry`, so `#print axioms` now agrees with the prose."*

The field was back at line 71 and the body read `ctx.factorization_ident`
again.  This is not prose that drifted: commit `b67ee924e84`, *"Convert
sorry to class fields for all 15 EXT_CITE files"*, re-added
`factorization_ident` and replaced the `sorry` with the projection, in one
diff, leaving the notice describing its own removal standing as a false
claim.  **14 of those 15 files still project a field that commit added**
(measured 2026-09-03: the field name appears in the commit's `+` lines and a
`:= …field` / `exact …field` appears in the file now).

How many of the 14 carry a docstring asserting an absent `sorry` is **not
measured** — a whole-file phrase match says 8 but cannot tell a live claim
from a historical note about the same defect, and a docstring-scoped
refinement finds only 3 projections against 14 by the robust test, so its
pairing is broken.  Treat 8 as an upper bound.  Adjudicated across the batch
in
[`docs/audits/lean-vacuity-review-ledger.json`](../../../../../docs/audits/lean-vacuity-review-ledger.json)
on 2026-08-24, verdict `genuine`.

## Independently found on `main`, and deliberately left to this PR

Commit `78988da5c92` — *"lean: nine docstrings claim their body is a `sorry`;
it is a projection"* — reached the same finding on this file from the
`lean-vacuity-axiom-audit` side, and **scoped its fix to the prose on
purpose**, recording that the projections themselves are
`proof-no-self-assuming-projection`, *"owned by bean `qou-z9ws` / PR #6422"*.
That is this change. The rebase conflicted because that commit corrected the
docstring of the projecting theorem which this commit deletes; the prose it
fixed no longer describes anything, so this side is kept.

Its stated reason for stopping at prose was that *"all nine have external
consumers, so restoring the promised `sorry` would propagate `sorryAx`
outward"*. **For this file that premise does not hold** — measured across
every `.lean` in the repository, nothing outside this file names
`nucleon_ordering_factorization` or `NucleonOrderingFactorizationContext`;
the only hits are an audit document quoting the class name and the chapter
manifest listing the block. Checked here only, not for the other eight.

The scoping decision was right regardless: two agents editing one
declaration's proof content is how a repair gets reverted, which is the very
history this file records below.

## Why the repair is neither of the two obvious options

Restoring the `sorry` undoes what that commit was for — reducing sorries —
and the projection is AGENTS.md §3b-cond item 5.  **Disposition 3 (name the
claim over parameters, assert nothing) is neither**: no `sorry`, no
projection, and no class whose instance chooses the objects the claim is
about.

With `trM_N` and the nine channel quantities as class *fields* the instance
picked all of them, so a `[NucleonOrderingFactorizationContext R]` binder
assumed nothing about anything a caller brought.  As *parameters* the claim
constrains the caller's data, and it becomes something other results can be
proved **from** — which is what `trace_ordering_independent` below does.

## What is proved here, and what is not

* `scalar_channel_ordering_independent` — sub-claim (i), sorry-free: a
  product of commuting scalars is permutation-invariant, so the symmetric
  and alternating channel values do not depend on the nucleon ordering.
* `trace_ordering_independent` — **derived**: two orderings related by a
  permutation, agreeing on the standard channel, give the same Markov
  trace.  This is the manuscript's ordering-independence conclusion, and it
  is obtained from the named decomposition rather than assumed.
* `not_nucleonOrderingFactorization_of_free_data` — the decomposition is
  refutable at freely-chosen data, which is why a `sorry` over it would
  read as "true, not yet proved" about something false.

**Unencoded, stated rather than implied:** the master factorisation itself
— the Wedderburn block decomposition of `H_3(q)` (sym ⊕ std ⊕ alt)
evaluated on the nuclear braid word — needs the Hecke representation-theory
and Markov-trace machinery, which is in `computations/` (GS reduction +
Hoefsmit) and not in Lean.  Nothing here constructs `tr_M`, the Wedderburn
weights, or the standard-representation matrix product; `S(π) = ∏ₖ(q + d_k)`
and `A(π) = ∏ₖ(−q⁻¹ + d_k)` are not tied to `q` either.

**Base ring (§7c).**  Generic `[CommRing R]`: the identity is a sum of
products with no ordering, radical or `Real.*` construct anywhere, so `ℝ`
buys nothing.  Same family as bean `qou-mtcx`.

Bean `qou-z9ws`.
-/

namespace QOU.Interactions

/-- **Scalar-channel ordering independence (derived).**

    Sub-claim (i) of the proposition: the symmetric / alternating channel
    value `∏ₖ f(d_k)` is a product of commuting scalars, so it is invariant
    under any reordering `π → π'` of the nucleon sequence.  Here `ds`/`ds'`
    are the per-nucleon channel data and `f` is the scalar map
    (`f d = q + d` for `S`, `f d = −q⁻¹ + d` for `A`).

    Proved by `List.Perm.prod_eq` — real content, not a projection.

    §7c: stated over a generic commutative monoid.  Permutation-invariance of a
    product uses no ordering, no radical and no `Real.*` construct, so `ℝ` bought
    nothing here; the channel data and the scalar map may even live in different
    types.  The archimedean instance is recovered at `α := ℝ`, `M := ℝ`. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization.md
theorem scalar_channel_ordering_independent {α : Type*} {M : Type*} [CommMonoid M]
    (f : α → M) (ds ds' : List α) (hperm : ds.Perm ds') :
    (ds.map f).prod = (ds'.map f).prod :=
  (hperm.map f).prod_eq

/-- **The claim of `prop:nucleon-ordering-factorization`**, as a proposition
over caller-supplied data:

  `tr_M(𝒩) = W_sym · S(π) + W_std · (z · a_π + b_π) + W_alt · A(π)`.

**Named, not asserted.**  See the module docstring for why neither a
projection nor a `sorry` is the honest form, and for what the master
factorisation would need in order to be derived. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization.md
def nucleon_ordering_factorization {R : Type*} [CommRing R]
    (trM_N W_sym W_std W_alt S_pi a_pi b_pi z A_pi : R) : Prop :=
  trM_N = W_sym * S_pi + W_std * (z * a_pi + b_pi) + W_alt * A_pi

/-- **Ordering independence of the Markov trace** — the proposition's actual
conclusion, *derived* from the decomposition rather than assumed.

Two nucleon orderings related by a permutation, whose symmetric and
alternating channels are the scalar products `∏ₖ fS(d_k)` and `∏ₖ fA(d_k)`
of sub-claim (i) and which agree on the standard channel `z·a_π + b_π`,
give the same Markov trace.

This is why the decomposition is worth naming: it is a hypothesis something
is proved **from**.  The standard channel is a `2 × 2` matrix product and is
*not* ordering-independent in general, which is exactly why its agreement
appears here as a hypothesis rather than as a lemma. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization-proof.md
theorem trace_ordering_independent {α : Type*} {R : Type*} [CommRing R]
    (fS fA : α → R) {ds ds' : List α} (hperm : ds.Perm ds')
    {trM trM' W_sym W_std W_alt a_pi b_pi a_pi' b_pi' z : R}
    (h : nucleon_ordering_factorization trM W_sym W_std W_alt
          (ds.map fS).prod a_pi b_pi z (ds.map fA).prod)
    (h' : nucleon_ordering_factorization trM' W_sym W_std W_alt
          (ds'.map fS).prod a_pi' b_pi' z (ds'.map fA).prod)
    (hstd : z * a_pi + b_pi = z * a_pi' + b_pi') :
    trM = trM' := by
  simp only [nucleon_ordering_factorization] at h h'
  rw [h, h', scalar_channel_ordering_independent fS ds ds' hperm,
    scalar_channel_ordering_independent fA ds ds' hperm, hstd]

/-- **The decomposition is refutable at freely-chosen data**, which is why it
is named rather than carried as a `sorry`.

At `tr_M = 1` with every channel quantity zero it reads `1 = 0`.  Recorded
as a theorem so a later attempt to "finish" this file by adding a `sorry`
over free data fails against a standing counterexample — and so the
2026-08-08 → `b67ee924e84` round trip cannot be repeated silently. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/nucleon-ordering-factorization.md
theorem not_nucleonOrderingFactorization_of_free_data :
    ¬ nucleon_ordering_factorization (1 : ℤ) 0 0 0 0 0 0 0 0 := by
  simp [nucleon_ordering_factorization]

end QOU.Interactions
