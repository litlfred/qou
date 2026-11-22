
*Part (1).*  When $q$ is not a root of unity, the Iwahori--Hecke algebra
$H_n(R, q)$ is isomorphic to $\mathbb{C}[S_n]$ as an abstract algebra
(Jimbo's theorem), hence semisimple.  By $q$-Schur--Weyl duality
the image of $H_n(R, q)$ in $\mathrm{End}(V^{\otimes n})$ is the
commutant of $\mathrm{SU}_q(2)$, which is the Temperley--Lieb
quotient $\mathrm{TL}_n(q)$; the decomposition of $V^{\otimes n}$ is
the standard result for $\mathrm{SU}_q(2)$, see e.g. Chari--Pressley,
Chapter 10.  The
restriction to partitions with at most two parts reflects
$\mathrm{rank}(\mathrm{SU}(2)) = 1$: the Young diagrams are at most
two-rowed.

*Part (2).*  Alexander's theorem guarantees surjectivity of the
braid closure map $\beta \mapsto \hat{\beta}$.  The Markov trace on
$H_n(R, q)$ is the unique trace satisfying the Markov property
$\mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x)$ for
$x \in H_n(R, q)$ and a parameter $z$ determined by $q$ (the
$\sigma_n^{-1}$ stabilisation then carries the derived loop value
$z_{-} = z - (q - q^{-1})$).  On each
irreducible summand $S_\lambda$, the trace restricts to a non-zero
scalar multiple of the character, so every summand is detected by
some braid closure; the trivial braid already suffices, since
$\chi_\lambda(1) = \dim S_\lambda \neq 0$.

*Part (3).*  $V_{\mathrm{phys}} := \varinjlim V^{\otimes n}$ is
the algebraic direct limit along $\iota_n(x) = x \otimes v_0$ — the
union of its finite-dimensional subspaces $V^{\otimes n}$, each of which is completely decomposed
by (1) — and so the irreducible summands, indexed by the partitions
$\lambda$ with $\ell(\lambda) \le 2$, span $V_{\mathrm{phys}}$. The construction
remains within rigid algebraic categories without any metric
completion.
