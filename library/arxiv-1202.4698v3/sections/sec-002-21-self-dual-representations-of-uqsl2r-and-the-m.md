---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-002-21-self-dual-representations-of-uqsl2r-and-the-m
section_title: "Self-dual representations of Uq(sl(2,R)) and the modular double"
section_number: 2.1
pages: 2-3
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.989
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
We will be considering the Hopf-algebra $\CU_q(\fsl(2,\BR))$
which has generators $E$, $F$ and $K$ subject to the usual 
relations. This algebra has a one-parameter
family of representations $\CP_{\al}$
\begin{equation}\label{Paldef}
\begin{aligned}
 \SE_\al
\equiv\pi_{\al}(E):=e^{+\pi b\sx}\frac{\cosh\pi b (\spp-s)}{\sin\pi b^2}
e^{+\pi b\sx}\,,\\
\SF_\al\equiv\pi_{\al}(F):=e^{-\pi b\sx}\frac{\cosh\pi b (\spp+s)}{\sin\pi b^2}
e^{-\pi b\sx}\,,
\end{aligned}
\qquad \SK_\al\equiv\pi_\al(K):=e^{-\pi b\spp}\,,
\end{equation}
where $\spp$ and $\sx$ are operators acting on functions $f(x)$ as
$\spp f(x)=(2\pi i)^{-1}\frac{\pa}{\pa x}f(x)$ and $\sx f(x)=xf(x)$,
respectively.
In the definitions \rf{Paldef} we are parameterizing $q$ as
$q=e^{\pi \textup{i} b^2}$, and write the parameter $\al$ as 
$\al=Q/2+\textup{i}s$. There is a maximal dense 
subspace $\CP_{\al}\subset L^2(\BR)$ on which all polynomials formed out of 
$\SE_\al$, $\SF_\al$ and $\SK_\al$ are well-defined 
\cite[Appendix B]{Bytsko:2006ut}.


These representations are distinguished by
a remarkable self-duality property: They are automatically 
representations of the quantum group 
$\CU_{\tilde{q}}(\fsl(2,\BR))$, where 
$\tilde{q}=e^{\pi \textup{i}/b^2}$ if $q=e^{\pi \textup{i} b^2}$. 
These representations are generated from operators 
$\tilde{\SE}_\al$, $\tilde{\SF}_\al$ and  $\tilde{\SK}_\al$ 
which are defined by formulae obtained from 
those in \rf{Paldef} by replacing $b\ra b^{-1}$.
The subspace $\CP_\al$ is simultaneously 
a maximal domain for the polynomial functions of 
$\tilde{\SE}_\al$, $\tilde{\SF}_\al$ and  $\tilde{\SK}_\al$ 
\cite[Appendix B]{Bytsko:2006ut}.

This phenomenon was observed independently in \cite{PT1} and in 
\cite{FMD}. 
It is closely related to the fact that  $\SE_\al$, $\SF_\al$ and $\SK_\al$
are  {\it positive} 
self-adjoint generators which allows one to construct
$\tilde{\SE}_\al$, $\tilde{\SF}_\al$ and  $\tilde{\SK}_\al$
as $\SE^{1/b^2}_\al$
$\SF^{1/b^2}_\al$, $\SK^{{1}/{b^2}}_\al$ \cite{BT1}. 

It was proposed in \cite{PT1,BT1} to construct a
noncompact quantum group which has as {\it complete} set 
of tempered representations the self-dual representations
$\CP_{\al}$. 
It's gradually becoming clear how to realize this suggestion
precisely. 
Relevant steps in this direction were taken in \cite{BT1} by 
defining co-product, R-operator and Haar-measure of such a 
quantum group. Further important progress in this direction was
recently made in \cite{Ip}. 
Following \cite{FMD}, we will in the following call 
this noncompact quantum 
group the modular double of $\CU_q(\fsl(2,\BR))$.
