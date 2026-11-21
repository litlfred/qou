---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-006-23-tilting-modules-and-the-tilting-category-t
section_title: "Tilting modules and the tilting category T"
section_number: 2.3
pages: 8-10
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.987
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-tiltmod}
\begin{defn}(\textbf{$\Delta$- and $\nabla$-filtration})\label{defn-filt}
We say that a $\Uq$-module $M$ has 
a $\Delta$\textit{-filtration} if there exists a descending sequence of 
$\Uq$-submodules
\[
M=F_{0}\supset F_1\supset\cdots\supset F_i\supset\dots,\quad\quad\bigcap_{i=0}^{\infty}F_i=0,
\]
such that for all $i=0,1\dots$ we have 
$F_{i}/F_{i+1}\cong \Vn{i^{\prime}}$ for 
some $i^{\prime}\in\bN$. A $\nabla$\textit{-filtration} is 
defined similarly, but using 
$\dVn{i^{\prime}}$ instead of 
$\Vn{i^{\prime}}$ and an ascending sequence of $\Uq$-submodules, that is
\[
0=F_{0}\subset F_1\subset\cdots\subset F_i\subset\dots,\quad\quad\bigcup_{i=0}^{\infty}F_i=M,
\]
such that for all $i=0,1\dots$ we 
have $F_{i+1}/F_{i}\cong \dVn{i^{\prime}}$ for some $i^{\prime}\in\bN$.
\end{defn}


One can prove, following similar arguments as in~\cite[Proposition~II.4.16]{jarag},
that such filtrations are unique up to reordering. It is clear that 
a finite-dimensional $\Uq$-module $M$ has a 
$\Delta$-filtration iff $M^*$ has a $\nabla$-filtration.



\begin{defn}(\textbf{Tilting modules})\label{defn-tilt}
We call a $\Uq$-module $M$ a $\Uq$-\textit{tilting module} 
if it has a $\Delta$- and a $\nabla$-filtration. 
We say for short that $M$ is \textit{tilting}.
\end{defn}




\begin{ex}\label{ex-tilt}
Recall that the category of finite-dimensional $\Uv$-modules is 
semisimple. It follows that all finite-dimensional 
$\Uv$-modules are tilting. Moreover, for $i<l$ or $i\equiv -1 \mod l$, 
by Proposition~\ref{prop-weyl} and 
Corollary~\ref{cor-weyl}, we see that $\Vn i\cong\Ln i\cong\dVn i$ is tilting.
\end{ex}



It is easy to see 
(in our $\mathfrak{sl}_2$ case - in general this 
is non-trivial, see e.g.~\cite[Theorem~3.3]{par}) 
that $\Vn i\otimes_{\bC}\Vn{i^{\prime}}$ has a $\Delta$-filtration with factors 
(likewise for $\dVn i\otimes_{\bC}\dVn{i^{\prime}}$)
\begin{equation}\label{eq-tiltfact}
\Vn{|i-i^{\prime}|},\,\Vn{|i-i^{\prime}|+2},\,\dots, \Vn{i+i^{\prime}-2},\,\Vn{i+i^{\prime}},\quad\quad i,i^{\prime}\geq 0.
\end{equation}



\begin{defn}(\textbf{Full tilting category})\label{defn-ftiltcat}
We denote by $\T^{\mathrm{all}}$ the full 
subcategory of all $\Uq$-modules that are tilting. 
We denote its class of objects by $\Ob(\T^{\mathrm{all}})$.
\end{defn}



\begin{prop}\label{prop-basicp}
The category $\T^{\mathrm{all}}$ has the following properties.
\begin{itemize}
\item[(a)] If $M,M^{\prime}\in\Ob(\T^{\mathrm{all}})$, then $M\oplus M^{\prime}\in\Ob(\T^{\mathrm{all}})$.
\item[(b)] If $M\oplus M^{\prime}\in\Ob(\T^{\mathrm{all}})$, then $M,M^{\prime}\in\Ob(\T^{\mathrm{all}})$.
\item[(c)] If $M,M^{\prime}\in\Ob(\T^{\mathrm{all}})$, then $M\otimes_{\bC} M^{\prime}\in\Ob(\T^{\mathrm{all}})$.\makeqed
\end{itemize}
\end{prop}



