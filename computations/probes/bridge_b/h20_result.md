# H20 result: the swapped pairs carry +v⁻² because the twisted trace sees only the squares (2026-11-21)

Pre-registration: `h20_preregistration.md` (committed in bec5a02 before the run). Probe: `h20_pair_sign_probe.py`. Output: `h20_pair_sign_probe.out.txt`. Exact arithmetic over ℚ at v = 2.

## Result: pass

On every swapped-pair orbit (i, n−i) of the modules (C^N)^{⊗n}, N = 2, 3, n = 4..7:
- the mixed term c_mix = tr(J P₊(T_i) P₋(T_j)) + tr(J P₋(T_i) P₊(T_j)) is 0;
- p_k = tr(J (T_i T_{n−i})^k) = c₊ v^{2k} + c₋ v^{−2k} exactly for k = 0..10.

| N | n | c₊ | c₋ |
|---|---|---|---|
| 2 | 4 | 3 | 1 |
| 2 | 6 | 6 | 2 |
| 3 | 4, 5 | 6 | 3 |
| 3 | 6, 7 | 18 | 9 |

At N = 2 with odd n every coefficient is 0; those rows pass trivially and carry no information (H18 found the same degeneracy).

## Why

The argument in the pre-registration holds on these modules. T_i and T_{n−i} commute and J swaps them. So J maps the joint eigenspace E_{ab} to E_{ba}, and the spaces with a ≠ b contribute nothing to the twisted trace. Only E_{v,v} and E_{−v⁻¹,−v⁻¹} remain, and on them T_i T_{n−i} acts by v² and (−v⁻¹)² = +v⁻². The mixed eigenvalue −1 of the pair product never appears.

So the +v⁻² of H18 and H19 is not a normalisation choice inside this test: it is forced for any module in which J swaps two commuting Hecke generators. Lusztig's weight-2 generator has roots (v², −v⁻²). A J-twisted trace of the ambient product T_i T_{n−i} cannot produce that sign. The fixed root and the weight-3 middle generator are each a single J-invariant element, which is why they carry Lusztig's sign.

## What this leaves open

- Whether some other twist (for example J combined with a sign on part of the module) reproduces Lusztig's −v⁻² for the pairs. Not tested.
- The general argument is a few lines of linear algebra but is not formalised in Lean.
- This is about the trace model, not about the folding conjecture itself, which stays open.

Nothing here is a mass or is compared with experiment.
