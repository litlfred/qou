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

## Output Format

```
- **Summary**: One-paragraph assessment of LaTeX correctness.
- **Issues Found**: Numbered list (severity: critical / major / minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
```
