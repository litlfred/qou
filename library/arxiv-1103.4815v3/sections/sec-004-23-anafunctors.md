---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-004-23-anafunctors
section_title: "Anafunctors"
section_number: 2.3
pages: 9-13
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.704
latex_coverage_ratio: 0.985
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{sec:ana}


An anafunctor is a generalization of a smooth functor between Lie groupoids, similar to a Morita equivalence, and also known as a Hilsum-Skandalis morphism.   The idea goes  back to Benabou \cite{benabou1}, also see \cite{johnstone1}. The references for the following definitions are \cite{lerman1,metzler}. 

\begin{definition}
Let $\mathcal{X}$ and $\mathcal{Y}$ be Lie groupoids. 
\begin{enumerate}
\item 
An \emph{anafunctor}\ $F: \mathcal{X} \to \mathcal{Y}$
is a smooth manifold $F$, a left action $(\alpha_l,\rho_l)$ of $\mathcal{X}$ on $F$, and  a right action $(\alpha_r,\rho_r)$ of $\mathcal{Y}$ on $F$ such that the actions commute and $\alpha_l: F \to \mathcal{X}_0$ is a principal $\mathcal{Y}$-bundle over $\mathcal{X}_0$.  

\item

A \emph{transformation} between anafunctors $f: F \Rightarrow F'$ is a smooth map $f: F \to F'$ which is $\mathcal{X}$-equivariant, $\mathcal{Y}$-equivariant, and satisfies $\alpha_l' \circ f= \alpha_l$ and $\alpha_r' \circ f = \alpha_r$. 
\end{enumerate}
\end{definition}

The smooth manifold $F$ of an anafunctor is called its \emph{total space}. Notice that the condition that the two actions on $F$ commute implies that each respects the anchor of the other. 
For fixed Lie groupoids $\mathcal{X}$ and $\mathcal{Y}$, anafunctors $F: \mathcal{X} \to \mathcal{Y}$ and transformations form a category $\af(\mathcal{X},\mathcal{Y})$. Since transformations are in particular morphisms between principal $\mathcal{Y}$-bundles, every transformation is invertible so that $\af(\mathcal{X},\mathcal{Y})$ is in fact a groupoid. 

\begin{example}[Anafunctors from ordinary functors]
\label{ex:anafunctor}
Given a smooth functor $\phi:\mathcal{X} \to \mathcal{Y}$, we obtain an anafunctor in the following way. We set $F := \mathcal{X}_0 \lli\phi\times _t \mathcal{Y}_1$ with anchors $\alpha_l:F \to \mathcal{X}_0$ and $\alpha_r: F \to \mathcal{Y}_0$ defined by $\alpha_l(x,g) := x$ and $\alpha_r(x,g) := s(g)$, and  actions \begin{equation*}
\rho_l: \mathcal{X}_1 \lli s \times_{\alpha_l} F \to F
\quad\text{ and }\quad
\rho_r: F \lli{\alpha_r}\times_t \mathcal{Y}_1 \to F
\end{equation*}
 defined by $\rho_l(f,(x,g)) := (t(f),\phi(f) \circ g)$ and $\rho_r((x,g),f) := (x, g \circ f)$. In the same way, a smooth natural transformation $\eta:\phi\Rightarrow \phi'$ defines a transformation $f_{\eta}:F \Rightarrow F'$ by $f_{\eta}(x,g) := (x,\eta(x) \circ g)$. Conversely, one can show that an anafunctor comes from a smooth functor, if its principal $\Gamma$-bundle has a smooth section. 
\end{example}


\begin{example}[Anafunctors with discrete source]
\label{anafunctors}
For $M$ a smooth manifold and $\Gamma$ a Lie groupoid, we have an equality of categories
\begin{equation*}
\bun\Gamma M = \af(\idmorph{M},\Gamma)\text{.}
\end{equation*}
Further, \emph{trivial} principal $\Gamma$-bundles correspond to smooth \emph{functors}.  
In particular, with Example \ref{ex:grpdbun} we have,
\begin{enumerate}[(a)]
\item
For $G$ a Lie group and $M$ a smooth manifold, an anafunctor $F: \idmorph{M} \to \mathcal{B}G$ is the same as an ordinary principal $G$-bundle over $M$.

\item
For $M$ and $X$ smooth manifolds, an anafunctor $F: \idmorph{M} \to \idmorph{X}$ is the same as a smooth map. 

\end{enumerate}
\end{example}

