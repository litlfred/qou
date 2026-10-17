---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-002-classical-and-quantum-a-polynomials
section_title: "Classical and quantum A-polynomials"
section_number: null
pages: 4-9
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.964
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

## The case of $\text{SL}(2,{\mathbb C})$ gauge group {#sec: sl2c}

In this work, we take $G_{{\mathbb C}} = \text{SL}(2,{\mathbb C})$. Therefore, we have simply $r=1$, and $$A_{{\cal K}}(P,X)=A_{{\cal K}, 1}(P_1,X_1)$$ is the classical $A$-polynomial of the knot [@Cooper:1994aa]. The operators $\hat{P}, \hat{X}$ act on $u$-states as $$\hat{P} |u\rangle = |u+ {\rm i}{\mathsf{b}}\rangle \, , \quad \hat{X} |u\rangle = X |u\rangle \, .$$ Equivalently, $\hat{P}$ is the operator that shifts $X$ into $q X$, and $\hat{X}$ is the ordinary multiplication. Building on previous results [@hikami01; @hikami07; @dglz], the exact, non-perturbative partition function $\chi_{{\cal K}}(u; \hbar)$ has been constructed from an ideal triangulation of $M$ and identified with a finite-dimensional integral whose integrand is a product of Faddeev's quantum dilogarithm functions [@faddeev], known as the state-integral invariant, or Andersen--Kashaev invariant [@ak; @ak2; @dimofte-rev]. This is a holomorphic function of $\hbar \in {\mathbb C}' = {\mathbb C}\backslash (-\infty, 0 ]$ and $u \in {\mathbb C}$. It can be explicitly verified [@amalusa] that it obeys the $q$-difference equation encoded in the quantized $A$-polynomial of the knot, that is, $$\label{AJ-eq}
\hat{A}_{{\cal K}}(\hat{P}, \hat{X},q) \chi_{{\cal K}}(u;\hbar) = 0 \, .$$

Recall that $S$-duality exchanges ${\mathsf{b}}$ with $1/{\mathsf{b}}$. Therefore, the $S$-dual images of $\hbar$ and $q$ are $$\hbar_D={4 \pi^2 \over \hbar} = \frac{2 \pi}{\tau} \, , \quad q_D= {\rm e}^{{\rm i}\hbar_D} = {\rm e}^{\frac{2 \pi {\rm i}}{\tau}}= \tilde q^{-1},$$ where we have introduced ${\tilde{q}}= {\rm e}^{-{2 \pi {\rm i}\over \tau}}$, while the variable $u$ is invariant under the action of $S$-duality and $X$ transforms into $$X_D = {\rm e}^{\frac{2 \pi u}{{\mathsf{b}}}} = X^{2 \pi \over \hbar} \, .$$ Remarkably, the wave function $\chi_{{\cal K}}(u;\hbar)$ is also invariant under this transformation, that is, $$\chi_{{\cal K}}(u;\hbar)=\chi_{{\cal K}}(u;\hbar_D) \, ,$$ and, in particular, it satisfies the $S$-dual quantum $A$-polynomial equation $$\hat A_{\cal K}(\hat{P}_D, \hat{X}_D, q_D)\chi_{{\cal K}}(u;\hbar)=0 \, ,$$ where $\hat{P}_D$ is the quantum operator acting on $u$-states by shifting $u$ into $u + {\rm i}/{\mathsf{b}}$, or, equivalently, transforming $X_D$ into $q_D X_D$, and $\hat{X}_D$ acts by multiplication.

<figure id="fig: simple_knots">
<p><embed src="figure-eight.pdf" style="width:30.0%" /> <embed src="three-twist.pdf" style="width:30.0%" /></p>
<figcaption>The hyperbolic knots known as the figure-eight knot (<span class="math inline"><strong>4</strong><sub>1</sub></span>), on the left side, and the three-twist knot (<span class="math inline"><strong>5</strong><sub>2</sub></span>), on the right side.</figcaption>
</figure>

Throughout this work, we look at two concrete examples of hyperbolic knots, which allow us to perform explicit and detailed calculations to provide support to and give insight into our claims. These are the figure-eight and the three-twist knots.

