import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Proton tower residual = m_e · tr_M(C_Frob)

The pure-tower proton mass computation gives a residual against
CODATA that equals the Markov trace of the Frobenius co-Casimir
of H_3(q):

  Δm_p = m_e · tr_M(C_Frob) = m_e · Σ_{λ ⊢ 3} 1/dim_q(λ)
       = m_e · (2 + 1/[2]_q)

where dim_q(λ) is the q-hook-length dimension and
C_Frob = Σ_λ ([n]!_q / (dim_q(λ)² · dim(λ))) · p_λ is the
Frobenius co-Casimir of the Markov-trace pairing on H_n(q).

At q = 1 this reduces to the classical (5/2)·m_e via
dim_q(λ) → d_λ and [2]_q → 2.

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:partition-sum-proton-residual`
-/

namespace QOU.BraidKnot

/-- The inverse-dimension partition sum at level n.
    Trivial degenerate witness: 0 (the function is unreferenced
    downstream — `frobeniusCoCasimirTraceN3` uses the opaque `qInt2`
    instead). The intended Σ_{λ ⊢ n} 1/d_λ requires a partition
    enumerator + hook-length dimension; deferred. -/
noncomputable def invDimPartitionSum (_n : ℕ) : ℚ := 0

/-- The pure-tower proton mass, in MeV, computed from the
    mass-endomorphism tower at q = q_0 and converted to MeV via
    electron-trefoil calibration.  Axiomatized. -/
noncomputable opaque protonTowerMass : ℝ

/-- The CODATA proton mass, in MeV. -/
noncomputable opaque protonCodata : ℝ

/-- The electron rest-mass, in MeV. -/
noncomputable opaque electronMass : ℝ

/-- The substrate parameter q_0 and q-integer [2]_q = q + q⁻¹. -/
noncomputable opaque qSubstrate : ℝ
noncomputable opaque qInt2 : ℝ  -- = q_0 + 1/q_0

/-- The Markov trace of the Frobenius co-Casimir of H_n(q):
      tr_M(C_Frob) = Σ_{λ ⊢ n} 1/dim_q(λ).
    For n = 3 this equals 2 + 1/[2]_q. -/
noncomputable def frobeniusCoCasimirTraceN3 : ℝ :=
  2 + 1 / qInt2

/-- **Proton tower residual = m_e · tr_M(C_Frob).**

    The pure-tower proton residual equals the Markov trace of the
    Frobenius co-Casimir of H_3(q):

      m_p_CODATA - m_p_tower = m_e · (2 + 1/[2]_q).

    At q = 1: reduces to m_e · 5/2 (the classical limit).
    At q_0 = 1.11: evaluates to 1.2761 MeV, matching the observed
    residual 1.2779 MeV to 0.14%.

    Ref: [manuscript] §Frobenius derivation in
    `prop:partition-sum-proton-residual`;
    `folio-assistant/computations/frobenius_partition_sum.py`. -/
theorem proton_tower_residual_frobenius :
    ∃ (ε : ℝ), abs ε ≤ electronMass * (2 / 1000) ∧
      protonCodata - protonTowerMass =
        electronMass * frobeniusCoCasimirTraceN3 + ε := by
  -- ⚠ **EMPIRICAL GAP (not a missing-Lean-tactic gap).**
  -- The witness numerics at q_0 = 1.10998 give:
  --   observed residual  m_p_CODATA - m_p_tower ≈ 1.2779 MeV
  --   predicted          m_e · (2 + 1/[2]_q_0)   ≈ 1.2761 MeV
  --   diff |ε|           ≈ 0.00179 MeV (0.140 % relative)
  --   bound m_e · 2/1000 ≈ 0.00102 MeV
  -- ⇒ |ε| ≈ 0.00179 > 0.00102 ⇒ the bound stated above is too tight
  -- for the witnessed values; the theorem is empirically false as
  -- written.  Compounding this, the underlying tower mass is itself
  -- off by ~544 145 ppb per `proton-mass-50dps.derivation.json`
  -- (target 1 ppb, gap of ~6 orders of magnitude).
  --
  -- To close, one of the following content changes is required:
  --   (a) loosen the bound from `2/1000` to at least `4/1000`
  --       (the witnessed 0.00179 MeV fits within `m_e · 4/1000`),
  --   (b) refine `protonTowerMass` (Phase A: Terms 2-6 at full 50 dps
  --       without f64 chokepoints) so that the residual matches
  --       `m_e · (2 + 1/[2]_q)` within the 2‰ band, OR
  --   (c) demote this `theorem` to a `conjecture` block.
  --
  -- Until one of (a)-(c) is taken, this remains `sorry` BY DESIGN —
  -- closing it under the current bound would require `False`, since
  -- the same witness-axiom strategy used for the neutron case would
  -- here yield a contradiction (the same proof pattern would *prove
  -- the negation*).
  -- Ref: [manuscript] `folio-assistant/computations/frobenius_partition_sum.py`,
  -- `folio-assistant/computations/proton-mass-50dps.derivation.json`.
  sorry

/-- The CODATA neutron mass and the pure-tower neutron mass at q_0,
    in MeV.  Axiomatised opaques (computed in
    `folio-assistant/computations/six_term_consumer.py`). -/
noncomputable opaque neutronCodata : ℝ
noncomputable opaque neutronTowerMass : ℝ

/-! ### Witness-bound axioms.

The opaque constants above are pinned to numerical intervals derived
from the high-precision witness files at $q_0 = 1.10998$:

  * `electronMass_witness`   — CODATA 2022 electron rest energy
                               (0.51099895 MeV ± 1 keV interval)
  * `neutronCodata_witness`  — CODATA 2022 neutron rest energy
                               (939.56542 MeV ± 1 keV interval)
  * `neutronTowerMass_witness` — pure-tower neutron mass at $q_0$
                                 (per `six_term_consumer.py`,
                                 411.227 MeV ± 1 keV interval)

These are bona-fide *witness axioms*, not lazy `sorry`s: they bind
opaque numerical constants to bounds derived from external 50-dps
computations whose Lean formalisation is not feasible without
arbitrary-precision real arithmetic in Mathlib.  Any future replacement
of `electronMass`/`neutronCodata`/`neutronTowerMass` with verifiable
computable terms must invalidate these axioms first. -/

axiom electronMass_witness :
    (0.510998 : ℝ) ≤ electronMass ∧ electronMass ≤ (0.511000 : ℝ)

axiom neutronCodata_witness :
    (939.564 : ℝ) ≤ neutronCodata ∧ neutronCodata ≤ (939.566 : ℝ)

axiom neutronTowerMass_witness :
    (411.226 : ℝ) ≤ neutronTowerMass ∧ neutronTowerMass ≤ (411.228 : ℝ)

/-- The neutron counterpart fails: tower residual for the neutron
    is NOT (5/2)·m_e but rather ~1034·m_e, a factor-400 miss.

    The neutron-containing isotope binding failures (D, T, ³He,
    ⁴He) all inherit this gap.

    Statement: there is **no** ε with |ε| ≤ 3‰·m_e satisfying
    `m_n_codata − m_n_tower = (5/2)·m_e + ε`.  The bare numeric
    literals 939.565 / 411.227 of the previous formulation are
    moved into opaque values to keep the type-level statement
    structural; the witness gap (528.34 MeV vs 1.278 MeV predicted,
    factor 413) is recorded in the proof comment and the witness
    JSON.

    Ref: [manuscript] `rem:deuteron-first-principles`. -/
theorem neutron_tower_residual_5halves_fails :
    ¬ ∃ (ε : ℝ), abs ε ≤ electronMass * (3 / 1000) ∧
      neutronCodata - neutronTowerMass = electronMass * (5 / 2) + ε := by
  -- The witness-bound axioms above pin the opaques to numerical
  -- intervals at q_0; the contradiction is then a linarith/nlinarith
  -- consequence:
  --   ε = (neutronCodata - neutronTowerMass) - electronMass · 5/2
  --     ≥ 939.564 - 411.228 - 0.511 · 2.5 = 527.0585 MeV,
  --   |ε| ≤ electronMass · 3/1000 ≤ 0.511 · 0.003 < 1 MeV  →  ⊥.
  -- Ref: [manuscript] `rem:deuteron-first-principles`;
  -- \cite{wenzl1988} for the underlying neutron-mass-tower
  -- structural undershoot (V̂_0^n far from q_0 pole).
  rintro ⟨ε, hε_bound, hε_eq⟩
  obtain ⟨he_lo, he_hi⟩ := electronMass_witness
  obtain ⟨hnc_lo, _⟩ := neutronCodata_witness
  obtain ⟨_, hnt_hi⟩ := neutronTowerMass_witness
  -- Lower bound on ε from the witness intervals.
  have h_eps_lb : (527 : ℝ) ≤ ε := by nlinarith
  -- Upper bound on |ε| from the stated tolerance.
  have h_abs_ub : ε ≤ electronMass * (3 / 1000) := (abs_le.mp hε_bound).2
  -- The tolerance interval is far below 527 MeV.
  have h_tol_small : electronMass * (3 / 1000) ≤ (1 : ℝ) := by nlinarith
  linarith

end QOU.BraidKnot
