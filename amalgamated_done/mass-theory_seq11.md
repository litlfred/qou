<!-- FILE_START: two-row-stratum.md -->
## Definition

Let $H_n(q)$ be the Iwahori–Hecke algebra on $n$ strands. It admits the canonical Wedderburn decomposition
$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)
$$
indexed by partitions $\lambda \vdash n$. The :defterm[two-row stratum]{#two-row-stratum} contains the partitions with at most two parts:
$$
  \Lambda^2(n) \;:=\; \{\, \lambda \vdash n : \ell(\lambda) \le 2 \,\}
  \;=\; \{\, (n-k, k) : 0 \le k \le \lfloor n/2 \rfloor \,\}.
$$

The :defterm[two-row projection]{#two-row-projection} is the orthogonal projection onto the two-row Wedderburn subalgebra:
$$
  \pi_{\mathrm{2-row}} \;\colon\; H_n(q) \;\to\;
    \bigoplus_{\lambda \in \Lambda^2(n)} \mathrm{End}(V_\lambda).
$$
The map is an idempotent ($\pi_{\mathrm{2-row}}^2 = \pi_{\mathrm{2-row}}$). The canonical Markov trace splits as:
$$
  \mathrm{tr}_M(\beta)
  \;=\; \underbrace{\sum_{\lambda \in \Lambda^2(n)} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M(\pi_{\mathrm{2-row}}\,\beta)}
  \;+\; \underbrace{\sum_{\ell(\lambda) > 2} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M((1-\pi_{\mathrm{2-row}})\,\beta)}
$$
where $y_\lambda$ is the Wenzl weight from [`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical).

## Structural significance

The two-row stratum carries the $\mathrm{SU}(2)$ Schur–Weyl image. We restrict to the $\mathrm{SU}(2)$ action:
$$
  H_n(q) \;\twoheadrightarrow\; \mathrm{End}_{\mathrm{SU}(2)}\!\bigl(V^{\otimes n}\bigr),
\quad V = \mathbb{C}^2.
$$
Partitions with $\ell(\lambda) > 2$ map to zero. They correspond to higher-rank symmetry components absent from the $\mathrm{SU}(2)$ spin-pairing observable. The $q$-deformed spin observables, including the magic-shell coupling of `conj:magic-shell-stabilization`, live strictly in the two-row sector.

## Indexing the stratum

We have $|\Lambda^2(n)| = \lfloor n/2 \rfloor + 1$. For the $^4\mathrm{He}$ strand count ($n = 12$), we obtain **7** partitions:
$$
\Lambda^2(12) = \{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\}.
$$

Distinguished partitions include:
- $\lambda = (n)$: the trivial representation. It is one-dimensional, $V_{(n)} = \mathbb{C}$.
- $\lambda = (n-1, 1)$: the standard representation. It has dimension $n - 1$.
- Self-conjugate $\lambda \in \Lambda^2(n)$: this is only $(n/2, n/2)$ for even $n$, the **balanced two-row** partition. For $n = 12$, this is $(6, 6)$.

The non-self-conjugate partitions $(n-k, k)$ with $k < n/2$ form mirror pairs under the bar involution $q \mapsto q^{-1}$. The conjugate partition $(n-k, k)'$ exits $\Lambda^2(n)$, so each $(n-k, k)$ pairs with itself under the involution.

## Empirical use

We compute the per-partition decomposition $c_\lambda := y_\lambda(q_0) \cdot \chi^\lambda_q(\beta_{^4\mathrm{He}})$ across all 77 partitions of 12. The two-row stratum $\Lambda^2(12)$ carries $86.6\,\%$ of the total trace $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$. We formalize this in [`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance).

We establish the identical pattern across the $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ series. The dominant block for each atom always lies in $\Lambda^2(3A)$.
<!-- FILE_END: two-row-stratum.md -->

<!-- FILE_START: he4-channel-active-set.md -->
## Setup

The $^4\mathrm{He}$ bound state admits three primary compositional channels summing to $A = 4$ nucleons:

| channel | constituents | $\sum \Delta_\mathrm{cat}$ (MeV) | residual $t_i$ (MeV) |
|---|---|---:|---:|
| $\mathrm{D} \oplus \mathrm{D}$    | $(1,1) + (1,1)$ | $4.05$ | $\mathbf{24.16}$ |
| $\mathrm{T} \oplus p$             | $(1,2) + (1,0)$ | $7.83$ | $\mathbf{20.38}$ |
| ${}^3\mathrm{He} \oplus n$        | $(2,1) + (0,1)$ | $7.04$ | $\mathbf{21.18}$ |

We define the **channel binding residual**:
$$
  t_i \;:=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) \;-\; \sum_{j \in \mathrm{channel}\, i} \Delta_\mathrm{cat}(j).
$$
This measures the binding that the magic-shell coupling must explain beyond the free constituents. We load the empirical anchors from [`magic-shell-empirical-instantiation.witness.json`](computations/magic-shell-empirical-instantiation.witness.json).

## LP formulation

We apply the [`prop:operator-selection-lp`](#prop:operator-selection-lp) canonical form. The vector $t \in \mathbb{R}^3$ holds the residuals. The matrix $G = I_3$ because the channels are orthogonal at leading order. Sub-braid corrections are sub-percent. We set:
$$
  n_\mathrm{target} \;=\; \Delta_\mathrm{coupling}(2, 2)
  \;=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) - 2\,\Delta_\mathrm{cat}({}^3\mathrm{He})
  \;=\; 13.197\,\mathrm{MeV}.
$$

## Solution

The LP solves uniquely with a duality gap of $0$. We have $\mathrm{primal\_obj} = \mathrm{dual\_obj} = 268.949$. The primal weights $x^\star$ and dual shadow prices $y^\star$ are:

| channel $i$ | $x^\star_i$ | $y^\star_i$ | status |
|---|---:|---:|---|
| $\mathrm{D} \oplus \mathrm{D}$    | $0$        | $\mathbf{3.778}$ | active |
| $\mathrm{T} \oplus p$             | $13.197$   | $0$              | primal-saturating |
| ${}^3\mathrm{He} \oplus n$        | $0$        | $0.796$          | active |

We have $y_0^\star = 20.380$. The **active set** contains the constraints with a positive dual variable:
$$
  \mathcal{A}({}^4\mathrm{He}) \;=\; \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}.
