---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-012-41-differential-non-abelian-cohomology
section_title: "Differential Non-Abelian Cohomology"
section_number: 4.1
pages: 25-33
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.96
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec4_1}

In this section we  set up a classifying theory for transport 2-functors $\mathcal{P}_2(M) \to T$ with structure Lie 2-groupoid $i: \mathcal{B}\mathfrak{G} \to T$, for $\mathfrak{G}$ a Lie 2-group coming from a smooth crossed module $(G,H,t,\alpha)$, $T$ an arbitrary 2-category, and $i$ an equivalence of categories. The latter condition together with Theorem \ref{th4} implies that we have equivalences  
\begin{equation}
\label{mainseq}
\transport{}{2}{\mathcal{B}\mathfrak{G}}{T}\cong \transsmoothpi{i}{2}{\mathrm{Gr}}{}_M \cong \transsmoothpi{\id_{\mathcal{B}\mathfrak{G}}}{2}{\mathrm{Gr}}{}_M  \end{equation}
of 2-categories. 

Our strategy is to translate the structure of the 2-category $\transsmoothpi{\id_{\mathcal{B}\mathfrak{G}}}{2}{\mathrm{Gr}}{}_M$ into  an equivalent 2-category of \quot{non-abelian differential cocycles} made up of smooth functions and differential forms, with respect to open covers of $M$.
Isomorphism classes of non-abelian differential cocycles form a set which we define as the \emph{non-abelian differential cohomology} of $M$; it classifies transport 2-functors on $M$ with $\mathcal{B}\mathfrak{G}$-structure up to isomorphism. 





\subsubsection{Smooth Functors and Differential Forms}



For the translation of the 2-category $\transsmoothpi{\id_{\mathcal{B}\mathfrak{G}}}{2}{\mathrm{Gr}}{}_M$ into  smooth functions and differential forms we recall a general result about  the 2-category $\mathrm{Funct}^{\infty}(\mathcal{P}_2(X),\mathcal{B}\mathfrak{G})$ of smooth 2-functors, smooth \pt s, and smooth modifications defined on a smooth manifold $X$, with values in the Lie 2-groupoid $\mathcal{B}\mathfrak{G}$. Following \cite[Section 2.2]{schreiber5}, it corresponds to the following structure expressed in terms of smooth functions and differential forms:



\begin{enumerate}[(i)]
\item 
A smooth 2-functor $F:\mathcal{P}_2(X) \to \mathcal{B}\mathfrak{G}$ induces a pair of differential forms: a 1-form $A\in\Omega^1(X,\mathfrak{g})$ with values in the Lie algebra of $G$, and a 2-form $B\in\Omega^2(X,\mathfrak{h})$ with values in the Lie algebra of $H$, such that
\begin{equation}
\label{42}
\mathrm{d}A + [A
\wedge A] = t_{*} \circ B\text{.}
\end{equation}

 
\item
A smooth pseudonatural transformation $\rho:F \to F'$ gives rise to a 1-form $\varphi\in\Omega^1(X,\mathfrak{h})$ and a smooth map $g:X \to G$, such that
\begin{eqnarray}
A' + t_{*} \circ \varphi &=& \mathrm{Ad}_g(A) - g^{*}\bar\theta   
\label{57}\\\label{55}
B' + \alpha_{*}(A' \wedge \varphi) + \mathrm{d}\varphi + [\varphi \wedge \varphi]&=& (\alpha_g)_{*} \circ B  \text{.}
\end{eqnarray}
The identity $\id:F \to F$ has $\varphi=0$ and $g=1$. If $\rho_1$ and $\rho_2$ are composable \pt s, the 1-form of their composition $\rho_2\circ\rho_1$ is $(\alpha_{g_{2}})_{*} \circ\varphi_1 +  \varphi_2$, and the smooth map is $g_2g_1:X \to G$.


\item
A smooth modification $\mathcal{A}: \rho \Rightarrow \rho'$ gives rise to a smooth map $a:X \to H$, such that
\begin{equation}
\label{58}
g' = (t \circ a) \cdot g
\quad\text{ and }\quad
\varphi' +(r_{a}^{-1} \circ \alpha_{a})_{*}(A') =  \mathrm{Ad}_a (\varphi) -a^{*}\bar\theta\text{.}
\end{equation}
The identity modification $\id_{\rho}$ has $a=1$. If two modifications $\mathcal{A}_1$ and $\mathcal{A}_2$ are vertically composable, $\mathcal{A}_2 \bullet \mathcal{A}_1$ has the map $a_2a_1$. If two modifications $\mathcal{A}_1:\rho_1 \Rightarrow \rho_1'$ and $\mathcal{A}_2:\rho_2 \Rightarrow \rho_2'$ are horizontally composable, $\mathcal{A}_2 \circ \mathcal{A}_1$ has the map $a_2\alpha(g_2,a_1)$.

\end{enumerate}
The structure (i), (ii) and (iii)  forms a strict 2-category $\diffco{\mathfrak{G}}{2}{X}$, which we call the  \emph{2-category of $\mathfrak{G}$-connections on $X$} \cite{schreiber5}. 




