import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.Mirror3d3dCorrespondence — the 3d–3d conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:mirror-3d-3d-correspondence`](mirror-3d-3d-correspondence.md).

**No instance is provided** — the honest open state for a conjecture (AGENTS.md §3b).

## 2026-09-05 — this carrier used to assert nothing

It read, in full:

```lean
class Mirror3d3dCorrespondence where
  holds : Prop
```

A field typed `: Prop` has the *universe* of propositions as its type, so an instance
supplies a proposition rather than a proof of one: `⟨True⟩` discharges it, and every
`[Mirror3d3dCorrespondence]`-conditional theorem was conditional on nothing.

**Prior work, credited.** The defect class is bean `qou-tsnp`'s — *"GAP: 12 conjecture
carriers axiomatised as `holds : Prop` assert nothing"* — which lists this carrier among
its twelve; the census is
[`docs/audits/2026-08-23-free-prop-field-census.md`](../../../docs/audits/2026-08-23-free-prop-field-census.md)
(PR #5562), with a detector at
[`scripts/free-prop-field-audit.py`](../../../scripts/free-prop-field-audit.py). New here is
the **repair**. A library-twin check ran first, per the D11 lesson (#6711), and came back
empty, so unlike D11 the content repair is the right move.

The old header also advertised `../lean/QOU/BraidsAndKnots/Mirror3d3dCorrespondence.lean`
as *"(file pending)"*. **That file does not exist** — the third dead pointer of this kind
found in this queue (D11 and the Kashaev carrier carried the same rot). Dropped.

## What is encoded

The block's one quantitative claim: applied to the Borromean rings complement, the 3d–3d
partition function's **four-loop perturbative coefficient matches the framework's
Markov-trace `h⁴` coefficient, `−3/4`**.

Both coefficient families are **caller parameters**, per the rule recorded in
`QOU/AlgebraicSubstrate/ConditionalClasses.lean` after its own retraction (*"an `∃` over a
quantity you get to pick cannot be false, while a `∀` about a quantity the caller supplies
can"*), so the class is refutable — discharged below rather than asserted.

**Consistency, deliberately:** `−3/4` here is the *same* number D10's carrier constrains as
`h_fourth_eq : levelCoeff 2 = -3/4`
([`nuclear-interactions/spin-from-so3-fiber.lean`](../nuclear-interactions/spin-from-so3-fiber.lean),
PR #6683), where it is the first non-trivial Borromean Markov-trace coefficient. The two
carriers approach it from different sides — a spherical-harmonic level there, a loop order
here — and they are stated so as not to contradict each other.

## 🛑 What is NOT encoded — and one row is excised by an owner ruling

**The `m_p` row of the block's table is deliberately NOT encoded.** The block asserts
*"the proton mass `m_p` as the value of that partition function at `q₀`"*, i.e.
`m_p ↔ Z_{T[B₃]}(q₀)`. AGENTS.md carries a standing **owner ruling of 2026-08-11**:

> **ABSOLUTE MASS EXCISED.** The framework no longer claims, targets, or scores an
> **absolute** nucleon or atomic mass in MeV (`m_p`, `m_n`, `m_⁴He`) as a prediction.

Encoding that row would put a claim in Lean that the owner has excised from the framework.
It is therefore left unstated, and flagged here rather than silently dropped: **whether the
block's table should still carry that row is a question about the physics and is the
author's**, not something to resolve by choosing what to formalise. The `h⁴` row is
dimensionless and is unaffected by the ruling, which is why it is the row encoded.

**Also not encoded — the correspondence itself.** The Dimofte–Gaiotto–Gukov map from a
hyperbolic 3-manifold `M³` to a 3d `N=2` theory `T[M³]`, and the equality of
`Z_{T[M³]}(q)` on the squashed `S³_b` with the state-integral invariant built from `Φ_q`,
need types for a 3d gauge theory and its partition function. The corpus has adjacent
analytic machinery (`Mathlib/BorelStateIntegralSummability.lean`) but no gauge-theory type,
so the coefficients are parameters and this file does **not** claim any partition function
exists or equals a state integral.

Per `qou-tsnp`'s guard — *"if a conjecture's claim cannot yet be stated against existing
types … say so and note what type must grow first"* — **what must grow first is a 3d
`N=2` partition-function type with a perturbative expansion indexed by loop order.**

## Base ring

`ℝ`, since the coefficients are real perturbative data and the block sits on the
observable side. No ordering or transcendental construct is used beyond that.

-- Ref: [manuscript] quantum-observable-universe/q-geometric-langlands/mirror-3d-3d-correspondence.ts
-/

namespace QOU.BraidsAndKnots

/-- **CONJECTURE (3d–3d mirror).** The 3d–3d correspondence applied to the Borromean rings
complement: the four-loop perturbative coefficient of `Z_{T[B₃]}` matches the framework's
Markov-trace `h⁴` coefficient.

`pertCoeff` indexes the gauge-theory side by loop order and `markovCoeff` the framework
side by power of `h`; both are supplied by the **caller**, so the class is false for
families that do not agree at the stated place and value.

**No instance is provided.** Downstream results consume this as
`[Mirror3d3dCorrespondence pertCoeff markovCoeff]` and are genuinely conditional on it.

-- Ref: [manuscript] conj:mirror-3d-3d-correspondence -/
class Mirror3d3dCorrespondence (pertCoeff markovCoeff : ℕ → ℝ) : Prop where
  /-- The gauge-theory four-loop contribution equals the framework's `h⁴` coefficient.
  This is the correspondence's content at the one order the block pins. -/
  four_loop_matches : pertCoeff 4 = markovCoeff 4
  /-- The Borromean Markov-trace `h⁴` coefficient is `−3/4` — the same value D10's carrier
  constrains as `levelCoeff 2`. -/
  borromean_h4 : markovCoeff 4 = -3 / 4

/-- **The gauge-theory four-loop coefficient is `−3/4`** — derived from the two fields
rather than stated as a third. This is the block's actual prediction on the gauge side,
and it follows rather than being assumed. -/
theorem mirror3d3d_four_loop_value (pertCoeff markovCoeff : ℕ → ℝ)
    [h : Mirror3d3dCorrespondence pertCoeff markovCoeff] :
    pertCoeff 4 = -3 / 4 := by
  rw [h.four_loop_matches, h.borromean_h4]

/-- The class is **refutable**, which the previous `holds : Prop` carrier was not: the
constant-zero families agree at every order and so satisfy `four_loop_matches`, but fail
`borromean_h4`.

A theorem rather than a docstring claim, because "the carrier asserts something" is
precisely the property that was missing. -/
theorem mirror3d3dCorrespondence_refutable :
    ¬ Mirror3d3dCorrespondence (fun _ => 0) (fun _ => 0) := by
  intro hc
  have h := hc.borromean_h4
  norm_num at h

end QOU.BraidsAndKnots
