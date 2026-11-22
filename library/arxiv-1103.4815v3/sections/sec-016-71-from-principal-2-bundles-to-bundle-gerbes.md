---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-016-71-from-principal-2-bundles-to-bundle-gerbes
section_title: "From Principal 2-Bundles to Bundle Gerbes"
section_number: 7.1
pages: 39-48
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.806
latex_coverage_ratio: 0.997
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{sec:extraction}


In this section we define the 2-functor
$\mathscr{E}_M: \zwoabun \Gamma M \to \grb\Gamma M$.



\subsubsection{Definition of $\mathscr{E}_M$ on objects}

Let $\mathcal{P}$ be a principal $\Gamma$-2-bundle over $M$, with projection $\pi: \mathcal{P} \to M$ and right action $R$ of $\Gamma$ on $\mathcal{P}$. The first ingredient of the $\Gamma$-bundle gerbe $\mathscr{E}_M(\mathcal{P})$ is the surjective submersion $\pi: \mathcal{P}_0 \to M$. The second ingredient is a principal $\Gamma$-bundle $P$ over $\mathcal{P}_0^{[2]}$. We put
\begin{equation*}
P := \mathcal{P}_1 \times \Gamma_0\text{.}
\end{equation*}
Bundle projection, anchor and $\Gamma$-action are given, respectively, by \begin{multline}
\label{defgerbefrombundle}
\chi(\rho,g) := (t(\rho),R(s(\rho),g^{-1}))
\quomma
\alpha(\rho,g) := g
\quand
(\rho,g) \circ \gamma := (R(\rho,\id_{g^{-1}} \cdot \gamma),s(\gamma))\text{.}
\end{multline}
These definitions are motivated by Remark \ref{rem:motivation} below. 
\begin{comment}
Notice that we also have
\begin{multline*}
 R(\rho,\id_{g^{-1}}\cdot \gamma) = R(R(\rho,\id_{g^{-1}}),\gamma) \\= R(R(\rho,\id_{g^{-1}}),\id_g) \circ R(\id_{R(s(\rho),g^{-1})},\gamma) = \rho \circ R(\id_{R(s(\rho),g^{-1})},\gamma)\text{.}
\end{multline*}
\end{comment}

\begin{lemma}
\label{lem:bundleforgerbe}
This defines a principal $\Gamma$-bundle over $\mathcal{P}_0^{[2]}$.
\end{lemma}

\begin{proof}
First we check that $\chi: P \to \mathcal{P}_0^{[2]}$ is a surjective submersion. Since the functor $\tau = (\id,R)$ is a weak equivalence, we know from Theorem \ref{weak} that
\begin{equation*}
f:(\mathcal{P}_0 \times \Gamma_0) \lli{\tau} \times_{t \times t} \mathcal{P}_1^{[2]} \to \mathcal{P}_0^{[2]} : (p,g,\rho_1,\rho_2) \mapsto (s(\rho_1),s(\rho_2))
\end{equation*} 
is a surjective submersion. Now consider the smooth surjective map
\begin{equation*}
g: (\mathcal{P}_0 \times \Gamma_0) \lli{\tau} \times_{t \times t} \mathcal{P}_1^{[2]} \to \mathcal{P}_1 \times \Gamma_0  : (p,g,\rho_1,\rho_2) \mapsto (\rho_1^{-1} \circ R(\rho_2,\id_{g^{-1}}),g^{-1})\text{.}
\end{equation*} 
\begin{comment}
It is well-defined because $s(\rho_1^{-1}) = t(\rho_1) = p = R(t(\rho_2),g^{-1}) = t(R(\rho_2, \id_{g^{-1}}))$. 
\end{comment}
We have $\chi \circ g = f$; thus, $\chi$ is a surjective submersion.
\begin{comment} 
Indeed,
\begin{multline*}
(\chi \circ g)(p,g,\rho_1,\rho_2) = \chi(\rho_1^{-1} \circ R(\rho_2,\id_{g^{-1}}),g^{-1}) = (t(\rho_1^{-1}),R(s(R(\rho_2,\id_{g^{-1}}))), g) \\= (s(\rho_{1}), s(\rho_2)) = f(p,g,\rho_1,\rho_2)\text{.}
\end{multline*}
\end{comment}
Next we check that we have defined an action. Suppose $(\rho,g) \in P$ and $\gamma\in \Gamma_1$ such that $\alpha(\rho,g) = g = t(\gamma)$. Then, $\alpha((\rho,g) \circ \gamma) =  s(\gamma)$. Moreover, suppose $\gamma_1,\gamma_2\in \Gamma_1$ with $t(\gamma_1)= g$ and $t(\gamma_2)=s(\gamma_1)$. Then,
\begin{multline*}
((\rho,g) \circ \gamma_1) \circ \gamma_2 
=
(R(\rho,\id_{g^{-1}} \cdot \gamma_1),s(\gamma_1)) \circ \gamma_2
=
(R(\rho,\id_{g^{-1}} \cdot \gamma_1 \cdot \id_{s(\gamma_1)^{-1}} \cdot \gamma_2),s(\gamma_2))
= (\rho,g) \circ (\gamma_1 \circ \gamma_2)\text{,}
\end{multline*}
where we have used that $\gamma_1 \circ \gamma_2 = \gamma_1 \cdot \id_{s(\gamma_1)^{-1}} \cdot \gamma_2$ in any 2-group. 
\begin{comment}
This follows from the fact that composition is a group homomorphism. Firstly,
\begin{multline*}
(\gamma_1 \cdot \id_{s(\gamma_1)^{-1}} \cdot \gamma_2) =(\gamma_1 \cdot (\id_{s(\gamma_1)^{-1}} \cdot \gamma_2)) \circ (\gamma_2 \cdot (i(\gamma_2) \cdot \id_{t(\gamma_2)^{-1}s(\gamma_1)^{-1}s(\gamma_2)}))\\= (\gamma_1 \circ \gamma_2) \cdot ((\id_{s(\gamma_1)^{-1}} \cdot \gamma_2) \circ (i(\gamma_2) \cdot \id_{t(\gamma_2)s(\gamma_1)^{-1}s(\gamma_2)}) )
\end{multline*}
and secondly,
\begin{equation*}
(\id_{s(\gamma_1)^{-1}} \cdot \gamma_2) \circ (i(\gamma_2) \cdot \id_{t(\gamma_2)s(\gamma_1)^{-1}s(\gamma_2)}) = i(\gamma_2) \cdot \gamma_2 = \id_1\text{.}
\end{equation*}
\end{comment}
It remains to check that the smooth map
\begin{equation*}
\tilde\tau: P \lli{\alpha}\times_{t} \Gamma_1 \to P \lli{\chi}\times_{\chi} P : ((\rho,g),\gamma) \mapsto ((\rho,g),(\rho,g)\circ \gamma)
\end{equation*} 
is a diffeomorphism. For this purpose, we consider the diagram
\begin{equation}
\label{eq:pullback}
\alxydim{@C=1.5cm@R=1.3cm}{ & \mathcal{P}_1^{[2]} \ar[d]^{s \times t} \\ (\mathcal{P}_0 \times \Gamma_0) \times (\mathcal{P}_0 \times \Gamma_0) \ar[r]_-{\tau \times \tau} & \mathcal{P}_0^{[2]} \times \mathcal{P}_0^{[2]}}
\end{equation}
and claim that (a)  $N_1 :=P \lli{\alpha} \times_{t}\Gamma_1$ is a pullback of \erf{eq:pullback}, (b) $N_2 :=P \lli{\chi} \times_{\chi} P$ is a pullback of \erf{eq:pullback}, and (c)  the unique map $N_1 \to N_2$ is $\tilde\tau$. Thus, $\tilde \tau$ is a diffeomorphism.

\begin{comment}
Before we prove the three claims we recall that a pullback of \erf{eq:pullback} is actually a triple $(N,f,g)$ consisting of a smooth manifold $N$ together with smooth maps $f: N \to \mathcal{P}_1^{[2]}$ and $g: N \to (\mathcal{P}_0 \times \Gamma_0) \times (\mathcal{P}_0 \times \Gamma_0)$, such that
\begin{equation}
\label{eq:pullback2}
\alxydim{@C=1.5cm}{N \ar[r]^{f} \ar[d]_{g} & \mathcal{P}_1^{[2]} \ar[d]^{s \times t} \\ (\mathcal{P}_0 \times \Gamma_0) \times (\mathcal{P}_0 \times \Gamma_0) \ar[r]_-{\tau \times \tau} & \mathcal{P}_0^{[2]} \times \mathcal{P}_0^{[2]}}
\end{equation}
is commutative, and $(N,f,g)$ has the universal property. 
\end{comment}

