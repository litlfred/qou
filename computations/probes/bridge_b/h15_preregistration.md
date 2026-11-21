# H15 pre-registration: the Hecke-level folding across strand numbers (2026-11-21, before any computation)

Owner, 2026-11-21: "Work folding conjectures." `conj:type-b-folding-cpt` says the 𝔰𝔩ₙ datum of H_n(q) folds under ι: αᵢ ↔ α_{n−i} into type B_{n/2}. Its Lean carrier encodes the crystal-level fold. The Hecke-level fold (Lusztig §16.2, quasisplit case) is not in the carrier. H14 checked it at n = 6 only.

Claims to test, for n = 3, 4, 5, 6, 7 strands (S_n, ι = conjugation by w₀):
A. Shape of the fold, from §16.2 (one generator w₀^I per ι-orbit I of simple reflections, L = ambient length):
   - n even: n/2 − 1 commuting pairs (L = 2) and one fixed middle reflection (L = 1); type B_{n/2}.
   - n odd: (n−3)/2 commuting pairs (L = 2) and one adjacent middle pair, whose w₀ is s_m s_{m+1} s_m (L = 3); type B_{(n−1)/2} for n ≥ 5, and A₁ for n = 3.
   So the carrier's "B_{n/2}" is right for even n and must read B_{(n−1)/2} with a weight-3 wall for odd n.
   Pass: the fixed group has the predicted order (2^m · m! for type B_m, 2 for n = 3), and the orbit generators generate it.
B. §16.6 consequence, as in H14: for all y ≤ x in W, folded KL coefficients ≡ ambient mod 2 and no larger in absolute value.
C. Control: equal weights (all L = 1) fail B for every n where W has a weight ≠ 1, i.e. every n ≥ 3 except none (n = 4: L = (1, 2); n = 3: L = 3).

A pass is a numerical check of a literature theorem on these cases, not a proof. It says nothing about the physical identification in the conjecture (matter = fixed points, CPT factorisation), which stays conjectural.
