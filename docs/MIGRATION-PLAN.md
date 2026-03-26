# LaTeX → Content Object Migration Plan

## Current State

- **Infrastructure**: Complete (schema, builders, validation, rendering pipeline)
- **Migrated**: 3 of 251 formal objects (Ch1: `ch1-intro`, `rigid-monoidal-category`, `rigid-monoidal-vect`)
- **Paper manifest**: exists, references Ch1 only (Ch2, Ch3 commented out)

## Strategy

### Ordering: Chapter 1 first, then dependency order

Chapter 1 contains all foundational definitions (28 defs, 32 examples, 6 props,
2 lemmas, 1 theorem, 16 remarks). Every later chapter `uses` Ch1 objects.
Complete Ch1 first, then proceed through Ch2–Ch7 (the mathematical core),
then Ch11 (experimental), skipping empty chapters (8–10, 12).

### Per-block migration procedure

For each LaTeX environment (`\begin{definition}...`):

1. **Create `<block-name>.ts`** — call the appropriate builder (`definition()`,
   `theorem()`, etc.) with label, title, lean ref, status, uses, tags
2. **Create `<block-name>.md`** — extract body from LaTeX, convert to markdown:
   - `\textbf{...}` → `**...**`
   - `\emph{...}` → `*...*`
   - `\hyperref[label]{text}` → `[text](#label)`
   - Keep `$...$` and `$$...$$` math as-is
   - Keep `\begin{tikzcd}`, `\begin{align}` etc. in ` ```tex ` fenced blocks
   - For theorems with proofs: put proof after `---` separator
3. **Register in chapter manifest** — add block name to appropriate section's
   `blocks[]` array
4. **Validate** — run `bun run content/pipeline/validate.ts`
5. **Build** — run content build and verify LaTeX output matches original

### Naming convention

Block names = label without prefix, kebab-case:
- `\label{def:quantum-universe}` → `quantum-universe.ts` / `.md`
- `\label{thm:emergence-gauge-group}` → `emergence-gauge-group.ts` / `.md`
- `\label{rem:tannaka-krein}` → `tannaka-krein.ts` / `.md`

---

## Phase 1: Complete Chapter 1 (82 remaining blocks)

### Section 1.1: Introduction
Already done: `ch1-intro` (prose)

### Section 1.2: Rigid monoidal categories
Already done: `rigid-monoidal-category` (def), `rigid-monoidal-vect` (example)

Remaining Ch1 blocks to migrate (in document order):

#### Definitions (27 remaining)
1. `quantum-universe` — def:quantum-universe
2. `higher-differential-forms` — def:higher-differential-forms
3. `quantum-observable-universe` — def:quantum-observable-universe
4. `involutive-structure` — def:involutive-structure
5. `positive-definite-structure` — def:positive-definite-structure
6. `spin-labels` — def:spin-labels
7. `maximal-torus` — def:maximal-torus
8. `weight-decomposition` — def:weight-decomposition
9. `categorical-reeb-derivation` — def:categorical-reeb-derivation
10. `projective-line-object` — def:projective-line-object
11. `categorical-connection-curvature` — def:categorical-connection-curvature
12. `categorical-jet-object` — def:categorical-jet-object
13. `categorical-hodge-star` — def:categorical-hodge-star
14. `substrate-parameter` — def:substrate-parameter
15. `quantum-gauge-group` — def:quantum-gauge-group
16. `quantum-planck-constant` — def:quantum-planck-constant
17. `q-hodge-star` — def:q-hodge-star
18. `categorical-action` — def:categorical-action
19. `categorical-q-exterior-derivative` — def:categorical-q-exterior-derivative
20. `particle` — def:particle
21. `fermion-boson-decomposition` — def:fermion-boson-decomposition
22. `categorical-point` — def:categorical-point
23. `observation` — def:observation
24. `categorical-instanton` — def:categorical-instanton
25. `categorical-q-lie-bracket` — def:categorical-q-lie-bracket
26. `categorical-q-connection` — def:categorical-q-connection
27. `q-weighted-yang-mills-levi` — def:q-weighted-yang-mills-levi

#### Theorem (1)
28. `emergence-gauge-group` — thm:emergence-gauge-group

#### Lemmas (2)
29. `volume-form-rigidity` — lem:volume-form-rigidity
30. `irreducibility-observability` — lem:irreducibility-observability

#### Propositions (6)
31. `frobenius-relation` — prop:frobenius-relation
32. `fiber-adjoint-fiber-involution` — prop:fiber-adjoint-fiber-involution
33. `variational-equations` — prop:variational-equations
34. `categorical-self-duality` — prop:categorical-self-duality
35. `non-vanishing-dq2` — prop:non-vanishing-dq2
36. `main-commutative-diagram` — prop:main-commutative-diagram

#### Remarks (16)
37–52. All remark blocks (base-ring-independence, tannaka-krein, etc.)

#### Examples (31 remaining)
53–83. All example blocks (su2-quantum-universe, su2-higher-forms, etc.)

### Chapter 1 section structure

The chapter manifest needs to be expanded with sections matching the LaTeX
`\section{}` structure. Blocks are assigned to sections in document order.

---

## Phase 2: Chapter 2 — QOU Elaboration (20 blocks)

- 3 definitions, 4 propositions, 13 remarks
- Create `ch2-qou-elaboration/` directory + chapter manifest
- Register in paper manifest

## Phase 3: Chapter 3 — Lifting of Quantum Torsion (47 blocks)

- 9 definitions, 2 theorems, 1 lemma, 10 propositions, 3 corollaries, 21 remarks, 1 example
- Largest single migration batch after Ch1

## Phase 4: Chapter 4 — Path Integrals and Braiding (24 blocks)

- 7 definitions, 2 propositions, 14 remarks, 1 example

## Phase 5: Chapter 5 — Bring's Surface (37 blocks)

- 6 definitions, 3 propositions, 28 remarks

## Phase 6: Chapter 6 — Descartes Universe (17 blocks)

- 3 definitions, 1 theorem, 1 proposition, 1 corollary, 10 remarks, 1 example

## Phase 7: Chapter 7 — p-Adic Quantum Groups (5 blocks)

- 1 definition, 1 proposition, 1 remark, 2 examples

## Phase 8: Chapter 11 — Experimental Evidence (16 blocks)

- 3 propositions, 13 remarks

## Phase 9: Empty chapters (8, 9, 10, 12)

- Create chapter directories and manifests with prose-only blocks
- No formal objects to migrate

---

## Execution approach

Each chapter migration should be done as a single session:

1. Read the full LaTeX chapter
2. Create chapter directory + manifest `.ts`
3. Create all block `.ts` + `.md` files
4. Register chapter in paper manifest
5. Run validation (`content_validate`)
6. Run build (`content_build`)
7. Verify generated `.tex` against original
8. Commit

### Batch size recommendation

- **Definitions**: migrate in groups of 5–10 with their associated examples
- **Remarks**: can be batched more aggressively (10–15 at a time)
- **Theorems/propositions with proofs**: one at a time (proofs need careful conversion)

### Validation checkpoints

After each batch:
```bash
bun run content/pipeline/validate.ts
bun run content/pipeline/build.ts
```

Compare generated `chapters/*.tex` with originals using `diff`.

---

## Estimated scope

| Phase | Chapter | Blocks | Files to create |
|-------|---------|--------|-----------------|
| 1 | Ch1 | 82 | ~164 (.ts + .md) |
| 2 | Ch2 | 20 | ~40 |
| 3 | Ch3 | 47 | ~94 |
| 4 | Ch4 | 24 | ~48 |
| 5 | Ch5 | 37 | ~74 |
| 6 | Ch6 | 17 | ~34 |
| 7 | Ch7 | 5 | ~10 |
| 8 | Ch11 | 16 | ~32 |
| 9 | Ch8–10,12 | 0 | ~8 (manifests) |
| **Total** | | **248** | **~504 files** |
