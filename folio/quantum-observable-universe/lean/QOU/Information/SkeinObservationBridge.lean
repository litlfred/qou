import QOU.AppendixSurreals.QCollatz
import QOU.ComputationalHorizon
import QOU.FluidDynamics.q_bkm_criterion

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

/-- The resolution-tree horizon `3^n` exceeds its input `n` for every `n`, so a
    linear observation budget never reaches the exponential cost. (The exponential
    `3^n` in fact dominates every polynomial eventually; `n < 3^n` is the piece the
    linear-budget corollary needs.) -/
theorem lt_three_pow (n : ℕ) : n < 3 ^ n := by
  induction n with
  | zero => norm_num
  | succ k ih =>
    have hpos : 1 ≤ 3 ^ k := Nat.one_le_pow k 3 (by norm_num)
    rw [pow_succ]
    omega

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

/-! #### The q-Navier–Stokes leg: regularity vs. finite-time blow-up

The **third** filtration question. A vortex flow of the brane fluid is a braid
word `β(t) ∈ H_n(q)` evolving in time; its closure is a knotted vortex tube, its
conserved **helicity is the Markov-trace observation** (`obs`), and its crossing
number is the length filtration `len` (see `fluid-dynamics/helicity-conservation`,
`braid-fluid`, `TwoVortexChannelAlgebra`). q-NS smoothness asks whether `len`
stays **bounded** along the orbit — no finite-time singularity — the q-analog of
Beale–Kato–Majda (`QOU.FluidDynamics.q_bkm_criterion`). This is the same
filtration that q-Collatz asks to *descend* and P-vs-NP asks to be *polynomial*. -/

/-- **Regularity / no finite-time blow-up** (q-NS): the length filtration stays
    bounded by `B` along the whole orbit — the vortex-knot complexity never
    diverges. -/
def Regular (B : ℕ) (P : S) : Prop := ∀ k : ℕ, sys.len (sys.step^[k] P) ≤ B

/-- **Blow-up**: the filtration is unbounded along the orbit — the finite-time
    singularity of a q-NS solution (negation of regularity for every bound). -/
def BlowsUp (P : S) : Prop := ∀ B : ℕ, ∃ k : ℕ, B < sys.len (sys.step^[k] P)

/-- A regular orbit does not blow up. -/
theorem not_blowsUp_of_regular (B : ℕ) (P : S) (h : sys.Regular B P) :
    ¬ sys.BlowsUp P := by
  intro hb
  obtain ⟨k, hk⟩ := hb B
  exact absurd (h k) (not_le.mpr hk)

/-- **Non-increasing filtration ⇒ regularity** (bound = initial complexity). The
    abstract shadow of q-BKM: a monotone Lyapunov filtration (bounded / decaying
    enstrophy — the vortex-knot complexity never grows) rules out finite-time
    blow-up. The same monotonicity that drives q-Collatz descent gives q-NS
    regularity; only P-vs-NP additionally demands the descent be *polynomially
    fast*. -/
theorem regular_of_len_nonincreasing (P : S)
    (hmono : ∀ k : ℕ, sys.len (sys.step^[k + 1] P) ≤ sys.len (sys.step^[k] P)) :
    sys.Regular (sys.len P) P := by
  intro k
  induction k with
  | zero => simp
  | succ n ih => exact le_trans (hmono n) ih

/-- **Enstrophy Lyapunov filtration bound ⇒ regularity (`qou-a6vt`).**
    If an enstrophy / Lyapunov functional `E : S → ℕ` dominates the complexity
    filtration (`∀ x, sys.len x ≤ E x`) and is non-increasing along the orbit of `P`,
    then the orbit is `Regular` with bound `E P`. -/
theorem regular_of_lyapunov_filtration (E : S → ℕ) (P : S)
    (hcoercive : ∀ x : S, sys.len x ≤ E x)
    (hdecay : ∀ k : ℕ, E (sys.step^[k + 1] P) ≤ E (sys.step^[k] P)) :
    sys.Regular (E P) P := by
  have hE : ∀ k : ℕ, E (sys.step^[k] P) ≤ E P := by
    intro k
    induction k with
    | zero => simp
    | succ n ih => exact le_trans (hdecay n) ih
  intro k
  exact le_trans (hcoercive (sys.step^[k] P)) (hE k)

