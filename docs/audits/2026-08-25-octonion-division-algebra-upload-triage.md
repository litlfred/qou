# Triage of the eight division-algebra uploads — and the SU(5) question

**Date:** 2026-08-25
**Trigger:** owner upload `21ae4db28` (8 PDFs), with the note *"we are maybe
missing SU(5) in qou... one of the papers describes the SU(5) gauge group and
its subgroup SU(3)C × SU(2)L × U(1)"*.
**Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5764)
**Method:** ingested to `library/`, then four independent reviewer agents, one
per paper cluster, each run against the eightfold §8 open-problem ledger.

---

## 0. Answer to the owner's question, first

**The instinct is right, and the paper is not the thing that fills it.**

Grand-unification `SU(5)` is genuinely near-absent from `content/`: three hits,
all bibliographic (`references.ts`, `bib-qa-verifications.json`). That is a real
gap.

But **`arxiv-1205.4617v1` does not close it.** It is a notational relabelling of
the textbook Georgi–Glashow construction: `SU(3)` is an *input* at its first
line, the octonion substitution is deferred to a prior paper by citation, and
the paper's own culminating gauge field (eq. 26) **contains no octonions at
all** — they drop out before the answer. Its central correspondence maps eight
`su(3)` generators onto seven octonion imaginaries by reusing `e₃`, which is not
injective and not a Lie-algebra map.

**The better source is already in the corpus.** Baez–Huerta,
*The Algebra of Grand Unified Theories* (arXiv:0904.1556) — the paper that
actually does `SU(5) ⊃ SU(3)×SU(2)×U(1)` with hypercharge from the `ΛC⁵`
grading — is ingested at `library/arxiv-0904.1556v2/`, registered as
`baez-huerta2010`, claim-verified in the source ledger, analysed in
[`2026-07-31-sm-lit-analysis-bean-workplan.md` §3](2026-07-31-sm-lit-analysis-bean-workplan.md),
and already cited by three content blocks. Anything wanted about GUT `SU(5)`
should be taken from there.

**One hazard worth naming.** A future agent grepping `SU(5)` will land on
[`2026-08-16-su-r-level-tower-gap-map.md`](2026-08-16-su-r-level-tower-gap-map.md)
line 46, `| 5 | 0.322749… | SU(5) | ≤5 |`. That is the **Wenzl level `r = 5`**,
`z₅ = q⁵/[5]_q` — level-rank data, with no relation to the grand-unification
group. The two senses share only the glyph.

## 1. What was ingested

`uploads/` is the staging area; `library/<doc-id>/` is the greppable corpus and
is **corpus-grep path 5**. All 26 PDFs in `uploads/` were un-ingested; these 7
are now done, the other 19 are not.

**7 distinct documents, not 8** — `1107.1559.pdf` and `1107.1559v1.pdf` share
`doc_id arxiv-1107.1559v1` (same v1 source, re-`dvips`ed in 2018; not
byte-identical, both kept).

## 2. Verdicts

| Document | Verdict | One-line reason |
|---|---|---|
| `arxiv-2403.00360v2` Causal Fermion Systems and Octonions | **cite-worthy, §2.3 only** | The cleanest complete definition of `𝕆`, `Aut(𝕆) = G₂`, and the `ℂ⊕ℂ³` splitting; §2 is authorially self-contained and free of causal-fermion-system commitments |
| `arxiv-2202.06733v1` SU(3) and Octonions in Geometric Algebra | **cite-worthy, narrowly** | Table 2 is an explicit `8×8` table in the **Baez convention — the same one the corpus's own `octMul` uses** — plus the caveat that 480 tables are compatible with `e₀ = 1` |
| `arxiv-2306.13098v2` Three generations from CD sedenions | **cite-worthy, narrowly** | Only source in the library giving a *mechanism* rather than an observation for the count three: `Aut(𝕊) = G₂ × S₃` (Brown), colour and family as clean direct factors |
| `arxiv-1205.4619v1` Quaternion-Octonion Casimirs | **context-only, borderline not-relevant** | Casimir content is textbook and carries nothing octonion-specific; self-reports redundancy with its own companions |
| `arxiv-1205.4617v1` QO Reformulation of GUTs | **not relevant** | §0 above |
| `arxiv-1107.1559v1` QO SU(3) Flavor Symmetry | **not relevant** | Relabels Gell-Mann matrices; **`λ₈ ∝ λ₃` collapses the Cartan to rank 1**, destroying `A₂` |
| `eps-hep2019-615` Sedenions, Cℓ(8), three generations | **not relevant** | Reviews a model its own author has since replaced; defines `𝕊` with "seven" imaginary units (should be fifteen) |

All four Pushpa–Bisht–Li–Negi / proceedings items are `physics.gen-ph`.

## 3. The one live defect the triage found — and it was ours, not the papers'

