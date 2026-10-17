---
doc_id: arxiv-1012.5432v4
doc_title: "quant-ph Towards Topological Quantum Computation? -"
section_id: sec-004-2-two-dimensions
section_title: "Two Dimensions"
section_number: 2
pages: 14-21
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.985
---
***Indistinguishable Particles: Braid Group*** On the other hand, in two dimensions the fundamental group of the configuration space of a system of $n$ identical particles is given by the more general braid group: $$\pi_1(C_n(\mathbb{R}^2)) \simeq B_n(\mathbb{R}^2) = \langle \sigma_i,  1 \leq i \leq n-1 | \sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1},$$ $$\sigma_i \sigma_j = \sigma_j \sigma_i \forall |i-j| \geq 2 \rangle .$$ The $\sigma_i$ are defined physically by interchanging the $i^{th}$ and $(i+1)^{st}$ particles counterclockwise. In contrast to the symmetric group, not all braid group generators satisfy $\sigma_i^2 = Id$. The monodromy operator/$R^2$ matrix is defined as the square of the braiding operator/R matrix.

Intuitively, two dimensional space allows for more possibilities because particles are topologically pointlike. Adding a particle to a 2D surface is like poking a hole in the surface, so loops around the hole can no longer be continuously deformed to a single point. (Note that our motivational Aharonov-Bohm effect example simulates 2D as the solenoid is infinite in length, so only 2 of the dimensions really matter. This corresponds to the fact that the loops around a line are characterized by the fundamental group (first homotopy group), $\pi_1(\mathbb{R}^2 \setminus line) = \pi_1(S^1 \times \mathbb{R}) = \mathbb{Z}$.)

***Truncated Braid Group*** The braid group as defined is infinite and torsion-free (all elements of the group have infinite order). For theories with a finite symmetry group, it is actually the truncated braid group $B(m,n)$, that governs the interaction of particles. These are the braid groups on $n$ elements with the additional condition that $\sigma^m=1$ for some finite $m$ ($m$ is taken to be minimal. $m=2$ corresponds to the case of $S_n$, so the truncated braid group is indeed a generalization of the symmetric groups.) When $\sigma$ acts on physical particles, the Hamiltonian transforms as a representation of $\sigma$ (the braid operator), which we call the $R$ matrix. (More on this topic will be discussed in the next section.)

***Distinguishable Particles: Colored (Pure) Braid Group*** If the particles are distinguishable, the configuration space is given by $C((\mathbb{R}^2)^n - D)$. The colored (pure) braid group $P(m,n)$, for $n$ even, describes the fundamental group of the configuration space of the underlying manifold. (Intuitively, only monodromy operators make sense since after each exchange the two particles have to be back in their original positions.) Formally, the pure braid group $P(m,n)$ is the kernel of the homomorphism $\phi: B_n \rightarrow S_n$ mapping each braid to the associated corresponding permutation.

***Partially Colored Braid Group*** If the system consists of a combination of distinguishable particles and indistinguishable particles, then the fundamental group is the partially colored braid group.

# Spin-Statistics Connection

## The Abelian Case

The topological approach to proving the spin-statistics connection ( [@prop])

that depends only on the existence of antiparticles and Lorentz invariance is useful when considering the spins of particles in 2 dimensions.

(This proof was originally proposed by Finkelstein and Rubinstein in the case of three spatial dimensions, then adapted to the two dimensional case by Propitius de Wild. [@prop]) Consider the process in which two particle/antiparticle pairs are created from the vacuum, the particles are interchanged, then the new pairs annihilate. The associated spacetime ribbon can be deformed via Lorentz transformations into the ribbon for rotation of a single one of the particles by an angle of $2 \pi$ about its center, as can be seen from diagram \[2\]. Thus from the topological perspective, these two processes are seen to be physically equivalent.

<figure id="fig:SpinStatistics">
<img src="SpinStatisticsConnection.jpg" style="width:15cm;height:10cm" />
<figcaption>Note that the effect of interchanging two particles in two separate particle/antiparticle pairs can be continuously deformed into the process under which one of the particles is rotated by an angle of <span class="math inline">2<em>π</em></span> about its center. Thus the two effects should be topologically the same.</figcaption>
</figure>

Thus the statistical phase factor $e^{i \theta}$ picked up by exchanging the two particles must in fact be equal to the spin factor $e^{2\pi i s}$ obtained by rotating a particle of spin $s$. Note that the procedure in the above proof is independent of whether the particles or the antiparticles are interchanged (the same orientation results either way). Thus as an additional consequence we obtain that the spin of the antiparticle is equal to that of the corresponding particle.

## The Non-Abelian Case: Generalized Spin-Statistics Connection

When the group is non-abelian, the canonical spin statistics connection must be generalized as the topological equivalence in Fig.\[3\] shows. Specifically, when a composite particle C (the result of fusion of A and B) is rotated, not only is the phase of the composite picked up, but each of the constituents A and B are also rotated. Thus both A and B must both be rotated back in the opposite direction, each picking up a phase.

