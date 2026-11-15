---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-008-4-weak-morita-equivalence-of-2z-12c-and-2cboxtim
section_title: "Weak Morita equivalence of $\2Z_1(\2C)$ and $\2C\boxtimes\2C^{\mbox{\scriptsize op}}$"
section_number: 4
pages: 16-18
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.698
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{sec-morita}

\subsection{A Frobenius Algebra in $\2C\boxtimes\2C^\op$}\label{ss-mcata}
Throughout this section $\2C$ will be a strict spherical tensor category with simple unit
over an algebraically closed field $\7F$. We require that $\2C$ is semisimple with
finite set $\Gamma$ of isomorphism classes of simple objects and $\dim\2C\ne 0$. The set
$\Gamma$ has a distinguished element $0$ representing the tensor unit and an involution
$i\mapsto\ol{\imath}$ which associates with every class the class of dual objects. We
choose representers $\{X_i,\ i\in \Gamma\}$ of these classes, which are arbitrary except
that we require $X_0=\11$. (We emphasize that we do not require $\ol{X_i}=X_{\ol{\imath}}$.
This can be achieved by a suitable strictification of the category if and only if all
self-dual objects are orthogonal \cite{bw1}. (The terms real vs.\ pseudo-real do not seem
appropriate if $\7F\ne\7C$.)) We choose once and for all square roots of the $d_i=d(X_i)$,
as well as $\lambda=\sqrt{\dim\2C}$  and $(\dim\2C)^{1/4}=\sqrt{\lambda}$. 
Let $N_{ij}^k$ be the dimension of the space $\Hom(X_k,X_iX_j)$, let 
$\{t_{ij}^{k\alpha},\ \alpha=1,\ldots,N_{ij}^k\}$ be a basis in $\Hom(X_k,X_iX_j)$ and
let $\{ {t'}_{ij}^{k\alpha} \}$ be the basis in $\Hom(X_iX_j,X_k)$ which is dual in the
sense of ${t'}_{ij}^{k\alpha}\circ t_{ij}^{k,\beta}=\delta_{\alpha\beta}$. Note that
this normalization of the dual basis differs from the one provided by the trace by a
factor of $d_k$. The present choice is more convenient since otherwise the dimensions
would appear in the equation 
\[ \sum_{k,\alpha} t_{ij}^{k\alpha}\circ {t'}_{ij}^{k\alpha}=\id_{X_iX_j}. \]
The choice of the of the square roots, the $X_i$ and of the bases $\{t_{ij}^{k\alpha}\}$
is immaterial but will be kept fixed throughout the rest of the paper, and the symbols  
$\Gamma, X_i, N_{ij}^k, t_{ij}^{k\alpha}$ will keep the above meanings. 

With these preparations we can embark on the 2-categorical approach to the quantum 
double. We define
\bea \2A & = & \2C\boxtimes\2C^\op, \\
 \hat{X}_i &=& X_i\boxtimes X_i^\op\in\obj\,\2A. \eea
By \cite[Lemma 2.9]{mue09}, $\2C^\op, \2C\otimes_\7F\2C^\op$ and $\2A$ are strict spherical
in a canonical way. Every $\hat{X}_i,\ i\in \Gamma$ is simple and if it is self-dual (i.e.\
if $i=\ol{\imath}$) then it is orthogonal irrespective of whether $X_i$ is orthogonal or
symplectic. 

The following is a very slight generalization of \cite[Proposition 4.10]{lre}.
\bprop Let $\7F$ be quadratically closed and let $\2C$ be $\7F$-linear semisimple
spherical with $\dim\2C\ne 0$. There is a normalized canonical Frobenius algebra
$\5Q=(Q,v,v',w,w')$ in $\2A=\2C\boxtimes\2C^\op$ (with $\lambda_1=\lambda_2=\lambda$) 
such that  
\begin{equation}Q\cong\bigoplus_{i\in \Gamma} \, \hat{X}_i. \label{gamma}\end{equation}
\eprop
\prf Clearly, $d(Q)=\dim\2C$. By definition of $Q$ there are morphisms 
\[ v_i\in\Hom(\hat{X}_i,Q),\quad v'_i\in\Hom(Q,\hat{X}_i),\ \ i\in \Gamma, \]
such that
\begin{equation}v'_i \circ v_j=\delta_{ij}\id_{\hat{X}_i},\quad \sum_i v_i\circ v'_i=\id_Q. 
\label{cuntz}\end{equation}
Defining $v=\lambda^{1/2} v_0, v'=\lambda^{1/2} v'_0$, (\ref{W5}) is trivial. With 
${t'}_{ij}^{k\alpha} \in\Hom_\2C(X_iX_j,X_k)\equiv\Hom_{\2C^\op}(X^\op_k,X^\op_iX^\op_j)$ 
the morphisms
\[ \hat{t}_{ij}^k= \sum_{\alpha=1}^{N_{ij}^k} t_{ij}^{k\alpha} \boxtimes 
   {t'}_{ij}^{k\alpha} \ \in \ \Hom_\2A(\hat{X}_k,\hat{X}_i\hat{X}_j) \]
are independent of the choices of the bases $\{t_{ij}^{k\alpha}\}$. Then
\begin{equation}w= \lambda^{-1/2} \ \sum_{i,j,k\in \Gamma} \sqrt{\frac{d_id_j}{d_k}} \,
   v_i \otimes v_j \mcirc \hat{t}_{ij}^k \mcirc v'_k \label{defW}\end{equation}
is in $\Hom_\2A(Q,Q^2)$, and $w'\in\Hom_\2A(Q^2,Q)$ is defined dually.
Eqs. (\ref{W2}, \ref{W2'}) of Definition \ref{d-Frob} are almost obvious. (Use
$N_{0i}^j=\delta_{ij}$). The proof that $w, w'$ satisfy (\ref{W1}, \ref{W1'}) and
(\ref{W3}) is omitted since it is entirely analogous to the one in \cite[p. 591]{lre}.
Finally, $w'\circ w=\lambda\id_Q$ is proven by a simple computation observing 
${\hat{t'}}^k_{ij} \circ \hat{t}_{ij}^k=N_{ij}^k\,\id_{\hat{X}_k}$ and using
\begin{equation}\label{ddN}
 \sum_{i,j} d_id_j N_{ij}^k=\sum_{i,j} d_id_j N_{j\ol{k}}^{\ol{\imath}}=\sum_j d_k d_j^2=
  d_k\dim\2C=d_k\lambda^2. \end{equation}
Thus $(Q,v,v',w,w')$ is a canonical Frobenius algebra in $\2A$. 
\qed

Thus Theorem \ref{Main} applies and yields a spherical bicategory $\2E$. ($\2E$ is strict as a
bicategory except for the existence of non-trivial unit constraints for $\11_\6B$ and
strict pivotal \cite{bw2} except for isomorphisms 
$\gamma_{X,Y}: \ol{Y}\circ\ol{X}\rarr\ol{X\circ Y}$ which are  non-trivial whenever
$\mbox{Ran}(Y)=\mbox{Src}(X)=\6B$.) In
particular, we have a spherical tensor category $\2B=\END_\2E(\6B)$.
In the rest of the paper $\2A, \5Q, \2E$ and $\2B$ will have the above meanings. By 
construction $Q$ contains the identity object of $\2A$ with multiplicity 1, thus $J, \oj $
and $\11_B$ are simple by \cite[Proposition 5.3]{mue09} and $d(J)=d(\oj)=\lambda$.
(The condition (iii) of that proposition can also easily be verified directly.) 

\blemma $\dim\2B=(\dim\2C)^2$. \elemma
\prf Follows from $\dim\2B=\dim\2A$ and $\dim\2A=(\dim\2C)^2$. The former is
\cite[Proposition 5.16]{mue09} and the latter is obvious since the simple objects of
$\2C\boxtimes\2C^\op$ are those of the form $X\boxtimes Y^\op$ with $X, Y$ simple. \qed 

In the sequel we will write $\11$ instead of $\11^\op$ in order to alleviate the
notation.
