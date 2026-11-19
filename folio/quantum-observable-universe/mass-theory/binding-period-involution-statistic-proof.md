**Proof.**

Write $b(\lambda) = \sum_{i \geq 1} (i-1)\lambda_i$, so that
$\mathrm{content}(\lambda) = b(\lambda') - b(\lambda)$ with $\lambda'$ the
conjugate partition, and let
$[k]_q = 1 + q + \cdots + q^{k-1}$ denote the unbalanced quantum integer and
$\tilde f^{\lambda}(q) = q^{b(\lambda)} [n]_q! / \prod_{c \in \lambda} [h(c)]_q$
the fake degree of $\lambda \vdash n$ \cite{stanley1999}.

**Step 1 (balanced twist).** From
$[k] = (q^k - q^{-k})/(q - q^{-1}) = q^{-(k-1)}[k]_{q^2}$ and the hook-length
identity $\sum_{c \in \lambda} h(c) = b(\lambda) + b(\lambda') + n$,

$$
\dim_q^{\mathrm{bal}}(\lambda)
= q^{\sum_{c}(h(c)-1) \, - \, \sum_{k=1}^{n}(k-1)}
  \cdot \frac{\prod_{k=1}^{n}[k]_{q^2}}{\prod_{c \in \lambda}[h(c)]_{q^2}}
= q^{\,\mathrm{content}(\lambda) - n(n-1)/2}\; \tilde f^{\lambda}(q^2).
$$

**Step 2 (q-hook-maj).** Stanley's formula gives, for every $\lambda \vdash n$,
$\sum_{T \in \mathrm{SYT}(\lambda)} q^{\mathrm{maj}(T)} = \tilde f^{\lambda}(q)$
\cite{stanley1999}.

**Step 3 (descent preservation on involutions).** RSK restricts to a
bijection $w \mapsto P(w)$ from the involutions of RSK shape $\lambda$ onto
$\mathrm{SYT}(\lambda)$, and $\mathrm{Des}(w) = \mathrm{Des}(P(w))$
(Schützenberger) \cite{sagan2001}; hence $\mathrm{maj}(w) = \mathrm{maj}(P(w))$ and

$$
\sum_{w \in \mathrm{Inv}(S_n),\; \lambda(w) = \lambda} q^{\,2\,\mathrm{maj}(w)}
= \tilde f^{\lambda}(q^2).
$$

Multiplying by $q^{\mathrm{content}(\lambda)}$, summing over $\lambda \vdash n$,
and applying Step 1 termwise yields
$\sum_{w} q^{2\,\mathrm{maj}(w) + \mathrm{content}(\lambda(w))}
= \sum_{\lambda \vdash n} q^{\mathrm{content}(\lambda)} \tilde f^{\lambda}(q^2)
= q^{n(n-1)/2} S^{\mathrm{bal}}(n; q)$. The $q = 1$ specialisation counts the
standard Young tableaux, $\sum_{\lambda \vdash n} f^{\lambda} = I(n)$ with
$f^{\lambda} = \tilde f^{\lambda}(1)$ their number per shape. $\blacksquare$

**Finite verification.** Direct evaluation of the exponent multisets
establishes the identity for $n = 3, 4$ from the computable RSK insertion; exact symbolic verification for $n \leq 8$ (all
$764$ involutions at $n = 8$) has been carried out, and
the transfer-operator reconstruction extends the exact cross-checks to
$n \leq 16$ (hook side) and $n \leq 24$ (at $q = 1$).
