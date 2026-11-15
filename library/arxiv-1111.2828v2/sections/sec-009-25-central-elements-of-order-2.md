---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-009-25-central-elements-of-order-2
section_title: "Central elements of order 2"
section_number: 2.5
pages: 11-11
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 1.0
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.central}

For any simple complex Lie group $G$, there is a canonical homomorphism (defined up to conjugation) 
\begin{equation}
\phi_G\colon \SL(2,\C)\to G.
\end{equation}
The element $s_G=\phi_G(-I)$ is a central element of $G$ of order dividing $2$, and equals $(-I)^{n+1}$ if $G=\SL(n,\C)$ (see e.g.~Fock-Goncharov~\cite[Corollary~2.1]{FockGoncharov}). Let  
\begin{equation}
pG=G/\langle s_G\rangle.
\end{equation} 
Note that $\phi_G$ descends to a homomorphism $\PSL(2,\C)\to pG$. The following follows easily from the Serre spectral sequence.

\begin{proposition}
\lbl{orderfourkernel}
Suppose $s_G$ has order $2$. The canonical map $p^*\colon H^4(BpG;\Z)\to H^4(BG;\Z)$ is surjective with kernel of order dividing $4$.\qed
\end{proposition}

\begin{corollary}
There is a canonical characteristic class 
$\widehat c\colon H_3(pG)\to \C/\pi^2\Z$.
\end{corollary}

\begin{proof}
By Proposition~\ref{orderfourkernel}, there exists a canonical class $u\in
H^4(BpG;\pi^2\Z)$ such that $p^*(u)=W(P)\in H^4(BG\semico \pi^2\Z)$. Define $\widehat c=S_{P,u}$.
\end{proof}

In Section~\ref{sub.pSLassignments}, we construct a homomorphism 
\begin{equation}
\widehat c\colon H_3(p\SL(n,\C),N)\to \C/\pi^2\Z,
\end{equation}
which extends $\widehat c$ to a characteristic class of bundles with boundary-unipotent holonomy. The complex volume of a representation in $p\SL(n,\C)$ is defined as in Definition~\ref{complexvolumedefn}.
