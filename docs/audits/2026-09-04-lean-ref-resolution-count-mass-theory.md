# Lean completeness by `lean.ref` resolution: the 17 "no sibling" blocks (2026-09-04)

Bean `qou-jkam`. Owner pick, 2026-09-04: *"a lean-completeness pass on the 14
'no sibling' blocks counted by lean.ref resolution."* Branch
`claude/lean-ref-resolution-qvalue-2026-09-04`, PR #6554.

## The question

The `wall-side-statement` drain (bean `qou-zmuu`, PRs #6450 / #6475 / #6499 /
#6529) found that most of the 2026-07-07 QA fails in `mass-theory` were not
wall-side findings at all: the checker had recorded *"sibling Lean file is
missing"*, and the re-adjudicating agents kept reporting that the block's
`lean.ref` resolves to a library declaration regardless. That measured
"sibling presence". This document measures **resolution** per AGENTS.md §0a:
(1) sibling `<root>.lean`, (2) `<lakeRoot>/<Decl/Path>.lean`, (3) grep.

The population is the 17 blocks the drain marked "Lean sibling missing" or
"Lean refuses" (15 in `mass-theory`, 2 in `predicted-spectra`); the owner's
"14" is the mass-theory subset before two late additions.

## Method

`scratchpad/leanref.py` (session-local; the table below is its output plus
hand reads). For each block: parse `lean.ref` from the `.ts`; try candidate 1
(sibling), then candidate 2 for the full declaration path and each parent
prefix; grep only if no candidate holds a declaration whose last name
segment matches the ref's. "decl" is a regex over `theorem | lemma | def |
structure | class | abbrev | instance` heads. **Sorries are counted on the
file with `/- … -/` and `--` comments stripped** — see §Correction.

## Result

| block | kind | `lean.ref` (after `qou:`) | resolves via | file | decl kind | proof sorries in file |
|---|---|---|---|---|---|---|
| ramified-disc-fusion | proposition | `QOU.BraidsKnots.RamifiedDiscFusion.resolvent_agreement` | cand-2 parent | `QOU/BraidsKnots/RamifiedDiscFusion.lean` | theorem | 0 |
| feynman-trace-collapse | lemma | `QOU.FeynmanPathIntegrals.trace_collapse` | cand-2 parent | `QOU/FeynmanPathIntegrals.lean` | theorem | 0 |
| skein-mass-from-linking | lemma | `QOU.BraidsKnots.skein_mass_from_linking` | cand-2 full | `QOU/BraidsKnots/skein_mass_from_linking.lean` | **def** | 0 |
| symbolic-character-table | proposition | `QOU.BraidKnot.symbolic_character_table` | cand-2 full | `QOU/BraidKnot/symbolic_character_table.lean` | theorem | 0 |
| knot-operator-transition | proposition | `QOU.BraidKnot.knot_operator_transition` | cand-2 full | `QOU/BraidKnot/knot_operator_transition.lean` | theorem | 0 |
| mass-categorical-descent | proposition | `QOU.ParticleInteractions.mass_categorical_descent` | cand-2 full | `QOU/ParticleInteractions/mass_categorical_descent.lean` | theorem | 0 |
| quantum-dilog-convergence | proposition | `QOU.MassEndomorphism.PhiQConvergence.quantumDilog_multipliable` | cand-2 parent | `QOU/MassEndomorphism/PhiQConvergence.lean` | theorem | 0 |
| feynman-categorical-trace | proposition | `QOU.FeynmanPathIntegrals.FeynmanCategoricalTrace` | cand-2 parent | `QOU/FeynmanPathIntegrals.lean` | **structure** | 0 |
| volume-perturbation-formula | proposition | `QOU.BraidKnot.volume_perturbation` | cand-2 full | `QOU/BraidKnot/volume_perturbation.lean` | theorem | 0 |
| q-reeb-flow-on-color-coords | definition | `QOU.CategoricalReeb.QReebFlowOnColorCoords` | sibling exists **without** the decl; cand-2 full | `QOU/CategoricalReeb/QReebFlowOnColorCoords.lean` | class | 0 (both files) |
| feynman-markov-identification | lemma | `QOU.FeynmanPathIntegrals.markov_identification` | cand-2 full | `QOU/FeynmanPathIntegrals/markov_identification.lean` | theorem | 0 |
| content-scaling-correspondence | proposition | `QOU.BraidKnot.BoxContent.boxContent` | cand-2 parent | `QOU/BraidKnot/BoxContent.lean` | **def** | 0 |
| feynman-eigenbasis-decomposition | lemma | `QOU.FeynmanPathIntegrals.eigenbasis_decomposition` | cand-2 parent | `QOU/FeynmanPathIntegrals.lean` | theorem | 0 |
| crossed-module-euler-characteristic | proposition | `QOU.BraidKnot.CrossedModuleEulerCharacteristic.crossed_module_euler_characteristic` | cand-2 parent | `QOU/BraidKnot/CrossedModuleEulerCharacteristic.lean` | theorem | 0 |
| tmli-constituent-composite-agreement | lemma | `QOU.BraidsKnots.tmli_constituent_composite_agreement` | cand-2 full | `QOU/BraidsKnots/tmli_constituent_composite_agreement.lean` | theorem | 0 |
| predicted-spectra/hadron-half-life | proposition | `QOU.Archimedean.hadron_half_life` | sibling | `predicted-spectra/hadron-half-life.lean` | **def** | 0 |
| predicted-spectra/q-value-transition | definition | was `QOU.Archimedean.QValueTransition` | sibling exists **without** the decl; cand-2 full | `QOU/Archimedean/QValueTransition.lean` | structure | 0 (both files) |

**Headline.** 17 of 17 resolve to an existing declaration; 0 of 17 have a
proof `sorry` in the resolved file. "Lean sibling missing" was a
sibling-presence artefact in every one of the 15 `mass-theory` rows. The
count by resolution is **15 / 15 resolved, 0 unformalised by absence.**

That is the count the owner asked for. It is not the same as "15 / 15
formalised", and the rest of this document is about the gap.

## What resolution does not tell you — five rows where the decl is not the claim

Resolution answers "does the ref point at a declaration". It does not
answer "does that declaration state the block's proposition". Read
against the `.md`, five rows fail the second test without any `sorry`:

1. **`content-scaling-correspondence` — the ref names a premise, and the file
   has no theorem.** `BoxContent.lean` contains `def boxContent` and no
   `theorem`/`lemma` at all. The block is a *proposition* ("the content
   $c = j - i$ equals the magnetic quantum number $m_j$ … and determines the
   BW scaling function"). The definition of box content is the setup, not the
   claim. **This is the one genuinely unformalised proposition in the set**,
   and it survived the drain precisely because its ref resolves.
2. **`feynman-categorical-trace` — the claim is a structure field.** The
   proposition is $\sum_\lambda w_\lambda\,\mathrm{tr}_{S_\lambda}(\rho(\beta))
   = \mathrm{tr}_M(\rho(\beta))$. In `FeynmanCategoricalTrace` that identity is
   the field `amplitude_eq_markov`; the only theorem, `mass_eq_abs_amplitude`,
   rewrites with the field and takes absolute values. Per AGENTS.md
   §3b-cond item 5 this is a carrier that *assumes* the block's conclusion
   — honest as a conjecture carrier, not a proof of the proposition. The
   `.md` calls it a proposition.
3. **`feynman-markov-identification` — the same shape, one level down.**
   `markov_identification` takes `h : markovTrace_branching …` and proves
   the amplitude equals the trace by `rw […, h]`. The hypothesis *is* the
   branching identity; the theorem is its projection. The file says so in
   its own docstring (the three "sorry" mentions that inflated my first
   count are that docstring explaining why the premise is named rather
   than sorried). Lemma proved; premise not established.
4. **`hadron-half-life` — a proposition whose ref names a `def`.**
   `hadron_half_life d := d.halfLife := Real.log 2 / qPrefactor d.q`, with
   `qPrefactor q = (q + q⁻¹)(q − q⁻¹)^5`. The `.md` proposition states
   $\Gamma_\beta = |\mathcal{W}(q)|^2 \mu_0 /(2\pi^3)\cdot[2]_q\cdots
   |\mathcal{M}_q|^2 f(Q)$. The Lean carries the $q$-shape of the
   prefactor and its positivity (`hadron_half_life_pos`); it does not carry
   $\mathcal{W}$, $\mu_0$, $\mathcal{M}_q$ or $f(Q)$. The old "Lean fails
   (linarith)" QA note is stale — the file verifies (`lean`-direct exit 0
   on this branch's environment was not run for this file; the sidecar's
   automated `proof-lean-compiles` is the live signal).
5. **`skein-mass-from-linking` — a lemma whose ref names a `def`.** Same
   pattern as 4: the ref points at the object, and whichever theorem
   states the lemma is not the one the block declares as its formal
   counterpart. Not read in detail here; flagged by decl kind.

And one partial: **`ramified-disc-fusion`** has three numbered claims;
`resolvent_agreement` (the ref) is claim 3, `galois_group_order`
(`card S3 = 6`) is a fragment of claim 2, and claim 1 (fusion into a single
ramified disc) is topological and has no Lean.

Two rows already carried in bean `qou-zmuu` and unchanged by this pass:
`volume_perturbation.lean` writes the Markov parameter in convention C
while the `.md` states D; `eigenbasis_decomposition` has a docstring
saying "sorry retained" over a sorry-free body.

## The two-carrier shape (both definitions in the set)

Both `definition` blocks in the set have **a sibling `.lean` that does not
contain the ref's declaration, and a library file at candidate 2 that
does**:

| block | sibling holds | library holds |
|---|---|---|
| `q-reeb-flow-on-color-coords` | `qReebFlowSector` over generic `R` (§7c-clean), composition + spectator lemmas | `class QReebFlowOnColorCoords (q : ℝ)` — an axiomatisation, consumed by `SixCanonicalKnotOperators.lean` |
| `q-value-transition` | `QqValue.value` — the categorical **action** difference (matches the title) | `structure QValueTransition` — the **mass** difference, header claiming to be "the manuscript definition" |

§0a says the sibling is checked first; a sibling without the named
declaration is neither a shadowing stub (it carries real content) nor a
resolution. For `q-value-transition` the two carriers defined *different
things* and the `.md` sided with the library one — that is bean
`qou-181p`, fixed on this branch (see the commit
`content(qou-181p)` and the rewritten header of
`lean/QOU/Archimedean/QValueTransition.lean`). For `q-reeb-flow` the two
carriers are the generic definition and its archimedean axiomatisation,
which is the §7c-sanctioned split; the defect is only that `lean.ref`
names the class while the sibling holds the definition. **Not changed
here** — it needs a decision on which file is the definition, and the
class has a consumer.

## Correction (my own, same session)

My first table reported per-file `sorry` counts of **13, 7, 7, 5, 2, 2, 1**
for `markov_identification`, `skein_mass_from_linking`,
`symbolic_character_table`, `mass_categorical_descent`,
`volume_perturbation`, `tmli_constituent_composite_agreement`,
`PhiQConvergence`. Those were `grep -c sorry` over the whole file, and every
one of them is a **docstring or comment mention** — files in this corpus
routinely document *why* something is not a `sorry`. With comments
stripped the count is **0 across all 18 files**. The earlier figure was
reported in the pre-compaction session summary and in no durable artifact;
this document is the first place the number lands, and it lands corrected.
The lesson is the one AGENTS.md already carries for `scriptCommitSha` and
for shape-matched conventions: a token count is not a measurement of the
thing the token names.

## Implications

- The `wall-side-statement` checker's "sibling missing" text should not be
  read as "unformalised". The drain already re-adjudicated all 17 as
  `pass` on the wall-side question; this pass confirms the Lean side
  exists for all of them.
- The lean-completeness question that *remains* is not presence but
  **statement integrity**: rows 1–5 above are `proof-statement-integrity`
  / `proof-no-self-assuming-projection` candidates, and none of them will
  fire a `sorry`-keyed detector. Row 1 (`content-scaling-correspondence`)
  is the only one with nothing to point at; rows 2–3 are carriers assuming
  their conclusion; rows 4–5 are refs aimed at objects instead of
  statements.

## Options

Stated as the owner's call; none of this is done on the branch.

- **(A) Leave as measured.** Nothing changes; the five rows stay as they
  are and are recorded here and in `qou-jkam`. Default if the owner says
  nothing. Costs nothing; the statement-integrity gap stays invisible to
  every automated gate.
- **(B) Formalise `content-scaling-correspondence`.** Write the proposition
  (content ↦ $m_j$ under $q$-Schur–Weyl) as a theorem in `BoxContent.lean`
  and repoint the ref. One file, one theorem, `lean`-direct verification;
  probably a day if the Schur–Weyl weight-space bookkeeping is already in
  the library, longer if not. Commits the block to a real proof or to an
  honest `sorry` + `-- Ref:`.
- **(C) Repoint refs 4–5 at statements.** `hadron-half-life` →
  `hadron_half_life_pos` (or a new theorem stating the formula shape);
  `skein-mass-from-linking` → whichever theorem in its file states the
  lemma. Two `.ts` edits plus sidecar refresh; changes what the formal
  graph attaches to those blocks. Cheap, reversible.
- **(D) Re-kind rows 2–3.** Downgrade `feynman-categorical-trace` to a
  conditional proposition with a `[FeynmanCategoricalTrace]`-style banner
  (§3b-cond) or to a conjecture. Touches the `.md` register and the
  chapter's claim count; a physics-facing change, not a bookkeeping one.

My recommendation, as judgement: (C) now (it is two lines and removes two
false "this decl is the claim" edges), (B) as its own bean, (D) only after
the owner reads row 2, because it changes what the chapter claims.
