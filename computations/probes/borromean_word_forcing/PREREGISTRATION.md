# Pre-registration: does anything force the Borromean word β_Bor = (σ₀σ₁⁻¹)³?

Written 2026-11-21, **before any code in this directory was run.** Thread
"Derive the proton's Borromean braid". Exact arithmetic only (Python `int`
Laurent polynomials); no float, no mpmath evaluation, no measured value
anywhere. Nothing here reads CODATA, AME or PDG.

## Objects

* B₃ words over the letters σ₀, σ₀⁻¹, σ₁, σ₁⁻¹, freely reduced.
* Writhe e(w) = (#positive) − (#negative).
* Strand permutation; *pure* = identity permutation (closure has 3 components).
* Pairwise linking lk_ij(w) = ½ Σ (signs of crossings between strands i and j).
* The H₃ (2,1) character χ(w) ∈ ℤ[q, q⁻¹], computed from the rational
  representation T_i = q · Burau_i(t = q⁻²) (entries in ℤ[q,q⁻¹]; eigenvalues
  q and −q⁻¹, so it satisfies the Hecke relation used by the corpus).
* Markov trace on B₃: tr(w) = y₍₃₎ q^e + y₍₁³₎ (−q⁻¹)^e + y₍₂,₁₎ χ(w)
  (Wedderburn decomposition; the (3) and (1³) blocks are 1-dimensional).

## Fact used as input (already in the corpus)

`tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h² + 4)`, `F_Bor = |tr_M|·[3]_q!/q³`
(`computations/phase5/phase1d_f_bor_exact_h_expansion.py`). F_Bor therefore
depends on the word only through tr_M.

## Questions and predictions (stated before running)

**P1. Minimal Brunnian word.** Enumerate all reduced words of length ≤ 8.
Keep those that are pure, have lk₀₁ = lk₀₂ = lk₁₂ = 0, and whose character
differs from the identity's (χ ≠ 2, i.e. tr ≠ tr(unlink) at writhe 0).
Prediction: **no survivor of length < 6; at length 6 every survivor has the
same character as β_Bor** (survivors = cyclic rotations, σ₀↔σ₁ flip,
inverse and mirror of β_Bor). If a length-6 survivor has a different
character, the "minimal Brunnian" route does not single out β_Bor's trace.

**P2. Same-trace fibre.** Among writhe-0 words up to length 10, list those with
χ(w) = χ(β_Bor) (same tr_M, hence same F_Bor) and with χ(w) giving
tr_M(w) = −tr_M(β_Bor) (same |tr_M|, same F_Bor). For each, report component
count and pairwise linking. Prediction: no word gives −tr_M; words with
χ = χ(β_Bor) exist beyond the symmetry orbit of β_Bor (at length 8 or 10),
because a B₃ character cannot separate all conjugacy classes. Whether any of
them is *not* Brunnian (non-zero linking or ≠ 3 components) is the
question that decides whether the mass identity itself sees the Borromean
property. No prediction on that.

**P3. Writhe ≠ 0.** The same check for |e| ≤ 4 words up to length 8 whose
tr_M equals ± tr_M(β_Bor) as a rational function of q, with y₍₃₎ = q³/[3]_q!,
y₍₂,₁₎ = 1/[2]_q², y₍₁³₎ = 1 − y₍₃₎ − 2y₍₂,₁₎ (the corpus F_Bor weights that — NOT convention D, see Addendum 3 —
reproduce the corpus tr_M(β_Bor) above; this is checked first, and the run
stops if it fails). Prediction: none.

## What would count as each outcome

* "β_Bor is singled out (up to symmetry) by minimality + Brunnian + non-trivial
  trace": P1 holds as predicted.
* "The mass cannot tell β_Bor from X": any P2/P3 hit not in β_Bor's orbit.
* A failed prediction is reported as such; nothing is re-run with a changed
  filter to make it pass.

## Addendum 1 (2026-11-21, after the first run, before the runs it describes)

First-run outcome, recorded before any extension: P1 as predicted (no
survivor below length 6; the 4 length-6 survivors are the 4 words of
β_Bor's orbit). At length 8, 56 survivors, all with χ = χ(β_Bor). P2: 4 / 56 /
300 same-χ words at lengths 6 / 8 / 10, none with tr = −tr_Bor, and every one
closes to 3 components with zero pairwise linking. P3: no hit.

The orbit used (rotation, flip, inverse, mirror) has only 4 elements, so the
length-8 and length-10 words are "outside the orbit" only because the orbit
omits conjugation by non-cyclic elements. Two extensions, stated now:

**E1. Conjugacy.** For each same-χ word w of length 8 and 10, search for a
conjugator c (reduced, length ≤ 5) with c·β·c⁻¹ = w in B₃ for some β in the
4-word orbit, testing equality by the Burau matrices (T_i = q·Burau_i(q⁻²);
the Burau representation of B₃ is faithful, Magnus–Peluso 1969, so matrix
equality is equality in B₃ — a cited fact, not proved here). Prediction:
every one is conjugate to β_Bor or to its mirror (σ₀⁻¹σ₁)³ with |c| ≤ 2.

**E2. P1 to length 12.** Prediction: at length 10 every survivor still has
χ = χ(β_Bor); at length 12 a second character appears (the commutator
[σ₀⁴, σ₁²]-type Brunnian braids, Milnor invariant 2), so "nontrivial
zero-linking pure ⇒ Borromean trace" is a statement about the *shortest*
words only.

## Addendum 2 (2026-11-21 20:31Z, owner chose "extend to length 14"; written before the run)

**E3. Same-character fibre to length 14.** All reduced writhe-0 words of length
12 and 14 with χ = χ(β_Bor) or tr_M = −tr_M(β_Bor). For each, search a conjugator
c (reduced, |c| ≤ 6) with c·β·c⁻¹ = w, β in the 4-word orbit (Burau equality,
faithful on B₃, cited). Prediction: still no −tr_M word; every same-χ word is
found conjugate to β_Bor. A same-χ word with no conjugator found is reported as
"not found within |c| ≤ 6", not as "not conjugate"; for those, report the
closure data (components, pairwise linking).

**E4. Brunnian characters to length 14.** Count the distinct non-trivial
characters among pure zero-linking words at lengths 12 and 14. No prediction
beyond: β_Bor's character stays the only one at length 6–8.

## Addendum 3 (2026-11-21, after QA review, written before the run it describes)

**Correction to P3's label.** P3 above calls y₍₃₎ = q³/[3]_q!, y₍₁³₎ = 1 − y₍₃₎ − 2y₍₂,₁₎
"the convention-D weights". That is wrong. Convention D (z = q³/(q²+1)) forces
y₍₁³₎ = 0 and so y₍₃₎ = 1 − 2y₍₂,₁₎ = (q² + q⁻²)/[2]_q² (≈ 0.505 at q₀), not
q³/[3]_q! (≈ 0.223). The P3 weights are the ones the corpus closed form for
tr_M(β_Bor) and F_Bor = |tr_M|·[3]_q!/q³ use. The P3 run is kept and relabelled
"corpus F_Bor weights, not convention D". P1, P2, E1–E4 are writhe 0, where
tr = 1 + y₍₂,₁₎(χ − 2) under both weight sets (only y₍₃₎ + y₍₁³₎ enters), so
they are unaffected.

**P3-D. Writhe ≠ 0 with true convention-D weights.** Same word set as P3
(reduced, length 1..8, 0 < |e| ≤ 4), with y₍₁³₎ = 0, y₍₂,₁₎ = 1/[2]_q²,
y₍₃₎ = 1 − 2/[2]_q². Count words with tr_M = ± tr_M^D(β_Bor) exactly as rational
functions of q. Under these weights tr = y₍₃₎q^e + y₍₂,₁₎χ, so a hit needs
χ = χ(β_Bor) − (q² + q⁻²)(q^e − 1) (or the − analogue). No prediction.
Also record tr_M^D(β_Bor) in closed form next to the corpus value.

## Addendum 4 (2026-11-21 22:40Z, owner "keep going"; written before the run)

**E5. Same-character fibre and Brunnian characters at length 16.** Same method as
E3/E4 (`borromean_fibre_len16.py`, a copy of the length-14 script with
`LENGTHS = (16,)` and conjugators searched to |c| ≤ 7). Predictions: (i) no word with
tr_M = −tr_M(β_Bor); (ii) every writhe-0 word with χ = χ(β_Bor) is found conjugate to
β_Bor. (iii) The count of distinct Brunnian characters keeps growing (more than 9).
Why (ii) is not automatic: at t = −1 the image of β_Bor is [[13, 8], [8, 5]], trace 18,
and trace alone does not fix SL(2,ℤ) conjugacy in general. A same-χ word with no
conjugator found is reported as "not found within |c| ≤ 7", with its closure data, and
then checked separately; it is not called "not conjugate" without a proof.

## Addendum 5 (2026-11-21 23:10Z, owner chose "1 2"; written before any computation)

**E6. All lengths, by reduction to SL(2,ℤ).** Cited standard facts (not proved here):
(F1) Burau at t = −1 (σ₀ ↦ R = [[1,1],[0,1]], σ₁⁻¹ ↦ L = [[1,0],[1,1]]) is onto SL(2,ℤ)
with kernel ⟨Δ⁴⟩, Δ = σ₀σ₁σ₀, writhe(Δ⁴) = 12. (F2) Every SL(2,ℤ) conjugacy class with
trace > 2 contains a positive word in R, L, unique up to cyclic rotation.
Consequences used: writhe is a homomorphism and ⟨Δ⁴⟩ meets writhe 0 trivially, so
writhe-0 braids map injectively to SL(2,ℤ), and two writhe-0 braids are conjugate in B₃
iff their images are conjugate in SL(2,ℤ) (lift the conjugator). For writhe 0,
T(w) = q^writhe·Burau_{t=q⁻²}(w) = Burau(w), so χ(w) at q = i is tr of the t = −1 image;
χ(β_Bor)(i) = 18. So any writhe-0 w with χ(w) = χ(β_Bor) has image of trace 18.

Plan: list all cyclic positive R/L-words of trace 18 (finite), lift each to the
braid σ₀^{a₁}σ₁^{−b₁}…, keep the classes with a writhe-0 lift (writhe ≡ 0 mod 12, then
multiply by Δ^{−4k}), and compute the generic χ of each. Prediction: exactly one such
class has χ = χ(β_Bor), namely β_Bor's (R L)³ ↔ trace of [[13,8],[8,5]]. If it holds,
"same χ at writhe 0 ⇒ conjugate to β_Bor" holds at **every length**, given F1 and F2.
If another class has χ = χ(β_Bor), that is a counterexample at some length > 16, and
it will be reported with its word.

**E7 (side check, no prediction).** Whether "same χ ⇒ conjugate" fails for *some*
writhe-0 class in general (other traces), e.g. via a braid and its reverse.