The corpus names **"the Günaydin–Gürsey decomposition"** as the source of its
colour-`SU(3)` picture in at least seven places — `color-su3-from-g2.md`,
`schur-weyl-eightfold.md`, `sm-colour-stabilizer-action.md`,
`OctonionSU3Stabilizer.lean`, `OctonionSU3BracketClosure.lean`,
`ColourComplexStructure.lean`, and a 2026-07 audit — and had **no bibliography
entry for it**. `color-su3-from-g2.ts` had no `cites` field at all, and
`OctonionSU3Stabilizer.lean:52` backed the claim with
`-- Ref: [manuscript] docs/audits/…`, a pointer at the corpus's own audit doc.
Under AGENTS.md §1, `[manuscript]` is licensed only when no published reference
exists. One does.

This is load-bearing, not decorative: the decomposition is what makes the
octonionic `3` **complex type rather than self-dual**, and non-self-duality is
precisely the input the `Sym²` gate consumes. A self-dual `3` carries a singlet
in `Sym²` and fails.

**Fixed in this pass:** `gunaydin-gursey1973` added to `references.ts` and wired
into all three sites.

**Metadata provenance, stated because it is not fully verified.** No DOI is
recorded: `api.crossref.org` is blocked by the sandbox proxy (403), so the DOI
could not be checked against a primary source and was **omitted rather than
written from memory**. Volume/issue/pages are corroborated by three independent
in-repo bibliographies that cite the work — `arxiv-2306.13098v2` ref [7],
`arxiv-2202.06733v1` ref [69], `arxiv-1205.4619v1` ref [7]. 432 of the 777
entries carry no DOI, so this is within convention.

## 4. What did NOT move

- **§8 item 1 (`N = 3`)** — untouched. No paper constructs a 3-dimensional
  object; the two that discuss `SU(3)` assume it. The sedenion route delivers
  **colour**, which the corpus already has.
- **§8 item 3 (`S⁶ = G₂/SU(3)`)** — untouched. No paper in the batch states the
  coset; `2403.00360` supplies the stabilizer but never the transitivity that
  would give it.
- **§8 item 4 (flavour vs colour)** — untouched, and `arxiv-1107.1559v1` is a
  worked instance of the conflation the item warns against: its title says
  flavour and its conclusion says strong interactions.
- **§8 item 6 (three generations)** — still open. `2306.13098v2` is the most
  interesting near-miss in the batch and §5 records why it is a near-miss.
- **The "`𝕆` is never defined" ledger row** — **re-scoped, not closed.** The
  reviewers established this is an **exposition** gap (no `definition` content
  block), not a citation or mathematical gap: `baez2002` is already registered
  and cited, and `QOU/MathlibExt/` carries ten `Octonion*.lean` files including
  a concrete `octMul` with a machine-checked complex structure. No external
  paper can close it.

## 5. Why `2306.13098v2`'s three generations is a near-miss, not a closure

Recorded because the result is attractive and the failure modes are not obvious.

The count three is `|⟨ψ⟩|` for an order-3 element of the `S₃` factor of
`Aut(𝕊) = G₂ × S₃` (Brown 1967) — a theorem, and genuinely stronger than
"sedenions happen to admit three octonion copies". But:

1. **The tower does not terminate.** Brown gives an extra `S₃` at each of
   `n = 4,5,6`, so the same construction at the 32-ions gives `ℤ₃ × ℤ₃`, i.e. up
   to nine families. The paper's defence is *"it therefore seems unlikely that
   CD algebras beyond `A₄ = 𝕊` will provide additional physical insight"*.
2. **Rank 2 dressed as three.** `ψ² + ψ + 1 = 0`, and the down-type quark states
   satisfy `A_i + B_i + C_i = 0` exactly. The three "generations" are three
   vectors at 120° in a plane.
3. **Only one of the three gets the right electric charges**, by the paper's own
   statement.

And a trap for anyone tempted to harvest the `⟨ψ⟩`-orbit as the missing
3-dimensional object: it fails twice. As an `S₃` representation the relation
`ψ² + ψ + 1 = 0` makes it the **2-dimensional standard representation**, not a
3-dimensional permutation representation; and at dimension 2 it is
real/orthogonal, so `Sym²` carries the invariant form — the gate's fail
condition. Consistent with `Sym2GateMultiplicity.lean`; not a counterexample to
it.

## 6. Provenance

Reviews were produced by four independent agents, each given the §8 ledger and
the corpus-grep discipline, each instructed to report a weak paper as weak.
Their central factual claims were re-verified in the main session before
anything was written here — the Baez–Huerta presence, the Günaydin–Gürsey
absence from `references.ts`, the uncited assertion at
`color-su3-from-g2.md:178`, the `[manuscript]` self-Ref, and the sedenion
novelty grep. One agent's "zero hits" for sedenion/Cayley–Dickson was scoped to
`docs/ content/ computations/` and missed `.beans/qou-60vx`, a *completed* bean
recording that PR #3671's octonion→`G₂` Cayley–Dickson infrastructure was closed
unmerged in favour of the focused follow-ons #3860 and #3948. That does not
change any verdict here, and is noted because a narrower grep than the
discipline prescribes is exactly the failure the discipline exists to catch.
