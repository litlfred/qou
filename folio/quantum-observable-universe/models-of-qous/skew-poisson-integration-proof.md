The proof of Theorem 3.7 in Leitner (arXiv:math/0602138) has two parts.

1. **Bialgebra structure.** Theorem 1.9 shows that $U \cong \bigotimes_i A_i$ as $k$-modules for a fixed ordering of the index set. Its proof exhibits a Gröbner basis of the defining ideal, made of the relations $f_{i,j}$ of the $A_i$ and the elements $g_{a,b} = ab - ba - \tilde\pi(a, b)$; this step uses only that $\pi$ is strongly filtered. Proposition 1.13 then uses strong multiplicativity to show that $\Delta$ vanishes on the $g_{a,b}$, so the comultiplication descends to an algebra map $U \to U \otimes U$.
2. **Divided-power structure.** With the bialgebra structure in hand, the proof writes $\Delta$ on ordered monomials $\delta_x^J$ using Remark 3.2 and checks that $U$ carries the DVPS structure of a distribution algebra.

The Lean declaration `QOU.FormalGroups.integrationMk_commutator` formalises only the defining relation of $U$: in the quotient, the image of $fg - gf$ equals the image of $\pi(f, g)$. This relation holds by construction for any bilinear bracket. Neither part of the proof above is formalised.
