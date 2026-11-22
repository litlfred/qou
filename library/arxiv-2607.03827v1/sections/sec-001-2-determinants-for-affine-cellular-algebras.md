---
doc_id: arxiv-2607.03827v1
doc_title: "Affine cellular algebras and asymptotic algebras"
section_id: sec-001-2-determinants-for-affine-cellular-algebras
section_title: "Determinants for affine Cellular Algebras"
section_number: 2
pages: 5-7
source_pdf: 2607.03827v1.pdf
source_sha256: 965d69603381942a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.961
doc_brief: "Affine cellular algebras and asymptotic algebras — The theory of affine cellular algebras A is extended to incorporate their asymptotic algebras ˆA, clarifying unexpected differences between"
---
Throughout this text let $k$ denote a commutative Noetherian domain. We recall
the definition of an affine cell ideal of a $k$-algebra, introduced in
\cite{KXaffine}, and then collect basic properties of determinants of
swich matrices. These determinants will play crucial roles in assumptions and
proofs of main results.
\begin{definition} Let $A$ be a unitary $k$-algebra with a $k$-involution $i$ on $A$. A two-sided ideal $J$ in $A$ is called an \emph{affine cell ideal} if and only if $i(J)=J$, such that 
\begin{enumerate}
\item there exist a free $k$-module $V$ of finite rank and an affine commutative $k$-algebra $B$ with identity and with a $k$-involution $\sigma$ such that $\Delta := V \otimes_k B$ is an $A-B$-bimodule, where the right $B$-module structure is induced by that of the right regular $B$-module $B_B$;
\item there is an $A-A$-bimodule isomorphism $\alpha: J \to \Delta \otimes_B \Delta'$, where $\Delta' = B \otimes_k V$ is a $B-A$-
bimodule with the left $B$-structure induced by $_BB$ and with the right $A$-structure via $i$, that is, $(b \otimes v) a := \tau (i(a)(v \otimes b))$ for $a\in A, b\in B$ and $v\in V$, such that 
$\alpha(i(\alpha^{-1}( u \otimes b \otimes v))) = v \otimes \sigma(b) \otimes u$, where one identifies $\Delta\otimes_B\otimes \Delta'$ and $V\otimes_k B \otimes_k V$ and where $\tau$ denotes the flip map.
\end{enumerate}
The module $\Delta$ is called a \emph{cell module} for the affine cell ideal $J$. (In \cite{KXaffine} the notion \emph{cell lattice} is used.) 

The algebra $A$ (with the involution $i$) is called \emph{affine cellular} if and only if there is a $k$-module decomposition 
$A = J'_1 \oplus J'_2 \oplus \cdots \oplus J'_n$ (for some $n$) with $i(J'_j) = J'_j$ for each $j$ and such that setting 
$J_j = \bigoplus_{i=1}^j J'_i$ gives a chain of two-sided ideals of $A$: $0 = J_0 \subset J_1 \subset J_2 \subset \cdots \subset J_n = A$  and for each $1\leq j\leq n$ the quotient $J_j/J_{j-1}$ is an affine cell ideal of $A/J_{j-1}$ (with respect to the involution induced by $i$ on the quotient). This chain is called a \emph{cell chain} for the affine cellular algebra $A$.
\end{definition}

A cellular $k$-algebra is an affine cellular $k$-algebra where all the occurring $k$-algebras $B$ are equal to the given commutative ground ring $k$.
\medskip

