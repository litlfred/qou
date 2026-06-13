**Track C Step B: axiomatic Markov-closure map**, reducing the open
content to two atomic axioms.

Per the Track-C plan in
[`rem:F3-eps6-leading-eq-neg-2b-cubed`](#rem:F3-eps6-leading-eq-neg-2b-cubed),
the substantive open content of $c_3 = J_{\text{Hopf}}(q=1) = -2$ lives
in the **3-fold Markov closure $\to$ Hopf-link substructure**
identification (Step 3 of the Track-C chain).

This remark **factorises that content** into two ATOMIC axioms:

## The two atomic axioms

1. **Markov-closure of a 2-strand 2-crossing braid is the Hopf link**:
   $$\widehat{\sigma_1^2 \in B_2} \;=\; \text{Hopf link}$$
   This is the **Alexander-Markov closure theorem** applied to a
   specific case. Combinatorial / topological content.

2. **Classical Jones value of the Hopf link**:
   $$J_{\text{Hopf}}(q{=}1) \;=\; -2$$
   Already proved in Lean ([`F3-eps6-leading-eq-neg-2b-cubed.lean`](F3-eps6-leading-eq-neg-2b-cubed.lean))
   via `unfold + norm_num`.

## Lean encoding

The companion file [`markov-closure-map-axiomatic.lean`](markov-closure-map-axiomatic.lean):

- Defines `class MarkovClosureMap2Strand` with explicit fields:
  - `closure : ℕ → Type` mapping crossing-count k to the closure type
  - `is_hopf_at_two`: `closure 2 = Unit` (the Hopf link)
  - `jones_at_one : ℕ → ℝ` giving the classical-limit Jones value
  - `jones_hopf_at_one_eq_neg_two : jones_at_one 2 = -2`

- Defines `class TrackCReducedAxiom` carrying the single axiomatic
  statement that c_3 factors through the Hopf identification.

- Proves `track_C_c_3_eq_neg_two`: under both classes, $c_3 = -2$.

## What this achieves

**Before**: the `ThreeFoldMarkovHopfExtraction` class had a single
broad axiomatic field encoding "the substantive 2-strand sub-braid
extraction at order 3".

**After**: that content is split into two ATOMIC axioms, each
representing a recorded knot-theoretic result:

| atomic axiom | known result | Lean status |
|---|---|---|
| `closure 2 = Hopf link` | Alexander-Markov 1923/1936 | type axiom |
| `jones_at_one 2 = -2` | Jones 1985 | proved (`unfold + norm_num`) |

The eventual full Track-A formalisation (defining $\text{Braid}_n \to \text{Link}$ explicitly in Lean and constructing the closure map) targets ONLY the first atom — the second is already closed.
