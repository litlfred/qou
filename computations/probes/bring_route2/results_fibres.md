# Route 2, option 1c: results

Recipe: `preregistration-fibres.md`, committed (3e485f3217) before this run. Producer: `fibres_probe.py`. Exact integer and sympy arithmetic for the braid keys; mpmath at 60 dps for q-lengths, with q₀ the proton pin. **6/6 checks pass.** No Q_β, CODATA or mass input.

## 1. Where the 316 word classes collapse

| stage | all 316 classes | the 90 on the shortest Bring loop |
|---|---|---|
| S1: braid, up to conjugacy in B₃ | **33** | **3** |
| S1′: Burau trace polynomial | 28 | 3 |
| S2: SL(2,ℤ) image, up to GL(2,ℤ) | 33 | 3 |
| S3: Bring loop, up to symmetry | 10 loops + "no loop" | 1 |

**Most of option 1b's 90-way tie was one braid written many ways.**
- **88** of the 90 word classes are the same braid: different positive spellings of one conjugacy class in B₃.
- The other two are different braids.
- So the Bring loop identifies three distinct braids, and the positive-word spelling multiplies one of them 88-fold.

The Burau trace polynomial is coarser than the braid class: 28 polynomials for 33 braids. Five pairs of distinct braids share a polynomial, and hence a q-length.

## 2. The energy tests (pre-registered §3)

E_q = q-length at t = −q₀, smaller first. At t = −q₀ every one of the 316 is hyperbolic, so none is excluded.

**Test A (all 316 classes): PASS.**
- The minimum is E_q = 0.1043407203195195123159062799730723970537 = ln q₀.
- It is attained by **one** braid: the conjugacy class of σ₀Δ⁴, where Δ² = (σ₀σ₁)³ is the full twist. That is σ₀ followed by two full twists, written in 55 positive spellings.
- Its image in SL(2,ℤ) is parabolic, conjugate to T = [[1,1],[0,1]]. Route 2 gives it **no loop** on Bring's surface.
- The next values are 0.5217…, 0.7304…, 1.3564… and 2.6496…, each attained by exactly one braid.

**Test B (the 90 on the shortest Bring loop, Bring loop first): PASS.**
- The minimum is E_q = 2.649587989469697311634307721571938264333.
- It is attained by one braid: the 88-spelling class.
- The other two braids give 7.1378… and 7.7007….

**Neither test selects a scored word.** These are fresh 13-letter words, not candidates. A pass says only that, unlike the Bring-loop energies, the q-length can tell braids apart.

**The two tests point in different directions.** The q-length on its own puts first a braid that has no Bring loop. Putting the Bring loop first moves to a different braid.

## 3. A bug found and fixed during this run (read this)

The first run reported **Test B: FAIL**: two braid classes, 65 and 23 word classes, tied at 2.6496….

That split was a bug in the S1 key, not in the braids. The key compared continued-fraction periods up to even shifts, as §1 says. But it did not account for the **parity of the pre-period**: each continued-fraction step is a GL(2,ℤ) map of determinant −1. Two SL(2,ℤ)-conjugate matrices could therefore receive different keys.

- **How it was caught:** reversing a braid word is an anti-automorphism of B₃, so it must send conjugacy classes to conjugacy classes. Under the buggy key it sent one class into two.
- **The fix:** start the period at the first even step. This makes the code do what §1 states (SL(2,ℤ)-conjugacy); it does not change the rule.

Independent verification of the fixed key:
- **Hyperbolic classes:** all 29 agree with Gauss's reduction cycles of the associated binary quadratic forms (proper equivalence). No class splits and no two classes merge.
- **Parabolic classes:** all 4 agree with an exact reduction to [[1,n],[0,1]].
- **Explicit conjugators:** found in SL(2,ℤ) for 267 of the 283 same-class pairs by a bounded search. The other 16 lie beyond the search bound and are covered by the two checks above.

The verdict of Test B changed with this fix. It is reported with that history rather than as a clean first-run pass.

## 4. What the two rules would say about the seen candidates (CONTAMINATED, no evidential weight)

The seen candidates' q-lengths were computed earlier, in `results_qdeformed.md`, so this is not a test. Applying the two fixed rules to the seen 11-letter words gives the following.
- **Rule A** (q-length alone) picks the parabolic braid. Its spellings are nuc11_interleaved = gluon_s0_s0 and gluon_s0_s1, with E_q = ln q₀. That is the element the dashboard currently scores.
- **Rule B** (Bring loop first) excludes it, because it has no loop. It picks class A (gluon_s1_s0 / gluon_s1_s1), which has the shorter Bring loop.

The two rules disagree. Which one, if either, is the selection principle is an owner decision. It cannot be settled by these numbers.