\begin{proof}
Part (a) is immediate. For part (b) one can, for 
example, argue as in~\cite[Proposition~3.7]{hum}, and the non-trivial 
part (c) can be deduced from~\eqref{eq-tiltfact} 
and the corresponding statement for the dual Weyl modules $\dVn i$.
\end{proof}


\begin{defn}(\textbf{The tilting category $\T$})\label{defn-tiltcat}
Let $\T$ be the full subcategory of $\T^{\mathrm{all}}$ consisting of:
\begin{itemize}
\item The objects $\Ob(\T)$ are all 
finite-dimensional $\Uq$-tilting modules $M\in\Ob(\T^{\mathrm{all}})$.
\item The morphisms $\Hom_{\T}(M,N)$ are all $\Uq$-intertwiners $f\in\Hom_{\Uq}(M,N)$. 
\end{itemize}
The objects of $\T$ have finite filtrations, 
i.e. $F_N=F_{N+i}$ for some $N\in\bN$ and all $i\in\bN$.
\end{defn}

Recall that an additive category is \textit{Krull-Schmidt}, 
if each object can be uniquely decomposed (up to permutation) 
into a finite direct sum of \textit{indecomposable objects}, i.e. objects 
$O$ such that $O\cong O^{\prime}\oplus O^{\prime\prime}$ implies that 
$O^{\prime}\cong 0$ or $O^{\prime\prime}\cong 0$.

\begin{lem}\label{lem-tiltcat}
We have the following.
\begin{itemize}
\item[(a)] The category $\T$ is additive (but not abelian), closed under 
finite direct sums, finite tensor products and under duals.
\item[(b)] $\T$ is a Krull-Schmidt category whose 
indecomposable objects are parametrized by $\bN$.
\item[(c)] $\Vn i$, $\dVn i$ and $\Ln i$ are in $\T$ 
iff $i<l$ or $i\equiv-1\mod l$.\makeqed
\end{itemize}
\end{lem}


\begin{proof}




\textbf{(a).} From Proposition~\ref{prop-basicp} and the fact that 
$\Hom_{\Uq}(\cdot,\bC)$ commutes with finite sums.

\textbf{(b).} 
The Krull-Schmidt property follows from finite-dimensionality and 
(b) of Proposition~\ref{prop-basicp}.
By Proposition~\ref{prop-tilt} below, all finite-dimensional 
indecomposable tiltings are of the form $\Tn i$.


\textbf{(c).} A direct consequence of Proposition~\ref{prop-weyl} and Corollary~\ref{cor-weyl}.
\end{proof}



\begin{rem}\label{rem-ribbon}
It follows from Lemma~\ref{lem-tiltcat} part (a) 
that $\T$ is a \textit{rigid category} 
(a monoidal category with duals and certain compatibility properties). 
Moreover, $\T$ is even a \textit{ribbon (tensor) category} and 
$\T$ gives rise to a \textit{modular category} 
(roughly: one mods out by tiltings whose quantum trace is zero) 
and thus, gives a $2+1$-dimensional TQFT and can 
be used to define the \textit{Witten-Reshetikhin-Turaev invariants} of $3$-manifolds. 
Good treatments of this are~\cite[Section~4]{an1} or~\cite[Section~7]{saw}.
\end{rem}



Define, using Propositions~\ref{prop-weyl} 
and~\ref{prop-basicp} and~\eqref{eq-tiltfact}, 
a family $(\Tn i)_{i\in\bN}$ of indecomposable tiltings as follows. 
We start by setting $\Tn 0=\Vn 0$ and $\Tn 1=\Vn 1$. 
Then we denote by $m_q\in\Tn 1$ any eigenvector for $K$ with eigenvalue $q$. 
For each $i>1$ we define $\Tn i$ to be the indecomposable 
summand of $(\Tn 1)^{\otimes i}$ which contains 
the vector $m_q\otimes\cdots\otimes m_q\in (\Tn 1)^{\otimes i}$.



