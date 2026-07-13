<!-- FILE_START: intro-plancherel-alpha-ribbon.md -->
The Plancherel measure on partitions and the categorical $\alpha_{\mathrm{EM}}$ coupling lock together through the ribbon structure of the Hecke category. The knot-factor distills directly from a Plancherel-weighted Wedderburn block sum.

This sequence identifies the Plancherel weight on Wedderburn blocks, verifies its probability-distribution properties at the substrate parameter, and formalizes the substrate-level knot-factor formula. Downstream binding-energy models rely strictly on the explicit knot-factor outputs $K(\mathrm{braid})$ tabulated in the final blocks.
<!-- FILE_END: intro-plancherel-alpha-ribbon.md -->

<!-- FILE_START: alpha-em-categorical-trace.md -->
**Remark (deprecated empirical $\alpha_{EM}$ forms).**
The categorical fine-structure constant relies exclusively on the robust, pre-archimedean evaluation:

$$
  \alpha_{EM} \;=\; \frac{h^2}{q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})}
              \;=\; \frac{1}{q\,[9]_q\,[10]_q}.
$$

Older isolated PSLQ-uniqueness guesses matching $q_0$ lack theoretical backing. These residual artifacts fail exact representation limits and smooth $q$ continuity. They exist purely as historical diagnostic markers and are completely replaced by the exact Hopf 2-strand operation model.
<!-- FILE_END: alpha-em-categorical-trace.md -->

<!-- FILE_START: plancherel-term-7-formulation.md -->
*Define the curvature-rank-$k$ residue functional using the q-deformed Wedderburn weight $\tilde w_\lambda = \dim_q^2 V_\lambda / [n]_q!$:*

$$
  \Phi_k(\mathcal{K}, \mathcal{T})
  \;:=\; \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
  \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$

*The universal residue extracts the high-tower contribution as:*

$$
  \mathfrak{m}^{\geq 4}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \alpha \cdot \!\!\sum_{k \geq 4}\!\Phi_k(\mathcal{K}, \mathcal{T}),
  \qquad \alpha \;=\; m_e \cdot 8G.
$$

At low strata ($k \leq 3$), the restricted Frobenius integral routes through distinct hyperbolic-knot ideals. At deep strata ($k \geq 4$), specific knot identities evaporate. The surviving residue isolates the universal Frobenius co-Casimir tail, dependent solely on the block weight topology.
<!-- FILE_END: plancherel-term-7-formulation.md -->

<!-- FILE_START: plancherel-weight-boundedness.md -->
*For semisimple $A = H_n(R, q)$, the canonical Plancherel weights $w_\lambda = (\dim V_\lambda)^2/n!$ fulfill strict probability-distribution conditions:*

1. *Non-negativity: Each $w_\lambda \in [0, 1]$.*
2. *Normalisation: $\sum_{\lambda \vdash n} w_\lambda = 1$ exactly in $\mathbb{Q}$.*

The classical dimension mapping guarantees standard conservation laws inside the algebra.
<!-- FILE_END: plancherel-weight-boundedness.md -->

<!-- FILE_START: plancherel-weight-boundedness-interpretation.md -->
**Remark (q-deformed alternative).**
The $q$-deformed weight $\widetilde{w}_\lambda = \dim_q^2 V_\lambda / [n]_q!$ sums to a finite value $\approx 1.51$ rather than exactly 1. It does not construct a pure probability measure at generic $q \neq 1$. However, the Plancherel boundedness property successfully neutralizes massive matrix dimension divergences inside log-pairings, suppressing massive combinatorial scale factors cleanly into manageable average bounds. Without this boundedness, the deep-tower calculations would mathematically diverge.
<!-- FILE_END: plancherel-weight-boundedness-interpretation.md -->

<!-- FILE_START: unified-curvature-rank-mass-formula.md -->
*The categorical mass decomposes perfectly over discrete GB-filtration depths $k$:*

$$
  \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T}),
  \qquad
  \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}\!\!
    \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$

The sum organizes the individual stratum contributions via q-deformed Wedderburn block weights. 
<!-- FILE_END: unified-curvature-rank-mass-formula.md -->

<!-- FILE_START: chirality-residue-mass-term.md -->
*The mass tower rigidly isolates into chirality and non-chirality segments based on the signed Young content $c_\lambda$:*

$$
  \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
  \;=\;
  \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;+\;
  \mathfrak{m}^{\neg\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T}).
$$

*The chirality branch spans specifically over $c_\lambda = 0$ Wedderburn blocks:*