$$K_{\alpha \beta \gamma}^{ABC} R^2 = e^{2 \pi i (s_{(C, \gamma)}-s_{(A, \alpha)}-s_{(B, \beta)})} K^{ABC}_{\alpha \beta \gamma}$$

<figure id="fig:GenSpinStatistics">
<img src="GenSpinStatistics.jpg" style="width:15cm;height:10cm" />
<figcaption>The Generalized Spin-Statistics Connection applies to two particle fusion in non-abelian theories. On the left, fusion is performed after a monodromy operation. This can be continuously deformed via Lorentz transformations to the diagram on the right, in which the particles are each twisted by a <span class="math inline"> − 2<em>π</em></span> rotation before being fused, then the fusion product is twisted by <span class="math inline">2<em>π</em></span>.</figcaption>
</figure>

When the two particles are the same, a square root version of the generalized Spin-Statistics Connection is satisfied:

$$K_{\alpha \alpha \gamma}^{AAC} R = \epsilon e^{\pi i (s_{(C,\gamma)}-2s_{(A, \alpha)})} K_{\alpha \alpha \gamma}^{AAC}$$

# Determining the Particles from the Hamiltonian

## Abelian

Consider the following action for a minimally coupled scalar field with an Abelian symmetry group:

$$S = S_{YMH} + S_{matter} = \int d^3 x (-\dfrac{1}{4} F_{\mu \nu} F^{\mu \nu} + (D^{\mu} \Phi)^* D_{\mu}\Phi - V(|\Phi|) - j^{\mu}A_{\mu} )$$ where the covariant derivative is given by $D_{\rho} \Phi = (\partial_{\rho} + i N e A_{\rho}) \Phi$ (i.e. the Higgs field has charge $Ne$ with respect to the compact $U(1)$ symmetry). The last term represents the contribution from the matter fields while the others are the Yang-Mills-Higgs contribution. Terms in the Lagrangian density that can be written as a total derivative are not included as usually the terms cancel at the boundaries. (This is not always the case. In particular, Chern-Simons theories contain an additional term which is a total derivative but the boundary conditions still contribute precisely because there is a non-trivial topological winding at the boundary as in the case, for instance, of axions. There is also a description of the Fractional Quantum Hall effect in terms of Chern-Simons theories. However, in this paper, the emphasis is on topological effects due solely to the ordinary Lagrangian terms.)

## Non-Abelian Cases

In the case of the nonabelian Higgs field, the field tensor must be given an extra index $a$. $$S_{YMH} = \int d^3x (-\dfrac{1}{4} F^{a \mu \nu} F^a_{\mu \nu} + (D^{\mu} \Phi)^\dag \cdot D_{ \mu } \Phi - V(\Phi))$$

where the covariant derivative is given, for instance, in the adjoint representation of the nonabelian group by $(D_{\mu} \Phi )_a = \partial_{\mu} \phi_a+ g f^{abc} A_{\mu}^b \Phi_c$. Explicitly, the field strength is $F^a_{\mu \nu} = \partial_{\mu} A^a_{\nu} - \partial_{\nu} A^a_{\mu} - g f^{abc} A^b_{\mu} A^c_{\nu}$.

## Determining the Particles

Note that there is spin-charge separation in the system as the flux and the charge can be measured independently (and there are both charged particles with no magnetic flux and magnetic fluxes with no electric charge). A specific particle type is determined by a conjugacy class A of the symmetry group H and a representation $\alpha$ of the centralizer of a representative of that conjugacy class. (The centralizers of each element of the conjugacy class are isomorphic, so the representation thus defined is independent of the particular representative chosen.) In particular, label the elements of each conjugacy class $^A C = \{^A h_1, ^A h_2, ..., ^A h_k \}$. Let $^A N$ denote the subgroup of H that is the centralizer for $^A h_1$. Choose a set of representatives of $H/^A N = \{^{\alpha}v_1,...,^{\alpha}v_k\}$. The states $$\{ |^A h_i, ^{\alpha}v_j \rangle \}$$ then constitute a basis for the internal Hilbert space $V_{\alpha}^A$.

