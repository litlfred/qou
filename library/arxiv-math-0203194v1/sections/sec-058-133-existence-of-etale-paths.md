---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-058-133-existence-of-etale-paths
section_title: "Existence of 'etale paths."
section_number: 13.3
pages: 121-123
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.931
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::1.3}  
 
\begin{para}\label{para::1.3.1} Let us fix a geometric point $\ovl{s}$ of
 $S$. We consider the fiber functor 
 \begin{equation*}
  F^{\mathrm{et}}_{S,\ovl{s}}=F^{\mathrm{et}}_{\ovl{s}} :
   \Cov^{\mathrm{et}}_S \longrightarrow \Sets,\;\; S' \mapsto
   \{\text{geometric points $\ovl{s}'$ of $S'$ above $\ovl{s}$}\}
 \end{equation*}
and its restrictions

\begin{equation*}
 F^{\mathrm{alg}}_{S,\ovl{s}}=F^{\mathrm{alg}}_{\ovl{s}}:
 \Cov^{\mathrm{alg}}_S\longrightarrow \Sets,
\end{equation*}
(considered in \cite{sga1}) and
\begin{equation*}
 F^{\mathrm{top}}_{S,\ovl{s}}=F^{\mathrm{top}}_{\ovl{s}}:
  \Cov^{\mathrm{top}}_S\longrightarrow \Sets.
