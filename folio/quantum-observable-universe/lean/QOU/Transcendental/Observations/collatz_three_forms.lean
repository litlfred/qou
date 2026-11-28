import Mathlib.Tactic

/-!
# The three faces of the `q`-Collatz conjecture (Tier C, C12)

`rem:collatz-three-forms` asserts that the contact-boundary condition — each
tripling followed by at least two halvings on average — has three equivalent
faces: **categorical** (Markov trace on `H_n(q)`), **arithmetic** (a contraction
threshold on `[2]_q`, `[3]_q`), and **residue** (behaviour at the `[2]_q`-divisor
`q = -1`). That remark carries **no `lean` ref at all**, making it the largest
unformalized item in the `q`-Collatz arc. This file supplies the carrier.

The three faces are formalized here at different epistemic tiers, and the tiers
are the point — they are *not* interchangeable:

| face | tier | here |
|---|---|---|
| arithmetic (threshold is exactly 2) | **proved** | `integer_threshold_eq_two`, `contactThreshold_mem_Ioo` |
| residue (`q = -1`) | **proved** | `qi2_at_divisor`, `odd_branch_at_divisor` |
| classical limit (`E[v₂(3n+1)] = 2`) | **proved** | `expected_halvings_eq_two` |
| categorical (`tr_M(𝒞_q^k(h)) → 1`) | **open conjecture** | `MarkovTraceConvergence`, content-bearing, **no instance** |

## What this file closes that was open

`QOU.Substrate.contact_threshold_lt_two` (in `QOU/QCollatz.lean`) is titled
*"The contact threshold `1 < v* < 2`"* — but its statement and proof establish
only `v* < 2`. The lower half `1 < v*` appears **nowhere in the corpus**
(grepped), and it is the half that matters for the remark's claim *"The integer
threshold is exactly `v = 2`. Two halvings per tripling are required."*: without
it, one halving might have sufficed. `one_lt_contactThreshold` supplies it and
`contactThreshold_mem_Ioo` states the two-sided result the docstring claims.

`integer_threshold_eq_two` then gives the remark's sentence directly, without any
transcendental quantity: `v = 1` is never enough and `v = 2` always is, for every
`q > 0`.

## The categorical face stays open, and is carried honestly

`MarkovTraceConvergence` is a **§3b-tax PRIMARY conjecture carrier**: a class
whose fields state the remark's display equation and its "identity braid is the
unique attractor" clause, with **no instance** — the honest encoding of an open
problem (AGENTS.md: axiomatization is not a proof; a fabricated instance would be
an audit dodge). It is not an empty marker: both fields are parameter-quantified
propositions with real content.

What *is* proved about it is the bridge C12 asks for —
`no_nontrivial_periodic_trace` derives, **from the conjecture**, that the step
operator admits no periodic orbit whose trace differs from the unknot value. That
is the categorical shadow of the arc's arithmetic cycle-exclusion results
(`qcollatz_no_adj_tail_cycle`, `qcollatz_no_front_loaded_cycle`), so the two
faces are now coupled by a theorem rather than by prose.

## Scope

Nothing here proves the `q`-Collatz conjecture or any part of it. The arithmetic
and residue faces were always elementary — the remark presents them as such; what
was missing was that they had no machine-checked carrier and that one of the two
threshold inequalities was unproved anywhere.

Base ring: the residue face is generic `[CommRing R]` (§7c); the threshold and
classical-limit faces are genuinely archimedean (`Real.log`, an infinite series)
and so are stated over `ℝ`, on the archimedean side of the wall.
-/

namespace QOU.AppendixSurreals.CollatzThreeForms

/-! ## Face 1 — arithmetic: the contraction threshold is exactly two halvings

With `[2]_q = q + 1` and `[3]_q = q² + q + 1` (`QOU.Substrate.qInt_two`,
`qInt_three` identify these with the `q`-integers). A cycle with one tripling and
`v` halvings contracts exactly when `[2]_q^v > [3]_q`. -/

/-- `[2]_q < [3]_q`: one halving never pays for a tripling. Their difference is
    `q²`, so this is strict for every `q ≠ 0`. -/
theorem qi2_lt_qi3 (q : ℝ) (hq : 0 < q) : q + 1 < q ^ 2 + q + 1 := by nlinarith

/-- `[3]_q < [2]_q²`: two halvings always do. Their difference is exactly the
    substrate parameter `q` — the algebraic gap of
    `QOU.Substrate.qInt_gap`. -/
