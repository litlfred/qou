/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.StandardModel.ChiralityGradingConstruction

/-!
# Type-B folding cannot supply the chirality involution

Bean `qou-wqto` (V11), under epic `qou-qia8`.  Continues
[`ChiralityGradingConstruction.lean`](ChiralityGradingConstruction.lean) (V10).

## Why this file exists

V10 constructed the chirality grading and left one thing open: the involution
`ι` on the physical state space is *assumed*, not derived.  Both the bean and
`AGENTS.md` §7b name the same next step —

> Type-B folding (AGENTS.md §7b) remains untried — it would be the route to
> DERIVING the involution rather than taking it as given.

Before building that route, the corpus was grepped for it (per the
"before declaring open" checklist).  It is **not** untried: the conjecture
[`type-b-folding-cpt`](../../nuclear-interactions/type-b-folding-cpt.md)
already states the folding, with the involution `ι : αᵢ ↔ α_{n-i}` on the
`𝔰𝔩ₙ` Cartan datum, and adds the reading that matters here:

> *Stable matter = fixed points of the folded crystal; antimatter = the
> `ι`-orbit complement.*

That reading collides with V10's existence criterion, and the collision is a
theorem rather than a matter of taste.  V10 proved
`free_of_reeb_odd_grading`: a **globally** `ι`-odd grading forces `ι` to have
**no fixed point**.  The folding conjecture places stable matter exactly *at*
the fixed points.  The two cannot both hold of one involution.

## What is proved here

Three statements, in increasing specificity:

* `stable_matter_and_global_chirality_incompatible` — no involution both fixes
  something and carries a global odd grading.  The bare dilemma.
* `no_state_chirality_of_folding_fixed_point` — the obstruction **transfers**
  along any map intertwining a folding involution with a state involution.  A
  fixed point upstairs kills the grading downstairs.  This is the form that
  bites, because the proposed route is exactly such a map.
* `folding_inducing_gen1_chirality_is_free` — instantiated at the corpus's own
  eight-state sector: any folding that induces `flipChirality` is itself
  fixed-point free, hence has **no stable matter in the conjecture's sense**.

## Scope — this is scope-(a), and deliberately so

Per the "before declaring refuted" discipline, the honest reading is the
scope-limited one:

**What is excluded.**  The Type-B folding involution, *read as the conjecture
reads it* (fixed points = stable matter), cannot itself be the chirality
involution.  That exclusion is backed by a proved invariant — a fixed-point /
parity obstruction — so on the (a)/(b) rubric it is genuinely structural *for
that identification*.

**What is NOT excluded, and must not be read as excluded.**  Type-B folding
retains every other role the conjecture gives it: the bar-involution
invariance of GS normal forms, the C/P/T decomposition, and the crystal
structure.  Folding may still *contain* the chirality datum — via an orbit
map, a sub-crystal, or a second involution on the folded object — just not by
its own fixed-point involution serving directly as `ι`.  Nothing here says the
route is dead; it says one identification inside the route is.

**No claim is made about which involution is correct.**  The geometric
identification V10 left open is still open.  This narrows the search rather
than closing it, which is the point of formalizing before running it.
-/

namespace QOU.StandardModel.Chirality

/-- **The dilemma.**  One involution cannot both fix a state and admit a
globally odd grading.

Read against the folding conjecture: "stable matter = fixed points" and "there
is a chirality grading odd under this involution" are inconsistent as claims
about a single `ι`. -/
theorem stable_matter_and_global_chirality_incompatible
    {State : Type*} (ι : State → State) :
    ¬ ((∃ s, ι s = s) ∧ (∃ chir : State → Bool, ∀ t, chir (ι t) = ! chir t)) := by
  rintro ⟨⟨s, hs⟩, ⟨chir, hodd⟩⟩
  exact free_of_reeb_odd_grading ι chir hodd s hs

/-- **The obstruction transfers along an intertwiner.**

`π` maps the folded crystal to the physical state space and intertwines the
folding involution `foldι` with the state involution `stateι` — this is
precisely what "the folding *induces* the chirality involution" means.  Then a
single fixed point of `foldι` (one piece of stable matter) rules out any
globally odd grading downstairs.

Note `π` need be neither injective nor surjective: the obstruction is carried
by one point, so no structure on `π` beyond equivariance is required. -/
theorem no_state_chirality_of_folding_fixed_point
    {Crystal State : Type*} (foldι : Crystal → Crystal) (stateι : State → State)
    (π : Crystal → State) (hnat : ∀ c, π (foldι c) = stateι (π c))
    {c : Crystal} (hfix : foldι c = c) :
    ¬ ∃ chir : State → Bool, ∀ t, chir (stateι t) = ! chir t := by
  rintro ⟨chir, hodd⟩
  have hs : stateι (π c) = π c := by rw [← hnat c, hfix]
  exact free_of_reeb_odd_grading stateι chir hodd (π c) hs

/-- **Contrapositive, as the usable form.**  A global grading forces the
involution free, i.e. forbids stable matter in the folding conjecture's
fixed-point sense. -/
theorem global_chirality_forces_no_fixed_matter
    {State : Type*} (ι : State → State) (chir : State → Bool)
    (hodd : ∀ t, chir (ι t) = ! chir t) :
    ¬ ∃ s, ι s = s := by
  rintro ⟨s, hs⟩
  exact free_of_reeb_odd_grading ι chir hodd s hs

/-- **Instantiated at the corpus's own sector.**

`flipChirality` on `Gen1Quark` is free (V10, `flipChirality_free`, by
inspection of the eight states).  So *any* folding involution that induces it
is free as well — it has no fixed point at all, hence no stable matter in the
sense the folding conjecture assigns to fixed points.

This is the sharp form of the finding: the separation is not hypothetical.
The corpus already carries a chirality involution with a *proved* fixed-point
structure, and it is the opposite of the folding conjecture's. -/
theorem folding_inducing_gen1_chirality_is_free
    {Crystal : Type*} (foldι : Crystal → Crystal) (π : Crystal → Gen1Quark)
    (hnat : ∀ c, π (foldι c) = flipChirality (π c)) :
    ∀ c, foldι c ≠ c := by
  intro c hfix
  have : flipChirality (π c) = π c := by rw [← hnat c, hfix]
  exact flipChirality_free (π c) this

end QOU.StandardModel.Chirality
