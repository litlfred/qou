**Conjecture (Entropic--area identification on the exceptional divisor).**

*Let $\mathcal{E}_q$ denote the exceptional divisor of the cluster
resolution at the substrate parameter $q$.  Then there exists a
canonical area form $\omega_q$ on $\mathcal{E}_q$ such that*

$$
  \tau(C_{\dim_q}) \;=\; \frac{1}{4 \, \mathrm{Area}_{\omega_q}(\mathcal{E}_q)}
  \cdot S_{\mathrm{ent}}(\mathcal{E}_q),
$$

*where $S_{\mathrm{ent}}(\mathcal{E}_q)$ is the entanglement
entropy of the substrate state across $\mathcal{E}_q$
([universal Frobenius co-dimension](#thm:frobenius-codim-universal),
[entropic gravity remark](#rem:entropic-gravity)).  This is the
holographic / Bekenstein--Hawking analogue: the categorical channel
sum $\sum 1/\dim_q(\lambda)$ is interpreted as the area of a
codimension-2 surface in the substrate, with the $\dim_q(\lambda)$
playing the role of horizon-mode degeneracies.*

**Physical reading.**  The substrate cost
$m_e \cdot \tau(C_{\dim_q})$ is the energy stored in the
exceptional divisor's area, and the limit
$\tau \to 2$ as $q \to 0^+, \infty$ corresponds to the divisor
collapsing to its **two self-dual fixed points** — the symmetric
$(n)$ and antisymmetric $(1^n)$ partitions — which form a
two-atom horizon.

**Status.** Open and the most speculative of the three.  Unlike
the Shannon-channel ([Shannon conjecture](#conj:tau-codim-shannon))
and Landauer ([Landauer conjecture](#conj:tau-codim-landauer))
candidates, this reading requires an explicit identification of
$\mathcal{E}_q$ with a codimension-2 spacelike surface — a
geometric structure that the categorical formalism does not
manifestly provide.

**Proof sketch.**

*Strategy.*  Three structural identifications are required:

1. **Geometrise the exceptional divisor.**  Show that $\mathcal{E}_q$
   ([Descartes elliptic curve](#prop:descartes-elliptic-curve)) carries
   a canonical area form $\omega_q$ such that
   $\mathrm{Area}_{\omega_q}(\mathcal{E}_q)$ is finite and depends
   smoothly on $q$.

2. **Identify the entanglement entropy.**  Define the substrate
   state $\rho_q$ on the categorical Hilbert space; compute the
   reduced density matrix $\rho_q^{\mathcal{E}_q}$ obtained by
   tracing over modes localised away from $\mathcal{E}_q$; show
   $S_{\mathrm{ent}} = -\mathrm{Tr}(\rho_q^{\mathcal{E}_q} \log
   \rho_q^{\mathcal{E}_q})$ is finite.

3. **Establish the area law.**  Prove
   $S_{\mathrm{ent}} = 4 \, \mathrm{Area}_{\omega_q}(\mathcal{E}_q)
   \cdot \tau(C_{\dim_q})$.

*What needs to be proved.*

- **(A1)** A canonical area form $\omega_q$ on the exceptional
  divisor exists and is uniquely determined (up to normalisation)
  by the substrate's Frobenius structure.
- **(A2)** The substrate state $\rho_q$ admits a well-defined
  bipartition across $\mathcal{E}_q$.
- **(A3)** The entanglement entropy obeys an area law with
  prefactor $\tau(C_{\dim_q})$ — i.e., the channel sum $\sum
  1/\dim_q(\lambda)$ is the *coefficient* in the area law, not a
  derived quantity.
- **(A4)** The self-dual limit $q \to 0, \infty$ corresponds
  geometrically to the divisor collapsing to two points (the
  symmetric and antisymmetric partitions).

*Obstructions.*  (A1) requires a Kähler structure on
$\mathcal{E}_q$ that is canonically determined by the substrate
parameter $q$ alone — no such canonical structure has been
identified in this paper.  The Weierstrass form
$\wp_q$ on $\mathcal{E}_q$ supplies a candidate
$\omega_q = i \, d\wp_q \wedge d\bar{\wp}_q$, but its
normalisation is not obviously tied to the Frobenius structure.

(A3) is the deepest obstruction: it requires a categorical
analogue of Ryu--Takayanagi, which would need a holographic
duality between $\mathbf{Rep}(H_n(q))$ and a bulk geometry.  This
is well beyond what the present formalism establishes.

*Anticipated form.*  If a canonical Kähler form $\omega_q$ exists,
the area-law coefficient would be expected to equal
$\tau(C_{\dim_q})$ via the Wedderburn block decomposition: each
block $\lambda$ contributes a horizon mode with degeneracy
$\dim_q(\lambda)$, and the area-law prefactor is
$\sum 1/\dim_q(\lambda)$ by a Cardy-type counting argument.

**Verification path.**  No direct numerical verification is
available without first solving (A1).  The most accessible test
would be checking that the *limit structure* $\tau \to 2$ at
$q \to 0, \infty$ matches a geometric collapse of $\mathcal{E}_q$
to two points — a check that requires explicit construction of
$\omega_q$.  Until (A1) is solved, this conjecture remains the
most aspirational of the three.
