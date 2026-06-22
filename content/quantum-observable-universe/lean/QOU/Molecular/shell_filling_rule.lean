/-!
# QOU.Molecular.shell_filling_rule

**Placeholder canonical** for content block
[`prop:shell-filling-rule`](../../../quantum-observable-universe/molecular-construction/shell-filling-rule.md): *Shell filling minimises $\\Phi_1$ (aufbau from LP dual)*.

The full Lean statement and proof are pending; this stub exists so
the `lean.ref` URI `qou:QOU.Molecular.shell_filling_rule` resolves to a real declaration in
the `qou` Lake package.  The body is `sorry` carrying the
manuscript citation per AGENTS.md §1.
-/

namespace QOU.Molecular


/-- Abstract context for the `shell_filling_rule` claim — manuscript-named
    typed fields below; the `holds` field carries the `Prop`-valued
    claim of the lemma. -/
class ShellFillingRuleContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- The valence shell index `n_val`. -/
  n_val : ℕ
  /-- The occupation count at shell `n` after aufbau. -/
  occupancy : ℕ → ℕ
  /-- Maximum capacity of shell `n` (2n²). -/
  capacity : ℕ → ℕ
  /-- Number of singly-occupied sites in the valence shell. -/
  singly_occupied : ℕ
  /-- LP dual variable `y_0` (electron chemical potential). -/
  y_0 : ℝ
  /-- LP primal objective for the electron assignment problem
      `Z · y_0`. -/
  primal_obj : ℝ
  /-- Proposition: the ground-state electron configuration satisfies the aufbau principle. -/
  aufbau_holds : Prop
  /-- Hypothesis that aufbau is active. -/
  aufbau_active : aufbau_holds
  /-- (i) Inner shells `n < n_val` fill completely: `occupancy n = capacity n` for all `n < n_val`. -/
  impl_inner_shells_fill : aufbau_holds → ∀ n : ℕ, n < n_val → occupancy n = capacity n
  /-- (ii) Hund's rule: the valence-shell configuration maximises singly-occupied sites. -/
  impl_hunds_rule_max : aufbau_holds → ∀ other : ℕ, other ≤ singly_occupied
  /-- (iii) LP dual objective equals `Z · y_0`. -/
  impl_lp_dual_objective : aufbau_holds → primal_obj = (Z : ℝ) * y_0

/-- **Proposition statement** (from manuscript):

The ground-state electron configuration of atom $(Z, N)$ is the
assignment of $Z$ electron trefoils to bonding sites that
minimises the total $\Phi_1$ of the atomic braid.  This
reproduces the aufbau principle:*

1. *Inner shells ($n < n_{\mathrm{val}}$) fill completely because
   each additional electron in a partly filled inner shell reduces
   $\Phi_1$ more than any valence electron.*

2. *Within the valence shell, electrons distribute to maximise the
   number of singly occupied sites (Hund's rule) because parallel
   electron trefoils have lower $\Phi_1$ than antiparallel pairs
   — the $ee$ crossing ($\sigma$, repulsive) is minimised when
   electrons occupy distinct spatial sites.*

3. *The LP dual of the electron assignment problem is:*

$$
  \max_{y} \; Z \cdot y_0
  \quad\text{s.t.}\quad
  y_0 + \sum_{n} G_{n,s} \, y_{n,s} \leq \Phi_1^{(s)}
  \;\;\forall\, \text{sites } s
$$

*where $\Phi_1^{(s)}$ is the $\Phi_1$ contribution of placing
an electron at site $s$, and $G_{n,s}$ encodes the Gram-matrix
penalty for electron-electron repulsion at shell $n$.*

*The dual variable $y_0$ gives the

    The Lean encoding below is a `theorem … : ctx.holds := by sorry` placeholder (the actual claim type sits on the context class);
    upgrading requires choosing the appropriate Lean types (Polynomial /
    Matrix / categorical structures / etc.) and translating the manuscript
    claim above. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.ts
theorem shell_filling_rule [ctx : ShellFillingRuleContext] :
    (∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n) ∧
    (∀ other : ℕ, other ≤ ctx.singly_occupied) ∧
    ctx.primal_obj = (ctx.Z : ℝ) * ctx.y_0 :=
  sorry

end QOU.Molecular
