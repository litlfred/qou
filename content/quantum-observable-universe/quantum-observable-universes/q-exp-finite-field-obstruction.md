The categorical $q$-exponential ([$q$-exponential](#def:q-exponential))
is defined purely Hopf-algebraically: $\exp_q$ is the unique grouplike
of $\mathcal{H}_q$ satisfying $D_q \exp_q = \exp_q$.  This characterisation is
base-ring independent.  Its archimedean realisation as the Taylor series

$$
  \exp_q(x) \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!}
$$

([Taylor series of $\exp_q$](#prop:q-exponential-taylor)) is,
however, an *archimedean-only* statement.  The series representation
*fails* over a field of characteristic $p$ whenever the Jackson
factorial $[n]_q!$ vanishes modulo $p$.

**Location of the vanishing.**  The Jackson integer
$[n]_q = (1 - q^n)/(1 - q)$ vanishes in $\mathbb{F}_p$ precisely when
$q^n = 1$ in $\mathbb{F}_p^\times$ — i.e.\ when the multiplicative
order $\mathrm{ord}_{\mathbb{F}_p^\times}(q)$ divides $n$.  Thus
$[n]_q! = 0$ for every $n$ at least equal to that order, and the
formal series $\sum x^n / [n]_q!$ has divisions by zero starting at
degree $\mathrm{ord}_{\mathbb{F}_p^\times}(q)$.

**Surviving abstract structure.**  The grouplike $\exp_q$ nonetheless
*exists* in the formal Hopf algebra $\mathcal{H}_q \otimes \mathbb{F}_p$:
one can define $\exp_q$ as a *symbol* (a formal grouplike, adjoined
to the Hopf algebra), characterised by its coproduct
$\Delta_q(\exp_q) = \exp_q \otimes \exp_q$ and the flow equation
$D_q \exp_q = \exp_q$, without attempting to evaluate it at specific
arguments.  This is analogous to the formal group law: the group
$\widehat{\mathbb{G}_a}$ is defined in any characteristic, even
though the exponential $\exp \colon \widehat{\mathbb{G}_a} \to \widehat{\mathbb{G}_m}$
is not realisable as a power series in characteristic $p$.

**Truncated $p$-exponential.**  A partial substitute over
$\mathbb{F}_p$ is the truncated series

$$
  \exp_q^{(p)}(x) \;=\; \sum_{n = 0}^{p - 1} \frac{x^n}{[n]_q!},
$$

well-defined whenever $[n]_q \ne 0$ for $1 \le n \le p - 1$.  This is
a polynomial, not a grouplike of the full Hopf algebra — but it
*becomes* grouplike modulo the relation $x^p = 0$ (or the
$\mathbb{F}_p$-Frobenius twist).  Geometrically: the $p$-truncated
$\exp_q$ lives on the first-order infinitesimal neighbourhood of
the identity in $G(\mathcal{H}_q)$.

**Witt-vector lift.**  The truncated $\mathbb{F}_p$-exponential lifts
uniquely to a convergent grouplike on $\mathbb{Q}_p$ and $\mathbb{C}_p$
when $q$ is $p$-adically close to $1$ — see
[$p$-adic realisations of $\exp_q$](#rem:q-exp-p-adic) for the
convergence radii and the $q$-analogue of the Artin--Hasse
exponential.

**Conclusion.**  $\exp_q$ is archimedean in its *series representation*,
but base-ring independent in its *Hopf-algebraic content*.  The same
applies to $\log_q$ ([$q$-logarithm](#def:q-logarithm)) and
$\mathrm{Li}_2^q$ ([$q$-dilogarithm](#def:q-dilogarithm)): the
categorical structures survive in characteristic $p$; only their
power-series avatars fail.
