# GitHub Copilot — Authoring Instructions for *Quantum Observable Universe*

These instructions apply to all LaTeX source files in this repository.
Follow them precisely when generating, completing, or refactoring content.

---

## 0  Response Discipline

This is a formal mathematics paper.  Copilot **must**:

- **Only make the change explicitly requested.**  Do not add sections,
  subsections, content, environments, or prose unless specifically asked.
- **Keep all changes minimal and concise.**  Surgical edits only.
- **Do not hallucinate.**  Never introduce definitions, theorems, examples,
  citations, or any mathematical content that was not explicitly requested.
- **Do not create new `\section` or `\subsection` headings** unless the
  user's request explicitly asks for them.

---

## 0a  Precision Goals (STRICT — read before precision-affecting changes)

The framework's headline precision goal has **two independent legs** —
read [`docs/precision-goals.md`](../docs/precision-goals.md) for the full
specification. Summary:

- **L1. Compute precision** — internal cross-method agreement ≤ 1 ppb at
  substrate q_0. Trivially met (`_precision.py` default 50 dps).
- **L2. Per-observable accuracy** — for each predicted observable O,
  `σ_pred(O) ≤ σ_exp(O) / 100` ("100× more precise than experimental").
  Variable per observable; **partial** (1/6 currently meets target).

Status witnesses:

- L1: `folio-assistant/computations/onepb-status-dashboard.witness.json`
- L2: `folio-assistant/computations/per-observable-100x-status.witness.json`

Never say "1 ppb met" without specifying *which leg*. L1 ≠ L2.

## 1  Guiding Philosophy

Model every chapter on the style of a rigorous graduate mathematics textbook —
specifically the structured, definition-first approach of Herrlich's
*Category Theory* (Sigma Series in Pure Mathematics, Heldermann Verlag).

The key principles are:

1. **Every named item carries a unique, human-readable label.**  Nothing is
   anonymous.  Theorem, definition, lemma, example, equation — all are
   labeled and referenceable.
2. **Structure precedes prose.**  Introduce a concept through a formal
   definition before discussing it in running text.
3. **Definitions are immediately grounded by examples.**  Every non-trivial
   definition is followed by at least one concrete example.
4. **Theorems are immediately followed by proofs** (or an explicit
   `% TODO: proof` comment if the proof is deferred).
5. **Cross-references, not repetition.**  Refer back to earlier items by
   label; do not restate them in full.

---

## 2  Document-Class and Preamble

- Use `\documentclass[12pt,a4paper]{report}`.
- Theorem environments are declared in `main.tex` and shared across all
  chapters.  Do **not** redeclare them inside chapter files.
- The canonical set of theorem environments (all sharing a single counter
  chained to `[chapter]`) is:

  | Environment   | Display name   |
  |---------------|----------------|
  | `theorem`     | Theorem        |
  | `lemma`       | Lemma          |
  | `proposition` | Proposition    |
  | `corollary`   | Corollary      |
  | `definition`  | Definition     |
  | `example`     | Example        |
  | `remark`      | Remark         |
  | `conjecture`  | Conjecture     |

  If a new environment type is required, add it to the preamble of
  `main.tex` following the same pattern:
  ```latex
  \newtheorem{<env>}[theorem]{<Display Name>}
  ```

---

## 3  Labeling Convention

Every `\chapter`, `\section`, theorem environment, and numbered equation
**must** carry a `\label{}`.  Use the prefixes below — consistently and
without exception.

| Item type              | Prefix    | Example key              |
|------------------------|-----------|--------------------------|
| Chapter                | `chap:`   | `chap:torsion`           |
| Section                | `sec:`    | `sec:quantum-torsion`    |
| Subsection             | `ssec:`   | `ssec:leibniz-rule`      |
| Definition             | `def:`    | `def:quantum-connection` |
| Theorem                | `thm:`    | `thm:lifting-exists`     |
| Lemma                  | `lem:`    | `lem:torsion-skew`       |
| Proposition            | `prop:`   | `prop:cstar-states`      |
| Corollary              | `cor:`    | `cor:unique-lifting`     |
| Example                | `ex:`     | `ex:flat-connection`     |
| Remark                 | `rem:`    | `rem:cstar-norm`         |
| Conjecture             | `conj:`   | `conj:phase-shift`       |
| Equation / align block | `eq:`     | `eq:schrodinger`         |
| Figure                 | `fig:`    | `fig:torsion-diagram`    |
| Table                  | `tab:`    | `tab:interp-comparison`  |

