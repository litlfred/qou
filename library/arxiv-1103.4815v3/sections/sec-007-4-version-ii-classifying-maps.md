---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-007-4-version-ii-classifying-maps
section_title: "Version II: Classifying Maps"
section_number: 4
pages: 18-21
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.995
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{versionII}

It is well known that for a Lie group $G$ the \emph{smooth} \v Cech-cohomology $ \h^1(M,G)$ and the \emph{continuous} \v Cech-cohomology $ \h_c^1(M,G)$  agree if $M$ is a smooth manifold (in particular paracompact).
This can e.g. be shown by locally approximating continuous cocycles by smooth ones without changing the cohomology class -- see \cite{wockel2}  (even for $G$ infinite-dimensional). Below we  generalize this fact to non-abelian cohomology for certain Lie 2-groups $\Gamma$.
Here the continuous \v Cech-cohomology $ \h^1_c(M,\Gamma)$ is defined in the same way as the smooth one (Definition \ref{def:cohomology}) but with all maps  continuous instead of smooth. A Lie groupoid $\Gamma$ is called \emph{smoothly separable}, if the set  $\upi_0\Gamma$ of isomorphism classes of objects is a smooth manifold for which the projection $\Gamma_0 \to \upi_0\Gamma$ is a submersion.  

\begin{proposition}
\label{smoothening}
Let $M$ be a  smooth manifold and let $\Gamma$ be a smoothly separable Lie 2-group. Then, the  inclusion
$$  \h^1(M,\Gamma) \to  \h_c^1(M,\Gamma) $$
of smooth into continuous \v Cech cohomology is a bijection.
\end{proposition}

\begin{remark}
It is possible that the assumption of being smoothly separable is not necessary, but a proof not assuming this would certainly be more involved than ours. Anyway, \emph{all} Lie 2-groups we are interested in are smoothly separable. 
\end{remark}


\begin{proof}[Proof of Proposition \ref{smoothening}] We denote by $\upi_1\Gamma $ the Lie subgroup of $\Gamma_{1}$ consisting of automorphisms of $1 \in \Gamma_0$. Since it has two commuting group structures -- composition and multiplication -- it is abelian.
The idea of the proof is to reduce the statement via  long exact sequences to statements proved in \cite{wockel2}. The exact sequence we need can be found in \cite{breen3}:
$$\h^0(M,\idmorph {(\upi_0\Gamma)}) \to \h^1(M,\mathcal B \upi_1 \Gamma) \to \h^1(M,\Gamma) 
  \to \h^1(M,\idmorph {(\upi_0\Gamma)}) \to \h^2(M,\mathcal B\upi_1\Gamma). $$
Note that $\h^1(M,\Gamma)$ and $\h^1(M,\idmorph {(\upi_0\Gamma)})$ do not have group structures: hence, exactness is only meant as exactness of pointed sets. But we actually have more structure, namely an action of $\h^1(M,B\upi_1\Gamma)$ on $\h^1(M,\Gamma)$. This action factors to an action of
$$C := \mathrm{coker}\Big(\h^0(M,\idmorph {(\upi_0\Gamma)}) \to \h^1(M,\mathcal B\upi_1 \Gamma)\Big).$$
In fact on the non-empty fibres of the morphism $\h^1(M,\Gamma) \to \h^1(M,\idmorph {(\upi_0\Gamma)})$ this action is simply transitive. In other words: $\h^1(M,\Gamma)$ is a $C$-Torsor over 
$$ K := \mathrm{ker}\Big(\h^1(M,\idmorph {(\upi_0\Gamma)}) \to \h^2(M,\mathcal B\upi_1 \Gamma)\Big).$$
The same type of sequence also exists in continuous cohomology, namely
$$ \h^0_c(M,\idmorph {(\upi_0\Gamma)}) \to \h^1_c(M,\mathcal B\upi_1 \Gamma) \to \h^1_c(M,\Gamma) 
  \to \h^1_c(M,\idmorph {(\upi_0\Gamma)}) \to \h^2_c(M,\mathcal B\upi_1 \Gamma).$$ 
With 
\begin{eqnarray*}
C' &:=& \mathrm{coker}\Big(\h^0_c(M,\idmorph {(\upi_0\Gamma)}) \to \h^1_c(M,\mathcal B\upi_1 \Gamma)\Big)
\\
K' &:=& \mathrm{ker}\Big(\h^1_c(M,\idmorph {(\upi_0\Gamma)}) \to \h^2_c(M,\mathcal B\upi_1 \Gamma)\Big)\text{,}
\end{eqnarray*}
we exhibit $\h^1_c(M,\Gamma)$ as a $C'$-Torsor over $K'$. 
  
The natural inclusions of smooth into continuous cohomology form a chain map between the two sequences. From 
\cite{wockel2} we know that they are isomorphisms on the second, fourth and fifth factor. In particular we have an induced isomorphism $K \iso K'$. Lemma \ref{lem:images} below additionally shows that  the induced morphism $C \to C'$ is an isomorphism. Using these isomorphisms we see that $\h^1(M,\Gamma)$ and $\h^1_c(M,\Gamma)$ are both $C$-torsors over $K$ and that the natural map $$\h^1(M,\Gamma) \to \h^1_c(M,\Gamma)$$ is a morphism of torsors. But each morphism of group torsors is bijective, which concludes the proof.
\end{proof}

