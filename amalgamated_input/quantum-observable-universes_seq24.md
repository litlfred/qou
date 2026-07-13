<!-- FILE_START: intro-q-special-functions.md -->
We identify the three categorical special functions that pair with the resolvent: the $q$-exponential $\exp_q \in G(\mathcal{H}_q)$, its primitive inverse $\log_q$, and the level-2 iterated primitive $\mathrm{Li}_2^q$. Each is defined Hopf-algebraically, circumventing analytic representations.
<!-- FILE_END: intro-q-special-functions.md -->

<!-- FILE_START: q-exponential.md -->
A grouplike of the $q$-shuffle Hopf algebra $\mathcal{H}_q$ is an element $g \in \mathcal{H}_q$ satisfying $\Delta_q(g) = g \otimes g$ and $\epsilon(g) = 1$. The **$q$-exponential** is the unique grouplike $\exp_q \in G(\mathcal{H}_q)$ satisfying the categorical flow equation

$$
  D_q  \exp_q  =  \exp_q, \qquad \exp_q(0) = 1.
$$
<!-- FILE_END: q-exponential.md -->

<!-- FILE_START: q-exponential-realisations.md -->
The $q$-exponential is the free grouplike on the primitive generator of the Reeb flow. Its Taylor coefficients lie in the Habiro ring $\widehat{\mathbb{Z}[q]}[\![x]\!]$. Evaluation at any root of unity is the purely algebraic cyclotomic-projection $\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_n(q)$. 

$\exp_q$ operates as the categorical generator of the Reeb flow, dictating the $q$-deformed rotation $\mathcal{L}_\xi Z = J\hbar_q Z$ on the substrate coordinate $Z$.
<!-- FILE_END: q-exponential-realisations.md -->

<!-- FILE_START: q-exponential-exists.md -->
Let $\mathcal{H}_q$ be the $q$-shuffle Hopf algebra over a base ring $R$ in which the Jackson integers $[n]_q$ are invertible. There exists a unique grouplike $\exp_q \in G(\mathcal{H}_q)$ satisfying $D_q \exp_q = \exp_q$ and $\epsilon(\exp_q) = 1$.
<!-- FILE_END: q-exponential-exists.md -->

<!-- FILE_START: q-exponential-unique.md -->
The grouplike $\exp_q$ is unique.
<!-- FILE_END: q-exponential-unique.md -->

<!-- FILE_START: q-exp-finite-field-obstruction.md -->
The archimedean Taylor series $\exp_q(x) = \sum_{n \ge 0} x^n / [n]_q!$ fails over a field of characteristic $p$ whenever the Jackson factorial $[n]_q!$ vanishes modulo $p$. The grouplike $\exp_q$ nonetheless exists as a symbol in the formal Hopf algebra $\mathcal{H}_q \otimes \mathbb{F}_p$. The truncated $p$-exponential $\exp_q^{(p)}(x) = \sum_{n = 0}^{p - 1} x^n / [n]_q!$ becomes grouplike modulo $x^p = 0$.
<!-- FILE_END: q-exp-finite-field-obstruction.md -->

<!-- FILE_START: q-exp-p-adic.md -->
The truncated $\mathbb{F}_p$-exponential lifts to a convergent grouplike on $\mathbb{Q}_p$ and $\mathbb{C}_p$ when $q$ is $p$-adically close to $1$. For $q \in 1 + p\mathbb{Z}_p$, the Jackson factorial satisfies $v_p([n]_q!) = v_p(n!)$. Over $\mathbb{C}_p$, the series converges for $v_p(x) > 1/(p - 1)$, exactly matching the classical $p$-adic exponential radius.
<!-- FILE_END: q-exp-p-adic.md -->

<!-- FILE_START: q-logarithm.md -->
A primitive of $\mathcal{H}_q$ satisfies $\Delta_q(p) = p \otimes 1 + 1 \otimes p$ and $\epsilon(p) = 0$. The **$q$-logarithm** is the unique primitive $\log_q \in \mathrm{Prim}(\mathcal{H}_q)$ satisfying

$$
  \log_q \circ \exp_q \;=\; \mathrm{id}.
$$

It acts as the left adjoint of the grouplike-of functor from primitives to grouplikes.
<!-- FILE_END: q-logarithm.md -->

<!-- FILE_START: q-logarithm-properties.md -->
The $q$-logarithm is base-ring independent. The adjoint pair $(\log_q, \exp_q)$ operates on the formal-power-series ring $\widehat{\mathbb{Z}[q]}[\![x]\!]$ over the Habiro ring. It measures the cosmological displacement in Hopf-algebraic units as the infinitesimal generator of the Reeb-flow holonomy.
<!-- FILE_END: q-logarithm-properties.md -->

<!-- FILE_START: q-logarithm-exists.md -->
Under the hypotheses securing $\exp_q$, there exists a unique primitive $\log_q \in \mathrm{Prim}(\mathcal{H}_q)$ satisfying $\log_q \circ \exp_q = \mathrm{id}$.
<!-- FILE_END: q-logarithm-exists.md -->

<!-- FILE_START: q-logarithm-unique.md -->
The primitive $\log_q$ is unique.
<!-- FILE_END: q-logarithm-unique.md -->

