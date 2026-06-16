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
- **Witnessed values must use `:val[name]`** in any block kind
  (definitions, propositions, conjectures, theorems, lemmas,
  corollaries, proofs, examples, remarks, prose, algorithms, equations).
  Numerical literals derived from `q_0` or another substrate witness
  must be cited via the witness registry — never hard-coded.  See
  [`witnessed-values.md`](./witnessed-values.md) for the registry
  contract, the directive syntax, and the codemod that rewrites
  legacy literals.  Flag any new hard-coded numeral that has (or
  could have) a registry entry as drift risk.

### 2. Scientific Rigor
- Claims are supported by evidence or sound reasoning.
- Scientific terminology is used correctly.
- Referenced constants, data, or facts are accurate.
- **PREFER $q$-DEFORMED FUNCTIONS over classical counterparts.**
  Use $\exp_q$, $\ln_q$, $\cos_q$, $\sin_q$, $[n]_q$, $[n]_q!$
  in all formulas unless explicitly working in the classical
  ($q = 1$) limit.  The natural logarithm in the QOU is the
  **base-$q$ logarithm** $\log_q(x) = \ln x / \ln q$, which
  maps Skein polynomial ratios to $q$-integers:
  $\log_q(q^n) = n$ exactly.  The Jackson $q$-logarithm
  $\ln_q(x) = (x^{\hbar_q} - 1)/\hbar_q$ (where
  $\hbar_q = 1 - q^{-1}$) is the appropriate $q$-analogue
  for infinitesimal quantities.
  **Keep all formulas parametric in $q$ as long as possible.**
  Evaluate at $q = 1.110$ only at the final numerical step.
  The $q$-rational structure (e.g., $\log_q(P_d/P_p) \approx
  -(N-1)$ for neutron number $N$) is lost when classical
  $\ln$ is used prematurely.
  Classical $\ln$, $\exp$, $\cos$, $\sin$ are the $q \to 1$
  limits and should be labeled as such when they appear.
  **In Python computation scripts**: use `log_q(x) = math.log(x)/math.log(q)`
  instead of bare `math.log(x)`. When `math.log` is needed for
  intermediate computation (e.g., log-sum to avoid overflow),
  divide by `ln_q = math.log(q)` immediately to convert to
  base-$q$.  Never use `math.cos`; use $\cos_q$ (the $q$-deformed
  cosine) or `cosh` with $q$-arguments.  The `math.exp` function
  should be `q**x` (the $q$-exponential $\exp_q(x) = q^x$).
  **ENFORCEMENT**: Every new computation script MUST define
  `LN_Q = math.log(q)` at the top and use `math.log(x)/LN_Q`
  for all log-ratios. The Q-value formula is:
    `Q = |Σ_i log_q(V̂_dau_i / V̂_par_i)| × κ_q`
  where `κ_q = LN_Q × m_e / 3`. The q-weighted decomposition:
    `Q_qwt = |q · log_q(u) + q⁻¹ · log_q(r) + log_q(unc)| × κ_q`
  F_conv uses log_q but cancels (ratio). Bare `math.log()` without
  `/LN_Q` is a review failure except inside log-sum overflow guards.
- **$q$-integer identities simplify transfer matrix chains.**
  The ratio $[n+1]_q / [n]_q = q + q^{-n}/[n]_q$ is exact.
  For large $n$: $[n+1]_q / [n]_q \to q$ (exponentially fast).
  The transfer matrix eigenvalue ratio $|\lambda_+/\lambda_-|
  = q^2$ (for pp crossings) is a consequence.  Use these
  identities to reduce transfer matrix products to $q$-integer
  expressions rather than floating-point chains.