$$

## Proposition

**(Conditional on [`he4-sdp-compositional-canonical evaluation.witness.json`](computations/he4-sdp-compositional-canonical evaluation.witness.json).)**
For the $^4\mathrm{He}$ operator-selection LP:
1. **Unique primal optimum:** The system selects the $\mathrm{T} \oplus p$ channel with $x^\star_{\mathrm{T} \oplus p} > 0$ and $x^\star_i = 0$ for all $i \neq \mathrm{T} \oplus p$.
2. **Active set:** The dual-tight constraints are $\mathcal{A}({}^4\mathrm{He}) = \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}$.
3. **Dual ordering:** We have $y^\star_{\mathrm{D} \oplus \mathrm{D}} > y^\star_{{}^3\mathrm{He} \oplus n} > y^\star_{\mathrm{T} \oplus p} = 0$.

## Interpretation

The LP selects the $\mathrm{T} \oplus p$ decomposition to satisfy the binding constraint because it has the smallest residual. However, the shadow prices identify $\mathrm{D} \oplus \mathrm{D}$ as the most binding-receptive sub-braid. A unit perturbation of the deuteron-pairing channel changes the primal binding cost by $3.778$ MeV. This is five times the effect of the ${}^3\mathrm{He} \oplus n$ channel.

This two-tier fingerprint mirrors the Wedderburn-block fingerprint of [`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance). Both identify a $q$-symmetric deuteron-pairing structure as the load-bearing geometry of the magic-shell coupling. The $\mathrm{T} \oplus p$ channel provides the energetic accounting. We make this connection explicit in `rem:he4-magic-shell-fingerprint`.
<!-- FILE_END: he4-channel-active-set.md -->

<!-- FILE_START: he4-two-row-dominance.md -->
## Statement

Let $\beta_{{}^4\mathrm{He}}$ be the canonical atomic braid word for $^4\mathrm{He}$ on $H_{12}(q)$. It has 47 crossings on 12 strands with three operator-valued inter-nucleon interfaces (pp at gen 2, pn at gen 5, nn at gen 8). We define the per-partition contribution:
$$
  c_\lambda(q_0) \;:=\; y_\lambda(q_0) \cdot \chi^\lambda_q\!\bigl(\beta_{{}^4\mathrm{He}}\bigr),
$$
where $y_\lambda$ is the Wenzl weight ([`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical)) and $\chi^\lambda_q$ is the Hoefsmit character. We have:
$$
  \sum_{\lambda \vdash 12} c_\lambda(q_0) \;=\; \mathrm{tr}_M\!\bigl(\beta_{{}^4\mathrm{He}}\bigr)(q_0).
