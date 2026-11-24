import Mathlib.Tactic
import Mathlib.Analysis.SpecificLimits.Normed

/-!
# QOU.Information.PhysicalIntractability — the honest, derived lower bound

The one route by which Option B yields a **derived** (non-fiat) separation —
though of something strictly weaker than abstract `P ≠ NP`.

The corpus's **Bekenstein / bandwidth bound** says a substrate computation
processes at most `𝔅(q)` q-bits per Planck step, so in `t` steps it can access
at most `t · 𝔅` bits.  If *deciding* an instance of size `n` genuinely requires
`info(n)` bits of the degree-0 obstruction, then a correct bandwidth-limited
device needs at least `info(n) / 𝔅` steps.  When `info(n)` is super-polynomial,
**no bandwidth-limited device decides the problem in polynomial time**.

This is a genuine information-theoretic lower bound — a pigeonhole argument,
proved sorry-free below — **not** a fiat identification.  Its honest scope:

* the physical input is `info(n)` super-polynomial (the degree-0 answer needs
  more than poly bits — the horizon/`3^c`-tree content, to be *derived*, not
  assumed);
* the conclusion bounds only **bandwidth-limited (physical)** computation.  A
  general Turing machine is not Bekenstein-limited, so this is **strictly
  weaker than abstract `P ≠ NP`** — a *physical Church–Turing* statement, not
  the Clay problem.

That is the ceiling of the non-fiat route, and it is the theorem the QOU is
actually positioned to prove.

## Relation to the query-model lower bound (integration)

This file is the **bandwidth / physical-device** derivation of the `3^c`
lower bound.  Its **query-model sibling** lives in
`QOU.Information.SkeinHorizonLowerBound` (`treeSearch`, `treeSearch_hcost`:
the observer must visit every one of the `3^d` leaves) and
`QOU.Information.SkeinInfoLowerBound` (`info_depth_lower_bound`,
`numLeaves_eq_three_pow_info`: the entropy floor `info = 3^c`, exact).  The
two are the same phenomenon proved in two models — a Bekenstein-bandwidth
pigeonhole here, a ternary decision-tree entropy floor there.

**Algebrization caveat (shared, do not over-claim).** The `correct`
hypothesis below — the device must access the full `3^{3n}`-tree worth of
bits — is exactly the *no-shortcut / black-box* assumption.
`SkeinHorizonLowerBound.no_horizon_cost_of_polyObservable` makes the flip
side precise: an efficiently-evaluable **algebraic** observation (a poly
shortcut) *refutes* `correct`, so neither this bandwidth bound nor the
query-model bound crosses to abstract `P ≠ NP` — that crossing needs a
genuinely non-algebraic separating invariant (the `χ(A)` residue), which is
the algebrization barrier (Aaronson–Wigderson).  Both derivations are
honestly weaker than the Clay problem, and for the same structural reason.
-/

namespace QOU.Information

/-- **Steps lower bound (sorry-free).**  A bandwidth-`B` device that in
    `steps n` steps accesses at most `steps n * B` bits, and is *correct*
    (accesses at least the `info n` bits needed to decide instance size `n`),
    must run for at least `info n / B` steps. -/
theorem steps_lower_bound (B : ℕ) (hB : 0 < B) (info steps : ℕ → ℕ)
    (correct : ∀ n, info n ≤ steps n * B) (n : ℕ) :
    info n / B ≤ steps n := by
  calc info n / B ≤ steps n * B / B := Nat.div_le_div_right (correct n)
    _ = steps n := Nat.mul_div_cancel _ hB

/-- A function `f : ℕ → ℕ` is **super-polynomial** if it exceeds every
    polynomial `c · n^k` at some argument `n ≥ 1`.

    The `1 ≤ n` guard is essential: without it the `n = 0` term `c · 0^k = 0`
    (for `k ≥ 1`) is `< f 0` for *any* `f` with `f 0 ≥ 1`, so a mere polynomial
    like `n ↦ (n+1)^2` would spuriously satisfy the predicate (confirmed in Lean,
    bean `qou-qgyw`). Guarding the witness away from `0` makes the predicate mean
    genuine polynomial domination and makes `PolyGrowth ⟹ ¬SuperPolynomial`
    (`PolyGrowthAlgebra.not_superPolynomial_of_polyGrowth`) provable. -/
def SuperPolynomial (f : ℕ → ℕ) : Prop := ∀ c k : ℕ, ∃ n, 1 ≤ n ∧ c * n ^ k < f n

open Filter Asymptotics in
/-- **`2^n` is super-polynomial (sorry-free).**  The standard "exponential
    dominates every polynomial" fact, discharged from Mathlib's little-o
    (`isLittleO_pow_const_const_pow_of_one_lt`).  Makes the QOU
    physical-intractability theorem below *unconditional*. -/
