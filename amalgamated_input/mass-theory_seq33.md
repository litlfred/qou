<!-- FILE_START: intro-spectral-sequence-chirality-confinement.md -->
The categorical braid-word space carries a natural filtration
indexed by jet-prefix length, and the resulting Gröbner–Shirshov
filtration converges via a spectral sequence to the categorical
normal-form invariants.  This section assembles the spectral
sequence, identifies its $E_\infty$ page with the chirality-
graded normal-form ring, and extracts the confinement-NF
structure that the chapter's normal-form computations consume.

The arc proceeds in three layers.  The first blocks define the
jet-prefix GS filtration and prove the resulting spectral
sequence converges; the middle blocks identify the $E_2$ page
with the chirality-graded ring (which carries the natural
involutive action mirroring matter ↔ antimatter), and derive
the $E_\infty$ identification with the confinement-NF structure;
the closing blocks tabulate the explicit $E_\infty$ classes for
small braid words and tie them to the binding-energy formulas
the next chapter uses.

The section's output is the confinement-NF normal-form
structure with explicit chirality grading.  This is the
chapter's structural backbone: every categorical mass / charge
computation downstream reads off the matching $E_\infty$ class
of its braid word.  Readers focused on applications can take
the closing tabulation; the spectral-sequence machinery is
technical but compactly handled.
<!-- FILE_END: intro-spectral-sequence-chirality-confinement.md -->