In order to prove  claim (a)
we use again that the functor $\tau = (\id, R)$ is  a weak equivalence, so that by Theorem \ref{weak} the triple $(\mathcal{P}_1 \times \Gamma_1,\tau,s \times t)$ is a pullback of \erf{eq:pullback}. 
We consider the smooth map 
\begin{equation*}
\xi: N_{1} \to \mathcal{P}_1 \times \Gamma_1:((\rho,g),\gamma) \mapsto (R(\rho,\id_{g^{-1}}),\gamma)
\end{equation*}
which is a diffeomorphism because  $(\rho,\gamma) \mapsto ((R(\rho,\id_{t(\gamma)}),t(\gamma)),\gamma)$ is a smooth map which is  inverse to $\xi$. 
\begin{comment}
Indeed,
\begin{equation*}
\xi^{-1}(\xi(\rho,g,\gamma)) = \xi^{-1}(R(\rho,\id_{g^{-1}}),\gamma) =(R(R(\rho,\id_{g^{-1}}),\id_{t(\gamma)}),t(\gamma),\gamma) = (\rho,g,\gamma)
\end{equation*}
and
\begin{equation*}
\xi(\xi^{-1}(\rho,\gamma)) = \xi(R(\rho,\id_{t(\gamma)}),t(\gamma),\gamma) =(R(R(\rho,\id_{t(\gamma)}),\id_{t(\gamma)^{-1}}),\gamma) = (\rho,\gamma)\text{.} 
\end{equation*}
\end{comment}
Thus, putting  $f_1 := \tau \circ \xi$ and $g_1 := (s \times t) \circ \xi$ we see that $(N_1,f_1,g_1)$ is a pullback of \erf{eq:pullback}. In order to prove claim (b), we put
\begin{eqnarray*}
f_2((\rho_1,g_1),(\rho_2,g_2)) &:=& (R(\rho_{1},\id_{g_1^{-1}}),\rho_2)
\\
g_2((\rho_1,g_1),(\rho_2,g_2)) &:=& (R(s(\rho),g_1^{-1}),g_2,R(t(\rho_1),g_1^{-1}),g_1)\text{,}
\end{eqnarray*}
and it is straightforward to check that the cone $(N_2,f_2,g_2)$ makes \erf{eq:pullback} commutative. 
\begin{comment}
Indeed,
\begin{eqnarray*}
((s \times t) \circ f_2)((\rho_1,g_1),(\rho_2,g_2)) &=& (s \times t)(R(\rho_{1},\id_{g_1^{-1}}),\rho_2)
\\&=& (R(s(\rho_1),g_1^{-1}),s(\rho_{2}), R(t(\rho_1),g_1^{-1}),t(\rho_2))
\\&=& (\tau(R(s(\rho),g_1^{-1}),g_2),\tau(R(t(\rho_1),g_1^{-1}),g_1))
\\&=& ((\tau \times \tau) \circ g_2)((\rho_1,g_1),(\rho_2,g_2))\text{,}
\end{eqnarray*}
where we have used that $t(\rho_1)=t(\rho_2)$ and $R(s(\rho_1),g_1^{-1}g_2)=s(\rho_2)$. \end{comment}
The triple $(N_2,f_2,g_2)$ is also universal: in order to see this suppose $N'$ is any smooth manifold with smooth maps $f': N' \to \mathcal{P}_1^{[2]}$ and $g': N' \to (\mathcal{P}_0 \times \Gamma_0) \times (\mathcal{P}_0 \times \Gamma_0)$ so that \erf{eq:pullback} is commutative. For $n\in N'$, we write $f'(n) = (\rho_1,\rho_2)$ and $g'(n)=(p_1,g_1,p_2,g_2)$. Then, $\sigma(n) := ((R(\rho_1,\id_{g_2^{-1}}),g_2),(\rho_2,g_1))$ defines a smooth map $\sigma:N' \to P \lli{\chi} \times_{\chi} P$. One checks that $f_2 \circ \sigma = f'$ and $g_2 \circ \sigma = g'$, and that $\sigma$ is the only smooth map satisfying these equations. This proves that $(N_2,f_2,g_2)$ is a pullback. We are left with claim (c). Here one only has to check that $\tau: N_1 \to N_2$ satisfies $f_2=f_1 \circ \tau$ and $g_2 = g_1 \circ \tau$. 
\end{proof}

\begin{remark}
\label{rem:motivation}
The smooth functor $\tau=(\id,R): \mathcal{P} \times \Gamma \to \mathcal{P} \times_M \mathcal{P}$ is a weak equivalence, and so has a canonical inverse anafunctor $\tau^{-1}$ (Remark \ref{rem:inverses}). The anafunctor
\begin{equation*}
\alxydim{}{\mathcal{P}_0^{[2]}  \ar[r]^-{\iota} & \mathcal{P} \times_M \mathcal{P} \ar[r]^-{c} & \mathcal{P} \times_M \mathcal{P}\ar[r]^-{\tau^{-1}} & \mathcal{P} \times \Gamma \ar[r]^-{\mathrm{pr}_2} &  \Gamma\text{,}}
\end{equation*}
where $c$ is the functor that switches the factors,
corresponds to a principal $\Gamma$-bundle over $\mathcal{P}_0^{[2]}$ that is canonically isomorphic to the bundle $P$ defined above. 
\begin{comment}
In order to compute the composite $\mathrm{pr}_2 \circ \tau^{-1} \circ c \circ \iota$ we use Example \ref{ex:composition} \erf{ex:composition:full}. So, it has the total space
\begin{equation*}
F := \left ( \mathcal{P}_0^{[2]} \lli{c \circ (\iota \times \iota)} \times_{s \times s} \mathcal{P}_1^{[2]} \lli{t \times t} \times_{\tau} (\mathcal{P}_0 \times \Gamma_0) \lli{\mathrm{pr}_2}\times_{t}\Gamma_1 \right )/ \sim
\end{equation*}
where the equivalence relation identifies
\begin{equation*}
(p_1,p_2,\tilde\rho^{-1} \circ \rho_1,R(\tilde\rho,\tilde\gamma)^{-1} \circ \rho_2,s(\tilde\rho),s(\tilde\gamma),\gamma) \sim (p_1,p_2,\rho_1,\rho_2,t(\tilde\rho),t(\tilde\gamma),\tilde\gamma \circ \gamma)
\end{equation*}
for all $\tilde\rho\in \mathcal{P}_1$, $\tilde\gamma\in \Gamma_1$ with $p_1=s(\rho_2)$, $p_2=s(\rho_1)$, $t(\rho_1)=t(\tilde\rho)$, $t(\rho_2)= t(R(\tilde\rho,\tilde\gamma))$ and  $s(\tilde\gamma)=t(\gamma)$. The bundle projection is to the $\mathcal{P}_0^{[2]}$-factor on the left hand side, and the anchor is $s: \Gamma_1 \to \Gamma_0$ on the right hand side. The $\Gamma$ action is simply by composition from the right.  

A projection- and anchor-preserving smooth map is given by
\begin{equation*}
\varphi: P \to F: (\rho,g) \mapsto (t(\rho),p,\id_{p},\rho^{-1},p,g,\id_g)
\end{equation*}
where $p := R(s(\rho),g^{-1})$. This is well-defined; the only calculation one has to do is $t(\rho^{-1})=  R(p,g)$. It remains to check that $\varphi$ preserves the $\Gamma$-action:
\begin{eqnarray*}
\varphi(\rho,g) \circ \gamma &=& (t(\rho),p,\id_{p},\rho^{-1},p,g,\id_g) \circ \gamma
\\&=& (t(\rho),p,\id_{p},\rho^{-1},p,g,\gamma)
\\&=& (t(\rho),p,\id_{p},R(\id_{p},\gamma^{-1}) \circ \rho^{-1},p,s(\gamma),\id_{s(\gamma)})
\\&=& \varphi(\rho \circ R(\id_{R(s(\rho),g^{-1})},\gamma),s(\gamma))
\\&=& \varphi((\rho,g) \circ \gamma)\text{.}
\end{eqnarray*}
So, $\varphi$ is a bundle isomorphism. 
\end{comment}
\end{remark}



It remains to  provide the bundle gerbe  product 
\begin{equation*}
\mu: \pi_{23}^{*}P \otimes \pi_{12}^{*}P \to \pi_{13}^{*}P\text{,}
\end{equation*}
which we define by the formula
\begin{equation}
\label{defmu}
\mu((\rho_{23},g_{23}),(\rho_{12},g_{12})) := (\rho_{12} \circ R(\rho_{23},\id_{g_{12}}) ,g_{23}g_{12})\text{.}
\end{equation}
\begin{comment}
Notice that we have by assumption 
\begin{equation*}
\pi_1(\chi(\rho_{23},g_{23})) = t(\rho_{23}) = R(s(\rho_{12}),g_{12}^{-1})  = \pi_2(\chi(\rho_{12},g_{12}))
\end{equation*}
so that the composition in \erf{defmu} is well-defined. 
\end{comment}

\begin{lemma}
Formula \erf{defmu} defines an associative isomorphism $\mu: \pi_{23}^{*}P \otimes \pi_{12}^{*}P \to \pi_{13}^{*}P$ of principal $\Gamma$-bundles over $\mathcal{P}_0^{[3]}$. \end{lemma}

