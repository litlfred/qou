The braid group $B_3$ acts on tensor products of the spin-$\tfrac{1}{2}$ representation $V = \mathbb{C}^2$ of $\mathcal{U}_q(\mathfrak{su}(2))$. The action on $V \otimes V$ is computed explicitly.

Choose the standard basis $\{e_1, e_2\}$ for $V$. The ordered basis for $V \otimes V$ is $\{e_1 \otimes e_1, e_1 \otimes e_2, e_2 \otimes e_1, e_2 \otimes e_2\}$. The braiding $\sigma \colon V \otimes V \to V \otimes V$ is the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$. It acts on basis vectors by:
$$
  \sigma(e_i \otimes e_j)
  = q^{\delta_{ij}} e_j \otimes e_i + (q - q^{-1})\delta_{i < j} e_i \otimes e_j.
$$
In the ordered basis, the $4 \times 4$ matrix is:
$$
  R = \begin{pmatrix}
    q & 0 & 0 & 0 \\
    0 & q - q^{-1} & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & q
  \end{pmatrix}.
$$

The tensor product decomposes into irreducible modules $V \otimes V =  \mathrm{Sym}^2_q(V) \oplus \Lambda^2_q(V)$. The symmetric (spin-1) part has dimension 3, spanned by $e_1 \otimes e_1$, $q^{-1/2} e_1 \otimes e_2 + q^{1/2} e_2 \otimes e_1$, and $e_2 \otimes e_2$. The antisymmetric (spin-0) part has dimension 1, spanned by $q^{1/2} e_1 \otimes e_2 - q^{-1/2} e_2 \otimes e_1$.

On each summand, the braiding $\sigma$ acts as a scalar. It acts as $q$ on the symmetric part (attractive/binding) and as $-q^{-1}$ on the antisymmetric part (repulsive). These are exactly the eigenvalues of the Iwahori--Hecke algebra generator $\sigma$, satisfying the Hecke relation $(\sigma - q)(\sigma + q^{-1}) = 0$.

The braid group $B_3$ acts on $V^{\otimes 3}$ by letting $\sigma_i$ braid the $i$-th and $(i+1)$-th factors using $R$. On $V \otimes V$, this representation factors through the Hecke algebra $H_2(R, q)$, meaning every braid word in $B_2$ reduces to a polynomial in $\sigma$.