\begin{example}[Anafunctors with discrete target]
\label{anafunctors:c}
For $\Gamma$ a Lie groupoid and $M$ a smooth manifold, we have an equivalence of categories
\begin{equation*}
\idmorph{C^{\infty}(\Gamma_0,M)^{\Gamma}} \cong \af(\Gamma,\idmorph M) 
\end{equation*}
where $C^{\infty}(\Gamma_0,M)^{\Gamma}$ denotes the set of smooth maps $f: \Gamma_0 \to M$ such that $f \circ s = f \circ t$ as maps $\Gamma_1 \to M$. The equivalence is induced by regarding a map $f \in C^{\infty}(\Gamma_0,M)^{\Gamma}$ as a smooth functor $f:\Gamma \to \idmorph{M}$, which in turn induces an anafunctor. Conversely, an anafunctor $F: \Gamma \to \idmorph{M}$ is in particular an $\idmorph{M}$-bundle over $\Gamma_0$, which is nothing but a smooth function $f: \Gamma_0 \to M$ by Example \ref{ex:idmorphbundle}. The additional $\Gamma$-action assures the $\Gamma$-invariance of $f$. 
\end{example}

\begin{example}[Anafunctors between one-object Lie groupoids]
Let $G$ and $H$ be Lie groups, and let $\mathcal{B}G$ and $\mathcal{B}H$ be the associated one-object Lie groupoids (Example \ref{example_groupoids} \ref{exBG}). Then, there is an equivalence of categories
\begin{equation*}
\act{\mathrm{Hom}(G,H)}H \cong \af(\mathcal{B}G,\mathcal{B}H) \text{,}
\end{equation*}
where the action of $H$ on $\mathrm{Hom}(G,H)$ is by point-wise conjugation. The functor which establishes this equivalence sends a smooth group homomorphism $\alpha:G \to H$ to the evident smooth functor $F_{\alpha}: \mathcal{B}G \to \mathcal{B}H$ and converts this into an anafunctor (Example \ref{ex:anafunctor}). A morphism $h:\alpha_1 \to \alpha_2$ is sent to the natural transformation $\eta_h: F_{\alpha_1} \to F_{\alpha_2}$ whose component at the single object is the morphism $h \in H$. 
In order to see that this is essentially surjective, it suffices to notice that the principal $H$-bundle of any smooth anafunctor $F: \mathcal{B}G \to \mathcal{B}H$ has a section. The proof that the functor is full and faithful is straightforward. 
\end{example}

For the following definition, we suppose $\mathcal{X}$, $\mathcal{Y}$ and $\mathcal{Z}$ are Lie groupoids, and
$F:\mathcal{X} \to \mathcal{Y}$
and
$G: \mathcal{Y} \to \mathcal{Z}$
are anafunctors given by $F=(F,\alpha_l,\rho_l,\alpha_r,\rho_r)$ and $G=(G,\beta_l,\tau_l,\beta_r,\tau_r)$.

\begin{definition}
 The \emph{composition}
$G \circ F: \mathcal{X} \to \mathcal{Z}$
is the anafunctor  defined in the following way:
\begin{enumerate}
\item 
Its total space is
\begin{equation*}
E := (F \lli{\alpha_r}\times_{\beta_l} G) / \sim
\end{equation*}
where $(f,\tau_l(h,g)) \sim (\rho_r(f,h),g)$ for all $h\in \mathcal{Y}_1$ with $\alpha_r(f)=t(h)$ and $\beta_l(g)=s(h)$.

\item
The anchors are  $(f,g) \mapsto \alpha_l(f)$ and $(f,g) \mapsto \beta_r(g)$. 
\item
The actions $\mathcal{X}_1 \lli{s}\times_{\alpha} E \to E$ and $E \lli{\beta}\times_{t} \mathcal{Z}_1 \to E$ are given, respectively, by
\begin{equation*}
(\gamma,(f,g)) \mapsto (\rho_l(\gamma,f),g)
\quand
((f,g), \gamma) \mapsto (f,\tau_r(g,\gamma))\text{.}
\end{equation*}
\end{enumerate}
\end{definition}

\begin{remark}
Lie groupoids, anafunctors and transformations form a bicategory. This bicategory  is equivalent to the bicategory of differentiable stacks (also known as geometric stacks) \cite{pronk}.
\end{remark}

\begin{comment}

