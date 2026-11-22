---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-013-42-abelian-bundle-gerbes-with-connection
section_title: "Abelian Bundle Gerbes with Connection"
section_number: 4.2
pages: 33-36
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.984
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec3_2}


In this section we consider the target 2-category $T=\mathcal{B}(S^1\text{-}\mathrm{Tor})$,  the monoidal category of $S^1$-torsors viewed as a 2-category with a single object \cite[Example A.2]{schreiber6}. Associated to this 2-category is the 2-functor 
\begin{equation*}
i_{S^1}: \mathcal{BB}S^1 \to \mathcal{B}(S^1\text{-}\mathrm{Tor})
\end{equation*}
that sends the single 1-morphism of $\mathcal{BB}S^1$ to the circle, viewed as an $S^1$-torsor over itself. The main result of this section is:
\begin{theorem}
\label{th:bgrb}
There is an equivalence
\begin{equation*}
\mathrm{Trans}_{\mathcal{BB}S^1}(M,\mathcal{B}(S^1\text{-}\mathrm{Tor})) \cong \mathfrak{BGrb}^{\nabla}(M) 
\end{equation*}
between the 2-category of transport 2-functors on $M$ with values in $\mathcal{B}(S^1\text{-}\mathrm{Tor})$ and with $\mathcal{BB}S^1$-structure, and the 2-category of  bundle gerbes with connection over $M$.
\end{theorem}


Let us first recall the definition of  bundle gerbes following \cite{murray,murray2,stevenson1,waldorf1}. For a surjective submersion $\pi:Y \to M$, we first define the following 2-category $\mathfrak{BGrb}^{\nabla}(\pi)$:

\begin{enumerate}
\item
An object is a tuple $(B,L,\omega,\mu)$ consisting of  a 2-form $B\in \Omega^{2}(Y)$, a principal $S^{1}$-bundle $L$ with connection $\omega$ over $Y^{[2]}$ of curvature $\mathrm{curv}(\omega) = \pi_1^{*}B - \pi_2^{*}B$, and an associative, connection-preserving bundle isomorphism 
\begin{equation*}
\mu: \pi_{23}^{*}L \otimes \pi_{12}^{*}L \to \pi_{13}^{*}L
\end{equation*}
over $Y^{[3]}$. 

\item
A 1-morphism $(B,L,\omega,\mu) \to (B',L',\omega',\mu')$, also known as   \emph{stable isomorphism}, is a principal $S^{1}$-bundle $A$ with connection $\varsigma$ over $Y$ of curvature $\mathrm{curv}(\varsigma)=B - B'$ together with a connection-preserving bundle isomorphism 
\begin{equation*}
\alpha:  \pi_2^{*}A \otimes L \to L' \otimes \pi_1^{*}A
\end{equation*}
over $Y^{[2]}$, such that the diagram
\begin{equation}
\label{43}
\alxydim{@C=2cm}{\pi_3^{*}A \otimes \pi_{23}^{*}L \otimes \pi_{12}^{*}L \ar[r]^-{\id\otimes\mu} \ar[d]_{\pi_{23}^{*}\alpha \otimes \id} & \pi_3^{*}A \otimes  \pi_{13}^{*}L  \ar[dd]^{\pi_{13}^{*}\alpha} \\ \pi_{23}^{*}L' \otimes \pi_{2}^{*}A \otimes L \ar[d]_{\id\otimes \pi_{12}^{*}\alpha} & \\ \pi_{23}^{*}L' \otimes \pi_{12}^{*}L'\otimes\pi_1^{*}A   \ar[r]_-{\mu'\otimes\id} & \pi_{13}^{*}L' \otimes \pi_{1}^{*}A}
\end{equation}
of bundle isomorphisms over $Y^{[3]}$ is commutative. 

\item
A 2-morphism $(A,\varsigma,\alpha) \Rightarrow (A',\varsigma',\alpha')$ is a connection-preserving bundle isomorphism $\varphi: A \to A'$ over $Y$, such that the diagram
\begin{equation}
\label{45}
\alxydim{@R=1.3cm@C=1.3cm}{\pi_2^{*}A \otimes L \ar[d]_{\pi_2^{*}\varphi \otimes \id_L} \ar[r]^{\alpha} & L' \otimes \pi_1^{*}A \ar[d]^{\id_{L'} \otimes \pi_1^{*}\varphi} \\ \pi_2^{*}A' \otimes L \ar[r]_{\alpha'} & L' \otimes \pi_1^{*}A'}
\end{equation}
of bundle isomorphisms over $Y^{[2]}$ is commutative.
\end{enumerate}
The full 2-category of bundle gerbes with connection  over $M$ is then defined as the direct limit
\begin{equation*}
\mathfrak{BGrb}^{\nabla}(M) := \lim_{\overrightarrow{\pi}} \mathfrak{BGrb}^{\nabla}(\pi)\text{.}
\end{equation*}


