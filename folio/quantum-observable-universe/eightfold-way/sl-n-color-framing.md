*Let $V$ be the vector representation of $\mathrm{U}_q(\mathfrak{gl}_N)$ and let
$\sigma_i$ act on $V^{\otimes n}$ by the Jimbo braiding \cite{jimbo1986}, with eigenvalue $q$ on
$\mathrm{Sym}^2 V$ and $-q^{-1}$ on $\Lambda^2 V$. Put
$\sigma_i^{\mathfrak{sl}} := q^{-1/N}\,\sigma_i$. Then:*

1. *the eigenvalues of $\sigma_i^{\mathfrak{sl}}$ on $\mathrm{Sym}^2 V$ and
   $\Lambda^2 V$ are $q^{2 c_{\mathrm{S}}}$ and $-q^{2 c_{\mathrm{A}}}$, where
   $c_R := \tfrac12\bigl(C_2(R) - 2C_F\bigr)$ is the one-gluon color factor,
   $c_{\mathrm{S}} = \tfrac{N-1}{2N}$ and $c_{\mathrm{A}} = -\tfrac{N+1}{2N}$;*
2. *the eigenvalues of $\sigma_i$ itself are $q^{2c_R + 1/N}$ up to sign;*
3. *the ratio $c_{\mathrm{A}}/c_{\mathrm{S}} = -\tfrac{N+1}{N-1}$ equals $-2$
   if and only if $N = 3$;*
4. *$q^{-1/N}$ is the unique positive scalar $c$ for which the monodromy of $V$
   around $\Lambda^N V$ under $c\,\sigma_i$ is the identity.*

**Proof.** Items 1--3 are identities in $\mathbb{Q}(N)$. They use the Casimir
values $C_F = \tfrac{N^2-1}{2N}$, $C_2(\mathrm{Sym}^2 V) = \tfrac{(N-1)(N+2)}{N}$
and $C_2(\Lambda^2 V) = \tfrac{(N+1)(N-2)}{N}$, together with the ribbon formula
for the braiding on a summand of $V \otimes V$ \cite{kassel1995}.

For item 4, the full twist acts on the irreducible summand indexed by $\lambda$
as $q^{2\,\mathrm{ct}(\lambda)}$, where $\mathrm{ct}(\lambda)$ is the sum of
contents. The tensor product $V \otimes \Lambda^N V$ is the summand
$\lambda = (2, 1^{N-1})$, and $\Lambda^N V$ is $(1^N)$. So the monodromy of $V$
around $\Lambda^N V$ is
$q^{2\,\mathrm{ct}(2,1^{N-1}) - 2\,\mathrm{ct}(1^N)} = q^{2}$. The braid has
$2N$ crossings, so rescaling to $c\,\sigma_i$ multiplies the monodromy by
$c^{2N}$. The condition $c^{2N} q^2 = 1$ with $c > 0$ forces $c = q^{-1/N}$.
$\square$

The value $q^2$ of the monodromy
is computed on explicit Jimbo matrices for $N = 2, 3$ and from contents for all
$N$.
