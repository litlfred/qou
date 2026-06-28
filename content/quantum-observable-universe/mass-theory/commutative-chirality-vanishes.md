**Corollary** (of [Frobenius S-classification](#prop:frobenius-s-classification)
applied in the [commutative QOU](#def:commutative-qou) limit).
*In the commutative specialisation $q \to 1$, the chirality term
$H_A^2 \Phi_3$ in the Wedderburn mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) vanishes
identically:*

$$
  \lim_{q \to 1} H_A^2 \cdot \Phi_3 = 0.
$$

*Consequently the commutative atomic mass formula reduces to the
two-term expression*

$$
  \mathcal{M}^{\mathrm{class}}(Z, N) = Z\,\mathfrak{m}_{\mathfrak{p}} + N\,\mathfrak{m}_{\mathfrak{n}} + Z\,m_e + \alpha \bigl(\Phi_1 - 6\,\Phi_2\bigr),
$$

*where $\alpha = m_e \cdot 8G$ and $\lim_{q \to 1} [3]_q = 3$.*

*Proof.*
By [Frobenius S-classification](#prop:frobenius-s-classification),
$H_A = q - q^{-1}$ has $S$-eigenvalue $-1$, so
$H_A^2$ has eigenvalue $+1$. As $q \to 1$, $H_A \to 0$ continuously,
hence $H_A^2 \to 0$. The chirality functional
$\Phi_3 = \sum_i \log\lvert\chi^{\mathrm{sym}}_i / \chi^{\mathrm{alt}}_i\rvert$
remains finite (each per-factor ratio approaches $\pm 1$ classically;
the sum of logs approaches $0$ for any chain whose primitive factors
include at least one ud crossing, and it approaches a finite limit
otherwise). The product $H_A^2 \Phi_3 \to 0 \cdot \Phi_3 = 0$.

For the quantum 3-integer:
$\lim_{q \to 1}[3]_q = \lim_{q \to 1}(q^2 + 1 + q^{-2}) = 3$.
$\square$

**Companion reading.**
The crossing-energy interpretation of the commutative limit
([commutative crossing energy](#rem:commutative-crossing-energy))
shows that the same vanishing $H_A \to 0$ corresponds geometrically
to the unit-circle parameterisation $q = e^{i\varTheta}$, where the
crossing weight $q - q^{-1} = 2i\sin\varTheta$ becomes pure imaginary.
The two readings agree: the chirality channel collapses to zero in
the strict commutative limit, while a unit-circle deformation
recovers a non-trivial $\mathrm{U}(1)$ phase.

**Diagnostic application.**
The commutative limit provides a structural test: any feature of
the formula that persists as $q \to 1$ is independent of the
quantum deformation and lies in the underlying classical
representation theory. Numerical scan
([`commutative_case_diagnostic.py`](#)) confirms that the
proton--neutron mass splitting *vanishes* in the strict $q \to 1$
limit (consistent with the chirality channel being the unique
S-odd carrier), and that the wrong-sign binding for $Z = N$
fully-paired atoms (D, ${}^{4}\mathrm{He}$) is **not** a $q$-deformation artefact
but a structural feature of $\Phi_1$ in the symmetric group
algebra $\mathbb{C}[S_n] = H_n(1)$.