### 3.1  Placement of `\label`

- For chapters and sections: immediately on the line after the heading macro.
- For theorem environments: as the **first** line inside the environment body
  (before any prose), unless a descriptive title is given in `[…]` — in
  that case, place it on the second line.
- For equations: at the end of the last line inside the `equation` /
  `align` environment, before `\end`.

```latex
% ── Correct placement examples ────────────────────────────────────────────────

\section{Quantum Torsion}
\label{sec:quantum-torsion}

\begin{definition}[Quantum Connection]
  \label{def:quantum-connection}
  A \emph{quantum connection} on a Hilbert bundle …
\end{definition}

\begin{theorem}[Existence of Torsion Lifting]
  \label{thm:lifting-exists}
  Under suitable curvature conditions …
\end{theorem}

\begin{equation}
  \mathcal{T}^\nabla(X,Y) = \nabla_X Y - \nabla_Y X - [X,Y].
  \label{eq:torsion-def}
\end{equation}
```

---

## 4  Cross-References

- Always use a non-breaking space before a reference macro:
  `Theorem~\ref{thm:lifting-exists}`, `Definition~\ref{def:quantum-connection}`.
- Use `\eqref{…}` (not `\ref{…}`) for equation references:
  `equation~\eqref{eq:schrodinger}`.
- Use the capitalized form when the reference begins a sentence or clause
  (`Theorem~\ref{…}`), and the lower-case form mid-sentence only after the
  word "see" or in parenthetical asides: `(see theorem~\ref{…})`.
- Ranges: `Chapters~\ref{chap:qou}--\ref{chap:interpretations}`.

---

## 5  Chapter Skeleton

Every chapter must follow this skeleton (sections may be subdivided further):

```latex
\chapter{<Title>}
\label{chap:<slug>}

% ── 1. Introduction ────────────────────────────────────────────────────────────
\section{Introduction}
\label{sec:<slug>-intro}
% Motivate the chapter; state what will be proved or defined.

% ── 2. Definitions ─────────────────────────────────────────────────────────────
\section{<Primary Concept>}
\label{sec:<slug>-<concept>}
% Pattern: Definition → Example → Remark (if needed)

\begin{definition}[…]
  \label{def:…}
  …
\end{definition}

\begin{example}
  \label{ex:…}
  …
\end{example}

% ── 3. Main Results ────────────────────────────────────────────────────────────
\section{<Results / Theorems>}
\label{sec:<slug>-results}
% Pattern: Lemma (if needed) → Theorem → Proof → Corollary (if applicable)

\begin{lemma}
  \label{lem:…}
  …
\end{lemma}
\begin{proof}
  …
\end{proof}

\begin{theorem}[…]
  \label{thm:…}
  …
\end{theorem}
\begin{proof}
  …
\end{proof}

% ── 4. Summary ─────────────────────────────────────────────────────────────────
\section{Summary}
\label{sec:<slug>-summary}
% One paragraph listing what was defined/proved and pointers to next chapter.
```

---

## 6  Theorem-Environment Style Rules

1. **Title field `[…]` is mandatory** for `definition`, `theorem`,
   `proposition`, `lemma`, and `conjecture`.  It is optional for `remark`,
   `example`, and `corollary`.
2. Body text is **indented two spaces** inside every environment.
3. Inline mathematics uses `$…$`; displayed, numbered mathematics uses the
   `equation` or `align` environment — **never** `$$…$$`.
4. A `definition` body states existence/membership conditions precisely; it
   does **not** contain motivating prose (move that to a following `remark`).
5. A `theorem` / `lemma` / `proposition` body states hypotheses first, then
   conclusion:  *"Under [hypotheses], [conclusion]."*
6. An `example` body starts with a concrete instantiation; it may include a
   short computation, but should close with a sentence linking back to the
   definition it illustrates.
7. Every `theorem` and `lemma` is immediately followed by `\begin{proof}…\end{proof}`;
   if the proof is incomplete, write:
   ```latex
   \begin{proof}
     % TODO: complete the proof.
   \end{proof}
   ```

---

## 7  Prose Style

- Write in formal academic English; avoid contractions, colloquialisms, and
  first-person singular ("I").  Use "we" for author–reader joint reasoning.
- Sentences end with two spaces.  (LaTeX ignores the extra space in text
  mode, but it aids source readability.)
