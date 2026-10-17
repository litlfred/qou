---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-009-23-the-case-of-the-figure-eight-knot-complement
section_title: "The case of the figure-eight knot complement"
section_number: 2.3
pages: 16-18
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.953
doc_brief: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement — We compute the real part of the semi-classical limit of the sequence of quantum hyperbolic invariants (QHI) of"
---
\label{4_1} Fix an orientation of $M=S^3\setminus 4_1$. Denote by $\lambda_{K}$ and $\mu_{K}$ the canonical longitude and the meridian of $K$, oriented so that the ordered pair $(\mu_K,\lambda_K)$ followed by the outward normal to $\partial \bar{M}$ defines a positive frame of $\bar{M}$. We denote also by $\lambda_K$, $\mu_K$ their classes in $H_1(\partial \bar M; \mz)$.

In this section we implement on $M$ the structures defined in Sections \ref{QGVsec} and \ref{sec:landbweights}. We will use the geometric, positive ideal triangulation $T$ of $M$ shown in Figure 1, with branching $b$ as indicated. The two tetrahedra $\Delta^0$, $\Delta^1$ have opposite $b$-orientations, and $\Delta^0$ is the positively $b$-oriented one; note that they were denoted $U$, $V$ in Section \ref{QHIintro2}.

Denote by $u:=(u_0,u_1,u_2)$ and $\bu:=(\bu_0,\bu_1,\bu_2)$ triples of classical and quantum shape parameters on $\Delta^0$, and by $(a_0,a_1,a_2)$ a triple of edge colors compatible with $\bu$. Denote similarly by $v:=(v_0,v_1,v_2)$, $\bv:=(\bv_0,\bv_1,\bv_2)$ and $(b_0,b_1,b_2)$ the corresponding data for $\Delta^1$. 

The Thurston gluing variety $G(T,b)$ is well-known, and can be described as follows. For the computation of the formulas \eqref{eqedgeu0v0} and \eqref{longmerformdec25} below, we refer to \cite[Section 15.1.4]{Martelli}, where we note that both tetrahedra are given positively oriented branchings, the classical shape parameters are ordered differently (the parameters $w$ and $z$ are $u_2$ and $1-v_2 = v_0^{-1}$ in our notations), and the curves $m$ and $l$ are $\mu_K$ and $\mu_K^{-2}\lambda_K$. Now, $G(T,b)$ can be identified with the irreducible curve in $\mc^2$ with coordinates $(u_0,v_0)$ and defining equation 
$$u_1u_2^2v_0^{-2}v_1^{-1}=1,$$
or equivalently
\begin{equation}\label{eqedgeu0v0}
u_0^2v_0^2=(1-u_0)(1-v_0).
\end{equation}
The point $w_{hyp}\in G(T,b)$ with coordinates $(u_0,v_0)=(e^{\pi i/3}, e^{-\pi i/3})$ realizes the complete structure on $M$, and any point $w\in G(T,b)$ sufficiently close to $w_{hyp}$ determines a (non-complete) hyperbolic structure on $M$ (see (ii) in Section \ref{sec:tri_GV}). 

For every point $w=(u,v)\in G(T,b)$ the dilation factor $\delta_{w}\in H^1(\partial \bar M; \mc^*)$ in \eqref{dilationdef} is given by  
\begin{equation}\label{longmerformdec25}
\delta_{w}(\lambda_K) = u_0^2u_2^{-2} = \frac{u_0^4}{(1-u_0)^2}\ ,\ \delta_{w}(\mu_K) = u_2v_2 = \frac{(u_0-1)(v_0-1)}{u_0v_0}.
\end{equation}

The quantum gluing variety $G_N(T,b)$ is the subspace of $\mc^6$ formed by the pairs $(\bu,\bv)$ of triples of quantum shape parameters $\bu:=(\bu_0,\bu_1,\bu_2)$ and  $\bv:=(\bv_0,\bv_1,\bv_2)$ satisfying the tetrahedral and edge relations
\begin{equation}\label{eqGN}
\begin{array}{ccc} \bu_0\bu_1\bu_2 =  e^{-\frac{\pi i}{N}} & ,& \bv_0\bv_1\bv_2 =  e^{+\frac{\pi i}{N}}\\
\bu_1\bu_2^2\bv_0^{-2}\bv_1^{-1} = e^{-\frac{2\pi i}{N}} & ,&  \bu_1\bu_0^2\bv_2^{-2}\bv_1^{-1}= e^{-\frac{2\pi i}{N}}.
\end{array}
\end{equation}
Using the tetrahedral relations it is easy to see that the two edge relations are equivalent. Thus we can identify $G_N(T,b)$ with the set of tuples $(\bu_0,\bu_1,\bv_0,\bv_1)$ satisfying $\bu_1\bu_0^2\bv_2^{-2}\bv_1^{-1}= e^{-\frac{2\pi i}{N}}$, for instance. Since $G(T,b)$ is an irreducible curve, we have
\begin{equation}\label{Ghypcas41mars25}
G_{hyp}(T,b)=G(T,b)\ {\rm and}\ G_{hyp,N}(T,b)=G_N(T,b).
\end{equation}

