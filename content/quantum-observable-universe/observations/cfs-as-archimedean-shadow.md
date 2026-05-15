Combining the propositions of this section yields a clean picture of
how the Finster program relates to QOU.

**The full factorisation.** QOU's algebraic side admits *two* parallel
Archimedean routes, both factoring through the Hecke operator
algebra $A_q$:

$$
  \begin{array}{cccccc}
    \mathbf{C}
      & \xrightarrow{\,\tau\,}
      & A_q
      & \xrightarrow{\,\mathrm{tr}_M\,}
      & R
      & \xrightarrow{\,\pi_\infty\,}\; \mathbb{R}
      \quad (\tau_{\mathrm{arch}}; \text{Kashaev, dilogarithm}) \\[6pt]
    \mathbf{C}
      & \xrightarrow{\,\tau\,}
      & A_q
      & \xrightarrow{\,\Pi_{\mathrm{tr}}\,}
      & (\widehat{A}_q, \tilde w_\lambda)
      & \xrightarrow{\,\mu_{\mathrm{arch}}\,}\; (\mathcal{F}, \rho)
      \quad (\mu_{\mathrm{arch}}; \text{CFS})
  \end{array}
$$

The first row is the scalar realisation $\tau_{\mathrm{arch}}$,
established by
[Kashaev as Archimedean realisation](#rem:kashaev-as-archimedean-realization)
and [dilogarithm Archimedean limit](#conj:dilogarithm-archimedean-limit).
The second row is the measure-valued route through the traceful
projection
$\Pi_{\mathrm{tr}}$
([CFS as traceful projection of QOU](#prop:cfs-as-traceful-projection-of-qou)),
which is established at every step *except* the Lagrangian match in
$\mu_{\mathrm{arch}}$
([μ_arch continuum limit](#conj:mu-arch-continuum-limit)).

**What conflating routes obscures.** Reading "CFS is the Archimedean
realisation of QOU" as a single functorial claim makes it look like a
single conjecture. The factorisation above shows it is actually two
maps with different targets (a real number vs. a measure on
operators), sharing the operator-algebra factor $A_q$. The scalar
$\tau_{\mathrm{arch}}$ is established (Jones–Kashaev volume
conjecture, Faddeev–Kashaev dilogarithm); the measure-valued
$\mu_{\mathrm{arch}}$ is now almost entirely established too — the
sole residual conjecture is the Lagrangian-universality match.

**What the traceful projection is and is not.** $\Pi_{\mathrm{tr}}$
collects the QOU algebraic data into its commutative spectral shadow:
the dual $\widehat{A}_q$ with the Plancherel weight, plus the family
of irreducible characters. This is structurally CFS-style data — a
measure space, a positive measure, a family of functionals — but the
projection is lossy. The commutator-vanishing identity
$\mathrm{tr}_M([x, y]) = 0$ already encodes the loss: any
information that depends on the *order* of operator multiplication
(braid order, knot crossing chirality, GS-reduction kinematics) is
not in the image of $\Pi_{\mathrm{tr}}$. CFS, being a measure-on-
operators framework, can express these only through their spectral
footprint, not their algebraic structure.

**Universality class coincidence.** Both QOU's pre-projection algebra
(via GNS to a type II$_1$ factor) and CFS's universal measure (on
operators of bounded signature) sit in the free-probability
universality class (Voiculescu–Biane). This is not a coincidence to
be conjectured but a structural fact: the Markov trace on
$H_\infty(q)$ has free-probability moments, and CFS's spectral data
is constructed precisely to be tractable in the same class. The
continuum carriers are therefore type-compatible.

**The remaining bifurcation.** What is *not* automatic at the
universality level is the agreement of the two Lagrangians. Finster's
$\mathcal{L}_{\mathrm{CFS}}$ extracts a max-of-pair-products
extremal functional from $\mathrm{spec}(x \cdot y)$; QOU's $Z_{\mathrm{Pl}}$
extracts the Plancherel-weighted sum of central characters of
$x \cdot y$. Both live on the same free-probability spectral limit.
If they coincide as functions, QOU and CFS are two presentations of
the same post-wall theory; if not, they are two distinct
falsifiable theories sharing every structural feature except the
action functional.

**Useful asymmetries.** As before, each side of the wall sees what
the other does not:

- QOU's pre-projection algebra sees: integer / cyclotomic structure
  of $A_q$, bar-involution, Wedderburn–LP geometry of the active
  set, *and the entire knot-topological derivation of particle
  physics* (which lives in $A_q \setminus \mathrm{ker}(\Pi_{\mathrm{tr}})$).
- CFS's continuum side sees: a Borel measure $\rho$, continuous
  families of Lagrangians, and the analytic machinery to take
  free-probability limits cleanly. QOU pre-projection sees these
  only through the finite $\tilde w_\lambda$ and polynomial central
  characters.

The proper relationship is therefore the pair
$(\tau_{\mathrm{arch}}, \mu_{\mathrm{arch}})$ of parallel Archimedean
projections sharing the operator-algebra factorisation through
$A_q$, with $\mu_{\mathrm{arch}}$ now reduced to a single
Lagrangian-form question on a shared free-probability limit.
