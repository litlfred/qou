# The up quark is an unknot in one block and a trefoil in another — measurement and options

Date 2026-11-20. Owner instruction (Carl, ~20:50): *"Investigate & propose."* Found by PR #8673
(the lepton-strand premise). **Nothing in `folio/` is changed by this document.** It records the
measurement and puts the choice to the owner.

## RULING (owner, 2026-11-20 ~21:05): option B

The owner chose **option B**: apply A, and reword every trefoil-quark site to match `def:up-quark`
(a quark is an unknot strand, i.e. a component of the pure braid `B₃`). This is an explicit yes for the
sweep. For blocks whose *argument* rests on trefoil quarks, the instruction was to reword the
identification, add a dated `authorNote` recording what the argument assumed and what stays valid,
and list them as follow-up. It was also to **report before changing** anything where a producer,
witness or Lean proof depends on the trefoil-quark reading.

### What was applied (PR #8677)

| commit | sites |
|---|---|
| `e5fb6b8695` | `def:electron-knot` (`.md`, `.ts` gains `rem:knot-particle-dictionary`, `.lean` docstring); `TorusKnot.lean:74` docstring |
| `a2ae2d5f27` | tables: knot-particle generation, building-block knots 1, tm-notation 3, linking-relations 1 and 2 |
| `e00cfd52b8` | `tm-knot-pairs`, `transfer-matrix-operator-properties`, `categorical-transfer-matrix-properties` (+ notes) |
| `a47c11124b` | `strangelet-intro`, `strangelet-witten-stability` (+ notes) |
| `974cae4443` | `torus-knot-prime-powers`, `jet-planck-particle-spectrum` (+ notes) |
| `8adb3646dd` | `linking-relations-table` (note only) |
| `1e4e6be1c9` | `computations/sdp_gamma_gamma_to_qqbar.py` comments (lines 15, 124) |
| `f5c1b5ea21` | `knot-formula-table` (+ table 2), `unmapped-torus-knots` (+ notes) |
| `ccbf74fce2` | `categorical-proton.lean` docstring |

### Correction of this document's own §1b and §2 (measured after the ruling)

**§1b undercounted.** It listed 14 trefoil-quark sites. The sweep found five more that my grep missed,
because they write `𝔲 = T_{2,3}` or `κ(u) = 3` without "up quark" near "trefoil":
`knot-formula-table` (+ its table 2), `unmapped-torus-knots`, `categorical-proton.lean` (docstring),
`braids-and-knots/knot-notation-convention`, and `knots-particles-confinement/lepton-meson-torus-knot-dictionary`.

**§2 was wrong where it mattered.** It said *"No producer depends on it"* and that no sorry-free Lean
decides a quark's knot type. Both were measured on a grep for "up quark" and "trefoil" near each other.
What that grep did not see is a **meson / weak-isospin cluster** that defines each quark as the torus
braid `T(2,n) = σ₁^{±n}`, with signed writhe `κ(u,c,t) = +(3,5,7)` and `κ(d,s,b) = −(3,5,7)`, and proves
results about that assignment:

- Lean (sorry-free, all decide the quark index by fiat):
  - `QOU/ParticleInteractions/WeakIsospinT3Grading.lean` (`signedWrithe`, `T3 = sign κ / 2`);
  - `QOU/ParticleInteractions/MesonOperatorSelectionT3.lean` (meson content `{−κ(q̄), +κ(q)}`, injectivity results);
  - `QOU/ParticleInteractions/MesonFluxTubeReduction.lean` (`windingContent`, `D_kaon_same_winding`);
  - `QOU/BraidKnot/MesonFusionIndexSelection.lean` (`quarkTorusIndex`, `scanPair_four_not_dictionary_index`);
  - `knots-particles-confinement/lepton-meson-torus-knot-dictionary.lean` (π = 3+3, K = 3+5 crossings).
- Compute: `computations/meson/meson_braid_length_cap_probe.py` → `meson/meson-braid-length-cap.witness.json`
  (`WINDINGS = {up: 3, charm: 5, top: 7}`), and `weak-isospin-t3-grading.witness.json`.
