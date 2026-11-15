---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-007-sufficiency-of-commutative-frobenius-relations-a
section_title: "Sufficiency of Commutative Frobenius Relations Among CF Generators"
section_number: null
pages: 41-46
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.979
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:sufficient}
Recall that there is a \textit{silly functor} defined in \ref{defn:Sillyfunctor}, \[
S: \operatorname{Cob}( 2) \to \operatorname{Cob}( 3)_{S^2, CF}
\]
sending disjoint unions of $n$-copies of $S^1$ to disjoint unions of $n$-copies of $S^2$, and the genus $g$ bordism \[
	[\Sigma_g \setminus int( \sqcup^{n_{inc}+n_{out}}D^2)]: \sqcup^{n_{inc}}S^1 \to \sqcup^{n_{out}}S^1
\]
to the bordism \[
	[\#^g(S^2 \times S^1) \setminus int( \sqcup^{n_{inc}+n_{out}}D^3)]: \sqcup^{n_{inc}}S^2 \to \sqcup^{n_{out}}S^2.
\]

Let's examine what this functor does to local failure models. Unsurprisingly, it maps $\operatorname{Cob}(2) $ non-trivial local failure types, to $\operatorname{Cob}(3)_{S^2,CF}$ relations by 
\begin{align*}
(0,1)_{B,D} &\mapsto (0,1)_{B,D} \\
(1,2)_{B,D} &\mapsto (2,3)_{B,D}\\
(1,1)_{X,\text{assoc}} & \mapsto (1,1)_{X,\text{assoc}}\\
(1,1)_{X,\text{coassoc}}&\mapsto (2,2)_{X,\text{coassoc}}\\
(1,1)_{X,\text{Frobenius}}&\mapsto (1,2)_{X,\text{Frobenius}}
\end{align*}

It also behaves well with the associated Morse data: note that $S([M]\circ [N]) = S([M])\circ S([N])$ and $S([\Sigma_g]) = [\#^g S^2\times S^1]$. In particular, if $M$ is a representative of $[M]$ with Morse function $f$ inducing decomposition $M=M_1 \cup \dots  \cup M_n$, then there exists a manifold $N $ a representative of $S([M])$ with Morse function $F$ inducing decomposition $N=N_1 \cup \dots \cup N_n$ such that the Morse decompositions are mapped to each other:  \[
S([M_i]) = [N_i],\quad  \forall i = 1, \dots , n
.\]

See figure \ref{fig:sillymap} for a simple example. Note that there are infinitely many choices of such $F$ on $N$, and, by composing with suitable monotonically increasing functions, in fact infinitely many $F$ that additionally has the same as critical values as those of $f$. Therefore WLOG we impose the condition that $F$ has the same critical values as those of $f$.

\begin{notations}
For simplicity and abusing the notations, we refer to any representative $N \in S([M])$ as $S(M)$, and any Morse function $F:N \to \mathbb{R}$, with the same critical values as $f$ and inducing $N= N_1 \cup \dots N_n$ such that $S([M_i])=[N_i]$, as $S(f)$.
\end{notations}
\begin{figure}[ht]
    \centering
    \incfig{sillymap}
\caption[Morse data between $\operatorname{Cob}( 2) $ and $\operatorname{Cob}( 3)_{S^2} $ ]{The behavior of Morse data under the isomorphism $S: \operatorname{Cob}( 2) \to \operatorname{Cob}( 3)_{S^2}$. $S(f) : S(M) \to \mathbb{R}$ is any Morse function such that it has the same critical values as $f$, and induces decomposition $S(M) = N_1  \cup \dots \cup N_n$ such that $S([M_i])=[N_i]$.}
    \label{fig:sillymap}
\end{figure}




Naively, when one is given a morphism $[M]$ in $\operatorname{Cob}( 2) $ and two different compositions related by a single 2-dimensional commutative Frobenius relation, one may use the silly functor $S$ on $[M]$ and its two compositions to get a morphism $S([M])$ in $\operatorname{Cob}( 3)_{S^2, CF} $ with two compositions related by a 3-dimensional commutative Frobenius relation. 

Because the silly functor $S: \operatorname{Cob}( 2) \to \operatorname{Cob}( 3)_{S^2, CF}$ is an isomorphism, this also works the other way around: given a morphism $[N]$ in $\operatorname{Cob}( 3)_{S^2, CF}$ and two distinct compositions related by a single commutative Frobenius relation, one can use the inverse silly functor to get $S^{-1}([N])$ in $\operatorname{Cob}( 2)$ and two compositions related by a single commutative Frobenius relations.

The next proposition \ref{prop:keyprop} says that this process is repeatable, and in fact has a Cerf-theoretic lift: given two Morse functions $f_0 ,f_1 :M \to \mathbb{R}$ and a path $f_t$ between them, one can construct a path $F_t $ between $F_0 , F_1 :S(M) \to \mathbb{R}$, where $S(M)$ is a representative of $S([M])$, and $F_{0,1}$ is induced by $f_{0,1} $. Along this path except with at finitely many isolated singularities, the function is not only admissible excellent Morse, but importantly also spherical. The isolated singularities also match those (non-trivial) singularities of $f_t$ in the sense that they are the $S$-image of local failures.

The strategy of the proof is simple: to construct $F_t: S(M)\to \mathbb{R}$, follow $f_t:M\to \mathbb{R}$ and use it as a blueprint. More specifically, whenever one encounters a specific singularity along $f_t$, isolates a local region $U$ of the manifold $M$ where the topology change occurs, and consider its image $S(U)$ in $S(M)$. All the commutative Frobenius relations in $\operatorname{Cob}( 3)_{S^2,CF} $ can be described by some basic paths $\tilde{F}_t$, so we declare that over $S(U)$ the path of functions takes the form $\tilde{F}_t$, and outside $U$ the path of functions is constant. Then we can glue the two paths of functions together with a bump function over a collared neighbourhood of $\partial S(U)$.

The reader is warned that the wording of the proposition and technical aspects of the proof may obscure the intuition and the proof strategy outlined above.

\begin{prop} \label{prop:keyprop}
Let $\left[ M \right] $ be a morphism in $\operatorname{Cob}(2) $ and $f_0 ,f_1 :M \to \mathbb{R}$ two admissible excellent Morse functions. Let $f_t$ be a path from $f_0 $ to $f_1 $ where $f_t $ fails to be excellent Morse at time $\left\{ t_1 <t_2 < \dots < t_n \right\} $ of non-trivial local failure type $\left\{ T_1, T_2, \dots , T_n \right\}  $, and possibly of trivial local failure type $(1,1)_X$ at other times $\left\{ \widehat{t}_1< \dots < \widehat{t}_m \right\} $. Then there exists a path $F_t$ connecting $S(f_0 ) ,S(f_1 ) : S(M) \to \mathbb{R} $ which fails to be admissible excellent spherical Morse only at time $\left\{ t_1, \dots , t_n \right\} $ of local failure type $\left\{ S(T_1), \dots , S(T_n) \right\} $.
\end{prop}

\begin{proof}
WLOG we can choose the critical values of $F_0$ and $F_1$ to be the same as those of $f_0 , f_1$. Indeed, for any $\left\{ x_1 <\dots x_k \right\} $ and $\left\{ y_1 <\dots <y_k \right\} $, there exists a monotonically increasing smooth function mapping  $x_i$ to $y_i$, and we can always take a smooth interpolation from the identity to this function.

Take a strict total ordering of all the times that $f_t$ fails to be excellent Morse: $\left\{ \tau_1 ,\tau_2, \dots , \tau _{n+m} \right\} $ such that each $\tau_j$ is either in $\left\{ t_1 , \dots , t_n \right\} $ or $\left\{ \widehat{t}_1, \dots , \widehat{t}_m \right\} $, corresponding to non-trivial local failures or trivial ones. Let $\epsilon>0$ be small enough such that $\cap_{j=1}^{m+n} (\tau_j -\epsilon, \tau_j + \epsilon) = \emptyset$, or equivalently \[
\cap_{i=1}^n (t_i - \epsilon, t_i + \epsilon) \cap_{j=1}^m (\widehat{t}_j - \epsilon, \widehat{t}_j + \epsilon)= \emptyset
.\]

We shall construct the path $F_t: I \times M \to \mathbb{R}$ from $F_0 = S(f_0 ) $ to $F_1 = S(f_1 )$ satisfying the desired property. First we split the path $f_t$ into $n+m+1$ segments: \[
(0, \tau _1 -\epsilon), (\tau _1 +\epsilon, \tau _2 -\epsilon), \dots , (\tau _{n+m} +\epsilon, 1) 
.\]

Over any such segment, $f_t$ is excellent good Morse and the Morse data are diffeomorphic. For the ``base case'', let $F_{\tau_1 -\epsilon}$ have the same critical values as $f_{\tau _1 -\epsilon}$, and let $F_t$ be the smooth interpolation from $F_0$ to $F_{\tau_1 -\epsilon}$.

Suppose $F_t$ is defined up to and including $\tau_i-\epsilon$, we will construct $F_t$ up to and including $\tau_{i+1}-\epsilon$. Over the interval $(\tau_i -\epsilon, \tau_i +\epsilon)$, $f_t$ fails to be excellent Morse exactly once at $\tau_i$. There are three possible cases:
\begin{enumerate}
\item the failure is of trivial local failure type $(1,1)_X$.

The Morse data before and after the failure are diffeomorphic, meaning $f_{\tau _i-\epsilon}$ and $f_{\tau _i+\epsilon}$ have diffeomorphic Morse decompositions. Therefore we let $F_t$ be a smooth interpolation from $F_{\tau _i -\epsilon}$ to $F_{\tau_{i+1} -\epsilon}$, where $F_{\tau_{i+1}-\epsilon} = S(f_{\tau _{i+1}-\epsilon})$ has the same critical values as $f_{\tau _{i+1}-\epsilon}$.

\item the failure is of non-trivial local failure type $(j, j+1)_B$ or $(j,j+1)_D$.

We will construct $F_t$ over the time interval $(\tau_i -\epsilon, \tau_i + \epsilon)$ such that $F_t$ is of local failure type $S((j,j+1)_{B,D})$ at $t=\tau_i $.

The birth or death of a pair of critical points of indices $(S(j),S(j)+1)$ is described locally by a path $\tilde{F}_t$ provided by standard Cerf theory. Let $U\subset S(M) $ be a neighbourhood over which $\tilde{F}_t$ is defined. Outside of $U\subset  S(M)$, we can take  $\tilde{G}_t: (\tau _i -\epsilon, \tau _i + \epsilon) \times U^c \to \mathbb{R}$ to be the same as $F_{\tau_i -\epsilon }|_{U^c}$ for all $t \in (\tau _i -\epsilon, \tau _i + \epsilon)$. We then glue $\tilde{F}$ and $\tilde{G}$ together using a bump function, and set the result to be the desired $F_t$ over the interval $(\tau_i -\epsilon, \tau _i +\epsilon)$. We then take a smooth interpolation from $F_{\tau _i +\epsilon}$ to $F_{\tau _{i+1} -\epsilon}=S(f_{\tau _{i+1}-\epsilon})$.

\item the failure is of non-trivial local failure type $(j,k)_{X,w,w'}$ where $w,w'$ are local models of $(j,k)$ before and after the exchange.

We will construct $F_t$ over the time interval $(\tau _i - \epsilon, \tau _i + \epsilon)$ such that $F_t$ is of local failure type $S((j,k)_{X,w,w'})$ at $t=\tau _i$. We use a similar approach to the birth-death type of failure, except instead of gluing a path defined on a neighbourhood, we glue a path defined on the relevant local model. 

First note that for any pairs of local models associated with the $S$-image of a non-trivial local failure type, our settings are simple enough that there exists an evident path of functions on the local model between the two inducing Morse functions. So let $U\subset S(M)$ be a local model induced by $F_{\tau_i -\epsilon}$ of the pair of critical points of index $S(j), S(k)$ whose critical values are being exchanged, namely $U$ is the underlying submanifold of the local model $S(w)$. Choose any local model $\cup_l U_l$ on $U$ diffeomorphic to $S(w')$, then there exists a path of functions $\tilde{F}_t: (\tau_i - \epsilon, \tau_i + \epsilon) \times U \to \mathbb{R}$ from $F_{\tau _i -\epsilon}|_U$ to the Morse function inducing $\cup_l U_l$, such that it is of the desired failure type at $t=\tau _i$. Outside $U$, we can take $\tilde{G}_t : (\tau_i - \epsilon, \tau _i + \epsilon)\times U^c \to \mathbb{R}$ to be the same as $F_{\tau _i - \epsilon}|_{U^c}$. Glue $ \tilde{F}$ and $\tilde{G}$ together to get the desired $F_t: (\tau _i -\epsilon, \tau _i + \epsilon)$ and take a smooth interpolation to $S(f_{\tau _{i+1}-\epsilon})$ at time $\tau _{i+1}-\epsilon$.
\end{enumerate}

Since there are only finitely many $t$ such that $f_t$ fails to be excellent Morse, this process eventually must terminate and all the smooth interpolations are taken from the constructed $F_{\tau_i + \epsilon}$ to $S(f_1)$. Also since $F_0$ is spherical, smooth interpolations preserves spherical-ness, and all local failures are spherical except at the singular point, we have that the constructed path $F_t$ is admissible excellent spherical Morse at all but time $\left\{ t_1 , \dots , t_n \right\} $.
\end{proof}






The power of proposition \ref{prop:keyprop} is that it allows a Cerf-path in $\operatorname{Cob}( 2)$ to lift to a spherical Cerf-path in $\operatorname{Cob}( 3)_{S^2,CF} $. Together with the silly functor $S$, we can show that there is always a spherical Cerf-path between any admissible excellent spherical Morse functions on $N$, a representative of a morphism $[N]$ in $\operatorname{Cob}( 3)_{S^2,CF} $.

\begin{prop}\label{prop:keypropCF}
Let $\left[ N \right] $ be a morphism in $\operatorname{Cob}(3)_{S^2, CF} $ and $F_0 ,F_1 :N \to \mathbb{R}$ two admissible excellent spherical Morse functions. Then there exists a path $F_t$ in $C^\infty(N)$ from $F_0 $ to $F_1 $ which is admissible excellent spherical Morse at all but finitely many $t$. Moreover, the types of failure are of CF type.
\end{prop}

\begin{proof}
Consider $f_0 = S^{-1}(F_0)$ and $f_1 = S^{-1}(F_1)$, both of which are Morse functions on $M$ a representative of $S^{-1}(\left[ N \right] )$. Let $f_t$ be any path of functions from $f_0$ to $f_1$ on $M$. Then by proposition \ref{prop:keyprop}, there exists a path $F_t$ from $S(f_0 ) = S(S^{-1}(F_0)) = F_0$ to $S(f_1 )=S(S^{-1}(F_1))=F_1 $ which fails to be admissible excellent spherical Morse at finitely many times, and the types of failure are of commutative Frobenius type.
\end{proof}

\begin{cor} \label{cor:CFonlycommFrob}
CF bordism generators satisfy no more relations.
\end{cor}

\begin{rmk}
Proposition \ref{prop:keypropCF} and corollary \ref{cor:CFonlycommFrob} addresses the major subtlety of the isomorphism between $\operatorname{Cob}( 2) $ and $\operatorname{Cob}( 3)_{S^2,CF} $: while two compositions of the same morphism $[N]$ in $\operatorname{Cob}( 3)_{S^2,CF}$ are always induced by two Morse functions $F_0, F_1:N\to \mathbb{R}$, a path $F_t^! $ from $F_0 $ to $F_1 $ may fail to be spherical. An example is example \ref{eg:S2xS1pantstoHeegaardtopants}, where $F_0 =F_1: S^2 \times S^1 \to \mathbb{R}$ are both pants decompositions, but the path $F_t^!$ has a segment which is the Heegaard splitting, in particular not spherical.

However by proposition \ref{prop:keypropCF} and corollary \ref{cor:CFonlycommFrob}, we now know that there is always a path $F_t$ from $F_0 $ to $F_1 $ that is spherical all the way except at singularities of commutative Frobenius type. So any two compositions of the same morphisms $[N]$ in $\operatorname{Cob}( 3)_{S^2, CF}$ can always be turned into each other using only commutative Frobenius relations.
\end{rmk}



















\chapter{Prime Relations} \label{ch:prime relations}
