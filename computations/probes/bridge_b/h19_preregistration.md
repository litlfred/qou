# H19 pre-registration: the weight-3 wall on a three-state module (2026-11-21, before any computation)

Why. In H18 the module (C²)^{⊗n} has zero twisted character at odd n, so it could not see the weight-3 wall. That wall is the case the wording fix to conj:type-b-folding-cpt added.

Module, and one substitution. The owner chose "spin-1 module". The spin-1 R-matrix of U_q(sl₂) on V₁⊗V₁ has three eigenvalues, so it does not satisfy the Hecke quadratic and is not a representation of H_n(q). The three-state module that is a Hecke representation is the gl₃ vector module V = (C³)^{⊗n}, with the Jimbo Ř in Hecke normalisation (eigenvalues v and −v⁻¹):
- Ř(e_i⊗e_i) = v e_i⊗e_i;
- for i < j, Ř(e_i⊗e_j) = e_j⊗e_i and Ř(e_j⊗e_i) = e_i⊗e_j + (v − v⁻¹) e_j⊗e_i.

This is the same rule as H18's C² matrix. Here J = F·P, where P reverses the tensor factors and F is the basis flip e_i ↦ e_{2−i}. At odd n, weights with equal numbers of e₀ and e₂ exist, so J fixes some weight spaces and the twisted character need not vanish.

Set-up checks, which stop the run if they fail: J² = 1, and J ρ(T̃_i) J = ρ(T̃_{n−i}) for all i. Also: the same code with C² must reproduce H18's p_0..p_3 at n = 4 and n = 6.

Test (pass/fail), the same as H18, exact over ℚ at v = 2, at n = 4, 5, 6, 7. For each ι-orbit generator A_I, compute p_k = tr(J A_I^k) for k = 0..10. The weight is forced to L if p_{k+2} = (a+b) p_{k+1} − ab p_k holds for k = 0..8 for some (a, b) ∈ {(v^L, −v^{−L}), (v^L, +v^{−L})}, and only at the orbit's ambient length L.

The key case is the middle orbit {s_m, s_{m+1}} at odd n, with ambient length 3.
- **Pass:** the p_k are not all zero, and only L = 3 satisfies the recurrence.
- **Fail:** some other L also satisfies it, or L = 3 does not.
- **Degenerate again:** all p_k = 0. That would be reported as inconclusive.

The sign (−v^{−L} or +v^{−L}) is reported, not judged; H18 left it open as a normalisation question.

Nothing here is a mass or is compared with experiment.
