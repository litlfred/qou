**Conjecture (conditional on [`prop:phi-q-aj-machinery-identification`](phi-q-aj-machinery-identification.md) + [`conj:q-zero-complex-extension`](q-zero-complex-extension.md)).**

*The substrate parameter $q_0$ admits a CANONICAL identification with a specific point on the geometric component of the character variety $X(\mathcal{B}_3)$, REALIZED VIA TWO DUAL PERSPECTIVES that coincide by the AJ-conjecture machinery:*

*(a) **Analytic / Stokes side**: $q_0$ is the parameter value at which the Stokes region of the colored-Jones generating function $G_K(x; q) = \sum_N J_N(K; q) \cdot x^N$ transitions between dilog-asymptotic regimes ($\Phi_q$ root-of-unity vs $\mathrm{Li}_2^q$ real).*

*(b) **Algebraic / Hom-functor side**: $q_0$ is the image under the archimedean functor of a specific $\underline{\mathrm{Hom}}_{\mathbf{C}}$-evaluation in the framework's brane-tower category $\mathbf{C}$ over $\mathbb{Z}[q, q^{\pm 1}]$.*

*The two perspectives are related by QOU duality (D17 DIM master Pentagon $\leftrightarrow$ D19 quantum-Langlands), which is exactly the AJ-conjecture machinery $\hat{A}_K \cdot J_N = 0$ in the q-Weyl algebra $\mathcal{A}_q$ over $\mathbb{Z}[q, q^{-1}]$.*

## §1. What's PROVED (100%, no conjecture)

The following can be stated as theorems over $\mathbb{Z}[q, q^{\pm 1}]$:

1. **Mostow-Prasad rigidity** (Mostow 1968 + Prasad 1973): for finite-volume hyperbolic 3-manifolds with $n \ge 3$, the discrete-faithful representation $\rho_{\mathrm{DF}}: \pi_1(S^3 \setminus \mathcal{B}_3) \to PSL_2(\mathbb{C})$ is **unique up to conjugation**. So a distinguished point $[\rho_{\mathrm{DF}}] \in X(\mathcal{B}_3)(\mathbb{C})$ EXISTS and is UNIQUE.

2. **Reid's trace field theorem** (Reid 1990): the trace field $\mathbb{Q}(\mathrm{tr}\,\rho_{\mathrm{DF}})$ is a number field of finite degree over $\mathbb{Q}$. So $[\rho_{\mathrm{DF}}] \in X(\mathcal{B}_3)(\overline{\mathbb{Q}})$ — **algebraic over $\mathbb{Q}$**.

3. **AJ algebraic identity** (Garoufalidis 2004; proved for 2-bridge knots Lê 2006 + many subsequent extensions): the quantum A-polynomial $\hat{A}_K \in \mathcal{A}_q$ annihilates the colored Jones tower: $\hat{A}_K \cdot J_N(K; q) = 0$ in $\mathbb{Z}[q, q^{-1}]$.

4. **Wedderburn decomposition** of $H_n(q)$ over $\mathbb{Z}[q, q^{-1}]$ holds for the Plancherel weights $w_\lambda = d_q(\lambda)^2 / [n]_q!$ — proved for the framework's H_2, H_3, H_4 cases (PRs #1165, #1185, #1238).

## §2. What's CONJECTURED (the gap)