\begin{proof}
First of all, we recall from Example \ref{ex:tensorproduct} \erf{ex:tensorproduct:general} that an element in the tensor product $\pi_{23}^{*}P \otimes \pi_{12}^{*}P$ is  represented by a triple $(p_{23},p_{12},\gamma)$ where $p_{23},p_{12} \in P$ with $\pi_1(\chi(p_{23})) = \pi_2(\chi(p_{12}))$, and $\alpha(p_{23}) \cdot \alpha(p_{12})=t(\gamma)$.
In \erf{defmu} we refer to triples where $\gamma = \id_{g_{23}g_{12}}$, and this definition extends to triples with general $\gamma \in \Gamma_1$ by employing the equivalence relation
\begin{equation}
\label{equivreltp}
(p_1,p_2,\gamma) \sim  (p_1 \circ (\gamma \cdot \id_{\alpha(p_2)^{-1}}),p_2,\id_{s(\gamma)})\text{.} \end{equation}
The complete formula for $\mu$ is then
\begin{equation}
\label{defmufull}
\mu((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma) = (\rho_{12} \circ R(\rho_{23},\id_{g_{23}^{-1}} \cdot \gamma)  ,s(\gamma))\text{.}
\end{equation}
\begin{comment}
Indeed,
\begin{eqnarray*}
\mu((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma) &=& \mu((\rho_{23},g_{23}) \circ (\gamma \cdot \id_{g_{12}^{-1}}),(\rho_{12},g_{12}))
\\&=&  \mu((\rho_{23} \circ R(\id_{R(s(\rho_{23}),g_{23}^{-1})},\gamma \cdot \id_{g_{12}^{-1}}),s(\gamma)g_{12}^{-1}),(\rho_{12},g_{12}))
\\&=&   (\rho_{12} \circ R(\rho_{23} \circ R(\id_{R(s(\rho_{23}),g_{23}^{-1})},\gamma \cdot \id_{g_{12}^{-1}}),\id_{g_{12}}) ,s(\gamma))
\\&=& (\rho_{12} \circ R(\rho_{23},\id_{g_{12}}) \circ R(\id_{R(s(\rho_{23}),g_{23}^{-1})},\gamma ) ,s(\gamma))
\\&=& (\rho_{12} \circ R(\rho_{23},\id_{g_{12}}) \circ R(\id_{s(\rho_{23})},\id_{g_{23}^{-1}}\cdot\gamma ) ,s(\gamma))
\\&=& (\rho_{12} \circ R(\rho_{23},\id_{g_{23}^{-1}} \cdot \gamma)  ,s(\gamma))
 \text{.}
\end{eqnarray*}
\end{comment}
Next we check that \erf{defmufull} is well-defined under the equivalence relation \erf{equivreltp}: 
\begin{eqnarray*}
\mu(((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma)) 
&=& (\rho_{12} \circ R(\rho_{23},\id_{g_{23}^{-1}} \cdot \gamma)  ,s(\gamma))
\\&=&   (\rho_{12} \circ R(\rho_{23} \circ R(\id_{R(s(\rho_{23}),g_{23}^{-1})},\gamma \cdot \id_{g_{12}^{-1}}),\id_{g_{12}} )  ,s(\gamma))
\\&=& \mu((\rho_{23} \circ R(\id_{R(s(\rho_{23}),g_{23}^{-1})},\gamma \cdot \id_{g_{12}^{-1}}),s(\gamma)g_{12}^{-1}),(\rho_{12},g_{12}),\id_{s(\gamma)}))
\\&=& \mu(((\rho_{23},g_{23}) \circ (\gamma \cdot \id_{g_{12}^{-1}}),(\rho_{12},g_{12}),\id_{s(\gamma)}))\text{.}
\end{eqnarray*}
Now we have shown that $\mu$ is a well-defined map from $\pi_{23}^{*}P \otimes \pi_{12}^{*}P$ to $\pi_{13}^{*}P$, and it remains to prove that it is a bundle morphism. Checking that it preserves fibres and anchors is straightforward.
\begin{comment}
Firstly, we check that \erf{defmufull} preserves the fibres:
\begin{eqnarray*}
\chi(\mu((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma)) 
&=&  \chi((\rho_{23} \circ R(\rho_{12},  \id_{g_{12}} \cdot i(\gamma)) ,s(\gamma)))
\\&=&  (R(s( R(\rho_{12},  \id_{g_{12}} \cdot i(\gamma))) ,s(\gamma)),t(\rho_{23}))
\\&=& (R(s(\rho_{12}),g_{12}),t(\rho_{23}))
\\&=& (\pi_1(\chi(\rho_{12},g_{12})),\pi_{2}(\chi(\rho_{23},g_{23})) )
\end{eqnarray*}
Secondly, we check that \erf{defmufull} preserves the anchors:
\begin{eqnarray*}
\alpha(\mu((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma)) 
&=& \alpha (\rho_{23} \circ R(\rho_{12},  \id_{g_{12}} \cdot i(\gamma)) ,s(\gamma) ) 
\\&=& s(\gamma)
\\&=& \alpha((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma)
\end{eqnarray*}
\end{comment}
It remains to check that \erf{defmufull} preserves the  $\Gamma$-action. We calculate
\begin{eqnarray*}
\mu(((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma) \circ \tilde\gamma)
&=& \mu((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma \circ \tilde\gamma)
\\&=& (\rho_{23} \circ R(\rho_{12},  \id_{g_{12}} \cdot i(\gamma \circ \tilde\gamma)) ,s( \tilde\gamma) )
\\&=& (\rho_{23} \circ R(R(\rho_{12},  \id_{g_{12}}), i(\gamma)\circ i(\tilde\gamma)),s(\tilde\gamma))
\\&=&(\rho_{23} \circ R(R(\rho_{12},  \id_{g_{12}}), i(\gamma)) \circ R(\id_{R(s(\rho_{12}),  g)},i(\tilde\gamma)),s(\tilde\gamma))
\\&=& (\rho_{23} \circ R(\rho_{12},  \id_{g_{12}} \cdot i(\gamma)) \circ R(\id_{R(s(\rho_{12}),  g)},i(\tilde\gamma)),s(\tilde\gamma))
\\&=& (\rho_{23} \circ R(\rho_{12},  \id_{g_{12}} \cdot i(\gamma)) ,s(\gamma) )\circ \tilde\gamma
\\&=& \mu((\rho_{23},g_{23}),(\rho_{12},g_{12}),\gamma)  \circ \tilde\gamma\text{.}
\end{eqnarray*}
Summarizing, $\mu$ is a morphism of $\Gamma$-bundles over $\mathcal{P}_0^{[3]}$. The associativity of $\mu$ follows directly from the definitions.
\begin{comment}
Consider a point $(p_1,p_2,p_3,p_4) \in \mathcal{P}_0^{[4]}$, together with elements $(\rho_{ij},g_{ij})\in P$ projecting to $(p_i,p_j)$. We calculate
\begin{eqnarray*}
\mu(\mu((\rho_{34},g_{34}),(\rho_{23},g_{23})) , (\rho_{12},g_{12})) 
&=&  \mu((\rho_{34} \circ R(\rho_{23},\id_{g_{34}^{-1}}),g_{34}g_{23}) , (\rho_{12},g_{12}))
\\&=&  (\rho_{34} \circ R(\rho_{23},\id_{g_{34}^{-1}}) \circ R(\rho_{12},\id_{g_{23}^{-1}g_{34}^{-1}}),g_{34}g_{23}g_{12})
\\&=&   (\rho_{34} \circ R(\rho_{23} \circ R(\rho_{12},\id_{g_{23}^{-1}}),\id_{g_{34}^{-1}}),g_{34}g_{23}g_{12})
\\&=& \mu((\rho_{34},g_{34}), (\rho_{23} \circ R(\rho_{12},\id_{g_{23}^{-1}}),g_{23}g_{12}))
\\&=& \mu((\rho_{34},g_{34}),\mu((\rho_{23},g_{23}) , (\rho_{12},g_{12})))\text{.}
\end{eqnarray*}
\end{comment}
\end{proof}






\subsubsection{Definition of $\mathscr{E}_M$ on 1-morphisms}


We define a 1-morphism $\mathscr{E}_M(F): \mathscr{E}_M(\mathcal{P}) \to \mathscr{E}_M(\mathcal{P}')$ between $\Gamma$-bundle gerbes from a 1-morphism $F: \mathcal{P} \to \mathcal{P}'$ between principal $\Gamma$-2-bundles. The refinement of the surjective submersions $\pi: \mathcal{P} \to M$ and $\pi': \mathcal{P}' \to M$ is the fibre product $Z := \mathcal{P}_0 \times_M \mathcal{P}_0'$. Its principal $\Gamma$-bundle has the total space
\begin{equation*}
Q := F \times \Gamma_0\text{,}
\end{equation*}
and its projection, anchor and $\Gamma$-action are given, respectively, by
\begin{multline}
\label{eq:emorph}
\chi(f,g) := (\alpha_l(f), R(\alpha_r(f),g^{-1}))
\quomma
\alpha(f,g) := g
\quand
(f,g) \circ \gamma := (\rho(f,\id_{g^{-1}}\cdot \gamma),s(\gamma))\text{,}
\end{multline}
where $\rho: F \times \Gamma_1 \to F$ denotes the $\Gamma_1$-action on $F$ that comes from the given $\Gamma$-equivariant structure on $F$ (see Appendix \ref{sec:equivariantanafunctorsandgroupactions}).

\begin{lemma}
This defines a principal $\Gamma$-bundle $Q$ over $Z$. 
\end{lemma}

\begin{proof}
We show first the the projection $\chi:Q \to Z$ is a surjective submersion. Since the  functor $\tau'\maps \mathcal{P}' \nobr\times\nobr \Gamma \to \mathcal{P} \times_M \mathcal{P}$ is a weak equivalence, we have by Theorem \ref{weak} a pullback 
\begin{equation*}
\alxydim{@R=1.3cm}{X \ar[r] \ar[d]_{\xi} & (\mathcal{P}_0' \times \Gamma_0) \lli{R}\times_{t} (\mathcal{P}_1' \times_M \mathcal{P}_1') \ar[d]^{s \circ \mathrm{pr}_2} \\ F \lli{\pi' \circ \alpha_l(f)}\times_{\pi'} \mathcal{P}_0' \ar[r] & \mathcal{P}_0' \times_M \mathcal{P}_0' }
\end{equation*}
along the bottom map $(f,p') \mapsto (\alpha_r(f),p')$, which is well-defined because the anafunctor $F$ preserves the projections to $M$ (see Remark \ref{rem:preserving} \erf{rem:preserving:b}). In particular, the map $\xi$ is a surjective submersion. It is easy to see that the smooth map
\begin{equation*}
k: X \to F \times \Gamma_0: ((f,p'),(p_0',g,\rho,\tilde\rho)) \mapsto (f \circ \rho^{-1} \circ R(\tilde\rho,\id_{g^{-1}}),g^{-1})
\end{equation*}
is surjective.
\begin{comment}
Indeed, the map 
\begin{equation*}
k':F \times\Gamma_0 \to X: (f,g) \mapsto (f,R(\alpha_r(f),g^{-1}),\alpha_r(f),g^{-1},\id_{\alpha_r(f)},\id_{R(\alpha_r(f),g^{-1})})
\end{equation*}
satisfies $k \circ k' = \id$. 
\end{comment}
Now we consider the commutative diagram
\begin{equation*}
\alxydim{@C=1.5cm@R=1.3cm}{X \ar[d]_{\xi} \ar[r]^-{k} & F \times \Gamma_0 \ar[d]^{\chi} \\  F \lli{\pi' \circ \alpha_l(f)}\times_{\pi'} \mathcal{P}_0 \ar[r]_-{\alpha_l \times \id} & \mathcal{P}_0 \times_M \mathcal{P}_0'\text{.}}
\end{equation*}
The surjectivity of $k$ and the fact that $\xi$ and $\alpha_l \times \id$ are surjective submersions shows that $\chi$ is one, too. 


Next, one checks (as in the proof of Lemma \ref{lem:bundleforgerbe}) that the $\Gamma$-action on $Q$ defined above is well-defined and preserves the projection.
\begin{comment}
Suppose $\gamma\in \Gamma_1$ with $t(\gamma) = g = \alpha(f,g)$. Then, $\alpha((f,g)\circ \gamma) = s(\gamma)$ as it should be. If $\gamma_1$ and $\gamma_2$ are composable, we have
\begin{multline*}
((f,g) \circ \gamma_1) \circ \gamma_2 = (\rho(f,\id_{g^{-1}}\cdot \gamma_{1}),s(\gamma_1)) \circ \gamma_2 =(\rho(\rho(f,\id_{g^{-1}}\cdot \gamma_{1}),\id_{s(\gamma_1)^{-1}}\cdot \gamma_2),s(\gamma_2)) \\= (\rho(f,\id_{g^{-1}}\cdot \gamma_{1}\cdot \id_{s(\gamma_1)^{-1}}\cdot \gamma_2),s(\gamma_2))= (\rho(f,\id_{g^{-1}}\cdot (\gamma_1 \circ \gamma_2)),s(\gamma_2)) \end{multline*}
using again  that $\gamma_1 \circ \gamma_2 = \gamma_1 \cdot \id_{s(\gamma_1)^{-1}} \cdot \gamma_2$ in any 2-group. Concerning the projection, we have
\begin{multline*}
\chi((f,g) \circ \gamma) = \chi(\rho(f,\id_{g^{-1}}\cdot \gamma),s(\gamma)))= (\alpha_l(\rho(f,\id_{g^{-1}}\cdot \gamma)), R(\alpha_r(\rho(f,\id_{g^{-1}}\cdot \gamma)),s(\gamma)^{-1})) \\ = (R(\alpha_l(f),g^{-1}t(\gamma)), R(\alpha_r(f),g^{-1}s(\gamma)s(\gamma)^{-1}) =  (\alpha_l(f), R(\alpha_r(f),g^{-1})=\chi(f,g) \text{.}
\end{multline*}
\end{comment}
Then it remains to check that the smooth map
\begin{equation*}
\xi \;:\;\; Q \lli{\alpha}\times_t \Gamma_1 \to Q \times_{\mathcal{P}_0 \times_M \mathcal{P}_0'} Q:(f,g,\gamma) \mapsto (f,g,\rho(f,\id_{g^{-1}}\cdot \gamma),s(\gamma))
\end{equation*}
is a diffeomorphism. An inverse map is given as follows. Given an element $(f_1,g_1,f_2,g_2)$ on the right hand side, we have $\alpha_l(f_1) = \alpha_l(f_2)$, so that there exists a unique element $\rho' \in \mathcal{P}_1'$ such that $f_1 \circ \rho' = f_2$. One calculates that $(\rho',g_2)$ and $(\id_{\alpha_r(f_1)},g_1)$ are elements of the principal $\Gamma$-bundle $\mathcal{P}' \times \Gamma_0$ over $\mathcal{P}_0'^{[2]}$   of Lemma \ref{lem:bundleforgerbe}. Thus, there exists a unique element $\gamma \in \Gamma_1$ such that $(\rho',g_2)=(\id_{\alpha_r(f_1)},g_1) \circ \gamma$. Clearly, $t(\gamma)=g_1$ and $s(\gamma)=g_2$, and we have $\rho' = R(\id_{\alpha_r(f_1)},\id_{g_1^{-1}} \cdot \gamma)$. We define $\xi^{-1}(f_1,g_1,f_2,g_2) := (f_1,g_1,\gamma)$. The calculation that $\xi^{-1}$ is an inverse for $\xi$ uses property (ii) of Definition \ref{def:actionanafunctor} for the action $\rho$, and is left to the reader.
\begin{comment}
Alas, we calculate
\begin{equation*}
\xi(\xi^{-1}(f_1,g_1,f_2,g_2)) = \xi(f_1,g_1,\gamma) = (f_1,g_1,\rho(f_1,\id_{g_1^{-1}}\cdot \gamma),g_2)
\end{equation*}
and are left with showing
\begin{equation*}
\rho(f_1,\id_{g_1^{-1}}\cdot \gamma) = \rho(f_1 \circ \id_{\alpha_r(f_1)},\id_1 \circ (\id_{g_1^{-1}}\cdot \gamma)) \stackrel{\text{(ii)}}{=} \rho(f_1,\id_1) \circ R(\id_{\alpha_r(f_1)},\id_{g_1}^{-1} \cdot \gamma) = f_1 \circ \rho'=f_2\text{.}
\end{equation*}
Conversely, in order to calculate $\xi^{-1}(\xi(f,g,\gamma))$, we define $\rho' := R(\id_{\alpha_r(f)},\id_{g^{-1}} \cdot \gamma)$ and show that $\rho'$ and $\gamma$ have the requested property from the construction of $\xi^{-1}$. Indeed,
\begin{equation*}
f \circ \rho' = f \circ R(\id_{\alpha_r(f)},\id_{g^{-1}} \cdot \gamma) =\rho(f,\id_{g^{-1}}\cdot \gamma) 
\end{equation*}
using the same trick as before, and
\begin{equation*}
(\id_{\alpha_r(f)},g) \circ \gamma = (R(\id_{\alpha_r(f)},\id_{g^{-1}} \cdot \gamma),s(\gamma)) = (\rho',s(\gamma))\text{.}
\end{equation*}
\end{comment}
\end{proof}

The next step in the definition of the 1-morphism $\mathscr{E}(F)$ is to define the bundle morphism
\begin{equation*}
\beta: P' \otimes \zeta_1^{*}Q  \to \zeta_2^{*}Q \otimes P
\end{equation*}
over $Z \times_M Z$. We use the notation of Example \ref{ex:tensorproduct} \erf{ex:tensorproduct:general} for elements of tensor pro\-ducts of principal $\Gamma$-bundles; in this notation, the morphism $\beta$ in the fibre over a point $((p_1,p_1'),(p_2,p_2')) \in Z \times_M Z$ is given by
\begin{equation*}
\beta:((\rho',g'),(f,g),\gamma) \mapsto ((\tilde f,g'gh),(\tilde \rho, h^{-1}),\gamma)\text{,}
\end{equation*}
where $h\in \Gamma_0$ and $\tilde\rho\in \mathcal{P}_1'$ are chosen such that $s(\tilde\rho) = R(p_2,h^{-1})$ and $t(\tilde\rho) = p_1$, and \begin{equation}
\label{eq:ftilde}
\tilde f := \rho(\tilde\rho^{-1} \circ f \circ R(\rho',\id_g),\id_h)\text{.}
\end{equation} 
\begin{comment}
These actions are well-defined because the fibre conditions $\chi(\rho',g') = (p_1',p_2')$ and $\chi(f,g)=(p_1,p_1')$ imply  $t(\rho') = p_1' = R(\alpha_r(f),g^{-1})$ and $\alpha_l(f) = p_1 = t(\tilde\rho)$. 
Also, the fibres are correctly preserved. 
\begin{eqnarray*}
\chi((\tilde f,g'gh)) &=& (\alpha_l(\tilde f),R(\alpha_r(\tilde f),h^{-1}g^{-1}g'^{-1})) \\&=& (R(\alpha_l(\tilde\rho^{-1} \circ f),h), R(\alpha_r(f \circ R(\rho',\id_g)),g^{-1}g'^{-1}))
\\&=& (R(s(\tilde\rho),h), R( s(\rho'),g'^{-1}))
\\&=& (p_{2}, p_{2}')
\end{eqnarray*}
and $\chi(\tilde \rho, h^{-1}) = (t(\tilde\rho),R(s(\tilde\rho),h)) = (p_1,p_2)$.
Finally, there is the condition $t(\gamma) = g'g$ for representatives in the tensor product, and the corresponding condition in the image of $\beta$ is $t(\gamma) = g'ghh^{-1}=g'g$ and thus satisfied. 
\end{comment}

\begin{lemma}
\label{lem:eonemorphisms}
This defines an isomorphism between principal $\Gamma$-bundles. 
\end{lemma}

\begin{proof}
The existence of  choices of $\tilde \rho,h$ follows because the  functor $\tau': \mathcal{P}' \times\Gamma \to \mathcal{P}' \times_M \mathcal{P}'$ is smoothly essentially surjective (Theorem \ref{weak}); in particular, one can choose them locally in a smooth way. We claim that the equivalence relation on $\zeta_2^{*}Q \otimes P$ identifies different choices; thus, we have a well-defined smooth map. In order to prove this claim, we assume other choices $\tilde\rho',h'$. The pairs $(\tilde\rho,h^{-1})$ and $(\tilde\rho',h'^{-1})$ are elements in the principal $\Gamma$-bundle $P'$ over $\mathcal{P}_0' \times_M \mathcal{P}_0'$ and sit over the same fibre; thus, there exists a unique $\tilde\gamma\in \Gamma_1$ such that $(\tilde\rho,h^{-1}) \circ \tilde\gamma = (\tilde\rho',h'^{-1})$, in particular, $R(\tilde\rho,\id_{h}\cdot \tilde\gamma) = \tilde\rho'$. Now we have
\begin{multline*}
((\tilde f,g'gh),(\tilde \rho, h^{-1}),\gamma) = ((\tilde f,g'gh),(\tilde \rho, h^{-1}),(\id_{t(\gamma)} \cdot i(\tilde\gamma)\cdot \tilde \gamma) \circ \gamma) \sim((\tilde f,g'gh) \circ (\id_{t(\gamma)} \cdot i(\tilde\gamma)),(\tilde \rho, h^{-1}) \circ \tilde \gamma,\gamma) 
\end{multline*}
so that it suffices to calculate
\begin{eqnarray*}
(\tilde f,g'gh) \circ (\id_{t(\gamma)} \cdot i(\tilde\gamma))
&=& (\rho(\tilde f,\id_{h^{-1}}\cdot i(\tilde \gamma)),g'gh')
\\&=& (\rho(\tilde\rho^{-1} \circ f \circ R(\rho',\id_g),i(\tilde\gamma)), g'gh')
\\&=& (\rho(R(\tilde\rho^{-1},i(\tilde\gamma)\cdot\id_{h'^{-1}}) \circ f \circ R(\rho',\id_g),\id_{h'}), g'gh')\text{,}
\end{eqnarray*} 
where the last step uses the compatibility condition for $\rho$ from Definition \ref{def:actionanafunctor} (ii). In any 2-group, we have $i(\tilde\gamma)\cdot\id_{s(\tilde\gamma)} = (\id_{t(\tilde\gamma)^{-1}} \cdot \tilde\gamma)^{-1}$, in which case the last line is exactly the formula \erf{eq:ftilde} for the pair $(\tilde\rho',h')$. \begin{comment}
This rule follows from the calculation
\begin{equation*}
(\id_{t(\tilde\gamma)^{-1}}\cdot \tilde\gamma)^{-1} \cdot (\id_{s(\tilde\gamma)} \cdot \tilde\gamma) = \id_1
\end{equation*}
that can easily been shown using formula $\gamma_1 \circ \gamma_2 = \gamma_1 \cdot \id_{s(\gamma_1)^{-1}} \cdot \gamma_2$ that was proved above. 
\end{comment}

Next we check that $\beta$ is well-defined under the equivalence relation on the tensor product $P' \otimes \zeta_1^{*}Q$. We have
\begin{equation*}
x:=((\rho',g'),(f,g),(\gamma_1\cdot\gamma_2) \circ \gamma) \sim ((\rho',g') \circ \gamma_1,(f,g) \circ \gamma_2,\gamma) =: x'
\end{equation*}
for $\gamma_1,\gamma_2 \in \Gamma_1$ such that $t(\gamma_1)=g'$, $t(\gamma_2) = g$ and $s(\gamma_1)s(\gamma_2) = t(\gamma)$. Taking advantage of the fact that we can make the same choice of $(\tilde\rho,h)$ for both representatives $x$ and $x'$, it is straightforward to show that $\beta(x) = \beta(x')$. \begin{comment}
Indeed,
\begin{eqnarray*}
\beta(x) 
&=& (\rho(\tilde\rho^{-1} \circ f\circ R(\rho',\id_g),\id_h),g'gh,\tilde\rho,h^{-1}, (\gamma_1 \cdot\gamma_2) \circ \gamma)
\\&\sim& (\rho(\tilde\rho^{-1} \circ f \circ R(\rho',\id_{g}), \id_{g^{-1}g'^{-1}}\cdot \gamma_1 \cdot \gamma_2\cdot \id_{h}), t(\gamma)h,\tilde\rho,h^{-1},\gamma )
\\&=& (\rho(\tilde\rho^{-1} \circ \rho(f,\id_{g^{-1}}\cdot\gamma_2) \circ R(\rho',\id_{g'^{-1}}\cdot\gamma_1\cdot\id_{s(\gamma_2)}),\id_h),s(\gamma_1)s(\gamma_2)h,\tilde\rho,h^{-1},\gamma)
\\&=& \beta(x')
\end{eqnarray*}
where the last but one step uses  Definition \ref{def:actionanafunctor} (b) and some algebra in the 2-group $\Gamma$, namely that

\begin{equation*}
\id_1 \circ (\id_{g^{-1}} \cdot \gamma_2) \circ (\id_{g^{-1}g'^{-1}} \cdot \gamma_1 \cdot \id_{s(\gamma_2)}) =  \id_{g^{-1}g'^{-1}}\cdot \gamma_1 \cdot \gamma_2\text{.}
\end{equation*}
\end{comment}
Finally, it is obvious from the definition of $\beta$ that it is anchor-preserving and $\Gamma$-equivariant.
\end{proof}

In order to show that the triple $(Z,Q,\beta)$ defines a 1-morphism between bundle gerbes, it remains to verify that the bundle isomorphism $\beta$ is compatible the with the bundle gerbe products $\mu_1$ and $\mu_2$ in the sense of diagram \erf{compgerbemorph}. This is straightforward to do and left for the reader. 


\begin{comment}
We start with an element in $\pi_{23}^{\prime*}P' \otimes \pi_{12}^{\prime*}P' \otimes \zeta_1^{*}Q$. In order to go counter-clockwise around the diagram we need to choose pairs $(\rho_{12},h_{12})$ and $(\rho_{23},h_{23})$. For the clockwise direction, we can then choose $\rho_{13} := \rho_{12} \circ R(\rho_{23},\id_{h_{12}^{-1}})$ and $h_{13} := h_{12}h_{23}$. Then, we get in the counter-clockwise direction:
\begin{eqnarray*}
&&\hspace{-2cm}(\id \otimes \mu)((\zeta_{23}^{*}\beta \otimes \id)((\id \otimes \zeta_{12}^{*}\beta)((((\rho_{23}',g_{23}'),(\rho_{12}',g_{12}'),(f,g)))) 
\\&=& (\id \otimes \mu)((\zeta_{23}^{*}\beta \otimes \id)(((\rho_{23}',g_{23}'),(\rho(\rho^{-1}_{12} \circ f \circ R(\rho_{12}',\id_g),\id_{h_{12}}),\\&&\hspace{2cm}g_{12}'gh_{12}),(\rho_{12},h_{12}^{-1}))) \\&=& (\id \otimes \mu)(\rho(\rho_{23}^{-1} \circ \rho(\rho^{-1}_{12} \circ f \circ R(\rho_{12}',\id_g),\id_{h_{12}}) \circ R(\rho_{23}',\id_{g_{12}'gh_{12}}),\id_{h_{23}}),\\&&\hspace{2cm}g_{23}'g_{12}'gh_{12}h_{23}),(\rho_{23},h_{23}^{-1}),(\rho_{12},h_{12}^{-1})) \\&=& (\rho(\rho_{13}^{-1} \circ f \circ  R(\rho_{12}',\id_{g}) \circ R(\rho_{23}',\id_{g_{12}'g}),\id_{h_{13}}),g_{23}'g_{12}'gh_{13}),(\rho_{13},h_{13}^{-1}))\text{,} \end{eqnarray*}
where the last step uses Definition \ref{def:actionanafunctor} (ii). In the clockwise direction, we get
\begin{eqnarray*}
&&\hspace{-2cm}\zeta_{13}^{*}\beta((\mu'\otimes \id)((\rho_{23}',g_{23}'),(\rho_{12}',g_{12}'),(f,g)))
\\&=& \zeta_{13}^{*}\beta((\rho_{12}' \circ R(\rho_{23}',\id_{g_{12}'}),g_{23}'g_{12}'),(f,g))
\\&=& (\rho(\rho_{13}^{-1} \circ f \circ  R(\rho_{12}' \circ R(\rho_{23}',\id_{g_{12}'}),\id_g),\id_{h_{13}}),g_{23}'g_{12}'gh_{13}),(\rho_{13},h_{13}^{-1}))\text{.}
\end{eqnarray*}
Up to a straightforward manipulation, the two results coincide. 
\end{comment}




\subsubsection{Definition of $\mathscr{E}_M$ on 2-morphisms, compositors and unitors}


Let $F_1,F_2: \mathcal{P} \to \mathcal{P}'$ be 1-morphisms between principal $\Gamma$-bundles over $M$, and let $\eta: F \Rightarrow G$ be a 2-morphism. Between the $\Gamma$-bundles $Q_1$ and $Q_2$, which live over the same common refinement $Z = \mathcal{P}_0 \times_M \mathcal{P}_0'$, we find immediately the smooth map
\begin{equation*}
\eta: Q_1 \to Q_2: (f_1,g) \mapsto (\eta(f_1),g)
\end{equation*}
which is easily verified to be a bundle morphism. 
\begin{comment}
Indeed, the bundle projection is respected because $\eta$ preserves the anchors. For the $\Gamma$-action, we calculate
\begin{equation*}
\eta((f_1,g)\circ \gamma)= \eta(\rho_1(f_1,\id_{g^{-1}}\cdot \gamma),s(\gamma)) =(\rho_2(\eta(f_1),\id_{g^{-1}} \cdot \gamma), s(\gamma)) = \eta(f_1,g) \circ \gamma\text{.}
\end{equation*}
\end{comment}
Its compatibility with the bundle morphisms $\beta_1$ and $\beta_2$ in the sense of the simplified diagram \erf{eq:comp2morphsimple} is also easy to check.
\begin{comment}
The calculation is over a point $((p_1,p_1'),(p_2,p_2'))\in Z^{[2]}$, so we may choose once a pair $(\tilde \rho,h)$ needed to perform the isomorphisms $\beta$. Then, we calculate
\begin{eqnarray*}
(\zeta_2^{*}\eta \otimes \id)(\beta_{1}((\rho',g'),(f,g),\gamma)) &=& (\zeta_2^{*}\eta \otimes \id)((\rho_1(\tilde\rho^{-1} \circ f \circ R(\rho',\id_g),\id_h),g'gh),(\tilde \rho, h^{-1}),\gamma)
\\&=& ((\eta(\rho_1(\tilde\rho^{-1} \circ f \circ R(\rho',\id_g),\id_h)),g'gh),(\tilde \rho, h^{-1}),\gamma)
\\&=& ((\rho_2(\tilde\rho^{-1} \circ \eta(f) \circ R(\rho',\id_g),\id_h)),g'gh),(\tilde \rho, h^{-1}),\gamma)
\\&=& \beta_2 ((\rho',g'),(\eta(f),g),\gamma)
\\&=& \beta_2 ((\id \otimes \zeta_1^{*}\eta)((\rho',g'),(f,g),\gamma))
\end{eqnarray*}
using that $\eta$ respects the actions on the total space of the anafunctors as well as the $\Gamma_1$-actions $\rho_1$ and $\rho_2$. 
\end{comment}
Thus, we have defined a 2-morphism $\mathscr{E}_M(\eta)\maps \mathscr{E}_M(F_1) \Rightarrow \mathscr{E}_M(F_2)$.



The compositor for  1-morphisms $F_1: \mathcal{P} \to \mathcal{P}'$ and $F_2: \mathcal{P}' \to \mathcal{P}''$ is a bundle gerbe 2-morphism 
\begin{equation*}
c_{F_1,F_2} : \mathscr{E}_M(F_2 \circ F_1) \to \mathscr{E}_M(F_2) \circ \mathscr{E}_M(F_1)\text{.}
\end{equation*}
Employing the above constructions, the 1-morphism $\mathscr{E}_M(F_2 \circ F_1)$ is defined on the common refinement $Z_{12} \df \mathcal{P}_0 \times_M \mathcal{P}_0''$ and has the $\Gamma$-bundle $Q_{12} = (F_1 \times_{\mathcal{P}_0'} F_2)/\mathcal{P}_1' \times \Gamma_0$, whereas the 1-morphism $\mathscr{E}_M(F_2) \circ \mathscr{E}_M(F_1)$ is defined on the common refinement $Z :=\mathcal{P}_0 \times_M \mathcal{P}_0' \times_M \mathcal{P}_0''$ and has the $\Gamma$-bundle $Q_2 \otimes Q_1$ with $Q_k = F_k \times \Gamma_0$. The compositor $c_{F_1,F_2}$ is defined over the refinement $Z$ with the obvious refinement maps  $\mathrm{pr}_{13}:Z \to Z_{12}$ and $\id:Z \to Z$ making diagram \erf{diag:refinement} commutative. It is thus a  bundle morphism $c_{F_1,F_2}: \mathrm{pr}_{13}^{*}Q_{12} \to Q_2 \otimes Q_1$. For elements in a tensor product of $\Gamma$-bundles we use the notation of Example \ref{ex:tensorproduct} \erf{ex:tensorproduct:general}. Then, we define $c_{F_1,F_2}$ by
\begin{equation}
\label{eq:assignmentcompositor}
((p,p',p''),(f_1,f_2,g)) \mapsto ((\rho_2(\tilde\rho^{-1} \circ f_2,\id_h),gh),(f_1 \circ \tilde \rho,h^{-1}),\id_g)\text{,}
\end{equation}
where $h\in \Gamma_0$  and $\tilde\rho: R(p',h^{-1}) \to \alpha_r(f_1)=\alpha_l(f_2)$ are chosen in the same way as in the proof of Lemma \ref{lem:eonemorphisms}. \begin{comment}
It is straightforward to see that this lands in the correct fibres: since we started with $p=\alpha_l(f_1)$ and $p'' = R(\alpha_r(f_2),g^{-1})$, we have
\begin{eqnarray*}
\alpha_l(f_1 \circ \tilde \rho) = \alpha_l(f_1) &=& p
\\
\alpha_l(\rho_2(\tilde\rho^{-1} \circ f_2,\id_h)) = R(\alpha_l(\tilde\rho^{-1} \circ f_2),h)= R(s(\tilde\rho),h) &=& p'
\\
R(\alpha_r(f_1 \circ \tilde \rho),h) = R(s(\tilde \rho),h)   &=& p'
\\
R(\alpha_r(\rho_2(\tilde\rho^{-1} \circ f_2,\id_h)),h^{-1}g^{-1}) = R(\alpha_r(f_2),g^{-1}) &=& p''
\\
gh \cdot h^{-1} &=& t(\id_g)\text{.}
\end{eqnarray*}
\end{comment}
The assignment \erf{eq:assignmentcompositor} does not depend on the choices of $h$ and $\tilde\rho$, nor on the choice of the representative $(f_1,f_2)$ in $(F_1 \times_{\mathcal{P}_0'} F_2)/\mathcal{P}_1' $. 
\begin{comment}
We prove this in one step by assuming equivalent representatives 
\begin{equation*}
(f_1 \circ \rho,f_2) \sim (f_1,\rho \circ f_2)
\end{equation*}
and choosing unrelated $(h_1,\tilde\rho_1)$ and $(h_2,\tilde\rho_2)$. It follows that $s(\rho) = \alpha_l(f_2)=t(\tilde\rho_1)$ and $t(\rho) = \alpha_r(f_1) = t(\tilde\rho_2)$. Now we look at the bijection that the smooth functor $\tau'$ induces on Hom-sets:
\begin{equation*}
\tau': \hom{(p',h_1^{-1})}{(p',h_2^{-1})} \to \hom{(p',R(p',h_1^{-1}))}{(p',R(p',h_2^{-1}))}\text{.}
\end{equation*}
On the right hand side, we have the element $(\id_{p'},\tilde\rho_2^{-1} \circ \rho \circ \tilde\rho_1)$, and the corresponding unique element on the left hand side must be of the form $(\id_{p'},\gamma)$, for some $\gamma \in \Gamma_1$ with $R(\id_{p'},\gamma) = \tilde\rho_2^{-1} \circ \rho \circ \tilde\rho_1$. Now we calculate:
\begin{eqnarray*}
&&\hspace{-2cm}c_{F_1,F_2}((p,p',p''),(f_1 \circ \rho,f_2)) 
\\&=& ((\rho_2(\tilde\rho_1^{-1} \circ f_2,\id_{h_1}),gh_1),(f_1 \circ \rho \circ \tilde \rho_1,h_1^{-1}), ((\id_g \cdot i(\gamma^{-1})) \cdot \gamma^{-1}) \circ \id_g) 
\\&=& ((\rho_2(\tilde\rho_1^{-1} \circ f_2,\id_{h_1}),gh_1) \circ (\id_g \cdot i(\gamma^{-1})),(f_1 \circ \rho \circ \tilde \rho_1,h_1^{-1}) \circ \gamma^{-1},  \id_g) 
\\&=& ((\rho_2(R(\id_{p'},\gamma^{-1}) \circ \tilde\rho_2^{-1} \circ \rho \circ f_2,i(\gamma^{-1}) \circ \id_{h_2}),gh_2) ,\\&&\hspace{2cm}(\rho_1(f_1 \circ \tilde\rho_2 \circ R(\id_{p'},\gamma),\id_1 \circ (\id_{h_1}\cdot\gamma^{-1})),h_2^{-1}),  \id_g) 
\\&=& ((R(\id_{p'},\gamma^{-1} \cdot i(\gamma^{-1})) \circ \rho_2(\tilde\rho_2^{-1} \circ \rho \circ f_2,\id_{h_2}),gh_2) , \\ && \hspace{2cm}(\rho_1(f_1 \circ \tilde\rho_2,\id_1)  \circ R(\id_{p'},\gamma \cdot (\id_{h_1}\cdot\gamma^{-1})),h_2^{-1}),  \id_g) 
\\&=& (\rho_2(\tilde\rho_2^{-1} \circ \rho \circ f_2,\id_{h_2}),gh_2,f_1  \circ \tilde\rho_2,h_2^{-1},\id_g)
\\&=& c_{F_1,F_2}((p,p',p''),(f_1,\rho \circ f_2))\text{.}
\end{eqnarray*}
In the middle we have used that $\gamma \cdot (\id_{h_1}\cdot\gamma^{-1}) = \id_{h_2^{-1}}$. 
\end{comment}
It is obvious that \erf{eq:assignmentcompositor} is anchor-preserving, and its $\Gamma$-equivariance can be seen by choosing $(\tilde\rho,h)$ in order to compute $c_{F_1,F_2}((p,p',p''),(f_1,f_2,g))$  and $(\tilde\rho',h)$ with $\tilde\rho' := R(\tilde\rho,\id_{g^{-1}} \cdot \gamma^{-1})$ in order to compute $c_{F_1,F_2}(((p,p',p''),(f_1,f_2,g)) \circ \gamma)$.
\begin{comment} 
Indeed,
\begin{eqnarray*}
&& \hspace{-2cm} c_{F_1,F_2}(((p,p',p''),(f_1,f_2,g)) \circ \gamma) 
\\ &=&  c_{F_1,F_2}((p,p',p''),(\rho_1(f_1,\id_{g^{-1}} \cdot \gamma),\rho_2(f_2,\id_{g^{-1}s(\gamma)}),s(\gamma)))
\\ &=&  (\rho_2(\tilde\rho'^{-1} \circ \rho_2(f_2,\id_{g^{-1}s(\gamma)}),\id_{h}),s(\gamma)h,\rho_1(f_1,\id_{g^{-1}} \cdot \gamma) \circ \tilde\rho',h^{-1},\id_{s(\gamma)})
\\&=&
(\rho_2(\tilde\rho^{-1} \circ f_2,\id_{g^{-1}} \cdot \gamma \cdot \id_h),s(\gamma)h,f_1 \circ \tilde\rho,h^{-1},\id_{s(\gamma)})
\\&=& (\rho_2(\tilde\rho^{-1} \circ f_2,\id_h),gh,f_1 \circ \tilde\rho,h^{-1},\gamma)
\\&=& c((p,p',p''),(f_1,f_2,g)) \circ \gamma\text{.}
\end{eqnarray*}
\end{comment}
In order to complete the construction of the bundle gerbe 2-morphism $c_{F_1,F_2}$ we have to prove that the bundle morphism $c_{F_1,F_2}$ is compatible with the isomorphisms $\beta_{12}$ of $\mathscr{E}_M(F_2 \circ F_1)$ and $(\id \otimes \beta_{1}) \circ (\beta_2 \otimes \id)$ of $\mathscr{E}_M(F_2) \circ \mathscr{E}_M(F_1)$ in the sense of diagram \erf{eq:comp2morphsimple}. We start with an element $((\rho'',g''),(f_{12},g)) \in \mathscr{E}_M(\mathcal{P}'') \otimes \zeta_1^{*}Q_{12}$, where $f_{12} = (f_1,f_2)$. We have
\begin{equation*}
\beta_{12}((\rho'',g''),(f_{12},g)) = (\widetilde{f_{12}},g''gh,\tilde \rho,h^{-1})
\end{equation*}
upon choosing $(\tilde \rho,h)$ as required in the definition of $\mathscr{E}_M(F_2 \circ F_1)$. Writing $\widetilde{f_{12}}=(\tilde f_1,\tilde f_2)$ further we have
\begin{equation}
\label{eq:prop719eq1}
(\zeta_2^{*}c_{F_1,F_2} \otimes \id)(\widetilde{f_{12}},g''gh,\tilde \rho,h^{-1}) = (\rho_2(\tilde\rho_2^{-1} \circ \tilde f_2,\id_{h_2}),g''ghh_2,\tilde f_1 \circ \tilde \rho_2,h_2^{-1},\tilde\rho,h^{-1})
\end{equation}
upon choosing appropriate $(\tilde\rho_2,h_2)$ as required in the definition of $c_{F_1,F_2}$. This is the result of the clockwise composition of diagram \erf{eq:comp2morphsimple}. Counter-clockwise, we first get
\begin{equation*}
(\id \otimes \zeta_1^{*}c_{F_1,F_2})((\rho'',g''),(f_{12},g)) = (\rho'',g'',f'',gh_1,f',h_1^{-1})
\end{equation*}
for choices $(\tilde\rho_1,h_1)$, where $f'' := \rho_2(\tilde\rho_1^{-1} \circ f_2 , \id_{h_1})$ and $f' := f_1 \circ \tilde \rho_1$. Next we apply the isomorphism $\beta_2$ of $\mathscr{E}_M(F_2)$ and get 
\begin{equation*}
(\beta_2 \otimes \id)(\rho'',g'',f'',gh_1,f'_1,h_1^{-1}) = (\widetilde {f''},g''ghh_2,\hat\rho,\hat h^{-1},f_1',h_1^{-1})
\end{equation*}
where we have used the choices $(\hat\rho,\hat h)$ defined by $\hat\rho := R(\tilde\rho_1^{-1},h_1) \circ R(\tilde\rho_2,h^{-1}h_1)$ and $\hat h := h_1^{-1}hh_2$. The last step is to apply the isomorphism $\beta_1$ of  $\mathscr{E}_M(F_2)$  which gives
\begin{equation}
\label{eq:prop719eq2}
(\id \otimes \beta_1)(\widetilde {f''},g''ghh_2,\hat\rho,\hat h^{-1},f_1',h_1^{-1}) = (\widetilde{f''},g''ghh_2,\widetilde{f'},h_2^{-1},\tilde\rho,h^{-1})\text{,}
\end{equation}
where we have used the choices $(\tilde\rho,h)$ from above. Comparing \erf{eq:prop719eq1} and \erf{eq:prop719eq2}, we have obvious coincidence in all but the first and the third components. For these remaining factors, coincidence follows from the definitions of the various variables.
\begin{comment}
The calculation
\begin{equation*}
\widetilde{f_{12}} = (\rho_1(\tilde\rho^{-1} \circ f_1,\id_h),\rho_2(f_2 \circ R(\rho'',\id_g),\id_h))
\end{equation*}
identifies what $\tilde f_1$ and $\tilde f_2$ are. 
Then we calculate
\begin{eqnarray*}
\widetilde{f'} &=& \rho_1(\tilde \rho^{-1} \circ f_1 \circ \tilde \rho_1 \circ R(\hat\rho,\id_{h_1^{-1}}),\id_h)
\\&=& \rho_1(\tilde\rho^{-1} \circ f_1 \circ R(\tilde \rho_2,h^{-1}),\id_{h})
\\&=& \tilde f_1 \circ \tilde \rho_2\text{.}
\\\widetilde{f''} &=& \rho_2(R(\tilde\rho_2^{-1},\id_{h^{-1}h_1}) \circ R(\tilde\rho_1,\id_{h_1}) \circ \rho_2(\tilde\rho_1^{1} \circ f_2 , \id_{h_1}) \circ R(\rho'',\id_{gh_1}),\id_{h_1^{-1}hh_2})
\\&=& \rho_2(\tilde\rho_2^{-1} \circ \rho_2(f_2,\id_h) \circ R(\rho'',\id_{gh}),\id_{h_2})
\\&=& \rho_2(\tilde\rho_2^{-1} \circ \tilde f_2,\id_{h_2})\text{.}
\end{eqnarray*}
This shows the claimed coincidence. 
\end{comment}


Finally, we have to construct unitors. The unitor for a principal $\Gamma$-2-bundle $\mathcal{P}$ over $M$ is a bundle gerbe 2-morphism
\begin{equation*}
u_{\mathcal{P}}: \mathscr{E}_M(\id_{\mathcal{P}}) \Rightarrow \id_{\mathscr{E}_M(\mathcal{P})}\text{.}
\end{equation*}
Abstractly, one can associate to $\id_{\mathscr{E}_M(\mathcal{P})}$ the 1-morphism $\id_{\mathscr{E}_M(\mathcal{P})}^{FP}$ constructed in the proof of Lemma  \ref{lem:canonicalrefinement}, and then notice that $\id_{\mathscr{E}_M(\mathcal{P})}^{FP}$ and $\mathscr{E}_M(\id_{\mathcal{P}})$ are canonically 2-isomorphic. In more concrete terms, the unitor $u_{\mathcal{P}}$ has the refinement $W := \mathcal{P}_0^{[3]}$ with the surjective submersions $r := \mathrm{pr}_{12}$ and $r' := \mathrm{pr}_{3}$ to the refinements $Z=\mathcal{P}_0^{[2]}$ and $Z'= \mathcal{P}_0$ of the 1-morphisms $\mathscr{E}_M(\id_{\mathcal{P}})$ and $\id_{\mathscr{E}_M(\mathcal{P})}$, respectively. The relevant maps $x_W$ and $y_W$ are $\mathrm{pr}_{13}$ and $\mathrm{pr}_{23}$, respectively. The principal $\Gamma$-bundle of the 1-morphism $\id_{\mathscr{E}_M(\mathcal{P})}$ is the trivial bundle $Q' = \trivlin_1$. We claim that the principal $\Gamma$-bundle $Q$ of $\mathscr{E}_M(\id_{\mathcal{P}})$ is the bundle $P$ of the bundle gerbe $\mathscr{E}_M(\mathcal{P})$. Indeed, the formulae \erf{eq:emorph} reduce for the identity anafunctor $\id_{\mathcal{P}}$ to those of \erf{defgerbefrombundle}. Now, the bundle isomorphism of the unitor $u_{\mathcal{P}}$ is
\begin{equation*}
\alxydim{}{y_W^{*}P \otimes r^{*}Q = \mathrm{pr}_{23}^{*}P \otimes \mathrm{pr}_{12}^{*}P \ar[r]^-{\mu} & \mathrm{pr}_{13}^{*}P \cong {r'}^{*}Q' \otimes x_W^{*}P\text{,} }
\end{equation*}
where $\mu$ is the bundle gerbe product of $\mathscr{E}_M(\mathcal{P})$. The commutativity of diagram \erf{eq:comp2morphcomplicated} follows from the associativity of $\mu$.



\begin{proposition}
\label{prop:efunctor}
The assignments $\mathscr{E}_M$ for objects, 1-morphisms  and 2-morphisms, together with the compositors and unitors defined above, define a 2-functor
\begin{equation*}
\mathscr{E}_M: \zwoabun \Gamma M \to \grb\Gamma M\text{.}
\end{equation*}
\end{proposition}


\begin{proof}
A list of axioms for a 2-functor with the same conventions as we use here can be found in \cite[Appendix A]{schreiber2}. The first axiom  requires that the 2-functor $\mathscr{E}_M$ respects the vertical composition of 2-morphisms -- this follows immediately from the definition. 

The second axiom requires that the compositors respect the horizontal composition of 2-morphisms. To see this, let $F_1,F_1': \mathcal{P} \to \mathcal{P}'$  and $F_2,F_2': \mathcal{P}' \to \mathcal{P}''$ be 1-morphisms between principal $\Gamma$-2-bundles, and let $\eta_1: F_1 \Rightarrow F_1'$ and $\eta_2: F_2 \Rightarrow F_2'$ be 2-morphisms. Then, the diagram
\begin{equation*}
\alxydim{@C=3cm@R=1.3cm}{\mathscr{E}_M(F_2 \circ F_1) \ar@{=>}[d]_{c_{F_1,F_2}} \ar@{=>}[r]^{\mathscr{E}_M(\eta_1 \circ \eta_2)} & \mathscr{E}_M(F_2' \circ F_1') \ar@{=>}[d]^{c_{F_1',F_2'}} \\ \mathscr{E}_M(F_2) \circ \mathscr{E}_M(F_1) \ar@{=>}[r]_{\mathscr{E}_M(\eta_1) \circ \mathscr{E}_M(\eta_2)} & \mathscr{E}_M(F_2') \circ \mathscr{E}_M(F_1')}
\end{equation*}
has to commute. Indeed, in order to compute $c_{F_1,F_2}$ and $c_{F_1',F_2'}$ one can make the same choice of $(\tilde\rho,h)$, because the transformations $\eta$ and $\eta_2$ preserve the anchors. Then, commutativity follows  from the fact that  $\eta_1$ and $\eta_2$ commute with the groupoid actions and the $\Gamma_1$-action according to Definition \ref{def:actionanafunctor}. 

The third axiom describes the compatibility of the compositors with the composition of 1-morphisms in the sense that the diagram
\begin{equation*}
\alxydim{@C=1.8cm@R=1.3cm}{\mathscr{E}_M(F_3 \circ F_2 \circ F_1) \ar@{=>}[r]^-{c_{F_2 \circ F_1,F_3}}  \ar@{=>}[d]_{c_{F_3 \circ F_2, F_1}} & \mathscr{E}_M(F_3) \circ \mathscr{E}_M(F_2 \circ F_1) \ar@{=>}[d]^{\id \circ c_{F_2,F_1}} \\ \mathscr{E}_M(F_3 \circ F_2) \circ \mathscr{E}_M(F_1) \ar@{=>}[r]_-{c_{F_3,F_2} \circ \id} & \mathscr{E}_M(F_3) \circ \mathscr{E}_M(F_2) \circ \mathscr{E}_M(F_1)\text{.}}
\end{equation*}
is commutative. In order to verify this, one starts with an element $(f_1,f_2,f_3,g)$ in $\mathscr{E}_M(F_3 \circ F_2 \circ F_1)$. In order to go clockwise, one chooses pairs $(\tilde \rho_{12,3},h_{12,3})$ and $(\tilde\rho_{1,2},h_{1,2})$ and gets from the definitions
\begin{equation*}
\mathrm{CW} = ((\rho_3(\tilde\rho_{12,3}^{-1} \circ f_3,\id_{h_{12,3}}),gh_{12,3}),(\rho_2(\tilde\rho_{1,2}^{-1} \circ f_2 \circ \tilde\rho_{12,3},\id_{h_{1,2}}),h_{12,3}^{-1}h_{1,2}),(f_1 \circ \tilde\rho_{1,2},h^{-1}_{1,2}))\text{.}
\end{equation*}
Counter-clockwise, one can choose firstly again the pair $(\tilde \rho_{1,2},h_{1,2})$ and then the pair $(\tilde\rho_{2,3},h_{2,3})$ with $\tilde\rho_{2,3} \eq R(\tilde\rho_{12,3},\id_{h_{1,2}})$ and $h_{2,3} = h^{-1}_{1,2}h_{12,3}$. Then, one gets
\begin{multline*}
\mathrm{CCW} = ((\rho_3(\tilde\rho_{2,3}^{-1} \circ \rho_3(f_3,\id_{h_{1,2}}),\id_{h_{2,3}}),gh_{1,2}h_{2,3}),(\rho_2(\tilde\rho_{1,2}^{-1} \circ f_2,\id_{h_{1,2}}) \circ \tilde\rho_{2,3},h_{2,3}^{-1}),(f_1 \circ \tilde\rho_{1,2},h^{-1}_{1,2}))\text{,}
\end{multline*}
where one has to use formula \erf{eq:companafunctorsaction} for the $\Gamma_1$-action on the composition of equivariant anafunctors.
Using the definitions of $h_{2,3}$ and $\tilde\rho_{2,3}$ as well as the axiom of Definition \ref{def:actionanafunctor} (ii) one can show that $\mathrm{CW}=\mathrm{CCW}$.

The fourth and last axiom requires that compositors and unitors are  compatible with each other in the sense that for each 1-morphism $F: \mathcal{P} \to \mathcal{P}'$ the 2-morphisms
\begin{equation*}
\alxydim{@C=1.5cm}{\mathscr{E}_M(F) \cong \mathscr{E}_M(F \circ \id_{\mathcal{P}}) \ar@{=>}[r]^-{c_{\id_{\mathcal{P}},F}} & \mathscr{E}_M(F) \circ \mathscr{E}_M(\id_{\mathcal{P}}) \ar@{=>}[r]^-{\id \circ u_{\mathcal{P}}} & \mathscr{E}_M(F) \circ \id_{\mathscr{E}_M(\mathcal{P})} \cong \mathscr{E}_M(F)}
\end{equation*}
and   
\begin{equation*}
\alxydim{@C=1.3cm}{\mathscr{E}_M(F) \cong \mathscr{E}_M(\id_{\mathcal{P'}} \circ F) \ar@{=>}[r]^-{c_{F,\id_{\mathcal{P'}}}} & \mathscr{E}_M(\id_{\mathcal{P'}}) \circ \mathscr{E}_M(F) \ar@{=>}[r]^-{ u_{\mathcal{P}'} \circ \id} & \id_{\mathscr{E}_M(\mathcal{P}')} \circ \mathscr{E}_M(F) \cong \mathscr{E}_M(F)}
\end{equation*}
are the identity 2-morphisms. We prove this for the first one and leave the second as an exercise. Using the definitions, we see that the 2-morphism has the refinement $W := \mathcal{P}_0 \times_M \mathcal{P}_0 \times_M \mathcal{P}_0'$ with $r = \mathrm{pr}_{13}$ and $r' = \mathrm{pr}_{23}$. The maps $x_W: W \to \mathcal{P}_0 \times_M \mathcal{P}_0$ and $y_W: W \to \mathcal{P}_0' \times_M \mathcal{P}_0'$ are $\mathrm{pr}_{12}$ and $\Delta \circ \mathrm{pr}_3$, respectively, where $\Delta$ is the diagonal map. Its bundle morphism is
a morphism
\begin{equation*}
\varphi : \mathrm{pr}_{13}^{*}Q \to \mathrm{pr}_{23}^{*}Q \otimes \mathrm{pr}_{12}^{*}P\text{,}
\end{equation*}
where $Q = F \times \Gamma_0$ is the principal $\Gamma$-bundle of $\mathscr{E}_M(F)$, and  $P=\mathcal{P}_1 \times \Gamma_0$ is the principal $\Gamma$-bundle of $\mathscr{E}_M(\mathcal{P})$. Over a point $(p_1,p_2,p')$ and $(f,g)\in \mathrm{pr}_{13}^{*}Q$, i.e. $\alpha_l(f)=p_1$ and $R(\alpha_r(f),g^{-1})=p'$, the bundle morphism $\varphi$ is given by
\begin{equation*}
 (f,g) \mapsto (\rho(\tilde\rho^{-1} \circ f,\id_h),gh,\tilde\rho,h^{-1})\text{,}
\end{equation*}
where $h \in \Gamma_0$, and $\tilde\rho \in \mathcal{P}_1$ with $s(\tilde\rho) = R(p_2,h^{-1})$ and $t(\tilde\rho) = \alpha_l(f)$. We have to compare $(W,\varphi)$ with the identity 2-morphism of $\mathscr{E}_M(F)$, which has the refinement $Z$ with $r=r' = \id$ and the identity bundle morphism.  According to the equivalence relation on bundle gerbe 2-morphisms we have to evaluate $\varphi$ over a point $w \in W$ with $r(w) = r'(w)$, i.e. $w$ is of the form $w=(p,p,p')$. Here we can choose $h=1$ and $\tilde\rho = \id_{p}$, in which case we have $\varphi(f,g) = ((f,g),(\id_p,1))$. This is indeed the identity on $Q$. 
\end{proof}


\subsubsection{Properties of the 2-functor $\mathscr{E}_M$}


For the proof of Theorem \ref{th:equivalence} we provide the following two statements.

\begin{lemma}
\label{lem:efullyfaithful}
The 2-functor $\mathscr{E}_M$ is fully faithful on Hom-categories. 
\end{lemma}

\begin{proof}
Let $\mathcal{P}, \mathcal{P}'$ be principal $\Gamma$-2-bundles over $M$, and let $F_1,F_2: \mathcal{P} \to \mathcal{P}'$ be 1-morphisms. By Lemma \ref{lem:canonicalrefinement} every 2-morphism $\eta: \mathscr{E}_M(F_1) \Rightarrow \mathscr{E}_M(F_2)$ can be represented by one whose refinement is $\mathcal{P}_0 \times_M \mathcal{P}_0'$, so that its bundle isomorphism is $\eta: Q_1 \to Q_2$, where  $Q_k := F_k \times \Gamma$ for $k=1,2$. We can read off a map $\eta: F_1 \to F_2$, and it is easy to see that this is a 2-morphism $\eta: F_1 \Rightarrow F_2$. This procedure is clearly inverse to the 2-functor $\mathscr{E}_M$ on 2-morphisms. \end{proof}



\begin{proposition}
\label{prop:estack}
The 2-functors $\mathscr{E}_M$ form a 1-morphism between pre-2-stacks. 
\end{proposition}

\begin{proof}
For a smooth map $f:M \to N$, we have to look at the diagram
\begin{equation*}
\alxydim{@R=1.3cm}{\zwoabun \Gamma N \ar[d]_{\mathscr{E}_N} \ar[r]^{f^{*}} & \zwoabun \Gamma M \ar[d]^{\mathscr{E}_M} \\ \grb\Gamma N \ar[r]_{f^{*}} & \grb\Gamma M}
\end{equation*}
of 2-functors. For $\mathcal{P}$ a principal $\Gamma$-2-bundle over $N$, the $\Gamma$-bundle gerbe $\mathscr{E}_M(f^{*}\mathcal{P})$ has the surjective submersion $\mathrm{pr}_1: Y:=M \times_N \mathcal{P}_0 \to M$, the principal $\Gamma$-bundle $P :=M \times_N \mathcal{P}_1 \times \Gamma_0$ over $Y^{[2]}$, and a bundle gerbe product $\mu$ defined as in \erf{defmu} that ignores the $M$-factor.  On the other hand, the $\Gamma$-bundle gerbe $f^{*}\mathscr{E}_N(\mathcal{P})$ has the same surjective submersion, and  -- up to canonical identifications between fibre products --  the same $\Gamma$-bundle and the same bundle gerbe product. These canonical identifications make up a pseudonatural transformation that renders the above diagram commutative.  
\end{proof}