- Introduce every new technical term with `\emph{…}` on first use within a
  chapter; do not re-emphasise on subsequent uses.
- Acronyms are introduced as `\emph{Full Name} (ACRONYM)` and thereafter
  used bare.
- Use the Oxford comma.
- Avoid starting a sentence with a mathematical symbol.  Write
  *"The operator $\hat{H}$ is …"* not *"$\hat{H}$ is …"*.
- Displayed equations that end a sentence carry a period inside the
  `equation` environment; those mid-sentence carry a comma.

---

## 8  Comment Conventions in Source Files

Use section-separator comments of the form:

```latex
% ── <Section title> ───────────────────────────────────────────────────────────
```

Use `% TODO: <description>` for incomplete content.  Keep TODO comments on
their own line, indented to match the surrounding content.

---

## 9  File Organisation

| Path                       | Purpose                                      |
|----------------------------|----------------------------------------------|
| `main.tex`                 | Preamble, metadata, document structure only  |
| `chapters/<title-slug>.tex`| One file per chapter, named after chapter title; no preamble content |
| `references.bib`           | BibTeX database; one entry per source        |

- Do **not** place `\usepackage`, `\newtheorem`, or `\geometry` calls inside
  chapter files.
- Chapter files contain only `\chapter`, `\section`, environments, and
  prose.

---

## 10  Bibliography

- Cite with `\cite{key}` inside running text: *"…as shown by Smith~\cite{smith2001}."*
- Every claim labelled as a theorem or proposition that relies on an
  external result must carry a citation.
- BibTeX keys follow the pattern `<firstauthorlastname><year>` (all
  lower-case), e.g., `herrlich2006`, `einstein1905`.
- **Bibliography QA**: Run `cd content && bun run pipeline/bib-qa.ts` to
  generate `bib-qa.json` with per-reference quality tags.  View results
  at `/folio/bib-qa.html`.  Every reference is scored 0–5 on: URL
  presence, URL resolution + content match, metadata completeness,
  citation coverage, and screenshot evidence.
- **Screenshots**: For references whose cited result (theorem, figure,
  table) is critical to the paper, save a screenshot to
  `content/bib-qa-images/<refid>.png`.

---

## 11  Notation Conventions

### 11.0  Glossary terms — `\defterm{}` / `\refterm{}` (Phase A)

Every term that appears in the paper's glossary is wrapped at every
occurrence — defining and referencing alike. **Never use plain text or
`\emph{}` for a defined term once the term is registered in a block's
`defines: [...]` list.**

- **Defining occurrence** (exactly one per term, in the block whose
  `defines[]` contains the slug):
  - LaTeX: `\defterm{slug}` or `\defterm{slug}{Visible}` when the
    visible label differs from the slug.
  - Markdown (`.md` files): `:defterm[Visible]` (slug = sluggified
    label) or `:defterm[Visible]{#slug}` (explicit slug).
- **Referencing occurrence** (every other mention, anywhere in the
  paper):
  - LaTeX: `\refterm{slug}` / `\refterm{slug}{Visible}`.
  - Markdown: `:refterm[Visible]` / `:refterm[Visible]{#slug}`.
- **PDF rendering** is intentionally clean — `\defterm` is bold-italic,
  `\refterm` is plain text with an invisible hyperlink target
  (`\phantomsection\label{term:slug}` → `\hyperref[term:slug]{...}`).
  No marginal anchors, no underlines.
- **HTML viewer** carries the affordance: `\defterm` becomes
  `<dfn id="term-slug">`, `\refterm` becomes `<a class="termref"
  href="#term-slug">` with a dotted underline on hover/focus and a
  click-to-jump to the canonical entry.
- The schema field `defines?: string[]` on `BlockBase` registers the
  slugs introduced by a block. Phase B validators will enforce
  declaration/coverage; for now the field is informational only.

Discovery and audit go through proper AST processing
(`remark-directive` for `.md`, `unified-latex` for `.tex`) — never
grep over raw source.

### 11.1  Prime Numbers vs. Manifold Points

- **Prime numbers** are typeset in Fraktur:  use the macro `\pp` (defined as
  `\mathfrak{p}` in `main.tex`).
  Examples:  `$\pp$-adic`, `$\mathbb{Q}_\pp$`, `$\mathbb{F}_\pp$`.
