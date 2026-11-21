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
| `eval_borOrbit_conj`, `conj_flip`, `conj_mirror` | The 4 Borromean words are conjugate in B₃ (the flip s₀↔s₁ is conjugation by Δ = σ₀σ₁σ₀, `conj_flip`; the mirror is a cyclic rotation followed by the flip, `conj_mirror`). |
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
  tr_M = ±tr_M(β_Bor) as a rational function of q. **Label corrected
  (Addendum 3):** these weights, y₍₃₎ = q³/[3]_q!, are the corpus F_Bor weights,
  *not* convention D, which has y₍₁³₎ = 0 and y₍₃₎ = 1 − 2/[2]_q².
* P3-D (Addendum 3, no prediction): rerun with true convention-D weights,
  `p3_convention_d.py`, 46 s, log `p3d.log`, witness `p3-convention-d.result.json`.
  **0 hits** at every length 1..8 (2 to 50 distinct (writhe, χ) classes per length).
  tr_M^D(β_Bor) equals the corpus closed form exactly, as it must at writhe 0.
  So the writhe ≠ 0 answer is the same under both weight sets.
* Side note for the /q³ question: F_Bor = |tr_M|·[3]_q!/q³ divides by the corpus
  y₍₃₎ = q³/[3]_q!. Under convention D the trivial-block weight is
  y₍₃₎ = (q² + q⁻²)/[2]_q² instead (≈ 0.505 vs ≈ 0.223 at q₀). This file does not
  decide which normalisation is right; it only records that the two differ.
* E2 (prediction failed in the timing): a **second Brunnian character appears at
  length 10, not 12** — 20 words, e.g. σ₀³σ₁⁻¹σ₀σ₁⁻³σ₀σ₁⁻¹; at length 12 three
  more characters, including (σ₀σ₁⁻¹)⁶ = β_Bor². So "Brunnian" alone does not fix
  the word; minimality does.

### Extension to lengths 14 and 16 (pre-registered Addenda 2 and 4)

`borromean_fibre_len14.py`, 3.59 M prefix nodes, 80 s, log `len14.log`,
witness `borromean-fibre-len14.result.json`. Both predictions held.

| length | words with χ = χ(β_Bor) | conjugate to β_Bor found (\|c\| ≤ 6) | tr_M = −tr_M(β_Bor) | distinct Brunnian characters |
|---|---|---|---|---|
| 12 | 2240 | 2240 | 0 | 4 |
| 14 | 15812 | 15812 | 0 | 9 |
| 16 (Addendum 4, \|c\| ≤ 7) | 110840 | 110840 | 0 | 15 |

Length 16: `borromean_fibre_len16.py`, 30.2 M prefix nodes, 753 s, log `len16.log`,
witness `borromean-fibre-len16.result.json`. All three pre-registered predictions held.

So to length 16, **the F_Bor value picks out exactly β_Bor's conjugacy class** among
writhe-0 three-strand words, while the number of other Brunnian traces keeps
growing (1, 1, 2, 4, 9, 15 at lengths 6 to 16).

### All lengths, by reduction to SL(2,ℤ) (pre-registered Addendum 5)

`sl2z_class_reduction.py`, log `sl2z.log`, witness `sl2z-class-reduction.result.json`.
Exact integer and Laurent arithmetic.

**Statement.** Let w be a three-strand word of writhe 0 with χ₍₂,₁₎(w) = χ₍₂,₁₎(β_Bor).
Then w is conjugate to β_Bor in B₃, at any length. This rests on two cited facts and a
finite computation.

**Cited facts.**
* (F1) Burau at t = −1 (σ₀ ↦ R = [[1,1],[0,1]], σ₁⁻¹ ↦ L = [[1,0],[1,1]]) maps B₃ onto
  SL(2,ℤ), with kernel ⟨Δ⁴⟩, where Δ = σ₀σ₁σ₀ and writhe(Δ⁴) = 12.
