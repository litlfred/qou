# Milnor = leading-Vassiliev bridge — formalization roadmap + citation due-diligence

Tracks bean `qou-q64u` (under epic `qou-pddf`). This is the analysis/design layer
for the bridge that would close `MilnorExactOrderConjecture` (#4471, bean `qou-ovxx`).
It is deliberately NON-Lean here — the Lean scaffold is owned by the
`claude/vassiliev-finite-type-infra-2026-08-01` agent branch; this doc is the
roadmap + the "not all papers are fully accurate" hypothesis-verification it consumes.

## The claim to formalize
For the length-`A` iterated-commutator Brunnian generator `w_A` (an `A`-component
Brunnian link), the trace-deficit `D_A(h) = 1 − τ(closure(w_A))` at `h = q − q⁻¹`
has leading order **exactly** `2(A−1)` with **nonzero** leading coefficient equal
to `±μ̄(12…A) = ±1` (the length-`A` Milnor invariant). #4471 proved the LOWER
bound `order(D_A) ≥ 2(A−1)`; the OPEN piece is the nonzero leading coefficient.

## Layered lemma chain (what the scaffold must reach)
1. **Chord diagrams / 4T / weight systems / finite-type def** — the scaffold agent.
2. **Jones-polynomial Vassiliev expansion** (Bar-Natan): the coefficient of `hᵐ`
   in `V_L(e^h)` is a finite-type invariant of degree `m`.
3. **Milnor = tree-level Kontsevich** (Habegger–Masbaum 2000): for string links the
   length-`k` Milnor invariant `μ̄` is the first non-vanishing finite-type invariant,
   recovered from the tree part of the Kontsevich integral.
4. **Brunnian ⇒ first μ̄ at length A** (Milnor): all proper sub-links of `w_A` are
   trivial ⇒ every `μ̄` of length `< A` vanishes; the length-`A` `μ̄(12…A) = ±1`
   for the iterated-commutator generator.
5. **Assemble**: (2)+(3)+(4) ⇒ the degree-`(A−1)` finite-type part is the first
   non-vanishing one and equals `±μ̄ = ±1` ⇒ nonzero leading coefficient.

## ⚠ Citation due-diligence — DO NOT trust the papers blind (the flagged risk)
Two hypotheses must be checked against OUR construction before the cited theorems
can be invoked; both are genuine open verification items, not mechanical:

- **DD-1 (the factor-of-2 grading).** Standard Vassiliev theory puts a degree-`m`
  invariant at order `hᵐ`. Naively that predicts leading order `(A−1)`, but #4471
  derives `2(A−1)` (one `h²` per nested commutator, `A−1` levels, from the Hecke
  relation `σ² = (q−q⁻¹)σ + 1`). The bridge is only valid once the precise relation
  between our `h = q−q⁻¹` grading (Markov-trace deficit) and the standard Vassiliev
  degree is pinned. Candidate resolution: the deficit pairs the tree with its mirror
  (a `|·|²`/bar-symmetric object), doubling the degree — but this must be PROVED, not
  assumed. If it fails, the "bridge" as literally cited does NOT apply as-is.
- **DD-2 (string-link vs closed-link normalisation).** Habegger–Masbaum is stated
  for STRING LINKS (μ̄ well-defined, no indeterminacy). Our object is the Markov
  CLOSURE of a braid word. Verify the closure does not introduce μ̄ indeterminacy at
  length `A` (it should not, since sub-links are trivial ⇒ lower μ̄ vanish ⇒ the
  length-`A` μ̄ is well-defined even for the closed link — but this is exactly the
  kind of "boundary hypothesis" that a physics/geometry citation glosses and must be
  re-checked in Lean).

## Honest status
- `qou-q64u`: OPEN. The bridge is a valid INTERIM citation-justification for the
  conjecture class; it is NOT axiomatized (§"Axiomatization is NOT a Proof").
- Even a full scaffold + (2)+(4) does not close it without DD-1 resolved — DD-1 is
  the real crux and may itself be an honest sub-wall.
- Route parallel to `qou-ovxx` route B (inductive leading-coefficient): B attacks the
  coefficient directly via the trace algebra; this bridge attacks it via topology.
  Two independent routes to the same nonvanishing — either landing closes it.
