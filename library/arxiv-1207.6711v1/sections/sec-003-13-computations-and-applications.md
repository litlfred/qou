---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-003-13-computations-and-applications
section_title: "Computations and applications"
section_number: 1.3
pages: 5-5
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sub.computations}

The gluing equations of an ideal triangulation is a standard object of 
SnapPy~\cite{SnapPy}, which is used to study invariants of hyperbolic $3$-manifolds. From the gluing equations, one can compute the so-called
\emph{Neumann-Zagier datum} of an ideal triangulation, i.e.~a triple $((A|B),z,f)$ that consists of the matrices $(A|B)$ of
the gluing equations, a shape solution $z$, and a choice of flattening $f$.
There are three recent applications of the Neumann-Zagier datum in quantum topology:
the quantum Riemann surfaces of \cite{Di1}, the loop invariants of \cite{DG}
and the 3D index of \cite{DGG2} (see also \cite{Ga-3Dindex}). These 
applications are reviewed in Section \ref{sub.applicationsQT}, and lead
to exact computations.

Our generalized gluing equations for $\PGL(n,\BC)$ have
been coded into SnapPy by the second author and will be available
in the next release of SnapPy. As an application, we can define and efficiently
compute the $\PGL(n,\BC)$ Neumann-Zagier datum of an ideal triangulation.
Every function of the $\PGL(2,\BC)$ Neumann-Zagier datum can be evaluated
at the $\PGL(n,\BC)$ Neumann-Zagier datum. Sample computations of the one-loop invariant
of the $\PGL(n,\BC)$ Neumann-Zagier datum (the former being an element
of the invariant trace field) are given in Section 
\ref{sub.applicationsQT}. 

Even for $n=2$, our results provide new data. Preexisting software such as SnapPea~\cite{SnapPea}, Snap~\cite{snapprogram}, and SnapPy~\cite{SnapPy} all solve the gluing equations numerically (exact computations can then be guessed using the LLL algorithm), but only give the shapes for the geometric representation. For the Ptolemy varieties exact computations are possible for $n=2$ even when there are many simplices, and there are often several components of representations besides the geometric one. We should point out that while Gr\"obner basis computations are feasible for the Ptolemy varieties even for many simplices, they are usually impractical for the gluing equations even when the cusp equations are added. However, the monomial map $\mu$ can be used to obtain shapes from Ptolemy coordinates. All our tools will be available in the upcoming release of SnapPy.
