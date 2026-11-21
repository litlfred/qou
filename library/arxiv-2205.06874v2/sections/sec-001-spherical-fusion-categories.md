---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-001-spherical-fusion-categories
section_title: "Spherical fusion categories"
section_number: null
pages: 4-5
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.976
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
We work over $\C$ and follow the conventions of Etingof et al.~in \cite{EGNO}. 
A {\bf multitensor category} is a  locally finite, $\C$-linear abelian rigid monoidal category  $\mac$ with a tensor product $\oo:\mac\times\mac\to \mac$  that is bilinear on the morphisms.  A {\bf tensor category} is an  indecomposable multitensor category
 with $\End_\mac(e)\cong \C$, where $e$ is the tensor unit.
A {\bf (multi)fusion category} is a finite semisimple (multi)tensor category.  

For all categories $\mac$ we denote by $\mac^{op}$ the opposite category and for all monoidal categories $\mac$ by $\mac^{rev}$ the category $\mac$ with the opposite monoidal structure. We define a {\bf left rigid} monoidal category as a category in which every object $x$ has a left dual $x^*$  and evaluation and coevaluation morphisms
\begin{align}\label{eq:coevl}
&\ev^L_x: x^*\oo x\to e, & &\coev^L_x: e\to x\oo x^*
\end{align}
that satisfy the identities 
\begin{align}\label{eq:snake}
(1_x\oo\ev^L_x)\circ (\coev^L_x\oo 1_x)=1_x\qquad (\ev^L_x\oo 1_{x^*})\circ (1_{x^*}\oo \coev^L_x)=1_{x^*},
\end{align}
 up to associators and unit constraints. 
We denote by $*: \mac\to\mac^{op,rev}$ the induced monoidal functor, see the  end of Section 2.10 in \cite{EGNO}. 
A {\bf pivotal} monoidal category $\mac$ is a left rigid monoidal category $\mac$ with a monoidal isomorphism  $\omega:**\Rightarrow\id_\mac$. 
Every pivotal category is right rigid with  
\begin{align}\label{eq:coevr}
&\ev^R_x=\ev^L_{x^*}\circ (\omega^\inv_x\oo 1_{x*}): x\oo x^*\to e, & &\coev^R_x=(1_{x^*}\oo\omega)\circ \coev^L_{x^*}: e\to x^*\oo x,
\end{align}
and the left and right trace of a morphism $\alpha\in \End_\mac(x)$ are given by
\begin{align}
&\tr^L(\alpha)=\ev^L_x\circ (1_{x^*}\oo \alpha)\circ \coev^R_x, & &\tr^R(\alpha)=\ev^R_x\circ (\alpha\oo 1_{x^*})\circ \coev^L_x.
\end{align}
A pivotal category $\mac$ is {\bf spherical} if $\tr^L(\alpha)=\tr^R(\alpha)$ for all endomorphisms $\alpha$ in $\mac$. In this case we  write $\tr(\alpha)=\tr^L(\alpha)=\tr^R(\alpha)$ and $\dim(x)=\tr(1_x)=\tr(1_{x^*})=\dim(x^*)$ for all $\alpha\in \End_\mac(x)$ and $x\in\Ob\mac$. 
The {\bf dimension} of a spherical fusion category $\mac$ is 
\begin{align}
\label{eq:catdimension}
\dim(\mac)=\sum_{i\in I} \dim(i)^2,
\end{align}
where $I$ is a set of representatives of the isomorphism classes of simple objects. 

\begin{example}\label{ex:vectgomega}\cite[Ex.~2.3.6]{EGNO}\\ Let $G$ be a finite group and $\omega: G\times G\times G\to \C^\times$ a normalised  3-cocycle. 
 The fusion category
$\mathrm{Vec}_G^\omega$ has
\begin{compactitem}
\item  as objects finite-dimensional $G$-graded vector spaces $V=\oplus_{g\in G} V_g$,
\item  as morphisms linear maps $f: V\to W$ with $f(V_g)\subset W_g$ for all $g\in G$,
\item  simple objects  $\delta^g$ for $g\in G$ with $(\delta^g)_g=\C$ and $(\delta^g)_h=0$ for $g\neq h$, 
\item  the  tensor product $V\oo W=\oplus_{g\in G}(\oplus_{hk=g} V_h\oo W_k)$, 
\item  the associator  given by $a_{\delta^g,\delta^h,\delta^k}=\omega(g,h,k) \id_{\delta^{ghk}}$ on the simple objects,  

\item dual objects $V^*=\oplus_{g\in G} V_{g^\inv}^*$ with the  usual (co)evaluation for finite-dimensional vector spaces,
\item pivotal structures that  are in bijection with characters $\kappa: G\to\C^\times$. 
 \end{compactitem}
A pivotal structure is spherical iff $\kappa(g)\in \{1,-1\}$ for all $g\in G$.
In particular, the trivial character $\kappa\equiv 1$ determines a spherical structure on  $\mathrm{Vec}_G^\omega$, its {\bf standard spherical structure}.
\end{example}
