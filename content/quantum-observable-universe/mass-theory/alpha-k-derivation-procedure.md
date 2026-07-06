**Setup.**
Working over $A = H_n(R, q)$ at generic $q$, with Markov parameter
$z = 1/(\sqrt q + 1/\sqrt q) \in R$.  Let $\{e_\lambda\}_{\lambda
\,\vdash\, n}$ be the central idempotents of the Wedderburn
decomposition.  The Jones–Markov trace
([Jones–Markov trace](#thm:jones-markov-trace)) admits a unique
expansion in central characters

$$
  \mathrm{tr}_M(\beta) \;=\; \sum_{\lambda \,\vdash\, n}
    y_\lambda \cdot \chi_\lambda(\beta),
  \qquad y_\lambda \in R,
$$

with $p(n) = \#\{\lambda \,\vdash\, n\}$ unknowns
$\{y_\lambda\}_{\lambda \,\vdash\, n}$.

**Proposition (linear-system characterisation of $y_\lambda$).**
*The Markov-trace property
$\mathrm{tr}_M(x \cdot T_n^{\pm 1}) = z^{\pm 1} \cdot
\mathrm{tr}_M(x)$, applied iteratively, fixes $\mathrm{tr}_M(w_\mu) =
z^{\,n - \mathrm{len}(\mu)}$ for every reduced word $w_\mu$ realising
the cycle type $\mu \vdash n$.  Substituting into the central
expansion yields the $p(n) \times p(n)$ linear system*

$$
  \sum_{\lambda \,\vdash\, n}
    \chi_\lambda(w_\mu)\, y_\lambda
  \;=\;
  z^{\,n - \mathrm{len}(\mu)},
  \qquad \mu \,\vdash\, n.
$$

*The character matrix $\bigl[\chi_\lambda(w_\mu)\bigr]_{\mu, \lambda}$
is invertible at generic $q$ (Schur–Weyl-Hecke duality), so the
system has a unique solution $y_\lambda \in R(\!(z)\!)$ — explicit,
$q$-rational, no fitting.*

**Formalization Goal Plausibility.** The current formalization proves the existence of a programmatic solution by effectively yielding `∃ y, y = solveJonesMarkov n S := ⟨_, rfl⟩`. The mathematical claim of *uniqueness* and *invertibility* of the character matrix is not yet fully formalized in Lean, as it requires a deep library of Schur-Weyl-Hecke duality and generic semisimple character theory. However, this gap is highly plausible to close because it is a standard, well-documented result in algebraic combinatorics (the non-degeneracy of the Hecke character table). The physical model relies on the existence of this unique derivation procedure, which is computationally verified, making the unformalized uniqueness a localized algebraic gap rather than a structural flaw in the mass theory.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
