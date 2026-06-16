# Path-α refinement: T(2,2k) embed on Bring + LP-selected knot operators

**Date:** 2026-05-05
**Branch:** `claude/w3-followup-term6-integration`
**Companion to:**
[`2026-05-05-nv-categorical-impasse.md`](2026-05-05-nv-categorical-impasse.md),
[`electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/descartes-universe/electroweak-higgs-torus-link-triplet.md),
[`weak-spectral-completeness.md`](../../content/quantum-observable-universe/braids-and-knots/weak-spectral-completeness.md).

## 1. Architecture correction — EW carriers embed on Bring

The existing
[`conj:electroweak-higgs-torus-link-triplet`](../../content/quantum-observable-universe/descartes-universe/electroweak-higgs-torus-link-triplet.md)
treats $T(2,4), T(2,6), T(2,8)$ as the **non-Bring complement** —
living on three separate host surfaces of genus 1, 2, 3. This
framing is **structurally redundant**: by the Diophantine bound
$g(T_{m,n}) \leq g(\text{host})$ used in
[`prop:torus-embeddable-complete`](../../content/quantum-observable-universe/descartes-universe/torus-embeddable-complete.md),

$$
  g(T(2, 2k)) \;=\; k - 1 \;\leq\; 4 \quad\text{for}\quad k \in \{1, 2, 3, 4\},
$$

so **every $T(2, 2k)$ with $k \leq 4$ embeds in the genus-$4$
Seifert fiber of Bring's surface** alongside the saturating
EM/strong carriers $\{T_{2,9}, T_{3,5}\}$. There is no need to
posit three additional host surfaces.

| link | $(2, 2k)$ | Seifert genus $k-1$ | embeds on Bring? | role |
|------|----------:|--------------------:|:----------------:|------|
| $T(2,2)$ | $(2,2)$ | 0 | ✓ | Hopf link (binding) |
| $T(2,4)$ | $(2,4)$ | 1 | ✓ | $W^\pm$ candidate |
| $T(2,6)$ | $(2,6)$ | 2 | ✓ | $Z$ candidate |
| $T(2,8)$ | $(2,8)$ | 3 | ✓ | $H$ candidate |
| $T(2,9)$ | $(2,9)$ | 4 | ✓ | strong/EM (saturating) |
| $T(3,5)$ | $(3,5)$ | 4 | ✓ | EM (saturating) |

The whole EM + EW carrier set lives in **one host** — Bring's
surface — making the "knot-vs-link dichotomy" a categorical
distinction (matter = knots, force = links), not a host-surface
distinction.

This **discharges U2** in the existing conjecture's uniqueness
analysis: U2 ("force-carriers are 2-component links, not knots")
becomes a categorical premise about object types in $\mathbf{C}$,
not a separate surface assumption.

## 2. q-precision contract (STRICT) — categorical ring $R$

The QOU framework works over a **categorical coefficient ring
$R$** (typically $\mathbb{Z}[q, q^{-1}]$ or its localization
$R = \mathbb{Q}(q)$ — see
[Hecke-Skein convention §7a](https://github.com/litlfred/qou/blob/main/CLAUDE.md)),
**not** the real numbers. The eigenvalue analysis in
[`prop:even-twist-torus-link-psd-feasibility`](../../content/quantum-observable-universe/descartes-universe/electroweak-higgs-torus-link-triplet.md)
states $\sigma_1^{2k}$ has block eigenvalues $(q^{2k}, q^{-2k})$.
The precision contract is on $q$ as an element of $R$:

| Locus of $q$ in $R$ | Status of statement |
|---------------------|--------------------|
| $q = 1$ (classical) | $H_n(1) = \mathbb{Q}[S_n]$; eigenvalues collapse to $(1, 1)$. **Excluded** — $q=1$ is a (trivial) root of unity. |
| $q$ a primitive $\ell$-th root of unity in $R$, $\ell \leq n$ | $H_n(q)$ is **not semisimple**; Wedderburn fails; PSD claim breaks. **Excluded.** |
| $q$ generic in $R$ (not a root of unity) | $H_n(q)$ is semisimple over $R$; eigenvalues $q^{2k}, q^{-2k} \in R^\times$. Identities hold formally over $R$. **Domain of validity for algebraic claims.** |
| Specialization $R \to F$ for $F$ a real-closed field, $q \mapsto q^* \in F$ with $q^* > 1$ | Eigenvalues become positive elements of $F$. **Domain of PSD/positivity claims.** |

**Explicit contract** for the refined blocks: algebraic identities
(eigenvalue expressions, Wedderburn projectors, Plancherel
weights) are stated **over generic $q \in R$, not a root of
unity**. Positivity / PSD claims (e.g. "both eigenvalues
positive") require an *additional* assumption — a specialization
to a real-closed field $F$ with $q \mapsto q^* > 1$ in $F$. The
numerical evaluation $q \mapsto q_0 = :val[q_0]{precision=6}\ldots$ is one
such specialization (with $F = \mathbb{R}$); $q_0$ should appear
**only** in numerical-evaluation remarks, never in the
proposition body.

This is a **direct correction** to the current
[`weak-spectral-completeness.md`](../../content/quantum-observable-universe/braids-and-knots/weak-spectral-completeness.md)
and
[`electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/descartes-universe/electroweak-higgs-torus-link-triplet.md)
blocks, both of which state eigenvalue expressions over an
unspecified $q$-domain and silently use $q_0$-specific values.
The
[Hecke-Skein convention §7a](https://github.com/litlfred/qou/blob/main/CLAUDE.md)
is generic in $q \in R$; per-block statements must inherit this
generality.

## 3. LP/SDP selection of operators per confinement

The existing infra ([CLAUDE.md §LP/SDP duals — first-class infra](https://github.com/litlfred/qou/blob/main/CLAUDE.md))
mandates that every operator-selection compute emit primal +
dual variables. The Gram-inverse basis on $H_3(q)$ supplies the
**dual basis** for knot operators:

$$
  G_{ij} \;=\; \tau(b_i \cdot b_j),
  \qquad
  G^{-1} \;\text{is the Frobenius dual.}
$$

In the NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$
(see
[`gram-matrix-spectral-connection.md`](../../content/quantum-observable-universe/braids-and-knots/gram-matrix-spectral-connection.md)),
the witness data already records:

| witness file | content |
|--------------|---------|
| [`gram-matrix-dual.witness.json`](../../computations/gram-matrix-dual.witness.json) | Full $G^{-1}$ at $q_0$, plus dual coordinates of $\{e^+, d, \gamma, e^-\}$ |
| [`knot-operator-table.witness.json`](../../computations/knot-operator-table.witness.json) | NF decomposition $b_i \cdot \beta(T_{m,n}) \cdot b_j$ for $T_{m,n} \in \{T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}\}$ |
| [`confinement-operator-selection.witness.json`](../../computations/confinement-operator-selection.witness.json) | Per-particle (proton, neutron) candidate operator NF + crossing energy + demand profile |

The observed **channel-supply fingerprint** (count of NF basis
pairs producing each output channel) shows monotone opening as
crossing count increases:

| operator | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
|----------|---------:|-----------:|-----------:|------:|------:|------:|
| $T_{1,0}$ (id) | 6/36 | 9/36 | 9/36 | 13/36 | 13/36 | 19/36 |
| $T_{2,1}$ ($\sigma_0$) | 9/36 | 13/36 | 13/36 | 18/36 | 18/36 | 24/36 |
| $T_{2,2}$ ($\sigma_0^2$) | 12/36 | 16/36 | 16/36 | 20/36 | 20/36 | 24/36 |
| $T_{2,3}$ (trefoil) | 19/36 | 24/36 | 24/36 | 32/36 | 32/36 | **36/36** |
| $T_{2,5}$ | 32/36 | 32/36 | **36/36** | **36/36** | **36/36** | **36/36** |

$T_{2,3}$ is the unique low-crossing operator unconditionally
opening the electron channel; $T_{2,5}$ saturates 5/6 channels.
This is the **LP feasibility certificate** — the demand vector
of each particle is dominated by exactly one operator's supply.

**Action item for the EW carriers:** extend the witness to
include $T(2,4), T(2,6), T(2,8)$ in $H_2(q)$ (rather than $H_3(q)$)
and compute their channel-supply fingerprint on the **2-strand
NF basis** $\{\gamma_2, \sigma_0\}$ where $\sigma_0^2 = h\sigma_0
+ \gamma_2$ from the Hecke relation. The eigenvalues
$(q^{2k}, q^{-2k})$ correspond to the (sym, alt) projectors. The
LP/SDP solve then selects which Gram-inverse element each EW
carrier saturates — providing the categorical identification
$W^\pm \leftrightarrow$ specific $G^{-1}$-basis element, etc.

## 4. Refined `conj:weak-spectral-completeness` statement

Replace the current "three different copies of $H_2(q)$, one per
host" with a **single $H_2(q)$ on Bring** decomposed into three
$\hat\tau$-equivariant sub-Wedderburn-blocks indexed by even-twist
$k = 2, 3, 4$:

$$
  H_2(q) \;\Big|_{\text{Bring, even-twist}}
  \;\cong\;
  \bigoplus_{k = 2, 3, 4}
    \bigl( e_+^{(k)} \,H_2(q)\, e_+^{(k)}
         \;\oplus\;
           e_-^{(k)} \,H_2(q)\, e_-^{(k)} \bigr)
$$

with $e_\pm^{(k)}$ the (sym, alt) projectors of $\sigma_1^{2k}$.
Completeness is the assertion that these six projectors exhaust
the EW Wedderburn-block content on Bring.

The Plancherel weights become:

$$
  w_X^{(k, \pm)}
  \;=\;
  \frac{(\dim_q \mathrm{im}\,e_X^{(k, \pm)})^2}{[2]_q!}
  \;=\;
  \frac{1}{[2]_q}
$$

(uniform across all six EW projectors for $q$ generic, not a root
of unity, $q > 1$). The host-distinctness premise is **dropped**;
even-twist parity becomes the unique structural selector.

## 5. Why this matters for $N_v$

Per the parallel pipeline in
[`electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/descartes-universe/electroweak-higgs-torus-link-triplet.md),
the EW closed form parallels the EM derivation:

| EM analog | EW analog |
|-----------|-----------|
| Strand count: 10 ($\Lambda^2 V^{10}$) | Strand count: **2** (each $T(2, 2k)$ in $B_2$) |
| Carriers: $\{T_{2,9}, T_{3,5}\}$ on Bring | Carriers: **$\{T(2,4), T(2,6), T(2,8)\}$ on Bring** (not separate hosts) |
| Categorical complexity: $[9]_q \cdot [10]_q$ | Categorical complexity: $[4]_q \cdot [6]_q \cdot [8]_q$ |
| Plancherel: $\delta_{CS} = \hbar_q^4 [5]_q$ | Plancherel: uniform $1/[2]_q$ across six projectors |
| Closed form: $1/\alpha = 45 [3]_q (1 + \delta_{CS} + 8q\delta_{CS}^2)$ | Closed form ansatz: $N_v = \prod_k [2k]_q^2 / [2]_q \cdot \mathcal{N}_{\rm sym}(q)$ |

The PSLQ basis for $N_v$ is now **strictly determined**: search
over $\{[4]_q, [6]_q, [8]_q, q^k, h^k, \mathcal{N}_{\rm sym}(q)\}$
where $\mathcal{N}_{\rm sym}(q)$ is the symmetric-channel
normalization (analog of the Plancherel ratio) yet to be
authored. This is a **structurally constrained** basis, unlike
the brute-force 7.5×10⁵-element basis of the impasse audit.

## 6. Prioritization plan (path-α only)

Six action items in **dependency order** with parallelizable phases:

### Phase A — Independent block refinements (start now)

1. **Refine `conj:electroweak-higgs-torus-link-triplet`** — replace
   "non-Bring even-twist" with "Bring-internal even-twist
   complement"; cite `prop:torus-embeddable-complete`; lift
   eigenvalue claims to generic $q \in R$, not a root of unity.
2. **Refine `conj:weak-spectral-completeness`** — drop
   host-distinctness assertion; state Wedderburn decomposition
   over generic $q \in R$, not a root of unity; specialize to a
   real-closed field for the Plancherel-weight positivity remark.

### Phase B — Witness extension (parallel to A)

4. **Extend `knot-operator-table` witness** — add $T(2,4),
   T(2,6), T(2,8)$ in $H_2(q)$ to the existing $H_3(q)$ table.
   Compute symbolically over $R = \mathbb{Z}[q, q^{-1}]$;
   evaluate at $q_0$ for numerical witness only.

### Phase C — New content blocks (gated on A + B)

3. **Author `prop:knot-operator-LP-selection`** — formal
   LP/SDP-duality statement that the Gram-inverse basis $G^{-1}$
   selects one knot operator per confinement, with the
   active-set (LP dual support) identifying the bound-state's
   saturated demand channels. Inputs: refined blocks (1, 2) +
   extended witness (4).
5. **Author `prop:weak-symmetric-normalization`** — define
   $\mathcal{N}_{\rm sym}(q) \in R$ structurally as the
   symmetric-channel Plancherel weight in the EW Wedderburn
   decomposition. Analog of
   `prop:gram-determinant-plancherel-ratio` for the EM sector.

### Phase D — Verification (gated on C)

6. **Run constrained PSLQ** for $N_v$ on the structurally
   constrained basis
   $\{[4]_q, [6]_q, [8]_q, [2]_q, q^k, h^k, \mathcal{N}_{\rm sym}\}$
   at 1000-dps with tolerance capped at CODATA $G_F$
   ($5\times 10^{-7}$). Treat as **uniqueness witness**, not
   discovery.

### Cross-branch coordination

| Branch | Overlap | Coordination message |
|--------|---------|---------------------|
| `claude/categorical-mass-divergence-audit` (PR #534) | dimensional anchor (Piece 1) ↔ $N_v$ derivation | Notify on this audit; their `prop:rho-k-graded-expansion` may inherit $\mathcal{N}_{\rm sym}$ structure |
| `claude/hoefsmit-2x2-fix` (PR #546) | per-partition $\chi^\lambda$ symbolic | Notify of R-precision contract; their symbolic engine should emit $R$-elements (not floats) for use in (3) and (5) |
| `copilot/identify-multiplicative-chain` (AXKIA, merged) | $\alpha_{\rm EM}$ closed form template | Already merged; (5) and (6) parallel the AXKIA pipeline |

## 7. Files

- This audit:
  [`docs/audits/2026-05-05-path-alpha-bring-refinement.md`](2026-05-05-path-alpha-bring-refinement.md)
- N_v impasse audit:
  [`docs/audits/2026-05-05-nv-categorical-impasse.md`](2026-05-05-nv-categorical-impasse.md)
- Existing block (to refine):
  [`content/quantum-observable-universe/descartes-universe/electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/descartes-universe/electroweak-higgs-torus-link-triplet.md)
- Existing block (to refine):
  [`content/quantum-observable-universe/braids-and-knots/weak-spectral-completeness.md`](../../content/quantum-observable-universe/braids-and-knots/weak-spectral-completeness.md)
- Witness inputs:
  [`gram-matrix-dual.witness.json`](../../computations/gram-matrix-dual.witness.json),
  [`knot-operator-table.witness.json`](../../computations/knot-operator-table.witness.json),
  [`confinement-operator-selection.witness.json`](../../computations/confinement-operator-selection.witness.json)
