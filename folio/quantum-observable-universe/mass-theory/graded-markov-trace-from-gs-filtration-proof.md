## Proof sketch

The Markov trace $\mathrm{tr}_M$ is uniquely characterised by its
cyclicity and Markov property
([Existence and non-degeneracy of the Markov trace (Jones, 1987)](#thm:jones-markov-trace)).  The GS
filtration $J^\bullet$ is two-sided
\cite{geckpfeiffer2000, mathas1999}, so for $T_1 \in J^a$,
$T_2 \in J^b$, $T_1 T_2 \in J^{a+b}$.  Cyclicity then implies that
$\mathrm{tr}_M(T_1 T_2) - \mathrm{tr}_M(T_2 T_1) = 0 \in
\mathbb{Q}(q)_{a + b}$, which is the right-hand grading at the
correct level. Hence the restriction of $\mathrm{tr}_M$ to $J^\ell$
descends to $J^\ell / J^{\ell+1}$ (any $T \in J^{\ell+1}$ has
$\mathrm{tr}_M(T) \in \mathbb{Q}(q)_{\ell+1}$, which is *strictly*
above the level $\ell$).  Uniqueness follows from the universal
property of the quotient.

The construction is purely algebraic — it makes no reference to
analytic continuation, complex evaluation, or roots of unity. The
companion block
[Cyclotomic residues of $\Phi_q \cdot \mathrm{tr}_{M, \ell}$](#prop:residue-at-root) supplies the
algebraic definition of the residues required to assemble the
GB-residue spectral sum
([GB-filtration spectral sequence and $E_\infty$ convergence of the 6-term mass](#prop:gb-spectral-sequence)).
