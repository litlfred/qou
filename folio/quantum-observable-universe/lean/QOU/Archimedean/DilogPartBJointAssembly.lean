import QOU.Archimedean.DilogPartBWP1Capstone
import QOU.Archimedean.DilogPartBEulerTail

/-!
# Joint-limit Part-B assembly (dilog Part B) — the second, Diophantine-gated closure

The coordination ledger (`docs/coordination/dilog-part-b-cusp-attack.md`) records **two**
routes to the Part-B total `reg_n → Li₂(x) − π²/3`:

* the **iterated** route (`wp1_outer_tendsto`, Diophantine-free but *weaker* — a `ρ→1⁻`
  after `q→1⁺` ordering), already assembled into the epic headline by
  `naStokes_physical_partB_value` (`DilogNaStokesOrdering.lean`), gated on the na-Stokes
  path-ordering *conjecture*;
* the **joint** `(q,n)` route — the physically/mathematically genuine limit — proved
  *conditionally* on an explicit Diophantine no-resonance bound by
  `tendsto_wp1_sum_of_no_resonance` (`DilogPartBWP1Capstone.lean`, #4270).

This file assembles the **joint** route: it fuses the joint W-P1 capstone with the W-P2
Euler / Dedekind-eta tail (`euler_tail_asymptotic`, composed along `p = 1/q → 1⁻`) into the
Part-B total, giving a **second, independent conditional closure** of the epic — under the
honest Diophantine no-resonance hypotheses carried *explicitly* in the signature (no
conjectural ordering class). Two independent confirmations of an open result strengthen it
(AGENTS.md §"Parallel exploration is valuable").

## Scope (honest, §"Conditional-proved ≠ premise-established")

The theorem proves the **implication**: under the joint filter `l` with `q→1`, the endpoint
`x·qⁿ→1⁻`, and the no-resonance bound `c(q−1) ≤ 1−x·qⁿ`, the combination
`W-P1 − wp2Tail → Li₂(x) − π²/3`. It does **not** discharge the no-resonance premise (the
unconditional joint limit is proved-*false* along a resonant counter-sequence — ledger
2026-07-25), and it does **not** re-prove the per-factor `k*`-split algebraic identity
`reg_n = W-P1 − wp2Tail` (that combinatorial reindexing is tracked separately; here the two
proved halves are combined exactly as `naStokes_physical_partB_value` combines its two class
hypotheses). `−π²/3 = −2·Li₂(1)` is an *abelian* dilog cusp value (two `π²/6` boundary
terms), **not** a curvature term (ledger 2026-07-26 correction).

## Base ring (§7c)

Archimedean throughout (`ℝ`): `LiTwo`, `Real.log`, `Real.pi`, and the one-sided filter
`𝓝[<] 1` live past the substrate→archimedean wall.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.Archimedean

open Filter Topology QOU.QPochhammer

/-- **W-P2 Euler-tail along the joint filter.**  The regularized negative-factor tail,
    written with the substrate variable `p = 1/q`, converges to `π²/6` along any filter on
    which `q → 1` (with `1 < q` eventually).  Immediate from `euler_tail_asymptotic`
    (`Tendsto _ (𝓝[<] 1) (𝓝 π²/6)`) composed with `1/q → 1⁻`: `q → 1` gives `(q)⁻¹ → 1`, and
    `1 < q` gives `(q)⁻¹ < 1`, so `(q)⁻¹ → 1⁻` lands in `𝓝[<] 1`. -/
theorem tendsto_wp2_tail_of_q {ι : Type*} {l : Filter ι} {q : ι → ℝ}
    (hq1 : ∀ᶠ i in l, 1 < q i) (hq : Tendsto q l (𝓝 (1 : ℝ))) :
    Tendsto (fun i => (1 - (q i)⁻¹) * ∑' m : ℕ, (-Real.log (1 - (q i)⁻¹ ^ (m + 1)))) l
      (𝓝 (Real.pi ^ 2 / 6)) := by
  have hinv : Tendsto (fun i => (q i)⁻¹) l (𝓝[<] (1 : ℝ)) := by
    rw [tendsto_nhdsWithin_iff]
    refine ⟨?_, ?_⟩
    · have h := hq.inv₀ (by norm_num : (1 : ℝ) ≠ 0)
      simpa using h
    · filter_upwards [hq1] with i hi
      have hqpos : (0 : ℝ) < q i := lt_trans one_pos hi
      simp only [Set.mem_Iio]
      rw [inv_lt_one₀ hqpos]
      exact hi
  exact euler_tail_asymptotic.comp hinv

/-- **Joint-limit Part-B total (conditional on Diophantine no-resonance).**  Along any filter
    `l` carrying substrate data `q → 1` (`1 < q` eventually), a partition index `n`, and a
    fixed target `0 < x`, with the going-up endpoint reaching the branch point
    (`x·qⁿ → 1⁻`) and the Diophantine no-resonance bound `c·(q−1) ≤ 1 − x·qⁿ` (`c > 0`), the
    Part-B combination

    `(q−1)·Σ_{k<n} log(1−x·qᵏ)  −  (1−q⁻¹)·Σ'_{m} (−log(1−q⁻ᵐ⁻¹))  ⟶  Li₂(x) − π²/3`.

    The first summand is the joint W-P1 (positive factors, → `Li₂(x) − π²/6` by
    `tendsto_wp1_sum_of_no_resonance`, #4270); the second is the W-P2 regularized
    negative-factor Euler tail (→ `π²/6` by `tendsto_wp2_tail_of_q`).  Their difference is the
    Part-B total `Li₂(x) − π²/3` (subtracted just as `naStokes_physical_partB_value` combines
    its two ordered pieces).  This is the **joint** route — the honest genuine limit — gated
    only on the explicitly-stated no-resonance premise, complementing the iterated (na-Stokes)
    route which reaches the same value under the ordering conjecture instead. -/
theorem tendsto_partB_total_joint_of_no_resonance
    {ι : Type*} {l : Filter ι} {x : ℝ} {q : ι → ℝ} {n : ι → ℕ} {c : ℝ}
    (hx0 : 0 < x) (hc : 0 < c)
    (hq1 : ∀ᶠ i in l, 1 < q i)
    (hbound : ∀ᶠ i in l, c * (q i - 1) ≤ 1 - x * q i ^ n i)
    (hxqn : Tendsto (fun i => x * q i ^ n i) l (𝓝[<] (1 : ℝ)))
    (hq : Tendsto q l (𝓝 (1 : ℝ))) :
    Tendsto (fun i =>
        (q i - 1) * ∑ k ∈ Finset.range (n i), Real.log (1 - x * q i ^ k)
        - (1 - (q i)⁻¹) * ∑' m : ℕ, (-Real.log (1 - (q i)⁻¹ ^ (m + 1))))
      l (𝓝 (LiTwo x - Real.pi ^ 2 / 3)) := by
  have hwp1 := tendsto_wp1_sum_of_no_resonance hx0 hc hq1 hbound hxqn hq
  have hwp2 := tendsto_wp2_tail_of_q hq1 hq
  have hsum := hwp1.sub hwp2
  have harith :
      LiTwo x - Real.pi ^ 2 / 6 - Real.pi ^ 2 / 6 = LiTwo x - Real.pi ^ 2 / 3 := by ring
  rw [harith] at hsum
  exact hsum

end QOU.Archimedean
