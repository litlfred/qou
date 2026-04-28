**Proposition.**
*Let $\sigma_i$ be the Hecke generator
([R-matrix braiding](#rem:r-matrix-braiding)) acting on
$V \otimes V$, where $V$ is the fundamental representation.
Then:*

1. **(Eigenspace decomposition.)** *The R-matrix decomposes
   $V \otimes V$ into two eigenspaces:*

   $$
     V \otimes V
     = 
     \mathrm{Sym}^2(V)  \oplus  \textstyle\bigwedge^2(V)
   $$

   *with eigenvalues $q$ (symmetric, ordered) and $-q^{-1}$
   (antisymmetric, disordered) respectively.  These are the
   two roots of the Hecke relation
   $T^2 = (q - q^{-1})T + 1$.*

2. **(Sorting is projection.)** *A sorting operation —
   swapping two adjacent items into the correct order —
   is the projection from $\bigwedge^2(V)$ to
   $\mathrm{Sym}^2(V)$ at the generator $\sigma_i$.  This
   projection is the $\mathrm{Ad}$ component of the
   observation: it acts on the colour fibre by rotating
   the gauge degrees of freedom from the antisymmetric
   (disordered) to the symmetric (ordered) eigenspace.*

3. **(Energy per crossing.)** *The energy deposited in the
   colour fibre by one sorting operation is the eigenvalue
   gap:*

   $$
     \Delta E_{\mathrm{colour}}
     =  q - (-q^{-1})
     =  q + q^{-1}
   $$

   *At $q = q_0$: $\Delta E = 2.011$ action units per
   crossing.*

4. **(Total sorting energy.)** *Let $\pi \in S_n$ be a
   permutation representing the disordered state of $n$
   items.  The minimum number of adjacent transpositions
   (braid crossings) needed to sort $\pi$ is the inversion
   count $\mathrm{inv}(\pi)$.  The total energy deposited
   in the colour fibre is:*

   $$
     E_{\mathrm{colour}}(\pi)
     = 
     \mathrm{inv}(\pi) \cdot (q + q^{-1})
   $$

   *The worst case (reverse permutation) requires
   $\binom{n}{2}$ crossings; the identity requires zero.*

*Proof.*
(1) The Hecke relation $T^2 - (q - q^{-1})T - 1 = 0$
has roots $q$ and $-q^{-1}$ by the quadratic formula.  The
corresponding idempotents are:

$$
  e_+ = \frac{T + q^{-1}}{q + q^{-1}}, \qquad
  e_- = \frac{q - T}{q + q^{-1}}
$$

with $e_+ + e_- = 1$ and $e_+ e_- = 0$.  The image of $e_+$
is $\mathrm{Sym}^2(V)$ (the symmetric representation,
eigenvalue $q$); the image of $e_-$ is $\bigwedge^2(V)$
(the antisymmetric representation, eigenvalue $-q^{-1}$).

(2) A disordered pair occupies $\bigwedge^2(V)$: the two
items are in the wrong order, so the state is antisymmetric
under exchange.  Sorting swaps them into the correct order,
moving the state to $\mathrm{Sym}^2(V)$.  This is the
projection $e_+$.  In the observation
([observation](#def:observation)), $e_+$ is the
$\mathrm{Ad}$ component: it acts on the colour fibre by
conjugation, rotating the antisymmetric state to the
symmetric eigenspace.

(3) The energy deposited is the eigenvalue difference:
$q - (-q^{-1}) = q + q^{-1}$.

(4) Each adjacent transposition in the sorting algorithm
corresponds to one braid crossing $\sigma_i$.  The standard
result from combinatorics: the minimum number of adjacent
transpositions to realise $\pi$ equals $\mathrm{inv}(\pi)$,
the number of pairs $(i, j)$ with $i < j$ and
$\pi(i) > \pi(j)$.  Each crossing deposits
$q + q^{-1}$ in the colour fibre.  $\square$

**Example: three socks.**

| Permutation $\pi$ | $\mathrm{inv}(\pi)$ | Crossings | $E_{\mathrm{colour}}$ |
|:-:|:-:|:-:|:-:|
| $(1,2,3)$ sorted | $0$ | $0$ | $0$ |
| $(1,3,2)$ one swap | $1$ | $\sigma_2$ | $q + q^{-1}$ |
| $(2,1,3)$ one swap | $1$ | $\sigma_1$ | $q + q^{-1}$ |
| $(2,3,1)$ two swaps | $2$ | $\sigma_1 \sigma_2$ | $2(q + q^{-1})$ |
| $(3,1,2)$ two swaps | $2$ | $\sigma_2 \sigma_1$ | $2(q + q^{-1})$ |
| $(3,2,1)$ reverse | $3$ | $\sigma_1 \sigma_2 \sigma_1$ | $3(q + q^{-1})$ |

At $q = q_0$: sorting three fully reversed socks costs
$3 \times 2.011 = 6.033$ action units in the colour fibre.
This energy is not lost — it is stored in the gauge degrees
of freedom as the record of the observer's intent.
