---
name: one-voice
description: Narrative voice and style consistency checker
roles: [reader, collaborator]
triggers:
  - "one voice"
  - "voice check"
  - "narrative check"
  - "style consistency"
  - "before committing narrative"
---

# One-Voice: Narrative Consistency Checker

Run this skill before committing any narrative content (.md files).
It ensures the paper speaks with a single, consistent voice across
all chapters, sections, and the running SU(2) example.

## Paper-Level Voice Rules

| Rule | Standard | Violation example |
|------|----------|-------------------|
| **Person** | First-person plural ("we") | "the author shows", "one can see", "it is shown" |
| **Referent** | "this paper" | "this book", "this work", "the present article" |
| **Tense** | Present ("we define", "the theorem states") | Past ("we defined", "the theorem stated") |
| **Tone** | Direct, declarative, no editorializing | "surprisingly", "remarkably", "it is perhaps the most", "interestingly" |
| **Math voice** | Active ("we construct $X$") for new definitions; passive ("$X$ is called") for established terms | Mixing active/passive for the same concept |
| **Reader address** | Never address the reader directly | "you can verify", "the reader will note" |

## Chapter-Specific Style

| Chapter | Style | Notes |
|---------|-------|-------|
| **Ch 0 (Intro)** | Expository, accessible, first-person plural | Sets up observations → axioms → consequences. No jargon without explanation. |
| **Ch 1 (QU)** | Definition-theorem-example | Formal mathematical prose. Each definition followed by the SU(2) example. |
| **Ch 2 (QOU)** | Same as Ch 1, but builds on Ch 1 vocabulary | Can assume reader knows Ch 1 terms. |
| **Ch 3 (Lifting)** | Technical, proof-heavy | Obstruction theory language. Still first-person for narrative glue. |
| **Ch 4 (Braids)** | Computational, concrete | Explicit matrices, crossing diagrams. "We compute" voice. |
| **Ch 5 (Models)** | Two parts: (A) general models use expository voice; (B) Descartes uses concrete, coordinate-heavy voice | Part B is the most "hands-on" chapter. |
| **Ch 6 (Observations)** | Data-driven, comparison tables | "We estimate", "the predicted value is", "which agrees with". No claims of precision beyond what the numbers show. |
| **Ch 7 (Information)** | Speculative but grounded | "The framework suggests", not "we prove". Mark conjectures clearly. |

## Running Example Consistency

The SU(2) running example (starting from `ex:rigid-monoidal-vect`
and `ex:quantum-universe-su2`) must maintain consistent notation
and voice across all chapters:

| Element | Notation | First introduced |
|---------|----------|-----------------|
| Category | $\mathbf{Rep}(\mathrm{SU}(2))$ | Ch 1 |
| Frobenius-Hopf object | $A = \mathcal{O}(\mathrm{SU}(2))$ | Ch 1 |
| Fundamental rep | $V = V_{1/2} \cong \mathbb{C}^2$ | Ch 1 |
| Basis | $\{e_1, e_2\}$ for $V$ | Ch 1 |
| Matrix generators | $\alpha, \beta, \bar{\alpha}, \bar{\beta}$ | Ch 1 |
| Fibre functor | $\tau$ (forgetful functor) | Ch 1 |

When extending the example in later chapters, always reference back:
"Continuing the SU(2) example from §1..." or use the `interprets`
field pointing to the earlier example block.

## Terminology Consistency

| Term | Correct | Incorrect |
|------|---------|-----------|
| Geometric tubes on Bring's surface | coral tubes | color tubes, chiral tubes |
| Coordinate system for r,g,b | color tube coordinates | coral tube coordinates |
| Physical chirality (experiments) | chiral | coral |
| Hadron variable | $\mathfrak{H}$ | $H$ (plain italic) |
| Hadron mass | $\mathfrak{m}_{\mathfrak{H}}$ | $\mathfrak{m}_H$, $m_H$ |
| Category | $\mathbf{C}$ (bold) | $\mathcal{C}$ (calligraphic) |
| Fibre functor | $\tau$ | $\omega$, $U$ |
| Energy | $\mathbf{E}$ (bold) | $\mathfrak{E}$ (fraktur) |
| Mass | $\mathfrak{m}$ (fraktur) | $m$ (plain) |
| Substrate parameter | $q$ (symbolic) | $q = 1.1097$ (numerical, except Ch 6-7) |

## Editorializing Blacklist

The following phrases and patterns must never appear in the paper:

- "surprisingly", "remarkably", "interestingly", "notably"
- "perhaps the most surprising/important/significant"
- "it is worth noting that"
- "the reader will appreciate"
- "it turns out that" (just state the result)
- "one might expect" (state what happens, not what was expected)
- "a beautiful result" / "an elegant proof"
- Any commentary on the importance or surprise value of results

Results speak for themselves.

## Pre-Commit Checklist

Before committing any .md content, verify:

1. [ ] **Person**: All narrative uses "we" (first-person plural)
2. [ ] **Referent**: "this paper" (never "this book/work/article")
3. [ ] **Tense**: Present tense for definitions and theorems
4. [ ] **Tone**: No editorializing phrases (check blacklist above)
5. [ ] **Notation**: All symbols match the notation register (§7aa)
6. [ ] **Coral/color**: Geometric tubes = "coral"; coordinates = "color"
7. [ ] **Hadron fraktur**: $\mathfrak{H}$ for hadrons, not $H$
8. [ ] **Example thread**: SU(2) examples use consistent notation
9. [ ] **Cross-chapter**: Terms introduced in earlier chapters are
       referenced, not re-defined

## Procedure

1. **Read** the target .md file(s)
2. **Identify** the chapter and section context
3. **Check** each rule in the pre-commit checklist
4. **Flag** violations with file path, line number, and fix
5. **If ambiguous** — if you're unsure whether a passage should be
   active or passive, concrete or abstract, or what the author's
   intent is — **ask the author** using AskUserQuestion before
   making changes
6. **Fix** all clear violations
7. **Report** summary of changes made
