import QOU.AppendixSurreals.QCollatz

/-!
# Block descent: the per-step formulation is the wrong shape for `q`-Collatz

Every termination lemma in the corpus — `reaches_cycle_of_descent`,
`reaches_of_descent_of_forward`, `reaches_cycle_of_descent_domainStable` — demands
a measure that descends at **every single step**:

    ∀ P, S P → P ≠ attractor → μ (C P) < μ P.

That is the wrong requirement for this map, and the mismatch is structural rather
than incidental.

## Why the orbit cannot descend per step

The Skein-Collatz orbit decomposes into **blocks**: one odd step, then a run of
even steps. An odd step is `P ↦ ([3]_q P + 1)/[2]_q` and an even step is
`P ↦ P/[2]_q`, so in the natural gradings the odd step *grows* the element and
each even step shrinks it. Over one block of an odd step followed by `v` even
steps the net change is `1 − v`: contractive exactly when `v ≥ 2`.

`v ≥ 2` is precisely the contact-boundary condition `⟨v_[2]⟩ ≥ 2` — *"each
tripling followed by at least two halvings on average"*
(`prop:collatz-contact-boundary`, `rem:collatz-three-forms`). So the paper's own
convergence criterion is a statement about **blocks**, while every reduction
available to discharge it was stated **per step**. A candidate measure was being
tested against a requirement the problem never had.

## What this file provides

`reaches_of_block_descent` weakens the hypothesis to: from every non-target point
of the cone, *some* number of steps ahead the measure has dropped. Convergence
still follows, by strong induction on `μ`. `reaches_of_descent_of_forward` is the
`n = 1` case, proved here as `per_step_is_block_descent`, so this is strictly
weaker rather than merely different.

`reaches_cycle_of_block_descent_domainStable` specialises it to `D∞`, exactly as
the per-step version does — forward-invariance is again free, since `D∞` is
closed under iteration (`domainStable_iterate`).

## What it does NOT do — and one thing it explicitly does not rescue

This is a **reduction, not a proof**. It replaces one open requirement with a
weaker open requirement; no measure is supplied, and supplying one would close
`q`-Collatz-on-a-QOU. Anti-laundering (AGENTS.md): nothing here is wired to
production and no `μ` is fabricated.

In particular it does **not** rescue `v_[2]`. The obstruction of bean `qou-4atn`
survives the reformulation verbatim: `μ` is `ℕ`-valued, so `μ (C^[n] P) < μ P` is
impossible wherever `μ P = 0`, whatever `n` is
(`block_descent_measure_pos_off_target`). Since `v_[2]` vanishes at every `q`-odd
point of `D∞`, it fails the block condition for the same reason it failed the
per-step one. Weakening the hypothesis buys nothing for any measure that
vanishes off the attractor — so the search should be over **heights**, not
valuations.
-/

namespace QOU.AppendixSurreals.CollatzBlockDescent

-- The two `{Skein : Type u}` theorems below never declared `u`.  The workspace sets
-- `autoImplicit = false` (root `lakefile.toml`), so it is not auto-bound and both
-- signatures fail to elaborate -- which in turn strips the expected type from the
-- anonymous constructor further down, producing a third, misleading error.
universe u

/-! ## The reduction -/

/-- **Block descent suffices for convergence.** If from every non-target point of
    a cone some finite number of steps ahead the measure has strictly dropped —
    and the cone is closed under taking that many steps — then every point of the
    cone reaches the target.

    The step count `n` may vary from point to point and is not bounded. Note it
    is automatically positive: `n = 0` would give `μ x < μ x`
    (`block_length_ne_zero`), so requiring `0 < n` as a hypothesis would be
    redundant and it is omitted. -/
