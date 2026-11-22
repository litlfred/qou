---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-010-34-curvature-2-functors
section_title: "Curvature 2-Functors"
section_number: 3.4
pages: 22-25
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.878
latex_coverage_ratio: 0.989
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec5_1}
\label{sec3_4}

In this section we provide a class of examples of transport 2-functors coming from transport functors, i.e. fibre bundle with connections. If $P$ is a principal $G$-bundle with connection $\omega$ over $M$, one can compare the parallel transport maps along two paths $\gamma_1,\gamma_2:x \to y$ by an automorphism of $P_y$, namely the holonomy around the loop $\gamma_2 \circ \gamma_1^{-1}$,
\begin{equation*}
\tau_{\gamma_2} = \mathrm{Hol}_{\omega}(\gamma_2 \circ \gamma_1^{-1}) \circ \tau_{\gamma_1}\text{.}
\end{equation*}
If the paths $\gamma_1$ and $\gamma_2$ are the source and the target of a bigon $\Sigma:\gamma_1\Rightarrow \gamma_2$, this holonomy is  related to the curvature of $\nabla$. So, a principal $G$-bundle with connection does not only assign fibres $P_x$ to points $x\in M$ and parallel transport maps $\tau_{\gamma}$ to paths, it also assigns a curvature-related quantity to bigons $\Sigma$.


Under the equivalence between principal $G$-bundles with connection and transport functors on $X$ with $\mathcal{B}G$-structure (Theorem \ref{th3}), the principal bundle $(P,\omega)$ corresponds to the transport functor
\begin{equation*}
\mathrm{tra}_P: \mathcal{P}_1(M) \to G\text{-}\mathrm{Tor}
\end{equation*}
that assigns the fibres $P_x$ to points $x\in M$ and the parallel transport maps $\tau_{\gamma}$ to paths $\gamma$. Adding an assignment for bigons  yields a \quot{curvature 2-functor}
\begin{equation*}
K(\mathrm{tra}_P): \mathcal{P}_2(M) \to \ttc{G\text{-}\mathrm{Tor}}
\end{equation*}
where $\ttc{G\text{-}\mathrm{Tor}}$ is the category $G\text{-}\mathrm{Tor}$ regarded as a strict 2-category with a unique 2-morphism between each pair of 1-morphisms. The uniqueness of the 2-morphisms expresses the fact that the curvature is  determined by the parallel transport. 


More generally, let us  start with a  transport functor $\mathrm{tra}: \mathcal{P}_1(M) \to T$ with $\mathcal{B}G$-structure for some Lie group $G$ and some functor $i:\mathcal{B}G \to T$. 
\begin{comment}
We recall from \cite{schreiber3} that this means that there exists a surjective submersion $\pi:Y \to M$, a functor $\mathrm{triv}:\mathcal{P}_1(Y) \to \mathcal{B}G$ and a natural equivalence
\begin{equation*}
t: \pi^{*}\mathrm{tra} \to \mathrm{triv}_i
\end{equation*}
such that its descent data is smooth: the functor $\mathrm{triv}$ is smooth, and the natural transformation $g:\pi_1^{*}\mathrm{triv}_i \to \pi_2^{*}\mathrm{triv}_i$ factors through a smooth natural transformation $\tilde g: \pi_1^{*}\mathrm{triv} \to \pi_2^{*}\mathrm{triv}$, i.e. $g(\alpha) = i(\tilde g(\alpha))$ for every $\alpha\in Y^{[2]}$.
\end{comment}
The \emph{curvature 2-functor} of $\mathrm{tra}$ is the strict 2-functor
\begin{equation*}
K(\mathrm{tra}): \mathcal{P}_2(M) \to \ttc{T}
\end{equation*}
which is on objects and 1-morphisms equal to $\mathrm{tra}$ and  on 2-morphisms  determined by the fact that $\ttc{T}$ has a exactly one 2-morphism between each pair of 1-morphisms. In the same way, we obtain a strict 2-functor
\begin{equation*}
K(i): \ttc{\mathcal{B}G} \to \ttc{T}
\end{equation*}
We observe that the Lie 2-groupoids $\ttc{\mathcal{B}G}$ and $\mathcal{BE}G$ (see Section \ref{sec:features}) are canonically isomorphic under the assignment
\begin{equation*}
\bigon{\ast}{\ast}{g_1}{g_2}{*}\quad\mapsto\quad\bigon{\ast}{\ast\text{,}}{g_1}{g_2}{g_2g_1^{-1}}
\end{equation*}
so that we obtain a 2-functor $\mathcal{BE}G \to \ttc{\mathcal{B}G} \to \ttc{T}$. Now we are in the position to introduce our explicit example of a transport 2-functor.

\begin{theorem}
\label{th:lem4}
The curvature 2-functor $K(\mathrm{tra})$ is a  transport 2-functor with $\mathcal{BE}G$-structure.
\end{theorem}

