import Mathlib.Tactic

/-!
# Which UIC functional is Lean-provable: the gate needs data the block's formula discards

Owner ruling, 2026-09-12, verbatim: **"resolve functionals ... what lean provable"**.

`prop:unified-iterative-correction` displays

    B_λ = m_e · H_q(λ) · u_λ · ( ln|tr M_λ| − ln d_λ ),   summed "strictly over all λ",

while `computations/hecke_core_legacy.py::unified_iterative_correction` sums the
same shape over only those `λ` whose **signed** final trace satisfies
`tr M_λ(atom) ≤ 0` (Pass 2, lines 2176-2188).  The two differ by a measured
factor 3.4-4.6 (`hecke_core_legacy.py:2148-2153`).

This file is the resolution's mathematical content.  It is *not* a claim about
which functional the physics wants.  It is the structural fact that decides what
can be *stated*:

* the block's displayed summand reads the trace only through `ln|tr|`, hence is
  **even** in the trace — `uicAll_sign_blind`;
* the producer's gate reads `sign(tr)`, which evenness has destroyed, so the
  gated total is **not a function of the data the block displays** —
  `gate_not_a_function_of_displayed_data`;
* therefore the block's formula, as written, *cannot express* the producer's
  functional, whatever one decides about the physics.  Something has to move.

Two further results bear on which:

* `uicGated_cs_eq` — under **genuine** complementary slackness for a constraint
  `⟨Φ, π_λ⟩ ≥ 0`, "tight" means `tr = 0`, and then the gated functional collapses
  to `(Σ_{selected} c_λ) · f 0`: it carries **no trace information at all** and
  cannot distinguish two atoms.  So complementary slackness does not justify the
  coded gate `tr ≤ 0`; it justifies nothing that varies with the nucleus.
* `uicGated_nonpos` — a non-negative scale against a non-positive log-ratio forces
  `B ≤ 0` on the gated set, for any index set.  This is the Lean form of
  `computations/probes/uic_sign_forced_by_gate_probe.py`.

Nothing here is conditional on a class, and nothing here assumes the gate.
The degeneracy that removes the gate's stated justification is proved elsewhere
and sorry-free: `QOU.ParticleInteractions.y_0_eq_zero_of_radical`
(`operator_selection_lp.lean:390`).

## Base ring

Everything except the two explicit witnesses is generic `[CommRing R]`; the
witnesses are over `ℚ` because they need an order and a decidable `≤`.  No `ℝ`
appears — the archimedean instantiation (`f = fun x => Real.log |x| - Real.log d`
is even) lives in `QOU.MassTheory.UICLogSummandEven`, per AGENTS.md §7c.

## References

- Kerov 1996, q-hook walk on Young diagrams [kerov1996]
- Satuła et al. 1997, empirical Wigner energy [satula1997]
-/

namespace QOU.MassTheory.UICFunctionalSelection

open scoped BigOperators

variable {ι : Type*} [Fintype ι]
variable {R : Type*}

section CommRing

variable [CommRing R]

/-- The UIC accumulator summed over **every** block, as
`prop:unified-iterative-correction` states it.

`c i` is the per-partition scale `m_e · H_q(λ) · y_λ · ρ_λ(s_*)`, `τ i` is the
**signed** final Markov trace of block `i`, and `f` is the displayed summand
`x ↦ ln|x| − ln d`.  Writing it this way keeps the two arguments the block's
formula actually reads — the scale and the summand — separate from the sign,
which is what the theorems below turn on. -/
def uicAll (c : ι → R) (f : R → R) (τ : ι → R) : R :=
  ∑ i, c i * f (τ i)

/-- The UIC accumulator summed over a **selected** set of blocks, as
`hecke_core_legacy.unified_iterative_correction` Pass 2 computes it.  The
producer's selector is `sel i := (τ i ≤ 0)`. -/
def uicGated (c : ι → R) (f : R → R) (τ : ι → R)
    (sel : ι → Prop) [DecidablePred sel] : R :=
  ∑ i ∈ Finset.univ.filter sel, c i * f (τ i)

/-- **The block's functional is blind to the sign of the trace.**