theorem reaches_of_block_descent {α : Type*} (f : α → α) (target : α)
    (S : α → Prop) (μ : α → ℕ)
    (hblock : ∀ x, S x → x ≠ target →
      ∃ n : ℕ, S (f^[n] x) ∧ μ (f^[n] x) < μ x) :
    ∀ x, S x → ∃ k : ℕ, f^[k] x = target := by
  suffices H : ∀ m x, μ x = m → S x → ∃ k, f^[k] x = target from
    fun x hx => H (μ x) x rfl hx
  intro m
  induction m using Nat.strong_induction_on with
  | _ m IH =>
    intro x hμ hx
    by_cases hc : x = target
    · exact ⟨0, by simpa using hc⟩
    · obtain ⟨n, hS, hlt⟩ := hblock x hx hc
      have hlt' : μ (f^[n] x) < m := hμ ▸ hlt
      obtain ⟨k, hk⟩ := IH (μ (f^[n] x)) hlt' (f^[n] x) rfl hS
      exact ⟨k + n, by rw [Function.iterate_add_apply]; exact hk⟩

/-- A descending block has positive length — so the omitted `0 < n` hypothesis
    would have been redundant. -/
theorem block_length_ne_zero {α : Type*} (f : α → α) (μ : α → ℕ) (x : α) (n : ℕ)
    (h : μ (f^[n] x) < μ x) : n ≠ 0 := by
  rintro rfl
  simp only [Function.iterate_zero_apply] at h
  exact absurd h (lt_irrefl _)

/-- **Per-step descent is the `n = 1` case**, so block descent is a strictly
    weaker hypothesis than `reaches_of_descent_of_forward`'s and this reduction
    subsumes it. -/
theorem per_step_is_block_descent {α : Type*} (f : α → α) (target : α)
    (S : α → Prop) (μ : α → ℕ)
    (hfwd : ∀ x, S x → x ≠ target → S (f x))
    (hdesc : ∀ x, S x → x ≠ target → μ (f x) < μ x) :
    ∀ x, S x → x ≠ target → ∃ n : ℕ, S (f^[n] x) ∧ μ (f^[n] x) < μ x := by
  intro x hx hne
  exact ⟨1, by simpa using hfwd x hx hne, by simpa using hdesc x hx hne⟩

/-! ## The obstruction survives the weakening

Reformulating does not rescue a measure that vanishes off the target. -/

/-- **Any `ℕ`-valued block-descent measure is still strictly positive off the
    target.** `μ (f^[n] x) < μ x` is impossible when `μ x = 0`, for every `n`. So
    the `qou-4atn` refutation of `v_[2]` applies verbatim to block descent: the
    weaker hypothesis buys nothing for a measure vanishing on the `q`-odd part of
    `D∞`. -/
theorem block_descent_measure_pos_off_target {α : Type*} (f : α → α) (target : α)
    (S : α → Prop) (μ : α → ℕ)
    (hblock : ∀ x, S x → x ≠ target →
      ∃ n : ℕ, S (f^[n] x) ∧ μ (f^[n] x) < μ x) :
    ∀ x, S x → x ≠ target → 0 < μ x := by
  intro x hx hne
  obtain ⟨n, _, hlt⟩ := hblock x hx hne
  omega

/-! ## Specialisation to the domain-stable cone -/

/-- **`D∞` is closed under iteration**, not merely under one step — the
    iterated form of `QCollatz.domainStable_forward`. -/
theorem domainStable_iterate {Skein : Type u} [CommRing Skein]
    [QCollatz Skein] (P : Skein)
    (h : QCollatz.domainStable P) (n : ℕ) :
    QCollatz.domainStable (QCollatz.C^[n] P) := by
  intro k
  rw [← Function.iterate_add_apply]
  exact h (k + n)

/-- **Convergence over `D∞` reduces to BLOCK descent.** The domain-stable
    counterpart of `reaches_cycle_of_descent_domainStable`, with the weaker
    hypothesis. Forward-invariance is free, as in the per-step version, because
    `D∞` is closed under iteration.

    This is the sharpest reduction of the `q`-Collatz convergence half currently
    in the corpus: the open content is now the existence of a measure that drops
    *somewhere ahead*, rather than at every step — which is the form the
    contact-boundary condition `⟨v_[2]⟩ ≥ 2` actually takes. It supplies no such
    measure. -/
