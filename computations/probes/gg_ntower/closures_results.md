# γγ climbing placements under three closures: results

Recipe: `closures_preregistration.md`, committed in `152a15575e` before any number was computed. Producer: `gg_closures_probe.py`. Witness: `gg-closures.witness.json`. Exact arithmetic in the field ℚ(q); signs at the proton pin q₀ by exact rational evaluation (mpmath 60 dps for display); signs on (1, ∞) by Sturm counts. No floats. Wall time 371 s.

The first run hit the 2 h background limit inside K1, because sympy factorisation was slow. No number from it was read. The rerun uses the same formulas in field arithmetic, about 100× faster. Two code fixes followed: K4 needed level-2 characters, and the h-order helper was wrong. Both are in the commit history.

Nothing is ranked, selected, or compared with data. Owner rulings in force: reading 3 at **every strand count** m = 3..n (2026-10-12), convention D.

## Checks: 4/4 pass

| check | what it confirms | result |
|---|---|---|
| K1 | Closure 1 (top) reproduces all **672** characters of #7733's witness exactly | pass |
| K2 | Top-level characters of W and of its flip φ_n W agree on every row (φ is inner) | pass |
| K3 | At q = 1, the level-3 χ_(2,1) under top and bottom closure equals the permutation-model value 2^{−c}·χ_(2,1)(π̂) | pass |
| K4 | χ_{μ+(1,1)}(y·e_m) = χ_μ(E(y)) for sample y ∈ H_m, m = 3, 4, 5. This is the Jones absorption law e·y·e = E(y)·e on characters, under convention D. It holds in these representations; the Lean class `JonesBasicConstruction` stays open | pass |

## Verdicts: 62 rows (2 vertices × shifts s ∈ {0, ±1, ±2, +3} × k, n ≤ 9)

**Outcome (ii) for every placement that genuinely climbs.** For s ∈ {−1, ±2, +3}, **no k is admissible under any closure**: top, bottom, pair from the top, or pair from the bottom. Both vertices.

**Outcome (iii) occurs only on the degenerate staircase s = +1** (which telescopes to σ₀σ_k⁻¹):

| rows | top | bottom | pair | pair (bottom) |
|---|---|---|---|---|
| V, s = +1, k = 4..7 | ✓ | ✗ | ✗ | ✗ |
| U, s = +1, k = 3..7 | ✓ | ✓ | ✗ | ✗ |
| every other row | same verdict in all four | | | |

The same-strand rows (s = 0, n = 3) close nothing, so all four closures agree there: k = 3 and k = 6 pass.

## How the closures differ, and why

**Top versus bottom: the difference is the vertex's orientation.**
- For U the two closures give identical characters on every row.
- For V they differ in characters on 20 rows, but the verdict changes only at s = +1.
- At level 3 they differ exactly on the rows whose q = 1 residue is a transposition (s = +1, and s = −1 with k even). There χ_(2,1) = 0 at q = 1, and the sign is decided at order t¹ by which single crossing survives.
- Worked case, the telescoped staircase σ₀σ_k⁻¹. Top closing removes the far crossing σ_k⁻¹ and leaves σ₀, with χ_(2,1)(σ₀) = h > 0. Bottom closing removes σ₀ and leaves the inverse crossing, with χ_(2,1) = −h < 0.
- The flip turns V into V⁻¹ (#7760). That is why top and bottom closing differ only for V, never for U.

**Pair closure: the trivial block flips sign.**
- The Jones projection e_i is the singlet (antisymmetric) projector on strands i, i+1, and σ_i acts on its image by the eigenvalue −q⁻¹.
- Annihilating the top pair as a singlet therefore evaluates every crossing on that pair at −q⁻¹. For s = ±2 and +3 (k ≥ 2), that makes the **trivial block** χ_(m,0) negative at a failing level. Example: V, s = +2, k = 2, level 3 gives χ_(3) = −q⁴/(q²+1).
- So for those shifts, under the pair closure reading 3 fails on the block that is positive under top and bottom closing: the failure moves from the spin-½ block to the spin-max block, and does not go away.
- For s = −1 the pair closure fails in the non-trivial blocks instead. For example, at level 3, k = 3: χ_(3) = 0 and χ_(2,1) = −q⁴/(q²+1).
- The same mechanism kills the s = +1 staircase, which top closing admits.
- Pair from the top and pair from the bottom differ in characters on 78 entries. They agree in verdict on all 62 rows.

**Level-3 q = 1 values under the pair closure.** With an odd strand count the pair chain ends at level 3:
- s = ±2, k even: χ_(2,1) = +2^{−(k−1)}, positive, while χ_(3) = −2^{−(k−1)}.
- s = −1, k odd: χ_(2,1) = −½.
- s = +3, k = 3: χ_(2,1) = −¼.

So at q = 1 the pair closure trades the 3-cycle defect for a sign defect on the symmetric block.

**Proportional to a single vertex?** (pre-registered question, §5)
- **Top/bottom:** yes for s = ±2 and +3 at every k, for both vertices; for V also at s = −1 with k odd, but for U not at s = −1. On the y > 0 blocks, the closed-down element is a positive multiple of one vertex. This is the "one uncancelled colour rotation" of `explanation.md`, now as an exact identity on those blocks.
- **Pair closure:** yes only for s = ±2 at k = 3 and for s = +3, k = 3.

## What this says

- Within rigid-shift placement, **no closure in the corpus (top, bottom, or Jones pair) confines a climbing γγ cascade**, up to 9 strands. This is scope (a): fixed vertex, rigid shift, these three closures.
- The closures disagree only where the q = 1 permutation residue is not a 3-cycle. There the sign is set at order t¹ by **which oriented crossing survives**, and that is the vertex orientation again (compare #7760: the γγ core is flip-odd up to h³).
- The pair closure does not rescue climbing. For s = ±2 and +3 it moves the failure to the symmetric (trivial) block, because annihilating a pair as a singlet evaluates its crossings at −q⁻¹. For s = −1 it fails in the other blocks.

## Not done

Non-rigid placements; quark letters; two nucleons; any comparison with data.
