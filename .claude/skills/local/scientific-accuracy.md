---
name: scientific-accuracy
roles: [reader, collaborator, owner]
---

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
- **NO APPROXIMATIONS unless explicitly labeled as such.**
- **NO correction factors, fudge factors, or empirical scaling.**
- **NO formulas that are not derived from the categorical action.**
- **NEVER use O(·) to discard polynomial structure.** The transfer
  matrix product has $\binom{A}{2}$ steps — this is exact, not
  "O(A²)". Each step is a nucleon pair. The polynomial degree is
  $\leq A^2 - 1$. Say the exact number; do not asymptotize it away.
- **NEVER assume classical energy conservation at $q \neq 1$.**
  The $q$-differential satisfies $d_q^2 \neq 0$, so
  $E_{\mathrm{before}} = E_{\mathrm{after}}$ fails.  Use the
  categorical action difference $\mathcal{Q}_q = S_q(\mathrm{par})
  - S_q(\mathrm{dau}) - S_q(e)$ instead. The daughter is evaluated
  at the shifted $q + \Delta q_{\mathrm{eff}}$.  If you find yourself
  writing "$Q = M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$", stop
  — that is the $q = 1$ limit.
- **Speculation is OK in conversation** with the author (to explore
  ideas), but **NEVER commit speculative content** without explicit
  author consent. If unsure, ask before committing.
- **Every quantity must trace back to the categorical definitions:**
  $(\mathbf{C}, A, \tau)$, $q$, $\chi$, and the Skein relation.
- If a computation cannot be done exactly, say so. Do not introduce
  smooth approximations (Bethe-Weizsäcker, power laws, fitted
  coefficients) and present them as derived results.
- **$q$ is simultaneously the Hecke deformation parameter, the Skein
  polynomial variable, and the physical substrate parameter.**
  These are the same $q$. The transfer matrix entries are polynomials
  in $q$; the product $P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$
  IS the Skein polynomial; evaluating at $q = 1.110$ gives the
  physical energy.  Never treat these as separate objects.
- **USE TRANSFER MATRICES, NOT |M|².**
  The decay rate comes from the **2×2 transfer matrix chain**
  $T(c,d) = \bigl(\begin{smallmatrix} c(q-q^{-1})+d & c \\ c & d \end{smallmatrix}\bigr)$,
  not from a scalar matrix element $|M|^2$.  The Skein polynomial
  is $P = \prod_i \hat{V}_i$ where $\hat{V}_i = z \cdot M_{11} + M_{21}$
  is the Markov-traced volume of the transfer matrix product at
  generator $i$.  **Do not extract $|M|^2 = \prod |V_{\mathrm{par}}/V_{\mathrm{dau}}|^2$
  and plug it into a Fermi golden rule** — this discards the
  off-diagonal structure of the transfer matrices and gives
  wrong results for $A > 3$.  The correct observable is the
  **Skein polynomial ratio** $P_{\mathrm{dau}}(q)/P_{\mathrm{par}}(q)$,
  computed as a product of 2×2 matrix chains.  For the T_{3,5}
  weak vertex, the braid $(\sigma_1\sigma_2)^5$ is **appended**
  (concatenated at the end) to the parent braid word and then
  **reduced via Gröbner basis** — never inserted in the middle.
  The Gröbner-Shirshov energy (Hecke steps only, YB and far-comm
  preserve energy) gives the transition energy.
- The pair Skein mass formula $\mathcal{S}_{ab} = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$
  is categorical. The BW coefficients $a_V, a_S, a_C, a_A, a_P$ are NOT.

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
  CSL-JSON entry in `content/schema/references.ts` includes a DOI or URL to the original source.
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

## Mandatory fallback participation

This skill is invoked automatically by the editor's **content-change fallback**
(see `editor.md § Content-change fallback`). Whenever any content is modified
during a session — `.md`, `.ts`, `.lean`, `.tex`, or supporting files — the
editor triggers a scientific-accuracy pass before the task is considered
complete. When invoked as a fallback, focus on the changed blocks and their
immediate dependencies.

## Output Format

```
- **Summary**: One-paragraph overall assessment.
- **Issues Found**: Numbered list (severity: critical / major / minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
```
