---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-024-61-quantization-at-k0
section_title: "Quantization at k=0"
section_number: 6.1
pages: 58-62
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.998
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:k0 label="sec:k0"}

Let's begin by reviewing a few facts about Chern-Simons theory with gauge group $G_{\mathbb C}=SL(2,{\mathbb C})$ [@Wit-CSgrav; @Witten-cx; @gukov-2003]. The most general complex bulk action on a 3-manifold $M$ is

$$S_{CS}(M) \,=\, \frac{t}{8\pi}\int_M {\rm Tr \,}\Big(\mathcal{A}\, d\mathcal{A}+\frac{2}{3}\mathcal{A}^3\Big)\,+\,\frac{\tilde t}{8\pi}\int_M {\rm Tr \,}\Big(\overline\mathcal{A}\, d\overline\mathcal{A}+\frac{2}{3}\overline\mathcal{A}^3\Big)\,,
\label{CSaction}$$

where $\mathcal{A}$ is a local $\mathfrak{g}_{\mathbb C}=\mathfrak{sl}(2,{\mathbb C})$-valued one-form, defined modulo the standard gauge transformations $\mathcal{A}\to g^{-1}\mathcal{A}\, g+ g^{-1}dg$. Unlike the case of real Chern-Simons theory, the complex action here contains both holomorphic and antiholomorphic terms, and each comes with its own coupling constant, here $t$ and $\tilde t$. Let us write

$$t=k+is\,,\qquad \tilde t=k-is\,.$$

A priori, $k$ and $s$ are independent complex parameters. However, independence of the path integral measure $\exp\big[ i S_{CS}(M) \big]$ under large gauge transformations forces $k$ to be an integer. Moreover, unitarity --- the statement that the path integral be conjugated under a change of orientation on $M$ --- requires $s\in {\mathbb R}$.

[^1]

If the boundary of $M$ is nonempty, then the Chern-Simons path integral on $M$ is a wavefunction in a boundary Hilbert space $\mathcal{H}_{\partial M}$. This space is the quantization of the classical phase space associated to the boundary,

$$\mathcal{P}_{\partial M} \;\simeq\; \big\{\, \text{flat connections $\mathcal{A}$ on $\partial M$}\,\big\}\,.$$

This space is endowed with a real symplectic structure induced from the Chern-Simons action:

$$\omega_{k,s} = \frac{t}{8\pi}\Omega+\frac{\tilde t}{8\pi}\overline\Omega\,,
\label{wtt}$$

where $\Omega = \int_{\partial M}{\rm Tr \,}\big(\delta\mathcal{A}\wedge \delta \mathcal{A})$ is a holomorphic symplectic form. By setting $\Omega  = \omega_I-i\omega_K$, we could also write this as

$$\omega_{k,s} = \frac{k}{4\pi}\omega_I+\frac{s}{4\pi}\omega_K\,.$$

Here $\omega_I$ and $\omega_K$ coincide with two of the standard real symplectic forms on $\mathcal{P}_{\partial M}$, viewed as a hyperkahler manifold [@Hitchin-SD], hence the notation. It turns out that, as cohomology classes, $[\omega_K]=0$ while $[\omega_I/(4\pi)] \in H^2(\mathcal{P}_{\partial M};{\mathbb Z})$ for any 2d boundary $\partial M$. Thus, as long as $k\in {\mathbb Z}$, we have $[\omega_{k,s}/(2\pi)]\in H^2(\partial M;{\mathbb Z})$, and the pair $(\mathcal{P}_{\partial M},\omega_{k,s})$ is quantizable (*cf.* [@woodhouse-1992]).

The Hilbert space $\mathcal{H}_{\partial M}$ is the quantization of $(\mathcal{P}_{\partial M},\omega_{k,s})$. However, this quantization depends critically on the relative values of $k$ and $s$. To illustrate this dependence more concretely, let us consider a "model" phase space $\mathcal{P}\simeq {\mathbb C}^*\times{\mathbb C}^*$, with coordinates $x$ and $p$, and a holomorphic symplectic form

$$\Omega = 2\,\frac{dp}{p}\wedge \frac{dx}{x}\,. \label{Omega}$$

It is also convenient to take logarithms

$$X = \log x\,,\qquad P=\log p\,,$$

