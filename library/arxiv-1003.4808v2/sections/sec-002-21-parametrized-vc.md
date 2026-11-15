---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-002-21-parametrized-vc
section_title: "Parametrized VC"
section_number: 2.1
pages: 6-9
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.926
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
The original volume conjecture only held for a special root of unity $q = e^{\frac{2\pi i}{N}}$. In order to generalize to arbitrary $q=e^{\frac{2\pi i}{k}}$, the appropriate limit to consider is

$$k\to\infty\,,\qquad N\to\infty\,,\qquad u := i\pi\frac { N} k \quad\text{fixed}\, \label{lim}$$

(or $q\to 1$, $q^N = e^{2u}$ fixed). The question, then, is how to understand

$$\lim_{k,N\to\infty} J_N(K;q)^{1/k}\quad ?$$

The answer, described in [@gukov-2003], uses the fact that in correspondence with the "deformation" in the colored Jones polynomial, there exists a one-parameter deformation of the hyperbolic structure on a knot complement $S^3\backslash K$. To understand this, let $\mu$ be a small loop linking the excised knot $K$, as in Figure [1](#fig:lm){reference-type="ref" reference="fig:lm"}a. In terms of flat $SL(2,{\mathbb{C}})$ connections, the geodesically complete hyperbolic metric has a parabolic $SL(2,{\mathbb{C}})$ holonomy around $\mu$,

$${\rm Hol}(\mu,{\rm complete}) =  \pm\begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix}\,, \label{hol0}$$

whereas the incomplete, $u$-deformed hyperbolic metric/$SL(2,{\mathbb{C}})$ connection is defined to have a holonomy conjugate to

$${\rm Hol}(\mu,u)  = \begin{pmatrix} e^u & 1 \\ 0 & e^{-u} \end{pmatrix}\,. \label{holu}$$

(As long as $e^{u}\neq e^{-u}$, this deformed holonomy is also conjugate to the purely diagonal matrix ${\rm diag}(e^u,e^{-u})$.) The resulting metric is not complete. For example, when $u$ is purely imaginary, the $u$-deformed metric has a conical cusp of angle $2{\rm Im}(u)$ at the knot $K$.

