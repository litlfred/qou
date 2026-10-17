---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-008-32-the-imprimitive-case
section_title: "The imprimitive case"
section_number: 3.2
pages: 11-19
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.982
---
\label{sec:imprimitive case}

 Let $G$ be an algebraic subgroup of $\GL_{n}(C)$.  We say that $G$ is imprimitive if there exists a nontrivial decomposition into $C$-vector spaces  $C^n =V_1 \oplus \dots \oplus V_k$, such that any element of $G$ induces a permutation between the $V_i$.  We say that $G$ is primitive otherwise.  

Consider $G$, an imprimitive group and let us write a decomposition   $C^n =V_1 \oplus \dots \oplus V_k$.  The image of $V_1$ under  an element of $G$ is of the form $V_j$,  where $V_j$ and $V_1$ have the same dimension. If we further assume that $G$ is irreducible, for all $1\leq j \leq k$, there exists $\sigma\in G$, such that  $\sigma (V_1)=V_j$, proving that each $V_j$ has the same dimension and thus is a divisor of the order $n$ of the equation \eqref{eq:diffcesystembase}.   Therefore,  when $n$ is prime and $G$ is irreducible,  the situation is simplified since every space has dimension one. 
In what follows, we  give information on the irreducible imprimitive groups that may occur as difference Galois groups when the order $n$ of the system \eqref{eq:diffcesystembase} is prime (see Theorem \ref{thm1}). Moreover, $\det(G)$ indicates which one of this information correspond to the Galois group $G$  (see Proposition~\ref{prop:detDistinguish}). More precisely, Theorem \ref{thm1} and Proposition~\ref{prop:detDistinguish} imply the following result.

\begin{thm}\label{thmimpr}
Assume that $n$ is a prime number.  Let $G \subset \mathrm{GL}_n (C)$ be an imprimitive irreducible group such that $G/G^{0}$ is finite and cyclic. 
\begin{enumerate}
 \item If $\det(G) = C^*$ then $G^0\sim (C^*)^n$ and  
$G/G^0 \sim  \Z/ n \Z$.
 \item If $\det(G)=\Z/  \nu \Z$ then ${G^0\sim (C^*)^{n-1}}$ and
$G/G^0 \sim  \Z/ ns \Z$  where
 $$s = \left\lbrace \begin{array}{ll}
      \nu/n & \text{ if }  \nu \in n\N^* \\
     \nu & \text{ otherwise. }
 \end{array}\right.$$
\end{enumerate}
\end{thm}

At the end of this section, we explain how to compute a reduced form and a gauge transformation which gives this reduced form (see Proposition \ref{prop2}). \par 


\subsubsection{Imprimitive groups that may occur}
 
 Let us now describe the possible irreducible imprimitive groups that may occur as difference Galois groups when $n$ is prime.  Let us begin by an elementary lemma that will be used several times. Note that the assumption $n$ prime is not required for this lemma.
 
\begin{lem}
\label{lem:irred_primitive_G}
Let $G \subset \mathrm{GL}_n (C)$ be an irreducible group and let $H\triangleleft G$ be such that $G/H$ is finite and cyclic. Then, $H$ is not composed only of dilatations.
\end{lem}

\begin{proof}
By contradiction, assume that $H$ is composed only of dilatations. Since $G/H$ is finite and cyclic,  there exists a matrix $\mathscr{F}$ such that $G=H\cup H \mathscr{F} \cup\dots  \cup H \mathscr{F}^{m-1}$ for some positive integer $m$.  The matrix $\mathscr{F}$ is triangularisable and since $H$ is formed by dilatations,  it implies that there is a common basis of triangularisation of every elements of $G$, which contradicts the fact that $G$ is irreducible.
\end{proof}

 
For $(\alpha_{1},\dots, \alpha_n)\in (C^*)^n$, let $$E_n (\alpha_{1},\dots, \alpha_n):=\begin{pmatrix}
& \alpha_1&&\\ 
 &  &\ddots & \\
&&&\alpha_{n-1}\\
\alpha_n&&&
\end{pmatrix}=
\mathrm{Diag} (\alpha_{1},\dots, \alpha_n)E_n, $$
where
$E_n=\begin{pmatrix}
& 1&&\\ 
 &  &\ddots & \\
&&&1\\
1&&&
\end{pmatrix}$ is the companion matrix with last row  $(1,0,\dots,0)$. To lighten the notations, we will denote it $E$. For $(\alpha_{1},\dots, \alpha_n)\in (C^*)^n$, let $\bar{\alpha}:=(\alpha_{1},\dots, \alpha_n)$ and let $\Pi\bar{\alpha} :=\prod_{i=1}^{n}\alpha_{i}$.  Note that $\left(E_n (\alpha_{1},\dots, \alpha_n)\right)^n=(\Pi \bar{\alpha} )\mathrm{Id}_n$. Let $\mathcal{M}_\ell$ be the set of invertible matrices of the form $\mathrm{Diag} (\alpha_{1},\dots, \alpha_n)E^{\ell}$.  Note that $\mathcal{M}_0$ is composed of diagonal matrices. The following theorem gives information on the possible groups that may occur as Galois groups. 


\begin{thm}\label{thm1}
Assume that $n$ is a prime number.  Let $G \subset \mathrm{GL}_n (C)$ be an imprimitive irreducible group such that $G/G^{0}$ is finite and cyclic. Then, up to a conjugation,  one of the following holds:
\begin{enumerate}
 \item\label{cas1} $G= \displaystyle \bigcup_{\ell=0}^{n-1} \mathcal{M}_{\ell}$. In that case $G^0\sim (C^*)^n$,  
