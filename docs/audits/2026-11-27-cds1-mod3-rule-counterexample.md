# The six-strand "multiple of 3" rule fails at ten vertices (bean `qou-cds1`)

Date: 2026-11-27. Follows [`2026-11-27-cds1-six-strand-neutral-selection.md`](2026-11-27-cds1-six-strand-neutral-selection.md), finding 1.
Probe: [`six_strand_mod3_counterexample_probe.py`](../../computations/probes/gg_six_strand/six_strand_mod3_counterexample_probe.py),
witness `six-strand-mod3-counterexample.witness.json` (exact `Fraction` evaluation plus rational
interpolation; no float arithmetic). Scope: the counterexample is exact; the length-≤ 9 statements
are exhaustive enumerations, scope (a).

## Question

The neutral-selection audit measured, for V-words of at most six vertices on six strands
(`V_i = σ_iσ_{i+1}⁻¹`, `i = 0..3`), that every linking-neutral word passing reading 3 uses each
`V_i` a multiple of 3 times. The task was to prove this at every length by a ℤ/3-type invariant.

## Result

**The rule is false.** The ten-vertex word

    W = (V₀V₂)⁵        (vertex counts 5, 0, 5, 0; twenty crossings)

is a pure braid, is linking-neutral (all ten pairwise signed crossing counts are 0, checked by the
probe's `neutral` and by an independent strand count), and passes reading 3 at q₀, 11/10 and 23/20.
Its mirror `(V₁V₃)⁵` behaves identically. The two-row characters, exact Laurent polynomials in q:

| λ | χ_λ(W) at q = 1 | first sign change above q = 1 |
|---|---|---|
| (6) | 1 | none (χ ≡ 1) |
| (5,1) | 5 | in [5659/4168, 5492/4045] ≈ 1.3577 |
| (4,2) | 9 | in [7889/5772, 436/319] ≈ 1.3668 |
| (3,3) | 5 | in [3138/2215, 3121/2203] ≈ 1.4167 |

So all four characters are positive on the whole interval `1 ≤ q < 1.3577`, which contains q₀
and both robustness points. The counterexample does not depend on the q₀ pin.

`χ_(5,1)(W) = −2q¹⁰ + 15q⁸ − 70q⁶ + 195q⁴ − 340q² + 409 − 340q⁻² + 195q⁻⁴ − 70q⁻⁶ + 15q⁻⁸ − 2q⁻¹⁰`;
the other two are in the witness.

At ten vertices there are **64** distinct (freely reduced) pure neutral V-words with some count
not divisible by 3, with counts `(5,0,5,0)`, `(0,5,0,5)` and `(3,2,2,3)`. **All 64 pass reading 3**
at all three q values.

## Why no ℤ/3 invariant can exist

At `q = 1` the Hecke algebra is the group algebra of S₆, and a pure braid maps to the identity, so
`χ_λ(w)|_{q=1} = dim λ > 0` for every pure word `w`. By continuity **every pure word passes
reading 3 on some interval `1 ≤ q < q*(w)`**, and it fails at q₀ only when `q*(w) < q₀`. Reading 3
at q₀ is therefore a condition on the permutation together with a q-dependent threshold, not on
vertex counts mod 3. Any count-only invariant would have to exclude `(V₀V₂)⁵`, which reading 3 keeps.

## What is true at short length (enumerated, scope (a))

The mod-3 pattern seen at length ≤ 6 splits into two separate facts:

1. **Reading 3 at q₀ kept only pure words.** In the original witness, the 58 survivors are exactly
   the 58 pure neutral words; every non-pure neutral word fails (1820 with a bad count, 28 with all
   counts ≡ 0 mod 3). Lengths 7–9: see the table below.
2. **Pure + neutral forces counts ≡ 0 mod 3 up to nine vertices, and not at ten.** Exhaustive over
   all `4^k` V-index sequences:

| vertices k | pure words with a count ≢ 0 mod 3 | of those, neutral |
|---|---|---|
| 1–3 | 0 | 0 |
| 4 | 6 | 0 |
| 5 | 0 | 0 |
| 6 | 6 | 0 |
| 7 | 168 | 0 |
| 8 | 250 | 0 |
| 9 | 594 | 0 |
| 10 | 6814 | **64** (all pass reading 3) |

Purity alone does not force the pattern even at k = 4 (`(V₀V₁)²` is pure, counts 2, 2); neutrality
is what removes those. There is a ℤ/3 shadow on two adjacent vertices only: `V_i, V_{i+1}` map to
3-cycles generating A₄, whose quotient A₄ → ℤ/3 gives `n_i ≡ n_{i+1} (mod 3)` for pure words in those
two letters. On three or more strand-triples the 3-cycles generate A₅ or A₆, which are simple and
have no ℤ/3 quotient; `(V₀V₂)⁵` uses exactly that (`(0 1 2)(2 3 4)` has order 5).

Reading-3 check of non-pure neutral words with a bad count at lengths 7–9: k = 7, none of 4848
pass at q₀; k = 8, none of 16 422 pass at q₀. k = 9 was still running when this PR was queued; its
result goes in a follow-up.

## Consequences

- Finding 1 of the neutral-selection audit holds as measured (length ≤ 6) but does not extend.
  The "nucleon core = V³" reading of that audit should not be generalised to "every survivor is a
  product of cubes": `(V₀V₂)⁵` and the 60 `(3,2,2,3)` words are survivors that are not.
- The right next target is the purity statement (reading 3 at q₀ ⇒ pure), which the data supports
  through the measured lengths, together with an honest description of `q*(w)` for pure words.
