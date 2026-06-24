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

**Example: three socks.**

See [Table](#tbl:sorting-color-energy-table-data).

At $q = q_0$: sorting three fully reversed socks costs
$3 \times 2.011 = 6.033$ action units in the colour fibre.
This energy is not lost — it is stored in the gauge degrees
of freedom as the record of the observer's intent.
