Let $V = \mathbb{C}^2$ be the fundamental representation of $\mathfrak{sl}_2$ with basis $e, f, h$, and let $\Omega = e \otimes f + f \otimes e + \tfrac{1}{2}\, h \otimes h$ be the split Casimir. For $n \geq 2$ let $X_n = \{(z_1, \dots, z_n) \in \mathbb{C}^n : z_i \neq z_j \text{ for } i \neq j\}$ be the configuration space of $n$ distinct points, and for $i < j$ let $\Omega_{ij}$ be $\Omega$ acting in tensor slots $i$ and $j$ of $V^{\otimes n}$.

The **Knizhnik--Zamolodchikov connection** with coupling $\lambda \in \mathbb{C}$ is the connection on the trivial bundle $X_n \times V^{\otimes n}$ given by

$$
  \nabla = d - \lambda\, \omega,
  \qquad
  \omega = \sum_{i<j} \Omega_{ij}\, d\log(z_i - z_j).
$$

On $V \otimes V$ the split Casimir equals $P - \tfrac{1}{2}$, where $P$ is the flip of the two factors: it acts by $\tfrac{1}{2}$ on the triplet, where $P = 1$, and by $-\tfrac{3}{2}$ on the singlet, where $P = -1$. Hence

$$
  \Omega_{ij} = s_{ij} - \tfrac{1}{2},
$$

where $s_{ij}$ permutes tensor factors $i$ and $j$. The residues are therefore images of the elements $(i\,j) - \tfrac{1}{2}$ of the group algebra $R[S_n]$, and the statements below hold over any commutative ring $R$.

A logarithmic connection $\omega = \sum_{i<j} M_{ij}\, d\log(z_i - z_j)$ is **flat** if $d\omega - \omega \wedge \omega = 0$. Since $d\omega = 0$, and the forms $d\log(z_i - z_j)$ satisfy the Arnold relation, flatness is equivalent to the **infinitesimal pure braid relations** [kohno1987]. For three points both directions of this equivalence are proved, using the Arnold relation $\omega_{12}\wedge\omega_{23}+\omega_{23}\wedge\omega_{31}+\omega_{31}\wedge\omega_{12}=0$:

$$
  [M_{ij}, M_{kl}] = 0 \quad \text{if } \{i,j\} \cap \{k,l\} = \varnothing,
  \qquad
  [M_{ij}, M_{ik} + M_{jk}] = 0 \quad \text{if } i, j, k \text{ are distinct}.
$$

The Knizhnik--Zamolodchikov residues satisfy both relations. The central scalar $\tfrac{1}{2}$ drops out of every commutator, and the remaining identities follow from conjugating transpositions: $s_{ij}\, s_{ik} = s_{jk}\, s_{ij}$ and $s_{ij}\, s_{jk} = s_{ik}\, s_{ij}$. The relations constrain the residues: on three points, the family $M_{12} = s_{12}$, $M_{13} = s_{23}$, $M_{23} = 0$ violates the second relation, since $s_{12}s_{23} \neq s_{23}s_{12}$.

Integrating $\nabla$ along loops in $X_n$ gives a representation of the pure braid group $P_n$ on $V^{\otimes n}$. Composed with the flip, it extends to the braid group $B_n$. This is the representation that Kohno's theorem [kohno1987] and Drinfeld's theorem [drinfeld1991] compare with the Jimbo $R$-matrix representation at $q = e^{i\pi\lambda}$.
