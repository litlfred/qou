---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-003-2-difference-algebra
section_title: "Difference algebra"
section_number: 2
pages: 3-7
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
text_source: latex
latex_prose_ratio: 0.707
latex_coverage_ratio: 0.971
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
\label{sec:diffceAlgebra}
\subsection{Galois groups}
\label{sec:GaloisGp}


In this section, we make a short overview of the Galois theory of linear difference equations.  
For more details on what follows, we refer to \cite[Chapter~1]{van2006galois}.
A difference ring is a commutative ring $\Rb$ equipped with an automorphism $\phi : \Rb\rightarrow \Rb$. We denote by $C_{\Rb}:= \{c\in \Rb| \phi(c)=c\}$, the constants of the difference ring $(\Rb,\phi)$. A difference ideal $I$ of a difference ring $(\Rb,\phi)$ is an ideal such that $\phi(I)\subset I$.  If $\Rb$ is a field, we call $(\Rb,\phi)$ a difference field. In this case, $C_{\Rb}$ is a field, the field of constants. 
With an abuse of notations, we will often denote by $\Rb$ the difference ring $(\Rb,\phi)$. 

\medskip

\emph{Throughout this paper, we assume that $(\k,\phi)$ is a difference field such that its field of constants $C_{\k}$ is algebraically closed.}

\medskip

If we consider a difference system 
\begin{equation}
\label{eq:diffcesystembase}
    \phi(Y) = AY,\quad with \quad A\in \GL_n\left(\k\right),
\end{equation}
according to \cite[Section 1.1]{van2006galois}, there exists a difference ring extension $(\L,\phi)$ of $(\k,\phi)$ such that:
\begin{itemize}[label=$\bullet$]
    \item there exists a fundamental matrix of solutions of \eqref{eq:diffcesystembase} with entries in $\L$, that is, a matrix $U\in\GL_n\left(\L\right)$ such that $\phi\left(U\right)=AU$;
    \item $\L$ is generated as a $\k$-algebra by the entries of $U$ and $\det\left(U\right)^{-1}$;
    \item the only difference ideals of $\L$ are $\lbrace 0\rbrace$ and $\L$.
\end{itemize}
A difference ring $\L$ which satisfies these conditions is called a Picard-Vessiot ring for the system \eqref{eq:diffcesystembase} over $\k$. It is unique up to isomorphisms of difference rings over $\k$. We have the following property: $C_{\L} = C_{\k}$.

The difference Galois group $G$ of \eqref{eq:diffcesystembase} over $\k$ is the group of $\k$-linear automorphisms of $\L$ commuting with $\phi$, that is, 
$$
G:=\lbrace \sigma\in\text{Aut}(\L/\k)\mid \sigma\circ\phi=\phi\circ\sigma \rbrace \, .
$$
For any fundamental matrix $U \in \GL_n(\L)$, an easy computation shows that 
$U^{-1}\sigma(U) \in \GL_{n}(C_{\L})= \GL_{n}(C_{\k})$ for all $\sigma \in G$. 
By  \cite[Theorem~1.13]{van2006galois}, the faithful representation
$$
\begin{array}{rccl}
 \rho: & G & \rightarrow & \GL_{n}(C_{\k}) \\ 
   & \sigma & \mapsto & U^{-1}\sigma(U)
\end{array}
$$
identifies $G $ with a linear algebraic subgroup $G\subset\GL_{n}(C_{\k})$.  If we take another fundamental matrix of solutions $V$, we find an algebraic group that is conjugated to the first one. 
In this paper, by ``computation of the difference Galois group $G$'', we mean ``computation of an algebraic subgroup of $\GL_n\left(C_{\k}\right)$ conjugated to $\rho(G)$'', thus we work up to conjugations.  Abusing notations, we will still denote by $G$ the image of the difference Galois group under the above representation.\par

We denote by $\k\left< \phi,\phi^{-1}\right> $ the \"Ore algebra of noncommutative Laurent polynomials with coefficients in $\k$ such that $\phi f = \phi(f)\phi$ for all $f\in\k$.
We consider the difference equation 
\begin{equation}\label{eq:diffceeqbase}
Ly=0,\quad  \text{where}\quad  L:=\sum_{i=0}^{n}  a_i \phi^{i} \in \k\left< \phi\right> \text{ with } a_0 a_n \neq 0 \, ,
\end{equation}
that is, 
$a_0 y+\dots +a_n \phi^n (y)=0$ with $a_i\in \k$ and $a_0 a_n \neq 0 $.
We transform the difference equation \eqref{eq:diffceeqbase}
into the difference system 
$$\phi(Y)=A_L Y,  \quad\hbox{ where} \quad A_L=\begin{pmatrix}
&1&&\\ 
 &  &\ddots & \\
