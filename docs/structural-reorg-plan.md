# Structural reorg — proposal

Applies the [structural framework](structural-framework.md) (P1–P6) to
the live corpus. Staged and audit-gated; **not** a single commit. The
audit (`content/pipeline/qa-section-title-audit.ts`) gates each stage:
23 title hard-defects, 75 structure findings at time of writing.

## Stage 0 — infra prerequisites

Every pipeline component that walks `sections[].blocks[]` must also walk
`subsections[].blocks[]`. The worked example (Stage 1, confinement)
surfaced three — two were real gaps, one was already fine:

1. **Renderer** — ✅ done. `render-latex.ts` now emits `\subsection{}`
   for L3 nodes (the `book`/`report` class already numbers them).
2. **Content validator** — ✅ done. `validate.ts` now loads subsection
   blocks; otherwise every `uses:` / `interprets:` / cross-ref to a
   nested block breaks (**39 errors** before the fix → `✓ Valid` after).
3. **Detangler (P6)** — already correct. `loadChapterGraph` builds the
   reading-order positions by regex-matching *every* `blocks: [...]`
   array in source order, which already includes subsection blocks after
   their parent — so `detangler-no-forward-ref` sees the right order.
   (`detangler-section-band` treats each subsection as a section, band
   3–18 vs the 2–12 we want — a minor over-strictness, refine later.)

**Lesson:** subsections are a cross-cutting change. Any *other*
`sections[]` walker (build, glossary, blueprint export) needs the same
recursion — audit them before the corpus-wide pass.

## Stage 1 — fold the 23 `" : <tag>"` artifacts into subsections

Each split-off section becomes a **subsection of its base**, titled
short + parent-scoped (read *under* the base). Section labels are not
prose-cross-referenced, so this is label-safe; `.qa.json` sidecars
regenerate.

| Base section (keeps its title) | → new subsection title |
|---|---|
| Confinement operator selection | SDP vs LP |
| Transfer matrices and beta decay | Spectral $Q_\beta$ |
| Skein Generation and Particle Correspondence | The knot–particle dictionary |
| Markov axioms and braid-link enumeration | Bar symmetry of the $c_k$ · The Markov closure map |
| The Quantum Universe | Frobenius-pairing uniqueness |
| Descartes condition: … genus completeness | The genus ideal |
| Mass predictions: methodology and validation | vs Feynman amplitudes |
| Mass predictions: per-particle derivations | Terminal resolution |
| Beta decay: mechanism, half-life, and tritium | Hadron half-life |
| Beta decay: magic-shell consequences | The $k{=}12$ barrier |
| Hoefsmit convergence: construction | Per partition |
| (Plancherel-$\alpha$ spectral foundations) | $\alpha_k$ for atom-knot mass |
| Spectral sequence, chirality, confinement-NF | Per-nucleon shift |
| Wenzl bridge, cyclotomic factorisation, $\alpha_k$ | LR tensor character |
| Parity classification, atomic atlas, discrepancy | Proton partition-sum residual |
| Six-term mass formula, crystal, isospin, chirality | Option-E isospin |
| Mesons and nucleons | Proton uniqueness |
| EM completeness and gauge coupling | Hartree $\alpha_{EM}$ |
| Archimedean Hartree, crystal basis, Mathlib bridge | Mass tower · Categorical $\alpha_{EM}$ |
| Nuclear stability and decay | Hadron half-life |
| Atomic shells: construction foundations | Skein finiteness |

Two bases (`Markov axioms…`, `Archimedean Hartree…`) collect **two**
subsections — so they satisfy P2 (≥ 2 children). The bases whose own
titles are compound (mass-theory, predicted-spectra) are shortened per
the [title conventions](../.claude/skills/local/one-voice-style-guide.md)
in the same edit (e.g. "Six-term mass formula, crystal, isospin, and
chirality" → "The six-term mass formula").

## Stage 2 — split over-weight sections (P4)

Sections > 2.5× their chapter's peer mean — split each into ≥ 2
subsections along a dependency-respecting cut (P6):

- `quantum-observable-universes` › **Emergence** (`sec:emergence`)
- `appendix-mass-binding-algorithms` › **Canonical chain** (`sec:mba-canonical-chain`)
- `glossary` › **Rigidity** (`sec:glossary-rigidity`)
- `braids-and-knots` › **Categorical braiding / Hecke eigenbasis**
- `appendix-surreals` › **Survives/breaks**, **Millennium bounds**

The cut points come from the blocks' `uses[]` clusters (the natural
sub-arcs), read off `content-graph-analysis.py` so no subsection
boundary crosses a backward edge.

## Stage 3 — bands + only-children (P2/P3)

- **only-child:** `index-of-definitions` is a 1-section chapter →
  flatten the section away (chapter holds the blocks directly) or split.
- **under-band sections** (< 3 blocks): mostly chapter intros /
  notation. Treat single-purpose *intro* and *notation/preview*
  sections as **exempt** from the floor (they are navigational, not
  content arcs) — a refinement to add to P3; otherwise merge the stray
  small sections into a neighbour.

## Order of operations (per chapter)

1. Run the audit on the chapter; read its `uses[]` graph.
2. Fold artifacts (Stage 1) → re-run `detangler` (recursed) → 0 new
   backward edges.
3. Split over-weight (Stage 2) along graph clusters.
4. Retitle to short + parent-scoped.
5. Audit must exit 0 (titles + structure) before the chapter is done.

The per-chapter audit exit code is the done-gate for the whole pass.
