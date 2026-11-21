**Proof.**

Let $K = \mathbb{Q}(q)$ and let $\iota$ be the ring involution of $H_n(q)$ over $K$ that sends $q \mapsto q^{-1}$ and $\sigma_i \mapsto \sigma_i^{-1}$. It is well defined because it preserves the defining relations: the braid relations are preserved by inverting every letter and reversing nothing, and the quadratic relation $\sigma_i^2 = h\sigma_i + 1$ becomes $\sigma_i^{-2} = -h\,\sigma_i^{-1} + 1$, which is the same relation multiplied by $\sigma_i^{-2}$. On a braid word $\beta$ the involution acts as $C$, since a braid word has coefficient $1$.

Let $\rho$ be an irreducible representation of $H_n(q)$ over $K$ with character $\chi^\lambda$. Define $\rho'(x) = \overline{\rho(\iota(x))}$, where the outer bar applies $q \mapsto q^{-1}$ to each matrix entry. The two semilinear twists cancel, so $\rho'$ is a $K$-linear representation; it is irreducible because $\iota$ is bijective. Its character is
$$
  \chi'(x) = \overline{\chi^\lambda(\iota(x))}.
$$
Characters of $H_n(q)$ take values in $\mathbb{Z}[q, q^{-1}]$, and specialising $q \mapsto 1$ sends each irreducible character of $H_n(q)$ to the corresponding irreducible character of $S_n$, which distinguishes them (Tits deformation). At $q = 1$ the outer bar is the identity and $\iota(\sigma_i) = \sigma_i^{-1} = \sigma_i$, so $\chi'$ specialises to the same character of $S_n$ as $\chi^\lambda$. Hence $\rho' \cong \rho$ and $\chi' = \chi^\lambda$. Applying this to a braid word $\beta$ and then barring both sides gives $\chi^\lambda(C(\beta))(q) = \chi^\lambda(\beta)(q^{-1})$. $\square$

**Explicit case $n = 3$, $\lambda = (2,1)$.** In the representation
$$
  \sigma_0 \mapsto \begin{pmatrix} -q^{-1} & q \\ 0 & q \end{pmatrix},\qquad
  \sigma_1 \mapsto \begin{pmatrix} q & 0 \\ q^{-1} & -q^{-1} \end{pmatrix}
$$
($q$ times the reduced Burau matrices at $t = q^{-2}$), the matrix $P = \mathrm{diag}(1, q^2)$ satisfies $P\,\sigma_i^{-1}(q) = \sigma_i(q^{-1})\,P$ for both generators. So $P\,\rho_q(C\beta)\,P^{-1} = \rho_{q^{-1}}(\beta)$ for every word, and the traces agree. The Lean sibling proves this case for every braid word over any field.

**Consequence for the earlier reading.** An earlier version of this block claimed $C \ne \mathrm{bar}$ on $(2,1)$, quoting $\chi^{(2,1)}$ of the meson word at $q_0$ as $+1.892$ after charge conjugation. The exact value is $-(q^4 - q^2 + 1)/q^2$ for the word, its charge conjugate and its bar alike. $C = \mathrm{bar}$ therefore does not single out $H_2(q)$, and it does not separate a lepton level from a meson level.
