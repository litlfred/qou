---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-016-51-joint-cumulants-of-the-spins
section_title: "Joint cumulants of the spins"
section_number: 5.1
pages: 32-41
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.977
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
When $\alpha=0$, one can realize the Ising model by choosing $\sigma(1)$ according to a Bernoulli random variable of parameter $\frac{1}{2}$, and then each sign $X_i=\sigma(i)\sigma(i+1)$ according to independent Bernoulli random variables with $$\proba[X_i=1]=1-\proba[X_i=-1]=\frac{\E^{\beta}}{2\cosh \beta}.$$ 
In particular, one recovers immediately the value of the partition function $Z_n(\IS,0,\beta)=2^n(\cosh \beta)^{n-1}$. We then want to compute the joint cumulants of the magnetization $M_n$; by parity, the odd cumulants and moments vanish. By multilinearity, one can expand
$$\kappa^{(2r)}(M_n)=\sum_{i_1,\ldots,i_{2r}=1}^n\kappa(\sigma(i_1),\ldots,\sigma(i_{2r})),$$
so the problem reduces to the computation of the joint cumulants of the individual spins, and to the gathering of these quantities. Notice that the joint moments of the spins can be computed easily. Indeed, fix $i_1\leq i_2 \leq \cdots \leq i_{2r}$, and let us calculate $\esper[\sigma(i_1)\cdots\sigma(i_{2r})]$. If $i_{2r-1}=i_{2r}$, then the two last terms cancel and one is reduced to the computation of a joint moment of smaller order. Otherwise, notice that
\begin{align*}\esper[\sigma(i_1)\cdots\sigma(i_{2r-2})\sigma(i_{2r-1})\sigma(i_{2r})]&=\esper[\sigma(i_1)\cdots\sigma(i_{2r-2})X_{i_{2r-1}}X_{i_{2r-1}+1}\cdots X_{i_{2r}-1}]\\
&=\esper[\sigma(i_1)\cdots\sigma(i_{2r-2})]\,x^{i_{2r}-i_{2r-1}} \quad\text{where }x=\tanh \beta.
\end{align*}
By induction, we thus get
$$\esper[\sigma(i_1)\cdots\sigma(i_{2r})]=x^{(i_2-i_1)+(i_4-i_3)+\cdots+(i_{2r}-i_{2r-1})}.$$\bigskip

Let us then go to the joint cumulants. We fix $i_1 \leq i_2 \leq \cdots \leq i_{2r}$, and to simplify a bit the notations, we denote $i_1=\mathbf{1}$, $i_2=\mathbf{2}$, \emph{etc}. We recall that the joint cumulants write as
$$\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r}))=\sum_{\Pi \in \qym_{2r}}\mu(\Pi)\,\prod_{A \in \Pi}\,\esper\!\left[\prod_{a \in A} \sigma(\mathbf{a})\right],$$
where the sum runs over set partitions of $\lle 1,2r\rre$. By parity, the set partitions with odd parts do not contribute to the sum, so one can restrict oneself to the set $\qym_{2r,\text{even}}$ of even set partitions. If $A=\{a_1<\cdots<a_{2s}\}$ is an even part of $\lle 1,2r\rre$, we write $x^{p(A)}=x^{(\mathbf{a}_{2}-\mathbf{a}_{1})+\cdots+(\mathbf{a}_{2s}-\mathbf{a}_{2s-1})}$. Thus,
$$\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r}))=\sum_{\Pi \in \qym_{2r,\text{even}}}\mu(\Pi)\prod_{A \in \Pi} x^{p(A)}.$$
In this polynomial in $x$, several set partitions give the same power of $x$; for instance, with $2r=4$, the set partitions $\{1,2,3,4\}$ and $\{1,2\} \sqcup \{3,4\}$ both give $x^{(\mathbf{2}-\mathbf{1})+(\mathbf{3}+\mathbf{4})}$. Denote $\pym_{2r}$ the set of set partitions of $\lle 1,2r\rre$ whose parts are all of cardinality $2$ (pair set partitions, or pairings). To every even set partition $\Pi$, one can associate a pairing $p(\Pi)$ by cutting all the even parts $\{a_1<a_2<\cdots<a_{2s-1}<a_{2s}\}$ into the pairs $\{a_1<a_2\},\ldots,\{a_{2s-1}<a_{2s}\}$. For instance, the even set partition $\Pi=\{1,3,4,5\}\sqcup\{2,6\}$ gives the pairing $(1,3)(4,5)(2,6)$. Then, with obvious notations,
\begin{equation}\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r}))=\sum_{\Pi \in \qym_{2r,\text{even}}}\mu(\Pi)\, x^{p(\Pi)}.
\label{eq:jointcumulant1}
\end{equation}
In Equation \eqref{eq:jointcumulant1}, two important simplifications can be made:\vspace{2mm}
\begin{enumerate}
\item One can gather the even set partitions $\Pi$ according to the pairing $\rho=p(\Pi) \in \pym_{2r}$ that they produce. It turns out that the corresponding sum of M\"obius functions $F(\rho)$ has a simple expression in terms of the pairing, see \S\ref{subsec:functionalF}.  \vspace{1mm}
\item Some pairings $\rho$ yield the same monomial $x^{\rho}$ and the same functional $F(\rho)$. By gathering these contributions, one can reduce further the complexity of the sum, see \S\ref{subsec:functionalN}.\vspace{1mm}
\end{enumerate}
In the end, we shall obtain an exact formula for $\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r}))$ that writes as a sum over Dyck paths of length $2r-2$, with simple coefficients; see Theorem \ref{thm:jointcumulant}.




