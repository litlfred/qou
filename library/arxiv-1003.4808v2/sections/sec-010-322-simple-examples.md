---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-010-322-simple-examples
section_title: "Simple examples"
section_number: 3.2.2
pages: 21-23
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.996
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
Let us now adapt the general statements here to some specific examples.

### Harmonic oscillator

The quintessential simplest nontrivial problem of quantization is the harmonic oscillator. Consider a classical system that consists of a particle moving on a line (with coordinate $x=x(t)$) with a potential energy $V = \frac12 x^2$. This is depicted in Figure [1](#fig:harm){reference-type="ref" reference="fig:harm"}. The total (potential + kinetic) energy of the particle at any moment of time is given by the Hamiltonian

$$H = \frac12 x^2 + \frac12 p^2\,,$$

where classically $p = \dot x = \frac{dx}{dt}$ is the momentum. This total energy $H$ is conserved. The classical phase space ${\cal M}$ is just ${\mathbb{R}}^2 = \{(x,p)\}$, endowed with a symplectic structure $\omega = dp\wedge dx$. A classical trajectory with energy $H=E$ is just a circle of radius $\sqrt{2E}$ in phase space. This defines a Lagrangian submanifold ${\cal L}_{(E)} \simeq S^1$.

![The harmonic oscillator: potential $V(x) = \frac12 x^2$ in physical space, phase space ${\cal M}$, a classical trajectory ${\cal L}_{(E)}$ in phase space, and the ground state quantum wavefunction $Z(x)$.](harmosc){#fig:harm width="5in"}

Now let us quantize the system. Since $H^2({\cal M};{\mathbb{Z}}) = 0$, there is no restriction or quantization of $\hbar^{-1}$. On the other hand, there *is* a restriction on ${\cal L}$ which quantizes the energy. Namely, according to [\[thetaq\]](#thetaq){reference-type="eqref" reference="thetaq"}, for a Liouville 1-form $\theta$ such that $\omega = d\theta$, the integral

$$\oint_{\cal L}\theta = \oint_{S^1} \theta = 2\pi E$$

must be an element of $2\pi\hbar\,{\mathbb{Z}}$, implying that $E = n\hbar$ for positive $n\in{\mathbb{Z}}$. In fact, this equation is corrected by quantum effects --- a Maslov correction in geometric quantization --- to

$$E = \hbar\Big(n+\frac12\Big)\,. \label{En}$$

This leads to the famous result that the lowest possible energy of a quantum harmonic oscillator (at $n=0$) is nonzero.

Suppose we choose a polarization $\partial/\partial p=0$, and a corresponding Liouville 1-form $\theta = p\,dx$. The Hilbert space ${\cal H}$ can simply be identified as $L^2({\mathbb{R}}) \sim \{\text{functions of $x$}\}$, on which the functions $x$ and $p$ act as operators

$$\hat{x}:={\cal O}_x = x\,, \qquad \hat{p}:={\cal O}_p = -i\hbar\frac{d}{dx}\,.$$

In this case, the exact quantum expression for the Hamiltonian is

$${\cal O}_H = \frac12(\hat{x}^2+\hat{p}^2)\,.$$

It is then easy to find the quantum wavefunctions corresponding to classical states ${\cal L}_{(E)}$. From [\[v\]](#v){reference-type="eqref" reference="v"}, we find a leading contribution

$$Z(x) \simeq \exp\left(\frac{i}{\hbar}\int_0^x \theta\right) = \exp\left(\frac{i}{\hbar}\int_0^x\sqrt{2E-x^2}\,dx\right)
 \simeq \exp\left(-\frac{1}{2\hbar}x^2+ \ldots\right)\,.$$

Since the Lagrangian ${\cal L}_{(E)}$ is defined classically by $H-E=0$, the complete expression for $Z(x)$ can be obtained by solving the operator equation $({\cal O}_H-E)Z=0$. This eigenvalue equation has square-integrable solutions only for the quantized energies [\[En\]](#En){reference-type="eqref" reference="En"}; for example, at the ground state energy $E = \hbar/2$, the exact solution is $Z(x) = \exp\left(-\frac{1}{2\hbar}x^2\right)$.

### Representations of Lie groups

Another famous application of quantization is the construction of unitary representations of Lie groups by quantization of coadjoint orbits. A basic premise of this approach, also known as the *orbit method*, is that coadjoint orbits come equipped with a natural symplectic structure (the Kostant-Kirillov-Souriau symplectic structure), therefore providing interesting examples for quantization.

Continuing with our default notations in these notes, we use $G$ for a compact Lie group (that we usually assume to be simple), $G_{{\mathbb{C}}}$ for its complexification, and $G_{{\mathbb{R}}}$ for some real form of the complex group $G_{{\mathbb{C}}}$ (that may be equal to $G$). We denote by ${\frak{g}}_{{\mathbb{R}}}$ the Lie algebra of $G_{{\mathbb{R}}}$, and similarly for $G$ and $G_{{\mathbb{C}}}$. Given an element $\lambda \in {\frak{g}}_{{\mathbb{R}}}^*$ (the highest weight of the desired unitary representation $R_\lambda$) one constructs ${\cal M}= G_{{\mathbb{R}}} \cdot \lambda$ as the coadjoint orbit of $G_{{\mathbb{R}}}$ in ${\frak{g}}_{{\mathbb{R}}}^*$ passing through $\lambda$.

In the case of compact groups, the phase space ${\cal M}$ is compact and its quantization leads to a finite-dimensional Hilbert space ${\cal H}$ as the space of the unitary representation $R_\lambda$. This is the statement of the Borel-Bott-Weil theorem. Moreover, the condition $\frac{1}{2\pi\hbar}\omega\in H^2({\cal M};{\mathbb{Z}})$ that ensures the existence of a prequantum line bundle becomes equivalent to the condition that $\lambda$ be an element of the weight lattice $\Lambda_w\subset{\frak{g}}^*$.

As a very simple illustration, consider the group $SU(2)$. In this case, a non-trivial coadjoint orbit is topologically equivalent to the flag manifold

$$SU(2)/U(1) \simeq {\mathbb{P}}^1 \,.$$

Letting $\omega$ be the unit volume form on ${\mathbb{P}}^1$, we see that $({\cal M},\omega)$ is quantizable for

$$\hbar^{-1} = 2\pi\lambda\,, \qquad \lambda\in{\mathbb{Z}}_{(+)}\,.$$

The prequantum line bundle with curvature $\hbar^{-1}\omega$ is simply ${\cal O}(\lambda)\to {\mathbb{P}}^1$. Choosing a holomorphic polarization, so that ${\cal H}$ is defined as the space of holomorphic sections of ${\cal O}(\lambda)$, we see that $\dim{\cal H}= \lambda+1$. The Hilbert space is precisely the space of the $(\lambda+1)$-dimensional representation of $SU(2)$.

Similarly, some infinite-dimensional representations, such as unitary principal series representations of $SL(n,{\mathbb{C}})$ or $SL(n,{\mathbb{R}})$, can be described as quantized orbits. Nevertheless, there remain some outstanding puzzles: there exist unitary representations that don't appear to correspond to orbits, and, conversely, there are real orbits that don't seem to correspond to unitary representations. An example of first kind occurs even in the basic case of the real group $G_{{\mathbb{R}}} = SL(2,{\mathbb{R}})$ and the complementary series representations. To illustrate the second phenomenon, one can take $G_{{\mathbb{R}}}$ to be a real group of Cartan type $B_N$, *i.e.* $G_{{\mathbb{R}}} = SO(p,q)$ with $p+q=2N+1$. The minimal orbit ${\cal O}_{{\rm min}}$ of $B_N$ is a nice symplectic manifold of (real) dimension $4N-4$, for any values of $p$ and $q$. On the other hand, the minimal representation of $SO(p,q)$ exists only if $p \le 3$ or $q \le 3$ [@vogan-singular-unitary]. Both of these issues can be resolved in the brane quantization approach [@gukov-2008], at the cost of replacing classical geometric objects (namely, coadjoint orbits) with their quantum or "stringy" analogs (branes). In particular, in the case of $B_N$ one finds that, while the minimal orbit exists for any values of $p$ and $q$, the corresponding brane exists only if $p \le 3$ or $q \le 3$. (In general, the condition is that the second Stieffel-Whitney class $w_2({\cal M}) \in H^2({\cal M};{\mathbb{Z}}_2)$ must be a mod 2 reduction of a torsion class in the integral cohomology of ${\cal M}$.)
