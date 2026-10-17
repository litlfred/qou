---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-014-6-galois-groups-of-equations-of-order-three
section_title: "Galois groups of equations of order three"
section_number: 6
pages: 23-30
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.654
latex_coverage_ratio: 0.975
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀerence Galois groups of order three equations for a large class"
---
\label{secord3}


Consider a linear  difference equation of order $3$ 
$$  \phi^3 (y)+ a_2 \phi^2 (y)+a_1 \phi (y)+a_0 y=0, \quad \text{where}\quad  a_i\in \k\quad \text{and}\quad  a_0 \neq 0.$$
 Let 
 $$
 L :=  \phi^3 + a_2 \phi^2 +a_1 \phi +a_0\in \k\left< \phi,\phi^{-1}\right>
 $$ 
be the corresponding difference operator and let $G\subset \GL_{3}(C)$ be its Galois group.  We want to compute $G$. 
 
 
\subsection{Reducible case}
 
 We follow the strategy explained in Section \ref{sec:reducible case} to treat the case where $G$ is reducible.  By \cite[Lemma~4.4]{adamczewski2021hypertranscendence}, $G$ is reducible if and only if the operator $L$ admits a right factor.  The right factor can have order one or two.  So $G$ is reducible if and only if the operator admits a right or left factor of order one.   Recall that up to consider the dual, we may reduce to the case where there is a right factor of order $1$.  \par 
Recall, see Lemma \ref{lem:eq left factor},  that the existence of a right factor of  order one is equivalent to the existence of  a solution $\alpha\in\k$ of the Riccati equation $\phi^2 (y)\phi(y)y+a_2 \phi (y)y+a_1y+a_0=0$.   
Assume that $L$ admits a right factor of order one.   Let us write $L$ as 
$\widetilde{L}(\phi -\alpha)$ where $\widetilde{L}:=\phi^2-\beta \phi-\gamma$. 
Then,  the system $[A_L]$ is equivalent to the system 
$$\phi (Y)= \left(\begin{array}{c|c}
\alpha &  1 \hspace*{0.3cm} 0  \\
\hline
0 &  A_2 
\end{array}\right)Y \, , $$
where the matrix $A_2$ corresponds to the equation of order two $\widetilde{L}y=0$ (that is $A_2 = A_{\widetilde{L}}$).  
From the order one and order two cases, we know how to compute $T_1\in \GL_1 (\k)$ and $T_2\in \GL_2 (\k)$ such that the systems whose matrices are $\phi(T_1)\alpha T_1^{-1}$ and $\phi(T_2)A_2 T_2^{-1}$ are in reduced form. Let us consider 
$$A := \begin{pmatrix}
\phi(T_1)&0 \\ 
0 &\phi(T_2)
\end{pmatrix}\left(\begin{array}{c|c}
\alpha &  1 \hspace*{0.3cm} 0  \\
\hline
0 &  A_2 
\end{array}\right)\begin{pmatrix}
T_1&0 \\ 
0 &T_2
\end{pmatrix}^{-1}.$$
This matrix  $A$ is of the form
$\begin{pmatrix}
\phi(T_1)\alpha T_1^{-1}&\star \\ 
0 &\phi(T_2)A_2 T_2^{-1}
\end{pmatrix}$. 
The first step consists in reducing the bloc diagonal system $[D]$ where $D:=\begin{pmatrix}
\phi(T_1)\alpha T_1^{-1}&0 \\ 
0 &\phi(T_2)A_2 T_2^{-1}
\end{pmatrix}$. Let $\Gdiag$ be the Galois group of this system, let $G_1$ be the Galois group of $[\phi(T_1)\alpha T_1^{-1}]$ and let $G_2$ be the Galois group of $[\phi(T_2)A_2 T_2^{-1}]$.  
The algebraic group $\Gdiag$ is an algebraic subgroup of $G_1\times G_2$. We explain the reduction on a case-by-case approach with respect to $G_2$. We will see that in each situation, reducing $[D]$ is equivalent to reducing a diagonal system whose reduction is explained in Section \ref{sec:diagonalCase}. Theorem \ref{thm:reduc_blocdiag} summarize the results we are going to prove for this first step.

  \begin{thm}
  \label{thm:reduc_blocdiag}
$\bullet$ Assume that $G_2$ is composed of diagonal matrices.  We can assume that $D$ is diagonal.  Then, we have to reduce a diagonal system and the reduction is explained in Section \ref{sec:diagonalCase}.\\
$\bullet$  Assume that $G_2$ is reducible and the first case does not hold.  We can assume that $D$ is upper triangular.  Then,   the reduction matrix is the diagonal matrix $T$ that reduces the diagonal  system $[\mathrm{Diag}(a,b,d)]$, where $a,b,d$ are the diagonal entries of $D$.  \\
$\bullet$ Assume that $G_2$ is imprimitive and irreducible.  We can assume that $\phi(T_2)A_2 T_2^{-1}$ is an anti-diagonal matrix.  Then $D_{[2]}$ is diagonal.  The reduction matrix that reduces $[D]$ is the matrix $T$ that reduces the diagonal  $\phi^{2}$-system $\phi^2 (Y)=D_{[2]}Y$. \\
$\bullet$ Assume that $G_2$ is primitive and irreducible. The reduction matrix is given by  $T:=\mathrm{Diag}(r_1,r_2,1)$, where  $\mathrm{Diag}(r_1,r_2)$ is the reduction matrix of the diagonal system $\phi (Y)=\begin{pmatrix}
\phi(T_1)\alpha T_1^{-1}&0\\ 
0 &\det(\phi(T_2)A_2 T_2^{-1})
\end{pmatrix}Y$.  
  \end{thm}

Let us  now prove the theorem. 

\begin{proof}
$\bullet$  Assume that $G_2$ is  formed by diagonal matrices. Then, $D$ is diagonal,  $\Gdiag$ is an algebraic group of diagonal matrices and the reduction is explained in Section \ref{sec:diagonalCase}. 

\medskip
$\bullet$
  Assume that  $G_2$ is reducible but not formed by diagonal matrices.   Up to a conjugation, we may assume that $G_2$ is formed by upper triangular matrices. By the classification of such nondiagonal reducible algebraic groups  that can be found in \cite[Lemma 4.4]{hendriks1998algorithm},  the upper triangular entry can be any  element of $C^*$.  
