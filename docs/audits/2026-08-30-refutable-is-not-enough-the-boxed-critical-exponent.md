# Refutable is not enough: a carrier can be perfectly falsifiable and still assert something nobody derived

**Date:** 2026-08-30 · **Bean:** `qou-4670`
**Corrects:** my own re-encoding of `QOU.AlgebraicSubstrate.CriticalExponent`, landed earlier the same day under `qou-93hu`

---

## The claim

`CriticalExponent`'s re-encoded field, `alpha_eq : α = 4 / 3`, asserted as
settled a value the corpus explicitly calls **open**. It survived the arc's own
gate because that gate tests refutability, and `α = 4/3` is refutable.

Fixed by transcribing the upstream carrier instead: `0 < α` plus the divergence
statement, with the value of `α` left open.

## The evidence

[`fluid-dynamics/p2-critical-exponent.md`](../../content/quantum-observable-universe/fluid-dynamics/p2-critical-exponent.md)
gives the exponent under a heading that announces its own status —
*"**Result (closure-dependent — two heuristic values, neither rigorous).**"* —
and offers two:

| closure | exponent |
|---|---|
| dissipation, `ε = ν_q·Ω` | `α = 1` |
| Kolmogorov cascade, `E(k) ~ k^{-5/3}` truncated at `N_eff` | `α = 4/3`, **up to logs** |

followed, verbatim, by:

> *"Neither closure is rigorous; the true `α` is fixed by the actual
> `q`-Navier–Stokes enstrophy spectrum (the turbulence-closure problem) and is
> open. The two values bracket it under their respective hypotheses."*

So the field took the larger of two bracketing candidates and wrote it into a
Lean class as an equation. Under its own closure the estimate is
`Ω_max ≲ (q-1)^{-4/3}(ln(q-1)^{-1})^{4/3}` — not a clean power law, so `4/3` is
not exactly right even there.

**And the corpus had already decided against exactly this**, six weeks earlier:

- Bean `qou-15gb`, **completed** 2026-07-18, is that reconciliation — *"state
  each conditional on named closure"*.
- `regularity-breakdown.ts` `authorNotes`: the exponent *"is now presented as
  closure-dependent, not a single boxed value"*.
- The established encoding names its closure in the declaration itself:
  `QOU.FluidDynamics.enstrophy_alpha_one_of_dissipation_closure`
  ([`q_ns_classical_bridge.lean:135`](../../content/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_classical_bridge.lean)).
- The **upstream** carrier `QOU.FluidDynamics.CriticalExponent`
  ([`p2-critical-exponent.lean`](../../content/quantum-observable-universe/fluid-dynamics/p2-critical-exponent.lean))
  leaves the exponent unconstrained and says so: *"the divergence rate is not
  encoded, and `criticalExponent` is accordingly unconstrained by any field of
  this class."*

A closure-free `α = 4/3` in `QOU.AlgebraicSubstrate` re-boxed the value one
namespace over.

## Why the gate did not catch it — the generalisable part

The arc's gate is
[`2026-08-30-qns-carriers-are-refutable.lean`](2026-08-30-qns-carriers-are-refutable.lean),
and its whole argument is that **compilation is not the gate; refutability is**,
because an `∃` over a quantity the class picks for itself cannot be false.

`α = 4/3` passes that test without difficulty. `CriticalExponent 2` is false;
`CriticalExponent (4/3)` is inhabited; the field quantifies over a
caller-supplied parameter; it is in the shape of the claim. Every property the
gate was built to check, it has.

**Refutability rules out the vacuous carrier. It does not rule out the
fabricated one.** They are different failure modes with opposite signatures:

| | vacuous | fabricated |
|---|---|---|
| can the field be false? | **no** | yes |
| does the corpus assert it? | n/a — it says nothing | **no** |
| caught by | a Lean witness | a corpus-grep |

The second question has to be asked separately, and no proof in a Lean file can
stand in for it: *is the proposition this field states one the corpus actually
asserts?* I ran the six-path grep for the vacuity — "has this carrier been
fixed already?" — and not for the number. The number is where the content was.

This is the same shape as the `sorry`-free-≠-derived rule AGENTS.md already
carries, one level down: a **statement** can be well-formed, non-trivial and
falsifiable and still have no derivation behind it. Draining vacuity is exactly
the moment the risk appears, because filling an empty field means writing
something, and the cheapest thing to write is the most specific-looking number
in the neighbourhood.