- **NO APPROXIMATIONS unless explicitly labeled as such.**
- **DISTINGUISH 'degree' FROM 'length' IN GRÖBNER COMPUTATIONS.**
  - **Degree** = genus of the knot = (r-1)(s-1)/2 for torus knot T_{r,s}.
    This is the physical degree from the shell structure on Σ₄.
    Degree 0 = unknot/trivial, degree 1 = T_{2,3}/T_{3,2},
    degree 2 = T_{2,5}, degree 3 = T_{2,7}, degree 4 = T_{3,5}/T_{2,9}.
  - **Length** = word length in the Hecke algebra = number of σ_i
    generators in a reduced word. This is the Gröbner reduction
    length, NOT the knot degree.
  - A length-4 word like σ₀·σ₁·σ₀·σ₂ can be degree 0 (genus 0)
    if its closure is the unknot.
  - The protium atom lives entirely in **degree 0** (ground state).
    Its length-4 dominant term is the Borromean core, which is a
    LINK (not a knot) with genus 0.
  - NEVER say "degree 4" when you mean "length 4".
  - The 6 embeddable torus knots on Σ₄ start at degree 1 (T_{2,3}).
    T_{2,1} = unknot = neutrino (degree 0).
    T_{3,1} is also degree 0 (not in the physical catalog).
- **NO correction factors, fudge factors, or empirical scaling.**
- **NO formulas that are not derived from the categorical action.**
- **PARTICLE INTERACTIONS MUST USE GRÖBNER BASIS REDUCTION.**
  When modeling particle interactions (beta decay, scattering,
  binding), do NOT use ad hoc transfer matrix ansätze or
  bolted-on correction factors. Instead:
  1. Start with the parent particle in Gröbner normal form
     (built by sequential Hopf linking + reduction).
  2. The ALLOWED interactions are the torus knot operators
     $T_{r,s}$ acting as generators of the ideal $I$.
  3. The ideal is $I = \{\text{Hecke}, \text{YB}, \text{far-comm},
     \text{torus knot relations}\}$.
  4. Insert the interaction operator (e.g., $T_{3,5}$ weak vertex
     for beta decay) into the parent braid word.
  5. Reduce the composed word through $I$ using `hecke_division.py`.
  6. Track every reduction step: which rule fires (Hecke, YB,
     far-comm), what the Hecke energy cost is.
  7. The output after reduction = daughter particle(s) + emitted
     particles (electron $T_{2,3}$, neutrino unknot, photon, etc.).
  8. The Q-value = Hecke energy difference between input and
     output normal forms.
  **The transfer matrix approach is a SHORTCUT** that works for
  the Skein polynomial ratio, but it misses the interaction
  structure (particle emission, crossing budget, Borromean
  un-ring/re-ring). For precision work, always verify against
  the full Gröbner computation.
