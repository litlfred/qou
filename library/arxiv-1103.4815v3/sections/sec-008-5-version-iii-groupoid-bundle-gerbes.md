---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-008-5-version-iii-groupoid-bundle-gerbes
section_title: "Version III: Groupoid Bundle Gerbes"
section_number: 5
pages: 21-27
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
text_source: latex
latex_prose_ratio: 0.625
latex_coverage_ratio: 0.972
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
\label{versionIII}

Several definitions of non-abelian bundle gerbes have appeared in literature so far \cite{aschieri,jurco1,murray5}. The approach we give here not only shows a conceptually clear way to define  non-abelian bundle gerbes, but also produces systematically a whole bicategory. Moreover, these bicategories form a 2-stack over smooth manifolds (with the Grothendieck topology of surjective submersions).  



\subsection{Definition via the Plus Construction}

Recall that the stack $\bun\Gamma-$ of principal $\Gamma$-bundles is monoidal if $\Gamma$ is a Lie 2-group (Proposition \ref{prop:monoidalstack}). Associated to the monoidal stack $\bun\Gamma-$ we have a pre-2-stack 
\begin{equation*}
\triv\grb \Gamma - := \mathcal{B}(\bun\Gamma-)
\end{equation*}
of \emph{trivial $\Gamma$-gerbes}. Explicitly, there is one trivial $\Gamma$-gerbe $\mathcal{I}$ over every smooth manifold $M$. The 1-morphisms from $\mathcal{I}$ to $\mathcal{I}$ are principal $\Gamma$-bundles over $M$, and the 2-morphisms between those are  morphisms of principal $\Gamma$-bundles.
Horizontal composition is given by the tensor product of principal $\Gamma$-bundles, and vertical composition is the ordinary composition of $\Gamma$-bundle morphisms. 

Now we apply the \emph{plus construction} of \cite{nikolaus2} in order to stackify this pre-2-stack. The resulting 2-stack is by definition the \emph{2-stack of $\Gamma$-bundle gerbes}, i.e.
\begin{equation*}
\grb\Gamma- := \left ( \triv\grb\Gamma- \right )^{+}\text{.}
\end{equation*}
Unwinding the details of the plus construction, we obtain the following definitions:

\begin{definition} \label{def:grb}
Let $M$ be a smooth manifold. A \emph{$\Gamma$-bundle gerbe over $M$} is a surjective submersion $\pi\maps Y \to M$, a principal $\Gamma$-bundle $P$ over $Y^{[2]}$ and an associative morphism
\begin{equation*}
\mu: \pi_{23}^{*}P \otimes \pi_{12}^{*}P \to \pi_{13}^{*}P
\end{equation*}
of $\Gamma$-bundles over $Y^{[3]}$.
\end{definition}

The morphism $\mu$ is called the \emph{bundle gerbe product}. 
Its associativity is the evident condition for bundle morphisms over $Y^{[4]}$. 


In order to proceed with the 1-morphisms, we say that a \emph{common refinement} of two surjective submersions $\pi_1: Y_1 \to M$ and $\pi_2: Y_2 \to M$ is a smooth manifold $Z$ together with surjective submersions $Z \to Y_1$ and $Z \to Y_2$ such that the diagram
\begin{equation*}
\alxydim{@=0.6cm}{& Z \ar[dr]^{} \ar[dl]_{} & \\ Y_1 \ar[dr]_{\pi_1} && Y_2 \ar[dl]^{\pi_2} \\ & M&}
\end{equation*}
is commutative. 


We fix the following convention: suppose $P_1$ and $P_2$ are $\Gamma$-bundles over surjective submersions $U_1$ and $U_2$, respectively, and $V$ is a common refinement of $U_1$ and $U_2$. Then, a bundle morphism $\varphi: P_1 \to P_2$ is understood to be a bundle morphism between the pullbacks of $P_{1}$ and $P_2$ to the common refinement $V$. For example, in the following definition
this convention applies to $U_1 = Y_1^{[2]}$, $U_2 = Y_2^{[2]}$ and $V =\ Z^{[2]}$. 
 

\begin{definition}
\label{def1mor}
Let $\mathcal{G}_1$ and $\mathcal{G}_2$ be $\Gamma$-bundle gerbes over $M$. A \emph{1-morphism} $\mathcal{A}: \mathcal{G}_1 \to \mathcal{G}_2$ is a common refinement $Z$ of the surjective submersions of $\mathcal{G}_1$ and $\mathcal{G}_2$ together with a principal $\Gamma$-bundle $Q$ over $Z$ and a morphism
\begin{equation*}
\beta: P_2 \otimes \zeta_1^{*}Q  \to \zeta_2^{*}Q \otimes P_1
\end{equation*}
of $\Gamma$-bundles over $Z^{[2]}$,  where $\zeta_{1},\zeta_2: Z^{[2]} \to Z$ are the two projections, such that $\alpha$ is compatible with the bundle gerbe products $\mu_1$ and $\mu_2$.
\end{definition}

\begin{comment}
Over a point $(z,z')\in Z^{[2]}$, the isomorphism $\beta$ is fibre-wise like
\begin{equation*}
\beta_{z,z'}: P_2|_{y_2(z),y_2(z')} \otimes Q_{z} \to Q_{z'} \otimes P_1|_{y_1(z),y_1(z')}\text{.}
\end{equation*}
\end{comment}

The compatibility of $\alpha$ with $\mu_1$ and $\mu_2$ means that the diagram
\begin{equation}
\label{compgerbemorph}
\alxydim{@C=2cm@R=1.3cm}{\pi_{23}^{*}P_2 \otimes \pi_{12}^{*}P_2 \otimes \zeta_1^{*}Q  \ar[d]_{\id \otimes \zeta_{12}^{*}\beta} \ar[r]^-{\mu_2 \otimes \id} & \pi_{13}^{*}P_2 \otimes \zeta_1^{*}Q \ar[dd] ^{\zeta_{13}^{*}\beta} \\ \pi_{23}^{*}P_2 \otimes \zeta_2^{*}Q \otimes \pi_{12}^{*}P_1 \ar[d]_{\zeta_{23}^{*}\beta \otimes \id} & \\ \zeta_3^{*}Q \otimes \pi_{23}^{*}P_1 \otimes \pi_{12}^{*}P_1 \ar[r]_-{ \id \otimes \mu_1} & \zeta_3^{*}Q \otimes \pi_{13}^{*}P_1}
\end{equation} 
of morphisms of $\Gamma$-bundles over $Z^{[3]}$ is commutative. 

