-- Probe: the bare-`Prop`-field carrier shape, stated for the SHAPE rather than
-- for named carriers.
--
-- Companion to `2026-08-23-free-prop-field-triviality-probe.lean`, which
-- demonstrates the same triviality by reproducing three real carriers verbatim
-- (`DimMasterPentagon`, `BringSurfaceSmoothness`, `HabiroFlowSolution`) and
-- discharging each with `⟨True, …⟩`. That probe has priority and this file does
-- not supersede it; what is added here is (a) the statement for the abstract
-- shape rather than for three instances, and (b) the conjunction case, which the
-- earlier probe exhibits in `HabiroFlowSolution` but does not state.
--
-- WHY THIS LIVES IN docs/audits/ AND NOT IN THE LIBRARY TREE.
-- `scripts/free-prop-field-audit.py` globs `content/**/*.lean`. A demonstration
-- carrier is, by construction, an instance of the very defect that audit counts,
-- so putting one in `content/` adds a permanent false positive to an active drain
-- queue (bean `qou-tsnp`). It was in
-- `QOU/ProofHygiene/SelfAssumingContexts.lean` briefly and did exactly that —
-- 2 fields, reported under `PropUniverseWithConjunction`. Moved here, where the
-- 2026-08-23 probe already sits for the same reason.
--
-- Self-contained: no imports, so it needs nothing from the Lake workspace.

namespace ProbePropUniverse

/-- A carrier whose field is typed `: Prop` — the *universe* of propositions. The
field supplies a proposition, not a proof of one. -/
structure PropUniverseContext where
  claim : Prop

/-- It is inhabited outright. No hypothesis, no conclusion, nothing established. -/
theorem propUniverse_inhabited : Nonempty PropUniverseContext := ⟨⟨True⟩⟩

/-- **The harm.** Any theorem stated conditional on such a carrier is
unconditional — the hypothesis discharges itself. So a `[C]`-conditional result
downstream of one is conditional on nothing, and §3b-cond's conditional-class
exception does not apply to it however the block is labelled. -/
theorem conditional_on_propUniverse_is_unconditional {P : Prop}
    (h : PropUniverseContext → P) : P :=
  h ⟨True⟩

/-- **A conjunction field does not rescue it** — the case
`2026-08-23-free-prop-field-triviality-probe.lean` exhibits in
`HabiroFlowSolution` (whose `all_hold` conjoins its three `Prop`-typed fields)
without stating it for the shape.

A conjunction is exactly what an author adds on being told the carrier asserts
nothing, and it changes nothing at all: the conjuncts are *propositions*, so
`True ∧ True` discharges it. The repair is to type the fields by actual
propositions, never to conjoin propositions-as-values. -/
structure PropUniverseWithConjunction where
  p : Prop
  q : Prop
  all_hold : p ∧ q

theorem propUniverseWithConjunction_inhabited :
    Nonempty PropUniverseWithConjunction :=
  ⟨⟨True, True, ⟨trivial, trivial⟩⟩⟩

/-- **The discriminator is the field's TYPE.** A carrier whose field is typed by
an actual proposition is *not* unconditionally inhabited: at `False` it has no
instance at all, while `PropUniverseContext` always does. So `claim : Prop`
versus `claim : C` is the whole difference, and a reader settles it by looking at
the field rather than at the docstring. -/
structure PropFieldContext (C : Prop) where
  claim : C

theorem propField_of_false_not_inhabited : ¬ Nonempty (PropFieldContext False) := by
  rintro ⟨ctx⟩
  exact ctx.claim

theorem discriminator :
    Nonempty PropUniverseContext ∧ ¬ Nonempty (PropFieldContext False) :=
  ⟨propUniverse_inhabited, propField_of_false_not_inhabited⟩

end ProbePropUniverse
