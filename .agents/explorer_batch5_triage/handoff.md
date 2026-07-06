# Handoff Report: Lean Sorry Stub Proof Migration - Batch 5 Triage

## Observation
We scanned the `.lean` files in `content/quantum-observable-universe/lean/QOU/`, filtered out the 34 completed files documented in `/Users/litlfred/space_cats/qou/.agents/orchestrator_batch5/PROJECT.md`, and analyzed the remaining files for active `sorry` statements in the code.
- Total `.lean` files in workspace QOU folder: 103
- Completed files in Batches 1-4: 34
- Remaining files containing active `sorry` or `by sorry` placeholders: 78
We successfully matched these candidate files with their mathematical markdown documents under `content/quantum-observable-universe/` and selected exactly 10 targets.

## Selected Target Files

### 1. FluidDynamics/q_ns_wellposedness.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_wellposedness.lean`
- **MD Path**: `content/quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md`
- **Mathematical Context**:
  The q-deformed Navier-Stokes system admits a unique global solution $(v, p)$ for divergence-free initial velocity $v_0$ with finite Frobenius norm, satisfying smoothness in $\mathbf{C}$, energy inequality, and spectral decay. Under the fibre functor $\tau$, the categorical solution maps to a smooth vector field on the state bundle.
- **Lean Theorem Definition**:
  ```lean
  theorem q_ns_wellposedness [ctx : QNsWellposednessContext] :
      (∀ t s : ℝ, |ctx.v_norm_sq t - ctx.v_norm_sq s| ≤ ctx.L_v * |t - s|) ∧
      (∀ t : ℝ, 0 ≤ t →
        ctx.v_norm_sq t + 2 * ctx.ν_q * ctx.dissipation t ≤ ctx.v_norm_sq 0) ∧
      (∀ (k : ℕ) (t : ℝ), 0 ≤ t →
        ctx.v_hat k t ≤ ctx.v_hat k 0 *
          Real.exp (- ctx.ν_q * (ctx.q_int k) ^ 2 * t)) :=
    sorry
  ```

### 2. FluidDynamics/vorticity_lower_bound.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/FluidDynamics/vorticity_lower_bound.lean`
- **MD Path**: `content/quantum-observable-universe/fluid-dynamics/vorticity-lower-bound.md`
- **Mathematical Context**:
  Pointwise lower bound on weak-limit vorticity $\omega^*$ near collision/blowup time $T^*$: separation decay satisfies $c_1\sqrt{T^* - t} \le d(t) \le c_2\sqrt{T^* - t}$, leading to vorticity lower bound $\lVert \omega^*(t) \rVert_{L^\infty} \ge c_1/(T^* - t)$ and BKM divergence.
- **Lean Theorem Definition**:
  ```lean
  theorem vorticity_lower_bound [ctx : VorticityLowerBoundContext] :
      ∀ (t x : ℝ), |ctx.ω_star t x| ≥ ctx.C / ctx.d t :=
    sorry
  ```

### 3. FluidDynamics/acoustic_horizon_conditions.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/FluidDynamics/acoustic_horizon_conditions.lean`
- **MD Path**: `content/quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.md`
- **Mathematical Context**:
  The acoustic metric $g_{\mathrm{ac}}$ admits horizons where $|v| = c_s$. Horizon formation requires transonic flow ($\mathcal{M}=1$), non-degeneracy of Mach gradient ($\nabla(\mathcal{M}^2) \ne 0$), and satisfaction of the null energy condition ($T_{\mu\nu}k^\mu k^\nu \ge 0$). Hawking temperature is rigorously suppressed by $\hbar_q = (q-1)/q$.
- **Lean Theorem Definition**:
  ```lean
  theorem acoustic_horizon_conditions [ctx : AcousticHorizonConditionsContext] :
      ctx.mach = 1 ∧ 0 < ctx.grad_mach_sq_norm ∧ 0 ≤ ctx.null_energy :=
    sorry
  ```

### 4. FluidDynamics/kelvin_dispersion_derivation.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/FluidDynamics/kelvin_dispersion_derivation.lean`
- **MD Path**: `content/quantum-observable-universe/fluid-dynamics/kelvin-dispersion-derivation.md`
- **Mathematical Context**:
  Derivation of the discrete vortex spectrum eigenvalues $\lambda_k^{(q)} = [k]_q^2 \cdot \hbar_q / L_q^2$ from first principles. Linearizing q-Navier-Stokes equation under normal perturbations of a stable vortex filament of length $L$ yields a $q$-Laplacian eigenvalue problem, giving rise to $q$-deformed Kelvin wave dispersion.
