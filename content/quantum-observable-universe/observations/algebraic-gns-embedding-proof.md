*Proof.* All four ingredients are standard; we collect them.

**(1) Tower of inclusions.** The Hecke algebra $H_n(R, q)$ has
presentation by braid generators $\sigma_1, \ldots, \sigma_{n-1}$
modulo the Hecke quadratic relation
$\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ and the braid relations. The
inclusion $H_n(q) \hookrightarrow H_{n+1}(q)$ adjoins $\sigma_n$;
this is unital, $R$-linear, and respects the bar-involution
$\sigma_i \leftrightarrow \sigma_i^{-1}$. Hence $\{H_n(q)\}_{n \geq 1}$
is a filtered inductive system in the category of unital
$*$-algebras over $R$, with colimit $H_\infty(q) = \bigcup_n H_n(q)$
[`jones1985`].

**(2) Markov property.** The Markov trace
$\mathrm{tr}_{M,n} \colon H_n(q) \to R$ satisfies, for any
$x \in H_n(q)$, the recursion
$\mathrm{tr}_{M,n+1}(x \cdot \sigma_n) = z \cdot \mathrm{tr}_{M,n}(x)$,
where $z = 1/(q^{1/2}+q^{-1/2})$
([Jones–Markov trace](#thm:jones-markov-trace)).
Equivalently, $\mathrm{tr}_{M,n+1}|_{H_n(q)} = \mathrm{tr}_{M,n}$,
so the family is compatible with the inclusions of step (1). By the
universal property of the colimit, there is a unique
$R\otimes\mathbb{Q}$-linear trace
$\mathrm{tr}_M \colon H_\infty(q) \to R\otimes\mathbb{Q}$ extending
all $\mathrm{tr}_{M,n}$.

**(3) Positivity.** Wenzl 1988 showed that for $q$ in the regime
$q^{1/2}+q^{-1/2} > 2$ (equivalently, $q \in (0, q_-) \cup (q_+, \infty)$
for the two real roots $q_\pm$ of $q + q^{-1} = 2$), the Markov trace
is a *positive* linear functional: for every $x \in H_n(q)$,
$\mathrm{tr}_{M,n}(x^* x) \geq 0$, with equality iff $x = 0$ in the
quotient by the trace ideal. The QOU substrate $q_0 \approx 1.11$
satisfies $q_0^{1/2}+q_0^{-1/2} \approx 1.054 + 0.949 = 2.003 > 2$
(narrowly — the binding regime sits right above the positivity
threshold). Hence Wenzl's positivity applies, and
$\mathrm{tr}_M$ is a positive trace on $H_\infty(q)$.

**(4) GNS construction.** Let
$\mathcal{N} := \{x \in H_\infty(q) : \mathrm{tr}_M(x^* x) = 0\}$.
By positivity and the Cauchy–Schwarz inequality
$|\mathrm{tr}_M(x^* y)|^2 \leq \mathrm{tr}_M(x^* x)\,\mathrm{tr}_M(y^* y)$,
$\mathcal{N}$ is a left ideal of $H_\infty(q)$. The quotient
$V := H_\infty(q) / \mathcal{N}$ is therefore an $H_\infty(q)$-module
under left multiplication, and the bilinear form
$\langle [x], [y] \rangle := \mathrm{tr}_M(x^* y)$ is well-defined,
sesquilinear (with respect to $*$), and positive definite on $V$.
Its completion $\mathcal{H}$ is a separable Hilbert space (separability
follows from countability of the basis of $H_\infty(q)$ as an
$R\otimes\mathbb{Q}$-module under any chosen presentation).

The left-multiplication action $\pi_{\mathrm{GNS}}(a)[x] := [a x]$
extends to a bounded operator on $\mathcal{H}$: the bound
$\|\pi_{\mathrm{GNS}}(a)\| \leq \|a\|_2$ uses the trace
Cauchy–Schwarz again. Faithfulness:
$\pi_{\mathrm{GNS}}(a) = 0 \implies \pi_{\mathrm{GNS}}(a)[1] = [a] = 0
\implies a \in \mathcal{N} \implies \mathrm{tr}_M(a^* a) = 0
\implies a = 0$ in the trace-quotient sense. The $*$-property
$\pi_{\mathrm{GNS}}(a^*) = \pi_{\mathrm{GNS}}(a)^*$ holds on the
dense subspace $V \subset \mathcal{H}$ by direct computation and
extends to all of $\mathcal{H}$ by continuity. $\square$

**Remark.** The image
$M := \pi_{\mathrm{GNS}}(H_\infty(q))'' \subset L(\mathcal{H})$
(double commutant) is a finite type II$_1$ von Neumann algebra with
trace $\mathrm{tr}_M$. This is the Jones–Wenzl subfactor planar
algebra at modular parameter $z$. The full machinery of subfactor
theory therefore applies on the QOU algebraic side; this is what
makes clause 1 of [CFS comparison summary](#rem:cfs-comparison-summary)
established rather than conjectural.