We can assume that the matrix $D$ is of the form $\begin{pmatrix}
a&0&0 \\ 
0 &b&c \\
0&0&d
\end{pmatrix}$ with $c\neq 0$.  Let us first reduce the diagonal system $[\mathrm{Diag}(a,b,d)]$. This will change the elements $a,b,c,d$ but, simplifying notations, let us denote by $a,b,c,d$ the new ones.  With Remark~\ref{rem1} and Theorem \ref{theo:reduced form},  we are looking for a reduction matrix of the form $T:=\begin{pmatrix}
1&0&0 \\ 
0&1&t \\
0&0&1
\end{pmatrix}$.
We denote by $[D']$ a reduced system, $D' = \begin{pmatrix}
a&0&0 \\ 
0 &b&c' \\
0&0&d
\end{pmatrix} $ for a $c'\in\k$. 
The only non-trivial equality in $\phi(T)D = D'T $ is on the $(2,3)$ entry: 
$$ 
c+  d \phi(t)  =  bt +c'.$$
We have $c'\neq 0$, otherwise the gauge transformation $\begin{pmatrix}
1&t \\
0&1
\end{pmatrix}$
would transform $[\phi(T_2)A_2 T_2^{-1}]$ into a diagonal system, a contradiction. 
By \cite{nguyen2008algebraic}, for all $c'\neq 0$, the algebraic group generated by   $ \begin{pmatrix}
b&c \\
0&d
\end{pmatrix} $  and $ \begin{pmatrix}
b&c' \\
0&d
\end{pmatrix} $ are the same. Since the $(1,1)$ entry of the algebraic group generated by $\begin{pmatrix}
\star&0&0 \\ 
0&\star&\star \\
0&0&\star
\end{pmatrix}$ does not affect the $(2,3)$ entry, we deduce that the algebraic group generated by $\begin{pmatrix}
a&0&0 \\ 
0&b&c\\
0&0&d
\end{pmatrix}$ and 
$\begin{pmatrix}
a&0&0 \\ 
0&b&c'\\
0&0&d
\end{pmatrix}$ are the same so  we may take $t=0$ and $c'=c$ and the system is already reduced. 

\medskip

$\bullet$ When $G_2$ is irreducible and imprimitive,  up to a conjugation, it is of the form 
 $G_2=G_{2,\mathcal{D}}\cup G_{2,\mathcal{A}}$, where $G_{2,\mathcal{D}}$ is formed by diagonal matrices and $G_{2,\mathcal{A}}$ by anti-diagonal matrices. 
We then have that  $\Gdiag$ is a union of diagonal matrices and   matrices of the form $\begin{pmatrix}
\star&0&0 \\ 
0 &0&\star \\
0&\star&0
\end{pmatrix}$.
We can assume that the matrix $D$ is of the form $\begin{pmatrix}
a&0&0 \\ 
0 &0&b \\
0&c&0
\end{pmatrix}$ since otherwise $G_2$ would be reducible.    

\begin{rem}
Note that $D_{[2]}$ is a diagonal matrix.  By Lemma \ref{lem2}, the connected components of the identity of the difference Galois groups of $[D]$ and $[D_{[2]}]$ are the same.  So if we are only interested in computing the connected component of $G$ we may just reduce the diagonal system $[D_{[2]}]$, see Section~\ref{sec:diagonalCase} for more details.
\end{rem}

Assuming we know how to compute the Galois group of a diagonal system,  we are able to compute a reduction  matrix $P\in \mathrm{GL}_{3}(\k)$ such that the system $\phi^2(Y) = \phi^2(P)D_{[2]}P^{-1}Y $ is reduced.  Consider $B:=\phi(P)DP^{-1}$, we have $B_{[2]}=\phi^2(P)D_{[2]}P^{-1}$ thus $[B_{[2]}]$ is reduced.    Let us prove that the system $[B]$ is already reduced.
  Let $H$ be the smallest algebraic group such that $B\in H(\k)$.  We have $\Gdiag\subset H$ (property of Galois groups, see Theorem~\ref{theo:reduced form}).
By Lemma~\ref{lem2},  the Galois group of the $\phi^2$-system $[B_{[2]}]$ and the Galois group of the $\phi$-system $[B]$ have the same connected component.  Since $[D_{[2]}]$  and $[B_{[2]}]$  have the same Galois group, and $[B_{[2]}]$  is reduced  we find 
$H^0=\Gdiag^0$.  We recall that $H$ is the smallest algebraic group such that $B\in H(\k)$. Then, $H/H^0=H/\Gdiag^0$ is generated by a single element, so it is cyclic (and finite since it is an algebraic group,  see \cite[Lemma 3.5]{hardouin2016galois}). 
Since $\Gdiag/\Gdiag^0$ is finite cyclic, 
$$
\Gdiag /\Gdiag^0 \sim  \Z/ m' \Z , \quad 
H/\Gdiag^0 \sim  \Z/ n' \Z,  
$$
for integers $m',n'$.   
 With Theorem \ref{theo:reduced form} and Lemma \ref{lem2}, there exists $k$ such that $B_{[k]}\in  \Gdiag^0 (\k)$.  
 
Since, $\Gdiag\subset H$,  we have   $m'\leq n'$.  By Theorem~\ref{theo:reduced form}, there exists $P_1\in H(\k)$ such that $B_{red}=\phi(P_1)BP_{1}^{-1}\in \Gdiag (\k)$ is reduced.  
 Since $H$ is an algebraic group defined over $C$, the equation over $C$ between the entries of $B$ and  $\phi^{k}(B)$, $k\in \Z$, are the same. Then, the class of $\phi^{k}(B)$ in $H/\Gdiag^0$ is independent of $k$. 
 
 Then, the  integer $m'$ (resp. $n'$) is the smallest such that we have the inclusion ${B_{red,[m']}=\phi^{m'-1}(B_{red})\times \dots \times B_{red}
\in \Gdiag^0 (\k)}$ (resp.  $B_{[n']}
\in \Gdiag^0 (\k)$).  Since $\Gdiag^0$ is composed of diagonal matrices and $B,B_{red}$ are not diagonal (otherwise $G_2$ would be reducible),  we find that $m'=2m$, $n'=2n$ for some integers $m,n$. 
We have $B_{red,[2m]}=\phi^{2m}(P_{1})B_{[2m]}P_{1}^{-1} \in \Gdiag^0(\k)$.
 Since $\Gdiag^0 $ is the smallest algebraic group such that  $B_{[2n]}\in \Gdiag^0 (\k)$
  and since $[B_{[2]}]$ is reduced as a $\phi^2$-system,  we have  $n\leq m$,  proving that $m'=n'$.  Then $\Gdiag=H$ and $[B]$ is already reduced. 
 
\medskip
  
$\bullet$  When $G_2$ is irreducible and primitive,  by  \cite[Section 4.4]{hendriks1998algorithm},  either  $G_2=\mathrm{GL}_2 (C)$, or there exists an integer $k$ such that 
$$
G_2 = \lbrace M\in\GL_2\left(\mathbb{C}\right) \mid \det(M)^{k}=1 \rbrace .
$$
We recall that $\det(G_2)$ is the difference Galois group of $\phi(Y)=dY$ with $d:=\det \left(\phi(T_2)A_2 T_2^{-1}\right)$.  
Let $R:=\mathrm{Diag}(r_1,r_2)$ be a reduction matrix of  the bloc diagonal system
 $\phi (Y)=BY$ where $B:=\begin{pmatrix}
\phi(T_1)\alpha T_1^{-1}&0\\ 
0 &d
\end{pmatrix}$.  
Then,  
$$
\phi(R)BR^{-1} = \mathrm{Diag}(\underbrace{\phi(r_1T_1)\alpha (T_1r_1)^{-1}}_{:=B_1}, \underbrace{\phi(r_2)d r_2^{-1}}_{:=B_2})\, .
$$
Let us prove that  $T:=\mathrm{Diag}(r_1,r_2,1)$ is a reduction matrix of $[D]$. Let $ H$ be the minimal algebraic group such that $B_{red}:=\phi(T)D T^{-1}\in H(\k)$. We set $B_{red}=\begin{pmatrix}
B_{red,1} & 0 \\ 0 & B_{red,2}
\end{pmatrix}$, with  $B_{red,\star}$ of convenient size. By construction, we have $B_{red,1} = B_1$ and $\det(B_{red,2}) = B_2$.
Note that $\Gdiag$ is a subgroup of  $G_1\times \det(G_2)  .\SL_2(C)$, where the identification $G_2\sim \det(G_2)  .\SL_2(C)$ is made via the map $\mathscr{M}= \mathrm{Diag}(\det(\mathscr{M}),1)\mathscr{M}'$, with $\det(\mathrm{Diag}(\det(\mathscr{M}),1))=\det(\mathscr{M})$, and $\mathscr{M}'\in \mathrm{SL}_2(C)$.   
Furthermore, since  $G_2$ is irreducible and primitive,  $\Gdiag$ contains $\{1\}\times \SL_2(C)$.  Consider the  map 
$$
\begin{array}{rccl}
\xi :  &   G_1 (\k) \times  \det(G_2). \SL_2 (\k) & \rightarrow & (\k^{*})^2 \\
     & (A,B) & \mapsto & (A,\det(B)) \, .
\end{array}
$$
 Let $ \{1\}\times \SL_2\subset H_1\subsetneq H_2\subset G_1\times G_2$ be two algebraic groups.   Since the kernel of $\xi$ is $ \{1\}\times \SL_2(\k)$,  we have $\xi(H_1(\k))\subsetneq \xi(H_2(\k))$.   Furthermore,  $\xi$ is injective on the set of  algebraic subgroups of  $(G_1\times G_2)(\k)$  containing $ \{1\}\times \SL_2(\k)$. \par 
By  Theorem \ref{theo:reduced form},  we find that $\Gdiag\subset H$ so that we have $\xi(\Gdiag(\k))\subset \xi(H(\k))$.  Since $R:=\mathrm{Diag}(r_1,r_2)$ is  a reduction matrix of  the bloc diagonal system
 $\phi (Y)=BY$, we have 
  $\xi(H(\k))\subset \xi(\Gdiag(\k))$,   and then $\xi(\Gdiag(\k))= \xi(H(\k))$.
From the above injectivity property,   $\Gdiag(\k)=H(\k)$. 
Then $T:=\mathrm{Diag}(r_1,r_2,1)$ is a reduction matrix of $[D]$.
\end{proof} 

  Thus, in all cases, we should be able to reduce the block diagonal system $[D]$ and find an associated reduction matrix, denoted by $T'$.  


\bigskip


The next step consists in reducing the system $[A]$.  We will see that finding the reduction matrix is equivalent to finding vector solutions in $\k$ of $\phi$-linear systems with coefficients in $\k$ that we will explicit. We summarize these results in Theorem \ref{thm:reduc_systcomplet}. We consider
$$B:=\phi(T')A T'^{-1}.
$$
The matrix $B$ is of the form $ \begin{pmatrix}
D_1& \widetilde{A} \\ 
0 &D_2
\end{pmatrix}$. By construction, the difference Galois group of $[B]$ is $G$, so let us compute the latter.  We write $B_{\mathcal{D}}:=\begin{pmatrix}
D_1&0 \\ 
0 & D_2
\end{pmatrix}$.  
Recall that  $\Gdiag$ is the Galois group of $[B_{\mathcal{D}}]$,  which is a reduced system thanks to the first step.
The Galois group $G$ is conjugated to a subgroup of 
$$\left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} c_1& c_2 \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c_1,c_2\in C \right\} =\Gdiag \ltimes U,
$$
where $U=\left\{ \begin{pmatrix}
1& c_1& c_2 \\ 
0 & 1 &0 \\
0&0&1
\end{pmatrix}\Bigg|   c_1,c_2\in C \right\}$  is isomorphic to two copies of the additive group.  

By Lemma \ref{lem:Gauge transfo reduc}, there exists $T:=\begin{pmatrix}
1& X \\ 
0 & \mathrm{Id}_2
\end{pmatrix}\in \GL_3 (\k)$
such that $[\phi(T)BT^{-1}]$ is reduced. 
 Let  $F:=\phi(T)BT^{-1}$.
 We have $F=  \begin{pmatrix}
D_1& A' \\ 
0 & D_2
\end{pmatrix}$ where $A' = - XD_1 +\widetilde{A}+\phi(X)D_2 $, that is, 
$$\widetilde{A}+\phi(X)D_2=XD_1 +A'.$$
Let $\Gunip=G \cap U$.  It is an algebraic subgroup of $U$ so it is of dimension $0$,  $1$ or $2$.

\begin{lem}
\label{lem:dimGu0}
The dimension of the algebraic group $\Gunip$ is $0$ if and only if there exists $X\in\k^2$ such that 
\begin{equation}
\label{eq:eqverif}
    \widetilde{A}+\phi(X)D_2=XD_1.
\end{equation}
In this case $[F]= [B_{\mathcal{D}}]$ is a reduced system equivalent to $[B]$ with the gauge transformation $T:=\begin{pmatrix}
1& X \\ 
0 & \mathrm{Id}_2
\end{pmatrix}$ and the Galois group $G$ is $\Gdiag$.
\end{lem}

\begin{proof}
From Theorem \ref{theo:reduced form}, the dimension of $\Gunip$ is $0$ if and only if $A' = (0\quad 0) $.
\end{proof}


\begin{lem}
\label{lem:dimGu1}
Assume that the dimension of $\Gunip$ is not $0$. 
 If the dimension of $\Gunip$ is $1$ then $D_2$ is a triangular matrix (lower or upper triangular, including the diagonal matrices).
If it is the case, we can assume that $D_2$ is a lower triangular matrix and three cases occur:

$\bullet$ Case where $D_2$ is lower triangular but not diagonal. In this case 
$$G =  \left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} c&0 \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\}.
$$

