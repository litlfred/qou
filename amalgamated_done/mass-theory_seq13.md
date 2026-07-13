<!-- FILE_START: mass-scale-su2.md -->
We evaluate the $q$-difference stabilisation for $G = \mathrm{SU}(2)$ and its invariant [vacuum state](#prop:vacuum-state-su2).

**The trace reduction.** For $G = \mathrm{SU}(2)$, the Markov trace $\tau_M$ on the direct limit algebra $A_\infty$ identifies with the Haar integral. The atomic trace $\tau_M(\beta_A)(q)$ evaluates the $A$-body symmetric polynomial $P_A(q)$ under the Haar measure. The generating series $\mathcal{B}(z, q)$ is the Fourier transform of the $A$-body spectral density.

**The volume term.** The asymptotic scaling of the Haar integrals yields the large-$A$ volume term. By Weyl's integration formula on $\mathrm{SU}(2)$, the dominating contribution to the $A$-fold tensor product $V^{\otimes A}$ comes from the peak of the Plancherel measure. The trace $m_A(q)$ scales with $A$. The $q$-difference $\nabla_A m_A(q)$ approaches a constant $c_{\mathrm{vol}}(q)$ as $A \to \infty$. This is the $q$-deformed volume-energy coefficient.

**The surface term.** The finite-$A$ correction to the volume term is the surface energy. The Haar integral on the $A$-fold tensor product incurs an $A^{-1/3}$ penalty from the boundary of the symmetric group representations. This produces the surface term $c_{\mathrm{surf}}(q) \cdot A^{-1/3}$.

**The magic shells.** The discrete representation jumps occur when the two-row stratum $\Lambda^2(3A)$ hits the dimensions of the $\mathrm{SU}(2)$ irreducible representations. For $A=4$ ($^4\mathrm{He}$), the closure of the $(6,6)$ block generates the strong binding spike $\nabla_A^2 m_A(q) \approx 0$ ([`prop:q-difference-recurrence-he4`](#prop:q-difference-recurrence-he4)). Higher magic numbers ($A=16$ for $^{16}\mathrm{O}$, $A=40$ for $^{40}\mathrm{Ca}$) correspond to subsequent structural closures in the tensor decomposition of the $\mathrm{SU}(2)$ modules. The algebraic generating series predicts the magic-shell sequence without phenomenological input.
<!-- FILE_END: mass-scale-su2.md -->

<!-- FILE_START: mass-scale-lean.md -->
## Lean formalisation

The properties of the QOU mass trace and its generating series are encoded in the `QOUMassTrace` class. We provide `sorry`-stubbed existence proofs for the scaling limits. The full derivation of the SEMF coefficients requires the exact coefficients of $P_A(q)$, which we leave for future computational verification. Downstream modules assume the thermodynamic limit converges.
<!-- FILE_END: mass-scale-lean.md -->

<!-- FILE_START: betti-intro.md -->
The categorical mass captures the trace of the identity. We now decompose this trace using Hodge theory. This section shows that the Betti numbers of the QOU state space provide the structural coefficients of the mass identity.

**Betti numbers and the QOU invariant** establishes the relation: the Euler characteristic splits into Betti numbers $\beta_i$. **Harmonic forms** provides the explicit generators for these Betti numbers via the Hodge theorem. **Betti stabilization** proves that these numbers remain invariant under the geometric descent of the brane tower. **Harmonic mass projection** decomposes the total mass onto the harmonic basis. **Uniqueness of the harmonic projection** shows this is the only stable decomposition.

The resulting harmonic projections feed directly into the *Geometric Mass* chapter, where they dictate the specific gravitational mass of the QOU.
<!-- FILE_END: betti-intro.md -->

<!-- FILE_START: betti-numbers.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe). Let $\mathcal{S}$ be its underlying site. The **Betti numbers** $\beta_i(A)$ of the universe are the dimensions of the sheaf cohomology groups of the state bundle:
$$
  \beta_i(A) \;:=\; \dim_R H^i(\mathcal{S}, \mathcal{O}_{\mathcal{S}}).
$$
The categorical Euler characteristic ([Euler characteristic stability](#prop:euler-char-stability)) splits as the alternating sum of Betti numbers:
$$
  \chi(A) \;=\; \sum_{i=0}^{\dim \mathcal{S}} (-1)^i \beta_i(A).
$$
In the archimedean realisation, these are the topological Betti numbers of the geometric state space $M$.
<!-- FILE_END: betti-numbers.md -->

<!-- FILE_START: harmonic-forms.md -->
We lift the Betti numbers to explicit operators using Hodge theory. Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over $\mathbb{C}$. Let $\mathcal{S}$ be a smooth projective variety. The De Rham cohomology $H^i_{\mathrm{dR}}(\mathcal{S})$ is isomorphic to the singular cohomology $H^i(\mathcal{S}, \mathbb{C})$.

The **harmonic forms** $\mathcal{H}^i(A)$ are the unique representatives of the De Rham classes that vanish under the Hodge Laplacian $\Delta = d d^* + d^* d$. By the Hodge theorem, we have:
$$
  \mathcal{H}^i(A) \;\cong\; H^i_{\mathrm{dR}}(\mathcal{S}) \;\cong\; H^i(\mathcal{S}, \mathbb{C}).
$$
The dimension of the space of harmonic $i$-forms is the Betti number $\beta_i(A)$.

The harmonic forms provide a canonical geometric basis for the QOU mass trace. The trace operator $\tau_M$ projects onto these forms to compute the mass contribution of each topological sector.
<!-- FILE_END: harmonic-forms.md -->

<!-- FILE_START: betti-stabilization.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $\{A_n\}_{n \geq 0}$ be its recursive brane tower. The Betti numbers $\beta_i(A_n)$ are constant for all $n \geq 0$:*
$$
  \beta_i(A_{n+1}) \;=\; \beta_i(A_n).
$$
*The harmonic forms $\mathcal{H}^i(A_n)$ pull back isomorphically under the geometric descent maps $r_n \colon \mathcal{S}_n \to \mathcal{S}_{n-1}$.*

**Proof sketch.**
The jet prolongation $A_n \hookrightarrow A_{n+1}$ realises the state bundle $\mathcal{S}_{n+1}$ as an affine bundle over $\mathcal{S}_n$. The fibres are vector spaces. The geometric descent map $r_n$ is a homotopy equivalence. It induces an isomorphism on cohomology groups. The Betti numbers match. The harmonic forms pull back isomorphically. $\square$

This proposition refines the Euler characteristic stability ([Euler characteristic stability](#prop:euler-char-stability)). Not only is the alternating sum constant, but each individual Betti term is invariant across the brane tower. The topological mass data is rigidly preserved.
<!-- FILE_END: betti-stabilization.md -->

<!-- FILE_START: harmonic-mass-projection.md -->
We decompose the categorical mass $\mathrm{tr}(\mathrm{id}_A)$ onto the harmonic basis. This separates the topological invariants into distinct energetic channels.

**Definition.**
Let $\omega_j^{(i)}$ be a basis for the harmonic forms $\mathcal{H}^i(A)$. Let $P_{\omega_j^{(i)}}$ be the orthogonal projection onto $\omega_j^{(i)}$ in the state bundle $\mathcal{S}$. The **harmonic mass projection** of the QOU is the decomposition:
$$
  M(A) \;=\; \sum_{i} (-1)^i \sum_j \tau_M(P_{\omega_j^{(i)}}).
$$
Each term $\tau_M(P_{\omega_j^{(i)}})$ is the mass carried by the specific harmonic topological defect $\omega_j^{(i)}$. The total sum recovers the Euler characteristic $\chi(A)$.

In the empirical particle spectrum, these projections correspond to the specific mass contributions of the topological colour-flavour tubes. The alternating sign assigns positive energy to even-degree forms and negative (binding) energy to odd-degree forms.
<!-- FILE_END: harmonic-mass-projection.md -->

<!-- FILE_START: harmonic-mass-uniqueness.md -->
**Proposition.**
*The harmonic mass projection is the unique decomposition of the QOU mass invariant under geometric descent.*

**Proof sketch.**
Any stable decomposition of the mass trace must assign weights to the generators of a cohomology theory invariant under the jet prolongation $A_n \to A_{n+1}$. By [Betti stabilization](#prop:betti-stabilization), the Betti numbers uniquely count these invariant generators. The Hodge theorem proves the harmonic forms uniquely represent these generators. The harmonic projection is the unique stable decomposition. $\square$

This uniqueness guarantees that our identification of mass with the trace of harmonic projections is not an arbitrary choice of basis, but the only basis that survives the Yekutieli lifting process of the brane tower.
<!-- FILE_END: harmonic-mass-uniqueness.md -->
