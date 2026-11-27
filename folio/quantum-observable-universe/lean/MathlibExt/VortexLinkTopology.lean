import Mathlib.Tactic

set_option autoImplicit false

/-!
# `QOU.FluidDynamics.VortexLinkTopology` — the discrete core of vortex-line linking

NS attack vector 2 (bean `qou-p6tm`).  This file formalises the **combinatorial**
half of the classical argument "smooth ideal flow preserves vortex-line topology,
so a topology change needs a crossing change (reconnection)".  It proves nothing
about Euler or Navier–Stokes; see the audit
`docs/audits/2026-10-12-ns-v2-vortex-topology.md` for what is, and is not, carried
to the PDE.

## Set-up

A braid word on `n + 1` strands is a list of letters `(i, e)`, `i : Fin n`, meaning
the Artin generator `σᵢ` (`e = true`) or `σᵢ⁻¹` (`e = false`).  We run the word on
a state consisting of

* `pos : Fin (n+1) → Fin (n+1)` — which strand **label** occupies each position;
* `C : Fin (n+1) → Fin (n+1) → ℤ` — the **signed crossing matrix**: `C a b` is the
  signed number of crossings between strands `a` and `b` so far (symmetric).

For a pure braid the strands are the components of the closure and `C a b / 2`
is the linking number `lk(a, b)` (half the signed inter-component crossing sum,
the standard diagrammatic definition).

## What is proved (all sorry-free, no axioms beyond Lean's core three)

1. `run_R2` — Reidemeister II (`σᵢ^e σᵢ^{-e}` = identity) leaves the state unchanged.
2. `run_braid` — the braid relation `σᵢσᵢ₊₁σᵢ = σᵢ₊₁σᵢσᵢ₊₁` (either sign, i.e.
   Reidemeister III) produces the **same** state.
3. `run_far` — far commutation `σᵢσⱼ = σⱼσᵢ` (`|i-j| ≥ 2`) produces the same state.
4. `run_congr` — these local equalities propagate to any context `w₁ ++ u ++ w₂`.
   Hence the crossing matrix (so every pairwise linking number) is invariant under
   every move that does **not** change a crossing: the discrete form of
   "an isotopy preserves linking".
5. `crossingChange_C` — replacing one letter `σᵢ^e` by `σᵢ^{-e}` changes `C` by exactly
   `-2·sgn e` on the pair `{a, b}` of strands crossing there and leaves every other
   entry unchanged; with injective labelling `a ≠ b` (`crossing_labels_ne`), so the
   linking number `lk(a,b)` moves by exactly `∓1` (`crossingChange_lk`).
6. `crossingChange_mutualHelicity` — for strand circulations `Γ`, the mutual
   (linking) helicity `Σₓ Σᵧ (C x y / 2) Γₓ Γᵧ` (= `2 Σ_{x<y} lk Γₓ Γᵧ`, Moffatt 1969)
   changes by exactly `-2·sgn e·Γₐ·Γ_b` under a crossing change, and is invariant
   under the moves of (1)–(3).
7. `hopf_C` — falsifiability check: the 2-strand full twist `σ₁²` has `C 0 1 = 2`,
   i.e. `lk = 1` (Hopf link), not `0`.

## What is NOT here

* No statement about the Euler/NS PDE.  That smooth Euler flow transports vortex
  lines (Helmholtz–Kelvin) and so realises an isotopy of any thin vortex tube is a
  cited classical theorem, not proved.
* The diagonal (self-linking / writhe + twist) part of helicity is in the content
  sibling `fluid-dynamics/helicity-conservation.lean` (Călugăreanu–White–Fuller as
  a hypothesis), not here.
* Conjugation (Markov I) invariance of component linking for non-pure braids is
  not proved here; it is proved in `QOU.FluidDynamics.VortexLinkMarkov`
  (`markovI_conj`).
-/

namespace QOU.FluidDynamics.VortexLink

/-- A braid letter on `n + 1` strands: generator index and sign (`true` = `σᵢ`). -/
abbrev Letter (n : ℕ) := Fin n × Bool

/-- The crossing sign of a letter. -/
def sgn (e : Bool) : ℤ := if e then 1 else -1

@[simp] lemma sgn_not (e : Bool) : sgn (!e) = - sgn e := by cases e <;> simp [sgn]

/-- Symmetric increment of the crossing matrix by `s` on the pair `(a, b)`. -/
def bump {m : ℕ} (C : Fin m → Fin m → ℤ) (a b : Fin m) (s : ℤ) : Fin m → Fin m → ℤ :=
  fun x y => C x y + (if x = a ∧ y = b then s else 0) + (if x = b ∧ y = a then s else 0)