$\bullet$ Case where $D_2$ is diagonal but not a dilatation.  In this case, $G$ is the same group as before or $\left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} 0&c \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\}$, depending if there is a solution in $\k$ of some linear equations with coefficients in $\k$ (see equations \eqref{eqaverifier} or \eqref{eqaverifierbis}). 

$\bullet$ Case where $D_2$ is a dilatation.  In this case,
$$G =  \left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} \lambda c & \mu c \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\}.
$$
where $\lambda, \mu\in C^2 \setminus \{(0,0)\}$ can be explicited, see \eqref{eq:eqverif3}.

In each case,  the proof gives an  explicit gauge transformation and a reduced system.
\end{lem}

\begin{proof}
Let $\mathscr{Y}$ be such that $h= \begin{pmatrix}
1&\mathscr{Y} \\ 
0 & \mathrm{Id}_2 
\end{pmatrix} \in \Gunip$.  
For $g=\begin{pmatrix}
a_g & \mathscr{C}_g \\ 
0 & \mathscr{B}_g  
\end{pmatrix} \in G$, let us compute $ghg^{-1}\in \Gunip$.  We write 
$ghg^{-1}= \begin{pmatrix}
1&\mathscr{Z}\\ 
0 & \mathrm{Id}_2 
\end{pmatrix} $,  so that we have $\begin{pmatrix}
a_g & \mathscr{C}_g \\ 
0 & \mathscr{B}_g  
\end{pmatrix}\begin{pmatrix}
1& \mathscr{Y} \\ 
0 & \mathrm{Id}_2 
\end{pmatrix} =\begin{pmatrix}
1&\mathscr{Z} \\ 
0 & \mathrm{Id}_2 
\end{pmatrix} \begin{pmatrix}
a_g & \mathscr{C}_g \\ 
0 & \mathscr{B}_g  
\end{pmatrix}$. 
Then,  $a_g \mathscr{Y} + \mathscr{C}_g = \mathscr{C}_g + \mathscr{Z}\mathscr{B}_g$ proving that
$ghg^{-1}= \begin{pmatrix}
1&a_g \mathscr{Y} \mathscr{B}_g^{-1} \\ 
0 & \mathrm{Id}_2 
\end{pmatrix}  \in \Gunip$.
If the dimension of $\Gunip$ is 1 then  $a_g \mathscr{Y} \mathscr{B}_{g}^{-1}=c\mathscr{Y}$ for some $c\in C^*$. Taking the transposition,  we find $(\mathscr{B}_g^{-1})^{t}\mathscr{Y}^{t}=c'\mathscr{Y}^t$ for some $c'\in C^*$. 
So $\mathscr{Y}^{t}$ is an eigenvector of any elements $(\mathscr{B}_g^{-1})^{t}$.  This means that the elements $\mathscr{B}_g$ are all conjugated to lower triangular matrices (or upper triangular matrices) and $Y^{t}$ is necessarily a common eigenvector. Since $[F]$ is a reduced system, $D_2$ is also a triangular matrix. Thus, if $\Gunip$ has dimension $1$ then $D_2$ is a triangular matrix.\\