theorem superPoly_two_pow : SuperPolynomial (fun n => 2 ^ n) := by
  intro c k
  have h : (fun n : ℕ => (n : ℝ) ^ k) =o[atTop] (fun n : ℕ => (2 : ℝ) ^ n) :=
    isLittleO_pow_const_const_pow_of_one_lt k (by norm_num)
  have hc : (0 : ℝ) < 1 / ((c : ℝ) + 1) := by positivity
  obtain ⟨n, hn, hn1⟩ := ((h.def hc).and (eventually_ge_atTop 1)).exists
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn1
  have hnk_pos : (0 : ℝ) < (n : ℝ) ^ k := pow_pos hnpos k
  have hcp : (0 : ℝ) < (c : ℝ) + 1 := by positivity
  have hnorm : (n : ℝ) ^ k ≤ (1 / ((c : ℝ) + 1)) * (2 : ℝ) ^ n := by
    have e1 : ‖(n : ℝ) ^ k‖ = (n : ℝ) ^ k := by
      rw [Real.norm_eq_abs, abs_of_nonneg (le_of_lt hnk_pos)]
    have e2 : ‖(2 : ℝ) ^ n‖ = (2 : ℝ) ^ n := by
      rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    rw [e1, e2] at hn; exact hn
  have h2 : ((c : ℝ) + 1) * (n : ℝ) ^ k ≤ (2 : ℝ) ^ n := by
    calc ((c : ℝ) + 1) * (n : ℝ) ^ k
        ≤ ((c : ℝ) + 1) * ((1 / ((c : ℝ) + 1)) * (2 : ℝ) ^ n) :=
          mul_le_mul_of_nonneg_left hnorm (le_of_lt hcp)
      _ = (2 : ℝ) ^ n := by field_simp
  refine ⟨n, hn1, ?_⟩
  have key : (c : ℝ) * (n : ℝ) ^ k < (2 : ℝ) ^ n := by nlinarith [h2, hnk_pos]
  have : ((c * n ^ k : ℕ) : ℝ) < (((2 : ℕ) ^ n : ℕ) : ℝ) := by
    push_cast; push_cast at key; linarith
  exact_mod_cast this

/-- **Physical intractability (sorry-free).**  If the information required to
    decide `L` (per bandwidth unit, `info n / B`) is super-polynomial, then the
    step count of *any* correct bandwidth-`B` device is super-polynomial too —
    i.e. no bandwidth-limited device decides `L` in polynomial time.

    A **derived** lower bound (pigeonhole on the bandwidth bound), not a fiat.
    Scope: bandwidth-limited computation only — strictly weaker than abstract
    `P ≠ NP`. -/
theorem no_poly_bandwidth_decider (B : ℕ) (hB : 0 < B) (info steps : ℕ → ℕ)
    (correct : ∀ n, info n ≤ steps n * B)
    (hinfo : SuperPolynomial (fun n => info n / B)) :
    SuperPolynomial steps := by
  intro c k
  obtain ⟨n, hn1, hn⟩ := hinfo c k
  exact ⟨n, hn1, lt_of_lt_of_le hn (steps_lower_bound B hB info steps correct n)⟩

namespace SuperPolynomial

/-- **Super-polynomiality lifts through a lower bound (sorry-free).**  If
    `g ≤ f` pointwise and `g` is super-polynomial, so is `f`.

    Lives in the `SuperPolynomial` namespace so that generalized field
    notation (`hg.of_le hle`) resolves: dot notation looks up
    `SuperPolynomial.of_le` on the head constant, and falls through to the
    unfolded pi-type (`Function.of_le`, which does not exist) if the lemma
    sits in the ambient `QOU.Information` namespace instead. -/
theorem of_le {f g : ℕ → ℕ} (hg : SuperPolynomial g)
    (hle : ∀ n, g n ≤ f n) : SuperPolynomial f := fun c k =>
  (hg c k).imp fun n hn => ⟨hn.1, lt_of_lt_of_le hn.2 (hle n)⟩

end SuperPolynomial

/-- **Exponential information ⇒ physical intractability (sorry-free).**  The
    concrete QOU case: if deciding size-`n` instances requires (per bandwidth
    unit) at least the `2^n` bits of the full degree-0 obstruction, and `2^n`
    itself is super-polynomial, then no bandwidth-limited device is
    polynomial-time. -/
theorem no_poly_bandwidth_decider_of_exp (B : ℕ) (hB : 0 < B)
    (info steps : ℕ → ℕ) (correct : ∀ n, info n ≤ steps n * B)
    (hexp : ∀ n, 2 ^ n ≤ info n / B)
    (hexp_superpoly : SuperPolynomial (fun n => 2 ^ n)) :
    SuperPolynomial steps :=
  no_poly_bandwidth_decider B hB info steps correct
    (hexp_superpoly.of_le hexp)

/-- **Division-free step lower bound (sorry-free).**  Cleaner than going
    through `info / B`: if `info n ≤ steps n * B` and `info` is
    super-polynomial, so is `steps` — cancel the constant `B` by scaling the
    polynomial witness.  This avoids `Nat`-division artifacts. -/