\begin{theorem}[{{\cite[Theorem 2.20]{schreiber5}}}]
\label{th1}
The correspondences described above furnish a strict 2-functor
\begin{equation*}
\alxydim{@C=1.5cm}{\mathrm{Funct}^{\infty}(\mathcal{P}_2(X),\mathcal{B}
\mathfrak{G}) \ar[r]^-{\mathcal{D}} &  \diffco{\mathfrak{G}}{2}{X}\text{,}}
\end{equation*}
which is an isomorphism of 2-categories.
\end{theorem}

We remark that  we have already used this isomorphism on the level of objects as a bijection \erf{bij}.


For a general Lie 2-group $\mathfrak{G}$ the correspondence between a smooth 2-functor $F: \mathcal{P}_2(X) \to \mathcal{B}\mathfrak{G}$ and the pair $(A,B)$ with $A\in \Omega^1(X,\mathfrak{g})$ and $B\in \Omega^2(X,\mathfrak{h})$ is established by an iterated integration and described in detail in \cite[Section 2.3.1]{schreiber5}. For the Lie 2-group $\mathfrak{G}=\mathcal{B}S^1$ it reduces to the following relation.



\begin{lemma}
\label{sfdfbsone}
Let $B \in \Omega^2(X)$ be a 2-form. Then, the smooth 2-functor $F: \mathcal{P}_2(X) \to \mathcal{BB}S^1$ that corresponds to $B$ under the isomorphism of Theorem \ref{th1} is given by
\begin{equation*}
F(\Sigma) = \exp \left (- \int_{[0,1]^2} \Sigma^{*}B \right )\text{,}
\end{equation*}
for all bigons $\Sigma \in BX$. 
\end{lemma}


\begin{proof}
We go through the construction in \cite[Section 2.3.1]{schreiber5} and reduce everything to the case $\mathfrak{G}=\mathcal{B}S^1$. The 1-form $\mathcal{A}_{\Sigma}$ in \cite[Equation 2.26]{schreiber5} is
\begin{equation*}
\mathcal{A}_{\Sigma} = -\int_{[0,1]} \Sigma^{*}B \in \Omega^1([0,1])\text{,}
\end{equation*}
with the integration performed over the second factor of $[0,1]^2$. It extends (due to the sitting instants of $\Sigma$) to a 1-form on $\R$, and so corresponds via \cite[Proposition 4.7]{schreiber3}  to a smooth functor $F_{\mathcal{A}_{\Sigma}}\maps\mathcal{P}_1(\R) \to \mathcal{B}S^1$, which is just a smooth map $f_{\Sigma}: \R \times \R \to S^1$. The correspondence between the 1-form $\mathcal{A}_{\Sigma}$ and the function $f_{\Sigma}$ is by \cite[Lemma 4.1]{schreiber3}:
\begin{equation*}
f_{\Sigma}(t_0,t_1) = \exp \left ( \int_{t_0}^{t_1} -\mathcal{A}_{\Sigma} \right )\text{.}
\end{equation*} 
According to the prescription, \cite[Equation 2.27]{schreiber5} and \cite[Proposition 2.17]{schreiber5} define
\begin{equation*}
F(\Sigma) = f_{\Sigma}(0,1)^{-1} = \exp \left (  \int_{0}^{1}  \mathcal{A}_{\Sigma} \right ) = \exp \left ( -\int_{[0,1]^2} \Sigma^{*}B \right )\text{.}\vspace{-1em}
\end{equation*}
\end{proof}









\subsubsection{Non-abelian Differential Cocycles}

We want to translate the structure of the  2-category $\transsmoothpi{\id_{\mathcal{B}\mathfrak{G}}}{2}{\mathrm{Gr}}{\pi}$ of smooth descent data with respect to a surjective submersion $\pi:Y \to M$ into smooth functions and differential forms, using Theorem \ref{th1} as a dictionary.  




We recall that an object in $\transsmooth{\id_{\mathcal{B}\mathfrak{G}}}{2}{}$ is a collection $(\mathrm{triv},g,\psi,f)$ containing a smooth 2-functor $\mathrm{triv}\maps\mathcal{P}_2(Y) \to \mathcal{B}\mathfrak{G}$, a \pt\
$g: \pi_1^{*}\mathrm{triv} \to \pi_2^{*}\mathrm{triv}$
whose associated functor $\holo(g_{0}):\mathcal{P}_1(Y^{[2]}) \to \mathcal{B}\mathfrak{G}$ is a transport functor, and  modifications $\psi$ and $f$ whose associated natural transformations $\mathscr{F}(\psi)$ and $\mathscr{F}(f)$ are morphisms between transport functors. 

We begin with looking at a sub-2-category $\mathcal{U} \subset \transsmooth{\id_{\mathcal{B}\mathfrak{G}}}{2}{}$ in which all pseudonatural transformations and modifications are smooth, i.e. correspond to trivial transport functors and morphisms between trivial transport functors. An object $(\mathrm{triv},g_{\infty},\psi_{\infty},f_{\infty})$  in $\mathcal{U}$ corresponds under Theorem \ref{th1} to the following structure:
\begin{enumerate}
\item[(a)]
an object $(A,B) := \fo(\mathrm{triv})$  in $\diffco{\mathfrak{G}}{2}{Y}$, i.e. differential forms $A\in\Omega^1(Y,\mathfrak{g})$ and $B\in\Omega^2(Y,\mathfrak{h})$ satisfying relation \erf{42}.