Its summand reads the trace only through `|tr|` (evenness hypothesis `hf`), so
flipping the sign of any subset of the block traces leaves the total unchanged.
This is exactly the invariance the displayed formula `ln|tr M_λ| − ln d_λ`
manifestly has. -/
theorem uicAll_sign_blind (c : ι → R) (f : R → R) (hf : ∀ x : R, f (-x) = f x)
    (τ ε : ι → R) (hε : ∀ i, ε i = 1 ∨ ε i = -1) :
    uicAll c f (fun i => ε i * τ i) = uicAll c f τ := by
  unfold uicAll
  refine Finset.sum_congr rfl ?_
  intro i _
  show c i * f (ε i * τ i) = c i * f (τ i)
  rcases hε i with h | h
  · rw [h, one_mul]
  · rw [h, neg_one_mul, hf]

/-- **The gated and ungated totals differ by exactly the excluded blocks.**

Immediate, but it is the statement that makes the 3.4-4.6× measured gap a
*quantity* rather than a discrepancy: it is the sum over the slack blocks. -/
theorem uicGated_add_compl (c : ι → R) (f : R → R) (τ : ι → R)
    (sel : ι → Prop) [DecidablePred sel] :
    uicGated c f τ sel
      + ∑ i ∈ Finset.univ.filter (fun i => ¬ sel i), c i * f (τ i)
      = uicAll c f τ :=
  Finset.sum_filter_add_sum_filter_not _ _ _

/-- **The two functionals agree iff the excluded blocks contribute nothing.**

So "gate or no gate" is not a matter of degree that a tolerance could absorb:
they coincide on exactly the measure-zero condition that the slack blocks cancel. -/
theorem uicGated_eq_uicAll_iff (c : ι → R) (f : R → R) (τ : ι → R)
    (sel : ι → Prop) [DecidablePred sel] :
    uicGated c f τ sel = uicAll c f τ
      ↔ ∑ i ∈ Finset.univ.filter (fun i => ¬ sel i), c i * f (τ i) = 0 := by
  rw [← uicGated_add_compl c f τ sel]
  exact left_eq_add

/-- **Genuine complementary slackness collapses the functional to a constant.**

For a Frobenius positivity constraint `⟨Φ, π_λ⟩ ≥ 0`, complementary slackness
makes "tight" mean `tr = 0` — not `tr ≤ 0`, which is what the producer codes.
Under the genuine condition every selected block contributes the *same* value
`f 0`, so the total is `(Σ_{selected} c_λ) · f 0`: it reads nothing about the
atom.  A selection rule that cannot vary with the nucleus cannot be the source
of a nucleus-dependent binding energy, so complementary slackness does not
justify the coded gate. -/
theorem uicGated_cs_eq (c : ι → R) (f : R → R) (τ : ι → R)
    (sel : ι → Prop) [DecidablePred sel] (hcs : ∀ i, sel i → τ i = 0) :
    uicGated c f τ sel = (∑ i ∈ Finset.univ.filter sel, c i) * f 0 := by
  unfold uicGated
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl ?_
  intro i hi
  rw [hcs i ((Finset.mem_filter.mp hi).2)]

omit [Fintype ι] in
/-- **The genuine complementary-slackness set meets the log summand's domain
nowhere.**

`ln|x|` is the honest logarithm only where `x ≠ 0`; complementary slackness
selects exactly `x = 0`.  Stated over sets, so no decidability is needed. -/
theorem cs_selection_excludes_log_domain (τ : ι → R) (sel : ι → Prop)
    (hcs : ∀ i, sel i → τ i = 0) :
    {i : ι | sel i ∧ τ i ≠ 0} = (∅ : Set ι) := by
  ext i
  simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false, not_and, not_not]
  exact hcs i

end CommRing

section Ordered

variable [CommRing R] [PartialOrder R] [IsOrderedRing R]

/-- **A non-negative scale against a non-positive log-ratio forces `B ≤ 0`.**