theorem reaches_cycle_of_block_descent_domainStable {Skein : Type u}
    [CommRing Skein] [QCollatz Skein] (μ : Skein → ℕ)
    (hblock : ∀ P : Skein, QCollatz.domainStable P →
      P ≠ QCollatz.attractor →
      ∃ n : ℕ, μ (QCollatz.C^[n] P) < μ P) :
    ∀ P : Skein, QCollatz.domainStable P →
      ∃ k : ℕ, QCollatz.C^[k] P = QCollatz.attractor :=
  reaches_of_block_descent QCollatz.C QCollatz.attractor
    QCollatz.domainStable μ
    (fun P hP hne =>
      let ⟨n, hn⟩ := hblock P hP hne
      ⟨n, domainStable_iterate P hP n, hn⟩)


/-! ## What actually follows an odd step — the block picture made precise

The block decomposition above assumed the shape "one odd step, then a run of even
steps". That shape is **not** automatic, and this section pins down exactly when
it holds.

A `q`-odd element is one with residue `-1` at the `[2]_q`-divisor, so it has the
form `P = -1 + [2]_q·A`. The odd branch then simplifies completely: -/

/-- **The odd branch on a `q`-odd element.** With `P = -1 + [2]_q·A`,

      [3]_q·P + 1 = [2]_q·(-q + [3]_q·A),

    so the branch's exact division is visible term by term and its output is
    `C(P) = -q + [3]_q·A`. A pure ring identity — no hypothesis on `q` or `A`. -/
theorem oddStep_of_qOdd_form {R : Type*} [CommRing R] (q A : R) :
    (q ^ 2 + q + 1) * (-1 + (q + 1) * A) + 1
      = (q + 1) * (-q + (q ^ 2 + q + 1) * A) := by
  ring

/-- **Residue of the odd branch's output.** At the divisor `q = -1`, the output
    `-q + [3]_q·A` has residue `1 + A(-1)`. So what follows an odd step is
    decided entirely by `A(-1)`:

    * `A(-1) = -1` → residue `0` → the next step is **even** (the block continues);
    * `A(-1) = -2` → residue `-1` → the next step is **odd** (a `v = 0` block);
    * anything else → the orbit **leaves the domain**.

    This is the trichotomy that makes "block" well defined. -/
theorem oddStep_next_residue {R S : Type*} [CommRing R] [CommRing S]
    (φ : R →+* S) (q A : R) (hq : φ q = -1) :
    φ (-q + (q ^ 2 + q + 1) * A) = 1 + φ A := by
  simp only [map_add, map_neg, map_mul, map_pow, map_one, hq]
  ring

/-- **Two consecutive odd steps are possible.** Taking `A = -2` gives a `q`-odd
    element whose odd-branch image is again `q`-odd — so the "odd then even"
    block shape is *not* a theorem about the map, only about orbits where
    `A(-1) = -1`.

    Concretely over `ℤ[q]` this is `P = -2q - 3 ↦ -2q² - 3q - 2`, both of residue
    `-1`. Measured separately
    (`computations/qcollatz_block_structure_probe.py`): of 1420 such
    consecutive-odd starts, **none** reached the attractor cycle — every one left
    the domain, 93 % of them within two steps. So no `v = 0` block has been
    exhibited inside `D∞`, but none is excluded either: whether one can occur
    there is **open**, and it is the precise obstacle to treating the block
    decomposition as total. -/
theorem consecutive_odd_steps_exist {R : Type*} [CommRing R]
    (φ : R →+* ℤ) (q : R) (hq : φ q = -1) :
    ∃ A : R, φ (-1 + (q + 1) * A) = -1 ∧ φ (-q + (q ^ 2 + q + 1) * A) = -1 := by
  refine ⟨-2, ?_, ?_⟩
  · simp only [map_add, map_neg, map_mul, map_one, map_ofNat, hq]
    ring
  · rw [oddStep_next_residue φ q (-2) hq, map_neg, map_ofNat]
    norm_num


/-! ## The cube-root criterion, and why the attractor has no odd-preimage

The `v = 0` question — can two consecutive odd steps occur inside `D∞`? — is
attacked from the backward side by asking which elements admit an **odd
branch-inverse** at all. That has an exact criterion at a primitive cube root of
unity `w`, where `[3]_q` vanishes, and the criterion is pure ring algebra.