Denote by $(T:\Vn{i})\in\bN$ the \textit{filtration multiplicity} for an $\Uq$-tilting module $T$. It is clear, by using~\eqref{eq-tiltfact}, that
\begin{equation}\label{eq-tiltfact2}
((\Tn 1)^{\otimes i}:\Vn i)=1,\quad\quad((\Tn 1)^{\otimes i}:\Vn{i^{\prime}})=0,\quad\quad\text{for } i^{\prime}>i.
\end{equation}
Hence, $\Tn i$ may also be described as 
the unique indecomposable summand of 
$(\Tn 1)^{\otimes i}$ that contains $\Vn i$. We note the following more precise statement.



\begin{prop}\label{prop-tilt}
\item[(a)] $\Vn i\cong\Ln i\cong\Tn i\cong\dVn i$ iff $i<l$ or $i\equiv -1\mod l$.
\item[(b)] Suppose $i=al+b$ for some $a,b\in\bN$ with 
$b\leq l-2$. Set $i^{\prime}=(a+2)l-b-2$. Then there exist short exact sequences
\[
0\longrightarrow \Vn{i^{\prime}}\hooklongrightarrow\Tn{i^{\prime}}\twoheadlongrightarrow \Vn{i}\longrightarrow 0,\quad\quad
0\longrightarrow \dVn{i}\hooklongrightarrow\Tn{i^{\prime}}\twoheadlongrightarrow \dVn{i^{\prime}}\longrightarrow 0.
\]
\item[(c)] We have $\Tn i\cong \Tn{i^{\prime}}$ 
iff $i=i^{\prime}$. Moreover, if $M\in\Ob(\T)$ 
is indecomposable, then there 
exists an $i\in\bN$ such that $M\cong \Tn i$.\makeqed
\end{prop}



\begin{proof}
\textbf{(a).} Clear by Proposition~\ref{prop-weyl} and Corollary~\ref{cor-weyl}.


\textbf{(b).} First let $T=\Vn{(a+1)l-1}\otimes \Vn 1$.  
Then $T=\Tn{(a+1)l-1}\otimes \Tn 1$ by (a), and, by~\eqref{eq-tiltfact}, 
we see that $T$ has a $\Delta_q$-filtration giving us the short exact sequence
\[
0\longrightarrow \Vn{(a+1)l}\hooklongrightarrow T\twoheadlongrightarrow \Vn{(a+1)l-2}\longrightarrow 0.
\] 
By duality, $T$ has an analogous $\nabla_q$-filtration, showing that $T$ is tilting. 
It is also indecomposable since otherwise the summand $\Tn{(a+1)l}$ 
of $T$ would be equal to $\Vn{(a+1)l}$, forcing it to be simple, which contradicts 
(b) of Proposition~\ref{prop-weyl}.
This proves the claim in case $b=l-2$.


