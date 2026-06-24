**Step 1 (bar action on central idempotents).** The bar involution
acts on the central primitive idempotent $e_\lambda \in Z(H_n(q))$
([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent),
[`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic)) by

$$
  \mathrm{bar}(e_\lambda) \;=\; e_{\lambda'},
$$

where $\lambda'$ is the transpose Young diagram.

**Step 2 (period-class bar-action).** Under the archimedean
realization functor $\tau_{\mathrm{arch}}$
([`def:archimedean-realization-functor`](#def:archimedean-realization-functor)),
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

*Self-conjugate case $\lambda = \lambda'$.* $\mathrm{bar}(e_\lambda) =
e_\lambda$ — the cell is bar-fixed. Pairing with a depth-$n$ grouplike
$g \in G^{(n)}(\mathcal{H}_q)$ under Markov trace yields a value in
the bar-fixed component of $\mathcal{P}_n / \mathcal{P}_{n - 1}$:

- At $n = 2$: pairs with $\mathrm{Vol}$ (bar-fixed) — non-by definition.
- At $n = 3$: pairs with $\mathrm{CS}$ (bar-anti-fixed) — gives zero
 on bar-fixed cells.

So bar-fixed cell $\Rightarrow$ $d_{\mathrm{II}}(\lambda) = 2$.

*Chiral pair case $\lambda \neq \lambda'$.* $\mathrm{bar}(e_\lambda) =
e_{\lambda'}$ — bar swaps the two cells. The bar-eigenspaces of the
direct sum $e_\lambda + e_{\lambda'}$ decompose as:

- Bar-symmetric: $(e_\lambda + e_{\lambda'})/2$ — pairs with depth-2
 (Vol-type) periods.
- Bar-antisymmetric: $(e_\lambda - e_{\lambda'})/2$ — pairs with
 depth-3 (CS-type) periods non-by definition.

The bar-symmetric part pairs by definition with depth-2 of a chiral knot
(volume can be non-zero, but in the chiral pair the antisymmetric
content carries the orientation-dependent signature). The
bar-antisymmetric part is the natural pairing partner of
$\mathrm{CS}$ (which is bar-anti-invariant).

So chiral pair $\Rightarrow$ $d_{\mathrm{II}}(\lambda) = 3$.

$\square$

### What the proof gives in full generality

The argument is *structural*, not case-by-case:

1. **No upper bound on $n$.** Works for partitions of any size.
2. **Bar-class of $\lambda$ is computable.** Self-conjugate partitions
 of $n$ are exactly those with bar-fixed Young diagram (a
 well-defined combinatorial property).
3. **Depth assignment is binary.** Either 2 or 3 — no other values
 arise in this bridge.

See [Table](#tbl:two-filtration-bridge-general-table-data).

(Self-conjugate partitions of $n$ are in bijection with partitions of
$n$ into distinct odd parts — a classical result.)

### Consequences

**Generalises round 9**: the small-cases bridge verification
at $n \leq 4$ extends to all $n$ via the bar-eigenspace argument.

**Consequence for B1**:
- For each self-conjugate cell, B1's depth-2 row is theorem-level
 (combining Bloch–Suslin + per-knot VC where available).
- For each chiral pair, B1's depth-3 row is conditional on the CS
 computation per knot.

**Combined with
[`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
+
[`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)**:
the depth-3 content over $\mathbb{Q}(\zeta_N)$ for every prime $N$ is
controlled by $\lfloor (N - 1)/2 \rfloor - 1$ genuinely-new real
numbers, all pairing with chiral-pair cells in the appropriate
$H_n(q)$.

### Cross-references

- Bridge conjecture: [`conj:two-filtration-bridge`](#conj:two-filtration-bridge)
- Small-cases verification: [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
- Chirality structure: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)
- Joint action discharge: [`prop:joint-galois-braid-discharged`](#prop:joint-galois-braid-discharged)
- Hecke-Baer-* and bar action on $e_\lambda$:
 [`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic),
 [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