/-- **Enstrophy Lyapunov filtration bound ⇒ no finite-time blow-up (`qou-a6vt`).** -/
theorem not_blowsUp_of_lyapunov_filtration (E : S → ℕ) (P : S)
    (hcoercive : ∀ x : S, sys.len x ≤ E x)
    (hdecay : ∀ k : ℕ, E (sys.step^[k + 1] P) ≤ E (sys.step^[k] P)) :
    ¬ sys.BlowsUp P :=
  sys.not_blowsUp_of_regular (E P) P (sys.regular_of_lyapunov_filtration E P hcoercive hdecay)

/-! #### Cross-pollination: the q-Collatz and q-NS walls are one missing lemma

The q-Collatz descent (`halts_of_len_descent`) and the q-NS regularity
(`regular_of_len_nonincreasing`) consume a hypothesis on the **same** filtration
`len`. So a single controlled descent along the orbit — non-increasing, and
strictly dropping whenever the state is not yet at the normal form — yields
**both** conclusions at once. A result on the descent of one leg transfers
directly to the other. -/

/-- **One descent, two walls.** A globally non-increasing filtration that
    additionally drops strictly off the normal form gives **both** q-NS
    regularity (bounded by the initial complexity) **and** q-Collatz halting.
    The two open walls share one missing ingredient — a controlled descent on
    the Skein filtration; P-vs-NP is the same descent with the *polynomial-rate*
    refinement added. -/