The strategy to prove Theorem \ref{th:bgrb} is to first establish the equivalence on a local level: 

\begin{proposition}
\label{prop:bgrb}
For every surjective submersion $\pi:Y \to M$ there is a  surjective equivalence of 2-categories:
\begin{equation*}
\transsmooth{i_{S^1}}{2}{\Sigma\Sigmna U(1)} \cong \mathfrak{BGrb}^{\nabla}(\pi)\text{.}
\end{equation*}
\end{proposition}

A 2-functor $\transsmooth{i_{S^1}}{2}{\Sigma\Sigmna U(1)} \to \mathfrak{BGrb}^{\nabla}(\pi)$ realizing the claimed equivalence is defined in the following way. For a smooth descent object $(\mathrm{triv},g,\psi,f)$,  the smooth 2-functor $\mathrm{triv}:\mathcal{P}_2(Y) \to \mathcal{B}\mathcal{B}S^1$ defines by Theorem \ref{th1}  a 2-form $B\in\Omega^2(Y)$, this is the first ingredient of the bundle gerbe. The \pt\ $g$ yields a transport functor 
\begin{equation*}
\holo(g):\mathcal{P}_1(Y^{[2]})
\to \Lambda_{i_{S^1}}\mathcal{B}(S^1\text{-}\mathrm{Tor})
\end{equation*}
with $\Lambda\mathcal{B\mathcal{B}}S^1$-structure. 
Despite of the heavy notation, the following lemma  translates this functor into familiar language. 
\begin{lemma}
\label{lem6}
For $X$ a smooth manifold, there is a canonical surjective equivalence of monoidal categories
\begin{equation*}
\sbunX \cong \transportX{2}{1}{_{\Lambda \mathcal{BB}S^1}}{\Lambda_{i_{S^1}}\mathcal{B}(S^1\text{-}\mathrm{Tor})}
\end{equation*}
between principal $S^1$-bundles with connection and transport functors with $\Lambda\mathcal{BB}S^1$-structure.
\end{lemma}

\begin{proof}
First of all, we have evidently
$\Lambda\mathcal{B}\mathcal{B}S^1 = \mathcal{B}S^1$. Second, there is a canonical equivalence of categories
\begin{equation}
\label{44}
\Lambda_{i_{S^1}}\mathcal{B}(S^1\text{-}\mathrm{Tor}) \cong S^1\text{-}\mathrm{Tor}\text{.}
\end{equation}
This comes from the fact that an object is in both categories an $S^1$-torsor. A morphism between $S^1$-torsors $V$ and $W$ in $\Lambda_{i_{S^1}}\mathcal{B}(S^1\text{-}\mathrm{Tor})$ is by definition a 2-morphism  
\begin{equation*}
\alxydim{@=1.2cm}{\ast \ar[r]^{S^1} \ar[d]_{V} & \ast \ar[d]^{W} \ar@{=>}[dl]|*+{f} \\ \ast \ar[r]_{S^1} & \ast }
\end{equation*}
in $\mathcal{B}(S^1\text{-}\mathrm{Tor})$, and this is in turn an $S^1$-equivariant map
\begin{equation*}
f: W \otimes S^1 \to S^1 \otimes V\text{.}
\end{equation*}
It can be identified canonically with an $S^1$-equivariant map $f^{-1}: V \to W$, i.e. a morphism in $S^1\text{-}\mathrm{Tor}$. It is straightforward to see that \erf{44} is even a monoidal equivalence. Then, the claim is proved by Theorem \ref{th3}.
\end{proof}

 Now, via Lemma \ref{lem6}  the transport functor $\holo(g)$ is  a principal $S^1$-bundle $L$ with connection $\omega$ over $Y^{[2]}$. This circle bundle will be the second ingredient of the bundle gerbe.
\begin{lemma}
\label{lem8}
The curvature of the connection $\nabla$ on the circle bundle $L$ satisfies \begin{equation*}
\mathrm{curv}(\omega)=\pi_1^{*}B - \pi_2^{*}B\text{.}
\end{equation*}
\end{lemma}