\subsubsection{Pairings, labelled Dyck paths and labelled planar trees}\label{subsec:combinatorics}
Before we start the reduction of Formula \eqref{eq:jointcumulant1}, it is convenient to recall some facts about the combinatorial class of pairings. We have defined a pairing $\rho$ of size $2r$ to be a set partition of $\lle 1,2r\rre $ in $r$ pairs $(a_1,b_1),\ldots,(a_r,b_r)$. There are 
$$\card\, \pym_{2r}=(2r-1)!!=(2r-1)(2r-3)\cdots 3\,1$$ pairings of size $2r$, and it is convenient to represent them by diagrams:
\figcap{pairing.pdf}{The diagram of a pairing of size $2r=10$.\label{fig:pairing}}\vspace{-5mm}
\figcap{labelledpath.pdf}{The labelled Dyck path corresponding to the pairing of Figure \ref{fig:pairing}.\label{fig:dyckpath}}
On the other hand, a labelled Dyck path of size $2r$ is a path $\delta : \lle 0,2r\rre \to \N$ with $2r$ steps either ascending or descending, such that:\vspace{2mm}
\begin{itemize}
\item the path $\delta$ starts from $0$, ends at $0$ and stays non-negative; \vspace{1mm}
\item each descending step $\delta(k)>\delta(k+1)$ is labelled by an integer $i \in \lle 1,\delta(k)\rre$.\vspace{1mm}
\end{itemize}
From a labelled Dyck path of size $2r$, one constructs a pairing on $2r$ points as follows: one reads the diagram from left to right, opening a bond when the path is ascending, and closing the $i$-th opened bond available from right to left when the path is descending with label $i$. For instance, if one starts from the Dyck path of Figure \ref{fig:dyckpath}, one obtains the pairing of Figure \ref{fig:pairing}. This provides a first bijection between pairings $\rho$ and labelled Dyck paths $\delta$. \bigskip

By considering a Dyck path as the code of the depth-first traversal of a rooted tree, one obtains a second bijection betwen pairings of size $2r$ and labelled planar rooted trees with $r$ edges. Here, by labelled planar rooted tree, we mean a planar rooted tree with a label $i$ on each edge $e$ that is between $1$ and the height $h(e)$ of the edge (with respect to the root). For instance, the following labelled tree $T$ corresponds to the Dyck path of Figure \ref{fig:dyckpath} and to the pairing of Figure \ref{fig:pairing}:

\figcap{labelledtree.pdf}{The labelled planar rooted tree corresponding to the pairing of Figure \ref{fig:pairing}.}