An odd step from `Q` to `P` is `[2]_q·P = [3]_q·Q + 1`. Evaluating at `w` kills
the `[3]_q` term outright, leaving `(w+1)·P(w) = 1` — a condition on `P` alone,
with `Q` eliminated. Since `(w+1)·(-w) = 1`, that pins `P(w) = -w`.

What this buys, proved below: the attractor `q⁻¹` evaluates to `w² ≠ -w`, so
**`q⁻¹` admits no odd-preimage** — the attractor is reached only by even steps.
That is the structural reason the backward tree's odd-preimages are as rare as
the probes find them (6 of 154 nodes at depth 40; 20 of 1260 at depth 120).

**What is NOT proved here, and is the open part.** The measured obstruction to a
`v = 0` block inside `D∞` is a *congruence*: across 1260 backward-tree nodes,
every one admitting an odd-preimage has `P'(w) ≡ -w (mod 6)`, whereas a second
chained odd-preimage requires `P'(w) = 2`, and `2 ≢ -w (mod 6)` because
`N(2+w) = 3` is not divisible by `N(6) = 36`. That congruence is an **observed
pattern, not a theorem** — it is not proved here and must not be cited as one.
Proving it would settle the `v = 0` question for the backward tree; the step from
there to all of `D∞` is the convergence conjecture itself (`qcz7` A1).

`w` is taken as a ring element satisfying `w² + w + 1 = 0` rather than
constructing `ℤ[w]`, which keeps every statement over a generic `[CommRing R]`
(§7c). -/

/-- `w + 1` is a **unit** whenever `w² + w + 1 = 0`, with inverse `-w`. -/
theorem cubeRoot_one_add_mul_neg {R : Type*} [CommRing R] (w : R)
    (hw : w ^ 2 + w + 1 = 0) : (w + 1) * (-w) = 1 := by
  linear_combination -hw

/-- **The cube-root criterion.** If `P` is the odd-branch image of `Q` —
    `[2]_q·P = [3]_q·Q + 1` — then at a primitive cube root `w` the `[3]_q` term
    vanishes and `P(w)` is pinned to `-w`, with `Q` eliminated entirely.

    So `P(w) = -w` is **necessary** for `P` to admit an odd-preimage. -/
theorem oddPreimage_forces_eval_cubeRoot {R : Type*} [CommRing R] (w p q : R)
    (hw : w ^ 2 + w + 1 = 0)
    (h : (w + 1) * p = (w ^ 2 + w + 1) * q + 1) :
    p = -w := by
  have h1 : (w + 1) * p = 1 := by linear_combination h + q * hw
  have hunit := cubeRoot_one_add_mul_neg w hw
  have hkey : (w + 1) * (p + w) = 0 := by linear_combination h1 - hunit
  have hexp : p + w = (-w) * ((w + 1) * (p + w)) := by
    linear_combination (-(p + w)) * hunit
  have hz : p + w = 0 := by rw [hkey] at hexp; simpa using hexp
  linear_combination hz

/-- **The attractor admits no odd-preimage.** `q⁻¹` evaluates to `w⁻¹ = w²` at a
    primitive cube root, and `w² = -w` would force `1 = 0`. So no `q`-odd element
    maps to the attractor under the odd branch — it is reached only by even
    steps.

    This is the structural reason odd-preimages are rare in the backward tree,
    and it is proved rather than observed. -/
theorem attractor_no_oddPreimage {R : Type*} [CommRing R] [Nontrivial R] (w : R)
    (hw : w ^ 2 + w + 1 = 0) : (w ^ 2 : R) ≠ -w := by
  intro h
  have : (1 : R) = 0 := by linear_combination hw - h
  exact one_ne_zero this


/-! ### The unit obstruction — why chained odd-preimages are blocked

The mod-6 congruence recorded above as an *observed pattern* has an explanation,
and the explanation is cleaner than the pattern. It needs no norm and no `ℤ[w]`:
it is about **unit-ness** of `P(w)`.

Three facts drive it.

