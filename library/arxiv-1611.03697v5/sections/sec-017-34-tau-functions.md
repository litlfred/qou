---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-017-34-tau-functions
section_title: "Tau functions"
section_number: 3.4
pages: 12-13
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let us consider a variation of BPS structures $(\Gamma_p,Z_p,\Omega_p)$ over a complex manifold $M$. We call such a variation framed if the local system  $(\Gamma_p)_{p\in M}$ is trivial, so that we can  identify all  the lattices $\Gamma_p$  with a fixed lattice $\Gamma$. We can always reduce to this case by passing to a cover of $M$, or by restricting to a neighbourhood of a given point $p\in M$.

Associated to a framed variation $(\Gamma,Z_p,\Omega_p)$ there is a holomorphic map
\[\pi\colon M\to \Hom_\bZ(\Gamma,\bC)\isom \bC^n, \quad p\mapsto Z_p\]
which we call the period map.
We say that the variation is miniversal if the period map is  a local isomorphism. In that case, if we choose a basis $(\gamma_1,\cdots, \gamma_n)\subset \Gamma$, the functions $z_i=Z(\gamma_i)$ form a system of local co-ordinates in a neighbourhood of any given point of $M$.

Consider a framed, miniversal variation $(\Gamma_p,Z_p,\Omega_p)$ over a manifold $M$, and choose a basis $(\gamma_1,\cdots, \gamma_n)\subset \Gamma$ as above. For  each point $p\in M$ we can consider the Riemann-Hilbert problem associated to the BPS structure $(\Gamma,Z_p,\Omega_p)$. The wall-crossing formula,  Definition \ref{co} (d), makes it reasonable to ask for a family of solutions to these problems which is a piecewise holomorphic function of $p\in M$.
Such a family of solutions is given by a piecewise holomorphic map
\[\Psi\colon M\times \bC^*\to \bT_+,\]
 which we view as a  function of the co-ordinates  $(z_1,\cdots, z_n)\in \bC^n$ and the parameter $t\in \bC^*$.  We define a  $\tau$-function for the given family of solutions to be a piecewise holomorphic function \[\tau\colon M\times \bC^* \to \bC^*,\]
 which is invariant under simultaneous  rescaling of all co-ordinates $z_i$ and the parameter $t$, and which satisfies  the equations
 \begin{equation}
\label{hungry}\frac{1}{2\pi i}\cdot \frac{\partial \log \Psi_{\gamma_j}}{\partial t}=\sum_i \epsilon_{ij}  \frac{\partial \log \tau}{\partial z_i}, \end{equation}
where $\epsilon_{ij}=\<\gamma_i,\gamma_j\> $.
When the form $\<-,-\>$ is non-degenerate these conditions uniquely determine $\tau$ up to multiplication by a constant scalar factor.

It is not clear at present why a $\tau$-function should exist in general, and the above definition should be thought of as being somewhat experimental. Nonetheless, in the uncoupled case we will see that $\tau$-functions do exist, and are closely related to various partition functions arising in quantum field theory. We hope to return to the general case in future publications.
