---
# qou-rh4b
title: 'GAP: q-Habiro completion projection for prop:residue-at-root'
status: todo
type: task
priority: normal
created_at: 2026-11-20T20:05:00Z
updated_at: 2026-11-20T20:05:00Z
parent: qou-tm3c
---

`prop:residue-at-root` lists `conj:gs-residue-at-root-existence`, and what it actually uses from it is the existence of the cyclotomic projection π_n on the Habiro completion (residue-at-root.md:22). Its Lean is a self-assuming projection (`residue-at-root.lean:27-30`), and the class allows an arbitrary target ring, not ℤ[q]/Φ_n.

Only the z-variable completion exists (`ZHabiroCompletion`, `lean/QOU/MassEndomorphism/ZHabiroCauchy.lean:522`). Sketch of a proof of the projection:

1. Define Ẑ[q] as the thread subring of lim ℤ[q]/((q;q)_N).
2. Project to level n.
3. Factor through Φ_n ∣ Xⁿ−1 ∣ (q;q)_n, using `Polynomial.cyclotomic.dvd_X_pow_sub_one` and `Ideal.Quotient.factor`.

Caveat: neither block shows that Φ_q·tr_{M,ℓ} lies in Ẑ[q], so proving the projection does not by itself discharge the block.

Found in the qou-tm3c residual analysis (#8526, comment 7048682948).
