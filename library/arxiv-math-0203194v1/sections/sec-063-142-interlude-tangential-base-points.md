---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-063-142-interlude-tangential-base-points
section_title: "Interlude: tangential base-points."
section_number: 14.2
pages: 137-139
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.969
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::2.2}

\begin{para}\label{para::2.2.1} Instead of basing fundamental groups at
 geometric points, it is sometimes more convenient\footnote{for instance
 in the study of Galois actions on fundamental groups.} to base them at 
 tangent vectors at points at infinity. 

 P. Deligne has explained the construction for affine algebraic curves in 
 characteristic zero, for topological, algebraic (= profinite) and other
 kinds of fundamental groups \cite{lgfdldpmtp}. In the profinite case, these
 tangential base-points amount to genuine geometric generic points,
 corresponding to embeddings of the function field of the curve into the
 field of Puiseux series at the chosen point at infinity (with respect
 to a fixed local parameter $z$ at that point; however, the embedding
 depends only on the tangent vector $\partial/\partial z$).

 If we try to imitate the construction in our non-archimedean setting, we
 face at once the following difficulty: let us assume for simplicity
 that the curve is the affine line; since there is no way to extend the
 Gauss norm on $K(z)$ to the field of Puiseux series with arbitrary coefficients in $K$, one does not get geometric (generic) points in the sense of \ref{para::1.2.2}.  We
 do not know how to overcome this difficulty for (analytic) \'etale coverings in
 general (and we doubt that this is possible). For temperate \'etale
 coverings, however, we can circumvent the difficulty as follows.
\end{para}