\end{equation*} 

 An {\it \'etale path} (\resp {\it algebraic path}) from
 $\ovl{s}$ to another geometric point $\ovl{t}$ of $S$ is an isomorphism
 of functors $F^{\mathrm{et}}_{\ovl{s}} \xrightarrow{\sim}
 F^{\mathrm{et}}_{\ovl{t}}$ (\resp $F^{\mathrm{alg}}_{\ovl{s}}
 \xrightarrow{\sim} F^{\mathrm{alg}}_{\ovl{t}}$). 

 The set of \'etale paths is topologized by taking as fundamental open
 neighborhoods of an \'etale path $\alpha$ the set 
 $\Stab_{S',\ovl{s}'}\circ \alpha$, where $\Stab_{S',\ovl{s}'}$ runs among
 the stabilizers in $\Aut(F_{\bar{s}}^{\mathrm{et}})$ of arbitrary geometric
 points $\ovl{s}'$ above 
 $\ovl{s}$ in arbitrary \'etale coverings $S'/S$.

 If we do the same for algebraic paths, we get the profinite topology
 considered in \cite{sga1}. 

 On the other hand, an isomorphism of functors
 $F^{\mathrm{top}}_{\ovl{s}} \xrightarrow{\sim}
 F^{\mathrm{top}}_{\ovl{t}}$ amounts to a path up to homotopy in the
 usual sense between $s$ and $t$ in the arcwise connected space $S$
 (this is compatible with composition of paths, which is juxtaposition
 in the reverse order according to our convention); they form a
 discrete set --- in fact, a principal homogeneous space under 
 $\pi^{\mathrm{top}}(S,s)$ acting on the left. 

 \medskip The inclusions $ \Cov^{\mathrm{alg}}_S \hookrightarrow
 \Cov^{\mathrm{et}}_S ,\;\Cov^{\mathrm{top}}_S \hookrightarrow
 \Cov^{\mathrm{et}}_S$ induce continuous maps from the space of \'etale
 paths between $\ovl{s}$ and $\ovl{t}$ to the space of algebraic paths
 between $\ovl{s}$ and $\ovl{t}$ (\resp to the discrete set of paths up
 to homotopy between $s$ and $t$).

 \medskip\noindent If $f: S\to X$ is any morphism of $K$-manifolds, and
 if $\alpha$ is an \'etale path from $\ovl{s}$ to $\ovl{t}$, there is an 
 obvious notion of push-forward $f_\ast\alpha$, which is an \'etale path
 from $f\circ \ovl{s}$ to $f\circ \ovl{t}$ ; it is compatible with
 composition of \'etale paths (as composition of isomorphisms of functors).
\end{para}

\begin{para}\label{para::1.3.2} It follows from \cite[exp. V]{sga1} that
 algebraic paths exist. Using the nice topology of Berkovich spaces,
 A.J. De Jong was able to prove \cite[2.9]{efgonas}: 
\end{para}

\begin{klem}\label{lem::1.3.3}  Etale paths exist. More precisely,
 any Berkovich path $\gamma$ (up to homotopy) between $s$ and 
 $t$ lifts to an \'etale path $\ovl{\gamma}$ between $\ovl{s}$ and $\ovl{t}$.
\end{klem}

\begin{proof}
 Up to introducing intermediate geometric points, we may assume
 that $S$ is affinoid (hence compact). For any {\it finite} open cover
 $\mathcal{U}=(U_i)$ of $S$, let us denote by
 $\Cov^{\mathrm{et}}_{S,\mathcal{U}}$ the full subcategory of
 $\Cov^{\mathrm{et}}_{S}$ of \'etale coverings $f:S'\to S$ such that
 $f^{-1}(U_i)= \coprod V_{ij}$ and $V_{ij}$ is \'etale finite over $U_i$
 via $f$.  We thus have
 \begin{equation*}
 \Cov^{\mathrm{et}}_{S}=\underset{\mathcal{U}}{\liminj}\;
  \Cov^{\mathrm{et}}_{S,\mathcal{U}}, \text{ and }
  \Isom(F^{\mathrm{et}}_{\ovl{s}}, F^{\mathrm{et}}_{\ovl{t}})
  =\underset{\mathcal{U}}{\limproj}\;
  \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
  F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})
 \end{equation*}

 \medskip\noindent where $F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}}$ denote the restrictions of
 $F^{\mathrm{et}}_{\ovl{s} }, F^{\mathrm{et}}_{\ovl{t} }$ to
 $\Cov^{\mathrm{et}}_{S,\mathcal{U}}$.

 We have to show that $\Isom(F^{\mathrm{et}}_{\ovl{s}},
 F^{\mathrm{et}}_{\ovl{t}}) \neq \emptyset$. The idea is to construct 
 non-empty compact subsets $K_\mathcal{U}$ of
 $\Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})$ (topologized as above) such that
 if $\mathcal{U}'$ refines $\mathcal{U}$, $K_{\mathcal{U}'}$ maps to
 $K_\mathcal{U} $ under the natural map
 $\Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}'},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}'})\to
 \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})$; it will follow that
 $\Isom(F^{\mathrm{et}}_{\ovl{s}}, F^{\mathrm{et}}_{\ovl{t}}) \supset
 \underset{\mathcal{U}}{\limproj} K_\mathcal{U}\neq \emptyset$.

 In fact, it suffices to do so for a cofinal system of $\mathcal{U}$'s,
 which are chosen as follows. Since $S$ is {\it arcwise connected}, there
 is a continuous embedding $I=[0,1]\hookrightarrow S$ with $0\mapsto
 s,\;1\mapsto t$.
 One considers finite open coverings $\mathcal{U} =(U_1,\ldots, U_n)$
 such that
 \begin{equation*}
 U_1\cap I = [0,r_1[,\;\ldots, U_i\cap I=]r_i,t_i[,\;\ldots, U_m\cap
  I=]r_m,1],\;U_{m+1}\cap 
  I=\emptyset,\ldots
 \end{equation*}
 \noindent for some points $r_i<t_{i-1}<r_{i+1}<t_i$ in $I \;(i=2,\ldots,
 m-1)$ and some $ m\leq n$.

 Given $\mathcal{U}$, one chooses $s_i$ in $U_i\cap U_{i+1}\cap I$ (which
 amounts to a real number between $r_{i+1}$ and $t_i$), and a geometric
 point $\ovl{s}_i$ above $s_i\; (i=1,\ldots, m-1)$; one completes this
 collection of geometric points by setting $\ovl{s}_0=\ovl{s},\;
 \ovl{s}_m=\ovl{t}$.  Let us look at the diagram

 \begin{equation*}
 \Cov^{\mathrm{et}}_{S,\mathcal{U}}
 \xrightarrow{\sigma_i}
 \Ind \Cov^{\mathrm{alg}}_{\mathcal{U}_{i+1}}
 \begin{array}{c}
  \xrightarrow{F^{\mathrm{alg}}_{\ovl{s}_i, U_{i+1}}}\\
  \xrightarrow{F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}}}\\
 \end{array}
 \Sets.
 \end{equation*}               
 One has $F^{\mathrm{alg}}_{\ovl{s}_j, U_{i+1}}\circ \sigma_i =
 F^{\mathrm{et}}_{\ovl{s}_i, \mathcal{U} },\;\;j=i,i+1$, whence
 continuous maps 
 \begin{equation*}
 \Isom(F^{\mathrm{alg}}_{\ovl{s}_i,
 U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}})\to
 \Isom(F^{\mathrm{et}}_{\ovl{s}_i, \mathcal{U}
 },F^{\mathrm{et}}_{\ovl{s}_{i+1}, \mathcal{U}}).
 \end{equation*} 
 Since algebraic paths exist, $\Isom(F^{\mathrm{alg}}_{\ovl{s}_i,
 U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}})$ is a non-empty
 compact set for any $i=0,\ldots, m$.  On composing such isomorphisms for
 $i=0,\ldots, m$, one gets a continuous map
 \begin{equation*}
 \sigma_{\mathcal{U},(\ovl{s}_i)}: \prod_{i=0}^m
  \Isom(F^{\mathrm{alg}}_{\ovl{s}_{i},
  U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}})\to
  \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
  F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})
 \end{equation*} 
 whose image is a non-empty compact set $K_\mathcal{U}$.

 In fact, while the map $\sigma_{\mathcal{U},(\ovl{s}_i)}$ depends on the
 choice of the geometric points $\ovl{s}_i$, its image $K_\mathcal{U}$
 does not. Indeed, for any other choice $\ovl{s}'_i$, there is an
 algebraic path
 \begin{equation*}
  \gamma_i:\;F^{\mathrm{alg}}_{\ovl{s}_i, U_{i+1}\cap U_i} \xrightarrow{\sim}
   F^{\mathrm{alg}}_{\ovl{s}'_i, U_{i+1}\cap
   U_i},\;\;\gamma_0=\id,\;\gamma_m=\id.
 \end{equation*} 
 We denote by the same letter the induced algebraic
 paths on $U_i$ and on $U_{i+1}$. Then 
 $\sigma_{\mathcal{U},(\ovl{s}_i)}(\alpha_0,\ldots,\alpha_m) 
 =
 \sigma_{\mathcal{U},(\ovl{s}'_i)}(\gamma_1\alpha_0\gamma_0^{-1},\ldots,
 \gamma_{m}\alpha_m\gamma_{m-1}^{-1})$, whence the independence.

 From this observation, it is straightforward to conclude that if
 $\mathcal{U}'$ refines $\mathcal{U}$, $K_{\mathcal{U}'}$ maps to 
 $K_\mathcal{U} $ under the natural map
 $\Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}'},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}'})\to
 \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})$. This establishes the first
 assertion.

 For the second one (the surjectivity of
 $\Isom(F_{\ovl{s}}^{\mathrm{et}}), F_{\ovl{t}}^{\mathrm{et}}) \to
 \Isom (F_{\ovl{s}}^{\mathrm{top}}, F_{\ovl{t}}^{\mathrm{top}})$), 
 one may argue as follows: let $\ovl{\tilde s}$ be a
 lifting of $\ovl{s}$ to the universal topological covering $\pi:\tilde
 S \to S$. Then $\gamma.\bar{\tilde s}$ is a lifting of $\ovl{t}$
 to the universal topological covering.  Let $\alpha$ be an \'etale path
 between $\bar{\tilde s}$ and $\gamma.\bar{\tilde s}$. Then
 $\ovl{\gamma}:=\pi_\ast(\alpha)$ is an \'etale path between $\ovl{s}$
 and $\ovl{t}$ which maps to the ordinary path $\gamma$ up to homotopy,
 viewed as an isomorphism $F_{\ovl{s}}^{\mathrm{top}}\to
 F_{\ovl{t}}^{\mathrm{top}}$.
\end{proof}
