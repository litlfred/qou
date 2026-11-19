### Proof — bar-eigenspace argument

**Step 1 (which involution transposes $\lambda$).** The bar involution does
**not** transpose cells. It fixes every central primitive idempotent:

$$
  \mathrm{bar}(e_\lambda) \;=\; e_\lambda .
$$

Bar is a ring automorphism of $H_n(q)$, so it permutes the $e_\lambda$. At
$q = 1$ it is $T_w \mapsto T_{w^{-1}}^{-1} = T_w$, the identity, and the
permutation is locally constant in $q$, so it is the identity. Explicitly in
$H_2$ (with $\sigma^{-1} = \sigma - h$, $h = q - q^{-1}$),
$e_{(2)} = (\sigma + q^{-1})/(q + q^{-1})$ maps to
$(\sigma - h + q)/(q^{-1} + q) = e_{(2)}$.

The involution that transposes is the Goldman involution
$\sigma_i \mapsto -\sigma_i^{-1}$, which is $q$-linear and at $q = 1$ is
tensoring with the sign character:

$$
  \#(e_\lambda) \;=\; e_{\lambda'} .
$$

In $H_2$, $\#(e_{(2)}) = (-\sigma + h + q^{-1})/(q + q^{-1}) = (q - \sigma)/(q + q^{-1}) = e_{(1,1)}$.
Writing $\mathrm{bar}(e_\lambda) = e_{\lambda'}$ instead would be false. Steps 2 and 3 below use the transposing involution, so read
"bar" there as $\#$ on the Hecke side.

**Step 2 (period-class bar-action).** Under the archimedean
realization functor $\tau_{\mathrm{arch}}$
([archimedean-realization-functor definition](#def:archimedean-realization-functor)),
the bar involution acts on the period side by:

- **Hyperbolic volume**: $\mathrm{Vol}(K) = \mathrm{Vol}(\overline{K})$
 — bar-INVARIANT (orientation-reversal preserves the metric).
 Lives in $\mathcal{P}_2^+$ (real, bar-fixed).
- **Chern–Simons**: $\mathrm{CS}(K) = -\mathrm{CS}(\overline{K})$ mod
 $\pi^2 \mathbb{Z}$ — bar-ANTI-INVARIANT (CS picks up the
 orientation sign). Lives in $\mathcal{P}_3^-$ (Tate-twisted).

These are the two characteristic period-class bar-types at depths 2
and 3 respectively.

**Step 3 (pairing analysis).**

*Self-conjugate case $\lambda = \lambda'$.* $\#(e_\lambda) =
e_\lambda$ — the cell is $\#$-fixed. Pairing with a depth-$n$ grouplike
$g \in G^{(n)}(\mathcal{H}_q)$ under Markov trace yields a value in
the bar-fixed component of $\mathcal{P}_n / \mathcal{P}_{n - 1}$:

- At $n = 2$: pairs with $\mathrm{Vol}$ (bar-fixed), which can be non-zero.
- At $n = 3$: pairs with $\mathrm{CS}$ (bar-anti-fixed) — gives zero
 on bar-fixed cells.

So bar-fixed cell $\Rightarrow$ $d_{\mathrm{II}}(\lambda) = 2$.

*Chiral pair case $\lambda \neq \lambda'$.* $\#(e_\lambda) =
e_{\lambda'}$ — $\#$ swaps the two cells, so $e_\lambda$ itself is not an
eigenvector: it is the sum of its symmetric and antisymmetric parts below,
both nonzero. The bar-eigenspaces of the
direct sum $e_\lambda + e_{\lambda'}$ decompose as:

- Bar-symmetric: $(e_\lambda + e_{\lambda'})/2$ — pairs with depth-2
 (Vol-type) periods.
- Bar-antisymmetric: $(e_\lambda - e_{\lambda'})/2$ — pairs with
 depth-3 (CS-type) periods, if the matching holds.

The bar-symmetric part pairs by definition with depth-2 of a chiral knot
(volume can be non-zero, but in the chiral pair the antisymmetric
content carries the orientation-dependent signature). The
bar-antisymmetric part is the natural pairing partner of
$\mathrm{CS}$ (which is bar-anti-invariant).

So chiral pair $\Rightarrow$ $d_{\mathrm{II}}(\lambda) = 3$.

**What this argument does not prove.** Steps 2 and 3 assume that $\#$ on the
Hecke side matches orientation reversal on the period side, and that "pairing
with a depth-$n$ grouplike" lands in the matching eigenspace. Neither is proved
here, and $d_{\mathrm{II}}$ itself is defined only through
[two-filtration-bridge conjecture](#conj:two-filtration-bridge). The argument is
therefore a heuristic, conditional on that conjecture and on this matching. The
part that is a theorem is item 4 of
[cellular-depth-filtration proposition](#prop:cellular-depth-filtration): under
(H-match) and (H-parity) it gives the vanishing and antisymmetry of odd-depth
components, but not the non-vanishing that the values $2$ and $3$ require.
Assigning a single depth to a chiral cell is not forced, because $e_\lambda$
carries both a symmetric and an antisymmetric part.

### Generality of the proof

The argument is *structural*, not case-by-case:

1. **No upper bound on $n$.** Works for partitions of any size.
2. **Bar-class of $\lambda$ is computable.** Self-conjugate partitions
 of $n$ are exactly those with bar-fixed Young diagram (a
 well-defined combinatorial property).
3. **Depth assignment is binary by definition.** The values 2 and 3 come
 from the definition of $d_{\mathrm{II}}$, whose third branch is empty.

See [Table](#tbl:two-filtration-bridge-general-table-data).

(Self-conjugate partitions of $n$ are in bijection with partitions of
$n$ into distinct odd parts — a classical result.)