1. An odd-preimage forces `P(w) = -w` (above), and `-w` is a **unit**
   (`(-w)·(-w²) = w³ = 1`). So *only a node whose cube-root evaluation is a unit
   can admit an odd-preimage at all*.
2. The even branch-inverse is `Q = [2]_q·P`, so `Q(w) = (w+1)·P(w)` — and `w+1`
   is itself a unit (`cubeRoot_one_add_mul_neg`). So **unit-ness of the
   evaluation is invariant along an entire even chain**.
3. Hence a single non-unit evaluation blocks odd-preimages *forever* along that
   chain (`evenSubtree_no_oddPreimage`).

That is the engine. Measured against the actual backward tree
(`computations/qcollatz_vzero_block_probe.py`), it accounts for everything the
sampling saw:

* `w+1` has multiplicative **order 6**, so along the main even chain from
  `1+q⁻¹` the evaluation returns to `-w` exactly at steps `n ≡ 0 (mod 6)` —
  *this is where the 6 comes from*;
* solving the coupled recursion gives the closed form
  `vₙ = αⁿv₀ + n·αⁿ⁻¹u₀` with `α = w+1`, verified against the real chain for
  `n = 0…24`, which produces exactly the observed `P'(w) = (-6k, -6k-1)`;
* the odd-preimage taken at the `n = 6k` node lands on an evaluation of norm
  `1 + 6k + 12k²` (verified `k = 0…10`), which equals `1` **only** for `k = 0` —
  and `k = 0` returns `q⁻¹`, already on the chain.

So for every `k ≥ 1` the odd branch sits at a non-unit evaluation, and by fact 3
no node of its even-subtree can admit a further odd-preimage. **No two chained
odd-preimages occur in the backward tree**, hence no `v = 0` block there.

**Scope — what is and is not established.** Facts 1–3 are proved below.

The two arithmetic inputs — the order-6 congruence with its closed form, the
norm formula `1 + 6k + 12k²`, and the tree-structure induction — were originally
*measured only*, over the finite ranges stated. They are now proved in
`QOU.AppendixSurreals.CollatzEisenstein`:

* `alpha_pow_six` — `(w+1)⁶ = 1`, the source of the 6;
* `chainData_snd` / `chainData_at_six_mul` — the closed form, and that it gives
  `P'(w) = (-6k, -6k-1)` at the `n = 6k` nodes;
* `branch_norm` — `N(Q_k(w)) = 1 + 6k + 12k²`, and `branch_norm_eq_one_iff` /
  `branch_norm_ge` that it exceeds `1` for every `k ≥ 1`;
* `branch_subtree_no_oddPreimage` — feeding that non-unit into fact 3: no node
  of any `k ≥ 1` branch admits a further odd-preimage, so each branch is a bare
  even chain.

Those proofs carry one hypothesis on the ambient ring — that `1` and `w` are
`ℤ`-independent — which holds in `ℤ[ω]` and fails in, say, `ZMod 3`. It is a
condition on the ring, not a conjecture; nothing is axiomatized.

**What is still not established.** This settles `v = 0` for the backward *tree*
only. The step to all of `D∞` is the convergence conjecture itself (`qcz7` A1)
and is not claimed. -/

/-- `w³ = 1` for a primitive cube root. -/
theorem cubeRoot_pow_three {R : Type*} [CommRing R] (w : R)
    (hw : w ^ 2 + w + 1 = 0) : w ^ 3 = 1 := by
  linear_combination (w - 1) * hw

/-- `-w` is a unit, with inverse `-w²`. -/
theorem isUnit_neg_cubeRoot {R : Type*} [CommRing R] (w : R)
    (hw : w ^ 2 + w + 1 = 0) : IsUnit (-w) :=
  isUnit_of_mul_eq_one (-w) (-w ^ 2) (by linear_combination (w - 1) * hw)

/-- `w + 1` is a unit, with inverse `-w`. -/
theorem isUnit_one_add_cubeRoot {R : Type*} [CommRing R] (w : R)
    (hw : w ^ 2 + w + 1 = 0) : IsUnit (w + 1) :=
  isUnit_of_mul_eq_one (w + 1) (-w) (cubeRoot_one_add_mul_neg w hw)