- Content: `knot-notation-convention` (the weak-isospin reading `T₃ = ½ sgn κ`) and
  `prop:lepton-meson-torus-knot-dictionary`; indexed from `appendix-standard-model/sm-results-index`.

**None of these were changed**, per the report-before-changing instruction. They are the decision
below. The `m_K/m_π` L2 row's credited Lean (`meson_qCG_3x4`, `meson_EM_closed_form`) does **not**
read the quark index: `MesonFusionIndexSelection.lean` states that the identity holds for every pair
`(m, m+d)`. Only its negative `scanPair_four_not_dictionary_index` (4 is not a quark index) uses the
dictionary, and that negative would lose its premise.

The same wrong §2 sentence was repeated in the first PR #8677 body and in the 2026-11-20T21:30Z note
on bean `qou-99qc`. Both are corrected in this round.

### Still open for the owner: the meson T(2,n) cluster

- **What it means.** Under the ruling, a quark is an unknot strand carrying one crossing letter. The
  meson cluster instead gives each quark a writhe of ±3/±5/±7, its partner's crossing count. The
  weak-isospin grading only needs the **sign** of κ, and that survives as the crossing orientation
  (σ vs σ⁻¹). The **magnitude** `|κ| = n`, the generation winding, has no carrier on an unknot strand
  except through the lepton partner.
- **Options.**
  - (i) Re-read `|κ|` as "the crossing count of the quark's lepton partner": relabel docstrings and
    prose, keep every theorem. Cheap; it makes the generation index a descent label, which the
    dictionary already uses.
  - (ii) Rebuild the cluster on single crossing letters. The `D`/kaon separation results would then
    need a new source of generation information.
  - (iii) Leave it unchanged (the default). The paper then carries two quark models: B₃ strands for
    baryons and the ruling, T(2,n) braids for mesons.
- **Recommendation (judgement).** (i). Every proved statement there uses κ only through its sign
  and its magnitude as a label, so relabelling loses nothing that was proved.

### Not done in this round

- **qa-sweep.** It cannot load in this container: the light platform lacks `fast-xml-parser`.
  Sidecars of the touched blocks are stale.
- **Precision gates.** `scripts/precision-gates.sh --changed` was killed at its 400 s timeout. The
  only computations change is comment-only. The audit witnesses the killed run rewrote were restored.
- **Witness drift.** `sdp-gamma-gamma-to-qqbar.witness.json` will show `scriptHash` drift from the
  comment-only edit, and it was deliberately not re-run.
- **Adjacent finding, left alone.** `sdp_gamma_gamma_to_qqbar.py:14` calls `σ₀σ₁` the "L₊ (Hopf
  link intermediate)". Its B₃ closure has one component, and the photon ruling retires the σ₀σ₁
  fourth term.

---

## 0. The decision

Which knot type does the paper give the up quark, and therefore what may `def:electron-knot` say
about it? Two definitions disagree:

- [`def:up-quark`](../../folio/quantum-observable-universe/knots-particles-confinement/up-quark.md)
  says the up quark **is an unknot** in a colour tube, distinguished only by its positive crossing
  orientation in the Borromean braid `B₃`. Its own text adds: *"The up quark is not a distinct knot
  type."*
- [`def:electron-knot`](../../folio/quantum-observable-universe/predicted-spectra/electron-knot.md)
  says the electron is the trefoil `T(2,3)` and *"shares this knot type with the up quark"*. Its
  `.ts` lists `def:up-quark` in `uses[]`, so it cites the block it contradicts.

This needs the owner because both texts are old, both have followers, and no ruling picks between
them (§2). One has a structural argument behind it (§3).

## 1. Measurement: who says what

Corpus-grep checklist run 2026-11-20 on `origin/main`: `folio/` (content `.md`/`.ts`/`.lean` and
library Lean), `computations/`, `docs/audits/`, `docs/coordination/`, beans on the mount, and
`git log` / GitHub commit history. Step 0 was run through the CLI (`bun scripts/corpus-search.ts`,
queries "up quark", "electron" and "trefoil" with `--search-text --limit 200`). It found no block
beyond the grep set; its one new hit, `tbl:borromean-quark-table-data`, lists the trefoil as
"Electron (gen. 1)" only. The query "quark trefoil" seeded nothing, and every seed was authored,
so no ingested source speaks to this.

