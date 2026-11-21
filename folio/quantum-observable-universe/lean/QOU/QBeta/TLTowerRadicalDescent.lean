import QOU.QBeta.MarkovTraceQuotient
import QOU.Machinery.MarkovTowerBridge

/-!
# QOU.QBeta.TLTowerRadicalDescent — the tower inclusion and the two radicals

Brick 3 of `qou-s7z2`. Bricks 1 and 2 built the quotient `A / rad τ` and showed
the Hecke generators descend to it. What neither does — and what a
`WenzlTowerStep` instance over `TL_n` still needs — is a relation between the
radicals at **consecutive ranks**. They are different ideals in different
algebras, and nothing so far connects them.

## The hypothesis that connects them

A bare inclusion `ι : Hn →ₐ Hn1` says nothing about the two radicals: membership
in `rad τn1` quantifies over all of `Hn1`, not over `ι '' Hn`, so no amount of
compatibility between `τn` and `τn1` *on the subalgebra* constrains it.

What does connect them is a conditional expectation `ε : Hn1 →ₗ Hn` together
with the level-`n+1` trace being the induced one, `τn1 = τn ∘ ε`
(`MarkovTowerBridge.towerTrace`). Then the bimodule law at `z = 1`
(`epsilon_inclusion_mul`, `ε (ι y * x) = y * ε x`) moves any test element of
`Hn1` back down to `Hn`, and the two radicals become comparable.

## What comes out — reflection, not just preservation

The expected statement is that `ι` carries `rad τn` into `rad τn1`. That holds,
and is the easy direction. The **converse also holds**, because `ε` retracts `ι`
and is therefore surjective, so a test element of `Hn` can always be lifted:
`ι a ∈ rad τn1 ↔ a ∈ rad τn`.

That is worth more than preservation alone. Preservation alone would give a map
of quotients; reflection makes it **injective**, i.e. `TL_n ↪ TL_{n+1}`, which is
what makes the quotients a *tower* rather than a sequence of unrelated algebras.

## Scope

This is still not a `WenzlTowerStep` instance at the Markov trace. It supplies
the tower's injectivity; what remains is assembling that with brick 2's
presentation descent into the class, and — untouched by any of bricks 1–3 —
`HeckeGramFactorial`'s open input, the general `T_w`-basis determinant.

🛑 Measured 2026-09-27: **nothing in the corpus consumes `WenzlTowerStep`** — 27
occurrences, of which 1 class definition, 2 discharge targets and 24 prose mentions,
and **zero** instance-hypothesis positions. So an instance unblocks no consumer, and
at a Hecke carrier its conclusion is free outright
(`isSemisimpleRing_hecke_generic`; see
`QOU.Machinery.HeckeRank.wenzlTowerStep_vacuous_of_isSemisimpleRing`). The sentence
above is kept as the record of what this file did not do; read it as naming an open
question, not a live blocker. Bean `qou-s7z2`.

Note also that `HeckeConditionalExpectation` is itself an OPEN §3b conjecture
class with no instance. Everything here is therefore conditional on it, in the
§3b-cond sense: the implication is proved, the premise is not established.
-/

namespace QOU.QBeta.TLTowerRadicalDescent

open QOU.QBeta.TemperleyLiebTower
open QOU.Machinery.HeckeTower
open QOU.Machinery.MarkovTowerBridge

variable {R : Type*} [Field R] {q : R}
variable {Hn Hn1 : Type*} [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
variable {σn1 : ℕ → Hn1} {rankHi : ℕ} [HeckeBraidedPresentationOfRank q rankHi Hn1 σn1]
variable (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn)

/-- **The inclusion carries the lower radical into the upper one.**

If `a` pairs to zero against all of `Hn`, then `ι a` pairs to zero against all of
`Hn1` under the induced trace — because `ε` moves the test element back down:
`τn1 (ι a * x) = τn (ε (ι a * x)) = τn (a * ε x) = 0`.

The conditional expectation is doing the work. Without it the statement is not
merely unproved but unstateable: nothing would relate a test element of `Hn1` to
one of `Hn`. -/
theorem map_mem_traceRadical
    (inst : HeckeConditionalExpectation R q rankHi Hn Hn1 σn1 ι ε)
    (trn : Hn → R) {a : Hn} (ha : a ∈ traceRadical trn) :
    ι a ∈ traceRadical (towerTrace trn ε) := by
  intro x
  show trn (ε (ι a * x)) = 0
  rw [epsilon_inclusion_mul ι ε inst a x]
  exact ha (ε x)

/-- **And reflects it.** The converse of `map_mem_traceRadical`: if `ι a` is in
the upper radical then `a` is in the lower one.

This direction is where `retract` is spent. A test element `b : Hn` is lifted to
`ι b : Hn1`; the hypothesis applied there gives `τn (a * ε (ι b)) = 0`, and
`ε (ι b) = b`. -/
theorem mem_traceRadical_of_map
    (inst : HeckeConditionalExpectation R q rankHi Hn Hn1 σn1 ι ε)
    (trn : Hn → R) {a : Hn}
    (ha : ι a ∈ traceRadical (towerTrace trn ε)) :
    a ∈ traceRadical trn := by
  intro b
  have h := ha (ι b)
  show trn (a * b) = 0
  rw [show (towerTrace trn ε) (ι a * ι b) = trn (ε (ι a * ι b)) from rfl,
    epsilon_inclusion_mul ι ε inst a (ι b), inst.retract b] at h
  exact h

/-- **The tower inclusion detects the radical exactly.**

Both directions together. This is the statement that makes the quotients a
*tower*: the induced map `Hn / rad τn → Hn1 / rad τn1` is injective, so `TL_n`
sits inside `TL_{n+1}` rather than merely mapping to it. -/
theorem map_mem_traceRadical_iff
    (inst : HeckeConditionalExpectation R q rankHi Hn Hn1 σn1 ι ε)
    (trn : Hn → R) (a : Hn) :
    ι a ∈ traceRadical (towerTrace trn ε) ↔ a ∈ traceRadical trn :=
  ⟨mem_traceRadical_of_map ι ε inst trn, map_mem_traceRadical ι ε inst trn⟩

/-! ### Non-vacuity

The three statements above would be worth nothing if `traceRadical trn` were
always everything or always `{0}` in the situations they apply to. The guard is
the same one brick 1 uses, transported up the tower: when the lower trace does
not kill the unit, the unit is outside both radicals, so neither is everything.
-/

/-- **Non-vacuity: the unit escapes both radicals** when `τn 1 ≠ 0`. The upper
statement is the interesting one — it says the induced trace on `Hn1` is not
identically zero on the image, which is what stops
`map_mem_traceRadical` from being a statement about the whole algebra. -/
theorem one_not_mem_either
    (inst : HeckeConditionalExpectation R q rankHi Hn Hn1 σn1 ι ε)
    (trn : Hn → R) (h : trn 1 ≠ 0) :
    (1 : Hn) ∉ traceRadical trn ∧ ι (1 : Hn) ∉ traceRadical (towerTrace trn ε) := by
  have hlow : (1 : Hn) ∉ traceRadical trn := fun hmem => h (by
    have := hmem 1
    rwa [mul_one] at this)
  exact ⟨hlow, fun hmem => hlow (mem_traceRadical_of_map ι ε inst trn hmem)⟩

end QOU.QBeta.TLTowerRadicalDescent