Let us  assume that $\Gunip$ has dimension $1$ thus  $D_2$ is a triangular matrix and, up to conjugation, we can assume that $D_2$ is lower triangular. In what follows, we denote by $\widetilde{A}_1$ and $\widetilde{A}_2$ the entries of $\widetilde{A}$. We distinguish three cases:

$\bullet$ Case where $D_2$ is lower triangular but not diagonal. We set $D_2 = \begin{pmatrix}
d_1 & 0 \\ d_3 & d_4
\end{pmatrix}$. In this case, the common eigenvectors of the  elements $(\mathscr{B}_g^{-1})^t$ for $g\in G$ are  $\mathscr{Y}^{t}$ with $\mathscr{Y}:=\begin{pmatrix}
    f & 0 
\end{pmatrix}$ where $f\in C$, thus the system $[B]$ is equivalent to the system $[F]$ where $F$ is of the form $\begin{pmatrix}
D_1& \begin{matrix} f& 0 \end{matrix} \\ 
0 &D_2
\end{pmatrix}$, for a certain $f\in \mathbf{k}^*$, thanks to a gauge transformation $T:=\begin{pmatrix}
1& x_1& x_2 \\ 
0 & 1 &0 \\
0&0&1
\end{pmatrix}$.  Recall that $\widetilde{A}+\phi(X)D_2=XD_1+A'$.  Since the second entry of $A'$ has to be $0$,  we obtain 
\begin{equation}
    \label{eq:eqaverifierD2triang}
    \widetilde{A}_2+\phi(x_2)d_4= D_1 x_2.
\end{equation}
From Theorem \ref{theo:reduced form}, this implies that
$$G\subset \left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} c&0 \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\}.
$$
Since $G = \Gdiag\ltimes \Gunip$, we obtain that the previous inclusion is an equality. 