If $\mathcal{A}_{12}: \mathcal{G}_1 \to \mathcal{G}_2$ and $\mathcal{A}_{23}: \mathcal{G}_2 \to \mathcal{G}_3$ are 1-morphisms between bundle gerbes over $M$, the composition $\mathcal{A}_{23} \circ \mathcal{A}_{12}: \mathcal{G}_1 \to \mathcal{G}_3$ is given by the fibre product $Z := Z_{23} \times_{Y_2} Z_{12}$, the principal $\Gamma$-bundle $Q := Q_{23} \otimes Q_{12}$ over $Z$, and the morphism
\begin{equation*}
\alxydim{@C=2cm}{P_3 \otimes \zeta_1^{*}Q   \ar[r]^-{\beta_{23} \otimes \id} & \zeta_2^{*}Q_{23} \otimes P_2 \otimes \zeta_1^{*}Q_{12} \ar[r]^-{\id \otimes \beta_{12}} &   \zeta_2^{*}Q \otimes P_1 \text{.}}
\end{equation*}
The identity 1-morphism $\id_{\mathcal{G}}$ associated to a $\Gamma$-bundle gerbe $\mathcal{G}$ is given by $Y$ regarded as a common refinement of $\pi:Y \to M$ with itself,  the trivial $\Gamma$-bundle $\trivlin_1$ (the tensor unit of $\bun\Gamma Y$), and the evident morphism $\trivlin_1 \otimes P \to P \otimes \trivlin_1$. 

