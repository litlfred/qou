import QOU.Information.SkeinObservationBridge

/-!
# QOU.Information.SkeinCounterfactual — what a counterexample would BE, on each leg

**Purpose.** The three QOU-internal Millennium reformulations are three predicates
on one shared object `SkeinObservationSystem` (see `SkeinObservationBridge`):

| Leg | Predicate | "false" means |
|---|---|---|
| q-Collatz | `Halts` | some orbit never reaches the normal form |
| q-Navier–Stokes | `Regular B` | `BlowsUp` — the filtration is unbounded |
| P-vs-NP | `PolyObservable poly` | the observation IS reachable in budget |

This file asks the **counterfactual**: *suppose a leg were false — what object would
the counterexample be, and what would it destroy?* The answers are contrapositives
of the bridge's descent lemmas, and they are sharper than "the conjecture fails":

* a q-Collatz counterexample **refutes every descent measure** on every
  forward-invariant cone containing it (`not_descent_of_not_halts`);
* a q-NS blow-up witness **refutes every monotone Lyapunov filtration** on that
  orbit (`not_len_nonincreasing_of_blowsUp`);
* a counterexample on *either* leg destroys the **shared** orbit-descent
  ingredient that `regular_and_halts_of_len_orbit_descent` uses to get both
  (`not_orbit_descent_of_counterexample`) — the two walls do not fail
  independently.

The P-vs-NP direction of this already exists sorry-free upstream
(`no_horizon_cost_of_polyObservable`, `not_polyObservable_or_not_horizon_cost` in
`SkeinHorizonLowerBound`); this file adds the other two to the same pattern and
then records the fact all three share.

## A scalar cannot decide halting POINTWISE — and what that does not show

Each predicate is a predicate on `P : S` — it varies **within** a fixed universe,
at a fixed substrate parameter, whereas an obstruction class evaluated at a fixed
`q₀` is one scalar for the whole universe (`thm:qou-obstruction-reduction`:
`dim_k Obs = 1`). A state-independent verdict can only be equivalent to a
predicate that is **constant** on states (`const_of_scalar_faithful`), and
halting is **not** constant — `stallAbove` below halts at `1` and not at `2`
(`stallAbove_halts_one`, `stallAbove_not_halts_two`, hence
`halts_not_constant`). So `no_scalar_faithful_to_halts`: no scalar is faithful to
halting **pointwise in the state**.

**This does not bar the obstruction route, and must not be read as doing so.**
The corpus never claims pointwise faithfulness. Every faithfulness claim it makes
is scalar ↔ a *single universally-quantified* proposition — `κ_C = 0` iff
**every** element reduces (`conj:q-collatz`); `NS(A) = 0` iff **the universe** is
NS-regular (`def:ns-obstruction`); `PNeqNPInQOU` is already `¬ ∃ c k, ∀ m n, …`
(`CountingModuliGrade`). A scalar *can* be faithful to a `∀`-statement — trivially,
`⟨_, Iff.rfl⟩` inhabits `∃ v, (v ↔ ∀ P, Halts P)`. So the result below is a
**scope-(a)** statement about one claim shape, not a structural exclusion of the
route. The genuine barrier for that route is the genericity argument in
`ObstructionGenericity` plus algebrization, and it is argued there, not here.

## Correction record (2026-08-15)

An earlier revision of this docstring claimed "the type mismatch alone bars the
route, before any barrier from complexity theory is invoked" — a scope-(b)
structural exclusion with no proved invariant covering the corpus's actual claim
shape. It was wrong: it attacked pointwise faithfulness, which nothing in the
corpus asserts. Caught by adversarial review before merge; the theorems were
sound, only the interpretation was over-claimed. Recorded per AGENTS.md
§"Before declaring refuted".

## Honesty / anti-laundering

Nothing here proves or refutes any of the three conjectures. Every theorem is a
contrapositive of an existing sorry-free descent lemma, or a statement about what
a hypothetical counterexample would destroy. The `stallAbove` witness is a
two-line dynamical system, **not** a Skein module — it establishes only that
`Halts` is non-constant in general. No claim is made that the q-Collatz cone
itself has a non-halting element; that is the open conjecture.

-- Ref: [cardona2021] https://doi.org/10.1073/pnas.2026818118
-/

universe u v

namespace QOU.Information

namespace SkeinObservationSystem

variable {S : Type u} {V : Type v} (sys : SkeinObservationSystem S V)

/-! ### The q-Collatz counterfactual: a non-halting orbit kills every descent -/

