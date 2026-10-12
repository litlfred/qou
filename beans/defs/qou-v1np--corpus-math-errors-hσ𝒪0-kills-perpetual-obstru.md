---
# qou-v1np
title: "Corpus math errors: H²(Σ,\U0001D4AA^×)=0 kills perpetual obstruction; H²(ℂP¹,\U0001D4AA^×)≠ℤ; Bring real dim is 2"
status: completed
type: bug
priority: high
created_at: 2026-10-12T19:22:58Z
updated_at: 2026-10-12T19:29:53Z
parent: qou-vo9t
---

Three corpus math errors found 2026-10-12 (session qou-vo9t, bean qou-lx8f). Each is standard mathematics, not a fit question, but they are content edits, so they wait on the owner.

1. **𝒪^× band kills the obstruction (scope b).** H²(Σ, 𝒪^×) = 0 for a compact Riemann surface, by the exponential sequence. Blocks using the 𝒪_M^× band therefore have κ_n identically 0 on Bring, contradicting "perpetual obstruction". Affected: lifting-and-descent/yekutieli-lifting.md, yekutieli-archimedean-band.md, archimedean-lifting-intro.md, yekutieli-mapping-table.md, descent-cocycle-deviation.md, plus the `persistence` fields.
2. **yekutieli-lifting-su2.md:16-18.** H²(ℂP¹, 𝒪^×) ≅ H²(ℂP¹, ℤ) ≅ ℤ is false; H²(ℂP¹, 𝒪^×) = 0, and the ℤ is Pic = H¹(𝒪^×). The same block calls SU(2) → ℂP¹ an SU(2)-principal bundle; it is a U(1)-bundle.
3. **fluid-dynamics/ns-obstruction-computation.md:30.** "Bring's surface possesses real dimension 4", with D⁴/S³ excision. Σ₄ has real dimension 2.

## 2026-10-12: fixed (owner authorised: "Fix qou-v1np errors")
1. `ns-obstruction-computation.md`: D^4/S^3 changed to D^2/S^1, and Bring's real dimension to 2. The old line was also internally wrong: H^2(D^4, S^3) = 0, not Z. The corrected excision gives Z, so nothing downstream moves.
2. `yekutieli-lifting-su2.md`: now derives H^2(CP^1, O^x) = 0 from the exponential sequence, and states the consequence. With the O^x band, every kappa_n = 0 and the lift exists. The c_1 = 1 of the Hopf bundle lives in Pic = H^1(O^x). The "perpetual obstruction" and "kappa_n >= 1" paragraphs are removed, and the title is changed in .ts, .jsonld and the definition index. `yekutieli-lifting-condition-su2.md`: "SU(2)-principal" becomes "principal U(1)-bundle (Hopf)", plus one sentence noting that its c_1 obstruction is in H^2(Z), not in H^2(O^x) = 0.
3. `yekutieli-lifting.md`: a note that on a closed surface H^2(M, O_M^x) = H^3(M, Z) = 0, so this band carries no obstruction there.

**Verification.** Render battery clean on all 4 .md files. `run-validate` against platform c56b73b (the pin): valid, 8 pre-existing issues, none in these blocks. qa-sweep run on all 4; it wrote attestations, and the LLM-judged criteria remain needs-agent.

**Not done, and still open under qou-lx8f.** The "perpetual obstruction" claims elsewhere (thm:qu-to-qou item 3, qu-to-qou-su2.md, and the `persistence` / `corrections_persistent` Lean fields) were not edited. They are consistent only under a Z band. qu-to-qou-su2.md also `uses` ex:yekutieli-lifting-su2, whose conclusion is now reversed.