/-- **Only a unit evaluation can admit an odd-preimage.** Combining
    `oddPreimage_forces_eval_cubeRoot` (`P(w) = -w`) with the unit-ness of `-w`. -/
theorem isUnit_eval_of_oddPreimage {R : Type*} [CommRing R] (w p q : R)
    (hw : w ^ 2 + w + 1 = 0)
    (h : (w + 1) * p = (w ^ 2 + w + 1) * q + 1) : IsUnit p := by
  rw [oddPreimage_forces_eval_cubeRoot w p q hw h]
  exact isUnit_neg_cubeRoot w hw

/-- **Unit-ness of the evaluation is invariant along an even chain.** The even
    branch-inverse multiplies `P(w)` by the unit `w + 1`. -/
theorem evenPreimage_isUnit_iff {R : Type*} [CommRing R] (w p : R)
    (hw : w ^ 2 + w + 1 = 0) : IsUnit ((w + 1) * p) ↔ IsUnit p := by
  constructor
  · intro h
    have hu : (-w) * ((w + 1) * p) = p := by linear_combination (-p) * hw
    rw [← hu]
    exact (isUnit_neg_cubeRoot w hw).mul h
  · intro h
    exact (isUnit_one_add_cubeRoot w hw).mul h

/-- Iterating: unit-ness survives any number of even branch-inverses. -/
theorem evenChain_isUnit_iff {R : Type*} [CommRing R] (w p : R)
    (hw : w ^ 2 + w + 1 = 0) :
    ∀ n : ℕ, IsUnit ((w + 1) ^ n * p) ↔ IsUnit p := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    have : (w + 1) ^ (n + 1) * p = (w + 1) * ((w + 1) ^ n * p) := by ring
    rw [this, evenPreimage_isUnit_iff w _ hw]
    exact ih

/-- **The obstruction.** If a node's cube-root evaluation is not a unit, then
    **no** node in its even-subtree admits an odd-preimage — the block is
    permanent, not local.

    This is why the `k ≥ 1` odd branches of the backward tree can never chain a
    second odd step: each lands on a non-unit evaluation (norm `1 + 6k + 12k²`),
    and every even descendant inherits that. -/
theorem evenSubtree_no_oddPreimage {R : Type*} [CommRing R] (w p : R)
    (hw : w ^ 2 + w + 1 = 0) (hnu : ¬ IsUnit p) (n : ℕ) :
    ¬ ∃ q : R, (w + 1) * ((w + 1) ^ n * p) = (w ^ 2 + w + 1) * q + 1 := by
  rintro ⟨q, hq⟩
  exact hnu ((evenChain_isUnit_iff w p hw n).mp
    (isUnit_eval_of_oddPreimage w _ q hw hq))


/-- **The chained-odd-preimage criterion, machine-checked.** Differentiating
    `[3]_q·Q = [2]_q·P - 1` at `w` (where `[3]_q` vanishes) gives

        (1 + 2w)·Q(w) = P(w) + (w+1)·P'(w),

    which is carried here as the hypothesis `hrel` — it is ordinary
    differentiation, not formalized in this file. Given `P(w) = -w` (so `P`
    admits an odd-preimage at all), that preimage satisfies `Q(w) = -w` — the
    condition for a **second** chained odd-preimage — only if `P'(w) = 2`.

    Contrapositive, which is how it is used: `P'(w) ≠ 2` rules out a chained
    odd-preimage. This is the criterion the probes evaluate, previously derived
    by hand; the cancellation is of the **unit** `w+1`, so no domain hypothesis
    is needed.

    (The converse would need to cancel `1 + 2w`, which is *not* a unit — it has
    norm 3 — so it holds in a domain but not over an arbitrary `CommRing`. Only
    the direction actually used is claimed.) -/
