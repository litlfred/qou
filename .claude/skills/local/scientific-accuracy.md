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

### 4a. Consequence vs. Axiom Audit
- When a condition inside a definition looks like it might follow from
  other axioms or from the ambient structure, investigate before
  restructuring:
  1. Identify the **hypotheses** the candidate consequence would need.
  2. Check whether those hypotheses are already supplied by the other
     axioms in the definition or by the ambient categorical structure.
  3. If the condition is **genuinely independent**, leave it in the
     definition.  If it is **derivable**, extract it into a proposition
     or lemma with a proof.
- *Example*: The categorical volume constraint (ε: Λ²V → **1**
  non-degenerate) was investigated as a possible consequence of
  non-degeneracy + observability.  It is independent — it is equivalent
  to symplectic self-duality of V, which is not forced by the other
  axioms — so it correctly remains as axiom (iii).
- When multiple objects across chapters share similar-sounding names
  (e.g., "volume constraint" vs. "volume form"), verify they refer to
  the same mathematical object before renaming.  Trace the geometric
  home of each: fiber, base, total space, or categorical.

### 5. Reproducibility
- Methods are described with sufficient detail to reproduce.
- Magic numbers are explained or referenced.
- Algorithms are correctly implemented.

### 6. Formalization Cross-References
- Numerical constants in the manuscript (CODATA values, knot volumes,
  mass ratios) must match the `noncomputable def` constants in the Lean
  source exactly.  Cross-check against:
  - `MassDerivation.vol_figure_eight` (2.0298832128)
  - `MassDerivation.experimental_mu_e_ratio` (206.768283)
  - `MassDerivation.substrate_q` (1.1097)
- Every claim citing experimental data must have a `\cite{key}` whose
  BibTeX entry includes a DOI or URL to the original source.
- The `-- Ref: [key]` annotations in Lean `sorry` markers must cite the
  correct foundational reference for the gap.  Verify that the cited
  paper is relevant to the unproved obligation.
- Knot Atlas URLs in `KnotRegistry.lean` docstrings must resolve to
  valid pages (format: `http://katlas.org/wiki/<ab_index>`).

## Content Object Integration

Scientific accuracy checks should leverage the content object triple
architecture (`.ts` manifest + `.md` narrative + `.lean` formalization)
for cross-validation.

**Lean declaration verification.** The `lean.decl` field in each `.ts`
manifest names the corresponding Lean declaration. Verify that:
- The declaration exists in the `.lean` sibling file.
- The Lean type signature matches the mathematical statement in `.md`.
- The `status` field reflects reality (`proved` only if sorry-free).

**Formalization cross-check.** Use `lean_hover_info` on the `lean.decl`
to confirm the Lean type matches the narrative claim. Numerical constants
in `.md` blocks must match their `noncomputable def` values in `.lean`.

**Content object completeness.** For blocks with `kind: "definition"`,
all three files must exist and be consistent. For `theorem`/`lemma`
blocks, a missing `.lean` sibling is a warning. The `uses[]` dependency
graph helps trace which upstream definitions a claim relies on — verify
those are formalized too.

## Output Format

```
- **Summary**: One-paragraph overall assessment.
- **Issues Found**: Numbered list (severity: critical / major / minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
```
