---
# qou-jr3k
title: 'H3 instance: blocked on ONE lemma — associativity of H3.mul (everything else proved)'
status: completed
type: task
priority: normal
created_at: 2026-08-09T12:31:35Z
updated_at: 2026-08-09T13:05:00Z
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

## DONE — `QOU/Hecke/InstanceH3.lean`

The one lemma landed first try:

```lean
theorem H3.mul_assoc (x y z : H3Carrier R) :
    H3.mul q (H3.mul q x y) z = H3.mul q x (H3.mul q y z) := by
  obtain ⟨a1, a2, a3, a4, a5, a6⟩ := x
  obtain ⟨b1, b2, b3, b4, b5, b6⟩ := y
  obtain ⟨c1, c2, c3, c4, c5, c6⟩ := z
  simp only [H3.mul, H3.mulSigma1, H3.mulSigma2, H3.smul, H3.add, Prod.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring⟩
```

Every coefficient of `H3.mul` is polynomial in the eighteen inputs and the single
scalar `q - q⁻¹`, so associativity is a polynomial identity and `ring` settles it
componentwise. That it *is* an identity is the content: it says `H3.mulSigma1`
and `H3.mulSigma2` faithfully transcribe left multiplication in `H₃(q)`.

Everything downstream followed:

| declaration | content |
|---|---|
| `H3Alg R q` | type synonym for `H3Carrier R` — `def`, so `Prod`'s componentwise `CommRing` cannot leak in |
| `instRing` / `instAlgebra` | `Ring` from the carrier lemmas; `Algebra` via `Algebra.ofModule` |
| `sigma1_sq`, `sigma2_sq` | Hecke quadratic, over an arbitrary field (was `ℝ`-only, generator-action form) |
| `braid` | `σ₁σ₂σ₁ = σ₂σ₁σ₂` in ring form |
| `sigma1_mul_sigma2` etc. | the three composite basis vectors |
| `decompose` | every `x` is an `R`-combination of words in the generators — what `spans` needs |
| **`instHeckeAlgebraH3`** | **`HeckeAlgebra R 3 q (H3Alg R q)`** |
| `finrank_H3Alg` | `finrank R (H3Alg R q) = 6` |
| **`instIsHeckeOfFullRankH3`** | **full Iwahori rank `6 = 3!`** (qou-nkd8's predicate) |

All axiom-clean (`propext, Classical.choice, Quot.sound`).

**This is the first non-vacuous braid relation in the tree.** `InstanceH2` said so
itself: at `n = 2`, `Generator 2` has one index, so `BraidRelation` and
`FarCommutativity` are never satisfiable and both fields are discharged by
`absurd`. At `n = 3` there are two indices, they *are* adjacent, and `braid` has to
be real.

Next rung: `H₄` free of rank `4` over `H₃`, then `isHeckeOfFullRank_succ` gives
`24 = 4!` with no dimension work. Needs H4 multiplication reconciled with
`QOU.Machinery.MarkovTraceH4`'s normal form.