$G/G^0 \sim  \Z/ n \Z$  and $\det(G)=C^*$.
 \item\label{cas2} There exists a positive integer $s$ such that 
 $$G\cap \mathcal{M}_0= \left\{\mathrm{Diag}(\alpha_{1},\dots, \alpha_n)\mid  (\Pi\overline{\alpha})^{s}=1\right\}$$ and there exists $\mathscr{M}$ of the form $E_n\left(\alpha_{1},\dots, \alpha_n\right)$, where $\Pi \overline{\alpha}=e^{2\mathbf{i}\pi k/(ns)}$ with $\gcd (k,s)=1$, such that $G/G^0$ is generated by $\mathscr{M}$.  In that case,  we find  that 
 ${G^0=  \left\{\mathrm{Diag}(\alpha_{1},\dots, \alpha_n)\mid \Pi\overline{\alpha}=1\right\}\sim (C^*)^{n-1}}$, 
$G/G^0 \sim  \Z/ ns \Z$  and 
 \begin{enumerate}
\item\label{cas21}   if $n=2$ then  $\det(G)=\Z/  (2s/\gcd(k+s,2)) \Z$;
\item\label{cas22}  if $n> 2$ then   $\det(G)=\Z/  (ns/\gcd(k,n)) \Z$.
 \end{enumerate}
\end{enumerate}
\end{thm}

