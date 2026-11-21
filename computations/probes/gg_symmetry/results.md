# γγ symmetry probe — results

Pre-registration: `preregistration.md` (8b642ae0784). Producer `gg_symmetry_probe.py`, witness `gg-symmetry.witness.json`.

## Outcome as pre-registered: (ii) — check S0 FAILS, and the derived prediction was wrong in one place

| quantity | inverse | mirror | reverse | swap |
|---|---|---|---|---|
| level-3 characters χ_(3), χ_(2,1) | equal (≤1e-40) | equal | equal | equal |
| level-2 restriction χ_(2), χ_(1,1) | **differ** | **differ** | equal | **differ** |
| level-1 | equal | equal | equal | equal |
| passes reading 3 alone | same as Vᵏ | same | same | same |

- The prediction "all four images are conjugate in B₃, so nothing changes" is right for the **full** level-3
  characters (a conjugation invariant) and wrong for the **level-2 restriction**. The restriction is taken along
  the tower H₂ ⊂ H₃, and the half-twist conjugation that relates V to its swap does not preserve H₂. So the
  level-2 numbers depend on how the braid sits relative to the tower, not only on its conjugacy class.
- Inverse, mirror and swap all give the **same** level-2 values. So the family splits into two classes at
  level 2: Vᵏ (and its reverse) versus V̄ᵏ (= mirror, = inverse, = swap). Example k=3:
  χ_(1,1) = 1.01123 for V³ vs 0.98296 for V̄³; χ_(2) = 0.99440 vs 1.00369.
- Passing alone, k = 1..9: exactly k = 3, 6, **9**, for all five forms. k = 9 was not in earlier probes.

## What this means (scope a)

The 3-strand γγ grammar does carry a two-valued label, but only at level 2, i.e. relative to the strand order of
the tower. It does not change whether a particle passes alone. Whether that label is "charge" or "handedness" is an
interpretation, not a result. Nothing is selected or wired.
