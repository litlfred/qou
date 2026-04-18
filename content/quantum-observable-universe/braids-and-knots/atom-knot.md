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
  \;\in\; S_{n(K)},
$$

*where:*

- *$n(K) = $ braid index of $K$ (minimum strand count over braid
  representatives).  For a $(Z, N)$ atom built from Borromean
  baryons on $3$ strands each plus inter-nucleon connectors,
  $n(K) = 3(Z+N)$.*
- *$w_{q^Z} \in S_{n(K)}$ is the **proton-quark block**: the product
  of $Z$ permutations, each realising the Borromean baryon NF for
  one $\mathfrak{u}\mathfrak{u}\mathfrak{d}$ proton-quark substructure
  on a disjoint $3$-strand block of $\{1, \ldots, n(K)\}$.*
- *$w_{\bar q^N}$ is the **neutron-quark block**: $N$ disjoint
  Borromean NFs for $\mathfrak{u}\mathfrak{d}\mathfrak{d}$
  neutron-quark substructures.*
- *$w_{\mathrm{inter}}$ is the **inter-nucleon connector**: a
  permutation realising the pp, nn, pn crossings between the
  $Z + N$ disjoint baryon blocks ([atomic
  braid](#def:atomic-braid)).*

*The decomposition is unique up to NF rewriting (Diamond Lemma) —
no positional or temporal ordering is imposed beyond the
shortlex-canonical NF.*

**Atom is a knot.**
*The atom is the closed braid $\hat K = \hat\beta$ obtained by
Markov closure of any braid representative $\beta$ realising $T_w$.
Markov-trace invariance ([Jones–Markov trace](#thm:jones-markov-trace))
guarantees that $\hat K$ is a well-defined knot/link in $S^3$
independent of the choice of $\beta$.  No phase or temperature
data enters the definition — the atom is a topological object.*

**Phase, dynamics, evolution** are separate structures defined on
the space of atom-knots — they are NOT part of the atom's definition
itself.  The same atom $K$ may exhibit different confinement
levels at different $q$
([confinement level](#def:confinement-level)), but $K$ itself is
$q$-independent.
