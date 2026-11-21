# Result: what singles out the Borromean word β_Bor = (σ₀σ₁⁻¹)³

2026-11-21, thread "Derive the proton's Borromean braid". Pre-registration:
[`PREREGISTRATION.md`](PREREGISTRATION.md) (written and committed before any run).
Lean: [`QOU/Mass/BorromeanWordForcing.lean`](../../../folio/quantum-observable-universe/lean/QOU/Mass/BorromeanWordForcing.lean),
`lean`-direct exit 0, no `sorry`, axioms `propext, Classical.choice, Quot.sound` only.
No measured value is used anywhere.

## 1. Proved in Lean

| theorem | statement |
|---|---|
| `minimal_pure_zeroLinking` | A reduced word in the B₃ letters that is pure with all three pairwise linking numbers zero has length 0 or ≥ 6; at length 6 it is the identity of B₃ or conjugate in B₃ to β_Bor; and β_Bor ≠ 1. |
| `pureZeroLinking_six` | Exactly 16 such words of length 6: the 4 Borromean words (β_Bor, its rotation, its mirror, the mirror's rotation) and 12 rotations of σ₀σ₁σ₀(σ₁σ₀σ₁)⁻¹ or its inverse. |
| `eval_trivSix` | The 12 are the identity (braid relation). |
| `eval_borOrbit_conj`, `conj_flip`, `conj_mirror` | The 4 Borromean words are conjugate in B₃ (the mirror is conjugate to β_Bor via Δ = σ₀σ₁σ₀). |
| `eval_borromean_ne_one` | β_Bor ↦ [[13, 8], [8, 5]] under the integer Burau representation at t = −1. |
| `markovTrace_writhe_zero` | With y₍₃₎ + 2y₍₂,₁₎ + y₍₁³₎ = 1, a writhe-0 word has tr = 1 + y₍₂,₁₎(χ − 2), χ its (2,1) character. |

Topological reading (cited, not formalised): for a pure 3-braid, removing a strand
leaves σ^{2k} with k the remaining pair's linking number, so the closure is Brunnian
exactly when all linking numbers vanish and the closure is not the unlink. So the
theorem says **β_Bor is, up to conjugacy, the shortest three-strand braid whose
closure can be Brunnian.**

## 2. Measured (exact Laurent arithmetic, pre-registered)

* P1 (predicted, held): no pure zero-linking word with a non-trivial (2,1)
  character below length 6; the 4 at length 6 all have χ(β_Bor).
* P2 (prediction partly failed): words with χ = χ(β_Bor): 4 / 56 / 300 at
  lengths 6 / 8 / 10, none with tr_M = −tr_M(β_Bor). I predicted some would lie
  outside β_Bor's conjugacy class; **E1 found every one conjugate to β_Bor**
  (conjugator length ≤ 2; equality tested by Burau matrices, faithful on B₃ by
  Magnus–Peluso, cited). So up to length 10 the F_Bor value picks out exactly
  β_Bor's conjugacy class.
* P3 (predicted, held): no word with writhe ≠ 0, |e| ≤ 4, length ≤ 8 has
  tr_M = ±tr_M(β_Bor) as a rational function of q.
* E2 (prediction failed in the timing): a **second Brunnian character appears at
  length 10, not 12** — 20 words, e.g. σ₀³σ₁⁻¹σ₀σ₁⁻³σ₀σ₁⁻¹; at length 12 three
  more characters, including (σ₀σ₁⁻¹)⁶ = β_Bor². So "Brunnian" alone does not fix
  the word; minimality does.

### Extension to length 14 (pre-registered Addendum 2, owner choice "extend")

`borromean_fibre_len14.py`, 3.59 M prefix nodes, 80 s, log `len14.log`,
witness `borromean-fibre-len14.result.json`. Both predictions held.

| length | words with χ = χ(β_Bor) | conjugate to β_Bor found (\|c\| ≤ 6) | tr_M = −tr_M(β_Bor) | distinct Brunnian characters |
|---|---|---|---|---|
| 12 | 2240 | 2240 | 0 | 4 |
| 14 | 15812 | 15812 | 0 | 9 |

So to length 14, **the F_Bor value picks out exactly β_Bor's conjugacy class** among
writhe-0 three-strand words, while the number of other Brunnian traces keeps
growing (1, 1, 2, 4, 9 at lengths 6, 8, 10, 12, 14).

## 3. What this does and does not settle

* β_Bor is **singled out** by: three strands + pure + zero pairwise linking +
  non-trivial + **minimal crossing number**. The last is the input: it is the same
  cost (crossing count) that the γγ route minimises
  (`QOU.Mass.GammaGammaSelectionAllK.frobeniusSelected_borromean_all`), so the two
  routes rest on the same cost axiom, reached from different premises.
* The γγ route (already in the corpus, sorry-free) selects β_Bor among all γγ words
  of H₃, conditional on the vertex σᵢσᵢ₊₁⁻¹, reading 3 (Frobenius positivity, owner's
  provisional choice) and 1 < q ≤ 23/20. This file's route uses none of those.
* **Freedom left by the mass identity:** F_Bor depends on the word only through
  (writhe, χ₍₂,₁₎). To length 14 that fibre is exactly β_Bor's conjugacy class;
  beyond length 14 it is not tested. Words with other characters (the length-10
  Brunnian braids, β_Bor²) give different F values, so the identity's agreement
  is specific to β_Bor among the Brunnian candidates.
* Not addressed: why three strands (the baryon number), and the colour-singlet
  reading ("zero signed gluon sum", `borromean-gluon-content.md`), which β_Bor
  does not satisfy exactly at q₀ by the corpus's own account.