### 1a. "Up quark is an unknot" (13 sites)

| site | statement |
|---|---|
| `knots-particles-confinement/up-quark.md` | unknot in a colour tube, `𝔲 = ν|_{B₃,+}`, "not a distinct knot type" |
| `knots-particles-confinement/down-quark.md` | unknot, negative orientation |
| `knots-particles-confinement/up-quark-properties.md` | "removing it unlinks the remaining two unknots" |
| `knots-particles-confinement/knot-particle-dictionary.md` | "Each quark is an **unknot** (0₁) within `B₃`… not knot type" |
| `knots-particles-confinement/knot-particle-dictionary-table4-data.md` | braid element `σ_i` / `σ_i⁻¹`; `T(2,3)` only in a column called *lepton descent* |
| `knots-particles-confinement/categorical-proton.md` | `B₃ = (σ₀σ₁⁻¹)³`, "the Borromean braid of three unknots" |
| `knots-particles-confinement/hadron-proton-example.md` | "Quarks are unknots `K_{0₁}`" |
| `observations/borromean-quark.md` | up quark = unknot, positive orientation |
| `observations/hydrogen-knot-structure-table1-data.md` | `ν_r`, `ν_g` = unknot = up quark |
| `appendix-knot-operations-archimedean/particle-nf-table.md` | `𝔲 = σ₀`; `𝔲 ← T(2,3)` is "the lepton partner… not the quark's own knot type" |
| `appendix-knot-operations-archimedean/gluon-model-comparison.md` | "Quarks interact as single-crossing unknots, not as full trefoils" |
| `observations/strangelet-crossing-energy.md` | "The arrow is the… lepton-descent relation, not an identity" |
| Lean `QOU/Archimedean/ParticleKnots.lean` (`UpQuark`, `DownQuark`: `crossing_number := 0`, `genus := 0`), `up-quark.lean`, `down-quark.lean`; `QOU/StandardModel/QuarkBraidChargeObstruction.lean` (`upQuark : BraidWord := [1]`) | |

### 1b. "Up quark is the trefoil `T(2,3)`" (14 sites)

| site | statement |
|---|---|
| `predicted-spectra/electron-knot.md` | "shares this knot type with the up quark"; "Both… are drawn as a solid trefoil" |
| `predicted-spectra/electron-knot.lean` (docstring) | "the same knot type as the up quark" |
| `predicted-spectra/torus-knot-prime-powers.md` (lines 16, 31, 65) | "the same knot type encodes both the electron and the up quark" |
| `knots-particles-confinement/knot-particle-generation-table-data.md` | `T(2,3)`: "Electron / Up quark (gen. 1)" |
| `observations/building-block-knots-table1-data.md` | trefoil: "`e⁻` / `u` (up quark)" |
| `observations/strangelet-witten-stability.md` | "Up `𝔲` \| `T_{2,3}`" |
| `observations/strangelet-intro.md` | "the down quark `𝔡 = T_{2,3}^σ` carries three" crossings |
| `information-theory/jet-planck-particle-spectrum.md` | "up quark (`u = T_{2,3}`) and down quark (`d = T_{2,3}^σ`)" |
| `appendix-transfer-matrices/tm-knot-pairs.md` | "`K₁ = T_{2,3}` (up quark), `K₂ = T_{2,3}` (up quark)" |
| `appendix-transfer-matrices/tm-notation-table3-data.md` | "Up quark `𝔲` \| `T_{2,3}`" |
| `mass-theory/transfer-matrix-operator-properties.md` | `𝔲𝔲` row: `T_{2,3}`, `T_{2,3}` |
| `mass-theory/categorical-transfer-matrix-properties.md` | "a proton has `K₁ = K₂ = T_{2,3}` for two up quarks" |
| `predicted-spectra/linking-relations-table-table1-data.md`, `-table2-data.md` | `T_{2,3} ⊕ T_{2,3}` = "`𝔲𝔲` pair" |
| Lean `QOU/Archimedean/TorusKnot.lean:74` (docstring only) | "Electron / up quark: `e = τ(2,3)`" |

