---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-013-4-negative-dependence-theory-for-strongly-raylei
section_title: "Negative Dependence Theory for Strongly Rayleigh Measures"
section_number: 4
pages: 21-21
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s-stable}

The importance of strongly Rayleigh measures -- that is, measures with stable 
generating polynomials (cf.~Definition~\ref{def-rsm}) -- in negative 
dependence stems from the theorem below proved by one of the authors  
in \cite{PB} (cf.~\S \ref{ss-real-s}).  

\begin{theorem}\label{stable-Rayleigh}
Let $g \in \RR[z_1,\ldots, z_n]$ be a multi-affine polynomial. Then $g$ is 
stable if and only if 
$$
\frac {\partial g} {\partial z_i}(x) \frac {\partial g} {\partial z_j}(x) 
\geq \frac {\partial^2 g} {\partial z_i \partial z_j}(x) g(x)$$
for any $x=(x_1,\ldots,x_n)\in \RR^n$ and $i,j\in [n]$.
\end{theorem}

Hence, perhaps somewhat surprisingly, if the Rayleigh condition 
in Definition~\ref{d1} is enforced to hold for all real vectors then this 
stronger correlation condition is equivalent to real stability. 
Clearly, a strongly Rayleigh measure is automatically Rayleigh 
(cf.~Remark~\ref{r-term}). As we will see in this section, the 
geometric properties encoded in the concept of real stability allow us 
to show that strongly Rayleigh measures 
enjoy all virtues of negative dependence, including the strongest
form of negative association $\CNA+$.
