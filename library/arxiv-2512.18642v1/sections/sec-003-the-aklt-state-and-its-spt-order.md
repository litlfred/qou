---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain"
section_id: sec-003-the-aklt-state-and-its-spt-order
section_title: "The AKLT State and its SPT Order"
section_number: null
pages: 4-6
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.978
doc_brief: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af"
---
[]{#SbSect_AKLT label="SbSect_AKLT"}

The seminal work of Affleck, Kennedy, Lieb, and Tasaki [@Affleck1988] marked a watershed moment in quantum magnetism by furnishing an exactly solvable model that provided rigorous foundation for Haldane's conjecture regarding the existence of a spectral gap in antiferromagnetic spin-1 chains. The AKLT Hamiltonian, defined on a one-dimensional lattice with spin-1 degrees of freedom, embodies profound physical insights through its elegantly simple form: $$\hat{H}_{\text{AKLT}} = \sum_{\langle i,j \rangle} \left[ \vec{S}_i \cdot \vec{S}_j + \frac{1}{3} (\vec{S}_i \cdot \vec{S}_j)^2 \right],$$ where $\vec{S}_i = (S_i^x, S_i^y, S_i^z)$ are spin-1 operators satisfying $\mathfrak{su}(2)$ commutation relations $$[S^x, S^y]  = iS^z, \quad [S^y, S^z]  = iS^x, \quad [S^z, S^x]  = iS^y$$

The AKLT state is defined on a spin-1 chain, where the physical Hilbert space at each site is $\mathcal{H}_1 \cong \mathbb{C}^3$, spanned by the $S^z$-eigenbasis $\{|+\rangle, |0\rangle, |-\rangle\}$. Its construction relies on an auxiliary, virtual spin-½ space $\mathcal{H}_{\frac{1}{2}} \cong \mathbb{C}^2$ with the orthonormal basis $\{|\uparrow\rangle, |\downarrow\rangle\}$, which is projectively embedded into the physical spin-1 space.

The AKLT state admits a canonical MPS representation that exactly captures its entanglement structure. The fundamental objects are three local matrices $\{A_+, A_0, A_-\} \in \mathcal{M}_2(\mathbb{C})$ that mediate between the physical spin-1 space and the auxiliary spin-½ space:

$$\begin{aligned}
\label{eq:Ak}
A_{+} &= \sqrt{\frac{2}{3}} \, \sigma^{+}, &
A_{0} &= \sqrt{\frac{1}{3}} \, \sigma^{z}, &
A_{-} &= -\sqrt{\frac{2}{3}} \, \sigma^{-}
\end{aligned}$$

Here, the operators $\sigma^+$, $\sigma^-$, and $\sigma^z$ act on the virtual space $\mathbb{C}^2$, which is spanned by the basis vectors $|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $|\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$. Their explicit action is defined by the following outer products: $$\begin{aligned}
\sigma^+ &=   \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad
\sigma^- &=  \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma^z &=   \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\end{aligned}$$

For an $n$-site periodic chain, the AKLT state is constructed as the uniform MPS:

$$\label{eqAKLT}
|\psi_{\mathrm{AKLT}}^{(n)}\rangle = \sum_{k_1,\dots,k_n \in \{+,0,-\}} \mathrm{Tr}\left(A_{k_1} A_{k_2} \cdots A_{k_n}\right) |k_1 k_2 \cdots k_n\rangle$$

<figure id="fig1">

<figcaption>Schematic diagram with eight qubits on the top row, grouped pairwise into singlet states (dashed ellipses), and projected downward into three spin-<span class="math inline">1</span> triplet nodes on the lower row. The increased vertical spacing highlights the correspondence between the two levels.</figcaption>
</figure>

Figure [1](#fig1){reference-type="ref" reference="fig1"} illustrates how pairs of spin-½ particles can be combined to form an effective spin-$1$ degree of freedom. At the lower level, the red circles grouped in ellipses represent the tensor product space $\mathcal{H}_{\frac{1}{2}} \otimes \mathcal{H}_{\frac{1}{2}}$, which naturally decomposes into a three-dimensional triplet sector and a one-dimensional singlet sector. The upper blue circles correspond to the symmetric triplet space, which carries the spin-$1$ representation.

The projection $P: \mathcal{H}_{\frac{1}{2}} \otimes \mathcal{H}_{ \frac{1}{2}} \to \mathcal{H}_{1}$ implements the Clebsch-Gordan decomposition $\frac{1}{2} \otimes \frac{1}{2} = 1 \oplus 0$: $$P = |+\rangle \langle \uparrow \uparrow| + |-\rangle \langle \downarrow \downarrow| + |0\rangle \frac{1}{\sqrt{2}}\left( \langle \uparrow \downarrow| + \langle \downarrow \uparrow| \right).$$ This projection satisfies $P^\dagger P = \Pi_{\text{sym}}$ and $PP^\dagger = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1}}$, establishing an isometric embedding that encodes the Haldane phase through its entanglement structure. Quantum channels channels are fundamental objects in the analysis of the AKLT model. The AKLT channel is defined on $\mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \equiv \mathbb{M}_2(\mathbb{C})$ as: $$\label{eq:aklE_channel}
    \Phi_{\mathrm{AKLT}}(Z) = \sum_{k \in \{+,0,-\}} A_k Z A_k^\dagger.$$