We shall denote $\tym_r$ the set of planar rooted trees with $r$ edges (without label), and $\dym_{2r}$ the corresponding set of Dyck paths (again without label); they have cardinality
$$\card \,\tym_r = \card \,\dym_{2r}= C_r = \frac{1}{r+1}\binom{2r}{r}.$$
They correspond to the subset $\nym_{2r}$ of $\pym_{2r}$ that consists in non-crossing pair partitions of $\lle 1,2r\rre$; a bijection is obtained by labelling each edge or descending step by $1$, and by using the previous constructions. For instance, the non-crossing pairing, the Dyck path and the planar rooted tree of Figure \ref{fig:restriction} do correspond. 
\figcap{restriction.pdf}{Bijection between non-crossing pairings, Dyck paths and planar rooted trees.\label{fig:restriction}}
\bigskip

In what follows, we shall always use the letters $\nu$, $\delta$ and $T$ respectively for non-crossing pairings, for Dyck paths and for planar rooted trees. We shall then use constantly the bijections described above, and denote for instance $\nu(T)$ for the non-cros\-sing pairing associated to a tree $T$, or $\delta(\nu)$ for the Dyck path associated to a non-cros\-sing pairing $\nu$. We shall also use the exponent $+$ to indicate the following operations on these combinatorial objects:\vspace{1mm}
\begin{itemize}
\item transforming a non-crossing pairing $\nu$ of size $2r-2$ in a non-crossing pairing $\nu^+$ of size $2r$ by adding the bond $\{1,2r\}$ "over" the bonds of $\nu$.\vspace{1mm}
\item transforming a Dyck path $\delta$ of length $2r-2$ in a Dyck path $\delta^+$ of length $2r$ by adding an ascending step before $\delta$ and a descending step after $\delta$.\vspace{1mm}
\item transforming a rooted tree $T$ with $r-1$ edges in a rooted tree $T^+$ with $r$ edges by adding an edge "below" the root.\vspace{1mm}
\end{itemize}
All these operations are compatible with the aforementioned bijections, so for instance $\nu(T^+)=(\nu(T))^+$ and $\delta(\nu^+)=(\delta(\nu))^+$.




\subsubsection{Uncrossing pairings and the associated poset}\label{subsec:functionalN}
 Let us now see how the combinatorics of pairings, Dyck paths and planar rooted trees intervene in Formula \eqref{eq:jointcumulant1}. We start by gathering the set partitions $\Pi$ with the same associated pairing $\rho=p(\Pi)$. Thus, let us write
$$\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r}))=\sum_{\rho \in \pym_{2r}} x^{\rho}\,\left(\sum_{\substack{\Pi \in \qym_{2r,\text{even}}\\ p(\Pi)=\rho}} \mu(\Pi) \right)=\sum_{\rho \in \pym_{2r}} x^\rho\,F(\rho),$$
where $F(\rho)$ stands for the sum in parentheses. Notice that $x^\rho$ is invariant if one replaces in a pairing two crossing pairs $\{a_1,a_3\},\{a_2,a_4\}$ with $a_1<a_2<a_3<a_4$ by two nested pairs (but non-crossing) $\{a_1,a_4\},\{a_2,a_3\}$; indeed,
$$(a_3-a_1)+(a_4-a_2)=(a_4-a_1)+(a_3-a_1).$$
We call uncrossing the operation on pairings which consists in replacing two crossing pairs by two nested pairs as described above, and we denote $\rho_1 \succeq \rho_2$ if there is a sequence of uncrossings from the pairing $\rho_1$ to the pairing $\rho_2$; this is a partial order on the set $\pym_{2r}$.
\figcap{uncrossing.pdf}{The operation of uncrossing on a pairing.}

\begin{proposition}
The poset $(\pym_{2r},\preceq)$ is a disjoint union of lattices, and each lattice contains a unique non-crossing set partition $\nu$, which is the minimum of this connected component of the Hasse diagram of $(\pym_{2r},\preceq)$. Moreover:\vspace{2mm}
\begin{enumerate}[1.]
\item On the lattice $L(\nu)$ associated to $\nu \in \nym_{2r}$, the monomial $x^{\rho}$ and the functional $F(\rho)$ are constant (equal to $x^{\nu}$ and $F(\nu)$). \vspace{1mm}
\item The cardinality $\card\, L(\nu)=N(\nu)$ is given by:
$$N(\nu)=\prod_{e \in E(T(\nu))} h(e,T(\nu)),$$
where $h(e,T)$ is the height of the edge $e$ in the (planar) rooted tree $T$, and $E(T)$ is the set of edges of a tree $T$.
\end{enumerate}
\end{proposition}

