---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-006-local-models-of-excellent-morse-failures
section_title: "Local Models of Excellent Morse Failures"
section_number: null
pages: 38-41
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.996
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:localmodels}
Proposition \ref{prop:CFcommFrob} gives the existence of commutative Frobenius relations among CF generators. We would like to know if they are sufficient-- namely, are there other necessary relations if one wants to give a presentation of the category $\operatorname{Cob}( 3)_{S^2,CF} $? This section introduces a tool which we call \textit{local models of failures}, which the next section uses alongside theorem \ref{thm:Cob2Cob3CFIso} to prove sufficiency.

\begin{defn} \label{defn:Local Model}
(Local Model) Let $f:M\to \mathbb{R}$ be a Morse function. A local model of critical points and indices $((m_j,i_j))_{j=1}^{n}$ is a connected submanifold $U\subset  M$ along with a Morse decomposition induced by $f|_U$: \[
U \cong U_1 \cup_{X_1} U_2 \cup_{X_2 } \cup \dots \cup_{X_{n-1}} U_n \subset  M
.\]
such that each $U_j$ is an elementary cobordism with critical point $m_j \in U_j$ of index $i_j$ satisfying \[
f(m_1)\leq f(m_2)\leq \dots \leq f(m_n)
.\]

If it is clear from context which critical points $(m_j)$ and which submanifold $U$ are being considered, we say the local model is of $(i_j)$ on $U$. Note that a local model on $U$ by definition is equipped with a inducing Morse function defined on at least $U$.

We say two local models $U \cong \cup _{i\in I} U_i, V \cong \cup_{i \in I} V_i$ are diffeomorphic if there exists a diffeomorphism $h:U \to V$ such that $h(U_j) = V_j$ preserves each boundary components (as a set, not necessarily acting as the identity on each boundary component) and $h$ sends critical points to corresponding critical points. 
\end{defn}

\begin{conventions}
This is a subtle convention. Given two local models $U_i, U_{i}'$ of the same critical points on $M$, we assume that they are two Morse decompositions of the same underlying connected submanifold $U\subset  M$. This is so that we can speak of a path of functions between two local models: it is a path of functions on a submanifold $U$ between the two Morse functions inducing the two local models $U_i$ and $U_i'$.
\end{conventions}

\begin{defn} \label{defn:Path of functions between two local models}
(Path of functions between two local models) Let $f_0, f_1 : M \to \mathbb{R}$ be Morse functions inducing two different local models on a connected submanifold $U \subset  M$. A path of functions between local models of $U$ is a path $f_t : I \times U \to \mathbb{R}$ from $f_0|_U $ to $f_1|_U$. Note we do not require that $f_t$ be defined on all of the ambient manifold $M$.
\end{defn}

\begin{eg}
For the associativity relation of $S^2$, figure \ref{fig:assocandcoassoc}-(a) gives two local models for $U=M$ and there exists an evident path of local models of $(1,1)$. This path is described by smoothly moving the two index $2$ critical points towards each other in height, and their critical values ultimately coincide and cross. In this case this path of local models is the same as a path of Morse functions on the whole $M$, which exchanges the critical values of the two critical points. Note that the local models are \textit{not} diffeomorphic: it exchanges boundary components.
\end{eg}





\begin{eg}
Consider the two torus $\Sigma_1 = S^1 \times S^1$ with $U$ the shaded region in figure \ref{fig:localmodelbirth}. Equip the torus on the left with the standard height function. In figure (a), $U$ has no critical points, so it is itself a trivial local model. In figure (b), $U$ has an index 1 critical point and an index $2$ critical point. In order to induce this on the same $\Sigma_1$, the Morse function on $\Sigma_1$ is no longer the height function in figure b. However standard Cerf theory shows there is a path $f_t$ between the height function and the Morse function inducing figure (b). When restricted to $U$, this path gives a path $f_t|_U$ of functions between the trivial local model of $U$ and the local model of indices $(1,2)$ of $U$.
\end{eg}

\begin{figure}[ht]
    \centering
    \incfig{localmodelbirth}
    \caption[A local model of the birth of a pair of critical points]{A local model of the birth of a pair of critical points.}
    \label{fig:localmodelbirth}
\end{figure}