/-- **A q-Collatz counterexample refutes every descent measure.** If `P` does not
    halt, then for every forward-invariant cone `C` containing `P` there is **no**
    strict `len`-descent off the normal form. Contrapositive of
    `halts_of_len_descent`: the open content of q-Collatz is the *existence* of
    such a descent, so a single non-halting orbit destroys every candidate at
    once — not merely the one being tested. -/
theorem not_descent_of_not_halts (C : S → Prop) (P : S) (hC : C P)
    (hfwd : ∀ x, C x → x ≠ sys.normalForm → C (sys.step x))
    (hnot : ¬ sys.Halts P) :
    ¬ (∀ x, C x → x ≠ sys.normalForm → sys.len (sys.step x) < sys.len x) := by
  intro hdesc
  exact hnot (sys.halts_of_len_descent C hfwd hdesc P hC)

/-! ### How hard is "find a descent measure"? Exactly as hard as the conjecture.

`halts_of_len_descent` is the corpus's route to q-Collatz: exhibit a filtration
that strictly drops off the normal form, and halting follows. The open core is
routinely described as *the descent measure* (`conj:collatz-contact-boundary`,
`PNeqNpWallUnification`, `collatz_obstruction_link`), with `v_[2]` refuted
scope-(a) in `collatz_vtwo_obstruction`.

It is worth knowing, before any further search, that the descent route is not a
*shortcut*. Descent is **equivalent** to halting on a forward-invariant cone, not
merely sufficient for it: if every element of the cone halts, the **hitting
time** `μ(x) = min {k | step^[k] x = normalForm}` is itself a strict ℕ-valued
descent measure. So "some descent measure exists" carries exactly the content of
the conjecture and cannot be established more cheaply.

**What this does and does not say.** It does **not** devalue the descent route —
the point of `halts_of_len_descent` is to let an *explicit, independently
motivated* `μ` (a valuation, a degree, a contact volume) discharge the
conjecture, and that remains the live programme. What it rules out is treating
"search for a descent measure" as a strictly easier target than "prove
q-Collatz": any search whose success criterion is mere existence is searching
for a restatement. A candidate `μ` is worth pursuing only for properties the
hitting time lacks — computability, a closed form, monotonicity under the
algebra of `[2]_q` and `[3]_q`.

Scope (a): a statement about the *route*, not about q-Collatz, which is
untouched here. -/

/-- **The hitting time is a descent measure.** If every element of a
    forward-invariant cone halts, then the step count to the normal form strictly
    decreases off it — so a descent measure exists. -/