\item[(b)]
a 1-morphism 
\begin{equation*}
(g,\varphi) := \fo(g_{\infty}):  \pi_1^{*}(A,B) \to \pi_2^{*}(A,B)
\end{equation*}
in $\diffco{\mathfrak{G}}{2}{Y^{[2]}}$, i.e. a smooth function $g:Y^{[2]} \to G$ and a 1-form $\varphi\in\Omega^1(Y^{[2]},\mathfrak{h})$ satisfying the relations \erf{57} and \erf{55}. 

\item[(c)]
a 2-morphism 
\begin{equation*}
f := \fo(f_{\infty}): \pi_{23}^{*}(g,\varphi) \circ \pi_{12}^{*}(g,\varphi)  \Rightarrow \pi_{13}^{*}(g,\varphi)
\end{equation*}
in $\diffco{\mathfrak{G}}{2}{Y^{[3]}}$ and a 2-morphism
\begin{equation*}
 \psi := \fo(\psi_{\infty}): \id_{(A,B)} \Rightarrow \Delta^{*}(g,\varphi)
\end{equation*} 
in $\diffco{\mathfrak{G}}{2}{Y}$; these are smooth functions $f:Y^{[3]} \to H$ and $\psi: Y \to H$ satisfying relations \erf{58}.
\end{enumerate}
The coherence conditions for $f_{\infty}$ and $\psi_{\infty}$ \cite[Definition 2.2.1]{schreiber6} imply the following equations of smooth functions, expressed as pasting diagrams: 
\begin{equation}
\label{eq:diffob1}
\alxydim{@C=1.3cm@R=1.9cm}{\pi_2^{*}(A,B) \ar[r]^{\pi_{23}^{*}(g,\varphi)} \ar@{<-}[d]_{\pi_{12}^{*}(g,\varphi)}
& \pi_{3}^{*}(A,B) \ar[d]^{\pi_{34}^{*}(g,\varphi)} \\ \pi_1^{*}(A,B)  \ar[ur]|{\pi_{13}^{*}(g,\varphi)}="2" \ar@{=>}[u];"2"|{\pi_{123}^{*}f} \ar[r]_{\pi_{14}^{*}(g,\varphi)}="1"
&  \ar@{<=}"1";"2"|{\pi_{134}^{*}f} \pi_{4}^{*}(A,B)}
=
\alxydim{@C=1.3cm@R=1.9cm}{\pi_2^{*}(A,B) \ar[dr]|{\pi_{24}^{*}(g,\varphi)}="2" \ar[r]^{\pi_{23}^{*}(g,\varphi)} \ar@{<-}[d]_{\pi_{12}^{*}(g,\varphi)}
& \pi_{3}^{*}(A,B) \ar[d]^{\pi_{34}^{*}(g,\varphi)}  \ar@{<=}"2";[]|{\pi_{234}^{*}f}
 \\  \pi_1^{*}(A,B)  \ar[r]_{\pi_{14}^{*}(g,\varphi)}="1"
\ar@{<=}"1";"2"|{\pi_{124}^{*}f}& \pi_{4}^{*}(A,B)}
\end{equation}
in the 2-category $\diffco{\mathfrak{G}}{2}{Y^{[4]}}$ and
\begin{equation}
\label{eq:diffob2}
\alxydim{@R=1.1cm@C=-0.2cm}{& \pi_2^{*}(A,B) \ar[dr]|{\Delta_{22}^{*}(g,\varphi)}="3" \ar@/^3pc/[dr]^{\id_{\pi_2^{*}(A,B)}}="2" \ar@{=>}"2";"3"|-{\pi_2^{*}\psi} & \\ \pi_1^{*}(A,B) \ar[ur]^{(g,\varphi)} \ar[rr]_{(g,\varphi)}="1" && \pi_2^{*}(A,B) \ar@{=>}[ul];"1"|>>>>>{\Delta_{122}^{*}f} }
\hspace{-0.8cm}= \id_{(g,\varphi)} = \hspace{-0.8cm}
\alxydim{@R=1.1cm@C=-0.2cm}{& \pi_1^{*}(A,B) \ar[dr]^{(g,\varphi)} & \\ \pi_1^{*}(A,B) \ar[ur]|{\Delta_{11}^{*}(g,\varphi)}="3"
\ar@/^3pc/[ur]^{\id_{\pi_1^{*}(A,B)}}="2" \ar@{=>}"2";"3"|-{\pi_1^{*}\psi} \ar[rr]_{(g,\varphi)}="1" && \pi_2^{*}(A,B) \ar@{=>}[ul];"1"|>>>>>{\Delta_{112}^{*}f} }
\end{equation}
in the 2-category $\diffco{\mathfrak{G}}{2}{Y^{[2]}}$.
We call the structure (a), (b), (c) subject to the two conditions
\erf{eq:diffob1} and \erf{eq:diffob1} a \emph{differential $\mathfrak{G}$-cocycle} for the surjective submersion $\pi:Y \to X$. 