**Practical rule.** When you replace a vacuous field with a numeric or
closed-form claim, grep that *value* before committing — not the carrier, not
the topic. If the source hedges it, the hedge belongs in the encoding: either
name the closure, or state only the unhedged part.

## The fix

```lean
class CriticalExponent (enstrophy : ℝ → ℝ) (α : ℝ) : Prop where
  alpha_pos : 0 < α
  enstrophy_diverges :
    ∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
      ∃ q : ℝ, 1 < q ∧ q - 1 < ε ∧ M < enstrophy q
```

Both fields transcribed from upstream; nothing chosen by me. This is what the
`.md` asserts without hedging — *"maximum enstrophy diverges as
`Ω_max(q) ~ (q-1)^{-α}` for some `α > 0`"* — and it is strictly more content
than the boxed value gave, since the divergence itself was never encoded here
at all.

Consumers in `ConditionalCorollaries.lean`: `critical_exponent_identity` (which
concluded `3α = 4` from the fabricated premise — a sound derivation from an
unsound hypothesis) is replaced by `critical_exponent_enstrophy_unbounded`; the
`α = 4/3` conjunct of `qNS_cone_full_composition` is replaced by the divergence
consequence. `SurrealRateCalculus.lean` no longer binds the class at all — a
sibling dropped the decorative binders on `main` before I got there.

## What is still open, and is not closed by this

The asymptotic `Ω_max(q) ~ (q-1)^{-α}` relating the class's two parameters is
absent here **and upstream**. Encoding it needs the asymptotic; pinning `α`
needs a closure that is not rigorous. That gap is the honest open state and
choosing a number does not close it.

## Verification

lean-direct against the restored Mathlib oleans; no `lake build` (a build over
a restored cache with `traces=0` evicts it).

| file | exit | `sorry` |
|---|---|---|
| `QOU/AlgebraicSubstrate/ConditionalClasses.lean` | **0** | 0 |
| `QOU/AlgebraicSubstrate/ConditionalCorollaries.lean` | **0** | 0 |
| `QOU/AlgebraicSubstrate/SurrealRateCalculus.lean` | **0** | 0 |
| `docs/audits/2026-08-30-qns-carriers-are-refutable.lean` | **0** | 0 |

`SurrealRateCalculus` emits two pre-existing Mathlib deprecation warnings
(`mul_lt_mul_left`, `mul_lt_mul_right`) that this change does not touch.

The gate file now carries **two** refutations for this carrier, one per field —
a non-positive `α`, and a bounded enstrophy — and a real satisfiability
witness, `enstrophy q = (q-1)⁻¹` at `α = 1`, which needs the ε-argument rather
than being a one-liner.

## Two side observations, recorded rather than acted on

**Bean `qou-k3hh` is stale at `todo`.** It reports that
`p2-critical-exponent.lean` and `p5-counterexample.lean` state strictly less
than their `.md` — the missing `q → 1` and `t → T*⁻` neighbourhood quantifiers
— with verified counterexample witnesses. Both files on `main` now carry those
quantifiers and cite the witness probe by name, so the proposed one-line fix has
landed. Not flipping the status here: it is another agent's bean, I have checked
only the two clauses named in its title, and it also carries a `conj:levi-degeneracy`
observation and a disclosed `ChiralityFactorClass` hit that I have not checked.

**The local carriers are much weaker than the upstream ones they claim to
re-declare**, and this is worth someone's attention beyond the one defect fixed
here. `ConditionalClasses.lean` opens by saying it *"re-declares the upstream
conjecture classes"*; measured, upstream `QAubinLions` has 5 parameters and 6
fields against the local 1-and-1, and upstream `RegularityBreakdown` has 5 and 6
against 1 and 1. Weaker hypotheses make stronger theorems, so nothing downstream
is wrong — but a `[QAubinLions K]` binder read as recording a dependency on
`conj:q-aubin-lions` records much less than the conjecture. `BlowupYekutieli`
is the extreme case: the local class is about a *blow-up rate* and the upstream
one is about *obstruction-class vanishing*, which is not a weakening but a
different proposition sharing a name — see
[`2026-08-30-blowup-yekutieli-has-no-source.md`](2026-08-30-blowup-yekutieli-has-no-source.md)
and bean `qou-88nf`.