\begin{proof}
Let $U_{\alpha}$ be open sets covering $Y^{[2]}$, and let $(\widetilde{\mathrm{triv}},\tilde t)$ be a local $i_{S^1}$-trivialization of the transport functor $\holo(g)$ consisting of smooth functors $\widetilde{\mathrm{triv}}_{\alpha}: \mathcal{P}_1(U_{\alpha}) \to \mathcal{B}S^1$ and natural transformations
\begin{equation*}
\tilde t_{\alpha}:  \holo(g)|_{U_{\alpha}} \to (\widetilde{\mathrm{triv}}_{\alpha})_{i_{S^1}}\text{.}
\end{equation*}
We observe that the functors $\widetilde{\mathrm{triv}}_{\alpha}$ and the natural transformation $\tilde t_{\alpha}$ lie in the image of the functor $\holo$, such that there exist smooth \pt s $\rho_{\alpha}: \pi_1^{*}\mathrm{triv}|_{U_{\alpha}} \to \pi_2^{*}\mathrm{triv}|_{U_{\alpha}}$ and modifications $t_{\alpha}: g|_{U_{\alpha}} \Rightarrow \rho_{\alpha}$ with 
\begin{equation*}
\widetilde{\mathrm{triv}}_{\alpha} = \holo(\rho_{\alpha})
\quad\text{ and }\quad
\tilde t_{\alpha} = \holo(t_{\alpha})\text{.}
\end{equation*}
As found in \cite{schreiber5} and reviewed in Section \ref{sec3_1} of the present article, associated to the smooth \pt\ $\rho_{\alpha}$ is a 1-form $\varphi_{\alpha}\in \Omega^1(U_{\alpha})$,
and equation \erf{55} infers in the present situation
\begin{equation*}
\pi_{1}^{*}B - \pi_2^{*}B =  \mathrm{d}\varphi_{\alpha}\text{.}
\end{equation*}
It remains to trace back the relation between $\varphi_{\alpha}$ and the curvature of the connection $\omega$ on circle bundle $L$. Namely, if $A_{\alpha}$ is the 1-form corresponding to the smooth functor $\widetilde{\mathrm{triv}}_{\alpha}$, we have
\begin{equation*}
A_{\alpha} = \varphi_{\alpha}
\quad\text{ and }\quad
\mathrm{d}A_{\alpha} = \mathrm{curv}(\omega)\text{.}
\end{equation*}
This shows the claim. 
\end{proof}

In order to complete the construction of the bundle gerbe, we note that the modification $f\maps \pi_{23}^{*}g \circ \pi_{12}^{*}g \Rightarrow \pi_{13}^{*}g$ induces an isomorphism 
\begin{equation*}
\holo(f): \pi_{23}^{*}\holo(g) \otimes \pi_{12}^{*}\holo(g) \to \pi_{13}^{*}\holo(g)
\end{equation*}
of transport functors; again by Lemma \ref{lem6} this defines an isomorphism
\begin{equation*}
\mu : \pi_{12}^{*}L \otimes \pi_{23}^{*}L \to \pi_{13}^{*}L 
\end{equation*}
of circle bundles with connection, which is the last ingredient of the bundle gerbe. The coherence axiom of \cite[Definition 2.2.1]{schreiber6}
implies the associativity condition on $\mu$. This shows that $(B,L,\nabla,\mu)$ is a bundle gerbe with connection. The descent datum $\psi$ has been forgotten by this construction.

Using Lemma \ref{lem6} in the same way as just demonstrated it is easy to assign bundle gerbe 1-morphisms to descent 1-morphisms and bundle gerbe 2-morphisms to descent 2-morphisms. Here the  coherence conditions of \cite[Definitions 2.2.2 and 2.2.3]{schreiber6}  translate  into the commutative diagrams \erf{43} and \erf{45}. The composition  for 1-morphisms and 2-morphisms  of bundle gerbes (which we have not carried out above) is precisely reproduced by the composition laws of the descent 2-category $\transsmooth{i_{S^1}}{2}{}$. This defines the 2-functor of Proposition \ref{prop:bgrb}. 

It is  evident that this 2-functor is an equivalence of 2-categories, since all manipulations we have made are equivalences according to Lemma \ref{lem6} and Theorem \ref{th1}. It remains to remark that the descent datum $\psi$ can be reproduced in a canonical way from a given bundle gerbe using the existence of dual circle bundles, see Lemma 1 in \cite{waldorf1}.
This finishes the proof of Proposition \ref{prop:bgrb}.



It is clear that the equivalence of Proposition \ref{prop:bgrb} is compatible with the refinement of surjective submersions, so that it given an equivalence in the direct limits:
\begin{equation*}
\mathfrak{Des}^2(i_{S^1})^{\infty}_M
 \cong \mathfrak{BGrb}^{\nabla}(M)\text{.}
\end{equation*}
With Theorem \ref{th4} this proves Theorem \ref{th:bgrb}.