We proceed similarly with a  1-morphism $(h_{\infty},\varepsilon_{\infty})$ between  objects $(\mathrm{triv},g_{\infty},\psi_{\infty},f_{\infty})$ and $(\mathrm{triv}',g'_{\infty},\psi'_{\infty},f'_{\infty})$ in $\mathcal{U}$, and obtain:
\begin{enumerate}
\item [(d)]
a 1-morphism
$(h,\phi) := \mathcal{D}(h_{\infty}): (A,B) \to (A',B')$
in $\diffco{\mathfrak{G}}{2}{Y}$, i.e. a smooth function $h\maps Y \to G$ and a 1-form $\phi\in\Omega^1(Y,\mathfrak{h})$ satisfying relations \erf{57} and \erf{55},

\item[(e)]
 a 2-morphism 
$\varepsilon := \mathcal{D}(\varepsilon): \pi_2^{*}(h,\phi) \circ (g,\varphi) \Rightarrow (g',\varphi') \circ \pi_1^{*}(h,\phi)$
in $\diffco{\mathfrak{G}}{2}{Y^{[2]}}$, i.e. a smooth function $\varepsilon: Y^{[2]} \to H$ satisfying \erf{58}. 
\end{enumerate}
The coherence conditions of Definition \cite[Definition 2.2.2]{schreiber6} result in the identities 
\begin{equation}
\label{eq:diff1morph1}
\alxydim{@C=1.2cm@R=1.2cm}{(A,B) \ar@/^2.5pc/[r]^{\id}="1" \ar[r]|{\Delta^{*}(g,\varphi)}="2"
\ar@{=>}"1";"2"|{\psi} \ar[d]_{(h,\phi)} & (A,B) \ar[d]^{(h,\phi)}
\ar@{=>}[dl]|{\Delta^{*}\varepsilon} \\ (A',B') \ar[r]_{\Delta^{*}(g',\varphi')} & (A',B')}
=
\alxydim{@C=1.2cm@R=1.2cm}{(A,B) \ar[r]^{\id} \ar[d]_{(h,\phi)} & (A,B) \ar[d]^{(h,\phi)}
\ar@{=>}[dl]|{\id_{(h,\phi)}} \\ (A',B') \ar@/_2.5pc/[r]_{\Delta^{*}(g',\varphi')}="2"   \ar[r]|{\id}="1" & (A',B') \ar@{=>}"1";"2"|{\psi'}}
\end{equation}
in the 2-category  $\diffco{\mathfrak{G}}{2}{Y}$ and
\begin{equation}
\label{eq:diff1morph2}
\alxydim{@R=1.2cm@C=-0.3cm}{&\pi_2^{*}(A,B) \ar@/^1pc/[dr]^-{\pi_{23}^{*}(g,\varphi)}&\\ \pi_1^{*}(A,B) \ar@/^1pc/[ur]^-{\pi_{12}^{*}(g,\varphi)} \ar[rr]^{\pi_{13}^{*}(g,\varphi)}="1" \ar@{=>}[ur];"1"|{^{}f} \ar[d]_{\pi_1^{*}(h,\phi)}
&&\pi_3^{*}(A,B) \ar[d]^{\pi_3^{*}(h,\phi)} \ar@{=>}[dll]|{\pi_{13}^{*}\varepsilon}
\\ \pi_1^{*}(A',B') \ar[rr]_{\pi_{13}^{*}(g',\varphi')} && \pi_3^{*}(A',B')'}
=
\alxydim{@R=1.2cm@C=0.8cm}{\pi_1^{*}(A,B)\ar[d]_{\pi_1^{*}(h,\phi)} \ar[r]^{\pi_{12}^{*}(g,\varphi)}
& \pi_2^{*}(A,B) \ar[d]|{\pi_2^{*}(h,\phi)} \ar@{=>}[dl]|{\pi_{12}^{*}\varepsilon} \ar[r]^{\pi_{23}^{*}(g,\varphi)}
&\pi_3^{*}(A,B) \ar[d]^{\pi_3^{*}(h,\phi)} \ar@{=>}[dl]|{\pi_{23}^{*}\varepsilon} \\\pi_1^{*}(A',B')  \ar@/_3.3pc/[rr]_{\pi_{13}^{*}(g',\varphi')}="2"
\ar@{=>}[r];"2"|{f'} \ar[r]_{\pi_{12}^{*}(g',\varphi')}
& \pi_2^{*}(A',B')\ar[r]_{\pi_{23}^{*}(g',\varphi')} & \pi_3^{*}(A',B')}
\end{equation}
in the 2-category  $\diffco{\mathfrak{G}}{2}{Y^{[3]}}$. The structure (d), (e) subject to the conditions \erf{eq:diff1morph1} and \erf{eq:diff1morph2} is called a \emph{1-morphism between differential $\mathfrak{G}$-cocycles} for the surjective submersion $\pi$.

Finally, a  2-morphism induces   a 2-morphism $E: (h,\phi) \Rightarrow (h',\phi')$ in $\diffco{\mathfrak{G}}{2}{Y}$, i.e. a smooth function $E:Y \to H$ that satisfies \erf{58}, and the coherence condition of \cite[Definition 2.2.3]{schreiber6} infers the identity 
\begin{equation*}
\hspace{-0.4cm}
\alxydim{@C=0.7cm@R=1.2cm}{\pi_1^{*}(A,B) \ar[r]^{(g,\varphi)} \ar@/_2.5pc/[d]_{\pi_1^{*}(h',\phi')}="2"
\ar[d]^{\pi_1^{*}(h,\phi)}="1" \ar@{=>}"1";"2"|-{\pi_1^{*}E} &  \pi_2^{*}(A,B)
\ar@{=>}[dl]|{\varepsilon}
\ar[d]^{\pi_2^{*}(h,\phi)} \\ 
\pi_1^{*}(A',B')\ar[r]_{(g',\varphi')} &\pi_2^{*}(A',B') }
=
\alxydim{@C=0.7cm@R=1.2cm}{\pi_1^{*}(A,B) \ar[r]^{(g,\varphi)} 
\ar[d]_{\pi_1^{*}(h',\phi')}& \pi_2^{*}(A,B)
\ar@/^2.5pc/[d]^{\pi_2^{*}(h,\phi)}="2"
\ar@{=>}[dl]|{\varepsilon'}
\ar[d]_{\pi_2^{*}h_2}="1" \ar@{=>}"2";"1"|{\pi_2^{*}E}   \\ \pi_1^{*}(A',B')
\ar[r]_{(g',\varphi')} & \pi_2^{*}(A',B')}
\end{equation*}
in the 2-category $\diffco{\mathfrak{G}}{2}{Y^{[2]}}$. Such data is called a \emph{2-morphism between differential $\mathfrak{G}$-cocycles}.


We have now collected, in a systematical way, objects, 1-morphisms, and 2-morphisms of a 2-category, the  \emph{2-category of degree two differential $\mathfrak{G}$-cocycles}, which we denote by $\diffco{\mathfrak{G}}{2}{\pi}$. By construction we have a 2-functor
\begin{equation*}
\alxydim{@C=1.5cm}{ \transsmoothpi{\id_{\mathcal{B}\mathfrak{G}}}{2}{\mathrm{Gr}}{\pi}\supseteq \mathcal{U} \ar[r]^-{\mathcal{D}_{\pi}} & \diffco{\mathfrak{G}}{2}{\pi} \text{,}} 
\end{equation*}
and Theorem \ref{th1} implies immediately that it is an isomorphism of 2-categories.

Next we argue that for certain surjective submersions, the sub-2-category $\mathcal{U}$ is in fact equivalent to $\transsmoothpi{\id_{\mathcal{B}\mathfrak{G}}}{2}{\mathrm{Gr}}{\pi}$. These are submersions for which $Y$ and $Y^{[2]}$ have contractible connected components; we will call these \emph{two-contractible}. Any good open cover gives rise to a two-contractible surjective submersion; in particular, any surjective submersion can be refined by a two-contractible one. 


\begin{proposition}
\label{prop1}
Let $\mathfrak{G}$ be a Lie 2-group and let $\pi:Y \to M$ be a two-contractible  surjective submersion. Then, the inverse of the 2-functor $\mathcal{D}_{\pi}$ induces an equivalence of categories:
\begin{equation*}
\diffco{\mathfrak{G}}{2}{\pi} \cong \transsmooth{\id_{\mathcal{B}\mathfrak{G}}}{2}{}\text{.} \end{equation*}
\end{proposition}

\begin{proof}
By \cite[Corollary 3.13]{schreiber3} transport functors over contractible manifolds are naturally equivalent to smooth functors. This applies to the transport functors $\mathscr{F}(g)$  contained in a descent object
$(\mathrm{triv},g,\psi,f)$, and to the transport functor $\mathscr{F}(h)$ contained in a descent 1-morphism $(h,\varepsilon)$. Such natural equivalences induce a descent 1-morphism $(\mathrm{triv},g,\psi,f) \cong (\mathrm{triv},g_{\infty},\psi',f')$ and a descent 2-morphism $(h,\varepsilon) \cong (h_{\infty},\varepsilon')$ with $g_{\infty}$ and $h_{\infty}$ smooth. Since the embedding of smooth functors into transport functors is full, all the modifications $\psi'$, $f'$, $\varepsilon'$ are then automatically smooth. This shows that $\transsmooth{\id_{\mathcal{B}\mathfrak{G}}}{2}{}$ is equivalent to its subcategory $\mathcal{U}$. \end{proof}





\subsubsection{Explicit Local Data}

\label{sec:localdata}


In order to make the structure of the 2-category $\diffco{\mathfrak{G}}{2}{\pi}$ of degree two differential $\mathfrak{G}$-cocycles more transparent, we shall spell out all details in case that the surjective submersion $\pi$ comes from an  open cover $\mathfrak{V}=\left \lbrace V_i \right \rbrace$ of $M$. In particular, we express the diagrammatic equations  above in terms of actual equations, using the relation between the Lie 2-groupoid $\mathcal{B}\mathfrak{G}$ and the crossed module $(G,H,t,\alpha)$ established in  Section \ref{sec:features}.


Firstly, a differential $\mathfrak{G}$-cocycle  $((A,B),(g,\varphi),\psi,f)$ has the following smooth functions and differential forms:
\begin{enumerate}
\item[(a)] 
On every open set $V_i$, 
\begin{equation*}
\psi_i: V_i \to H
\quad\text{, }\quad
A_i \in \Omega^1(V_i,\mathfrak{g})
\quad\text{ and }\quad
B_i \in \Omega^2(V_i,\mathfrak{h})\text{.}
\end{equation*}

\item[(b)]
On every two-fold intersection $V_i \cap V_j$, 
\begin{equation*}
g_{ij}:V_i \cap V_j \to G
\quad\text{ and }\quad
\varphi_{ij} \in \Omega^1(V_i \cap V_j,\mathfrak{h})\text{.}
\end{equation*}
\item[(c)]
On every three-fold intersection $V_i \cap V_j \cap V_k$,
\begin{equation*}
f_{ijk}:V_i \cap V_j \cap V_k \to H\text{.}
\end{equation*}
\end{enumerate}  
The cocycle conditions are the following:
\begin{enumerate}
\item 
Over every open set $V_i$,
\begin{eqnarray}
\label{31}
\mathrm{d}A_i + [A_i \wedge A_i] &=& t_{*}(B_i)
\\
\label{31a}
g_{ii}&=&t(\psi_i)
\\
\varphi_{ii}&=&-(r^{-1}_{\psi_i} \circ\alpha_{\psi_i})_{*}(A_i) - \psi_i^{*}\bar\theta\text{.}\nonumber
\end{eqnarray}
\item
Over every two-fold intersection $V_i \cap V_j$,
\begin{eqnarray}
\nonumber
A_j &=&\mathrm{Ad}_{g_{ij}}(A_{i}) - g_{ij}^*\bar\theta- t_{*}(\varphi_{ij})
\\
\nonumber
B_j  &=& (\alpha_{g_{ij}})_{*}(B_i)- \alpha_{*}(A_j \wedge \varphi_{ij}) - \mathrm{d}\varphi_{ij} - [\varphi_{ij}\wedge \varphi_{ij}]
\\
\label{31b}
1&=&f_{ijj}  \psi_j = f_{iij} \, \alpha_{g_{ij}}(\psi_i)\text{.}
\end{eqnarray}
\item
Over every three-fold intersection $V_i \cap V_j \cap V_k$,
\begin{eqnarray*}
g_{ik} &=& t(f_{ijk})  g_{jk}g_{ij}
\\
\mathrm{Ad}_{f_{ijk}}(\varphi_{ik})&=& (\alpha_{g_{jk}})_{*}(\varphi_{ij}) + \varphi_{jk} + (r_{f_{ijk}}^{-1} \circ \alpha_{f_{ijk}})_{*}(A_k) + f_{ijk}^{*}\bar\theta\text{.}
\end{eqnarray*}

\item
Over every four-fold intersection $V_i \cap V_j \cap V_k \cap V_l$,
\begin{equation}
\label{31c}
f_{ikl} \alpha(g_{kl},f_{ijk})=f_{ijl}f_{jkl}\text{.}
\end{equation}
\end{enumerate} 
Additionally, the curvature of the differential cocycle is according to Definition \ref{def:curv} given by
\begin{equation*}
H_i := \mathrm{d}B_i + \alpha_{*}(A_i \wedge B_i) \in \Omega^3(V_i,\mathfrak{h})\text{.}
\end{equation*}

Secondly, a 1-morphism $((h,\varepsilon),\phi)$ between differential cocycles $((A,B),(g,\varphi),\psi,f)$ and $((A',B'),(g',\varphi'),\psi',f')$ has the following structure:
\begin{enumerate}
\item[(a)]
On every open set $V_i$,
\begin{equation*}
h_{i}:V_{i} \to G
\quad\text{ and }\quad
\phi_{i}\in\Omega^1(V,\mathfrak{h})\text{.}
\end{equation*}
\item[(b)]
On every two-fold intersection $V_i \cap V_j$,
\begin{equation*}
\epsilon_{ij}:V_i \cap V_j \to H\text{.}
\end{equation*}
\end{enumerate}
The following conditions have to be satisfied:
\begin{enumerate}
\item 
Over every open set $V_i$,
\begin{eqnarray}
\label{32}
B_i' &=& (\alpha_{h_i})_{*}(B_i) - \alpha_{*}(A_i' \wedge \phi_i) - \mathrm{d}\phi_i - [\phi_i \wedge \phi_i]
\\
\label{32a}
A'_i &=& \mathrm{Ad}_{h_i}(A_i) - t_{*}(\phi_i) - h_i^{*}\bar\theta
\\
\label{32b}
\psi_i'&=& \epsilon_{ii}\alpha(h_i,\psi_i)\text{.}
\end{eqnarray}

\item
Over every two-fold intersection $V_i \cap V_j$,
\begin{eqnarray}
\label{32c}
g_{ij}' &=& t(\epsilon_{ij})h_jg_{ij}h_i^{-1}
\\
\label{32d}
\varphi_{ij}' &=& \mathrm{Ad}_{\epsilon_{ij}}((\alpha_{h_j})_{*}(\varphi_{ij}) + \phi_j) 
- (\alpha_{g_{ij}'})_{*}(\phi_i) - (r_{\varepsilon_{ij}}^{-1} \circ \alpha_{\epsilon_{ij}})_{*}(A'_{j}) - \epsilon_{ij}^{*}\bar\theta
\end{eqnarray}
\item
Over every three-fold
 intersection $V_i \cap V_j \cap V_k$,
\begin{equation}
\label{32f}
f_{ijk}' = \epsilon_{ik}\alpha(h_k,f_{ijk})\alpha(g'_{ik},\epsilon_{ij}^{-1})\epsilon_{jk}^{-1}\text{.}
\end{equation}
\end{enumerate}
Finally, a 2-morphism  $E$ between differential cocycles has, for any open set $V_i$, a smooth function $E_i: V_{i} \to H$  such that on every open set $V_i$
\begin{eqnarray*}
h'_i &=& t(E_i) h_i
\\
\phi'_i &=& \mathrm{Ad}_{E_i} (\phi_i)  - (r^{-1}_{E_i} \circ \alpha_{E_i})_{*}(A'_i)-E_i^{*}\bar\theta
\end{eqnarray*}
and, on every 2-fold intersection $V_i \cap V_j$,
\begin{equation*}
\epsilon_{ij}' = \alpha(g_{ij}',E_i) \epsilon_{ij}E_j^{-1}\text{.}
\end{equation*}

Concluding this discussion we note the following normalization lemma, which we need for the discussion of surface holonomy.
It   can be seen as a 
variant of the maybe familiar normalization result for \v Cech
cocycles.

\begin{lemma}
\label{equiavelncenormalized}
Every differential $\mathfrak{G}$-cocycle with respect to an open cover $\left \lbrace V_i \right \rbrace_{i\in I}$ is 1-isomorphic to a differential $\mathfrak{G}$-cocycle  with 
\begin{equation*} 
\psi_i=1
\quomma
g_{ii}=1
\quomma
f_{iij}=f_{ijj}=1
\quand
f_{iji}=y_{ij}^{-1}\alpha(x_{ij},y_{ij})
\end{equation*}  
for all $i,j\in I$, and  elements $x_{ij}\in G$ and $y_{ij}\in H$. In particular, if $\mathfrak{G}=\mathcal{B}A$ for an abelian Lie group $A$, then $f_{iji}=1$. 
\end{lemma}

\begin{proof}
Suppose $((A,B),(g,\varphi),\psi,f)$ is a differential $\mathfrak{G}$-cocycle with respect to $\left \lbrace V_i \right \rbrace$. It is easy to see that one can always pass to a1-isomorphic cocycle with $\psi_i=1$, $g_{ii}=1$, and $f_{iij}=f_{ijj}=1$. 
\begin{comment}
We look at  the triple $(\phi_i,h_i,\varepsilon_{ij})$ with the differential forms $\phi_i := 0 \in \Omega^1(V_i)$, smooth maps $h_{i} := 1$ on $V_i$, and smooth maps
\begin{equation*}
\varepsilon_{ij} := \begin{cases}\psi_i^{-1} & i=j \\
1 & i \neq j \\
\end{cases}
\end{equation*}
defined on $V_i \cap V_j$. Then we \emph{define} a new differential $\mathfrak{G}$-cocycle $((A',B'),(g',\varphi'),\psi',f')$ via equations \erf{32} to \erf{32f}. We have $\psi'_i = \epsilon_{ii}\alpha(h_i,\psi_i)=\varepsilon_{ii}\psi_i^{-1}=1$. Then,  $g'_{ii}=1$  follows from \erf{31a}, and $f_{iij}'=f_{ijj}'=1$ follows from \erf{31b}. \end{comment}
In order to achieve the remaining condition for $f_{iji}$, we choose a total order on the index set $I$ of the open cover, and look at  smooth maps
\begin{equation*}
\varepsilon_{ij} := \begin{cases}1 & i\leq j \\
f_{iji} & i>j \\
\end{cases}
\end{equation*}
defined on $V_i \cap V_j$. Then we define yet another differential $\mathfrak{G}$-cocycle $((A',B'),(g',\varphi'),\psi',f')$ via  equations \erf{32} to \erf{32f}, and it is straightforward to see that this one has the claimed form.
\begin{comment}
We still have $\psi_i''=1$ and hence still $g_{ii}''=f_{iij}''=f_{ijj}=1$. From \erf{31c} we conclude $\alpha(g_{ij},f_{iji})=f_{jij}$.
Further, we get from \erf{32f}
\begin{equation*}
f_{iji}'' = f'_{iji}\epsilon_{ij}^{-1}\epsilon_{ji}^{-1}\text{.}
\end{equation*}
For $i>j$, this gives $f''_{iji}= f'_{iji}\epsilon_{ij}^{-1}\epsilon_{ji}^{-1} = f_{iji}'f'_{iji}^{-1}=1$, so that $f_{iji}=y_{ij}^{-1}\alpha(x_{ij},y_{ij})$ for $x_{ij}=y_{ij}=1$. For $i < j$, this gives $f_{iji}'' = f'_{iji}f'_{jij}^{-1}=f_{iji}'\alpha(g_{ij},f_{iji}^{-1})$, so that $f_{iji}=y_{ij}^{-1}\alpha(x_{ij},y_{ij})$ for $x_{ij}=g_{ij}$ and $y_{ij}=f_{iji}^{-1}$.
\end{comment}
\end{proof}



\subsubsection{Non-abelian Differential Cohomology}


The 2-categories $\diffco{\mathfrak{G}}{2}{\pi}$ of degree two differential $\mathfrak{G}$-cocycles form a direct system for surjective submersions over $M$, and so do the sets $\hc 0 (\diffco{\mathfrak{G}}{2}{\pi})$ of isomorphism classes of objects.  

\begin{definition}
\label{def:nonco}
The direct limit
\begin{equation*}
\hat H^2(M,\mathfrak{G}) := \lim_{\overrightarrow{\pi}} \hc 0(\diffco{\mathfrak{G}}{2}{\pi})
\end{equation*} 
is called the degree two \emph{differential non-abelian cohomology} of $M$ with values in $\mathfrak{G}$.
\end{definition}


The terminology \quot{non-abelian differential cohomology} is motivated by the following observation. If one drops all differential forms from the local data described in Section \ref{sec:localdata}, and only keeps the smooth functions, the corresponding limit coincides with  the \emph{non-abelian cohomology} $H^2(M,\mathfrak{G})$, as it appears for instance in \cite{giraud,breen2,bartels,wockel1}. Thus, Definition \ref{def:nonco} extends ordinary non-abelian cohomology by differential form data. 

We remark that by Lemma \ref{equiavelncenormalized} and the fact that every surjective submersion can be refined by an open cover, one can define non-abelian differential cohomology by only  using cocycles that are normalized in the sense of Lemma \ref{equiavelncenormalized}. 

Since every surjective submersion can be refined to a two-contractible one (for example, by a good open cover), it also suffices to take the limit over the two-contractible surjective submersions. Then, Proposition \ref{prop1} and Theorem \ref{th4} imply via \erf{mainseq} the following classification result.

\begin{theorem}
\label{th:class}
Let $\mathfrak{G}$ be a Lie 2-group, and let $i: \mathcal{B}\mathfrak{G} \to T$ be an equivalence of 2-categories. Then, there is a bijection
\begin{equation*}
\hc 0 \transport{}{2}{\mathrm{Gr}}{T} \cong \hat H^2(M,\mathfrak{G})\text{.}
\end{equation*}
In other words, transport 2-functors on $M$ with $\mathcal{B}\mathfrak{G}$-structure are classified up to isomorphism by the non-abelian differential cohomology of $M$ with values in $\mathfrak{G}$.
\end{theorem}



Let us specify two particular examples of differential non-abelian cohomology which have appeared before in the literature:
\begin{enumerate}
\item 
The Lie 2-group $\mathfrak{G} = \mathcal{B}S^1$. We leave it as an easy exercise to the reader to check  that our differential non-abelian cohomology is precisely degree two Deligne cohomology,
\begin{equation*}
\hat H^2(M,\mathcal{B}S^1) = H^2(M,\mathcal{D}(2))\text{.}
\end{equation*}
Deligne cohomology \cite{brylinski1} is a well-known local description of abelian gerbes with connection. 

\item
The Lie 2-group $\mathfrak{G}=\mathrm{AUT}(H)$ for $H$ some ordinary Lie group $H$. We also leave it to the reader to check that our differential cocycles are precisely  the local description of connections in  non-abelian gerbes given by Breen and Messing \cite{breen1} (see Remark \ref{rem2} below). Thus, we have an equality
\begin{equation*}
\hat H^2(M,\mathrm{AUT}(H)) = \bigset{5.4cm}{Equivalence classes of local data\\of Breen-Messing $H$-gerbes\\with connection over $M$}  \text{.}
\end{equation*}
\end{enumerate}
Summarizing, the  theory of transport 2-functors covers both Deligne cocycles and Breen-Messing cocycles.

\begin{remark}
\label{rem2}
We remark that condition \erf{31} between the 1-curving $A$ and the 2-curving $B$  of a differential $\mathfrak{G}$-cocycle is present neither  in Breen-Messing gerbes \cite{breen1} nor in the non-abelian bundle gerbes of  \cite{aschieri}, which we discuss in Section \ref{sec3_3}. Breen and Messing call the local 2-form
\begin{equation*}
t_{*}(B_i) - \mathrm{d}A_i - [A_i \wedge A_i]
\end{equation*}
which is here zero by \erf{31}, the \emph{fake curvature} of the gerbe.
In this terminology, transport 2-functors only cover Breen-Messing gerbes with vanishing fake curvature. 

The crucial point is here that unlike transport 2-functors, neither  Breen-Messing gerbes nor   non-abelian bundle gerbes have concepts of holonomy or parallel transport. And indeed, equation \erf{31} comes from an important consistency condition on this parallel transport, namely from the target-source matching condition for the transport 2-functor, which makes it possible to decompose parallel transport into pieces.  So we understand equation \erf{31} as an \emph{integrability condition} which is necessarily for a consistent parallel transport. In other words, vanishing fake curvature is not specifying a subclass of connections, it is a \emph{necessary condition} every connection has to satisfy.


\end{remark}