\begin{proof}
First, notice that if $\rho_1 \preceq \rho_2$ in $\pym_{2r}$, then there is a sequence of pairings going from $\rho_1$ to $\rho_2$ such that every two consecutive terms $\mu$ and $\rho$ of the sequence differ only by the replacement of a simple nesting by a simple crossing. By that we mean that we do not need to do replacements such as the one on Figure \ref{fig:complexnesting}, which creates $3$ crossings at once.
\figcap{complexnesting.pdf}{The crossing of a nesting that is not simple.\label{fig:complexnesting}}
 Indeed, denoting $(i,j)$ the crossing of the $i$-th bond with the $j$-th bond, bonds being numeroted from their starting point, one has $(1,3)=(1,2)\circ (2,3)\circ(1,2)$, which is a composition of simple operations of crossing; and the same idea works for nestings of higher depth. Thus, the Hasse diagram of the poset $(\pym_{2r},\preceq)$ has edges that consist in replacements of simple nestings by simple crossings.\bigskip

This being clarified, it suffices now to notice that \emph{via} the bijection between pairings and labelled Dyck paths explained in \S\ref{subsec:combinatorics}, the replacing a simple nesting by a simple crossing corresponds to the raising of a label by $1$:
\figcap{uncrossing2.pdf}{The operation of uncrossing is a change of labels on Dyck paths.}
In particular, if $\rho_1$ and $\rho_2$ are two comparable pairings in $(\pym_{2r},\preceq)$, then the corresponding labelled Dyck paths have the same shape; and for a given shape $\delta \in \dym_{2r}$, there is exactly one corresponding non-crossing pair partition $\nu=\nu(\delta)$, which is minimal in its connected component in the Hasse diagram of $(\pym_{2r},\preceq)$. Endowed with $\preceq$, this connected component $L(\nu)$ is isomorphic as a poset to the product of intervals
$$\prod_{e \in T(\nu)} \lle 1,h(e,T(\nu))\rre.$$
Indeed, the order on the set of labelled trees of shape $T(\nu)$ induced by $(L(\nu),\preceq)$ and by the bijection between pairings and labelled trees is simply the product of the orders of the intervals of labels. This proves all of the Proposition but the invariance of $F(\cdot)$ on $L(\nu)$ (the invariance of $x^{(\cdot)}$ was shown at the beginning of this paragraph); we devote \S\ref{subsec:functionalF} to this last point and to the actual computation of the functional $F(\cdot)$.
\end{proof}
\bigskip

Assuming the invariance of $F(\cdot)$ on each lattice $L(\nu)$, we thus get:
\begin{equation}\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r}))=\sum_{\rho \in \pym_{2r}} x^{\rho}\,F(\rho) = \sum_{\nu \in \nym_{2r}} x^{\nu}\,N(\nu)\,F(\nu) \label{eq:jointcumulant2},
\end{equation}
where $N(\nu)$ is explicit. Hence, it remains to compute the functional $F(\rho)$.



\subsubsection{Computation of the functional $F$}\label{subsec:functionalF}
The main result of this paragraph is:
\begin{proposition}\label{prop:functionalF}
The functional $F(\cdot)$ is constant on $L(\nu)$, and if $\nu$ is a non-crossing pairing, then
$$F(\nu)=(-1)^{r-1}\,\prod_{\substack{e \in T(\nu)\\h(e,T(\nu))\neq 1}} (h(e,T(\nu))-1)$$
if $T(\nu)$ has a single edge of height $1$, and $0$ otherwise.
\end{proposition}

\begin{lemma}
The functional $F$ vanishes on pairings associated to labelled rooted trees with more than one edge of height $1$.    
\end{lemma}