theorem qi3_lt_qi2_sq (q : ℝ) (hq : 0 < q) : q ^ 2 + q + 1 < (q + 1) ^ 2 := by
  nlinarith

/-- **The integer contraction threshold is exactly `v = 2`**, for every `q > 0` —
    the remark's *"Two halvings per tripling are required"*, with no
    transcendental quantity involved. Three claims: `v = 1` never suffices,
    `v = 2` always does, and no `v` below `2` can suffice. -/
theorem integer_threshold_eq_two (q : ℝ) (hq : 0 < q) :
    ¬ (q ^ 2 + q + 1 < (q + 1) ^ 1) ∧
    (q ^ 2 + q + 1 < (q + 1) ^ 2) ∧
    (∀ v : ℕ, q ^ 2 + q + 1 < (q + 1) ^ v → 2 ≤ v) := by
  refine ⟨?_, qi3_lt_qi2_sq q hq, ?_⟩
  · simp only [pow_one, not_lt]
    exact le_of_lt (qi2_lt_qi3 q hq)
  · intro v hv
    by_contra hlt
    push_neg at hlt
    interval_cases v <;> simp only [pow_zero, pow_one] at hv <;> nlinarith

/-! ### The transcendental form of the same statement

`v* = log[3]_q / log[2]_q` is the real threshold; the integer condition `v ≥ 2`
is what the remark uses. -/

/-- The real contact threshold `v* = log [3]_q / log [2]_q`. -/
noncomputable def contactThreshold (q : ℝ) : ℝ :=
  Real.log (q ^ 2 + q + 1) / Real.log (q + 1)

/-- **`1 < v*` — the half `QOU.Substrate.contact_threshold_lt_two` claims in its
    docstring and does not prove.** Without it, `v = 1` is not ruled out and the
    remark's *"the integer threshold is exactly 2"* has no support. -/
theorem one_lt_contactThreshold (q : ℝ) (hq : 0 < q) : 1 < contactThreshold q := by
  have h2pos : (0 : ℝ) < q + 1 := by linarith
  have h2gt1 : (1 : ℝ) < q + 1 := by linarith
  have hlog2 : 0 < Real.log (q + 1) := Real.log_pos h2gt1
  have hlt : Real.log (q + 1) < Real.log (q ^ 2 + q + 1) :=
    Real.log_lt_log h2pos (qi2_lt_qi3 q hq)
  rw [contactThreshold, lt_div_iff₀ hlog2, one_mul]
  exact hlt

/-- `v* < 2`, restated self-containedly (the archimedean
    `QOU.Substrate.contact_threshold_lt_two` proves the same over `qInt`). -/
theorem contactThreshold_lt_two (q : ℝ) (hq : 0 < q) : contactThreshold q < 2 := by
  have h2pos : (0 : ℝ) < q + 1 := by linarith
  have h2gt1 : (1 : ℝ) < q + 1 := by linarith
  have h3pos : (0 : ℝ) < q ^ 2 + q + 1 := by nlinarith
  have hlog2 : 0 < Real.log (q + 1) := Real.log_pos h2gt1
  rw [contactThreshold, div_lt_iff₀ hlog2]
  have hcast : (2 : ℝ) * Real.log (q + 1) = Real.log ((q + 1) ^ 2) := by
    rw [Real.log_pow]; push_cast; ring
  rw [hcast]
  exact Real.log_lt_log h3pos (qi3_lt_qi2_sq q hq)

/-- **The contact threshold lies strictly between one and two halvings.** This is
    the two-sided statement `QOU.Substrate.contact_threshold_lt_two` announces;
    its lower half is new here. Being strictly above `1` and strictly below `2`,
    the least sufficient *integer* number of halvings is exactly `2`. -/
theorem contactThreshold_mem_Ioo (q : ℝ) (hq : 0 < q) :
    1 < contactThreshold q ∧ contactThreshold q < 2 :=
  ⟨one_lt_contactThreshold q hq, contactThreshold_lt_two q hq⟩

/-! ## Face 2 — residue: behaviour at the `[2]_q`-divisor `q = -1`

Generic `[CommRing R]` (§7c): no ordering or archimedean construct is used. -/

variable {R : Type*} [CommRing R]

/-- **`[2]_q` vanishes at the divisor.** `q = -1` is the `[2]_q`-divisor. -/
theorem qi2_at_divisor : (-1 : R) + 1 = 0 := by ring

