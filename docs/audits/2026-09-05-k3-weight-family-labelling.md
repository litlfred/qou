# Every k=3 knot conclusion in the corpus, and the weight family it was computed under

**Date:** 2026-09-05
**Bean:** `qou-9b50`
**Acts on:** [`2026-09-05-phi-k-weight-family.md`](2026-09-05-phi-k-weight-family.md) (`qou-oots`) §3 — the k=3 FR-pullback ranking is not weight-family-invariant
**Builds on:** [`2026-09-04-plancherel-convention-gap.md`](2026-09-04-plancherel-convention-gap.md) (`qou-7o7h`)
**Discriminator witness:** [`computations/probes/phi-k-weight-family-discriminator.witness.json`](../../computations/probes/phi-k-weight-family-discriminator.witness.json)

---

## 0. Why this sweep exists

The discriminator measured the k=3 FR-pullback ranking on one harness, with the
same braid words and the same upstream character witnesses, varying **only** the
partition weight `w_λ`:

| family | 4₁ | 5₂ | 6₁ | best |
|---|---|---|---|---|
| **(1)** `d_q²/[n]_q!` (textbook) | **1.5014667** | 1.5394226 | 1.6040329 | **4₁** |
| **(2)** `d_q²/D²` (self-normalised, RT/Verlinde) | 1.2425297 | 1.2911323 | **1.0478474** | **6₁** |
| **(3)** Molien `f^λ q^{−κ_λ} d_q(λ)/[n]_q!` | 1.2308566 | **1.2168828** | 1.6067832 | **5₂** |
| **(4)** `y_λ` (Markov block mass) | 5.3561249 | 5.3561249 | 5.3561249 | — vacuous |

Three scoreable families, three different winners; the fourth makes the depth-3
stratum identically zero (the `SU(N)` row cap), so the test is undefined under
it. **A k=3 knot conclusion that does not name its weight family is therefore
not interpretable** — the same computation supports three different answers.

This document is the sweep for such claims and the record of what was done to
each. **It changes no number and re-runs no producer.** Where a claim's family
could be determined from its own source, the family is named; where it could
not, that is recorded as a finding rather than guessed.

---

## 1. Per-hit table

`class` is (a) live claim asserting a best/distinguished knot or a variance
figure; (b) dated historical record; (c) not a k=3 weight-weighted claim.

### Class (a) — fixed

| path:line | claim | family? before | family | action |
|---|---|---|---|---|
| [`content/…/mass-theory/depth-stratified-frobenius-reciprocity.md:5`](../../content/quantum-observable-universe/mass-theory/depth-stratified-frobenius-reciprocity.md) | "At $k=3$, $K_3^*=4_1$ gives the best variance reduction" — the paper's live k=3 identification | **no** | **(1)** `d_q²/[n]_q!` (PR #826, `qfac`) | family named inline; a follow-on note after the statement records the three-way family dependence and that the family is open (`qou-oots`) |
| same file, new §note (line 21) | — | — | — | added |
| [`…/lean/QOU/BraidKnot/DepthStratifiedFrobeniusReciprocity.lean:8`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DepthStratifiedFrobeniusReciprocity.lean) (module docstring) | "At k = 3: K_3* = 4_1 (chirality channel, named in prop:plancherel-term-7-formulation)" | **no** | **(1)** | `WEIGHT FAMILY` block added; the dangling citation dropped (see §3) |
| same file, `DistinguishedKnotIdeal.knot_label` docstring | `"4_1" at k = 3` | no | (1) | marked family-relative |
| same file, `chirality_ideal_4_1` docstring | "4_1 … named in prop:plancherel-term-7-formulation" | no | (1) | family named; provenance corrected to PR #826 |
| [`…/DepthStratifiedFrobeniusReciprocityVariance.lean:22,33,44,50`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DepthStratifiedFrobeniusReciprocityVariance.lean) | the `1.82×` uniform baseline, `2.30`/`5.94` falsifications, `3.96`/`2.31`/`5.47` scoreboard — all cross-atom max/min | **no** | **(1)** | module `WEIGHT FAMILY` block + per-theorem docstring labels; states that the same baseline under **(2)** is `1.19×`, not `1.82×`. Theorem statements untouched |
| [`docs/coordination/trace-convention-registry.md:136`](../coordination/trace-convention-registry.md) | "`fr_pullback_k3_test.py` uses the textbook form" | names (1) — **but wrongly, for that producer** | producer is now **(2)** | corrected: the producer migrated 2026-09-04 (`selfnorm_denominator`); its *committed* figures are the pre-migration (1) run. New blockquote records the three-way family dependence |
| [`docs/coordination/trace-convention-registry.json:104`](../coordination/trace-convention-registry.json) `conventions[].normalization_gap.consequence_for_readers` | same stale producer→family claim | same | same | same correction; new `k3_ranking_is_family_dependent` key |
| [`docs/coordination/1ppb-categorical-chain.md:359`](../coordination/1ppb-categorical-chain.md) | "**Authoritative finding (post-#826):** the K_3* candidate empirically minimising variance is **4_1**, not 6_1" | **no**, and phrased as current | **(1)** | dated blockquote added directly beneath, naming the family and the three-way dependence. The dated table rows above it are left as the record they are |
| [`.beans/yfvb…:44`](../../.beans/yfvb--gap-9b-fr-frontier-producerwitness-q-refactor-prer.md) | under "What is already validated (does NOT need redoing)": "4_1 best 1.55×, paper's 6_1 NOT best" | **no**, and asserted as settled | **(1)** | `AMENDED 2026-09-05` note; records that "6_1 NOT best" **reverses** under (2). The q₀-insensitivity half is left alone — it is about the anchor, not the weight |

