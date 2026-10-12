---
# qou-v1np
title: "Corpus math errors: H²(Σ,\U0001D4AA^×)=0 kills perpetual obstruction; H²(ℂP¹,\U0001D4AA^×)≠ℤ; Bring real dim is 2"
status: todo
type: bug
priority: high
created_at: 2026-10-12T19:22:58Z
updated_at: 2026-10-12T19:22:58Z
parent: qou-vo9t
---

Three corpus math errors found 2026-10-12 (session qou-vo9t, bean qou-lx8f). Each is standard mathematics, not a fit question, but they are content edits, so they wait on the owner.

1. **𝒪^× band kills the obstruction (scope b).** H²(Σ, 𝒪^×) = 0 for a compact Riemann surface, by the exponential sequence. Blocks using the 𝒪_M^× band therefore have κ_n identically 0 on Bring, contradicting "perpetual obstruction". Affected: lifting-and-descent/yekutieli-lifting.md, yekutieli-archimedean-band.md, archimedean-lifting-intro.md, yekutieli-mapping-table.md, descent-cocycle-deviation.md, plus the `persistence` fields.
2. **yekutieli-lifting-su2.md:16-18.** H²(ℂP¹, 𝒪^×) ≅ H²(ℂP¹, ℤ) ≅ ℤ is false; H²(ℂP¹, 𝒪^×) = 0, and the ℤ is Pic = H¹(𝒪^×). The same block calls SU(2) → ℂP¹ an SU(2)-principal bundle; it is a U(1)-bundle.
3. **fluid-dynamics/ns-obstruction-computation.md:30.** "Bring's surface possesses real dimension 4", with D⁴/S³ excision. Σ₄ has real dimension 2.
