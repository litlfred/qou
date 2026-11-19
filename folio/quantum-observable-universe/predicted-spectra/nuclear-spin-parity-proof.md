*Proof.*
Each nucleon—proton $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ or neutron $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$—is a knot (a single-component link closure of the Borromean braid). Knots carry half-integral spin; links carry integral spin.

The nuclear link $\mathcal{N}(Z, N)$ is a satellite of $A$ Borromean knots joined by Hopf links. In $\mathrm{SU}_q(2)$ representation theory, the tensor product of $A$ spin-$\tfrac{1}{2}$ representations decomposes as:

$$
  \left(\tfrac{1}{2}\right)^{\otimes A}
  = 
  \bigoplus_{J = J_{\min}}^{A/2} V_J^{\oplus m_J}
$$

Here, $J_{\min} = 0$ for even $A$ and $J_{\min} = \tfrac{1}{2}$ for odd $A$. Every summand $V_J$ shares the parity ($J \bmod 1$) of $A/2 \bmod 1$. This standard result holds for all $q > 0$. The $q$-deformation preserves the spin parity of tensor products.

Explicitly, the $q$-Clebsch--Gordan decomposition $V_{1/2} \otimes V_J = V_{J+1/2} \oplus V_{J-1/2}$ (for $J \geq 1/2$) adds $\tfrac{1}{2}$ at each step. After $A$ tensor factors, the spin parity equals $A/2 \bmod 1$. $\square$

**The braid group perspective.**
In the braid group $B_A$, the writhe $w(\beta)$ of the standard nuclear braid representative has parity:

$$
  w(\beta) \equiv \binom{A}{2} \pmod{2}.
$$

Writhe parity determines statistics:
- $w$ even $\Leftrightarrow$ bosonic statistics $\Leftrightarrow$ $J \in \mathbb{Z}$.
- $w$ odd $\Leftrightarrow$ fermionic statistics $\Leftrightarrow$ $J \in \mathbb{Z} + \tfrac{1}{2}$.

Since $\binom{A}{2} = A(A-1)/2$, the writhe is even if and only if $A \equiv 0$ or $1 \pmod{4}$. However, the $q$-deformed spin-statistics theorem follows directly from representation theory, independent of writhe.

**The Jones--Wenzl projector.**
In the Temperley--Lieb algebra $TL_A(\delta)$ with $\delta = -(q^{1/2} + q^{-1/2})$, the Jones--Wenzl projector $p_A$ projects onto the highest-weight irreducible representation $V_{A/2}$. The embedding of the nuclear link in the TL algebra and the action of $p_A$ determine the ground state spin.

For ${}^{14}\mathrm{N}$ ($A = 14$, even), the ground state has $J = 1$. The projector $p_{14}$ projects onto $V_7$, but the nuclear link's embedding selects the $J = 1$ subrepresentation via the coupling pattern of 7 protons and 7 neutrons.

**Key examples.**
See [Table](#tbl:nuclear-spin-parity-table-data).

The integer spin ($J = 1$) of ${}^{14}\mathrm{N}$ ruled out the pre-1932 proton-electron nuclear model, which predicted 21 fermions (14 protons, 7 electrons) and half-integer spin. Neutrons as spin-$\tfrac{1}{2}$ particles resolved this, giving 14 nucleons and integer spin.

Within the categorical knot model, this parity follows automatically. Both the proton and neutron are spin-$\tfrac{1}{2}$ knots. They share the Borromean topology but differ in quark colouring. Thus, 14 half-integer spins couple to an integer total spin.