\begin{example}
\label{ex:composition}
Let $F: \mathcal{X} \to \mathcal{Y}$ be an anafunctor with anchors $\alpha_l,\alpha_r$, and let $E: \mathcal{W} \to \mathcal{X}$ and $G: \mathcal{Y} \to \mathcal{Z}$ be smooth functors. 
\begin{enumerate}[(i)]
\item 
The composition $F \circ E: \mathcal{W} \to \mathcal{Y}$ is the anafunctor with the total space $\mathcal{W}_0 \lli{E}\times_{\alpha_l} F$, anchors $\beta_l(w,f) = w$ and $\beta_r(w,f) = \alpha_r(f)$, and actions
\begin{equation*}
(w,f) \circ \gamma = (w,f \circ \gamma)
\quand
\omega' \circ (w,f) = (t(\omega'), E(\omega') \circ f)\text{.}
\end{equation*}

\item
The composition $G \circ F: \mathcal{X} \to \mathcal{Z}$ is the anafunctor with the total space $(F \lli{G \circ \alpha_r} \times_{t} \mathcal{Z}_1) / \sim$, where $(f \circ \gamma,\zeta) \sim (f,G(\gamma) \circ \zeta)$ for all $\gamma \in \mathcal{Y}_1$ with $\alpha_r(f)=t(\gamma)$ and $G(s(\gamma))= t(\zeta)$. The anchors are $\beta_l(f,\zeta) = \alpha_l(f)$ and $\beta_r(f,\zeta) = s(\zeta)$, and the actions are
\begin{equation*}
\chi \circ (f,\zeta) = (\chi \circ f,\zeta)
\quand
(f,\zeta) \circ \xi = (f,\zeta \circ \xi)\text{.}
\end{equation*}

\item
\label{ex:composition:full}
Moreover, the composite $G \circ F \circ E: \mathcal{W} \to \mathcal{Z}$ is given by the total space
\begin{equation*}
(\mathcal{W}_0 \lli{E}\times_{\alpha_l} F \lli{G \circ \alpha_r} \times_{t} \mathcal{Z}_1) / \sim
\end{equation*}
where $(w,f \circ \gamma,\zeta) \sim (w,f,G(\gamma) \circ \zeta)$ for all $\gamma \in \mathcal{Y}_1$ with $\alpha_r(f)=t(\gamma)$ and $G(s(\gamma))= t(\zeta)$. The anchors are $\beta_r(w,f,\zeta) = w$ and $\beta_r(w,f,\zeta) = s(\zeta)$, and the actions are
\begin{equation*}
\omega \circ (w,f,\zeta) = (t(\omega), E(\omega) \circ f,\zeta)
\quand
(w,f,\zeta) \circ \xi = (w,f,\zeta \circ \xi)\text{.}
\end{equation*}

\end{enumerate}
\end{example}
\end{comment}

In this article, anafunctors serve  two purposes. The first is that one can use conveniently the composition of anafunctors to define \emph{extensions} of principal groupoid bundles:

\begin{definition}
\label{def:extension}
 If $P: \idmorph M \to \Gamma$ is a principal $\Gamma$-bundle over $M$, and $\Lambda: \Gamma \to \Omega$ is an anafunctor, then the principal $\Omega$-bundle
\begin{equation*}
\Lambda P := \Lambda \circ P :\idmorph M \to \Omega
\end{equation*}
is called the \emph{extension of $P$ along $\Lambda$}.
\end{definition}

Unwinding this definition, the principal $\Omega$-bundle $\Lambda P$ has the total space
\begin{equation}
\label{bundleextension}
\Lambda P = (P \lli{\alpha}\times_{\alpha_l} \Lambda) \;/\; \sim
\end{equation}
where $(p,\rho_l(\gamma,\lambda)) \sim (\rho(p,\gamma),\lambda)$ for all $p\in P$, $\lambda\in \Lambda$ and $\gamma\in \Gamma_1$ with $\alpha(p)=t(\gamma)$ and $\alpha_l(\lambda)=s(\gamma)$. Here $\alpha$ is the anchor and $\rho$ is the action of $P$, and $\Lambda = (\Lambda,\alpha_l,\alpha_r,\rho_l,\rho_r)$. The bundle projection is $(p,\lambda) \mapsto \pi(p)$, where $\pi$ is the bundle projection of $P$, the anchor  is $(p,\lambda) \mapsto \alpha_r(\lambda)$, and the action is $(p,\lambda)\circ \omega=(p,\rho_r(\lambda,\omega))$. 

\begin{comment}
In particular, if $\Lambda: \Gamma \to \Omega$ is a smooth \emph{functor}, we get via Example \ref{ex:anafunctor} 
\begin{equation*}
\Lambda P= (P \lli{\Lambda \circ \alpha}  \times_{t} \Omega_1) \;/\; \sim
\end{equation*}
where $(p,\Lambda(\gamma) \circ \omega) \sim (\rho(p,\gamma),\omega)$ for all $p\in P$, $\omega\in \Omega_1$ and $\gamma\in \Gamma_1$ with $\Lambda(s(\gamma)) = t(\omega)$ and $t(\gamma) = \alpha(p)$. Here, the bundle projection is $(p,\omega) \mapsto \pi(p)$, the anchor is $(p,\omega) \mapsto s(\omega)$, and the action is $(p,\omega) \circ \omega'= (p,\omega \circ \omega')$. 
\end{comment}


