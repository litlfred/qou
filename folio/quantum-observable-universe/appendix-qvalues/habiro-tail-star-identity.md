**Proposition.** *Let $R$ be a field and $a \in R$ with $a \neq 0$. Write
$\bar q = a^{2}$ and $\tilde q = a^{-2}$, let $(\,q;q)_n = \prod_{j=1}^{n}(1-q^{j})$
denote the $q$-Pochhammer symbol, let $[n,k]_q$ denote the Gaussian binomial
coefficient, and let $C_n(a)$ be the $n$-th Masbaum cyclotomic coefficient of
$5_2$. Then for every $n \geq 0$*

$$
C_n(a)\,(\bar q;\bar q)_n^{2}\,a^{-(5n^{2}+7n)}
  \;=\; (-1)^{n}\,(\tilde q;\tilde q)_n^{2}
        \sum_{k=0}^{n} \tilde q^{\,k(n+1)}\,[n,k]_{\tilde q}.
$$

This is the *Habiro-tail star identity*.

## What the identity does

The left-hand side is the Masbaum cyclotomic datum in its native variable
$a$, carrying a quadratic exponent in both $n$ and the summation index $k$.
The right-hand side is a $q$-Borel transform evaluated at the bar-inverted
argument $\tilde q$, with an exponent that is **linear** in $k$. The identity
is therefore an exponent-collapse: it trades a quadratic $k$-dependence for a
linear one, and simultaneously exchanges $\bar q \leftrightarrow \tilde q$.

Two inversion lemmas supply the collapse, one for each factor.

**Bar-inversion of the Gaussian binomial.** For $q \neq 0$,

$$
[n,k]_q \;=\; q^{\,k(n-k)}\,[n,k]_{q^{-1}}.
$$

Applied termwise, this converts each summand's $a$-exponent
$3n^{2}+5n+k^{2}-2k-3nk-k(n-k)$ into $3n^{2}+5n-2k-2nk$; the quadratic
$k^{2}$ cancels. Multiplying by the overall $a^{-(5n^{2}+7n)}$ leaves
$-2(n+1)(n+k)$, that is, exactly
$(\bar q)^{-n(n+1)}\cdot(\bar q^{-1})^{k(n+1)}$.

**Bar-inversion of the squared Pochhammer.** For $q \neq 0$,

$$
(\,q;q)_n^{2} \;=\; q^{\,n(n+1)}\,(\,q^{-1};q^{-1})_n^{2}.
$$

This absorbs the residual $(\bar q)^{-n(n+1)}$ prefactor. Squaring is what
makes the statement clean: the unsquared inversion carries a sign $(-1)^n$
and the half-exponent $n(n+1)/2$, and both disappear on squaring.

## Consequences

Write $\hat T_n(q) = (\,q;q)_n^{2}\sum_{k=0}^{n} q^{k(n+1)}[n,k]_q$ for the
right-hand side up to sign, so that the identity reads
$C_n(a)(\bar q;\bar q)_n^{2}a^{-(5n^{2}+7n)} = (-1)^n \hat T_n(\tilde q)$.

**Transient structure.** The $k=0$ term of the sum is exactly $1$, whence

$$
\hat T_n(q) \;=\; (\,q;q)_n^{2}\Bigl(1 + q^{\,n+1}
  \sum_{k=0}^{n-1} q^{\,k(n+1)}\,[n,k+1]_q\Bigr).
$$

Every correction to the leading $(\,q;q)_n^{2}$ carries a factor $q^{n+1}$.
This is the algebraic source of the transient behaviour observed in the
numerical Borel data.

**Pochhammer recursion.** $(\,q;q)_{n+1} = (\,q;q)_n\,(1-q^{\,n+1})$, the
finite-order step whose limit governs the Borel residue.

The two *analytic* facts recorded in the computational witnesses — the
residue $c_\infty = (\tilde q;\tilde q)_\infty^{2}$ as a convergent infinite
product, and the pole ladder at $w = -q_0^{\,k}$ — are limit statements about
the archimedean evaluation and are not part of this proposition. What the
proposition supplies is their algebraic skeleton: the recursion and the
$q^{n+1}$ transient factor of which those limits are taken.

## Status

The identity is proved at every order $n$, over a
generic field with no archimedean construct (the statement is pre-wall).
It was first established computationally as an exact integer-Laurent
equality for $n \leq 32$ and numerically to $10^{-497}$ for $n \leq 64$;
the proof discharges that computation for all $n$.