/-- Running state: position-to-label map and signed crossing matrix. -/
structure St (n : ℕ) where
  pos : Fin (n + 1) → Fin (n + 1)
  C : Fin (n + 1) → Fin (n + 1) → ℤ

/-- One crossing: strands at positions `i` and `i+1` cross with sign `sgn e`, then
swap positions. -/
def step {n : ℕ} (s : St n) (l : Letter n) : St n :=
  ⟨s.pos ∘ Equiv.swap l.1.castSucc l.1.succ,
   bump s.C (s.pos l.1.castSucc) (s.pos l.1.succ) (sgn l.2)⟩

/-- Run a braid word. -/
def run {n : ℕ} (s : St n) (w : List (Letter n)) : St n := w.foldl step s

@[simp] lemma run_nil {n : ℕ} (s : St n) : run s [] = s := rfl
@[simp] lemma run_cons {n : ℕ} (s : St n) (l : Letter n) (w : List (Letter n)) :
    run s (l :: w) = run (step s l) w := rfl
lemma run_append {n : ℕ} (s : St n) (u v : List (Letter n)) :
    run s (u ++ v) = run (run s u) v := by
  simp [run, List.foldl_append]

/-- **Context propagation.**  Two subwords with the same effect on every state can
be exchanged inside any word. -/
theorem run_congr {n : ℕ} {u v : List (Letter n)} (h : ∀ s, run s u = run s v)
    (w₁ w₂ : List (Letter n)) (s : St n) :
    run s (w₁ ++ u ++ w₂) = run s (w₁ ++ v ++ w₂) := by
  simp only [run_append, h]

/-! ### Algebra of `bump` -/

lemma bump_cancel {m : ℕ} (C : Fin m → Fin m → ℤ) (a b : Fin m) (s : ℤ) :
    bump (bump C a b s) b a (-s) = C := by
  funext x y
  simp only [bump]
  split_ifs <;> omega

lemma bump_comm {m : ℕ} (C : Fin m → Fin m → ℤ) (a b c d : Fin m) (s t : ℤ) :
    bump (bump C a b s) c d t = bump (bump C c d t) a b s := by
  funext x y
  simp only [bump]
  ring

/-! ### Reidemeister II -/

/-- **Reidemeister II.**  `σᵢ^e σᵢ^{-e}` has no effect on the state. -/
theorem run_R2 {n : ℕ} (i : Fin n) (e : Bool) (s : St n) :
    run s [(i, e), (i, !e)] = s := by
  obtain ⟨p, C⟩ := s
  simp only [run_cons, run_nil, step, Function.comp_apply, Equiv.swap_apply_left,
    Equiv.swap_apply_right, sgn_not]
  congr 1
  · funext k; simp [Function.comp_apply, Equiv.swap_apply_self]
  · exact bump_cancel C _ _ _

/-! ### Reidemeister III / braid relation -/

/-- One crossing at abstract positions `x, y`. -/
def stepAt {m : ℕ} (s : (Fin m → Fin m) × (Fin m → Fin m → ℤ)) (x y : Fin m) (t : ℤ) :
    (Fin m → Fin m) × (Fin m → Fin m → ℤ) :=
  (s.1 ∘ Equiv.swap x y, bump s.2 (s.1 x) (s.1 y) t)

/-- Braid relation at three distinct abstract positions. -/
lemma braid_core {m : ℕ} (s : (Fin m → Fin m) × (Fin m → Fin m → ℤ)) (a b c : Fin m)
    (hab : a ≠ b) (hbc : b ≠ c) (hac : a ≠ c) (t : ℤ) :
    stepAt (stepAt (stepAt s a b t) b c t) a b t
      = stepAt (stepAt (stepAt s b c t) a b t) b c t := by
  obtain ⟨p, C⟩ := s
  simp only [stepAt, Function.comp_apply, Equiv.swap_apply_left, Equiv.swap_apply_right,
    Equiv.swap_apply_of_ne_of_ne hac.symm hbc.symm, Equiv.swap_apply_of_ne_of_ne hab hac,
    Prod.mk.injEq]
  constructor
  · funext k
    simp only [Function.comp_apply]
    by_cases hka : k = a
    · subst hka
      simp [Equiv.swap_apply_def, hab, hac, hbc.symm, hac.symm]
    by_cases hkb : k = b
    · subst hkb
      simp [Equiv.swap_apply_def, hab, hac, hbc.symm, hac.symm]
    by_cases hkc : k = c
    · subst hkc
      simp [Equiv.swap_apply_def, hab, hac, hbc.symm, hac.symm]
    simp [Equiv.swap_apply_of_ne_of_ne hka hkb, Equiv.swap_apply_of_ne_of_ne hkb hkc]
  · funext x y
    simp only [bump]
    ring