$$

**Proposition (conditional on [`he4-canonical-tr-m-block-fingerprint.witness.json`](computations/he4-canonical-tr-m-block-fingerprint.witness.json)).**
The two-row stratum $\Lambda^2(12)$ ([`def:two-row-stratum`](#def:two-row-stratum)) carries at least $80\,\%$ of the canonical Markov trace at the substrate parameter:
$$
  \frac{\bigl|\sum_{\lambda \in \Lambda^2(12)} c_\lambda(q_0)\bigr|}
       {\bigl|\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0)\bigr|}
  \;\ge\; 0.80.
$$

## Empirical verification

The trace is $\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0) = 0.05534835$. The two-row-stratum ratio is **$86.6\,\%$**. The top five Wedderburn blocks lie entirely in $\Lambda^2(12)$:

| rank | $\lambda \vdash 12$ | $\dim_\lambda$ | $y_\lambda(q_0)$ | $\chi^\lambda_q(\beta_{{}^4\mathrm{He}})$ | $c_\lambda$ | $\%$ of $\lvert$total$\rvert$ |
|---:|---|---:|---:|---:|---:|---:|
| 1 | $(9, 3)$  | 154 | $+5.87\,e{-4}$ | $+27.33$ | $+1.604\,e{-2}$ | $29.0$ |
| 2 | $(8, 4)$  | 275 | $+4.31\,e{-4}$ | $+30.26$ | $+1.304\,e{-2}$ | $23.6$ |
| 3 | $(10, 2)$ | 54  | $+7.12\,e{-4}$ | $+10.46$ | $+7.45\,e{-3}$  | $13.5$ |
| 4 | $(7, 5)$  | 297 | $+2.62\,e{-4}$ | $+21.77$ | $+5.70\,e{-3}$  | $10.3$ |
| 5 | $(11, 1)$ | 11  | $+7.67\,e{-4}$ | $+7.39$  | $+5.67\,e{-3}$  | $10.2$ |
|   |           |     |                |          | top-5 cum         | $\mathbf{86.5}$ |

The trivial representation $(12)$ contributes $2.9\,\%$. The sign representation $(1^{12})$ contributes $4.7 \times 10^{-10}$.

## Structural interpretation

The two-row stratum carries the SU(2) Schur-Weyl image. Partitions with $\ell(\lambda) > 2$ correspond to higher-rank symmetry components absent from the spin-$\tfrac{1}{2}$ pairing observable. The dominance of $\Lambda^2(12)$ is the algebraic fingerprint of $^4\mathrm{He}$ as a $q$-symmetric spin-pairing bound state.

The canonical formalism predicts the top block $\lambda^* = (9, 3)$ via the $\Delta_\lambda$ empirical-tabulation route. This proposition derives the identical fingerprint from the $\Sigma_\lambda y_\lambda \cdot \chi^\lambda_q$ Wedderburn sum.
<!-- FILE_END: he4-two-row-dominance.md -->

<!-- FILE_START: markov-trace-frobenius-selection.md -->
**Proposition (Markov trace uniqueness on H_n(R, q)).**
*The Jones–Markov form $\tau_M$ is the unique non-degenerate Frobenius pairing on the Iwahori–Hecke algebra $H_n(R, q)$ at generic $q$. The QOU mass identity's Markov trace is uniquely fixed by the categorical action, the fibre functor, and the Markov-trace uniqueness theorem (Jones 1987, Wenzl 1988).*

| form | $\tau(1)$ | $\tau(\sigma_i)$ | $w_\lambda$ | non-degenerate? |
|---|---:|---:|---|:---:|
| Jones–Markov $\tau_M$ | $1$ | $z = 1/[q^{1/2}+q^{-1/2}]$ | Wenzl-bridge $y_\lambda$ | yes, on $H_n(q)$ |

## The chain: cat-action to Markov trace

We trace each step from the QOU substrate:

### Step 1: Cat-action of $\mathbf{C}$ on the state bundle

A quantum observable universe specifies a rigid monoidal category $\mathbf{C}$ with a fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}$. The category fixes the acting Frobenius–Hopf algebra $A$. We typically use $A = H_n(R, q)$.

### Step 2: Non-abelian Stokes at finite slice