Now, if $b<l-2$, then consider the diagram
\[
\xy
\xymatrix{
0\ar[r] & \Vn{i^{\prime}}\ar@{^{(}->}[r] & \Vn{i^{\prime}-1}\otimes \Vn 1\ar@{->>}[r]\ar@{^{(}->}[d] & \Vn{i^{\prime}-2}\ar[r] & 0\\
 &  & \Tn{i^{\prime}-1}\otimes \Tn 1\ar@{->>}[d] &  & \\
0\ar[r] & \dVn{i^{\prime}-2}\ar@{^{(}->}[r] & \dVn{i^{\prime}-1}\otimes \dVn 1\ar@{->>}[r] & \dVn{i^{\prime}}\ar[r] & 0.\\
}
\endxy
\]
Here the bottom and top sequences come from~\eqref{eq-tiltfact}. 
A computation shows that these split. This 
gives an inclusion $\Vn{i^{\prime}-2}\hookrightarrow\Tn{i^{\prime}-1}\otimes \Tn 1$ 
which extends to $\Tn{i^{\prime}-2}$, and a surjection 
$\Tn{i^{\prime}-1}\otimes \Tn 1\twoheadrightarrow\dVn{i^{\prime}-2}$ 
factoring through $\Tn{i^{\prime}-2}$. The resulting endomorphism of $\Tn{i^{\prime}-2}$
is non-zero on the 
$i^{\prime}-2$ weight space (the reader unfamiliar 
with this notion might consider Remark~\ref{rem-tria} 
where the notation is $M_i$ for the $i$-th weight space) 
and thus, an isomorphism. 
Hence, 
$\Tn{i^{\prime}-1}\otimes \Tn 1\cong\Tn{i^{\prime}-2}\oplus T$ 
for some $\Uq$-module $T$, which 
is tilting by (a) of Lemma~\ref{lem-tiltcat}. 
Using an inductive argument, we have that $T$ has two $\Delta_q$- 
and $\nabla_q$-factors as in the statement of (b). As above, we see that 
$T=\Tn{i^{\prime}}$, which proves the claim.

\textbf{(c).} To see the first statement note that it suffices to show 
that $\Tn i\not\cong \Tn{i^{\prime}}$ for $i\neq i^{\prime}$. To this end, assume without 
loss of generality that $i^{\prime}>i$. 
By~\eqref{eq-tiltfact2}, we see 
that $\Vn{i^{\prime}}$ appears with multiplicity 
$1$ in $\Tn{i^{\prime}}$, but not in $\Tn i$. Thus,  
$\Tn i\not\cong \Tn{i^{\prime}}$.
That every finite-dimensional 
indecomposable tilting is of this 
form needs a little bit more treatment. 
But it is a standard argument that appears 
in various contexts and can be 
adopted for example 
from~\cite[Section~11.2]{hum} or, alternatively, 
from~\cite[Chapter~II, Section~E.6]{jarag}.
\end{proof}


\begin{ex}\label{ex-tilt1}
Let $l=3$ again. The $\Uq$-tilting module $\Tn 2$ can be 
visualized as
\begin{equation*}
\begin{gathered}
\xymatrix{
 \otimes \ar@{.}[r]\ar@{.}[d]& m_1 \ar@<2pt>[r]^{1}\ar@(ul,ur)|{q^{-1}}  &  m_0  \ar@<2pt>[l]^1\ar@(ul,ur)|{q^{+1}}  \\
 m_1\ar@<2pt>[d]^{1}\ar@(ul,dl)|{q^{-1}} & m_{11} \ar@<2pt>[r]^{1}\ar@<2pt>[d]^{1}\ar@(ul,dl)|{q^{-2}}  &  m_{01}  \ar@<2pt>[l]^1\ar@<2pt>[d]^{1}\ar@{.}[dl]|{+}\ar@(ur,dr)|{q^{0}}  \\
 m_0\ar@<2pt>[u]^{1}\ar@(ul,dl)|{q^{+1}} & m_{10} \ar@<2pt>[r]^{1}\ar@<2pt>[u]^{1}\ar@(ul,dl)|{q^{0}}  &  m_{00}  \ar@<2pt>[l]^1\ar@<2pt>[u]^{1}\ar@(ur,dr)|{q^{+2}}  \\
}
\end{gathered},
\end{equation*}
where we use $m_{ij}=m_i\otimes m_j$. 
By construction, $\Tn 2$ contains $m_{00}$ and it therefore has to be the span of $\{m_{00},q^{-1}m_{10}+m_{01},m_{11}\}$ as indicated above (which is isomorphic to $\Ln 2$).
\end{ex}


\begin{rem}\label{rem-proj}
One can 
show that the category of all 
finite-dimensional projective $\Uq$-modules
is a full 
subcategory of $\T$. 
The same is true for finite-dimensional 
injective $\Uq$-modules: $\T$ has enough injectives and projectives. 
In fact, $\Tn{i}$ is injective and projective 
for all $i\geq l-1$. Hence, 
$\{\Tn{i}\mid i\geq l-1\}$ is a complete set of 
pairwise non-isomorphic, projective-injective
indecomposable, finite-dimensional $\Uq$-modules. 
See for example~\cite[Section~5]{an1}
\end{rem}