defined modulo $2\pi i{\mathbb Z}$ . $\mathcal{P}$ is the actual phase space for the boundary $\partial\Delta$ of a tetrahedron --- thinking of $\partial\Delta$ as a four-punctured sphere, with unit $SL(2,{\mathbb C})$ holonomy eigenvalues at each puncture [@DGG] --- and it can be used as a building block to approximate the phase space of any more complicated boundary [@DGGV-hybrid]. For example, the phase space of a torus is $\mathcal{P}_{T^2}\simeq \mathcal{P}/{\mathbb Z}_2$, while for a genus $g\geq 2$ surface with $s$ punctures an open patch of the phase space looks like a quotient of $\mathcal{P}^{3g-3+s}$. The coordinates $z$ and $p$ can be thought of as models for eigenvalues of general $SL(2,{\mathbb C})$ holonomies.

Now, to demonstrate the sensitivity of quantization to the values of $k,s$, suppose first that we quantize $(\mathcal{P},\omega_{k,s})$ for a choice of coupling constants $s=0$ and $k\neq 0$. In other words, we choose the real symplectic form

$$\omega_{k,0} = \frac{k}{4\pi}\omega_I = \frac{k}{2\pi}\big[d\,{\rm Re}(P)\wedge d\,{\rm Re}(X)- d\,{\rm Im}(P)\wedge d\,{\rm Im}(X)\big]\,. \label{wI}$$

Thus, writing $\mathcal{P}= {\mathbb C}^*_1\times {\mathbb C}^*_2\simeq ({\mathbb R}_1\times {\mathbb R}_2)\times(S^1_1\times S^1_2)$, [\[wI\]](#wI){reference-type="eqref" reference="wI"} indicates that the two noncompact real directions are canonically conjugate to each other, as are the two $S^1$ directions. Moreover, it is easy to see that $[\omega_{k,0}/(2\pi)]\in H^2(\mathcal{P};{\mathbb Z})$, since $\int_{S^1_1\times S^1_2}\omega_{k,0}=-2\pi k$. If we choose a polarization such that (say) ${\rm Re}(Z)$ and ${\rm Im}(Z)$ are both "positions" while ${\rm Re}(P)$ and ${\rm Im}(P)$ serve as "momenta," the Hilbert space becomes

$$\mathcal{H}_{k,0} \;\simeq\; L^2({\mathbb R})\otimes L^2({\mathbb Z}_k)\,,$$

with an infinite-dimensional factor coming from quantization of ${\mathbb R}_1\times {\mathbb R}_2$, and a $|k|$-dimensional factor coming from quantization of the compact $S^1_1\times S^1_2$. The latter factor is much like the Hilbert space of Chern-Simons theory with compact gauge group $SU(2)$.

The choice $s=0$ and $k\neq 0$ turns out not to be the relevant one for the 3d index. Rather, we conjecture that the index is related to Chern-Simons theory quantized in the opposite limit $k=0$ and $s\neq 0$. The Hilbert space in this case looks very different, and we will proceed to analyze it for the remainder of this section. The general situation $k,s\neq 0$ is a slightly twisted variation of $k=0,\,s\neq 0$; it would be interesting to see if it were related to a generalization of the index.

The real symplectic structure at $k=0$ is

$$\begin{aligned}
 \omega_{0,s} &\,=\,\frac{s}{4\pi}\omega_K \,=\, \frac{i}{\hbar} dP\wedge dX - \frac{i}\hbar d\overline P\wedge d\overline X \label{ws1}  \\
 &\,=\, -\frac{2}\hbar\,\big[ d\,{\rm Re}P\wedge d\,{\rm Im}X+d\,{\rm Im}P\wedge d\,{\rm Re}X\big]  \,, \label{ws2}
\end{aligned}$$

with

$$\boxed{\hbar \equiv \frac{4\pi}{s}}\,.$$

Then, we see that the coordinate on each noncompact ${\mathbb R}$ factor in $\mathcal{P}$ is canonically conjugate to the coordinate on a compact $S^1$. In fact, we could more naturally write the phase space $(\mathcal{P},\omega_{0,s})$ as $T^*(S^1_1\times S_2^1)$, with the standard symplectic form of a cotangent bundle. In order to quantize $(\mathcal{P},\omega_{0,s})$ we must choose a polarization, and there are several nice choices, summarized in Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"}. The polarizations differ in the combinations of compact and noncompact coordinates that are designated as positions and momenta.

[^2]

This choice is somewhat distinct from the coarser distinction of $Z$ vs. $P$ as position and momentum, and the related $Sp(2,{\mathbb Z})$ action that featured prominently in the construction of theories $T_M$ and indices $\mathcal{I}_M$. We will return to the $Sp(2,{\mathbb Z})$ action in Section [\[sec:CSsymp\]](#sec:CSsymp){reference-type="ref" reference="sec:CSsymp"}.

$\begin{array}{|@{\;\;}l@{\quad}l@{\quad}l@{\qquad}l@{\;\;}|} \hline
&\text{\underline{Positions}} & \text{\underline{Momenta}} & \text{\underline{Hilbert space $\mathcal{H}\equiv \mathcal{H}_{0,s}$}} \\[.1cm]
\text{a)} & {\rm Im}\, X\,,\;{\rm Im}\, P\;\;(S^1_1\times S^1_2) & -2\,{\rm Re}\, P\,,\;2\,{\rm Re}\, X\;\; ({\mathbb R}_2\times {\mathbb R}_1) & L^2(S^1)\times L^2(S^1) \\[.1cm]
\text{b)} & {\rm Im}\, X\,,\;{\rm Re}\, X\;\; (S^1_1\times {\mathbb R}_1) & -2\,{\rm Re}\, P\,,\;-2\,{\rm Im}\, P \;\;({\mathbb R}_2\times S^1_2) & L^2(S^1)\times L^2({\mathbb Z}) \\[.1cm]
\text{c)} & {\rm Re}\, P\,,\;{\rm Im}\, P\;\; ({\mathbb R}_2\times S^1_2) & 2\,{\rm Im}\, X\,,\;2\,{\rm Re}\, X \;\;(S^1_1\times {\mathbb R}_1) & L^2({\mathbb Z})\times L^2(S^1) \\[.1cm]
\text{d)} & {\rm Re}\, X\,,\;{\rm Re}\, P \;\;({\mathbb R}_1\times {\mathbb R}_2) & -2\,{\rm Im}\, P\,,\; 2\,{\rm Im}\, X \;\;(S^1_2\times S^1_1) & L^2({\mathbb Z})\times L^2({\mathbb Z}) \\\hline \end{array}$