/-- **Braid relation** `σᵢσⱼσᵢ = σⱼσᵢσⱼ` for `j = i + 1`, any common sign `e`:
both sides leave the same position map and the same crossing matrix. -/
theorem run_braid {n : ℕ} (i j : Fin n) (hij : (j : ℕ) = i + 1) (e : Bool) (s : St n) :
    run s [(i, e), (j, e), (i, e)] = run s [(j, e), (i, e), (j, e)] := by
  obtain ⟨p, C⟩ := s
  have hjb : j.castSucc = i.succ := by ext; simp [hij]
  have hab : (i.castSucc : Fin (n + 1)) ≠ i.succ := by
    intro h; have := congrArg Fin.val h; simp at this
  have hbc : (i.succ : Fin (n + 1)) ≠ j.succ := by
    intro h; have := congrArg Fin.val h; simp [hij] at this
  have hac : (i.castSucc : Fin (n + 1)) ≠ j.succ := by
    intro h; have := congrArg Fin.val h; simp [hij] at this; omega
  have key := braid_core (p, C) i.castSucc i.succ j.succ hab hbc hac (sgn e)
  simp only [stepAt] at key
  simp only [run_cons, run_nil, step, hjb]
  simp only [Prod.mk.injEq] at key
  rw [St.mk.injEq]
  exact key

/-! ### Far commutation -/

/-- **Far commutation** `σᵢσⱼ = σⱼσᵢ` for `i + 2 ≤ j`, independent signs. -/
theorem run_far {n : ℕ} (i j : Fin n) (hij : (i : ℕ) + 2 ≤ j) (e f : Bool) (s : St n) :
    run s [(i, e), (j, f)] = run s [(j, f), (i, e)] := by
  obtain ⟨p, C⟩ := s
  have h1 : (j.castSucc : Fin (n + 1)) ≠ i.castSucc := by simp [Fin.ext_iff]; omega
  have h2 : (j.castSucc : Fin (n + 1)) ≠ i.succ := by simp [Fin.ext_iff]; omega
  have h3 : (j.succ : Fin (n + 1)) ≠ i.castSucc := by simp [Fin.ext_iff]; omega
  have h4 : (j.succ : Fin (n + 1)) ≠ i.succ := by simp [Fin.ext_iff]; omega
  simp only [run_cons, run_nil, step, Function.comp_apply,
    Equiv.swap_apply_of_ne_of_ne h1 h2, Equiv.swap_apply_of_ne_of_ne h3 h4,
    Equiv.swap_apply_of_ne_of_ne h1.symm h3.symm,
    Equiv.swap_apply_of_ne_of_ne h2.symm h4.symm]
  congr 1
  · funext k
    simp only [Function.comp_apply, Equiv.swap_apply_def]
    split_ifs <;> simp_all [Fin.ext_iff]
  · exact bump_comm C _ _ _ _ _ _

/-! ### Linearity of the crossing matrix and crossing changes -/

/-- The crossing matrix accumulates additively: running from `⟨p, C⟩` gives the
run from `⟨p, 0⟩` shifted by `C`. -/
lemma run_C_add {n : ℕ} (w : List (Letter n)) (p : Fin (n + 1) → Fin (n + 1))
    (C : Fin (n + 1) → Fin (n + 1) → ℤ) :
    run ⟨p, C⟩ w = ⟨(run ⟨p, 0⟩ w).pos, C + (run ⟨p, 0⟩ w).C⟩ := by
  induction w generalizing p C with
  | nil => simp
  | cons l w ih =>
    simp only [run_cons, step]
    rw [ih, ih (C := bump 0 _ _ _)]
    simp only [St.mk.injEq, true_and]
    funext x y
    simp only [Pi.add_apply, bump, Pi.zero_apply]
    ring

