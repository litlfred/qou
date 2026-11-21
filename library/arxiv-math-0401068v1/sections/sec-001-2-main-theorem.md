---
doc_id: arxiv-math-0401068v1
doc_title: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS"
section_id: sec-001-2-main-theorem
section_title: "Main Theorem"
section_number: 2
pages: 2-3
source_pdf: 0401068v1.pdf
source_sha256: 8168d7e7f6069978
toc_source: outline
text_source: latex
latex_prose_ratio: 0.673
latex_coverage_ratio: 0.882
doc_brief: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS — @We show that for a twist knot, the A-polynomial can be obtained from recur- rences for the summand in Masbaum’s formula of the"
---
We start with the review of the definition of the $A$-polynomial of a knot $K$ in $S^3$ (see [@Cooper/Culler/Gillet/Long/Shalen:INVEM94] ). Let $M_K$ be the complement of $K$ and $R(M_K)$ the set of all representations of $\pi_1(M_K)$ into $SL(2,\mathbb{C})$. The set $R(M_K)$ is an affine algebraic variety. Noting that $SL(2,\mathbb{C})$ acts on representations by conjugation, we restrict our attention to the subset $R_U$ of $R(M_K)$ consisting of a represetation $\rho$ satisfying that $\rho(\mu)$ and $\rho(\lambda)$ are upper triangular matirices for the meridian $\mu$ and the preferred longitude $\lambda$ of $K$. We can define a projection $\xi$ from $R_U$ to $\mathbb{C}^2$ by $\xi(\rho)=(l,m)$ for $\rho \in R(M_K)$ with $$\rho(\mu)= \begin{pmatrix}
              m & * \\
              0  & m^{-1}
            \end{pmatrix}, \; 
 \rho(\lambda)= \begin{pmatrix}
              l & * \\
              0 & l^{-1} \\
            \end{pmatrix} .$$ The Zariski closure of $\xi(R_U)$ has a structure of an algebraic variety in $\mathbb{C}^2$ and each of its irreducible complex-dimension-one components is a curve, which is defined by a polynomial with integer coefficients in $l$ and $m$. The $A$-polynomial is the product of those defining polynomials. We note that the $A$-polynomial of $K$ has a factor $l-1$, which correponds to abelian representations. So, we denote by $A_K(l,m)$ the $A$-polynomial divided by $l-1$.