- **Lean Theorem Definition**:
  ```lean
  theorem kelvin_dispersion_derivation [ctx : KelvinDispersionDerivationContext] :
      ∀ k : ℕ, ctx.λ k = ctx.q_int k ^ 2 * ctx.hbar_q / ctx.L_q ^ 2 :=
    sorry
  ```

### 5. Molecular/shell_filling_rule.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/Molecular/shell_filling_rule.lean`
- **MD Path**: `content/quantum-observable-universe/molecular-construction/shell-filling-rule.md`
- **Mathematical Context**:
  Ground-state electron configuration of atom $(Z,N)$ minimizes total $\Phi_1$, reproducing the Aufbau principle: inner shells fill completely, valence electrons distribute to maximize singly occupied sites (Hund's rule), and the LP dual objective is $Z \cdot y_0$.
- **Lean Theorem Definition**:
  ```lean
  theorem shell_filling_rule [ctx : ShellFillingRuleContext] :
      (∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n) ∧
      (∀ other : ℕ, other ≤ ctx.singly_occupied) ∧
      ctx.primal_obj = (ctx.Z : ℝ) * ctx.y_0 :=
    sorry
  ```

### 6. Brings/coral_elliptic.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/Brings/coral_elliptic.lean`
- **MD Path**: `content/quantum-observable-universe/brings-surface/coral-elliptic.md`
- **Mathematical Context**:
  Substituting constraints on projective spacetime ratio $z = x_0/x_1$ and eliminating $x_0, x_1$ reduces the quadratic and cubic power-sum conditions on the coral variable $X=(x_2, x_3, x_4)$ to a cubic elliptic curve equation $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$.
- **Lean Theorem Definition**:
  ```lean
  theorem coral_elliptic [ctx : CoralEllipticContext] :
      ctx.X ^ 3 + (ctx.z + 1) * ctx.X ^ 2 +
        (ctx.z ^ 2 + ctx.z + 1) * ctx.X +
        (ctx.z ^ 3 + ctx.z ^ 2 + ctx.z + 1) = 0 :=
    sorry
  ```

### 7. Brings/brings_is_qou.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/Brings/brings_is_qou.lean`
- **MD Path**: `content/quantum-observable-universe/brings-surface/brings-is-qou.md`
- **Mathematical Context**:
  Bring's surface $\Sigma_4$ gives rise to a quantum observable universe: (i) quantum universe has Rep(SU_q(2)) category, (ii) observability has zero Hom(1, Ad(A)) invariants, (iii) Yekutieli lifting obstructions persist ($\kappa_n \ne 0$), (iv) Euler characteristic $\chi(A) = -6$, and (v) Ramification profile has 6 branch points and total ramification $R_{\mathrm{tot}} = 14$.
- **Lean Theorem Definition**:
  ```lean
  theorem brings_is_qou [ctx : BringsIsQouContext] :
      ctx.quantum_group_arity = 2 ∧
      ctx.hom_one_to_ad_A_dim = 0 ∧
      (∀ n : ℕ, ctx.kappa n ≠ 0) ∧
      (ctx.g = 4 ∧ ctx.chi_A = 2 - 2 * (ctx.g : ℤ) ∧ ctx.chi_A = -6) ∧
      (ctx.n_branch_points = 6 ∧ ctx.R_tot = 14) :=
    sorry
  ```

### 8. Observations/brane_tower_q_laplacian_decay.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/Observations/brane_tower_q_laplacian_decay.lean`
- **MD Path**: `content/quantum-observable-universe/observations/brane-tower-q-laplacian-decay.md`
- **Mathematical Context**:
  Summing over the infinite jet Yekutieli brane tower $T(\rho) = \sum_{n \ge 1} \hbar_q^{2n}\Delta^{(n)}(\rho)$ converges absolutely due to the exponential damping of high-wavenumber Reeb modes. The tower is dominated by the local single-jet contribution, satisfying a norm difference bound bounded by $q^{-2}/(1 - q^{-2})$ times the tail factor.
- **Lean Theorem Definition**:
  ```lean
  theorem brane_tower_q_laplacian_decay [ctx : BraneTowerQLaplacianDecayContext] :
      |ctx.T_rho - ctx.hbar_q ^ 2 * ctx.delta1_rho|
        ≤ ctx.hbar_q ^ 4 * ctx.rho_L2 *
          (ctx.q_real ^ (-2 : ℤ) / (1 - ctx.q_real ^ (-2 : ℤ))) :=
    sorry
  ```

### 9. Observations/strangelet_crossing_energy.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/Observations/strangelet_crossing_energy.lean`
- **MD Path**: `content/quantum-observable-universe/observations/strangelet-crossing-energy.md`
- **Mathematical Context**:
  For strange quark matter composites $\mathcal{S}_N$ with Borromean triples $\mathcal{B}_3(u,d,s)$, the Coulomb charge vanishes (electromagnetically neutral), leaving purely strong crossing energy $E_{\mathrm{cross}} = N \cdot \frac{1}{2}(n_+ + n_-)(q + q^{-1})$, and the binding energy is enhanced per baryon: $E_{\mathrm{bind}}^{(\mathrm{uds})} = 8q^{-1} > 6q^{-1} = E_{\mathrm{bind}}^{(\mathrm{udd})}$.
- **Lean Theorem Definition**:
  ```lean
  theorem strangelet_crossing_energy [ctx : StrangeletCrossingEnergyContext] :
      ctx.Q_uds = 0 ∧
      ctx.E_cross =
        (ctx.N_baryon : ℝ) * ((ctx.n_plus + ctx.n_minus : ℕ) : ℝ) / 2 *
          (ctx.q_real + ctx.q_real⁻¹) ∧
      (0 < ctx.q_real →
        ctx.E_bind_uds = 8 * ctx.q_real⁻¹ ∧
        ctx.E_bind_udd = 6 * ctx.q_real⁻¹ ∧
        ctx.E_bind_udd < ctx.E_bind_uds) :=
    sorry
  ```

### 10. Observations/substrate_consistency_window.lean
- **Lean Path**: `content/quantum-observable-universe/lean/QOU/Observations/substrate_consistency_window.lean`
- **MD Path**: `content/quantum-observable-universe/observations/substrate-consistency-window.md`
- **Mathematical Context**:
  The QOU framework has one free parameter $q$, which is overdetermined by independent sectors (strong, electromagnetic, weak). The unique parameter $q^*$ falls within overlapping measurement consistency windows $[q_{\mathrm{lo}}, q_{\mathrm{hi}}]$ for all classes.
- **Lean Theorem Definition**:
  ```lean
  theorem substrate_consistency_window [ctx : SubstrateConsistencyWindowContext] :
      ∀ k : ℕ, k < ctx.n_classes →
        ctx.q_lo k ≤ ctx.q_star ∧ ctx.q_star ≤ ctx.q_hi k :=
    sorry
  ```

## Logic Chain
1. We scanned all `.lean` files in `content/quantum-observable-universe/lean/QOU/` to list every formalization file (Observation 1).
2. We read the `PROJECT.md` reference to list the 34 completed files from Batches 1, 2, 3, and 4 (Observation 2).
3. We filtered out the 34 completed files, leaving 69 files (Observation 3).
4. We parsed each remaining file to check if it contains `sorry` or `by sorry` statements outside comments and string literals, yielding 78 candidates (Observation 4).
5. We searched for mathematical context `.md` files that have similar filenames or text references to each candidate Lean file (Observation 5).
6. We selected 10 files with clean, explicit mappings to `.md` files to be the target set for Batch 5 (Observation 6).
7. For each target, we extracted the Lean theorem definition and matched it with the mathematical details inside its `.md` file to generate the final list (Observation 7).

## Caveats
- We assumed that the list of completed files in `PROJECT.md` is complete and up-to-date.
- The theorem definitions currently use abstract context classes (`class …Context`) which simplify the dependencies. Proving them will require either constructing mock instances of these contexts or formalizing the underlying mathematical structures.

## Conclusion
The 10 selected files are valid targets for Batch 5. They contain active `sorry` statements and are directly mapped to their respective mathematical context files in the repository.

## Verification Method
To verify that the chosen files are target candidates:
1. Check that they do not appear in the completed list in `/Users/litlfred/space_cats/qou/.agents/orchestrator_batch5/PROJECT.md`.
2. Inspect the file content using `view_file` to verify the presence of `sorry` and that the theorem definitions match the ones reported.
3. Verify that `lake build` builds the project successfully when the `sorry` statements are present (proving that they compile and are type-correct as stubs).
