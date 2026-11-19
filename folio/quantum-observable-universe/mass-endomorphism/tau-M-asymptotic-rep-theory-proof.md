## Proof

The factorisation defines $F_\lambda$; the substance lies in the parity and the proved rungs.

**Parity (even in $\hbar_q$).** The cosine envelope and every rung factor depend on $\hbar_q$ only through $\hbar_q^2$, since $u_\lambda = b_\lambda\hbar_q^2$. So $F_\lambda$, in the factorised form, is even in $\hbar_q$ by construction. The bar involution does not supply this: it sends $\hbar_q = (q-1)/q$ to $1 - q = -q\,\hbar_q$. The bar-parity alternation $\overline{c_k} = (-1)^k c_k$ is a separate statement, established in [the Habiro $q$-difference recursion for $c_k$](#prop:q-beta-c-k-recursion-from-habiro-q-difference). $\square$

**Baseline $F_\lambda = 1$ at $q = 1$.** At $q = 1$, $\hbar_q = 0$, and $\rho_\lambda(\sigma_i)$ maps to the symmetric-group permutation matrix. Therefore, $\mathrm{tr}_M^{V_\lambda} = \mathrm{Tr}\,\rho_\lambda(\beta)$ and $F_\lambda(0) = 1$. $\square$

**One-dimensional irreducible representations.** For the trivial representation $V_{(n)}$ and the sign representation $V_{(1^n)}$, $\rho_\lambda(\sigma_i)$ is a scalar. The off-diagonal coupling vanishes ($b_\lambda = 0$, hence $u_\lambda = 0$), and the Markov-symmetrised character equals the bare character. Thus, $F_\lambda \equiv 1$. The one-dimensional closed forms are documented in [closed-form characters of 1-d Hecke representations](#prop:hecke-1d-irrep-closed-form-character). $\square$

**$N=1$ envelope (coupling $b$), $V_{(2,1)}$.** The first non-trivial irreducible representation is the two-dimensional $V_{(2,1)}$ of $H_3$. Its single $\tilde f_1$ Kashiwara edge carries weight $b_\lambda = b$. This produces the eigenphase shift $-b\,\hbar_q^2/2$, given by the $\tilde f_1$ matrix element in the seminormal basis multiplied by $\hbar_q^2/2$. The shift resums into the $\cos(\alpha - b\hbar_q^2/2)$ envelope. This provides the $N=1$ result of [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization). $\square$

**Second rung, $V_{(2,1)}$: $c_2 = -1$.** The $N=2$ correction factor is $(1 - b^2\hbar_q^4) = (1 - u^2)$ with $u = b\hbar_q^2$. Written in the ladder form $(1 + c_2 u^2)$, it gives $c_2 = -1$. This is a rewriting of the factor rather than a derivation of it: the factor $(1 - b^2\hbar_q^4)$ is taken from the Kashiwara $\tilde f_1^\dagger\tilde f_1$ correction, which is not proved here. $\square$

The proof gives $F_\lambda = 1$ at $q = 1$, the one-dimensional triviality, the $N=1$ coupling $b$, the reading $c_2 = -1$ of the $N=2$ factor, and the evenness in $\hbar_q$ of the factorised form. Generating the operator-graded rungs $c_k^{(\lambda)}$ for $k \geq 3$ via [the Habiro $q$-difference recursion for $c_k$](#prop:q-beta-c-k-recursion-from-habiro-q-difference) requires specifying the fibre-level kernel $R(q,\xi)$, which is conjectural. $\blacksquare$