\begin{proof}
Up to a conjugation, $G$ is a subgroup of $ \displaystyle \bigcup_{\ell=1}^{n} \mathcal{M}_{\ell}$. 
Since $G$ is irreducible, it contains a nondiagonal element thus there exists $0<\ell<n$ such that $G$ contains an element of $\mathcal{M}_{\ell}$.  Using that $G$ is a group, $G$ contains an element of $\mathcal{M}_{k\ell}$ for all $k\in\mathbb{Z}$. Since $n$ is prime,   for all $0\leq k'<n$, there exists an integer $k$ such that $k\ell= k' \mod n$. This shows that $G$ contains an element of $\mathcal{M}_{k'}$, for all $0\leq k' <n$. 
Let $\mathcal{D}$ be the diagonal elements of $G$.  It induces an algebraic subgroup of $n$ copies of the multiplicative group.  

Assume first that $\mathcal{D}$ is equal to the group of invertible diagonal matrices.  Since the latter is connected,   $G^0=\mathcal{D}$. 
Thus, $G$ contains all the invertible diagonal elements. Since $G$ contains an element of $\mathcal{M}_{k'}$ for all $0\leq k' <n$ and contains $\mathcal{M}_0$ it follows that $G= \displaystyle \bigcup_{\ell=0}^{n-1} \mathcal{M}_{\ell}$.  This is the first case. 

\medskip
 
Assume now that $\mathcal{D}$ is strictly included in the group of invertible diagonal matrices. Since $G\subset  \displaystyle \bigcup_{\ell=1}^{n} \mathcal{M}_{\ell}$, we have $G^0\subset \mathcal{D}$. There exists $\bn:=(s_1,\dots s_n)\in\mathbb{Z}^n$, where the $s_i$ are not all zero, such that the diagonal matrices $\mathrm{Diag}(\alpha_{1},\dots, \alpha_n)$ in $G$ satisfy $\prod\limits_{j=1}^n \alpha_j^{s_j}=1$.   We have $\sum_{j=1}^{n}s_j \ln(|\alpha_j|)=0$. 

Consider a matrix $P:=E_n\left(\beta_1,\ldots, \beta_n\right)\in \mathcal{M}_1\cap G\, .$
We have 
$$P .\text{Diag}\left(\alpha_n,\alpha_1,\alpha_{2},\ldots, \alpha_{n-1} \right) = \text{Diag}\left(\alpha_1,\alpha_{2},\ldots, \alpha_{n} \right).P\, .$$
Therefore, if $\text{Diag}\left(\alpha_1,\alpha_{2},\ldots, \alpha_{n} \right)\in G$ then $\text{Diag}\left(\alpha_n,\alpha_1,\alpha_{2},\ldots, \alpha_{n-1} \right)\in G$.
Iterating this computation,  we obtain that the nonzero vector $\mathfrak{X}=( \ln(|\alpha_{1}|),\dots,  \ln(|\alpha_{n}|))^t$ is a solution of 
$$B\mathfrak{X}=0, \quad  \hbox{ where} \quad B=\begin{pmatrix}
s_1&s_2 &\cdots &s_n\\ 
s_n &s_1  &\ddots &\vdots \\
\vdots &\ddots & \ddots & s_2\\
s_{2}&\cdots & s_n &s_{1}
\end{pmatrix}.$$
Note that $B= \sum_{\ell=0}^{n-1} s_{\ell+1} E^{\ell}$ is a circulant matrix.  Since   $E^n$ is the identity, $E$ is diagonalisable with eigenvectors $\mathfrak{X}_k=(1, e^{2\mathbf{i}k\pi/n}, \dots, e^{2\mathbf{i}k(n-1)\pi/n} )^t$, $0\leq k\leq n-1$, and its eigenvalues are the $n$th roots of unity:
$$
E\mathfrak{X}_k = e^{2\mathbf{i}k\pi/n}\mathfrak{X}_k\, .
$$
These eigenvectors are also eigenvectors for every polynomial in $E$,  in particular they are eigenvectors of $B$.
Since $E$ is diagonalisable, there exists $P\in\GL_n(C)$  such that $E=PD_0 P^{-1}$, where $D_0 =\mathrm{Diag}(1,e^{2\mathbf{i}\pi/n},\dots,e^{2\mathbf{i}(n-1)\pi/n})$ is a diagonal matrix. 
Since $B\mathfrak{X}=0$ and $P^{-1}BP=\sum_{\ell=0}^{n-1} s_{\ell+1} D_0^{\ell}$, the diagonal matrix $\sum_{\ell=0}^{n-1} s_{\ell+1} D_0^{\ell}$ has a nontrivial kernel, that is, one of its diagonal entries is zero: there exists $0\leq k_0 \leq n-1$ such that  $\sum_{\ell=0}^{n-1} s_{\ell+1} e^{2\mathbf{i}\ell k_0\pi/n}=0$. 
The $n$th roots of unity satisfy $z^n=1$ and we have $z^n -1=(z-1)\Phi_n(z)$ where $\Phi_n(z):=1+z+\dots +z^{n-1}$.  Because $n$ is prime, the cyclotomic polynomial $\Phi_n$ is irreducible on $\mathbb{Z}$.   If $k_0>0$, then we must have $s:=s_1=\dots=s_n\neq 0$. Let us prove by contradiction that we work in the case $k_0\neq 0$.  

By contradiction, assume that  $k_0=0$.  Then,  $\sum_{\ell=0}^{n-1} s_{\ell+1}=0$.  Recall that the $s_i$ are not all zero.  In particular,  we cannot be in the situation where $s_1=\dots=s_n$. From what precedes,  this implies that for all  $k\neq0$  we have $\mathfrak{X}_k\notin\ker(B)$.  Thus, $\ker(B)=\mathrm{Vect}(\mathfrak{X}_0)$ and in particular $\mathfrak{X}\in \mathrm{Vect}(\mathfrak{X}_0)$, that is $\ln(|\alpha_{1}|)=\dots=\ln(|\alpha_{n}|)$. We obtain 
\begin{equation}
\label{eq:mod}
|\alpha_1|=\ldots = |\alpha_n|\, .    
\end{equation}  Let $g:=\gcd(s_1,\ldots,s_n)$, $s_i':=\frac{s_i}{g}$ and $\beta_i := \alpha_i^g$ for $i\in \lbrace 1,\ldots, n\rbrace$. Since $\prod\limits_{j=1}^n \alpha_j^{s_j}=1$, we have $\prod\limits_{j=1}^n \beta_j^{s_j'}=1$. Thus,  there exists $\ell_0\in\mathbb Z$ such that $\sum_{j=1}^{n}s_j' \arg(\beta_j) = 2\pi \ell_0$. Moreover, since $\gcd(s_1',\ldots,s_n') = 1$, by the Bézout's identity, there exist $u_1,\ldots, u_n\in\mathbb{Z}$ such that  $\sum_{j=1}^{n}u_js_j' = 1$.  We can replace $\arg(\beta_j)$ with $\arg(\beta_j) - 2\pi u_j\ell_0$ (new choices for the determinations of arguments), also called $\arg(\beta_j)$ to lighten notations. With these new choices, $\sum_{j=1}^{n}s_j' \arg(\beta_j) = 0$. Thus $\mathfrak{Y}:=(\arg(\beta_1),\ldots,\arg(\beta_n))^t$ satisfies $B\mathfrak{Y}=0$. As before (with $\mathfrak Y$ instead of $\mathfrak X$), we obtain 
\begin{equation}
\label{eq:arg}
\arg(\beta_1)=\ldots=\arg(\beta_n)\, .    
\end{equation} 
From \eqref{eq:mod} and \eqref{eq:arg}, we have
$
\alpha_1^g = \ldots = \alpha_n^g \, .
$
 Thus, in that case, there exists $g\in \mathbb{N}^*$ such that $\mathcal{D}\subset \lbrace \mathrm{Diag}(\alpha_1,\ldots,\alpha_n) \in\GL_n\left( C\right)\mid \alpha_1^g = \ldots = \alpha_n^g\rbrace$. Let us prove that  the connected component of the identity of $\mathcal{D}$ is composed by dilatations.  Indeed,  with the equality $\alpha_1^g-\alpha_j^g=(\alpha_1-\alpha_j)(\alpha_1^{g-1}+\alpha_1^{g-2}\alpha_j + ... + \alpha_1 \alpha_j^{g-2}+ \alpha_j^{g-1})=0$, we find that $\lbrace \mathrm{Diag}(\alpha_1,\ldots,\alpha_n) \in\GL_n\left( C\right)\mid \alpha_1^g = \ldots = \alpha_n^g\rbrace$ contains the closed set $\alpha_1=\ldots = \alpha_n$. The latter is composed by dilatations matrices and contains  the connected component of the identity. This implies that the elements of $G^0$ are dilatations, which is a contradiction because of Lemma \ref{lem:irred_primitive_G} (with $H:=G^0$ in this lemma).  Therefore, $k_0>0$ so we must have $s:=s_1=\dots=s_n\neq 0$.
\color{black}

We proved that $\mathcal{D}\subset \mathcal{D}_s:=\lbrace \mathrm{Diag}(\alpha_{1},\dots, \alpha_n)\mid (\Pi \overline{\alpha})^{s}=1\rbrace$ and, since $\mathcal{D}_{s}=\mathcal{D}_{-s}$, we can assume that $s$ is positive. If $\mathcal{D}$ is a strict subgroup of $\mathcal{D}_s$, the same reasoning implies that $\mathcal{D}\subset \mathcal{D}_{s'}$ for some $s'$ that divides $s$. So, up to taking a smaller positive integer $s$, we may assume that $\mathcal{D}= \mathcal{D}_s$.
In this case, $G^0=\mathcal{D}_1$.  
 
Let $\mathscr{F}:=\mathrm{Diag} (\alpha_{1},\dots, \alpha_n)E^{\ell}\in \mathcal{M}_{\ell}\cap G$ be a non diagonal element of $G$ which generates the finite group $G/G^0$ (we can choose in particular $0<\ell<n$). Since $n$ is prime, $n$ is the smallest integer such that $\mathscr{F}^n$ is diagonal. We have $\mathscr{F}^n = \mathrm{Diag} (\Pi \baralp ,\dots, \Pi \baralp)$ thus it satisfies $(\Pi \baralp)^{sn}=1$. We have $\Pi \baralp=e^{2\mathbf{i}\pi k/sn}$ for some integer $0\leq k<sn$ and $\mathscr{F}^n$ has to generate the diagonal elements of $G$. This shows that $(\Pi \baralp)^n$ has to be a primitive $s$th root of unity, that is, $k$ has to be coprime with $s$. Since $G$ is defined up to an isomorphism and since $\mathscr{F}$ is conjugate to $\mathrm{Diag} (\alpha_{\mu(1)},\dots, \alpha_{\mu(n)})E$ where $\mu\in\mathfrak{S}_n$ is a permutation, we can assume (up to renumbering the $\alpha_i$'s, which can be done since we just have conditions on $\Pi \baralp$) that $\mathscr{F} = \mathrm{Diag} (\alpha_{1},\dots, \alpha_n)E = E_n\left(\alpha_{1},\dots, \alpha_n\right)$.\par 
The determinant of the diagonal elements is a power of $e^{2\mathbf{i}\pi/s}$. When $n>2$, $n$ is odd and the determinant of $\mathscr{F}$ is $e^{2\mathbf{i}\pi k/sn}$. When $n=2$ the determinant of $\mathscr{F}$ is  $-e^{2\mathbf{i}\pi k/2s}=e^{2\mathbf{i}\pi (k+s)/2s}$.   
The results on the determinant  follow.
\end{proof}


\begin{rem}
When $n=2$, we recover \cite[Lemma 4.8]{hendriks1998algorithm}.
\end{rem}

Let us now see how $\det(G)$ helps us to distinguish the cases in Theorem \ref{thm1} and compute~$s$. We will explain how to compute $\det(G)$ in Section \ref{secorder1}. 

\begin{prop}
\label{prop:detDistinguish}
Assume that $n$ is prime.  Let $G \subset \mathrm{GL}_n (C)$ be an imprimitive irreducible group such that $G/G^{0}$ is finite and cyclic.  The following statements holds.
\begin{itemize}
\item  $\det(G)=C^*$ if and only if  $G$ is the group  in the case \ref{cas1} of Theorem \ref{thm1}.   
\item If  $\det(G)=\Z/  \nu \Z$, with $\nu \in n\N^*$,  then $s=\nu/n$. where $s$ is defined in  Theorem~\ref{thm1}.
\item Otherwise,  $s=\nu$. 
\end{itemize}
\end{prop}

\begin{proof}
If $\det(G)=C^*$ we are clearly in the case case \ref{cas1} of Theorem \ref{thm1}.  The converse is also true.  
 \par 
 Assume that $n\neq 2$, thus by Theorem \ref{thm1},  $\det(G)=\Z/  (sn/\gcd(k,n)) \Z$.  We know the integers $n$, $\nu:=(sn/\gcd(k,n))$  and we want to compute $s$. 
Note that, since $n$ is prime,  $\nu=sn/\gcd(k,n)$ is either $sn$ or $s$.  Let us prove that $\nu=s$ if and only if  $\gcd(\nu,n)=1$.    If $\nu=s$ then $\gcd(k,n)=n$ and, since  $k$ is coprime with $s$,  this implies $\gcd(n,s)=1$, that is $\gcd(\nu,n)=1$. Obviously, if $\nu=sn$ then $\gcd(\nu,n)=n$.  
Therefore, either $\gcd(\nu,n)=1$ and $s=\nu$ or $\gcd(\nu,n)=n$ and $s=\nu/n$. \par 
In the case $n=2$, $k$ is replaced by $k+s$.  Note that $k+s$ is coprime with $s$ and the same conclusion holds.  
\end{proof}


\subsubsection{How to compute a reduced form?}

First, we prove a result which is useful in what follows.

\begin{prop}
\label{prop:irred_primitive}
    Let $n$ be a prime number and let $H\subset\GL_n(C)$ be an irreducible group. Assume that $K$ is not composed only of dilatations and $K\triangleleft H$. If $H$ is a primitive group, then $K$ is an irreducible group.
\end{prop}

\begin{proof}
Let us prove by contradiction the irreducibility of $K$. If $K$ is not irreducible, there exists a vector space $V\subsetneq C^n$ of minimal dimension $\nu>0$ such that $K(V)=V$.  
We denote by $V_1,\dots, V_k$  vector subspaces of $C^n$ in direct sum such that $\nu=\dim(V_j)$ and $K(V_j)=V_j$.  We then have $V_1\oplus \dots \oplus V_k\subset C^n$. Thereofore $\nu k< n$ and $k$ is bounded. Then, without loss of generalities we may assume that $k$ is maximal, meaning that for all $V'\subset C^n$, with $\dim (V')=\nu$ and $K(V')=V'$, $V'$ is not in direct sum with $V_1\oplus \dots \oplus V_k$.

We claim that  $V_1\oplus \dots \oplus V_k =C^n$.  To the contrary, assume that $V_1\oplus \dots \oplus V_k \subsetneq C^n$. By irreducibility of $H$, there exist $\mathscr{H}\in H$ and $\ell\in\lbrace 1,\ldots,k\rbrace$ such that $Y:=\mathscr{H}(V_\ell)$, whose dimension is $\nu$, is not included in $V_1\oplus \dots \oplus V_k$. Since $K$ is a normal subgroup of $H$, $K\mathscr{H}=\mathscr{H}K$. In particular, $KY=Y$ so $Y$ is stable under $K$.  
Since $Y\cap (V_1\oplus \dots \oplus V_k)$ is stable under $K$, by minimality of the dimension $\nu$, it follows that the dimension of $Y\cap (V_1\oplus \dots \oplus V_k)$ is either $0$ or $\nu$. In the first case, this proves that $Y$ is in direct sum with $V_1\oplus \dots \oplus V_k$ and, in 
the second case, this proves that $Y \subset V_1\oplus \dots \oplus V_k$. In both situations this is a contradiction thus $V_1\oplus \dots \oplus V_k= C^n$. Hence $\nu k=n$ and, since $n$ is prime, we have $k=n$ and $\nu=1$. 
At this stage, we know that $V_1\oplus \dots \oplus V_n= C^n$ with $\dim(V_j)=1$ and $K(V_j)=V_j$ for all $j\in\lbrace 1,\ldots,n\rbrace$. This implies that $K$ is composed of diagonal matrices in a basis $\mathcal{B}$ induced by $V_1,\ldots,V_n$. 

Let us prove by contradiction that the common eigenspaces of the matrices in $K$ must have the same dimension. Indeed, 
if it is not the case and if $W_1,\ldots,W_\ell$ are the eigenspaces of $K$ of maximal dimension, then we have $W:=W_1\oplus\ldots\oplus W_\ell\subsetneq C^n$ (it is not $C^n$ because we assume that there exists at least an eigenspace which has an another dimension). Since $K(W_i)=W_i$  for all $i\in\lbrace 1,\ldots,n\rbrace$ and  $K\mathscr{H}=\mathscr{H}K$ for all $\mathscr{H}\in H$, we have $K(\mathscr{H}(W_i))=\mathscr{H}(W_i)$. Thus, by maximality of $\dim(W_i)=\dim(\mathscr{H}(W_i))$, $\mathscr{H}(W_i)$ is a common eigenspace of the matrices in $K$, that is $\mathscr{H}(W_i)=W_j$ for a certain $j$. Hence  $\mathscr{H}(W_i)\subset W$, which proves that $H(W)\subset W$ (and taking the dimension, we have $H(W)=W$), in contradiction with the irreducibility of $H$. 

We proved that the matrices in $K$ are diagonal and we see that the common eigenspaces of the matrices in $K$ have the same dimension. Since, the direct sum of these eigenspaces is $C^n$, this dimension must divides $n$, which is a prime number. Thus, this dimension is $1$ or $n$. In the second case, it means that the matrices in $K$ are dilatations, a contradiction with a hypothesis on $K$. In the first case, the eigenspaces are $V_1,\ldots,V_n$. As before, if $\mathscr{H}\in H$, for all $i\in\lbrace 1,\ldots,n\rbrace$, we have $K(\mathscr{H}(V_i))=\mathscr{H}(V_i)$. Thus, $\mathscr{H}(V_i)$, whose  dimension is $1$, is included in an eigenspace of $K$ so  $\mathscr{H}(V_i)=V_j$ for a $j\in\lbrace 1,\ldots,n\rbrace$. We obtain in this case that any element of $H$ induces a permutation between the $V_i$, which contradicts the fact that $H$ is primitive. In both situations, we obtain a contradiction. Finally, $K$ is irreducible. 
\end{proof}





The rest of the subsection is devoted to the computation of the reduced form.
We recall that $A_{[\ell]}:=\phi^{\ell-1}(A)\dots A$ and $G_{[\ell]}$ is the difference Galois group of the system $\phi^{\ell}(Y)=A_{[\ell]}Y$.  Let us first give a criterion of imprimitivity.

  \begin{prop}\label{prop1}
 Assume that $G$ is irreducible and $n$ prime.  It is imprimitive if and only if $G_{[n]}$ is  diagonal. \par 
 Furthermore,  when   $G$ is imprimitive,   the Riccati equation corresponding to $\phi^n (Y)=A_{[n]}Y$ admits a solution    $d\in \k^*$ and we may assume that the $(1,1)$ entry of $A_{[n]}$ is $d$.  
 \end{prop} 
 
 \begin{proof}
 If $G$ is imprimitive but irreducible,  there exists a gauge transformation $T$ such that $B:=\phi(T)AT^{-1}$ is an invertible matrix of the form  $\begin{pmatrix}
& b_1&&\\ 
 &  &\ddots & \\
&&&b_{n-1}\\
b_{n}&&&
\end{pmatrix}$, where $b_i\in \mathbf{k}^*$,  and  such that $[B]$ is in reduced form.  Then,  $\phi^{n}(T)A_{[n]}T^{-1}=\phi^{n-1}(B)\dots \phi(B)B=:B_{[n]}$ is diagonal.   By Theorem \ref{theo:reduced form}, 
this proves that the Galois group of $\phi^{n}(Y)=A_{[n]}Y$ is  diagonal. \par 
    Let us prove the converse.   Assume that the Galois group of $\phi^{n}(Y)=A_{[n]}Y$ is  diagonal,  and $G$ is irreducible.  Consider  a basis of $C^n$ such that the matrices of  $G_{[n]}$ are diagonal. Then, from Lemma \ref{lem2},   $G^0 =G_{[n]}^0$ thus $G^0$ is  diagonal.  Let us prove that $G$ is imprimitive. 
From Lemma \ref{lem:irred_primitive_G} (where $H:=G^0$), the group $G^0$ is not composed only of dilatations. Thus, by Proposition \ref{prop:irred_primitive} (applied to $H:=G$ and $K:=G^0$), if $G$ is a primitive group then $G^0$ is irreducible, which contradicts the fact that $G^0$ is diagonal. Thus, $G$ is imprimitive. 
 
The statement on the Riccati equation is a consequence of Remark~\ref{rem:rightFactorOrder1}.
\end{proof}


Assume that $G$ is irreducible,  imprimitive and $n$ is prime.  By Proposition  \ref{prop1}, the Riccati equation corresponding to $\phi^n (Y)=A_{[n]}Y$ admits a solution    $d\in \k^*$.   Assume that we are able to compute a reduced form of $\phi(y)=dy$, that is compute $f\in \k^*$ such that $\phi(y)=d\frac{\phi(f)}{f}y$ is reduced. The goal of what follows is to prove the following result.

\begin{prop}\label{prop2}
 Assume that $G$ is irreducible, imprimitive  and $n$ prime. The system $\phi(Y)=AY$ is equivalent to $\phi(Y)=E_n (1,\dots, 1, d)Y$. 
The system $\phi(Y)=E_n (1,\dots, 1,f^{-1}, \phi(f)d)Y$ is a reduced form of $\phi(Y)=E_n (1,\dots, 1, d)Y$ with reduction matrix $\mathrm{Diag}(1,\ldots,1,f)$.
\end{prop}

Let us begin by proving a technical lemma. 
\begin{lem}\label{lem5}
 Assume that $G$ is irreducible, imprimitive  and $n$ prime.  Then, there exist $T\in \mathrm{GL}_n (\mathbf{k})$ and $u\in \mathbf{k}^*$ such that $\phi(T)AT^{-1}=\begin{pmatrix}
& 1&&\\ 
 &  &\ddots & \\
&&&1\\
u&&&
\end{pmatrix}$, that is, $\phi(T)AT^{-1}=E_n(1,\ldots,1,u)$. 
\end{lem}

\begin{proof}
This is inspired by \cite[Section 4.2]{hendriks1998algorithm}. By Theorem \ref{theo:reduced form}, there exist $T\in \mathrm{GL}_n (\mathbf{k})$ and $u_1,\dots,  u_n \in \mathbf{k}^*$  such that 
$\phi(T)AT^{-1}=E_n(u_2,\ldots,u_n,u_1)$.
Let $D:=\mathrm{Diag}\left(a_1,\ldots,a_n\right)$.
We have the following equality 
$$
\phi(D)E_n(u_2,\ldots,u_n,u_1)D^{-1} = E_n\left(\frac{\phi(a_1) u_2}{a_2},\ldots,\frac{\phi(a_{n-1}) u_n}{a_n},\frac{\phi(a_n) u_1}{a_1}\right)\, .
$$


If we perform the gauge transformation $D:=\mathrm{Diag}(1,u_2,1,\ldots,1)$, we may reduce to the case $u_2=1$. Then,  if $n>2$,  performing the gauge transformation $D:=\mathrm{Diag}(1,1,\phi(u_2)u_3,1,\ldots,1)$, we may reduce to the case $u_3=1$. Iterating this process  allows at the end to reduce to the case $u_2= \dots=u_n=1$ and we change $u_1$ to $u:=u_1\phi(u_n)\phi^2(u_{n-1})\ldots\phi^{n-1}(u_2)$.
\end{proof}


Let us continue the proof of Propositon \ref{prop2}. 
By the previous lemma, we have that $[A]$ is equivalent to $E_n(1,\ldots,1,u)$, therefore $\phi^n(Y)=A_{[n]}Y$ is equivalent to $\phi^n(Y)=\mathrm{Diag}(u,\phi(u),\dots,  \phi^{n-1} u)Y$.  Unfortunately, we are not yet able to compute $u$.   By Proposition \ref{prop1},  there exists 
 a diagonal system  $\phi^n (Y)=DY$, that is  equivalent to $\phi^n (Y)=A_{[n]}Y$ with $(1,1)$ entry $d$. 
 We write 
$$
D:=\mathrm{Diag}(d_1,d_2,d_3,\ldots,d_n)
$$
where we set $d_1:=d$.  Let us now see that we may reduce to the case where $d_i=\phi^{i-1-i_1}(d)$ for an integer $i_1\in\lbrace 1,\ldots,n\rbrace$. 
\begin{lem}
There exists a  gauge transformation $X$ and an integer $i_1\in\lbrace 1,\ldots,n\rbrace$ such that 
\begin{equation}
\label{eq:findX}
   \phi^n(X)D X^{-1} = \mathrm{Diag}(\phi^{-i_1}(d),\ldots,\phi^{n-1-i_1}(d))\, . 
\end{equation}
\end{lem}

\begin{proof}
Note that there exists  an invertible matrix $Z$ such that   $\phi^n (Z)DZ^{-1}=\mathrm{Diag}(u,\phi(u),\dots,  \phi^{n-1} u)$. 
Let $Z_{i,j}$ be the entries of $Z$. Since $Z$ is invertible, for all $j$ there exists $i_j\in\lbrace 1, \ldots,n\rbrace$ such that $Z_{i_j,j}\neq 0$. We can moreover assume that the $i_j$ are distinct. Taking the $(i_j,j)$-coefficient in $\phi^n (Z)D=\mathrm{Diag}(u,\phi(u),\dots,  \phi^{n-1} (u))Z$ yields $\phi^n  (Z_{i_j,j})d_j=\phi^{i_j-1}(u)Z_{i_j,j}$. Thus, for all $j\in\lbrace 1,\ldots, n\rbrace$, there exist $i_j\in\lbrace 1,\ldots, n\rbrace$ and $f_j\in\k^*$ such that 
\begin{equation}
    \label{eq:d}
    \phi^n(f_j)d_j = \phi^{i_j-1}(u)f_j\, .
\end{equation}
 For $j=1$ in \eqref{eq:d}, we have $\phi^{i_1-1}(u) = \frac{\phi^n(f_1)d_1}{f_1}$ thus $\phi^{i_j-1}(u) = \frac{\phi^n(\phi^{i_j-i_1}(f_1))\phi^{i_j-i_1}(d_1)}{\phi^{i_j-i_1}(f_1)}$. Therefore, from \eqref{eq:d}, setting $g_j:= \frac{f_j}{\phi^{i_j-i_1}(f_1)}$,  we obtain
 $$
 \phi^n(g_j)d_j= \frac{\phi^n (f_j)d_j}{\phi^n(\phi^{i_j-i_1}(f_1))}= \frac{ \phi^{i_j-1}(u)f_j}{\phi^n(\phi^{i_j-i_1}(f_1))}=  \phi^{i_j-i_1}(d_1)g_j.
 $$ 
Applying $\phi^{i_1}$ to this equality, we proved that there exists an invertible diagonal matrix $Z_0$ and distinct integers $i_1,\ldots,i_n\in\lbrace 1,\ldots,n\rbrace$ such that 
$$
\phi^n(Z_0)\phi^{i_1}(D)Z_0^{-1} = \mathrm{Diag}(\phi^{i_1}(d_1) ,\dots,  \phi^{i_n}(d_1))\, . 
$$
Thus there exists a permutation matrix $Z_1$ such that 
$$
\phi^n(Y)\phi^{i_1}(D) Y^{-1} = \mathrm{Diag}(d,\ldots,\phi^{n-1}(d))\quad \text{with } Y:=Z_1Z_0\, .
$$
 Thus,
$$
\phi^n(X)D X^{-1} = \mathrm{Diag}(\phi^{-i_1}(d),\ldots,\phi^{n-1-i_1}(d))\quad \text{where }X:=\phi^{-i_1}(Y)\, .
$$
\end{proof}

Thus, at this stage, we know  the existence of $i_1\in\lbrace 1,\ldots,n\rbrace$  such that   $\phi^n (Y)=A_{[n]}Y$ is equivalent to 
$$
\phi^n(Y)=\mathrm{Diag}(\phi^{-i_1}(d),\phi^{1-i_1}(d),\ldots,  \phi^{n-1-i_1}(d))Y\, .
$$
Since the system 
$
\phi^n(Y)=\mathrm{Diag}(\phi^{-i_1}(d),\phi^{1-i_1}(d),\ldots,  \phi^{n-1-i_1}(d))Y
$ is diagonal, we may assume that we have a diagonal fundamental matrix of solutions $U$. This matrix can be taken of the form $U=\mathrm{Diag}(y,\phi(y),\dots,  \phi^{n-1}(y))$. Then, 
$$
\phi(U)=FU, \quad \text{where}\quad F:=\begin{pmatrix}
& 1&&\\ 
 &  &\ddots & \\
&&&1 \\
\phi^{-i_1}(d)&&&
\end{pmatrix}=E_n (1,\dots, 1, \phi^{-i_1}(d))\, .
$$
By construction, 
$F_{[n]} = \mathrm{Diag}(\phi^{-i_1}(d),\phi^{1-i_1}(d),\ldots,\phi^{n-1-i_1}(d))$. We thus have two $\phi^n$- systems $\phi^n(Y) = A_{[n]}Y$ and $\phi^n(Y) = F_{[n]}Y$, that are equivalent and we want to prove that they are equivalent as $\phi$-system. This is the goal of the next lemma. 

\begin{lem}
\label{lem:gaugeTransfoEquiv}
Let $F\in\GL_n(\k)$ be such that the systems $\phi^n(Y) = F_{[n]}Y$ and $\phi^n(Y) = A_{[n]}Y$ are equivalent. 
Then, the systems $[A]$ and $[F]$ are equivalent.
\end{lem}

\begin{proof}
Let $\mathcal{Y}$ and $\mathcal{Z}$ be two fundamental matrices of solutions of $\phi(Y)=AY$ and $\phi(Y)=FY$ respectively. 
Thus, $\phi^n(\mathcal{Y})=A_{[n]}\mathcal{Y}$ and $\phi^n(\mathcal{Z})=F_{[n]}\mathcal{Z}$. By hypothesis,  there exists $T\in\GL_n(\k)$ such that $\mathcal{X}:=T\mathcal{Y}$ is a solution of $\phi^n(Y)=F_{[n]}Y$.
This implies that  $P:=\mathcal{X}^{-1}\mathcal{Z}$ is a $\phi^n$-constant  matrix.  By \cite[Lemma 3.1]{DH21}, the entries of $P$ belong to $C$ so we have 
$$
A = \phi(\mathcal{Y})\mathcal{Y}^{-1} = \phi(T^{-1}) \phi(\mathcal{X})\mathcal{X}^{-1}T= \phi(T^{-1}) \phi(\mathcal{Z})\mathcal{Z}^{-1} T =\phi(T)^{-1} FT .
$$
\end{proof}

Let us finish the proof of Proposition \ref{prop2}.  From what precedes,   $[A]$ is equivalent to $[F]$ where 
$F=E_n (1,\dots, 1, \phi^{-i_1}(d))$. Using the following lemma and the fact that $\phi(1)=1$, we obtain that this system is equivalent to $[J]$, where $J:=E_n (1,\dots, 1, d)$.

\begin{lem}
Let $J\in \GL_n(\k)$ and $\ell\in\mathbb{N}$. The systems $[\phi^{\ell}(J)]$ and $[\phi^{\ell +1}(J)]$ are equivalent.
\end{lem}
\begin{proof}
    It follows from the fact that $\phi^{\ell+1}(J) = \phi(X)\phi^{\ell}(J) X^{-1}$ with $X:=\phi^{\ell}(J)$.
\end{proof}

Thus, we have that $[A]$ and $[J]$ are equivalent systems. 
Now, we perform the gauge transformation $S=\mathrm{Diag}(1,\ldots,1,f)$ to find that $[A]$ is equivalent to $\phi(Y)=E_n (1,\dots, 1,f^{-1}, d\phi(f))Y$.  It remains to check that this system is in a reduced form.  


By Theorem \ref{theo:reduced form},  there exists a reduction matrix of the form 
 $T:= \mathrm{Diag}(f_1,\dots, f_n)E^k$.  Note that $T$ may be the identity.  We are going to apply Theorem \ref{thm1} and look at the product of the nonzero entries of  $B:=\phi(T)E_n (1,\dots, 1,f^{-1}, d\phi(f))T^{-1}$. The latter  is $\frac{\phi(f_1\times \dots \times f_n) }{f_1\times \dots \times f_n}\frac{\phi(f)}{f}d$.  Since $\phi y=\frac{\phi(f)}{f}dy$ is in reduced form,  the algebraic group generated by $\frac{\phi(f_1\times \dots \times f_n) }{f_1\times \dots \times f_n}\frac{\phi(f)}{f}d$ is bigger than the algebraic group generated by $\frac{\phi(f)}{f}d$. Since $[B]$ is reduced, by Theorem~\ref{theo:reduced form},  it is also smaller, proving that the algebraic group generated by $\frac{\phi(f_1\times \dots \times f_n) }{f_1\times \dots \times f_n}\frac{\phi(f)}{f}d$ is the algebraic group generated by $\frac{\phi(f)}{f}d$.  By Theorem \ref{theo:reduced form} again, this shows that $\phi(Y)=E_n (1,\dots, 1,f^{-1}, d\phi(f))Y$ is already reduced.

\begin{ex}\label{ex2}
Let us go back to the example \eqref{eq0} and recall, see Example \ref{ex1}, that the difference Galois group $G$ is irreducible. Assume that $t\neq 0$. Instead of applying the criterion of Proposition~\ref{prop1} to show that $G$ is imprimitive,  let us use a shortcut.  We refer to \cite[Section 2.2]{ramis2013local} for more details on what follows. 
We define the Newton polygon of a $q$-difference operator 
$L=\sum_i a_{i} \phi^k$
as the convex hull in $\R^2$ of  
$$
\{(i,j) \ \vert \ i,j \in \Z, \ j \geq \val(a_{i}(z))\} \subset \R^{2}
$$
where $\val : \C((z)) \rightarrow \Q \cup \{+\infty\}$ denotes the $z$-adic valuation.  The Newton polygon  is invariant by an analytic change of variables. 
By Lemma \ref{lem5}, when $n$ is prime, if the difference Galois group of an equation is irreducible and imprimitive,  then the lower bound of the Newton polygon is delimited by the segment from $(0,\val (u))$ to $(n,0)$.  In Example \eqref{eq0}, the lower part is composed of the segment delimited by $(0,1)$ and $(1,0)$ and the segment delimited by $(1,0)$ and $(3,0)$, see Figure \ref{fig1}.  Since $G$ is irreducible,  see Example~\ref{ex1}, we find that $G$ is primitive. 

\begin{figure}[!h]
\begin{center}
\begin{tikzpicture}
\coordinate (O) at (0,2);
\coordinate (A) at (0,1);
\coordinate (B) at (1,0);
\coordinate (C) at (2,0);
\coordinate (D) at (3,0);
\coordinate (E) at (3,2);
\draw (O) -- (A);
\draw (A) -- (B);
\draw (B) -- (D);
\draw (E) -- (D);

\draw [dotted] (0,0) grid (3,2);
\put(0,30){{$(0,1)$}}
\put(20,-15){{$(1,0)$}}
\put(50,-15){{$(2,0)$}}
\put(80,-15){{$(3,0)$}}
\node (centre) at (0,1){$\bullet$};
\node (centre) at (1,0){$\bullet$};
\node (centre) at (2,0){$\bullet$};
\node (centre) at (3,0){$\bullet$};
\end{tikzpicture}
\caption{The Newton polygon of the operator associated with $U(z,t)$.}\label{fig1}
\end{center}
\end{figure}

\end{ex}
