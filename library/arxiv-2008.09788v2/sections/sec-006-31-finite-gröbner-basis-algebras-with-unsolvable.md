---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY"
section_id: sec-006-31-finite-gröbner-basis-algebras-with-unsolvable
section_title: "Finite Gröbner basis algebras with unsolvable nilpotency problem and zero divisors problem"
section_number: 3.1
pages: 23-25
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.767
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
\label{sec31}

\subsubsection{\bf The sketch of construction}\label{sk}

Let $A$ be an algebra over a field $K$.

The set of all words in the alphabet $\{a_1,\dots , a_N\}$ is a semigroup. The main idea of the construction is a
realization of a universal Turing machine in this semigroup. We use the universal Turing
machine constructed by Marvin Minsky in \cite{Minsky}. This machine has $7$ states and $4$-color
tape. The machine can be completely defined by $28$ instructions.


Note that $27$ of them have a form
$$(i,j) \rightarrow (L,q(i,j),p(i,j)) \text{ or } (i,j) \rightarrow (R,q(i,j),p(i,j)),$$
where $0\leq i \leq 6$ is the current machine state, $0\leq j\leq 3$ is the current cell color,
$L$ or $R$ (left or right) is the direction of a head moving after execution of the current
instruction, $q(i,j)$ is the state after current instruction, $p(i,j)$ is the new color of
the current cell.

Thus, the instruction $(2,3) \rightarrow (L,3,1)$ means the following: ``If the color of the
current cell is $3$ and the state is $2$, then the cell changes the color to $1$, the head moves
one cell to the left, the machine changes the state to $3$.

The last instruction is $(4,3) \rightarrow\ $STOP. Hence, if the machine is in state $4$ and
the current cell has color $3$, then the machine halts.

\medskip


\subsubsection{\bf Letters.}\label{let}



By $Q_i$, $0\leq i\leq 6$ denote the current state of the machine. By $P_j$, $0\leq j\leq 3$
denote the color of the current cell.

The action of the machine depends on the current state $Q_i$ and current cell color $P_j$.
Thus every pair $Q_i$ and $P_j$ corresponds to one instruction of the machine.

The instructions moving the head to the left (right) are called {\it left} ({\it right}) ones.
Therefore there are {\it left pairs} $(i,j)$ for the left instructions, {\it right pairs} for
the right ones and instruction STOP for the pair $(4,3)$.




All cells with nonzero color are said to be {\it non-empty cells}.
We shall use letters $a_1$, $a_2$, $a_3$ for nonzero colors and letter $a_0$ for color zero.
Also, we use $R$ for edges of colored area.
Hence, the word $Ra_{u_1}a_{u_2}\dots a_{u_k}Q_iP_j a_{v_1}a_{v_2}\dots a_{v_l}R$ presents a full state of Turing machine.