`brings-surface/cohomological-embedding-table2-data.md` puts `𝔲/𝔡` "on divisor" beside the trefoil
row. That is compatible with the descent reading and is not counted on either side.

### 1c. History

The clone is shallow, so dates come from the GitHub commits API on the pre-2026-09-27 paths.
Both texts predate every visible commit:

- `electron-knot.md`'s *"shares this knot type"* is present at `e32d978dbf` (2026-05-25), the
  chapter split that created `predicted-spectra/`.
- `up-quark.md`'s unknot text is present at `1b60cb2fa2` (2026-08-04). The dictionary's
  lepton-descent column is present by `def7c7da5e` (2026-08-01).
- The only edit to either definition since then is the voice sweep `f1d9e43002` (2026-11-20,
  impersonal voice), which did not touch the claim.

No PR or commit introduced either statement as a correction of the other. They look like two
models that were written side by side and never reconciled.

## 2. Is either one canonical?

**Owner ruling: none found.** I searched `docs/audits/` (2,738 files), `docs/coordination/`, the
beans mount, and this document's source `AGENTS.md`. Three items come close, and none rules on
this question:

- `docs/audits/2026-11-15-quark-equals-strand-implications.md` records the owner's *"try quark =
  strand"* (2026-11-15). That instruction was to **explore** a reading, not to adopt it. Under that
  reading a quark is one strand of a braid, and its closure is an unknot (§3).
- `docs/audits/2026-08-01-tau-knot-discussion-review.md` calls the Borromean-link baryon model
  (`observations/borromean-quark`) *"an established block"* that a competing assignment would
  have to displace. That is an agent's assessment, not an owner ruling.
- Bean `qou-ijnu` (scrapped) raised electron = trefoil against fermion = hyperbolic complement.
  It is a different clash.

**Sorry-free Lean that decides it: none.** Every Lean statement about either particle's knot type
is `rfl` on a **default field value** of a hand-written structure. Examples:
`up_quark_is_unknot : ({} : UpQuark).crossing_number = 0 := ⟨rfl, rfl⟩` and
`electron_crossing_number : ({} : Electron).crossing_number = 3 := rfl`. These theorems restate the
two assignments; they do not derive them. `KnotRegistry.lean` gives `trefoilEntry` the identity
`.electron` and has no quark entry.

**Producer that depends on it: none.** No file in `computations/` reads a quark's knot type. The
`up quark` hits are labels: `basis_knot_tables.py` names `σ₀` the "up quark channel", which agrees
with the unknot reading. None of the 14 trefoil-side blocks has a `computation` link, so no witness
moves under any option.

**So there is no canonical answer on record.** The unknot reading has more support in what defines
the particles (the definitions, the dictionary, the quark letters of the γγ work, the Lean
structures). The trefoil reading has more support in the tables and the transfer-matrix appendix.

## 3. A structural argument (scope b, given the Borromean reading)

`B₃ = (σ₀σ₁⁻¹)³` is a **pure braid**: its permutation is the identity. This is sorry-free Lean,
`QOU.Eightfold.borromean_perm_eq_one` and
`QOU.BraidsAndKnots.ComponentCountSelectivity.borromeanWord_components` (3 components).

Each component of a closed pure braid is the closure of one strand, after the other strands are
deleted. A 1-strand braid is trivial, so **every component is an unknot.**

Consequence: if the up quark is a component of the closed Borromean braid, as `def:up-quark`,
`categorical-proton` and `conj:borromean-quark` all say, it cannot be a trefoil. A trefoil needs at
least two strands (`σ³` in `B₂`).

The strand-deletion step is standard knot theory and is **not formalised** in this corpus. The
argument also binds only under the Borromean reading. If the paper drops "quark = component of
`B₃`", it no longer applies.

**Selection evidence I deliberately did not use.** `gluon-model-comparison.md` reports that the
unknot model "matches CODATA exactly" while trefoil quarks land "away from CODATA". Under §NO
FITTING, agreement with a target is not evidence for an identification. It plays no part in the
recommendation below.

