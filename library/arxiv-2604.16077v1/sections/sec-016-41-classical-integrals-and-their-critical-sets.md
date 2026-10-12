---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-016-41-classical-integrals-and-their-critical-sets
section_title: "Classical integrals and their critical sets"
section_number: 4.1
pages: 35-37
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.934
---
\label{sec:class_int} Recall the contour $C_N$ from  \eqref{choiceCN}. By the assumption \eqref{situation2}, when $z\in C_N$ both cases $0< \mathfrak{I}(\bl_{0,\infty}+z) < 2\pi$ and $-2\pi < \mathfrak{I}(\bl_{0,\infty}+z) < 0$ may happen. If $0< \mathfrak{I}(\bl_{0,\infty}+z) < 2\pi$, then $\hat S_N(\bl_{0,\infty}+z)$ is given by the formulas \eqref{intrepS}-\eqref{defShat}, and Lemma \ref{estimatehatS} yields
\begin{equation}\label{equiv1}
\hat S_N(\bl_{0,\infty} + z)= e^{\frac{N}{2i\pi} {\rm Li}_2(e^{\bl_{0,\infty} + z})}\mathcal{O}_{N\ra \infty}(1).
\end{equation}
If $-2\pi < \mathfrak{I}(\bl_{0,\infty}+z) < 0$, we get $\hat S_N(\bl_{0,\infty}+z) = (1-e^{N(\bl_{0,\infty}+z)})\hat S_N(\bl_{0,\infty}+z+2\pi i)$ by using $N$ times the functional equation \eqref{eqfunchatS}; so in this case we have 
\begin{equation}\label{equiv2}
\hat S_N(\bl_{0,\infty} + z)= \left\lbrace \begin{array}{rl} e^{N\bl_{0,\infty}}e^{\frac{N}{2i\pi} ({\rm Li}_2(e^{\bl_{0,\infty} + z})+2i\pi z)}\mathcal{O}_{N\ra \infty}(1) & {\rm if}\ \mathfrak{R}(\bl_{0,\infty} + z)>0\\ e^{\frac{N}{2i\pi} {\rm Li}_2(e^{\bl_{0,\infty} + z})}\mathcal{O}_{N\ra \infty}(1) & {\rm if}\ \mathfrak{R}(\bl_{0,\infty} + z)<0. \end{array}\right.
\end{equation}
It is easily checked that $\textstyle \coth(\frac{Nz}{2})$ is bounded on $C_N$, and therefore the integrand on the RHS of \eqref{int1} satisfies, for $z\in C_N$: 
\begin{multline}\label{equiv3mars26}
e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2}) =\\ \left\lbrace \begin{array}{rl} e^{N\bl_{0,\infty}}e^{\frac{N}{2i\pi} \mathcal{L}_+(z;\bl_{0,\infty},\bl_{1,\infty})}\mathcal{O}_{N\ra \infty}(1) & {\rm if}\ \mathfrak{R}(\bl_{0,\infty} + z)>0 \ {\rm and}\\
& -2\pi < \mathfrak{I}(\bl_{0,\infty}+z) < 0,\\ e^{\frac{N}{2i\pi} \mathcal{L}_-(z;\bl_{0,\infty},\bl_{1,\infty})}\mathcal{O}_{N\ra \infty}(1) & {\rm otherwise}, \end{array}\right. 
\end{multline}
where 
\begin{equation}\label{defL+-}
\left\lbrace\begin{array}{ll}
\mathcal{L}_-(z;\bl_{0,\infty},\bl_{1,\infty}) := {\rm Li}_2(e^{\bl_{0,\infty} + z})+z^2- \bl_{1,\infty} z,& \\
\mathcal{L}_+(z;\bl_{0,\infty},\bl_{1,\infty}) := {\rm Li}_2(e^{\bl_{0,\infty} + z})+z^2 -(\bl_{1,\infty}-2i\pi) z. &
\end{array}\right.
\end{equation}
Note that the two halves of $C_N$, in the left and right half spaces of $\mc$, are homotopic to $i[s_N^-,2\pi-s_N^+]$ (with opposite orientations) relatively to their endpoints. We call 
\begin{equation}
I_{\pm,N}(\bl_{0,\infty},\bl_{1,\infty}) = \int_{i[s_N^-,2\pi-s_N^+]} e^{\frac{N}{2i\pi}\mathcal{L}_\pm(z;\bl_{0,\infty},\bl_{1,\infty})}dz\label{I+}
\end{equation}
the {\it classical integrals}.\\
Because of \eqref{equiv3mars26}, it is reasonable to expect that the asymptotics of the integrals $I_{\pm,N}(\bl_{0,\infty},\bl_{1,\infty})$ have a lot to do with those of the integral on the RHS of \eqref{int1} (see Lemma \ref{qcintjui25} for a rigourous statement). Then, in view of the saddle point method (see Section \ref{sub:SPM:PV}), we are naturally let to consider the critical sets of the functions $z\mapsto \mathcal{L}_\pm(z;\bl_{0,\infty}^\bx,\bl_{1,\infty}^\bx)$, where the parameters $\bl_{0,\infty}^\bx$, $\bl_{1,\infty}^\bx$, with $\bx=\bu$ and $\bv$, are associated to the tetrehedra $\Delta^0$ and $\Delta^1$, as usual. In particular, by Lemma \ref{lemYo} it is interesting to consider the situations where $(e^{\bl_{0,\infty}^{\bu}},e^{\bl_{1,\infty}^{\bu}},e^{\bl_{0,\infty}^{\bv}},e^{\bl_{1,\infty}^{\bv}}) \in \{0\}\times \mathcal{A}(T,b)\subset\mathcal{C}(T,b)\times \mathcal{A}(T,b)$. By \eqref{eqloginfinity} and \eqref{asycurvemu}, such a tuple $(\bl_{0,\infty}^{\bu}, \bl_{1,\infty}^{\bu},\bl_{0,\infty}^{\bv}, \bl_{1,\infty}^{\bv})$ satisfies the sole relation
\begin{equation}\label{asycurvelog}
\bl_{1,\infty}^{\bu}+2\bl_{2,\infty}^{\bu}-2\bl_{0,\infty}^{\bv}-\bl_{1,\infty}^{\bv} = 0 \quad {\rm mod}(2\pi i),
\end{equation}
and it determines an asymptotic angular holonomy by the system 
\begin{equation}\label{asycurvelog2}
\left\lbrace\begin{array}{ll} 
\bl_{0,\infty}^{\bu}+\bl_{1,\infty}^{\bu}+\bl_{0,\infty}^{\bv}+\bl_{1,\infty}^{\bv}  & = - i\arg(\kappa^\infty(\mu_K))  \quad {\rm mod}(2\pi i)\\
4\bl_{0,\infty}^{\bu}+2\bl_{1,\infty}^{\bu}  & = i\arg(\kappa^\infty(\lambda_K)) \quad {\rm mod}(2\pi i).\end{array}\right.
\end{equation} 
Denote by $\mathcal{A}'(T,b)$ the set of solutions of the equation \eqref{asycurvelog}. Let us define a sign
\begin{equation}\label{signcriteqhol}
\star:=\left\lbrace\begin{array}{ll} +1 & {\rm if} \ \ \textstyle 2\bl_{0}^{\bu,\infty}+\bl_{1}^{\bu,\infty} = \frac{i\arg(\kappa^\infty(\lambda_K))}{2}\quad  {\rm mod}(2\pi i)\\ -1 & {\rm  if} \ \ \textstyle 2\bl_{0}^{\bu,\infty}+\bl_{1}^{\bu,\infty}  = \frac{i\arg(\kappa^\infty(\lambda_K))}{2} +\pi i\quad {\rm mod}(2\pi i).\end{array}\right.
\end{equation}
\begin{lem}\label{lemcritpts} The function $\mathcal{L}_\pm(\cdot ;\bl_{0,\infty},\bl_{1,\infty})$ has a unique critical point $z_0:=z_0^\pm(\bl_{0,\infty},\bl_{1,\infty})$, and this point satisfies the equation:
\begin{equation}\label{criteqhol}
\star e^{-\frac{i\arg(\kappa^\infty(\lambda_K))}{2}}e^{2(\bl_{0,\infty}+z_0)} +e^{\bl_{0,\infty}+z_0}-1=0.
\end{equation}
Moreover, the image of the map 
$$\fonc{\Xi}{\mathcal{A}'(T,b)}{\mc^2}{(\bl_{0,\infty}^{\bu}, \bl_{1,\infty}^{\bu},\bl_{0,\infty}^{\bv}, \bl_{1,\infty}^{\bv})}{\left(e^{\bl_{0,\infty}^{\bu}+z_0^-(\bl_{0,\infty}^{\bu}, \bl_{1,\infty}^{\bu})},e^{\bl_{0,\infty}^{\bv}+z_0^+(\bl_{0,\infty}^{\bv}, \bl_{1,\infty}^{\bv})}\right)}$$
is contained in $G(T,b)$ and covers a neighborhood of $w_{hyp}$, the geometric solution to the gluing equations.
\end{lem}
\proof We have
\begin{equation}\label{crit1} 
\begin{array}{l}
(\partial_z\mathcal{L}_-)(z_0;\bl_{0,\infty},\bl_{1,\infty}) =0\Longleftrightarrow 2z_0-\Log(1-e^{\bl_{0,\infty}+z_0})- \bl_{1,\infty}=0 ,\\
(\partial_z\mathcal{L}_+)(z_0;\bl_{0,\infty},\bl_{1,\infty}) =0\Longleftrightarrow 2z_0-\Log(1-e^{\bl_{0,\infty}+z_0})+2i\pi-\bl_{1,\infty}=0 .
\end{array}
\end{equation}
Passing to the exponential, both equations yield the following degree two equation in $e^{z_0}$:
\begin{equation}\label{criteq}
e^{-\bl_{1,\infty}}e^{2z_0} +e^{\bl_{0,\infty}}e^{z_0}-1=0.
\end{equation}
The two roots have product $-e^{\bl_{1,\infty}}$, hence their arguments sum to $\mathfrak{I}(\bl_{1,\infty})+\pi$ mod$(2\pi)$. On the other hand, the first equation of \eqref{crit1} imposes $2\mathfrak{I}(z_0)\in ]-\pi+\mathfrak{I}(\bl_{1,\infty});\pi+\mathfrak{I}(\bl_{1,\infty})]$, and the second imposes $2\mathfrak{I}(z_0)\in ]-3\pi+\mathfrak{I}(\bl_{1,\infty});-\pi+\mathfrak{I}(\bl_{1,\infty})]$. Combining the two facts, we see that $\mathcal{L}_+(z;\bl_{0,\infty},\bl_{1,\infty})$ and $\mathcal{L}_-(z;\bl_{0,\infty},\bl_{1,\infty})$ have exactly one critical point for every fixed values of $\bl_{0,\infty}$ and $\bl_{1,\infty}$. The identity \eqref{criteqhol} follows immediately from \eqref{criteq} and the second relation in \eqref{asycurvelog2}. This proves the first claim. \\
From \eqref{criteq} we get
\begin{equation}\label{criteq2oct24}
e^{-\bl_{1,\infty}-2\bl_{0,\infty}} = e^{-2(z_0+\bl_{0,\infty})}(1-e^{z_0+\bl_{0,\infty}}).
\end{equation}
It is also an immediate check that this identity and the first of \eqref{asycurvelog} imply that $(u_0,v_0):=(e^{\bl_0^{\bu,\infty}+z_0^\pm(\bl_0^{\bu,\infty}, \bl_1^{\bu,\infty})},e^{\bl_0^{\bv,\infty}+z_0^\pm(\bl_0^{\bv,\infty}, \bl_1^{\bv,\infty})})$ is a solution of the defining equation \eqref{eqedgeu0v0} of $G(T,b)$. This proves the second claim.
 
 Finally note that $\Xi(-2\pi i, \pi i,2\pi i, -\pi i) = (e^{\pi i/3}, e^{- \pi i/3})$. A straightforward computation shows that the Jacobian of $\Xi$ at $(-2\pi i, \pi i,2\pi i, -\pi i)$ has real rank $2$. Since $G(T,b)$ is a curve and $(e^{\pi i/3}, e^{- \pi i/3})$ is a smooth point, this shows that $\Xi$ is a submersion, and the last claim follows.\cvd
\medskip

We note the following simple caracterization of critical points $z_0$ which are saddle points of order $1$:
$$\partial_z^2\mathcal{L}_\pm(z_0;\bl_{0,\infty},\bl_{1,\infty}) = 1+(1-e^{{\rm l}_0 +z_0})^{-1} \ne 0.$$
