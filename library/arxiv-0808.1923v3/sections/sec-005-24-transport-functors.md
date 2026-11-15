---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-005-24-transport-functors
section_title: "Transport Functors"
section_number: 2.4
pages: 10-12
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.993
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec3_5}
\label{sec:smoothnessconditions}


The second tool we need for Section \ref{sec6_3} is the concept of a transport functor. 
Transport functors are an axiomatic formulation of  connections in fibre bundles -- they are the one-dimensional analogue of transport 2-functors, the axiomatic formulation of connections on non-abelian gerbes we are aiming at in the present article. We have introduced and discussed transport functors in \cite{schreiber3}.


From a general perspective, the definition of a \quot{transport $n$-functor} is supposed to rely on a recursive principle in the sense that it uses transport $(n-1)$-functors.  This is one reason to recall the definition of a transport functor. The other reason is to highlight the analogy between the two definitions, which might be helpful to notice: 

\begin{enumerate}[(a)]
\item 
Instead of the path 2-groupoid $\mathcal{P}_2(X)$, we are looking at the \emph{path groupoid} $\mathcal{P}_1(X)$, obtained by just taking objects and 1-morphisms of $\mathcal{P}_2(X)$. A transport functor is a certain functor
\begin{equation*}
F: \mathcal{P}_1(X) \to T\text{,}
\end{equation*}
for some target category $T$: it assigns objects in $T$ -- the \quot{fibres} -- to the points of $X$, and morphisms in $T$ -- the \quot{parallel transport maps} -- to paths in $X$. 

\item
In order to say which functors are transport functors we need a Lie groupoid $\mathrm{Gr}$ and a functor $i\maps \mathrm{Gr} \to T$.
A \emph{local $i$-trivialization} of $F$ is a surjective submersion $\pi:Y \to X$, a functor $\mathrm{triv}: \mathcal{P}_1(Y) \to \mathrm{Gr}$, and a natural equivalence
\begin{equation*}
\alxydim{}{\mathcal{P}_1(Y) \ar[r]^{\pi_{*}} \ar[d]_{\mathrm{triv}} & \mathcal{P}_1(X) \ar@{=>}[dl]|*+{t} \ar[d]^{F} \\ \mathrm{Gr} \ar[r]_{i} & T\text{.} }
\end{equation*}

\item
Associated to a local trivialization is a \emph{descent object}: it is a pair $(\mathrm{triv},g)$ consisting of the functor $\mathrm{triv}: \mathcal{P}_1(Y) \to \mathrm{Gr}$ and of a natural equivalence
\begin{equation*}
g: \pi_1^{*}\mathrm{triv}_i \to \pi_2^{*}\mathrm{triv}_i
\end{equation*}
satisfying a cocycle condition. 

\end{enumerate}
The final step in the definition of a transport functor is the characterization of \emph{smooth descent data}. 
\begin{enumerate}
\item[(d)]
A descent object $(\mathrm{triv},g)$ is called \emph{smooth}, if the functor \begin{equation*}
\mathrm{triv}: \mathcal{P}_1(X)\to \mathrm{Gr}
\end{equation*}
is smooth, i.e. internal to diffeological spaces, and if the components map 
\begin{equation*}
g: Y^{[2]} \to \mathrm{Mor}(T)
\end{equation*}
of the natural equivalence $g$ is the composition of a \emph{smooth} map $\tilde g: Y^{[2]} \to \mathrm{Mor}(\mathrm{Gr})$ with $i: \mathrm{Gr} \to T$. 

\end{enumerate}
In view of the analogy between  (a) - (c) and  Sections \ref{sec:path2groupoid} and \ref{sec:loctriv}, (d) is the analogue of the forthcoming Section \ref{sec:smoothdescent}. Summarizing, we have: 




\begin{definition}[{{\cite[Definition 3.6]{schreiber3}}}]
A \emph{transport functor on $X$ with values in $T$ and with $\mathrm{Gr}$-structure} is a locally $i$-trivializable functor
\begin{equation*}
F: \mathcal{P}_1(X) \to T
\end{equation*}
with smooth descent data. 
\end{definition} 


Transport functors form a category which we denote by $\transportX{i}{1}{\mathrm{Gr}}{T}$.
The main result of our paper \cite{schreiber3} is that transport functors are an axiomatic formulation of connection on fibre bundles. 

In order to illustrate that, and since we need this result later several times, we provide the following example.  let $G$ be a Lie group, and let $\gbunX$ be the category of principal $G$-bundles with connection over $X$. Further, we denote by $\mathcal{B}G$ the Lie groupoid with one object and morphisms $G$, by $G\text{-}\mathrm{Tor}$ the category of $G$-torsors, and by $i: \mathcal{B}G \to G\text{-}\mathrm{Tor}$ the functor that sends the single object of $\mathcal{B}G$ to $G$, regarded as a $G$-torsor over itself. Then, we have:

\begin{theorem}[{{\cite[Theorem 5.8]{schreiber3}}}]
\label{th3}
\label{th2}
Let $X$ be a smooth manifold. The assignment
\begin{equation*}
\gbunX \to \transportX{i}{1}{\mathcal{B}G}{G\text{-}\mathrm{Tor}}: (P,\omega) \mapsto F_{P,\omega}
\end{equation*}
defined by
\begin{equation*}
F_{P,\omega}(x) := P_x \quand
F_{P,\omega}(\gamma) := \tau_{\gamma}\text{,}
\end{equation*}
where $x\in X$, $\gamma\in PX$, and $\tau_\gamma$ is the parallel transport of $\omega$ along $\gamma$, establishes a surjective equivalence of categories.
\end{theorem}

\setsecnumdepth{3}