The complexified hyperbolic volume for this one-parameter family of metrics can again be defined in terms of the Chern-Simons functional $I_{CS}({\cal A})$ appearing in [\[ICS\]](#ICS){reference-type="eqref" reference="ICS"}. Now, however, ${\cal A}={\cal A}(u)$ should be a flat $SL(2,{\mathbb{C}})$ connection with prescribed holonomy [\[holu\]](#holu){reference-type="eqref" reference="holu"}. The \"parametrized\" volume conjecture then takes the form [@gukov-2003]

$$\boxed{ J_N(K;q) \;\overset{k,N\to\infty}{\sim}\; e^{-\frac{k}{4\pi i}I_{CS}({\cal A}(u))} } \,. \label{VCu}$$

![ a) The "longitude" $\lambda$ and "meridian" $\mu$ holonomy paths in the knot complement $S^3\backslash K$. b) Integration on the A-polynomial curve to find the deformed complex volume.](LM){#fig:lm width="6in"}

The quantity $I_{CS}({\cal A}(u))$ can be described very explicitly. Indeed, suppose that we require a hyperbolic metric (expressed in terms of a flat $SL(2,{\mathbb{C}})$ connection) to have holonomies conjugate to ${\rm diag}(e^u,e^{-u})$ and ${\rm diag}(e^v,e^{-v})$, respectively, along the meridian and longitude loops depicted in Figure [1](#fig:lm){reference-type="ref" reference="fig:lm"}a. Such a metric exists if and only if the so-called A-polynomial of $K$ vanishes [@cooper-1994],

$$A(\ell,m) = 0 \qquad\text{for}\qquad \ell=e^v\,,\quad m=e^u\,. \label{A}$$

Given a fixed $e^{u}\in{\mathbb{C}}^*$, exactly one of the solutions $v=v^{\rm hyp}(u)$ of this equation corresponds to the $u$-deformed hyperbolic metric. The Chern-Simons functional evaluated at the flat connection ${\cal A}(u)$ can then be written as

$$I_{CS}({\cal A}(u)) = I_{CS}({\cal A}(i\pi)) +4 \int_\gamma \theta\,, \label{CStheta}$$

where ${\cal A}(i\pi)$ is the non-deformed hyperbolic flat connection,

$$\theta = -(v'+i\pi)\,du'$$

is a one-form on the curve $A(e^{v'},e^{u'})=0$, and $\gamma$ is a path on this curve that connects the complete hyperbolic structure at $(e^{v'},e^{u'})=(-1,\pm1)$ to the $u$-deformed metric at $(e^{v'},e^{u'})=(e^{v^{\rm hyp}(u)},e^u)$, as in Figure [1](#fig:lm){reference-type="ref" reference="fig:lm"}b.

[^1]

As our recurrent example, consider again the figure-eight knot. The complete colored Jones polynomial, *cf.* [@Habiro-Jones], is

$$J_N(\mathbf{4_1};q) = \frac{q^{\frac N 2}-q^{-\frac N 2}}{q^\frac12-q^{-\frac12}}\sum_{j=0}^{N-1}q^{Nj}\prod_{k=1}^j(1-q^{k-N})(1-q^{-k-N})\,.$$

The A-polynomial of the figure-eight knot is

$$A(\ell,m) = (\ell-1)(m^4\ell^2-(1-m^2-2m^4-m^6+m^8)\ell+m^4\ell^2)\,,$$

and from [\[CStheta\]](#CStheta){reference-type="eqref" reference="CStheta"} and [\[vol41\]](#vol41){reference-type="eqref" reference="vol41"}, it results (after some algebra) that the Chern-Simons functional can be written as

$$I_{CS}({\cal A}(u)) = 2{\rm Li}_2(e^{-p-u})-2{\rm Li}_2(e^{p-u})+8(p-i\pi)(u-i\pi)\,,$$

where $x=e^p$ is the solution to $m^3x^2+(1-m^2-m^4)x+m^3=0$ with smallest negative imaginary part. For irrational $u/ i\pi$ in a neighborhood of $u=i\pi$ it can then be shown (*cf.* [@Mur-parametrized; @Mur-Yok]) that the proposed asymptotics [\[VCu\]](#VCu){reference-type="eqref" reference="VCu"} indeed hold.\
The necessity for taking $u/i\pi$ irrational here may appear a little strange at first glance. It stems fundamentally from the fact that the Jones polynomials $J_N(K;q=e^{\frac{2\pi i}{k}})$ are really only defined for $N,k\in {\mathbb{Z}}$. A subtle analytic continuation in either $N$ or $k$ is necessary to achieve $u/i\pi = N/k\notin {\mathbb{Q}}$. As anticipated in [@gukov-2003] and explained recently in [@Wit-anal], it is this continuation that causes the growth of the colored Jones polynomial to be exponential. We will remark on this further in Section [\[sec:path\]](#sec:path){reference-type="ref" reference="sec:path"}.

In light of this argument, one might ask now why the original volume conjecture at the rational value $k=N$ or $u=i\pi$ held in the first place. Recall that $J_N(K;q)$ actually vanished at $k=N$, so it was necessary to divide by $J_N({\,\raisebox{-.08cm}{\includegraphics[width=.4cm]{unknot}}\,};q)$ to obtain the non-vanishing ratio $V_N(K;q)$. Examining $V_N(K;q)$ at $u\to 0$ is equivalent to considering the *derivative* of $J_N(K;q)$ at $u=i\pi$, which of course knows about analytic continuation.[^2]

[^1]: The actual complexified volume that appears in the literature on hyperbolic geometry (*cf.* [@NZ; @yoshida-1985; @Hilden-1996]) is related to $I_{CS}({\cal A}(u))$ as

    $${\rm Vol}(S^3\backslash K;u)+i{\rm CS}(S^3\backslash K;u) = \frac{i}{2}I_{CS}({\cal A}(u)) + 2iv(u){\rm Re}(u)-2\pi u+2\pi^2 i\,.$$

    Note that $I_{CS}({\cal A}(u))$ is analytic in $u$, whereas ${\rm Vol}(u)+i{\rm CS}(u)$ is not.

[^2]: We thank E. Witten for useful observations on this subject.