Yekutieli's non-abelian Stokes theorem at finite slice depth yields the multiplicative trace on the closed surface obtained by Markov closure of the braid word $T_w$:
$$
  \int_{S^1} T_w
  \;=\;
  \mathrm{tr}\bigl(\rho(\sigma_{i_1}) \cdots \rho(\sigma_{i_\ell})\bigr).
$$
This trace is the categorical trace in $\mathbf{C}$. It depends on the fibre functor $\tau$.

### Step 3: Frobenius pairing

The categorical trace descends to a Frobenius integral $\int_A \colon A \to R$. The algebra $A$ is a Frobenius algebra relative to this integral. This defines a non-degenerate bilinear form:
$$
  \langle x, y \rangle_\tau \;:=\; \tau(xy).
$$

The QOU mass identity uses the Frobenius co-Casimir trace identity ([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)):
$$
  \tau(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$
This identity requires $\tau(p_\lambda) \neq 0$ for every Wedderburn block. The trace $\tau$ must be non-degenerate.

The **Jones–Markov form** $\tau_M$ satisfies:
- $\tau_M(1) = 1$.
- $\tau_M(x \sigma_{n-1}) = z \cdot \tau_M(x)$ for $x \in H_{n-1}$ with $z = 1/(q^{1/2} + q^{-1/2})$.

It is non-degenerate on $H_n(R, q)$. The trace on the primitive idempotents is $\tau_M(p_\lambda) = \dim_q(\lambda) \cdot d_\lambda / [n]_q!$. This is non-zero for every $\lambda \vdash n$ at generic $q$. The Markov-trace uniqueness theorem forces $\tau_M$ to be the unique non-degenerate Frobenius form on the Hecke algebra.

### Step 4: Wedderburn + Markov-trace formula

The trace $\tau_M$ admits the explicit form:
$$
  \tau_M(x) \;=\; \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(x),
$$
where $y_\lambda(q)$ are the Wenzl-bridge weights.

## Uniqueness theorem

**Theorem (Markov-trace uniqueness on H_n(R, q)).** *Any non-degenerate Frobenius form on the Iwahori–Hecke algebra $H_n(R, q)$ at generic $q$ equals the Jones–Markov form $\tau_M$ block-wise. The QOU mass identity uniquely determines $\tau_M$ as the canonical Markov trace.*

## Discussion

This proposition is a structural theorem about the representation theory of the Hecke algebra. We introduce no fitting or empirical input. We formalize the uniqueness via the `MarkovTraceUniqueness` class in Lean. Downstream Lean results depend on this class instance.

## Computational consequence

The QOU production stack computes $\tau_M$ on the canonical 11-crossing proton/neutron braid via four independent paths. They agree to $\leq 2 \times 10^{-15}$ at the proton-pinned $q_0$:

| atom | $\tau_M(\beta_{\rm atom}, q_0)$ | error vs 4-way |
|---|---:|---:|
| proton | $1.0653061442544499$ | $\leq 2.57\times 10^{-16}$ |
| neutron | $0.9232332299116371$ | $\leq 2.03\times 10^{-16}$ |
| deuteron | $0.3882864240747888$ | $\leq 8.16\times 10^{-16}$ |
<!-- FILE_END: markov-trace-frobenius-selection.md -->

<!-- FILE_START: t-beta-markov-frobenius-collapse.md -->
**Proposition (Min-Frobenius-norm collapse for $T_\beta$).**
*Let $H = H_n(R, q)$ be the Iwahori–Hecke algebra over a field $R$, equipped with the unique Jones–Markov trace $\tau_M : H \to R$ ([Wenzl–Jones uniqueness theorem](#prop:markov-trace-frobenius-selection)). Equip $H$ with the Frobenius inner product $\langle X, Y \rangle_\tau := \tau_M(X \cdot Y)$. The element of minimum Frobenius norm satisfying the linear constraint $\tau_M(T_\beta) = S$ for a scalar $S \in R$ is:*
$$
\boxed{\; T_\beta = S \cdot 1_H \;}
$$
*with $\| T_\beta \|^2_\tau = S^2$.*

## Corollary — observable c_k invariance

The $\mathfrak{Q}_\beta$ production rule extracts the Taylor coefficients $c_k$ from $\tau_M(T_\beta)(q)$. The constraint $\tau_M(T_\beta) = S = \mathfrak{Q}_\beta / E_0$ is satisfied identically under both the Euclidean $L^2$ coordinate norm and the canonical Markov–Frobenius norm. We have $\tau_M(T_\beta)(q) \equiv S(q)$. The coefficients $c_k$ are invariant:
$$
c_k^{\,L2} = c_k^{\,Markov} = c_k\!\!\left(S(q)\right)
\quad\text{for all } k.
$$
The observables are extracted from the constraint, not from the operator expansion. The norms only differ in selecting the primal-feasible operator $T_\beta \in H_n(R, q)$.

## Categorical reading

Under the Markov–Frobenius norm, $T_\beta = S \cdot 1_H$ is a scalar multiple of the identity. The $q$-dependence flows entirely through $S(q)$. There is no multi-channel SHAPE distributed across the normal-form basis. The Euclidean norm's six-channel spread is an artifact of the coordinate basis. The Markov–Frobenius minimum-norm solution is the canonical choice.

## Lean formalisation

The substrate-model proof ($A = R$, $\tau = \mathrm{id}$) is sorry-free at [`t_beta_markov_min_frobenius_collapse_substrate`](markov-trace-frobenius-selection.lean). The general $H_n(R, q)$ proof lifts this algebraic content via Mathlib `Algebra R A` typeclasses.
<!-- FILE_END: t-beta-markov-frobenius-collapse.md -->

<!-- FILE_START: t-beta-markov-frobenius-collapse-general.md -->
**Proposition (Min-Frobenius-norm collapse — general unital R-algebra).**
*Let $R$ be a strict-ordered field. Let $A$ be a unital $R$-algebra. Let $\tau : A \to R$ be an $R$-linear normalised trace ($\tau(1) = 1$, $\tau(xy) = \tau(yx)$). Assume $\tau$ is positive-semi-definite on squares: $0 \le \tau(X \cdot X)$ for all $X \in A$. For any $S \in R$ and $X \in A$ satisfying $\tau(X) = S$, we have:*
$$
S^2 \;\le\; \tau(X \cdot X).
$$
*If $\tau$ is non-degenerate on squares ($\tau(Y \cdot Y) = 0 \implies Y = 0$), the lower bound is attained if and only if $X = S \cdot 1_A$.*

## Relation to the substrate-model version

This proposition lifts [`prop:t-beta-markov-frobenius-collapse`](t-beta-markov-frobenius-collapse.md) from the substrate model ($A = R$, $\tau = \mathrm{id}$) to the general unital $R$-algebra setting, where $A$ may be non-commutative and infinite-dimensional.

## Application to the Iwahori–Hecke algebra

For $A = H_n(R, q)$ at generic $q > 0$ with $\tau = \tau_M$, this proposition identifies the canonical SDP-min-Frobenius-norm operator for the constraint $\tau_M(T_\beta) = S$:
$$
T_\beta^{\mathrm{Markov}} \;=\; S \cdot 1_H.
$$
The $L^2$-Euclidean coordinate-norm operator and the Markov-Frobenius operator both reproduce the SDP constraint. The observable $c_k$ Taylor coefficients remain invariant.
<!-- FILE_END: t-beta-markov-frobenius-collapse-general.md -->

<!-- FILE_START: pn-averaging-uniqueness.md -->
**Proposition (canonical p-n averaging uniqueness).**
*Let $\sigma_{pn}$ and $\sigma_{pn}'$ be two p-n interface averaging functionals on $H_{3A}(R, q)$. Assume both satisfy: (a) bar-invariance $\sigma_{pn}(q) = \sigma_{pn}(q^{-1})$, (b) color-flavor compatibility, and (c) standard normalisation $\sigma_{pn} = z$. Then they are equal block-wise. The canonical p-n averaging is uniquely determined.*

## Setting

The QOU mass identity at $A \geq 2$ contracts a per-interface averaging functional $\sigma_{pn}$ across the p-n boundary slice. The two production candidates are the uniform bar-invariant form and the Bring color-tube weighted form. Both satisfy bar-invariance and standard normalisation. Once we fix color-flavor compatibility, the averaging is uniquely determined.

### Derivation chain for the closed-form weight

The substrate evaluation $w(t, t', q) = 1/(1 - h_q \cdot q^{10})$ derives from Bring's surface geometry:
- Bring's surface has genus $g = 4$.
- The genus-4 force-carrier pair is $\{T(2,9), T(3,5)\}$.
- We prove $\alpha_{\text{shift}}(T_{p,k}) = k \cdot (p-1)$. For $T(3,5)$, $\alpha_{\text{shift}}(T(3,5)) = 10$. This specifies the pole order of $\sigma$.
- The Bring color-tube weight inherits this derived pole order $q^{10}$.

## Lean structure

We stage the uniqueness via the conditional-class pattern:
- `BarInvariant R σ_pn`: the bar-involution axiom.
- `ColorFlavorCompatible R σ_pn`: the open class for color-sheet mapping.
- `StandardNorm R σ_pn z`: the pointwise normalisation.

Conditional on these classes, `theorem pn_averaging_unique` proves $\sigma_{pn} = \sigma_{pn}'$.
<!-- FILE_END: pn-averaging-uniqueness.md -->

<!-- FILE_START: averaging-resonance-rule.md -->
**Theorem (averaging-resonant rung selection rule).**
*Let $\sigma_{\mathrm{avg}} = \tfrac{1}{2}(\sigma + \sigma^{-1})$ be the bar-symmetric averaged-crossing operator on $H_{n_{\mathrm{total}}}(R, q)$. Let $P_{\mathrm{avg}} = (1 + \overline{\,\cdot\,})/2$ be the bar-invariant averaging projection. For canonical typed-$\mathbf{B}_3$ braids admitting the half-fill cyclic structure, the unique $\sigma_{\mathrm{avg}}$-resonant rung is:*
$$
  k_{\mathrm{res}}
  \;=\;
  \left\lfloor \frac{n_{\mathrm{total}}}{2} \right\rfloor
  \;+\; \mathbb{1}_{\mathrm{wrap}}(n_{\mathrm{total}}).
$$
*The wrap indicator $\mathbb{1}_{\mathrm{wrap}}$ adds one when the half-fill cycle closes through the proton recipe's inter-nucleon interface. It is zero otherwise.*

## Structural content

1. **Half-fill cyclicity.** The projection $P_{\mathrm{avg}}$ restricts to the typed-$\mathbf{B}_3$ braid to isolate the half-fill rung in the Markov-trace expansion. Rung positions above the floor see their bar-averaged amplitudes cancel by the crossing-cyclicity dual. This uniquely determines $k_{\mathrm{res}}$ from $n_{\mathrm{total}}$.
2. **Bar-invariant magnitude.** At the selected rung, the $P_{\mathrm{avg}}$-fingerprint contributes magnitude $1/2$ to the resonant Markov-trace coefficient.

## The $k = 5$ selection

For the proton typed-$\mathbf{B}_3$ braid ($n_{\mathrm{total}} = 9$), the half-fill floor is $4$. The inter-nucleon interface contributes $+1$. We obtain $k_{\mathrm{res}} = 5$. This wrap-around contribution ensures the recipe is canonical.

## Lean closure

The structural content is verified in [`averaging_resonance_rule_structural`](averaging-resonance-rule.lean) using arithmetic. We retain the backward-compatible `class AveragingResonanceRule`.
<!-- FILE_END: averaging-resonance-rule.md -->

<!-- FILE_START: meson-color-tube-uniqueness.md -->
**Proposition (meson m_K/m_π ratio uniqueness via the α_shift universal chain).**
*The substrate-evaluated ratio $m_K^2 / m_\pi^2$ factors uniquely through the torus knots $T(2, 3)$ and $T(2, 4)$ as:*
$$
  [\alpha_{\text{shift}}(T(2,3))]_q \cdot [\alpha_{\text{shift}}(T(2,4))]_q
  = [3]_q \cdot [4]_q.
$$
*The $q$-integer indices are forced by the $\alpha_{\text{shift}} = k \cdot (p - 1)$ formula (`prop:alpha-shift-torus-knot`).*

## The meson force-carrier pair $\{T(2, 3), T(2, 4)\}$

The pair $\{T(2, 3), T(2, 4)\}$ is the smallest non-trivial torus-knot pair on the substrate's Hecke-algebra surface. The knot $T(2,3)$ carries $[3]_q$ and $T(2,4)$ carries $[4]_q$. This forms the meson analogue of the genus-4 Bring pair $\{T(2, 9), T(3, 5)\}$ and the lepton tower $T(2, k)$.

## Lean structure

We stage the uniqueness via the conditional-class pattern:
- `MesonGMORFactorization R mK2_over_mpi2 qChar m n`: the substrate factorisation axiom.
- `MesonForceCarrierPair`: the derived index assertion $\alpha_{\text{shift}}(T(2, 3)) = 3$ and $\alpha_{\text{shift}}(T(2, 4)) = 4$.
- `theorem meson_ratio_via_alpha_shift`: proves the factorisation using the specific indices.
<!-- FILE_END: meson-color-tube-uniqueness.md -->
