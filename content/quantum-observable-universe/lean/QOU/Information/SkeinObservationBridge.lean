import QOU.AppendixSurreals.QCollatz
import QOU.ComputationalHorizon

/-!
# The Skein-observation bridge: q-Collatz halting ↔ the P-vs-NP horizon

**Purpose.** Make explicit, in Lean, the *shared substrate* linking two
QOU-internal reformulations of Millennium-class open problems:

* **q-Collatz** — does every domain-stable positive Skein element reach the
  fundamental cycle? (`QOU.AppendixSurreals.QCollatz.reaches_cycle`.)
* **P-vs-NP** — is the degree-0 observation of a braid computation extractable
  in time polynomial in the crossing count, rather than the naive `3^c`
  resolution-tree cost? (`QOU.ComputationalHorizon`.)

Both live on the **same Skein module** `𝒮(q) ≅ ℤ[q^{±1}]`, both read their
output through the **same observation map** — the Markov trace `tr_M` — and both
ask a *reachability* question about a **discrete dynamical system graded by a
ℕ-valued length/complexity filtration**.

## The structural point (not an ideal)

One might hope to "classify the ideal of Skein relations specific to halting."
There is **no such ideal**. The Skein relations give a *single, fixed* ideal
cutting `ℤ⟨braids⟩` down to `𝒮(q)`, and that ideal yields a **decidable**
invariant (the Markov trace / Jones polynomial is computable). The halting /
hardness content is **not** algebraic: it lives in the **length filtration** of
the reduction dynamics (crossing count `c`; braid length; the `[2]_q`-adic
valuation). By Reeb- / Skein-Turing-completeness (Cardona–Miranda–Peralta-Salas–
Presas) the halting set is undecidable, hence *not* cut out by any ideal.

So the two problems **share the ideal** (⟹ share the decidable observable,
`haltsObserved_of_halts` below) and **differ only in the filtration-reachability
question** they ask. This file packages that shared structure as
`SkeinObservationSystem`, instantiates it for q-Collatz, links its filtration to
the horizon's `3^c` leaf count, and records the **conditional** proof-by-
contradiction skeleton for a residue-based separation.

## Honesty / anti-laundering

Nothing here proves either conjecture. The q-Collatz instance is conditional on
a `[QCollatz Skein]` hypothesis (no fabricated instance); the separation
skeleton `separation_of_residue_nonzero` is a modus-tollens *by design* whose
entire content sits in two **named open hypotheses** — the faithfulness-leg
equivalence (`QOU.Information.PNeqNpEquivalence`, still `sorry`) and the χ(A)
residue non-vanishing. It is the machine-checked *shape* of the argument, not a
resolution of P vs NP (which additionally must clear the algebrization barrier,
Aaronson–Wigderson 2008 — the residue must be a genuinely non-algebraic
cohomological invariant, not polynomial data).

-- Ref: [cardona2021] https://doi.org/10.1073/pnas.2026818118
-/

universe u v

namespace QOU.Information

open QOU.AppendixSurreals

/-- An abstract **Skein-observation system**: a discrete dynamical system on a
    state space `S`, with an observation map `obs : S → V` (the Markov trace), a
    normal-form target (the attractor / unknot), and a ℕ-valued length /
    complexity filtration `len` (crossing count / braid length / `[2]_q`-adic
    valuation). Both the q-Collatz halting problem and the P-vs-NP computational
    horizon are instances. -/
structure SkeinObservationSystem (S : Type u) (V : Type v) where
  /-- One reduction step of the dynamical system (`C_q`; one crossing resolution). -/
  step : S → S
  /-- The observation map: the Markov trace / Jones value the observer reads. -/
  obs : S → V
  /-- The normal-form target — the fundamental cycle / the unknot. -/
  normalForm : S
  /-- The ℕ-valued length/complexity filtration grading the reduction. -/
  len : S → ℕ

namespace SkeinObservationSystem

variable {S : Type u} {V : Type v} (sys : SkeinObservationSystem S V)

/-- **Halting**: the orbit reaches the normal form (the dynamical question). -/
def Halts (P : S) : Prop := ∃ k : ℕ, sys.step^[k] P = sys.normalForm

/-- **Observed halting**: the observed output reaches the normal form's. This is
    the *decidable shadow* — it depends only on the Markov trace, not the full
    dynamics. -/
def HaltsObserved (P : S) : Prop :=
  ∃ k : ℕ, sys.obs (sys.step^[k] P) = sys.obs sys.normalForm

/-- **The general C12**: halting implies observed halting. The observation is a
    functorial shadow of the dynamics — the abstract form of
    `reaches_cycle_observed`. The converse is false in general (distinct states
    can share a Skein value), which is exactly why the observable is *easy* and
    the halting is *hard*. -/
theorem haltsObserved_of_halts (P : S) (h : sys.Halts P) : sys.HaltsObserved P := by
  obtain ⟨k, hk⟩ := h
  exact ⟨k, by rw [hk]⟩

/-- **Descent ⇒ halting**, over a forward-invariant cone graded by `len`.
    Abstract form of `reaches_of_descent_of_forward`: if `len` strictly
    decreases off the normal form on a forward-invariant cone `C`, every element
    of `C` halts. The *open* content of both q-Collatz and P-vs-NP is precisely
    the existence of such a descent for their filtration. -/
theorem halts_of_len_descent (C : S → Prop)
    (hfwd : ∀ x, C x → x ≠ sys.normalForm → C (sys.step x))
    (hdesc : ∀ x, C x → x ≠ sys.normalForm → sys.len (sys.step x) < sys.len x) :
    ∀ x, C x → sys.Halts x :=
  reaches_of_descent_of_forward sys.step sys.normalForm C sys.len hfwd hdesc