theorem chained_oddPreimage_forces_deriv_eq_two {R : Type*} [CommRing R]
    (w v Qw : R) (hw : w ^ 2 + w + 1 = 0)
    (hrel : (1 + 2 * w) * Qw = -w + (w + 1) * v)
    (hQ : Qw = -w) : v = 2 := by
  subst hQ
  have h1 : (w + 1) * v = (w + 1) * 2 := by linear_combination -hrel - 2 * hw
  have hu : (-w) * ((w + 1) * v) = v := by linear_combination (-v) * hw
  have hu2 : (-w) * ((w + 1) * 2) = 2 := by linear_combination (-2 : R) * hw
  rw [h1, hu2] at hu
  exact hu.symm

/-! ## Skein filtration block-descent halting theorem (`qou-i5so`)

Formalizes the abstract block-descent principle on the Skein filtration degree
`ell : S → ℕ`: if `ell` strictly decreases across every `blockLen`-step block on
non-terminal states, then:
1. No non-terminal state can be fixed by a `blockLen`-step block
   (`no_nonterminal_block_fixed_of_descent`).
2. Every initial state `x` reaches a terminal state within `ell x` blocks
   (`reaches_terminal_within_blocks`), i.e. within `blockLen * ell x` elementary
   steps (`reaches_terminal_step_bound`). -/

/-- A dynamical system on `S` equipped with a `ℕ`-valued Skein filtration measure
    `ell` that strictly decreases along `blockLen`-step blocks outside a terminal
    set `IsTerminal`. -/
structure SkeinFiltrationDescent (S : Type*) where
  step : S → S
  IsTerminal : S → Prop
  ell : S → ℕ
  blockLen : ℕ
  blockLen_pos : 0 < blockLen
  block_descent : ∀ x : S, ¬ IsTerminal x → ell (step^[blockLen] x) < ell x

/-- No non-terminal state can be periodic of period `blockLen` under block descent. -/
theorem no_nonterminal_block_fixed_of_descent {S : Type*}
    (sys : SkeinFiltrationDescent S) (x : S)
    (hfix : sys.step^[sys.blockLen] x = x) : sys.IsTerminal x := by
  by_contra hnt
  have hlt := sys.block_descent x hnt
  rw [hfix] at hlt
  exact Nat.lt_irrefl (sys.ell x) hlt

/-- By induction on the filtration bound `B`, every state `x` with `sys.ell x ≤ B`
    reaches `IsTerminal` within at most `B` applications of `sys.step^[sys.blockLen]`. -/
theorem reaches_terminal_within_blocks {S : Type*}
    (sys : SkeinFiltrationDescent S) :
    ∀ B : ℕ, ∀ x : S, sys.ell x ≤ B →
      ∃ j : ℕ, j ≤ B ∧ sys.IsTerminal ((sys.step^[sys.blockLen])^[j] x) := by
  intro B
  induction B with
  | zero =>
    intro x hx
    refine ⟨0, le_rfl, ?_⟩
    by_contra hnt
    have hlt := sys.block_descent x hnt
    omega
  | succ n ih =>
    intro x hx
    by_cases hterm : sys.IsTerminal x
    · exact ⟨0, Nat.zero_le (n + 1), hterm⟩
    · have hlt := sys.block_descent x hterm
      have hle : sys.ell (sys.step^[sys.blockLen] x) ≤ n := by omega
      obtain ⟨j, hj, htj⟩ := ih (sys.step^[sys.blockLen] x) hle
      refine ⟨j + 1, by omega, ?_⟩
      rw [Function.iterate_succ_apply]
      exact htj

/-- Every initial state `x` reaches a terminal state in at most
    `sys.blockLen * sys.ell x` elementary steps. -/
theorem reaches_terminal_step_bound {S : Type*}
    (sys : SkeinFiltrationDescent S) (x : S) :
    ∃ k : ℕ, k ≤ sys.blockLen * sys.ell x ∧ sys.IsTerminal (sys.step^[k] x) := by
  obtain ⟨j, hj, htj⟩ := reaches_terminal_within_blocks sys (sys.ell x) x le_rfl
  refine ⟨sys.blockLen * j, Nat.mul_le_mul_left sys.blockLen hj, ?_⟩
  rw [Function.iterate_mul]
  exact htj

end QOU.AppendixSurreals.CollatzBlockDescent