$\bullet$ Case where $D_2$ is diagonal but not a dilatation.  We set $D_2 = \mathrm{Diag}(d_1,d_4)$. Up to a conjugation, we have $\Gunip=\left\{ \begin{pmatrix}
1& c&0 \\ 
0 & 1 &0 \\
0&0&1
\end{pmatrix}, c\in C \right\}$ or  $\Gunip=\left\{ \begin{pmatrix}
1& 0&c \\ 
0 & 1 &0 \\
0&0&1
\end{pmatrix}, c\in C \right\}$. 
Using the same notations as before, we obtain that $\Gunip$ is the first one, resp. the second one, if there exists a solution $y\in \k$ of the equation
\begin{align}
    \label{eqaverifier}
    \widetilde{A}_2 + \phi(y)d_4 = D_1y \, ,
\end{align}
resp. of the equation
\begin{align}
    \label{eqaverifierbis}
   \widetilde{A}_1 + \phi(y)d_1 = D_1y  \, .
\end{align}
Not that only one of these two equations has a solution in $\k$ because if it is not the case, the solutions $x_1, x_2$ are such that $X:=(x_1\quad x_2)\in\k^2$ is a solution of \eqref{eq:eqverif}, a contradiction since the dimension of $\Gunip$ is not $0$.
With the same reasoning as before, we obtain that the Galois group $G$ is 
$$\left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} c & 0 \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\} \text{ or } \left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} 0&c \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\}\, ,
$$
if $\Gunip$ is respectively the first or the second algebraic group. 


$\bullet$ Case where $D_2$ is a dilatation. We set $D_2=d\mathrm{Id}_2$ with $d\in \mathbf{k}^*$. Let $\lambda,\mu\in C$ not all zero such that 
$\Gunip=\left\{ \begin{pmatrix}
1& \lambda c& \mu c \\ 
0 & 1 &0 \\
0&0&1
\end{pmatrix}, c\in C \right\}$. From Lemma \ref{lem:Gauge transfo reduc}, since $G = \Gdiag \ltimes \Gunip$, there exists $T:=\begin{pmatrix}
 1 & X \\ 0 & \mathrm{Id}_2
\end{pmatrix}$ such that $\phi(T)B=FT$,
 where $[F]$ is reduced with $F=\begin{pmatrix}
D_1& \begin{matrix} \lambda f& \mu f\end{matrix} \\
0 &D_2
\end{pmatrix}$, $f\in  \mathbf{k}^*$.
This is equivalent to
$$\widetilde{A}+\phi(X)D_2=D_1X+\begin{pmatrix}\lambda f & \mu f  \end{pmatrix}\, ,$$
that is,
$$
\left\lbrace\begin{array}{l}
     d \phi (x_1) = D_1 x_1 - \widetilde{A}_1 +\lambda f  \\
     d \phi (x_2) = D_1 x_2 - \widetilde{A}_2 +\mu f 
\end{array}\right.
$$
where $x_1,x_2$ are the coordinates of $X$. 
Taking $\mu$ times the first line minus $\lambda$ times the second,  we find that $x=\mu x_1-\lambda x_2$ is solution of $d\phi(x)=D_1 x- \mu \widetilde{A}_1 +\lambda  \widetilde{A}_2$. 
We then find that
 this is equivalent to the fact that the vector $Y:= \begin{pmatrix} \lambda\\ \mu \\ x \end{pmatrix}$ is solution of 
\begin{equation}
\label{eq:eqverif3}
    \phi(Y)=
 \begin{pmatrix}1 & 0 & 0  \\
0&1&0\\
\widetilde{A}_2d^{-1} & -\widetilde{A}_1 d^{-1} & D_1d^{-1}
 \end{pmatrix}Y.
\end{equation}
Conversely, any nonzero solution of the latter system in $\mathbf{k}^3$ will give a reduction matrix, and a reduced form.
\end{proof}

Let us summarize the results proved in Lemma \ref{lem:dimGu0} and Lemma \ref{lem:dimGu1}. 

\begin{thm}
\label{thm:reduc_systcomplet}
If the equation \eqref{eq:eqverif} has a solution then the Galois group $G$ is $\Gdiag$. If this equation has no solution then we have the following cases :
\begin{itemize}
    \item if $D_2$ is a triangular matrix but not diagonal, up to a conjugation we assume that it is lower triangular, and if the equation \eqref{eq:eqaverifierD2triang} has a solution then $$G = \left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} c&0 \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\}.
$$ 
    \item if $D_2$ is a diagonal matrix but not a dilatation and if \eqref{eqaverifier} (the same equation as \eqref{eq:eqaverifierD2triang})  or \eqref{eqaverifierbis} has a solution then $G$ is the previous group or respectively $$ \left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} 0&c \end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\}.
$$ 
    \item if $D_2$ is a dilatation and \eqref{eq:eqverif3} has a solution then $$G = \left\{ \begin{pmatrix}
\mathscr{C}_1& \begin{matrix} \lambda c&\mu c\end{matrix} \\ 
0 & \mathscr{C}_2
\end{pmatrix}\Bigg|   \begin{pmatrix}
\mathscr{C}_1& 0 \\ 
0 & \mathscr{C}_2
\end{pmatrix} \in \Gdiag,   c\in C \right\} 
$$  where $\lambda, \mu\in C$ not all zero are given by a solution of \eqref{eq:eqverif3}. 
    \item if none of these three cases occur then $G=\Gdiag\ltimes U$ (in this case, the dimension of $\Gunip$ is $2$).
\end{itemize}
\end{thm}



\subsection{Imprimitive case}
Assume now that $G$ is irreducible and treat the case where $G$ is imprimitive. This case is  solved in Section \ref{sec:imprimitive case}.
 It is imprimitive if and only if the difference Galois group of $\phi^3 Y=A_{[3]}Y$ is diagonal. We use the reducible case (with $\phi$ replaced by $\phi^3$) to check this property.   In that case we are able to compute $d\in \k^*$,  solution of the Riccati equation corresponding to $\phi^3 Y=A_{[3]}Y$.  We now follow Proposition \ref{prop2}. 
Let us   compute a reduced form of $\phi(y)=dy$, that is compute $f\in \k^*$ such that $\phi(y)=d\frac{\phi(f)}{f}y$ is reduced.  Then, a reduced form is given by 
$\left( \begin{array}{ccc}
0&1&0\\
0 &0&  f^{-1}\\
\phi(f)d & 0&0
\end{array}\right) $ with reduction matrix $\mathrm{Diag}(1,1,f)$.  



 

\subsection{Primitive case}