- **Points on the manifold** use bare italic $p$:  `$p \in M$`.
- In `\chapter` and `\section` titles that contain `\pp`, wrap the math in
  `\texorpdfstring{$\pp$}{p}` so that PDF bookmarks remain plain text.

### 11.2  Vectors

- All vector quantities must carry a **half-arrow** accent:  use `\vec{…}`.
  Examples:  `$\vec{q}$`, `$\vec{v}$`, `$\vec{X}$`.
- This distinguishes vector-valued quantities from scalar parameters
  (e.g.\ the substrate parameter $q$ from a vector $\vec{q}$).
- Do **not** use bold (`\mathbf`) for vectors; reserve bold for operator
  names (e.g.\ `$\mathbf{E}$` for the Euler–Lagrange operator) and
  **categories** (see §11.3).

### 11.3  Category and Functor Notation (Herrlich–Strecker conventions)

Following Herrlich–Strecker, categories are set in **bold upright**:

| Object | Notation | Example |
|--------|----------|---------|
| Generic category | `$\mathbf{C}$` | $\mathbf{C}$ |
| Named categories | bold name | `$\mathbf{Rep}(\mathrm{SU}_q(2))$`, `$\mathbf{Mod}_R$` |
| Monoidal unit | `$\mathbf{1}$` | (unchanged) |
| Forgetful/fibre functor | `$\tau$` | Kept for Tannakian/trace/proper-time resonance (see `tau-notation.md`); minimise its appearance |
| QOU categorical datum | `$(\mathbf{C}, A)$` | Suppress $\tau$ from the triple where possible; write $(\mathbf{C}, A, \tau)$ only when $\tau$ is needed |
| QOU archimedean tuple | `$(\mathbf{C}, \varTheta, G, \mathcal{S})$` | **Canonical 4-tuple.** $M$ (base manifold) is subordinate to $\varTheta$ (its domain); $P$ (principal bundle) is subordinate to $\mathcal{S}$ (its associated state bundle under $G$). Old 5-tuple $(M, \varTheta, G, P, E)$ is **deprecated**. |
| State bundle | `$\mathcal{S}$` | The associated state bundle $\mathcal{S} = P \times_G \mathbb{CP}^1(\mathbb{C}) \to M$; replaces $E$. Fibre at $p$: `$\mathcal{S}_p$` (never `$E_p$`). |
| Elliptic curve | `$\mathcal{E}_q$` | Descartes elliptic curve (never `$E_q$`). |
| Particles | fraktur | Quarks: `$\mathfrak{u}, \mathfrak{d}, \mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}$`. Nucleons: `$\mathfrak{p}, \mathfrak{n}$`. |
| Energy | fraktur | `$\mathfrak{E}_q$` ($q$-energy), `$\mathfrak{E}_\times$` (crossing), `$\mathfrak{E}_{\mathrm{bind}}$` (binding). |
| Color | plain italic | `$c$` (vector), `$c_r, c_g, c_b$` (tube coords), `$\hat{c}_r$` (chromaticity). |
| Proton number | `$Z$` | Atomic number (standard nuclear convention). Never use `$p$` for proton count. |
| Julia-set measure | `$\mu_J$` | Standard measure notation. |
| Hom-spaces | `$\mathrm{Hom}_{\mathbf{C}}$` | Bold subscript matches the category |
| Tensor product | `$\otimes$` | (unchanged) |
| Dual object | `$V^{\vee}$` | Mathlib convention; equivalent to $V^*$ |
| Associator, unitors | `$\alpha, \lambda, \rho$` | Mac Lane / Mathlib convention |
| Braiding | `$\sigma_{X,Y}$` | (unchanged) |

**Do not use** `$\mathcal{C}$` (calligraphic) for categories. Calligraphic
letters are reserved for sheaves, sites, algebras, bundles, and curves
(`$\mathcal{S}$` = state bundle, `$\mathcal{E}_q$` = elliptic curve,
`$\mathcal{O}$`, `$\mathcal{A}$`).

**Numerical substrate values** (`$q = 1.1097$` etc.) **must not appear**
outside the introduction and Chapter 7 (Physical Observations).
Geometry chapters use symbolic `$q$`.

**Subordination rules for the archimedean tuple:**
- $M$ is implicit — it is the domain of $\varTheta$. Write `$p \in M$` when
  referring to points, but do not list $M$ in the tuple.