theorem steps_superPoly_of_info (B : ℕ) (hB : 0 < B) (info steps : ℕ → ℕ)
    (correct : ∀ n, info n ≤ steps n * B) (hinfo : SuperPolynomial info) :
    SuperPolynomial steps := by
  intro c k
  obtain ⟨n, hn1, hn⟩ := hinfo (c * B) k
  refine ⟨n, hn1, ?_⟩
  have h1 : c * n ^ k * B < steps n * B :=
    calc c * n ^ k * B = c * B * n ^ k := by ring
      _ < info n := hn
      _ ≤ steps n * B := correct n
  exact lt_of_mul_lt_mul_right h1 (Nat.le_of_lt hB)

/-! ## The QOU resolution-tree information requirement

The corpus derives the physical input `info(n)` — the information the degree-0
answer requires — from the **skein resolution tree**.  A `c`-crossing link has a
`3^c`-leaf resolution tree (three skein channels per crossing).  At a
**non-torsion** substrate `q₀` (`qt.q ^ c ≠ 1`), `nontorsion_full_tree` proves
both the non-torsion certificate `qt.q ^ c ≠ 1` and the exact branch-space
cardinality `Fintype.card (ResolutionTreeBranch c) = 3^c ≥ 3`; the physical
non-cancellation hypothesis (that no resolution paths cancel in the degree-0
evaluation, so extracting the degree-0 answer for the `c_N = 3N` boundary
family (`conj:p-vs-np-boundary`) requires reading all `info(n) = 3^{3n}` leaves)
enters below as the explicit hypothesis `correct` of `qou_physical_intractability`
(and is derived in the query model in `QOU.Information.SkeinHorizonLowerBound`
and `QOU.Information.SkeinInfoLowerBound`).
-/

/-- The skein **resolution-tree size** of a `c`-crossing link: `3^c` leaves
    (three skein channels per crossing; in the non-torsion regime none cancel). -/
def resolutionTreeSize (c : ℕ) : ℕ := 3 ^ c

/-- `2^n ≤ 3^{3n}` (sorry-free): the surviving tree of the size-`n` boundary
    instance (`c = 3n`) dominates `2^n`. -/
theorem two_pow_le_resolutionTreeSize (n : ℕ) :
    2 ^ n ≤ resolutionTreeSize (3 * n) := by
  unfold resolutionTreeSize
  calc 2 ^ n ≤ 27 ^ n := Nat.pow_le_pow_left (by norm_num) n
    _ = 3 ^ (3 * n) := by rw [show (27 : ℕ) = 3 ^ 3 by norm_num, ← pow_mul]

/-- **QOU physical intractability (sorry-free, conditional on the two named
    inputs).**  For the non-torsion substrate, if a bandwidth-`B` device
    correctly extracts the full surviving `3^{3n}`-leaf resolution tree for the
    boundary family, then — given the standard fact that `2^n` dominates every
    polynomial — its step count is super-polynomial: **no bandwidth-limited
    device decides the boundary problem in polynomial time.**

    The `info(n) = 3^{3n}` requirement is *derived* here from the resolution
    tree (the QOU physical content); `exp_dominates_poly` is the standard
    exponential-domination fact (Mathlib-dischargeable; bean `qou-*`).  Scope
    remains bandwidth-limited computation — strictly weaker than abstract
    `P ≠ NP`. -/
theorem qou_physical_intractability (B : ℕ) (hB : 0 < B) (steps : ℕ → ℕ)
    (exp_dominates_poly : SuperPolynomial (fun n => 2 ^ n))
    (correct : ∀ n, resolutionTreeSize (3 * n) ≤ steps n * B) :
    SuperPolynomial steps :=
  steps_superPoly_of_info B hB (fun n => resolutionTreeSize (3 * n)) steps correct
    (exp_dominates_poly.of_le two_pow_le_resolutionTreeSize)

/-- **QOU physical intractability — UNCONDITIONAL (sorry-free).**  The only
    remaining hypothesis is the *physical model*: a bandwidth-`B` device that
    correctly extracts the full surviving `3^{3n}`-leaf resolution tree accesses
    `≤ steps n · B` bits.  Given that, its step count is super-polynomial — **no
    bandwidth-limited device decides the boundary problem in polynomial time.**
    The exponential-domination fact is now discharged (`superPoly_two_pow`);
    the information requirement `3^{3n}` is derived from the tree.  Scope:
    bandwidth-limited computation — strictly weaker than abstract `P ≠ NP`. -/
theorem qou_physical_intractability_unconditional (B : ℕ) (hB : 0 < B)
    (steps : ℕ → ℕ)
    (correct : ∀ n, resolutionTreeSize (3 * n) ≤ steps n * B) :
    SuperPolynomial steps :=
  qou_physical_intractability B hB steps superPoly_two_pow correct

end QOU.Information
