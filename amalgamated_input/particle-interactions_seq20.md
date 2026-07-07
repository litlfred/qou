<!-- FILE_START: intro-atom-isotope-knots.md -->
An atom constitutes a categorical knot in the substrate. Its defining braid word encodes exact proton and neutron counts. An isotope represents the same atomic-number knot but employs an altered braid-word presentation for the neutron component. This section assigns each $(Z, N)$ pair a canonical knot in the categorical knot category and proves this assignment is faithful.

We proceed from definition to taxonomy. We define atom-knots and isotope-knots, and we prove the uniqueness of their assignment. We then survey small-$Z$ cases (hydrogen, helium, lithium) by comparing them to explicit braid words computed in the appendix. This yields a total mapping $\{(Z, N)\} \to \{\text{atom-knots}\}$. The atomic-mass appendix consumes this mapping wholesale, connecting substrate-level categorical predictions directly to empirical CODATA values.
<!-- FILE_END: intro-atom-isotope-knots.md -->

<!-- FILE_START: atom-knot.md -->
**Definition.**
*An **atom of type $(Z, N)$** is a closed braid $K$ whose
Gröbner–Shirshov normal form
([Hecke normal form](#def:hecke-normal-form)) in $H_{n(K)}(q)$
admits a block decomposition:*

$$
  T_w
  \;=\;
  T_{w_{q^Z}} \;\cdot\; T_{w_{\bar q^N}} \;\cdot\; T_{w_{\mathrm{inter}}},
  \qquad
  w \;=\; w_{q^Z} \cdot w_{\bar q^N} \cdot w_{\mathrm{inter}}
  \;\in\; S_{n(K)}.
$$

*The components are:*

- *$n(K)$ is the braid index of $K$ (the minimum strand count over braid
  representatives). For a $(Z, N)$ atom built from Borromean
  baryons on $3$ strands each plus inter-nucleon connectors,
  $n(K) = 3(Z+N)$.*
- *$w_{q^Z} \in S_{n(K)}$ is the proton-quark block. It is the product
  of $Z$ permutations. Each permutation realizes the Borromean baryon normal form for
  one $\mathfrak{u}\mathfrak{u}\mathfrak{d}$ proton-quark substructure
  on a disjoint $3$-strand block of $\{1, \ldots, n(K)\}$.*
- *$w_{\bar q^N}$ is the neutron-quark block. It consists of $N$ disjoint
  Borromean normal forms for $\mathfrak{u}\mathfrak{d}\mathfrak{d}$
  neutron-quark substructures.*
- *$w_{\mathrm{inter}}$ is the inter-nucleon connector. This
  permutation realizes the pp, nn, and pn crossings between the
  $Z + N$ disjoint baryon blocks ([atomic
  braid](#def:atomic-braid)).*

*The decomposition is unique up to normal form rewriting (by the Diamond Lemma).
No positional or temporal ordering is imposed beyond the
shortlex-canonical normal form.*

**The atom is a knot.**
*The atom is the closed braid $\hat K = \hat\beta$ obtained via
the Markov closure of any braid representative $\beta$ that realizes $T_w$.
Markov-trace invariance ([Jones–Markov trace](#thm:jones-markov-trace))
guarantees that $\hat K$ forms a well-defined knot or link in $S^3$,
independent of the choice of $\beta$. No phase or temperature
data enters the definition. The atom represents a purely topological object.*

Phase, dynamics, and evolution represent separate structures defined on
the space of atom-knots. They do not enter the atom's definition.
The same atom $K$ may exhibit different confinement
levels at different $q$
([confinement level](#def:confinement-level)), but $K$ itself remains
independent of $q$.
<!-- FILE_END: atom-knot.md -->

<!-- FILE_START: atom-knot-exists.md -->
**Proposition.**
*For any pair $(Z, N) \in \mathbb{N}_{\geq 0}^2$ with $Z + N \geq 1$,
the [atom-knot](#def:atom-knot) of type $(Z, N)$ exists as a closed
braid in $H_{3(Z+N)}(q)$ on the generic locus.*
<!-- FILE_END: atom-knot-exists.md -->

<!-- FILE_START: atom-knot-unique.md -->
**Proposition.**
*The atom-knot of type $(Z, N)$ is unique up to Markov
equivalence of braid representatives.*

*Suppose $\beta_1$ and $\beta_2$ are two braids in $B_{n(K)}$ that both realize
the normal form block decomposition $T_w = T_{w_{q^Z}} \cdot T_{w_{\bar q^N}}
\cdot T_{w_{\mathrm{inter}}}$ ([atom-knot](#def:atom-knot)). Then
their Markov closures are isotopic in $S^3$:*

$$
  \hat\beta_1 \;\cong_{\mathrm{isotopy}}\; \hat\beta_2.
$$
<!-- FILE_END: atom-knot-unique.md -->

<!-- FILE_START: isotope-knot.md -->
**Definition.**
*Two atom-knots ([atom](#def:atom-knot)) $K_1, K_2$ of types $(Z, N_1)$ and $(Z, N_2)$ with $N_1 \neq N_2$ are **isotopes** iff their NF block decompositions agree on the proton-quark block:*

$$
  T_{w_1} \;=\; T_{w_{q^Z}} \cdot T_{w_{\bar q^{N_1}}^{(1)}} \cdot T_{w_{\mathrm{inter}}^{(1)}},
  \qquad
  T_{w_2} \;=\; T_{w_{q^Z}} \cdot T_{w_{\bar q^{N_2}}^{(2)}} \cdot T_{w_{\mathrm{inter}}^{(2)}},
$$

*with **identical $w_{q^Z}$**.*

*The isotope relation is an equivalence on $\{\text{atom-knots with fixed } Z\}$. The relation is reflexive ($K \sim K$), symmetric, and transitive (both share $w_{q^Z}$). The isotope class of $K$ at fixed $Z$ is parameterized by the neutron-quark block $w_{\bar q^N}$ and the inter-nucleon connector $w_{\mathrm{inter}}$.*

**Two isotopes are knot-distinct.**
*The Markov closures of $T_{w_1}$ and $T_{w_2}$ generally have different Jones polynomials whenever $N_1 \neq N_2$. The neutron-quark blocks contribute distinct Hecke generators. Isotopes are therefore distinct knots, not the same knot at different substrate parameters.*

**Stability per isotope is independent.**
*The LP-dual ILP-feasibility ([stable atom](#def:stable-atom)) is computed on the full NF $T_w$. This includes the $w_{\bar q^N}$ and $w_{\mathrm{inter}}$ blocks. Thus, different isotopes can have different stabilities at the same $q$ ([unstable atom](#def:unstable-atom)). This is the categorical analogue of the classical observation that ${}^{12}\mathrm{C}$ is stable while ${}^{14}\mathrm{C}$ is not.*
<!-- FILE_END: isotope-knot.md -->

<!-- FILE_START: isotope-knot-equivalence.md -->
**Proposition.**
*The [isotope](#def:isotope-knot) relation is an equivalence on
$\{\text{atom-knots with fixed } Z\}$.*
<!-- FILE_END: isotope-knot-equivalence.md -->

