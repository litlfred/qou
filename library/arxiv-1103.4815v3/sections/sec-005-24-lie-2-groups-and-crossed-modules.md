---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-005-24-lie-2-groups-and-crossed-modules
section_title: "Lie 2-Groups and crossed Modules"
section_number: 2.4
pages: 13-16
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.791
latex_coverage_ratio: 0.995
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
A (strict) \emph{Lie 2-group} is a  Lie groupoid $\Gamma$ whose objects and morphisms are Lie groups, and all of whose structure maps are Lie group homomorphisms. One can conveniently bundle the multiplications and the inversions into smooth functors
\begin{equation*}
m: \Gamma \times \Gamma \to \Gamma
\quad\text{ and }\quad
i: \Gamma \to \Gamma\text{.} 
\end{equation*}

\begin{example} 
For $A$ an abelian Lie group, the Lie groupoid $\mathcal{B}A$ from Example \ref{exliecat} (b) is a Lie 2-group. The condition that $A$ is abelian is necessary.
\end{example}


\begin{example}
\label{crossedmodule}
Let $t: H \to G$ be a homomorphism of Lie groups, and let $\act GH$ be the corresponding Lie groupoid from Example \ref{exliecat} \erf{extHG}.  This Lie groupoid becomes  a Lie 2-group if the following structure is given: a smooth left action of $G$ on $H$ by Lie group homomorphisms, denoted $(g,h) \mapsto \lw gh$, satisfying
\begin{equation*}
t(\lw gh) = gt(h)g^{-1}
\quad\text{ and }\quad
\lw{t(h)}x=hxh^{-1}
\end{equation*} 
for all $g\in G$ and $h,x\in H$. Indeed, the objects $G$ of $\act G H$  already form a Lie group, and the multiplication on the morphisms $H \times G$ of $\act G H$ is the semi-direct product
\begin{equation}
\label{multiplication}
(h_2,g_2) \cdot (h_1,g_1) = (h_2\;\lw{g_2}{h_1},g_2g_1)\text{.}
\end{equation}
The homomorphism $t:H \to G$ together with the action of $G$ on $H$ is called a \emph{smooth crossed module}. Summarizing, every smooth crossed module defines a Lie 2-group.
\end{example}

