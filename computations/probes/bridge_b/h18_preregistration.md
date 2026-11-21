# H18 pre-registration: a model in which the wall weight is forced (2026-11-21, before any computation)

Why. In H17 the two-strand model takes any wall parameter s, because 𝒦Ř𝒦Ř = Ř𝒦Ř𝒦 holds for every s. The weight-3 wall was put in by hand there, so that model cannot test it. Here the folded generators are not given their own matrices. Each one is the ambient operator itself, so its weight is forced by the ambient algebra.

Model. Take the ambient H̃ = H(S_n) at parameter v, acting on V = (C²)^{⊗n} by the Jimbo Ř (eigenvalues v and −v⁻¹) on strands i, i+1. The involution ι : s_i ↔ s_{n−i} is realised on V by J = F·P, where P reverses the tensor factors and F = σ_x^{⊗n} flips each spin. Check first: J² = 1 and J ρ(T̃_i) J = ρ(T̃_{n−i}) for all i. If this fails, stop and report.

For each ι-orbit I, take its longest element w_I with ambient reduced word, and set A_I = ρ(T̃_{w_I}). A_I commutes with J. The twisted power sums p_k = tr(J A_I^k), for k = 0..10, are the power sums of the virtual eigenvalue multiset "eigenvalues on V⁺ minus eigenvalues on V⁻", where V^± are the J = ±1 eigenspaces. This is the K♯ / twisted-trace view of Lusztig §16.

Criterion (pass/fail), at exact rational v = 2. For each orbit and each n = 4, 5, 6, 7:
1. The p_k obey p_{k+2} = (a + b) p_{k+1} − ab p_k for k = 0..8 for exactly one pair (a, b) with |a| = v^L and |b| = v^{−L} drawn from the candidates (v^L, −v^{−L}) and (v^L, v^{−L}), and only when L equals the orbit's ambient length (1 for a fixed root, 2 for a swapped pair, 3 for the adjacent middle pair at odd n). Every wrong L must fail. The weight is then forced, by the modulus of the virtual eigenvalues.
2. Report which sign holds. Lusztig 16.7(b) is (b − v^L)(b + v^{−L}) = 0, i.e. the pair (v^L, −v^{−L}). If instead the pair (v^L, +v^{−L}) holds, that is a sign normalisation (Lusztig's normalised φ_x, §16.4) and is reported as such, not as a failure of the weight.
3. Report p_0 = tr J (the virtual dimension) for each n.

What would count against the weight-3 wall: at n = 5 or 7, the middle orbit's twisted power sums fail the recurrence for L = 3, or pass it for some other L.

Nothing here is a mass or is compared with experiment.
