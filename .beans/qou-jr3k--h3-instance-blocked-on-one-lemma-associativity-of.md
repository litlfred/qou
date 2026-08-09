---
# qou-jr3k
title: 'H3 instance: blocked on ONE lemma — associativity of H3.mul (everything else proved)'
status: todo
type: task
created_at: 2026-08-09T12:31:35Z
updated_at: 2026-08-09T12:31:35Z
---


`QOU/Mathlib/HeckeAlgebra.lean` already contains almost all of `H_3(q)`:

| piece | status |
|---|---|
| `H3Carrier R = R⁶` | rank **6 = 3!** — correct |
| `H3.sigma1`, `H3.sigma2`, basis | present |
| `H3.mulSigma1` / `mulSigma2` (generator actions) | present |
| `H3.mul` (full multiplication) | present |
| `H3.sigma1_sq_eq`, `H3.sigma2_sq_eq` | **proved** |
| `H3.braid_relation` | **proved** |
| `H3.one_mul` | **proved** |
| `mul_assoc` for `H3.mul` | **MISSING** |
| `Ring` / `Mul` instance on `H3Carrier` | **MISSING** |

The Hecke relations are already theorems. The only blocker is that
`H3Carrier` is not a `Ring` — `QOU.Hecke.HeckeAlgebra` requires
`[Ring A] [Algebra R A]`, and associativity of `H3.mul` is unproved.

**So this is one lemma, not a construction.**

## Task

- [ ] Prove `H3.mul` associative. It is defined by basis decomposition, so this
      is a finite check — 6³ = 216 basis triples. Likely wants the definition
      restated basis-wise rather than through `H3.smul` folds, so the cases
      reduce cleanly.
- [ ] Derive `Ring (H3Carrier R)` and `Algebra R (H3Carrier R)`.
- [ ] Restate the three relations in ring-multiplication form. They are
      currently in generator-action form (`mulSigma1 q (sigma1 ℝ) = …`) and over
      `ℝ` specifically rather than a general field.
- [ ] Instantiate `QOU.Hecke.HeckeAlgebra R 3 q (H3Carrier R)`.

## Note

Do this **after** qou-nkd8 (the rank axiom), or the instance proves nothing that
`rankOneModel` does not already prove. The value of H3 is that it has the right
rank — which the class currently cannot express.

Compute already has the structure constants
(`computations/markov/gen_gram_closure.py` shows the generator pattern that
would make the 216-case check mechanical).
