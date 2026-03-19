# Readability Editing Skill

## Purpose

Review LaTeX manuscripts for narrative clarity, prose quality, and
editorial polish.  This skill is less concerned with mathematical
correctness and more concerned with how well the text communicates
ideas to a graduate-level reader.

## Checks

### 1. Narrative Flow
- Sections and subsections follow a logical progression.
- Transitions between paragraphs and sections are smooth.
- The reader is never left wondering *why* a topic is introduced.

### 2. Definition Hygiene
- Definitions are concise and self-contained.
- Each definition introduces exactly one concept.
- Technical terms are introduced with `\emph{...}` on first use and
  are not re-defined later.
- Every non-trivial definition is followed by at least one example.

### 3. Spelling and Grammar
- Identify misspelled words (including common LaTeX-adjacent typos).
- Flag grammatical errors: subject-verb agreement, dangling modifiers,
  comma splices, run-on sentences.
- Enforce the project prose style: formal academic English, no
  contractions, no first-person singular ("I"), Oxford comma.

### 4. Sentence-Level Clarity
- Flag overly long or convoluted sentences.
- Suggest simpler alternatives where meaning is preserved.
- Ensure that sentences do not begin with a mathematical symbol.

### 5. Consistency
- Notation introduced in one section is used consistently throughout.
- Acronyms are expanded on first use and used bare thereafter.
- Displayed equations ending a sentence include a period inside the
  environment.

## Output Format

```
- **Summary**: One-paragraph assessment of readability.
- **Issues Found**: Numbered list (severity: critical / major / minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
```
