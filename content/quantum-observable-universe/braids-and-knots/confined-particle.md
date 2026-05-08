**Definition.**
*A **confined particle** is a tuple*

$$
  P \;=\; (\mathrm{name},\ \ell,\ [K]_M,\ n_0)
$$

*where:*

1. *$\mathrm{name}$ is a symbol drawn from a fixed registry of
   particle shortcuts — e.g. `quark`, `proton`, `neutron`,
   `electron`, `\He4`, `\C12`, `\benzene`. (The shortcut registry
   is authoring sugar; a formal `def:particle-shortcut` block is
   deferred and is not required for the mathematical content of
   this definition.);*

2. *$\ell \in \mathbb{Z}_{\ge 0}$ is the **confinement level**
   (quark = 0, nucleon = 1, atom = 2, molecule/compound = 3, …);*

3. *$[K]_M$ is the **Markov-equivalence class** of a closed braid
   $K$ — i.e. the class of $K$ under braid-group conjugation and
   Markov stabilisation.  It is represented canonically by the
   **Gröbner–Shirshov normal form** of its associated Hecke element
   $T_w \in H_{n_0}(q)$;*

4. *$n_0$ is the **coarse strand count** at level $\ell$: the
   minimal number of strands needed to express $K$ as a closed
   braid at its own level, independent of any deeper unfolding.*

*The class $[K]_M$ is **not required to be confined at any
particular $q$**: confinement is a $q$-indexed predicate
$\mathrm{confined}(P, q)$ that holds iff the matrix Frobenius
PSD cone admits a feasible $\Phi^* \succeq 0$
([confinement SDP](#prop:confinement-sdp)).  A confined
particle is **stable at $q$** iff it is additionally
Frobenius-non-degenerate there ([topological
confinement](#prop:confinement-topological)).  Unstable species
(e.g. $^3\mathrm{H}$, transient hadronic resonances) are
confined particles for all $q$ in the generic locus even though
their decay channels are open.*

**Canonical representative.**
*Among all closed-braid words in $[K]_M$, the one with shortlex-minimal
Gröbner–Shirshov normal form is chosen as the canonical representative
$\mathrm{GS}(P)$.  The witness data $k_{\max}(P, q)$
([confinement level](#def:confinement-level)) is computed on this
representative.  Two particles are equal iff their names are equal iff
$\mathrm{GS}(P_1) = \mathrm{GS}(P_2)$.*

**Examples.**

- *`quark`: $\ell = 0$, $n_0 = 1$, $[K]_M = [\sigma_0]$ in $H_1(q)$.*
- *`neutrino`: $\ell = 0$, $n_0 = 1$,
  $[K]_M = [\mathbf{1}]$ (unknot $0_1$, no crossings).
  Confined and stable at $q_0$ (vacuum-drag particle); the
  Frobenius-PSD cone is satisfied trivially since
  $\Phi^* = \mathbf{1} \succeq 0$.*
- *`photon`: $\ell = 0$, $n_0 = 4$,
  $[K]_M = [\mathbf{1}_{B_4}]$ — four-strand identity in $B_4$
  (no crossings; four polarisation × chirality components on the
  exceptional divisor $\mathcal{S}_p$).  Confined at $q_0$ via
  the Reeb-bundle holonomy
  ([breit-wheeler-vertex](#rem:breit-wheeler-vertex));
  see notation discussion in
  [knot-particle-dictionary](#rem:knot-particle-dictionary)
  Table 3.*
- *`proton`: $\ell = 1$, $n_0 = 3$,
  $[K]_M = [B_3(\mathrm{uud})]$ with crossing types $(pp, pn, pn)$.*
- *`neutron`: $\ell = 1$, $n_0 = 3$, $[K]_M = [B_3(\mathrm{udd})]$.*
- *`electron`: $\ell = 1$, $n_0 = 2$,
  $[K]_M = [\sigma_1^3]$ (trefoil $3_1$).*
- *`\He4`: $\ell = 2$, $n_0 = 4$ nucleons, $[K]_M$ determined by
  the canonical ILP ground-state configuration for $(Z,N)=(2,2)$.*
- *`\benzene`: $\ell = 3$, $n_0 = 6$ atom-strands (six C-atoms
  in aromatic ring).*