\begin{proof}
Suppose that $\Pi$ is an even set partition with $p(\Pi)=\rho$; $\rho$ being a pairing of size $2r$ associated to a labelled Dyck path that reaches $0$ after $2a$ steps, with $2r=2a+2b$, $a>0$ and $b>0$ (this is equivalent to the statement "having more than one edge of height $1$"). We denote $\rho_1$ and $\rho_2$ the pairings associated to the two parts of the Dyck path. There are several possibilities:\vspace{1mm}
\begin{itemize}
\item either $\Pi$ can be split as two even set partitions $\Pi_1$ of $\lle 1,2a\rre$ and $\Pi_2$ of $\lle 2a+1,2r\rre$, with respectively $k$ and $l$ parts, and with $p(\Pi_1)=\rho_1$ and $p(\Pi_2)=\rho_2$;\vspace{1mm}
\item or, $\Pi$ is one of the $k\times l$ possible ways to unite two such even set partitions $\Pi_1$ and $\Pi_2$ by joining one part of $\Pi_1$ with one part of $\Pi_2$;\vspace{1mm}
\item or, $\Pi$ is one of the $\binom{k}{2}\times \binom{l}{2} \times 2!$ possible ways to unite two such even set partitions $\Pi_1$ and $\Pi_2$ by joining two parts of $\Pi_1$ with two parts of $\Pi_2$;\vspace{1mm}
\item or, $\Pi$ is one of the $\binom{k}{3}\times \binom{l}{3} \times 3!$ possible ways to unite two such even set partitions $\Pi_1$ and $\Pi_2$ by joining three parts of $\Pi_1$ with three parts of $\Pi_2$;\vspace{1mm}
\item \emph{etc.}\vspace{1mm}
\end{itemize}
So, $F(\rho)$ can be rewritten as
$$\sum_{\substack{p(\Pi_1)=\rho_1 \\ p(\Pi_2)=\rho_2} }\!\!(-1)^{t-1} \,\left((t-1)! -kl\,(t-2)!+\binom{k}{2}\binom{l}{2}\,2!\,(t-3)!-\binom{k}{3}\binom{l}{3}\,3!\,(t-4)!+\cdots\right),$$
where $t=k+l$. However, for every possible value of $k \geq 1$ and $l \geq 1$, the term in parentheses vanishes. Indeed, assuming for instance $k \leq l$, we look at
\begin{align*}
&(k+l-1)!\,\sum_{x=0}^{k} (-1)^x \, \binom{k}{x}\,\binom{l}{x} \,\binom{k+l-1}{x}^{\!\!-1}\\
 &=k!\,(l-1)!\,\sum_{x=0}^{k} (-1)^x \,\binom{l}{x} \,\binom{k+l-1-x}{k-x}\\
&=k!\,(l-1)!\,\binom{k-1}{k}=0
\end{align*}
by using Riordan's array rule for the second identity.  
\end{proof}\bigskip

Thus, $F$ vanishes on pairings $\rho$ associated to labelled trees with more than one edge of height $1$. In other words, if $F(\rho)\neq 0$, then $\{1,2r\}$ is a pair in $\rho$, and we can look at the restricted pairing $\tilde\rho=\rho_{|\lle 2,2r-1\rre}$, which is of size $2r-2$; and we can consider $F$ as a functional on $\pym_{2r-2}$. 
To avoid any ambiguity, we denote this new functional
$$G(\rho \in \pym_{2r})=\sum_{p(\Pi)=\rho}(-1)^{\ell(\Pi)}\, (\ell(\Pi))!$$
We then expect the formula $G(\rho)=(-1)^{r}\,\prod_{e \in E(T(\rho))} h(e)$. We proceed by induction on labelled rooted planar trees, and we look at the action of adding a leave of label $1$ to the tree, and of increasing a label of an edge by $1$. To fix the ideas, it is convenient to consider the following example of pairing $\rho$, and the associated set of set partitions $\Pi$ with $p(\Pi)=\rho$. The pairing $\rho$ of Figure \ref{fig:setpartition} is associated to the labelled planar rooted tree on Figure \ref{fig:labelledtree}, and it has functional $G(\rho)=(-1)^3\,3! + 2\times (-1)^2\,2!=-2$. We denote $N(l,\rho)$ the number of set partitions such that $p(\Pi)=\rho$ and $\ell(\Pi)=l$. Hence, $$G(\rho)=\sum_{l=1}^{r}N(l,\rho)\,(-1)^l\,l!$$
\clearpage