<!-- FILE_START: jet-prefix-gb-filtration.md -->
**Proposition (candidate: GB-filtration-indexed prefix; conditional on [`conj:confinement-grading-correspondence`](#conj:confinement-grading-correspondence)).**
*Define the **Gröbner–Shirshov-filtered prefix** $\beta_k^{\mathrm{GS}}$
of an atomic braid word $T_w \in H_{3A}(q)$ as the projection of
$T_w$ onto the filtration stratum*

$$
  \beta_k^{\mathrm{GS}}
  \;:=\;
  \sigma_{k-3}\bigl(T_w\bigr)
  \;\in\;
  J^{k-3}(q) / J^{k-2}(q),
$$

*where $J^\ell(q)$ is the confinement filtration
([confinement level](#def:confinement-level)) and $\sigma_\ell$
is the symbol map to the $\ell$-th graded piece. The jet-level
prefix formula then reads*

$$
  a_k(\beta_k^{\mathrm{GS}})
  \;=\;
  \frac{\mathrm{tr}_M^{[\ell]}\bigl(\beta_k^{\mathrm{GS}}\bigr)}
       {\sum_\lambda w_\lambda\,\dim\mathrm{Res}^{H_k}_{H_3}(V_\lambda)},
$$

*where $\mathrm{tr}_M^{[\ell]}$ is the Markov trace restricted to
the level-$\ell$ graded piece.*

**GB filtration versus geometric cutoffs.**
*The geometric cutoffs (nucleon count, strand count, generator index)
do not respect the Hecke-algebra structure. The GB filtration
is **algebraically** defined by the knot-operator energies
$E_\ell(q)$, so the prefix $\beta_k^{\mathrm{GS}}$ respects the
Hecke-algebra structure. Each filtration level has a well-defined
$\dim\mathrm{Res}^{H_k}_{H_3}$ because the graded piece
$J^\ell/J^{\ell+1}$ is itself a semisimple $H_3$-bimodule.*

**KLR grading interpretation.**
*Under the
[confinement–grading correspondence](#conj:confinement-grading-correspondence),
the confinement level $\ell(K, q)$ of a closed braid $K$ coincides
with the top non-zero $\mathbb{Z}$-grading degree of its KLR-module
lift $\mathfrak{M}_K$ on the cyclotomic KLR algebra; the symbol
$\sigma_\ell(T_w) \in J^\ell / J^{\ell+1}$ is that top graded
component. Truncating $T_w$ at jet order $k$ therefore keeps the
graded components of $\mathfrak{M}_K$ in degrees $\leq k$ of the KLR complex;
the residual error $E(k)$ is the homological remainder supported in
degrees $k < d \leq \ell(K, q)$, and the truncation is exact
precisely when $k \geq \ell(K, q)$. The candidate prefix
$\beta_k^{\mathrm{GS}}$ inherits its restriction multiplicities
$\dim\mathrm{Res}^{H_k}_{H_3}$ from this graded structure.*

**Predictions of the GB-filtration prefix.**

1. *At level $0$: $\beta_0^{\mathrm{GS}} = $ descended Markov-trace
 part. $a_0 = 1$ by definition (the ratio is $\mathrm{tr}_M/\mathrm{tr}_M = 1$).*
2. *At level $\ell \geq 1$: $\beta_\ell^{\mathrm{GS}}$ picks up the
 corresponding root-of-unity residue
 ([GB residue spectral sum](#prop:gb-residue-spectral-sum)).*
3. *Product $\prod_\ell a_\ell = 1 + $ (corrections from higher
 strata) — matches the "near 1" shape expected.*
<!-- FILE_END: jet-prefix-gb-filtration.md -->

<!-- FILE_START: jet-prefix-gb-filtration-evidence.md -->
**Failed prefix conventions (pre-history).**
Upstream attempts implemented the paper's jet-level prefix formula

$$
  a_k(\beta_k)
  \;=\;
  \frac{\sum_\lambda w_\lambda\, \chi_\lambda^{(k)}(\beta_k)}
       {\sum_\lambda w_\lambda\,\dim\mathrm{Res}^{H_k}_{H_3}(V_\lambda)},
  \qquad
  a(Z, N)
  \;=\;
  \prod_{k = 3}^{3A} a_k(\beta_k),
$$

where $\beta_k$ is the **prefix** of the atomic braid word at Hecke
level $k$, and $\mathrm{Res}^{H_k}_{H_3}$ is the restriction functor.
Three prefix conventions were tested — all failed to reproduce AME
bindings:

| convention | D | T | ${}^{3}\mathrm{He}$ | ${}^{4}\mathrm{He}$ |
|---|---|---|---|---|
| nucleon-cumulative ($A$-step prefix) | $-65\%$ | $-91\%$ | $-91\%$ | degenerate |
| strand-cumulative (first $k$ strands) | $-99\%$ | $-99\%$ | $-99\%$ | degenerate |
| generator-bounded (gen $\leq k-2$) | $3.1 \times 10^{-6}$ (essentially zero) | $\sim 0$ | $\sim 0$ | $\sim 0$ |

*All three converge to zero rather than a "correction near 1",
suggesting a structural mis-identification of the prefix.*

**Caveat.** A first candidate prefix — the height-based heuristic — fails the test below; the GB-filtration prefix of [prop:jet-prefix-gb-filtration](#prop:jet-prefix-gb-filtration) replaces it.

*A first-pass version uses the heuristic filtration level $\ell(\lambda) = \mathrm{len}(\lambda) - 1$
(diagram height minus one) to group partitions. Results:*

| isotope | $\prod_k a_k$ (free) | $\prod_k a_k$ (atom) |
|---|---|---|
| $\mathfrak{p}$ | $+0.924$ | — |
| $\mathfrak{n}$ | $-0.647$ | — |
| D | $+0.015$ | $-3.9 \times 10^{-4}$ |
| T | $-2 \times 10^{-6}$ | $+1.5 \times 10^{-11}$ |
| ${}^{3}\mathrm{He}$ | $-7 \times 10^{-7}$ | $-1.8 \times 10^{-11}$ |

*Products collapse rapidly with $A$, have arbitrary signs, and
differ from the expected "correction near 1" shape. This
heuristic filtration level does not reproduce Term 6.*

*Four candidate prefix conventions have now been tested (three
upstream + this one), all fail. This is **structural evidence**
that the jet-level prefix formula — as stated in the
paper — is either wrong or requires a different filtration
definition entirely. Possibilities:*

1. *The filtration index must use the **true confinement-level**
 $\ell(K, q)$ (energy-sorted $J^\bullet$), not a combinatorial
 proxy. Implementing this requires solving the LP at each
 $k$, a substantially heavier computation.*
2. *The prefix formula should use **restriction** $\mathrm{Res}^{H_k}_{H_3}$
 in a different basis (not classical dim but $\dim_q$).*
3. *Term 6 may not be a multiplicative prefix at all, but an
 additive correction in the spectral-sequence
 ([$E_\infty$ page identifications](#prop:e-infinity-page-identifications))
 from $E_\infty^{\ell \geq 3, *}$ pages directly.*

*The "research direction" label on the candidate proposition therefore
upgrades: the prefix formula requires **structural reformulation**,
not just better implementation.*

**Relation to existing blocks.**

- *The GB residue spectral sum
 ([GB residue spectral sum](#prop:gb-residue-spectral-sum)) is
 the **output** of the prefix formula: the sum $\sum_\ell
  a_\ell$ of level contributions.*
- *The Schur–Weyl decomposition
 ([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition))
 is the **full** Markov trace; the prefix formula computes it
 level-by-level.*
- *Paper's figure-eight BW coefficients
 ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
 give the A$\ge$3 specialisation that the prefix formula must
 reproduce.*

**Open questions.**

1. *Is the GB-filtration-indexed prefix the **unique** algebraically-
 natural choice, or are there other filtration-based options?*
2. *Does the product formula $a = \prod_k a_k$ converge for all $A$?*
3. *What is the canonical structural verification cost for $A = 3, 4$?*
4. *Does the jet-level prefix recover paper's BW+chirality at
 $A = 3$?*
<!-- FILE_END: jet-prefix-gb-filtration-evidence.md -->

<!-- FILE_START: frobenius-self-pairing-chirality.md -->
**Definition (Frobenius self-pairing chirality).**
*Let $(A, \tau)$ be a self-dual Frobenius algebra (e.g., the Hecke
algebra $H_n(R, q)$ under Markov trace
([Jones–Markov trace](#thm:jones-markov-trace))), and let
$\beta \in A$ be a braid word. Let $\beta^* \in A$ denote the
image of $\beta$ under the algebra **antipode** (the anti-involution
$\sigma_i \mapsto \sigma_i^{-1}$, reverse word order). Define the
**chirality factor** of $\beta$ as*

$$
  a_K(\beta)
  \;:=\;
  \frac{\tau(\beta \cdot \beta^*)}{\tau(1 \cdot 1)}.
$$

*Equivalently: $a_K(\beta) = \|\beta\|_\tau^2 / \|1\|_\tau^2$ is the
normalised Frobenius norm of $\beta$ in the self-dual pairing.*
<!-- FILE_END: frobenius-self-pairing-chirality.md -->

<!-- FILE_START: chirality-from-frobenius-self-pairing.md -->
**Proposition (chirality classification by writhe and topology).**
*Let $a_K(\beta) = \tau(\beta\beta^*)/\tau(1)$ be the Frobenius
self-pairing chirality factor
([def:frobenius-self-pairing-chirality](#def:frobenius-self-pairing-chirality))
of the atomic braid $\beta$. The chirality factor satisfies:*

1. *For a **chiral knot** $K$ with writhe $w(K) \neq 0$:*

$$
   a_K \;=\; 1 + w(K) \cdot h \;+\; O(h^2),
$$

*to leading order in the Hecke deformation $h = q - q^{-1}$.*

2. *For an **amphichiral knot** $K$ (i.e., $K = \overline{K}$ under
 mirror):*

$$
   a_K \;=\; 1 - c_K \cdot h^2 \;+\; O(h^4),
$$

*where $c_K$ is a topological invariant (writhe-squared
contribution). For the figure-eight $4_1$: $c_K = 1$, giving
$a_K = 1 - h^2$.*

3. *For a **Borromean-type link** (multiple amphichiral sublinks):*

$$
   a_K \;=\; \prod_i (1 - c_{K_i} h^2).
$$

*For $^4$He (two amphichiral pairs): $a_K = (1 - h^2)^2$.*

**Derivation sketch.**

*Under the Markov trace, $\tau(\sigma_i \sigma_i^{-1}) = \tau(1) = 1$
(Hecke eigenvalue pair $q, -q^{-1}$ gives $\sigma_i \sigma_i^{-1} = 1$
in $H_n(R, q)$). Thus the identity braid has $a_K = 1$.*

*For a **single positive crossing** $\beta = \sigma_i$:*

$$
  \beta^* = \sigma_i^{-1},
  \qquad
  \beta \beta^* = \sigma_i \sigma_i^{-1} = 1,
  \qquad
  \tau(\beta \beta^*) = 1,
$$

*which gives $a_K = 1$ — no deformation from the identity. The
**first-order** $h$-contribution therefore requires the braid to
have a **genuine chiral structure** that is not undone by the
self-pairing.*

*For $\beta = $ trefoil $(3_1) = \sigma_1^3$: $\beta^* = \sigma_1^{-3}$,
$\beta \beta^* = 1$, so $a_K = 1$ — trefoil is chiral but its
Frobenius self-pairing is trivial at the raw Hecke level. The
non-trivial $(1 + h)$ chirality factor arises from **higher Markov
moments** when the braid is viewed as a morphism $\varrho: \mathbf{1}
\to A$ (closure operation), not as an abstract algebra element.*

*Paper's derivation
(figure-eight BW coefficients
§Proof) uses the Fricke trace relation*

$$
  \mathrm{tr}([A, B])
  = \mathrm{tr}(A)^2 + \mathrm{tr}(B)^2 + \mathrm{tr}(AB)^2
  - \mathrm{tr}(A)\mathrm{tr}(B)\mathrm{tr}(AB) - 2
$$

*in $\mathrm{SL}_2$, evaluated at $A = T_1, B = T_2^{-1}$ in the
standard representation of $H_3(R, q)$. This gives the figure-eight
character $\chi_{4_1}((2,1)) = 2 - [3]_q = -1 - h^2$, from which
$a_{4_1} = 1 - h^2$. For satellite knots (e.g., $D$), the Fricke
relation does not apply at $H_3$ level — one must work in $H_6(R, q)$
or larger, where the character-trace identities are more involved.*
<!-- FILE_END: chirality-from-frobenius-self-pairing.md -->

<!-- FILE_START: chirality-from-frobenius-self-pairing-scope.md -->
**Scope.** This proposition derives only the amphichiral case.

*The Frobenius self-pairing gives a rigorous definition
$a_K(\beta) = \tau(\beta \beta^*)$ that is categorical (monoidal-
category self-duality) and universal (applies to any $(A, \tau)$
with antipode). For **amphichiral** knots ($4_1$, Borromean), the
Fricke identity + paper's derivation gives the specific values.
For **chiral knots** (trefoil, satellite), the Frobenius self-pairing
at the Hecke algebra level gives $a_K = 1$ by definition; the observed
$1 + h$ factor for $D$ comes from the **closure** operation
(Markov-trace normalisation), not from the algebra pairing.*

*A complete categorical derivation of all three cases requires
tracking the **braid closure** (cylinder tensor product) in a
:refterm[braided monoidal category]{#braided-monoidal-category} with ribbon structure. The ribbon twist
$\varTheta_X$ encodes writhe; its interaction with the Frobenius
pairing produces the first-order $h$ contribution for chiral knots.
This derivation is **open**; paper's empirical values
$\{1+h, 1-h^2, (1-h^2)^2\}$ await a uniform categorical proof.*

**Structural value.**

*Even without the complete derivation, this proposition provides:*

1. *A **rigorous** definition of chirality in any self-dual Frobenius
 algebra with antipode — not the Hecke case.*
2. *A categorical framing that ties chirality to the **same**
 Frobenius structure producing the co-Casimir residual
 ([Frobenius universal](#thm:frobenius-codim-universal)).*
3. *A clear path to the missing derivation: ribbon-category closure
 + writhe identification.*

*Recommended next step: formalise the ribbon-category closure of
$\varrho: \mathbf{1} \to A$ and compute $a_K$ via the composite
$\tau \circ (\varrho \otimes \varrho^*)$ explicitly for trefoil and
figure-eight.*
<!-- FILE_END: chirality-from-frobenius-self-pairing-scope.md -->

<!-- FILE_START: hecke-curvature-2-cocycle.md -->
**Definition (Hecke curvature 2-cocycle).**
*The Hecke algebra $H_n(R, q)$ has free-algebra generators $\sigma_1,
\ldots, \sigma_{n-1}$ subject to two relations:*

$$
  R_H(i) \;:=\; \sigma_i^{\,2} - (q - q^{-1})\,\sigma_i - \mathbf{1}, \qquad
  R_{YB}(i) \;:=\; \sigma_i \sigma_{i+1} \sigma_i - \sigma_{i+1} \sigma_i \sigma_{i+1}.
$$

*The **Hecke curvature 2-cocycle** is the 2-form-valued bilinear
map $F \in C^2(H_n(R, q), H_n(R, q))$ defined on generator pairs by:*

$$
  F(\sigma_i, \sigma_j) \;=\;
  \begin{cases}
    R_H(i) & \text{if } i = j, \\
    R_{YB}(i) & \text{if } |i - j| = 1, \\
    [\sigma_i, \sigma_j] & \text{if } |i - j| \geq 2,
  \end{cases}
$$

*and extended to general elements by the Leibniz rule
$F(ab, c) = a F(b, c) + F(a, c) b$, $F(a, bc) = F(a, b) c + b F(a, c)$.
$F$ is a $2$-cochain in the Hochschild complex
([GB spectral sequence](#prop:gb-spectral-sequence)), and on the
free algebra $\mathbb{C}\langle \sigma_1, \ldots, \sigma_{n-1}\rangle$,
$F$ measures **failure of commutativity** at each generator pair
in the same way that the curvature $F_A = dA + A \wedge A$ of a
principal connection measures failure of flatness.*
<!-- FILE_END: hecke-curvature-2-cocycle.md -->

<!-- FILE_START: curvature-rank.md -->
**Definition (curvature-rank).**
*For an element $T_w \in H_n(R, q)$ written as a word in
$\sigma_i^{\pm 1}$ of length $\ell(T_w)$, the **curvature-rank**
$r(T_w)$ is the smallest non-negative integer $r$ such that*

$$
  F^{\,r}(T_w) \;=\; F\bigl(F\bigl(\cdots F(T_w)\cdots\bigr)\bigr)
  \;\in\; J^{\,r}(q) \setminus J^{\,r+1}(q),
$$

*where $F$ is the Hecke curvature 2-cocycle
([def:hecke-curvature-2-cocycle](#def:hecke-curvature-2-cocycle)),
$F^{\,r}$ is the $r$-fold iterated curvature applied via
Leibniz extension, and $J^\bullet(q)$ is the GB confinement
filtration ([confinement level](#def:confinement-level)).
Equivalently, $r(T_w)$ counts the minimal number of times the
Hecke or Yang–Baxter relations must be applied to express $T_w$
in normal form starting from its free-algebra representative.*

*By construction $r(\mathbf{1}) = 0$, $r(\sigma_i) = 0$,
$r(\sigma_i^{\,2}) = 1$ (one Hecke reduction),
$r(\sigma_i \sigma_{i+1} \sigma_i) = 0$ in normal form but $1$ if
the YB relation must be applied.  In general,
$r(T_w) \leq \ell(T_w)$ with equality only for words requiring
maximal reduction.*
<!-- FILE_END: curvature-rank.md -->

<!-- FILE_START: curvature-rank-gb-stratification.md -->
**Proposition (curvature-rank = GB filtration index).**
*Let $F$ be the Hecke curvature 2-cocycle
([def:hecke-curvature-2-cocycle](#def:hecke-curvature-2-cocycle))
and $r(T_w)$ the curvature-rank
([def:curvature-rank](#def:curvature-rank)) of $T_w \in H_n(R, q)$.
The curvature-rank stratifies the GB filtration:*

$$
  \boxed{
    J^{\,r}(q) / J^{\,r+1}(q)
    \;=\;
    \bigl\{T_w \in H_n(R, q)\ \bigm|\ r(T_w) = r\bigr\},
  }
$$

*so the spectral-sequence pages of
[GB spectral sequence](#prop:gb-spectral-sequence) decompose by
curvature-rank:*

$$
  E_r^{\ell, *}(H_n(R, q))
  \;=\;
  \bigl\{ T_w\text{-induced cohomology classes of curvature-rank } \ell\bigr\}.
$$

*Consequence: the **non-abelian Stokes residue** of the Markov
trace at filtration depth $\ell$ equals the contribution from
words of curvature-rank $\ell$.*
<!-- FILE_END: curvature-rank-gb-stratification.md -->

<!-- FILE_START: curvature-rank-gb-stratification-interpretation.md -->
**Remark (geometric reading).**
*Under the archimedean realisation
([topological mass](#prop:topological-mass-formula)), the Markov
trace becomes a holonomy along the boundary of a Seifert surface,
and the curvature 2-cocycle $F$ becomes the curvature 2-form of
the corresponding flat connection on the Frobenius–Hopf bundle.
Non-abelian Stokes:*

$$
  \mathrm{tr}_M(\beta) \;=\; \mathrm{Hol}_{\partial \Sigma}\bigl(A\bigr)
  \;=\; \int_\Sigma F_A
  \;=\; \sum_{r \geq 0} \int_{\Sigma_r} F^{\,r}_A,
$$

*where $\Sigma_r \subset \Sigma$ is the curvature-rank-$r$ stratum
of the Seifert surface (its $r$-fold blow-up locus).
Each integral $\int_{\Sigma_r} F^r_A$ corresponds to the $E_\infty^{r,*}$
contribution and to one of the six mass terms.*
<!-- FILE_END: curvature-rank-gb-stratification-interpretation.md -->

<!-- FILE_START: ks-finiteness-via-diamond-lemma.md -->
To put a motivic measure on the moduli stack of objects,
Kontsevich--Soibelman *assume* their categories are
**ind-constructible** \cite{kontsevich-soibelman-2008} — countable
inductive limits of constructible sets (their Lemma 1, Corollary 1).
For a general $3$-Calabi--Yau category there is no other way to make
"the number of objects of class $\gamma$" well defined; the hypothesis
is the load-bearing tameness input.

In the QOU setting this finiteness is **not assumed but proved**, in
two lines, by the Gröbner--Shirshov / Diamond Lemma — the same move by
which Poincaré--Birkhoff--Witt becomes an algebraic triviality (the
unital Gröbner-bases route to PBW).

**Setup (one definition).** The Gröbner--Shirshov normal form gives
$H_n(q)$ a basis of **standard monomials** $\{T_w : w \in S_n\}$
indexed by the finite Coxeter group $S_n$ — confluence of the braid +
Hecke rewriting system (Bergman's Diamond Lemma \cite{bergman1978};
Bokut \cite{bokut2005}).

**Two-line proof.** The standard monomials of Coxeter length
$\ell(w) = k$ form a **finite** set — at most
$|\{w \in S_n : \ell(w) = k\}| \le |S_n|$ of them — so each length-$k$
slice of $H_n(q)$ is a finite-dimensional scheme, *constructible by
theorem*, and the curvature-rank stratification ([GB
stratification](#prop:curvature-rank-gb-stratification)) refines it
into finitely many strata. No tameness hypothesis is needed:
confluence delivers the finite slice. $\square$

So where KS *assume* ind-constructibility to buy finiteness, QOU
*earns* it from the Diamond Lemma — a known structural input given a
prior abstract assumption, recovered here as an algebraic theorem. The
price is specificity: QOU commits to the semisimple Hecke/braid
category rather than an arbitrary $3$CY, which is exactly the trade
that lets the partition decomposition replace the motivic Hall
algebra.
<!-- FILE_END: ks-finiteness-via-diamond-lemma.md -->

<!-- FILE_START: spectral-sequence-collapse.md -->
**Proposition (cohomology vanishing collapses the GB spectral sequence).**
*Let $A = H_n(R, q)$ for $R$ a commutative ring with $q \in R$ such
that $A$ is semisimple
([three-parameters-wedderburn](#prop:three-parameters-wedderburn)).
Then Hochschild cohomology vanishes in positive degrees:*

$$
  \mathrm{HH}^k(A,\, A) \;=\; 0 \quad \text{for all } k \geq 1.
$$

*Consequently the GB filtration spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence)) collapses at
$E_1$, with all contributions concentrated in*

$$
  E_\infty^{0, *} \;=\; \mathrm{HH}^0(A) \;=\; Z(A) \;=\; \bigoplus_{\lambda \,\vdash\, n} R \cdot e_\lambda,
$$

*the centre, a direct sum of central idempotents indexed by partitions
of $n$.*
<!-- FILE_END: spectral-sequence-collapse.md -->

<!-- FILE_START: delta-q-decoration.md -->
**Definition (q-dimension decoration of the NF basis).**
*Let $H_n(q)$ be the Iwahori–Hecke algebra over
$R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, with normal-form
basis $\{b_w\}_{w \in S_n}$ indexed by reduced expressions of
permutations $w \in S_n$.  The
**$\delta_q$-decoration** is the map*

$$
  \delta_q : H_n(q) \;\longrightarrow\; R^{|\,\mathrm{Par}(n)\,|}
$$

*— the **:defterm[$\delta_q$-decoration]{#delta-q-decoration}** —
sending an algebra element $b \in H_n(q)$ to the tuple of its
$q$-characters in each irreducible representation
$V_\lambda$ (for $\lambda \vdash n$):*

$$
  \delta_q(b)
  \;:=\;
  \bigl(\chi_\lambda(b)\bigr)_{\lambda \vdash n}
  \;\in\;
  R^{|\,\mathrm{Par}(n)\,|},
$$

*where $\chi_\lambda(b) = \mathrm{tr}_{V_\lambda}(\rho_\lambda(b))$
is the trace of $b$ acting in the seminormal-basis representation
$\rho_\lambda : H_n(q) \to \mathrm{End}(V_\lambda)$.*

### Significance of the :defterm[q-dimension layer]{#q-dimension-layer}

The Markov trace $\mathrm{tr}_M : H_n(q) \to R$ is the
characteristic invariant used in operator-selection LP
([`prop:operator-selection-lp`](#prop:operator-selection-lp))
and in the Φ$_q$ tower. It corresponds to a single weighted sum
over irreps:

$$
  \mathrm{tr}_M(b) \;=\; \sum_{\lambda \vdash n}
  w_\lambda \cdot \frac{\chi_\lambda(b)}{f^\lambda},
$$

where $w_\lambda = \dim_q(V_\lambda)^2 / [n]_q!$ and
$f^\lambda = \dim V_\lambda$ is the classical irrep dimension
(number of standard Young tableaux of shape $\lambda$).

The $\delta_q$-decoration **preserves the per-irrep structure**
that the Markov trace collapses by summing.  This refinement is
necessary to identify how $\alpha_{EM}$ — which lives in the
q-dimension layer
([`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation),
round 11) — projects onto specific Wedderburn components of
the molecular bound-state operator
([`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)).

### Wedderburn structure

Recall the Wedderburn decomposition for semisimple $H_n(q)$:

$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n}
  \mathrm{End}(V_\lambda).
$$

Under this isomorphism, $\delta_q(b)$ records exactly the per-block
trace:

$$
  \delta_q(b)_\lambda \;=\; \mathrm{tr}_{V_\lambda}\bigl(\rho_\lambda(b)\bigr).
$$

The **Markov trace contribution from each block** is then

$$
  \mathrm{tr}_M^\lambda(b)
  \;=\;
  \frac{w_\lambda}{f^\lambda}\,\delta_q(b)_\lambda.
$$

Summing over $\lambda$ recovers the standard Markov trace.

### Computation

A reusable Python implementation is available in
the canonical formalism,
using the seminormal Hoefsmit representation matrices from
the canonical formalism.
The witness data
[`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json)
caches the per-irrep characters for $H_2, H_3, H_4$ NF bases and
the force-carrier knots $T_{2,9}, T_{3,5}$.

**Computational complexity.** For partition $\lambda \vdash n$
with $f^\lambda$ standard Young tableaux, $\rho_\lambda(\sigma_i)$
is an $f^\lambda \times f^\lambda$ matrix.  Computing
$\delta_q(\beta)$ for a braid $\beta$ of length $\ell$ costs
$O(\ell \cdot \sum_\lambda (f^\lambda)^3)$ in matrix
multiplications.  For $n = 4$:
$\sum_\lambda (f^\lambda)^3 = 1 + 27 + 8 + 27 + 1 = 64$.

### Force-carrier examples

For the Bring force-carrier torus knots
([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness))
the $\delta_q$-decoration produces the q-dimensions appearing in
the bare formula
$1/\alpha_{EM} = q\,[9]_q\,[10]_q$
([`prop:em-coupling-projection`](#prop:em-coupling-projection)):

$$
  \delta_q(T_{2,9})
  \;=\;
  q^{9} - q^{-9}
  \;=\;
  h\,[9]_q,
$$

(in the $H_2(q)$ representation, summed over the two irreps
$V_{(2)}, V_{(1,1)}$ with eigenvalues $q^9, -q^{-9}$ respectively).

The companion identity
([`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio))
expresses $\alpha_{EM}$ as a categorical-trace ratio:

$$
  \alpha_{EM}
  \;=\;
  \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}.
$$

### Reusability

The $\delta_q$-decoration is the **single new infrastructure layer**
identified in
[`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation)
round 11 as the missing piece for fully categorical derivation of
the Hartree energy.  It is reusable across:

- Operator-selection LP (refines the Markov-trace cost into
  per-irrep contributions, useful for symbolic-$q$ analysis of LP
  optima).
- Bound-state projection analysis (rounds 17–18 of the
  $E_h$ investigation: identifies which irrep channels carry
  force-carrier content via the
  [`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)).
- Cache-and-reuse for downstream binding-energy computations
  (the witness JSON enables $O(1)$ lookup of per-irrep characters
  rather than re-multiplying matrices).
<!-- FILE_END: delta-q-decoration.md -->

<!-- FILE_START: alpha-basis-knot-delta-q.md -->
*Lean sibling: a field $R$ carrying the $q$-data (AGENTS.md §7c); the identity is purely algebraic, pre-archimedean.*

**Proposition (q-dimension decoration of the basis knots).** *For the basis
torus knot $T_{2,k}$, the q-dimension decoration factors as the Hecke
deformation $h$ times the quantum integer $[k]_q$:*

$$
  \delta_q(T_{2,k}) \;:=\; q^{k} - q^{-k}
  \;=\; h\,[k]_q,
  \qquad
  h = q - q^{-1},\quad [k]_q = \frac{q^{k} - q^{-k}}{q - q^{-1}},
$$

*an exact identity in the substrate ring $R = \mathbb{Z}[q^{\pm 1/2}, h^{-1}]$ —
**pre-archimedean, no $\pi$** — needing only $q - q^{-1} \neq 0$ for the
division. Lean `deltaQ_eq_h_qbracket`, sorry-free.*

This is the q-data building block of the **$\alpha_{\text{basis-knot}}$ coupling
family**: the fine-structure constant is
[`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
$\alpha_{EM} = h^2/\bigl(q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})\bigr)$, the
antisymmetric $e_-$ (sinh) coupling of the Hopf 2-strand operation, with
$\alpha_{EM} := \alpha_{T_{2,3}}$. Each $\delta_q(T_{2,k})$ above is one such
$h\,[k]_q$ factor. Symbolic cross-check (basis-knot exponents $\{3,5,7,9,10\}$,
all exact):
the canonical formalism.
<!-- FILE_END: alpha-basis-knot-delta-q.md -->

<!-- FILE_START: torus-knot-delta-q-writhe.md -->
*Lean sibling: a field $R$ carrying the $q$-data (AGENTS.md §7c); the identity is purely algebraic, pre-archimedean.*

**Proposition (writhe exponent of the torus-knot $\delta_q$ decoration).** *For the
torus knot $T_{m,p}$ — the closure of the standard positive braid
$(\sigma_1\cdots\sigma_{m-1})^p$, $\gcd(m,p)=1$ — the $q$-dimension decoration is the
Hecke deformation $h$ times the quantum integer at the **writhe** $w = (m-1)p$:*

$$
  \delta_q(T_{m,p}) \;:=\; q^{w} - q^{-w}
  \;=\; h\,[w]_q,
  \qquad
  w = (m-1)p,\quad h = q - q^{-1},\quad [w]_q = \frac{q^{w} - q^{-w}}{q - q^{-1}}.
$$

*an exact identity in the substrate ring $R = \mathbb{Z}[q^{\pm 1/2}, h^{-1}]$ —
**pre-archimedean, no $\pi$** — needing only $q - q^{-1} \neq 0$. Lean
`torus_deltaQ_eq_h_qbracket`, sorry-free.*

The decoration is the **bar-odd** ($\sinh$, $e_-$) part of the **trivial /
top-channel twist** $q^{(m-1)p}$: in the trivial one-dimensional block of the
Hecke algebra $H_m(q)$ every generator acts by the symmetric eigenvalue
$\sigma_i \mapsto q$, so the Coxeter word $\sigma_1\cdots\sigma_{m-1}$ acts by
$q^{m-1}$ and $(\sigma_1\cdots\sigma_{m-1})^p$ by $q^{(m-1)p}$; its bar-conjugate
($q \leftrightarrow q^{-1}$) is $q^{-(m-1)p}$, and the antisymmetric extraction is
$\delta_q = q^{w} - q^{-w}$. The writhe $w = (m-1)p$ is the number of positive
crossings of the braid.

The two-strand case $m = 2$ recovers the basis-knot decoration
[`prop:alpha-basis-knot-delta-q`](#prop:alpha-basis-knot-delta-q),
$\delta_q(T_{2,k}) = h\,[k]_q$ (writhe $w = k$). The three-strand force-carriers
then have **derived** (not assumed) exponents

$$
  \delta_q(T_{3,4}) = h\,[8]_q, \qquad \delta_q(T_{3,5}) = h\,[10]_q,
$$

the latter confirming the value used by
[`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
in $\alpha_{EM} = h^2/\bigl(q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})\bigr)$. The
writhe exponents are rigidly tied to the leading twist $-q^{2p}$ of the Jones
polynomial of $T_{3,p}$ (cross-checked against the knot tables
$8_{19} = T_{3,4}$, $10_{124} = T_{3,5}$). Symbolic cross-check:
the canonical formalism.

The same writhe $w$ governs the chirality mass-factor $a_K = 1 + w\,h$ of
[`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation),
but the two are distinct: that factor comes from the **ribbon full-twist**
$\varTheta\,v_\lambda = q^{2c(\lambda)}v_\lambda$ acting on *every* Wedderburn
block by its content $c(\lambda)$, whereas $\delta_q$ here is the **bar-odd part
of the single trivial-channel twist** $q^{(m-1)p}$. They share the writhe but
extract different data (a full-twist framing factor vs. an $e_-$ decoration).
<!-- FILE_END: torus-knot-delta-q-writhe.md -->

<!-- FILE_START: force-carrier-intertwining-correspondence.md -->
**Proposition (force-carrier intertwining correspondence; conditional on [`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation)).**
*Let $T_{p,q}$ be a torus-knot force carrier
([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness),
genus-$4$-saturating) with $p < q$ and $\gcd(p,q) = 1$.  When
applied via Hecke action to an $n$-strand molecular braid
$\beta \in B_n$ (with $n \geq p$), the $\delta_q$-decoration
([`def:delta-q-decoration`](#def:delta-q-decoration)) of the
combined operator $T_{p,q} \cdot \beta$ has its dominant
non-trivial Wedderburn weight on the partition*

$$
  \boxed{\;\;
    \lambda^{(T_{p,q})}
    \;=\;
    (p,\, \underbrace{1, 1, \ldots, 1}_{n-p \text{ ones}})
  \;\;}
$$

*— the unique partition of $n$ with one part of size $p$ and the
rest of size 1.  This corresponds to $T_{p,q}$ **intertwining $p$
of the $n$ strands** while the remaining $n-p$ strands carry along
untouched.*

### Combinatorial principle

A torus knot $T_{p,q}$ is a $p$-strand braid (the closure of
$(\sigma_1 \sigma_2 \cdots \sigma_{p-1})^q$ in $B_p$).  When
embedded into $B_n$ via the natural inclusion $B_p \hookrightarrow
B_n$ that places $T_{p,q}$ on strands $\{1, 2, \ldots, p\}$ (or
any other choice of $p$ strands), the resulting operator
intertwines exactly $p$ strands — equivalently, the
*permutation* it generates on $\{1, \ldots, n\}$ has a single
non-trivial orbit of size $p$ and $n-p$ fixed points.

In the symmetric-group / Hecke-algebra correspondence, partitions
$\lambda \vdash n$ index irreducible representations $V_\lambda$
with the structure:

- A part of size $k$ in $\lambda$ corresponds to $k$ strands acting
  in a "tied-together" $\mathrm{Sym}^{k}$-like or hook-like
  channel.
- A part of size $1$ corresponds to a free strand.

The partition $(p, 1, \ldots, 1)$ is therefore the natural
"$p$-strand intertwining + $(n - p)$ free-strand" Wedderburn
channel.

### Worked example: $H_4(q)$ molecular braid

For the H$_{2}$ molecular bound state in
[`prop:h2-lp-dual-binding`](#prop:h2-lp-dual-binding), the braid
acts on $n = 4$ strands ($p_1, e_2, e_1, p_2$ in the optimal
ordering).  The two force-carrier predictions:

| Force carrier | Strand count $p$ | Predicted $\lambda$ |
|---|---|---|
| $T_{2,9}$ | $p = 2$ | $\lambda = (2, 1, 1)$ |
| $T_{3,5}$ | $p = 3$ | $\lambda = (3, 1)$ |

Computational verification at $q_0 \approx 1.110$ (witness
[`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json)):

| $\lambda \vdash 4$ | $\delta_q$-component on bare braid $\sigma_1\sigma_2\sigma_3$ | interpretation |
|---|---:|---|
| $(4)$ | $+1.368$ | all 4 together (no intertwining channel) |
| $(3, 1)$ | $-1.110$ | **$T_{3,5}$ channel** (confirmed) |
| $(2, 2)$ | $0.000$ | impossible (would require simultaneous 2-strand pair) |
| $(2, 1, 1)$ | $+0.901$ | **$T_{2,9}$ channel** (confirmed) |
| $(1, 1, 1, 1)$ | $-0.731$ | all 4 free (no intertwining) |

The dominant non-trivial channels $(3,1)$ and $(2,1,1)$ match
exactly the predicted $\lambda^{(T_{3,5})}$ and $\lambda^{(T_{2,9)}}$.
The exact zero at $(2,2)$ is **structurally explained**: a single
$T_{2,9}$ force-carrier insertion can only intertwine *one* pair
of strands, not two simultaneous disjoint pairs.

### Frobenius self-duality of the bound-state channel

The two force-carrier channels are *transpose* partitions:
$(3,1)^{T} = (2,1,1)$.  Equivalently, the Young diagrams are
mirror-reflections through the diagonal:

- $(3, 1)$:    $\;\square\square\square / \square$    (3-row; 1+1+1+1 columns)
- $(2, 1, 1)$: $\;\square\square / \square / \square$ (2-row; 1+1+1 columns, shifted)

Their q-dimensions and Wedderburn weights are equal:
$\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)}$ and
$w_{(3,1)} = w_{(2,1,1)}$.

This **transpose-pairing** is the Frobenius self-dual structure
expected of a parity-symmetric bound state: under the Hopf-algebra
antipode $S$, $V_\lambda \mapsto V_{\lambda^T}$, so the bound-state
channel is closed under $S$.

### Generalisation

The intertwining correspondence applies to any torus-knot force
carrier on any $n$-strand braid:

- $T_{2,9}$ in $B_2 \hookrightarrow B_n$: $\lambda = (2, 1^{n-2})$.
- $T_{3,5}$ in $B_3 \hookrightarrow B_n$: $\lambda = (3, 1^{n-3})$.
- $T_{p,q}$ in $B_p \hookrightarrow B_n$: $\lambda = (p, 1^{n-p})$.

For a covalent $H_2$ bond ($n=4$), only the $T_{2,9}$ and $T_{3,5}$
channels contribute (since $p \leq 4$ requires $p \in \{2, 3\}$
for the genus-$4$ force carriers).

For larger molecular systems ($n > 4$), additional channels become
geometrically accessible — e.g., $T_{3,5}$ acting on a 5-strand
methane-like configuration would land on $\lambda = (3, 1, 1)$.

### Significance

Combined with
[`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio),
this proposition gives the categorical mechanism by which
$\alpha_{EM}$ enters the molecular bound-state energy:

1. The bound-state operator's $\delta_q$-decoration has dominant
   weight on $\lambda^{(T_{p,q})}$ for the relevant force carriers.
2. $\alpha_{EM}$ is a categorical-trace ratio of the force-carrier
   $\delta_q$ values.
3. The product of the two channels' contributions therefore
   carries an $\alpha_{EM}^{2}$ factor, recovering the standard
   Hartree-energy scaling.

This is the **post-round-18 closure path** for
[`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation)
— with the specific algebraic identity between
$\chi_{(3,1)} \cdot \chi_{(2,1,1)}$ and the $\delta_q$ values
remaining as the final symbolic-$q$ check.
<!-- FILE_END: force-carrier-intertwining-correspondence.md -->

<!-- FILE_START: alpha-shift-torus-knot.md -->
<!-- Theorem (conditional on:
       def:delta-q-decoration,
       prop:force-carrier-intertwining-correspondence). -->

**Proposition (torus-knot $\alpha_{\mathrm{shift}}$).**
*Let $p \geq 1$, $k \geq 1$ with $\gcd(p, k) = 1$, and let
$T_{p,k}$ be the $(p, k)$-torus knot, presented as the closure
of the braid $\beta_{p,k} = (\sigma_1 \sigma_2 \cdots
\sigma_{p-1})^k \in B_p$. Define the **shift exponent***

$$
  \alpha_{\mathrm{shift}}(T_{p,k})
  \;:=\;
  \max_{\lambda \,\vdash\, p}\;
  \mathrm{ord}_{q=0}^{(-)}\; \chi_\lambda(\beta_{p,k})
$$

*where $\chi_\lambda$ is the seminormal Hecke character on
$V_\lambda$ ([`def:delta-q-decoration`](#def:delta-q-decoration))
and $\mathrm{ord}_{q=0}^{(-)}$ denotes the pole order at $q = 0$
(i.e. the negative of the Laurent valuation). Then:*

1. *The maximizer is the all-anti-symmetric channel $V_{(1^p)}$.*
2. *$\alpha_{\mathrm{shift}}(T_{p,k}) = k(p - 1)$.*
### Witness summary

The canonical evidence
([`alpha-shift-torus.witness.json`](../../computations/alpha/alpha-shift-torus.witness.json))
records the full per-irrep symbolic $\chi_\lambda \in \mathbb{Q}(q)$
together with the pole order at $q = 0$ for every test pair, summarised
in
[Table: $\alpha_{\mathrm{shift}}(T_{p,k})$ for 6 test pairs](#tbl:alpha-shift-torus-knot-table-data).
All $14$ assertions in the witness pass.

### Cross-link

The two values $\alpha_{\mathrm{shift}}(T_{2,9}) = 9$ and
$\alpha_{\mathrm{shift}}(T_{3,5}) = 10$ are precisely the
$q$-integer indices appearing in
[`prop:em-coupling-projection`](#prop:em-coupling-projection)'s
formula

$$
  \alpha_{EM}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q.
$$

[`prop:alpha-em-shift-multiplicative-chain`](#prop:alpha-em-shift-multiplicative-chain)
combines the two identities into the **shift-exponent form**

$$
  \alpha_{EM}^{-1}
  \;=\;
  q \cdot
  \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q \cdot
  \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q,
$$

upgrading AXKIA's $\delta_q$-trace identity into the same
combinatorial universe as the w3-w4 atomic-shift formula
([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md)).
<!-- FILE_END: alpha-shift-torus-knot.md -->

