**Proposition (placement of paper's existing knot-indexed
convolutions in the bi-filtration grid; conditional on [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)).**

*Each existing "non-tensor product" operation in the QOU paper —
where two morphisms are combined via a knot/braid/partition-shaped
twist rather than a plain tensor product — sits at a specific
$(n, K)$ stratum of the bi-filtration $\mathcal{H}_q^{(n, K)}$
([`def:hq-bi-filtration`](#def:hq-bi-filtration)).*

### The grid

See [Table 1](#tbl:knot-indexed-convolution-grid-table1-data).

### Two structural observations

#### Observation 1: most "knot-indexed" operations sit at $n = 0$

The paper's *operational* knot-indexed convolutions ($\mathrm{Lk}_R^{(k)}$,
$\bowtie_K$, Hoefsmit pairing, Markov trace) live at depth $n = 0$
on the algebraic side — they manipulate Hecke elements without
introducing polylogarithms. Their *archimedean image* sits at
higher depth depending on what is paired with: Markov trace + braid
of a hyperbolic knot lands at depth 2 (volume); CS lands at depth 3.

This is not accidental: the bi-filtration encodes a clear separation
between **input shape** (the knot index $K$, depth-$0$ on the
algebraic side) and **output transcendence depth** (achieved only
after applying $\tau_{\mathrm{arch}}$, which involves the depth-$n$
grouplike $\mathrm{Li}_n^q$).

#### Observation 2: the $\bowtie_K$ "non-tensor product" pattern is a depth-0 knot index

The original confusion in the first answer of this session — was
$\bowtie_K$ a Mikusiński-style convolution? — reduces to: **$\bowtie_K$
is a depth-0, knot-indexed Hecke element**. In the bi-filtration
language:

$$
  \bowtie_K \;\in\; \mathcal{H}_q^{(0, \,\text{EW interface braid})}.
$$

The "convolution" structure the user identified is the bi-filtration
itself: convolution by $\bowtie_K$ shifts the knot-index axis (via
left/right multiplication in $H_6(q)$) without changing the depth
axis. This is a *structural translation*, not a polylogarithmic
operation.

### Closure properties of the grid

See [Table 2](#tbl:knot-indexed-convolution-grid-table2-data).

### Significance for the paper's existing operations

This proposition serves three purposes:

1. **Names the pattern.** The "$\bowtie_K$-style" non-tensor products
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

### Discussion

**Tabulation block.** The placement of each existing operation is
*verified by inspection* of its defining block. The closure
properties are *conjectural* (modulo well-definedness of the
bi-filtration). The joint-action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
sharpens the closure into an equivariance.
