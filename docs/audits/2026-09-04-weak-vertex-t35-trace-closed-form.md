# The weak-vertex form factor has a closed form — and the published value is not it

**Date:** 2026-09-04 · **Bean:** `qou-egvf` (closes the one-level-down GAP left by `qou-jk6k`, PR #6631) · **Branch:** `claude/weak-vertex-t35-trace-2026-09-04`

## Claim

The weak-vertex form factor of `rem:hadron-half-life-fermi` — the canonical Markov trace of the
`T(3,5)` torus braid `(σ₀σ₁)⁵` in `H₃(q)` — is, under convention D (`h = q − q⁻¹`,
`z = q³/(q²+1)`, owner ruling R1 2026-08-15):

```
W(q) = tr_M((σ₀σ₁)⁵) = q²(q¹² + q⁸ − 1) / (q² + 1)²
```

| quantity | value |
|---|---|
| `W(q₀)`, proton pin, convention D | `1.18748061314596264610711583007920…` |
| `W(q₀)`, convention C (`z = √q/(q+1)`, **excised**; comparison only) | `0.90633830989628740115525382540208…` |
| `W(1)` | `1/4` |
| published in `obs:hadron-half-life-verification` ("computed exactly") | `≈ 0.7036` |

## Evidence

Two exact, independent routes agree (`computations/markov/weak_vertex_t35_trace.py`, 9/9
assertions, sympy-exact, mpmath at 60 dps for the numerics; witness
`computations/weak-vertex-t35-trace.witness.json`):

1. **The canonical trace on the word.** `markov_trace_canonical.tr_M_word((0,1)*5, 3, z_D, h)`
   returns `q²(q¹²+q⁸−1)/(q²+1)²` after factoring.
2. **Wedderburn.** `tr_M = Σ_λ y_λ χ_λ`. Solving the three basis values `tr(1)=1`, `tr(σ₀)=z`,
   `tr(σ₀σ₁)=z²` gives `y₍₃₎ = (q⁴+1)/(q²+1)²`, `y₍₂₁₎ = q²/(q²+1)²`, `y₍₁₁₁₎ = 0`; the same
   weights reproduce the other three basis values (`tr(σ₁)`, `tr(σ₁σ₀)`, `tr(σ₀σ₁σ₀) = hz²+z`),
   which is the check that they are right. On the `(2,1)` block `(σ₀σ₁)³ = Δ²` is the identity
   (content sum of `(2,1)` is 0), so `χ₍₂₁₎((σ₀σ₁)⁵) = χ₍₂₁₎((σ₀σ₁)²) = −1`; on the trivial block
   it is `q¹⁰`. Hence `W = y₍₃₎ q¹⁰ − y₍₂₁₎`.

`y₍₁₁₁₎ = 0` is the statement that convention D is the `SU(2)`/Temperley–Lieb trace.

**Cross-check against a published invariant.** `T(3,5)` is `10₁₂₄`, `V(t) = t⁴ + t⁶ − t¹⁰`. The
numerator `q²(q¹²+q⁸−1)` equals `q²²·V(q⁻²)` — the writhe/mirror normalisation of the Ocneanu
trace of a positive three-strand braid. This is an identity of Laurent polynomials independent of
the Wedderburn route.

**Lean** (sorry-free, `lean`-direct exit 0, axioms `propext, Classical.choice, Quot.sound` only):
[`QOU/Braiding/WeakVertexT35TraceClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/Braiding/WeakVertexT35TraceClosedForm.lean),
over a generic field `K` (§7c): the seminormal `(2,1)` matrices with their Hecke and braid
relations, `(σ₀σ₁)³ = 1` on that block, `χ₍₂₁₎((σ₀σ₁)⁵) = −1`, the six Ocneanu basis values of the
Wedderburn functional, `weakVertexTrace_eq`, the Jones identity, `W(1) = 1/4`, and the numerical
envelope `1.187 < W(q₀) < 1.188`. The one step the reader supplies is standard and stated in the
header: a linear functional on the six-dimensional `H₃(q)` is determined by its values on the six
reduced words, so the functional built here *is* `tr_M`.

## The finding: `0.7036` is reproduced by neither convention

`obs:hadron-half-life-verification.md` §"T_{3,5} weak vertex" states *"We compute the vertex form
factor exactly: `𝒲(q) = tr_Markov((σ₁σ₂)⁵) ≈ 0.7036` at `q = q₀`"* and reads off *"an 11 %
reduction in transition amplitude"*. Measured this session: convention D gives `1.1875`,
convention C gives `0.9063`. The number's source is the deprecated convention-C
`hecke_division` pipeline — `fsh-guts/deprecated/computations/t35-full-calculation.py` builds
`(σ₃σ₄)⁵` on five strands and calls `div.markov_trace(·, 5)`. **Its `0.7036` was not reproduced
this session**: the surface searched was that script's construction and the two conventions of
the Ocneanu trace of `(σ₀σ₁)⁵`; a different Hecke normalisation inside `hecke_division` (e.g. the
unbalanced `(σ−q)(σ+1)=0`) would separate the hypotheses and was not run.

Consequences in paper terms: the form factor is **> 1** at the substrate, not an 11 % reduction,
and the "resolves the 10–17 % overshoot" sentence in `rem:hadron-half-life-fermi` item 2 rests on
the old number. `prop:hadron-half-life`'s Lean (`BetaRateData.W2`) is unaffected — it carries
`W²` as positive data with no value.

## Decision for the owner — the content blocks

**What is being decided.** Whether to replace the published `0.7036` and the "11 % reduction"
reading with the derived closed form and its value, and whether to close item 2 of the Fermi
remark's "Open computations". Nothing in this PR edits either block.

**Default if nothing is said.** The Lean, the producer and this note land; both content blocks keep
their current text; the discrepancy stays recorded here and in bean `qou-egvf`.

**Option 1 — replace the value and the reading in `obs:hadron-half-life-verification`, close item 2
in `rem:hadron-half-life-fermi`.**
- *Means:* the verification block states `W(q₀) ≈ 1.187` from the closed form, the Fermi remark's
  item 2 becomes "settled: `W(q) = q²(q¹²+q⁸−1)/(q²+1)²`", both pointing at the Lean and witness.
- *Costs:* two `.md` edits, two sidecar refreshes, one dated author note each; no compute re-run.
- *Risks:* the block's "11 % reduction" narrative and any downstream half-life figure that used
  `0.7036` (the MAE `4.5 %` table in the same block was produced by the same deprecated pipeline)
  become internally inconsistent unless re-derived; that re-derivation is a separate, larger job.
- *Commits to:* the D-frame value as the published one; the deprecated-pipeline half-life table
  needs its own re-run before the block is coherent again.

**Option 2 — replace the value, keep item 2 open with a pointer.**
- *Means:* the verification block gets the corrected value; the Fermi remark keeps item 2 "open"
  but cites the closed form as the candidate.
- *Costs / risks / commits:* as option 1 minus the Fermi edit; leaves an "open" label on a settled
  computation, which the corpus-grep discipline treats as a defect.

**Option 3 — do nothing to content now (the default).**
- *Means:* both blocks stay as they are; the corpus carries a proved closed form beside a published
  number that contradicts it.
- *Costs:* none now; *risks:* the next reader of the verification block takes `0.7036` as current.

**Recommendation (judgement, not a finding):** option 1, but as its own tranche after this one
merges, because the verification block's half-life table has to be re-derived in the same edit for
the block to be coherent, and that is a producer re-run, not a wording change.

## Provenance

- `computations/markov/weak_vertex_t35_trace.py` → `computations/weak-vertex-t35-trace.witness.json`
  (proton pin, `q0Value` stamped; convention D; the C number is a labelled comparison).
- Lean: `QOU.Braiding.WeakVertexT35.*`, verified `lean`-direct against the paper's olean tree.

---

## CORRECTION (2026-09-05, bean `qou-ix74`) — the provenance of `0.7036` was mis-attributed above

§"The published value" says the number's source is the **deprecated** convention-C
pipeline `fsh-guts/deprecated/computations/t35-full-calculation.py`. **That was wrong, and it
was a guess from file names rather than a measurement.** The number is reproduced by
the **live** engine `computations/hecke/hecke_division.py`: its former `_trace_word`
applied only the Markov rotation `tr(x·σ_top) = z·tr(x)` and never the Hecke relation,
which collapses to `Σ_w c_w z^{|w|}` over the (correctly) reduced word. Measured on the
reducer's own output for `(σ₀σ₁)⁵`:

| Markov parameter | `Σ c_w z^{|w|}` | where it was published |
|---|---|---|
| `z_C = √q/(q+1)` | **0.70355** | `ex:hadron-half-life-verification` ("≈ 0.7036") |
| `z_D = q³/(q²+1)` | **0.96844** | `computations/t35-weak-vertex.witness.json` (2026-08-29) |

So both stale values are one defect at two parameters, and the "(σ₃σ₄)⁵ on 5 strands"
detail was irrelevant. The engine is fixed (it now delegates to
`markov_trace_canonical.tr_M_word`), `t35-weak-vertex.witness.json` now carries
`1.18748`, and the identification is asserted in
`computations/weak-vertex-substitution-scale.witness.json`. Full record:
[`2026-09-05-weak-vertex-substitution-scale-and-engine-defect.md`](2026-09-05-weak-vertex-substitution-scale-and-engine-defect.md).

**Where the wrong attribution was repeated** (all corrected in the same tranche, except the
immutable PR bodies): the header of `WeakVertexT35TraceClosedForm.lean`, the docstring and
`published_value_finding.provenance` of `weak_vertex_t35_trace.py` and its witness, the status
author note on `ex:hadron-half-life-verification` (#6689), beans `qou-egvf` / `qou-4x7c`, and
the bodies of PRs #6664 and #6689.
