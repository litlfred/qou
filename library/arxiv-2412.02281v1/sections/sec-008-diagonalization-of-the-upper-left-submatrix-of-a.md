---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-008-diagonalization-of-the-upper-left-submatrix-of-a
section_title: "Diagonalization of the Upper Left Submatrix of A"
section_number: null
pages: 11-12
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.919
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
\label{sec:diag}
 We first introduce a diagonalized system under   the   conditions:
\begin{align}\label{ineq1}
\lambda^{\left(n-1\right)}_i & \ne \lambda^{\left(n-1\right)}_j, \text{ for } \ 1\leq i\neq j \leq n-1,\\ \label{ineq2}
\lambda^{\left(n-1\right)}_i & \ne \lambda^{\left(n-2\right)}_j, \text{ for } \ 1\leq i \leq n-1, \  1\leq j \leq n-2 .
\end{align}

 Under the conditions \eqref{ineq1} and \eqref{ineq2},    let us take the $\left(n-1\right)\times \left(n-1\right)$ matrix $P_{n-1}$ given by
\begin{equation*}
    (P_{n-1})_{ij}:=\frac{(-1)^{i+j}\Delta^{1,...,n-2}_{1,...,\hat{i},...,n-1}\left(A-\lambda^{\left(n-1\right)}_j\cdot \mathrm{Id}_n\right)}{\sqrt{ \prod_{l=1,l\ne j}^{n-1}\left(\lambda^{\left(n-1\right)}_l-\lambda^{\left(n-1\right)}_j\right)\prod_{l=1}^{n-2}\left(\lambda^{\left(n-2\right)}_l-\lambda^{\left(n-1\right)}_j\right)} }.
\end{equation*}
Here $\Delta_{1,...,\hat{i},..., n-1}^{1,...,n-2}\left(A-\lambda^{\left(n-1\right)}_j\cdot \mathrm{Id}_n\right)$  is  the  minor of the matrix $A-\lambda^{\left(n-1\right)}_j\cdot \mathrm{Id}_n$, formed by the first $n-2$ rows and the first $n-1$ columns, with the   $i$-th column  omitted.  Then the inverse matrix of $P_{n-1}$ is given explicitly as follows and we can use $P_{n-1}$ to diagonalize the upper left  submatrix  $A^{(n-1)}$ of $A$.
\begin{prop}[see e.g., \cite{lin2024explicit}]\label{An-1Pn-1}
     If $A$ satisfies \eqref{ineq1} and \eqref{ineq2}, then $P_{n-1}$ is invertible and the inverse matrix $P_{n-1}^{-1}$ is given by
    \begin{equation*}
        \left(P_{n-1}^{-1}\right)_{i j}=\frac{(-1)^{i+j}\Delta^{1,...,\hat{j},...,n-1}_{1,...,n-2}   \left(A-\lambda^{\left(n-1\right)}_i\cdot \mathrm{Id}_n\right)}{\sqrt{ \prod_{l=1,l\ne i}^{n-1}\left(\lambda^{\left(n-1\right)}_l-\lambda^{\left(n-1\right)}_i\right)\prod_{l=1}^{n-2}\left(\lambda^{\left(n-2\right)}_l-\lambda^{\left(n-1\right)}_i\right)} },  \  \text{for}  \  1\leq i,j \leq    n-1     .
    \end{equation*}
    Moreover, we have
    \begin{equation*}
       P_{n-1}^{-1} A^{\left(n-1\right)} {P}_{n-1}= \mathrm{diag}\left(\lambda^{\left(n-1\right)}_1,\ldots,\lambda^{\left(n-1\right)}_{n-1}\right), 
    \end{equation*}
    and we introduce
    \begin{eqnarray*}
        A_{n-1}:=\operatorname{diag}\left({P}_{n-1}^{-1},1\right)\cdot A \cdot \operatorname{diag}\left({P}_{n-1},1\right) = \left(\begin{array}{cccc}
\lambda^{\left(n-1\right)}_1 & & 0 & a^{\left(n-1\right)}_1 \\
 & \ddots & & \vdots \\
0 & & \lambda^{\left(n-1\right)}_{n-1} & a^{\left(n-1\right)}_{n-1} \\
b^{\left(n-1\right)}_1 & \cdots & b^{\left(n-1\right)}_{n-1} & a_{n n} 
\end{array} \right).
    \end{eqnarray*}
Here   $a^{\left(n-1\right)}_i$ and $b^{\left(n-1\right)}_i$  are
\begin{align*}

    a^{\left(n-1\right)}_i&= \sum_{v=1}^{n-1}\left({P}_{n-1}^{-1}\right)_{i v} \cdot a_{v n}=\frac{(-1)^{i+n-1}\Delta^{1,...,n-1}_{1,...,n-2,n}\left(A-\lambda^{\left(n-1\right)}_i\cdot \mathrm{Id}_n\right)}{\sqrt{\prod_{l=1,l\ne i}^{n-1}\left(\lambda^{\left(n-1\right)}_l-\lambda^{\left(n-1\right)}_i\right)\prod_{l=1}^{n-2}\left(\lambda^{\left(n-2\right)}_l-\lambda^{\left(n-1\right)}_i\right)}},\\ 
    
    b^{\left(n-1\right)}_i&= \sum_{v=1}^{n-1} a_{n v}\cdot \left({P}_{n-1}\right)_{v i}=\frac{(-1)^{i+n-1}\Delta_{1,...,n-1}^{1,..., n-2,n}\left(A-\lambda_i^{\left(n-1\right)}\cdot \mathrm{Id}_n\right)}{\sqrt{\prod_{l=1,l\ne i}^{n-1}\left(\lambda^{\left(n-1\right)}_l-\lambda^{\left(n-1\right)}_i\right)\prod_{l=1}^{n-2}\left(\lambda^{\left(n-2\right)}_l-\lambda^{\left(n-1\right)}_i\right)}},
\end{align*}
and  we  have
\begin{equation}\label{eq:aibi}
 a^{\left(n-1\right)}_i   b^{\left(n-1\right)}_i =-\frac{\prod_{l=1}^{n}\left(\lambda^{\left(n\right)}_l-\lambda^{\left(n-1\right)}_i\right)}{\prod_{l=1,l\neq i}^{n-1}\left(\lambda^{\left(n-1\right)}_l-\lambda^{\left(n-1\right)}_i\right)}.
\end{equation}
\end{prop}



Now let us use the conjugation of the $n\times n$ matrix $\operatorname{diag}\left({P}_{n-1},1\right)$ to diagonalize the upper left part of the equation \eqref{qdes}  and   obtain the equation 
\begin{equation}
    D_q F_q\left(z\right)=\left( E_{n n}+\frac{A_{n-1}}{z}\right) F_q\left(z\right).\label{diagqdes}
\end{equation}