\begin{remark}
\label{rem:crossedmodule}
Every Lie 2-group $\Gamma$ can be obtained from a smooth crossed module. Indeed, one puts
$G := \Gamma_0$ and $H := \mathrm{ker}(s)$,
equipped with the Lie group structures defined by the multiplication functor $m$ of $\Gamma$. The homomorphism $t : H \to G$ is the target map $t: \Gamma_1 \to \Gamma_0$, and the action of $G$ on $H$ is given by the formula
$\lw g\gamma := \id_{g} \cdot \gamma \cdot \id_{g^{-1}}$  for $g \in \Gamma_0$ and $\gamma \in \mathrm{ker}(s)$. These two constructions are inverse to each other (up to canonical Lie group isomorphisms and strict Lie 2-group isomorphisms, respectively). 
\begin{comment}
Indeed, starting with a smooth crossed module $t:H \to G$, then we get reconstructed the smooth crossed module $t': H' \to G'$ with $G' = G$, 
\begin{equation*}
H' = \mathrm{ker}(s) = \left \lbrace (h,g) \in H \times G \;|\; g=1 \right \rbrace \cong H\text{,}
\end{equation*}
$t(h') = t(h,g) = t(h)g = t(h)$ and
\begin{equation*}
\lw{g}{h'} = \id_{g} \cdot (h,1) \cdot \id_{g^{-1}} = (1,g) \cdot (h,1) \cdot (1,g^{-1}) = (\lw gh,1)=\lw gh\text{.}
\end{equation*}
Conversely, starting with a Lie 2-group $\Gamma$, we get reconstructed the Lie 2-groupoid $\Gamma'$ with objects $\Gamma_0$ and morphisms $\mathrm{ker}(s) \times \Gamma_0$, target and source maps given by $t(\gamma,g) = t(\gamma)g$, $s(\gamma,g) = g$ and composition $(\gamma_2,g_2) \circ (\gamma_1,g_1) := (\gamma_2 \circ \gamma_1,g_1)$. We have the diffeomorphism 
\begin{equation*}
\varphi: \Gamma_1 \to \Gamma_1': \gamma \mapsto (\gamma \cdot \id_{s(\gamma)^{-1}},s(\gamma))
\end{equation*}
whose inverse is $(\gamma,g)\mapsto \gamma \cdot \id_g$. It further respects obviously source and target maps as well as the composition. The multiplication  on $\Gamma_1$ is 
\begin{equation*} 
(\gamma_2,g_2) \cdot (\gamma_1,g_1) := (\gamma_2 \lw{g_2}{\gamma_1},g_2g_1) = (\gamma_2 \cdot \id_{g_2} \cdot \gamma_1 \cdot \id_{g_2^{-1}},g_2g_1)\text{,}
\end{equation*}
and it is a straightforward calculation to check that $\varphi$ is a group homomorphism. 
\end{comment}
\end{remark}


\begin{example}
\label{aut2group}
Consider a connected Lie group $H$, so that its automorphism group $\mathrm{Aut}(H)$ is again a Lie group \cite{onishchik1}. Then, we have a smooth crossed module $(\mathrm{Aut}(H),H,i,\ev)$, where $i: H \to \mathrm{Aut}(H)$ is the assignment of inner automorphisms to group elements, and $\ev: \mathrm{Aut}(H) \times H \to H$ is the evaluation action. The associated Lie 2-group is denoted $\mathrm{AUT}(H)$ and is called the \emph{automorphism 2-group} of $H$.
\end{example}


\begin{example}
\label{exactsequence}
Let
\begin{equation*}
\alxydim{}{1 \ar[r] & H \ar[r]^{t} & G \ar[r]^{p} & K \ar[r] & 1}
\end{equation*} 
be an exact sequence of Lie groups, i.e. an exact sequence in which $p$ is a  submersion and $t$ is an embedding. The homomorphisms $t:H \to G$ and $p:G \to K$ define action groupoids $\act G H$ and $\act K G$ as explained in Example \ref{exliecat}. The first one is even a Lie 2-group:  the action  of $G$ on $H$ is defined by $\lw gh := t^{-1}(gt(h)g^{-1})$. This is well-defined: since 
\begin{equation*}
p(gt(h)g^{-1}) = p(g)p(t(h))p(g^{-1})=p(g)p(g)^{-1}=1\text{,}
\end{equation*}
the element $gt(h)g^{-1}$ lies in the image of $t$, and has a unique preimage. The action is smooth because $t$ is an embedding.  
The axioms of a crossed module are obviously satisfied. 
\end{example}


If a Lie groupoid $\Gamma$ is a Lie 2-group in virtue of a multiplication functor $m: \Gamma \times \Gamma \to \Gamma$, then the category $\bun \Gamma M$ of principal $\Gamma$-bundles over a smooth manifold $M$ is monoidal: 

\begin{definition}
\label{def:tensorproduct}
Let $P: \idmorph M \to \Gamma$ and $Q:\idmorph M \to \Gamma$ be principal $\Gamma$-bundles. The \emph{tensor product} $P \otimes Q$ is the anafunctor
\begin{equation*}
\alxydim{@C=1.5cm}{\idmorph M \ar[r]^-{\mathrm{diag}} & \idmorph M \times \idmorph M \ar[r]^-{P \times Q} & \Gamma \times \Gamma \ar[r]^-{m} &\Gamma \text{.}}
\end{equation*}
\end{definition}


\begin{example}
\label{ex:tensorproduct}
\begin{enumerate}[(a)]
\item 
\label{ex:tensorproduct:trivial}
Since trivial principal $\Gamma$-bundles $\trivlin_f$ correspond to \emph{smooth} functors $f:\idmorph M \to \Gamma$ (Example \ref{anafunctors}), it is clear that  $\trivlin_{f} \otimes \trivlin_g = \trivlin_{fg}$. 

\item
\label{ex:tensorproduct:general}
Unwinding Definition \ref{def:tensorproduct} in the  general case, the tensor product of two principal $\Gamma$-bundles $P_1$ and $P_2$ with anchors $\alpha_1$ and $\alpha_2$, respectively, and actions $\rho_1$ and $\rho_2$, respectively, is given by
\begin{equation}
\label{eq:tensorexplicit}
P_1 \otimes P_2 = ((P_1 \times_M P_2) \lli{m \circ (\alpha_1 \times \alpha_2)} \times_{t} \Gamma_1) \;/\; \sim\text{,}
\end{equation}
where 
\begin{equation}
\label{deftensorproductrel}
(p_1,p_2,m(\gamma_1,\gamma_2) \circ \gamma) \sim (\rho_1(p_1, \gamma_1), \rho_2(p_2 , \gamma_2), \gamma)
\end{equation}
for all $p_1\in P_1$, $p_2\in P_2$ and morphisms $\gamma,\gamma_1,\gamma_2\in \Gamma_1$ satisfying $t(\gamma_i)=\alpha_i(p_i)$ for $i=1,2$ and $s(\gamma_1)s(\gamma_2)\eq t(\gamma)$. The bundle projection is $\tilde\pi(p_1,p_2,\gamma) := \pi_1(p_1)=\pi_2(p_2)$, the anchor is $\tilde\alpha(p_1,p_2,\gamma) :=  s(\gamma)$, and the $\Gamma$-action is given by $\tilde\rho((p_1,p_2,\gamma),\gamma') := (p_1,p_2,\gamma \circ \gamma')$.
\end{enumerate}
\end{example}

\begin{comment}
\begin{remark}
\label{rem:tensorproduct}
In fact, since we have extended along a very special functor, namely the multiplication $m$, one can get rid of the $\Gamma_1$ factor in \erf{eq:tensorexplicit}. However, the formulas for the equivalence relation and the action become more complicated, so we keep representing elements in tensor products by triples $(p_1,p_2,\gamma)$.  
Indeed, if $(p_1,p_2,\gamma) \in P_1 \otimes P_2$, we put $\gamma_1 := \gamma \cdot \id_{\alpha_2(p_2)^{-1}}$ and $\gamma_2 := \id_{\alpha_2(p_2)}$. Then, $m(\gamma_1,\gamma_2)=\gamma$, $t(\gamma_1)=\alpha_1(p_1)$, $t(\gamma_2)=\alpha_2(p_2)$ and $s(\gamma_1)s(\gamma_2)=t(\gamma)$. Accordingly, we have $(p_1,p_2,\gamma) \sim (p_1 \circ \gamma_1,p_2 ,\id_{s(\gamma)})$. Thus, any equivalence class has a representative with $\gamma=\id$. Then, we would get
\begin{equation}
\label{remtp1}
P_1 \otimes P_2  =  ( P_1 \times_M P_2) \;/\; \sim\text{,}
\end{equation}
where 
\begin{equation}
\label{remtp2}
(\rho_1(p_1,\gamma),p_2) \sim (p_{1}, \rho_2(p_2 ,m( i(\gamma^{-1}) , \id_{s(\gamma)\alpha_2(p_2)})))
\end{equation}
for all $\gamma\in \Gamma_1$ with $t(\gamma)=\alpha_1(p_1)$, where $i: \Gamma_1 \to \Gamma_1$ denotes the inversion with respect to the multiplication $m$. The anchor is 
\begin{equation}
\label{remtp3}
\alpha(p_1,p_2) = \alpha_1(p_1)\alpha_2(p_2)\text{,}
\end{equation}
and the action of $\Gamma$ on $P_1 \otimes P_2$ is given by 
\begin{equation}
\label{remtp4}
(p_1,p_2)\circ\gamma = (\rho_1(p_1 ,m(\gamma , \id_{\alpha_2(p_2)^{-1}})),p_2 ) = (p_{1}, \rho_2(p_2 ,m(i(\gamma)^{-1} , \id_{s(\gamma)\alpha_2(p_2)})) \text{.}
\end{equation}
\end{remark}
\end{comment}

As a consequence of Lemma \ref{extensionfunctor} and the fact that the composition of anafunctors is associative up to coherent transformations, we have

\begin{proposition}
\label{prop:monoidalstack}
For $M$ a smooth manifold and $\Gamma$ a Lie 2-group, the tensor product
\begin{equation*}
\otimes : \bun\Gamma M \times \bun\Gamma M \to \bun\Gamma M
\end{equation*}
equips the groupoid of principal $\Gamma$-bundles over $M$ with a monoidal structure.  Moreover, it turns the stack $\bun\Gamma-$ into a monoidal stack. \end{proposition}


Notice that the tensor unit of the monoidal groupoid $\bun\Gamma M$ is the trivial principal $\Gamma$-bundle $\trivlin_{1}$ associated to the constant map $1: M \to \Gamma_0$, or, in terms of anafunctors, the one associated to the constant functor $1: M \to \Gamma$. 


A (weak) \emph{Lie 2-group homomorphism} between Lie 2-groups $(\Gamma,m_{\Gamma})$ and $(\Omega,m_{\Omega})$ is an anafunctor $\Lambda: \Gamma \to \Omega$ together with a transformation
\begin{equation}
\label{eq:lie2grouphom}
\alxydim{@=1.3cm}{\Gamma \times \Gamma \ar[r]^-{m_{\Gamma}}   \ar[d]_{\Lambda \times \Lambda} &  \Gamma \ar[d]^{\Lambda} \ar@{=>}[dl]|*+{\eta} \\ \Omega \times \Omega \ar[r]_-{m_{\Omega}} & \Omega}
\end{equation}
satisfying the evident coherence condition. Under the equivalence with smooth crossed modules (Remark \ref{rem:crossedmodule}),  Lie 2-group homomorphisms correspond to so-called butterflies \cite{Aldrovandi2009}. 
A Lie 2-group homomorphism is called \emph{weak equivalence}, if the anafunctor $\Lambda$ is a weak equivalence.
Since extensions and tensor products are both defined via  composition of anafunctors,  we immediately obtain

\begin{proposition}
\label{extensionstackmorphism}
Extension along a Lie 2-group homomorphism $\Lambda: \Gamma \to \Omega$ between Lie 2-groups is a monoidal functor
\begin{equation*}
\Lambda: \bun{\Gamma}M \to \bun\Omega M
\end{equation*}
between monoidal categories. Moreover, these form a monoidal morphism between monoidal stacks.
\end{proposition}

Since a monoidal functor is an equivalence of monoidal categories if it is an equivalence of the underlying categories, Corollary \ref{co:extensionweakequivalence} implies:

\begin{corollary}
\label{co:extensionweakequivalence2groups}
For $\Lambda: \Gamma \to \Omega$ a weak equivalence between Lie 2-groups, the monoidal functor of Proposition \ref{extensionstackmorphism} is an equivalence of monoidal categories. Moreover, these form a monoidal equivalence between monoidal stacks. 
\end{corollary}


If we represent the Lie 2-group $\Gamma$ by a smooth crossed module $t:H \to G$ as described in Example \ref{crossedmodule}, we want to determine explicitly what the tensor product looks like under the correspondence of $\act GH$-bundles and principal $H$-bundles with anti-equivariant maps to $G$, see Lemma \ref{actionbundles}.


\begin{lemma}
\label{lem:actiontensorbundles}
Let $t: H \to G$ be a crossed module and let $P$ and $Q$ be $\act GH$-bundles over $M$. Let $(P_H,f)$ and $(Q_H,g)$ be the principal $H$-bundles together with their $H$-anti-equivariant maps that belong to $P$ and $Q$, respectively, under the equivalence of Lemma \ref{actionbundles}. Then, the principal $H$-bundle that corresponds to the tensor product $P \otimes Q$ is given by 
\begin{equation*}
(P \otimes Q)_H = \big(P \times_M Q\big) / \sim
\quere
(p \star h,q) \sim (p,q \star (\lw{f(p)^{-1}}{h}))\text{.}
\end{equation*}
The action of $H$ on $(P \otimes Q)_H$ is  $ [(p,q)] \star h = [(p \star h,q)] $, and the $H$-anti-equivariant map of $(P \otimes Q)_H$ is   
$ [(p,q) ] \mapsto f(p) \cdot g(q)$.
\end{lemma}


\begin{comment}
Proof. 
We use the formula from the comment in Remark \ref{rem:tensorproduct}. Writing $\gamma\in \Gamma_1$ from \erf{remtp2} as $\gamma=(h,g)$, where $g$ is determined by $g = t(h)^{-1}\alpha_1(p_1)$, we get $\gamma^{-1}=(h^{-1},\alpha_1(p_1))$ and further $i(\gamma^{-1}) = (\lw{\alpha_1(p_1)^{-1}}h,\alpha_1(p_1)^{-1})$, so that
\begin{multline*}
m( i(\gamma^{-1}) , \id_{s(\gamma)\alpha_2(p_2)}) = (\lw{\alpha_1(p_1)^{-1}}h,\alpha_1(p_1)^{-1}) \cdot (1,s(\gamma)\alpha_2(p_2)) \\=(\lw{\alpha_1(p_1)^{-1}}h,\alpha_1(p_1)^{-1}s(\gamma)\alpha_2(p_2))\text{.} \end{multline*}
Then, the left hand side of \erf{remtp2} is
\begin{equation*}
p_1 \cdot \gamma = p_1 \cdot (h,g) = p_1 \cdot (h, t(h)^{-1}\alpha_1(p_1)) = p_1 \star h
\end{equation*}
and the right hand side of \erf{remtp2} is
\begin{multline*}
(p_{1}, \rho_2(p_2 ,m( i(\gamma^{-1}) , \id_{s(\gamma)\alpha_2(p_2)}))) 
\\=  (p_{1}, p_{2} \cdot (\lw{\alpha_1(p_1)^{-1}}h,\alpha_1(p_1)^{-1}t(h)^{-1}\alpha_1(p_1)\alpha_2(p_2))) = (p_1,p_2 \star (\lw{\alpha_1(p_1)}{h}))\text{,}
\end{multline*}
where we have used the axioms of the crossed module in the last step. This reproduces the claimed equivalence relation. The $H$-anti-equivariant map is given by the anchor \erf{remtp3}. Finally, the action is given by \erf{remtp4}: for $\gamma = (h,g)$, where $g=t(h)^{-1}\alpha_1(p_1)\alpha_2(p_2)$, we compute
\begin{equation*}
m(\gamma , \id_{\alpha_2(p_2)^{-1}}) = (h,g) \cdot (1,\alpha_2(p_2)^{-1}) = (h,t(h)^{-1}\alpha_1(p_1))\text{.}
\end{equation*} 
Then, \erf{remtp4} implies the claimed action.
\end{comment}

Similar to the tensor product of principal $\Gamma$-bundles, the dual $P^{\vee}$ of a principal $\Gamma$-bundle $P$ over $M$ is the extension of $P$ along the inversion $i:\Gamma \to \Gamma$ of the 2-group, $P^{\vee} := i(P)$. The equality $m \circ (\id,i) = 1$ of functors $M \to \Gamma$ induces a \quot{death map} $d: P \otimes P^{\vee} \to \trivlin_{1}$.
We are going to use this bundle morphism in Section \ref{sec:gerbeprop}, but omit a further systematical treatment of duals for the sake of brevity. 


\setsecnumdepth{1}