Extensions of bundles are accompanied by extensions of bundle morphisms. If $\varphi: P_1 \to P_2$ is a morphism between $\Gamma$-bundles, a morphism $\Lambda\varphi: \Lambda P_1 \to \Lambda P_2$ is defined by $\Lambda\varphi(p_1,\lambda) := (\varphi(p_1),\lambda)$ in terms of \erf{bundleextension}. Summarizing, we have

\begin{lemma}
\label{extensionfunctor}
Let $M$ be a smooth manifold and $\Lambda:\Gamma \to \Omega$ be an anafunctor. Then, extension along $\Lambda$ is a functor
\begin{equation*}
\Lambda: \bun\Gamma M \to \bun\Omega M\text{.}
\end{equation*}
Moreover, it commutes with pullbacks and so extends to a morphism between stacks. 
\end{lemma}


Next we suppose that  $t:H \to G$ is a Lie group homomorphism, and $\act GH$ is the associated action groupoid of Example \ref{exliecat} \erf{extHG}. We look at the functor $\Theta: \act GH \to \mathcal{B}H$ which is defined by $\Theta(h,g) := h$. Combining Lemma
\ref{actionbundles} with the extension along $\Theta$, we obtain 

\begin{lemma}
\label{crossedbundles}
The category $\bun {\act GH}M$ of principal $\act G H$-bundles over a smooth manifold $M$  is equivalent to a category with
\begin{itemize}
\item 
Objects: principal $H$-bundles $P_H$ over $M$ together with a section of  $\Theta (P_H)$.

\item
Morphisms: morphisms $\varphi$ of $H$-bundles so that $\Theta(\varphi)$ preserves the sections.
\end{itemize}
\end{lemma}


The second motivation for introducing anafunctors is that they provide the inverses to certain smooth functors which are not necessarily equivalences of categories.


\begin{definition}\label{defweak}
A smooth functor or anafunctor $F:\mathcal{X} \to \mathcal{Y}$ is called a \emph{weak equivalence}, if there exists an anafunctor $G: \mathcal{Y} \to \mathcal{X}$ together with transformations $G \circ F \cong \id_{\mathcal{X}}$ and $F \circ G \cong \id_\mathcal{Y}$. 
\end{definition}


We have the following immediate consequence for the stack morphisms of Lemma \ref{extensionfunctor}.

\begin{corollary}
\label{co:extensionweakequivalence}
Let $\Lambda: \Gamma \to \Omega$ be a weak equivalence between Lie groupoids. Then, extension of principal  bundles along $\Lambda$ is an equivalence
$\Lambda: \bun\Gamma M \to \bun\Omega M$ of categories. Moreover, these define an equivalence between the stacks $\bun\Gamma-$ and $\bun \Omega-$.
\end{corollary}

Concerning the claimed generalization of invertibility, we have 
the following well-known theorem, see \cite[Lemma 3.34]{lerman1}, \cite[Proposition 60]{metzler}. 

\begin{theorem}
\label{weak}
A smooth functor $F: \mathcal{X} \to \mathcal{Y}$ is a weak equivalence if and only if the following two conditions are satisfied:
\begin{enumerate}[(a)]
\item 
it is smoothly essentially surjective: the map
\begin{equation*}
s \circ \mathrm{pr}_2: \mathcal{X}_0 \lli{F_0}\times_{t} \mathcal{Y}_1 \to \mathcal{Y}_0
\end{equation*}
is a surjective submersion.

\item
it is smoothly fully faithful: the diagram
\begin{equation*}
\alxydim{@C=1.5cm@R=1.3cm}{\mathcal{X}_1 \ar[r]^{F} \ar[d]_{s \times t} & \mathcal{Y}_1 \ar[d]^{s \times t} \\ \mathcal{X}_0 \times \mathcal{X}_0 \ar[r]_-{F \times F} & \mathcal{Y}_0 \times \mathcal{Y}_0}
\end{equation*}
is a pullback diagram.
\end{enumerate}
\end{theorem}

\begin{comment}
\begin{remark}
More explicitly, condition (b) means that for every smooth manifold $N$ with smooth maps $f: N \to \mathcal{X}_0 \times \mathcal{X}_0$ and $g:N \to \mathcal{Y}_1$ for which the diagram 
\begin{equation}
\label{univprop}
\alxydim{@C=1.5cm}{N \ar[r]^{g} \ar[d]_{f} & \mathcal{Y}_1 \ar[d]^{s \times t} \\ \mathcal{X}_0 \times \mathcal{X}_0 \ar[r]_-{F \times F} & \mathcal{Y}_0 \times \mathcal{Y}_0}
\end{equation}
is commutative, there exists a unique smooth map $\sigma: N \to \mathcal{X}_1$ such that $(s \times t) \circ \sigma = f$ and $F \circ \sigma = g$. 
\end{remark}
\end{comment}

