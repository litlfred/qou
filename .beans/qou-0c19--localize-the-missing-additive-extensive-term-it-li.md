---
# qou-0c19
title: 'LOCALIZE the missing additive extensive term: it lives in the inter-nucleon COLOR-TUBE channel (conj:inter-nucleon-channel-color-tube). Diagnostic: per-isotope error ∝ inter-nucleon arc count R²=0.83 (vs signed-h R²=0.26) = the extensive ∝A signature. Missing structure = color-tube weight W_{c1c2}. OPEN Q: does color-tube weighting saturate at A=4 (magic-shell) giving ρ_4? Conditional on conj:s5-so3-fiber-action.'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T15:55:10Z
updated_at: 2026-08-02T19:10:41Z
---


---
**Update 2026-08-30 (session arc-count-degeneracy, PR pending) — 🛑 THE TITLE'S
EVIDENCE DOES NOT SURVIVE READING ITS OWN SOURCE. Re-scope before acting.**

Scope (a). Nothing refuted, nothing wired. This bean had a title and no body;
the title's diagnostic was its whole content, so this is most of it.

**The citation does not match the witness.** The title asserts *"per-isotope
error ∝ inter-nucleon arc count R²=0.83 (vs signed-h R²=0.26) = the extensive
∝A signature"*. The same sentence is in
`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`
§4 and in `brings-surface/inter-nucleon-channel-color-tube.md:34`, which names
the source: `computations/low-isotope-sign-flip-diagnostic.witness.json`.

Read it. The string `0.83` occurs **zero** times. What it records:

| | quoted | actually in the witness |
|---|---|---|
| err_pct ~ n_inter (arc count) | 0.83 | **0.26529448…** |
| err_pct ~ signed_h            | 0.26 | **0.00175532…** |
| sample                        | —    | **n = 5**, two are A=1 anchors at \|err_pct\| < 1e-3 |
| its own verdict               | "localizes it" | **"WEAK correlation … sign-flips are NOT explained by simple linear channel models"** |

So the durable artifacts cite a witness for a number it does not contain, in
support of a conclusion its own recorded verdict contradicts, on three
informative points. Note the quoted `0.26` for SIGNED-H is, to three digits, the
witness's ARC-COUNT value.

**And the claim as written is degenerate anyway.** Read as "the extensive ∝A
signature" — an ABSOLUTE-error statement — it cannot discriminate, twice over,
both exact:
- R² is invariant under scaling the response, so a model short by a constant
  FRACTION has R²(err ~ X) = R²(B ~ X) for every X; and R²(B_AME ~ arc) =
  **0.9943** over the 2449 AME2020 nuclei with 2 ≤ A ≤ 240, with no model at all.
  Clearing 0.83 needs nothing missing.
- R² is invariant under affine reparametrisation of the regressor and arc = A−1,
  so arc count scores EXACTLY what bare A scores (and what 7A−3 scores). The
  diagnostic cannot tell the inter-nucleon arc structure from the mass number.
  "It beats signed-h" then says only that binding is extensive and signed-h is
  not a proxy for A.

**SCOPE LIMIT, kept explicit because it cuts against my own argument:** the
witness fits `err_pct`, RELATIVE error, for which a constant fractional
shortfall has zero variance — so the two bullets above govern the claim as
WRITTEN in this title, the audit and the block (all of which say "extensive ∝A"),
NOT the witness's own regression. What disposes of that one is its n=5 and its
own WEAK verdict.

**NOT claimed:** that `conj:inter-nucleon-channel-color-tube` is false — it may
hold on the categorical argument, untested here. Not that 0.83 was fabricated:
this clone is shallow, only 2 commits touching that witness are in the fetched
window and both carry 0.2653, so an earlier version cannot be excluded. The
claim is about the witness as committed today, which is what a reader following
the citation finds.

**Re-scope.** The premise "the missing object is an additive extensive term,
localized to the inter-nucleon channel" is not supported by the evidence this
bean cites. Companion finding the same day (PR #6271, bean `qou-brng`): for the
chain assembly the extensive framing does not apply at all — B_model is affine
in (Z,N), B/A converges, and the shortfall is a SHAPE mismatch whose missing
piece is the Z(Z−1) Coulomb multiplicity that
`CrossingCountAffine.no_crossing_combination_is_protonPairs` proves the crossing
counts cannot supply. Retitle to the Z(Z−1) + A^{1/3} target, or close as
superseded.

Corrected in the same PR: the audit §4 paragraph (struck through, with what the
source actually says) and the content block's claim. Probe:
`computations/probes/arc_count_diagnostic_degeneracy_probe.py` (6/6, exact
rational arithmetic, no float64).

## 2026-09-04 — the colour tube now has a NUMBER, and a structural obstruction

`qbeta_strand_multiplicity_probe.py` (7/7). Three crossings on three independent
strand pairs give `-ln b -> 3(-ln b)` exactly (if `tr_M` factorises over disjoint
supports), and the additive law's coefficient becomes `8.77274 MeV/nucleon`
against a measured peak `B/A` of `8.79456` at `A = 62` — **0.25 %**. The required
factor is 3.0075 and the strand count is 3.

So this bean's conjecture, if true, closes the extensive-term magnitude gap
(`qou-ib3g`) with no free parameter.

**Two obstructions, both new here:**

1. **The existing `m_pp`/`m_pn`/`m_nn` parameter is NOT it.** It repeats the same
   letter on the same generator, giving `X^3` in a 2-dim subalgebra: factors
   0.335 / 0.984 / 1.709, and `b > 1` (negative bond energy) at `m = 2`.
2. **The 3A layout cannot express a colour tube.** Nucleon `k` holds strands
   `3k, 3k+1, 3k+2`, so colour-matched pairs across an interface are distance 3
   apart; reaching them needs a braid, not the single `sigma_{3k+2}` emitted.

The decidable next step is (a): **does `tr_M` factorise over disjoint supports?**
That is checkable without building the tube, and it is what the `b -> b^3` claim
rests on entirely.
