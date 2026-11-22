---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-002-classical-and-quantum-a-polynomials
section_title: "Classical and quantum A-polynomials"
section_number: null
pages: 4-6
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.94
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: Apoly label="sec: Apoly"} The classical action of CS theory with complex gauge group $G_{{\mathbb C}}$ can be written as [@witten91]

$$S = \frac{t}{8 \pi} \int_M {\rm Tr}\left({\cal A}\wedge d{\cal A}+ \frac{2}{3} {\cal A}\wedge {\cal A}\wedge {\cal A}\right) +  \frac{t'}{8 \pi} \int_M {\rm Tr}\left(\bar{{\cal A}} \wedge d\bar{{\cal A}} + \frac{2}{3} \bar{{\cal A}} \wedge \bar{{\cal A}} \wedge \bar{{\cal A}} \right) \, ,$$

where $M$ is the underlying closed three-manifold, whose boundary is the closed Riemann surface $\Sigma = \partial M$, ${\cal A}$ is the complex gauge field, which is a one-form on $M$ taking values in the Lie algebra $\mathfrak{g}_{{\mathbb C}}$, and $t, t'$ are complex coefficients such that $t=k+s$ and $t'=k-s$ where $k \in {\mathbb Z}$. For the theory to be unitary, $s$ must be real or purely imaginary, although we will not need this in our discussion. We also introduce the complex coupling constant ${\mathsf{b}}^2$ defined by

$${\mathsf{b}}^2= \frac{t'}{t} \, .$$

The classical phase space of the theory is the moduli space of flat $G_{{\mathbb C}}$-connections on $\Sigma$ modulo gauge transformations, that is, $$\label{phase_space}
{\cal M}_{\rm{flat}} (G_{{\mathbb C}}, \Sigma) = {\rm Hom}\left(\pi_1(\Sigma), G_{{\mathbb C}} \right) / \sim \, ,$$ where $\pi_1$ denotes the fundamental group and $\sim$ is conjugation by elements of $G_{{\mathbb C}}$. This comes naturally equipped with a symplectic two-form $$\label{omega}
\omega = \frac{t}{8 \pi} \int_{\Sigma} {\rm Tr}\left(\delta {\cal A}\wedge \delta {\cal A}\right) + \frac{t'}{8 \pi} \int_{\Sigma} {\rm Tr}\left(\delta \bar{{\cal A}} \wedge \delta \bar{{\cal A}} \right) \, .$$

A classical solution on $M$ is a gauge equivalence class of flat $G_{{\mathbb C}}$-connections on $M$, which are gauge connections ${\cal A}$ satisfying the property $$d {\cal A}+ {\cal A}\wedge {\cal A}= 0 \, ,$$ and analogously for $\bar{{\cal A}}$. The moduli space of classical solutions on $M$ is a Lagrangian submanifold of the classical phase space. Namely, the submanifold $${\cal L}= {\cal M}_{\rm{flat}} (G_{{\mathbb C}}, M) \subset {\cal M}_{\rm{flat}} (G_{{\mathbb C}}, \Sigma)$$ is Lagrangian with respect to the symplectic structure $\omega$ in Eq. [\[omega\]](#omega){reference-type="eqref" reference="omega"}.

In this paper, we will focus on a three-manifold $M$ obtained as the complement of a hyperbolic knot ${\cal K}$ in the three-sphere ${\mathbb S}^3$, that is,

$$\label{MK}
M = {\mathbb S}^3 \backslash {\cal K}\, ,$$ which has a single toral boundary $\Sigma = {\mathbb T}^2$. Its moduli space of flat $G_{{\mathbb C}}$-connections is a complex Lagrangian submanifold ${\cal L}$ of the full phase space $$\label{phase_spaceK}
{\cal M}_{\rm{flat}} (G_{{\mathbb C}}, {\mathbb T}^2) = \left( {\mathbb T}_{{\mathbb C}} \times {\mathbb T}_{{\mathbb C}} \right) / {\cal W}\, ,$$ where ${\mathbb T}_{{\mathbb C}}$ is the maximal toral subgroup of $G_{{\mathbb C}}$ and ${\cal W}$ is the Weyl group.

Let us denote by $\bm{P}=(P_1, \dots, P_r)$ and $\bm{X}=(X_1, \dots, X_r)$, where $r$ is the rank of the gauge group, the complex variables parametrizing each copy of the maximal torus ${\mathbb T}_{{\mathbb C}}$ in Eq. [\[phase_spaceK\]](#phase_spaceK){reference-type="eqref" reference="phase_spaceK"}, which are defined modulo the action of the Weyl group[^1]. It follows that the irreducible components of ${\cal L}$ are described by ${\cal W}$-invariant polynomial equations $$\label{Apoly_eqs}
A_{{\cal K}, i} (\bm{P}, \bm{X}) = 0 \, , \quad i=1, \dots, r \, ,$$ where the polynomials $A_{{\cal K}, i} (\bm{P}, \bm{X})$ have coefficients in ${\mathbb R}$.

Quantizing the classical phase space in Eq. [\[phase_space\]](#phase_space){reference-type="eqref" reference="phase_space"} with its symplectic structure in Eq. [\[omega\]](#omega){reference-type="eqref" reference="omega"} produces a Hilbert space ${\cal H}_{\Sigma}$. In the quantized theory, the path integral over the manifold $M$ leads to a vector $|M\rangle \in {\cal H}_{\Sigma}$, while the polynomials $A_{{\cal K}, i}(\bm{P}, \bm{X})$ in Eq. [\[Apoly_eqs\]](#Apoly_eqs){reference-type="eqref" reference="Apoly_eqs"} are expected to produce quantum operators $\hat{A}_{{\cal K}, i}(\hat{\bm{P}}, \hat{\bm{X}},q)$, $i=1, \dots, r$, acting on ${\cal H}_{\Sigma}$, which annihilate the state $|M\rangle$. Here, the complex variables $\bm{P}, \bm{X}$ are promoted to the operators $\hat{\bm{P}}, \hat{\bm{X}}$, which satisfy the commutation relations $$\hat{P}_i \hat{X}_j = q^{\delta_{ij}} \hat{X}_j \hat{P}_i \, , \quad i,j=1, \dots, r \, ,$$ where $\delta_{ij}$ is the Kronecker delta, we have introduced $q= {\rm e}^{{\rm i}\hbar}$, and $$\hbar = 2 \pi {\mathsf{b}}^2$$ is the complex coupling parameter playing the role of Planck's constant. We will sometimes denote $\tau= {\mathsf{b}}^2$. Note that the quantization of the theory depends on the level $k$ and, in this work, we will restrict ourselves to the case $k=1$. See, *e.g.*, [@dimofte-levelk]. The classical constraints in Eq. [\[Apoly_eqs\]](#Apoly_eqs){reference-type="eqref" reference="Apoly_eqs"} become Schrödinger-like operator equations in the quantum theory. Namely,

$$\label{quantumApoly}
\hat{A}_{{\cal K}, i}(\hat{\bm{P}}, \hat{\bm{X}},q) \chi_{{\cal K}}(\hbar) = 0 \, , \quad i=1, \dots, r \, ,$$ where $\chi_{\cal K}(\hbar)$ is the partition function associated to the manifold $M$ in Eq. [\[MK\]](#MK){reference-type="eqref" reference="MK"} defined by the complement of the knot ${\cal K}$. Following the conventions of [@ggm2], we define the continuous complex variables $\bm{u}=(u_1, \dots, u_r)$ such that $$X_i = {\rm e}^{2 \pi {\mathsf{b}}u_i} \, , \quad i=1, \dots, r \, .$$ The corresponding quantum operators $\hat{u}_i$ determine a complete basis of states $|u\rangle \in {\cal H}_{\Sigma}$ on which they act by multiplication. Therefore, the partition function on $M$ can be regarded as a wave function in $u$-space, which we represent as $$\chi_{{\cal K}}(\bm{u}; \hbar) \, .$$

We stress that the quantization of the $A$-polynomials in Eq. [\[Apoly_eqs\]](#Apoly_eqs){reference-type="eqref" reference="Apoly_eqs"} is not obtained simply by promoting $\bm{P}, \bm{X}$ to their operator counterpart. On top of ordering issues, the resulting operators have a non-trivial dependence on $\hbar$ through $q$. It is fair to say that the spectral theory of these operators is not entirely understood, and a deeper grasp of this issue might clarify the corresponding non-trivial quantization problem. A concrete way of constructing the quantized $A$-polynomials is, for example, to use the original AJ conjecture of [@stavros-aj].

The wave function $\chi_{{\cal K}}(\bm{u}; \hbar)$ can be calculated perturbatively in a saddle-point approximation where the saddle, or classical solution, of the EOM is described by the homomorphism $$\rho : \pi_1(M) \rightarrow G_{{\mathbb C}} \, .$$ Equivalently, the saddle points can be identified with the different classical solutions $\bm{P}^{(\alpha)}$ to Eq. [\[Apoly_eqs\]](#Apoly_eqs){reference-type="eqref" reference="Apoly_eqs"} for fixed $\bm{X}$, which we denote with the additional discrete label $\alpha$. We recall that the branches of the polynomials in Eq. [\[Apoly_eqs\]](#Apoly_eqs){reference-type="eqref" reference="Apoly_eqs"} come in conjugate pairs due to the symmetry of the theory under conjugation. Thus, each flat connection ${\cal A}^{(\rho)}$, labeled by $\rho \in {\rm Hom}\left(\pi_1(M), G_{{\mathbb C}} \right)$, has a conjugate flat connection ${\cal A}^{(\bar{\rho})}$, corresponding to the conjugate homomorphism $\bar{\rho}$. We will subsequently denote by $\bar{\alpha}$ the branch which is conjugate to $\alpha$.

There is always an abelian branch $\alpha = \rm{abel}$ described by $P_1=\dots=P_r=1$, which is self-conjugate, and a geometric branch[^2] $\alpha = \rm{geom}$ containing the discrete faithful representation of $\pi_1(M)$ into $\text{PSL}(2, {\mathbb C})$, which has a distinct conjugate $\alpha = \rm{conj}$. In the rest of this work, we will only consider non-abelian branches. Therefore, we simplify the factor corresponding to the abelian classical solution from the polynomials in Eq. [\[Apoly_eqs\]](#Apoly_eqs){reference-type="eqref" reference="Apoly_eqs"} and proceed to quantize the simplified form.

When computed in the saddle-point approximation, that is, using the WKB method, the perturbative wave function, denoted by $\chi_{{\cal K}}^{(\alpha), \rm{WKB}}(\bm{u};\hbar)$ is given by an asymptotic power series in $\hbar$ of the form [@dglz] $$\label{WKB}
 \chi_{{\cal K}}^{(\alpha), \rm{WKB}}(\bm{u};\hbar) = \exp \left( \frac{1}{\hbar} S_0^{(\alpha)}(\bm{u}) - \frac{\delta^{(\alpha)}}{2} \log \hbar + \sum_{n=0}^{\infty} S_{n+1}^{(\alpha)}(\bm{u}) \hbar^n  \right) \, ,$$ where the leading coefficient $S_0^{(\alpha)}(\bm{u})$ is determined by the classical CS functional, the next-to-leading coefficient $\delta^{(\alpha)}$ is an integer, and the higher-order coefficients $S_n^{(\alpha)}(\bm{u})$, $n \ge 1$, are obtained, in principle, by summing systematically the contributions of Feynman diagrams with $n$-loops. Note that $\delta^{(\alpha)} = 0$ for $\alpha \ne \rm{abel}$.

[^1]: $\bm{P}$ and $\bm{X}$ can be interpreted as the vectors of eigenvalues of the holonomies of the flat gauge connections on the boundary torus over its two basic one-cycles.

[^2]: On the geometric branch, $\bm{u}$ can be thought of as parametrizing the quantum deformations of the complex hyperbolic structure of $M$.
