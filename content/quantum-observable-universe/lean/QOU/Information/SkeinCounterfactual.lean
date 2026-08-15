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

/-! ### The strong form: a q-NS counterexample **is** a q-Collatz counterexample

`not_orbit_descent_of_counterexample` above says a counterexample on either leg
destroys the *shared proof ingredient*. That is a statement about methods. The
lemmas here upgrade it to a statement about the **objects**: on a system whose
normal form is a fixed point, blow-up and halting are outright incompatible, so a
q-NS singularity witness is automatically a q-Collatz divergence witness.

The fixed-point hypothesis `step normalForm = normalForm` is a real hypothesis,
carried explicitly and never assumed globally: the q-Collatz attractor is the
**2-cycle** `{q⁻¹, 1 + q⁻¹}`, not a fixed point (`conj:q-collatz`), so the
transfer applies to normal-form-as-fixed-point systems and the cyclic case needs
the orbit-level argument instead. Stating it with the hypothesis visible is the
honest scope. -/

/-- Once the orbit reaches a **fixed** normal form it stays there. -/
theorem iterate_normalForm_of_ge (hfix : sys.step sys.normalForm = sys.normalForm)
    (P : S) (k : ℕ) (hk : sys.step^[k] P = sys.normalForm) :
    ∀ j, k ≤ j → sys.step^[j] P = sys.normalForm := by
  intro j hj
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hj
  clear hj
  induction d with
  | zero => simpa using hk
  | succ n ih =>
    rw [show k + (n + 1) = (k + n) + 1 by ring, Function.iterate_succ_apply', ih, hfix]

/-- **Halting bounds the filtration.** A halting orbit is eventually constant at
    the normal form, so its complexity never exceeds the maximum reached on the
    finite prefix before it lands. The bound is explicit. -/
theorem regular_of_halts (hfix : sys.step sys.normalForm = sys.normalForm)
    (P : S) (h : sys.Halts P) : ∃ B : ℕ, sys.Regular B P := by
  obtain ⟨k, hk⟩ := h
  refine ⟨(Finset.range (k + 1)).sup (fun i => sys.len (sys.step^[i] P)), fun j => ?_⟩
  rcases le_or_gt j k with hjk | hkj
  · exact Finset.le_sup (f := fun i => sys.len (sys.step^[i] P))
      (Finset.mem_range.mpr (Nat.lt_succ_of_le hjk))
  · rw [iterate_normalForm_of_ge sys hfix P k hk j hkj.le, ← hk]
    exact Finset.le_sup (f := fun i => sys.len (sys.step^[i] P))
      (Finset.mem_range.mpr (Nat.lt_succ_of_le le_rfl))

/-- **Blow-up excludes halting.** The two walls do not fail independently: on a
    system with a fixed normal form, a q-NS singularity witness *is* a q-Collatz
    divergence witness. Nothing chooses which leg the object belongs to. -/
theorem not_halts_of_blowsUp (hfix : sys.step sys.normalForm = sys.normalForm)
    (P : S) (hblow : sys.BlowsUp P) : ¬ sys.Halts P := by
  intro h
  obtain ⟨B, hreg⟩ := regular_of_halts sys hfix P h
  exact sys.not_blowsUp_of_regular B P hreg hblow

/-- **Contrapositive.** A halting orbit never blows up — q-Collatz convergence on
    an orbit gives q-NS regularity on it for free, with an explicit bound. The
    implication is one-directional: bounded complexity does **not** imply
    halting (a bounded orbit may cycle forever), which is exactly why q-Collatz
    is the harder leg. -/
theorem not_blowsUp_of_halts (hfix : sys.step sys.normalForm = sys.normalForm)
    (P : S) (h : sys.Halts P) : ¬ sys.BlowsUp P :=
  fun hblow => not_halts_of_blowsUp sys hfix P hblow h

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