&&&1\\
-a_0/a_n& \dots&&-a_{n-1}/a_n
\end{pmatrix} $$
is the companion matrix associated with $L$.
By definition, the difference Galois group of \eqref{eq:diffceeqbase} is the difference Galois group of the system $[A_L]$.\par 

The change of variables $Z:=TY$,  $T\in \GL_{n}(\k)$, transforms the system  $\phi Y=AY$ with  $A\in  \GL_{n}(\k)$ into $\phi Z=BZ$ where $B:=\phi(T)AT^{-1}\in  \GL_{n}(\k)$.  Let  $A,B\in  \GL_{n}(\k)$.  We will say that $[A]$ and $[B]$ are equivalent over $\k$ if there exists   $T\in \GL_{n}(\k)$ such that $B=\phi(T)AT^{-1}$. \par 

In what follows, we assume moreover that the field $\k$ satisfies:
\begin{itemize}
    \item $\k$ is a $\mathcal{C}^{1}$-field, that is every non-constant homogeneous polynomial $P$ over $\k$ has a nontrivial zero provided that the number of its variables is more than its degree;
    \item $\k$ is the only finite algebraic difference field extension of $\k$.
\end{itemize}
All the above mentioned examples (S,Q,M,E) satisfy these two conditions, see \cite{hendriks1997algorithm,hendriks1998algorithm,dreyfus2015galois,roques2018algebraic}. 
Note that in the $q$-difference case, the field $(C(z),\phi)$ is a difference field but there are nontrivial finite  algebraic difference field extensions. For instance $C(z^{1/2})|C(z)$ is of degree two and we may extend $\phi$ on it with $\phi (z^{1/2})=q^{1/2}z^{1/2}$. This is the reason why we consider $C(z^{1/*})$ instead of $C(z)$ in that setting. Similar considerations occur in the elliptic case.


We recall that $C:= C_{\k}$ is by hypothesis algebraically closed and the characteristic of $\k$ is zero. 
The following statement will be crucial in what follows.  See \cite[Propositions~1.20 and 1.21]{van2006galois}, see also  \cite[Theorem 2.4]{dreyfus2015galois}.  
\begin{theo}
\label{theo:reduced form}
Let $G \subset \GL_{n}(C)$ be the difference Galois group over $(\k,\phi)$ of \eqref{eq:diffcesystembase}. 
Then, the following properties hold:
\begin{itemize}
\item $G/G^0$ is finite and cyclic, where $G^0$ is the identity component of $G$;
\item there exists $B \in G(\k)$ such that \eqref{eq:diffcesystembase} is equivalent to $\phi Y=BY$ over~$\k$. 
\end{itemize}
Let $\widetilde{G}$ be an algebraic subgroup of $\GL_{n}(C)$ such that~$A\in \widetilde{G}(\k)$. The following properties hold:
\begin{itemize}
\item $G$ is conjugate to a subgroup of $\widetilde{G}$;
\item any minimal element in the set of algebraic subgroups $\widetilde{H}$ of $\widetilde{G}$ for which there exists 
$T\in \GL_{n}(\k)$ such that $\phi(T)AT^{-1}\in \widetilde{H}(\k)$ is conjugate to~$G$;
\item $G$ is conjugate to $\widetilde{G}$ if and only if, for any $T\in  \widetilde{G}(\k)$ and for any proper algebraic subgroup $\widetilde{H}$ of $\widetilde{G}$, 
one has that $\phi(T)AT^{-1}\notin \widetilde{H}(\k)$.
\end{itemize}
\end{theo}

In practice, to compute the difference Galois group, we are going to compute a gauge transformation such that the transformed system lies in $G(\k)$.
This leads to the following definition.  

\begin{defn}
Let $G \subset \GL_{n}(C)$ be the difference Galois group over $(\k,\phi)$ of the system \eqref{eq:diffcesystembase}. We say that the system \eqref{eq:diffcesystembase} is \emph{in reduced form} (or \emph{reduced}) when $A\in G(\k)$.  
\end{defn} 

Given a difference system $\phi(Y)=AY$ and an integer $\ell\geq 1$,  we can iterate it: \begin{equation}
    \label{eq:iterateSystem}
    \phi^{\ell}(Y)=A_{[\ell]}Y, \quad  \text{where} \quad  A_{[\ell]}=\phi^{\ell-1}(A)\times \dots \times A\, .
\end{equation}
Let $G_{[\ell]}$ be the difference Galois group of the system \eqref{eq:iterateSystem}. 
The following lemma may be deduced from the proof \cite[Proposition~4.6]{dreyfus2021functional} in the particular case where the parametric operator is the identity,  and is proved in  \cite[Proposition~4.10]{adamczewski2021hypertranscendence}.
It compares the Galois groups $G_{[\ell]}$,  $\ell \geq 1$. 

\begin{lem}\label{lem2}
For all $\ell \geq 1$,  $G_{[\ell]}$ has the same connected component of the identity as $G$.  Furthermore,  there exists $\ell_0\geq 1$, such that $G_{[\ell_0]}$ is the connected component of the identity of $G$.
\end{lem}
 



\subsection{Factorisations of difference operators}\label{secfact}
In this subsection, we focus on the reducible difference operators and make the relation with the reducible Galois groups and the Riccati equation.  
Let $G$ be an algebraic subgroup of $\GL_{n}(C)$. We say that $G$ is reducible if there exists a non trivial vector subspace $V$ of $C^n$ such that for all $\sigma\in G$, $\sigma(V)\subset V$.  We say that $G$ is irreducible otherwise. \par 
The following lemma relates the irreducibility of the difference Galois group with the factorisation of the difference operator, see \cite[Lemma 4.4]{adamczewski2021hypertranscendence}.

\begin{lem}\label{lem1}
Let $G\subset \GL_{n}(C)$ be the difference Galois group of \eqref{eq:diffcesystembase}. Then,  $G$ is reducible with a nontrivial invariant space of dimension $0<m<n$, if and only if there exists $T\in \GL_n(\k)$,  $A_1\in \GL_m(\k)$, and $A_2,A_3$ matrices of convenient size,    such that 
$$\phi(T)AT^{-1}=\left(\begin{array}{cc}
A_1 &  A_2\\
0 & A_3  
\end{array}\right).
$$
If we consider the difference system $[A_L]$ attached to \eqref{eq:diffceeqbase}, then its difference Galois group is reducible with $A_1\in \GL_m(\k)$ if and only if
$L$ admits a nontrivial right factor of order $m$.
\end{lem}

Thus, to determine whether $G$ is irreducible or not, we have to determine whether the difference operator $L$ defined in \eqref{eq:diffceeqbase} admits a nontrivial right factor or not.  For right factors of order one, we have the following criterion. 

\begin{lem}[Lemma 2 in \cite{abramov2021rational}]\label{lem:eq left factor}
Let $L$ be the difference operator defined in \eqref{eq:diffceeqbase}.
The operator of order one $\phi-\alpha $ is a right factor of $L$ if and only if 
$$
\sum\limits_{i=0}^n a_i \prod\limits_{j=0}^{i-1} \phi^j(\alpha) = 0.
$$
\end{lem}

Although the above equation,  called the Riccati equation,   is nonlinear it might be solved in some situations we are going to describe later.\par 
When $L$ has order two,  it admits a nontrivial factor if and only if it admits a nontrivial right factor of order one. \par
When $L$ has order three, it admits a nontrivial factor if and only if it admits a nontrivial factor of order one.  The latter may be either a right or a left factor.  Let us see how we can pass from left factor to right factor.   
 We define the dual $M^{\vee} $ of an operator $M=\sum_{i=m}^{n}   a_{i}\phi^{i} \in\k\left< \phi,\phi^{-1}\right>$ by 
$$
M^{\vee} := \sum_{i=m}^{n}  \phi^{-i} (a_{i})
\phi^{-i}.$$ 
By linearity, if $M_1, M_2\in \k\left< \phi,\phi^{-1}\right>$, we can check that
$$
 (M_1 M_2)^{\vee}=M_2^{\vee}M_1^{\vee}. 
$$
Hence, an operator has a left factor of order one if and only if its dual has a right factor of order one.   So we will focus on right factors of order one. 

\begin{rem}
\label{rem:rightFactorOrder1}
Assume $n>1$ and that $L$ admits a right factor of order one so let us write $L$ as 
$\widetilde{L}(\phi-\alpha)$ where $\alpha\in \k$ and  $\widetilde{L}\in\k\left< \phi,\phi^{-1}\right>$ has order $n-1$.  
Let $y_1$ be a solution of $Ly=0$ such that $\phi(y_1)\neq \alpha y_1$ and let $y_2:=\phi(y_1)-\alpha y_1$. By construction $y_2\neq 0$ is a solution of $\widetilde{L}y=0$. If $Y:=\left(y_1,y_2,\ldots,\phi^{n-2}(y_2)\right)^t$ then $\phi(Y)=\widetilde{A}Y$ where
$$
\widetilde{A}:=\left(\begin{array}{c|cccc}
\alpha &  1 & 0 & \cdots & 0 \\
\hline
0 & & & &  \\
\vdots & & & A_{\widetilde{L}}&  \\
0 & & & & 
\end{array}\right)\, .
$$
Thus, the companion system associated with $Ly=0$ is equivalent to the system $[\widetilde{A}]$.  Furthermore, $A_{\widetilde{L}}$ is a companion matrix associated with $\widetilde{L}$.\end{rem}


\subsection{From theory to practice}
\label{sec:theoryPractice}
We recall that the aim of this paper is to explain how one can compute theoretically the Galois group of a difference equation of order $3$.
In practice we may also need to make more assumptions on the difference field $(\k,\phi)$ in order to compute effectively the difference Galois groups:
\begin{itemize}
\item
Assume that $\mathbf{k}$ is an effective field,
i.e. that one can compute representatives of the four operations $+,-,\times,/$ and one can effectively test whether two elements of $\mathbf{k}$ are equal.  
\item 
Assume that, given a homogeneous linear difference system $[A]$ with $A\in \GL_n(\mathbf{k})$, we can effectively find a 
basis of its rational solutions, i.e. its solutions $Y\in \mathbf{k}^n$.
\item Assume that given a difference operator $L$, if $L$ admits at least one right factor of order one, then we are able to compute effectively one of such right factors.
\end{itemize}


When $C=\overline{\Q}$,  for the cases (S, Q, M), the  two first points are satisfied. One can find some references for the second point in this table:
\medskip
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
    cases &  (S) & (Q) & (M)&(E) \\
\hline 
    ref. & \cite{Abr95,AB98,vanHoeij1998,AB2001} & \cite{Abr95,AB2001,Abr02} & \cite{CDDM18} & \cite{dreyfus2015galois,combot2022hyperexponential}\\
\hline
\end{tabular}
\end{center}
\medskip 

Note that in the elliptic case the second  point is not satisfied, unless considering the case $n=2$, see \cite{dreyfus2015galois} (note that the latter is concerned by the more general problem of solving Riccati equations), or when the framework is modified,  see for instance \cite{combot2022hyperexponential}.  Thus, in that case, our algorithm may not lead to a systematic computation of the difference Galois group. It will reduce the computation to the determination of rational solutions of certain linear difference equations that may be complicated to solve concretely.
Throughout this paper, we will emphasize which kind of equations we have to be able to solve. 


We saw in Section \ref{secfact} that the study of the irreducibility of the Galois groups is closely related to the factorisation of the difference operator.  From Lemma \ref{lem:eq left factor}, when we look at a right factor of order one, we have to solve a Riccati equation of the form  $$
\sum\limits_{i=0}^n a_i \prod\limits_{j=0}^{i-1} \phi^j(\alpha) = 0.
$$

When $C=\overline{\Q}$,  we are able to compute right-factors of order $1$ in the cases (S,Q,E) but we want to emphasis that the complexity is exponential, in the order of the equation, contrary to the search of rational solutions, whose complexity is polynomial. 
   Here-below, one can find some references for these computations:

\medskip
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
    cases &  (S) & (Q) & (E)\\
\hline 
ref.  & \cite{Petkovsek92,CvH06,abramov2021rational} & \cite{APP98,CvH06,abramov2021rational} &\cite{dreyfus2015galois,combot2022hyperexponential} \\
\hline
\end{tabular}
\end{center}
\medskip 
For the Mahler case, the computation of Riccati solution is a work in progress by the first author of this paper, Chyzak, Dumas and Mezzarobba.
\medskip
\begin{ex}\label{ex1}
Let us now present the strategy of \cite{abramov2021rational} to show that the difference Galois group of  \eqref{eq0} over $\C(z^{1/*})$ is irreducible, which is equivalent to show that the corresponding operator has no factor of order $1$. We point out the fact that $\C(z^{1/*})$ is not an effective field but the strategy still work in that case. 
Assume that $t\neq 0$. 
 Let us begin by proving that there is no right factor of order one. Let 
 $$L=a_0+a_1 \phi+ a_2\phi^2+a_3 \phi^3$$
  be the $q$-difference operator corresponding to \eqref{eq0}, and let $L^{\vee} $ be its dual. 
By  \cite[Lemma 3]{abramov2021rational},
 For any $\alpha \in \k^{\times}$  there exist $\lambda \in \C^{\times}$, $\ell\in\N^*$ and unitary $b,c,r\in \C[z^{1/\ell}] \setminus \{0\}$  such that 
$$
  \alpha =\lambda\hspace{0.1cm}  \frac{b}{c} \hspace{0.1cm}\frac{\phi(r)}{r}
$$
 and 
\begin{itemize}
\item $\gcd (b, \phi^k (c))=1$ for all $k\in \lbrace 0,1, 2\rbrace$;
\item $\gcd (b, r)=1$;
\item $\gcd (c, \phi (r))=1$.
\end{itemize}
Using this, one can deduce by  \cite[Lemma 3]{abramov2021rational} that if $\phi-\alpha$ is a right factor of order $1$ of $L$ for some  $\alpha \in \k^{\times}$, then, in the above decomposition for $\alpha$, we have $b \vert a_{0}$,   $c \vert \phi^{-2}(a_{3})$,  and 
\begin{equation}\label{eq:bla}
 \lambda^3  a_{3} b \phi(b)\phi^2 (b)  \phi^3 (r) +\lambda^2 a_{2}  b \phi(b)\phi^2 (c) \phi^2 (r)+\lambda a_{1} b \phi(c)\phi^2 (c)  \phi (r)+ a_{0} c \phi(c)\phi^2 (c) r=0.
\end{equation}


The strategy to decide whether $L$ has a right factor of order one is the following.  For every unitary pair   $(b,c)\in \left( \C[z^{1/\ell}]\setminus \{0\}\right)^2$ such that $b \vert a_{0}$,   $c \vert \phi^{-2}(a_{3})$,  we decide whether there exist $\lambda \in \C^{\times}$ and $r\in \C[z^{1/\ell}] \setminus \{0\}$ such that \eqref{eq:bla} holds. If we find a solution then we have a right factor of order one, otherwise there is no right factor of order one.
Here, since $a_0=q^3 z$, $a_3=t$ are monomials in $z$ (recall that $t\neq 0)$ the choices are very limited. The only possibilities for the pair $(b,c)$ are $(z^d,1)$, with $0\leq d\leq 1 $.   Recall that $\deg(a_3)=0$,  $\deg(a_2)=2$,  $\deg(a_1)=\deg(a_0)=1$.  
The degrees of the terms in \eqref{eq:bla} are respectively given by  
$$3d+\deg r(z), \quad 2+2d+\deg r(z), \quad 1+d+\deg r(z), \quad 1+\deg r(z)$$
and a direct calculation shows that, for $0\leq d\leq 1 $,  $2+2d+\deg r(z)$ is greater than the remaining ones, whence there is no solution.
  We proceed similarly with the dual for the left factor of length one.
  \begin{multline*}
 L^{\vee}=a_{3}(q^{-3}z)\sigmaq^{-3}  + a_{2}(q^{-2}z)\sigmaq^{-2} +a_{1}(q^{-1}z)\sigmaq^{-1} +a_{0}(z)\\
=\sigmaq^{-3}\Big(a_{3}(z)  +a_{2}(qz)\sigmaq +a_{1}(q^{2}z)\sigmaq^{2} +a_{0}(q^{3}z)\sigmaq^{3}\Big)
\end{multline*} 
Here the possible pairs for $(b,c)$ are $( 1,z^d)$, with $0\leq d\leq 1 $. The degrees of the terms of the equation corresponding to \eqref{eq:bla}  are
$$1+\deg r(z), \quad 1+d+\deg r(z), \quad 2+2d+\deg r(z), \quad 3d+ \deg r(z) .$$
Again, for $0\leq d\leq 1 $,  $2+2d+\deg r(z)$ is greater than the remaining ones.
\end{ex}