/-- **Poly-observability** — the "P" side. Given a length budget `poly`, an
    element is poly-observable if its observed output is reached within
    `poly (len P)` steps: *polynomially* in the filtration level, not the naive
    `3^c` leaf count of the resolution tree (`ComputationalHorizon.numLeaves`).
    This is the bridge form of the P-vs-NP horizon question. Left as an OPEN
    predicate — nothing here proves it holds or fails. -/
def PolyObservable (poly : ℕ → ℕ) (P : S) : Prop :=
  ∃ k ≤ poly (sys.len P), sys.obs (sys.step^[k] P) = sys.obs sys.normalForm

/-- Poly-observability refines observed halting. -/
theorem haltsObserved_of_polyObservable (poly : ℕ → ℕ) (P : S)
    (h : sys.PolyObservable poly P) : sys.HaltsObserved P := by
  obtain ⟨k, _, hk⟩ := h
  exact ⟨k, hk⟩

/-- **P=NP collapse** at the level of one distinguished `universal` state: it is
    poly-observable within the budget. This is the object a hypothetical P=NP
    would furnish; the separation lemma below shows it cannot exist under the
    residue-non-vanishing hypothesis. -/
def PolyCollapse (poly : ℕ → ℕ) (universal : S) : Prop :=
  sys.PolyObservable poly universal

end SkeinObservationSystem

/-! ### Proof-by-contradiction skeleton for a residue-based separation -/

/-- **The lift-and-contradict skeleton.** Suppose the framework's central
    equivalence holds — the P=NP horizon collapse is EQUIVALENT to the vanishing
    of the obstruction residue (`hequiv : PolyCollapse ↔ resZero`) — and the
    residue is provably non-zero (`hres : ¬ resZero`, a topological computation
    of `χ(A)`). Then the collapse cannot occur (`¬ PolyCollapse`): the
    separation.

    Contrapositive reading — exactly the user's "lift an example P=NP and
    contradict": *if* the collapse held, *then* (through the equivalence) the
    residue would vanish, contradicting `hres`.

    **Both hypotheses are open inputs.** `hequiv` is the faithfulness leg
    (`QOU.Information.PNeqNpEquivalence`, still `sorry`); `hres` is the χ(A)
    non-vanishing. This is a modus-tollens *by design* — the machine-checked
    SHAPE of the argument, proving nothing about P vs NP unconditionally, and it
    does NOT by itself clear the algebrization barrier (the residue must be a
    genuinely non-algebraic cohomological invariant for the argument to have
    content). -/
theorem separation_of_residue_nonzero {PolyCollapse resZero : Prop}
    (hequiv : PolyCollapse ↔ resZero) (hres : ¬ resZero) : ¬ PolyCollapse :=
  fun h => hres (hequiv.mp h)

/-! ### q-Collatz as a Skein-observation system -/

/-- The **q-Collatz halting problem** as a Skein-observation system: `step = C_q`,
    `obs` a chosen observation map (the Markov trace into `V`), `normalForm` the
    fundamental 2-cycle attractor, and `len` the intended `[2]_q`-adic descent
    measure (any ℕ-measure typechecks; the valuation is the intended witness).
    Conditional on a `[QCollatz Skein]` instance — no fabricated data. -/
def qCollatzSystem {Skein : Type u} [CommRing Skein] [QCollatz Skein]
    {V : Type v} (obs : Skein → V) (len : Skein → ℕ) :
    SkeinObservationSystem Skein V where
  step := QCollatz.C
  obs := obs
  normalForm := QCollatz.attractor
  len := len

/-- q-Collatz `reaches_cycle` **is** `Halts` in the bridge — the two problems are
    the same reachability question in this abstraction. -/
theorem qCollatzSystem_halts_iff {Skein : Type u} [CommRing Skein] [QCollatz Skein]
    {V : Type v} (obs : Skein → V) (len : Skein → ℕ) (P : Skein) :
    (qCollatzSystem obs len).Halts P
      ↔ ∃ k : ℕ, QCollatz.C^[k] P = QCollatz.attractor :=
  Iff.rfl

/-- The bridge recovers `reaches_cycle_observed`: conditional on the conjecture
    (`QCollatz.reaches_cycle`), a positive q-Collatz orbit's observed output
    stabilises to the attractor's — observed halting to the unknot trace. -/
theorem qCollatzSystem_haltsObserved {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] {V : Type v} (obs : Skein → V) (len : Skein → ℕ) (P : Skein)
    (hP : QCollatz.pos P) : (qCollatzSystem obs len).HaltsObserved P :=
  (qCollatzSystem obs len).haltsObserved_of_halts P (QCollatz.reaches_cycle P hP)

/-! ### The computational horizon supplies the length filtration -/

/-- The horizon's **crossing count** `c` is the natural filtration level: `N`
    Toffoli gates give `c = 3N` crossings and a resolution tree with `3^c`
    leaves, so the brute-force observation cost is exponential in the filtration.
    P-vs-NP asks whether the degree-0 observation is `PolyObservable` with a
    budget sub-exponential in this level. -/
def horizonFiltrationLevel (H : QOU.ComputationalHorizon) : ℕ := H.c

/-- The resolution-tree leaf count is `3` to the filtration level — the naive,
    exponential observation cost the P side must beat. -/
theorem horizon_numLeaves_eq_three_pow_filtrationLevel
    (H : QOU.ComputationalHorizon) :
    H.numLeaves = 3 ^ horizonFiltrationLevel H := H.numLeaves_eq

end QOU.Information
