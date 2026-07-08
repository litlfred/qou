<!-- FILE_START: braid-symmetric-intro.md -->
Having established their categorical origin, we now provide explicit presentations and representations of the braid group.
<!-- FILE_END: braid-symmetric-intro.md -->

<!-- FILE_START: braid-group.md -->
The **braid group on three strands** has the presentation:
```tex
\begin{equation}\label{eq:braid-presentation}
  B_3
  =\bigl\langle\sigma_1,\sigma_2
     \big| \sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2\bigr\rangle.
\end{equation}
```
This is the fundamental group of the configuration space of three unordered points in the plane. It is isomorphic to the fundamental group of the trefoil knot complement.
<!-- FILE_END: braid-group.md -->

<!-- FILE_START: braid-group-su2.md -->
The braid group $B_3$ acts on tensor products of the spin-$\tfrac{1}{2}$ representation $V = \mathbb{C}^2$ of $\mathcal{U}_q(\mathfrak{su}(2))$. We explicitly compute the action on $V \otimes V$.

Choose the standard basis $\{e_1, e_2\}$ for $V$. The ordered basis for $V \otimes V$ is $\{e_1 \otimes e_1, e_1 \otimes e_2, e_2 \otimes e_1, e_2 \otimes e_2\}$. The braiding $\sigma \colon V \otimes V \to V \otimes V$ is the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$. It acts on basis vectors by:
$$
  \sigma(e_i \otimes e_j)
  = q^{\delta_{ij}} e_j \otimes e_i
  + (q - q^{-1})\delta_{i < j} e_i \otimes e_j.
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

The tensor product decomposes into irreducible modules $V \otimes V =  \mathrm{Sym}^2_q(V) \oplus \Lambda^2_q(V)$. The symmetric (spin-1) part has dimension 3, spanned by $e_1 \otimes e_1$, $q^{1/2} e_1 \otimes e_2 + q^{-1/2} e_2 \otimes e_1$, and $e_2 \otimes e_2$. The antisymmetric (spin-0) part has dimension 1, spanned by $q^{1/2} e_1 \otimes e_2 - q^{-1/2} e_2 \otimes e_1$.

On each summand, the braiding $\sigma$ acts as a scalar. It acts as $q$ on the symmetric part (attractive/binding) and as $-q^{-1}$ on the antisymmetric part (repulsive). These are exactly the eigenvalues of the Iwahori--Hecke algebra generator $T = \sigma$, satisfying the Hecke relation $(T - q)(T + q^{-1}) = 0$.

The braid group $B_3$ acts on $V^{\otimes 3}$ by letting $\sigma_i$ braid the $i$-th and $(i+1)$-th factors using $R$. On $V \otimes V$, this representation factors through the Hecke algebra $H_2(R, q)$, meaning every braid word in $B_2$ reduces to a polynomial in $T$.
<!-- FILE_END: braid-group-su2.md -->

<!-- FILE_START: knot-notation-convention.md -->
Particles in this framework are identified with their knots. We write $\mathfrak{K}_x^{\pm}$, where $x$ designates the particle and $\pm$ designates the knot's chirality. The superscript distinguishes a particle from its antiparticle via mirror reflection (charge conjugation).

See [Table 1](#tbl:knot-notation-convention-table1-data).

The sign convention assigns $\mathfrak{K}_e^- = T_{2,3}$ to the electron and $\mathfrak{K}_e^+ = T_{2,3}^{\sigma}$ to the positron. For amphichiral knots like $\mathfrak{K}_\mu$ and $\mathfrak{K}_\gamma$, the sign is trivial since $K \cong K^{\sigma}$. 

While the unknot $\mathfrak{K}_\nu$ is amphichiral unoriented, the left-handed neutrino $\nu_L$ and right-handed antineutrino $\nu_R^{\sigma}$ are distinguished by framing rather than knot type.

We denote torus knots by $T_{m,n}$, with mirror image $T_{m,n}^{\sigma} = T_{m,-n}$.

See [Table 2](#tbl:knot-notation-convention-table2-data).

The connected sum is $\mathfrak{K}_1 \mathbin{\#} \mathfrak{K}_2$. A hadron is written $[\mathfrak{K}_1, \mathfrak{K}_2, \mathfrak{K}_3]_p \oplus \mathcal{L}_H$, where the subscript designates colour-tube coupling and $\oplus$ denotes linking. The proton is:
$$
  \mathfrak{p} = [\mathfrak{K}_u, \mathfrak{K}_u, \mathfrak{K}_d]_p
  \oplus \mathcal{L}_H.
$$

We use $\sigma_i$ for both the braid generator and its image in $H_n(R, q)$, which satisfies $\sigma_i^{2} = (q - q^{-1})\sigma_i + 1$. The Jones polynomial is always denoted $J_K(q)$. Topological masses are evaluated via $\mathfrak{m}(K) = \mathrm{Vol}(K) / \hbar_q^{2}$, where $\hbar_q = 1 - q^{-1}$.
<!-- FILE_END: knot-notation-convention.md -->

<!-- FILE_START: fundamental-knots-operator-basis.md -->
The framework's particle catalogue and operator algebra share a single six-element basis. Fundamentally, each particle is a knot or link on Bring's surface. Interaction operators form the six-dimensional Iwahori--Hecke algebra $H_3(q)$.

| Particle | Knot / link | Type | Braid word | $q$-invariant |
|---|---|---|---|---|
| neutrino $\nu$ | unknot $0_1$ | trivial | $\mathbf{1}$ | $\mathrm{Vol}=0$, $J=1$ |
| electron $e^-$ | trefoil $3_1 = T(2,3)$ | torus | $\sigma_1^3$ | $\mathrm{Vol}=0$ |
| strong force | Hopf link $L2a1 = T(2,2)$ | torus | $\sigma_1^2$ | $\mathrm{Vol}=0$ |
| Higgs $h$ | figure-eight $4_1$ | hyperbolic | $(\sigma_1\sigma_2^{-1})^2$ | $\mathrm{Vol}\approx 2.0299$ |
| nucleon $\mathfrak{p},\mathfrak{n}$ | Borromean rings $L6a4$ | hyperbolic | $(\sigma_1\sigma_2^{-1})^3$ | $\mathrm{Vol}\approx 7.328 = 8G$ |
| photon $\gamma$ | — (not a knot) | Hecke element | $\mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ | $J=1$ (bare) |

Torus knots carry zero hyperbolic volume, representing the massless, force-carrying sector. Hyperbolic knots carry positive volume, which translates to mass via $\mathrm{Vol}(K)/\hbar_q^{2}$. The photon is not a knot but a four-term element of $H_3(q)$ whose products generate the rest of the spectrum.

The six Gröbner--Shirshov normal-form words span $H_3(q)$:

| Operator | Braid word | Permutation | $\mathrm{tr}_M$ at $q_0$ |
|---|---|---|---|
| $\gamma$ (identity) | $\varnothing$ | $e$ | $1.000$ |
| $\sigma_0$ | $(0)$ | $(1\;2)$ | $0.499$ |
| $\sigma_1$ | $(1)$ | $(2\;3)$ | $0.499$ |
| $L_+$ | $(0,1)$ | $(1\;2\;3)$ | $0.249$ |
| $L_-$ | $(1,0)$ | $(1\;3\;2)$ | $0.249$ |
| $e^-$ | $(0,1,0)$ | $(1\;3)$ | $0.551$ |

These basis operators are algebraically distinct from the topological knots sharing their names. Their Markov traces at the substrate parameter $q_0$ provide the exact weights used for mass and binding computations.
<!-- FILE_END: fundamental-knots-operator-basis.md -->