The quantum channel $\Phi_{\mathrm{AKLT}}$ is bi-stochastic: it is both trace-preserving $\operatorname{Tr}(\Phi_{\mathrm{AKLT}}(Z)) = \operatorname{Tr}(Z)$ and identity-preserving $\Phi_{\mathrm{AKLT}}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{1/2}}) = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1/2}}$. When interpreted as a transfer matrix within the valence-bond-solid formalism, its spectral structure dictates the system's correlation functions: the largest eigenvalue is unity, while the second largest eigenvalue in magnitude, $\lambda_2$, sets the dominant correlation length via $\xi^{-1} = -\ln |\lambda_2|$ [@Pollmann2012]. The contractive nature of the channel upon iteration, a direct consequence of this spectral gap, underpins the mixing behavior and the exponential decay of correlations characteristic of the gapped phase of the AKLT state [@SA25].

Let $G$ be a subgroup of the special orthogonal group in three dimensions $G = \mathrm{SO}(3)$, which constitutes our symmetry group. This group acts on the physical and virtual spaces of our system via distinct unitary representations. The physical Hilbert space is $\mathcal{H}_{1}$, on which $G$ acts via the fundamental, integer-spin representation $\rho: G \to \mathcal{U}(\mathcal{H}_{\frac{1}{2}})$, which is isomorphic to the spin-1 representation. The virtual, or auxiliary, Hilbert space is $\mathcal{H}_{\frac{1}{2}}$, where $G$ acts via the projective spin-½ representation $\pi: G \to \mathcal{U}(\mathcal{H}_{\frac{1}{2}})$. This representation $\pi$ is projective, meaning it satisfies the composition rule $\pi(g_1)\pi(g_2) = \omega(g_1,g_2)\pi(g_1g_2)$ for all $g_1, g_2 \in G$, with a non-trivial cocycle $\omega: G \times G \to \mathrm{U}(1)$. The cohomology class $[\omega]$ is a non-trivial element of the second group cohomology $H^2(\mathrm{SO}(3),\mathrm{U}(1))$, which is isomorphic to $\mathbb{Z}_2$, thereby encoding the double-cover relationship between $\mathrm{SO}(3)$ and $\mathrm{SU}(2)$ [@Chen2011b].

A crucial property of the AKLT state, which guarantees its non-trivial SPT phase [@AKLT1987], is the exact intertwining relation between the virtual representation $\pi$ and the physical representation $\rho$. This relation is mathematically expressed as follows: For every $g \in G$ and for every $k \in \{+, 0, -\}$, The MPS tensors $\{A_{k'}\}$ satisfy the following covariance relation: $$\label{eq:Cov}
    \sum_{k'} \rho(g)_{k k'} A_{k'} = \pi(g) A_k \pi(g)^\dagger$$ where $\rho(g)_{kk'} = \langle k | \rho(g) |k' \rangle$ denotes the matrix element of the operator $\rho(g)$. This equation means that a symmetry transformation $g$ applied to the physical index of the tensor is equivalent to a conjugation of the virtual operators by the projective representation $\pi(g)$ [@Pollmann2010].

The symmetry action extends naturally to the dihedral group $D_2 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, a finite subgroup of $\mathrm{SO}(3)$ consisting of $\pi$-rotations about three orthogonal axes. This subgroup is a key symmetry of the AKLT Hamiltonian. The non-triviality of the SPT phase under this $D_2$ symmetry is detected by the Ogata index [@Tas23], a $\mathbb{Z}_2$-valued topological invariant. For a translation-invariant MPS that is invariant under the dihedral group $D_2 = \{e, g_x, g_y, g_z\}$ (the group of $\pi$-rotations about orthogonal axes), the SPT phase is classified by a $\mathbb{Z}_2$ index. This index is determined by the projective commutation relation of the symmetry actions on the virtual space.

Let $U_g$ be the unitary operators implementing the symmetry $g \in D_2$ on the physical spin-1 space. For the generators $g_x$ and $g_y$, the projective algebra is: $$U_x^2 = \eta_x I, \quad U_y^2 = \eta_y I, \quad U_x U_y = \eta_{xy} U_y U_x,$$ with $\eta_x, \eta_y, \eta_{xy} \in \{\pm 1\}$. The $\mathbb{Z}_2$ index characterizing the SPT phase is given by $\theta = \eta_{xy}$.

For the AKLT state, with virtual space dimension $d=2$, one finds $\eta_x = \eta_y = +1$ but $\eta_{xy} = -1$, yielding the non-trivial index $\theta = -1$. This value is a topological invariant, which can be computed via the gauge-invariant formula: $$\theta = \frac{1}{d} \mathrm{Tr}(U_x U_y U_x^\dagger U_y^\dagger).$$ Substituting $d=2$ and $U_x U_y U_x^\dagger U_y^\dagger = -I$ for the AKLT state confirms $\theta = -1$ [@Pollmann2010; @Pollmann2012].
