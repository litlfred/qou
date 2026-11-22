# H20 pre-registration: why the swapped pairs carry +v⁻² (2026-11-21, before any computation)

Why. In H18 and H19 the twisted power sums of each swapped-pair orbit {s_i, s_{n−i}} satisfy the recurrence with roots (v², +v⁻²). Lusztig's folded generator of weight 2 has roots (v², −v⁻²). The fixed root and the weight-3 wall carry Lusztig's sign. This probe tests one explanation for the pair sign.

Claim (a short argument, to be checked by computation). Let T_i, T_j commute, each satisfy (T − v)(T + v⁻¹) = 0, and be diagonalisable, and let J be an involution with J T_i J = T_j. Split V into joint eigenspaces E_{ab} (a, b ∈ {v, −v⁻¹}). J maps E_{ab} to E_{ba}, so for a ≠ b it contributes nothing to tr(J X) for any X preserving the E's. Hence

  p_k = tr(J (T_i T_j)^k) = c₊ v^{2k} + c₋ v^{−2k},  c₊ = tr(J|E_{v,v}),  c₋ = tr(J|E_{−v⁻¹,−v⁻¹}).

The mixed eigenvalue −1 of T_i T_j never appears, and the second root is (−v⁻¹)² = +v⁻². If the claim holds, +v⁻² is forced for every module of this kind, and Lusztig's −v⁻² cannot come from a J-twisted trace of the ambient pair product.

Test (pass/fail), exact over ℚ at v = 2, on the H19 modules (C^N)^{⊗n}, N = 2, 3, n = 4..7, for every swapped-pair orbit:
1. compute the projectors P_±(T) = (T − b)/(a − b) and c₊ = tr(J P_+(T_i) P_+(T_j)), c₋ = tr(J P_−(T_i) P_−(T_j)), c_mix = tr(J P_+(T_i) P_−(T_j)) + tr(J P_−(T_i) P_+(T_j));
2. **pass** if c_mix = 0 and p_k = c₊ v^{2k} + c₋ v^{−2k} for k = 0..10 at every orbit;
3. **fail** otherwise.

The p_k are recomputed exactly as in H19. Nothing here is a mass or is compared with experiment.
