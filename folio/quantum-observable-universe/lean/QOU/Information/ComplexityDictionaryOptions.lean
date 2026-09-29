import QOU.Information.QouPNeqNp
import Mathlib.Tactic

/-!
# QOU.Information.ComplexityDictionaryOptions — options for the degree↔complexity map

"A computation runs on a Turing machine; **observing its result is taking a
trace**."  Correct — and it sharpens the whole difficulty, because *what the
QOU trace natively computes is a COUNT, not a decision bit*.  The Markov trace
`τ(ρ(β_L)) = J_L(q)` is the **Jones polynomial value** — a weighted count of
skein resolutions — so its complexity home is `#P` (counting), while `P` vs
`NP` is about the 1-bit **decision**.  Every dictionary option is a choice of
how to cross that counting→decision gap.

This file lays the options out as opaque propositions (Mathlib has no formal
`P`/`NP`) with their **rigor status made explicit**: which implications are
provable from cited facts (soundness) and which are the open wall
(faithfulness).

## The complexity objects

* `ExactTraceInFP` — the exact observation trace `J_L(q₀)` is polynomial-time.
* `FPeqSharpP` — `FP = #P` (exact counting is easy).
* `PeqNP` — the decision collapse `P = NP`.

## The cited facts (`CitedComplexity`, no instance — literature)

* **JVW** (`jvw_sharpP_hard`): exact evaluation of the Jones polynomial at a
  non-root-of-unity is `#P`-hard, so `ExactTraceInFP → FPeqSharpP`.
* **Toda / `NP ⊆ P^#P`** (`toda_collapse`): if counting is easy the polynomial
  hierarchy collapses, so `FPeqSharpP → PeqNP`.

## The asymmetry (the whole point)

* **SOUNDNESS is provable** (`trace_notInFP_of_sep`): `P ≠ NP ⟹ J_L(q₀) ∉ FP`.
  The trace *does* deliver this direction — counting-hardness follows from
  decision-hardness.
* **FAITHFULNESS is the wall** (`TraceFaithfulness`, no instance):
  `J_L(q₀) ∉ FP ⟹ P ≠ NP` is **not** implied by JVW + Toda.  Counting-hardness
  does not hand you decision-hardness; no known result closes it.

## The dictionary options (each = a way to try to supply faithfulness)

* **Option A — Decision (the framework's degree-0 reading).**  Identify the
  blocked degree-0 observable with the *decision answer* and degree-≥1 leakage
  with *NP witnesses*.  Then horizon opacity = "answer inaccessible" = `P ≠ NP`.
  *Status:* supplies faithfulness **by fiat** — it is exactly an instance of
  `TraceFaithfulness`, i.e. it *assumes* the open step.  (`JetHorizonScaffold.ComplexityDictionary`.)
* **Option B — Counting (the native reading).**  The trace observable is the
  `#P` count `J_L(q₀)`.  *Status:* honest and provable, but yields only
  `FP ≠ #P`, **not** `P ≠ NP` — the direction the framework needs is missing.
* **Option C — Toda soundness.**  Use `NP ⊆ P^#P`.  *Status:* provable, but it
  runs the *wrong way* — it gives `P ≠ NP ⟹ FP ≠ #P`, never the reverse.
* **Option D — BQP (torsion reading).**  At a root of unity the trace
  approximation is `BQP`-complete (AJL).  *Status:* a different axis (`BQP`),
  orthogonal to `P` vs `NP`; no bridge.

Options B–D are each either provable-but-insufficient or off-axis.  Only Option
A reaches `P ≠ NP`, and only by *assuming* faithfulness.  That is the analysis:
**the observation trace gives counting-hardness for free; the counting→decision
step is the entire open problem, and every dictionary that reaches `P ≠ NP`
smuggles it in.**
-/

namespace QOU.Information

/-- The exact observation trace `J_L(q₀)` is polynomial-time computable. -/
opaque ExactTraceInFP : Prop

/-- Exact counting is easy: `FP = #P`. -/
opaque FPeqSharpP : Prop

/-- The decision collapse `P = NP`. -/
opaque PeqNP : Prop

/-- **Cited complexity facts** (no instance — established literature that
    Mathlib cannot express).  JVW `#P`-hardness of the Jones value and Toda's
    `NP ⊆ P^#P`. -/
class CitedComplexity : Prop where
  /-- Jaeger–Vertigan–Welsh: exact Jones evaluation is `#P`-hard, so a
      poly-time trace collapses `FP = #P`. -/
  jvw_sharpP_hard : ExactTraceInFP → FPeqSharpP
  /-- Toda / `NP ⊆ P^#P`: easy counting collapses the hierarchy, `P = NP`. -/
  toda_collapse : FPeqSharpP → PeqNP

/-- **SOUNDNESS is provable (sorry-free).**  `P ≠ NP ⟹ J_L(q₀) ∉ FP`: the
    observation trace *does* deliver counting-hardness from decision-hardness.
    This is the direction the framework gets for free. -/
theorem trace_notInFP_of_sep [C : CitedComplexity] (h : ¬PeqNP) :
    ¬ExactTraceInFP :=
  fun hfp => h (C.toda_collapse (C.jvw_sharpP_hard hfp))

/-- Equivalently: exact Jones evaluation lies outside `FP` once `P ≠ NP`
    (sorry-free). -/
theorem exactTrace_notInFP [CitedComplexity] (h : ¬PeqNP) : ¬ExactTraceInFP :=
  trace_notInFP_of_sep h

/-- **FAITHFULNESS is the wall (open — no instance).**  The reverse implication
    `J_L(q₀) ∉ FP ⟹ P ≠ NP` is *not* a consequence of `CitedComplexity`
    (counting-hardness ⇏ decision-hardness).  Every dictionary option that
    reaches `P ≠ NP` amounts to supplying an instance of this class — i.e.
    *assuming* exactly the open step. -/
class TraceFaithfulness : Prop where
  /-- The conjectural counting→decision transfer. -/
  faithful : ¬ExactTraceInFP → ¬PeqNP

/-- **The wall, made explicit (sorry-free from the hypotheses).**  With the
    cited facts *and* a `TraceFaithfulness` instance, `P ≠ NP` is equivalent to
    `J_L(q₀) ∉ FP`.  The forward direction is free (soundness); the backward
    direction is exactly `TraceFaithfulness` — the open input. -/
theorem sep_iff_trace_notInFP [CitedComplexity] [F : TraceFaithfulness] :
    ¬PeqNP ↔ ¬ExactTraceInFP :=
  ⟨trace_notInFP_of_sep, F.faithful⟩

end QOU.Information
