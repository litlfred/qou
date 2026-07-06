**Track C Step B: Axiomatic Markov-closure map.** We reduce the open content to two atomic axioms.

Following the Track-C plan
([`rem:F3-eps6-leading-eq-neg-2b-cubed`](#rem:F3-eps6-leading-eq-neg-2b-cubed)),
the substantive open content of $c_3 = J_{\text{Hopf}}(q=1) = -2$ lives
in the 3-fold Markov closure $\to$ Hopf-link substructure
identification (Step 3 of the Track-C chain). We factorise this content into two atomic axioms.

## The two atomic axioms

1. **Markov-closure of a 2-strand 2-crossing braid is the Hopf link:**
   $$\widehat{\sigma_1^2 \in B_2} \;=\; \text{Hopf link}.$$
   This applies the Alexander-Markov closure theorem to a specific case. The content is combinatorial and topological.

2. **Classical Jones value of the Hopf link:**
   $$J_{\text{Hopf}}(q{=}1) \;=\; -2.$$
   We proved this in Lean ([`F3-eps6-leading-eq-neg-2b-cubed.lean`](F3-eps6-leading-eq-neg-2b-cubed.lean)) via `unfold + norm_num`.

## Lean encoding

The companion file [`markov-closure-map-axiomatic.lean`](markov-closure-map-axiomatic.lean) implements this structure:

- We define `class MarkovClosureMap2Strand` with explicit fields:
  - `closure : ℕ → Type` maps crossing-count $k$ to the closure type.
  - `is_hopf_at_two` enforces `closure 2 = Unit` (the Hopf link).
  - `jones_at_one : ℕ → ℝ` gives the classical-limit Jones value.
  - `jones_hopf_at_one_eq_neg_two` enforces `jones_at_one 2 = -2`.

- We define `class TrackCReducedAxiom` carrying the single axiomatic statement that $c_3$ factors through the Hopf identification.

- We prove `track_C_c_3_eq_neg_two`: under both classes, $c_3 = -2$.

## Result

Before this step, the `ThreeFoldMarkovHopfExtraction` class used a single broad axiomatic field to encode the substantive 2-strand sub-braid extraction at order 3. We split that content into two atomic axioms, each representing a known knot-theoretic result:

| Atomic axiom | Known result | Lean status |
|---|---|---|
| `closure 2 = Hopf link` | Alexander-Markov 1923/1936 | type axiom |
| `jones_at_one 2 = -2` | Jones 1985 | proved (`unfold + norm_num`) |

The eventual full Track-A formalisation constructs the explicit $\text{Braid}_n \to \text{Link}$ closure map in Lean. This targets only the first atom; the second is already closed.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, physical observables, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Generic categorical identities remain valid over an abstract coefficient ring; we specialise only their archimedean realisations.
