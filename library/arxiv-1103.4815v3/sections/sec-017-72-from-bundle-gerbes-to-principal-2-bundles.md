---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-017-72-from-bundle-gerbes-to-principal-2-bundles
section_title: "From Bundle Gerbes to Principal 2-Bundles"
section_number: 7.2
pages: 48-57
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.878
latex_coverage_ratio: 0.996
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{sec:reconstruction}


We now provide the data we will feed into Lemma \ref{lem:equivalence} in order to produce a 2-functor
$\mathscr{R}_M\maps \grb \Gamma M \to \zwoabun \Gamma M$
that is inverse to the 2-functor $\mathscr{E}_M$ constructed in the previous section. These data are:
\begin{enumerate}
\item 
A principal $\Gamma$-2-bundle $\mathscr{R}_\mathcal{G}$ for each $\Gamma$-bundle gerbe $\mathcal{G}$ over $M$.

\item
A 1-isomorphism $\mathcal{A}_{\mathcal{G}}: \mathcal{G} \to \mathscr{E}_M(\mathscr{R}_{\mathcal{G}})$ for each  $\Gamma$-bundle gerbe $\mathcal{G}$ over $M$.

\item
A 1-isomorphism $\mathscr{R}_{\mathcal{A}}: \mathcal{P} \to \mathcal{P}'$ and a 2-isomorphism $\eta_{\mathcal{A}}: \mathcal{A} \Rightarrow \mathscr{E}_M(\mathscr{R}_{\mathcal{A}})$ for all principal $\Gamma$-2-bundles $\mathcal{P},\mathcal{P}'$ over $M$ and all bundle gerbe 1-morphisms $\mathcal{A}: \mathscr{E}_M(\mathcal{P}) \to \mathscr{E}_M(\mathcal{P}')$. 


\end{enumerate}



\subsubsection{Construction of the principal $\Gamma$-2-bundle $\mathscr{R}_{\mathcal{G}}$}


 We assume that $\mathcal{G}$ consists of a surjective submersion $\pi:Y \to M$, a principal $\Gamma$-bundle $P$ over $Y^{[2]}$ and a bundle gerbe product $\mu$. Let $\alpha: P \to \Gamma_0$ be the anchor of $P$, and let $\chi: P \to Y^{[2]}$ be the bundle projection. 


The Lie groupoid $\mathcal{P}$ of the principal 2-bundle $\mathscr{R}_\mathcal{G}$ is defined by
\begin{equation*}
\mathcal{P}_0 := Y \times \Gamma_0
\quand
\mathcal{P}_1 := P \times \Gamma_0\text{;}
\end{equation*}
source map, target maps, and composition are given by, respectively,
\begin{multline}
\label{defbundlefromgerbe}
s(p,g):= (\pi_2(\chi(p)),g)
\quomma
t(p,g):=  (\pi_1(\chi(p)),\alpha(p)^{-1} \cdot g)
\quand 
(p_2,g_2) \circ (p_1,g_1) := (\mu(p_1 , p_2), g_1)\text{.}
\end{multline}
\begin{comment}
This is well-defined because
\begin{equation*}
s(\mu(p_1,p_2), g_1) = (\pi_2(\chi(\mu(p_1 , p_2))),g_1)= s(p_1,g_1)
\end{equation*}
and
\begin{equation*}
t(\mu(p_1,p_2), g_1) =  (\pi_1(\chi(\mu(p_1, p_2))),\alpha(p_2)^{-1}\alpha(p_1)^{-1}g_1) = t(p_2,g_2)
\end{equation*}
where we have used $\alpha(\mu(p_1 , p_2))=\alpha(p_1 , p_2)=\alpha(p_1)\alpha(p_2)$ from Definition \ref{def:tensorproduct} and the target-source matching condition $g_2=\alpha(p_1)^{-1}g_1$.
\end{comment}
The identity morphism of an object $(y,g) \in \mathcal{P}_0$ is $(t_y,g) \in \mathcal{P}_1$, where $t_{y}$ denotes the unit element in $P$ over the point $(y,y)$, see Lemma \ref{lem:buntriv}. The inverse of a morphism $(p,g) \in \mathcal{P}_1$ is $(i(p),\alpha(p)^{-1}g)$, where $i: P \to P$  is the map from Lemma \ref{lem:buntriv}.
\begin{comment}
Indeed, we have $s(\id_{(y,g)})= (\pi_2(t_y),g) = (y,g) = (\pi_1(t_y),\alpha(t_y)^{-1},g) = t(\id_{(y,g)})$. The axioms for an identity are
\begin{equation*}
(p,g) \circ \id_{s(p,g)} =(p,g) \circ  (t_{\pi_2(\chi(p))},g) = (\mu(t_{\pi_2(\chi(p))},p),g) = (p,g)
\end{equation*}
and
\begin{equation*}
\id_{t(p,g)} \circ (p,g)=(t_{\pi_1(\chi(p))},\alpha(p)^{-1}  g) \circ (p,g) = (\mu(p,t_{\pi_1(\chi(p))}),g)=(p,g)\text{.}
\end{equation*}

Concerning the inverses, we have
\begin{multline*}
s((p,g)^{-1}) = s(i(p), \alpha(p)^{-1}g) = (\pi_2(i(p)), \alpha(p)^{-1}g) \\= (\pi_1(p), \alpha(p)^{-1}g) = (\pi_1(p), \alpha(p)^{-1}g) = t(p,g)
\end{multline*}
and
\begin{equation*}
t((p,g)^{-1}) = t(i(p),\alpha(p)^{-1}g) = (\pi_1(i(p)), \alpha(i(p))^{-1}\alpha(p)^{-1}g) = (\pi_2(p),g) = s(p,g)\text{.}
\end{equation*}
The axioms for inverses are
\begin{equation*}
(p,g) \circ (i(p),\alpha(p)^{-1}g) = (\mu(i(p),p),\alpha(p)^{-1}g) = (t_{\pi_1(p)},\alpha(p)^{-1}g) = \id_{t(p,g)}
\end{equation*}
and
\begin{equation*}
(i(p),\alpha(p)^{-1}g) \circ (p,g) = (\mu(p,i(p)),g) = (t_{\pi_2(p)},g) = \id_{s(p,g)}\text{.}
\end{equation*}
\end{comment}
The bundle projection is $\pi(y,g) := \pi(y)$. The action is given on objects and morphisms by
\begin{equation}
\label{defaction}
R_0((y,g),g') := (y,gg')
\quand
R_1((p,g),\gamma) := \Big(p \circ \big(\id_{g} \cdot \gamma \cdot \id_{t(\gamma)^{-1}g^{-1}\alpha(p)}\big),g\cdot s(\gamma)\Big)\text{.}
\end{equation}

\begin{lemma}
\label{lem:action}
This defines a functor 
$R: \mathcal{P} \times \Gamma \to \mathcal{P}$, and $R$ is an action of $\Gamma$ on $\mathcal{P}$.
\end{lemma}

\begin{proof}
We assume that $t:H \to G$ is a smooth crossed module, and that $\Gamma$ is the Lie 2-group associated to it, see Example \ref{crossedmodule} and Remark \ref{rem:crossedmodule}. Then we use the correspondence between principal $\Gamma$-bundles and principal $H$-bundles with $H$-anti-equivariant maps to $G$ of Lemma \ref{actionbundles}.
Writing $\gamma = (h,g')$, we have
\begin{equation*}
R_1((p,g),\gamma) = (p \star \lw{g}{h},gg')\text{.}
\end{equation*}
\begin{comment}
Indeed, we have $s(\gamma)=g'$, $t(\gamma) = t(h)g'$ and 
\begin{equation*}
\id_{g} \cdot \gamma \cdot \id_{t(\gamma)^{-1}g^{-1}\alpha(p)} = (1,g) \cdot (h,g') \cdot (1,g'^{-1}t(h)^{-1}g^{-1}\alpha(p)) = (\lw{g}{h},t(\lw{g}{h^{-1}})\alpha(p)) \text{,}
\end{equation*}
and $p \star h$ was defined as $p \circ (h,t(h^{-1})\alpha(p))$, see Lemma \ref{actionbundles}. 
\end{comment}
With this simple formula at hand it is straightforward to show that $R$ respects source and target maps and satisfies the axiom of an action.  
\begin{comment}
Indeed, we have
\begin{multline*}
s(R((p,g),(h,g'))) = s(p \star \lw gh , gg') = (\pi_2(p \star \lw gh),gg') \\= (\pi_2(p),gg')= R((\pi_2(p),g),g') = R(s(p,g),s(h,g'))
\end{multline*}
and
\begin{eqnarray*}
t(R((p,g),(h,g'))) &=& t(p \star \lw gh , gg') \\&=& (\pi_1(p \star \lw gh),\alpha(p \star \lw gh)^{-1}gg')  \\ &=& (\pi_1(p), (t(\lw gh^{-1})\alpha(p))^{-1}gg') \\ &=& (\pi_1(p),\alpha(p)^{-1}(gt(h^{-1})g^{-1})^{-1}gg') \\ &=& R((\pi_1(p), \alpha(p)^{-1}g), t(h)g')
\\&=& R(t(p,g),t(h,g'))\text{.}
\end{eqnarray*}

Finally, we check that the functor $R$ is an action in the sense of Definition \ref{def:rightaction}. On objects this is trivial, and on morphisms we calculate \begin{eqnarray*}
R(R((p,g),(h_2,g_2')),(h_1,g_1')) 
&=& R((p \star \lw{g}h_2,gg_2'),(h_1,g_1'))\\
&=& (p \star (\lw g(h_2 \cdot \lw{g_2'}h_1)),gg_2'g_1')\\
&=& R((p,g), (h_2 \cdot \lw{g_2'}h_1,g_2'g_1'))\\
&=& R((p,g),(h_2,g_2') \cdot (h_1,g_1')) \text{.}
\end{eqnarray*}
\end{comment}
For the composition, we assume composable  $(p_2,g_2),(p_1,g_1) \in \mathcal{P}_1$, i.e. $g_2 = \alpha(p_1)^{-1}g_1$, and composable $(h_2,g_2'),(h_1,g_1') \in \Gamma_1$, i.e. $g_2' = t(h_1)g_1'$. Then we have
\begin{eqnarray*}
R((p_2,g_2) \circ (p_1,g_1),(h_2,g_2') \circ (h_1,g_1')) 
&=& R((\mu(p_1,p_2),g_1),(h_2h_1,g_1'))\\
&=& (\mu(p_1,p_2) \star \lw{g_1}{(h_2h_1)},g_1g_1')\\
&=& (\mu(p_1 \star \lw{g_1}{h_2},p_2) \star \lw{g_1}{h_1},g_1g_1')\\
&=& (\mu(p_1,p_2 \star \lw{g_2}{h_2}) \star \lw{g_1}{h_1},g_1g_1')\\
&=& (\mu(p_1\star \lw{g_1}{h_1},p_2 \star \lw{g_2}{h_2}) ,g_1g_1')\\
&=& (p_2 \star \lw{g_2}h_2,g_{2}g_{2}') \circ (p_1 \star \lw{g_1}h_1,g_1g_1')\\
&=& R((p_2,g_2),(h_2,g_2')) \circ R((p_1,g_1),(h_1,g_1'))\text{,}
\end{eqnarray*} 
finishing the proof.
\end{proof}


It is obvious that the action $R$ preserves the projection $\pi$. Thus,  in order to complete the construction of the principal 2-bundle  $\mathscr{R}_\mathcal{G}$  it  remains to show that the functor $\tau = (\mathrm{pr}_1,R)$ is a weak equivalence.
This is the content of the following two lemmata in connection with Theorem \ref{weak}.

\begin{lemma}
$\tau$ is smoothly essentially surjective. 
\end{lemma}

\begin{proof}
The condition we have to check is whether or not the map
\begin{equation*}
\alxydim{@C=2cm}{(Y \times \Gamma_0 \times \Gamma_0) \lli{\tau}\times_t ((P \times \Gamma_0) \times_M (P \times \Gamma_0)) \ar[r]^-{(s \times s) \circ \mathrm{pr}_2} & (Y \times \Gamma_0) \times_M (Y \times \Gamma_0)}
\end{equation*}
is a surjective submersion. The left hand side is diffeomorphic to $(P \times \Gamma_0) \lli{\pi_1} \times_{\pi_1} (P \times \Gamma_0)$ via $\mathrm{pr}_2$, so that this is equivalent to checking that
\begin{equation*}
s \times s: (P \times \Gamma_0) \lli{\pi_1 \circ \chi} \times_{\pi_1 \circ \chi} (P \times \Gamma_0) \to  (Y \times \Gamma_0) \times_M (Y \times \Gamma_0)
\end{equation*}
is a surjective submersion. Since the $\Gamma_0$-factors are just spectators, this is in turn equivalent to checking that
\begin{equation*}
(\pi_2 \times \pi_2) \circ (\chi \times \chi): P \lli{\pi_1 \circ \chi}\times_{\pi_1 \circ \chi} P \to Y^{[2]}
\end{equation*} 
is a surjective submersion. It fits into the pullback diagram
\begin{equation*}
\alxydim{@R=1.3cm}{P \lli{\pi_1 \circ \chi}\times_{\pi_1 \circ \chi} P \ar@{^(->}[r] \ar[d]_{\chi \times \chi} & P \times P \ar[d]^{\chi \times \chi} \\ Y^{[2]} \lli{\pi_1}\times_{\pi_1} Y^{[2]} \ar[d]_{\pi_2 \times \pi_2} \ar@{^(->}[r] & Y^{[2]} \times Y^{[2]} \ar[d]^{\pi_2 \times \pi_2} \\ Y^{[2]} \ar@{^(->}[r] & Y \times Y}
\end{equation*}
which has  a surjective submersion on the right hand side; hence, also the map on the left hand side must be a surjective submersion. 
\end{proof}

\begin{lemma}
$\tau$ is smoothly fully faithful. 
\end{lemma}

\begin{proof}
We assume a smooth manifold $N$ with two smooth maps 
\begin{equation*}
f: N \to (\mathcal{P}_0 \times \Gamma_0) \times (\mathcal{P}_0 \times \Gamma_0)
\quand
g: N \to \mathcal{P}_1 \times_M \mathcal{P}_1
\end{equation*}
such that the diagram
\begin{equation*}
\alxydim{@R=1.3cm}{N \ar[d]_{f} \ar[r]^-{g} & \mathcal{P}_1 \times_M \mathcal{P}_1 \ar[d]^{s \times t} \\  (\mathcal{P}_0 \times \Gamma_0) \times (\mathcal{P}_0 \times \Gamma_0) \ar[r]_-{\tau \times \tau} & (\mathcal{P}_0 \times_M \mathcal{P}_0) \times (\mathcal{P}_0 \times_M \mathcal{P}_0) }
\end{equation*}
is commutative. For a fixed point $n \in N$ we put 
\begin{equation*}
((p_1,g_1),(p_2,g_2)):= g(n)\in (P \times \Gamma_0) \times_M (P \times \Gamma_0)
\end{equation*}
and
\begin{equation*}
((y,g,\tilde g),(y',g',\tilde g')) := f(n) \in (Y \times \Gamma_0 \times \Gamma_0) \times (Y \times \Gamma_0 \times \Gamma_0)\text{.}
\end{equation*}
\begin{comment}
The condition that the diagram is commutative means
\begin{eqnarray*}
(y,g,y,g\tilde g) &=& (\pi_2(p_1),g_1,\pi_2(p_2),g_2) \\
(y',g',y',g'\tilde g') &=& (\pi_1(p_1), \alpha(p_1)^{-1}g_1,\pi_1(p_2),\alpha(p_2)^{-1}g_2)\text{.}
\end{eqnarray*}
\end{comment}
The commutativity of the diagram implies $\chi(p_1)=\chi(p_2)=(y',y)$, so that there exists  $\gamma' \in \Gamma_1$ with $p_2 = p_1 \circ \gamma'$. We define 
$\gamma := \id_{g_1^{-1}} \cdot \gamma'\cdot \id_{\alpha(p_2)^{-1}g_2}$, 
which yields a morphism $\gamma\in \Gamma_1$ satisfying $\tau(p_1,g_1,\gamma) = (p_1,g_1,p_2,g_2) = g(n)$. On the other hand, we check that 
\begin{equation*}
(s(p_1,g_1,\gamma), t(p_1,g_1,\gamma)) = (\pi_2(p_1),g_1,s(\gamma),\pi_1(p_1),\alpha(p_1)^{-1}g_1,t(\gamma))  = f(n)\text{,}
\end{equation*} 
using that $s(\gamma) = g_1^{-1}g_2$ and $t(\gamma) = g_1^{-1}\alpha(p_1)\alpha(p_2)^{-1}g_2$. Summarizing, we have defined a smooth map
\begin{equation*}
\sigma: N \to \mathcal{P}_1 \times \Gamma_1:n \mapsto (p_1,g_1,\gamma)
\end{equation*}
such that $\tau \circ \sigma = g$ and $(s \times t) \circ \sigma=f$. Now let $\sigma':N \to \mathcal{P}_1 \times \Gamma_1$ be another such map, and let $\sigma'(n) =: (p_1',g_1',\gamma')$. The condition that $\tau(\sigma(n)) =g(n) = \tau(\sigma'(n))$  shows immediately that $p_1=p_1'$ and $g_1=g_1'$, and then that $p_1 \circ \gamma = p_1 \circ \gamma'$. But since the $\Gamma$-action on $P$ is principal, we have $\gamma=\gamma'$. This shows $\sigma=\sigma'$.
Summarizing, $\mathcal{P}_1 \times \Gamma_1$ is a pullback. 
\begin{comment}
More precisely,
\begin{equation*}
\alxydim{}{\mathcal{P}_1 \times \Gamma_1 \ar[r]^{\tau} \ar[d]_{s \times t} & \mathcal{P}_1 \times_M \mathcal{P}_1 \ar[d]^{s \times t} \\  (\mathcal{P}_0 \times \Gamma_0) \times (\mathcal{P}_0 \times \Gamma_0) \ar[r]_-{\tau \times \tau} & (\mathcal{P}_0 \times_M \mathcal{P}_0) \times (\mathcal{P}_0 \times_M \mathcal{P}_0) }
\end{equation*}
is a pullback diagram.
\end{comment}
\end{proof}




\begin{example}
\label{trans_abelian}
Suppose $\Gamma = \mathcal{B}\ueins$ (see Example \ref{example_groupoids} \erf{exBG}) and suppose $\mathcal{G}$ is a $\Gamma$-bundle gerbe over $M$, also known as a $\ueins$-bundle gerbe, see Example \ref{ex:abelianbundlegerbes}. Then, the associated principal $\mathcal{B}\ueins$-2-bundle $\mathscr{R}_\mathcal{G}$ has the  groupoid $\mathcal{P}$ with $\mathcal{P}_0=Y$ and $\mathcal{P}_1=P$, source and target maps $s = \pi_2 \circ \chi$ and $t=\pi_1 \circ \chi$, and composition $p_2 \circ p_1 = \mu(p_1,p_2)$. The action of $\mathcal{B}\ueins$ on $\mathcal{P}$ is trivial on the level of objects and the given $\ueins$-action on $P$ on the level of morphisms. The same applies for general abelian Lie groups $A$ instead of $\ueins.$
\end{example}



\subsubsection{Construction of the 1-isomorphism $\mathcal{A}_{\mathcal{G}}: \mathcal{G} \to \mathscr{E}_M(\mathscr{R}_{\mathcal{G}})$}


The $\Gamma$-bundle gerbe $\mathscr{E}_M(\mathscr{R}_\mathcal{G})$ has the surjective submersion $\tilde Y := Y \times \Gamma_0$ with $\tilde\pi(y,g) := \pi(y)$. The total space of its $\Gamma$-bundle $\tilde P$ is $\tilde P := P \times \Gamma_0 \times \Gamma_0$; it has the anchor $\alpha(p,g,h)= h$, the bundle projection
\begin{equation*}
\tilde\chi: \tilde P \to \tilde Y^{[2]}: (p,g,h) \mapsto (  (\pi_1(\chi(p)),\alpha(p)^{-1}  g),(\pi_2(\chi(p)),gh^{-1}))\text{,}
\end{equation*}
 the $\Gamma$-action is
\begin{eqnarray*}
(p,g,h) \circ \gamma 
&\stackrel{\text{\erf{defgerbefrombundle}}}{=}&  ((p,g) \circ R((t_{\pi_2(\chi(p))},gh^{-1}),\gamma),s(\gamma))
 \\&\stackrel{\text{\erf{defaction}}}{=}& ((p,g) \circ (t_{\pi_2(\chi(p))} \circ (\id_{gh^{-1}} \cdot \gamma \cdot \id_{g^{-1}}),gh^{-1} s(\gamma)),s(\gamma))
 \\&\stackrel{\text{\erf{defbundlefromgerbe}}}{=}& (\mu (t_{\pi_2(\chi(p))} \circ \big(\id_{gh^{-1}} \cdot \gamma \cdot \id_{g^{-1}}\big),p),gh^{-1} s(\gamma),s(\gamma))
 \\&\stackrel{\text{\erf{deftensorproductrel}}}{=}& (p \circ \big(\id_{gh^{-1}} \cdot \gamma \cdot \id_{g^{-1}\alpha(p)}\big),gh^{-1} s(\gamma),s(\gamma))\text{,}
\end{eqnarray*}
 and its bundle gerbe product $\tilde\mu$ is given by
\begin{eqnarray*}
\tilde\mu((p_{23},g_{23},h_{23}),(p_{12},g_{12},h_{12})) 
&\stackrel{\text{\erf{defmu}}}{=}&   ((p_{12},g_{12}) \circ R((p_{23},g_{23}),\id_{h_{12}}) ,h_{23}h_{12})
\\&\stackrel{\text{\erf{defaction}}}{=}& ((p_{12},g_{12}) \circ (p_{23},g_{23}h_{12}) ,h_{23}h_{12})
\\&\stackrel{\text{\erf{defbundlefromgerbe}}}{=}&   (\mu(p_{23},p_{12}),g_{23}h_{12} ,h_{23}h_{12})\text{.}
\end{eqnarray*}
In order to compare the bundle gerbes $\mathcal{G}$ and $\mathscr{E}_M(\mathscr{R}_\mathcal{G})$ we consider the smooth maps  $\sigma: Y \to Y \times \Gamma_0$ and $\tilde\sigma: P \to \tilde P$  that are defined  by $\sigma(y):=(y,1)$ and $\tilde\sigma(p) := (p,\alpha(p),\alpha(p))$. 

\begin{lemma}
$\tilde\sigma$ defines an isomorphism $\tilde\sigma: P \to (\sigma \times \sigma)^{*}\tilde P$ of $\Gamma$-bundles over $Y^{[2]}$. Moreover, the diagram
\begin{equation*}
\alxydim{@C=1.4cm@R=1.3cm}{\pi_{23}^{*}P \otimes \pi_{12}^{*}P \ar[d]_{\mu} \ar[r]^{\tilde\sigma \otimes \tilde\sigma} & \tilde\pi_{23}^{*}\tilde P  \otimes \tilde\pi_{12}^{*}\tilde P \ar[d]^{\tilde\mu} \\ \pi_{13}^{*}P \ar[r]_{\tilde\sigma} & \tilde\pi_{13}^{*}\tilde P}
\end{equation*}
is commutative.
\end{lemma}


\begin{proof}
For the first part it suffices to prove that $\tilde\sigma$ is $\Gamma$-equivariant, preserves the anchors, and that the diagram
\begin{equation*}
\alxydim{@R=1.3cm}{P \ar[d]_{\chi} \ar[r]^{\tilde\sigma} & \tilde P \ar[d]^{\tilde\chi} \\ Y^{[2]} \ar[r]_{\sigma \times \sigma} & \tilde Y^{[2]}}
\end{equation*}
is commutative. Indeed, the commutativity of the diagram is obvious, and also that the anchors are preserved. For the $\Gamma$-equivariance, we have
\begin{equation*}
\tilde\sigma(p \circ \gamma) = (p \circ \gamma, s(\gamma), s(\gamma)) = (p,\alpha(p),\alpha(p)) \circ \gamma= \tilde\sigma(p) \circ \gamma\text{.}
\end{equation*}  
Finally, we calculate
\begin{eqnarray*}
\tilde\mu((p_{23},\alpha(p_{23}),\alpha(p_{23})),(p_{12},\alpha(p_{12}),\alpha(p_{12}))) &=& (\mu(p_{23},p_{12}),\alpha(p_{23})\alpha(p_{12}) ,\alpha(p_{23})\alpha(p_{12}))
\\&=& (\mu(p_{23},p_{12}),\alpha(\mu(p_{23},p_{12})),\alpha(\mu(p_{23},p_{12})))
\end{eqnarray*}
which shows the commutativity of the diagram.
\end{proof}

Via Lemma \ref{lem:invertibility}  the bundle morphism $\tilde\sigma$ defines the required 1-morphism $\mathcal{A}_{\mathcal{G}}$, and Lemma \ref{lem:nonstablemorphisms} guarantees that $\mathcal{A}_{\mathcal{G}}$ is  a 1-\emph{iso}morphism.



\subsubsection{Construction of the 1-morphism $\mathscr{R}_{\mathcal{A}}: \mathcal{P} \to \mathcal{P}'$}

Let $\mathcal{A}: \mathscr{E}_M(\mathcal{P}) \to \mathscr{E}_M(\mathcal{P}')$ be a 1-morphism between $\Gamma$-bundle gerbes obtained from principal $\Gamma$-2-bundles $\mathcal{P}$ and $\mathcal{P}'$ over $M$.
By Lemma \ref{lem:canonicalrefinement} we can assume that $\mathcal{A}$ consists of a principal $\Gamma$-bundle $\chi:Q\to Z$ with $Z=\mathcal{P}_0 \times_M \mathcal{P}_0'$, and some isomorphism $\beta$ over $Z^{[2]}$. For preparation,
we consider the fibre products $Z_r:= \mathcal{P}_0 \times_M \mathcal{P}_0'^{[2]}$ and $Z_l := \mathcal{P}_0^{[2]} \times_M \mathcal{P}_0'$ with the obvious embeddings $\iota_l: Z_l \to Z$ and $\iota_r: Z_r \to Z$ obtained by doubling elements. Together with the trivialization of Corollary \ref{co:groupoidstructure}, the pullbacks of $\beta$ along $\iota_l$ and $\iota_r$ yield bundle morphisms
\begin{equation*}
\beta_l := \iota_l^{*}\beta : \mathrm{pr}_{13}^{*}Q \to \mathrm{pr}_{23}^{*}Q \otimes \mathrm{pr}_{12}^{*}P
\quand
 \beta_r := \iota_r^{*}\beta : \mathrm{pr}_{23}^{*}P' \otimes \mathrm{pr}_{12}^{*}Q \to \mathrm{pr}_{13}^{*}Q\text{,}
\end{equation*}
where $P := \mathcal{P}_1 \times \Gamma_0$ and $P' := \mathcal{P}' \times \Gamma_0$ are the principal $\Gamma$-bundles of the $\Gamma$-bundle gerbes $\mathscr{E}_M(\mathcal{P})$ and $\mathscr{E}_M(\mathcal{P}')$, respectively. \begin{comment}
Over points $(p,p_1',p_2') \in Z_r$ and $(p_1,p_2,p') \in Z_l$, the bundle morphisms $\beta_r$ and $\beta_l$ are fibrewise like
\begin{equation*}
\beta_l: Q_{p_1,p'} \to Q_{p_2,p'} \otimes P_{p_1,p_2}
\quand
\beta_r: P'_{p_1',p_2'} \otimes Q_{p,p_1'} \to Q_{p,p_2'}\text{.}
\end{equation*}
\end{comment}

\begin{lemma}
\label{lem:betaprop}
The bundle morphisms $\beta_l$ and $\beta_r$ have the following properties:
\begin{enumerate}[(i)]
\item 
They commute with each other in these sense that the diagram
\begin{equation*}
\alxydim{@C=1.7cm@R=1.3cm}{P'_{p_1',p_2'} \otimes Q_{p_1,p_1'} \ar[dr]|{\beta}  \ar[r]^-{\beta_r } \ar[d]_{\id \otimes \beta_l} & Q_{p_1,p_2'} \ar[d]^{\beta_l} \\ P'_{p_1',p_2'} \otimes Q_{p_2,p_1'} \otimes P_{p_1,p_2} \ar[r]_-{\beta_r \otimes \id} & Q_{p_2,p_2'} \otimes P_{p_1,p_2}}
\end{equation*}
is commutative for all $((p_1,p_1'),(p_2,p_2')) \in Z^{[2]}$. 

\item
$\beta_l$ is compatible with the bundle gerbe product $\mu$ in the sense that
\begin{equation*}
\beta_l|_{p_1,p_3,p'} = (\id \otimes \mu_{p_1,p_2,p_3}) \circ (\beta_l|_{p_2,p_3,p'} \otimes \id) \circ \beta_l|_{p_1,p_2,p'}
\end{equation*}
for all $(p_1,p_2,p_3,p')\in \mathcal{P}_0^{[3]} \times_M \mathcal{P}_0'$.

\item
$\beta_r$ is compatible with the bundle gerbe product $\mu'$ in the sense that
\begin{equation*}
\beta_r|_{p,p_1',p_3'} \circ (\mu'_{p_1',p_2',p_3'} \otimes \id)  = \beta_r|_{p,p_2',p_3'} \circ (\id \otimes \beta_r|_{p,p_1',p_2'})
\end{equation*}
for all $(p,p_1',p_2',p_3')\in \mathcal{P}_0 \times_M \mathcal{P}_0'^{[3]}$.

\end{enumerate}
\end{lemma}

\begin{proof}
The identities (ii) and (iii) follow by restricting the commutative diagram \erf{compgerbemorph} to the submanifolds $\mathcal{P}_0^{[3]} \times_M \mathcal{P}_0'$ and $\mathcal{P}_0 \times_M \mathcal{P}_0'^{[3]}$  of $Z^{[3]}$, respectively. Similarly, the commutativity of the two triangular subdiagrams in (i) follows by restricting \erf{compgerbemorph} along appropriate embeddings $Z^{[2]} \to Z^{[3]}$.
\end{proof}

Now we are in position to define the anafunctor $\mathscr{R}_{\mathcal{A}}$. First, we consider the left action
\begin{equation*}
\beta_0: \Gamma_0 \times Q \to Q : (g,q) \mapsto \beta_r((\id,g),q)
\end{equation*}
that satisfies $\alpha(\beta_0(g,q)) = g\alpha(q)$. 
\begin{comment}
If $\chi(q)=(p,p')$, then $\chi(\id_{p'},g) = (p',R(p',g^{-1})) $ and $\chi(\beta_0(g,q)) = (p,R(p',g^{-1}))$. We have
\begin{multline*}
\beta_0(g_2,\beta_0(g_1,q)) = \beta_r((\id,g_2),\beta_r((\id,g_1),q)) \stackrel{\text{(iii)}}{=} \beta_r(\mu'((\id,g_2),(\id,g_1)),q)\\=\beta_r((\id,g_2g_1),q)=\beta_0(g_2g_1,g). \end{multline*}
\end{comment}
The action $\beta_0$ is properly discontinuous and free because $\beta_r$ is a bundle isomorphism. 
The quotient $F := Q/\Gamma_0$ is the total space of the anafunctor $\mathscr{R}_{\mathcal{A}}$ we want to construct. Left and right anchors of an element $q\in F$ with $\chi(q)=(p,p')$ are given by 
\begin{equation*}
\alpha_l(q) := p
\quand
\alpha_r(q) := R(p',\alpha(q))\text{.}
\end{equation*}
\begin{comment}
This is well-defined under the action of $\beta_0$; for $\alpha_l$ this is clear and for $\alpha_r$ this is
\begin{equation*}
\alpha_r(\beta_0(g,q)) = R(R(p',g^{-1}),\alpha(\beta_0(g,q))) = R(p',g^{-1}g\alpha(q))=\alpha_r(q)\text{.}
\end{equation*}
\end{comment}
The actions are  defined by
\begin{equation*}
\rho_l(\rho, q) := \beta_l^{-1}(q,(\rho,1))
\quand
\rho_r(q , \rho') := \beta_r((R(\rho',\id_{\alpha(q)^{-1}}),1),q)\text{.}
\end{equation*}
The left action is invariant under the action $\beta_0$ because of Lemma \ref{lem:betaprop} (i). For the right action, invariance follows from Lemma \ref{lem:betaprop} (ii) and the identity
\begin{equation*}
\mu'((R(\rho',\id_{\alpha(q)^{-1}g^{-1}}),1),(\id,g)) \stackrel{\text{\erf{defmu}}}{=}  \mu'((\id,g),(R(\rho',\id_{\alpha(q)^{-1}}),1))\text{.}
\end{equation*}

\begin{lemma}
The above formulas  define an anafunctor $F : \mathcal{P} \to \mathcal{P}'$.
\end{lemma}


\begin{proof}
The compatibility between anchors and actions is easy to check. The axiom for the actions $\rho_l$ and $\rho_r$ follows from Lemma \ref{lem:betaprop} (ii) and (iii). Lemma \ref{lem:betaprop} (i) shows that the actions commute.
It remains to prove that $\alpha_l: F \to \mathcal{P}_0$ is a principal $\mathcal{P}'$-bundle. Since $\alpha_l$ is a composition of surjective submersions, we only have to show that the map
\begin{equation*}
\tau: F \lli{\alpha_r} \times_{t} \mathcal{P}' \to F \lli{\alpha_l} \times_{\alpha_l} F : (q,\rho') \mapsto (q, \rho_r(q ,\rho'))
\end{equation*} 
is a diffeomorphism. We construct an inverse map $\tau^{-1}$ as follows. For $(q_1,q_2)$ with $\chi(q_1) = (p,p')$ and $\chi(q_2)\eq (p,\tilde p')$, choose a representative \begin{equation*}
((\tilde\rho',g'),\tilde q) := \beta_r|_{p,p',\tilde p'}^{-1}(q_2)\text{.}
\end{equation*}
Such choices can be made locally in a smooth way, and the result will not depend on them. We have $\chi(\tilde q) = (p,p')$ that that there exists a unique $\gamma \in \Gamma_1$ such that $q_1 = \tilde q \circ \gamma$. Now we put
\begin{equation*}
\tau^{-1}(q_1,q_2) := (q_1, R(\tilde\rho',\gamma^{-1}))\text{.}
\end{equation*}
The calculation of $\tau^{-1} \circ \tau$ is straightforward.
\begin{comment}
Indeed, if $q_2 = \beta_r((R(\rho',\id_{\alpha(q)^{-1}}),1),q)$, we get $\tilde\rho' := R(\rho',\id_{\alpha(q)^{-1}})$, $g'=1$ and $\tilde q=q$, in particular $\gamma = \id_{\alpha(q)}$. Then, $R(\tilde\rho',\gamma^{-1}) = \rho'$.
\end{comment}
For the calculation of $(\tau \circ \tau^{-1})(q_1,q_2)$ we have to compute in the second component
\begin{eqnarray*}
\beta_r((R(\tilde\rho',\gamma^{-1} \cdot \id_{\alpha(q_1)^{-1}}),1),q_1) &=& \beta_r((R(\tilde\rho',\gamma^{-1}\cdot \id_{\alpha(q_1)^{-1}}),1) \circ (\gamma \cdot \id_{\alpha(\tilde q)^{-1}}),\tilde q)
\\&=& \beta_r((\tilde\rho',\alpha(q_1)\alpha(\tilde q)^{-1}),\tilde q)
\\&=& \beta_0(\alpha(q_1)\alpha(\tilde q)^{-1}g'^{-1},\beta_r((\tilde\rho',g'),\tilde q))
\\&=& \beta_0(\alpha(q_1)\alpha(\tilde q)^{-1}g'^{-1},q_{2})\text{,}
\end{eqnarray*}
and this is equivalent to $q_2$. 
\end{proof}






In order to promote the anafunctor $F$ to a 1-morphism between principal 2-bundles, we have to do two things: we have to check that $F$ commutes with the projections of the bundle $\mathcal{P}_1$ and $\mathcal{P}_2$, and we have to construct a $\Gamma$-equivariant structure on $F$. For the first point we use Remark \ref{rem:preserving} \erf{rem:preserving:b}, whose criterion $\pi \circ \alpha_l = \pi \circ \alpha_r$ is clearly satisfied. For the second point we provide a smooth action $\rho: F \times \Gamma_1 \to F$ in the sense of Definition \ref{def:actionanafunctor} and  use Lemma \ref{lem:equivarianceidentification}, which provides a construction of a $\Gamma$-equivariant structure. The action is defined by
\begin{equation}
\label{gammaactionanafunctorconstruction}
\rho(q,\gamma) := \beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}),(\id_{R(\alpha_l(q),t(\gamma))},t(\gamma))) \text{.}
\end{equation}


\begin{lemma}
This defines a smooth action of $\Gamma_1$ on $F$ in the sense of Definition \ref{def:actionanafunctor}.
\end{lemma}


\begin{proof}
Smoothness is clear from the definition. The identity
\begin{equation*}
\rho(\rho(q,\gamma_1),\gamma_2) = \beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot  \gamma_1 \cdot \gamma_2 \cdot \id_{t(\gamma_2)^{-1}t(\gamma_1)^{-1}}),(\id,t(\gamma_{1}\cdot\gamma_{2}))) = \rho(q,\gamma_1 \cdot \gamma_2)
\end{equation*}
follows from the definition and the two identities 
\begin{multline}
\label{eq:lem729id1}
\alpha(\rho(q,\gamma)) = \alpha(q)s(\gamma)
\quand
(\gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}) \cdot ( \id_{s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}t(\gamma_1)^{-1}}) =\gamma_1 \cdot \gamma_2 \cdot \id_{t(\gamma_2)^{-1}t(\gamma_1)^{-1}} \text{.}
\end{multline}
The latter can easily be verified upon substituting a crossed module for $\Gamma$. 
\begin{comment}
Indeed, the calculation is 
\footnotesize
\begin{eqnarray*}
&&\hspace{-1cm}\rho(\rho(q,\gamma_1),\gamma_2)
\\&=& \beta_l^{-1}(\rho(q,\gamma_1) \circ (\id_{\alpha(\rho(q,\gamma_1))} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}}),(\id,t(\gamma_{2})))
\\&\stackrel{\text{\erf{eq:lem729id1}}}{=}& \beta_l^{-1}(\beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot \gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}),(\id,t(\gamma_{1}))) \circ (\id_{\alpha(q)s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}}),(\id,t(\gamma_{2})))
\\&=& \beta_l^{-1}(\beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot \gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}),(\id,t(\gamma_{1})),  \id_{\alpha(q)s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}}),(\id,t(\gamma_{2})))
\\&=& \beta_l^{-1}(\beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot \gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}) \circ ( \id_{\alpha(q)s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}t(\gamma_1)^{-1}}),(\id,t(\gamma_{1}))),(\id,t(\gamma_{2})))
\\&=& \beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot \gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}) \circ ( \id_{\alpha(q)s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}t(\gamma_1)^{-1}}),(\id,t(\gamma_{1}\cdot\gamma_{2})))
\\&=& \beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot ((\gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}) \circ ( \id_{s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}t(\gamma_1)^{-1}}))),(\id,t(\gamma_{1}\cdot\gamma_{2})))
\\&\stackrel{\text{\erf{eq:lem729id1}}}{=}& \beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot  \gamma_1 \cdot \gamma_2 \cdot \id_{t(\gamma_2)^{-1}t(\gamma_1)^{-1}}),(\id,t(\gamma_{1}\cdot\gamma_{2})))
\end{eqnarray*}
\end{comment}
\begin{comment}
The proof of the second identity is
\begin{eqnarray*}
(\gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}) &=& (h_1,g_1)\cdot (1,g_1^{-1}t(h_1)^{-1}) \\&=& (h_1,t(h_1)^{-1})
\\
( \id_{s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}t(\gamma_1)^{-1}}) &=& (1,g_1) \cdot (h_2,g_2) \cdot (1,g_2^{-1}t(h_2)^{-1}g_1^{-1}t(h_1)^{-1})
\\&=& (\lw{g_1}h_2,g_1g_2) \cdot  (1,g_2^{-1}t(h_2)^{-1}g_1^{-1}t(h_1)^{-1})
\\ &=&  (\lw{g_1}h_2, g_1t(h_2)^{-1}g_1^{-1}t(h_1)^{-1})
\\
(\gamma_{1} \cdot \id_{t(\gamma_{1})^{-1}}) \circ ( \id_{s(\gamma_1)} \cdot \gamma_{2} \cdot \id_{t(\gamma_{2})^{-1}t(\gamma_1)^{-1}}) &=&  (h_1,t(h_1)^{-1}) \circ(\lw{g_1}h_2, g_1t(h_2)^{-1}g_1^{-1}t(h_1)^{-1})
\\&=& (h_1\lw{g_1}h_2, g_1t(h_2)^{-1}g_1^{-1}t(h_1)^{-1})
\\&=& (h_1,g_1) \cdot (h_2,g_2) \cdot (1,g_2^{-1}t(h_2)^{-1}g_1^{-1}t(h_1)^{-1})
\\&=& \gamma_1\cdot \gamma_2 \cdot \id_{t(\gamma_2)^{-1}t(\gamma_1)^{-1}}\text{.}
\end{eqnarray*}
\end{comment}
Checking  condition (i) of Definition \ref{def:actionanafunctor} just uses the definitions.
\begin{comment}
\begin{eqnarray*}
\alpha_l(\rho(q,\gamma)) 
&=& \alpha_l(\beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}),(\id_{R(\alpha_l(q),t(\gamma))},t(\gamma))))
\\&=& t(\id_{R(\alpha_l(q),t(\gamma))})
\\&=& R(\alpha_l(q),t(\gamma))
\\
\alpha_r(\rho(q,\gamma)) &=& \alpha_r(\beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}),(\id_{R(\alpha_l(q),t(\gamma))},t(\gamma))))
\\&=& R(\alpha_r(q \circ (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}})),t(\gamma))
\\&=& R(\alpha_r(q),\alpha(q)^{-1}\alpha(q \circ (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}))t(\gamma))
\\&=& R(\alpha_r(q),\alpha(q)^{-1}s(\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}})t(\gamma))
\\&=& R(\alpha_r(q),s(\gamma))\text{.}
\end{eqnarray*}
\end{comment}
We check condition (ii) in two steps. First we prove the identity
\begin{equation*}
\rho(\rho_l(\rho,q),\gamma_l \circ \gamma) = \rho_l(R(\rho,\gamma_l),\rho(q,\gamma))\text{.}
\end{equation*}
The main ingredient is the decomposition
\begin{equation}
\label{eq:lem729id2}
\id_{\alpha(q)} \cdot (\gamma_l \circ \gamma) \cdot \id_{t(\gamma_l)^{-1}} = (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}) \circ (\id_{\alpha(q)s(\gamma)t(\gamma)^{-1}} \cdot \gamma_l \cdot \id_{t(\gamma_l)^{-1}})
\end{equation}
that can e.g. be verified in the crossed module language. 
\begin{comment}
Indeed, we have with $\gamma=(h,g)$ and $\gamma_l = (h_l,g_l)$ and $t(\gamma) = t(h)g=g_l=s(\gamma_l)$:
\begin{eqnarray*}
\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}} &=& (\lw{\alpha(q)}{h},\alpha(q)t(h)^{-1})
\\
\id_{\alpha(q)s(\gamma)t(\gamma)^{-1}} \cdot \gamma_l \cdot \id_{t(\gamma_l)^{-1}} &=& (\lw{\alpha(q)t(h)^{-1}}{h_l},\alpha(q)t(h)^{-1}t(h_l)^{-1})
\\
\id_{\alpha(q)} \cdot (\gamma_l \circ \gamma) \cdot \id_{t(\gamma_l)^{-1}} &=& (\lw{\alpha(q)}{(h_lh)},\alpha(q)t(h)^{-1}t(h_l)^{-1})\text{,}
\end{eqnarray*}
and the composition of the first two expressions yields the third.
\end{comment}
Now we compute
\begin{eqnarray*}
\rho(\rho_l(\rho,q),\gamma_l \circ \gamma) &=& \beta_l^{-1}(q \circ (\id_{\alpha(q)} \cdot (\gamma_l \circ \gamma) \cdot \id_{t(\gamma_l)^{-1}}), (R(\rho,t(\gamma_l)),t(\gamma_l)))
\\&\stackrel{\text{\erf{eq:lem729id2}}}{=}&  \beta_l^{-1}(q \circ  (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}) ,(R(\rho,\gamma_l),t(\gamma_l)))
\\&=& \rho_l(R(\rho,\gamma_l),\rho(q,\gamma))\text{.}
\end{eqnarray*}
The second step is to show the identity
\begin{equation*}
\rho(\rho_r(q,\rho'),\gamma \circ \gamma_r) = \rho_r(\rho(q,\gamma),R(\rho',\gamma_r))\text{.}
\end{equation*}
Here we use the decomposition
\begin{equation}
\label{eq:lem729id3}
\id_{\alpha(q)} \cdot (\gamma \circ \gamma_r) \cdot \id_{t(\gamma)^{-1}} = (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}) \circ (\id_{\alpha(q)}\cdot \gamma_r \cdot \id_{t(\gamma)^{-1}})\text{.}
\end{equation}
\begin{comment}
For $\gamma=(h,g)$ and $\gamma_r=(h_r,g_r)$ with $g = t(h_r)g_r$ we have
\begin{eqnarray*}
\id_{\alpha(q)} \cdot (\gamma \circ \gamma_r) \cdot \id_{t(\gamma)^{-1}} &=&  (\lw{\alpha(q)}{(hh_r),\alpha(q)t(h_r)^{-1}t(h)^{-1}})
\\
\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}} &=&  (\lw{\alpha(q)}{h},\alpha(q)t(h)^{-1})
\\
\id_{\alpha(q)}\cdot \gamma_r \cdot \id_{t(\gamma)^{-1}} &=&  (\lw{\alpha(q)}{h_r},\alpha(q)t(h_r)^{-1}t(h)^{-1})
\end{eqnarray*}
and the composition of the last two expressions clearly gives the first.
\end{comment}
Then we compute
\begin{eqnarray*}
&&\hspace{-1.5cm}\rho(\rho_r(q,\rho'),\gamma \circ \gamma_r) \\&=& \beta_l^{-1}(\beta_r((R(\rho',\id_{\alpha(q)^{-1}}),1),q \circ (\id_{\alpha(q)} \cdot (\gamma \circ \gamma_r) \cdot \id_{t(\gamma)^{-1}})),(\id,t(\gamma)))
\\&\stackrel{\text{\erf{eq:lem729id3}}}{=}&
\beta_l^{-1}(\beta_r((R(\rho',\gamma_r\cdot \id_{s(\gamma)^{-1}\alpha(q)^{-1}}),1),\\&&\hspace{2cm}\beta_0(\alpha(q)s(\gamma_r)s(\gamma)^{-1}\alpha(q)^{-1},q \circ (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}}))),(\id,t(\gamma)))
\\&\stackrel{\text{\erf{eq:lem729id1}}}{=}& \beta_l^{-1}(\beta_r((R(\rho',\gamma_r \cdot \id_{\alpha(\rho(q,\gamma))^{-1}})),q \circ (\id_{\alpha(q)} \cdot \gamma \cdot \id_{t(\gamma)^{-1}})),(\id,t(\gamma)))
\\ &=& \rho_r(\rho(q,\gamma),R(\rho',\gamma_r))\text{,}
\end{eqnarray*}
where we have employed the equivalence relation on $F$ that was generated by the action of $\beta_0$. 
\end{proof}



\subsubsection{Construction of a 2-isomorphism $\eta_{\mathcal{A}}: \mathcal{A} \Rightarrow \mathscr{E}_M(\mathscr{R}_{\mathcal{A}})$}


We may again assume that the common refinement of $\mathcal{A}$ is the fibre product $\mathcal{P}_0 \times_M \mathcal{P}_0'$; otherwise, the proof of Lemma \ref{lem:canonicalrefinement} provides a 2-isomorphism between $\mathcal{A}$ and one of these.  
Now, $\mathcal{A}$ and $\mathscr{E}_M(\mathscr{R}_{\mathcal{A}})$ have the same common refinement, and $\eta_{\mathcal{A}}$ is given by the map
\begin{equation*}
\eta: Q \to F \times \Gamma_0 : q \mapsto (q,\alpha(q))\text{.}
\end{equation*}
This is obviously smooth and respects the projections to the base: if $\chi(q)=(p,p')$, then 
\begin{equation*}
\chi(q,\alpha(q)) \stackrel{\text{\erf{eq:emorph}}}{=} (\alpha_l(q),R(\alpha_r(q),\alpha(q)^{-1}))=(p,p')\text{.}
\end{equation*}
Further, it respects the $\Gamma$-actions:
\begin{equation*}
\eta(q \circ \gamma) = (q \circ \gamma, s(\gamma)) = \beta_l^{-1}(q \circ \gamma,(\id,1))  \stackrel{\text{\erf{gammaactionanafunctorconstruction}}}{=} (\rho(q,\id_{\alpha(q)^{-1}}\cdot \gamma),s(\gamma))\stackrel{\text{\erf{eq:emorph}}}{=} \eta(q) \circ \gamma\text{,}
\end{equation*}
so that $\eta$ is a bundle morphism. It remains to verify the commutativity of the compatibility diagram \erf{eq:comp2morphsimple}. Let $((\rho',g'),q') \in P' \otimes \zeta_1^{*}Q$, and let $(q,(\rho,g)) \in \zeta_2^{*}Q \otimes P$ be a representative for $\beta((\rho',g'),q')$. In particular, we have $\alpha(q)g=g'\alpha(q')$, since $\beta_r$ is anchor-preserving. Then, we get clockwise
\begin{equation}
\label{eq:clockwiseeta}
(\eta \otimes \id)(\beta((\rho',g'),q')) = ((q,\alpha(q)),(\rho,g))\text{.}
\end{equation}
Counter-clockwise, we have to use the isomorphism  of Lemma \ref{lem:eonemorphisms} that we call $\tilde\beta$ here. Then,
\begin{equation}
\label{eq:counterclockwiseeta}
\tilde\beta((\id \otimes \eta)((\rho',g'),q')) = \tilde\beta((\rho',g'),(q',\alpha(q')))
= ((\tilde q,g'\alpha(q')g^{-1}),(\rho, g))
\end{equation}
where the choices $(\tilde\rho,h)$ we have to make for the definition of $\tilde\beta$ are here $(\rho,g^{-1})$, and $\tilde q$ is defined in  \erf{eq:ftilde}, which gives  here
\begin{equation*}
\tilde q = \beta_l^{-1}(\beta_r((\rho',1),q'),(R(\rho^{-1},\id_{g^{-1}}),g^{-1}))\text{.}
\end{equation*}
\begin{comment}
Indeed, the full calculation is
\begin{eqnarray*}
\tilde q &:=& \rho(\rho_l(\rho^{-1} , \rho_r(q', R(\rho',\id_{\alpha(q')}))),\id_{g^{-1}}) \\&=& \rho(\beta_l^{-1}(\beta_r((\rho',1),q'),(\rho^{-1},1)),\id_{g^{-1}}) \\ &=& \beta_l^{-1}(\beta_r((\rho',1),q'),\mu((\rho^{-1},1) ,(\id,g^{-1}))) \\ &=& \beta_l^{-1}(\beta_r((\rho',1),q'),(R(\rho^{-1},\id_{g^{-1}}),g^{-1}))
\end{eqnarray*}
\end{comment}
Comparing \erf{eq:clockwiseeta} and \erf{eq:counterclockwiseeta} it remains to prove $q = \tilde q$ in $F$. As $F$ was the quotient of $Q$ by the action $\beta_0$, it suffices to have
\begin{eqnarray*}
\beta_0(g',\tilde q) &\stackrel{\text{(i)}}{=}& \beta_l^{-1}(\beta_r((\id,g'),\beta_r((\rho',1),q')), (R(\rho^{-1},\id_{g^{-1}}),g^{-1}))
\\ &\stackrel{\text{(iii)}}{=}& \beta_l^{-1}(\beta_r((\rho',g'),q'), (R(\rho^{-1},\id_{g^{-1}}),g^{-1}))
\\ &=& \beta_l^{-1}(\beta_l^{-1}(q,(\rho,g)), (R(\rho^{-1},\id_{g^{-1}}),g^{-1}))
\\ &\stackrel{\text{(ii)}}{=}& \beta_l^{-1}(q,(\id,1))
\\ &=& q\text{.}
\end{eqnarray*}
This finishes the construction of the 2-isomorphism $\eta_{\mathcal{A}}$. 





\begin{appendix}

\setsecnumdepth{1}