A bit more formally, given the flux values take values in a group H, then quantum mechanically we should consider complex combinations $\mathbb{C}[H]$. The electric charge takes values in the dual $\textit{F}(H)$. The particles thus correspond to representations of Drinfeld's quantum double construction applied to the Abelian algebra $\textit{F}(H)$ of functions on a finite group $H$. Generators are given by combinations $\{P_h g\}_{h,g \in H}$, where $P_h$ is the operator projecting the flux $h \in H$ and $g \in H$ corresponds to the global symmetry transformation. The operators $P_h$ are projections as $P_h P_{h'} = \delta_{h, h'}P_h$. We demonstrated earlier that the action of the global symmetry transformations does not commute with the flux projection operators, and in fact: $g P_h = P_{g h g^{-1}} g$ due to flux metamorphosis. Combining these two relations we obtain the multiplication rule for two elements of the quantum double: $P_h g \cdot P_{h'}g' = \delta_{h, g h' g^{-1} P_h g g}$. The particles permitted by a discrete gauge theory are given by unitary irreducible representations of the quantum double. Note that since the quantum double is an algebra, not a group, representations $\Pi$ here are defined not only to respect the multiplicative structure, but are also required to be linear, i.e. addition and scalar multiplication are preserved. Each unitary irreducible representation of $D(H)$ is labeled uniquely by fixing a conjugacy class of the underlying group H and specifying the representation of the centralizer of a representative element in that conjugacy class. The algebra is semisimple, i.e. it can be decomposed into a direct sum. Thus the sum of squares of internal Hilbert spaces = the dimension of the quantum double. (This will be used as a consistency check to confirm the explicit dimensions obtained in future sections.)

## Changing Basis: The S-Matrix

The S-matrix implements the change of basis between the given basis of the fusion algebra and the diagonal basis. (Such a matrix S must exist since the algebra is commutative and associative.) Explicitly, the S matrix can be written as:

$$S_{\alpha \beta}^{AB} := \dfrac{1}{|H|} tr \textrm{ }R^{-2}{ }^{AB}_{\alpha \beta}$$ $$= \dfrac{1}{|H|} \sum_{^Ah_i \in ^AC, ^Bh_j \in ^BC: [^Ah_i, ^Bh_j]=e} tr(\alpha(^Ax_i^{-1} { }^Bh_j ^Ax_i))^* tr (\beta(^Bx_j^{-1}{ }^Ah_i ^Bx_j))^*$$

In the appendices, a MAGMA program that computes the S matrix values is included.

## Spin and the T-Matrix

The diagonal T-matrix records the information about the spins. Explicitly, the T matrix is given by:

$$T_{\alpha \beta}^{AB} := \delta_{\alpha,\beta} \delta^{A,B} e^{2\pi i s_{(A, \alpha)}}$$

Within each internal Hilbert space, all particles carry the same spin. Furthermore, the only particles which have nontrivial spin are dyons with both nontrivial flux and nontrivial charge. Note that in the construction for the quantum double, by definition the conjugacy class A representative element $^A h_1$ commutes with all elements in the centralizer $^A N$, so Schur's lemma yields:

$$\alpha(^A h_1) = e^{2 \pi i s_{(A, \alpha)}} \textbf{1}_{\alpha}$$

for every irreducible representation $\alpha$. This formula is implemented in the MAGMA program to yield the values of the spin for the various anyonic particles. While this does not distinguish between spin $s=0$ and $s=1$, it does the best that is possible in any superselection sector as it is always possible to add orbital angular momentum. In the specific groups discussed in the next section, a number of exotic spins are discovered.

## Magnetic-Electric Charge Duality

The symmetry transformations of the second factor ($\mathbb{C}(H)$) in the quantum double construction relate $D(H)$ to the electric charge. Similarly, the first part $F(H)$ of $D(H)$ yields the magnetic fluxes. Note that these are in fact dual to each other, as $F(H)\simeq \mathbb{C}H^*$. The magnetic-electric charge duality is implemented by the $SL(2, \mathbb{Z})$ action generated by the S and T matrices. The action of the $S$ matrix has an interpretation as a Fourier transform. [@koorn]

### Fusion

Similar to regular quantum field theory of the collision of two particles in three dimensions, the fusion of two particles can lead to multiple possible outcomes. The fusion rules are the analog in this two dimensional setting of the selection rule for addition of angular momenta $J_1$, $J_2$ in quantum mechanics which permits values between $-|J_2-J_1|$ and $J_2+J_1$ as feasible outcomes for the combined system. The fusion coefficients indicate how many different ways there are to obtain that outcome. (However, this still does not tell us the probabilities of obtaining the specific outcomes, so it is not quite the analog of the Clebsch-Gordon coefficients.)

The fusion coefficients are encoded in the comultiplication of the dual $D(H)^*$. Explicitly,

$$N^{AB \gamma}_{\alpha \beta C} = \sum_{D,\delta} \dfrac{S_{\alpha \delta}^{AD} S_{\beta \delta}^{BD} (S^*)_{\gamma \delta}^{CD}}{S_{0 \delta}^{eD}}$$

where as before the modular S matrix is given by: $$S_{\alpha \beta}^{AB} := \dfrac{1}{|H|} tr \textrm{ }R^{-2}{ }^{AB}_{\alpha \beta}$$ $$= \dfrac{1}{|H|} \sum_{^Ah_i \in ^AC, ^Bh_j \in ^BC: [^Ah_i, ^Bh_j]=e} tr(\alpha(^Ax_i^{-1} { }^Bh_j ^Ax_i))^* tr (\beta(^Bx_j^{-1}{ } ^Ah_i ^Bx_j))^*$$
