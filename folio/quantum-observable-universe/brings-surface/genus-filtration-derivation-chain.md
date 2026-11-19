The chain from the algebra to Bring's surface runs:

1. **QOU axioms** give $G = \mathrm{SU}_q(2)$ with braiding on $V_1^{\otimes n}$, producing $H_n(q)$.
2. **Strand count closure**: Only $m \in \{2, 3\}$ contribute new torus knots. The algebra is $H_2(q) \oplus H_3(q)$, with $5$ irreps.
3. **Hecke completeness**: The evaluation matrix must have rank $5$, which first occurs at $g = 4$.
4. **Chebyshev overflow**: At $g = 4$, $a_9$ fits (degree $4$), and $a_{11}$ overflows (degree $5$).
5. **Ideal**: The genus-filtration ideal $\mathfrak{I}_4 = (u^5)$ kills $T_{2,p}$ for $p \geq 11$.
6. **Yekutieli**: The leading coefficient $c_{g+1} = 1$ yields a nonzero obstruction via $d_q^2 \neq 0$.
7. **Bring surface**: $\Sigma_4$ is the unique genus-$4$ curve with maximal symmetry ($S_5$), fixed by $\chi_{\mathrm{eu}}(M_0) = -6$.

**Step 3 does not hold, so the chain does not deliver the genus.** The evaluation matrix is block-diagonal — a $T_{r,s}$ is a closure on $r$ strands and so evaluates only in the $H_r(q)$ columns — and at $g = 4$ its rank is at most $2 + 2 = 4$, for every $q$ ([the block-rank remark](#rem:torus-evaluation-block-rank)). What step 3 can support is the weaker *count* statement: $g = 4$ is the least genus at which the number of embeddable $T_{r,s}$, $r \in \{2,3\}$, reaches the five irreducibles. A count of five vectors is not a spanning set, so steps 4 through 7 take $g = 4$ as given rather than receiving it from step 2.

**Unconditional establishment of step 1 independently of $\chi$.** The QOU volume axiom $\Lambda^2 V \cong \mathbf{1}$, together with the dagger condition and $\det = 1$, forces $\dim V = 2$ and $G \subseteq \mathrm{SU}(2)$ — with no Euler characteristic, genus, or reference to Bring's surface anywhere in the argument. So step 1 is not a place where $\chi = -6$ re-enters, and the chain is not circular *there*. It is instead incomplete at step 3.

**Consequently Bring's surface enters as an input to the chain rather than emerging as a consequence of it.** With step 3 unavailable, nothing in steps 1 and 2 selects genus $4$, and Bring's surface enters through the genus rather than being produced by it.
