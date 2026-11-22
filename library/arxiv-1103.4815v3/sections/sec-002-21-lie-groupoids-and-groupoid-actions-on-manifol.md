---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-002-21-lie-groupoids-and-groupoid-actions-on-manifol
section_title: "Lie Groupoids and Groupoid Actions on Manifolds"
section_number: 2.1
pages: 5-6
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.787
latex_coverage_ratio: 0.971
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
We assume that the reader is familiar with the notions of Lie groupoids, smooth functors and smooth natural transformations. 
\begin{comment}
\textsf{}A \emph{Lie category} is a small category $\mathcal{C}$ whose sets $\mathcal{C}_0$ of objects and $\mathcal{C}_{1}$ morphisms are smooth manifolds, its target and source maps $t,s: \mathcal{C}_1 \to \mathcal{C}_0$ are surjective submersions, the identity map $\id: \mathcal{C}_0 \to \mathcal{C}_1$ is an embedding and the composition $\circ: \mathcal{C}_1 \lli{s}\times_t \mathcal{C}_1 \to \mathcal{C}_1$ is smooth. A functor $F:\mathcal{C} \to \mathcal{C}'$ between Lie categories is called \emph{smooth}, if its components $F_0:C_0 \to C_0'$ and $F_1: \mathcal{C}_1 \to \mathcal{C}_1'$ are smooth maps. Finally, a natural transformation $\eta: F \Rightarrow F'$ between functors $F,F': \mathcal{C} \to \mathcal{C}'$ is called smooth, if its component map $\eta: \mathcal{C}_0 \to \mathcal{C}_1'$ is smooth. A \emph{Lie groupoid} is a Lie category $\mathcal{C}$ in which all morphisms are invertible, and the inversion $i: \mathcal{C} \to \mathcal{C}$ is smooth.  
\end{comment}
In this paper, the following examples of Lie groupoids  appear:

\begin{example}
\label{example_groupoids}
\label{exliecat}
\begin{enumerate}[(a)]
\item \label{exM}
Every smooth manifold $M$ defines a Lie groupoid  denoted by $\idmorph{M}$ whose objects and morphisms are $M$, and all of whose structure maps are identities.

\item \label{exBG}
Every Lie group $G$ defines a Lie groupoid denoted by $\mathcal{B}G$, with one object, with $G$ as its smooth manifold of morphisms, and with the composition  $g_2 \circ g_1 := g_2g_1$.

\item
Suppose $X$ is a smooth manifold and $\rho:H \times X \to X$ is a smooth left action of a Lie group $H$  on $X$. Then, a Lie groupoid $\act X H$ is defined with objects $X$ and morphisms $H \times X$, and with
\begin{equation*}
s(h,x) := x
\quad\text{, }\quad
t(h,x) := \rho(h,x) 
\quad\text{ and }\quad
\id_x := (1,x)\text{.}
\end{equation*}
The composition is
\begin{equation*}
(h_2,x_2) \circ (h_1,x_1) := (h_2h_1,x_1)\text{,}
\end{equation*}
where $x_2 = \rho(h_1,x_1)$. The Lie groupoid $\act X H$ is called the \emph{action groupoid} of the action of $H$ on $X$.

\item \label{extHG}
Let $t: H \to G$ be a homomorphism of Lie groups. Then, 
\begin{equation*}
\rho: H \times G \to G: (h,g) \mapsto (t(h)g)
\end{equation*}
defines a smooth left action of $H$ on $G$. Thus, we have a Lie groupoid $\act G H$. 

\item
To every Lie groupoid $\Gamma$ one can associate an \emph{opposite Lie groupoid} $\Gamma^{\mathrm{op}}$ which has the source and the target map exchanged.

\end{enumerate}
\end{example}


We say that a \emph{right action} of a Lie groupoid $\Gamma$ on a smooth manifold $M$
is a pair $(\alpha,\rho)$ consisting of smooth maps $\alpha: M \to \Gamma_0$ and $\rho: M \lli \alpha \times_{t} \Gamma_1 \to M$ such that
\begin{equation*}
\rho(\rho(x,g),h)= \rho(x,g \circ h)
\quad\text{, }\quad
\rho(x,\id_{\alpha(x)})=x
\quad\text{ and }\quad
\alpha(\rho(x,g)) = s(g)
\end{equation*}
for all possible $g,h\in \Gamma_1$, $p\in \Gamma_0$ and $x\in M$. The map $\alpha$ is  called  \emph{anchor}. Later on we will replace the letter $\rho$ for the action by the symbol $\circ$ that denotes the composition of the groupoid.  A \emph{left action} of $\Gamma$ on $M$ is a right action of the opposite Lie groupoid $\Gamma^{\mathrm{op}}$. A smooth map $f:M \to M'$ between  $\Gamma$-spaces with actions $(\alpha,\rho)$ and $(\alpha',\rho')$ is called \emph{$\Gamma$-equivariant} if 
\begin{equation*} 
\alpha' \circ f=\alpha
\quad\text{ and }\quad
f(\rho(x,g)) = \rho' (f(x),g)\text{.}
\end{equation*}



\begin{example}
\label{exliegroupoidact}
\begin{enumerate}[(a)]
\item
Let $\Gamma$ be a Lie groupoid. Then, $\Gamma$ acts on the right on its morphisms $\Gamma_1$ by  $\alpha :=s$ and $\rho := \circ\;$. It acts on the left on its morphisms by $\alpha:= t$ and $\rho:=\circ\;$. 


\item
Let $G$ be a Lie group. Then, a right/left action of the Lie groupoid $\mathcal{B}G$ (see Example \ref{example_groupoids} \erf{exBG}) on $M$ is the same as an ordinary smooth right/left action of $G$ on  $M$. 

\item
Let $X$ be a smooth manifold. A right/left action of $\idmorph X$ (see Example \ref{example_groupoids} \erf{exM}) on $M$ is the same as a smooth map $\alpha: M \to X$. 

\end{enumerate}
\end{example}
