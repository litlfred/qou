---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-010-52-properties-of-groupoid-bundle-gerbes
section_title: "Properties of Groupoid Bundle Gerbes"
section_number: 5.2
pages: 27-31
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.995
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
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