\begin{proof}
We construct a local trivialization of $K(\mathrm{tra})$ starting with a local trivialization $(\mathrm{triv},t)$ of $\mathrm{tra}$ with respect to some surjective submersion $\pi:Y \to M$.  Let $\mathrm{dtriv}\maps\mathcal{P}_2(Y) \to \mathcal{BE}G$ be the derivative 2-functor associated to $\mathrm{triv}$ \cite{schreiber5}: on objects and 1-morphisms it is given by $\mathrm{triv}$, and it sends every bigon $\Sigma:\gamma_1\Rightarrow \gamma_2$ in $Y$ to the unique 2-morphism in $\mathcal{BE}G$ between the images of $\gamma_1$ and $\gamma_2$ under $\mathrm{triv}$. A \pe
\begin{equation*}
K(t): \pi^{*}K(\mathrm{tra}) \to K(i) \circ \mathrm{dtriv}
\end{equation*}
is defined as follows. Its component at a point $a\in Y$ is the 1-morphism
\begin{equation*}
K(t)(a):=t(a): \mathrm{tra}(\pi(a)) \to i(*)
\end{equation*}
in $T$. Its component $t(\gamma)$ at a path $\gamma:a \to b$ is the unique 2-morphism in $\ttc{T}$. Notice that since $t$ is a natural transformation, we have a commutative diagram
\begin{equation*}
\alxydim{@C=1.5cm}{\mathrm{tra}(\pi(a)) \ar[r]^{\mathrm{tra}(\pi(\gamma))} \ar[d]_{t(a)} & \mathrm{tra}(\pi(b)) \ar[d]^{t(b)} \\ i(*) \ar[r]_{\mathrm{triv}_i(\gamma)} & i(*)}
\end{equation*}
meaning that $t(\gamma)=\id$. This defines the \pt\ $t$ as required. 

Now we assume that the descent data $(\mathrm{triv},g_t)$ associated to the local trivialization $(\mathrm{triv},t)$ is smooth, and show that then also the descent object $(\mathrm{dtriv},g_{K(t)},\psi,f)$ is smooth. As observed in \cite{schreiber5}, the derivative 2-functor $\mathrm{dtriv}$ is smooth if and only if $\mathrm{triv}$ is smooth. To extract the remaining descent data according to the procedure described in Section \ref{sec:loctriv}. It turns out that the only non-trivial descent datum is the \pt\ 
\begin{equation*}
g_{K(t)}: \pi_1^{*}\mathrm{dtriv}_{K(i)} \to \pi_2^{*}\mathrm{dtriv}_{K(i)}\text{.}
\end{equation*}
Its component at a point $\alpha\in Y^{[2]}$ is given by $g_{K(t)}(\alpha) := g_t(\alpha)$, and its component at some path $\Theta:\alpha \to \alpha'$ is  the identity. 

The last step is to show that 
\begin{equation*}
\holo(g_{K(t)}): \mathcal{P}_1(Y^{[2]}) \to \Lambda_{K(i)}\ttc{T}
\end{equation*}
is a transport functor with $\Lambda\mathcal{BE}G$-structure.
To do so we have to find a local trivialization with smooth descent data. This is here particulary simple: the functor $\holo(g_{K(t)})$ is \emph{globally} trivial in the sense that it factors through the functor
\begin{equation*}
\Lambda K(i):\Lambda\mathcal{BE}G \to \Lambda_{K(i)}\ttc{T}\text{.}
\end{equation*}
To see this we use the smoothness condition on the natural transformation $g_t$, namely that it factors through a smooth natural transformation $\tilde g_t$. We obtain a smooth pseudonatural transformation $\tilde g_{K(t)}: \pi_1^{*}\mathrm{dtriv} \to \pi_2^{*}\mathrm{dtriv}$ such that $g_{K(t)} = K(i) (\tilde g_{K(t)})$. This finally gives us
\begin{equation*}
\holo(g_{K(t)}) = \Lambda K(i) \circ \holo(\tilde g_{K(t)})
\end{equation*}  
meaning that $\holo(g_{K(t)})$ is a transport functor with $\Lambda\mathcal{BE}G$-structure.
\end{proof}




Since the value of the curvature 2-functor $K(\mathrm{tra})$ on bigons does not depend on the bigon itself but only on its source and target path, we have the following.

\begin{proposition}
\label{prop5}
The curvature 2-functor $K(\mathrm{tra})$ of any transport functor  is flat.
\end{proposition}

This proposition gains a very nice interpretation when we relate the curvature of a connection $\omega$ in a principal $G$-bundle $p:P\to M$ to the  curvature 2-functor $K(\mathrm{tra}_P)$ associated to the corresponding transport functor $\mathrm{tra}_P$. First we show:

