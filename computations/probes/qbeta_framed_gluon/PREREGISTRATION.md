# Pre-registration: framed gluon loops inside γγ words (issue #8833, front 1)

Written and committed before the Lean file and the probe are run.

## Why

Owner, 2026-11-21: *"GammaGamma should be able to make it (it just might not be standalone/unstable
if isolated)"*, about a gluon that is an unknot shifted up in q (a framed unknot). A γγ word has
total writhe 0 (`writhe_eq_zero`), but the total splits into the self-crossings of each closure
component plus the crossings between components. So one component, the gluon loop, can carry a
framing of its own, balanced by its crossings with the quark components. It cannot exist as a
framed unknot by itself (that word would have writhe ≠ 0), only inside a larger word.

An unpreregistered quick scan (2026-11-21, recorded in the thread, nothing committed) found 50
such words with gluon framing ±1 or ±2 in the existing 4/5-strand family plus 6 strands up to 4
extra vertices, F ∈ [−0.17, 1.113]. This registration extends the family to larger framings and
asks a single question.

## Inputs (rulings, none chosen here)

* γγ rule: words are products of V_i = σ_iσ_{i+1}⁻¹.
* Nucleon word V₀³ on quark strands 0–2; D1 sectors on the quark strands.
* Normalisation as derived in `qbeta_lepton_normalisation` (N1–N3): unobserved strands summed,
  divide by [2]^c, framing correction q^{−2·writhe} with the whole-word writhe (= 0 here). The
  gluon's own framing is therefore **not** removed; it stays inside the trace.
* Confinement: reading 3, whole word, reported as a filter.

## The closed family

W = X · V₀³ on n strands, strands 3.. are gluon strands, X every product of 1..L vertices from
{V₀, …, V_{n−2}} that touches a gluon strand and maps {0,1,2} to itself. L = 8 (n = 4),
L = 7 (n = 5), L = 5 (n = 6). Fixed here for compute cost; traces are unbounded in length.

## Value

Gluon framing f(W) = signed sum of self-crossings over the closure components made of gluon
strands. F(W) = ε_flav(W)/ε_flav(V₀³), compared with F_required = 2.40397.

## Question and reporting

Q: does max |F| over words with |f| = k grow with k? Reported per k: number of words, F range,
range over reading-3 survivors, and the number of words with |F| ≥ F_required. No word is
selected by closeness to F_required, and no framing is chosen.

## Lean first

`QOU/QBeta/FramedGluonWrithe.lean`: for a γγ word and any labelling of its crossings as
self / between components, the self part of the writhe is minus the between part. That is the
statement that a framed component inside a γγ word must be balanced by its linking.
