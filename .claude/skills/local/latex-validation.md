---
name: latex-validation
roles: [reader, collaborator, owner]
---

# LaTeX Validation Skill

## Purpose

Validate LaTeX source files for syntactic correctness, structural
consistency, and adherence to project conventions defined in the
repository's `copilot-instructions.md`.

## Checks

### 1. Syntax Correctness
- Every `\begin{env}` has a matching `\end{env}`.
- Braces `{}`, brackets `[]`, and parentheses `()` are balanced.
- No undefined control sequences (commands must be provided by a
  declared package or defined in the preamble).
- Math mode delimiters (`$...$`, `\(...\)`, `\[...\]`) are properly
  paired.

### 2. Environment Usage
- Theorem-like environments (`theorem`, `lemma`, `proposition`,
  `corollary`, `definition`, `example`, `remark`, `conjecture`) are
  used only as declared in `main.tex` and are never redeclared in
  chapter files.
- Display math uses `equation` or `align` environments — never
  `$$...$$`.

### 3. Label Conventions
- Every labeled item uses the correct prefix as specified in the
  project labeling convention:
  - `chap:` for chapters
  - `sec:` / `ssec:` for sections / subsections
  - `def:` / `thm:` / `lem:` / `prop:` / `cor:` / `ex:` / `rem:` /
    `conj:` for theorem-like environments
  - `eq:` for equations, `fig:` for figures, `tab:` for tables
- Every theorem-like environment and every numbered equation carries a
  `\label{...}`.

### 4. Cross-References
- `\ref` and `\eqref` targets correspond to existing `\label`
  commands within the changeset or the broader document.
- Non-breaking spaces (`~`) precede `\ref` and `\eqref`.

### 5. Bibliography
- Every `\cite{key}` key appears in `references.bib`.
- BibTeX keys follow the `<firstauthorlastname><year>` convention.
- Every new reference must include at minimum: `author`, `title`,
  `year`, and either `doi` or `url`.

### 6. Commutative Diagrams (Herrlich–Strecker style)
- Use `tikzcd` environments, **not** `CD` (amscd).  Both packages are
  loaded, but `tikzcd` is the project standard.
- Every definition must include commutative diagrams alongside equations.
  Diagrams come first; the equation they express follows.
- Standard spacings: `row sep=2.5em, column sep=3em` (or `3.5em` for
  wider labels).
- Arrow styles: `\ar[r, "label"]` for horizontal,
  `\ar[d, "label"']` for downward (label below), `two heads` for
  epimorphisms, `dashed` for induced/factored morphisms,
  `equal` for identity/equality arrows.
- Definitions of algebraic structures (Hopf, Frobenius, monoidal) must
  display the structure morphisms as a diagram before listing axioms.

### 7. Deformation Parameter Convention
- The parameter $q$ must **not** appear in definitions, examples,
  lemmas, or theorems before the substrate parameter section
  (Section~\ref{sec:substrate-parameter}).
- Categorical dimensions are written as plain integers (e.g.\ `$2$`)
  in the pre-substrate definitions; the $q$-deformed form `$[2]_q$`
  appears only after the substrate parameter is introduced.
- The gauge group is $\mathrm{SU}(2)$ (not $\mathrm{SU}_q(2)$) in
  the pre-substrate material.

### 8. LeanBlueprint Macros
- `\lean{QOU.Namespace.decl}` must reference a fully qualified Lean
  declaration that exists (or will exist after stub generation) in the
  `lean/QOU/` source tree.
- `\leanok` may only appear when the corresponding Lean proof contains
  **no** `sorry`.  Never add `\leanok` speculatively.
- `\uses{label1, label2}` must reference labels that exist in the same
  document or in `blueprint/src/content.tex`.  Every dependency edge
  must be bidirectionally consistent: if B `\uses{A}`, then A must
  carry a `\label{}`.
- `\proves{thm:label}` links a proof block to its statement; the label
  must match an existing theorem-like `\label{}`.
- Place blueprint macros **inside** the environment, immediately after
  `\label{}`:
  ```latex
  \begin{theorem}\label{thm:my-result}
    \lean{QOU.Chapter.my_result}
    \uses{def:prerequisite}
    Statement...
  \end{theorem}
  ```
- `blueprint/src/content.tex` is the single source of truth for the
  formalization dependency graph.  Every `\lean{}` macro in
  `chapters/*.tex` must have a corresponding entry there.

### 9. Blueprint-BibTeX Cross-References
- Every `-- Ref: [key]` annotation in Lean files must have a matching
  entry in `references.bib` (exact case-sensitive key match).
- When adding a `sorry` to a Lean file, precede it with a
  `-- Ref: [key] url` comment linking to the foundational reference.
- `\cite{key}` keys in `blueprint/src/content.tex` must resolve against
  `references.bib` via the `../../references` relative path.

## Output Format

```
- **Summary**: One-paragraph assessment of LaTeX correctness.
- **Issues Found**: Numbered list (severity: critical / major / minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
```
