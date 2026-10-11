# Route 2, option 1c: where do words collapse, and does the q-length split them? (pre-registration)

Written 2026-10-11, before anything below was computed. The owner picked "3" that day: pre-register a finer energy that keeps the word, not only its Bring loop. Nothing in this file reads Q_β, CODATA, a mass or any target.

## 0. Why

Option 1b (`results_sameloop.md`) found two things:
- the 316 fresh 13-letter classes give only 10 loops on Bring's surface, up to symmetry;
- the shortest loop, which also has the smallest ropelength, carries **90** word classes.

So no energy on the Bring loop can choose a word. An energy that does choose one has to remember something the loop forgets. Before designing that energy, this file first measures **where** along route 2's chain the 90 words become indistinguishable. That measurement selects nothing.

What is already known, and so contaminated:
- the 13-letter Bring loops and their Λ values (option 1b);
- the q-recipe values on the seven named 9- and 11-letter candidates (`results_qdeformed.md`).

No q-length of a 13-letter word has been computed.

## 1. The stages (fixed now)

For each of the 316 classes of positive 13-letter words in σ₀, σ₁ (up to rotation and the σ₀ ↔ σ₁ swap; the same set as option 1b), record:

**S1. The braid, up to conjugacy in B₃.** For words of equal length this is decided exactly by the image in PSL(2,ℤ), via σ₀ ↦ T = [[1,1],[0,1]] and σ₁ ↦ L = [[1,0],[−1,1]]. The argument:
- the kernel of B₃ → PSL(2,ℤ) is the centre ⟨Δ²⟩, and Δ² has exponent sum 6;
- so if c b c⁻¹ = b′ Δ^{2k}, equal exponent sums force k = 0.

The canonical key for M ∈ SL(2,ℤ), after multiplying by ±1 so that tr ≥ 0:
- **Hyperbolic** (tr > 2): the trace, together with the continued-fraction period of the attracting fixed point. The period is taken up to **even** cyclic shifts, after doubling it if its length is odd. This is SL(2,ℤ)-equivalence, not GL(2,ℤ)-equivalence.
- **Parabolic** (tr = 2): the signed integer n with M conjugate to [[1,n],[0,1]]. Here |n| = gcd of the entries of M − I, and the sign is sign(b), or sign(−c) when b = 0.
- **Elliptic** (tr < 2): the trace, together with the sign of c (the direction of rotation) when tr ≠ 0.

**S1′. The Burau trace polynomial** tr ρ(w) ∈ ℤ[t]. It is computed exactly, with ρ the reduced Burau representation of `bring_route2_qdeformed_probe.py`. It is a conjugacy invariant, so it can only be as fine as S1 or coarser.

**S2. The SL(2,ℤ) image up to GL(2,ℤ)-conjugacy**, the rule option 1 used.

**S3. The Bring loop up to symmetry**, taken from `results_sameloop.json`. Words with no loop get "none".

**S4. The q-lengths** ℓ(t) at t = −q₀, the owner-ruled recipe, and at t = +q₀, for cross-reference. The formulas are those of `preregistration-qdeformed.md`, with q₀ the proton pin from `qou_substrate.constants.Q_50_DIGIT_STR`, at mpmath 60 dps:
- x = |tr|/√|det|;
- if det > 0: ℓ = 2·arccosh(x/2) when x > 2, ℓ = 0 when parabolic, and ℓ = 0 with a rotation angle when elliptic;
- if det < 0: ℓ = 2·arcsinh(x/2).

Since 13 is odd, det = (−t)¹³ = q₀¹³ > 0 at t = −q₀, and det < 0 at t = +q₀.

## 2. Reported, with no verdict (diagnostic)

- The number of classes at each stage, over all 316 word classes.
- The same for the **90 word classes on the shortest Bring loop**.
- Whether S1′ separates exactly what S1 separates.

## 3. The energy test (fixed now)

**Energy.** E_q(w) = ℓ(−q₀), the q-length at the ruled point. **Smaller ranks higher**, as for every route 2 energy so far. Words with ℓ = 0 (parabolic or elliptic at t = −q₀) are reported separately and excluded from the ranking, as route 2 excludes words with no loop.

**Test A (stand-alone).** Over all 316 classes, E_q passes when its smallest positive value is attained by exactly **one** B₃ conjugacy class (S1), comparing values to 40 digits.

**Test B (combined, fixed order).** Among the 90 word classes on the shortest Bring loop, E_q passes when its smallest positive value is attained by exactly one B₃ conjugacy class. "Bring loop first, then q-length" is the order fixed here, and no other order is tried.

**Either result selects nothing.** A pass means only that this energy can discriminate on fresh words. The seen candidates are 9 and 11 letters long and are not in this set.

## 4. Checks (pre-registered)

1. **Class count:** 316 classes, matching option 1b.
2. **Invariance:** same S1 key ⇒ same Burau trace polynomial. This is a theorem, so any violation is a bug.
3. **Classical limit:** the Burau trace at t = −1 equals the SL(2,ℤ) trace.
4. **Reproduction:** the q-length at t = −q₀ of `gluon_s1_s0` (class A) matches `results_qdeformed.json` to 40 digits.
5. **S1 is at least as fine as S2:** same S1 key ⇒ same S2 key.
6. **Arithmetic:** mpmath only; no float64.