\figcap{setpartition.pdf}{A pairing  of size $2r=6$ (the upper diagram) and the associated set of set partitions, which contains 3 elements.\label{fig:setpartition}}\vspace{-10mm}
\figcap{labelledtree2.pdf}{The labelled planar rooted tree associated to the pairing of Figure \ref{fig:setpartition}.\label{fig:labelledtree}}

\begin{enumerate}
 \item \emph{Adding an edge}. Suppose that one adds an edge with label $1$, to obtain for instance: 
\figcap{induction1.pdf}{Addition of an new edge of label 1 to the planar rooted tree.}
Set $\rho'$ for the new pairing; notice that it is obtained from $\rho$ by inserting a simple bond \includegraphics{bond.pdf}. The set partitions $\Pi'$ with $p(\Pi')=\rho'$ are of two kinds:\vspace{1mm}
\begin{enumerate}
\item those where the new bond is left alone. They all come from a set partition $\Pi$ with $p(\Pi)=\rho$ by simply inserting the new bond:
\end{enumerate}
\end{enumerate}
\figcap{induction2.pdf}{Set partitions where the new bond is left alone.}
\begin{enumerate}
\item[]
\begin{enumerate}
\item[] These terms give the following contribution to $G(\rho')$:
$$G_{(\textrm{a})}(\rho')=-\sum_{l=1}^{r}N(l,\rho)\,(-1)^{l}\,(l+1)!.$$
\vspace{1mm}
\setcounter{enumii}{1}
\item those where the new bond is linked to another part of a set partition $\Pi$ with $p(\Pi)=\rho$. Starting from a set partition $\Pi$ with $p(\Pi)=\rho$, the number of parts of $\Pi$ that can actually receive the new bond is $\ell(\Pi)-(h(e)-1)$, because the new bond cannot be linked to the $h(e)-1$ parts that go above him. In our example:
\vspace{1mm}
\end{enumerate}
\end{enumerate}
\figcap{induction3.pdf}{Set partitions where the new bound is integrated in another part.}

\begin{enumerate}
\item[]~ \setcounter{enumi}{1}
\begin{enumerate}
\item[] These other terms give the following contribution to $G(\rho')$:
$$G_{(\textrm{b})}(\rho')=\sum_{l=1}^{r}N(l,\rho)\,(-1)^{l}\,l!\,(l+1-h(e)).$$
\vspace{1mm}
\end{enumerate}
We conclude that $G(\rho')=G_{(\textrm{a})}(\rho')+G_{(\textrm{b})}(\rho')=-h(e)\,G(\rho)$, so the formula for $G$ stays true when one adds an edge of label $1$.
\vspace{3mm}

\item \emph{Raising a label}. As explained before, raising a label corresponds to adding a simple crossing to the pairing $\rho$, which is done by exchanging two ends $b$ and $d$ of two simply nested pairs $\{a<b\}$ and $\{c<d\}$ of $\rho$. This does not change the structure of the set of even set partitions $\Pi$ with $p(\Pi)=\rho$; that is, $N(l,\rho)=N(l,\rho')$ for every $l$. So, the formula for $G$ also stays true when one raises a label.
 \vspace{3mm}
 \end{enumerate}
Since every labelled rooted tree is obtained inductively from the empty tree by adding edges and raising labels, the proof of Proposition \ref{prop:functionalF} is done.




\subsubsection{Expansion of the joint cumulants as sums over Dyck paths}
Recall that $x^{\nu}$ stands for $x^{(\mathbf{a}_2-\mathbf{a}_1)+\cdots+(\mathbf{a}_{2r}-\mathbf{a}_{2r-1})}$ if $\nu$ is the pairing $\{a_1<a_2\},\ldots,\{a_{2r-1}<a_{2r}\}$. We adopt the same notations with Dyck paths and planar rooted trees, so $x^\delta$ or $x^T$ stands for $x^\nu$ if $\delta=\delta(\nu)$ or if $T=T(\nu)$. We also denote $\dym_{2r}^*$ the image of $\dym_{2r-2}$ in $\dym_{2r}$ by the operation $\delta \mapsto \delta^+$. Notice that if $\Delta=(\delta(T))^+$ with $T$ tree with $r-1$ edges, then
$$\prod_{e \in E(T)} h(e)\,(h(e)+1)= \prod_{i=1}^{2r-1} \Delta_i,$$
$\Delta_i$ denoting the value of the Dyck path $\Delta$ after $i$ steps. Starting from Equation \eqref{eq:jointcumulant2} and using the explicit formulas that we have obtained for $N(\nu)$ and $F(\nu)$, we therefore get:

\begin{theorem}
\label{thm:jointcumulant}
For every indices $\mathbf{1}\leq\cdots\leq\mathbf{2r}$, 
$$\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r}))=(-1)^{r-1}\,\sum_{\delta \in \dym_{2r}^*} \left(\prod_{i=1}^{2r-1}\delta_i\right)\, x^{\delta}.$$    
\end{theorem}

\begin{example}
The two non-crossing pairings of size $4$ are \includegraphics{3example1.pdf} and \includegraphics{3example2.pdf}, the associated powers of $x$ are 
$$x^{(\mathbf{6}-\mathbf{1})+(\mathbf{5}-\mathbf{4})+(\mathbf{3}-\mathbf{2})} \quad\text{and}\quad x^{(\mathbf{6}-\mathbf{1})+(\mathbf{5}-\mathbf{2})+(\mathbf{4}-\mathbf{3})},$$
and the associated quantities $G(\nu)$ are $4$ and $12$, so, with $r=3$,
$$\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{6}))=4\,x^{\mathbf{6}+\mathbf{5}+\mathbf{3}-\mathbf{4}-\mathbf{2}-\mathbf{1}} + 12\, x^{\mathbf{6}+\mathbf{5}+\mathbf{4}-\mathbf{3}-\mathbf{2}-\mathbf{1}}.$$    
\end{example}
\bigskip

Theorem \ref{thm:jointcumulant} has several easy corollaries. First of all, we see immediately from it that the sign of a joint cumulant of spins is prescribed, which was \emph{a priori} non-obvious. On the other hand, applying Theorem \ref{thm:jointcumulant} to the case $r=1$ yields $$\kappa(\sigma(i),\sigma(j))=x^{|j-i|},$$ that is, the correlation between two spins decreases exponentially with the distance between the spins. More generally, one can use Theorem \ref{thm:jointcumulant} to get a useful bound on cumulants. Notice that the minimal exponent of $x$ that appears in the right-hand side of the formula is $$x^{\mathbf{(2r)}+(\mathbf{(2r-1)}-\mathbf{(2r-2)})+(\mathbf{(2r-3)}-\mathbf{(2r-4)})+\cdots+(\mathbf{3}-\mathbf{2})-\mathbf{1}}.$$
Indeed, it is easily seen that the exponent of $x$ in $x^T$ increases when one makes a rotation of a leaf of $T$ in the sense of Tamari (\emph{cf.} \cite{Tam62}). Since all trees are generated by leaf rotations from the tree with all edges of height $1$ (\emph{cf.} \cite{Knu04}), the previous claim is shown. It follows that 
$$\left|\kappa(\sigma(\mathbf{1}),\ldots,\sigma(\mathbf{2r})) \right|\leq \left(\sum_{\delta \in \dym_{2r}^*} \prod_{i=1}^{2r-1} \delta_i \right) x^{\mathbf{(2r)}+(\mathbf{(2r-1)}-\mathbf{(2r-2)})+\cdots+(\mathbf{3}-\mathbf{2})-\mathbf{1}}.$$
The quantity $$Q(r)=\sum_{\delta \in \dym_{2r}^*} \left(\prod_{i=1}^{2r-1} \delta_i\right) = \sum_{T \in \tym_{r-1}} \left(\prod_{e \in E(T)} h(e)\,(h(e)+1)\right)$$ has for first values $1,2,16,272,7936,\ldots,$ and a simple bound on $Q(r)$ is $(2r-2)!$, see Proposition \ref{prop:polynomial} hereafter. Hence, a generalization of the exponential decay of covariances is given by:

\begin{proposition}
For any positions of spins $i_1\leq i_2 \leq \cdots \leq i_{2r}$, 
$$\left|\kappa(\sigma(i_1),\ldots,\sigma(i_{2r})) \right|\leq (2r-2)!\,\, x^{i_{2r}+(i_{2r-1}-i_{2r-2})+\cdots+(i_{3}-i_{2})-i_{1}}.$$
\end{proposition}
\medskip