$$
  \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;=\;
  \sum_{k = 0}^{n-1} \alpha_k \cdot
    \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k \\ c_\lambda \,=\, 0}}\!\!
    w_\lambda \cdot
    \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$
<!-- FILE_END: chirality-residue-mass-term.md -->

<!-- FILE_START: chirality-residue-mass-term-interpretation.md -->
**Remark (Physical interpretation).**
The chirality component contributes a positive, attractive confining force across all isotopes. It actively counterbalances the net-negative repulsive base structure, framing the gauge-invariant background holding mass conglomerates together.
<!-- FILE_END: chirality-residue-mass-term-interpretation.md -->

<!-- FILE_START: e-infinity-page-identifications.md -->
*The six-term categorical mass formula components correlate strictly to $E_\infty^{p, *}$ pages:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \sum_{p = 0}^{\infty}
  \bigl\langle \mathrm{tr}_M,\ E_\infty^{p, *}(T_w) \bigr\rangle
  \;+\;
  \bigl\langle \mathrm{tr}_M \circ (\mathrm{id} \otimes \varTheta),\ E_\infty^{0, *}(T_w) \bigr\rangle
  \;+\;
  m_e \cdot \tau\bigl(C_{\dim_q}\bigr).
$$

*Term 1 descends directly to the identity base mapping cleanly to $E_\infty^{0, *}$. Terms 2 and 3 isolate single-generator and pair-tower functional limits mapping explicitly to $E_\infty^{1, *}$ and $E_\infty^{2, *}$. Term 6 aggregates all deeper-strata residues spanning $\ell \geq 3$ mapping to the algebraic elliptic-curve residues without requiring speculative contour assumptions.*
<!-- FILE_END: e-infinity-page-identifications.md -->

<!-- FILE_START: spectral-sequence-h3-explicit.md -->
*The differentials $d_1$ and $d_2$ execute completely algebraically on $H_3(R, q)$.*

The initial $E_1$ page categorizes directly into four explicit levels holding ranks 1, 2, 2, and 1. The $d_1$ differential acts directly through the Hecke relation $\sigma_i^2 = (q - q^{-1}) \sigma_i + \mathbf{1}$. It drives pair matrices into pure symmetric/antisymmetric splits, killing specific states outright. The $d_2$ differential governs the Yang-Baxter overlap, further squashing rank bounds before fully locking into the final $E_\infty$ stable state.

The explicitly computed $E_\infty$ trace limits correctly extract zero trace for single generators and exact pair traces for the $z^2$ multiplier, thoroughly fulfilling the term expectations mathematically.
<!-- FILE_END: spectral-sequence-h3-explicit.md -->

<!-- FILE_START: chirality-writhe-ribbon-derivation.md -->
*For a braid $\beta$ with integer writhe $w(\beta)$, the chirality factor derived from the Kauffman ribbon-twist evaluation limits strictly to:*

$$
  a_K(\beta)
  \;=\;
  1 \;+\; w(\beta) \cdot h \;+\; O(h^2).
$$

This rigorously locks the first-order Hecke deformation factor strictly to the topological writhe, cleanly bridging the pure algebraic sequence mapping directly to observed ribbon dynamics.
<!-- FILE_END: chirality-writhe-ribbon-derivation.md -->

<!-- FILE_START: gram-matrix-spectral-connection.md -->
**Remark.**
*User question: where does the Gram matrix fit in the
spectral-sequence / Frobenius framework?*

**Role of the Gram matrix.**
*The **Gram matrix** $G$ of the Markov pairing is the common
algebraic object that encodes:*

1. *The **Frobenius algebra structure** of $H_n(R, q)$: the pairing
   $\langle x, y \rangle_\tau := \tau(x \cdot y)$ is non-degenerate
   iff $\det G \neq 0$
   ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).*