theorem exists_descent_of_halts (C : S → Prop)
    (hfwd : ∀ x, C x → x ≠ sys.normalForm → C (sys.step x))
    (hhalt : ∀ x, C x → sys.Halts x) :
    ∃ μ : S → ℕ, ∀ x, C x → x ≠ sys.normalForm → μ (sys.step x) < μ x := by
  classical
  refine ⟨fun x => if h : sys.Halts x then Nat.find h else 0, fun x hx hne => ?_⟩
  have hxh : sys.Halts x := hhalt x hx
  have hsh : sys.Halts (sys.step x) := hhalt _ (hfwd x hx hne)
  dsimp only
  rw [dif_pos hxh, dif_pos hsh]
  -- the hitting time of `x` is positive, since `x` is not already the normal form
  have hpos : 0 < Nat.find hxh := by
    rcases Nat.eq_zero_or_pos (Nat.find hxh) with h0 | h; swap; · exact h
    exact absurd (by simpa [h0] using Nat.find_spec hxh) hne
  -- one step of `x` reaches the normal form in `Nat.find hxh - 1` further steps
  have hstep : sys.step^[Nat.find hxh - 1] (sys.step x) = sys.normalForm := by
    have := Nat.find_spec hxh
    rwa [← Nat.succ_pred_eq_of_pos hpos, Function.iterate_succ_apply] at this
  exact lt_of_le_of_lt (Nat.find_le hstep) (Nat.pred_lt hpos.ne')

/-- **Descent ⟺ halting on the cone.** Combining with `halts_of_len_descent`:
    the existence of a strict descent measure is not a sufficient condition that
    might be easier to verify — it carries exactly the conjecture's content. -/
theorem exists_descent_iff_halts (C : S → Prop)
    (hfwd : ∀ x, C x → x ≠ sys.normalForm → C (sys.step x)) :
    (∃ μ : S → ℕ, ∀ x, C x → x ≠ sys.normalForm → μ (sys.step x) < μ x) ↔
      (∀ x, C x → sys.Halts x) := by
  constructor
  · rintro ⟨μ, hdesc⟩
    exact fun x hx =>
      QOU.AppendixSurreals.reaches_of_descent_of_forward
        sys.step sys.normalForm C μ hfwd hdesc x hx
  · exact fun h => exists_descent_of_halts sys C hfwd h

/-! ### The q-NS counterfactual: blow-up kills every monotone Lyapunov -/

/-- **A q-NS blow-up witness refutes every monotone Lyapunov filtration.** If the
    orbit of `P` blows up, the filtration cannot be non-increasing along it.
    Contrapositive of `regular_of_len_nonincreasing` — the abstract shadow of
    "bounded enstrophy rules out blow-up", read backwards: exhibiting a
    singularity is exactly exhibiting a failure of monotone complexity. -/
theorem not_len_nonincreasing_of_blowsUp (P : S) (hblow : sys.BlowsUp P) :
    ¬ (∀ k : ℕ, sys.len (sys.step^[k + 1] P) ≤ sys.len (sys.step^[k] P)) := by
  intro hmono
  exact sys.not_blowsUp_of_regular (sys.len P) P
    (sys.regular_of_len_nonincreasing P hmono) hblow

/-! ### The shared ingredient: one counterexample kills BOTH walls

`regular_and_halts_of_len_orbit_descent` derives q-NS regularity *and* q-Collatz
halting from a single orbit-descent hypothesis. So the contrapositive says the
two walls are not independent: a counterexample on **either** leg refutes the
shared ingredient, hence removes the common route to the **other**. -/

/-- **One counterexample, two walls.** If `P` either blows up or fails to halt,
    the shared orbit-descent hypothesis (non-increasing, and strictly dropping off
    the normal form) fails at `P`. A q-NS singularity and a q-Collatz divergent
    orbit cannot both be ruled out by one descent lemma — whichever appears first
    destroys the route to both. -/
theorem not_orbit_descent_of_counterexample (P : S)
    (hcex : sys.BlowsUp P ∨ ¬ sys.Halts P) :
    ¬ ((∀ k : ℕ, sys.len (sys.step^[k + 1] P) ≤ sys.len (sys.step^[k] P)) ∧
       (∀ k : ℕ, sys.step^[k] P ≠ sys.normalForm →
          sys.len (sys.step^[k + 1] P) < sys.len (sys.step^[k] P))) := by
  rintro ⟨hmono, hstrict⟩
  obtain ⟨hreg, hhalts⟩ := sys.regular_and_halts_of_len_orbit_descent P hmono hstrict
  rcases hcex with hblow | hnh
  · exact sys.not_blowsUp_of_regular (sys.len P) P hreg hblow
  · exact hnh hhalts

/-! ### The strong form, and its exact scope: **one system, two questions**

`not_orbit_descent_of_counterexample` above says a counterexample on either leg
destroys the *shared proof ingredient*. That is a statement about methods. The
lemmas here upgrade it to a statement about the **objects**, within a **single**
system: when the normal form is periodic, an orbit whose filtration is unbounded
cannot reach it. Boundedness and descent are not independent questions *of one
instance*.

**Scope — this does NOT identify a Navier–Stokes singularity with a q-Collatz
divergence (correction, 2026-08-15).** Every lemma below fixes one
`sys : SkeinObservationSystem S V` and one `P : S`, reading `BlowsUp` and
`Halts` off the *same* `step`, `normalForm` and `len`. The corpus instantiates
the two legs as **different systems**: q-Collatz is `qCollatzSystem` (`step =
QCollatz.C` on the Skein module, and `len` a caller-supplied parameter — the
bridge concedes "any ℕ-measure typechecks"), while the concrete NS instance is
`vortexReductionSystem` on `ℕ`. On the latter `BlowsUp` is outright
unsatisfiable, since `vortexReductionSystem_regular` proves it regular. So the
transfer couples two questions asked of **one instance**; it says nothing about
one leg's counterexample being the other's.

An earlier revision of this header claimed exactly that ("a q-NS singularity
witness is automatically a q-Collatz divergence witness"). It was wrong for the
reason above — conflating a shared *type* with a shared *instance*, which is the
same conflation as the two prior corrections on this branch, one abstraction
level up. Caught by adversarial review before merge.

The hypothesis is **periodicity** of the normal form, `IsPeriodicPt step p
normalForm` with `0 < p`, and it is carried explicitly on every statement rather
than assumed globally.

**Why periodicity and not a fixed point (correction, 2026-08-15).** The first
version of this section assumed `step normalForm = normalForm`. That hypothesis
is not merely restrictive, it is **provably false** for the corpus's q-Collatz
system: `QCollatz` carries `attractor_not_fixed : C attractor ≠ attractor`
alongside `attractor_period_two : C (C attractor) = attractor`, because the
attractor is the **2-cycle** `{q⁻¹, 1 + q⁻¹}`, the q-lift of the classical
`{1, 2}`. So the fixed-point form of this transfer was *vacuous on the one
instance it was written for*. Periodicity is the hypothesis that actually holds
— `attractor_period_two` is exactly `IsPeriodicPt C 2 attractor` — and the
argument goes through unchanged, because an orbit that lands in a finite cycle
still has bounded complexity. Caught before merge; recorded per AGENTS.md
§"Report honest negatives". -/

/-- Reaching a **periodic** normal form pins every later state to a point of the
    cycle: past the landing time `k`, the orbit is `step^[i] normalForm` for some
    `i < p`. -/
theorem iterate_mem_cycle_of_ge {p : ℕ} (hp : 0 < p)
    (hper : Function.IsPeriodicPt sys.step p sys.normalForm)
    (P : S) (k : ℕ) (hk : sys.step^[k] P = sys.normalForm) :
    ∀ j, k ≤ j → ∃ i, i < p ∧ sys.step^[j] P = sys.step^[i] sys.normalForm := by
  intro j hj
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hj
  refine ⟨d % p, Nat.mod_lt _ hp, ?_⟩
  rw [Nat.add_comm k d, Function.iterate_add_apply, hk]
  exact (hper.iterate_mod_apply d).symm

/-- **Halting bounds the filtration.** A halting orbit lands in the normal form's
    cycle and thereafter visits only finitely many states, so its complexity
    never exceeds the maximum over the finite prefix together with the cycle.
    The bound is explicit and depends on `P` — no uniform bound is claimed. -/
theorem regular_of_halts {p : ℕ} (hp : 0 < p)
    (hper : Function.IsPeriodicPt sys.step p sys.normalForm)
    (P : S) (h : sys.Halts P) : ∃ B : ℕ, sys.Regular B P := by
  obtain ⟨k, hk⟩ := h
  refine ⟨(Finset.range (k + 1)).sup (fun i => sys.len (sys.step^[i] P)) ⊔
      (Finset.range p).sup (fun i => sys.len (sys.step^[i] sys.normalForm)), fun j => ?_⟩
  rcases le_or_gt j k with hjk | hkj
  · exact le_sup_of_le_left (Finset.le_sup (f := fun i => sys.len (sys.step^[i] P))
      (Finset.mem_range.mpr (Nat.lt_succ_of_le hjk)))
  · obtain ⟨i, hip, hji⟩ := iterate_mem_cycle_of_ge sys hp hper P k hk j hkj.le
    rw [hji]
    exact le_sup_of_le_right
      (Finset.le_sup (f := fun i => sys.len (sys.step^[i] sys.normalForm))
        (Finset.mem_range.mpr hip))

/-- **Blow-up excludes halting, within one system.** When the normal form is
    periodic — as the q-Collatz attractor is, by `attractor_period_two` — an
    orbit with unbounded filtration cannot reach it. The boundedness question and
    the descent question are not independent *of the same instance*.

    **Not a cross-leg identification.** `sys` is one system; see the section
    header. The corpus's two legs are different instances, and on the concrete
    NS instance this hypothesis is unsatisfiable. -/
theorem not_halts_of_blowsUp {p : ℕ} (hp : 0 < p)
    (hper : Function.IsPeriodicPt sys.step p sys.normalForm)
    (P : S) (hblow : sys.BlowsUp P) : ¬ sys.Halts P := by
  intro h
  obtain ⟨B, hreg⟩ := regular_of_halts sys hp hper P h
  exact sys.not_blowsUp_of_regular B P hreg hblow

/-- **Contrapositive.** A halting orbit never blows up — q-Collatz convergence at
    an orbit gives q-NS regularity at that orbit for free, with an explicit
    bound. The implication is one-directional: bounded complexity does **not**
    imply halting (a bounded orbit may cycle forever without reaching the normal
    form), which is exactly why descent is the harder question. -/
theorem not_blowsUp_of_halts {p : ℕ} (hp : 0 < p)
    (hper : Function.IsPeriodicPt sys.step p sys.normalForm)
    (P : S) (h : sys.Halts P) : ¬ sys.BlowsUp P :=
  fun hblow => not_halts_of_blowsUp sys hp hper P hblow h

end SkeinObservationSystem

/-- **The q-Collatz instance discharges the periodicity hypothesis.** Recorded as
    a lemma rather than asserted in prose: `attractor_period_two` *is*
    `IsPeriodicPt` at `p = 2`, definitionally. Both prior corrections on this
    branch were "asserted about the instance, never checked against it", so the
    discharge is machine-checked here. -/
theorem qCollatzSystem_normalForm_periodic {Skein : Type u} [CommRing Skein]
    [QOU.AppendixSurreals.QCollatz Skein] {V : Type v}
    (obs : Skein → V) (len : Skein → ℕ) :
    Function.IsPeriodicPt (qCollatzSystem obs len).step 2
      (qCollatzSystem obs len).normalForm :=
  QOU.AppendixSurreals.QCollatz.attractor_period_two

namespace SkeinObservationSystem

variable {S : Type u} {V : Type v} (sys : SkeinObservationSystem S V)

/-! ### The leg-independent bar: a scalar cannot decide a state predicate -/

/-- **A state-independent scalar can only decide a constant predicate.** If a
    single truth value `v` (the "obstruction is non-zero at `q₀`" verdict, which
    carries no dependence on the state `P`) is equivalent to `Pred P` for every
    `P`, then `Pred` is constant on states.

    This is the state-indexed form of `ObstructionVerdictCap.verdict_cap`, which
    is the same `Iff` algebra with the quantifier stripped; the two are kept
    apart only because that module carries no dependency on this one. See the
    module docstring for what this does **not** show. -/
theorem const_of_scalar_faithful {Pred : S → Prop} {v : Prop}
    (hfaithful : ∀ P, v ↔ Pred P) (P Q : S) : Pred P ↔ Pred Q :=
  (hfaithful P).symm.trans (hfaithful Q)

end SkeinObservationSystem

/-! ### A concrete witness that `Halts` is not constant

`stallAbove` sends everything at most `1` to the normal form `0` and fixes
everything above it. So `1` halts and `2` does not — an unconditional,
two-line refutation of "the halting predicate is constant on states". -/

/-- Collapse `{0,1}` to the normal form; stall everywhere above. -/
def stallAbove : SkeinObservationSystem ℕ ℕ where
  step := fun n => if n ≤ 1 then 0 else n
  obs := id
  normalForm := 0
  len := id

/-- `1` halts under `stallAbove`, in one step. -/
theorem stallAbove_halts_one : stallAbove.Halts 1 := ⟨1, by norm_num [stallAbove]⟩

/-- Every iterate fixes `2`: the stalled orbit never moves. -/
theorem stallAbove_iterate_two (k : ℕ) : stallAbove.step^[k] 2 = 2 := by
  induction k with
  | zero => rfl
  | succ n ih => rw [Function.iterate_succ_apply', ih]; norm_num [stallAbove]

/-- `2` does not halt under `stallAbove`. -/
theorem stallAbove_not_halts_two : ¬ stallAbove.Halts 2 := by
  rintro ⟨k, hk⟩
  rw [stallAbove_iterate_two k] at hk
  exact absurd hk (by norm_num [stallAbove])

/-- **`Halts` is not a constant predicate.** Hence, by `const_of_scalar_faithful`,
    no state-independent scalar verdict is equivalent to halting. The obstruction
    route needs an invariant that varies over states — which a one-dimensional
    `Obs` evaluated at a fixed `q₀` does not supply. -/
theorem halts_not_constant :
    ¬ (∀ P Q : ℕ, stallAbove.Halts P ↔ stallAbove.Halts Q) := by
  intro h
  exact stallAbove_not_halts_two ((h 1 2).mp stallAbove_halts_one)

/-- **No scalar is faithful to halting POINTWISE (sorry-free).** No
    state-independent verdict `v` satisfies `∀ P, v ↔ Halts P` on `stallAbove`.

    **Scope (a).** This excludes the *pointwise* claim shape only. It does **not**
    exclude a scalar faithful to the universally-quantified statement
    `∀ P, Halts P` — that is trivially inhabited, and it is the shape the corpus
    actually uses. See the module docstring's correction record. -/
theorem no_scalar_faithful_to_halts (v : Prop) :
    ¬ (∀ P : ℕ, v ↔ stallAbove.Halts P) := by
  intro hfaithful
  exact halts_not_constant fun P Q =>
    SkeinObservationSystem.const_of_scalar_faithful hfaithful P Q

end QOU.Information
