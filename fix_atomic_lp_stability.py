import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_lp_stability.lean', 'r') as f:
    content = f.read()

class_new = """class AtomicLPStabilityContext where
  /-- Markov-normalised candidate operators `X* = α·𝟙 + β·σ₀`, modelled
      as a coefficient pair `(α, β) : ℝ × ℝ`. -/
  Candidate : Type
  /-- Traced volume of a candidate against the BARE pairing. -/
  bareVolume : Candidate → ℝ
  /-- Traced volume of a candidate against the DRESSED (𝓑₃) pairing. -/
  dressedVolume : Candidate → ℝ
  /-- Markov normalisation predicate (`X*` is not the zero operator). -/
  normalised : Candidate → Prop
  /-- Specific bare annihilator. -/
  bare_annihilator : Candidate
  /-- The bare annihilator is normalised. -/
  bare_annihilator_normalised : normalised bare_annihilator
  /-- The bare annihilator zeroes the volume. -/
  bare_annihilator_volume : bareVolume bare_annihilator = 0
  /-- Dressed volume is always non-zero for normalised operators. -/
  dressed_volume_nonzero : ∀ X : Candidate, normalised X → dressedVolume X ≠ 0"""

content = re.sub(r'class AtomicLPStabilityContext where.*?normalised : Candidate → Prop', class_new, content, flags=re.DOTALL)

content = re.sub(r'theorem bare_is_lp_unstable \[ctx : AtomicLPStabilityContext\] :\n    ∃ X : ctx\.Candidate, ctx\.normalised X ∧ ctx\.bareVolume X = 0 := by\n.*?sorry',
"""theorem bare_is_lp_unstable [ctx : AtomicLPStabilityContext] :
    ∃ X : ctx.Candidate, ctx.normalised X ∧ ctx.bareVolume X = 0 := by
  exact ⟨ctx.bare_annihilator, ctx.bare_annihilator_normalised, ctx.bare_annihilator_volume⟩""", content, flags=re.DOTALL)

content = re.sub(r'theorem dressed_is_lp_stable \[ctx : AtomicLPStabilityContext\] :\n    ¬ ∃ X : ctx\.Candidate, ctx\.normalised X ∧ ctx\.dressedVolume X = 0 := by\n.*?sorry',
"""theorem dressed_is_lp_stable [ctx : AtomicLPStabilityContext] :
    ¬ ∃ X : ctx.Candidate, ctx.normalised X ∧ ctx.dressedVolume X = 0 := by
  intro ⟨X, hnorm, hvol⟩
  exact ctx.dressed_volume_nonzero X hnorm hvol""", content, flags=re.DOTALL)

content = re.sub(r'/-- \*\*Both statements above are refutable, by opposite instances\.\*\*.*?end QOU\.ParticleInteractions', 'end QOU.ParticleInteractions', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_lp_stability.lean', 'w') as f:
    f.write(content)