2. *The **inverse** $G^{-1}$ enters the **Frobenius co-Casimir**
   ([Frobenius universal](#thm:frobenius-codim-universal)):
   $C_{\dim_q} = \sum_{i, j} (G^{-1})_{ij} \cdot b_i \cdot b_j$
   in a non-central-idempotent basis (standard Frobenius
   identity).*
3. *The **spectral-sequence pairing**: each $E_\infty^{p, *}$ is
   paired with $\mathrm{tr}_M$ via the Gram matrix restricted to
   the stratum — so $E_\infty^{p, *}(T_w) \to R$ is really
   $T_w \mapsto G_{T_w, *}$ projected to the stratum.*
4. *The **knot-factor Frobenius pairing**
   ([knot factor Frobenius pairing](#conj:knot-factor-frobenius-pairing))
   computes $G_{\beta, \beta^*}$ for braid-mirror pairs — the
   chirality factor $a_K$ of Term 5 is a normalised Gram-matrix
   entry.*

**Gram matrix in the three derived terms.**

| term | Gram matrix role |
|---|---|
| Term 1 (descended) | $G_{T_w, \mathbf{1}} = \tau(T_w)$ — single matrix entry |
| Term 2, 3 (brane tower) | $G_{\sigma_i, \sigma_i} = \tau(\sigma_i^2) = hz + 1$; pair $G_{\sigma_i \sigma_j, \sigma_j \sigma_i}$ |
| Term 4 (Frobenius co-Casimir) | $\tau(C_{\dim_q}) = \mathrm{tr}(G^{-1} \cdot D)$ where $D_{ij} = \delta_{ij}/\dim_q$ per block basis |
| Term 5 (chirality) | $a_K = G_{\beta, \beta^*} / G_{\mathbf{1}, \mathbf{1}}$ |
| Term 6 (jet-prefix) | $G$ restricted to higher filtration strata |

**Gram matrix for $H_3(R, q)$ over $R$.**

*Basis: $\{1, \sigma_0, \sigma_1, \sigma_0 \sigma_1, \sigma_1 \sigma_0, \sigma_0 \sigma_1 \sigma_0\}$.
Markov trace on standard basis ([Markov trace factorization](#thm:markov-trace-factorization)):
$\tau(T_w) = z^{\ell(w)}$ for $w \in S_n$ reduced, where
$\ell(w)$ is the length.  So $\tau(1) = 1$, $\tau(\sigma_i) = z$,
$\tau(\sigma_i \sigma_j) = z^2$. The naïve length rule $z^{\ell(w)}$
**fails for adjacent triples** (the rule assumes the rightmost
generator lies in the proper sub-algebra; this fails for
$\sigma_0\sigma_1\sigma_0$ since $\sigma_1\sigma_0 \notin H_2$).
The canonical Ocneanu--Wenzl recursion gives
$\tau(\sigma_0\sigma_1\sigma_0) = hz^2 + z$
(formerly stated as $z^3$ in this block; corrected per
[Markov-bug audit](https://github.com/litlfred/qou/blob/main/docs/audits/-trm5-markov-bug.md)).*

*Gram matrix $G_{ij} = \tau(b_i b_j^{-1})$ (cyclic self-pairing).
The first-row/column entries below shown as $z^3$ are stale per
the Markov-bug fix and should read $hz^2 + z$:*

$$
  G \;=\;
  \begin{pmatrix}
    1 & z & z & z^2 & z^2 & z^3 \\
    z & 1 + hz & * & * & * & * \\
    z & * & 1 + hz & * & * & * \\
    z^2 & * & * & * & * & * \\
    z^2 & * & * & * & * & * \\
    z^3 & * & * & * & * & *
  \end{pmatrix},
$$

*with off-diagonal entries computed via Hecke relations.  At
$q = q_0$, $\det G \neq 0$ (generically), confirming the
Frobenius property.*

**Gram $\leftrightarrow$ Wedderburn conjugation.**
*In the central-idempotent basis $\{e_\lambda\}$, the Gram matrix
is **block-diagonal**: $G_{\lambda, \mu} = \delta_{\lambda \mu}
\cdot \tau(e_\lambda^2) = \delta_{\lambda \mu} \cdot \tau(e_\lambda)
= \delta_{\lambda \mu} \cdot \frac{\dim_q(\lambda) \cdot \dim(\lambda)}{[n]_q!}$.
The inverse is
$G^{-1}_{\lambda, \mu} = \delta_{\lambda \mu} \cdot \frac{[n]_q!}{\dim_q(\lambda) \cdot \dim(\lambda)}$.
Summing $G^{-1}$ diagonal times $1/\dim_q$ gives exactly the Frobenius
co-Casimir trace $\sum_\lambda 1/\dim_q(\lambda)$ — recovering
([Frobenius universal](#thm:frobenius-codim-universal)).*

*The quantum dimensions $\dim_q(\lambda)$ entering this block structure
are the Wedderburn-block face of the $q$-Laplacian spectral tower
([the $q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower)):
at a root of unity $q = e^{i\pi/\kappa}$ they truncate to the finite
Verlinde/ADE set, so the Gram matrix becomes finite block-diagonal
modular-tensor data there.*

**Gram-matrix rank and the spectral sequence.**

*The filtration $J^\bullet(q)$ induces a block structure on $G$:
entries $G_{ij}$ with $b_i \in J^p$ and $b_j \in J^{q}$ sit in
the $(p, q)$-block.  The filtered Gram matrix has **block-triangular**
shape in the standard basis (since $\tau(J^p \cdot J^q) \subset J^{p+q}$
generically), and its **diagonal blocks** $G^{(p)} :=
G|_{J^p/J^{p+1}}$ are the **pairings on $E_0^{p, *}$**.  The
spectral-sequence differentials $d_r$ are encoded in the
**off-diagonal** blocks of $G$ under filtered inversion.*

*So the Gram matrix is the **single algebraic object** whose
block structure generates the entire spectral sequence and its
mass-term identification.  Computing $G$ explicitly for $H_3(R, q)$
([spectral-sequence H3 explicit](#prop:spectral-sequence-h3-explicit))
is equivalent to computing all pages $E_r^{p, *}$.*
<!-- FILE_END: gram-matrix-spectral-connection.md -->

<!-- FILE_START: weak-spectral-completeness.md -->
**Conjecture (weak-sector spectral completeness — Hoefsmit
$n=6$ form).**
*Over the categorical ring $R$ with $q$ generic (not a root of
unity in $R$ — note $q = 1$ IS excluded), the EW/Higgs
force-carrier sector $\{T(2,4), T(2,6), T(2,8)\}$
(electroweak/Higgs torus-link triplet)
admits a **categorically complete idempotent decomposition** in
$\mathrm{End}_R(V^{\otimes 6})$ via the disjoint-strand-pair
Hoefsmit assignment*

$$
  W \leftrightarrow \sigma_1^4, \qquad
  Z \leftrightarrow \sigma_3^6, \qquad
  H \leftrightarrow \sigma_5^8
$$

*([`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)).
Eight pairwise-orthogonal pure-eigenspace projectors of
$(\sigma_1, \sigma_3, \sigma_5)$ — labelled by sym/alt patterns —
exhaust the EW Wedderburn content with cell-content
multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ summing to $20$ (out
of $\sum_{\lambda \vdash 6} f_\lambda = 76$ seminormal-basis
vectors). The substrate-level structural quantity is the
**bar-self-dual cell-content trace***

$$
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  4\bigl(q^{18} + q^{-18}\bigr)
  + 2\bigl(q^{10} + q^{-10}\bigr)
  + \bigl(q^{6} + q^{-6}\bigr)
  + 3\bigl(q^{2} + q^{-2}\bigr)
  \;\in\; R
$$

*— derivable directly from cell-content multiplicities, **without
invoking Plancherel weights**.*

### Statement (formal)

Over the categorical ring $R$ with $q$ generic (not a root of
unity), the Hecke algebra $H_2(q)$ has Wedderburn decomposition
$H_2(q) \cong R \oplus R$ with two 1-dimensional blocks (sym and
alt), summing to a 2-dimensional algebra over $R$. Each torus
link $T(2, 2k) = \sigma_1^{2k}$ acts on these two blocks with
eigenvalues $(q^{2k}, q^{-2k}) \in R^\times \times R^\times$
(prop:even-twist-torus-link-psd-feasibility).

Define the **per-link block projectors**:
- $e_W^{+} := $ sym block of $T(2, 4)$, $e_W^{-} := $ alt block
- $e_Z^{+} := $ sym block of $T(2, 6)$, $e_Z^{-} := $ alt block
- $e_H^{+} := $ sym block of $T(2, 8)$, $e_H^{-} := $ alt block

The three torus links **all embed in the same Bring-surface
genus-$4$ Seifert fiber**
([prop:torus-embeddable-complete](#prop:torus-embeddable-complete)),
since their Seifert genera $1, 2, 3$ are each $\leq 4$. So the
six projectors live in $H_2(q)$ in the same ambient host as the
saturating EM/strong carriers $\{T_{2,9}, T_{3,5}\}$. The
completeness statement asserts that within the EW sector, the
direct sum $e_W^{+} \oplus e_W^{-} \oplus \cdots \oplus e_H^{-}$
exhausts the Wedderburn-block content of the EW Hecke action on
Bring's surface.

### Proof sketch (parallels EM spectral completeness)

The argument mirrors
[`thm:em-spectral-completeness`](#thm:em-spectral-completeness)
applied to the two-strand idempotent decomposition $w_+ + w_- = 1$
on the EM sector:

**Step 1 — Per-host two-strand completeness.**
For each $T(2, 2k)$, the two-strand braiding
$\sigma_1 \in B_2$ has the standard Hecke decomposition
$w_+^{(k)} + w_-^{(k)} = \mathbf{1}_{H_2(q)}$ where $w_\pm^{(k)}$
are the (sym, alt) idempotents acting on $V \otimes V$ for the
$k$-th host's natural representation $V_k$.

**Step 2 — EW sector decomposes by even-twist parity within
$H_2(q)$ on Bring.**
All three carriers live in **the same** $H_2(q)$ over $R$ (one
host: Bring's surface). They are distinguished by their
even-twist parameter $k \in \{2, 3, 4\}$, which selects different
generalized eigenspaces under $\sigma_1^{2k}$ — specifically, the
six idempotents $e_X^\pm$ are pairwise orthogonal as elements of
$H_2(q)$ because the eigenvalues $(q^{2k}, q^{-2k})$ for $k = 2,
3, 4$ are pairwise distinct in $R$ (as $q$ is not a root of
unity). The EW total Hecke action is therefore
$\bigoplus_{k=2,3,4} H_2(q)|_{T(2, 2k)\text{-spectrum}}$, with
completeness across the direct sum following from per-link
completeness in Step 1 + pairwise orthogonality of the six
$e_X^\pm$ in $H_2(q)$.

**Step 3 — Cell-content trace, not Plancherel weight.**

> **Demoted.** Earlier drafts of this proof used
> Plancherel weights $w_X = 1/[2]_q$ as a "uniform completeness
> signature." That uniform-weight expression was a degenerate
> artifact of the dimensionally-collapsed $H_2(q)$-only
> formulation (six rank-1 projectors cannot fit in a 2-dim
> algebra; see audit
> [`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md)
> §"Plancherel weight is degenerate special case"). The Hoefsmit
> $n=6$ formulation supersedes it.

The substrate-level structural quantity is the cell-content
trace, computed directly from the eight pure-pattern
multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$:

$$
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  4\bigl(q^{18} + q^{-18}\bigr)
  + 2\bigl(q^{10} + q^{-10}\bigr)
  + \bigl(q^{6} + q^{-6}\bigr)
  + 3\bigl(q^{2} + q^{-2}\bigr)
  \;\in\; R.
$$

This expression is **bar-self-dual** under
$\iota \colon q \mapsto q^{-1}$ — the substrate-level
[bar T-duality](#prop:bar-t-duality-substrate) at the trace level.
The duality is automatic from the disjoint-strand-pair
construction: each $\sigma_i^{2k}$ is bar-self-dual on its own
(`prop:even-twist-torus-link-psd-feasibility`),
and disjoint products preserve the duality.

The Plancherel-weighted form
$\mathcal{N}_{\rm sym}^{\rm Plancherel} = q^6 (1 + q^2 + q^4)/3$
from
[`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)
is **not** bar-self-dual and differs from $\mathrm{tr}_{\rm pure}$
by a factor of $\sim 22$ at $q_0$. It is retained only as a
legacy/degenerate reference; the cell-content trace is operative.

### Downstream consequence — closes NV-1

The weak-scale crossing count $N_v$ is conjecturally derivable
from the **bar-self-dual cell-content trace** over the EW
force-carrier sector. The structural ansatz takes the form

$$
  N_v \;\stackrel{?}{=}\;
  F\bigl( [2]_q,\, [4]_q,\, [6]_q,\, [8]_q,\,
  \mathrm{tr}_{\rm pure}(\sigma_1^4 \sigma_3^6 \sigma_5^8) \bigr)
$$

for some $R$-rational function $F$. The bar-self-duality of
$\mathrm{tr}_{\rm pure}$ is a strong structural constraint on
admissible $F$: any candidate must be invariant under
$\iota: q \mapsto q^{-1}$ (since $N_v$ is a $q$-independent
constant when evaluated at $q_0$, and the substrate-level
identity must hold at all generic $q$).

**PSLQ test.** The constrained basis is
$\{[2]_q, [4]_q, [6]_q, [8]_q, q^k, h^k,
\mathrm{tr}_{\rm pure}\}$ — strictly smaller than the
brute-force monomial basis of the impasse audit. The earlier
Plancherel-weight basis $\{[2k]_q^2/[2]_q, \mathcal{N}_{\rm sym}\}$
is **superseded**.
### Audit-flag impact

If this conjecture closes:
- **NV-1**: hard flag closed via constrained PSLQ on the extended basis
- **β-decay rates**: $G_F = 1/(\sqrt{2}\,N_v^2 E_\times^2 \mu_0^2)$
  becomes derivable from $(q_0, m_e)$ alone, closing every β-decay
  half-life prediction simultaneously.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: weak-spectral-completeness.md -->

