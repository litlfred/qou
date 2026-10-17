---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-008-31-volumes-of-non-ideal-tetrahedra
section_title: "Volumes of non-ideal tetrahedra"
section_number: 3.1
pages: 8-9
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.861
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
We are considering non-ideal tetrahedra which are
completely defined by the collection of six dihedral 
angles $\eta_1,\dots,\eta_6$. In order to formulate the
formula for their volumes from \cite{M}, let us
use the notation $A_k=e^{\textup{i}\eta_k}$, and define
\begin{align} \label{Udef}
 U({u},\underline{{A}}) = & 
\Li_2({u}) +  \Li_2({A}_{st13} {u}) + \
\Li_2({A}_{st24} {u}) + \Li_2({A}_{1234} {u}) \\ & 
 - \Li_2(-{A}_{12s}{u}) - \Li_2(-{A}_{s34} {u}) - 
\Li_2(-{A}_{4t1} {u}) - \Li_2(-{A}_{32t} {u})\,,
\nonumber\end{align}
where $A_{ijk}:=A_iA_jA_k$, $A_{ijkl}:=A_iA_jA_kA_l$, along with
\begin{align}\label{Deltadef}
 \Delta(\underline{{A}}) &= \log {A}_s {A}_t + \log {A}_2 {A}_4 + \log {A}_1 {A}_3  \\ & \quad + \tilde{\Delta}({A}_s,{A}_1,{A}_2) + \tilde{\Delta}({A}_s,{A}_3,{A}_3) + \tilde{\Delta}({A}_t,{A}_1,{A}_4) + \tilde{\Delta}({A}_t,{A}_2,{A}_3)\,, 
\notag\end{align}
where
\begin{align}
 \tilde{\Delta}({A}_1,{A}_2,{A}_3) = -\frac12 \big( & \Li_2(-{A}_1{A}_2{A}_3^{-1}) + \Li_2(-{A}_1{A}_2^{-1}{A}_3) + \Li_2(-{A}_1^{-1}{A}_2{A}_3) \nonumber \\ & + \Li_2(-{A}_1^{-1}{A}_2^{-1}{A}_3^{-1}) + \log^2 {A}_1 + \log^2 {A}_2 + \log^2 {A}_3 \big).
\notag\end{align}
The following formula was found in 
\cite[Theorem 2]{M} 
\beq \label{volume}
{\rm Vol}(\underline{{A}}) = \frac 12 \,{\rm Im}\big[ 
U(u_+,\underline{{A}})+ \Delta(\underline{{A}})\big] 
= - \frac 12  \,{\rm Im}\big[U(u_-,\underline{{A}})+ 
\Delta(\underline{{A}})\big]\,,
\eeq
where $u_\pm$ are the two roots of the equation
\beq \label{eq}
\frac{dU(u,\underline{{A}})}{du} \ = \ - \frac{2 \pi \textup{i}}{u}\,.
\eeq
It can be shown \cite{M} that equation (\ref{eq}) is a 
quadratic equation which has two 
solutions $u_\pm$ which are 
pure phase, $|u_{\pm}| =  1$.