## 4. The three "electrons" (context from PR #8673)

`def:electron-knot` is one of three distinct objects that the corpus calls the electron:

1. the trefoil `T(2,3)`, one component (`trefoil_one_component`);
2. the γγ normal-form word `e⁻ = σ₀σ₁σ₀`, whose closure in `B₃` has at least 2 components
   (`perm_e_gg`), so it is not the trefoil;
3. the strand electron of `LeptonStrandPremise.lean`, which is a weight vector, not a braid.

Every option below concerns only object 1 and its relation to the up quark. Unifying the three is
a separate owner question, framed in the #8673 body.

**Adjacent false comment, not a definition.** `computations/sdp_gamma_gamma_to_qqbar.py` lines 15
and 124 say *"σ₀σ₁σ₀ closes to a trefoil knot = electron"*. In `B₃` that contradicts `perm_e_gg`:
the word's permutation is a transposition, so the closure has 2 components. The trefoil is `σ₁³`
in `B₂`. Correcting the comment is "derived from the corpus" (exemption 2), but I have **not**
changed it here.

## 5. The options

### Option A — keep the unknot; reword `def:electron-knot` as descent (minimal)

**What it means.** The up quark stays an unknot. The electron block stops claiming a shared knot
type and says what the dictionary already says: the up quark's *lepton partner* is the trefoil.

**Exact edits** (3 files, no numbers, no Lean semantics):

`predicted-spectra/electron-knot.md`, paragraph 3, before:

> It shares this knot type with the up quark. Environment distinguishes them: the up quark threads
> a color tube on Bring's surface, while the electron orbits the nucleus via Hopf linking.

after:

