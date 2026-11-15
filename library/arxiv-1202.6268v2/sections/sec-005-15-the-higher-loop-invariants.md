---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-005-15-the-higher-loop-invariants
section_title: "The higher-loop invariants"
section_number: 1.5
pages: 6-8
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.944
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.nloop label="sub.nloop"}

In this section we define the higher loop invariants $S_{\mathcal{T},n}$ for $n \geq 2$. They are analyzed in detail in Section [\[sec.SIM\]](#sec.SIM){reference-type="ref" reference="sec.SIM"}, using a state integral [\[SIM\]](#SIM){reference-type="eqref" reference="SIM"}. The result, however, may be summarized as follows. Let us introduce a formal power series $$\label{eq.psixz}
\psi_{\hbar}(x;z)=\exp\left(
\sum_{n,\, k,\, 2n+k-2 > 0} 
\frac{\hbar^{n+\tfrac k2-1} (-x)^kB_n}{n!k!}\, {\rm Li}_{2-n-k}(z^{-1})
\right) \in \mathbb Q(z)[\![x,\hbar^{\frac12}]\!]$$ where $B_n$ is the $n^{\rm th}$ *Bernoulli number* (with $B_1=+1/2$), and $L_m(z)$ is the $m^{\rm th}$ polylogarithm. Note that ${\rm Li}_m(z) \in (1-z)^{-m-1}\mathbb Z[z]$ is a rational function for all nonpositive integers $m$. This formal series comes from the asymptotic expansion of the quantum dilogarithm function after removal of its two leading asymptotic terms [@Ba; @FK-QDL; @Fa]. The quantum dilogarithm is the Chern-Simons partition function of a single tetrahedron and its asymptotics are studied in detail in Section [\[sec.SIM\]](#sec.SIM){reference-type="ref" reference="sec.SIM"}.

We fix an enhanced Neumann-Zagier datum $\widehat 
\beta_{\mathcal T}=(z,\mathbf A, \mathbf B,f)$ of an oriented 1-cusped manifold $M$ and a regular ideal triangulation $\mathcal T$ with $N$ tetrahedra. Let $\nu=\mathbf A f + \mathbf B f''$. We assume that

$$\det(\mathbf B) \neq 0\,,\qquad  \tau_M \neq 0\,. \notag$$

The condition $\det(\mathbf B) \neq 0$ is always satisfied with a suitable labeling of shapes; see Lemma [\[lemma.B\]](#lemma.B){reference-type="ref" reference="lemma.B"}. In that case, Lemma [\[lemma.BA\]](#lemma.BA){reference-type="ref" reference="lemma.BA"} implies that

$$\mathcal{H}=-\mathbf B^{-1}\mathbf A+\Delta_{z'}\,,$$

is a symmetric matrix, where $\Delta_{z'}=\text{diag}(z_1',...,z_N')$. We define

$$f_{\mathcal T,\hbar}(x;z)=
\exp \bigg(-\frac{\hbar^{\frac12}}{2} x^T \mathbf B^{-1} \nu+\frac\hbar8 f^T\mathbf B^{-1}\mathbf A f \bigg) 
\prod_{i=1}^N \psi_{\hbar}(x_i,z_i) \in \mathbb Q(z)[\![x,\hbar^{\frac12}]\!]\,,
\quad$$

where $x=(x_1,...,x_N)^T$ and $z=(z_1,...,z_N)$. Assuming that $\mathcal{H}$ is invertible, a formal power series $f_\hbar(x)\in \mathbb Q(z)[\![x,\hbar^{\frac12}]\!]$ has a *formal Gaussian integration*, given by (*cf.* [@BIZ])

$$\label{formalG}
\langle f_{\hbar}(x)\rangle= \frac{\int dx \, e^{-\frac12x^T \mathcal{H}\,x}f_{\hbar}(x)}{\int dx \, e^{-\frac12x^T \mathcal{H}\,x}}\,.$$

This integration is defined by expanding $f_\hbar(x)$ as a series in $x$, and then formally integrating each monomial, using the quadratic form $\mathcal{H}^{-1}$ to contract $x$-indices pairwise.

::: definition
[]{#def.Sn label="def.Sn"} With the above conventions, we define

$$\exp\left(\sum_{n=2}^\infty S_{\mathcal T,n}(z) \hbar^{n-1}\right)
:=
\langle f_{\mathcal T,\hbar}(x;z)
\rangle\,.$$
:::

::: remark
[]{#rem.tau3n label="rem.tau3n"} Notice that the result involves only integral powers of $\hbar$ and each term is a rational function in the complex numbers $z$. Moreover, $S_{\mathcal T,n} \in \tau_{\mathcal{T}}^{-3n+3} \mathbb Q[z,z',z'']$ for all $n \geq 2$. This follows from the fact that the connected Feynman diagrams that contribute to $S_{\mathcal{T},n}$ have at most $3n-3$ edges and each edge (contracted by $\mathcal{H}^{-1}$) contributes a factor of $\det(\mathcal{H})^{-1}$. Thus, we can also write

$$\label{tordivide}
\exp\left(\sum_{n=2}^\infty S_{\mathcal T,n} \hbar^{n-1}\right)=
1+ \sum_{n=1}^\infty  \frac{\widetilde S_{\mathcal T,n}}{\tau_{\mathcal{T}}^{3n}}\hbar^n \,,$$

where $\widetilde S_{\mathcal{T},n} \in \mathbb Q[z,z',z'']$. Experimentally, it appears that $\widetilde S_{\mathcal T,n}$ have lower complexity than $S_{\mathcal T,n}$, see Appendix [\[app.compute\]](#app.compute){reference-type="ref" reference="app.compute"}.
:::
