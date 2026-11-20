# Pre-registration — Gamow–Teller (spin) part of the β amplitude, λ(q)

Bean `qou-99qc`. Owner (Carl), 2026-11-20 ~20:15: *derive the β-decay rate as a function of q,
nothing chosen.* Written and committed BEFORE `qbeta_gt_spin_probe.py` is run.

## Inputs taken as given (not re-derived here)

* #8638 `QOU/QuarkState/ChargedCurrentW.lean`: strand-tracked Jimbo crossing `P·Ř = R₀ + h·(E⊗F)`;
  lepton = fourth strand, second copy of the strand space, `ν = u`, `e⁻ = d`; leftward positive
  passage `σ₁σ₂σ₃` gives the `n ν → e⁻ p` block `(h q)·T⁺`.
* `QOU/SchurWeyl/QuarkStrandConsequences.lean` Result 1: a FACTORISED strand space `A ⊗ B` with
  both factors Hecke at `q` is Hecke at no parameter. So at most one factor is `q`-braided.
* `QOU/SchurWeyl/ColourChannelSpinStatistics.lean`: colour `(1³)` forces the spin–flavour part
  into the symmetric channel `(3)` (the SU(6) 56 at `q = 1`).

## Corpus finding fixed before computing

No block or Lean declaration carries LORENTZ spin of a quark or lepton strand. `spin-labels`
and `q-angular-momentum` use the one `U_q(sl₂)` doublet that #8638 uses as isospin;
`electroweak-triplet-charge-spin-from-involution` states its "spin" is a sector label, not
Lorentz spin. Existing `g_A` routes (`Archimedean/AxialCoupling.lean`: `(5/3)·|tr_std|/|tr_sym|`;
`gt_matrix_pslq_probe.py`: `[5]_q/[4]_q`) select an irrep / a q-ratio against the target
`1.2754` and are fits under §NO FITTING; they are NOT used here.

## Two premises for where spin lives (the only two consistent with Result 1)

* **(A) factorised**: strand space `V_iso ⊗ V_spin`, isospin `q`-braided (Jimbo), spin braided
  classically by the swap `P` (spin rides on the strand).
* **(W) unfactorised**: strand space `C⁴ = {u↑,u↓,d↑,d↓}` with the `U_q(gl₄)` Jimbo crossing
  (Hecke at `q`, so Result 1 does not apply) — the `q`-Wigner spin–isospin supermultiplet.
  Its exchange term `h·Σ_{a<b} E_ab⊗E_ba` depends on an ORDERING of the four basis states.

## Predictions (stated before running)

* **P-A1**: under (A) the 4-strand passage commutes with every total-spin operator of the
  quark strands and with the lepton spin, so the β block is `(h q)·T⁺ ⊗ (spin carried)`;
  Fierz decomposition gives `c_GT = 0`: **λ(q) ≡ 0, 1+3λ² ≡ 1** for all `q`, including `q → 1`.
  (The SU(6) `5/3` needs `Σ σ_i τ_i⁺`, which no crossing supplies under (A).)
* **P-W1**: under (W) with an iso-major ordering (both `u` states before both `d` states), the
  single-crossing quark–lepton β current is `h·(τ⁺ ⊗ τ⁻) ⊗ P_spin`, and `P_spin = ½(1 + σ⃗·σ⃗)`
  gives a QUARK-level `λ_q = 1` exactly, independent of `q`.
* **P-W2**: of the 24 orderings, exactly 4 (u's first) give the full rotation-invariant
  current in the positive crossing; 4 (d's first) give it in the negative crossing; the other
  16 give a partial, rotation-non-invariant spin current.
* **P-W3** (CONDITIONAL, labelled choice C-SU6): nucleon states taken as the classical SU(6)
  `n↑, p↑` wavefunctions (the `q`-symmetric 20 of `U_q(gl₄)` has no Hopf-compatible
  `SU(2)_spin × SU(2)_iso` that separates `N` from `Δ`, so this is a choice). Expect
  `λ_N(1) = 5/3` (SU(6)) and some `λ_N(q₀) ≠ 5/3`. The comparison value `|λ| = 1.2754`
  is read only after the numbers are fixed. No outcome of P-W3 is wired anywhere.

Definition of λ (fixed now): write the β block as a 4×4 matrix `A` on
(nucleon spin ⊗ lepton spin), `c_μ = ¼ Tr((σ^μ ⊗ σ^μ)† A)`, `μ = 0..3`,
`1 + 3λ² := (|c₀|² + Σ_k |c_k|²)/|c₀|²`, λ signed by `c_z/c₀` when `c_x = c_y = c_z`.
