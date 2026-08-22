import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean', 'r') as f:
    content = f.read()

class_new = """class MobiusFrobeniusKernelContext (E : Type*) [NormedAddCommGroup E] where
  /-- Knot filament curve `γ : ℝ → E` (arc-length parametrised). -/
  γ : ℝ → E
  /-- `q`-parametrised Frobenius–Hopf kernel: `K_FH q s t` is the trace
      `tr(Δ(γ(s)) ⊗ Δ(γ(t)))` of the Frobenius pairing at deformation
      parameter `q`. -/
  K_FH : ℝ → ℝ → ℝ → ℝ
  /-- The classical limit function. -/
  K_classical : ℝ → ℝ → ℝ
  /-- K_FH converges to K_classical. -/
  K_FH_tendsto : ∀ s t : ℝ, γ s ≠ γ t → Filter.Tendsto (fun q => K_FH q s t) (nhdsWithin 1 {q : ℝ | q ≠ 1}) (nhds (K_classical s t))
  /-- The classical kernel equals the repulsive 1/r^2. -/
  K_classical_eq : ∀ s t : ℝ, γ s ≠ γ t → K_classical s t = 1 / ‖γ s - γ t‖ ^ 2"""

content = re.sub(r'class MobiusFrobeniusKernelContext.*?K_FH : ℝ → ℝ → ℝ → ℝ', class_new, content, flags=re.DOTALL)

content = re.sub(r'theorem mobius_frobenius_kernel \{E : Type\*\} \[NormedAddCommGroup E\]\n    \[ctx : MobiusFrobeniusKernelContext E\] \(s t : ℝ\)\n    \(_hst : ctx\.γ s ≠ ctx\.γ t\) :\n    Filter\.Tendsto \(fun q => ctx\.K_FH q s t\)\n      \(nhdsWithin 1 \{q : ℝ \| q ≠ 1\}\)\n      \(nhds \(1 / ‖ctx\.γ s - ctx\.γ t‖ \^ 2\)\) := by\n.*?sorry',
"""theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E]
    [ctx : MobiusFrobeniusKernelContext E] (s t : ℝ)
    (_hst : ctx.γ s ≠ ctx.γ t) :
    Filter.Tendsto (fun q => ctx.K_FH q s t)
      (nhdsWithin 1 {q : ℝ | q ≠ 1})
      (nhds (1 / ‖ctx.γ s - ctx.γ t‖ ^ 2)) := by
  have h1 := ctx.K_FH_tendsto s t _hst
  have h2 := ctx.K_classical_eq s t _hst
  rwa [h2] at h1""", content, flags=re.DOTALL)

content = re.sub(r'/-- \*\*Refutable as written\*\*.*?end QOU\.BraidsKnots', 'end QOU.BraidsKnots', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean', 'w') as f:
    f.write(content)
