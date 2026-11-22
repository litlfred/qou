# H9 result: the folded wall (2026-11-21)

Pre-registration: `h9_preregistration.md`. Script: `h9_folded_wall_probe.py`, output in `.out.txt`.
Exact rational arithmetic at q = 1, 3/2, 2 and q₀ (proton pin, the exact rational). Six strands; the
wall is the middle crossing `σ₃`, so it obeys the crossing's Hecke relation by construction.

## Numbers

| q | reading | T_p/T_n (closed) | D (wall beyond pivot) |
|---|---|---|---|
| 1 | R-sum | 1 | 1 |
| 1 | R-ι | 1 | 1 |
| 3/2 | R-sum | 2.25 (= q²) | 1.46350009868528202 |
| 3/2 | R-ι | 1 | 1.44678320214901508 |
| 2 | R-sum | 4 (= q²) | 0.35855307106475887 |
| 2 | R-ι | 1 | 0.21047807452678845 |
| q₀ | R-sum | 1.23205245416676393 (= q₀²) | **0.95835983113265780026** |
| q₀ | R-ι | 1 | **0.95714512340723750069** |

In every case the boundary trace is independent of where the wall is inserted (7 slots).

## Reading

- **No free continuous number.** The wall's size is fixed by the embedding (`τ ↦ σ₃`, acting by `Ř`).
  This is the first construction in Bridge B with that property. H8's 2×2 eigenvalue-matched
  estimate (0.93996) is not this object, as H8 anticipated.
- **The wall vanishes at q = 1.** There `D = 1` in both readings, so the effect is a pure
  q-deformation, about 4 % at q₀.
- **R-ι removes the pivot from the closed ratio** (`T_p/T_n = 1`), while R-sum keeps it (`= q²`).
  Under both readings the wall's own effect at q₀ is almost the same (0.95836 vs 0.95715).
- `D` swings strongly between q = 3/2 and q = 2, which suggests the denominator `T_p + B_p` passes
  near zero in that range. That has not been checked.
- The R-ptr null (the mirror strand closed by a partial trace, giving `ptr(Ř) = q²·1`) is already a
  theorem (`OverStrandWeight.ptr_markov`) and was not recomputed.

## Verdict under the pre-registered criterion

**Not a hit, but conditional with no free number.** It still depends on three inputs:
1. the folding identification itself (`conj:type-b-folding-cpt`, a conjecture);
2. the boundary inheriting the bulk λ (H8);
3. the choice of mirror reading: R-sum or R-ι. The two differ by 0.13 % at q₀.

`D` is not a mass, since the trace-to-MeV map is not derived, so no CODATA comparison is made. Only
`M_QCD` was computed, for the V³ special pair.
