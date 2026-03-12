# GitHub Copilot — Authoring Instructions for *Quantum Observable Universe*

These instructions apply to all LaTeX source files in this repository.
Follow them precisely when generating, completing, or refactoring content.

---

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