\begin{remark}
\label{rem:inverses}
One can show that any smooth functor $F:\mathcal{X} \to \mathcal{Y}$ that is a weak equivalence actually has a \emph{canonical} inverse  anafunctor. \end{remark}

\begin{comment}
\begin{lemma}
\label{lem:inverse}
Suppose $F: \mathcal{X} \to \mathcal{Y}$ is a smooth functor, and suppose $E: \mathcal{Y} \to \mathcal{X}$ is an anafunctor with anchors $\alpha_l,\alpha_r$. Suppose further that $\varphi: \mathcal{X}_0 \to E$ and $\psi: E \to \mathcal{Y}_1$ are smooth map satisfying
\begin{equation}
\label{condphi}
\alpha_r \circ \varphi \circ s = s
\quomma
\alpha_l \circ \varphi \circ s = s \circ F
\quand
F(\chi) \circ \varphi(s(\chi)) = \varphi(t(\chi)) \circ \chi
\end{equation}
and
\begin{multline}
\label{condpsi}
s \circ \psi = \alpha_l
\quomma
t \circ \psi = F \circ \alpha_r
\quomma
\psi(\gamma \circ e) =\psi(e) \circ \gamma^{-1}
\\\quand
F(\chi) \circ \psi(e) = \psi(e \circ \chi^{-1})
\end{multline}
Then, $\varphi$ and $\psi$ determine transformations $E \circ F \cong \id_{\mathcal{X}}$ and $F \circ E \cong \id_{\mathcal{Y}}$. In particular, $F$ is a weak equivalence.
\end{lemma}

\begin{proof}
The composite $E \circ F$ has the total space $(\mathcal{X}_0 \lli{F} \times_{t} \mathcal{Y}_1 \lli{s} \times_{\alpha_l} E)/\sim$ with the equivalence relation of dividing out $\mathcal{Y}_1$ in the middle.
Left anchor/action and right anchor/action are given, respectively, by
\begin{eqnarray*}
\beta_l(x,\gamma,e) &=& x 
\\
\chi \circ (x,\gamma,e) &=& (t(\chi),F(\chi) \circ \gamma,e)
\\
\beta_r(x,\gamma,e) &=& \alpha_r(e)
\\
(x,\gamma,e) \circ \chi &=& (x,\gamma,e \circ \chi)\text{.}
\end{eqnarray*}
A transformation $\tilde\varphi: \id_{\mathcal{X}} \to E \circ F$ is given by
\begin{equation*}
\tilde \varphi: \mathcal{X}_1 \to \mathcal{X}_0 \lli{F} \times_{t} \mathcal{Y}_1 \lli{s} \times_{\alpha_l} E: \chi \mapsto (t(\chi),F(\chi),\varphi(s(\chi)))\text{.}
\end{equation*}
This is well-defined due to \erf{condphi}. 
We check that anchors and actions are preserved: for the right anchors and the left action, this is trivial: $\beta_l(\tilde\varphi(\chi)) = t(\chi)$ and
\begin{equation*}
\tilde\varphi(\chi'\circ \chi) = (t(\chi'),F(\chi' \circ\chi),\varphi(s(\chi))) = \chi' \circ (t(\chi),F(\chi),\varphi(s(\chi))) = \chi' \circ \tilde\varphi(x)\text{.}
\end{equation*}
For the left anchor and the right action we use \erf{condphi}:
\begin{equation*}
\beta_r(\tilde\varphi(\chi)) = \alpha_r(\varphi(s(\chi))) = s(\chi)
\end{equation*}
and
\begin{multline*}
\tilde\varphi(\chi \circ \chi') = (t(\chi),F(\chi \circ \chi'),\varphi(s(\chi'))) = (t(\chi),F(\chi),F(\chi') \circ \varphi(s(\chi'))) \\= (t(\chi), F(\chi), \varphi(t(\chi')) \circ \chi') = (t(\chi),F(\chi),\varphi(s(\chi))) \circ \chi' = \tilde\varphi(\chi) \circ \chi'\text{.}
\end{multline*}
The other composite, $F \circ E$, has the total space $(E \lli{F \circ \alpha_r}   \times_t \mathcal{Y}_1)/\sim $ with the equivalence relation of dividing out $\mathcal{X}_1$ in the middle.
Left anchor/action and right anchor/action are given, respectively, by
\begin{eqnarray*}
\beta_l(e,\gamma) &=& \alpha_l(e) 
\\
\gamma' \circ (e,\gamma) &=& (\gamma' \circ e,\gamma)
\\
\beta_r(e,\gamma) &=& s(\gamma)
\\
(e,\gamma) \circ \gamma' &=& (e,\gamma \circ \gamma')\text{.}
\end{eqnarray*}
A transformation $\tilde\psi: F \circ E \to \id_{\mathcal{Y}}$ is defined by
\begin{equation*}
\psi:(E \lli{F \circ \alpha_r}   \times_t \mathcal{Y}_1)/\sim \to \mathcal{Y}_1 : (e,\gamma) \mapsto \psi(e)^{-1} \circ \gamma\text{.}
\end{equation*}
This is well-defined under $\sim$ due to \erf{condpsi}.
The right anchor is preserved by trivial reasons: $\beta_r(e,\gamma) = s(\gamma) = s(\psi(e)^{-1} \circ \gamma) = s(\tilde\psi(e,\gamma))$, while left anchor and both actions require \erf{condpsi}: the anchor goes
\begin{equation*}
\beta_l(e,\gamma) = \alpha_l(e) = s(\psi(e)) = t(\psi(e)^{-1} \circ \gamma)= t(\tilde\psi(e,\gamma))\text{,}
\end{equation*}
the right action goes
\begin{equation*}
\tilde\psi((e,\gamma) \circ \gamma') = \tilde\psi(e,\gamma\circ \gamma') = \psi(e)^{-1} \circ \gamma\circ \gamma' = \tilde\psi(e,\gamma) \circ \gamma'\text{,}
\end{equation*}
and the left action goes
\begin{equation*}
\tilde\psi(\gamma' \circ (e,\gamma)) = \tilde\psi(\gamma' \circ e,\gamma) = \psi(\gamma' \circ e)^{-1} \circ \gamma = \gamma' \circ \psi(e)^{-1} \circ \gamma = \gamma' \circ \tilde\psi(e,\gamma)\text{.}
\end{equation*}
\end{proof}
\end{comment}

\begin{comment}
\begin{proof}[Proof of Theorem \ref{weak}]
We only proof the \quot{if}-part, by defining -- in a canonical way -- an inverse anafunctor $\bar F:\mathcal{Y} \to \mathcal{X}$ . We will eventually need this construction later, so we will give the full details. Recall from Example \ref{ex:anafunctor} that the functor $F$ is represented by an anafunctor $F: \mathcal{X} \to \mathcal{Y}$ with total space $F :=\mathcal{X}_0 \lli{F} \times_{t} \mathcal{Y}_1$, left anchor $\alpha_l(x,\gamma) := x$, right anchor $\alpha_r(x,\gamma) := s(\gamma)$, left action $\chi \circ (x,\gamma) := (t(\chi),F(\chi) \circ \gamma)$, and right action $(x,\gamma) \circ \gamma' := (x,\gamma \circ \gamma')$. 