Two of the polarizations in Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"} may begin to look familiar from our discussion of indices. In particular, in polarization (d), the compactness of the momenta quantizes the position coordinates ${\rm Re}\,X$ and ${\rm Re}\,P$. Specifically, we find

$$\boxed{{\rm Re}\,X = m\tfrac{\hbar}2\,,\qquad {\rm Re}\,P = e\tfrac{\hbar}{2}\,,\qquad m,\,e\,\in\,{\mathbb Z}}\,,$$

so that wavefunctions in $\mathcal{H}$ are just complex-valued functions of the two integers $(m,e)$ and the real parameter $\hbar$. This appears identical to the form of the index in a "charge basis" [\[chargeindex\]](#chargeindex){reference-type="eqref" reference="chargeindex"}. Alternatively, if we treat both real and imaginary parts of $Z$ as positions, as in (b), the wavefunctions become non-holomorphic functions of $x = \exp({\rm Re}\,X+i\,{\rm Im}\,X)$. The compact momentum ${\rm Im}\, P$ still quantizes ${\rm Re}\,Z\in \tfrac\hbar2{\mathbb Z}$, so

$$\hspace{.3in} \boxed{x = q^{\frac m2}\zeta}\,,\qquad\text{with}\quad q\equiv e^\hbar\,,\; m\in {\mathbb Z}\,;\;\;\; \zeta =e^{i\theta} \equiv e^{i\,{\rm Im}\,X}\,.
\label{zzeta}$$

Therefore, wavefunctions in polarization (b) look like indices in an electric fugacity basis [\[Izeta\]](#Izeta){reference-type="eqref" reference="Izeta"}. To go from one polarization to another, one should use Fourier transform,

$f^{(b)}(x,\bar x;\hbar)= f^{(b)}(m,\zeta;\hbar) = \sum_{e\in {\mathbb Z}} f^{(d)}(m,e;\hbar)\,\zeta^e\,,$

just as described below [\[chargeindex\]](#chargeindex){reference-type="eqref" reference="chargeindex"}.

Further confirmation of the relation between Chern-Simons wavefunctions and indices comes from analyzing the algebra of operators acting on the Hilbert spaces in Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"}. In *any* polarization, the coordinates $X,\overline X,P,\overline P$ become promoted to operators with commutation relations

$$\big[\hat P,\hat X\,\big]=\hbar\,,\qquad \big[\,\hat{\overline P},\hat{\overline X}\,\big]=-\hbar\,,\qquad \big[\hat P,\hat{\overline X}\,\big]=\big[\,\hat{\overline P},\hat X\,\big]=0\,. \label{CSops}$$

These relations can be read off directly from the form [\[ws1\]](#ws1){reference-type="eqref" reference="ws1"} of $\omega_{0,s}$. One can then work out the action of the operators on wavefunctions, in various polarizations. In particular, acting on $f^{(d)}(m,e;\hbar)$ we find

$$\hat X=m\tfrac\hbar 2-\partial_e\,,\qquad \hat P=e\tfrac\hbar2+\partial_m\,,\qquad \hat{\overline X}=m\tfrac\hbar 2+\partial_e\,,\qquad \hat {\overline P}=e\tfrac\hbar2-\partial_m$$

whereas acting on $f^{(b)}(m,\zeta;\hbar)$ we have

$$\hat X=X\,,\qquad \hat P=\hbar \,\partial_X\,,\qquad \hat{\overline X}=\overline X\,,\qquad \hat {\overline P}=-\hbar\,\partial_{\overline X}\,.$$

Even in the $(b)$ polarization, it is nice to note that the compactness of the position ${\rm Im}\,Z$ necessarily quantizes the spectrum of the conjugate momentum operator $\widehat{{\rm Re}P}=\tfrac12\big(\hat P+\hat {\overline P}\big) = e\tfrac\hbar2\,,$ $e\in {\mathbb Z}$.

It should be evident that the operator algebra just described is identical to the algebra of index operators from Sections [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"} and [\[sec:tetdiff\]](#sec:tetdiff){reference-type="ref" reference="sec:tetdiff"}, with the identification $(\hat X,\hat{\overline X},\hat P,\hat {\overline P})=(\hat X_+,\hat X_-,\hat P_+,\hat P_-)$. With this information in hand, we can move beyond Hilbert spaces and compare the actual wavefunctions of nontrivial 3-manifolds. As reviewed at the beginning of this section (and in many other places), the classical solutions to complex Chern-Simons theory on $M$ cut out a Lagrangian submanifold $\mathcal{L}_M$ in the boundary phase space $\mathcal{P}_{\partial M}$; and the quantum wavefunction of $M$ is annihilated by a quantization of the defining equations for the Lagrangian, $\hat \mathcal{L}_M\cdot \mathcal{Z}_M=0$. The quantization $\mathcal{L}_M\to \hat \mathcal{L}_M$ is universal in Chern-Simons theory, in the sense that it does not depend on a certain real or complex form of the gauge group, or on choices of polarization, *cf.* [@gukov-2003; @GW-branes]. Therefore, we can borrow results of [@Dimofte-QRS], where Lagrangians were quantized in analytically continued Chern-Simons theory, and simply apply them to find quantized Lagrangians in the present case of physical $SL(2,{\mathbb C})$ Chern-Simons at $k=0$.

The simplest example of such quantization is for a tetrahedron itself. The phase space is just our model phase space, $\mathcal{P}_{\partial\Delta}=\mathcal{P}$ with standard coordinates $x=z$, $p=z''$, and the classical Lagrangian $\mathcal{L}_\Delta$ is cut out by the equation $z''+z^{-1}-1=0$. Since the real symplectic form $\omega_{0,s}$ manifestly breaks the holomorphic structure of $\mathcal{P}$, it is perhaps better to write the Lagrangian as

$$\mathcal{L}_\Delta\,:\quad z''+z^{-1}-1 = 0\,,\qquad  \overline z''+\overline z^{-1}-1 = 0\,.$$

Then quantization with respect to $\omega_{0,s}$ produces operators $\hat \mathcal{L}_{\Delta+}=\hat z''+\hat z^{-1}-1$, $\hat \mathcal{L}_{\Delta-}=\hat{\overline z}''+\hat{\overline z}^{-1}-1$ that must annihilate the tetrahedron wavefunction. (As usual, we define $\hat z=\exp \hat Z$, etc.) In polarization (b), the equations determine

$$\mathcal{Z}^{CS}_\Delta(z,\overline z;\hbar) = \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r \,\overline z^{-1}} \label{CStet}$$

up to an overall function of $q$. Given the dictionary $z=q^{\frac m2}\zeta$ of [\[zzeta\]](#zzeta){reference-type="eqref" reference="zzeta"}, this establishes the equivalence of the Chern-Simons wavefunction with the index in an electric fugacity basis, up to normalization.

In order to understand $SL(2,{\mathbb C})$ Chern-Simons theory on a more general 3-manifold $M$ with boundary, we can decompose $M$ into ideal tetrahedra, and then try to apply the symplectic gluing framework of [@Dimofte-QRS]. This requires defining an affine symplectic $Sp(*,{\mathbb Z})$ action on the tetrahedron Hilbert spaces $\mathcal{H}= \mathcal{H}_{0,s}$ of Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"} and their products. It also requires an appropriate quantum version of symplectic reduction, in order to implement gluing. We will describe these operations in Section [\[sec:CSsymp\]](#sec:CSsymp){reference-type="ref" reference="sec:CSsymp"}. Of course, we will find that they coincide with the operations on the index $\mathcal{I}_M$ found in Section [\[sec:actions\]](#sec:actions){reference-type="ref" reference="sec:actions"}, so that Chern-Simons wavefunctions can be constructed using the index-gluing rules of Section [\[sec:rules\]](#sec:rules){reference-type="ref" reference="sec:rules"}. Moreover, asking for $SL(2,{\mathbb C})$ Chern-Simons wavefunctions at $k=0$ to be independent of a triangulation (invariant under 2-3 moves) even fixes the normalization of the single-tetrahedron wavefunction [\[CStet\]](#CStet){reference-type="eqref" reference="CStet"} to agree with that of the tetrahedron index. Taken together, these facts constitute an axiomatic proof

[^3]

that the index of $T_M$ is equivalent to an $SL(2,{\mathbb C})$ Chern-Simons wavefunction, $\mathcal{I}_M = \mathcal{Z}_M^{CS}$.

We may finally note that $SL(2,{\mathbb C})$ Chern-Simons theory has an obvious conjugation symmetry, stemming from the symmetry of the action [\[CSaction\]](#CSaction){reference-type="eqref" reference="CSaction"}. It acts on a semi-classical phase space $(\mathcal{P},\omega_{k,s})$ as complex conjugation and simultaneous exchange of $t$ and $\tilde t$, to preserve the symplectic form [\[wtt\]](#wtt){reference-type="eqref" reference="wtt"}. In the case $k=0$, this means $\hbar\to-\hbar$, or $q\to q^{-1}$. Following the dictionary [\[zzeta\]](#zzeta){reference-type="eqref" reference="zzeta"} or [\[tmZ\]](#tmZ){reference-type="eqref" reference="tmZ"}, we see that complex conjugation is precisely $\rho$ symmetry for the index, from Section [\[sec:kappa\]](#sec:kappa){reference-type="ref" reference="sec:kappa"}. Interestingly, the action of conjugation on wavefunctions suffers from the same "Fock space reorganization" subtleties as the index --- discussed briefly, for example, in Section 6.5 of [@Wfiveknots].

[^1]: An alternative unitarity structure with $s\in i {\mathbb R}$ was also discussed in [@Witten-cx]. However, it does not appear to have direct relevance for 3d indices.

[^2]: In the terminology of geometric quantization, all the polarizations in Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"} are *real* polarizations. One advantage of this is that quantum wavefunctions can then be expressed as standard functions, rather than sections of a line bundle, *cf.* [@Witten-cx].

[^3]: The same technicalities involving convergence and univalent edges from Section [\[sec:TM\]](#sec:TM){reference-type="ref" reference="sec:TM"} appear in Chern-Simons theory too. We mean a non-rigorous, physical "proof."
