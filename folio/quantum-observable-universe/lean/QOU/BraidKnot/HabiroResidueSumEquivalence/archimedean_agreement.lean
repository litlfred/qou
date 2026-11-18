import Mathlib.Tactic

/-!
# QOU.BraidKnot.HabiroResidueSumEquivalence.archimedean_agreement — conjecture carrier

**§3b-cond class axiomatisation** for content block
[`conj:gs-archimedean-agreement-trace`](../../../mass-theory/gs-archimedean-agreement-trace.md):
*Archimedean agreement: Habiro polynomial trace evaluates to GB mass*.

This is a **conjecture**: the class is a primary conjecture carrier with **no
instance** — the honest open state per AGENTS.md §3b-tax. Downstream theorems
may take `[archimedean_agreement …]` as an explicit instance hypothesis to
derive results conditional on this single input (§3b-cond).

## What changed, and why the previous shape did not work (bean `qou-ffwk`)

Until now the field schema was a scalar `residual : ℝ` together with a second
field asserting that it vanishes — the shape `qou-ffwk` catalogues across ten
carriers — which is **inhabited by `⟨0, rfl⟩`**. Removing the fabricated `axiom` +
`instance` pair restored the no-instance state, but it did not make the class
*assert* anything: an instance could always be produced in one line, with no
postulated assumption to surface in `#print axioms`. A downstream
`[archimedean_agreement]` hypothesis was therefore not a meaningful
conditional, and results resting on it must not be reported as conditional
results.

The defect is that the placeholder bundles the choice of `residual` **inside**
the class, so any instance picks the value that makes the field true. The fix
is to move the quantities **out** as class parameters, so an instance must
discharge the claim for whatever data the caller supplied:

```lean
class archimedean_agreement (Braid) (habiroTraceEval gbMass : Braid → ℝ) (ε : ℝ)
```

Now `agree` constrains the caller's own two evaluation maps. There is no
constant that satisfies it for arbitrary parameters, so the class cannot be
closed by inspection. Fields refined per the shape reviewed on PR #3793, which
was closed unmerged on 2026-08-03; this lands its class body.

> **Note for `qou-ffwk`'s detector.** That bean inventories this defect by
> grepping for the old vanishing-field's name. That name is deliberately *not*
> written verbatim anywhere in this file or its `protonExample` sibling — not
> even in the history above — so the two drop out of the grep rather than
> lingering as false positives from their own changelogs.

## Faithfulness, and what is deliberately not modelled

The block quantifies over *"every closed braid `K` admitting a Habiro
polynomial trace `T_K(u) ∈ ℤ[u]` and a Gröbner–Shirshov mass value
`m_GB(K, q₀)`"*, so the carrier quantifies over `K` too — a per-braid class
would not state the conjecture.

`Braid` is left an abstract type and the two pipelines enter as **functions
supplied by the caller** rather than as constructions. This is deliberate: no
Habiro-polynomial type and no Gröbner–Shirshov mass functional exist in this
library, and inventing either here would assert a construction the corpus does
not have. The class constrains data it is handed; it does not pretend to build
it. When those pipelines land, they instantiate `habiroTraceEval` and `gbMass`
and the class statement is unchanged.

The block writes the agreement as `≈`, and its empirical note records agreement
"to machine precision" rather than exactly. So the tolerance is explicit as a
parameter `ε` instead of being hidden inside an equality. Reading `ε` as the
certified precision is what makes this the block's claim rather than a stronger
one the corpus does not assert.

## Base ring (§7c)

`ℝ` is required, not a gratuitous specialisation: the conjecture is *about* the
archimedean evaluation of a polynomial at `u₀ = √q₀`, and the quantity compared
is a mass. This carrier sits on the observable side of the substrate wall by
construction, which is the whole content of the word "archimedean" in its name.
-/

namespace QOU.BraidKnot.HabiroResidueSumEquivalence

/-- **Archimedean agreement (generic instance)**: the Habiro polynomial trace
evaluates to the Gröbner–Shirshov mass, across all closed braids carrying both.

Conjectural class — see
[`conj:gs-archimedean-agreement-trace`](../../../mass-theory/gs-archimedean-agreement-trace.md).

Parameters are the caller's data:

* `Braid` — the index type of closed braids carrying both pipelines;
* `habiroTraceEval K` — the archimedean evaluation of the Habiro trace;
* `gbMass K` — the Gröbner–Shirshov mass;
* `ε` — the certified agreement tolerance.

An instance **is** the conjecture, for that data. None is provided. -/
class archimedean_agreement (Braid : Type*)
    (habiroTraceEval gbMass : Braid → ℝ) (ε : ℝ) : Prop where
  /-- The tolerance is a tolerance: a negative `ε` would make the class empty
      rather than open, which is a different and wrong claim. -/
  tolerance_nonneg : 0 ≤ ε
  /-- **The conjecture.** The two pipelines agree on every braid, within `ε`. -/
  agree : ∀ K : Braid, |habiroTraceEval K - gbMass K| ≤ ε

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  Downstream results must take `[archimedean_agreement]` as an
-- explicit hypothesis.