\begin{notations}
Let $f_0 ,f_1 $ be two admissible excellent Morse functions on $M$, and $\gamma :\left[ 0,1 \right] \to C^\infty(M)$ a path from $f_0 $ to $f_1 $. Let $f_t = \gamma (t)$. Then standard Cerf theory applies and $f_t$ is admissible excellent Morse for all but finitely many $t$, say at $\left\{ t_1 ,\dots t_n \right\} $. 
\begin{enumerate}
\item  We say $f_{t_i}$ is of failure type $(j,j+1)_{B}$ or $ (j,j+1)_D $ if two critical points of index $j, j+1$ were created or destroyed at time $t_i$. 
\item We say $f_{t_i}$ is of failure type $(k,l)_X$ if two critical points of index $k,l$ have the same critical value at $f_{t_i}$. The ordering is such that $f_{t_i - \epsilon} (x_k) < f_{t_i - \epsilon}(x_j)$ if $x_k$ is the critical point of index $k$.
\item We say $f_{t_i}$ is of local failure type $(j,j+1)_{B,D}$ if it is of failure type $(j,j+1)_{B,D}$.
\item We say $f_{t_i}$ is of local failure type $(k,l)_{X, M,M'}$ if it is of failure type $(k,l)_X$ and $M,M'$ are local models of $(k,l)$ before and after the exchange.
\item We say $f_{t_i}$ is of trivial local failure type $(k,l)_{X}$ if it is of local failure type $(k,l)_{X,M,M'}$ where $M,M'$ are diffeomorphic local models of $(k,l)$.
\end{enumerate}

In this language, a \textit{relation} between two (non-cylindrical) cobordism generators is either a local failure type $(j,j+1)_{B,D}$ or a non-trivial local failure type $(k,l)_{X,M,M'}$, where $M,M'$ are not the same (i.e. diffeomorphic) local models. To classify relations between CF generators, we want the local models before and after a failure to have only spherical boundaries.
\end{notations}

\begin{rmk}
The need to distinguish failure and local failure is because even though birth/death is purely local, exchanges of critical values are not. However the purpose of introducing local models is so we can isolate a local region and treat the whole region as a whole. Although this is not usually a focal issue in standard Cerf theory or in $\operatorname{Cob}(3)_{S^2, CF}$, presently it is necessary to distinguish $(1,1)_{X}$ exchanges in $\operatorname{Cob}(2) $ by their local models, as illustrated in the following example.
\end{rmk}

\begin{eg}
Consider the standard height function on the two-torus $T=\Sigma_1 \cong S^1 \times S^1$, embedded in  $\mathbb{R}^3$ as in figure \ref{fig:tiltingtorus}. Consider rotating the torus by $\theta(t)$ about the $x$-axis, where $\theta(t) = \pi t$. Then there is a path of maps parametrized by $t$ \[
f_t: T=\Sigma_1 \cong S^1 \times S^1 \hookrightarrow \mathbb{R}^3 \overset{R_x(\theta(t))}{\longrightarrow } \mathbb{R}^3 \overset{proj_z}{\relbar\joinrel\twoheadrightarrow} \mathbb{R}
.\]
such that at $\theta(0)=0$ one recovers the standard height function. As one increases $t$, the critical values of the two index $1$ critical points move towards each other, ultimately coinciding at some $\theta_c(t_c)$. For a time $t=t_c + \epsilon$ slightly after $t_c$, the critical values become distinct again.

\begin{figure}[ht]
    \centering
    \incfig{tiltingtorus}
    \caption[The tilting torus]{The tilting torus. The figure on the left is the standard embedding of the 2-torus. As one rotates the torus, the critical values of the index 1 critical points move towards each other, ultimately coinciding as depicted in the right figure. The critical level set is depicted as the two dashed circles wedged together at two points. For a better visualization, we encourage the reader to cut a few donuts or bagles like so in real life. }
    \label{fig:tiltingtorus}
\end{figure}

Note however that $f_{t_c}$ is of trivial local failure type $(1,1)_X$-- the local models of $(1,1)$, before and after the exchange of critical values, are diffeomorphic-- both are of the form \[
\text{pants} \cup_{S^1 \sqcup S^1} \text{copants}
.\]

Therefore in this tilting torus example, the exchange of the critical values of the two index $1$ critical points do not constitute a relation. 
\end{eg}

\begin{eg}
By remark \ref{rmk:12Bnotspherical}, the birth of the pair of critical points of index $(1,2)$ is not a relation between CF generators because the local model after the birth has torus boundaries.
\end{eg}

\begin{eg}
If $\dim(M)=2$, the possible failure types are \[
\left\{ (0,1)_B, (0,1)_D, (1,2)_B, (1,2)_D, (1,1)_X  \right\} 
.\]
The possible relations, aka non-trivial local failure types are \[
\left\{ (0,1)_B, (0,1)_D, (1,2)_B, (1,2)_D, (1,1)_{X, \text{assoc}}, (1,1)_{X, \text{coassoc}}, (1,1)_{X, \text{Frobenius}} \right\} 
.\]
where the pairs of local models are the evident ones.
\end{eg}

\begin{eg}
If $\dim(M)=3$, the possible failure types are \[
\left\{ (0,1)_B, (0,1)_D, (2,3)_B, (2,3)_D, (1,1)_X, (2,2)_X, (1,2)_X  \right\} 
.\]
The possible relations, aka non-trivial local failure types are \[
\left\{ (0,1)_B, (0,1)_D, (2,3)_B, (2,3)_D, (1,1)_{X, \text{assoc}}, (2,2)_{X, \text{coassoc}}, (1,2)_{X, \text{Frobenius}} \right\} 
.\]
where the pairs of local models are the evident ones.
\end{eg}