### Class (a) — deferred to the producer owner (no producer edited; see §2)

| path:line | claim | family (determined by reading the code) | what it needs |
|---|---|---|---|
| [`computations/fr_pullback_k3_test.py:410`](../../computations/fr_pullback_k3_test.py) → `fr-pullback-k3-test.witness.json` `description` | "Empirical test … at k=3 with candidate distinguished knots {4_1, 5_2, 6_1} … FR-pulled-back weight normalized to preserve uniform Plancherel depth-3 total" | **(2)** live (`selfnorm_denominator`); the **committed witness numbers are (1)** | the `description` names no family, and the producer's family changed under it on 2026-09-04. See §4 — this file is the coordinator's this session |
| [`computations/fr_pullback_k1_k2_test.py`](../../computations/fr_pullback_k1_k2_test.py) + [`fr-pullback-k1-k2.witness.json:14,23,32,56`](../../computations/fr-pullback-k1-k2.witness.json) | "K_3* = 4_1 baseline is 1.5506× (matches PR #826)"; "best (K_1*,K_2*) variance 1.5428×" | **(1)** — `qfac(n_strands, Q0_PROTON)` at line 131 | family name in the four assertion `source` strings and the `description` |
| [`computations/fr_pullback_cosh_h_test.py`](../../computations/fr_pullback_cosh_h_test.py) + [`fr-pullback-cosh-h.witness.json:38`](../../computations/fr-pullback-cosh-h.witness.json) | "closes the residual 1.54× variance left after PR #826's K_3* = 4_1 resolution" | **(1)** — `qfac` at line 104 | family name in `description` |
| [`computations/delta_lambda_k_star_variance_phase5d_5b.py:306,374`](../../computations/delta_lambda_k_star_variance_phase5d_5b.py) + [`k-star-variance-phase5d-5b.witness.json:14,45`](../../computations/k-star-variance-phase5d-5b.witness.json) | `baseline_variance_uniform_plancherel = 1.82`; "(× K_3* = 6_1 fixed per the catalog)" | **(1)** — `qfac` from `q_mpmath` | family name; **and** the 6₁ here is the superseded 5d.5b probe (wrong 3-strand braid word + missing `S_uniform` preservation, both caught by #826) — the witness does not say so |
| [`computations/delta_lambda_full_variance_phase5e_1.py`](../../computations/delta_lambda_full_variance_phase5e_1.py) + [`delta-lambda-full-variance-phase5e-1.witness.json:14,37`](../../computations/delta-lambda-full-variance-phase5e-1.witness.json) | "Best K_k* variance under FULL formula: 1.3219. Baseline (no FR projector): 1.5621. Phase 5d.5b … best: 1.4889 (K_1* = 6_1)" | **(1)** — `qfac(n_strands, Q0_PROTON)` at line 145 | family name in `description` + the assertion `source` |
| [`computations/constit_factor_and_volhyp_test.py:5,26,72,236`](../../computations/constit_factor_and_volhyp_test.py) | "the … variance left in the depth-stratified formula after PR #826's K_3* = 4_1"; "K_3* = 4_1 (canonical from PR #826)" — **"canonical" is the word that needs the qualifier** | **(1)** by inheritance from #826 | family name; drop or qualify "canonical" |
| [`computations/binding_depth_stratified_selfconj.py:7,165`](../../computations/binding_depth_stratified_selfconj.py) | "at low k ≤ 3 the Frobenius integral factors through a distinguished hyperbolic-knot ideal (e.g. 6_1 at k=3, the chirality channel)" | **undeterminable** — see §3 | the family cannot be recovered from this file or its cited source |

### Class (a) — already compliant, no action

| path | why |
|---|---|
| [`content/…/mass-theory/plancherel-term-7-formulation.md`](../../content/quantum-observable-universe/mass-theory/plancherel-term-7-formulation.md) | defines `w_λ` and names **no** knot; its 2026-09-05 note already names (1), (2) and (3) explicitly and marks the numerator question open. Nothing to add |
| [`docs/audits/2026-07-06-gap9b-frprojector-driver.md`](2026-07-06-gap9b-frprojector-driver.md) §4–§6 | already labels its own v1 numbers `dim_q²/[n]_q!` and its v2 numbers self-normalised, and already says the k3-test's `1.82×/1.55×` "should be re-read against the self-normalized 1.19×/1.14×" |
| [`computations/probe_k3_selfnormalized_recheck.py`](../../computations/probe_k3_selfnormalized_recheck.py) + witness | names both families in its own docstring and `description` |

### Class (b) — dated records, left as records

| path | note |
|---|---|
| [`docs/audits/2026-05-19-phase5f-fr-pullback-k1-k2.md`](2026-05-19-phase5f-fr-pullback-k1-k2.md) | the `1.82×` / `1.551×` / `1.5432×` scoreboard. Family (1) throughout. Cited **as current** by `1ppb-categorical-chain.md` §Phase 5f, which is now covered by the blockquote added at line 361 |
| [`docs/audits/2026-05-20-phase5g-5h-5i-results.md`](2026-05-20-phase5g-5h-5i-results.md) | `1.5507×` baseline table, family (1) |
| [`docs/audits/2026-05-19-variance-per-depth-diagnosis.md:59`](2026-05-19-variance-per-depth-diagnosis.md) | "The k=3 case ($6_1$)" — pre-#826, superseded by that PR on its own terms |
| [`docs/coordination/1ppb-categorical-chain.md`](../coordination/1ppb-categorical-chain.md) dated rows (5d.5b, #826, Phase 5f) | left verbatim; the family qualification sits once, at the "Authoritative finding" line the rows feed |
| [`docs/audits/2026-09-04-plancherel-convention-gap.md:192`](2026-09-04-plancherel-convention-gap.md) | "`fr_pullback_k3_test.py` — textbook form" is stale by one day — but **§7 of the same document, added the same day, records the migration** ("corrected in place"). Self-superseding within one file; left as written |
| `.beans/qou-oots`, `.beans/qou-7o7h`, `.beans/qou-7mvf` | session records that already name their families |

### Class (c) — excluded, with the reason

| path | reason |
|---|---|
| [`content/…/mass-theory/curvature-rank-gb-stratification-proof.md:75`](../../content/quantum-observable-universe/mass-theory/curvature-rank-gb-stratification-proof.md) | "(GB depth 3, jet 1, std channel) — the $6_1$ knot" is an ideal-position identification read off the **Gröbner–Shirshov filtration**, not a `w_λ`-weighted variance result. No weight family enters, so none can be named. See §3 |
| [`content/…/observations/confinement-curvature-rank.md:33`](../../content/quantum-observable-universe/observations/confinement-curvature-rank.md), [`…/mass-theory/confinement-categorical-proof.md:58`](../../content/quantum-observable-universe/mass-theory/confinement-categorical-proof.md) | "rank-3 chirality residue $\mathrm{Vol}(6_1)\cdot|(q;q)_3|$" in the $\mathfrak{Q}_\beta$ formula — a hyperbolic volume in a decay-sector product, not a partition weight |
| `…/MassTheory/BraneTowerLevelAmplitude.lean`, `…/VassilievMagnitudeA3.lean`, `docs/audits/2026-07-18-deltalambda-k4-collective-magnitude.md` | `K₃` = the **complete graph** on 3 vertices (coordination graph), not a knot |
| `…/mass-theory/borromean-bloch-group-element.lean`, `…/Machinery/HeckeTauAssignmentGaugeGate.lean`, `…/definition-index.md:512` | `K₃(ℂ)` / `K₃^{ind}(F)` = **algebraic K-theory**, not a knot |
| `…/BraidKnot/IsotopeKnot.lean:42`, `…/isotope-knot-equivalence.lean:31` | `K₃` = a bound variable in a transitivity lemma |
| `computations/sublemma_2_1_A_operator_extract_h12_nn_streamed.py:378` | `K_3*len(parts_3)` is a Python multiplication, not `K_3*` |
| `…/Knot/MortonFranksWilliams.lean`, `…/Knot/SixOneCertified.lean`, `…/Knot/GeneratedCusp.lean`, `…/mass-theory/hyperbolic-knot-shape-fields.md` | `6₁` braid index / cusp / trace field geometry — unrelated to depth stratification |
| `content/schema/references.ts:8485` | `AIF_2000__50_6_1859_0` — a substring of a Numdam URL |

---

## 2. Counts

| | class (a) | class (b) | class (c) |
|---|---|---|---|
| distinct files | **15** | 7 | 12 |
| **fixed this pass** | **7 files / 12 sites** | — | — |
| already compliant, no action | 3 files | — | — |
| **deferred to producer owners** | **7 producer/witness pairs** | — | — |
| left as record | — | 7 files | — |
| excluded | — | — | 12 files |

**Why the seven `computations/` hits were not edited.** A docstring-only edit
drifts the producer's `scriptHash` while leaving its payload byte-identical,
which flags every one of its witnesses as self-stale for a refresh that cannot
change a number. AGENTS.md §"Refresh stale sidecars + witnesses" is explicit on
the trade: *"Cheap probes: just re-run. Long-compute producer with a
comment-only diff: claim it as a bean rather than spend the idle pass
recomputing numbers that cannot change."* These are H₉/H₁₂ character computes
(the ⁴He leg alone is ~25 min), and this task's own brief forbids re-running
anything. They are recorded here with the family already determined by reading
the code, so applying them later is a mechanical edit, not a re-derivation.

---

## 3. Claims whose weight family is UNDETERMINABLE

Two, and they are the same defect seen from two sides.

**3.1 `binding_depth_stratified_selfconj.py:7` — "e.g. 6_1 at k=3, the chirality
channel", cited to `prop:plancherel-term-7-formulation`.** That block defines
`w_λ` and **names no knot at all** — not `6_1`, not `4_1`. So the citation does
not source the identification, and the script computes a *different* hypothesis
(self-conjugate restriction) rather than an FR pullback at any named knot, so
the `6_1` never enters its own arithmetic either. There is no run behind this
`6_1` whose weight family could be read off. The honest form is **"the k=3
chirality knot is named `6_1` here under an unrecorded provenance and an
unrecorded weight family"**, and that is what this note records rather than
guessing (1) from the file's use of `qfac`, which would attribute a family to a
claim that was never computed.

**3.2 The same dangling citation was in the Lean.**
`DepthStratifiedFrobeniusReciprocity.lean` carried "K_3* = 4_1 (chirality
channel, **named in prop:plancherel-term-7-formulation**)". Here the *family* was
recoverable — the `4_1` is PR #826's measured result, family (1) — so the site is
fixed rather than listed as undeterminable; but the citation was pointing at a
block that names no knot, exactly as in 3.1. Both were removed/corrected.

**A third, adjacent finding, and it is the more useful one.** The corpus's two
live "the k=3 knot is X" claims come from **two different derivations**, and only
one of them has a weight family at all:

- the **FR-pullback variance route** (`conj:depth-stratified-frobenius-reciprocity`,
  the k3-test and its descendants) says `4_1` — and, as measured, says `6_1` or
  `5_2` instead if you change `w_λ`;
- the **GB-filtration route** (`curvature-rank-gb-stratification-proof`,
  `confinement-curvature-rank`) says `6_1` at curvature-rank 3, structurally,
  with no `w_λ` anywhere in it.

So "the paper's named `6₁`" that the discriminator audit contrasts against is
**not** a weight-family result and is not refuted by any weight-family
measurement — it is a claim of a different kind, sourced elsewhere. The
`K_3* = 6_1` that PR #826 overturned is the *catalog aside* recorded in
`1ppb-categorical-chain.md`, which is a third thing again and no longer appears
anywhere in `content/`. Keeping these three apart matters: a reader who reads the
discriminator's "under family (3) the paper's named 6₁ is the worst of the three"
as bearing on the GB-filtration identification is making an inference the
measurement does not license.

---

## 4. What `fr_pullback_k3_test.py` needs (for its owner)

Not edited — it is claimed by the merge coordinator this session. Two items,
both `description`-level, neither touching a number:

1. **Name the family in the producer's witness `description`.** It currently
   reads *"FR-pulled-back weight normalized to preserve uniform Plancherel
   depth-3 total"*, which names the *redistribution rule* but not the *base
   measure*. It should say the base measure is `d_q²/D²` (self-normalised,
   RT/Verlinde) — and, because the producer migrated on 2026-09-04, that the
   `1.82×` / `1.5015×` figures quoted downstream are the **pre-migration**
   `d_q²/[n]_q!` run and are not comparable with its live output.
2. **Say that the k=3 ranking is family-dependent**, in one line, with the three
   winners and a pointer to `qou-oots`. Everything downstream of this producer
   (`fr_pullback_k1_k2_test`, `fr_pullback_cosh_h_test`,
   `constit_factor_and_volhyp_test`, the two `delta_lambda_*_variance_*` probes)
   inherits its framing, and each of those carries the claim unlabelled today.

A third item is out of scope here but is the same file: bean `qou-u6zt` records
that this producer takes `q₀` from `qou_substrate.constants.Q`, a Python
`float`. That is `2.7e-17` relative and is fifteen orders below the ~30 % ranking
effects above; it is **not** a reason to doubt any figure in this document.

---

## 5. Verification run for the changes in §1

CI is unavailable repo-wide (`workflow_dispatch`-only), so this is the
Phase-4 verification gate, stated rather than assumed:

- **Lean** — both changed files `lean`-direct **exit 0** against the restored
  Mathlib olean cone (3470 oleans), `0` `sorry` in either. Changes are docstring
  and comment text only; no declaration, statement or proof term was touched.
- **Content block** — `bun run scripts/run-validate.ts content/quantum-observable-universe`
  → **`✓ Valid`**, 10 issues, all pre-existing and none in the changed block
  (six are the known `authorNotes`/`computation` silently-dropped-field class
  that AGENTS.md documents; four are unrelated cross-references).
- **Render QA** — the LaTeX render + `unified-latex` AST validation **did** run,
  inside the validate pass above: `validate.ts:621-622` calls `renderBlock` then
  `validateLatexAst` on every block, and the changed block raised nothing.

  > **Do not "verify" this the way I first did.** I initially ran
  > `bun run folio-assistant/content/pipeline/render-latex.ts <block>`, got a
  > silent `rc=0`, and wrote it up as a clean render. It is not evidence:
  > `render-latex.ts` is a **library module with no CLI entry point** (no
  > `import.meta.main`), so `bun run` loads it and exits — the *same* `rc=0`
  > comes back for `…/mass-theory/NO-SUCH-BLOCK`, which is how the no-op was
  > caught. A green exit from a command that cannot fail is worth nothing;
  > route the render through `run-validate.ts` (or `build.ts`, which does have
  > a main).

  The manual grep battery also passes independently: `$` tokens even (60), `$$`
  balanced (2), braces balanced (20/20), no `\bigl`/`\bigr` or `\begin`/`\end`
  introduced, no line inside `$$…$$` starting `+`/`-`/`*`.
- **Sidecar** — `qa-sweep` re-run on the changed block; script-reviewer criteria
  refreshed against the new source hashes, agent criteria left `needs-agent`.
- **JSON** — `trace-convention-registry.json` re-parses.
- **Not run, and why**: no producer was executed and no witness regenerated —
  see §2. `check-sidecars.sh` flags `ℝ` literals in
  `DepthStratifiedFrobeniusReciprocityVariance.lean` under §7c; those are
  pre-existing and are the file's entire stated purpose (it exists *because* the
  §7c split put the archimedean decimals there), not something this pass
  introduced.

---

## 6. Scope

**Established.** Which durable artifacts assert a k=3 knot or a k=3 variance
figure; which weight family each was computed under, where that is recoverable;
and that two of them are not recoverable (§3).

**Not established, and not to be read in.** Nothing here says which family is
right — that is open (`qou-oots`) — and nothing here says any k=3 knot
identification is correct or incorrect. No number in the corpus was changed and
no verdict was restated. The output is labels.
