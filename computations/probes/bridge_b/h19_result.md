# H19 result: the weight-3 wall is forced on the three-state module (2026-11-21)

Pre-registration: `h19_preregistration.md` (written before the run). Probe: `h19_three_state_probe.py`. Output: `h19_three_state_probe.out.txt`. Exact arithmetic over ℚ at v = 2; no floats.

## Substitution, stated again

The owner chose "spin-1 module". The spin-1 R-matrix of U_q(sl₂) has three eigenvalues and is not a Hecke representation, so the probe uses the three-state Hecke module (C³)^{⊗n} with the gl₃ Jimbo Ř, as the pre-registration says. This is a gl₃ module, not the spin-1 sl₂ module.

## Set-up checks (all pass)

- J² = 1 and J ρ(T̃_i) J = ρ(T̃_{n−i}) for all i, at n = 4, 5, 6, 7, for both N = 2 and N = 3.
- Control: the N = 2 run reproduces H18's p_0..p_3 exactly at n = 4 (4, 49/4, 769/16, 12289/64 and 4, 3, 17/2, 63/4) and n = 6.

## Result: pass

At every n and every orbit, the recurrence p_{k+2} = (a+b)p_{k+1} − ab p_k (k = 0..8) holds for exactly one candidate (L, sign), and L is the orbit's ambient length.

| orbit type | L forced | sign of b | example p_0..p_3 |
|---|---|---|---|
| fixed root (even n) | 1 | −v⁻¹ | n=4: 9, 21/2, 99/4, 381/8 |
| swapped pair s_i, s_{n−i} | 2 | +v⁻² | n=4: 9, 99/4, 1539/16, 24579/64 |
| middle orbit s_m s_{m+1} s_m (odd n) | **3** | **−v⁻³** | n=5: 9, 381/8, 24579/64, 1572861/512 |
| | | | n=7: 27, 1143/8, 73737/64, 4718583/512 |

So the key case of the pre-registration passes: at n = 5 and n = 7 the middle-orbit power sums are non-zero, and only L = 3 satisfies the recurrence. The weight-3 wall that the wording fix to conj:type-b-folding-cpt added is forced by the ambient operator, and it carries Lusztig's sign −v⁻³.

## What is still open

- The swapped pairs carry +v⁻² here, against Lusztig's −v⁻² (§16.4). H18 found the same. The fixed root and the weight-3 wall both carry Lusztig's sign, so the difference is confined to the pairs. It is a normalisation question about how J acts on the pair, and is not settled here.
- This is a necessary-condition check on one family of modules (gl_N vector modules, N = 2, 3). It is not a proof of the folding conjecture, and the trace-to-MeV map is untouched.

Nothing here is a mass or is compared with experiment.
