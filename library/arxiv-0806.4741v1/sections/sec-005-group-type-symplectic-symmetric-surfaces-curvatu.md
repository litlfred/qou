---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-005-group-type-symplectic-symmetric-surfaces-curvatu
section_title: "Group type symplectic symmetric surfaces, curvature contractions"
section_number: null
pages: 7-8
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.989
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
A symplectic symmetric space $(M,\omega,s)$ is said to be {\sl of group type} if there exists in its
automorphism group $G$ a Lie subgroup $\SS$ that acts on $M$ in a simply transitive manner i.e.
in a way that for all $x$ in $M$ there is one and only one element $g$ in $\SS$ with $x=go$. In that
case, one has a $\SS$-equivariant diffeomorphism:
\begin{equation}
\SS\to M:g\mapsto go\;.
\end{equation}
The symplectic structure $\omega$ on $M$ then pulls back to the group manifold $\SS$ as a left-invariant
symplectic structure $\omega^\SS$. Also, the symmetry at $o$ corresponds to a symplectic involution
\begin{equation}
\Psi^M:\SS\to\SS
\end{equation}
that encodes at the level of $\SS$ the  whole structure of symmetric space of $(M,s)$:
the symmetry at a point $g\in\SS$ is given by:
\begin{equation}
s^M_g(g')\;:=\;g.\Psi^M(g^{-1}.g')\;.
\end{equation}
A quick look at the above list in the 2-dimensional case leads us to the observation that

\vspace{2mm}

\noindent{\sl up to isomorphism, there are two and only two non-flat symplectic symmetric affine geometries
that are of group type: the hyperbolic plane $\DD$ and the Poincar\'e orbit $\MM$}.

\vspace{2mm}

\noindent The corresponding automorphism subgroups are in fact both isomorphic to the 2-dimensional affine group $\SS$
that we realize as $\SS:=\{(a,\ell)\}$ with the group law:
\begin{equation}\label{ANmult}
(a,\ell).(a',\ell')\;:=\;(\,a\,+\,a'\,,\,e^{-2a'}\ell\,+\,\ell'\,)\;.
\end{equation}
The unit element is then $e=(0,0)$ and the inverse map is given by $(a,\ell)^{-1}=(-a,-e^{2a}\ell)$.

\noindent Within this setting (see appendix \ref{AppenB}), the affine structures are encoded by the maps :
\begin{equation}\label{PSIM}
\Psi^\MM(a,\ell)\;:=\;(\,-a\,,\,-\ell\,)\;;
\end{equation}
and 
\begin{equation}\label{PSID}
\Psi^\DD(a,\ell)\;:=\;\left(\,-a-\frac{1}{2}\log(1+\ell^2)\,,\,-\ell\,\right)\;.
\end{equation}

\noindent Regarding the symplectic structures, one observes that the constant 2-form ${\rm d}a\wedge{\rm d}\ell$
is invariant under the left-action. Therefore, for every $k\in\R^+_0$, the symplectic structure
\begin{equation}
\omega^{(k)}\;:=\;\sqrt{k}\,{\rm d}a\wedge{\rm d}\ell
\end{equation}
induces the following symplectic symmetric surfaces: $(\SS,s^\DD,\omega^{(k)})$ and $(\SS, s^\MM,\omega^{(k)})$.
The first one is isomorphic to the hyperbolic plane $\DD$ with curvature $\frac{-1}{k}$. In the second one,
the parameter $k$ is indifferent in the sense that for all $k$, one has the isomorphism: $(\SS, s^\MM,\omega^{(k)})\simeq(\SS, s^\MM,\omega^{(1)})$.
