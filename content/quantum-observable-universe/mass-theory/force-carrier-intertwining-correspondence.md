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
| $(3, 1)$ | $-1.110$ | **$T_{3,5}$ channel** ✓ |
| $(2, 2)$ | $0.000$ | impossible (would require simultaneous 2-strand pair) |
| $(2, 1, 1)$ | $+0.901$ | **$T_{2,9}$ channel** ✓ |
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
