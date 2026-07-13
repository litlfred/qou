*Proof.*
The dihedral relations hold by inspection. The orbit of $\varphi$ under $\langle \sigma \rangle$ is the set $\{\sigma^k \varphi : k = 0, 1, 2, 3\} = \{\varphi, i\varphi, -\varphi, -i\varphi\}$. Acting by $\tau$ yields the reciprocals $\{1/\varphi, -i/\varphi, -1/\varphi, i/\varphi\}$. This generates the full octet $G_8$. Since $|D_4| = 8$ and $|G_8| = 8$, the action is transitive, and the stabilizer of each element is trivial.

For the polynomial, $P(z/i) = P(-iz) = z^4 + 3z^2 + 1$. The product is a difference of squares:

$$
  (z^4 - 3z^2 + 1)(z^4 + 3z^2 + 1)
   =  (z^4 + 1)^2 - (3z^2)^2
   =  z^8 - 7z^4 + 1.  \quad\square
$$

**Real subgroup.**
The subgroup of $D_4$ preserving the real axis $\mathbb{R}^\times \subset \mathbb{C}^\times$ is

$$
  D_4^{\mathbb{R}}
   =  \langle\,\sigma^2,\,\tau\,\rangle
   =  \langle\,-1,\;q \mapsto q^{-1}\,\rangle
   \cong  \mathbb{Z}/2 \times \mathbb{Z}/2.
$$

Its orbit through $\varphi$ is the real golden quartet $Q$. The full $D_4$ extends this orbit via imaginary $\sigma$-rotations.

**Möbius lifts to $\mathrm{GL}_2(\mathbb{Z}[i])$.**
The baryon integration-limit Möbius matrix

$$
  M  =  \begin{pmatrix} -1 & 4 \\ 4 & 3 \end{pmatrix} \in \mathrm{GL}_2(\mathbb{Z})
$$

acts on $\mathbb{CP}^1(\mathbb{C})$, fixing the real golden pair $\{1/\varphi, -\varphi\}$. Under conjugation by $S = \mathrm{diag}(i, 1) \in \mathrm{GL}_2(\mathbb{Z}[i])$, which realises $\sigma\colon q \mapsto iq$, the conjugate is

$$
  M^\sigma  :=  S^{-1} M S
   =  \begin{pmatrix} -1 & -4i \\ 4i & 3 \end{pmatrix}
   \in  \mathrm{GL}_2(\mathbb{Z}[i]).
$$

This matrix fixes the $i$-rotated golden pair $\{i/\varphi, -i\varphi\}$. Its bar conjugate fixes $\{i\varphi, -i/\varphi\}$. The four matrices

$$
  \{\,M,\;M',\;M^\sigma,\;M'^\sigma\,\}
$$

fix the full golden octet $G_8$. Each matrix fixes exactly one coset of $G_8$. Thus $\mathbb{Z}[i]$ is the natural ring of definition for the Möbius family. The four transformations form a $D_4$-equivariant family on $\mathrm{GL}_2(\mathbb{Z}[i])$, with $M, M' \in \mathrm{GL}_2(\mathbb{Z})$ as the real-axis elements.

**Unit circle.**
The group $D_4$ acts on the unit circle $|q| = 1$. From $\zeta_8 = e^{i\pi/4}$, the orbit is

$$
  D_4 \cdot \zeta_8
   =  \{\,\zeta_8,\,\zeta_8^3,\,\zeta_8^5,\,\zeta_8^7\,\}.
$$

These primitive eighth roots of unity lie outside $G_8$, but inhabit the same $D_4$-symmetric structure. Together, $G_8 \cup \{\zeta_8\text{-orbit}\}$ form the full $D_4$-fixed locus on $\mathbb{C}^\times$:

| Orbit type | Representative | Stabilizer | Orbit size |
|------------|---------------|------------|------------|
| Real golden | $\varphi$ | trivial | 8 (= $G_8$) |
| Unit-circle $\zeta_8$ | $\zeta_8$ | $\langle\sigma\tau\rangle$ | 4 |
| Real $± 1$ | $1$ | $\langle\tau\rangle$ | 4 (= 4th roots) |
| Origin / infinity | $0$, $\infty$ | $D_4$ | 1 each |

The coordinates $q$ and $i$ govern the structure: $q$ generates radial motion, while $i$ generates the $\sigma$-rotation connecting rays.