Assume now that $G$ is irreducible and primitive.  Let $D(G^0)$ be the derived subgroup of $G^0$ that is irreducible and primitive by Proposition \ref{prop4}. By definition, $D(G^0)\subset \mathrm{SL}_{3}(C)$.   By \cite[Section 2.2]{singer1993galois}, either $D(G^0)$ is $\mathrm{SL}_3(C)$, or it is isomorphic to $\mathrm{PSL}_2(C)$.  Since $\mathrm{SO}_3(C)$ is also a primitive subgroup of  $\mathrm{SL}_3(C)$,  it is isomorphic to $\mathrm{PSL}_2(C)$.  
The matrices commuting with   $\mathrm{SL}_3(C)$  (resp. $\mathrm{SO}_3(C)$)  are dilatations and we find that $Z(G^0)$, the center of $G^0$, is isomorphic to an algebraic subgroup of  $C^*$.  Since it is connected, it is then $C^*$ or $\{1\}$. By Proposition~\ref{prop4}, $G^0=Z(G^0).D(G^0)$.  \par 
When $D(G^0)=\mathrm{SL}_3(C)$ we find that either $G^0=\mathrm{GL}_3(C)$, or 
$G^0=\mathrm{SL}_3(C)$. Since $G/G^0$ is cyclic, we deduce that  either $G=\mathrm{GL}_3(C)$, or there exists an integer $k$, which is the order of the group $G/G^0$, such that 
$G=\lbrace M\in\GL_3\left( C\right) \mid \det(M)^{k}=1 \rbrace $. Then $G=Z(G).D(G)$, where $Z(G)$ is composed by dilatations matrices and $D(G)=\mathrm{SL}_3(C)$.\par 
Assume now that $D(G^0)=\mathrm{SO}_3(C)$. Then  either $G^0 \sim C^* .\mathrm{SO}_3(C)$, or $G^0=\mathrm{SO}_3(C)$. Moreover, since $G/G^0$ is cyclic, it is abelian and since the derived group $D(G)$ is the smallest subgroup $H$ of $G$ such that $G/H$ is abelian, we have $D(G)\subset G^0$.
Then $\mathrm{SO}_3(C)=D(G^0)\subset D(G)\subset G^0 \subset C^*. \mathrm{SO}_3(C)$. The normalizer of $\mathrm{SO}_3(C)$ in $\mathrm{GL}_3(C)$ is $C^* . \mathrm{SO}_3(C)$ and the same holds for $C^*. \mathrm{SO}_3(C)$. Since the normalizer of $D(G)$ in $G$, which is $G$, is included in the normalizer of $D(G)$ in $\GL_3(C)$, we find that $G\subset C^*. \mathrm{SO}_3(C)$. Thus, $\mathrm{SO}_3(C)\subset G\subset C^*. \mathrm{SO}_3(C)$.
 Then, either $G\sim C^*. \mathrm{SO}_3(C)$, or there exists $k\in \N^*$, such that $G\sim U_k .\mathrm{SO}_3(C)$, where $U_k$ denote the group of all k-th roots of unity. Hence $G=Z(G).D(G)$, where $Z(G)$ is composed by dilatations matrices and $D(G)=\mathrm{SO}_3(C)$.
 To summary, we have proved the following result:
 \begin{prop}\label{prop5}
 Assume that $G$ is irreducible and primitive. Then, $G=Z(G).D(G)$, where $Z(G)$ is included in the group of scalar matrices and $D(G)$ is either $\mathrm{SL}_3(C)$ or $\mathrm{SO}_3(C)$. 
 \end{prop}
\begin{rem}
If $D(G)=\mathrm{SL}_3(C)$, then
$ 
Z(G) = \lbrace\lambda \mathrm{Id}_3  \text{ where } \lambda^3\in \det(G) \rbrace\, .
$
Recall that  $\det(G)$ is the Galois group of an equation of order one $\phi (y)=\det (A)y$. 

Assume now $D(G)=\mathrm{SO}_3(C)$. If $\det(G)=C^*$, then $Z(G) = C^*$. If $\det(G)=U_n$ with $\gcd(n,3)\neq 1$, then $Z(G)=U_{3n}$. In the case $\det(G)=U_n$ with $\gcd(n,3)= 1$, we have $Z(G)=U_{3n}$ or $U_n$.
\end{rem}

We want to give a criterion to decide whether $D(G)=\mathrm{SO}_3(C)$ or not.  Let us prove the following lemma. 

 \begin{lem}\label{lem3}
Assume that $G$ is irreducible and primitive. Let  $\overline{\mathbf{k}}$ be the algebraic closure of $\k$. We may extend $\phi$ on the latter.   The following facts are equivalent. 
\begin{itemize}
\item  $D(G)=\mathrm{SO}_3(C)$.
\item there exist $T\in \mathrm{GL}_3(\k)$,  $\lambda \in \mathbf{k}^*$  and $B\in  \mathrm{SO}_3(\mathbf{k})$ such that   \begin{equation}\label{eq1}
 \phi(T)AT^{-1}=\lambda B.
 \end{equation}
\item there exist $T\in \mathrm{GL}_3(\overline{\mathbf{k}})$,  $\lambda \in \overline{\mathbf{k}}^*$  and $B\in  \mathrm{SO}_3(\overline{\mathbf{k}})$ such that  \eqref{eq1} holds. 
\end{itemize}
\end{lem}

\begin{proof}
Recall that   $G\sim Z(G). D(G)$,  where $D(G)\in \{\mathrm{SO}_3(C),\mathrm{SL}_3(C) \}$ and $Z(G)$ is composed by dilatations matrices.  By Theorem~\ref{theo:reduced form},  $D(G)=\mathrm{SO}_3(C)$ if and only if 
there exist $T\in \mathrm{GL}_3(\k)$,  $\lambda \in \mathbf{k}^*$   and $B\in  \mathrm{SO}_3(\mathbf{k})$ such that  \eqref{eq1} holds.  So the first two items are equivalent.   If the second item holds, then the third item holds.  Conversely assume that the third item holds.  
Consider $\overline{G}$,  the Galois group over $\overline{\mathbf{k}}$.  By Theorem \ref{theo:reduced form},  $\overline{G}\subset \overline{C}^*. \mathrm{SO}_3(\overline{C})$. 
 By Galois correspondence, see \cite[Chapter 1]{van2006galois},  $\overline{G}$ is a subgroup of $G$ and $G/\overline{G}$ is  finite. Since $G\sim  Z(G). D(G)$,  where $D(G)\in \{\mathrm{SO}_3(C),\mathrm{SL}_3(C) \}$, this shows that $D(G)$ cannot be $\mathrm{SL}_3(C)$.  Then $D(G)= \mathrm{SO}_3(C)$. 