Given a point $\bw:=(\bu,\bv)\in G_N(T,b)$, let $w:=(u,v)\in G(T,b)$, and $d:=(a,b)$ be a system of edge colors such that $(w,d)$ is compatible with $\bw$; hence they are related by the formula \eqref{coldef}. Consider the log weight $l\kappa$ associated to $(w,d)$ by \eqref{formulelkappa}, and the boundary weight $\kappa:=\kappa_{\bw}$ associated to $\bw$ by \eqref{formulekappa}. Recall the bulk weight $h_2\in H^1(M; \mz/2)$ in \eqref{formulebulkw}, and the relation \eqref{kappaborddef}. As $M$ is a knot complement we have $h_2(\lambda_K)=0$. Therefore
\begin{equation}\label{compbord}
\kappa_\bw(\lambda_K) = \bu_0^{2}\bu_2^{-2}   = e^{\frac{l\kappa(\lambda_K)}{N}}\ ,\ \kappa_\bw(\mu_K) = \bu_2\bv_2  = (-1)^{h_2(\mu_K)} e^{\frac{l\kappa(\mu_K)}{N}}.
\end{equation}
For $k=0,1,2$, let us write $\bu_k$, $\bv_k$  as in \eqref{coldef}, in terms of edge colors and rescaled log-parameters $\bl_{k}^\bu:=N^{-1}(\Log(u_k)+\pi i a_k)$, $\bl_{k}^\bv:=N^{-1}(\Log(v_k)+\pi i b_k)$; so 
\begin{equation}\label{qshapeuvoct25}
\bu_{k} = \exp(\bl_{k}^\bu+\pi i a_k)\ ,\ \bv_{k} = \exp(\bl_{k}^\bv+ \pi i b_k).
\end{equation}
The relations \eqref{tetcol2}, \eqref{edgecol} and \eqref{formulelkappa} provide logarithms of \eqref{eqGN} and \eqref{compbord} of the form 
\begin{equation}\label{eqlog}
\left\lbrace\begin{array}{rcl}
\bl_{0}^\bu+\bl_{1}^\bu+\bl_{2}^\bu & = &\textstyle -\frac{\pi i}{N}+\pi i(a_0+a_1+a_2)\\
\bl_{0}^\bv+\bl_{1}^\bv+\bl_{2}^\bv & = & \textstyle +\frac{\pi i}{N}+\pi i(b_0+b_1+b_2)\\
\bl_{1}^\bu+2\bl_{2}^\bu-2\bl_{0}^\bv-\bl_{1}^\bv & = & \textstyle -\frac{2\pi i}{N}+\pi i(a_1+2a_2-2b_0-b_1)\\
2\bl_{0}^\bu-2\bl_{2}^\bu & = &\textstyle \frac{l\kappa(\lambda_K)}{N}+\pi i(2a_0-2a_2)\\
\bl_{2}^\bu+\bl_{2}^\bv & = & \textstyle \frac{l\kappa(\mu_K)}{N} +\pi i(a_2+b_2).
\end{array}\right.
\end{equation}
Note that $h_2(\mu_K) = a_2+b_2$ mod$(2)$ by \eqref{formulebulkw}; all other sums of edge colors on the right side of the system \eqref{eqlog} are even integers ({\it e.g.}, by \eqref{sumdeven}). 

The system \eqref{eqlog} may be rewritten in a very convenient form by fixing the point $w\in G(T,b)$, and working solely with edge colors. To see this, assume at first that $w=w_{hyp}$, so we have $(u_0,v_0)=(e^{\frac{\pi i}{3}}, e^{-\frac{\pi i}{3}})$. Then by \eqref{tetcol} and \eqref{edgecol} the tetrahedral and edge relations between edge colors are (they correspond to the first three relations in \eqref{eqlog}):
\begin{align}a_2=-2-a_0-a_1\ ,\ b_2=2-b_0-b_1\label{tetrel41}\\
a_1+2a_2-2b_0-b_1 = -4.\quad \quad \quad \label{edgerel41}
\end{align}
As $w_{hyp}$ realizes the complete hyperbolic structure, we have $\delta_{w_{hyp}}(\mu_K)=\delta_{w_{hyp}}(\lambda_K)=1$, and the identity $\kappa^N = \delta_{w_{hyp}}$ implies $l\kappa(\mu_K)\in \pi i \mz$ and $l\kappa(\lambda_K)\in 2\pi i \mz$. The relations \eqref{tetrel41}, \eqref{edgerel41} and the formula \eqref{formulelkappa} give:
\begin{equation}\label{standardf3} a_1=-2a_0+\frac{l\kappa(\lambda_K)}{2\pi i}-2\ ,\ b_0 = \frac{l\kappa(\mu_K)}{\pi i}-a_0\ ,\ b_1 = 2a_0-\frac{2l\kappa(\mu_K)}{\pi i}-\frac{l\kappa(\lambda_K)}{2\pi i}+2.
\end{equation}
Next consider the case when $w\in G(T,b)$, $w\ne w_{hyp}$. If the coordinates $u_0$, $v_0$ of $w$ satisfy $\mathfrak{I}(u_0)>0$ and $\mathfrak{I}(v_0)<0$, the relations \eqref{tetrel41} and \eqref{edgerel41} are unchanged, and those in \eqref{standardf3} still hold true if one replaces $l\kappa(\cdot)$ with $h_\rho(\cdot) =l\kappa(\cdot )-\Log(\delta_w(\cdot))$ (see \eqref{dconstraintclass}). For an arbitrary point $w\in G(T,b)$ the relations are obtained by doing the same replacement in \eqref{standardf3}, possibly adding even integers to the colors $a_k$, $b_k$ (depending on $w$).
