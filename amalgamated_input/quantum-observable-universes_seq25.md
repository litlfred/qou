<!-- FILE_START: q-special-functions-dilog-intro.md -->
We introduce the $q$-dilogarithm as the framework's central transcendental object, anchored by its $\mathrm{SU}(2)$ specialisation and Reeb-flow PDE characterisation.
<!-- FILE_END: q-special-functions-dilog-intro.md -->

<!-- FILE_START: q-dilogarithm.md -->
A level-$k$ primitive $p_k \in \mathcal{H}_q^{\otimes k}$ satisfies the shuffle recursion $\Delta_q(p_k) = p_k \otimes 1 + 1 \otimes p_k + \sum_{i=1}^{k-1} p_i \otimes p_{k-i}$. The **$q$-dilogarithm** is the unique level-2 primitive $\mathrm{Li}_2^q \in \mathcal{H}_q^{\otimes 2}$ normalised by the pentagon relation

$$
  \mathrm{Li}_2^q(y) + \mathrm{Li}_2^q(x) = \mathrm{Li}_2^q(xy) + \mathrm{Li}_2^q\!\left(\frac{x(1-y)}{1-xy}\right) + \mathrm{Li}_2^q\!\left(\frac{y(1-x)}{1-xy}\right).
$$
<!-- FILE_END: q-dilogarithm.md -->

<!-- FILE_START: q-dilogarithm-pentagon-associator.md -->
The pentagon relation normalising the $q$-dilogarithm enforces the pentagon axiom for the monoidal category $\mathbf{C}$: $\mathrm{Li}_2^q$ is the unique level-2 primitive compatible with the monoidal associator $\alpha_{X,Y,Z}$.
<!-- FILE_END: q-dilogarithm-pentagon-associator.md -->

<!-- FILE_START: q-dilogarithm-properties.md -->
The universal $R$-matrix of $U_q(\mathfrak{sl}_2)$ admits the Faddeev--Kashaev factorisation. The logarithm of $\mathcal{R}$ matches the $q$-dilogarithm at leading order. $\mathrm{Li}_2^q$ constitutes the categorical braiding potential.
<!-- FILE_END: q-dilogarithm-properties.md -->

<!-- FILE_START: q-dilog-habiro-ring.md -->
The formal series $\mathrm{Li}_2^q(x) = \sum_{n \geq 1} x^n / (n\,[n]_q)$ holds coefficients in the Habiro ring $\widehat{\mathbb{Z}[q]}[\![x]\!]$. Cyclotomic projection evaluates the series at any root of unity without invoking analytic continuation.
<!-- FILE_END: q-dilog-habiro-ring.md -->

<!-- FILE_START: q-dilog-three-contexts.md -->
The extra denominator $n$ forces tighter convergence constraints. Over $\mathbb{F}_p$, the series truncates to $\mathrm{Li}_2^{q,(p)}(x) = \sum_{n=1}^{p-1} x^n / (n [n]_q)$. Over $\mathbb{Q}_p$ and $\mathbb{C}_p$, it converges securely within $v_p(x) > 1/(p-1)$.
<!-- FILE_END: q-dilog-three-contexts.md -->

<!-- FILE_START: q-dilog-archimedean.md -->
Over $\mathbb{C}$, the $q$-dilogarithm represents the convergent Kirillov series $\mathrm{Li}_2^q(x) = \sum_{n \ge 1} \frac{x^n}{n  [n]_q}$ for $|x| < 1$.
<!-- FILE_END: q-dilog-archimedean.md -->

<!-- FILE_START: q-dilog-heat-partition.md -->
The $q$-dilogarithm generates the partition function of the $q$-heat flow. The contour integral of the resolvent against the spectrum sums logarithmic branches at each eigenvalue $\lambda_j(q)$ to produce $\mathrm{Li}_2^q$.
<!-- FILE_END: q-dilog-heat-partition.md -->

<!-- FILE_START: q-dilog-physical-meaning.md -->
The $q$-dilogarithm controls the one-loop correction to the Reeb-flow entropy on the substrate.
<!-- FILE_END: q-dilog-physical-meaning.md -->

<!-- FILE_START: q-dilogarithm-exists.md -->
There exists a unique level-2 iterated primitive $\mathrm{Li}_2^q \in \mathcal{H}_q^{\otimes 2}$ satisfying the pentagon identity.
<!-- FILE_END: q-dilogarithm-exists.md -->

<!-- FILE_START: q-dilogarithm-unique.md -->
The $q$-dilogarithm $\mathrm{Li}_2^q$ is unique up to a fixed scalar in $R$.
<!-- FILE_END: q-dilogarithm-unique.md -->

<!-- FILE_START: generating-functions-solve-reeb-flow.md -->
The functions $\exp_q$, $\mathrm{Li}_2^q$, and the categorical Fourier transform constitute the exact algebraic solutions to the characteristic flow equations on the Reeb bundle within the Habiro completion. 

1. $\exp_q$ provides the formal solution of the base Reeb-flow equation $L_{\xi_q} Z = J\hbar_q Z$.
2. The categorical Fourier transform diagonalises the $q$-heat equation $\partial_t u = -\Delta_q u$ across Peter–Weyl isotypic components.
3. $\mathrm{Li}_2^q$ evaluates the volumetric expansion of the Reeb-heat flow. Under the archimedean realisation $\tau_\infty$, it produces the Bloch–Wigner dilogarithm.

These functions are not combinatorial conveniences; they are the unique algebraic objects in the Habiro completion satisfying the categorical evolution equations.
<!-- FILE_END: generating-functions-solve-reeb-flow.md -->

<!-- FILE_START: archimedean-realisation-volume-compatibility.md -->
The local archimedean realisation functor $\tau_\infty \colon \widehat{\mathbb{Z}[q]} \to \mathbb{C}[\![q-1]\!]$ acts on the Habiro-ring volume. The global archimedean realization functor $\mathcal{R}_{\mathrm{top}} \colon \widehat{\mathcal{M}} \to \mathbb{R}$ evaluates the motivic volume class. 

Conjecturally, for every QOU braid $\beta$, the archimedean value of the Habiro-ring volume and the topological realization of the motivic volume coincide with the hyperbolic volume:

$$
  \mathrm{ev}_{q \to 1}\bigl(\tau_\infty(-\mathrm{Li}_2^q(-V_0(\beta)))\bigr) = \mathcal{R}_{\mathrm{top}}\bigl(\mu(\beta)\bigr) = V_{\mathrm{hyp}}(K_\beta).
$$
<!-- FILE_END: archimedean-realisation-volume-compatibility.md -->