The  total space of $\bar F$ is the  smooth manifold $F$, and the anchors are exchanged: $\bar\alpha_l(x,\gamma) = s(\gamma)$ and $\bar\alpha_r(x,\gamma) := x$. The actions are also exchanged but additionally inverted in order to transform a right in a left action and vice versa, i.e. $\tilde \gamma \circ (x,\gamma) := (x,\gamma \circ \tilde\gamma^{-1})$   and $(x,\gamma) \circ \chi := (s(\chi),F(\chi)^{-1} \circ \gamma)$. These actions clearly commute as before.
 Conditions (a) and (b) imply  that $\bar\alpha_l: F \to \mathcal{Y}_0$ is a principal $\mathcal{X}$-bundle. Indeed, (a) is exactly the condition that the bundle projection $\bar\alpha_l$ is a surjective submersion. Then it remains to show that 
\begin{equation}
\label{eq:scherung1}
\tau: F \lli{\bar\alpha_r} \times_{t} \mathcal{X}_1 \to F \lli{\bar\alpha_l}\times_{\bar\alpha_l} F:((x,\gamma),\chi) \mapsto ((x,\gamma),(s(\chi),F(\chi)^{-1} \circ \gamma))
\end{equation}
is a diffeomorphism. We consider $N := F \lli{\bar\alpha_l}\times_{\bar\alpha_l} F$ with $f:N \to \mathcal{X}_0 \times \mathcal{X}_0$ and $g:N \to \mathcal{Y}_1$ given by $f((x_1,\gamma_1),(x_2,\gamma_2)) := (x_2,x_1)$ and $g((x_1,\gamma_1),(x_2,\gamma_2)) :=\gamma_1 \circ \gamma_2^{-1} $. It fits into the commutative diagram \erf{univprop} and so we have by (b) the smooth map $\sigma:N \to \mathcal{X}_1$. We put
$\tau^{-1}=(\mathrm{pr}_1,\sigma): N \to F \lli{\bar\alpha_r} \times_{t} \mathcal{X}_1$. This is smooth and one can show that it is an inverse to \erf{eq:scherung1}.
First of all, we have that 
\begin{equation*}
\bar \alpha_r((x_1,\gamma_1)) = x_1 =  \mathrm{pr}_2(f((x_1,\gamma_1),(x_2,\gamma_2)))= t(\sigma((x_1,\gamma_1),(x_2,\gamma_2)))
\end{equation*}
so that $\tau^{-1}$ lands in the fibre product  $F \lli{\bar\alpha_r} \times_{t} \mathcal{X}_1$.
\begin{enumerate}
\item 
We calculate
\begin{equation*}
\tau^{-1}(\tau(x,\gamma,\chi))= \tau^{-1}(x,\gamma, s(\chi),F(\chi)^{-1} \circ \gamma) =(x,\gamma,\sigma(x,\gamma, s(\chi),F(\chi)^{-1} \circ \gamma))\text{.}
\end{equation*}
Now we look at $N' := \mathcal{X}_1 \times \mathcal{Y}_1$ equipped with smooth maps $f': N' \to \mathcal{X}_0 \times \mathcal{X}_0$ and $g': N' \to \mathcal{Y}_1$ defined by $f'(\chi,\gamma) := (s(\chi),t(\chi))$ and $g'(\chi,\gamma) := F(\chi)$. Again, this fits into the commutative diagram \erf{univprop}. We have the obvious map $\mathrm{pr}_2: N' \to \mathcal{X}_1$ satisfying $(s \times t) \circ \mathrm{pr}_2 = f'$ and $F \circ \mathrm{pr}_2 = g'$. On the other hand, we can look at the map $\sigma \circ h: N' \to \mathcal{X}_1$ where $h: N' \to N$ is defined by
\begin{equation*}
h(\chi,\gamma) := (t(\chi),\gamma,s(\chi),F(\chi)^{-1} \circ \gamma) 
\end{equation*}
and satisfies 
$(s \times t) \circ \sigma \circ h = f \circ h = f'$ and $F \circ \sigma \circ h = g \circ h = g'$, By the universal property (b) we have $\mathrm{pr}_2 = \sigma \circ h$. This shows that
\begin{equation*}
\sigma(x,\gamma, s(\chi),F(\chi)^{-1} \circ \gamma) = \sigma(h(\chi,\gamma)) = \mathrm{pr}_2(\chi,\gamma)=\chi\text{.}
\end{equation*}
Thus, $\tau^{-1}(\tau(x,\gamma,\chi))= (x,\gamma,\chi)$. 
\end{enumerate}
\begin{enumerate}
\item[2.]
Then we calculate
\begin{eqnarray*}
\tau(\tau^{-1}(x_1,\gamma_1,x_2,\gamma_2)) &=& \tau(x_1,\gamma_1,\sigma(x_1,\gamma_1,x_2,\gamma_2)) \\&=& (x_1,\gamma_1,s(\sigma(x_1,\gamma_1,x_2,\gamma_2)),F(\sigma(x_1,\gamma_1,x_2,\gamma_2))^{-1} \circ \gamma_1)
\\&=& (x_1,\gamma_1, \mathrm{pr}_1(f(x_1,\gamma_1,x_2,\gamma_2)),g(x_1,\gamma_1,x_2,\gamma_2)^{-1} \circ \gamma_1)
\\&=& (x_1,\gamma_1,x_2,\gamma_2)\text{.}
\end{eqnarray*}
\end{enumerate}
So, $\bar F: \mathcal{Y} \to \mathcal{X}$ is an anafunctor. 


