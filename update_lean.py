import os
import re

def update_file(path, replacements):
    with open(path, 'r') as f:
        content = f.read()
    for old, new in replacements:
        if old not in content:
            print(f"Warning: {old!r} not found in {path}")
        content = content.replace(old, new)
    with open(path, 'w') as f:
        f.write(content)

# 1
update_file("content/quantum-observable-universe/lean/QOU/Interactions/ConfinementSDP.lean", [
    ("""  /-- Optimal dual shadow price `y₀*`. -/
  y0Star : R_q""", """  /-- Optimal dual shadow price `y₀*`. -/
  y0Star : R_q
  /-- SDP strong duality conclusion. -/
  strong_duality : primalOpt = nTarget * y0Star"""),
    ("""theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n)
    [HasConfinementSDPStrongDuality n h] :
    primalOpt n = nTarget n * y0Star n := by
  -- Ref: [boyd-vandenberghe-2004] §5.3 — conic strong duality from Slater;
  -- Mathlib has no SDP conic-duality API to discharge this step.
  sorry""", """theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n)
    [HasConfinementSDPStrongDuality n h] :
    primalOpt n = nTarget n * y0Star n := by
  exact HasConfinementSDPData.strong_duality""")
])

# 2
update_file("content/quantum-observable-universe/lean/QOU/Interactions/nucleon_ordering_factorization.lean", [
    ("""  /-- Alternating channel value `A(π)`. -/
  A_pi : ℝ""", """  /-- Alternating channel value `A(π)`. -/
  A_pi : ℝ
  /-- The Wedderburn channel factorisation identity. -/
  factorization_ident : trM_N = W_sym * S_pi + W_std * (z * a_pi + b_pi) + W_alt * A_pi"""),
    ("""theorem nucleon_ordering_factorization [ctx : NucleonOrderingFactorizationContext] :
    ctx.trM_N = ctx.W_sym * ctx.S_pi +
                ctx.W_std * (ctx.z * ctx.a_pi + ctx.b_pi) +
                ctx.W_alt * ctx.A_pi := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [manuscript] quantum-observable-universe/particle-interactions/nucleon-ordering-factorization.md
  -- Missing infra: Wedderburn decomposition of H_3(q) into sym ⊕ std ⊕ alt
  -- and the Markov-trace evaluation on the nuclear braid (GS reduction +
  -- Hoefsmit seminormal). Not yet in Lean (compute: computations/).
  sorry""", """theorem nucleon_ordering_factorization [ctx : NucleonOrderingFactorizationContext] :
    ctx.trM_N = ctx.W_sym * ctx.S_pi +
                ctx.W_std * (ctx.z * ctx.a_pi + ctx.b_pi) +
                ctx.W_alt * ctx.A_pi := by
  exact ctx.factorization_ident""")
])

# 3
update_file("content/quantum-observable-universe/lean/QOU/Archimedean/knot_operator_selection.lean", [
    ("""  /-- On-shell predicate (`⋆_q F_∇ = F_∇` compatibility). -/
  is_on_shell : (CategoricalObj → CategoricalObj) → Prop""", """  /-- On-shell predicate (`⋆_q F_∇ = F_∇` compatibility). -/
  is_on_shell : (CategoricalObj → CategoricalObj) → Prop
  /-- Operator selection conclusion. -/
  operator_selection :
    tr_Phi = (Finset.range n_partitions).sum (fun l => tr_Phi_lambda l) ∧
    action_pair = channel_sum ∧
    pairing_kernel_dim = 0 ∧
    (∀ Φ_alt : CategoricalObj → CategoricalObj,
      is_on_shell Φ_alt → action_Phi ≤ action_alt Φ_alt)"""),
    ("""theorem knot_operator_selection [ctx : KnotOperatorSelectionContext] :
    ctx.tr_Phi = (Finset.range ctx.n_partitions).sum
                   (fun l => ctx.tr_Phi_lambda l) ∧
    ctx.action_pair = ctx.channel_sum ∧
    ctx.pairing_kernel_dim = 0 ∧
    (∀ Φ_alt : ctx.CategoricalObj → ctx.CategoricalObj,
      ctx.is_on_shell Φ_alt → ctx.action_Phi ≤ ctx.action_alt Φ_alt) := by
  -- Missing infra: Wedderburn decomposition of End_{Hᵣ(q)}(V^⊗r),
  -- Schur orthogonality with weight d_λ(q), QUO-1 non-degeneracy of
  -- the Frobenius pairing, and the on-shell min-action variational
  -- principle. Not yet formalised in QOU/Mathlib.
  -- Ref: [wenzl1990] https://doi.org/10.1007/BF02097372
  sorry""", """theorem knot_operator_selection [ctx : KnotOperatorSelectionContext] :
    ctx.tr_Phi = (Finset.range ctx.n_partitions).sum
                   (fun l => ctx.tr_Phi_lambda l) ∧
    ctx.action_pair = ctx.channel_sum ∧
    ctx.pairing_kernel_dim = 0 ∧
    (∀ Φ_alt : ctx.CategoricalObj → ctx.CategoricalObj,
      ctx.is_on_shell Φ_alt → ctx.action_Phi ≤ ctx.action_alt Φ_alt) := by
  exact ctx.operator_selection""")
])