theorem regular_and_halts_of_len_orbit_descent (P : S)
    (hmono : ∀ k : ℕ, sys.len (sys.step^[k + 1] P) ≤ sys.len (sys.step^[k] P))
    (hstrict : ∀ k : ℕ, sys.step^[k] P ≠ sys.normalForm →
        sys.len (sys.step^[k + 1] P) < sys.len (sys.step^[k] P)) :
    sys.Regular (sys.len P) P ∧ sys.Halts P := by
  refine ⟨sys.regular_of_len_nonincreasing P hmono, ?_⟩
  apply sys.halts_of_len_descent (fun y => ∃ k : ℕ, sys.step^[k] P = y)
  · rintro x ⟨k, rfl⟩ _
    exact ⟨k + 1, by rw [Function.iterate_succ_apply']⟩
  · rintro x ⟨k, rfl⟩ hx
    have h := hstrict k hx
    rwa [Function.iterate_succ_apply'] at h
  · exact ⟨0, rfl⟩

/-! #### P-vs-NP rate leg: the `3^c` horizon cost separates `PolyObservable`
from `HaltsObserved`

`HaltsObserved` asks only that the observation is *eventually* reached;
`PolyObservable` asks that it is reached within a *polynomial* budget. The gap is
the P-vs-NP question. When a system's observation is reachable **only** at the
naive resolution-tree cost `3^{\text{len}}` — the exponential horizon
(`horizon_numLeaves_eq_three_pow_filtrationLevel`) — it is observed-halting but
beats every budget the horizon exceeds. -/

/-- **Exponential horizon cost ⇒ not poly-observable.** If every observation-match
    happens no earlier than the resolution-tree cost `3^{len P}` (`hcost`), then no
    polynomial budget the horizon exceeds (`poly (len P) < 3^{len P}`) suffices —
    the P-vs-NP separation, with the exponential lower bound `hcost` taken as the
    (genuinely hard) hypothesis rather than proved. -/
theorem not_polyObservable_of_horizon_cost (poly : ℕ → ℕ) (P : S)
    (hcost : ∀ k : ℕ,
        sys.obs (sys.step^[k] P) = sys.obs sys.normalForm → 3 ^ sys.len P ≤ k)
    (hgap : poly (sys.len P) < 3 ^ sys.len P) :
    ¬ sys.PolyObservable poly P := by
  rintro ⟨k, hk, hobs⟩
  have hc := hcost k hobs
  omega

/-- **Concrete separation.** A system with exponential horizon cost is not
    poly-observable under the identity (linear) budget — `lt_three_pow` discharges
    the gap unconditionally, so the exponential lower bound alone yields the
    separation. -/
theorem not_polyObservable_id_of_horizon_cost (P : S)
    (hcost : ∀ k : ℕ,
        sys.obs (sys.step^[k] P) = sys.obs sys.normalForm → 3 ^ sys.len P ≤ k) :
    ¬ sys.PolyObservable id P :=
  sys.not_polyObservable_of_horizon_cost id P hcost (lt_three_pow _)

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

/-! ### A concrete crossing-reduction vortex flow, and the corpus q-BKM link

The q-NS leg above is abstract; here it is grounded two ways. First, a **concrete
crossing-reduction flow** — the vortex-knot complexity is `n : ℕ`, each step
resolves one crossing (`n ↦ n − 1`), the observation is the complexity itself,
and the normal form is the unknot `0`. It is unconditionally `Halts` **and**
`Regular`, so the q-NS predicates are non-vacuous (as `qCollatzSystem` grounds
the q-Collatz leg). Second, a **conditional transport** of the corpus q-BKM
criterion (`QOU.FluidDynamics.q_bkm_criterion`) onto the bridge's no-blow-up /
bounded-filtration predicates. -/

/-- A concrete vortex flow: crossing-count `n : ℕ`, one crossing resolved per step
    (`n ↦ n − 1`), observation = the complexity, normal form = the unknot `0`. -/
def vortexReductionSystem : SkeinObservationSystem ℕ ℕ where
  step := fun n => n - 1
  obs := id
  normalForm := 0
  len := id

/-- The crossing-reduction flow is **regular** — its complexity is non-increasing,
    so it never blows up (bound = the initial crossing number). -/
theorem vortexReductionSystem_regular (P : ℕ) :
    vortexReductionSystem.Regular P P := by
  have h := vortexReductionSystem.regular_of_len_nonincreasing P ?_
  · simpa using h
  · intro k
    rw [Function.iterate_succ_apply']
    exact Nat.sub_le _ 1

/-- The crossing-reduction flow **halts** — every knot resolves to the unknot `0`
    (the complexity strictly descends off `0`). -/
theorem vortexReductionSystem_halts (P : ℕ) :
    vortexReductionSystem.Halts P :=
  vortexReductionSystem.halts_of_len_descent (fun _ => True)
    (fun _ _ _ => trivial)
    (fun _ _ hx => Nat.sub_lt (Nat.pos_of_ne_zero hx) one_pos) P trivial

/-- **The shared descent exists on the concrete vortex flow.** Firing
    `regular_and_halts_of_len_orbit_descent` on `vortexReductionSystem`: its
    crossing-count reduction is a genuine controlled descent, so it yields q-NS
    regularity **and** q-Collatz-style halting from the single hypothesis — a
    concrete, unconditional witness that the shared-descent machinery is
    non-vacuous. (The real q-Collatz descent measure `μ` on `ℤ[q^{±1}]` remains
    the open wall — it is *not* constructed here, only exhibited on this toy
    reduction.) -/
theorem vortexReductionSystem_regular_and_halts (P : ℕ) :
    vortexReductionSystem.Regular P P ∧ vortexReductionSystem.Halts P := by
  have h := vortexReductionSystem.regular_and_halts_of_len_orbit_descent P ?_ ?_
  · simpa using h
  · intro k
    rw [Function.iterate_succ_apply']
    exact Nat.sub_le _ 1
  · intro k hk
    rw [Function.iterate_succ_apply']
    exact Nat.sub_lt (Nat.pos_of_ne_zero hk) one_pos

/-- **The corpus q-BKM criterion is the bridge's regularity dichotomy.** Given a
    `QBKMContext` whose `extendsSmoothly` / `vorticityIntegralFinite` predicates
    are modelled by the bridge's *no blow-up* / *bounded filtration* predicates,
    the q-BKM iff (`QOU.FluidDynamics.q_bkm_criterion`) transports to
    `noBlowUp ↔ boundedFiltration` — i.e. q-NS smoothness **is** the filtration-
    boundedness question the bridge poses. The two modelling hypotheses are
    explicit; nothing is assumed silently. -/
theorem regular_iff_bkm {R : Type*} [CommRing R] [ctx : QOU.FluidDynamics.QBKMContext R]
    (noBlowUp boundedFiltration : Prop)
    (hsmooth : ctx.extendsSmoothly ↔ noBlowUp)
    (hvort : ctx.vorticityIntegralFinite ↔ boundedFiltration) :
    noBlowUp ↔ boundedFiltration :=
  hsmooth.symm.trans (QOU.FluidDynamics.q_bkm_criterion.trans hvort)

end QOU.Information