- **QUOTIENT IDEAL APPROACH FOR INDUCTIVE ATOM CONSTRUCTION.**
  When building atoms inductively (protium → deuterium → ...),
  factor out STRUCTURAL operations at the START using quotient
  ideals I₁-I₇:
    I₁: σ₀-extension (leading quark link, ratio +0.315)
    I₂: YB reordering (energy-preserving)
    I₃: B₃ Borromean prefix (proton core)
    I₄: 𝔫₁ neutron tail (electron-Borromean-linked neutron)
    I₅: Protium completeness (whole atom = 1 object, not 4 terms)
    I₆: Structural defects (missing bond → known energy cost)
    I₇: Electron bridge (σ₂·σ₃·σ₂ Borromean bridge)
    I₈: Adjacency correlation — σ_i·σ_{i+1} absorbed into σ_{i+1}.
         The off-diagonal of the transfer matrix product M_i.
         Structural: determined by q and the crossing types.
    I₉: Closed shell (per-generator chain collapse) — when w·σ_j
         extends w (a word already in the NF), absorb w·σ_j.
         Recursive: strip from longest words first. This is the
         per-generator transfer matrix factorization.
         The palindromic NF {1,3,4,3,1,...} factors into
         independent per-generator volumes V̂_i.
    I₁₀: Pairing — even occupancy in a shell creates (σ,1) pairs
         via Hecke σ²=HA·σ+1. Odd occupancy leaves unpaired σ-only.
         Pairing energy = net(even-even) / net(odd-odd) at same A.
         Histogram is A-universal (same for all Z,N at same A).
         Pairing is in the WEIGHTS, not the counts.
  Each completed atom's NF is registered as a formal variable
  (ℵ₁, ℵ₂, ...) in the quotient ideal for the NEXT step.
  Track energy at every quotient substitution.
  The GOAL is n_terms = n_strands (optimal Gröbner basis).
  **ACHIEVED** for all nuclei through A=8 (⁸Be):
    D:2, ³H:3, ³He:3, ⁴He:4, ⁵Li:5, ⁶Li:6, ⁷Li:7, ⁸Be:8.
  All balanced (Z=N) nucleon-level NFs are palindromic.
  Valley of stability: optimality holds for N ≥ Z−1 exactly.
  **IMPLEMENTATION:**
  - Python `hecke_symbolic.py`: exact in q, A ≤ 7
  - Rust `hecke-engine` v1: f64 at q₀, A ≤ 10 (22s for A=10)
  - Rust `hecke-engine` v2: packed u128 words, A ≤ 8 exact, A ≤ 10 fast
  - Quotient-with-accumulation: F_Pauli for A=11+ via streaming
  - Witness: `pauli-witness.py` (symbolic), `pauli-witness-A8.json` (f64)
  **Q-VALUE FORMULA (hybrid, MAE = 4.2%):**
  - Shell 1-4: Q = |q·log_q(u) + q⁻¹·log_q(r) + log_q(unc)| × κ_q
  - Shell 5+: Q = |log_q(V̂_conv^dau/V̂_conv^par)| × κ_q
  - Magic: × F_Pauli from H₃(q) alternating irrep (0.6382)
  - κ_q = ln(q) × m_e/3 = 0.01777 MeV
  See: `QOU.QuotientIdeal` in Lean for formal definitions.
- **Q-VALUES ARE ALGEBRAIC IN q, NOT NUMERICAL.**
  The Q-value for any beta decay is an EXACT polynomial in q^½:
    Q(q) = |net(parent)(q) − net(daughter)(q)| × κ(q)
  where net(X) = Σ coefficients of 𝒩̄(X), and κ = E_× · μ₀ = m_e/3.
  All NF coefficients are elements of ℤ[q^½, q^{-½}].
  Substitute q = q₀ ONLY when comparing to measured values.
  Example: tritium σ₁ coefficient = q²(q+1)²(q²−q+1)/4 (factored
  cyclotomic). He-3 σ₁ coefficient = (q²+1)²/4. The Q-value
  comes from the ALGEBRAIC DIFFERENCE of these polynomials.
  Use `hecke_symbolic.py` for exact-in-q computation.
  See: `QOU.NuclearNormalForms` in Lean for declarations.
- **EVERY observed value MUST carry ± uncertainty.** No CODATA,
  NNDC, PDG, or any experimental constant without an error bound.
  Use `experimental_constants.py` as the single source of truth.
- **EVERY derived quantity MUST propagate error.** If $f(x)$
  depends on $x \pm \delta x$, then $\delta f = |f'(x)| \delta x$.
  For products: relative errors add in quadrature. For $Q^5$:
  $\delta\Gamma/\Gamma = 5 \,\delta Q/Q$. The $q$-sensitivity
  $\partial\ln\Gamma/\partial\ln q \approx 48$ means even
  $10^{-6}\%$ error in $q$ propagates to $\sim 5 \times 10^{-5}\%$
  in the rate. Track this explicitly.
- **NEVER use O(·) to discard polynomial structure.** The transfer
  matrix product has $\binom{A}{2}$ steps — this is exact, not
  "O(A²)". Each step is a nucleon pair. The polynomial degree is
  $\leq A^2 - 1$. Say the exact number; do not asymptotize it away.
