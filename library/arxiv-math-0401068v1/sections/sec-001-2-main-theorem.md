---
doc_id: arxiv-math-0401068v1
doc_title: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS"
section_id: sec-001-2-main-theorem
section_title: "Main Theorem"
section_number: 2
pages: 2-6
source_pdf: 0401068v1.pdf
source_sha256: 8168d7e7f6069978
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.614
doc_brief: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS — @We show that for a twist knot, the A-polynomial can be obtained fr om recur- rences for the summand in Masbaum’s formula of the"
---
We start with the review of the definition of the $A$-polynomial of a knot $K$ in $S^3$ (see [@Cooper/Culler/Gillet/Long/Shalen:INVEM94] ). Let $M_K$ be the complement of $K$ and $R(M_K)$ the set of all representations of $\pi_1(M_K)$ into $SL(2,\mathbb{C})$. The set $R(M_K)$ is an affine algebraic variety. Noting that $SL(2,\mathbb{C})$ acts on representations by conjugation, we restrict our attention to the subset $R_U$ of $R(M_K)$ consisting of a represetation $\rho$ satisfying that $\rho(\mu)$ and $\rho(\lambda)$ are upper triangular matirices for the meridian $\mu$ and the preferred longitude $\lambda$ of $K$. We can define a projection $\xi$ from $R_U$ to $\mathbb{C}^2$ by $\xi(\rho)=(l,m)$ for $\rho \in R(M_K)$ with $$\rho(\mu)= \begin{pmatrix}
              m & * \\
              0  & m^{-1}
            \end{pmatrix}, \; 
 \rho(\lambda)= \begin{pmatrix}
              l & * \\
              0 & l^{-1} \\
            \end{pmatrix} .$$ The Zariski closure of $\xi(R_U)$ has a structure of an algebraic variety in $\mathbb{C}^2$ and each of its irreducible complex-dimension-one components is a curve, which is defined by a polynomial with integer coefficients in $l$ and $m$. The $A$-polynomial is the product of those defining polynomials. We note that the $A$-polynomial of $K$ has a factor $l-1$, which correponds to abelian representations. So, we denote by $A_K(l,m)$ the $A$-polynomial divided by $l-1$.

Nextly, we recall Masbaum's formula of the colored Jones polynomial for a twist knot. Some notations are fixed. $$\begin{eqnarray*}
& & \{n\}=s^{n}-s^{-n},  \; s^2=q, \\ 
& & \{n\}!=\{n\}\{n-1\}\cdots \{1\}, \; (q)_n=(1-q)(1-q^2)\cdots (1-q^n).
\end{eqnarray*}$$ Let $J_K(n)$ be the colored Jones polynomial of a 0-framing knot $K$ colored with the $n$-dimensional irreducible representation of $sl_2(\mathbb{C})$, where $J_K(n)$ is normalized by $J_{\bigcirc}(n)=1$ for the trivial knot ${\bigcirc}$. ($J'_K(n)$ in [@Masbaum:AGT03] is equal to $J_K(n)$ in this paper.)

Let $K_p$ be the twist knot drawn in figure 1. In [@Masbaum:AGT03], Masbaum obtained the following formula for the colored Jones polynomial of the twist knot $K_p$.

::: thm
[@Masbaum:AGT03] The colored Jones polynomial of the twist knot $K_p$ is given by $$\begin{equation}
J_{K_p}(n)=\sum_{k=0}^{\infty} \mathcal C_{K_p}(k) 
       \frac {\{n-k \} \{n-k+1\} \cdots \{n+k\}} {\{n\}},
\label{eqn:mas}
\end{equation}$$ where $$\begin{equation}
\mathcal C_{K_p}(k)
=(-1)^{k+1}s^{k(k+3)/2}\sum_{l=0}^k (-1)^l q^{l(l+1)p} \{2l+1\}
 \frac {\{k \}! }{\{k+l+1 \}! \{k-l\}!}.
\end{equation}$$
:::

We make use of the rearranged Masbaum's formula ([@Garoufalidis/Le:math.GT]) $$\begin{eqnarray*}
J_{K_p}(n)&=&\sum_{k=0}^{\infty}\sum_{l=0}^k (-1)^{k+1} q^{k(k+3)/2}
        q^{nk}\frac {(q^{-1})_{n+k}(q^{-1})_{n-1}}
                    {(q^{-1})_{n}(q^{-1})_{n-k-1}}\\
 {} & & \qquad \times 
       (-1)^l q^{l(l+1)p+l(l-1)/2}(q^{2l+1}-1) 
       \frac {(q)_k}{(q)_{k+l+1} (q)_{k-l}}.\qquad \qquad
\end{eqnarray*}$$ Let us put $$\begin{eqnarray*}
& & F(n,k,l)\\
& &=(-1)^{k+1} q^{k(k+3)/2}
        q^{nk}\frac {(q^{-1})_{n+k}(q^{-1})_{n-1}}
                    {(q^{-1})_{n}(q^{-1})_{n-k-1}} 
       (-1)^l q^{l(l+1)p+l(l-1)/2}(q^{2l+1}-1) 
       \frac {(q)_k}{(q)_{k+l+1} (q)_{k-l}}.
\end{eqnarray*}$$ Then, it easily follows that $$\begin{eqnarray}
f_0(q,q^n,q^k,q^l) & := &\frac {F(n+1,k,l)} {F(n,k,l)}
 =q^k\frac{(1-q^{-n-k-1})(1-q^{-n})}{(1-q^{-n-1})(1-q^{-n+k})},
 \label{eqn:f0}\\
f_1(q,q^n,q^k,q^l) & := &\frac {F(n,k+1,l)} {F(n,k,l)}
 =-q^{k+n+2}
  \frac {(1-q^{-n-k-1})(1-q^{-n+k+1})(1-q^k)}{(1-q^{k+l+2})(1-q^{k-l+1})},
 \label{eqn:f1} \\ 
f_2(q,q^n,q^k,q^l) & := &\frac {F(n,k,l+1)} {F(n,k,l)}
  =-q^{(2p+1)l+2p}
  \frac {(q^{2(l+1)+1}-1)(1-q^{k-l})}{(q^{2l+1}-1)(1-q^{k+l+2})}.
 \label{eqn:f2}
\end{eqnarray}$$ We obtain the following result.

::: thm
[]{#thm:main label="thm:main"} From the three equations $$f_0(1,m^2,x,y)=l, \; f_1(1,m^2,x,y)=1, \; f_2(1,m^2,x,y)=1,$$ we can obtain $$x=\frac {lm^2+1}{m^2+l}, \quad 
(y+1)(1-x)y^p h_p(m,x)=0,$$ where $h_p(m,x)$ is an element in $\mathbb{Z}[m^{\pm 1},x]$ and satisfies that if we put $$B_{K_p}(l,m):=\left\{
    \begin{array}{ll}
    (m^2+l)^{2p-1}(m^2)^p h_p(m,\frac {lm^2+1}{m^2+l} ), \quad & p>0,\\
    (m^2+l)^{2|p|}(m^2)^{|p|} h_p(m,\frac {lm^2+1}{m^2+l} ),  & p \le 0,\\
    \end{array}
    \right.$$ then, $B_{K_p}(l,m)=A_{K_p}(l,m)$.
:::
