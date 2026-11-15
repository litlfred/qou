---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds"
section_id: sec-001-2-quaternionic-matrices-and-flags
section_title: "Quaternionic matrices and flags"
section_number: 2
pages: 2-4
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.939
doc_brief: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-vector ﬁelds on quaternionic ﬂag manifolds, which geometrically determine"
---
We begin with some generalities on quaternionic matrices for which we
define the following subgroups of $\GL{\H}$:
\begin{eqnarray*}
	\RR 
		& 
		:= 
			&  
			\{ \diag{r_1,\dots,r_n} \ | \ r_i \in \R_+ \} 
	\\
	\UU 
		& 
		:= 
			& 
			\{\mbox{upper triangular matrices with  }1\mbox{'s along the
			diagonal}\} 
	\\
	\VV_w 
		&
		:=
			&
			\{ U\in \UU \ | \ \left( P_w U P_w^{-1}\right)^{t} \in \UU \}
	\\
		&
			&
			\mbox{here} \ P_w \
			\mbox{denotes the permutation matrix}
	\\
		&
			&
			(P_w)_{i,j}=\delta_{i,w(j)} \ \mbox{for} \
			w\in S_{n}  
	\\ 
        \DD 
		& 
		:= 
			& 
			\{ \diag{d_1,\dots, d_n} \ | \ d_i \in \H^* \}
	\\
        \BB 
		& 
		:= 
			& 
			\UU\DD
\end{eqnarray*}

\noindent Now for $G\in\GL{\H}$ we recall
 the \emph{strict Bruhat normal form} \cite{Draxl} of $G$ as:

\begin{displaymath}
	G = U D P_w V
\end{displaymath}

\noindent Here all the matrices are uniquely determined:
the matrix $D=\diag{d_1,\dots,d_n}$ belongs to $\DD$; $P_w$
is, as usual,  the permutation matrix corresponding to $w\in S_n$;
both $U$ and $V$ belong to $\UU$;  
and we further require that $P_w V P_w^{-1}$ 
is lower triangular with $1$'s along the diagonal, i.e. 
$V\in \VV_w$.  
This decomposition allows us to  define the Dieudonn\'{e} 
determinant \cite{Dieu} as the residue
of $\sgn{w}\cdot\prod d_i$ in $\H/[\H,\H]=\R_{+}$.
Moreover, by means of the strict Bruhat normal form, we obtain the Bruhat decomposition: 
 
\begin{eqnarray*} 
\GL{\H}=\coprod_{w\in S_n} \BB P_w \VV_w. 
\end{eqnarray*} 


\noindent Denoting $\ZZ_{w}:= \{ \BB P_w \VV_w \}$, we obtain from the
Bruhat decomposition a parameterization 
of $\GL{\H}$ by $S_n$. 
The condition that  $V^{w }:=wVw^{-1}$ is lower triangular 
implies in the case of $w =\id$ that  $V^{\id}=V$ must be both upper and lower
 triangular  hence equals  the identity matrix and hence
$\dim{\ZZ_{\id}}=\dim{\BB}$.
Taking $w$ to be  the longest permutation, $w_l=\left(n\ (n-1) \cdots \ 2\ 1\right)$,
rotates the matrix $V$ by $180^\circ$ so that it is lower triangular.
As no further conditions
on the entries of $V$ are imposed, we have that
$\dim{\ZZ_{w_l}}=4n^2$.  In general, we
define the length  of a permutation $w$, $\len{w}$,
to be the minimal number of adjacent transpositions required
in  a factorization of the permutation.  
One readily sees that the maximal number of non-zero
entries allowed in $V$, so that $V^w $ is lower triangular,
 is exactly $\len{w }$ so that
$\dim{\ZZ_w }=4\cdot \len{w }+\dim{\BB}$.  
We will see later that
the entries of $V$ give coordinates on the Bruhat cells of quaternionic flags.
 
Denoting conjugate transpose by $(\cdot)^\ast$, we have the Lie group:
\begin{displaymath}
  	\Sp:=\{g\in\GL{\H} \ | \ g^{\ast}g=\id\}
\end{displaymath}

\noindent We also identify the corresponding Lie algebra:

\begin{displaymath}
  	\sp:=\{X\in\gl{\H} \ | \  X + X^{\ast}=0\}
\end{displaymath}
with  $\Tn[x]{\Sp}$ for $x\in\GL{\H}$ by
left translation.  
One knows that matrices in $\Sp$  have Dieudonn\'{e} determinant 1, and
thus lie inside the semi-simple group:
\begin{displaymath}
	\SL:=\{g\in\GL{\H} \ | \ \det{g} = 1\}.
\end{displaymath}

\noindent We define the \emph{spheroid} to be 
$\Sph:=\Sp[1]^{n}\simeq (S^3)^n$, whose elements
are of the form $\diag{\exp{s_1},\dots,\exp{s_n}}$ where the $s_i$ 
are purely quaternionic (no real component).  
This is a subgroup of $\DD$, and we have, in fact, that:
\begin{displaymath}
	\DD = \Sph\times \RR
\end{displaymath}

\noindent We  denote the corresponding Lie algebra by $\s$.
The full quaternionic flag of $\H^n$, which we denote $F_n$,
can now be identified as $F_n \simeq \Sph\backslash\Sp\simeq
\BB\backslash\GL{\H}$.
Using the second identification of $F_n$, we denote
$\CC_w := \BB\backslash \ZZ_w$, which we call the \emph{Bruhat cells} of the
flag.  By our discussion above, we see that
\ $\dim{\CC_w}= 4\cdot \len{w}$. 

\
 
\example
Consider the space $\HP[1]$ identified as
 $\HP[1]\simeq \Sph\backslash\Sp[2] \simeq S^{4}$
from which we  obtain the  fibration: 
$$
\begin{array}{ccc}
\Sph\simeq S^3\times S^3\simeq\Sp[1]\times\Sp[1]	& \rightarrow	& \Sp[2]  \\
	             		&             	&  \downarrow      \\
	       			&             	& \HP[1] \simeq S^4
\end{array}.
$$

The Bruhat decomposition yeilds a decomposition of 
$\Sph\backslash\Sp[2]\simeq\HP[1]$ into the cells
$\CC _{(12)}$ and $\CC_\id$
which have real dimensions $4$ and $0$ respectively.
We view the cells under the identifications that
	$\CC_{(12)}\simeq \NN^2 = \mat{1}{\ast}{0}{1}\simeq\H$ 
and $\CC_\id$ is the North pole.  

Recall that $S^{4}$ has neither
a symplectic nor a complex structure (nor even an almost complex \cite{Mass}).  
This is one of the reasons for introducing the 
tetraplectic structure in \cite{F1}. 
\qex