::: example
[]{#41example label="41example"} The figure-eight knot, also denoted by $\bm{4}_1$, is shown on the left side of Fig. [1](#fig: simple_knots){reference-type="ref" reference="fig: simple_knots"}. Its classical $A$-polynomial can be written in symmetrized form as

$$A_{\bm{4}_1}(P, X) = P^{-1} + P -( X^2+ X^{-2} -X -X^{-1} -2) \, .$$

The corresponding polynomial equation $A_{\bm{4}_1}(P, X)=0$ has only two distinct non-abelian branches. Explicitly, the geometric and conjugate branches are labeled as $$\alpha = \rm{geom}, \rm{conj} \, ,$$ and they are described by $$\label{classicP}
P^{(\rm{geom}, \rm{conj})} = \frac{T(X) \pm (1-X^2) \sqrt{\Delta(X)} }{2 X^2} \, ,$$ where we have introduced $$\begin{align}
T(X) &= 1 - X - 2 X^2 - X^3 + X^4 \, , \label{classicT} \\
\Delta(X) &= 1 - 2 X -  X^2 - 2 X^3 + X^4 \, . \label{classicD}
\end{align}$$

Building on the results and conventions of [@ggm2], the descendant $\hat A$-operator is given by

$$\label{rec41x}
    \hat A_{\bf{4}_1} (\hat{P},\hat{X},q^m,q) = \sum_{j=0}^2 C_j(\hat{X},q^m,q) \hat{P}^j \, ,$$

where $m$ takes values in ${\mathbb Z}$ and the coefficient functions $C_j(\hat{X},q^m,q)$ are

$$\begin{align}
      \label{rec41x0}
      C_0(\hat{X},q^m,q) =&q^{2 + 3 m} \hat{X}^2 (-1 + q^{3 + m} \hat{X}^2) \, , \\
      \label{rec41x1}
      C_1(\hat{X},q^m,q) =& -q^m (-1 + q^{2 + m} \hat{X}^2) (1 - q \hat{X} - q^{1 + m} \hat{X}^2 \\
      &- q^{3 + m} \hat{X}^2 - q^{3 + m} \hat{X}^3 + q^{4 + 2 m} \hat{X}^4) \, ,\nonumber \\ 
      \label{rec41x2}
      C_2(\hat{X},q^m,q) =& q^2 \hat{X}^2 (-1 + q^{1 + m} \hat{X}^2) \, .
\end{align}$$ If we set $m=0$, symmetrize by multiplying by $\hat{P}^{-1}$, simplify a common factor $q^2 \hat{X}^2$, and perform the change of variable $\hat{X} \rightarrow q^{-1} \hat{X}$, we obtain the conventional $\hat A$-operator of the figure-eight knot, that is,

$$\label{41Ahat}
    \hat A_{\bf{4}_1} (\hat{P},\hat{X},q) = C_0(\hat{X},q) \hat{P}^{-1} + C_1(\hat{X},q) + C_2(\hat{X},q) \hat{P} \, ,$$

where the coefficient functions $C_j(\hat{X},q)$ are

$$\begin{align}
      \label{41xC0}
      C_0(\hat{X},q) =&q \hat{X}^2-1 \, ,\\
      \label{41xC1}
      C_1(\hat{X},q) =& - (\hat{X}^2-1)( \hat{X}^2 + \hat{X}^{-2} - \hat{X} - \hat{X}^{-1} - q - q^{-1} ) \, ,\\ 
      \label{41xC2}
      C_2(\hat{X},q) =& q^{-1} \hat{X}^2-1 \, .
\end{align}$$
:::

::: example
[]{#52example label="52example"} The three-twist knot, also denoted by $\bm{5}_2$, is shown on the right side of Fig. [1](#fig: simple_knots){reference-type="ref" reference="fig: simple_knots"}. Its classical $A$-polynomial can be written in symmetrized form as

$$\begin{aligned}
A_{\bm{5}_2}(P, X) = &P^{-1} -(X^{-2} -X^{-1} +2 X + 2 X^2 - X^3) \\
&- (X^{-1} - 2 - 2 X + X^3 - X^4) P - X^2 P^2 \, .
\end{aligned}$$

The corresponding polynomial equation $A_{\bm{5}_2}(P, X)=0$ has three distinct non-abelian branches: the geometric branch, its conjugate, and a third, self-conjugate branch. We label them by $$\alpha = \rm{geom}, \rm{conj}, \rm{\text{self}} \, .$$ Again, following [@ggm2], the descendant $\hat A$-operator is given by

$$\label{rec52x}
    \hat A_{\bf{5}_2} (\hat{P},\hat{X},q^m,q) = \sum_{j=0}^3 C_j(\hat{X},q^m,q) \hat{P}^j \, ,$$

where $m$ takes values in ${\mathbb Z}$ and the coefficient functions $C_j(\hat{X},q^m,q)$ are

$$\begin{align}
      \label{rec52x0}
      C_0(\hat{X},q^m,q) =
      &-q^{2 + m} \hat{X}^2 (1-q^2 \hat{X})(1+q^2 \hat{X})(1-q^5 \hat{X}^2) \, , \\
      \label{rec52x1}
      C_1(\hat{X},q^m,q) =
      & (1-q \hat{X})(1+q \hat{X})(1-q^5 \hat{X}^2)(1-q\hat{X}-q\hat{X}^2-q^4\hat{X}^2 \\
      &+q^{2+m}\hat{X}^2+q^{3+m}\hat{X}^2+q^2\hat{X}^3+q^5\hat{X}^3+q^5\hat{X}^4+q^{5+m}\hat{X}^4-q^6\hat{X}^5) \, , \nonumber\\ 
      \label{rec52x2}
      C_2(\hat{X},q^m,q) =
      & q\hat{X}(1-q^2\hat{X})(1+q^2\hat{X})(1-q\hat{X}^2)(1-q^2\hat{X}-q^{2+m}\hat{X}-q^2\hat{X}^2-q^5\hat{X}^2 \\
      &+q^4\hat{X}^3+q^7\hat{X}^3-q^{5+m}\hat{X}^3-q^{6+m}\hat{X}^3+q^7\hat{X}^4-q^9\hat{X}^5) \, , \nonumber \\
      \label{rec52x3}
      C_3(\hat{X},q^m,q) =
      & q^{8+m}\hat{X}^4(1-q\hat{X})(1+q\hat{X})(1-q\hat{X}^2) \,.
\end{align}$$

If we set $m=0$, symmetrize by multiplying by $\hat{P}^{-2}$, and perform the change of variable $\hat{X} \rightarrow q^{-1} \hat{X}$, we obtain the conventional $\hat A$-operator of the three-twist knot, that is,

$$\label{52Ahat}
\begin{aligned}
\hat A_{\bf{5}_2}(\hat{P},\hat{X},q) = C_0(\hat{X},q) \hat{P}^{-2} + C_1(\hat{X},q) \hat{P}^{-1} + C_2(\hat{X},q) + C_3(\hat{X},q) \hat{P} \, ,
\end{aligned}$$

where we have defined $$\label{52xC}
\begin{align}
      \label{52xC0}
      C_0(\hat{X},q) =&-\hat{X}^2 (1-q^2 \hat{X}^2) (1-q^3 \hat{X}^2) \, , \\
      \label{52xC1}
      C_1(\hat{X},q) =& (1-\hat{X}^2) (1-q^3 \hat{X}^2)(q^2 \hat{X}^3-q^2 \hat{X}^2-q \hat{X}^5 \\
      &+2 q \hat{X}^4+q^{-1}\hat{X}^3+q \hat{X}^2-q^{-1}\hat{X}^2+\hat{X}^2-\hat{X}+1) \, , \nonumber \\ 
      \label{52xC2}
      C_2(\hat{X},q) =& \hat{X} (1-q^2 \hat{X}^2) (1-q^{-1}\hat{X}^2) (-q^4 \hat{X}^5+q^4 \hat{X}^3 \\
      &+q^3 \hat{X}^4-q^3 \hat{X}^3-q^3 \hat{X}^2-q^2 \hat{X}^3+q \hat{X}^3-2 q \hat{X}-\hat{X}^2+1)  \, , \nonumber \\
      \label{52xC3}
      C_3(\hat{X},q) =& q^4 \hat{X}^4 (1-\hat{X}^2)(1-q^{-1}\hat{X}^2) \, .
\end{align}$$
:::

[^1]: $\bm{P}$ and $\bm{X}$ can be interpreted as the vectors of eigenvalues of the holonomies of the flat gauge connections on the boundary torus over its two basic one-cycles.

[^2]: On the geometric branch, $\bm{u}$ can be thought of as parametrizing the quantum deformations of the complex hyperbolic structure of $M$.