It remains to prove that $\bar F$ is inverse to the given smooth functor $F$. We use Lemma \ref{lem:inverse} with $E := \bar F = \mathcal{X}_0 \lli{F} \times_{t} \mathcal{Y}_1$. The smooth function $\varphi: \mathcal{X}_0 \to \bar F$ and $\psi: \bar F \to \mathcal{Y}_1$ are given by $\varphi(x) := (x,\id_{F(x)})$ and $\psi(x,\gamma) := \gamma$. It is straightforward to check the necessary conditions for these maps.
Indeed, the ones for $\varphi$ are:
\begin{eqnarray*}
\bar\alpha_r(\varphi(s(\chi))) &=& \bar\alpha_r(s(\chi),\id_{F(s(\chi))}) = s(\chi)
\\
\bar\alpha_l(\varphi(s(\chi))) &=& \bar\alpha_l(s(\chi),\id_{F(s(\chi))}) = F(s(\chi)) = s(F(\chi))
\\
F(\chi) \circ \varphi(s(\chi)) &=& F(\chi) \circ(s(\chi),\id_{F(s(\chi))}) = (t(\chi),F(\chi)^{-1}) \\&=& (t(\chi),\id_{t(\chi)}) \circ \chi =\varphi(t(\chi)) \circ \chi\text{.}
\end{eqnarray*}
The ones for $\psi$ are:
\begin{eqnarray*}
s(\psi(x,\gamma)) &=&s(\gamma) = \bar\alpha_l(x,\gamma)
\\ t(\psi(x,\gamma)) &=& t(\gamma) = F(x) = F(\alpha_r(x,\gamma))
\\ F(\chi) \circ \psi(x,\gamma) &=& F(\chi) \circ \gamma = \psi(t(\chi),F(\chi) \circ \gamma) = \psi((x,\gamma) \circ \chi^{-1})
\\ \psi(\gamma' \circ (x,\gamma)) &=& \psi((x,\gamma \circ \gamma^{\prime-1}))=\gamma \circ \gamma^{\prime-1} = \psi(x,\gamma) \circ \gamma^{\prime-1}
\end{eqnarray*}
\end{proof}

\begin{definition}
\label{inverseanafunctor}
Let $F: \mathcal{X} \to \mathcal{Y}$ be a smoothly essentially surjective, smoothly fully faithful, smooth functor. Then, the anafunctor $\bar F: \mathcal{Y} \to \mathcal{X}$ from the proof of Theorem \ref{weak} is called the \emph{inverse anafunctor of $F$}.
\end{definition}
\end{comment}




\begin{comment}
This was an example we didn't need anymore.
\label{ex:refinement}
Consider a Lie groupoid $\Gamma$, and a surjective submersion $\pi:E \to \Gamma_0$. 
\begin{enumerate}
\item 
The following Lie groupoid $\pi^{-1}\Gamma$ is called the \emph{refinement of $\Gamma$ along $\pi$}. It has objects $E$ and morphisms $E \lli{\pi} \times_{t} \Gamma_1\; \lli{s} \times_{\pi} E$, source and target maps are $s= \mathrm{pr}_3$, $t=\mathrm{pr}_1$, and the composition is $(e_2',\gamma_2,e_2) \circ (e_1',\gamma_1,e_1) := (e_2',  \gamma_2 \circ \gamma_1, e_1)$. The refinement $\pi^{-1}\Gamma$ comes with a smooth functor
\begin{equation*}
\Pi: \pi^{-1}\Gamma \to \Gamma
\end{equation*}
that is $\pi$ on objects and $\mathrm{pr}_2$ on morphisms. 

\item
The functor $\Pi$ is smoothly essentially surjective and fully faithful, so that it is invertible by an anafunctor. One has the following canonical choice denoted 
\begin{equation*}
\Pi^{-1} : \pi^{-1}\Gamma \to \Gamma\text{.}
\end{equation*}
It is given by
\begin{equation*}
F := \Gamma_1 \lli{s} \times_{\pi} E
\quomma
\alpha_l(\gamma,e) := t(\gamma) 
\quand
\alpha_r(\gamma,e) := e\text{.}
\end{equation*}
The actions are
\begin{equation*}
\rho_l: \Gamma_1 \lli{s} \times_{\alpha_l} F \to F: (\gamma_2,(\gamma_1,e)) \mapsto (\gamma_2 \circ \gamma_1, e)
\end{equation*} 
and
\begin{equation*}
\rho_r: F \lli{\alpha_r} \times_{t} (E \lli{\pi}\times_{t} \Gamma_1\; \lli{s} \times_{\pi} E) \to F: ((\gamma,e),(e,\gamma',e')) \mapsto (\gamma \circ \gamma',e')\text{.}
\end{equation*}
The second action is principal in the fibres of $\alpha_l$. 

\item
We check that the anafunctor $\Pi^{-1}$ is an inverse to the smooth functor $\Pi$. The composition $\Pi \circ \Pi^{-1}$ is the anafunctor with the total space $(\Gamma_1 \lli{s} \times_\pi E \lli{\pi} \times_{t} \Gamma_1)/\sim$, where $(\gamma_1,e,\gamma_2)\sim (\gamma_1 \circ \gamma,e,\gamma^{-1} \circ \gamma_2)$ for $\gamma \in \Gamma_1$ with $s(\gamma)=t(\gamma)=e$, with left and right anchor given by $t \circ \mathrm{pr}_3$ and $s \circ \mathrm{pr}_1$, respectively, and with left and right actions given in the obvious way. The identity anafunctor $\id_{\Gamma}:\Gamma \to \Gamma$ has the total space $\Gamma_1$ with left and right anchor given by $t$ and $s$, respectively, and with the obvious actions. A transformation $\Pi \circ \Pi^{-1} \Rightarrow \id_{\Gamma}$ is defined by $(\gamma_1,e,\gamma_2) \mapsto \gamma_1 \circ \gamma_2$. The other direction goes completely analogous. \end{enumerate}
\end{comment}
