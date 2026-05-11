**Proposition (placement of paper's existing knot-indexed
convolutions in the bi-filtration grid).**

*Each existing "non-tensor product" operation in the QOU paper —
where two morphisms are combined via a knot/braid/partition-shaped
twist rather than a plain tensor product — sits at a specific
$(n, K)$ stratum of the bi-filtration $\mathcal{H}_q^{(n, K)}$
([`def:hq-bi-filtration`](#def:hq-bi-filtration)).*

### The grid

| Operation | Block | $n$ (depth) | $K$ (knot/braid index) | Output type |
|---|---|---|---|---|
| Markov trace $\mathrm{tr}_M$ | [`thm:jones-markov-trace`](#thm:jones-markov-trace) | 0 | trivial (closed braid) | Laurent in $q$ — algebraic $\mathcal{P}_0$ |
| Hoefsmit pairing $\langle \cdot, \chi_\lambda \rangle$ | [`prop:hoefsmit-seminormal-form`](#prop:hoefsmit-seminormal-form) | 0 | partition $\lambda$ | $y_\lambda(q) \in \mathbb{Z}[q^{\pm 1}]$ |
| EW interface knot $\Delta_I$ | `def:ew-interface-knot` (orphan block — not yet in any chapter section) | 0 | EW braid in $B_6$ with interface $I$ | element of $H_6(q)$ |
| Higgs-vev mechanism $\mathrm{Lk}_R^{(1)}$ | `conj:categorical-higgs-mechanism` (orphan block) Step C | 0 | linking $k = 1$ | $\mathrm{End}_R(A)$ |
| Categorical linking $\mathrm{Lk}_R^{(k)}$ | `conj:categorical-linking-operation` (orphan block) | 0 | linking integer $k$ | $\mathrm{End}_R(A)$ |
| $q$-shuffle convolution $*_q$ | [`def:frobenius-hopf-substrate`](#def:frobenius-hopf-substrate) | preserves $n$ | preserves $K$ (or merges) | $\mathcal{H}_q^{(n_1 + n_2, K \cdot K')}$ |
| Volume functor $\mathrm{Vol}$ | [`prop:vol-through-tau`](#prop:vol-through-tau) | **2** | hyperbolic knot | $\mathcal{P}_2 / \mathcal{P}_1$ (real) |
| Chern–Simons $\mathrm{CS}$ | (open in paper) | **3** | hyperbolic knot | $\mathcal{P}_3 / \mathcal{P}_2$ (Tate-twisted) |
| Trilog at $\zeta_5$ orbit | [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness) | **3** | $S_5$-Bring orbit | weight-3 cyclotomic period |

### Two structural observations

#### Observation 1: most "knot-indexed" operations sit at $n = 0$

The paper's *operational* knot-indexed convolutions ($\mathrm{Lk}_R^{(k)}$,
$\Delta_I$, Hoefsmit pairing, Markov trace) live at depth $n = 0$
on the algebraic side — they manipulate Hecke elements without
introducing polylogarithms. Their *archimedean image* sits at
higher depth depending on what is paired with: Markov trace + braid
of a hyperbolic knot lands at depth 2 (volume); CS lands at depth 3.

This is not accidental: the bi-filtration encodes a clear separation
between **input shape** (the knot index $K$, depth-$0$ on the
algebraic side) and **output transcendence depth** (achieved only
after applying $\tau_{\mathrm{arch}}$, which involves the depth-$n$
grouplike $\mathrm{Li}_n^q$).

#### Observation 2: the $\Delta_I$ "non-tensor product" pattern is a depth-0 knot index

The original confusion in the first answer of this session — was
$\Delta_I$ a Mikusiński-style convolution? — reduces to: **$\Delta_I$
is a depth-0, knot-indexed Hecke element**. In the bi-filtration
language:

$$
  \Delta_I \;\in\; \mathcal{H}_q^{(0, \,\text{EW interface braid})}.
$$

The "convolution" structure the user identified is the bi-filtration
itself: convolution by $\Delta_I$ shifts the knot-index axis (via
left/right multiplication in $H_6(q)$) without changing the depth
axis. This is a *structural translation*, not a polylogarithmic
operation.

### Closure properties of the grid

| Closure | Holds | Notes |
|---|---|---|
| Sum of $(n, K)$-elements: $\mathcal{H}_q^{(n, K)} + \mathcal{H}_q^{(n, K')}$ | yes (linearity) | not in $\mathcal{H}_q^{(n, K)}$ unless $K = K'$ |
| Product (convolution): $\mathcal{H}_q^{(n_1, K_1)} *_q \mathcal{H}_q^{(n_2, K_2)}$ | yes | $\subseteq \bigoplus \mathcal{H}_q^{(n_1 + n_2, K')}$ |
| Bar involution: $\mathcal{H}_q^{(n, K)} \to \mathcal{H}_q^{(n, K^*)}$ | yes | mirror knot $K^*$ |
| Markov trace $\mathrm{tr}_M$: $\mathcal{H}_q^{(n, K)} \to \mathcal{P}_n$ | yes | depth-preserving |
| Joint Galois action ([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)) | conjectural | semi-direct product structure |

### Significance for the paper's existing operations

This proposition serves three purposes:

1. **Names the pattern.** The "$\Delta_I$-style" non-tensor products
   are now collected under one definition: each is a knot-indexed
   convolution at a specific $(n, K)$ stratum.

2. **Predicts compatibility.** Operations at the same depth $n$ but
   different $K$ should compose via convolution as the table predicts.
   E.g., $\mathrm{Lk}_R^{(k_1)} *_q \mathrm{Lk}_R^{(k_2)}$ should
   land in $\mathcal{H}_q^{(0, \text{double link})}$.

3. **Identifies novel candidates.** The empty cells of the grid —
   in particular high-$n$ chiral entries and the $S_5$-Galois orbit
   of depth-3 cyclotomic periods — are *predicted to exist* by the
   bi-filtration definition but are not yet realised in the paper.
   Each is a falsifiability target.

### Status

**Tabulation block.** The placement of each existing operation is
*verified by inspection* of its defining block. The closure
properties are *conjectural* (modulo well-definedness of the
bi-filtration). The joint-action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
sharpens the closure into an equivariance.