- $P$ is implicit — it is the frame bundle of $\mathcal{S}$ under $G$.
  Mention $P$ only when discussing gauge structure directly.
- The old 5-tuple $(M, \varTheta, G, P, E)$ must not appear in new content.
  Existing occurrences should be migrated to $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

Where physics notation is more natural than category-theoretic notation
(e.g.\ differential operators $d_q$, $\nabla$, $\star_q$, $\xi$),
prefer the physics convention.

---

## 12  Using Skills for Content Changes

This repository subscribes to external skill packages (see `skills-config.json`).
Synced skills live under `.claude/skills/<package>/` while repo-specific skills
live under `.claude/skills/local/`.

When **writing or editing manuscript content**, apply the following skills:

| Task | Skill(s) to consult |
|------|---------------------|
| Writing new sections or chapters | `local/scientific-accuracy`, `local/readability-editing`, `claude-scientific-skills/scientific-writing` |
| Reviewing or revising text | `local/readability-editing`, `claude-scientific-skills/peer-review`, `claude-scientific-skills/scientific-critical-thinking` |
| Adding or verifying references | `local/bib-qa`, `local/scientific-accuracy`, `claude-scientific-skills/citation-management`, `claude-scientific-skills/arxiv-database` |
| Bibliography QA dashboard | `local/bib-qa` |
| Generating figures or plots | `claude-scientific-skills/scientific-visualization`, `claude-scientific-skills/matplotlib` |
| Verifying equations or proofs | `local/scientific-accuracy`, `claude-scientific-skills/sympy` |
| Citing substrate-derived numerical values | `local/witnessed-values`, `local/content-validation` |
| Auditing compute scripts for speedup opportunities | `local/compute-audit` |
| Validating LaTeX syntax | `local/latex-validation` |
| Brainstorming new research directions | `claude-scientific-skills/hypothesis-generation`, `claude-scientific-skills/scientific-brainstorming` |
| Literature search | `claude-scientific-skills/literature-review`, `claude-scientific-skills/arxiv-database` |

| Generating or updating Lean stubs | `local/lean-generation` |
| Reviewing Lean proofs | `local/lean-proof-review` |
| Tracking proof formalization status | `local/proof-status-tracking` |

When **writing or editing Lean formalization code**, apply the following:

| Task | Skill(s) to consult | Key signals in user request |
|------|---------------------|-----------------------------|
| Filling `sorry` with proofs | `local/formalizer`, `local/category-theory` | "fill in", "prove", "remove sorry" |
| Adding new structures/defs | `local/formalizer`, `local/lean-generation` | "define", "formalize", "add structure" |
| Diagram chasing / naturality | `local/category-theory` | "commutes", "diagram", "naturality", "functor" |
| Monoidal / braided constructions | `local/category-theory` | "monoidal", "tensor", "braiding", "Hopf", "Frobenius" |
| Extracting theorems from LaTeX | `local/lean-generation` | "extract", "stub", "from LaTeX", "from chapter" |
| Reviewing Lean changes (PR) | `local/lean-proof-review` | "review", "check", "audit" |
| Updating proof-objects.json | `local/proof-status-tracking` | "status", "tracking", "manifest" |
| Ontology / type resolution | `local/ontologist` | "glossary", "type", "resolve", "naming" |
| Knot-theoretic formalization | `local/category-theory` (§Knot Theory) | "knot", "crossing", "Jones", "volume" |
| Triage: what to prove next | `local/proof-triage` | "what next", "priority", "triage", "roadmap" |

### Skill routing decision tree (for agents)

When a user request arrives, apply this decision tree to select skills:

1. **Does it touch `chapters/*.tex`?** → consult LaTeX skills (§12 table above)
2. **Does it touch `lean/QOU/*.lean`?**
   a. **Writing new Lean code** → `local/formalizer` + `local/category-theory`
   b. **Reviewing existing Lean code** → `local/lean-proof-review`
   c. **Generating stubs from LaTeX** → `local/lean-generation`
   d. **Updating manifests** → `local/proof-status-tracking`
3. **Does it touch both LaTeX and Lean?** → also consult `local/lean-generation`
   for cross-referencing (`\lean{}`, `\leanok`, `\uses{}`)
4. **Is it a research/brainstorming question?** → synced scientific skills
5. **Ambiguous?** → read the relevant skill `.md` files, then ask the user