/-- The position map does not depend on the crossing matrix. -/
lemma run_pos {n : ℕ} (w : List (Letter n)) (p : Fin (n + 1) → Fin (n + 1))
    (C C' : Fin (n + 1) → Fin (n + 1) → ℤ) : (run ⟨p, C⟩ w).pos = (run ⟨p, C'⟩ w).pos := by
  rw [run_C_add, run_C_add (C := C')]

/-- Running preserves injectivity of the labelling. -/
lemma run_pos_injective {n : ℕ} (w : List (Letter n)) (s : St n)
    (hs : Function.Injective s.pos) : Function.Injective (run s w).pos := by
  induction w generalizing s with
  | nil => simpa using hs
  | cons l w ih => exact ih _ (hs.comp (Equiv.injective _))

/-- **Crossing change.**  Flipping the sign of one letter changes the crossing matrix
by exactly `-2 · sgn e` on the pair of strands `{a, b}` meeting at that crossing,
and nowhere else.  Here `a, b` are the labels at the crossing's positions after
the prefix `w₁`. -/
theorem crossingChange_C {n : ℕ} (w₁ w₂ : List (Letter n)) (i : Fin n) (e : Bool)
    (s : St n) (x y : Fin (n + 1)) :
    (run s (w₁ ++ [(i, !e)] ++ w₂)).C x y
      = (run s (w₁ ++ [(i, e)] ++ w₂)).C x y
        - 2 * sgn e * ((if x = (run s w₁).pos i.castSucc ∧ y = (run s w₁).pos i.succ
                          then 1 else 0)
                      + (if x = (run s w₁).pos i.succ ∧ y = (run s w₁).pos i.castSucc
                          then 1 else 0)) := by
  simp only [run_append, run_cons, run_nil]
  set s₁ := run s w₁
  obtain ⟨p, C⟩ := s₁
  simp only [step, sgn_not]
  rw [run_C_add w₂ _ (bump C _ _ _), run_C_add w₂ _ (bump C _ _ (sgn e))]
  simp only [Pi.add_apply, bump]
  split_ifs <;> ring

/-- With injective labelling (distinct strands), the two strands meeting at a
crossing are distinct, so the crossing is genuinely **between** two strands. -/
theorem crossing_labels_ne {n : ℕ} (w : List (Letter n)) (s : St n)
    (hs : Function.Injective s.pos) (i : Fin n) :
    (run s w).pos i.castSucc ≠ (run s w).pos i.succ := by
  intro h
  have := run_pos_injective w s hs h
  simp [Fin.ext_iff] at this

/-- **Linking number moves by exactly one.**  In the linking-number normalisation
`lk = C / 2`, a crossing change between distinct strands `a ≠ b` changes
`lk(a,b)` by exactly `-sgn e` (i.e. `∓1`), and only that pair (and its mirror)
changes. -/
theorem crossingChange_lk {n : ℕ} (w₁ w₂ : List (Letter n)) (i : Fin n) (e : Bool)
    (s : St n) (hs : Function.Injective s.pos) :
    let a := (run s w₁).pos i.castSucc
    let b := (run s w₁).pos i.succ
    ((run s (w₁ ++ [(i, !e)] ++ w₂)).C a b : ℚ) / 2
      = ((run s (w₁ ++ [(i, e)] ++ w₂)).C a b : ℚ) / 2 - sgn e := by
  intro a b
  have hab : a ≠ b := crossing_labels_ne w₁ s hs i
  rw [crossingChange_C w₁ w₂ i e s a b]
  rw [if_pos ⟨rfl, rfl⟩, if_neg (fun h => hab h.1)]
  push_cast
  ring

/-! ### Mutual (linking) helicity -/

/-- Mutual helicity of strands with circulations `Γ` and crossing matrix `C`:
`Σₓ Σᵧ (C x y / 2) Γₓ Γᵧ`, which equals `2 Σ_{x<y} lk(x,y) Γₓ Γᵧ` when `C` is
symmetric with zero diagonal (Moffatt 1969's mutual term). -/
noncomputable def mutualHelicity {m : ℕ} (C : Fin m → Fin m → ℤ) (Γ : Fin m → ℝ) : ℝ :=
  ∑ x, ∑ y, ((C x y : ℝ) / 2) * Γ x * Γ y

/-- Algebraic core: a symmetric rank-two change of the crossing matrix moves the
mutual helicity by `-2 t Γₐ Γ_b`. -/
lemma mutualHelicity_sub {m : ℕ} (C C' : Fin m → Fin m → ℤ) (Γ : Fin m → ℝ) (a b : Fin m)
    (t : ℤ) (hC : ∀ x y, C' x y = C x y - 2 * t * ((if x = a ∧ y = b then 1 else 0)
      + (if x = b ∧ y = a then 1 else 0))) :
    mutualHelicity C' Γ = mutualHelicity C Γ - 2 * t * Γ a * Γ b := by
  unfold mutualHelicity
  have hpt : ∀ x y, (C' x y : ℝ) / 2 * Γ x * Γ y
      = (C x y : ℝ) / 2 * Γ x * Γ y - (t : ℝ) * ((if x = a ∧ y = b then Γ x * Γ y else 0)
        + (if x = b ∧ y = a then Γ x * Γ y else 0)) := by
    intro x y
    rw [hC]
    split_ifs <;> push_cast <;> ring
  simp only [hpt, Finset.sum_sub_distrib, Finset.sum_add_distrib, ← Finset.mul_sum]
  have hs : ∀ u v : Fin m, ∑ x, ∑ y, (if x = u ∧ y = v then Γ x * Γ y else 0) = Γ u * Γ v := by
    intro u v
    rw [Finset.sum_eq_single u (fun x _ hx => by simp [hx]) (by simp)]
    rw [Finset.sum_eq_single v (fun y _ hy => by simp [hy]) (by simp)]
    simp
  rw [hs a b, hs b a]
  ring

/-- **Helicity jump under a crossing change.**  The mutual helicity changes by exactly
`-2 · sgn e · Γₐ · Γ_b`: a single reconnection-type crossing change between tubes of
circulation `Γₐ, Γ_b` alters helicity by `2 Γₐ Γ_b` in magnitude. -/
theorem crossingChange_mutualHelicity {n : ℕ} (w₁ w₂ : List (Letter n)) (i : Fin n)
    (e : Bool) (s : St n) (Γ : Fin (n + 1) → ℝ) :
    mutualHelicity (run s (w₁ ++ [(i, !e)] ++ w₂)).C Γ
      = mutualHelicity (run s (w₁ ++ [(i, e)] ++ w₂)).C Γ
        - 2 * sgn e * Γ ((run s w₁).pos i.castSucc) * Γ ((run s w₁).pos i.succ) := by
  have := mutualHelicity_sub _ _ Γ ((run s w₁).pos i.castSucc) ((run s w₁).pos i.succ)
    (sgn e) (crossingChange_C w₁ w₂ i e s)
  rw [this]

/-- Mutual helicity is unchanged by Reidemeister II anywhere in a word. -/
theorem mutualHelicity_R2 {n : ℕ} (w₁ w₂ : List (Letter n)) (i : Fin n) (e : Bool)
    (s : St n) (Γ : Fin (n + 1) → ℝ) :
    mutualHelicity (run s (w₁ ++ [(i, e), (i, !e)] ++ w₂)).C Γ
      = mutualHelicity (run s (w₁ ++ [] ++ w₂)).C Γ := by
  rw [run_congr (u := [(i, e), (i, !e)]) (v := []) (fun s => (run_R2 i e s).trans (run_nil s).symm)]

/-- Mutual helicity is unchanged by the braid relation anywhere in a word. -/
theorem mutualHelicity_braid {n : ℕ} (w₁ w₂ : List (Letter n)) (i j : Fin n)
    (hij : (j : ℕ) = i + 1) (e : Bool) (s : St n) (Γ : Fin (n + 1) → ℝ) :
    mutualHelicity (run s (w₁ ++ [(i, e), (j, e), (i, e)] ++ w₂)).C Γ
      = mutualHelicity (run s (w₁ ++ [(j, e), (i, e), (j, e)] ++ w₂)).C Γ := by
  rw [run_congr (fun s => run_braid i j hij e s)]

/-! ### Falsifiability check: the Hopf link -/

/-- Identity labelling, zero crossings. -/
def init (n : ℕ) : St n := ⟨id, 0⟩

/-- The 2-strand full twist `σ₁²` closes to the Hopf link: `C 0 1 = 2`, so `lk = 1`. -/
theorem hopf_C : (run (init 1) [((0 : Fin 1), true), ((0 : Fin 1), true)]).C 0 1 = 2 := by
  decide

/-- A single crossing `σ₁` (a 2-strand braid closing to the unknot, one component)
also records `C 0 1 = 1`; the closure is a knot, so this is self-crossing data, not
inter-component linking — the pure-braid hypothesis is load-bearing. -/
theorem single_crossing_C : (run (init 1) [((0 : Fin 1), true)]).C 0 1 = 1 := by
  decide

/-- `σ₁ σ₁⁻¹` (unlink) records zero. -/
theorem unlink_C : (run (init 1) [((0 : Fin 1), true), ((0 : Fin 1), false)]).C 0 1 = 0 := by
  decide

end QOU.FluidDynamics.VortexLink