\begin{lemma}
\label{lem2}
The curvature 2-functor $K(\mathrm{tra}_P): \mathcal{P}_2(M) \to \ttc{G\text{-}\mathrm{Tor}}$ has a canonical smooth $p$-local trivialization $(p,t,\mathrm{triv})$. The classical curvature $\mathrm{curv}(\omega) \in \Omega^2(P,\mathfrak{g})$ is the 2-curving of  $K(\mathrm{tra}_P)$ with respect to the trivialization $(p,t,\mathrm{triv})$.
\end{lemma}

\begin{proof}
As described in detail in \cite[Section 5.1]{schreiber3}, $\mathrm{tra}_P$ admits local trivializations with respect to the surjective submersion $p:P \to M$ and with smooth descent data $(\mathrm{triv}',g)$ such that the connection 1-form $\omega \in \Omega^1(P,\mathfrak{g})$ of the bundle $P$ corresponds to the smooth functor $\mathrm{triv}':\mathcal{P}_1(P) \to \mathcal{B}G$ under the bijection of \cite[Proposition 4.7]{schreiber3}. Then, by \cite[Lemma 3.5]{schreiber5}, the 2-form $B'$ associated to $\mathrm{dtriv}'$ under the bijection \erf{bij}, which is by Definition \ref{def:curv} (i) the 2-curving of $K(\mathrm{tra}_P)$, is given by
\begin{equation*}
B'=\mathrm{d}\omega + [\omega \wedge \omega]\text{.}
\end{equation*}
The latter is by definition the curvature of the connection $\omega$. 
\end{proof}

The announced  interpretation of Proposition \ref{prop5} now is  as follows: using Lemma \ref{lem2} one can  calculate the curvature $\mathrm{curv}(K(\mathrm{tra}_P))$ of the curvature 2-functor of $\mathrm{tra}_P$. The calculation involves the second Bianchi identity for the connection $\omega$ on the principal $G$-bundle $P$, and the result is
\begin{equation*}
\mathrm{curv}(K(\mathrm{tra}_P)) = 0\text{,}
\end{equation*}
which is according to Proposition \ref{prop3} an independent proof of Proposition \ref{prop5}. In other words, Proposition \ref{prop5} is equivalent to the \emph{second Bianchi identity} for connections on fibre bundles.  


\begin{comment}
In case that $G$ is an abelian Lie group $A$ the situation is simplified by the fact that there exists a canonical smooth 2-functor $\mathrm{pr}_A: \mathcal{BE}A \to \mathcal{BB}A$ given by
\begin{equation*}
\mathrm{pr}_A\quad:\quad\bigon{\ast}{\ast}{g_1}{g_2}{g_2g_1^{-1}} \quad \mapsto \bigon{\ast}{\ast}{}{}{g_2g_1^{-1}}
\end{equation*} 
The composition of $\mathrm{pr}_A$ with $K(i)$ yields a 2-functor $\mathcal{BB}A \to \ttc{T}$. We leave it to the reader to prove  the following lemma.

\begin{lemma}
If $\mathrm{tra}:\mathcal{P}_1(M) \to T$ is a transport functor with $\mathcal{B}A$-structure, the curvature 2-functor $K(\mathrm{tra})$ is a  globally trivial transport 2-functor with $\mathcal{BB}A$-structure. 
\end{lemma}

\begin{proof}
To see that $K(\mathrm{tra})$ is a transport 2-functor with $\mathcal{BB}A$-structure  we simply use the local trivialization $K(t)$ from the proof of Lemma \ref{lem4} which lead to the \pt\ $g_{K(t)}=K(i)(\tilde g_{K(t)})$. We modify $K(t)$ by attaching the canonical \pt\  $\rho: K(i) \to i_A \circ \mathrm{pr}_A$, where $i_A: \mathcal{BB}A \to \hat T$ is the constant 2-functor. The pseudonatural transformation $g'_{K(t)}$ associated to this trivialization is then given by $g'_{K(t)} = i_A(\mathrm{pr}_A(\tilde g_{K(t)}))$. This shows that $K(\mathrm{tra})$ is a transport 2-functor with $\mathcal{BB}A$-structure.
Since the projection $\mathrm{pr}_A$ killed  the only non-trivial datum in $\tilde g_{K(t)}$, it follows that $g'_{K(t)}$ is the identity transformation, in particular $\pi_1^{*}\mathrm{dtriv}=\pi_2^{*}\mathrm{dtriv}$. Hence $\mathrm{dtriv}$ is a globally defined smooth 2-functor.
\end{proof}

As a consequence, if $P$ is a principal $A$-bundle over $M$ with connection $\omega$, its curvature  $\mathrm{curv}(\omega)\in \Omega^2(M,\mathfrak{a})$ is  precisely the  2-form which corresponds to $K(\mathrm{tra}_P)$ under the bijection of Theorem \ref{th1}.
\end{comment}
