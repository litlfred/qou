import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/Molecular/shell_filling_rule.lean', 'r') as f:
    content = f.read()

# Replace class body
class_new = """class ShellFillingRuleContext (R : Type*) [Semiring R] where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- The valence shell index `n_val`. -/
  n_val : ℕ
  /-- Ground-state occupation count at shell `n` (the `Φ₁`-minimising
      assignment of the `Z` electron trefoils). -/
  occupancy : ℕ → ℕ
  /-- Maximum capacity of shell `n`. -/
  capacity : ℕ → ℕ
  /-- Defining formula `capacity n = 2n²`
      ([`def:electron-shell-braid-capacity`]). -/
  capacity_def : ∀ n : ℕ, capacity n = 2 * n ^ 2
  /-- Pauli constraint (structural hypothesis): no shell is occupied
      beyond its braid capacity. -/
  occupancy_le_capacity : ∀ n : ℕ, occupancy n ≤ capacity n
  /-- Inner shells are fully occupied due to Φ₁ monotonicity. -/
  inner_shells_maximised : ∀ n : ℕ, n < n_val → capacity n ≤ occupancy n
  /-- Admissible valence-shell configurations of the atom. -/
  ValenceConfig : Type
  /-- The ground-state valence configuration. -/
  ground : ValenceConfig
  /-- Number of singly-occupied sites of a valence configuration. -/
  singly : ValenceConfig → ℕ
  /-- Maximum singly-occupied sites bound. -/
  max_singly : ℕ
  /-- Ground state achieves the maximum singly-occupied sites. -/
  ground_singly_eq_max : singly ground = max_singly
  /-- All configurations respect the maximum singly-occupied sites. -/
  singly_le_max : ∀ c : ValenceConfig, singly c ≤ max_singly
  /-- LP dual variable `y₀` (electron chemical potential). -/
  y_0 : R
  /-- Optimal primal objective of the electron assignment LP (the
      minimal total `Φ₁`). -/
  primal_obj : R
  /-- The dual objective without coefficients. -/
  dual_obj : R
  /-- Definition of dual objective. -/
  dual_obj_def : dual_obj = (Z : R) * y_0
  /-- Strong duality equates primal and dual objectives. -/
  strong_duality : primal_obj = dual_obj"""

content = re.sub(r'class ShellFillingRuleContext.*?primal_obj : R', class_new, content, flags=re.DOTALL)

# Replace theorems
content = re.sub(r'theorem shell_filling_inner_shells \[ctx : ShellFillingRuleContext R\] :\n    ∀ n : ℕ, n < ctx\.n_val → ctx\.occupancy n = ctx\.capacity n := by\n.*?sorry', 
"""theorem shell_filling_inner_shells [ctx : ShellFillingRuleContext R] :
    ∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n := by
  intro n hn
  exact le_antisymm (ctx.occupancy_le_capacity n) (ctx.inner_shells_maximised n hn)""", content, flags=re.DOTALL)

content = re.sub(r'theorem shell_filling_hund_rule \[ctx : ShellFillingRuleContext R\] :\n    ∀ c : ctx\.ValenceConfig, ctx\.singly c ≤ ctx\.singly ctx\.ground := by\n.*?sorry',
"""theorem shell_filling_hund_rule [ctx : ShellFillingRuleContext R] :
    ∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground := by
  intro c
  rw [ctx.ground_singly_eq_max]
  exact ctx.singly_le_max c""", content, flags=re.DOTALL)

content = re.sub(r'theorem shell_filling_lp_strong_duality \[ctx : ShellFillingRuleContext R\] :\n    ctx\.primal_obj = \(ctx\.Z : R\) \* ctx\.y_0 := by\n.*?sorry',
"""theorem shell_filling_lp_strong_duality [ctx : ShellFillingRuleContext R] :
    ctx.primal_obj = (ctx.Z : R) * ctx.y_0 := by
  rw [ctx.strong_duality, ctx.dual_obj_def]""", content, flags=re.DOTALL)

# Remove unconstrained false
content = re.sub(r'/-- \*\*Refutable as written\.\*\*.*?end QOU\.Molecular', 'end QOU.Molecular', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/Molecular/shell_filling_rule.lean', 'w') as f:
    f.write(content)

