---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-001-11-the-kashaev-invariant-and-perturbative-chern
section_title: "The Kashaev invariant and perturbative Chern-Simons theory"
section_number: 1.1
pages: 1-4
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.667
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.summary label="sub.summary"}

The *Kashaev invariant* $\langle K \rangle_N \in \mathbb C$ of a knot $K$ in 3-space (for $N=2,3,\dots$) is a powerful sequence of complex numbers determined by the *Jones polynomial* of the knot [@Jo] and its cablings [@Turaev; @Witten-Jones]. The *Volume Conjecture* of Kashaev and Murakami-Murakami [@K94; @K95; @MM] relates the Kashaev invariant of a hyperbolic knot $K$ with the hyperbolic volume $\mathrm{Vol}(M)$ of its complement $M=S^3\setminus K$ [@Th] $$\lim_{N\to\infty} \frac{1}{N} \log|\langle K \rangle_N|=\frac{\mathrm{Vol}(M)}{2\pi} \,.$$ A generalization of the Volume Conjecture [@Gu] predicts a full asymptotic expansion of the Kashaev invariant to all orders in $1/N$ $$\label{eq.KAS}
\langle K \rangle_N \overset{N\to\infty}{\sim} \mathcal{Z}_M(2 \pi i /N)$$ for a suitable formal power series $$\label{eq.ZMhb}
\qquad \mathcal{Z}_M(\hbar)=\exp\bigg(\frac1\hbar S_{M,0}-\frac32\log\hbar+S_{M,1}
+\sum_{n\geq 2}\hbar^{n-1}S_{M,n}\bigg)\,,\qquad \hbar = \frac{2\pi i}{N}\,.$$ The formal power series $\mathcal{Z}_M(\hbar)$ in [\[eq.ZMhb\]](#eq.ZMhb){reference-type="eqref" reference="eq.ZMhb"} is conjectured to coincide with the perturbative partition function of Chern-Simons theory with complex gauge group $\mathrm{SL}(2,\mathbb C)$ along the discrete faithful representation $\rho_0$ of the hyperbolic manifold $M$. Combining such an interpretation with further conjectures of [@DGLZ; @Ga1; @GL] one predicts that

-   $S_{M,0}=i(\text{Vol}_M+i\text{CS}_M) \in \mathbb C/(4 \pi^2\mathbb Z)$ is the complexified volume of $M$ (*cf.* [@Thurston-paper; @Neumann-combi]).

-   $S_{M,1}$ is related [@Witten-cx; @BNW; @GuM] to the nonabelian Ray-Singer torsion [@RS], which ought to equal (*cf.* [@Muller-cx]) the combinatorial nonabelian Reidemeister torsion. More precisely, [@DG Conj.1.8] we should have $$\label{TRMS1}
    \tau^\mathrm{R}_M= 4\pi^3 \exp(-2 S_{M,1}) \in E_M^*$$ where $\tau^\mathrm{R}_M$ is the nonabelian Reidemeister-Ray-Singer torsion of $M$ with respect to the meridian [@Po; @Db], and $E_M$ is the invariant trace field of $M$.

-   For $n \geq 2$, the *$n$-loop invariants* $S_{M,n}$ are conjectured to lie in the invariant trace field $E_M$ [@DGLZ; @Ga1].

The generalization [\[eq.KAS\]](#eq.KAS){reference-type="eqref" reference="eq.KAS"} of the Volume Conjecture has been numerically verified for a few knots using either state-integral formulas for Chern-Simons theory when available [@DGLZ] or a numerical computation of the Kashaev invariant and its numerical asymptotics, lifted to algebraic numbers [@GZ; @Ga2].

Our goal is to provide an exact, combinatorial definition of the formal power series $\mathcal{Z}_M(\hbar)$ via formal Gaussian integration using the shape parameters and the Neumann-Zagier matrices of a regular ideal triangulation of $M$. Our definitions

-   express the putative torsion $\exp(-2S_{M,1})$ and the $n$-loop invariants $S_{M,n}$ manifestly in terms of the shape parameters $z_i$ and the gluing matrices of a regular ideal triangulation $\mathcal{T}$ of $M$;

-   manifestly deduce that the putative torsion and the $n$-loop invariants for $n \geq 2$ are elements of the invariant trace field;

-   explain the difference of $\mathcal{Z}_M(\hbar)$ for pairs of geometrically similar knots studied by Zagier and the second author;

-   provide an effective way to compute the $n$-loop invariants using standard commands of the `SnapPy` toolbox [@SnapPy] --- as demonstrated for $n=1,2,3$ for hyperbolic knots with at most 14 crossings; and

-   allow efficient tests of the asymptotics of the Volume Conjecture [\[eq.KAS\]](#eq.KAS){reference-type="eqref" reference="eq.KAS"}, the "1-loop Conjecture" [\[TRMS1\]](#TRMS1){reference-type="eqref" reference="TRMS1"} and other conjectures in Quantum Topology.

We note that we only define $\exp(-2S_{M,1})$ up to a sign, and $S_{M,2}$ modulo $\mathbb{Z}/24$. All higher $n$-loop invariants are defined unambiguously.

Although we give a purely combinatorial definition of $\mathcal{Z}_M(\hbar)$ without any knowledge of state integrals or Chern-Simons theory with complex gauge group, in Section [\[sec.SIM\]](#sec.SIM){reference-type="ref" reference="sec.SIM"} we explain how our definition follows from the state-integral model of the first author [@D1] and its perturbative expansion.