**Rules:**
- Always apply `local/latex-validation` before finalizing any LaTeX change.
- Always apply `local/scientific-accuracy` when modifying mathematical content.
- Consult the synced skills proactively — do not wait to be told.
- If a synced skill directory contains a `SKILL.md`, read it for detailed
  instructions specific to that tool or database.

## 13  Lean Formalization & Proof Linkages

This repository is a **root Lake workspace** (`/lakefile.toml`,
`/lean-toolchain`) that aggregates one Lake package per paper:

| Package | Paper directory | Library |
|---------|-----------------|---------|
| `qou` | `content/quantum-observable-universe/lean/` | `QOU` |
| `ugb` | `content/unital-groebner-bases/lean/` | `UGB` |
| `fred2005` | `content/fred2005-formal-groups/lean/` | `Fred2005` |

`lake build` at the repo root builds every paper; `lake build <lib>`
builds a single library.  See `CLAUDE.md §0` for the full convention.

Every theorem-like environment in `chapters/*.tex` is tracked in
`proof-objects.json`, which maps LaTeX labels to Lean declarations.

### Content-block `lean.ref` — package-qualified URIs

Each content block manifest uses a single string URI to reference its
Lean declaration:

```ts
lean: { ref: "qou:QOU.Torsion.lifting_exists" }
lean: { ref: "ugb:UGB.GrobnerShirshov.Basis" }
```

- The `<package>` prefix must be registered in
  `folio-assistant/schemas/lean-packages.ts` (`LEAN_PACKAGES`).
- Use `parseLeanRef()` from that module when reading refs
  programmatically — do not regex-split on `:`.
- The legacy `lean: { decl, file? }` shape is **removed**.  Zod
  validation fails on blocks that still use it.

### Rebase / merge across the `lean.ref` migration — agent workflow

If you are an agent working on an older branch and a rebase or merge
surfaces `lean: { decl: "..." }` in content blocks, **run the
idempotent migration script — do not hand-edit**:

```bash
cd content
bun run migrate-lean-refs        # apply (writes in place)
bun run migrate-lean-refs:dry    # preview only
```

The script is safe to re-run; it chooses the Lake package prefix
from each block's paper directory via `LEAN_PACKAGES`.  Re-run
`bun run validate` after the migration to confirm the schema is
clean.  **Never add `decl` back to the schema to unblock a merge.**

### When reviewing LaTeX changes:
- Check `proof-objects.json` for linked Lean declarations.
- If a theorem statement changes, flag that the linked Lean declaration may
  need updating.
- If `\lean{}` macros are present, verify the declaration name is correct.

### LeanBlueprint macros:
- `\lean{QOU.Namespace.decl_name}` — links to a Lean declaration.
  (Blueprint macro uses the bare `<Decl>`, not the `<pkg>:<Decl>` URI.)
- `\leanok` — claims the Lean proof is `sorry`-free.
- `\uses{label1, label2}` — declares mathematical dependencies.
- `\proves{thm:label}` — links a proof block to its statement.

### Lean file structure:
`.lean` files live under each paper's Lake root (e.g.
`content/quantum-observable-universe/lean/QOU/<Module>.lean`).
Every paper's `lakefile.toml` pins `mathlib4` on the same commit.
Stubs use `sorry` for incomplete proofs.

### Base ring convention (CLAUDE.md §7c):
Every Lean declaration that holds in a generic commutative ring must
be stated over a **type variable**, never silently specialised to `ℝ`.
Use a generic `{R : Type*}` parameter with the weakest typeclass that
admits the construction (`[CommRing R]`, `[Field R]`,
`[GroupWithZero R]`). Specialise to `ℝ` **only** when the declaration
genuinely needs `Real.sqrt`, `Real.rpow`, `Real.cos`, `Real.exp`,
`Real.log`, an ordering predicate (`0 < q`, `q < 1`), `linarith` /
`positivity` / `nlinarith`, or a CODATA / experimental numerical
literal. See `CLAUDE.md` §7c for the typeclass cheat-sheet and the
archimedean-wall membership list.

When in doubt, **start generic**: generic → `ℝ` specialisation is
cheap (drop the parameter); `ℝ` → generic refactor is much harder
once downstream code accretes archimedean assumptions silently.

### Agent Coordination and Workplans:
**CRITICAL WORKFLOW**: ALWAYS ALWAYS when starting a new goal/bean, create a feature branch and immediately push it to the remote GitHub repository. Otherwise, agents cannot coordinate effectively and the workflow will fail.