\end{proof}

The equation \eqref{eq1} is non linear and may be complicated to solve. Let us see how we may reduce to a linear equation over $\overline{\mathbf{k}}$.  
For the sake of completeness, let us first prove a well-known
result that will  be used in the sequel.
 
 \begin{lem}\label{lem4}
 Let $K$ be a field of characteristic zero.   
Let $X\in \mathrm{GL}_n (K)$ be a symmetric matrix. Then, there exist $F,D\in \mathrm{GL}_n (K)$ with $D$ diagonal such that $X=FDF^t$. 
 \end{lem}
 
 \begin{proof}
 Let $E_{i,j}$ be the square matrix of order $n$ whose $(i,j)$ entry is $1$ and the other entries are $0$. 
For $i\neq j$, let $T_{i,j}$ be the corresponding  transvection matrix, that is $\mathrm{Id}_n+E_{i,j}$. 
If we consider 
$T_{i,j}X(T_{i,j})^{t}$ we make the following operations: the column $C_i$ of $X$ is replaced by $C_{j}+C_i$ and then the line $L_i$ is replaced by $L_{i}+L_j$. Take $i=1$. This shows that $X_{1,1}$ is replaced by $X_{1,1}+X_{j,1}+X_{1,j} +X_{j,j}=X_{1,1}+2X_{1,j}+X_{j,j}$. \par 
Let us see how to reduce to the case $X_{1,1}\neq 0$.  Assume $X_{1,1}=0$. If there exists $j>1$ such that $X_{j,j}\neq 0$ then we replace $X$ by $PXP^t$ where $P = E_{1,j} + E_{j,1} + \sum\limits_{k\neq 1,j}E_{k,k}$ is the permutation matrix which exchanges the lines $1$ and $j$. We have $P= P^{-1} = P^{t}$. If $X_{j,j}=0$ for all $j$, we consider $j$ such that $X_{1,j}\neq 0$ (such $j$ exists otherwise the first line is only composed of $0$ entries, contradicting  the fact that $X$ is invertible).  Let us perform 
$T_{1,j}X(T_{1,j})^{t}$ so that $X_{1,1}$ is replaced by $X_{1,1}+2X_{1,j}+X_{j,j}=2X_{1,j}\neq 0$.   So we may reduce to the case where $X_{1,1}\neq 0$. \par 
For $i\in \lbrace 2,\ldots,n\rbrace$, let $T  := \mathrm{Id}_n + \alpha_i E_{i,1}$ with $\alpha_i:=- X_{i,1}/X_{1,1}$. Computing $TXT^{t}$, $X_{i,1}$ is replaced by  $\alpha_i X_{1,1} + X_{i,1} = 0$ thus, as in a Gaussian Pivot, we force $X_{2,1}=\dots =X_{n,1}=0$. We also have  $X_{1,2}=\dots =X_{1,n}=0$ since the matrix obtained remains symmetric.  We repeat the procedure to  the other lines and columns to find the result. 
 \end{proof}
 
 Toward an efficient way to check that \eqref{eq1} holds,  let us prove the following. 
 
 \begin{lem}\label{lem6}
The following facts are equivalent. 
\begin{itemize}
\item There exist $T\in \mathrm{GL}_3(\overline{\mathbf{k}})$,  $\lambda \in \overline{\mathbf{k}}^*$  and $B\in  \mathrm{SO}_3(\overline{\mathbf{k}})$ such that \eqref{eq1} holds. 
\item There exist $\lambda \in \overline{\mathbf{k}}^* $,  $X\in \mathrm{GL}_3(\overline{\mathbf{k}})$ such that $X=X^t$,  and  $A XA^t =\lambda^2\phi(X)$.
\end{itemize}
\end{lem}

\begin{proof}
Let us prove that the first point implies the second.  
Let us assume the existence of  $T\in \mathrm{GL}_3(\overline{\mathbf{k}})$,  $\lambda \in \mathbf{\overline{\mathbf{k}}}^*$,  and $B\in  \mathrm{SO}_3(\overline{\k})$ such that \eqref{eq1} holds. Let us set $P:=T^{-1}$ and note that $P^t$ is the inverse of $T^t$.  Using $BB^t=\mathrm{Id}_3$ we find that \eqref{eq1} implies
 $$\phi(T)APP^t A^t \phi(T^t)=\lambda^2 \mathrm{Id}_3.$$
The latter is equivalent to 
 $$APP^t A^t =\lambda^2\phi(PP^t).$$
 We obtain the result if we set $X=PP^t$. \par 
 Conversely,  assume that the second item holds.  By Lemma \ref{lem4},  let us write $X=FDF^t$ with matrices whose coefficients are in $\overline{\mathbf{k}}$. Since $\overline{\mathbf{k}}$ is algebraically closed,  $F\sqrt{D}$ has coefficients in $\overline{\mathbf{k}}$ and we may write 
 $X=F\sqrt{D}(\sqrt{D})^t F^t$, where $\sqrt{D}$ is any diagonal matrix whose square is $D$.  Let us perform $\phi(T)AT^{-1}$ where $T\in \mathrm{GL}_3(\overline{\mathbf{k}})$ is the inverse of $F\sqrt{D}$.  Note that $X=T^{-1}(T^{-1})^t $.  It suffices to prove that $B=\phi(T)AT^{-1}\lambda^{-1}\in \mathrm{SO}_3(\overline{\mathbf{k}})$. 
 Then, 
 $$B B^t=\lambda^{-2} \phi(T)AT^{-1}(T^{-1})^t A^{t}\phi(T^t)=\lambda^{-2} \phi(T)AX A^{t}\phi(T^t).$$
 We now use $A XA^t =\lambda^{2}\phi(X)$ to deduce that the latter equals 
 $ \phi(T)\phi(X) \phi(T^t). $
With $X=T^{-1}(T^{-1})^t $, we deduce that  $\phi(T)\phi(X) \phi(T^t)$ is the identity, that is $B\in  \mathrm{SO}_3(\overline{\mathbf{k}})$. 
\end{proof}