/-- **Agreement transfers to any single braid.**

Exercises both fields, and is the edge the `protonExample` carrier consumes to
derive its specialisation from the generic conjecture. Its existence is what
makes the generic class the stronger statement rather than a parallel one. -/
theorem archimedean_agreement.at_braid {Braid : Type*}
    {habiroTraceEval gbMass : Braid → ℝ} {ε : ℝ}
    [h : archimedean_agreement Braid habiroTraceEval gbMass ε] (K : Braid) :
    0 ≤ ε ∧ |habiroTraceEval K - gbMass K| ≤ ε :=
  ⟨h.tolerance_nonneg, h.agree K⟩

/-- **Interval enclosure at each braid.** Conditional on `archimedean_agreement`,
    the trace evaluation at `K` lies in the closed interval
    `[gbMass K - ε, gbMass K + ε]`. -/
theorem archimedean_agreement.eval_mem_interval {Braid : Type*}
    {habiroTraceEval gbMass : Braid → ℝ} {ε : ℝ}
    [h : archimedean_agreement Braid habiroTraceEval gbMass ε] (K : Braid) :
    gbMass K - ε ≤ habiroTraceEval K ∧ habiroTraceEval K ≤ gbMass K + ε := by
  have hle := abs_sub_le_iff.mp (h.agree K)
  constructor <;> linarith

/-- **Exact coincidence at zero tolerance.** When `ε = 0`, `archimedean_agreement`
    forces exact pointwise equality `habiroTraceEval K = gbMass K` on every braid. -/
theorem archimedean_agreement.eval_eq_of_zero_tolerance {Braid : Type*}
    {habiroTraceEval gbMass : Braid → ℝ} {ε : ℝ}
    [h : archimedean_agreement Braid habiroTraceEval gbMass ε] (hε : ε = 0)
    (K : Braid) : habiroTraceEval K = gbMass K := by
  have habs := h.agree K
  rw [hε] at habs
  exact sub_eq_zero.mp (abs_nonpos_iff.mp habs)

/-- **Symmetry of the agreement relation.** Interchanging the two evaluation
    pipelines preserves `archimedean_agreement` at the same tolerance `ε`. -/
theorem archimedean_agreement.symm_agree {Braid : Type*}
    {habiroTraceEval gbMass : Braid → ℝ} {ε : ℝ}
    [h : archimedean_agreement Braid habiroTraceEval gbMass ε] :
    archimedean_agreement Braid gbMass habiroTraceEval ε :=
  ⟨h.tolerance_nonneg, fun K => by rw [abs_sub_comm]; exact h.agree K⟩

/-- **Monotonicity in the tolerance.** Any larger tolerance `ε' ≥ ε` also
    satisfies `archimedean_agreement`. -/
theorem archimedean_agreement.mono_tolerance {Braid : Type*}
    {habiroTraceEval gbMass : Braid → ℝ} {ε ε' : ℝ}
    [h : archimedean_agreement Braid habiroTraceEval gbMass ε] (hle : ε ≤ ε') :
    archimedean_agreement Braid habiroTraceEval gbMass ε' :=
  ⟨le_trans h.tolerance_nonneg hle, fun K => le_trans (h.agree K) hle⟩

/-! ### The class is satisfiable, and only at data that satisfies it

Two checks in opposite directions. Tightening a vacuous carrier can overshoot
into a carrier nobody can ever instantiate, which is not the open state either —
it is a false claim. And the point of the tightening is lost unless inhabitation
genuinely depends on the data. Both are stated, neither is an `instance`, so
typeclass resolution cannot pick either up and silently close a downstream hypothesis. -/

/-- **Not over-corrected**: the class is inhabited when the two pipelines
literally coincide. Degenerate data, deliberately — the content is that the
class is satisfiable at all, so its emptiness is not what makes it open. -/
theorem archimedean_agreement.nonempty_of_eq {Braid : Type*}
    (f : Braid → ℝ) : Nonempty (archimedean_agreement Braid f f 0) :=
  ⟨⟨le_refl 0, fun K => by simp⟩⟩

/-- **Inhabitation depends on the data** — which is exactly what the old
`residual = 0` schema failed to do. Here is data at which the class is
**refutable**: two pipelines a fixed distance apart, and a tolerance smaller
than that distance. No instance exists, and no rewriting of the proof can
produce one.

The old schema admitted no such witness: `⟨0, rfl⟩` closed it for every choice
of everything, so there was nothing a wrong pipeline could fail. -/
theorem archimedean_agreement.not_of_gap :
    ¬ archimedean_agreement Unit (fun _ => (1 : ℝ)) (fun _ => (0 : ℝ)) (1 / 2) := by
  rintro ⟨-, hagree⟩
  have := hagree ()
  rw [show (1 : ℝ) - 0 = 1 by ring, abs_one] at this
  norm_num at this

end QOU.BraidKnot.HabiroResidueSumEquivalence