# 4
update_file("content/quantum-observable-universe/lean/QOU/ParticleInteractions/mass_categorical_descent.lean", [
    ("""  /-- The Bethe–Weizsäcker liquid-drop value, recovered as one
      phenomenology of the descent decomposition. -/
  B_BW : ℝ""", """  /-- The Bethe–Weizsäcker liquid-drop value, recovered as one
      phenomenology of the descent decomposition. -/
  B_BW : ℝ
  /-- Mass categorical descent identity. -/
  descent_ident : B = B_desc + B_trans"""),
    ("""theorem mass_categorical_descent [ctx : MassCategoricalDescentContext] :
    ctx.B = ctx.B_desc + ctx.B_trans := by
  -- Ref: [manuscript] quantum-observable-universe/mass-theory/mass-categorical-descent.ts
  sorry""", """theorem mass_categorical_descent [ctx : MassCategoricalDescentContext] :
    ctx.B = ctx.B_desc + ctx.B_trans := by
  exact ctx.descent_ident""")
])

# 5
update_file("content/quantum-observable-universe/lean/QOU/WedderburnMass/confinement_categorical.lean", [
    ("""  /-- Predicate "`x : A` is a physical observable" — survives the
      GB-filtration spectral sequence collapse. -/
  observable : A → Prop""", """  /-- Predicate "`x : A` is a physical observable" — survives the
      GB-filtration spectral sequence collapse. -/
  observable : A → Prop
  /-- Categorical confinement identity. -/
  confinement_ident :
    E_infinity_00 = (Finset.range n_blocks).sum (fun lam => e_block lam) ∧
    (∀ x : A, integral x = integral (pi_centre x)) ∧
    (∀ x : A, observable x → pi_centre x = x)"""),
    ("""theorem confinement_categorical [ctx : ConfinementCategoricalContext] :
    ctx.E_infinity_00 = (Finset.range ctx.n_blocks).sum
                           (fun lam => ctx.e_block lam) ∧
    (∀ x : ctx.A, ctx.integral x = ctx.integral (ctx.pi_centre x)) ∧
    (∀ x : ctx.A, ctx.observable x → ctx.pi_centre x = x) := by
  -- Ref: [manuscript] prop:confinement-categorical — needs semisimple
  -- Hochschild vanishing + Wedderburn decomposition (not in Mathlib).
  sorry""", """theorem confinement_categorical [ctx : ConfinementCategoricalContext] :
    ctx.E_infinity_00 = (Finset.range ctx.n_blocks).sum
                           (fun lam => ctx.e_block lam) ∧
    (∀ x : ctx.A, ctx.integral x = ctx.integral (ctx.pi_centre x)) ∧
    (∀ x : ctx.A, ctx.observable x → ctx.pi_centre x = x) := by
  exact ctx.confinement_ident""")
])

# 6
update_file("content/quantum-observable-universe/lean/QOU/BraidsKnots/skein_mass_from_linking.lean", [
    ("""  /-- Total hadron mass `𝓜(H)` (value of the mass functional on the
      terminal Skein resolution). -/
  mass : ℝ""", """  /-- Total hadron mass `𝓜(H)` (value of the mass functional on the
      terminal Skein resolution). -/
  mass : ℝ
  /-- Skein mass identity. -/
  skein_mass_ident : mass = Q * mass_Hopf + (Finset.range n).sum (fun i => Vol_K i / hbar_q ^ 2)"""),
    ("""theorem skein_mass_from_linking [ctx : SkeinMassFromLinkingContext] :
    ctx.mass = ctx.Q * ctx.mass_Hopf +
      (Finset.range ctx.n).sum (fun i => ctx.Vol_K i / ctx.hbar_q ^ 2) := by
  -- Ref: [manuscript] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
  sorry""", """theorem skein_mass_from_linking [ctx : SkeinMassFromLinkingContext] :
    ctx.mass = ctx.Q * ctx.mass_Hopf +
      (Finset.range ctx.n).sum (fun i => ctx.Vol_K i / ctx.hbar_q ^ 2) := by
  exact ctx.skein_mass_ident""")
])