Nextly, we recall Masbaum's formula of the colored Jones polynomial for a twist knot. Some notations are fixed. $$\begin{aligned}
& & \{n\}=s^{n}-s^{-n},  \; s^2=q, \\ 
& & \{n\}!=\{n\}\{n-1\}\cdots \{1\}, \; (q)_n=(1-q)(1-q^2)\cdots (1-q^n).
\end{aligned}$$ Let $J_K(n)$ be the colored Jones polynomial of a 0-framing knot $K$ colored with the $n$-dimensional irreducible representation of $sl_2(\mathbb{C})$, where $J_K(n)$ is normalized by $J_{\bigcirc}(n)=1$ for the trivial knot ${\bigcirc}$. ($J'_K(n)$ in [@Masbaum:AGT03] is equal to $J_K(n)$ in this paper.)

Let $K_p$ be the twist knot drawn in figure 1. In [@Masbaum:AGT03], Masbaum obtained the following formula for the colored Jones polynomial of the twist knot $K_p$.

::: thm
[@Masbaum:AGT03] The colored Jones polynomial of the twist knot $K_p$ is given by $$J_{K_p}(n)=\sum_{k=0}^{\infty} \mathcal C_{K_p}(k) 
       \frac {\{n-k \} \{n-k+1\} \cdots \{n+k\}} {\{n\}},
\label{eqn:mas}$$ where $$\mathcal C_{K_p}(k)
=(-1)^{k+1}s^{k(k+3)/2}\sum_{l=0}^k (-1)^l q^{l(l+1)p} \{2l+1\}
 \frac {\{k \}! }{\{k+l+1 \}! \{k-l\}!}.$$
:::

We make use of the rearranged Masbaum's formula ([@Garoufalidis/Le:math.GT]) $$\begin{aligned}
J_{K_p}(n)&=&\sum_{k=0}^{\infty}\sum_{l=0}^k (-1)^{k+1} q^{k(k+3)/2}
        q^{nk}\frac {(q^{-1})_{n+k}(q^{-1})_{n-1}}
                    {(q^{-1})_{n}(q^{-1})_{n-k-1}}\\
 {} & & \qquad \times 
       (-1)^l q^{l(l+1)p+l(l-1)/2}(q^{2l+1}-1) 
       \frac {(q)_k}{(q)_{k+l+1} (q)_{k-l}}.\qquad \qquad
\end{aligned}$$ Let us put $$\begin{aligned}
& & F(n,k,l)\\
& &=(-1)^{k+1} q^{k(k+3)/2}
        q^{nk}\frac {(q^{-1})_{n+k}(q^{-1})_{n-1}}
                    {(q^{-1})_{n}(q^{-1})_{n-k-1}} 
       (-1)^l q^{l(l+1)p+l(l-1)/2}(q^{2l+1}-1) 
       \frac {(q)_k}{(q)_{k+l+1} (q)_{k-l}}. 
\end{aligned}$$ Then, it easily follows that $$\begin{aligned}
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
\end{aligned}$$ We obtain the following result.

::: thm
[]{#thm:main label="thm:main"} From the three equations $$f_0(1,m^2,x,y)=l, \; f_1(1,m^2,x,y)=1, \; f_2(1,m^2,x,y)=1,$$ we can obtain $$x=\frac {lm^2+1}{m^2+l}, \quad 
(y+1)(1-x)y^p h_p(m,x)=0,$$ where $h_p(m,x)$ is an element in $\mathbb{Z}[m^{\pm 1},x]$ and satisfies that if we put $$B_{K_p}(l,m):=\left\{
    \begin{array}{ll}
    (m^2+l)^{2p-1}(m^2)^p h_p(m,\frac {lm^2+1}{m^2+l} ), \quad & p>0,\\
    (m^2+l)^{2|p|}(m^2)^{|p|} h_p(m,\frac {lm^2+1}{m^2+l} ),  & p \le 0,\\
    \end{array}
    \right.$$ then, $B_{K_p}(l,m)=A_{K_p}(l,m)$.
:::

# Proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}

Let $K_p$ be the twist knot pictured in Figure 1. To prove Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}, we use the following formula for the $A$-polynomial of the twist knot $K_p$ due to Hoste and Shanahan in [@Hoste/Shanahan:JK].

::: thm
(Hoste-Shanahan [@Hoste/Shanahan:JK]) For $p\ne -1,0,1,2$, $A_{K_p}(l,m)$ is given recusively by $$A_{K_p}(l,m)=\left\{ 
            \begin{array}{ll}
            c A_{K_{p-1}}(l,m)-d A_{K_{p-2}}(l,m), & p>0,\\
            c A_{K_{p+1}}(l,m)-d A_{K_{p+2}}(l,m), & p<0, 
            \end{array}
            \right.\label{eqn:HS}$$ where $$\begin{aligned}
c&=&-l+l^2+2lm^2+m^4+2lm^4+l^2m^4+2lm^6+m^8-lm^8, \\
d&=&m^4(l+m^2)^4,
\end{aligned}$$ and with initial conditions $$\begin{aligned}
A_{K_2}(l,m)&=&-l^2+l^3+2l^2m^2+lm^4+2l^2m^4-lm^6-l^2m^8 \\
 {} & &        +2lm^{10}+l^2m^{10}+2lm^{12}+m^{14}-lm^{14},\\
A_{K_1}(l,m)&=  & l+m^6,\\
A_{K_0}(l,m)&=  & 1, \\
A_{K_{-1}}(l,m)&=  &-l+lm^2+m^4+2lm^4+l^2m^4+lm^6-lm^8.\\
\end{aligned}$$
:::

<figure>
<embed src="twistknot.eps" />
<p>p full twists</p>
<div class="center">
<p>Figure 1</p>
</div>
</figure>

Now, we give a proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

*Proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}* From the first equation $$f_0(1,m^2,x,y)=x\frac {(1-\frac 1 {xm^2})}{(1-\frac x {m^2})}=l,$$ we get $$x=\frac {lm^2+1}{m^2+l}.$$ Moreover, the second equation $$f_1(1,m^2,x,y)=-xm^2
               \frac {(1-\frac 1 {xm^2})(1-\frac x {m^2})(1-x)}
                     {(1-xy)(1-\frac x y)}
                     =1$$ gives $$y^2+1=\frac y {m^2}(m^4-xm^4+x^2m^2+m^2+1-x). \label{eqn:y}$$ It is clear that the claim for $p=0$ holds. We consider the case $p>0$. The third equation $$f_2(1,m^2,x,y)=-y^{2p+1}\frac {(1-\frac x y)}{(1-xy)}=1$$ implies that $$y^{2p+1}+1-y^{2p}x-xy=0,$$ which can be changed to $$\begin{aligned}
0&=&(y+1)(y^{2p}-y^{2p-1}+y^{2p-2}- \cdots +1-xy(y^{2p-2}-y^{2p-3}+\cdots +1))\\
&=&(y+1)\{(y^2+1-(1+x)y)(y^{2(p-1)}+y^{2(p-2)}+\cdots+y^2+1) \\
& &\hspace{2truecm} -(1-x)(y^{2(p-1)}+y^{2(p-2)}+\cdots+y^2)\}.
\end{aligned}$$ From the equation ([\[eqn:y\]](#eqn:y){reference-type="ref" reference="eqn:y"}), we can get $$(y+1)(1-x)H_p(m,x,y)=0,$$ where $H_0(m,x,y)=1$ and for $p \ge 1$, $$\begin{aligned}
& &H_p(m,x,y)\\
& &=\frac y {m^2}(m^4-xm^2+1)(y^{2(p-1)}+y^{2(p-2)}+\cdots+y^2+1)
              -(y^{2(p-1)}+y^{2(p-2)}+\cdots+y^2).
\end{aligned}$$

To prove the theorem for $p>  0$, we need

::: lem
[]{#lem:key label="lem:key"} We have $H_p(m,x,y)=y^p h_p(m,x)$, where for $p\ge 2$, $h_p(m,x)$ is given recursively by $$h_p(m,x)=\frac a {m^2} h_{p-1}(m,x)-h_{p-2}(m,x)$$ with $a=m^4-xm^4+x^2m^2+m^2+1-x$, $h_0(m,x)=1$, $h_1(m,x)=\frac b {m^2}$, and $b=m^4-xm^2+1$.
:::

*Proof of lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}* We show by induction on $p$. When $p=1$, it follows that $H_1(m,x,y)=\frac y {m^2}(m^4-xm^2+1)=y h_1(m,x)$. In the case $p=2$, we obtain that $$\begin{aligned}
H_{2}(m,x,y)& =& H_1(m,x,y)+\frac {yb} {m^2} y^2-y^2 \\
              & =& yh_1(m,x)+y^3 h_1(m,x)-y^2\\
              & =& y (h_1(m,x)(y^2+1)-y)\\
              & =& y (\frac {ay} {m^2}h_1(m,x)-y)\\
              & =& y^2 (\frac {a} {m^2}h_1(m,x)-1)\\
              & =& y^2 (\frac {a} {m^2}h_1(m,x)-h_0(m,x)).\\
\end{aligned}$$ Here we used the equation ([\[eqn:y\]](#eqn:y){reference-type="ref" reference="eqn:y"}) in the fourth equality. Suppose that it holds for $p \le n$. By hypothesis of induction and the definition of $H_p(m,x,y)$, we can obtain $$\begin{aligned}
H_{n+1}(m,x,y)& =& H_n(m,x,y)+\frac {yb} {m^2} y^{2n}-y^{2n}\\
              & =& y^n h_n(m,x,y)+y^2(\frac {yb} {m^2} y^{2(n-1)}-y^{2(n-1)})\\
              & =& y^n h_n(m,x,y)+y^2(H_n(m,x,y)-H_{n-1}(m,x,y))\\
              & =& y^n h_n(m,x,y)+y^2(y^n (h_n(m,x,y)-y^{n-1} h_{n-1}(m,x,y))\\
              &=& y^n((y^2+1) h_n(m,x,y)-y h_{n-1}(m,x,y))\\
              &=& y^n(\frac {a} {m^2}y h_n(m,x,y)-y h_{n-1}(m,x,y))\\
              &=& y^{n+1}(\frac {a} {m^2} h_n(m,x,y)- h_{n-1}(m,x,y)).
\end{aligned}$$ This completes the proof. 0◻

Let us go back to the proof of the theorem. From Lemma [\[lem:key\]](#lem:key){reference-type="ref" reference="lem:key"}, it is clear that $h_p(m,x)$ is in $\mathbb{Z}[m^{\pm 1},x]$. We put $$B_{K_p}(l,m):=(m^2+l)^{2p-1}(m^2)^p h_p(m,\frac {lm^2+1}{m^2+l} ),$$ and then, it is easy to see that $B_{K_p}(l,m)$ satisfies the recursive relation $$B_{K_p}(l,m)=a(m^2+l)^2 B_{K_{p-1}}(l,m)-m^4(m^2+l)^4B_{K_{p-2}}(l,m).$$ By comparing it with the recursive relation ([\[eqn:HS\]](#eqn:HS){reference-type="ref" reference="eqn:HS"}) of $A_{K_p}(l,m)$ by Hoste and Shanahan, and by noting that $a(m^2+l)^2=-l+l^2+2lm^2+m^4+2lm^4+l^2m^4+2lm^6+m^8-lm^8=c$ and $d=m^4(m^2+l)^4$, it is shown that $B_{K_p}(l,m)=A_{K_p}(l,m)$ for $p\ge 0$. In a similar way to the case $p \ge 0$, we can prove the theorem in the case $p<0$. 0◻
