**Remark (per-partition $k_\lambda$ — the open structural form of $n_\star$).**

The level-selection rule $n_\star$ of
[conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro) was tested
empirically against the AME light-isotope sample $\{D, T, {}^3\mathrm{He}\}$
under three increasingly-refined ansatze, and is now sharpened to the
following structural form. The progression of refutations
 and partial closures localises the open piece.

## Refutation chain (substrate-only scalar candidates)

| Form of $n_\star$ | Verdict | Witness |
|:---|:---:|:---|
| Scalar-eigenvalue family (uniform $k$, GB grade, additive $\ell n_0 + k$) | **refuted** |  §"Closure: scalar-eigenvalue form$\ldots$" |
| Per-eigenvalue operator-valued ($\Phi_q$ per $\mu_a^{(\lambda)}$, signed) | **refuted** at uniform $k$ |  §"Operator-valued probe" |
| Type-B-folded-crystal depth ($\#\{\lambda \vdash 3A : \lambda = \lambda^T\}$) | **partial** — fits $D$ and $T$, fails ${}^3\mathrm{He}$ | [probe-phiq-type-b-fold-depth.witness.json](https://github.com/litlfred/qou/blob/main/computations/probe-phiq-type-b-fold-depth.witness.json) |
| Type-B + scalar near-pole multiplicity $m$ (4 two-input rules) | **refuted** | [probe-phiq-multiplicity-refinement.witness.json](https://github.com/litlfred/qou/blob/main/computations/probe-phiq-multiplicity-refinement.witness.json) |

## Sharpened open form: per-partition $k_\lambda$

's analysis of #638's per-eigenvalue spectra showed that the
**failure at uniform $k = 2$ is dominated by ONE partition per atom**:

| Atom | dominant $\lambda$ | $\dim V_\lambda$ | $\text{contrib}_\lambda(k=2)$ | $\text{contrib}_\lambda(k=1)$ |
|:---|---:|---:|---:|---:|
| $D$ | $[2, 2, 1, 1]$ | $9$ | $-6.220$ | $\approx 0$ |
| $T$ | $[6, 3]$ | $48$ | $-3.001$ | $+0.050$ |
| ${}^3\mathrm{He}$ | $[5, 4]$ | $42$ | $-11.692$ | $-0.028$ |

Re-assigning $k_\lambda = 1$ for the dominant partition while keeping
$k_\lambda = 2$ for the other 29-or-so partitions collapses each
atom's total tower magnitude to $\lvert\mathrm{tower}\rvert < 2$
(vs uniform-$k$ towers in the range $5$–$11$).

This is the **sufficient relaxation** — non-uniform truncation
across Wedderburn blocks closes the gap that *no* scalar rule
(fold depth alone, $m_{\text{near-pole}}$ alone, or any 2-input
combination) could close at uniform $k$. The surviving open form
of the conjecture is:

> **Per-partition $k_\lambda$ form of $n_\star$.** *There exists a
> substrate-derivable map*
>
> $$
>   k_\lambda \;\colon\; \{\text{partitions of } 3A\}
>   \;\longrightarrow\; \mathbb{N}_{\geq 1},
> $$
>
> *such that*
>
> $$
>   \mathrm{tower}_{\mathrm{op}}^{(k_\lambda)}(\beta_\mathfrak{H})
>   \;:=\;
>   \Biggl\lvert
>   \sum_\lambda y_\lambda(q_0) \cdot
>     \sum_{a=1}^{\dim V_\lambda}
>       \Phi_q^{[\leq k_\lambda]}\bigl(\mu_a^{(\lambda)}\bigr)
>   \Biggr\rvert
> $$
>
> *closes the AME light-isotope binding* $B(\mathfrak{H})$ *to within
> $\sim 5\%$ across* $\{D, T, {}^3\mathrm{He}\}$ *without per-atom
> retuning of the rule itself.*

The empirical evidence
([probe-phiq-per-partition-klambda.witness.json](https://github.com/litlfred/qou/blob/main/computations/probe-phiq-per-partition-klambda.witness.json))
shows that the rule

$$
  k_\lambda = \begin{cases}
    1 & \text{if } \lambda \text{ is the maximum-} \lvert\mu\rvert \text{ partition of } \beta_\mathfrak{H}, \\
    2 & \text{otherwise}
  \end{cases}
$$

closes all three atoms simultaneously. The "max-$\lvert\mu\rvert$"
selector is a substrate property of the **braid word**'s action on
$V_\lambda$, not just of $\lambda$ in isolation — it distinguishes
${}^3\mathrm{He}$ (max $\lvert\mu\rvert \approx 10.69$ at $[5, 4]$)
from $T$ (max $\lvert\mu\rvert \approx 8.23$ at $[4, 3, 1, 1]$)
despite identical strand count $n = 9$.

## Why this is structurally meaningful

The eigenvalue magnitudes of $\rho_\lambda(\beta)$ in the Hoefsmit
seminormal form depend on **both** the partition $\lambda$ and the
braid word $\beta$. For a given $\lambda$, larger $\lvert\mu\rvert$
indicates the braid word's action has higher "winding" or
"twist" content in that Wedderburn block. The empirical pattern —
that *the* maximum-$\lvert\mu\rvert$ partition is the one requiring
shallower truncation — is consistent with the dilogarithm tail
intuition: deeper truncation $\Phi_q^{[\leq k]}$ amplifies
contributions of large-magnitude eigenvalues
(each factor $1/(1 - q^{-j} \mu)$ for fixed $j$ becomes more
sensitive to $\lvert\mu\rvert$ as $k$ grows).

## What this rules in / out

**Rules in:**

* The Wedderburn-decomposition of the brane-tower operator is the
 **correct level of structure** at which to formulate $n_\star$ —
 not a single scalar invariant per atom.
* The eigenvalue-magnitude profile of $\rho_\lambda(\beta_\mathfrak{H})$
 carries the multiplicity information that scalar substrate
 invariants miss.

**Rules out:**

* Any *uniform* $n_\star \in \mathbb{N}$ per atom (closed at uniform
 $k$ for at most $2/3$ of $\{D, T, {}^3\mathrm{He}\}$).
* Any rule constructed from scalar partitions of $(\ell, n_0, k, m)$
 alone (the four-tuple's $m$ is per-atom, not per-partition).
* **Any partition-shape-only selector.** The Hoefsmit content
 spread $\Delta c_{\max}(\lambda)$ test
 ([probe-hoefsmit-content-selector.witness.json](https://github.com/litlfred/qou/blob/main/computations/probe-hoefsmit-content-selector.witness.json))
 refutes content-spread argmax for all 3 atoms: empirical dominants
 $\{[2,2,1,1], [6,3], [5,4]\}$ have spreads $\{4, 6, 5\}$, while
 the partition-only argmax of spread is the single-row / single-
 column family with spread $= n - 1$.

## Writhe accounting (audit)

The braid word $\beta_\mathfrak{H}$ that enters all of #639's
per-partition compute (consumed via #638's
[`probe_phiq_operator_valued.py`](https://github.com/litlfred/qou/blob/claude/close-level-selection-rule-bvMvw/computations/probe_phiq_operator_valued.py))
encodes the writhe **implicitly** through the signed
$(c, d)$ Hecke coefficients of
[`atom_braid_word_3A(Z, N)`](https://github.com/litlfred/qou/blob/main/computations/mass_at_3A_proper.py):

| nucleon pair | $(c, d)$ | Hecke meaning | crossing sign |
|---|---|---|---|
| p–p | $(1.0,\, 0.0)$ | bare $\sigma_i$ | $+1$ (positive) |
| n–n | $(1.0,\, -h)$ | $\sigma_i^{-1} = \sigma_i - h$ | $-1$ (negative) |
| p–n / n–p | $(1.0,\, -h/2)$ | half-Hecke interpolant | sign-mixed |

The total writhe $w(\mathfrak{H})$ is determined by the
$(Z, N)$-conditional structure of `atom_braid_word_3A`. Per
CLAUDE.md §7a (Hecke–Skein convention), the framework fixes the
framing via the braid-word convention and defines
$J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$ **directly**, without an
explicit $(-q)^{3w/2}$ Kauffman correction. Consequently:

* The eigenvalue spectra $\{\mu_a^{(\lambda)}\}$ in #638's probe
 are the spectra of the **writhe-encoded** operator
 $\rho_\lambda(\beta_\mathfrak{H})$ — different writhes produce
 different spectra even at the same $\lambda$ and $q_0$.
* This is why ${}^3\mathrm{He}$'s spectrum at $[5, 4]$ differs from
 $T$'s spectrum at the same $\lambda$: $(Z, N) = (2, 1)$ vs $(1, 2)$
 gives different p–n / n–n crossing patterns and hence different
 writhes, producing different eigenvalue magnitudes (${}^{3}$He max
 $\lvert\mu\rvert \approx 10.69$ vs $T$'s $\approx 8.23$).
* The candidate SDP-active-set selector (above) reads the writhe-
 encoded SDP output and therefore inherits the writhe-dependence
 automatically — no separate writhe normalization is needed in
 the selector definition.

The half-Hecke p–n interpolant $(1.0, -h/2)$ is a framework choice
(it corresponds to a sign-mixed isospin crossing in the categorical
encoding); the SDP solver consumes this directly. This subtlety
explains why the per-partition $k_\lambda$ rule cannot be reduced
to "count positive minus negative crossings" alone — the half-
weight crossing carries a continuous, not integer, contribution
to the algebraic writhe.

## Structural reason: the selector is intrinsically $(q, \beta)$-dependent

The negative finding above is **not** a failure of imagination; it
is structurally forced. The operator-selection SDP / LP solver
that produces the per-partition operator data
([prop:operator-selection-lp](#prop:operator-selection-lp)
and the LP / SDP infrastructure of CLAUDE.md §"LP / SDP duals —
first-class infra") consumes **both** the substrate parameter
$q_0$ (CAL-2) and the **braid word** $\beta_\mathfrak{H}$ as inputs:

$$
  \text{SDP}\bigl(q_0, \beta_\mathfrak{H}\bigr)
  \;\longmapsto\;
  \bigl\{\rho_\lambda(\beta_\mathfrak{H}), \,
    \{\mu_a^{(\lambda)}\}_{a}, \,
    y_\lambda(q_0), \, y_0^\star, \ldots\bigr\}.
$$

The selector $\lambda \mapsto k_\lambda$ is a property of the
**SDP output spectrum**, not of the SDP inputs in isolation. Two
atoms with the same strand count $n = 3A$ but different braid
words $\beta_{T} \neq \beta_{{}^3\mathrm{He}}$ produce different
SDP outputs even at the same $q_0$; the partition shape
$\lambda \vdash n$ alone cannot resolve them. The empirical
max-$\lvert\mu\rvert$ selector
([probe-phiq-per-partition-klambda.witness.json](https://github.com/litlfred/qou/blob/main/computations/probe-phiq-per-partition-klambda.witness.json))
*is* the right shape — it reads the SDP-output eigenvalue spectrum
directly. The remaining structural identification problem is to
express this max-$\lvert\mu\rvert$ predicate as a **closed-form
function of $(q_0, \beta_\mathfrak{H}, \lambda)$**, not just
$\lambda$.

## Open structural question

The remaining identification problem, sharpened by the SDP-
dependence observation above:

> *Express the empirical selector "$\lambda$ has the maximum
> $\lvert\mu\rvert$ in the spectrum of $\rho_\lambda(\beta)$" as a
> **closed-form structural rule** in terms of substrate data
> $(q_0, \beta_\mathfrak{H}, \lambda)$ — without empirical
> evaluation of the eigenvalue spectrum, but explicitly
> consuming the braid word $\beta_\mathfrak{H}$, not the
> partition $\lambda$ in isolation.*

Candidate routes (all $(q, \beta)$-aware):

* **(Most promising) SDP active-set / shadow-price selector.** The
 operator-selection SDP of
 [prop:operator-selection-lp](#prop:operator-selection-lp) —
 routed through `lp_dual_solver.solve_psd_operator_selection_sdp(t, G, n_target)`
 per CLAUDE.md §"LP / SDP duals — first-class infra" — produces,
 for inputs $(q_0, \beta_\mathfrak{H})$, a primal-dual pair whose
 **dual** carries:
 - a shadow price $y_0^\star$ on the net constraint,
 - per-block shadow prices $y_\lambda^\star \geq 0$ on the
 Wedderburn Frobenius-positivity constraints,
 - an **active set** $\mathrm{Active} = \{\lambda : y_\lambda^\star > 0\}$
 of binding blocks.

 The natural candidate for the per-partition selector is:

 $$
    \mathrm{isMaxEigSpectrum}(\lambda)
    \;\stackrel{?}{=}\;
    \lambda = \mathop{\mathrm{argmax}}_{\lambda' \in \mathrm{Active}}
    \; y_{\lambda'}^\star.
  $$

 This is substrate-only (no eigenvalue evaluation), $(q_0, \beta)$-dependent
 (the SDP inputs), and **already infrastructure-supported**: the SDP
 emits the required dual fields per the LP / SDP first-class-infra
 contract (`y_star`, `active_set`, `duality_gap`). Testable directly
 against 's empirical dominants $\{[2,2,1,1], [6,3], [5,4]\}$
 by running the SDP at each atom's braid word and reading off the
 argmax of $y_\lambda^\star$.

 Predicted alignment: the dominant partition $\lambda_\mathrm{dom}$
 identified empirically by max-$\lvert\mu\rvert$ should equal
 $\mathrm{argmax}_\lambda y_\lambda^\star$ — both measure
 "where the operator's binding-energy demand concentrates," one
 via the spectrum, the other via the LP shadow price. The
 prop:mass-coefficient-shadow-price linkage between BW coefficients
 and SDP shadow prices (per the existing LP/SDP infra) supports
 the structural equivalence.

* **Hoefsmit hook-content asymptotic along a reduced braid word.**
 The maximum eigenvalue of $\rho_\lambda(\sigma_i)$ in the
 Hoefsmit seminormal form is bounded by a hook-content product
 over the Young diagram of $\lambda$. Iterating along a braid
 word's reduced expression $\beta = \sigma_{i_1}^{\varepsilon_1}
  \cdots \sigma_{i_\ell}^{\varepsilon_\ell}$ gives an a-priori
 upper bound on $\max \lvert\mu(\rho_\lambda(\beta))\rvert$ — the
 bound is $\beta$-dependent (through the index sequence
 $i_1, \ldots, i_\ell$) and $q_0$-dependent (through the
 Hoefsmit matrix entries), matching the structural shape needed.
* **Type-B-folded-crystal weight asymptotic** (the natural next
 refinement of [audit--type-b-fold-depth-n-star.md](https://github.com/litlfred/qou/blob/main/docs/audits/-type-b-fold-depth-n-star.md)).
* **Symbolic action of $\beta$ in the Kashiwara crystal.** The
 combinatorial action of the braid word on Young tableaux may
 identify the dominant partition without numerical eigenvalue
 evaluation.

Closure of this open form would constitute the structural lift
formula of [conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro) — the missing piece flagged in
that conjecture's "Status of $n_\star$" section.

## Paper-canonical $\sigma_w$ basis (cycle 7)

 cycle 6 established that the SDP shadow-price hypothesis
**cannot** be tested in the per-partition basis: by Wedderburn
orthogonality, the off-diagonal Gram entries are identically zero
([probe-off-diagonal-gram-wedderburn.witness.json](https://github.com/litlfred/qou/blob/main/computations/probe-off-diagonal-gram-wedderburn.witness.json) —
110/110 partition pairs of $H_6$ confirmed zero). The SDP-with-
diagonal-Gram reduces to the LP cost ranking, which we refuted
for $D$ and ${}^3\mathrm{He}$.

The genuine SDP refinement uses the **paper-canonical reduced
braid-word basis** $\{\sigma_w : w \text{ reduced}\}$ of $H_n(q)$
(per CLAUDE.md §7a Hecke–Skein convention). Witness:
[probe-braid-word-basis-gram.witness.json](https://github.com/litlfred/qou/blob/main/computations/probe-braid-word-basis-gram.witness.json).

### Empirical content at $H_3(q_0)$ — full $6 \times 6$ Gram

The Gram $G_{wv} = \mathrm{tr}_M(\sigma_w \cdot \sigma_v)$ in the
six-element reduced-word basis $\{e, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0\}$
at $q_0 = 1.109978595554181\ldots$ (50 dps):

| | $e$ | $\sigma_0$ | $\sigma_1$ | $\sigma_0\sigma_1$ | $\sigma_1\sigma_0$ | $\sigma_0\sigma_1\sigma_0$ |
|---|---:|---:|---:|---:|---:|---:|
| $e$ | $1.000$ | $0.499$ | $0.499$ | $0.249$ | $0.249$ | $0.551$ |
| $\sigma_0$ | $0.499$ | $1.104$ | $0.249$ | $0.551$ | $0.551$ | $0.365$ |
| $\sigma_1$ | $0.499$ | $0.249$ | $1.104$ | $0.551$ | $0.551$ | $0.365$ |
| $\sigma_0\sigma_1$ | $0.249$ | $0.551$ | $0.551$ | $0.365$ | $1.220$ | $0.628$ |
| $\sigma_1\sigma_0$ | $0.249$ | $0.551$ | $0.551$ | $1.220$ | $0.365$ | $0.628$ |
| $\sigma_0\sigma_1\sigma_0$ | $0.551$ | $0.365$ | $0.365$ | $0.628$ | $0.628$ | $1.351$ |

**Structural findings**:

1. **All 15 off-diagonal entries are non-zero.** Max magnitude
 $G_{\sigma_0\sigma_1, \sigma_1\sigma_0} = 1.220$ — actually
 *larger* than the diagonal $G_{\sigma_0\sigma_1, \sigma_0\sigma_1} = 0.365$.
 The σ-basis is overcomplete with respect to the Markov bilinear form.
2. **Symmetric** (Markov-trace cyclicity): $G_{wv} = G_{vw}$ for all
 pairs, confirmed to numerical precision.
3. **Substrate-only**: every entry is a $\mathbb{Z}[q^{\pm 1}]$ polynomial in $q$
 evaluated at $q_0$ via the Wenzl bridge

 $$
     G_{wv}(q_0) = \sum_{\lambda \vdash 3} y_\lambda(q_0) \cdot
       \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda(\sigma_w \cdot \sigma_v)\bigr),
   $$

 with $y_\lambda(q_0)$ from the canonical Jones-Markov machinery
 and $\rho_\lambda(\sigma_w \sigma_v)$ from Hoefsmit seminormal
 matrix products.

### Operator-selection LP in $\sigma_w$ basis

Running [`solve_operator_selection_lp`](https://github.com/litlfred/qou/blob/main/computations/lp_dual_solver.py)
on the $H_3$ basis with $\mathbf{t}_w = \mathrm{tr}_M(\sigma_w)$
and unit categorical target gives strong-duality with gap $5\times 10^{-17}$;
the active set picks out the identity $e$ alone (since $\mathbf{t}_e = 1$
is the unit-norm channel and the LP is unconstrained at $n_\mathrm{target} = 1$).
For atomic compute (β-decay, deuteron) the basis extends to $H_{3A}(q_0)$
and the LP/SDP active set is the **substrate-derivable**
$(q_0, \beta_\mathfrak{H})$-dependent ranking the per-partition
basis could not produce.

### Bridge to Murphy / cellular basis

The reduced $\sigma_w$ basis and the Murphy basis $\{m_{S,T}^\lambda\}$
of $H_n(q)$ (per Graham–Lehrer 1996; over $\mathbb{Z}[q^{\pm 1}]$, the
same parameter ring) are related by a triangular change-of-basis:

$$
  \sigma_w = \sum_{(\lambda, S, T)} c^{\lambda, S, T}_w \cdot m_{S, T}^\lambda,
  \qquad c^{\lambda, S, T}_w \in \mathbb{Z}[q^{\pm 1}].
$$

Pulling the σ-basis LP/SDP back through this expansion gives a
per-cell ranking at $(\lambda, T)$-resolution — strictly finer than
per-partition. The Murphy basis is:

* **Over $\mathbb{Z}[q^{\pm 1}]$** — matches the paper's parameter ring
 (Habiro / brane-tower bicompletion lives over the same ring).
* **Cellular** — block-diagonal in $\lambda$ under dominance order
 (same Wedderburn block-structure as Hoefsmit), but with genuine
 off-diagonal $(S, T)$-structure *within each block*.
* **Aligned with QOU's Gröbner–Shirshov filtration** — Murphy is
 cellular w.r.t. the dominance order on partitions, which is the
 natural partial order refining GS depth.
* **NOT directly aligned with Type-B folding / Kashiwara crystals** —
 those are functorial-categorical structures Murphy doesn't speak
 to directly.

The σ-basis $\to$ Murphy expansion is the canonical bridge to the
per-cell selector refinement. Atomic braid words
$\beta_\mathfrak{H} = \mathtt{atom\_braid\_word\_3A}(Z, N)$ are
specific σ-products; their Murphy expansion gives a substrate-
derivable, $(q_0, \beta)$-aware decomposition into per-cell weights.

### Per-cell weights for deuteron at $H_6(q_0)$

[`probe_murphy_per_cell_weights.py`](https://github.com/litlfred/qou/blob/main/computations/probe_murphy_per_cell_weights.py)
computes $w_{\lambda, S, T} = \lvert\langle v_S, \rho_\lambda(\beta_D) v_T\rangle\rvert$
for all 720 cells of $H_6(q_0)$ (= $6!$, Wedderburn dimension check
passes). Top-3 per-cell weights (y-weighted):

| rank | $\lambda$ | $(S, T)$ | $w_{\lambda,S,T}$ | $y_\lambda \cdot w$ |
|---:|---|---|---:|---:|
| 1 | $[5, 1]$ | $(0, 0)$ | $2.798$ | $0.165$ |
| 2 | $[5, 1]$ | $(3, 1)$ | $2.389$ | $0.141$ |
| 3 | $[4, 2]$ | $(4, 2)$ | $3.464$ | $0.140$ |

**Substantive negative finding.** The per-cell argmax partition is
$[5, 1]$ (and the per-partition rollup argmax is $[4, 2]$), neither
of which is the empirical max-$\lvert\mu\rvert$ dominant
$[2, 2, 1, 1]$ identified by
[`probe_phiq_per_partition_klambda.py`](https://github.com/litlfred/qou/blob/main/computations/probe_phiq_per_partition_klambda.py).

**Structural reason.** The two observables on $\rho_\lambda(\beta)$
measure different things:

| Observable | Quantity | Probe |
|---|---|---|
| Per-cell matrix entries | $\lvert\langle v_S, \rho_\lambda(\beta) v_T\rangle\rvert$ | this Murphy probe |
| Per-partition $\Phi_q$ contribution | $\lvert y_\lambda \sum_a \Phi_q^{[\leq k]}(\mu_a^{(\lambda)})\rvert$ |  cycle 5b |

The first is the bilinear-pairing observable (basis-expression
strength). The second is the spectral observable (eigenvalue
truncation-weighted dilogarithm). Both come from the same
$\rho_\lambda(\beta_D)$, but they rank partitions by different
properties of the operator.

**Implication for the open question.** The per-cell Murphy
ranking is a valid substrate-derivable selector, but it picks a
*different* dominant partition than the empirical max-$\lvert\mu\rvert$
selector that closes the brane-tower truncation gap. The
structural identification of the brane-tower-relevant selector
must privilege the **spectral** observable (eigenvalues of
$\rho_\lambda(\beta)$) over the **bilinear** observable (matrix
entries) — these are *not* equivalent rankings, despite being
extractable from the same operator data.

Surviving candidates for the spectral substrate-derivable selector:

* **Hoefsmit hook-content asymptotic along a reduced braid word**
 (the upper-bound route on $\max\lvert\mu(\rho_\lambda(\beta))\rvert$ —
 already listed above).
* **q-Casimir spectral bound**: in the centre of $H_n(q)$, the
 q-Casimir element has spectrum on $V_\lambda$ given by a
 $\lambda$-content polynomial; this bounds $\max\lvert\mu\rvert$
 for any operator built from σ-generators with explicit
 $(q, \beta)$-dependence.
* **Operator-norm via Schur-Weyl duality**: $\rho_\lambda(\beta)$ in
 $V_\lambda$ corresponds (via Schur-Weyl) to a $U_q(\mathfrak{sl}_n)$
 intertwiner whose operator norm has a closed-form expression in
 terms of the q-deformed weight diagram.

Both Murphy/cell-level structure and the σ-basis Gram remain
valuable for other questions (per-cell selectors, σ-basis SDP) —
just not directly for the per-partition brane-tower selector
$k_\lambda$.