> It is the lepton partner of the [up quark](#def:up-quark) in the
> [knot–particle dictionary](#rem:knot-particle-dictionary). The two do not share a knot type: the
> up quark is an unknot in a color tube on Bring's surface, distinguished by its positive crossing
> orientation in $\mathcal{B}_3$, while the electron is the trefoil and orbits the nucleus via Hopf
> linking.

paragraph 4, before:

> Both the electron and the up quark are drawn as a solid trefoil to denote the forward time
> direction. Context separates the lepton from the quark.

after:

> The electron is drawn as a solid trefoil to denote the forward time direction.

`predicted-spectra/electron-knot.lean`, module docstring, before:

> It is the same knot type as the up quark, but not localized in a color tube — it orbits the
> nucleus via Hopf linking.

after:

> It is the lepton partner of the up quark, which is an unknot localized in a color tube; the
> electron instead orbits the nucleus via Hopf linking.

`lean/QOU/Archimedean/TorusKnot.lean:74`, docstring, before: `Electron / up quark: e = τ(2,3) (trefoil).`
after: `Electron: e = τ(2,3) (trefoil); the up quark's lepton partner (the up quark itself is an unknot).`

`electron-knot.ts`: keep `uses: ["def:up-quark"]`; it is still referenced. Add
`"rem:knot-particle-dictionary"`.

- **Costs.** 4 files, about 10 lines. Lean change is docstrings only; verify with lean-direct
  (`-DautoImplicit=false -s 65536`). Render-QA, and a `qa-sweep` on the two touched blocks.
- **Risks.** Close to none in physics or numbers terms: no producer, witness or proof changes. It
  leaves the 13 other trefoil-side sites in §1b still contradicting `def:up-quark`. The clash is
  then no longer *between two definitions*, but the paper still says both things.
- **Commits to.** The unknot reading at the definition level. It does **not** settle what "lepton
  descent" means. The dictionary's `:refterm[descent]{#descent}` resolves to
  `lifting-and-descent/descent-involution`, the jet-level descent **homomorphism**
  `End(A_{n+1}) → End(A_n)`. No block shows that this map sends `T(2,3)` to the up quark. So the
  relation Option A leans on is a **name, not a derived map.** Option A should be read as
  "the trefoil is listed against the up quark", nothing stronger.

### Option B — Option A, plus the 13 trefoil-side sites reworded to descent

**What it means.** One reading throughout: quarks are unknots. Every `u = T(2,3)` / `d = T(2,3)^σ`
becomes `u ← T(2,3)`, i.e. "lepton partner", in the 13 sites of §1b.

- **Costs.** About 14 files across 6 chapters. The transfer-matrix appendix needs more than a
  relabel. `tm-knot-pairs`, `transfer-matrix-operator-properties` and
  `categorical-transfer-matrix-properties` build `𝔲𝔲` and `𝔲𝔡` pair matrices **from two trefoils**.
  Under B those matrices describe pairs of *lepton partners*, and their reading as proton–proton
  repulsion or proton–neutron binding loses its basis. They would need either rescoping as
  trefoil-pair mathematics or recomputing on single-crossing quark letters. `torus-knot-prime-powers`
  argues that the trefoil is *the common seed* of the electron and the up quark (line 31). That
  argument has to be rescoped to "seed of the lepton partner".
- **Risks.** It moves physics claims that a reader sees: the strangelet stability argument
  (`strangelet-witten-stability`, `strangelet-intro`, which counts 3 crossings for `𝔡` from
  `T_{2,3}^σ`) and the jet-step particle spectrum. No witness moves, because none is linked.
  Reversible, since it is prose.
- **Commits to.** The Borromean/strand quark model as the paper's quark model, and the
  torus-knot quark classification as a lepton-side table only. It forecloses using trefoil
  transfer matrices as quark–quark interaction terms unless they are re-derived.
- §ASK THE OWNER: this is a multi-chapter sweep and is **not exempt**. It needs an explicit yes.

### Option C — make the trefoil canonical; rewrite the quark definitions

**What it means.** The up quark is `T(2,3)` and the down quark is `T(2,3)^σ`. Rewrite
`def:up-quark` and `def:down-quark`, `ParticleKnots.UpQuark/DownQuark` (`crossing_number 0 → 3`,
`genus 0 → 1`), the dictionary, `categorical-proton`, `hadron-proton-example`, `borromean-quark`,
`particle-nf-table`, `gluon-model-comparison`.

- **Costs.** At least 13 sites in §1a plus Lean structure changes, with consumers to re-verify.
- **Risks.** Collides with the pure-braid fact (§3): a trefoil cannot be a component of the closed
  `B₃`. So C requires **giving up the Borromean quark model** (`conj:borromean-quark`), the
  single-letter quark words of the γγ work (`σ₀`, `QuarkBraidChargeObstruction.upQuark = [1]`) and
  the quark = strand exploration. It also reopens the `qou-ijnu` question (a trefoil is a torus
  knot, volume 0).
- **Commits to.** A different baryon model. That would be the paper's largest structural change
  since the convention-D ruling.

### Option D — no-op (the default)

**What it means.** Nothing changes. `def:electron-knot` keeps citing `def:up-quark` while
contradicting it, and both readings stay live across six chapters.

- **Costs.** None now.
- **Risks.** A referee who reads the electron and up-quark definitions finds the contradiction
  within two pages of each other. Agents keep building on whichever reading they find first, as
  happened with the transfer-matrix appendix.
- **Commits to.** Nothing. It is safe to defer: no number, witness or proof depends on the choice.

### Recommendation (my judgement, not a finding)

**A now, and B as a separate decision.** A removes the contradiction between the two *definitions*
at almost no cost, and it agrees with the side that has the structural argument (§3), the
dictionary, and the Lean structures. B is the honest end state if the Borromean model stands, but
it rescopes the transfer-matrix appendix and the strangelet argument, and those are owner calls in
their own right. I would not take C unless the Borromean quark model is being abandoned for other
reasons.

Separately, in any option: the meaning of "lepton descent" is undefined (it borrows a glossary slug
for a different map). That should be a bean, not a silent edit.

## 6. What this document does not establish

- The graph search was seeded on three queries only. Prior work phrased in other words may still exist.
- The strand-deletion argument in §3 is not formalised in Lean.
- The list in §1b came from greps on `T_{2,3}`, "trefoil" and "up quark" near each other. A block
  that calls the up quark a trefoil in other words, e.g. through `3_1` alone or a figure, would not
  appear.
