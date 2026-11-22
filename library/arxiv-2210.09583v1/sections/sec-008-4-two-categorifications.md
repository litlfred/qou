---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-008-4-two-categorifications
section_title: "Two Categorifications"
section_number: 4
pages: 12-13
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.962
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
\label{section:cat}
As we know from \cite{C,Blu09}, the $\mf{osp}(1|2)$ polynomial (and hence our invariant $\hat{J}$) is practically identical to the Jones polynomial.
Now that we have this Kauffman-bracket type definition of $\hat{J}$, it should not come as much of a surprise that one can categorify this invariant using a homology theory that is practically identical to Khovanov homology.
Indeed, we show in this section that one can repeat the construction of Khovanov homology seen in \cite{BN2} but where an extra $\Z_4$-grading is attached to everything to get a categorification.
We then construct a $\Z\times \Z_4$-graded version of Putyra's covering Khovanov homology \cite{P} in a similar fashion.



\begin{notation}
  An "e-graded" object refers to an object with a $\Z\times \Z_4$-grading.
\end{notation}
For example, an e-graded vector space is a $\Z\times \Z_4$-graded vector space.
\begin{definition}
  Let $\cat{egVec}$ be subcategory of $\cat{Vect}$ consisting of $\Z\times \Z_4$-graded vector spaces and degree-preserving linear maps.
\end{definition}
This is a symmetric monoidal category with the same braiding as $\cat{Vect}$.
The tensor product of linear maps is given by $(f\otimes g)(v\otimes w)=f(v)\otimes g(w)$.
We bring this example up to emphasize that the $\Z_4$-grading doesn't impact the tensor product of linear maps or the braiding like the $\Z_2$-grading does for superspaces.
For the remainder of the paper, we choose to work with modules instead of vector spaces.


An e-graded module $M$ over a e-graded ring $R$ is a $\Z\times \Z_4$-graded $R$-module such that $R_{(a,b)}M_{(x,y)}\subset M_{(x+a,y+b)}$.
We refer to the degree of a homogeneous element in some e-graded module with $deg(-)$ for the rest of the paper.

\begin{definition}
  The category of e-graded $R$-modules $\cat{R-emod}$ is the subcategory of $\cat{R-mod}$ whose objects are e-graded $R$-modules and whose morphisms are degree preserving $R$-module homomorphisms.
\end{definition}

For our discussion on Khovanov homology, we set $R=\Z$ (concentrated in degree $(0,0)$).

\begin{definition}
  Let $W=\bigoplus\limits_{(m,n)\in \Z \times \Z_4} W_{m,n}$ be a e-graded $R$-module with homogeneous components $W_{m,n}$. The graded dimension of $W$ is the power series $\text{dim}_{q,\tau}(W)=\sum_{m,n}q^m\tau^n \text{dim}(W_{m,n})$. When $W$ is finite dimensional, this lies in $\Z^\tau[q,q^{-1}]$.
\end{definition}
\begin{definition}
  Let $W= \bigoplus W_{m,n}$ as before. Then define $\{(a,b)\}$ to be the degree shift. That is, we set $W\{(a,b)\}_{(m,n)}=W_{(m-a,n-b)}$ so that $\text{dim}_{q,\tau}W\{(a,b)\}=q^{a}\tau^b \text{dim}_{q,\tau} W$.
\end{definition}


Let $\cat{2Cob}$ denote the category of 2D-cobordisms $Cob^3(\emptyset)$ from \cite{BN2}.
The objects are closed 1-dimensional manifolds (collections of circles), and the morphisms are given by 2-dimensional cobordisms between these collections of circles up to boundary preserving isotopies.
We also use the grading conventions in \cite[Section 6]{BN2}, which tell us that the degree of a cobordism $W: \Sigma_1\{m\}\to \Sigma_2\{n\}$ is given by $\chi(W)+n-m$.
We will later attach an additional $\Z_4$-grading to this category.
