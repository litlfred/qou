---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-004-bimodule-categories-with-bimodule-traces
section_title: "Bimodule categories with bimodule traces"
section_number: null
pages: 9-11
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.961
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
(Bi)module traces on (bi)module categories over fusion categories were first  introduced by Schaumann in \cite{G12} and investigated further in  \cite{G14}.
We summarise (bi)module traces for finite semisimple (bi)module categories over pivotal fusion categories from \cite{G12,G14}. 
To keep notation simple, we focus on left module categories and identify $(\mac,\mad)$-bimodule categories with $\mac\boxtimes\mad^{rev}$-left module categories.


\begin{definition}\label{def:moduletrace} \cite[Def.~3.7]{G12}

Let $\mac$ be a pivotal multifusion category and $\mam$  a finite semisimple $\mac$-module category.\\
A {\bf trace} on $\mam$ is a collection of morphisms $\theta_m: \End_\mam(m)\to \C$ indexed by objects $m\in\Ob\mam$ that satisfy
\begin{compactenum}
\item {\bf cyclicity:} $\theta_m(\beta\circ \alpha)=\theta_{m'}(\alpha\circ \beta)$ for all $\alpha\in \Hom_\mam(m,m')$ and $\beta\in \Hom_\mam(m',m)$.
\item {\bf non-degeneracy:} for all $m,m'\in\Ob\mam$ the following bilinear maps are non-degenerate.
$$
\Hom_\mam(m',m)\times \Hom_\mam(m,m')\to \C,\quad (\beta,\alpha)\mapsto \theta_m(\beta\circ \alpha)
$$
\end{compactenum}
A trace  on $\mam$ is called a {\bf $\mac$-module trace} if $\theta_{c\rhd m}(\alpha)=\theta_{m}(\tr^\mac(\alpha))$ for all $\alpha\in \End_\mam(c\rhd m)$, where $\tr^\mac(\alpha)$  is the partial trace of $\alpha$ with respect to $\mac$
$$
\tr^\mac(\alpha)=(\ev^L_c\rhd 1_m)\circ c^\inv_{c^*,c,m}\circ (1_{c^*}\rhd \alpha)\circ c_{c^*,c,m}\circ (\coev^R_{c}\rhd 1_m): m\to m.
$$
\end{definition}

Analogously, a $\mad$-right module trace on a $\mad$-right module category $\mam$ is defined as a $\mad^{rev}$-module trace and a
$(\mac,\mad)$-bimodule trace on a $(\mac,\mad)$-bimodule category $\mam$ as a $\mac\boxtimes \mad^{rev}$-module trace. 

As for spherical categories,  the {\bf dimension} of an object $m$ in a (bi)module category $\mam$ with a (bi)module trace is $\dim(m)=\theta_m(1_m)$ and  for any set $I$ of representatives of the isomorphism classes of simple objects 
\begin{align}
\dim(\mam)=\sum_{m\in I} \dim(m)^2.
\end{align}
If $\mathcal C$ is spherical, the condition that $\theta$ is a $\mac$-module trace  implies for all $c\in \Ob\mac$  and $m\in\Ob\mam$
\begin{align}\label{eq:dimensionsmodule}
\dim(c\rhd m)=\dim(c)\dim(m).
\end{align}
It is shown in \cite[Prop.~4.4]{G12} that a $\mac$-module trace on an {\em indecomposable} finite semisimple module category $\mam$ is unique up to rescaling $\theta_m\to z\theta_m$ with $z\in\C^\times$. The existence of a $\mac$-module trace on a $\mac$-module category $\mam$ is a condition on  the dimensions of simple objects of $\mac$ and $\mam$, see \cite[Sec.~5]{G12}.

\begin{example} \label{ex:sphtriv}
 A pivotal fusion category $\mac$ as a $(\mac,\mac)$-bimodule category over itself has a bimodule trace if and only if $\mac$ is spherical. 
\end{example}

\begin{example}\label{ex:opptrace}
Each  $(\mac,\mad)$-bimodule trace on a finite semisimple $(\mac,\mad)$-bimodule category $\mam$ defines a $(\mad,\mac)$-bimodule trace on the opposite bimodule category $\mam^\#$ from Example \ref{ex:dualcat}.
\end{example}

\begin{example}\cite[Ex.~3.13]{G12} \label{ex:tracevect}An indecomposable module category over the pivotal fusion category $(\mathrm{Vec}_G, \kappa)$,  given by a pair $(G/L,\psi)$ as in Example \ref{ex:modvectgomega}, admits a module trace iff $\kappa\vert_{L}\equiv 1$.
Any indecomposable semisimple module category over $\mathrm{Vec}_G$ with the standard spherical structure admits a module trace.
\end{example}




(Bi)module traces on (bi)module categories equip (bi)module functors between them with additional structure. It is shown in \cite[Th.~4.5]{G12}  that for module categories $\mam$ and $\man$  over a pivotal fusion category $\mac$  with  module traces, any module functor $F:\mam\to\man$ is naturally isomorphic to its double left adjoint $F^{ll}: \mam\to\man$. This  defines a pivotal structure in the sense of \cite[Def.~A.12]{G14}, namely  a natural 2-isomorphism $\omega: \id\Rightarrow **$, where $*$ is the contravariant 2-functor that assigns each module category to itself,  each functor to its left dual and each module natural transformation $\nu: F\Rightarrow G$ to the induced natural transformation $\nu^*: G^l\Rightarrow F^l$. 


\begin{theorem}\label{th:pivot}\cite[Th.~4.5]{G12}, \cite[Th.~5.8]{G14} 
\begin{enumerate}
\item For all pivotal fusion categories $\mac$ the 2-category $\text{Mod}^{\,\theta}(\mac)$ of $\mac$-module categories with $\mac$-module traces, $\mac$-module functors between them  and $\mac$-module natural transformations is pivotal.

\item For all  pivotal fusion categories $\mac,\mad$ the 2-category  $\Bimod^\theta(\mac,\mad)$ of  $(\mac,\mad)$-bimodule categories with bimodule traces, $(\mac,\mad)$-bimodule functors between them and $(\mac,\mad)$-bimodule transformations is pivotal. 
\end{enumerate}
\end{theorem}

In particular, this yields  pivotal structures  on the finite multifusion  categories  $\End_\mac(\mam)$. If the underlying fusion category $\mac$ is spherical, these pivotal structures become spherical.  If $\mam$ is also indecomposable, then  $\End_\mac(\mam)$ is a spherical fusion category. An earlier proof of this was given by Mueger in \cite[Th.~5.16]{Mue}.

\begin{corollary} \label{cor:endmpiv} \cite[Prop.~5.10]{G12}  For any spherical fusion category $\mac$ and any  $\mac$-module category $\mam$ with a $\mac$-module trace,
$\End_\mac(\mam)$ is  spherical. If $\mam$ is indecomposable, $\End_\mac(\mam)$ is a spherical fusion category.
\end{corollary}



For any module category $\mam$ over a fusion category $\mac$ with a $\mac$-module trace, the multifusion category $\End_\mac(\mam)$ acts on $\mam$. This  action functor is given by the evaluation of endofunctors  and natural transformations between them on objects and morphisms of $\mam$. If $\mac$ is pivotal, then $\End_\mac(\mam)$ is pivotal and the module trace of $\mam$ also satisfies the module trace condition for the $\End_\mac(\mam)$-module category structure. 


\begin{corollary}\label{lem:macmodule}\cite[Cor.~4.6]{G12} Let $\mac$ be a pivotal fusion category and  $\mam$ be a $\mac$-module category with a $\mac$-module trace $\theta$. Then $\theta$ is also an $\End_\mac(\mam)$-module trace.  
\end{corollary}


More explicitly, the pivotal structure from Theorem \ref{th:pivot} and Corollaries \ref{cor:endmpiv} and \ref{lem:macmodule} is given as follows. If we denote by $F^l: \mam\to\mam$ the left adjoint of a $\mac$-module functor $F:\mam\to\mam$, by $\eta^F: \id_\man\Rightarrow FF^l$ the unit and  by $\epsilon^F:F^lF\Rightarrow \id_\mam$ the counit of this adjunction,
 then the component morphisms
 $\omega^F: F^{ll}\Rightarrow F$ of the pivotal structure are characterised by the condition
\begin{align}
\label{eq:pivcond}
\theta^\mam_{F^l(n)}(\beta\circ\epsilon^F_m\circ F^l(\alpha))=\theta^\man_n (\epsilon^{F^l}_n\circ F^{ll}(\beta)\circ\omega^{F\inv}_m \circ \alpha)
\end{align}
for all $\alpha\in \Hom_\man(n, F(m))$ and $\beta\in \Hom_\mam(m, F^l(n))$. This condition encodes the chain of natural isomorphisms that defines $\omega^F$  in equation (4.14) in \cite{G12}.

Condition \eqref{eq:pivcond} implies an identity that  generalises Corollary \ref{lem:macmodule} to $\mac$-module functors that are not endofunctors. 
It is obtained from the (co)evaluations for the right duals  induced by  $\omega^F: F^{ll}\Rightarrow F$
\begin{align}\label{eq	:etaprime}\eta'^{F}=F^l\omega^F\circ \eta^{F^l}:\id_\mam\Rightarrow F^lF\qquad\qquad \epsilon'^F= \epsilon^{F^l}\circ \omega^{F\inv}F^l:FF^l \Rightarrow \id_\man.
\end{align} 

 

\begin{corollary}\label{cor:functortrace} Let $\mac$ be a pivotal fusion category and $\mam$, $\man$ $\mac$-module categories with $\mac$-module traces. Then any $\mac$-module functor $F:\mam\to\man$ satisfies
\begin{align}\label{eq:traceconds}
&\theta^\mam_m(\epsilon^{F}_m\circ F^l(\alpha)\circ \eta'^F_m)=\theta^\man_{F(m)}(\alpha)
\end{align}
for all $m\in\Ob\mam$, $n\in\Ob\man$ and morphisms $\alpha: F(m)\to F(m)$.
\end{corollary}

\begin{proof}
This follows by setting $n=F(m)$ and $\beta=\eta'^F_m=F^l(\omega^F_m)\circ \eta^{F^l}_m: m\to F^lF(m)$ in \eqref{eq:pivcond}. By cyclicity of $\theta^\mam$, the left-hand side of  \eqref{eq:pivcond} is  equal to the left-hand side of \eqref{eq:traceconds}. The right-hand side of \eqref{eq:pivcond} can  be simplified using the naturality of  $\omega^F$ and the for the defining identities for the unit and counit of an adjunction and yields the right-hand side of \eqref{eq:traceconds}. 
\end{proof}

Note that for an endofunctor $F:\mam\to\mam$, condition \eqref{eq:traceconds} is just the partial trace condition from Definition \ref{def:moduletrace} for the  $\End_\mac(\mam)$-module structure on $\mam$ and  Corollary \ref{cor:functortrace} reduces to Corollary \ref{lem:macmodule}.
