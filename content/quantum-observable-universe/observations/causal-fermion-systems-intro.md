Finster's causal fermion systems (CFS) [`finster2021`, `finster2022`,
`finster2024`, `dappiaggi2024`] are a parallel program for unifying
quantum field theory with general relativity via a universal measure
$\rho$ on operators of bounded signature, minimising a causal action
$\mathcal{S} = \iint \mathcal{L}_{\mathrm{CFS}}\,d\rho\,d\rho$.

Using the non-commutative probability framework of the previous
section, the relationship between QOU and CFS is now explicit:

- **Same carrier algebra**: both are type II$_1$ factors with
  faithful trace ([algebraic GNS embedding](#prop:algebraic-gns-embedding)).
- **Same universality class**: free probability under asymptotic
  scaling
  ([q-Plancherel asymptotic skeleton](#prop:q-plancherel-asymptotic-skeleton);
  Voiculescu–Biane, Féray–Méliot).
- **Different action functionals**: CFS uses a non-linear,
  spectral-difference-extremal Lagrangian; QOU uses the bilinear
  Frobenius Gram kernel $G(x, y) = \mathrm{tr}_M(x \cdot y)$
  ([prop:qou-continuum-kernel-is-frobenius-gram](#prop:qou-continuum-kernel-is-frobenius-gram)).

Two propositions refute the "QOU = CFS in the limit" hypothesis. The
strict-match version fails at $n = 2$ on the unit pair:
$G(1, 1) = 1$ while $\mathcal{L}_{\mathrm{CFS}}(1, 1) = 0$
([prop:mu-arch-strict-match-fails-at-n2](#prop:mu-arch-strict-match-fails-at-n2)).
The integral-match version fails under any centered free-probability
limit by a parity argument
([prop:mu-arch-integral-match-symmetry-obstruction](#prop:mu-arch-integral-match-symmetry-obstruction)).

What remains is the algebraic decomposition
$\mathcal{L}_{\mathrm{CFS}} = n \cdot G_2 - \lVert x \cdot y\rVert_1^{\,2}$
([prop:even-kernel-modification-g2](#prop:even-kernel-modification-g2)),
which identifies CFS's action as QOU's energy-quadratic
$G_2 := \mathrm{tr}_M((xy)^2)$ minus an explicit trace-class
correction. The two frameworks are distinct continuum theories of the
same operator-algebra substrate, related by a known kernel difference
rather than by an asymptotic equivalence. The narrow residual
conjecture
([conj:mu-arch-continuum-limit](#conj:mu-arch-continuum-limit))
asks whether the correction integral
$\langle \lVert x \cdot y\rVert_1^{\,2}\rangle_{\rho_\infty}$ might
coincidentally vanish at $q_0$ — generically expected to be
non-zero.
