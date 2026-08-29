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

end QOU.AppendixSurreals.CollatzBlockDescent