Given an affine cell ideal $J$ of $A$, we frequently identify $J$ with $\Delta \otimes_B \Delta'$ via $\alpha$ and the latter with $V\otimes_k B \otimes_k V$. From \cite[Proposition 2.2]{KXaffine} we know that if $J$ is an affine cell ideal of $A$ with involution $i$, then there is a $k$-linear map $\psi : V\otimes_k V \to B$, such that $\sigma (\psi(v, v')) = \psi(v', v)$, and
    \begin{equation}
\alpha\left( \alpha^{-1}(u \otimes b \otimes v) \alpha^{-1}(u' \otimes b' \otimes v') \right) = u \otimes b\psi(v,u') b' \otimes v'        
    \end{equation}
for all $u, u' , v, v' \in V$ and  $b, b' \in B$; and for any element $a\in A$ and $u\otimes b \otimes v \in V\otimes B \otimes V$ we have
\begin{equation}
    a(u \otimes b \otimes v) \in  V \otimes_k  Bb  \otimes_k v, \quad \mbox{ and } \quad (u \otimes b \otimes v)a \in u \otimes_k bB \otimes_k V.
\end{equation}

In particular, fixing a basis $v_1, \ldots, v_n$ for the free $k$-module $V$, we obtain the matrix $\psi = \left( \psi(v_i,v_j)\right)_{i,j} \in M_n(B)$, which is $\sigma$-symmetric in the sense that $\psi = \sigma(\psi)^T$, where $T$ denotes the transposition of matrices and $\sigma$ is extended from $B$ to $M_n(B)$. 
Moreover, $V\otimes_k B\otimes_k V$ gets identified with $M_n(B)$ by sending $v_i\otimes b \otimes v_j$ to $bE_{ij}$, with $E_{ij} \in M_n(B)$ being the elementary matrix with $1$ in the $(i,j)$th entry and $0$ elsewhere. Hence the multiplication of $J$ induces a multiplication on $M_n(B)$ via the $k$-linear isomorphism $\alpha:J\to \Delta\otimes_B \Delta' \cong V\otimes_k B\otimes_k V \cong M_n(B)$, which is given by the matrix $\psi$, namely by
$M\cdot M' = M\psi M'$, for $M,M' \in M_n(B)$. The resulting (not necessarily unital) $k$-algebra will be denoted by $\widetilde{M_n(B)} = (M_n(B),\psi)$ and is called the \emph{generalised matrix ring}. The matrix $\psi$ is also called a \emph{swich} (or \emph{sandwich}) matrix. Thus $\psi$ encodes the multiplication of $J$ (seen as a non-unital ring), but does not have information about the $A$-action on $J$. We will refer to the quintuple $(B,\sigma, \Delta, \psi,\alpha)$ as the \emph{cell datum} of $J$.  


Affine cell ideals were introduced to generalise cell ideals of cellular algebras and to provide a framework for studying affine versions of algebras like Hecke or Brauer algebras. A cell ideal of a $k$-algebra $A$ is an affine cell ideal $J$ with cell datum $(k,id, \Delta, \psi, \alpha)$, where $\Delta=V$ is a free $k$-module of rank $n$.  Following Graham and Lehrer \cite{GrahamLehrer}, see also Mathas \cite{Mathas}, a \emph{radical of $\Delta$} is defined as $\rad(\Delta)=\{ x\in \Delta \mid \psi(x,y)=0, \: \forall y\in \Delta\}$. (By definition, this is the
radical of the bilinear form associated with $\psi$. It is in general different
from the radical of the $A$-module ${}_A\Delta$.)

For an affine cell ideal let $\overline{\psi}:\Delta' \otimes_A \Delta \to B$
be given by 
\begin{equation}
    \overline{\psi}(b\otimes v, u\otimes b') := b\psi(v,u)b'
\end{equation}
for $b,b'\in B$ and $v,u\in V$. Then $\overline{\psi}$ is a $B$-bimodule homomorphism that satisfies 
\begin{equation}\label{eq:bilinear-psi}
    \overline{\psi}(y.a, x) = \overline{\psi}(y, a.x),
\end{equation}
for all $y\in \Delta'$, $x\in \Delta$ and $a\in A$.
We define the radical of $\Delta$ to be:
\begin{equation}\label{def:rad}
    \rad(\Delta)=\{ x\in \Delta \mid \overline{\psi}(y, x)=0, \: \forall y\in \Delta'\}.
\end{equation}
The subset $\rad(\Delta)$ is a left $A$-submodule of $\Delta$, since if $x\in \rad(\Delta)$ and $a\in A$, then by (\ref{eq:bilinear-psi}),  
$ \overline{\psi}(y, a.x)=\overline{\psi}(y.a, x)=0$, for any $y\in \Delta'$ and hence $a.x \in \rad(\Delta)$.

For a subset $J\subseteq A$ of a ring $A$ denote by $\ann_Y(J) = \{ y\in Y: Jy=0\}$ the annihilator of $J$ in a left $A$-module $Y$.

\begin{lemma}\label{lemma1}
    Let $\Delta$ be a cell module of an affine cell ideal $J$ with cell datum $(B,\sigma, \Delta, \alpha, \psi)$. Then the following statements are equivalent:
    \begin{enumerate}
        \item[(a)] $\rad(\Delta)=0$;
        \item[(b)] $\psi$ is not a zero-divisor in $M_n(B)$;
        \item[(c)] $\det(\psi)$ is not a zero-divisor in $B$;
        \item[(d)] $\ann_A(J) \cap J = 0$;
        \item[(e)] $\ann_{\Delta}(J)=0$;
        \item[(f)] the ring homomorphism $A\to A/J \times \End(J_A)$ with $a\mapsto (a+J, \lambda_a)$ is injective, where  $\lambda_a$ denotes the left $A$-action of $a$ on $J$.
    \end{enumerate}
\end{lemma}

\begin{proof}
Fix a basis $v_1, \ldots, v_n$ of $V$.

$(a) \Leftrightarrow (b)$: 
Let $x=\sum_{j=1}^n v_j \otimes b_j \in \Delta$. Then for any $1\leq i\leq n$: 
\begin{equation}\label{eq:radical}
 \overline{\psi}(v_i, x) =  \sum_{i=1}^n \psi(v_i, v_j)b_j = \sum_{j=1}^n \psi_{ij}b_j.
\end{equation} 
Hence, $\psi$ is a zero-divisor in $M_n(B)$ if and only if there exists a non-zero matrix $M = \sum_{r,s=1}^n b_{rs} E_{rs}$, such that 
\begin{equation}
\psi M     

= \sum_{i,j,s=1}^n \psi_{ij}b_{js} E_{is}
= \sum_{i,s=1}^n \overline{\psi}\left(v_i, \sum_{j=1}^n v_j\otimes b_{js} \right) E_{is}=0 
\end{equation}
if and only if $\sum_{j=1}^n v_j\otimes b_{js} \in \rad(\Delta)$, for all $1\leq s \leq n$ with at least one $b_{js}$ being non-zero.

$(b)\Leftrightarrow (c)$ follows from \cite[Theorem 9.1]{Brown}; $(c)\Leftrightarrow (d)$ follows from \cite[Lemma 3.2]{CKLS}; 
$(d)\Leftrightarrow (e)$ follows from the fact that $J\cong \Delta^d$, for some $d>0$;
$(d)\Leftrightarrow (f)$ follows from \cite[Proposition 3.14]{CKLS}.
\end{proof}

Let $A$ be an affine cellular $k$-algebra with cell chain
$0 = J_0 \subset J_1 \subset J_2 \subset \cdots \subset J_n = A$. 
Let $J_i/J_{i-1}\cong (M_{d_i}(B_i),\psi^{(i)})$. Recall that in the case of $A$ being a cellular algebra,  $B_i=k$, for all $i$. Denote by $\Delta_i$ the cell module associated to the cell ideal $J_i/J_{i-1}$. In the original definition of cellular algebras, Graham and Lehrer called a $k$-algebra cellular if there exists a \emph{cellular basis}, $\{ a_{st}^i : 1\leq i\leq n, \: 1\leq s,t\leq d_i\}$ satisfying certain axioms (see \cite{GrahamLehrer}). In particular,  $A=\bigoplus_{i=1}^n J'_i$, with $J'_i$ being the free $k$-module with basis $\{a_{st}^i : 1\leq s,t \leq d_i\}$. Moreover, $\Delta_i=V_i$ is the free $k$-module generated by $\{ a_{s1}^i : 1\leq s \leq d_i\}$, which is a left $A$-submodule of $J_i/J_{i-1}$. The bilinear form $\psi^{(i)}:\Delta_i \times \Delta_i \to k$ is determined by the matrix $\left( \psi^{(i)}(a_{s1}^i, a_{t1}^i) \right)_{1\leq s,t\leq d_i}$. Its determinant is called the \emph{Gram determinant} of $\psi^{(i)}$ and denoted by $G(i) = \det\left( \psi^{(i)}(a_{s1}^i, a_{t1}^i) \right)_{1\leq s,t\leq d_i}$. By construction, the Gram determinant coincides with the determinant
of the swich matrix.
