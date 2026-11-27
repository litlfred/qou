*One-dimensional characters.* A one-dimensional character sends every $\sigma_i$ to the same eigenvalue $\epsilon$, either $q$ or $-q^{-1}$. Then $\sigma_i^{-1} \mapsto \epsilon^{-1}$, and $\epsilon^{-1}(q) = \epsilon(q^{-1})$ in both cases, since $q^{-1} = q^{-1}$ and $(-q^{-1})^{-1} = -q = -(q^{-1})^{-1}$. So $\chi(C\beta)(q) = \chi(\beta)(q^{-1})$ for every word.

*The representation $(2,1)$ of $H_3(q)$.* Take
$$
  \sigma_0 \mapsto \begin{pmatrix} -q^{-1} & q \\ 0 & q \end{pmatrix},\qquad
  \sigma_1 \mapsto \begin{pmatrix} q & 0 \\ q^{-1} & -q^{-1} \end{pmatrix},
$$
which is $q$ times the reduced Burau matrices at $t = q^{-2}$. Write $\rho_q$ for this representation. The matrix $P = \mathrm{diag}(1, q^2)$ satisfies
$$
  P\,\rho_q(\sigma_i^{-1}) = \rho_{q^{-1}}(\sigma_i)\,P
  \quad\text{and}\quad
  P\,\rho_q(\sigma_i) = \rho_{q^{-1}}(\sigma_i^{-1})\,P
$$
for $i = 0, 1$. By induction on the length of a word, $P\,\rho_q(C\beta)\,P^{-1} = \rho_{q^{-1}}(\beta)$ for every braid word $\beta$, and taking traces gives the identity. $\square$

The $(2,1)$ identity holds for every braid word over any field with $q \ne 0$.

**Remark (extension to every $n$).** The same identity holds for every irreducible character of $H_n(q)$. Let $K = \mathbb{Q}(q)$ and let $\iota$ be the ring involution of $H_n(q)$ that sends $q \mapsto q^{-1}$ and $\sigma_i \mapsto \sigma_i^{-1}$. It is well defined because inverting every letter preserves the braid relations, and the quadratic relation $\sigma_i^2 = h\sigma_i + 1$ becomes $\sigma_i^{-2} = -h\,\sigma_i^{-1} + 1$, which is the same relation multiplied by $\sigma_i^{-2}$. For an irreducible representation $\rho$ with character $\chi^\lambda$, set $\rho'(x) = \overline{\rho(\iota(x))}$, where the outer bar applies $q \mapsto q^{-1}$ to each entry. The two semilinear twists cancel, so $\rho'$ is a $K$-linear irreducible representation with character $\overline{\chi^\lambda(\iota(x))}$. At $q = 1$ both twists are the identity, so $\rho'$ and $\rho$ specialise to the same irreducible character of $S_n$, and by Tits deformation $\rho' \cong \rho$. Evaluating on a braid word and barring both sides gives $\chi^\lambda(C\beta)(q) = \chi^\lambda(\beta)(q^{-1})$. Because Tits's deformation theorem is invoked externally for general $n$, the proposition above is stated explicitly for $H_3(q)$.

**Consequence for the meson word.** On the meson word in $H_3(q)$, the character $\chi^{(2,1)}$ takes the exact value $-(q^4 - q^2 + 1)/q^2$ for the word, its charge conjugate, and its bar image alike. The character identity $C = \mathrm{bar}$ therefore holds on $(2,1)$ as well as on the one-dimensional characters: it does not single out $H_2(q)$, and it does not separate a lepton level from a meson level.