- **NEVER assume classical energy conservation at $q \neq 1$.**
  The $q$-differential satisfies $d_q^2 \neq 0$, so
  $E_{\mathrm{before}} = E_{\mathrm{after}}$ fails.  Use the
  categorical action difference $Q = S_q(\mathrm{par})
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
- **Derived constants from $q$ (canonical formulas):**
  - Speed of light: $c_q = 1/(q-1)$ — ratio of spatial to temporal
    coupling in $A_q = q^{-1}A + \hbar_q\,\iota_\xi A\,\theta$.
  - Planck constant: $\hbar_q = (q-1)/q$.
  - Mass-energy equivalence: $E_H = \mathfrak{m}_H \cdot c_q^2$,
    i.e., $E_H = \mathfrak{m}_H/(q-1)^2$.  Plain $E_H$ is safe:
    the exceptional divisor is now $\mathcal{S}_c$, so $E$ is
    no longer overloaded.
  - Generic closed vortex: $\varrho \colon \mathbf{1} \to A$ (not
    $\gamma$, which is reserved for the photon).
  - Operational entropy: $\eta_q = (2q-1)/q^3$.
  - Hausdorff dimension: $d_H(q) = (2q-1)^2/q^3$.
  - $q$-deformed Lyapunov exponent: $\chi_q = 1/(2q-1)$.
  - Gravitational constant: $G_{\mathrm{Planck}} = 1$ (exact),
    from in-progress braid entropy $S_{\mathrm{cell}} = (q-1)^2/q^3$
    with quadratic suppression $\hbar_q^{2k}$ per jet level.
  - Golden crossover: $d_H = 1$ at $q = 1$ and $q = (3+\sqrt{5})/2
    = \varphi^2$.
  - EM/strong ratio: $\tanh(\ln q)$.
  - Fine structure: $\alpha_{\mathrm{EM}} = q^{-1}/([9]_q \cdot
    [10]_q)$ where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$
    (symmetric $q$-integer).
  - Mass as photon threading cost: $\mathfrak{m}_H = E_H \cdot (q-1)^2$
    = total Gröbner--Shirshov Hecke reduction cost of threading
    $\gamma$ through $\beta_H$.  Three equivalent computations:
    Yekutieli MI (analytic), ribbon trace (algebraic), Gröbner
    reduction (computational).
  These formulas are **derived**, not postulated. Agents must not
  introduce alternative expressions for these quantities.
- **Notation conventions (this session):**
  - $E_H$ = crossing energy of composite $H$ (plain italic, safe
    since exceptional divisor is now $\mathcal{S}_c$).
  - $\mathfrak{m}_H$ = categorical mass of composite $H$ (fraktur).
  - $c_q$ = speed of light (subscript, not function notation).
  - $\varrho \colon \mathbf{1} \to A$ = generic closed vortex.
  - $\gamma$ = photon (exclusively).  Never use for generic path.
  - $\wp$ = reserved for Weierstrass projection (future use).

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

### 4b. Canonical-derivation discipline (three-calibration rule)

The QOU framework admits **exactly three** external calibration
inputs, per
[`prop:three-calibration-inputs`](../../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)
and
[`prop:three-calibration-discipline`](../../../content/quantum-observable-universe/observations/three-calibration-discipline.md):

| ID | Quantity | (Co)homology | Source |
|----|----------|--------------|--------|
| **CAL-1** | $m_e$ | $H^0$ | CODATA |
| **CAL-2** | $m_\mu/m_e \to q_0$ | $H^1$ | CODATA (phys-obs may anchor $q_0$ on $m_p/m_e$ for precision) |
| **CAL-3** | $m_{\pi^\pm}$ (meson scale) | orthogonal class | PDG ($Q_\beta$ is *derived* from CAL-1+CAL-2, not CAL-3) |

