**Proposition (crystal-basis reduction of three mass-tower open
problems; conditional on
[`conj:kazhdan-lusztig-classical-limit`](../particle-interactions/kazhdan-lusztig-classical-limit.md)
+ Brundan-Kleshchev / Lecouvey conjectures per §3b-cond).**
*Under the Brundan-Kleshchev isomorphism
$H_n(R, q) \cong R^\Lambda_\alpha$ (cyclotomic KLR algebra)
[`brundankleshchev2009`] and the Lecouvey GS-irreducible /
crystal-highest-weight bijection [`lecouvey2007`]
([`conj:crystal-graph-realization`](#conj:crystal-graph-realization)),
three of the four remaining mass-tower open problems reduce to
finite-graph combinatorics on Kashiwara crystals
$\mathrm{Cryst}(\mathfrak{sl}_n)$ [`kashiwara1991`]:*

- *the chirality factor's $\langle c \rangle_\beta$ Wedderburn-weighted
 average becomes a sum over **integer crystal multiplicities**;*
- *Term 7's level-5 character projector $\chi_5(T_w)$ becomes a
 **height-6 crystal-vertex count**;*
- *the brane-tower $|V|\to 1$ divergence is regularised by the
 Kazhdan-Lusztig classical-limit functor
 ([`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)),
 whose action collapses $H_n(R, q)$ to $\mathbb{Z}[S_n]$ via
 integer KL coefficients.*

## The three reductions

### Reduction 1: chirality $\langle c \rangle_\beta$ via Type-B folding

[`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation)
yields the first-order chirality factor

$$
  a_K(\beta) \;=\; 1 + w(\beta) \cdot \langle c \rangle_\beta \cdot h
   \;+\; O(h^2),
\qquad
  \langle c \rangle_\beta \;:=\; \frac{\sum_\lambda w_\lambda\,\chi^\lambda(\beta)\,c(\lambda)}
       {\sum_\lambda w_\lambda\,\chi^\lambda(\beta)}.
$$

The Wedderburn weights $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ and
characters $\chi^\lambda(\beta)$ are conventionally computed in
the $H_n(R, q)$ semi-normal form. Under Brundan-Kleshchev, both
become **graded crystal multiplicities**:
$\dim_q(\lambda)$ is the $q$-character of the crystal component
labelled by $\lambda$, and $\chi^\lambda(\beta)$ is the trace of
$\beta$ acting on the crystal-graph image of the projective
$P_\lambda$.

**Type-B folding shortcut (AGENTS.md §7b).** *To enforce
matter–antimatter pairing structurally — equivalently, the
bar-involution $q \leftrightarrow q^{-1}$ symmetry — fold the
$\mathfrak{sl}_n$ Cartan datum into a Type B datum. The resulting
Kashiwara graph is a **symmetric crystal**, and its GS normal forms
are bar-involution invariant by construction.* For chirality,
this means: **on the folded Type-B crystal, $\langle c \rangle_\beta$
is a sum of cell-content invariants paired by the fold involution
$\lambda \leftrightarrow \lambda^T$, hence a fixed-point integer
combination $c(\lambda) + c(\lambda^T) = 0$ summand-by-summand.**
The non-trivial part of $\langle c \rangle_\beta$ is the
**imbalance** between $\chi^\lambda(\beta)$ and $\chi^{\lambda^T}(\beta)$
along the folded-crystal Demazure components — a purely
combinatorial finite computation on the Type-B crystal graph.

### Reduction 2: Term 7's $\chi_5$ via height-6 crystal vertices

`conj:shell-correction-term-seven`
defines the level-5 character projector

$$
  \chi_5(T_w)
  \;:=\;
  \sum_{\lambda \vdash 3A,\;\mathrm{height}(\lambda) = 6}
    w_\lambda(q) \cdot \chi^\lambda(T_w).
$$

Under Brundan-Kleshchev, partitions $\lambda$ of height 6 correspond
to **crystal vertices at depth 6 in $\mathrm{Cryst}(\mathfrak{sl}_{3A})$**
(depth = number of Kashiwara $\tilde{f}_i$ operators applied from
the highest weight). The set
$\{\lambda \vdash 3A : \mathrm{height}(\lambda) = 6\}$ is a **finite
crystal-vertex enumeration** for any fixed $A$ — a standard
RSK / hook-content computation [`khovanovlauda2009`].

The α_5 magnitude open in `Term7ShellCorrectionClass` reduces to:
*compute the crystal-vertex sum at height 6 for $A = 4$ ($^4$He),
$A = 5$ ($^5$Li, $^5$He), $\ldots$, multiply by the Wedderburn weight
$w_\lambda(q_0)$, and read off the AME-residual amplitude.* No new
mathematical machinery; the finite crystal computation.

The shell-closure sign $\alpha_5 < 0$
([`Term7ShellCorrectionClass`](mass-tower-open-problems-classes.lean))
is now a **structural consequence**: height-6 partitions exist
only for $3A \geq 6$ (i.e. $A \geq 2$), and the binding-enhancing
sign follows from the **Demazure sub-crystal** structure at
height 6 (AGENTS.md §7b: *Demazure sub-crystals for resonances*).
Each Demazure component represents an *incomplete* topological
state that lowers the energy budget — exactly the binding
enhancement $\alpha_5 < 0$ encodes.

### Reduction 3: brane-tower $|V|\to 1$ via Kazhdan-Lusztig classical limit

[`conj:brane-tower-z-habiro`](../braids-and-knots/brane-tower-z-habiro.md)
diagnoses an analytic divergence: per-generator volumes
$z_i = |\hat{V}_i|$ for low isotopes lie just below
$z = q_0 \approx 1.11$, the first pole of $\Phi_q$. The summand
$\Phi_q(z)$ is enormous and the analytic series diverges.

The Kazhdan-Lusztig classical-limit functor
[`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)
sends each KLR canonical basis element $b_w$ to its $q \to 1$
specialisation $C_w \in \mathbb{Z}[S_n]$ — a **specific integer
$\pm 1$ permutation sign**. Under this functor the divergent
analytic Hecke trace becomes a **finite integer-coefficient sum
over the symmetric group $S_n$**, since the Wedderburn dimensions
specialise to the classical hook-length integers. The KL classical
limit is therefore the **canonical regularisation** of the brane
tower at $|V|\to 1$ — independent of the Yekutieli finite-slice
or $q$-Habiro completion choices. The uniform bound demanded by
`ZHabiroConvergenceClass` becomes:

$$
  M \;\leq\; \sum_{w \in S_n} |C_w(q_0 \to 1)|
       \;=\; \sum_{\lambda \vdash n}
       \dim(V_\lambda) \;\cdot\;\bigl|\langle\,\cdot\,\rangle_\lambda\bigr|
       \;<\; \infty
$$

— a finite sum of classical hook-length-integer dimensions
multiplied by classical character values, both bounded.

## The fourth open problem

The K-theoretic identification
[`conj:bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition)
asks whether $2/(3\pi)$ lies in the rank-8 Bloch group image of
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$. Crystal bases do *not*
directly resolve this: Bloch-Wigner values $D[Z_K]$ are
**transcendental** archimedean realisations, while crystal bases
are **integer-coefficient** combinatorial objects. The crystal
side gives the q-rational Hecke trace structure
(pre-archimedean, in $R$); the Bloch group lives on the other
side of $\tau_{\text{arch}}$. The open question is therefore
genuinely transverse to the crystal-basis machinery — a finite
integer-relation search in $\mathbb{R}$ rather than a
crystal-graph computation.

## Provability summary

| Open problem | Crystal-basis reduction | Open content after reduction |
|---|---|---|
| Chirality $\langle c \rangle_\beta$ | Type-B folded crystal imbalance computation | finite Kashiwara graph traversal |
| Term 7 $\alpha_5$ magnitude | height-6 crystal-vertex enumeration | RSK / hook-content sum at $\lambda \vdash 3A$, ht 6 |
| z-Habiro $\lvert V\rvert\to 1$ | KL classical-limit integer regularisation | bounded by classical dim$(V_\lambda)$ sums |
| Bloch decomposition of $2/(3\pi)$ | (transverse — crystal bases pre-archimedean) | Bloch-group integer relation search |

Three of the four problems become **finite combinatorial
computations on Kashiwara crystals** — substantially more
tractable than their original analytic / structural formulations.
The Lean infrastructure documented in
[`mass-tower-open-problems-classes.md`](mass-tower-open-problems-classes.md)
remains the §3b-cond hook structure; this proposition supplies
the mathematical pathway by which the open class instances can be
inhabited via crystal-graph computations once the upstream
Brundan-Kleshchev correspondence is formally tight.
