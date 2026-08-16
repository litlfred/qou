# SU(r) level tower — gap-closure map

**Status: IN PROGRESS (stub — opened with the PR per AGENTS.md rule 2).**

## Premise (owner-supplied, to be independently verified in this branch)

At Wenzl level `r` the Markov parameter is

```
z_r = q^r / [r]_q ,   [r]_q = (q^r - q^{-r})/(q - q^{-1})
```

with (proton pin `q0 = 1.1099785827513808`):

| r | z_r | quotient | row cap |
|---|-----|----------|---------|
| 1 | q | abelian | <=1 |
| 2 | z_D | TL = SU(2) | <=2 |
| 3 | — | SU(3) | <=3 |
| 4 | — | SU(4) | <=4 |
| inf | h = q - 1/q | full H_n | none |

and `y_lambda = 0 <=> len(lambda) > r`.

## Work items

1. Delta_lambda binding magnitude — re-score the six failed closure ansaetze
   with <=2-row support at the D frame. **Not a seventh ansatz.**
2. Per-channel levels from the trace-convention registry.
3. Mass: sites that *posit* the two-row cap and infer D from it.
4. Standard model / 8-fold — adversarial; measure the colour channel's `z`.
5. Compute: `dim TL_n = Catalan(n)` vs `n!`.
