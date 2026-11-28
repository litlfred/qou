The previous sub-section established the classical-limit functor and its aether-level constructions. The consequences follow. The graded Baer-star structure on $\mathcal{H}_q$ descends through the two-filtration bridge to relate the Gröbner--Shirshov depth filtration to Goncharov's period filtration.

The sub-section then states the classical Riemann zeta function and the Riemann hypothesis. What the book can say about them is limited, and it is said here so that the blocks below are read correctly.

- The Riemann hypothesis is an open problem. It is stated in Lean over Mathlib's `riemannZeta` with no instance, and the book assumes no proof of it.
- The local zeta functions of Bring's curve do not assemble into $\zeta(s)$. Their product over the primes is $\zeta(s)\,\zeta(s-1)/L(E,s)^4$ up to finitely many factors, with $E$ the elliptic curve 50a1 ([geometric stability via the Weil bound](#sec:q-gl-weil-bound-stability)). The local critical-line property concerns $L(E,s)$; $\zeta(s)$ is the $H^0$ factor and inherits nothing from it.
- In the macroscopic stability equivalence, the link between the optimal prime-counting error and the Riemann hypothesis is classical (von Koch 1901 and the explicit formula) but is carried as a hypothesis, since it is not in Mathlib. The link between the Riemann hypothesis and a Reeb spectrum needs a Reeb operator whose spectrum is tied to $\zeta$. The book does not construct one, so that link is open.

The adelic Tate squeeze closes the chapter as the surreal-bound infrastructure consumed by the appendix-surreal Millennium bounds. The Riemann-hypothesis instance of those bounds is a heuristic comparison of scales, not a proof.

The sub-section ends with the chapter outro, preparing the archimedean-universe specialisation in the next chapter.
