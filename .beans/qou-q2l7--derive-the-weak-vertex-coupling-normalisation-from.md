---
# qou-q2l7
title: Derive the weak-vertex coupling normalisation from the Jones-Markov relation
status: completed
type: task
priority: high
created_at: 2026-09-05T07:21:24Z
updated_at: 2026-09-05T07:52:20Z
---

## Result — the normalisation is the Jones–Markov relation, and it is DERIVED

`qou-pfh7` (#6735) excluded the family `c·(W − W(1))·bridge` and left the
normalisation open. It is not a constant to be found: it is the framing-and-rank
factor of the Jones–Markov relation.

**The rule.** For `β ∈ B_n` with exponent sum `e`,
`tr_M(closure β) = q^{2e}·V(q^{−2})/[2]_q^{n−1}` — framing `q^{2e}` (writhe
correction in `t = q^{−2}`) and rank `[2]_q^{n−1}` (`tr_M 1 = 1` on `H_n`), both
read off the braid word. Verified against `markov_trace_canonical` (convention D)
on **eight** torus knots at `n = 2,3,4,5`, incl. the mirror pairs T(3,4)/T(4,3)
and T(3,5)/T(5,3). For the weak vertex (`n = 3`, `e = 10`):
`W·[2]_q² = q¹² + q⁸ − 1 = q²⁰·J`, `J := V_{T(3,5)}(q^{−2})`.

**Why the free constant is gone.** `V_K(1) = 1` and `V′_K(1) = 0` for every knot,
so `J − 1` is the canonically-normalised deviation — offset and vanishing order
are topological. `W − W(1)` failed because `W(1) = 1/4` is the Markov rank factor
`[2]_1² = 4` showing through, i.e. a normalisation artefact, not an invariant.

**The coupling is a product of two q-differences.** `J − 1 = −h₄h₆/q¹⁰` exactly,
`h_k := q^k − q^{−k}`; exponents 4 and 6 are the Jones exponents of T(3,5),
`q^{−10}` the framing. `h_k′(1) = 2k`, so second-order vanishing is a
*consequence* of two q-differences (not something a bridge arranges), leading
coefficient `−(2·4)(2·6) = −96`, `J″(1) = −192`. The rate's own coupling is the
same shape at half scale: `s² = h_{1/2}²`, leading coefficient 1.

**The ratio, exactly — no limit, no derivative.** With `G_n(q) = 1+q+⋯+q^{n−1}`:
`q²⁰(J−1) = −(q⁸−1)(q¹²−1) = −(q−1)²G₈G₁₂` and `q·s² = (q−1)²`, so
`(J−1)/s² = −G₈(q)G₁₂(q)/q¹⁹` — `−96` at `q=1` (`= −8·12`), `−39.9856` at 11/10,
`−37.0915` at `q₀`, `−5.7214` at 3/2, `−1.9917` at 2. Order, leading coefficient
AND running come off one rational function; the whole Lean stays over a generic
field, so the earlier `hasDerivAt` route was never necessary.

## What it settles

- The **order** of `qou-ix74`'s `1.19e4` substitution factor:
  `96² < |W(q₀)|²/s(q₀)⁴ < 2·96²`, machine-checked both ways. Good to a factor
  of two and **no better** — the upper bound is the honest limit, not decoration.
- **No rescaling constant exists, and now we know why**: `couplingRatio` is a
  non-constant rational function; the framing `q^{−19}` and the larger exponents
  suppress it. That explains `qou-pfh7` rather than repairing it.

## Honest limit — read before citing

`s² = h_{1/2}²` is a **formal half-scale analogue, not a Jones deviation**: its
exponents are `½`, and a Jones exponent is an integer, so no knot's `V − 1`
equals `s²`. The shape match is exact; the *identification* is not, and nothing
here supplies one. The `qou-ix74` negative stands.

## Still open (the live remainder)

Whether the β-decay rate's `s²` *should* be the half-scale q-difference at all —
i.e. whether the rate formula's construction picks out a specific exponent pair
the way the trace's does. That is a question about the **rate's** derivation, not
the trace's. The three untested shapes from `qou-pfh7` are unaffected: a ratio
against another trace, a bar-parity component, a Jones-normalised object of a
different knot.

## Artefacts

- Producer `computations/markov/weak_vertex_jones_markov_normalisation.py` — 13/13
- Witness `computations/weak-vertex-jones-markov-normalisation.witness.json`
- Lean `QOU/Braiding/WeakVertexJonesMarkov.lean` (generic, 14 decls) +
  `WeakVertexJonesMarkovArchimedean.lean` (ℝ, 2 anchor envelopes) — split per
  §7c; `lean`-direct exit 0, `#print axioms` clean on all 16, zero `sorry`
- Audit `docs/audits/2026-09-05-weak-vertex-jones-markov-derivation.md`
- PR #6765

## Carried forward

The §7c MIXED flag is still latent in `WeakVertexT35TraceClosedForm.lean`
(`weakVertexTrace_near_q0`) and `WeakVertexSubstitutionScale.lean` (the two
`substitutionRateFactor` envelopes) — `check-sidecars.sh` only inspects *changed*
files. Mechanical split, no mathematical content; deliberately not done here.
Also on `qou-pfh7`.