* (F2) Every SL(2,ℤ) class of trace > 2 contains a positive R/L word, unique up to
  cyclic rotation.

**Proof.**
1. Writhe is a homomorphism, and ⟨Δ⁴⟩ contains no non-trivial element of writhe 0. So
   writhe-0 braids map injectively to SL(2,ℤ).
2. Two writhe-0 braids are conjugate in B₃ iff their images are conjugate in SL(2,ℤ):
   lift the conjugator by (F1) and use step 1.
3. At writhe 0, T(w) = q^writhe·Burau_{t=q⁻²}(w) = Burau(w). So χ(w) evaluated at q = i
   is the trace of the t = −1 image, and χ(β_Bor)(i) = 18. Any w with χ(w) = χ(β_Bor)
   therefore maps to a trace-18 class.
4. By (F2), the trace-18 classes are the positive R/L words of trace 18 up to rotation.
   The search is complete for words of at most 40 letters, and every trace-18 word is
   that short: for non-negative SL(2,ℤ) matrices with diagonal ≥ 1,
   tr(MN) ≥ tr M + tr N − 2, and tr(RᵃLᵇ) = ab + 2 ≥ a + b + 1. Hence a word with
   n letters has trace ≥ n/2 + 2, so trace 18 forces n ≤ 32. The enumeration at bound
   60 returns the same 8 classes.
5. There are **8 classes**. Only two lift to writhe 0, because the lift writhe must be
   ≡ 0 mod 12: (RL)³, which is β_Bor, and R⁴L⁴. For R⁴L⁴, χ(σ₀⁴σ₁⁻⁴) ≠ χ(β_Bor). So
   β_Bor's class is the whole fibre.

The pre-registered prediction held. This subsumes the length-6 to length-16 searches,
which agree with it.

**E7 (no prediction): the general statement is false.** "Same χ at writhe 0 ⇒
conjugate" fails for other classes. Searching traces 3–40 found 8 pairs of distinct
writhe-0 classes with the same χ. The first is at trace 15: RL R²L² and RL² R²L, that is
σ₀σ₁⁻¹σ₀²σ₁⁻² and its reverse. Their images are not conjugate in SL(2,ℤ), so by step 2
the braids are not conjugate in B₃. A braid and its reverse always share χ. So the
uniqueness above is specific to β_Bor, whose reverse is conjugate to itself.

## 3. What this does and does not settle

* β_Bor is **singled out** by: three strands + pure + zero pairwise linking +
  non-trivial + **minimal crossing number**. The last is the input: it is the same
  cost (crossing count) that the γγ route minimises
  (`QOU.Mass.GammaGammaSelectionAllK.frobeniusSelected_borromean_all`) and the
  U(1)-neutral cut (owner ruling of 2026-11-21 on whole-word U(1) neutrality, `QOU/PhotonU1NeutralCut.lean`, PR #8835,
  which selects V³ = β_Bor up to 10 crossings by enumeration), so these routes rest
  on the same cost axiom, reached from different premises.
* The γγ route (already in the corpus, sorry-free) selects β_Bor among all γγ words
  of H₃, conditional on the vertex σᵢσᵢ₊₁⁻¹, reading 3 (Frobenius positivity, owner's
  provisional choice) and 1 < q ≤ 23/20. This file's route uses none of those.
* **Freedom left by the mass identity:** F_Bor depends on the word only through
  (writhe, χ₍₂,₁₎). That fibre is exactly β_Bor's conjugacy class **at every length** (SL(2,ℤ)
  reduction above, given the cited F1 and F2). Words with other characters (the length-10
  Brunnian braids, β_Bor²) give different F values, so the identity's agreement
  is specific to β_Bor among the Brunnian candidates.
* Not addressed: why three strands (the baryon number), and the colour-singlet
  reading ("zero signed gluon sum", `borromean-gluon-content.md`), which β_Bor
  does not satisfy exactly at q₀ by the corpus's own account.