We model head moving and cell painting using computations with powers of $a_i$ (cells) and $P_i$ and $Q_i$
(current cell and state of the machine's head).


\medskip








We use the universal Turing machine constructed by Minsky. This machine is defined by the following instructions:

\medskip

$(0,0)\rightarrow (L,4,1) \ (0,1)\rightarrow (L,1,3) \ (0,2)\rightarrow (R,0,0) \ (0,3)\rightarrow (R,0,1)$

$(1,0)\rightarrow (L,1,2) \ (1,1)\rightarrow (L,1,3) \ (1,2)\rightarrow (R,0,0) \ (1,3)\rightarrow (L,1,3)$

$(2,0)\rightarrow (R,2,2) \ (2,1)\rightarrow (R,2,1) \ (2,2)\rightarrow (R,2,0) \ (2,3)\rightarrow (L,4,1)$

$(3,0)\rightarrow (R,3,2) \ (3,1)\rightarrow (R,3,1) \ (3,2)\rightarrow (R,3,0) \ (3,3)\rightarrow (L,4,0)$

$(4,0)\rightarrow (L,5,2) \ (4,1)\rightarrow (L,4,1) \ (4,2)\rightarrow (L,4,0) \ (4,3)\rightarrow $ STOP

$(5,0)\rightarrow (L,5,2) \ (5,1)\rightarrow (L,5,1) \ (5,2)\rightarrow (L,6,2) \ (5,3)\rightarrow (R,2,1)$

$(6,0)\rightarrow (R,0,3) \ (6,1)\rightarrow (R,6,3) \ (6,2)\rightarrow (R,6,2) \ (6,3)\rightarrow (R,3,1)$

\medskip

We use the following alphabet:
$$\{t, \, a_0, \dots  a_3, \, Q_0, \dots Q_6, \, P_0 \dots P_3, \,  R\}$$

For every pair except $(4,3)$ the following functions are defined:
$q(i,j)$ is a new state, $p(i,j)$ is a new color of the current cell (the head leaves it).


\subsubsection{\bf Defining relations for the nilpotency question}\label{df1}

Consider the following defining relations:

\begin{eqnarray}
   &
tRa_l=Rta_l;  \text{\ \  $0\leq l\leq 3$}                           \label{tt1}  \\ &
ta_lR=a_lRt;  \text{\ \  $0\leq l\leq 3$}                           \label{tt1b}  \\ &
ta_ka_j=a_kta_j;                           \quad \text{ $0\leq k,j\leq 3$}    \label{tt2} \\ &
ta_kQ_iP_j=Q_{q(i,j)}P_kta_{p(i,j)}; \text{for left pairs $(i,j)$ and $0\leq k\leq 3$} \label{tt3} \\ &
tRQ_iP_j=RQ_{q(i,j)}P_0ta_{p(i,j)}; \text{for left pairs $(i,j)$ and $0\leq k\leq 3$} \label{tt5} \\ &
ta_lQ_iP_ja_ka_n=a_la_{p(i,j)}Q_{q(i,j)}P_kta_n;\text{for right pairs $(i,j)$ and $0\leq k\leq 3$} \label{tt4} \\ &
ta_lQ_iP_ja_kR=a_la_{p(i,j)}Q_{q(i,j)}P_kRt;\text{for right pairs $(i,j)$ and $0\leq k\leq 3$} \label{tt4r} \\ &
tRQ_iP_ja_ka_n=Ra_{p(i,j)}Q_{q(i,j)}P_kta_n;\text{for right pairs $(i,j)$ and $0\leq k\leq 3$} \label{tt4b} \\ &
tRQ_iP_ja_kR=Ra_{p(i,j)}Q_{q(i,j)}P_kRt;\text{for right pairs $(i,j)$ and $0\leq k\leq 3$} \label{tt4ar} \\ &
ta_lQ_iP_jR=a_la_{p(i,j)}Q_{q(i,j)}P_0Rt; \text{for right pairs $(i,j)$ and $0\leq l\leq 3$} \label{tt6}  \\ &
tRQ_iP_jR=Ra_{p(i,j)}Q_{q(i,j)}P_0Rt; \text{for right pairs $(i,j)$} \label{tt6b}  \\ &
Q_4P_3=0.                                  \label{tt7}
\end{eqnarray}

The relations \eqref{tt1} and \eqref{tt2} are used to move $t$ from the left edge to the last letter $a_l$ standing before
$Q_iP_j$ which represent the head of the machine.  The relations \eqref{tt3}--\eqref{tt6b}
represent the computation process. The relation \eqref{tt1b} is used to move $t$ through the finishing letter $R$.

Finally, the relation \eqref{tt7} halts the machine.


Let us call  $tRa_{u_1}a_{u_2}\dots a_{u_k}Q_iP_j a_{v_1}a_{v_2}\dots a_{v_l}R$ {\it the main word}.



\begin{thm} \label{th1}
Consider an algebra $A$ presented by the defining
relations \eqref{tt1}--\eqref{tt7}.
The word $tRUQ_iP_jVR$ is nilpotent in $A$ if and only if machine $M(i,j,U,V)$ halts.
\end{thm}



Actually we can prove that multiplication on the left by an element $t$ leads to the transition to the next state of the machine.



\subsubsection{\bf Defining relations for a zero divisors question}\label{df2}


We use the following alphabet:
$$\Psi=\{t, \, s, \, a_0, \dots  a_3, \, Q_0, \dots Q_6, \, P_0 \dots P_3, \,  L, \,  R \}.$$

For every pair except $(4,3)$ the following functions are defined:
$q(i,j)$ is a new state, $p(i,j)$ is a new color of the current cell (the head leaves it).



Consider the following defining relations:

\begin{eqnarray}
   &
tLa_k=Lta_k; \text{ $0\leq k\leq 3$}                             \label{td1}  \\ &
ta_ka_l=a_kta_l;                           \quad \text{ $0\leq k,l\leq 3$}    \label{td2} \\ &
sR=Rs;         \label{td9}  \\ &
sa_k=a_ks;    \text{ $0\leq k\leq 3$}  \label{td8} \\ &
ta_kQ_iP_j=Q_{q(i,j)}P_ka_{p(i,j)}s; \text{for left pairs $(i,j)$ and $0\leq k\leq 3$} \label{td3} \\ &
tLQ_iP_j=LQ_{q(i,j)}P_0a_{p(i,j)}s; \text{for left pairs $(i,j)$} \label{td5} \\ &
ta_lQ_iP_ja_k=a_la_{p(i,j)}Q_{q(i,j)}P_ks;\text{for right pairs $(i,j)$ and $0\leq k,l\leq 3$} \label{td4} \\ &
tLQ_iP_ja_k=La_{p(i,j)}Q_{q(i,j)}P_ks;\text{for right pairs $(i,j)$ and $0\leq k\leq 3$} \label{td4b} \\ &
ta_lQ_iP_jR=a_la_{p(i,j)}Q_{q(i,j)}P_0Rs; \text{for right pairs $(i,j)$ and  $0\leq l\leq 3$ } \label{td6}  \\ &
tLQ_iP_jR=La_{p(i,j)}Q_{q(i,j)}P_0Rs; \text{for right pairs $(i,j)$} \label{td6b}  \\ &
Q_4P_3=0;                                  \label{td7}
\end{eqnarray}

The relations \eqref{td1}--\eqref{td2} are used to move $t$ from the left edge to the letters
$Q_i$, $P_j$ which present the head of the machine.
The relations \eqref{td9}--\eqref{td8} are used to move $s$ from the letter $Q_i$, $P_j$ to the right edge.
The relations \eqref{td3}--\eqref{td6} represent the computation process. Here we use relations of the form $tU=Vs$.

Finally, the relation \eqref{td7} halts the machine.


\subsubsection{\bf Zero divisors and machine halt}\label{zd}


Let us call  $La_{u_1}a_{u_2}\dots a_{u_k}Q_iP_j a_{v_1}a_{v_2}\dots a_{v_l}R$ {\it the main word}.


\begin{thm} \label{th2}
The machine halts if and only if the main word is a zero divisor in
the algebra presented by the defining relations \eqref{td1}--\eqref{td7}.
\end{thm}



\medskip

\begin{rem*}
 We can consider two semigroups corresponding to our algebras:
 in both algebras each relation is written as an equality of two monomials.
 Therefore the same alphabets together with the same sets of relations define semigroups.
 In both semigroups the equality problem is algorithmically solvable, since it is solvable in algebras.
 However in the first semigroup a nilpotency problem is algorithmically unsolvable,
 and in the second semigroup a zero divisor problem is algorithmically unsolvable.
\end{rem*}


The entire proofs can be found at \cite{IPM}.