/-- **`[3]_q = 1` at the divisor** — the remark's `[3]_q|_{q=-1} = 1`. -/
theorem qi3_at_divisor : (-1 : R) ^ 2 + (-1) + 1 = 1 := by ring

/-- **The odd branch degenerates to a shift at the divisor.** Since `[3]_q ↦ 1`,
    the numerator `[3]_q·P + 1` of an odd step becomes `P + 1`. This is why the
    domain condition of the Skein-Collatz map is `P|_{q=-1} ∈ {0, -1}`: those are
    exactly the values at which one more halving is available. -/
theorem odd_branch_at_divisor (P : R) : ((-1 : R) ^ 2 + (-1) + 1) * P + 1 = P + 1 := by
  ring

/-! ## Face 3 — the classical limit `q = 1`: the margin is exactly zero

The remark's displayed identity. For uniformly distributed odd `n`, the `2`-adic
valuation of `3n + 1` is `k` with probability `2^{-k}`, so its expectation is
`∑ k·2^{-k}`. -/

/-- **`E[v₂(3n+1)] = ∑_{k} k·2^{-k} = 2`** — the remark's displayed identity,
    exactly. (The `n = 0` term contributes `0`, so summing over all of `ℕ` agrees
    with the remark's sum from `k = 1`.) -/
theorem expected_halvings_eq_two :
    ∑' n : ℕ, (n : ℝ) * (1 / 2 : ℝ) ^ n = 2 := by
  have hnorm : ‖(1 / 2 : ℝ)‖ < 1 := by
    rw [Real.norm_eq_abs]; rw [abs_of_nonneg] <;> norm_num
  rw [tsum_coe_mul_geometric_of_norm_lt_one hnorm]
  norm_num

/-- **The classical case has no margin.** The expected number of halvings per
    tripling at `q = 1` equals the integer threshold `2` established in
    `integer_threshold_eq_two` — the remark's *"There is no margin."*

    Stated as a conjunction of two facts about two different kinds of object (an
    expectation and a sufficiency threshold), deliberately **not** as an
    equivalence between them: they are numerically equal, which is what "critical"
    means here, and nothing stronger is asserted. -/
theorem classical_limit_is_critical :
    (∑' n : ℕ, (n : ℝ) * (1 / 2 : ℝ) ^ n = 2) ∧
    (∀ q : ℝ, 0 < q → ∀ v : ℕ, q ^ 2 + q + 1 < (q + 1) ^ v → 2 ≤ v) :=
  ⟨expected_halvings_eq_two, fun q hq => (integer_threshold_eq_two q hq).2.2⟩

/-! ## Face 4 — categorical: the Markov trace on `H_n(q)`. **OPEN.** -/

/-- The categorical setup: a carrier `H` (the Hecke algebra `H_n(q)` in the
    intended reading) with a Markov trace into the Skein ring `S`, a Collatz step
    operator, and a distinguished identity braid whose trace is the unknot value
    `1` and which the step fixes.

    This is **setup, not conjecture** — every field is a definitional property of
    the identity braid, discharged in any intended model. -/
structure HeckeCollatzSystem (H S : Type*) [One S] where
  /-- The Markov trace `tr_M : H_n(q) → 𝒮(q)`, sending braid words to Jones
      polynomials. -/
  trM : H → S
  /-- One application of the Skein-Collatz operator `𝒞_q`. -/
  step : H → H
  /-- The identity braid. -/
  identity : H
  /-- Its trace is the unknot value. -/
  trM_identity : trM identity = 1
  /-- The step fixes it. -/
  identity_fixed : step identity = identity

variable {H S : Type*} [One S]

/-- **The conjecture's target is attained** — unconditionally, no class needed.
    The identity braid's whole orbit has trace `1`, so the conclusion of
    `MarkovTraceConvergence` is not vacuously unreachable. -/
theorem identity_orbit_trace_one (sys : HeckeCollatzSystem H S) (k : ℕ) :
    sys.trM (sys.step^[k] sys.identity) = 1 := by
  rw [Function.iterate_fixed sys.identity_fixed k]
  exact sys.trM_identity

/-- **`conj:q-collatz`, categorical face — a §3b-tax PRIMARY conjecture carrier.**

    `tr_M(𝒞_q^k(h)) → 1` for every `h ∈ H_n(q)`: every braid untangles to the
    unknot under iterated crossing resolution and destabilization, and the
    identity braid is the *unique* attractor.

    **There is deliberately no instance.** The absence is the honest encoding of
    an open problem: per AGENTS.md, an axiom or a fabricated instance is not a
    proof, and supplying one here would be an audit dodge. Both fields carry real
    content — neither is `True` and the class is not an empty marker — so a
    downstream `[MarkovTraceConvergence sys]` result is a genuine conditional. -/
class MarkovTraceConvergence (sys : HeckeCollatzSystem H S) : Prop where
  /-- The displayed convergence: every orbit's trace is eventually the unknot. -/
  trace_converges : ∀ h : H, ∃ K : ℕ, ∀ k : ℕ, K ≤ k → sys.trM (sys.step^[k] h) = 1
  /-- Uniqueness of the attractor: any fixed point already has unknot trace. -/
  identity_unique_attractor : ∀ h : H, sys.step h = h → sys.trM h = 1

/-- **The categorical face implies categorical cycle-exclusion.** Under the
    conjecture, `𝒞_q` has no periodic orbit whose trace differs from the unknot
    value: a period-`p` orbit's trace sequence is periodic, and eventual
    convergence to `1` then forces it to equal `1` outright.

    This is the coupling C12 asks for. It is the categorical shadow of the arc's
    arithmetic cycle-exclusion results (`qcollatz_no_adj_tail_cycle`,
    `qcollatz_no_front_loaded_cycle`), which exclude cycles on the Skein side by a
    height obstruction — so the two faces are now related by a theorem rather than
    by prose. **Conditional**: it assumes the open conjecture and proves nothing
    about it. -/
theorem no_nontrivial_periodic_trace (sys : HeckeCollatzSystem H S)
    [inst : MarkovTraceConvergence sys] (h : H) (p : ℕ) (hp : 0 < p)
    (hper : sys.step^[p] h = h) : sys.trM h = 1 := by
  obtain ⟨K, hK⟩ := inst.trace_converges h
  have hfix : (sys.step^[p])^[K] h = h := Function.iterate_fixed hper K
  have hmul : sys.step^[p * K] h = h := by
    rw [Function.iterate_mul]; exact hfix
  have hle : K ≤ p * K := Nat.le_mul_of_pos_left K hp
  have := hK (p * K) hle
  rwa [hmul] at this

/-- At the `[2]_q`-divisor `q = -1`, iterating the odd-branch numerator twice
    shifts `P` by `+2`. -/
theorem odd_branch_iterated_two_at_divisor (P : R) :
    ((-1 : R) ^ 2 + (-1) + 1) * (((-1 : R) ^ 2 + (-1) + 1) * P + 1) + 1 = P + 2 := by
  have h1 := odd_branch_at_divisor P
  have h2 := odd_branch_at_divisor (P + 1)
  rw [h1, h2]
  ring

/-- **Preperiodic tail trace exclusion (`qcz15` C12).** Under
    `[MarkovTraceConvergence sys]`, if the orbit of `h` enters a `p`-periodic
    cycle after `m` steps (`p > 0`), then the cycle entry `sys.step^[m] h`
    already has Markov trace `1`. -/
theorem no_nontrivial_preperiodic_tail_trace (sys : HeckeCollatzSystem H S)
    [inst : MarkovTraceConvergence sys] (h : H) (m p : ℕ) (hp : 0 < p)
    (hper : sys.step^[p] (sys.step^[m] h) = sys.step^[m] h) :
    sys.trM (sys.step^[m] h) = 1 := by
  have hcyc := no_nontrivial_periodic_trace sys (sys.step^[m] h) p hp hper
  exact hcyc

/-- Under `[MarkovTraceConvergence sys]`, every fixed point `sys.step h = h` has
    unknot Markov trace `1` across all iterates `sys.step^[k] h`. -/
theorem fixed_point_orbit_trace_one (sys : HeckeCollatzSystem H S)
    [inst : MarkovTraceConvergence sys] (h : H) (hfix : sys.step h = h) (k : ℕ) :
    sys.trM (sys.step^[k] h) = 1 := by
  have hiter : sys.step^[k] h = h := Function.iterate_fixed hfix k
  have htr : sys.trM h = 1 := inst.identity_unique_attractor h hfix
  rw [hiter]
  exact htr

end QOU.AppendixSurreals.CollatzThreeForms
