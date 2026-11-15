---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-017-53-non-abelian-line-defects
section_title: "Non-abelian line defects"
section_number: 5.3
pages: 52-62
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.958
---
There are natural ways to use the three-dimensional theories $T_M$ to define domain walls in the UV for four-dimensional ${\cal N}=2$ $SU(2)$ gauge theories. A full account of that construction will be the subject of a future publication [@DGGV-hybrid]. For now, we will content ourselves with sketching some interesting directions of inquiry. For simplicity, we will focus on the example of $SU(2)$ ${\cal N}=2^*$ SYM.

We would like to establish a very concrete parallel between the general structure of Pestun's $S^4$ partition function and the refined index. In the presence of line defects or domain walls at the equator, localization reduces Pestun's partition function to a matrix element of a self-adjoint operator [@DGOT; @AGGTV; @DGG-defects] $$\langle Z_S| \hat O | Z_N \rangle \equiv \int d\nu(a') d\nu(a) \bar Z_{\mathrm{inst}}(a') O(a',a)  Z_{\mathrm{inst}}(a)$$ Here $Z_{\mathrm{inst}}(a)$ is the instanton partition function (together with the tree-level contribution) for the gauge theory, which is naturally thought of as a wavefunction, $| Z_N\rangle=Z_{\mathrm{inst}}(a)$, and $\langle Z_S |$ is the complex conjugate; $d\nu(a)$ is the one-loop integration measure, and $O(a',a)$ is an integration kernel that encodes the effect of the domain wall or line defect. For domain walls, $O(a',a)$ is basically the $S^3$ partition function of the domain wall 3d degrees of freedom. For 'tHooft-Wilson line defects $L$, $O(a,a')$ is a sum over delta functions, so that $\hat O$ takes the form of a sum over shift operators $$\hat O_L = \sum_n R_n(a) e^{2 \pi n \partial_a}$$ The functions $R_n(a)$ can in principle be computed from the geometry of monopole moduli spaces, as they account for "bubbling monopole" configurations near the line defect [@GOP-tHooft] that interpolate between the "bare" 'tHooft monopole magnetic flux and an Abelian magnetic flux $n/2$.

A simple way to understand the physical meaning of the matrix element is to realize the configuration starting from two hemispheres with Dirichlet boundary conditions for the gauge fields, and then glue together the hemispheres, along with any extra degrees of freedom at the equator, by gauging appropriate 3d flavor symmetries. In particular, it is natural to see the wavefunction $|Z_N\rangle$ as the partition function on a hemisphere with Dirichlet boundary conditions. Notice that the notion of Dirichlet boundary condition is not S-duality invariant, but depends on a choice of weakly coupled duality frame. Hence $| Z_N\rangle$ transforms in interesting ways under S-duality, while the $S^4$ partition function $\langle Z_S| Z_N \rangle$ is S-duality invariant. Incidentally, in the gluing procedure one also has to pick adequate boundary conditions for the hypers, as discussed before. Different choices split the one-loop measure in different way among North and South hemisphere, and change the normalization of the wavefunctions.

In the context of AGT [@AGT], the wavefunctions are identified with BPZ conformal blocks, and the matrix elements with 2d CFT correlation functions. The operators $O_L$ coincide with the so-called Verlinde line operators, or with topological defects in the 2d CFT. Crucially, they can be computed explicitly through a laborious algorithm [@AGGTV; @DGOT], sidestepping the difficult localization calculations of gauge theory. The whole structure described above can be deformed to generic $b$, though the corresponding deformation $S^4_b$ of the $S^4$ geometry has not been described yet. We will need the generalized formulae in the following. The simplest 'tHooft-Wilson loop for ${\cal N}=2^*$ SYM is the operator of magnetic charge $1$ and electric charge $s$, $$\hat O_{1,s} = \frac{\sin \pi b(2 a - Q -\mu)}{\sin \pi b(2a-Q)}e^{i \pi b (2a-Q) s - \frac{b}{2}\partial_a} + \frac{\sin \pi b(2 a - Q + \mu)}{\sin \pi b(2a-Q)}e^{-i \pi b (2a-Q) s + \frac{b}{2}\partial_a}\,.$$ It is self-adjoint against the standard Liouville measure $d\nu(a) = \sin \pi b (2 a-Q) \sin \pi/b (2a-Q) da$, as long as the mass parameter $\mu$ lies in the physical line $Q/2+ i {\mathbb R}$. Notice that the first factor in the measure cancels against the denominators in $\hat O_{1,s}$ and the second factor in the measure commutes with the shift operators. The opposite is true for a second family of operators, obtained from $\hat O_{1,s}$ by $b \to b^{-1}$. The operator is explicitly symmetric under $a \to Q-a$ but not under $\mu \to Q-\mu$, due to an asymmetric split of the one-loop factors between North and South hemispheres. The symmetry $\mu \to Q-\mu$ can be implemented by conjugation by an appropriate rescaling factor.

In order to set up our analogy, we can break down the calculation of the index of a 4d theory, possibly in the presence of a domain wall on the equator of the $S^3$ or of line defects, by first defining a "half-index" $I\!I_m(q,\zeta,\Gamma)$ as the index of the 4d gauge theory on half of $S^3$ with Dirichlet boundary conditions. This will be a function of the fugacities and magnetic fluxes $\zeta,m$ associated to the 3d flavor symmetries and of the choice of S-duality frame $\Gamma$. The full index of the 4d theory can be recovered by combining the half-indices for the two hemispheres with the measure for a three-dimensional non-abelian gauge theory: $$\left( I\!I_S | I\!I_N \right) \equiv \sum_m \oint \frac{d\zeta}{2\pi i\zeta} \Delta_m(\zeta) I\!I_m(q,\zeta,N) I\!I_m(q,\zeta,S)\,.$$ In the absence of 'tHooft operators in the bulk, we expect $I\!I_m(q,\zeta,\Gamma)$ to be non-zero only at $m=0$. The measure $\Delta_0(\zeta)$ is the usual Vandermonde measure. In the presence of 'tHooft loops, we will have contributions at non-zero (possibly half-integral) $m$ and we will find a natural generalization of the measure, $$\Delta_m(\zeta)= \frac{1}{2} (q^{m/2} \zeta-q^{-m/2} \zeta^{-1})(q^{-m/2} \zeta-q^{m/2} \zeta^{-1})\,.$$

How can we add 'tHooft operators to the half-index? The hard way would be to do a careful localization computation, taking into account bubbling monopole contributions that screen the magnetic charge at the pole, giving a variety of possible Abelian fluxes $m$ at the equator. But there is a shortcut. We can try to borrow the calculation of $R_n(a)$ from the Verlinde loop operators. Notice that if we assume the existence of a dictionary, these are very constrained. Namely, the OPE of line defects and the Ward identities satisfied when they are brought to collide with domain walls must take the same form for the $S^4_b$ partition function and for the index, upon the dictionary established in the rest of this paper between vector-multiplet vevs and fugacities, and $2 \pi i b^2 \to \hbar$. In particular, we will map $$\label{opdict}
 e^{i \pi b (2a-Q)} \to \hat x_+ = q^{m/2} \zeta  \qquad  e^{b \partial_a} \to \hat p_+ = e^{\partial_m + \frac{\hbar}{2} \partial_{\log \zeta}} \qquad  e^{i \pi b (2m-Q)} \to \eta$$ We can replace $(\hat x_+,\hat p_+)$ with $(\hat x_-,\hat p_-)$ for operators acting from the opposite side of the equator.

We are led to conjecture that the half-index in the presence of a 'tHooft-Wilson loop $L$ can be computed by acting on the half-index in the absence of the loop with the image of $\hat O_L$ under the above dictionary. Let's consider a concrete example. The 4d index of $SU(2)$ ${\cal N}=2^*$ is

$$\begin{aligned}
&I(\eta,q) = \oint \frac{d\zeta}{4\pi i\zeta} (1-\zeta^2)(1-\zeta^{-2}) \\\notag &\times \prod_{n=0}^{\infty} \frac{\left(1-q^{n+1}\right)^2 \left(1-\frac{q^{n+1}}{\zeta^2}\right)^2 \left(1-\zeta^2 q^{n+1}\right)^2}{\left(1-\eta^{-1}q^{n+\frac{1}{2}}\right) \left(1-\eta q^{n+\frac{1}{2}}\right)
   \left(1-\frac{q^{n+\frac{1}{2}}}{\eta \zeta^2}\right) \left(1-\frac{\eta q^{n+\frac{1}{2}}}{\zeta^2}\right) \left(1-\frac{\zeta^2 q^{n+\frac{1}{2}}}{\eta}\right) \left(1-\eta \zeta^2 q^{n+\frac{1}{2}}\right)}\,,
\end{aligned}$$

and the half-index is $$\begin{aligned}
&I\!I_m(\zeta,\eta,q) = \delta_{m,0} \prod_{n=0}^{\infty} \frac{\left(1-q^{n+1}\right)\left(1-\frac{q^{n+1}}{\zeta^2}\right) \left(1-\zeta^2 q^{n+1}\right)}{ \left(1-\eta^{-1} q^{n+\frac{1}{2}}\right)
   \left(1-\frac{\eta^{-1} q^{n+\frac{1}{2}}}{\zeta^2}\right) \left(1-\eta^{-1} \zeta^2 q^{n+\frac{1}{2}}\right)}\,,
\end{aligned}$$ so that $$I(\eta,q) =  \sum_m \oint \frac{d\zeta}{2\pi i\zeta} \Delta_m(\zeta) I\!I_m(q,\zeta,\eta) I\!I_m(q,\zeta,\eta^{-1})\,.$$

Now we can act with a Wilson loop operator, $2 \cos \pi b (2a-Q) \to q^{m/2} \zeta+q^{-m/2} \zeta^{-1}$, following [\[opdict\]](#opdict){reference-type="eqref" reference="opdict"}. We get that the half-index in the presence of a Wilson loop is simply multiplied by the appropriate character, thanks to the $\delta_{m,0}$ constraint: $$\begin{aligned}
\hat O_{0,1} I\!I_m(\zeta,\eta,q) = \left(\zeta + \zeta^{-1} \right) I\!I_m(\zeta,\eta,q)\,.
\end{aligned}$$

On the other hand, if we act with the translated 'tHooft-Wilson operator $$\begin{aligned}
\hat O_{1,s} &\,=\, \frac{q^{m/2-1/4} \zeta \eta^{-1/2} - q^{-m/2+1/4} \zeta^{-1} \eta^{1/2}}{q^{m/2} \zeta - q^{-m/2} \zeta^{-1}}q^{- s/4} q^{s m/2} \zeta^s p_+^{-1/2} \notag \\ &\qquad+\, \frac{q^{m/2+1/4} \zeta \eta^{1/2} - q^{-m/2-1/4} \zeta^{-1} \eta^{-1/2}}{q^{m/2} \zeta - q^{-m/2} \zeta^{-1}}q^{- s/4} q^{-s m/2} \zeta^{-s} p_+^{1/2}\,,
\end{aligned}$$ we get $$\begin{aligned}
& \hspace{-.4cm}\hat O_{1,s}  I\!I_m(\zeta,\eta,q) = q^{1/4} \eta^{1/2} \left( \zeta^s \delta_{m,1/2} + \zeta^{-s} \delta_{m,-1/2}  \right) \prod_{n=0}^{\infty} \frac{\left(1-q^{n+1}\right)\left(1-\frac{q^{n+3/2}}{\zeta^2}\right) \left(1-\zeta^2 q^{n+3/2}\right)}{ \left(1-\eta^{-1} q^{n+\frac{1}{2}}\right)
   \left(1-\frac{\eta^{-1} q^{n+1}}{\zeta^2}\right) \left(1-\eta^{-1} \zeta^2 q^{n+1}\right)}\,.
\end{aligned}$$ Several useful cancellations led to a simple result. We would have derived the same result if we had used $(\hat x_-,\hat p_-)$ in the dictionary, as it should be: the half-index for a bare hemisphere should intertwine the line defects acting on opposite sides of the equator. Notice that we chose a measure $\Delta_m(\zeta) = \frac{1}{2} (x_+ - x_+^{-1})(x_- - x_-^{-1})$, which mimics the properties of the Liouville measure.

We can now compare the index in the presence of two basic Wilson loops, one for each hemisphere, $$\begin{aligned}
&I_{el}(\eta,q) = \oint \frac{d\zeta}{4\pi i\zeta} (1-\zeta^2)(1-\zeta^{-2}) \\\notag &\times\prod_{n=0}^{\infty} \frac{(\zeta + \zeta^{-1})^2 \left(1-q^{n+1}\right)^2 \left(1-\frac{q^{n+1}}{\zeta^2}\right)^2 \left(1-\zeta^2 q^{n+1}\right)^2}{\left(1-\eta^{-1}q^{n+\frac{1}{2}}\right) \left(1-\eta q^{n+\frac{1}{2}}\right)
   \left(1-\frac{q^{n+\frac{1}{2}}}{\eta \zeta^2}\right) \left(1-\frac{\eta q^{n+\frac{1}{2}}}{\zeta^2}\right) \left(1-\frac{\zeta^2 q^{n+\frac{1}{2}}}{\eta}\right) \left(1-\eta \zeta^2 q^{n+\frac{1}{2}}\right)}\,,
\end{aligned}$$ with the index in the presence of two 'tHooft loops (of zero electric charge) , $$\begin{aligned}
&I(\eta,q) =2 \oint \frac{d\zeta}{4\pi i\zeta} (1-q^{1/2} \zeta^2)(1-q^{1/2} \zeta^{-2}) \\\notag &\quad\times \prod_{n=0}^{\infty} \frac{\left(1-q^{n+1}\right)^2 \left(1-\frac{q^{n+3/2}}{\zeta^2}\right)^2 \left(1-\zeta^2 q^{n+3/2}\right)^2}{\left(1-\eta^{-1}q^{n+\frac{1}{2}}\right) \left(1-\eta q^{n+\frac{1}{2}}\right)
   \left(1-\frac{q^{n+1}}{\eta \zeta^2}\right) \left(1-\frac{\eta q^{n+1}}{\zeta^2}\right) \left(1-\frac{\zeta^2 q^{n+1}}{\eta}\right) \left(1-\eta \zeta^2 q^{n+1}\right)}\,.
\end{aligned}$$ The factor of $2$ arises from the sum of the abelian contributions of magnetic charge $\pm 1/2$. We absorbed the factors $q^{1/4} \eta^{1/2}q^{1/4} \eta^{-1/2}$ in the measure. Amazingly, the two results agree, computationally, to as high an order as we could check in the $q$ expansion. This is a striking verification that our prescription of the line defects is compatible with S-duality.

# The index as $SL(2,{\mathbb C})$ Chern-Simons theory {#sec:CS}

Throughout the preceding sections, there have been various hints that the index $\mathcal{I}_M(m,e;q)$ of a theory $T_M$ may have some relation to complex Chern-Simons theory on $M$ itself, *i.e.* Chern-Simons theory with complex gauge group $SL(2,{\mathbb C})$. For example, the constructions of $T_M$ and $\mathcal{I}_M$ involve choosing a polarization on the phase space $\mathcal{P}_{\partial M}$, and this is precisely the phase space of complex Chern-Simons theory on a 3-manifold $M$ with boundary [@Wit-Jones; @Witten-cx]. In addition, the flat $SL(2,{\mathbb C})$ connections in the bulk of $M$, which project to the Lagrangian submanifold $\mathcal{L}_M$,

$$\begin{aligned}
 \mathcal{L}_M &\;=\;\{\text{flat $SL(2,{\mathbb C})$ connections on $\partial M$ that extend to $M$}\} \notag \\
\cap\;\; & \notag \\
\mathcal{P}_{\partial M} &\;=\;\{\text{flat $SL(2,{\mathbb C})$ connections on $\partial M$}\}\,, \notag
\end{aligned}$$

correspond to spaces of SUSY vacua for $T_M$ [@DGH; @DGG]; and these flat connections on $M$ are the classical solutions to Chern-Simons theory. Moreover, we saw in Sections [\[sec:TM\]](#sec:TM){reference-type="ref" reference="sec:TM"} and [\[sec:3d4d\]](#sec:3d4d){reference-type="ref" reference="sec:3d4d"} that a quantization of the Lagrangian's defining equations, $\hat\mathcal{L}_M$, provides difference operators that annihilate the index. This again is an expected property of Chern-Simons wavefunctions: the constraints describing classical solutions $(\mathcal{L}_M)$ become promoted to quantum operators $(\hat\mathcal{L}_M)$ that annihilate the quantum wavefunctions [@gukov-2003].

To be even more suggestive, consider the tetrahedron index in the electric fugacity basis [\[Iztet2\]](#Iztet2){reference-type="eqref" reference="Iztet2"}. Note that in the definition of the index as a partition function on $S^2\times S^1$, the parameter $q=e^\hbar$ is real, while $\zeta = e^{i\theta}$ is a pure phase. We can then recombine $m$ and $\theta$ into complex variables, as in Section [\[sec:T1\]](#sec:T1){reference-type="ref" reference="sec:T1"} :

$$Z = \frac{m}{2}\hbar+i\theta\,,\qquad \overline Z = \frac{m}{2}\hbar-i\theta\,, \label{tmZ}$$

or

$$z = e^Z = q^{\frac m2}\zeta\,,\qquad \overline z = e^{\overline Z}=q^{\frac m2}\zeta^{-1}\,; \label{tmz}$$

so that the tetrahedron index takes the form

$$\mathcal{I}_\Delta(m;q,\zeta) = \mathcal{I}_\Delta(z,\overline z;q) = \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r\,\overline{z}^{-1}}\,.$$

If we define $\mathcal{Z}_\Delta(z;q)\equiv\prod_{r\geq 1} (1-q^r z^{-1})$ for $|q|<1$, and allow ourselves the "Fock space reorganization" $\prod_{r\geq 1}(1-q^{-r}z)=\prod_{r\geq 0}(1-q^{r}z)^{-1}$, we would then have an index

$$\mathcal{I}_\Delta(z,\overline z;q) \;\text{``}\!=\!\text{''}\; \mathcal{Z}_\Delta(z;q)\,\mathcal{Z}_\Delta(\overline z;q^{-1})\,, \label{Dfact}$$

factorized into identical holomorphic and antiholomorphic pieces.

Such a factorization is familiar from the studies of $SL(2,{\mathbb C})$ Chern-Simons partition functions in [@gukov-2003; @DGLZ; @Wit-anal]. More generally, the physical Chern-Simons partition function on a 3-manifold $M$ would be a sum over classical flat connections $\alpha$ with fixed boundary conditions $x$,

$$\mathcal{Z}^{\rm CS}_M(x,\overline x;q)\; = \; \sum_{\alpha}n_{\alpha\bar\alpha}\,\mathcal{Z}_M^\alpha(x;q)\,\mathcal{Z}_M^{\bar \alpha}(\overline x;q^{-1})\,, \label{CSfact}$$

and with $n_{\alpha\bar\alpha}$ real and diagonal.

[^1] In the case of the tetrahedron, there is a unique flat connection at fixed boundary condition $x=z$, and so a single term in [\[CSfact\]](#CSfact){reference-type="eqref" reference="CSfact"}. Note that [\[CSfact\]](#CSfact){reference-type="eqref" reference="CSfact"} has a symmetry under complex conjugation and exchange of $q$ and $q^{-1}$, which looks like $\rho$ symmetry [\[kind\]](#kind){reference-type="eqref" reference="kind"} for the index.

Our goal in this section is to make the relation between $SL(2,{\mathbb C})$ Chern-Simons theory and the index as precise as possible. There actually exist several inequivalent quantizations of complex Chern-Simons theory --- corresponding to different real symplectic structures on the complex phase space $\mathcal{P}_{\partial M}$ --- and we will see that one special choice is related to the generalized index $\mathcal{I}_M(m;q,\zeta)$. An interesting open question is to understand what the other quantizations might mean. In Section [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}, we will give a "top-down," qualitative view of the equivalence between Chern-Simons theory and the index by considering the theory of M5-branes in the geometry $S^1\times S^2\times M$ and applying various known dualities.

## Quantization at $k=0$ {#sec:k0}

Let's begin by reviewing a few facts about Chern-Simons theory with gauge group $G_{\mathbb C}=SL(2,{\mathbb C})$ [@Wit-CSgrav; @Witten-cx; @gukov-2003]. The most general complex bulk action on a 3-manifold $M$ is

$$S_{CS}(M) \,=\, \frac{t}{8\pi}\int_M {\rm Tr \,}\Big(\mathcal{A}\, d\mathcal{A}+\frac{2}{3}\mathcal{A}^3\Big)\,+\,\frac{\tilde t}{8\pi}\int_M {\rm Tr \,}\Big(\overline\mathcal{A}\, d\overline\mathcal{A}+\frac{2}{3}\overline\mathcal{A}^3\Big)\,,
\label{CSaction}$$

where $\mathcal{A}$ is a local $\mathfrak{g}_{\mathbb C}=\mathfrak{sl}(2,{\mathbb C})$-valued one-form, defined modulo the standard gauge transformations $\mathcal{A}\to g^{-1}\mathcal{A}\, g+ g^{-1}dg$. Unlike the case of real Chern-Simons theory, the complex action here contains both holomorphic and antiholomorphic terms, and each comes with its own coupling constant, here $t$ and $\tilde t$. Let us write

$$t=k+is\,,\qquad \tilde t=k-is\,.$$

A priori, $k$ and $s$ are independent complex parameters. However, independence of the path integral measure $\exp\big[ i S_{CS}(M) \big]$ under large gauge transformations forces $k$ to be an integer. Moreover, unitarity --- the statement that the path integral be conjugated under a change of orientation on $M$ --- requires $s\in {\mathbb R}$.

[^2]

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

[^3]

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

[^4]

that the index of $T_M$ is equivalent to an $SL(2,{\mathbb C})$ Chern-Simons wavefunction, $\mathcal{I}_M = \mathcal{Z}_M^{CS}$.

We may finally note that $SL(2,{\mathbb C})$ Chern-Simons theory has an obvious conjugation symmetry, stemming from the symmetry of the action [\[CSaction\]](#CSaction){reference-type="eqref" reference="CSaction"}. It acts on a semi-classical phase space $(\mathcal{P},\omega_{k,s})$ as complex conjugation and simultaneous exchange of $t$ and $\tilde t$, to preserve the symplectic form [\[wtt\]](#wtt){reference-type="eqref" reference="wtt"}. In the case $k=0$, this means $\hbar\to-\hbar$, or $q\to q^{-1}$. Following the dictionary [\[zzeta\]](#zzeta){reference-type="eqref" reference="zzeta"} or [\[tmZ\]](#tmZ){reference-type="eqref" reference="tmZ"}, we see that complex conjugation is precisely $\rho$ symmetry for the index, from Section [\[sec:kappa\]](#sec:kappa){reference-type="ref" reference="sec:kappa"}. Interestingly, the action of conjugation on wavefunctions suffers from the same "Fock space reorganization" subtleties as the index --- discussed briefly, for example, in Section 6.5 of [@Wfiveknots].

[^1]: Explicit expansions of this type, not for indices but for the closely related ellipsoid partition functions of some theories in class $\mathcal{R}$, have recently appeared in [@Pasquetti-fact].

[^2]: An alternative unitarity structure with $s\in i {\mathbb R}$ was also discussed in [@Witten-cx]. However, it does not appear to have direct relevance for 3d indices.

[^3]: In the terminology of geometric quantization, all the polarizations in Table [\[tab:pol\]](#tab:pol){reference-type="ref" reference="tab:pol"} are *real* polarizations. One advantage of this is that quantum wavefunctions can then be expressed as standard functions, rather than sections of a line bundle, *cf.* [@Witten-cx].

[^4]: The same technicalities involving convergence and univalent edges from Section [\[sec:TM\]](#sec:TM){reference-type="ref" reference="sec:TM"} appear in Chern-Simons theory too. We mean a non-rigorous, physical "proof."