\begin{para}\label{para::2.2.2} We assume that $K$ is algebraically
 closed of characteristic $0$. Let $\ovl{S}$ be a $K$-manifold of
 dimension one, and let $S$ be the complement of a {\it classical} point
 $0$ in $\ovl{S}$ (so that $0$ has a basis of open neighborhoods
 consisting in disks centered at $0$). As above, it follows from
 \ref{lem::2.1.11} 
 that {\it the restriction of any temperate covering of $S$ to a
 punctured disk around $0$ of sufficiently small radius splits into a
 disjoint union of Kummer coverings of bounded degree}. If we replace
 $\ovl{S}$ by the its tangent space at $0$ and $0$ by the zero tangent
 vector, the same construction yields an equivalence of categories, with
 an obvious inverse given by `extension'. We thus get a {\it
 specialization functor}:
 \begin{equation*}
 \Cov^{\mathrm{temp}}_S\to  \Cov^{\mathrm{temp}}_{T_{\ovl{S},0}^0}.
 \end{equation*}         
 Any geometric point $\vec t$ of $T_{\ovl{S},0}^0$, 
 \eg any non-zero tangent vector at $0$, then gives rise by composition
 to a fiber functor 
 \begin{equation*}
  F^{\mathrm{temp}}_{\vec t}\;:\; \Cov^{\mathrm{temp}}_S\to  \Sets.
 \end{equation*}         
\end{para}

\begin{pro}\label{pro::2.2.3} This fiber functor is isomorphic to
 $F^{\mathrm{temp}}_{\ovl{t}}$ for any geometric point $\ovl{t}$.
\end{pro}
\begin{proof}
 We follow the line of proof of \ref{lem::1.3.3}. We may assume that
 $\ovl{S}$ is affinoid (hence compact). Let us consider finite open covers
 $\ovl{\mathcal{U}}=(\ovl{U}_i)_{i\geq 1}$ of $S$ {\it such that
 $\ovl{U}_1$ is a disk centered at $0$ and $\;0 \notin \ovl{U}_i\;$ 
 for $\;i>1$.}

 Let us denote by $ \mathcal{U}=(U_i)$ its trace on $S$, and by
 $\Cov^{\mathrm{temp}}_{S,\mathcal{U}}$ the full subcategory of 
 $\Cov^{\mathrm{temp}}_{S}$ of temperate coverings $f:S'\to S$ such that
 $f^{-1}U_i= \coprod V_{ij}$ and $V_{ij}$ is \'etale finite over 
 $U_i$ via $f$. 
 
 The point is that {\it by \ref{thm::2.1.10} (or \ref{para::2.2.2})}, we
 have
 $\displaystyle
 \Cov^{\mathrm{temp}}_{S}=\underset{\mathcal{U}}{\liminj} 
 \Cov^{\mathrm{temp}}_{S,\mathcal{U}}, $ where $\mathcal{U}$ runs among
 the open covers of $S$ satisfying the above properties. Also
 \begin{equation*}
  \Isom(F^{\mathrm{temp}}_{\vec t}, F^{\mathrm{temp}}_{\ovl{t}})
   =\underset{\mathcal{U}}{\limproj} \Isom(F^{\mathrm{temp}}_{\vec
   t,\mathcal{U}}, F^{\mathrm{temp}}_{\ovl{t},\mathcal{U}})
 \end{equation*}
 where $F^{\mathrm{temp}}_{\vec t,\mathcal{U}},
 F^{\mathrm{temp}}_{\ovl{t},\mathcal{U}}$ denote the restrictions of 
 $F^{\mathrm{temp}}_{\vec t }, F^{\mathrm{temp}}_{\ovl{t} }$ to
 $\Cov^{\mathrm{temp}}_{S,\mathcal{U}}$.

 To show that $\Isom(F^{\mathrm{temp}}_{\vec t},
 F^{\mathrm{temp}}_{\ovl{t}}) \neq \emptyset$, we construct 
 non-empty compact subsets $K_\mathcal{U}$ of
 $\Isom(F^{\mathrm{temp}}_{\vec t,\mathcal{U}},
 F^{\mathrm{temp}}_{\ovl{t},\mathcal{U}})$ (topologized 
 as before) such that if $\mathcal{U}'$ refines $\mathcal{U}$,
 $K_{\mathcal{U}'}$ maps to $K_\mathcal{U} $ under the natural map 
 $\Isom(F^{\mathrm{temp}}_{\vec t,\mathcal{U}'},
 F^{\mathrm{temp}}_{\ovl{t},\mathcal{U}'})\to
 \Isom(F^{\mathrm{temp}}_{\vec t,\mathcal{U}},
 F^{\mathrm{temp}}_{\ovl{t},\mathcal{U}})$; it will follow that
 $\Isom(F^{\mathrm{temp}}_{\vec t}, F^{\mathrm{temp}}_{\ovl{t}}) \supset
 \limproj_{\mathcal{U}}\, K_\mathcal{U}\neq 
 \emptyset$. 

 In fact, it suffices to do so for a cofinal system of
 $\mathcal{U}$'s. We now use a continuous embedding 
 $I=[0,1]\hookrightarrow \ovl{S}$ with $0\mapsto 0\in \ovl{S},\;1\mapsto t$. We
 consider open covers $\mathcal{U}  =(U_1,\ldots, U_n)$ as above, and
 such that
 \begin{equation*}
  U_1\cap I = 0,r_1[,\;\ldots, U_i\cap I=]r_i,t_i[,\;\ldots, U_m\cap
   I=]r_m,1],\;U_{m+1}\cap I=\emptyset,\ldots
 \end{equation*}
 for some points $r_i<t_{i-1}<r_{i+1}<t_i$ in $I \;(i=2,\ldots, m-1)$ and
 some $ m\leq n$.
 
 Given $\mathcal{U}$, one chooses $s_i$ in $U_i\cap U_{i+1}\cap I$ (which
 amounts to a real number between $r_{i+1}$ 
 and $t_i$), and a geometric point $\ovl{s}_i$ above $s_i\; (i=1,\ldots,
 m-1)$; one completes this collection by setting 
 $\ovl{s}_0=\vec t,\; \ovl{s}_m=\ovl{t}$. 

 Let us look at the diagram 
 \begin{equation*}
  \Cov^{\mathrm{temp}}_{S,\mathcal{U}}
   \xrightarrow{\sigma_i}
   \Ind\Cov^{\mathrm{alg}}_{\mathcal{U}_{i+1}}
   \begin{array}{c}
    \xrightarrow{F^{\mathrm{alg}}_{\ovl{s}_i, U_{i+1}}}\\
    \xrightarrow{F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}}}\\
   \end{array}
   \longrightarrow \Sets.
 \end{equation*}               
 One has $F^{\mathrm{alg}}_{\ovl{s}_j, U_{i+1}}\circ \sigma_i =
 F^{\mathrm{temp}}_{\ovl{s}_i, \mathcal{U} },\;\;j=i,i+1$, whence
 continuous maps 
 \begin{equation*}
  \Isom(F^{\mathrm{alg}}_{\ovl{s}_i,
   U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, 
   U_{i+1}})\to \Isom(F^{\mathrm{temp}}_{\ovl{s}_i,
   \mathcal{U}},F^{\mathrm{temp}}_{\ovl{s}_{i+1}, \mathcal{U}}).
 \end{equation*} 
 But $\Isom(F^{\mathrm{alg}}_{\ovl{s}_i,
 U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}})$ is a non-empty
 compact set for any $i=0,\ldots, m$: for $i=0\;$ ($s_0=\vec t$), one
 uses the analogue of \ref{pro::2.2.3} for the category of finite \'etale
 coverings, which follows from Deligne's discussion, {\it loc.~cit} (or
 even directly from \cite[V]{sga1}, interpreting
 $F^{\mathrm{alg}}_{\vec t, U_{i+1}}$ as a fiber functor at a geometric
 generic point). The rest of the proof goes exactly as in \ref{lem::1.3.3}.
\end{proof}

\begin{para}\label{para::2.2.4} This proposition allows to construct
 fundamental groups $\pi_1^\bullet(S,\,\vec t\,)$ based at a tangential
base-point $\vec t\,$ for any full subcategory $\Cov^\bullet_S\to
\Cov^{\mathrm{temp}}_S$ stable under taking connected components, fiber
products and quotients.  The theory of 1.4 extends without change to this
variant, as far as one restricts to curves over an algebraically closed
field of characteristic zero. For $\;\Cov^{\mathrm{top}}_S\to
\Cov^{\mathrm{temp}}_S$, the interpretation of tangential base-points is
not as transparent as in the complex-analytic context.
\end{para}