\begin{lemma}
\label{lem:images}
The images of 
$$f: \h^0(M,\idmorph {(\upi_0\Gamma)}) \to \h^1(M,\mathcal B\upi_1 \Gamma) \quad \text{and} \quad f':\h^0_c(M,\idmorph {(\upi_0\Gamma)}) \to \h^1_c(M,\mathcal B\upi_1 \Gamma)$$
are isomorphic.
\end{lemma}
\begin{proof}
 $\h^0(M,\idmorph {(\upi_0\Gamma)})$ is the group of smooth maps $s: M \to \upi_0\Gamma$ and $\h^0_c(M,\idmorph {(\upi_0\Gamma)})$ is the group of continuous maps $t: M \to \upi_0\Gamma$. The groups $\h^1(M,\mathcal B\upi_1 \Gamma) = \h^2(M,\upi_1 \Gamma)$ and $\h^1_c(M,\mathcal B\upi_1 \Gamma) = \h^2_{c}(M,\upi_1 \Gamma)$ are isomorphic by the result of \cite{wockel2}. Under the connecting homomorphism
\begin{equation*}
\h^0(\upi_0\Gamma,\idmorph {(\upi_0\Gamma)}) \to \h^1(\upi_0\Gamma,\mathcal B\upi_1 \Gamma)
\end{equation*}
the identity $\id_{\upi_0\Gamma}$ is sent to a class $\xi_{\Gamma}$ with the property that  $f(s) = s^{*}\xi_{\Gamma}$ and $f'(t) = t^{*}\xi_{\Gamma}$. Hence it suffices to show that for each continuous map $t: M \to \upi_0\Gamma$ there is a smooth map $s:M \to  \upi_0\Gamma$ with $s^*\xi_\Gamma = t^*\xi_\Gamma$.
It is well known that for each continuous map $t$ between smooth manifolds a homotopic smooth map $s$ exists. It remains to show that the pullback $\h^1(\upi_0\Gamma,\mathcal{B}\upi_1 \Gamma) \to \h^1(M,\mathcal{B}\upi_1 \Gamma)$ along smooth maps is homotopy invariant. This can e.g. be seen by choosing smooth (abelian) $\mathcal{B}\upi_1 \Gamma$-bundle gerbes as representatives, in which case the homotopy invariance can be deduced from the existence of connections.  
\end{proof}

It is a standard result in topology that the continuous $G$-valued \v Cech cohomology of paracompact spaces is in bijection with homotopy classes of maps to the classifying space $\mathfrak BG$ of the group $G$. A model for the classifying space $\mathfrak BG$ is for example the geometric realization of the nerve of the groupoid $\mathcal B G$, or Milnor's join construction \cite{milnor}. 


Now let $\Gamma$ be a Lie 2-group, and let $|\Gamma|$ denote the geometric realization of the nerve of $\Gamma$. Since the nerve is a simplicial topological group, $|\Gamma|$ is a topological group. Version II for smooth $\Gamma$-gerbes is:

\begin{definition}[{\cite{baez8}}]
\label{def:classmap}
A classifying map for a smooth $\Gamma$-gerbe is a continuous map
\begin{equation*}
f: M \to \mathfrak{B}|\Gamma|\text{.}
\end{equation*}
\end{definition}

We denote by $\big[ M , \mathfrak B |\Gamma|\big]$ the set of homotopy classes of classifying maps. 

\begin{proposition}[{{\cite[Theorem 1]{baez8}}}]
\label{bstheorem}
Let $\Gamma$ be a Lie 2-group. Then there is a bijection 
$$ \h_c^1(M,\Gamma) \cong \big[ M , \mathfrak B |\Gamma|\big]$$
where the topological group $|\Gamma|$ is the geometric realization of the nerve of $\Gamma$.
\end{proposition}

Note that the assumption of \cite[Theorem 1]{baez8} that $\Gamma$ is well-pointed is automatically satisfied because  Lie groups are well-pointed. Propositions \ref{smoothening} and \ref{bstheorem}  imply the following equivalence theorem between Version I and Version II.

\begin{theorem}
\label{th:classifying}
For $M$ a smooth manifold and $\Gamma$ a smoothly separable Lie 2-group, there is a  bijection
\begin{equation*}
\h^1(M,\Gamma) \cong \big[ M , \mathfrak B |\Gamma|\big].
\end{equation*}
\end{theorem}


\begin{remark}
\label{rem:baas}
 Baez and Stevenson argue in \cite[Section 5.2.]{baez8} that the space $\mathfrak B |\Gamma|$ is homotopy equivalent to a certain geometric realization of the Lie 2-groupoid  $|\mathcal B\Gamma|$ from Section \ref{versionI}. Baas, B�stedt and Kro have shown \cite{baas2} that $|\mathcal{B}\Gamma|$ classifies concordance classes of charted $\Gamma$-2-bundles. In particular, charted $\Gamma$-2-bundles are a further equivalent version of smooth $\Gamma$-gerbes. 
\end{remark}



\setsecnumdepth{2}
