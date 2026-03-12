# Scientific Accuracy Skill

## Purpose

Evaluate commits for mathematical correctness, scientific rigor, and
logical consistency.  This skill is derived from established scientific
peer-review practices and the methodology of
[K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills).

## Checks

### 1. Mathematical Verification
- All equations, formulas, and numerical computations are correct.
- Dimensional analysis and unit consistency hold.
- Boundary conditions and edge cases are handled appropriately.

### 2. Scientific Rigor
- Claims are supported by evidence or sound reasoning.
- Scientific terminology is used correctly.
- Referenced constants, data, or facts are accurate.

### 3. Statistical and Methodological Soundness
- Statistical methods are appropriate for the analysis.
- Sample sizes, power calculations, and significance thresholds are
  reasonable.
- Common pitfalls are avoided: p-hacking, multiple comparisons,
  survivorship bias.

### 4. Logical Consistency
- No logical fallacies or unsupported leaps in reasoning.
- Conclusions follow from the presented evidence.
- Internal consistency is maintained across the changeset.

### 5. Reproducibility
- Methods are described with sufficient detail to reproduce.
- Magic numbers are explained or referenced.
- Algorithms are correctly implemented.

## Output Format

```
- **Summary**: One-paragraph overall assessment.
- **Issues Found**: Numbered list (severity: critical / major / minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
```
