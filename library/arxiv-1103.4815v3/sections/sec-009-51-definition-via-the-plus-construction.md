---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-009-51-definition-via-the-plus-construction
section_title: "Definition via the Plus Construction"
section_number: 5.1
pages: 21-27
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.985
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
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
