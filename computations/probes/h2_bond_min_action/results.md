# Results: the H₂ bond by minimum action (issue #8879)

Pre-registered in `PREREGISTRATION.md` (0e083dfc960) before any number here was computed.
Witness `h2-bond-min-action.witness.json`, 2/2 checks: C1 (the length ≤ 3 candidates are exactly
`V₄³, V₅³`, as Lean `gg_atom_bonds` states) and C2 (the `V³` rows reproduce
`h2-ruled-electron.witness.json`, 8/8 verdicts, ratio diff 3e-21).

## Outcome (ii): hypothesis H fails in all four cells

Candidates are the γγ words in `V₄, V₅` of length 1–6 that are atom-preserving and not split:
20 words. 11 pass reading 3 in every cell. The least trace ratio among the passing words is
**`V₄⁶`**, ratio `0.99220056…`, in all four cells. `V₄³` has `0.99739514…`, and `V₅³` has
`0.9985` (`pe`) or `1.0` (`ep`).

| cell | passing | least ratio | `V₄³` | `V₅³` |
|---|---|---|---|---|
| `V³`, `pe` | 11/20 | `V₄⁶` 0.992201 | 0.997395 | 0.998497 |
| `V³`, `ep` | 11/20 | `V₄⁶` 0.992201 | 0.997395 | 1.0 |
| `V⁶`, `pe` | 11/20 | `V₄⁶` 0.992201 | 0.997395 | 0.998447 |
| `V⁶`, `ep` | 11/20 | `V₄⁶` 0.992201 | 0.997395 | 1.0 |

Full ranked lists are in the witness. `V₅V₄V₅V₄`, the only admissible four-photon word, passes
and has ratio `1.0329`, the largest.

## What this means

Minimum trace, read on words, does **not** select `V³`: the six-photon `V₄⁶` has less action, and
the pattern (`V₄⁶ < V₄³`) suggests the trace keeps falling with more photons, so the reading may
have no minimum at all. That was not tested beyond six photons and is not claimed.

So `V³` is selected by γγ + atom-preserving + not split only as the **shortest** admissible bond.
Shortness is not the min-action rule. The nearest corpus statement,
`rem:assembly-shortest-production`, takes the shortest representative of one word modulo the
braid relations. It does not compare different words, so it does not supply the step either.

## Status

- Proved (Lean, merged #8884): the admissible bonds of ≤ 3 photons are `V₄³, V₅³`.
- Measured here: among ≤ 6 photons, min action prefers `V₄⁶`.
- Open: a corpus rule that prefers the fewest photons (or bounds the bond length), or a reason
  min action should be applied with a length bound.