The Lean form of `computations/probes/uic_sign_forced_by_gate_probe.py`: the
per-partition scale `m_e · H_q · y_λ · ρ_λ` is non-negative factor by factor
(measured: negative in 0 of 682 partitions), so the sign of the gated total is
decided entirely by the sign of the log-ratios on the selected set. -/
theorem uicGated_nonpos (c : ι → R) (f : R → R) (τ : ι → R)
    (sel : ι → Prop) [DecidablePred sel]
    (hc : ∀ i, 0 ≤ c i) (hf : ∀ i, sel i → f (τ i) ≤ 0) :
    uicGated c f τ sel ≤ 0 := by
  unfold uicGated
  refine Finset.sum_nonpos ?_
  intro i hi
  exact mul_nonpos_of_nonneg_of_nonpos (hc i) (hf i ((Finset.mem_filter.mp hi).2))

end Ordered

section ResolventField

variable [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The resolvent-damped scale `m_e · H_q(λ) · y_λ · ρ_λ(s)` with
`ρ_λ(s) = 1/(μ_λ + s)` — the factor the producer applies
(`hecke_core_legacy.py:548`, `:1915`) and the content block omits.  `def:q-resolvent`
gives `R_q(s) = (s + Δ̂_q)⁻¹`; on the `λ`-block of the Wedderburn decomposition
that is the scalar `1/(μ_λ + s)`. -/
def resolventScale (m_e Hq y mu s : R) : R :=
  m_e * Hq * y * (1 / (mu + s))

/-- **The resolvent factor never supplies a sign.**

Non-negative whenever its four inputs are, so adding it to the content block
changes the magnitude of every per-partition term and the sign of none.  This is
why divergence 2 is a statable omission rather than a disagreement: the block's
formula is the producer's with one non-negative factor deleted. -/
theorem resolventScale_nonneg
    (m_e Hq y mu s : R) (hm : 0 ≤ m_e) (hH : 0 ≤ Hq) (hy : 0 ≤ y)
    (hms : 0 < mu + s) : 0 ≤ resolventScale m_e Hq y mu s := by
  unfold resolventScale
  have h1 : (0 : R) ≤ 1 / (mu + s) := le_of_lt (by positivity)
  have h2 : (0 : R) ≤ m_e * Hq * y := by positivity
  exact mul_nonneg h2 h1


end ResolventField

/-! ## The discriminator, with an explicit witness

The witness is over `ℚ` with a single block.  `ℚ` because the gate needs a
decidable `≤`; one block because one is enough — the failure is not a matter of
size. -/

/-- **The producer's gate is not a function of the data the block's formula
displays.**

Two trace vectors that agree on *every* value the displayed formula reads —
`f (τ i)` for all `i` — give different gated totals.  So there is no way to
write the producer's functional in the block's own variables: the gate needs the
sign, and `ln|tr|` has already thrown it away.

This is the resolution's load-bearing theorem.  It says the mismatch is
structural, not editorial: the block's text is not a loose paraphrase of the
producer, it is a formula that *cannot* denote what the producer computes. -/
theorem gate_not_a_function_of_displayed_data :
    ∃ (c : Fin 1 → ℚ) (f : ℚ → ℚ) (τ τ' : Fin 1 → ℚ),
      (∀ x : ℚ, f (-x) = f x)
      ∧ (∀ i, f (τ i) = f (τ' i))
      ∧ uicAll c f τ = uicAll c f τ'
      ∧ uicGated c f τ (fun i => τ i ≤ 0) ≠ uicGated c f τ' (fun i => τ' i ≤ 0) := by
  refine ⟨fun _ => 1, fun x => |x|, fun _ => 1, fun _ => -1, fun x => abs_neg x, ?_, ?_, ?_⟩
  · intro i; simp
  · simp [uicAll]
  · simp [uicGated]

/-! ## Axiom audit -/

#print axioms uicAll_sign_blind
#print axioms uicGated_add_compl
#print axioms uicGated_eq_uicAll_iff
#print axioms uicGated_cs_eq
#print axioms cs_selection_excludes_log_domain
#print axioms uicGated_nonpos
#print axioms resolventScale_nonneg
#print axioms gate_not_a_function_of_displayed_data

end QOU.MassTheory.UICFunctionalSelection