The **specific algebraic identification** of $q_0$ as a particular invariant of $[\rho_{\mathrm{DF}}]$. Three candidate refinements (per [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §11):

(a) **Dehn-deformed representation**: $q_0$ corresponds to an INCOMPLETE hyperbolic structure (Dehn-filled at specific coefficients), where the meridian becomes hyperbolic and $\mathrm{tr}(\rho(\mu)) \ne \pm 2$. The cusp coordinates $(M, L)$ on the A-polynomial curve $A_{\mathcal{B}_3}(L, M) = 0$ trace this deformation.

(b) **Different group element / longitude trace**: $q_0$ might be defined via $\mathrm{tr}(\rho_{\mathrm{DF}}(\lambda))$ (longitude) or a specific peripheral curve — not the meridian (which is parabolic at completion, forcing $\mathrm{tr} = \pm 2$).

(c) **Markov-trace parameterization**: $q_0$ is defined via the Markov-trace normalization $z = 1/(\sqrt{q} + 1/\sqrt{q})$ as a structural anchor at the Hecke-algebra level, with NO direct geometric trace correspondence.

The unifying framing — Option 6 of the audit §13 — uses Stokes asymptotics:

$$q_0 \;=\; \text{(parameter at which the Stokes structure of $G_{\mathcal{B}_3}(x; q)$ transitions)}$$

and connects via QOU duality to:

$$q_0 \;=\; \iota(\underline{\mathrm{Hom}}_{\mathbf{C}}(\text{some specific objects})(\text{evaluated at}\ \mathbb{Z}[q, q^{-1}]))$$

where $\mathbf{C}$ is the framework's brane-tower category, $\iota$ is the archimedean functor.

## §3. Universal base: everything over $\mathbb{Z}[q, q^{\pm 1}]$

Per author directive: *"I want all to work over $\mathbb{Z}[q, q^{-1}]$"*.

The Iwahori-Hecke algebra $H_n(q)$ is naturally an algebra over $\mathbb{Z}[q, q^{\pm 1}]$ (the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ has integer-Laurent coefficients). All structural identities — Wedderburn weights, Markov trace, P_m/Q_m, AJ recurrence, Φ_q/Li_2^q dilog — can be stated over this universal base.

**Specialization to our universe:** apply the archimedean functor $\iota_\infty: \mathbb{Z}[q, q^{\pm 1}] \to \mathbb{R}$ at $q := q_0$ (with $q_0$ the specific algebraic value selected by CAL-2). Physical observables ($m_p / m_e$, etc.) are then the images of $\mathbb{Z}[q, q^{\pm 1}]$-valued algebraic expressions under this specialization.

**Char-p universes** (mathematical, not physical): specialize $\mathbb{Z}[q, q^{\pm 1}] \to \mathbb{F}_p[q, q^{\pm 1}]$ for any prime $p$ not dividing relevant denominators. Structural identities continue to hold.

## §4. The duality (Stokes $\leftrightarrow$ Hom-functor)

The two candidate identifications (Option 4 Hom + Option 6 Stokes from [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §12) are **DUAL VIEWS of the SAME structure** via QOU duality:

| Side | Object | What's evaluated |
|---|---|---|
| **Analytic (Stokes)** | $G_K(x; q) = \sum J_N(K; q) x^N$ | Asymptotic at $N \to \infty$ |
| **Algebraic (Hom)** | $\underline{\mathrm{Hom}}_{\mathbf{C}}(\text{object}, \text{object})$ | Categorical evaluation |
| **Bridge (AJ)** | $\hat{A}_K \in \mathcal{A}_q$ | q-difference recurrence |

The AJ identity $\hat{A}_K \cdot J_N = 0$ over $\mathbb{Z}[q, q^{\pm 1}]$ is precisely the **categorical-vs-analytic translation**:

- Read algebraically: $\hat{A}_K$ as a Hom in the q-Weyl algebra
- Read analytically: $\hat{A}_K$ as the operator whose saddle-points define the Stokes regions of $G_K$

These coincide because of the Volume-Conjecture asymptotic of $J_N$ — proved for many specific knots (Kashaev-Murakami-Murakami 2001 onwards), conjectural in general.

## §5. The 100%-proved track

Per author directive: *"lets put in paper lean all that we can and narrow unproven until we work it out. 100% proved"*

This conjecture is decomposed into a chain where each step is INDEPENDENTLY trackable:

```
[PROVED] Mostow-Prasad: ∃! ρ_DF up to conjugation
    ↓
[PROVED] Reid: trace field of ρ_DF is in $\overline{\mathbb{Q}}$ (number field)
    ↓
[PROVED] X(K)_Z is a Z-scheme of finite type (Procesi)
    ↓
[CONJECTURE A] specific identification q_0 = f([ρ_DF]) for some
              algebraic invariant f — the OPEN gap.
    ↓
[CONJECTURE B] AJ for B_3 specifically (likely proved in literature,
              needs Hikami/Habiro reference verification)
    ↓
[PROVED conditional on A+B] structural framework downstream.
```

The conjecture is exactly the gap at step A — promoting it from CONJECTURE to PROVED is the work.

## §6. Lean formalization (conditional class per §3b-cond)

[`q-zero-stokes-region-identification.lean`](q-zero-stokes-region-identification.lean) encodes this as a **conditional class structure** per AGENTS.md §3b-cond:

- Class `MostowPrasadDistinguished K` — axiomatizes Mostow-Prasad $\exists!$
- Class `ReidTraceField K` — axiomatizes trace-field-in-number-field
- Class `QZeroStokesIdentification K` — the CONDITIONAL identification (= the open gap)
- Theorems consuming these classes give the chain of conditional results

The Lean `sorry` count is EXACTLY ONE per OPEN GAP — not per missing tactic.

## §7. Cross-references

- [`prop:phi-q-aj-machinery-identification`](phi-q-aj-machinery-identification.md) — Φ_q / Li_2^q $\leftrightarrow$ AJ machinery
- [`conj:q-zero-complex-extension`](q-zero-complex-extension.md) — q_0 may not be real
- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — distinguishing the involutions
- [`borromean-markov-trace-closed-form.md`](borromean-markov-trace-closed-form.md) — the closed form whose categorical derivation is the rescoped Path B
- [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §§11-13 — origin of this conjecture
- [`docs/coordination/-post-1231-wire-up-ledger.md`](../../../docs/coordination/-post-1231-wire-up-ledger.md) — session ledger

## §8. Honest assessment

**What's NEW in this conjecture (vs prior content blocks):**
- Explicit identification of the structural gap (Option A from §11 of the audit)
- Universal-base framing over $\mathbb{Z}[q, q^{\pm 1}]$
- Duality between Stokes-asymptotic + Hom-functor views via AJ
- Lean conditional-class structure for the 100%-proved track

**What this does NOT claim:**
- A specific algebraic formula for $q_0$ (the GAP)
- That all candidate identifications (a)/(b)/(c) from §2 reduce to the same thing
- That AJ is proved for $\mathcal{B}_3$ specifically (needs literature verification)

**What this enables:**
- Lean development can proceed with explicit class hypotheses
- Future probes can target the conjecture-A gap directly (e.g., compute $A_{\mathcal{B}_3}(L, M)$ classical + identify q_0 on the curve)
- The framework's $q_0$ stays well-defined under different conjecture statuses