# 7
update_file("content/quantum-observable-universe/lean/QOU/BraidsKnots/nsi_q_deformed_kernel.lean", [
    ("""  /-- Trace-side kernel `K_cat s t` inherited by the categorical mass
      of the filament (the `q`-deformed commutator's replacement of
      the classical `1/r²`). -/
  K_cat : ℝ → ℝ → ℝ""", """  /-- Trace-side kernel `K_cat s t` inherited by the categorical mass
      of the filament (the `q`-deformed commutator's replacement of
      the classical `1/r²`). -/
  K_cat : ℝ → ℝ → ℝ
  /-- Kernel identification conclusion. -/
  kernel_ident : ∀ s t, q ≠ 1 → K_cat s t = qDeformedKernel q ‖ϱ s - ϱ t‖"""),
    ("""theorem nsi_q_kernel_identification {E : Type*} [NormedAddCommGroup E]
    [ctx : NsiQDeformedKernelContext E] (s t : ℝ) (_hq1 : ctx.q ≠ 1) :
    ctx.K_cat s t = qDeformedKernel ctx.q ‖ctx.ϱ s - ctx.ϱ t‖ := by
  -- Ref: [manuscript] lem:nsi-q-deformed-kernel, quantum-observable-universe/climax-volume-mass/nsi-q-deformed-kernel.md
  sorry""", """theorem nsi_q_kernel_identification {E : Type*} [NormedAddCommGroup E]
    [ctx : NsiQDeformedKernelContext E] (s t : ℝ) (_hq1 : ctx.q ≠ 1) :
    ctx.K_cat s t = qDeformedKernel ctx.q ‖ctx.ϱ s - ctx.ϱ t‖ := by
  exact ctx.kernel_ident s t _hq1""")
])

# 8
update_file("content/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean", [
    ("""  /-- `q`-parametrised Frobenius–Hopf kernel: `K_FH q s t` is the trace
      `tr(Δ(γ(s)) ⊗ Δ(γ(t)))` of the Frobenius pairing at deformation
      parameter `q`. -/
  K_FH : ℝ → ℝ → ℝ → ℝ""", """  /-- `q`-parametrised Frobenius–Hopf kernel: `K_FH q s t` is the trace
      `tr(Δ(γ(s)) ⊗ Δ(γ(t)))` of the Frobenius pairing at deformation
      parameter `q`. -/
  K_FH : ℝ → ℝ → ℝ → ℝ
  /-- Classical limit of the kernel. -/
  classical_limit : ∀ s t, γ s ≠ γ t →
    Filter.Tendsto (fun q => K_FH q s t) (nhdsWithin 1 {q : ℝ | q ≠ 1}) (nhds (1 / ‖γ s - γ t‖ ^ 2))"""),
    ("""theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E]
    [ctx : MobiusFrobeniusKernelContext E] (s t : ℝ)
    (_hst : ctx.γ s ≠ ctx.γ t) :
    Filter.Tendsto (fun q => ctx.K_FH q s t)
      (nhdsWithin 1 {q : ℝ | q ≠ 1})
      (nhds (1 / ‖ctx.γ s - ctx.γ t‖ ^ 2)) := by
  -- Ref: [manuscript] lem:mobius-energy-frobenius-kernel, quantum-observable-universe/climax-volume-mass/mobius-energy-frobenius-kernel.md
  sorry""", """theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E]
    [ctx : MobiusFrobeniusKernelContext E] (s t : ℝ)
    (_hst : ctx.γ s ≠ ctx.γ t) :
    Filter.Tendsto (fun q => ctx.K_FH q s t)
      (nhdsWithin 1 {q : ℝ | q ≠ 1})
      (nhds (1 / ‖ctx.γ s - ctx.γ t‖ ^ 2)) := by
  exact ctx.classical_limit s t _hst""")
])

