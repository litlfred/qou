---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-004-23-stokes-constants-in-topological-string-theory
section_title: "Stokes constants in topological string theory"
section_number: 2.3
pages: 10-11
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
\label{sc:S-topo}

The Stokes constants defined above can be finite or infinite in number, depending on the cardinality of the set $\Omega$ which labels the basic trans-series of the model. 
They are, in general, complex numbers. In the case of asymptotic series associated to 
irregular singularities of non-linear ODEs, like the Painlev\'e equations, there is an infinite number of Stokes constants, and they are transcendental numbers. In many examples of linear ODEs, the Stokes constants are a finite set of integers. However, there is a third category of examples involving {\it infinitely many integer Stokes constants}. This is the case of ``peacock patterns," which was studied in detail in \cite{ggm1,ggm2} in the case of complex CS theory. We conjecture that peacock patterns are typical of theories based on quantum curves. 
This includes topological string theory on toric CY threefolds (as we discuss in this paper), (complex) CS theory, and the exact WKB method for generic difference equations. 

Let us now discuss in more detail how to apply the framework of the previous section to the 
perturbative series defined in (\ref{phiN}). We first recall that, as explained in (\ref{phiN}), for every set of integers $\bN$, 
topological string theory provides a {\it single} perturbative series $\Phi_{\bN}(g_s)$. It is easy to verify in examples that these series 
are Gevrey-1 and resurgent functions, and we conjecture that this is the case in general. 
We also expect that each of these series will be accompanied by 
additional series (or basic trans-series), leading to a minimal resurgent structure $\mathfrak{B}_{\Phi_{\bN}}$. This structure 
can be found by studying the singularities of their Borel transforms. 

This is indeed the case, and, as we will see in the examples discussed below, 
one finds a ``peacock pattern structure" very similar to the one described in \cite{ggm1, ggm2} in complex CS theory.  
More precisely, the minimal resurgent structure $\mathfrak{B}_{\Phi_{\bN}}$ consists of the following ingredients. There is a 
{\it finite} number of Gevrey-1 series 

\be
\label{bts}
\Phi_{\sigma ; \bN}(g_s), \qquad \sigma=0, 1, \cdots, \ell_{\bN}, 
\ee

where $ \Phi_{0,\bN} (g_s)= \Phi_{\bN} (g_s)$ is the original series (\ref{phiN}). The total number of these series, $\ell_{\bN}+1$, depends, as we 
have indicated, on $\bN$, and on the CY we are considering. In addition to this finite number of basic trans-series, we have an infinite family of them, labelled by an additional integer $n \in \IZ$, and of the form 

\be
\label{full-bts}
\Phi_{\sigma, n; \bN} (g_s)= \Phi_{\sigma ;\bN}(g_s) \re^{-n {\CA \over g_s}}, \qquad n \in \IZ, 
\ee

where $\CA$ is a complex constant which depends on $\bN$ and on the CY. Note in particular that the singularities of the Borel transforms $\widehat  \Phi_{\sigma ; \bN}(\zeta)$ form infinite towers in the Borel plane, spaced by integer multiples of $\CA$. The minimal resurgent structure is then of the form 

\be
\mathfrak{B}_{\Phi_{\bN}}=\{ \Phi_{\sigma, n; \bN} (g_s) \}_{\sigma=0, \cdots,  \ell_{\bN}; \, n \in \IZ}. 
\ee


Given the structure (\ref{full-bts}), the Stokes constants $\mS_{\sigma \sigma', n; \bN}$ are labelled by a pair of indices $\sigma, \sigma' =0, \cdots, \ell_{\bN}$ and an integer $n$, and we conjecture that they are {\it integers}, after a 
natural normalization of the fundamental series in (\ref{bts}). They can be naturally organized as $q$-series, 

\be
\mS_{\sigma \sigma'; \bN}(q)= \sum_{n \in \IZ} \mS_{\sigma \sigma', n; \bN} q^n. \label{eq:Sqn}
\ee


Let us note that the formal series (\ref{full-bts}) represent 
additional sectors of the topological string which are invisible in perturbation theory (in particular, they 
involve explicit non-perturbative corrections in the string coupling constant $g_s$). 
We believe that they are closely related to the trans-series constructed in \cite{cesv1,cesv2} by using the holomorphic anomaly. At this moment, 
however, the geometric and physical meaning of these sectors is not clear. 

The above procedure can be summarized as a ``resurgent machine" in which we start with perturbative series and we end up, conjecturally, with 
integer invariants organized in $q$ series. Schematically, 

\be
\text{perturbative series} \longrightarrow \text{integer invariants/$q$-series}. 
\ee

We should mention that this procedure to obtain integer invariants and $q$-series from perturbative series is 
different from the one suggested in \cite{lz,hikami1, hikami-dec, gpv, gmp, gppv,andersen}, in the context of 
Chern--Simons theory with a compact gauge group. In those papers, the perturbative series is 
upgraded to a $q$-series, in such a way that the former is recovered 
through the so-called radial asymptotics of the latter. In that upgrading, the $q$-series is not defined in a unique way 
from the perturbative series. In contrast, in the procedure described above, the perturbative series determines uniquely the different
$q$-series, since it determines uniquely the set of Stokes constants.