If we replace $X$ by $X':=X\det(X)^{-1/3}\in \mathrm{SL}_3 (\overline{\mathbf{k}})$,  we find $A X'A^t =\det(A)^{2/3}\phi(X')$. Indeed, the equality $AXA^t=\lambda^2 \phi(X)$ is equivalent to 
\begin{equation}
\label{eq:for_determinant}
AX'A^t = \lambda^2\det(X)^{-1/3}\det(\phi(X))^{1/3} \phi(X')\, .
\end{equation}
Taking the determinant in \eqref{eq:for_determinant} and using that $\det(X')=1$, we have $\det(A)^2=\lambda^6\det(X)^{-1}\det(\phi(X))$. We obtain the desired result thanks to 
 \eqref{eq:for_determinant} and this last equality.
With Lemma \ref{lem3},  and Lemma \ref{lem4},  we have proved the following result.
 
\begin{prop}\label{prop3}
Assume that $G$ is irreducible and primitive.   Then,  $D(G)=\mathrm{SO}_3(C)$ if and only if there exists $X\in \mathrm{SL}_3(\overline{\mathbf{k}})$ such that $X=X^t$ and  $A XA^t =\det(A)^{2/3}\phi(X)$.
\end{prop}

Proposition \ref{prop3} then reduces the criterion on $D(G)$ to look at solutions in $\overline{\mathbf{k}} $ of linear $\phi$-difference systems with coefficients in $\overline{\mathbf{k}}$. More precisely the condition $X=X^t$ drops the number of unknowns from $9$ to 
$6$.  
Solving a system in $\overline{\mathbf{k}}$ is in general a complicated task but in many examples, by studying the poles of the system for instance, we might be able to prove that the system has no solutions, showing that $D(G)\neq \mathrm{SO}_3(C)$.

Let us now see  how to compute the reduced form.  
First, assume that $D(G)=\mathrm{SL}_3 (C)$. 
We compute $\det(G)$ as the difference Galois group of an order one system $\phi(y)=a_0 y$ with reduction matrix $f\in \k^*$, that is $\phi(y)=a_0\frac{\phi(f)}{f} y$ is reduced with Galois group $\det(G)$.
Then, we perform, as in \cite[Section 4.4]{hendriks1998algorithm}, the gauge transformation  $T=\mathrm{Diag}(f,1,1)$ to obtain a system $[B]$.  Since $\det(B)=a_0\frac{\phi(f)}{f}$,   and $\phi(y)=a_0\frac{\phi(f)}{f}y$ is reduced with Galois group $\det(G)$,  we find that $B\in G(\mathbf{k})$.  Then,  $B$ is a reduced form and $T$ is the reduction matrix.   \par
Now consider the case where $D(G)= \mathrm{SO}_3(C)$. 
By Lemma \ref{lem3}, we know that there exist $T\in \mathrm{GL}_3(\k)$,  $\lambda \in \mathbf{k}^*$  and $B\in  \mathrm{SO}_3(\mathbf{k})$ such that \eqref{eq1} holds. As above, let us set $X'=T^{-1}(T^{-1})^{t}\det(T)^{2/3}\in \mathrm{SL}_3 (\overline{\mathbf{k}})$. Then, $X'$ satisfies $X'=(X')^t$ and  $A X'A^t =\det(A)^{2/3}\phi(X')$. Let us write $X'=FDF^t$ as in Lemma \ref{lem4}.   Note that the proof of Lemma \ref{lem4} is constructive so $F$ and $D$ may be effectively computed. 
Let us perform the gauge transformation  $\phi(\alpha (F\sqrt{D})^{-1})A(\alpha (F\sqrt{D})^{-1})^{-1}$ where $(F\sqrt{D})^{-1}\in \mathrm{GL}_3(\overline{\mathbf{k}})$ and $\alpha \in \overline{\mathbf{k}}^*$. From what precedes, all reduction matrices with coefficients in $\overline{\mathbf{k}}$  are of this form. Since there is a reduction matrix with coefficients in $\k$,
there is a choice of $X'$  and $\alpha$ such that the corresponding $\alpha (F\sqrt{D})^{-1}$ has entries in $\k$. Note that this procedure is purely theoretical and not effective. So if $\alpha (F\sqrt{D})^{-1}$ does not have entries in  $\mathbf{k}$ for all $\alpha \in \overline{\mathbf{k}}^*$,  we take another solutions $X'$ 
with a corresponding $\alpha (F\sqrt{D})^{-1}\in \mathrm{GL}_3(\mathbf{k})$. At this stage, we have $\phi(\alpha (F\sqrt{D})^{-1})A(\alpha  (F\sqrt{D})^{-1})^{-1}=\beta A_0$, with $\beta \in \mathbf{k}^*$  and $A_0\in \mathrm{SO}_3 (\mathbf{k})$. By Theorem~\ref{theo:reduced form} and Proposition \ref{prop5}, we find that a reduction matrix is of the form $\alpha_1 \alpha (F\sqrt{D})^{-1}$, $\alpha_1 \in \mathbf{k}^*$.  We may compute $\alpha_1$ by reducing the system $\phi (y)=\beta y$. Hence the reduced form is $\frac{\phi (\alpha_1)}{\alpha_1}\beta A_0$.



\begin{ex}\label{ex4}
Consider $G$ the difference Galois group of \eqref{eq0} over $\C(z^{1/*})$. Assume that $t\neq 0$. Assume by contradiction that $D(G)=\mathrm{SO}_3(\C)$.
The eigenvalues of matrices of $\mathrm{SO}_3(\C)$ are of the form $(1,a^{\pm 1})$,  $a\in \C^*$.  Then,  the eigenvalues of elements of $G$ are for the form $(c,ca^{\pm 1})$,  $c,a\in \C^*$.   By \cite[Section 2.4]{RS2009}, combined with the computation of the Newton polygon in Example \ref{ex2}, $G$ contains the so-called theta torus,  elements of the form $\mathrm{Diag}(1,1,d)$, $d\in \C^*$.  If the triple  $\mathrm{Diag}(1,1,d)$ is of the form $(c,ca^{\pm 1})$, then either $a=1=c=d$, or $a=c=-1$ and $d=-1$.  Then,  $\mathrm{Diag}(1,1,2)$ can never be of the form $(c,ca^{\pm 1})$,  showing that $D(G)\neq \mathrm{SO}_3(\C)$.  Then $D(G)=\mathrm{SL}_3(\C)$. 
\end{ex}