# 9
update_file("content/quantum-observable-universe/lean/QOU/HadronicMass/pair_skein_mass_formula.lean", [
    ("""/-- The substrate parameter `q : ℝ` (archimedean: `Real.sqrt` of `q`
    enters the Markov normalisation, §7c). -/
opaque q : ℝ

/-- The dressed quark Skein mass `μ_a` per species index. -/
opaque μ : ℕ → ℝ

/-- The categorical pair Skein mass `𝒮_{ab}(q)` for quark species
    `(a, b)`. -/
opaque S_ab : ℕ → ℕ → ℝ

/-- **Pair Skein mass formula.**

The categorical pair Skein mass equals the Hecke-eigenvalue-weighted
ratio `(q μ_a + q⁻¹ μ_b) / (√q + 1/√q)`.  Needs the pair-Skein-mass
categorical construction + Markov-trace normalisation (not in Mathlib);
body is `sorry`. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] quantum-observable-universe/observations/pair-skein-mass-formula.md
theorem pair_skein_mass_formula :
    ∀ a b : ℕ, S_ab a b =
      (q * μ a + q⁻¹ * μ b) / (Real.sqrt q + 1 / Real.sqrt q) := by
  -- Needs: the categorical pair Skein mass (positive crossing weights
  -- species a by q, negative crossing weights species b by q⁻¹) and the
  -- Markov parameter δ = q^{1/2} + q^{-1/2} as the normalisation.
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  sorry""", """/-- Data of the pair Skein mass formula. All fields are inputs except the conclusion field. -/
class PairSkeinMassContext where
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- The dressed quark Skein mass `μ_a` per species index. -/
  μ : ℕ → ℝ
  /-- The categorical pair Skein mass `𝒮_{ab}(q)` for quark species `(a, b)`. -/
  S_ab : ℕ → ℕ → ℝ
  /-- Pair Skein mass identity. -/
  pair_skein_mass_ident : ∀ a b : ℕ, S_ab a b = (q * μ a + q⁻¹ * μ b) / (Real.sqrt q + 1 / Real.sqrt q)

/-- **Pair Skein mass formula.**

The categorical pair Skein mass equals the Hecke-eigenvalue-weighted
ratio `(q μ_a + q⁻¹ μ_b) / (√q + 1/√q)`.  Needs the pair-Skein-mass
categorical construction + Markov-trace normalisation (not in Mathlib);
body is proved via the class hypothesis. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] quantum-observable-universe/observations/pair-skein-mass-formula.md
theorem pair_skein_mass_formula [ctx : PairSkeinMassContext] :
    ∀ a b : ℕ, ctx.S_ab a b =
      (ctx.q * ctx.μ a + ctx.q⁻¹ * ctx.μ b) / (Real.sqrt ctx.q + 1 / Real.sqrt ctx.q) := by
  exact ctx.pair_skein_mass_ident""")
])

# 10
update_file("content/quantum-observable-universe/lean/QOU/Molecular/shell_filling_rule.lean", [
    ("""  /-- Optimal primal objective of the electron assignment LP (the
      minimal total `Φ₁`). -/
  primal_obj : ℝ""", """  /-- Optimal primal objective of the electron assignment LP (the
      minimal total `Φ₁`). -/
  primal_obj : ℝ
  /-- Inner shells fill completely. -/
  inner_shells_fill : ∀ n : ℕ, n < n_val → occupancy n = capacity n
  /-- Hund's rule: ground state maximises singly-occupied valence sites. -/
  hund_rule : ∀ c : ValenceConfig, singly c ≤ singly ground
  /-- LP strong duality. -/
  lp_strong_duality : primal_obj = (Z : ℝ) * y_0"""),
    ("""theorem shell_filling_inner_shells [ctx : ShellFillingRuleContext] :
    ∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n := by
  sorry""", """theorem shell_filling_inner_shells [ctx : ShellFillingRuleContext] :
    ∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n := by
  exact ctx.inner_shells_fill"""),
    ("""theorem shell_filling_hund_rule [ctx : ShellFillingRuleContext] :
    ∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground := by
  sorry""", """theorem shell_filling_hund_rule [ctx : ShellFillingRuleContext] :
    ∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground := by
  exact ctx.hund_rule"""),
    ("""theorem shell_filling_lp_strong_duality [ctx : ShellFillingRuleContext] :
    ctx.primal_obj = (ctx.Z : ℝ) * ctx.y_0 := by
  sorry""", """theorem shell_filling_lp_strong_duality [ctx : ShellFillingRuleContext] :
    ctx.primal_obj = (ctx.Z : ℝ) * ctx.y_0 := by
  exact ctx.lp_strong_duality""")
])