In order to define 2-morphisms, suppose that $\pi_1: Y_1 \to M$ and $\pi_2:Y_2 \to M$ are surjective submersions, and that $Z$ and $Z'$ are common refinements of $\pi_1$ and $\pi_2$. Let $W$ be a  common refinement of $Z$ and $Z'$  with surjective submersions $r:W \to Z$ and $r':W \to Z'$.  We obtain  two maps
\begin{equation*}
\alxydim{}{s_1: W \ar[r]^-{r} & Z \ar[r] & Y_1 
\quad\quand\quad
t_1: W \ar[r]^-{r'} & Z' \ar[r] & Y_1\text{,}}
\end{equation*}
and analogously,  two maps $s_2,t_2: W \to Y_2$. These patch together to maps 
$$x_W:=(s_1,t_1)~:~ W \to Y_1 \times_M Y_1 \qquad\text{and}\qquad y_W:=(s_2,t_2)~:~ W \to Y_2 \times_M Y_2.$$


\begin{definition}
\label{def2mor}
Let $\mathcal{G}_1$ and $\mathcal{G}_2$ be $\Gamma$-bundle gerbes over $M$, and let $\mathcal{A},\mathcal{A}': \mathcal{G}_1 \to \mathcal{G}_2$ be 1-morphisms. A \emph{2-morphism} $\varphi: \mathcal{A} \Rightarrow \mathcal{A}'$ is a common refinement $W$ of the common refinements $Z$ and $Z'$, together with a morphism 
\begin{equation*}
\varphi: y_W^*P_2 \otimes r^{*}Q \to {r'}^{*}Q' \otimes x_W^* P_1
\end{equation*}
of $\Gamma$-bundles over $W$ that is compatible with the morphisms $\beta$ and $\beta'$.
\end{definition}

The compatibility means that a certain diagram over $W^{[2]}$ commutes. Fibrewise over a point $(w,w') \in W \times_M \nobr W$ this diagram looks as follows:
\begin{equation}
\label{eq:comp2morphcomplicated}
\alxydim{@R=1.3cm@C=0.35cm}{
{P_2}|_{s_2(w'),t_2(w')} \otimes {P_2}|_{s_2(w),s_2(w')} \otimes Q|_{r(w)}  \ar[rr]^-{\id \otimes \beta} \ar[d]_{\mu_2 \otimes \id} & &
{P_2}|_{s_2(w'),t_2(w')} \otimes Q|_{r(w')} \otimes {P_1}|_{s_1(w),s_1(w')} \ar[d]^{\varphi \otimes \id} \\ 
{P_2}|_{s_2(w),t_2(w')} \otimes Q|_{r(w)}\ar[d]_{\mu_2^{-1} \otimes \id} && 
{Q'}|_{r'(w')} \otimes {P_1}|_{s_1(w'),t_1(w')} \otimes {P_1}|_{s_1(w),s_1(w')} \ar[d]^{id \otimes \mu_1} \\
{P_2}|_{t_2(w),t_2(w')} \otimes {P_2}|_{s_2(w),t_2(w)}\otimes Q|_{r(w)}  \ar[d]_{\id \otimes \varphi} &&
 {Q'}|_{r'(w')} \otimes {P_1}|_{s_1(w),t_1(w')} \ar[d]^{id \otimes \mu_1^{-1}}\\
{P_2}|_{t_2(w),t_2(w')} \otimes {Q'}|_{r'(w)} \otimes {P_1}|_{s_1(w),t_1(w)} \ar[rr]_{\beta' \otimes \id}&&
{Q'}|_{r'(w')} \otimes {P_1}|_{t_1(w),t_1(w')} \otimes {P_1}|_{s_1(w),t_1(w)}
}
\end{equation} 
Finally we identify two 2-morphisms  $(W_1,r_1,r_1',\varphi_1)$ and $(W_2,r_2,r_2',\varphi_2)$ if the pullbacks of $\varphi_1$ 
and $\varphi_2$ to $W \times_{Z \times_{\times} Z'} \nobr W'$ agree. Explicitly, this condition means that for all $w_{1} \in W_1$ 
and $w_{2} \in W_{2}$ with $r_1(w_1)=r_2(w_2)$ and $r_1'(w_1) = r_2'(w_2)$, and for all
$p_2 \in y_{W_1}^{*}P_2 = y_{W_2}^{*}P_2$ and $q\in r_1^{*}Q = r_2^{*}Q$ we have $\varphi_1(p_2,q) = \varphi_2(p_2,q)$. 



\begin{remark}
\label{rem:2morphisms}
\begin{itemize}
\item 
In the above situation of a common refinement $W$ of two common refinements $Z,Z'$ of surjective submersions $Y_1,Y_2$, the diagram 
\begin{equation}
\label{diag:refinement}
\alxydim{@=0.8cm}{
& Z \ar[dr]^{} \ar[dl]_{} & \\ 
Y_1  & W \ar[u]_-{r}\ar[d]^-{r'} & Y_2 \\
 & Z' \ar[lu]\ar[ru] &
}
\end{equation}
is \emph{not} necessarily commutative. In fact, diagram \erf{diag:refinement} commutes if and only if the two maps $x_W\maps W \to Y_1 \times_M Y_1$ and $y_W: W \to Y_2 \times_M Y_2$ factor through the diagonal maps $Y_1 \to Y_1 \times_M Y_1$ and $Y_2 \to Y_2 \times_M Y_2$, respectively.

\item
In the case that a 2-morphism $\varphi$ is defined on a common refinement $Z$ for which diagram \erf{diag:refinement} \emph{does} commute, Definition \ref{def2mor} can be simplified. As remarked before, the two maps $x_W$ and $y_W$ factor through the diagonals, over which  the bundles $P_1$ and $P_2$  have canonical trivializations (see Corollary \ref{co:groupoidstructure}). Under these trivializations, $\varphi$ can be identified with a bundle morphism
\begin{equation*}
\varphi: Q \to Q' \text{.}
\end{equation*}
Furthermore, the compatibility diagram \erf{eq:comp2morphcomplicated}  simplifies to the diagram
\begin{equation}
\label{eq:comp2morphsimple}
\alxydim{@=1.3cm}{P_2 \otimes \eta_1^{*}Q \ar[r]^{\beta} \ar[d]_{\id \otimes \eta_1^{*}\varphi}  & \eta_2^{*}Q \otimes P_1 \ar[d]^{\eta_2^{*}\varphi \otimes \id} \\ P_2 \otimes \eta_1^{*}Q' \ar[r]_{\beta'} & \eta_2^{*}Q' \otimes P_1\text{.}}
\end{equation} 
\begin{comment}
In spite of these simplifications, it is  necessary to stick to general refinements $W$ (with non-commuting diagram \erf{diag:refinement}) in order to get enough 2-morphisms.
\end{comment}
\end{itemize}
\end{remark}


Next we  define the vertical composition $\varphi_{23} \bullet \varphi_{12}: \mathcal{A}_1 \Rightarrow \mathcal{A}_3$ of 2-morphisms $\varphi_{12}: \mathcal{A}_1 \Rightarrow \mathcal{A}_2$ and $\varphi_{23} \maps \mathcal{A}_2 \Rightarrow \mathcal{A}_3$. The refinement is the fibre product $W :=  W_{12} \times_{Z_2} W_{23}$ of the covers of $\varphi_{12}$ and $\varphi_{23}$. The bundle gerbe products induce  isomorphisms
$$ x_W^* P_1 \cong x_{W_{23}}^*P_1 \otimes x_{W_{12}}^*P_1 \qquad \text{and} \qquad y_W^* P_2 \cong y_{W_{23}}^*P_2 \otimes y_{W_{12}}^*P_2$$
over $W$. Under these identifications, the morphism $y_W^*P_2 \otimes Q_1 \to Q_3 \otimes x_W^*P_1$ for the 2-morphism $\varphi_{23} \bullet \varphi_{12}$ is defined as
\begin{equation*}
\alxydim{@C=0.6cm}{
y_{W_{23}}^*P_2 \otimes y_{W_{12}}^*P_2 \otimes Q_1 \ar[rr]^-{\id \otimes \varphi_{12}} && 
y_{W_{23}}^*P_2 \otimes Q_2 \otimes x_{W_{12}}^*P_1 \ar[rr]^-{\varphi_{23} \otimes \id} &&
Q_3 \otimes x_{W_{23}}^*P_1  \otimes x_{W_{12}}^*P_1\text{.}
}
\end{equation*}
The identity for vertical composition is just the identity refinement and the identity morphism. Finally we come to the horizontal composition 
\begin{equation*}
\varphi_{23} \circ \varphi_{12}: \mathcal{A}_{23} \circ \mathcal{A}_{12} \Rightarrow \mathcal{A}_{23}' \circ \mathcal{A}_{12}'
\end{equation*}
of 2-morphisms $\varphi_{12}: \mathcal{A}_{12} \Rightarrow \mathcal{A}_{12}'$ and $\varphi_{23}: \mathcal{A}_{23} \Rightarrow \mathcal{A}_{23}'$: its refinement $W$ is given by $W_{12} \times_{(Y_2 \times Y_2)} W_{23}$. We look at the three relevant maps  $x_W: W \to Y_1 \times_M Y_1$, $y_W: W \to Y_2 \times_M Y_2$ and $z_W: W \to Y_3 \times_M Y_3$. The morphism $\varphi$ of the 2-morphism $\varphi_{23} \circ \varphi_{12}$ is defined as the composition
\begin{equation*}
\alxydim{}{
z_W^* P_3 \otimes Q_{23} \otimes Q_{12} \ar[rr]^-{\varphi_{23} \otimes \id} &&
Q'_{23} \otimes y_W^*P_2 \otimes Q_{12} \ar[rr]^-{\id \otimes \varphi_{12}} &&
Q'_{23} \otimes Q'_{12} \otimes x_W^*P_1 \text{.}
}
\end{equation*}

It follows from the properties of the plus construction \cite{nikolaus2} that (a) these definitions fit together into a bicategory $\grb\Gamma M$, and that (b) these form a pre-2-stack $\grb\Gamma-$ over smooth manifolds. That means, there are \emph{pullback 2-functors}
\begin{equation*}
f^{*}: \grb\Gamma N \to \grb\Gamma M
\end{equation*}
associated to  smooth maps $f:M \to N$, and that these are compatible with the composition of smooth maps. Pullbacks of $\Gamma$-bundle gerbes, 1-morphisms, and 2-morphisms are  obtained by just taking the pullbacks of all involved data.
Finally, the plus construction implies (c):


\begin{theorem}[{{\cite[Theorem 3.3]{nikolaus2}}}]
\label{th:stack}
The pre-2-stack $\grb\Gamma-$ of $\Gamma$-bundle gerbes is a 2-stack. 
\end{theorem}


\begin{remark}
\label{rem:grbgrp}
Every 2-stack over smooth manifolds defines a 2-stack over Lie groupoids \cite[Proposition 2.8]{nikolaus2}. This way, our approach produces automatically bicategories $\grb \Gamma{\mathcal{X}}$ of $\Gamma$-bundle gerbes over a Lie groupoid $\mathcal{X}$. In particular, for an action groupoid $\mathcal{X}=\act MG$ we have a bicategory $\grb\Gamma{\act MG}$ of \emph{$G$-equivariant $\Gamma$-bundle gerbes} over $M$.
\end{remark}

In the remainder of this section we give some examples and describe relations between the definitions given here and existing ones. 


\begin{example}
\label{ex:abelianbundlegerbes}
Let $A$ be an abelian Lie group, for instance $\ueins$. Then, $\mathcal{B}A$-bundle gerbes are  the same as the well-known $A$-bundle gerbes \cite{murray}. For more details see Remark \ref{re:1-morphisms} below.
\end{example}

\begin{example}
Let $(G,H,t,\alpha)$ be a smooth crossed module, and let $\act GH$ be the associated action groupoid. Then, a $(\act GH)$-bundle gerbe is the same as a \emph{crossed module bundle gerbe} in the sense of Jurco \cite{jurco1}. The equivalence relation \quot{stably isomorphic} of \cite{jurco1} is given by \quot{1-isomorphic} in terms of the bicategory constructed here. These coincidences come from the equivalence between $(\act GH)$-bundles and so-called $G$-$H$-bundles used in \cite{jurco1,aschieri} expressed by Lemma \ref{crossedbundles}. In particular, in case of the automorphism 2-group $\mathrm{AUT}(H)$ of a connected Lie group $H$, a $\mathrm{AUT}(H)$-bundle gerbe is the same as a $H$-bibundle gerbe in the sense of Aschieri, Cantini and Jurco \cite{aschieri}.
\end{example}

\begin{example}
\label{ex:idmorphgrb}
Let $G$ be a Lie group, so that $\idmorph{G}$ is a Lie 2-group. Then, there is an equivalence of 2-categories
\begin{equation*}
\grb{{\idmorph{G}}}M \cong \idmorph{\bun{\mathcal{B}G}M}\text{.}
\end{equation*}
Indeed, if $\mathcal{G}$ is a $\idmorph G$-bundle gerbe over $M$, its principal $\idmorph G$-bundle over $Y^{[2]}$ is by Example \ref{ex:idmorphbundle} just a smooth map $\alpha: Y^{[2]} \to G$, and its bundle gerbe product degenerates to an equality $\pi_{23}^{*}\alpha \cdot \pi_{12}^{*}\alpha = \pi_{13}^{*}\alpha$ for functions on $Y^{[3]}$. In other words, a $\idmorph{G}$-bundle gerbe is the same as a so-called \quot{$G$-bundle 0-gerbe}. These form a category that is equivalent to the one of ordinary principal $G$-bundles, as pointed out in  Section \ref{intro}.  
\end{example}


\begin{remark}
\label{re:1-morphisms}
There are two differences between the definitions given here (for $\Gamma = \mathcal{B}A$) and the ones of Murray et al. \cite{murray, murray2, stevenson1}. Firstly, we have a slightly  different  ordering of  tensor products of bundles. These orderings are not essential in the case of abelian groups because the tensor category of ordinary $A$-bundles is symmetric. In the non-abelian case, a consistent theory requires the conventions we have chosen here. Secondly, the definitions of 1-morphisms and 2-morphisms have been generalized step by step:
\begin{enumerate}
\item 
In \cite{murray}, 1-morphisms did not include a \emph{common} refinement, but rather required that the surjective submersion of one bundle gerbe refines
the other. This definition is too restrictive in the sense that e.g. $\ueins$-bundle gerbes are not classified by $\mathrm{H}^3(M,\Z)$, as intended.


\item
In \cite{murray2}, 1-morphisms were defined on the canonical refinement $Z := Y_1 \times_M Y_2$ of the surjective submersions of the bundle gerbes. This definition solves the previous problems concerning the classification of bundle gerbes, but makes the composition of 1-morphisms quite involved \cite{stevenson1}. 


\item
In \cite{waldorf1}, 1-morphisms were defined on refinements $\zeta: Z \to Y_1 \times_M Y_2$. This generalization allows the same elegant definition of composition we have given here, and results in the same isomorphism classes of bundle gerbes. Moreover, 2-morphisms are defined with \emph{commutative} diagrams \erf{diag:refinement} -- this makes the structure of the bicategory outmost simple (see Remark \ref{rem:2morphisms}). 
\begin{comment}
However, the identity 1-morphisms look slightly more complicated since a cover $Y$ is not a refinement of $Y \times_M Y$.
\end{comment}


\item
In the present article we have allowed for a yet more general refinement in the definition of 1-morphisms. Its achievement is that bundle gerbes come out as an example of a more general concept -- the plus construction -- and we get e.g. Theorem \ref{th:stack} for free.  

\end{enumerate}
Despite these different definitions of 1-morphisms and 2-morphisms, the resulting bicategories of $\mathcal{B}A$-bundle gerbes in 2., 3. and 4. are all equivalent (see \cite[Theorem 1]{waldorf1}, \cite[Remark 4.5]{nikolaus2} and Lemma \ref{lem:canonicalrefinement} below). 
\end{remark}




\subsection{Properties of Groupoid Bundle Gerbes}


\label{sec:gerbeprop}

We recall that a homomorphism
 $\Lambda: \Gamma \to \Omega$ between Lie 2-groups is an anafunctor together with a transformation \erf{eq:lie2grouphom} describing its compatibility with the multiplications. We recall further from Proposition \ref{extensionstackmorphism} that   extension along $\Lambda$ is a 1-morphism
\begin{equation*}
\Lambda: \bun{\Gamma}- \to \bun\Omega-
\end{equation*}
between monoidal stacks over smooth manifolds.
That is, extension along $\Lambda$ is compatible with pullbacks, tensor products, and morphisms between principal $\Gamma$-bundles. Applying it to the principal $\Gamma$-bundle $P$ of a $\Gamma$-bundle gerbe $\mathcal{G}$, and also to the bundle gerbe product $\mu$, we obtain immediately an $\Omega$-bundle gerbe $\Lambda\mathcal{G}$. The same is evidently true for morphisms and 2-morphisms. Summarizing,
we get:
\begin{proposition}
\label{grbextension}
Extension of bundle gerbes along a homomorphism $\Lambda: \Gamma \to \Omega$ between Lie 2-groups defines a 1-morphism
\begin{equation*}
\Lambda: \grb\Gamma- \to \grb\Omega-
\end{equation*}
of 2-stacks over smooth manifolds. 
\end{proposition}

We recall that a weak equivalence between Lie 2-groups is a homomorphism $\Lambda: \Gamma \to \Omega$ that is a weak equivalence (see Definition \ref{defweak}). We have:

\begin{theorem}\label{extequiv}
Suppose $\Lambda: \Gamma \to \Omega$ is a weak equivalence between Lie 2-groups. Then, the 1-morphism $\Lambda: \grb\Gamma- \to \grb\Omega-$ of Proposition \ref{grbextension} is an equivalence of 2-stacks.
\end{theorem}
\begin{proof}
The monoidal equivalence  $\Lambda:\bun\Gamma- \to \bun\Omega-$ between the monoidal stacks (Corollary \ref{co:extensionweakequivalence2groups})
induces an equivalence
$\triv\grb\Gamma M \to \triv\grb\Lambda M$ between pre-2-stacks. Since the plus construction is functorial, this induces in turn the claimed  equivalence of 2-stacks.
\end{proof}


Next we generalize a couple of well-known results from abelian to non-abelian bundle gerbes. We define a \emph{refinement} of a surjective submersion $\pi:Y \to M$ to be another surjective submersion $\omega: W \to M$ together with a smooth map $f:W \to Y$ such that $\zeta = \pi \circ f$.
Notice that such a refinement induces smooth maps $f_k: W^{[k]} \to Y^{[k]}$ that commute with the various projections $\omega_{i_1...i_k}$ and $\pi_{i_1...i_k}$. 


\begin{lemma}
\label{lem:nonstablemorphisms}
Suppose $\mathcal{G}_1 = (Y_1,P_1,\mu_1)$ and $\mathcal{G}_2=(Y_2,P_2,\mu_2)$ are $\Gamma$-bundle gerbes over $M$, $f: Y_1 \to Y_2$ is a refinement of surjective submersions, and $\varphi: f_2^{*}P_2 \to P_1$ is an isomorphism of $\Gamma$-bundles over $Y_1^{[2]}$ that is compatible with the bundle gerbe products $\mu_1$ and $\mu_2$ in the sense that the diagram
\begin{equation*}
\alxydim{@=1.3cm}{\pi_{23}^{*}f_2^{*}P_2 \otimes \pi_{12}^{*}f_2^{*}P_2 \ar[d]_{\pi_{23}^{*}\varphi \otimes \pi_{12}^{*}\varphi} \ar[r]^-{f_3^{*}\mu} & \pi_{13}^{*}f_2^{*}P_2 \ar[d]^{\pi_{13}^{*}\varphi} \\ \pi_{23}^{*}P_1 \otimes \pi_{12}^{*}P_1 \ar[r]_-{\mu} & \pi_{13}^{*}P_1}
\end{equation*}
is commutative. Then, $\mathcal{G}_1$ and $\mathcal{G}_2$ are isomorphic.
\end{lemma}

The proof works just the same way as in the abelian case: one constructs the 1-isomorphism over the  common refinement $Z := Y_1 \times_M Y_2$ in a straightforward way. 
\begin{comment}
\begin{proof}
We construct an isomorphism $\mathcal{S}_{f,\varphi}: \mathcal{G}_1 \to \mathcal{G}_2$ based on the common refinement $Z := Y_1 \times_M Y_2$ with the evident projections to $Y_1$ and $Y_2$. Consider the smooth maps 
\begin{eqnarray*}
f' : Z \to Y_2^{[2]} &:& (y_1,y_2) \mapsto (f(y_2),y_2)
\\
f_1' : Z^{[2]} \to Y_2^{[3]} &:& ((y_1,y_2),(y_1',y_2')) \mapsto (f(y_1),y_2,y_{2}')
\\
f_2' : Z^{[2]} \to Y_2^{[3]} &:& ((y_1,y_2),(y_1',y_2')) \mapsto (f(y_1),f(y_1'),y_2')\text{.}
\end{eqnarray*}
The principal $\Gamma$-bundle of $\mathcal{S}_{f,\varphi}$ is $Q := f'^{*}P_2$, and the isomorphism is
\begin{equation*}
\alxydim{@C=1.5cm}{P_2 \otimes f'^{*}P_2  \ar[r]^-{f_1'^{*}\mu_2} & f'^{*}P_2 \ar[r]^-{f_2'^{*}\mu_2^{-1}} & f'P_2 \otimes f_2^{*}P_2 \ar[r]^-{\id \otimes \varphi} & f'^{*}P_2 \otimes P_1\text{.} }
\end{equation*}
Over a point $(y_1,y_2),(y_1',y_2')$, this is:
\begin{equation*}
\alxydim{@C=1cm}{P_2|_{(y_2,y_2')} \otimes (f'^{*}P_2)_{(y_1,y_2)}   \ar[r]^-{f_1'^{*}\mu_2} & (f'^{*}P_2)_{(y_1,y_2')} \ar[d]^-{f_2'^{*}\mu_2^{-1}}\\ & (f'^{*}P_2)|_{y_1',y_2'} \otimes (f_2^{*}P_2)_{(y_1,y_1')} \ar[r]^-{\id \otimes \varphi} & (f'^{*}P_2)_{(y_1',y_2')} \otimes P_1|_{y_1,y_1'}\text{.} }
\end{equation*}
Its axiom follows from the associativity of $\mu_2$ and the compatibility of $\varphi$ with $\mu_1$ and $\mu_2$.
\end{proof}
\end{comment}
As a consequence of Lemma \ref{lem:nonstablemorphisms} we have

\begin{proposition}
\label{prop:pullback}
Let $\mathcal{G} = (Y,P,\mu)$ be a $\Gamma$-bundle gerbe over $M$, and let $f:W \to Y$ be a refinement of its surjective submersion $\pi:Y \to M$. Then, $(W,f_2^{*}P,f_3^{*}\mu)$
is a $\Gamma$-bundle gerbe over $M$, and is isomorphic to $\mathcal{G}$.
\end{proposition}


\begin{comment}
\begin{definition}
The isomorphism $\mathcal{S}_{f}: \mathcal{G}^{f} \to \mathcal{G}$ from the proof of Lemma \ref{lem:nonstablemorphisms} is called the \emph{refinement isomorphism} associated to the refinement $f$.
\end{definition}
\end{comment}



\begin{lemma}
\label{lem:buntriv}
Let $\mathcal{G}=(Y,P,\mu)$ be a $\Gamma$-bundle gerbe over $M$. Then, there exist unique smooth maps $i: P \to P$ and $t: Y \to P$ such that
\begin{enumerate}[(i)]
\item 
the diagrams
\begin{equation*}
\alxydim{@=1.3cm}{P \ar[r]^{i} \ar[d]_{\chi} & P \ar[d]^{\chi} \\ Y^{[2]} \ar[r]_{\mathrm{flip}} & Y^{[2]}}
\quand
\alxydim{@=1.3cm}{& P \ar[d]^{\chi} \\ Y \ar[r]_-{\mathrm{diag}} \ar[ur]^{t} & Y^{[2]}}
\end{equation*}
are commutative.

\item
the map 
$t$ is neutral with respect to the bundle gerbe product $\mu$, i.e.
\begin{equation*}
\mu(t(y_{2}),p) = p = \mu(p,t(y_{1}))\text{.}
\end{equation*}
for all $p \in P$ with $\chi(p)=(y_1,y_2)$.


\item
the map $i$ provides inverses with respect to the bundle gerbe product $\mu$, i.e.
\begin{equation*}
\mu(i(p),p) = t(y_{1})
\quand
\mu(p,i(p)) = t(y_2)
\end{equation*}
for all $p\in P$ with $\chi(p)=(y_1,y_2)$.
\end{enumerate}
Moreover, 
$\alpha(t(y))=1$ and $\alpha(i(p)) = \alpha(p)^{-1}$
for all $p\in P$ and $y\in Y$.
\end{lemma}


\begin{proof}
Concerning uniqueness, suppose $(t,i)$ and $(t',i')$ are pairs of maps satisfying (i), (ii) and (iii). Firstly, we have $t'(y) = \mu(t(y),t'(y)) = t(y)$ and so $t=t'$. Then, $\mu(i(p),p)= t(y_1)=t'(y_1)=\mu(i'(p),p)$ implies $i(p)=i'(p)$, and so $i=i'$. In order to see the existence of $t$ and $i$, denote by $Q := \mathrm{diag}^{*}P$ the pullback of $P$ to $Y$,  denote by $Q^{\vee}$ the dual bundle and by $d: Q \otimes Q^{\vee} \to \trivlin_1$ the death map. Consider the smooth map
\begin{equation*}
\alxydim{@C=1cm}{Y \ar[r]^{s} & \trivlin_1 \ar[r]^-{d^{-1}} & Q \otimes Q^{\vee} \ar[rr]^-{\mu^{-1} \otimes \id_{Q^{\vee}}} && Q \otimes Q \otimes Q^{\vee} \ar[r]^-{\id \otimes d} & \trivlin_1 \otimes Q \cong Q \ar[r]^-{\mathrm{diag}} & P }
\end{equation*}
where $s:Y \to \trivlin_1$ is the canonical section
(see the proof of Lemma \ref{lem:loctriv}). It is straightforward to see that this satisfies the properties of the map $t$. Since all maps in the above sequence are (anchor-preserving) bundle morphisms, it is clear that $t \circ \alpha = 1$.  
\end{proof}



\begin{corollary}
\label{co:groupoidstructure}
Let $\mathcal{G}=(Y,P,\mu)$ be a $\Gamma$-bundle gerbe over $M$, and let $t$ and $i$ be the unique maps of Lemma \ref{lem:buntriv}. Then,
\begin{enumerate}[(i)]
\item
\label{co:groupoidstructure:cantriv}
$t$ is a section of $\mathrm{diag}^{*}P$, and defines a trivialization $\mathrm{diag}^{*}P \cong \trivlin_1$.  

\item
$i$ is a bundle isomorphism $i: P^{\vee} \to \mathrm{flip}^{*}P$.

\item 
$\mathcal{C}_0 := Y$ and $\mathcal{C}_1 := P$ define a Lie groupoid with source and target maps $\pi_1 \circ \chi$ and $\pi_2 \circ \chi$, respectively, composition $\mu$, identity $t$ and inversion $i$. \end{enumerate}
\end{corollary}

The following statement is well-known for abelian gerbes; the general version can be proved by a straightforward generalization of the constructions given in the proof of \cite[Proposition 3]{waldorf1}. 

\begin{lemma}
\label{lem:invertibility}
Every 1-morphism $\mathcal{A}: \mathcal{G} \to \mathcal{H}$ between $\Gamma$-bundle gerbes over $M$ is invertible. 
\end{lemma}


The last statement of this section shows a way to bring 1-morphisms and 2-morphisms into a simpler form (see Remark \ref{re:1-morphisms}). For bundle gerbes $\mathcal{G}_1$ and $\mathcal{G}_2$ with surjective submersions $\pi_1:Y_1 \to M$ and $\pi_2:Y_2 \to M$ we denote by $\hom {\mathcal{G}_1}{\mathcal{G}_2}$ the Hom-category in the bicategory $\grb\Gamma M$, and by $\hom {\mathcal{G}_1}{\mathcal{G}_2}^{FP}$ the category  whose objects are those 1-morphisms whose common refinement is $Z := Y_1 \times_M Y_2$, and whose 2-morphisms are those 2-morphisms whose refinement is $W := Y_1 \times_M Y_2$ with the maps $r,r': W \to Z$ the identity maps. 





\begin{lemma}
\label{lem:canonicalrefinement}
The inclusion
$\hom {\mathcal{G}_1}{\mathcal{G}_2}^{FP} \to  \hom {\mathcal{G}_1}{\mathcal{G}_2}$
is an equivalence of categories.
\end{lemma}

\begin{proof}
First we show that it is essentially surjective. We assume $\mathcal{A}: \mathcal{G}_1 \to \mathcal{G}_2$ is a general 1-morphism with a principal $\Gamma$-bundle $Q$ over a common refinement $Z$ of the surjective submersions $\pi_1:Y_1 \to M$ and $\pi_2:Y_2 \to M$ of the two bundle gerbes. We look at the principal $\Gamma$-bundle
\begin{equation*}
\tilde Q := \kappa_2^{*}P_2 \otimes \mathrm{pr}_2^{*}Q \otimes \kappa_1^{*}P_1
\end{equation*}
over $\tilde Z := Y_1 \times_M Z \times_M Y_2$, where 
\begin{equation*}
\kappa_1: \tilde Z \to Y_1^{[2]}: (y_1,z,y_2) \mapsto (y_1,y_1(z))
\;\text{ and }\;
\kappa_2: \tilde Z \to Y_2^{[2]}: (y_1,z,y_2) \mapsto (y_2(z),y_2)\text{.}
\end{equation*}
The projection $\mathrm{pr}_{13}: \tilde Z \to Y_1 \times_M Y_2$ is a surjective submersion, and over
 $\tilde Z \times_{Y_1 \times_M Y_2} \tilde Z$ we have a bundle morphism
$\alpha : \mathrm{pr}_1^{*}\tilde Q \to \mathrm{pr}_2^{*}\tilde Q$
defined over a point $(\tilde z,\tilde z')$ with $\tilde z = (y_1,z,y_2)$ and $\tilde z' = (y_1,z',y_2)$ by
\begin{equation*}
\alxydim{@R=0.6cm}{\tilde Q_{\tilde z} \ar@{=}[r] & P_2|_{y_2(z),y_2} \otimes Q_{z} \otimes P_1|_{y_1,y_1(z)} \ar[d]^-{\mu_2^{-1} \otimes \id \otimes \id} \\ & P_2|_{y_2(z'),y_2} \otimes P_2|_{y_2(z),y_2(z')} \otimes Q_{z} \otimes P_1|_{y_1,y_1(z)} \ar[d]^{\id \otimes \beta \otimes \id}  \\ & P_2|_{y_2(z'),y_2} \otimes Q_{z'} \otimes P_1|_{y_1(z),y_1(z')} \otimes P_1|_{y_1,y_1(z)} \ar[d]^{ \id \otimes \id \otimes \mu_1}  \\ &  P_2|_{y_2(z'),y_2} \otimes Q_{z'} \otimes P_1|_{y_1,y_1(z')} \ar@{=}[r] & \tilde Q_{\tilde z'}\text{.} }
\end{equation*}
The compatibility condition \erf{compgerbemorph} implies a cocycle condition for $\alpha$ over the three-fold fibre product of $\tilde Z$ over $Y_1 \times_M Y_2$, and since principal $\Gamma$-bundles form a stack, the pair $(\tilde Q,\alpha)$ defines a principal $\Gamma$-bundle $Q^{FP}$ over $Z^{FP} := Y_1 \times_M Y_2$. It is now straightforward to show that the bundle isomorphism $\beta$ itself descends to a bundle isomorphism $\beta^{FP}$ over $Z^{FP} \times_M Z^{FP}$ in such a way that the triple $(Z^{FP},Q^{FP},\beta^{FP})$ forms a 1-morphism $\mathcal{A}^{FP}: \mathcal{G}_1 \to \mathcal{G}_2$.


In order to show that $\mathcal{A}^{FP}$ is an essential preimage of $\mathcal{A}$, it remains to construct a 2-morphism $\varphi_{\mathcal{A}}^{FP}\maps  \mathcal{A} \Rightarrow \mathcal{A}^{FP}$. In the terminology of Definition \ref{def2mor}, we choose $W = \tilde Z$ with $r := \mathrm{pr}_2:W \to Z$   and $r' := \mathrm{pr}_{13} : W \to Z^{FP}$. Note that diagram \erf{diag:refinement} does not commute. The maps $x_W: W \to Y_1^{[2]}$ and $y_W: W \to Y_2^{[2]}$ are given by $x_W = s \circ \kappa_1$ and $y_W = \kappa_2$, where $s: Y_1^{[2]} \to Y_1^{[2]}$ switches the factors. Now, the bundle isomorphism of the 2-morphism $\varphi_{\mathcal{A}}^{FP}$ we want to construct is a bundle isomorphism
\begin{equation*}
\varphi : y_W^{*}P_2 \otimes r^{*}Q \to \tilde Q \otimes x_W^{*}P_1
\end{equation*}
over $W$, and is fibrewise over a point $w=(y_1,z,y_2)$ given by
\begin{equation*}
\alxydim{@R=0.6cm}{P_2|_{y_2(z),y_2} \otimes Q_z \ar[r]^-{\id \otimes \id \otimes t^{-1}} & P_2|_{y_2(z),y_2} \otimes Q_z \otimes P_{y_1(z),y_1(z)} \ar[d]^{\id \otimes \id \otimes \mu_1^{-1}}   \\ & P_2|_{y_2(z),y_2} \otimes Q_z \otimes P_1|_{y_1,y_1(z)} \otimes P_1|_{y_1(z),y_1} \ar@{=}[r] & \tilde Q_{w} \otimes P_1|_{s(y_1,y_1(z))}\text{,}}
\end{equation*}
where $t$ is the trivialization of $\mathrm{diag}^{*}P$ of Corollary \ref{co:groupoidstructure}. The compatibility condition \erf{eq:comp2morphcomplicated} is straightforward to check. 


Now we show that the inclusion $\hom {\mathcal{G}_1}{\mathcal{G}_2}^{FP} \to  \hom {\mathcal{G}_1}{\mathcal{G}_2}$
is full and faithful. Since it is clearly faithful, it only remains to show that it is full. Given a morphism $\mathcal{A} \to \mathcal{A}' $ in $\hom {\mathcal{G}_1}{\mathcal{G}_2}$, i.e. a common refinement $W$ of $Y_1 \times_M Y_2$ with itself and a bundle morphism $\varphi$, we have to find a morphism in $\hom {\mathcal{G}_1}{\mathcal{G}_2}^{FP}$ such that the two morphisms are identified under the equivalence relation on bundle gerbe 2-morphisms. We denote the bundles over $Y_1 \times_M Y_2$ corresponding to $\mathcal{A}$ and $\mathcal{A}'$ by $Q$ and $Q'$. The refinement maps are denoted as before by $r=(s_1,s_2): W \to Y_1 \times_M Y_2$ and $r'= (t_1,t_2): W \to Y_1 \times_M Y_2$. Then we obtain an isomorphism
$r^*Q \to {r}^*Q'$ 
fibrewise over a point $w \in W$ by
\begin{equation}
\label{eq:morlong}
\alxydim{@=0.6cm}{
Q|_{s_1(w),s_2(w)} \ar[rr]^-{d^{-1} \otimes \id} & & 
P_2^\vee |_{s_2(w),t_2(w)} \otimes P_2|_{s_2(w),t_2(w)} \otimes Q|_{s_1(w),s_2(w)}\ar[d]^-{\id \otimes \varphi}&&  \\
&& P_2^\vee|_{s_2(w),t_2(w)} \otimes Q'|_{t_1(w),t_2(w)} \otimes P_1|_{s_1(w),t_1(w)} \ar[d]^-{\id \otimes \beta'^{-1}} &&\\
&& P_2^\vee|_{s_2(w),t_2(w)} \otimes P_2|_{s_2(w),t_2(w)} \otimes Q'|_{s_1(w),s_2(w)} \ar[rr]^-{d \otimes \id} && Q'|_{s_1(w),s_2(w)}
}\hspace{-1cm}
\end{equation}
where $d: P_2^\vee |_{s_2(w),t_2(w)} \otimes P_2|_{s_2(w),t_2(w)} \to \trivlin_1$ is the death map. One can use the compatibility condition for $\varphi$ to show that this morphism descends to a morphism $\psi: Q \to Q'$ which is a morphism in 
$\hom {\mathcal{G}_1}{\mathcal{G}_2}^{FP}$. The two morphisms $(W,\psi)$ and $(Y_1\times_MY_2,\varphi)$ are identified if their pullbacks to 
\begin{equation*}
W \times_{(Y_1 \times_M Y_2 \times_M Y_1 \times_M Y_2)} (Y_1 \times_M Y_2) = \{w \in W \mid r(w) = r'(w) \} =: W_0 
\end{equation*}
are equal. On the one side, the map $W_0 \to W$ is the inclusion and the map $W_0 \to Y_1 \times_M Y_2$ is equal to $r$. The pullback of $\psi$ along $r$ is by construction the map $r^*Q \to r^*Q'$ from \eqref{eq:morlong}. On the other side,  bundles $x^*_W P_1$ and $y^*_W P_2$ over $W_0$ have canonical trivializations (Lemma \ref{co:groupoidstructure} \erf{co:groupoidstructure:cantriv}) under which $\varphi$ becomes also equal to the morphism \eqref{eq:morlong}.
\end{proof}




\subsection{Classification by \v Cech Cohomology}



In this section we prove that Versions I (\v Cech $\Gamma$-1-cocycles) and III ($\Gamma$-bundle gerbes) are equivalent. For this purpose, 
we extract a \v Cech cocycle from a $\Gamma$-bundle gerbe $\mathcal{G}$ over $M$, and prove that this procedure defines a bijection on the level of equivalence classes (Theorem \ref{th:gerbesclass}). First we have to ensure the existence of appropriate open covers.

\begin{lemma}
\label{lem:goodcover}
For every $\Gamma$-bundle gerbe $\mathcal{G}=(Y,P,\mu)$ over $M$ there exists an open cover $\mathscr{U}=\left \lbrace U_i \right \rbrace_{i\in I}$ of $M $with sections $\sigma_i : U_i \to Y$, such that the principal $\Gamma$-bundles $(\sigma_{i} \times \sigma_j)^{*}P$ over $U_i \cap U_j$ are trivializable. \end{lemma}

\begin{proof}
One can choose an open cover such that the 2-fold intersections $U_i \cap U_j$ are contractible. Since every Lie 2-group is a crossed module $\act GH$ (Remark \ref{rem:crossedmodule}), and $\act GH$-bundles are ordinary $H$-bundles (Lemma \ref{actionbundles}), these  admit sections over contractible smooth manifolds. But a section is enough to trivialize the original $\Gamma$-bundle (Lemma \ref{lem:loctriv}).
\end{proof}


Let $\mathcal{G}$ be a $\Gamma$-bundle gerbe over $M$, and let $\mathscr{U} = \left \lbrace U_i \right \rbrace_{i\in I}$ be an open cover with the properties of Lemma \ref{lem:goodcover}. We denote by $M_\mathscr{U}$ the disjoint union of all the open sets $U_i$, and by $\sigma:M_{\mathscr{U}} \to Y$ the union of the sections $\sigma_i$. Then, $\sigma$ is a refinement of $\pi:Y \to M$, and we have a $\Gamma$-bundle gerbe $\mathcal{G}_{\mathscr{U},\sigma}$ that is isomorphic to $\mathcal{G}$ (Proposition \ref{prop:pullback}). 

The principal $\Gamma$-bundle $P_{ij}$ of $\mathcal{G}_{\mathscr{U},\sigma}$ over the component $U_i \cap U_j$ is by assumption trivializable. Thus there exists a trivialization
$t_{ij}: P_{ij} \to \trivlin_{f_{ij}}$
for  smooth functions $f_{ij}:U_i \cap U_j \to \Gamma_0$. We define an isomorphism $\mu_{ijk}$ between trivial bundles such that the diagram
\begin{equation*}
\alxydim{@=1.3cm}{P_{jk} \otimes P_{ij} \ar[r]^-{\mu} \ar[d]_{t_{jk} \otimes t_{ij}} & P_{ik} \ar[d]^{t_{ik}} \\ \trivlin_{f_{jk}} \otimes \trivlin_{f_{ij}} \ar[r]_-{\mu_{ijk}} & \trivlin_{f_{ik}}}
\end{equation*}
is commutative. Now we are in the situation of Lemma \ref{lem:nonstablemorphisms}, which implies that the $\Gamma$-bundle gerbe $\mathcal{G}_{\mathscr{U},\sigma,t} \df (M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ is still isomorphic to $\mathcal{G}$. 


Combining Lemma \ref{homsets} with Example \ref{ex:tensorproduct} \erf{ex:tensorproduct:trivial}, we see that the  isomorphisms $\mu_{ijk}$ correspond to smooth maps $g_{ijk}:U_i \cap U_j \cap U_k \to \Gamma_1$ such that $s(g_{ijk})=f_{jk} \cdot f_{ij}$ and $t(g_{ijk})=f_{ik}$. The associativity condition for $\mu_{ijk}$ implies moreover that
\begin{equation*}
g_{\alpha\gamma\delta} \circ (g_{\alpha\beta\gamma} \cdot \id_{f_{\gamma \delta}}) = 
g_{\alpha \beta \delta} \circ (\id_{f_{\alpha \beta}} \cdot g_{\beta \gamma \delta})\text{.}
\end{equation*}
Hence, the collection $\left \lbrace f_{ij},g_{ijk} \right \rbrace$ is a $\Gamma$-1-cocycle on $M$ with respect to the open cover $\mathscr{U}$. 

\begin{theorem}
\label{th:gerbesclass}
Let $M$ be a smooth manifold and let $\Gamma$ be a Lie 2-group. The above construction defines a bijection
\begin{equation*}
\bigset{3.7cm}{Isomorphism classes of $\Gamma$-bundle gerbes over $M$} \cong \h^1(M,\Gamma)\text{.}
\end{equation*}
\end{theorem}


\begin{proof}
We claim  that $\Gamma$-bundle gerbes $(M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ and $(M_{\mathscr{V}},\trivlin_{h_{ij}},\nu_{ijk})$ are isomorphic if and only if the corresponding $\Gamma$-1-cocycles are equivalent. This proves at the same time that the choices of open covers and sections we have made during the construction do not matter,  that the resulting map is well-defined on isomorphism classes, and that this map is injective. Surjectivity follows by assigning to a $\Gamma$-1-cocycle $(f_{ij},g_{ijk})$ with respect to some cover $\mathscr{U}$ the $\Gamma$-bundle gerbe $(M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ with $\mu_{ijk}$ determined by Lemma \ref{homsets}.

It remains to prove that claim. We assume $\mathcal{A}=(Z,Q,\alpha)$ is a 1-isomorphism between the $\Gamma$-bundle gerbes $(M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ and $(M_{\mathscr{V}},\trivlin_{h_{ij}},\nu_{ijk})$. Similarly to Lemma \ref{lem:goodcover} one can show that there exists a cover $\mathscr{W}$ of $M$ by open sets $W_i$ that refines both $\mathscr{U}$ and $\mathscr{V}$, and that allows smooth sections $\omega_i:W_i \to Z$ for which the $\Gamma$-bundle $\omega_i^{*}Q$ is trivializable. In the terminology of the above construction, choosing a trivialization $t: \omega^{*}Q \to \trivlin_{h_i}$ with smooth maps $h_i: W_i \to \Gamma_0$ over $M_{\mathscr{W}}$ converts the isomorphism $\alpha$ into smooth functions $s_{ij}: W_i \cap W_j \to \Gamma_1$ satisfying $s(s_{ij}) = g_{ij}' \cdot h_{i}$ and $t(s_{ij}) = h_{j} \cdot g_{ij}$. The compatibility diagram \erf{compgerbemorph} implies the remaining condition that makes $(h_{i},s_{ij})$ an equivalence between the $\Gamma$-2-cocycles $(f_{ij},g_{ijk})$ and $(f_{ij}',g_{ijk}')$.
\end{proof}