Every numerical observable in the paper must factor as
$\mathcal{O} = \hat{\mathcal{O}}(q_0) \cdot m_e^{\,a} \cdot Q_\beta^{\,b}$
with $\hat{\mathcal{O}}(q_0) \in \mathbb{Q}(q_0)$ (the discipline
minimum per `prop:three-calibration-discipline`) and the
empirically-observed Laurent refinement
$\hat{\mathcal{O}}(q_0) \in \mathbb{Z}[q_0^{\pm 1/2}]$ per
`prop:three-calibration-inputs`. Exponents
$a, b \in \mathbb{Z}_{\geq 0}$ are subject to the dimensional-
homogeneity constraint $a + b \in \{0, 1\}$ (output is
dimensionless, mass-scale, or energy-scale; never higher-power
composites). Anything else is a discipline violation. **Flag**
as part of accuracy review:

- *Free parameters* beyond CAL-1/2/3 — a fourth dimensional input
  is a hard audit failure.
- *Coefficient fits* to AME / CODATA / PDG (Bethe-Weizsäcker
  coefficients labelled "ad hoc", "approx", "tuned").
- *Numerological substitutions* (magic numbers $\{2,8,20,28,50,82,126\}$
  asserted as data without derivation from Bring's surface or BB/LR
  homology).
- *Second pinning of $q_0$* (independent fits to $m_e$, $m_\mu$,
  $m_\tau$, etc.).
- *Second hadronic scale* (proton mass, pion mass introduced as
  inputs rather than predictions).
- *Archimedean-side input* (volumes, hyperbolic, Mostow constants)
  appearing in an algebraic-side derivation.
- *Tautologies* where a "derivation" uses its own result as input
  (e.g. LO $\rho_K$ pattern in `atomic_mass_via_rho_k.py`).
- *Rationalization*: prose in a proposition body arguing *why* a
  value is right rather than *deriving* it.

The three **categorically allowed exceptions** are Class-A
(acknowledged-stub with banner), Class-B (baseline-extraction
script that *produces* a calibration input), and Class-C
(diagnostic probe / cross-check, read-only, no downstream witness).
Each must carry an explicit banner / docstring marker. See
[`canonical-watcher.md`](./canonical-watcher.md) for the
opt-out protocol and
[`docs/audits/2026-05-11-three-calibration-discipline-violations.md`](../../../docs/audits/2026-05-11-three-calibration-discipline-violations.md)
for the audit precedent.

For active monitoring of canonical-derivation discipline across
incoming commits + PRs, route the request to
[`local/canonical-watcher`](./canonical-watcher.md).

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

**Lean declaration verification.** The `lean.ref` URI (form
`"<pkg>:<Decl>"`, parsed via `parseLeanRef()`) in each `.ts` manifest
names the corresponding Lean declaration. Verify that:
- The declaration exists in the `.lean` sibling file.
- The Lean type signature matches the mathematical statement in `.md`.
- Formalization status is derived at build time (not stored in `.ts`);
  cross-check against `proof-objects.json`.

**Formalization cross-check.** Use `lean_hover_info` on the declaration
named by `lean.ref` to confirm the Lean type matches the narrative claim.
Numerical constants in `.md` blocks must match their `noncomputable def`
values in `.lean`.

**Content object completeness.** For blocks with `kind: "definition"`,
all three files must exist and be consistent. For `theorem`/`lemma`
blocks, a missing `.lean` sibling is a warning. The `uses[]` dependency
graph helps trace which upstream definitions a claim relies on — verify
those are formalized too.

**Glossary terms (`:defterm` / `:refterm`).** Every term registered in
any block's `defines: [...]` must appear wrapped at every mention —
`:defterm[…]{#slug}` once, `:refterm[…]{#slug}` everywhere else (LaTeX:
`\defterm{slug}` / `\refterm{slug}`). Bare-text or `\emph{}` mentions
of a defined term are scientific-accuracy violations because they
break the canonical-name → canonical-definition link the validator
relies on. Run `bun run validate <paper> --strict` to catch
`term-mention-coverage` warnings. See `local/glossary-build` skill.

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
