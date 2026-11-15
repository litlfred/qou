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
`QOU/AlgebraicSubstrate/ConditionalClasses.lean` after its own retraction — an `∃` over a
quantity the class itself chooses cannot be false, whereas a `∀` about a quantity the
caller supplies can be — so the class is refutable, discharged below rather than asserted.

**Consistency, deliberately:** `−3/4` here is the *same* number D10's carrier constrains as
`h_fourth_eq : levelCoeff 2 = -3/4`
([`nuclear-interactions/spin-from-so3-fiber.lean`](../nuclear-interactions/spin-from-so3-fiber.lean),
PR #6683), where it is the first non-trivial Borromean Markov-trace coefficient. The two
carriers approach it from different sides — a spherical-harmonic level there, a loop order
here — and they are stated so as not to contradict each other.

## What is NOT encoded — and the row that was flagged has since been RESTATED

**The `m_p` row of the block's table is not encoded, and it no longer says `m_p`.** When
this carrier was written the block asserted *"the proton mass `m_p` as the value of that
partition function at `q₀`"*, i.e. `m_p ↔ Z_{T[B₃]}(q₀)`, which the standing **owner ruling
of 2026-08-11** excises:

> **ABSOLUTE MASS EXCISED.** The framework no longer claims, targets, or scores an
> **absolute** nucleon or atomic mass in MeV (`m_p`, `m_n`, `m_⁴He`) as a prediction.

That row was therefore left unstated here and flagged as the author's call rather than
settled by choosing what to formalise. **It has since been ruled on and restated
dimensionlessly**: the block now pairs `Z_{T[B₃]}(q₀)` with the dimensionless Borromean
dressing `F_B = |tr_M(β_B)|·[3]_q!/q³`. Note the row was dimensionally incoherent as well
as ruled out — a partition function is a pure number and `m_p` is carried in MeV.

It stays unencoded here for a *different* reason: which normalisation of `Z_{T[B₃]}`
matches `F_B` is open, and the block now says so. The `h⁴` row was always dimensionless and
unaffected by the ruling, which is why it is the row this carrier encodes.

**Also not encoded — the correspondence itself.** The Dimofte–Gaiotto–Gukov map from a
hyperbolic 3-manifold `M³` to a 3d `N=2` theory `T[M³]`, and the equality of
`Z_{T[M³]}(q)` on the squashed `S³_b` with the state-integral invariant built from `Φ_q`,
need types for a 3d gauge theory and its partition function. The corpus has adjacent
analytic machinery (`Mathlib/BorelStateIntegralSummability.lean`) but no gauge-theory
type. The coefficients are therefore parameters, and this file does **not** claim any
partition function exists or equals a state integral.

Per `qou-tsnp`'s guard — *"if a conjecture's claim cannot yet be stated against existing
types … say so and note what type must grow first"* — **what must grow first is a 3d
`N=2` partition-function type with a perturbative expansion indexed by loop order.**

## Base ring — generic, corrected 2026-09-05

This file first declared the coefficient families over `ℝ`, on the reasoning that *"the
coefficients are real perturbative data and the block sits on the observable side"*. That
was wrong under §7c, and a `wall-side-correct` sweep flagged it **critical**: the file is in
a categorical chapter, and nothing in it is archimedean. There is no ordering, no
`Real.sqrt`, no `Real.log`, no `Real.exp` — the whole content is two equations and a
rational constant, and `-3/4` needs nothing beyond division.

The class is now generic over `{R : Type*} [DivisionRing R]`, which is strictly more
general and clears the wall. The refutability witness instantiates at `ℚ`, leaving no `ℝ`
in the declarations at all.

**Worth recording as a method note, because the flag had been invisible.** The critical did
not appear when this carrier was merged; it appeared when the sidecar was refreshed. The
earlier `wall-side-correct` verdict was a `pass` recorded against a *previous version of
this file*, and a stale sidecar is indistinguishable from a clean one.

-- Ref: [leitner2026] quantum-observable-universe/q-geometric-langlands/mirror-3d-3d-correspondence.ts
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

-- Ref: [leitner2026] conj:mirror-3d-3d-correspondence -/
class Mirror3d3dCorrespondence {R : Type*} [DivisionRing R] (pertCoeff markovCoeff : ℕ → R) :
    Prop where
  /-- The gauge-theory four-loop contribution equals the framework's `h⁴` coefficient.
  This is the correspondence's content at the one order the block pins. -/
  four_loop_matches : pertCoeff 4 = markovCoeff 4
  /-- The Borromean Markov-trace `h⁴` coefficient is `−3/4` — the same value D10's carrier
  constrains as `levelCoeff 2`. -/
  borromean_h4 : markovCoeff 4 = -3 / 4

/-- **The gauge-theory four-loop coefficient is `−3/4`** — derived from the two fields
rather than stated as a third. This is the block's actual prediction on the gauge side,
and it follows rather than being assumed. -/
theorem mirror3d3d_four_loop_value {R : Type*} [DivisionRing R] (pertCoeff markovCoeff : ℕ → R)
    [h : Mirror3d3dCorrespondence pertCoeff markovCoeff] :
    pertCoeff 4 = -3 / 4 := by
  rw [h.four_loop_matches, h.borromean_h4]

/-- The class is **refutable**, which the previous `holds : Prop` carrier was not: the
constant-zero families agree at every order and so satisfy `four_loop_matches`, but fail
`borromean_h4`.

A theorem rather than a docstring claim, because "the carrier asserts something" is
precisely the property that was missing. -/
theorem mirror3d3dCorrespondence_refutable :
    ¬ Mirror3d3dCorrespondence (R := ℚ) (fun _ => 0) (fun _ => 0) := by
  intro hc
  have h := hc.borromean_h4
  norm_num at h

end QOU.BraidsAndKnots
