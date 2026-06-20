# Closed-form coefficients from first-principles categorical machinery — workplan

**Branch**: `claude/closed-forms-first-principles`
**Date**: 2026-05-19
**Goal**: Prove the closed-form coefficients appearing in QOU mass / binding-energy / amplification formulas from the categorical substrate alone (Hecke algebra + Markov trace + Galois data + Möbius pencil + algebraic residue), eliminating all fit-based ansätze.

## The bottleneck — identified

All six strategic options proposed in this session's reassessment ultimately converge on **one closed form**:

$$
  \Delta_\lambda(K) \;\colon\; \text{partitions} \times \text{knots} \;\longrightarrow\; R
$$

— the per-partition correction in the binding-energy master formula

$$
  B(K) \;=\; m_e \cdot \sum_\lambda y_\lambda(q) \, \chi^\lambda(\beta_K) \, \Delta_\lambda(K).
$$

[PR #777](https://github.com/litlfred/qou/pull/777) records **six failed closure ansätze** for $\Delta_\lambda$ on the deuteron:

| Ansatz | Outcome |
|---|---|
| Occam single-support | underdetermined; arbitrary (λ=[5,1], Δ=−22.96) |
| Frobenius co-Casimir $1/\dim_q(\lambda)$ ([PR #602](https://github.com/litlfred/qou/pull/602)) | wrong sign, vortex-blind |
| Demazure-fibre $y_\lambda \cdot D_w / D_{w_0}$ | reproduces M_LO tautologically |
| LP-Plancherel cost ([PR #603](https://github.com/litlfred/qou/pull/603)) | reproduces Occam (shifts underdetermination) |
| LP-Frobenius cost ([PR #603](https://github.com/litlfred/qou/pull/603)) | different singleton, same issue |
| Crystal-graph weight | in flight, TBD |

PR #777's diagnosis (carried forward from 2026-05-09 audit):

> *"$M_\lambda(K)$ is the Archimedean realization functor's per-block action — GAP-A-3 / GAP-A-4. Don't propose a 7th fit-based ansatz; the three-calibration discipline review will catch it."*

**This is the same archimedean realization functor $\tau$ that the [PR #779](https://github.com/litlfred/qou/pull/779) algebraic-residue swap reformulated.** $\Delta_\lambda$ is its per-λ-block manifestation.

## Convergence of the six options

| Option | What it asks | Reduces to |
|---|---|---|
| **A** Substrate-derive ρ_K | substrate-pure m_p / m_n / Δm_pn | $\Delta_\lambda$ (since ρ_K's non-LO content is exactly $\sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$) |
| **B** Δ_λ via algebraic residue | first-principles $\Delta_\lambda$ closure | **THE GOAL** — direct |
| **C** m_μ closure | first L2 success (6.5× → 100×) | Borromean refinement; either Δ_λ for μ-channel or sub-leading $(1+\hbar_q^3)$ from PR #690 |
| **D** Compute: LP → SDP for gluon | ~1 MeV on D | per-atom gluon choice; downstream of accurate Δ_λ |
| **E** F1 non-vanishing theorem | complete d²A story in Lean | independent infrastructure piece |
| **F** Coordinate with #781 | mass-tables alignment | downstream consumer of A / B |

**Foundational target: option B (Δ_λ via algebraic residue).**

## Categorical machinery available

From PR #779 + PR #780, the substrate carries:

| Categorical object | $R$-side ring | Used for |
|---|---|---|
| Color-tube cubic $F(z, c)$ | $\mathbb{Z}[z][c]$ | discriminant, Galois data |
| Discriminant $\Delta(z) \in \mathbb{Z}[z]$ | palindromic, deg 6 | 3 Galois orbits |
| Möbius pencil $a(q) = (4-q)/(4q+3) = \tau_q(M)$ | $\operatorname{Frac}(\mathbb{Z}[q^{\pm 1}])$ | integration-limit |
| Algebraic residue $\mathrm{Res}^{\mathrm{alg}}_p$ | $\Omega^1(\mathcal{E}_q) \to R$ | A2.4 |
| Principal Galois orbit $\mathcal{O}_{\mathrm{prin}} = \{z_c^\pm\}$ | selected by palindromy + conjugation | innermost orbit |
| Morse wall $q^2+q-1 = 0$ | $\operatorname{Frac}(\mathbb{Z}[q^{\pm 1}, \zeta_5])$ | $q$-moduli boundary |
| Yekutieli MI-integral $\mathrm{MI}\!\int_\Sigma$ | $\Omega^k(A) \to R$ | non-abelian Stokes |
| Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ | $R$-bilinear on $H_n$ | block-by-block character $\chi^\lambda$ |
| Wedderburn weights $y_\lambda(q), \tilde w_\lambda(q)$ | $R$-rational in $q$ | Jones-Markov coefficient |

The framework's **per-λ-block** structure: $H_n(R, q) = \bigoplus_\lambda \mathrm{End}(V_\lambda)$. The Markov trace restricts block-by-block to $\chi^\lambda$. The archimedean realization functor $\tau$ commutes with block decomposition.

## Proposed categorical Δ_λ closure

**Hypothesis (Δ_λ as per-block algebraic residue).**

*Let $V_\lambda$ be the irreducible $H_n(R, q)$-module at partition $\lambda \vdash n$. Define the **per-λ Seiberg–Witten differential** on a per-block analogue $\mathcal{E}_q^{(\lambda)}$ of the Descartes elliptic curve as the projection*

$$
  \lambda^{(k)}_{\mathrm{SW}, \lambda} \;:=\; \pi_\lambda \bigl(\lambda^{(k)}_{\mathrm{SW}}\bigr)
$$

*where $\pi_\lambda: \mathcal{E}_q \to \mathcal{E}_q^{(\lambda)}$ is the block-projection induced by the central idempotent $e_\lambda \in H_n(R, q)$.*

*The corresponding **per-λ principal Galois orbit** $\mathcal{O}_{\mathrm{prin}}^{(\lambda)}$ is the conjugate pair of the per-λ discriminant $\Delta^{(\lambda)}(z) = \pi_\lambda(\Delta(z))$ closest to the fixed locus of complex conjugation.*

*Then*

$$
  \boxed{\;
    \Delta_\lambda(K)
    \;:=\;
    \tau_q\!\Bigl(\sum_{p \in \mathcal{O}_{\mathrm{prin}}^{(\lambda)}}
      \mathrm{Res}^{\mathrm{alg}}_p \bigl(\chi^\lambda(\beta_K) \cdot \lambda^{(k)}_{\mathrm{SW}, \lambda}\bigr)\Bigr).
  \;}
$$

**Properties of this closure form:**

1. **Categorical, not fit-based** — every ingredient (block-projection $\pi_\lambda$, residue, Galois orbit, character $\chi^\lambda$) is intrinsic to the substrate.
2. **Reduces to PR #779 A2.4 at $\lambda = (n)$ (trivial isotype)** — the trivial partition's block is one-dimensional, $\pi_\lambda$ is the identity, $\Delta^{(n)} = \Delta$, $\chi^{(n)} = 1$; the formula reduces to the bare SW-period residue on the full discriminant. ✓
3. **Matches Demazure-fibre topology** — for self-conjugate λ, the Demazure-fibre decomposition refines $\mathcal{O}_{\mathrm{prin}}^{(\lambda)}$ into Demazure sub-orbits per AGENTS.md §7b (Brundan–Kleshchev / Kashiwara crystal-on-Type-B). The crystal-graph weight ansatz from PR #777's table was a coarse approximation of this.
4. **Categorical-ring-side** — the formula is over $R = \mathbb{Z}[q^{\pm 1/2}, \zeta_5]$ for generic $K$; $\tau_q$ provides the archimedean numerical value.
5. **Survives the three-calibration discipline** — uses only $\chi^\lambda$, $y_\lambda$, $\mathrm{Res}^{\mathrm{alg}}$, all derived. No empirical input beyond $q_0$ (CAL-1 anchor on $m_e$).

**Open questions for the closure form:**

- *Per-λ discriminant $\Delta^{(\lambda)}(z)$ — does it factor cleanly from $\Delta(z)$ under $\pi_\lambda$? Or does the block-decomposition require a different polynomial datum (e.g. the per-block Wedderburn discriminant)?*
- *Principal-orbit selection $\mathcal{O}_{\mathrm{prin}}^{(\lambda)}$ — at $\lambda = (1^n)$ (the alternating isotype, baryon channel), is this the same $\{z_c^\pm\}$ as in PR #779, or a smaller orbit?*
- *Numerical verification on D — does this formula give a non-tautological $\Delta_\lambda(D)$ that matches AME 2020 binding to ≤ 1 ppm at q_0?*

## Workplan (sequenced, with parallelism notes)

### Phase 1 — Substantiate the closure form numerically (this PR)

| Task | Files | Effort |
|---|---|---|
| **1a. Author the closure form** as a content block — `prop:delta-lambda-categorical-closure` | `content/quantum-observable-universe/descartes-universe/delta-lambda-categorical-closure.{ts,md,lean}` | small |
| **1b. Verification witness on deuteron** — compute $\Delta_\lambda(D)$ for $n = 6$ partitions via the formula, compare to empirical AME 2020 binding | `computations/delta_lambda_categorical_verification.py` (new) + witness | medium |
| **1c. Update PR #777 status table** — document the closure form as the 7th candidate (categorical, not fit-based) | ledger update | tiny |

### Phase 2 — Extend coverage (follow-up PR)

| Task | Yield |
|---|---|
| **2a. Triton, ³He verification** | extend witness; tests block-projection consistency across $n = 9$ |
| **2b. ⁴He verification** | $n = 12$; first multi-cluster test |
| **2c. ⁶Li, ¹²C** | tests α-clustering ($n = 18, 36$) |

### Phase 3 — Promote to provable block (later PR)

If the numerical verification succeeds:
- Re-classify `conj:delta-lambda-categorical-closure` → `theorem:delta-lambda-categorical-closure`
- Author the Lean proof using PR #779's A2.4 algebraic-residue machinery + block-decomposition lemmas
- Cite the per-block extension of A2.4 as the operative theorem

### Phase 4 — Downstream propagation (separate PRs)

Options A, C, D, F all become downstream of a working Phase 1–3:
- **A** (substrate ρ_K): immediate — once $\Delta_\lambda$ is closed, ρ_K is substrate-pure
- **C** (m_μ): test on $n = 1$ trivial-isotype refinement
- **D** (LP → SDP): independent compute upgrade; can run in parallel
- **F** (PR #781 coord): downstream consumer

### Phase 5 — Adjacent options (E)

- **E** (F1 non-vanishing in `lean/QOU/CategoricalDqSquared.lean`): completely independent of the Δ_λ thread; can run in parallel as a separate branch.

## Why this is most strategic

1. **One closure form unblocks five options simultaneously** (A, B, C, D, F).
2. **Builds directly on merged PR #779/#780 categorical machinery** — no new infrastructure needed; only block-decomposition + residue restriction.
3. **Respects the three-calibration discipline** — no fit-based input.
4. **Substantiates PR #777's diagnosis** — provides the formal version of "$M_\lambda(K)$ as per-block archimedean realization".
5. **High mathematical clarity** — the formula has five named ingredients, each provenance-traceable to a merged content block.

## Risk register

- **High risk (R1)**: the per-λ discriminant $\Delta^{(\lambda)}(z)$ may not factor cleanly; block-decomposition of a polynomial in $z$ may not respect the Hecke block structure.
- **Medium risk (R2)**: numerical $\Delta_\lambda(D)$ may match empirical only loosely (10–50% level), not at 1 ppm. In that case the closure form is qualitatively right but quantitatively requires refinement.
- **Low risk (R3)**: the principal-orbit selection $\mathcal{O}_{\mathrm{prin}}^{(\lambda)}$ may differ from PR #779's selection at non-trivial $\lambda$ — needs explicit derivation.

R1 is the critical risk. Phase 1b will surface it immediately if the discriminant doesn't factor.

## Coordination

- [PR #777](https://github.com/litlfred/qou/pull/777) — workplan v7. This branch's $\Delta_\lambda$ closure is the **7th candidate** under PR #777's table. **Coordination comment posted below.**
- [PR #781](https://github.com/litlfred/qou/pull/781) — mass tables alignment. Downstream consumer of any successful $\Delta_\lambda$ closure. Light-touch intent posted.
- [PR #708] (merged) — Borromean tower closure. The substrate-derived ρ_K starting point; the $\Delta_\lambda$ closure refines this beyond the LO tautology.

## Status

- [x] Audit / workplan doc landed (this file)
- [ ] Phase 1a — closure-form content block authored
- [ ] Phase 1b — verification witness computed
- [ ] Phase 1c — PR #777 ledger updated
- [ ] Phase 2 — extension to T, ³He, ⁴He, ⁶Li, ¹²C
- [ ] Phase 3 — Lean promotion
- [ ] Phase 4 — downstream propagation (A, C, D, F)
- [ ] Phase 5 — E (F1 non-vanishing) — separate parallel branch
