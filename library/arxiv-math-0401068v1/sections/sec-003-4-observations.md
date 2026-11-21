---
doc_id: arxiv-math-0401068v1
doc_title: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS"
section_id: sec-003-4-observations
section_title: "Observations"
section_number: 4
pages: 6-11
source_pdf: 0401068v1.pdf
source_sha256: 8168d7e7f6069978
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.935
doc_brief: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS — @We show that for a twist knot, the A-polynomial can be obtained from recur- rences for the summand in Masbaum’s formula of the"
---
We start with reviewing Wilf-Zeilberger's algorithm. For more details, we refer to [@Garoufalidis/Le:math.GT] and [@Garoufalidis:math.GT]. A disctrete function $F(n,{\bf k})$ is called proper $q$-hypergeometric if it is one of the form $$F(n,{\bf k})=\frac {\prod_{s}(A_s;q)_{a_s n+{\bf b}_s\cdot {\bf k} +c_s}}
                    {\prod_{t}(B_t;q)_{u_t n+{\bf v}_t\cdot {\bf k} +w_t}}
                    q^{A(n,{\bf k})}\xi^{\bf k},$$ where ${\bf k}=(k_1,\ldots,k_r)$, $A_s, B_t \in \mathbb{Q}(q)$, $a_s$, $u_t$ are integers, ${\bf b}_s$, ${\bf k}_s$ are vectors of $r$ integers, $A(n,{\bf k})$ is a quadratic form, $c_s$, $w_t$ are variables and $\xi$ is an $r$ vector of elements in $\mathbb{Q}(q)$, and for $k\ge 0$, $$(A,q)_k:=\left\{
        \begin{array}{ll}
        (1-A)(1-Aq)\cdots (1-Aq^{k-1}) & \mathrm{if} \; k>0,\\
        1                              & \mathrm{if} \; k=0.\\
        \end{array}
        \right.$$

In [@Garoufalidis/Le:math.GT], Garoufalidis and Le proved that the colored Jones polynomial $J_K(n)$ can be written as a multisum $$J_K(n)=\sum_{\bf k=0}^{\infty} F(n,k_1,\ldots,k_r)$$ of a proper $q$-hypergeometric function $F(n,k_1,\ldots,k_r)$, where only finitely many terms in the right hand side are nonzero. Consider the operators $E$, $E_i$, $Q$ and $Q_j$, $(1 \le i,j \le r)$ acting on a discrete function $f: \mathbb{N}^r \to \mathbb{Z}[q^{\pm }]$ by $$\begin{aligned}
 & &(E f)(n,k_1,\ldots,k_r)=f(n+1,k_1,\ldots,k_r), \\
 & &(E_i f)(n,k_1,\ldots,k_r)=f(n,k_1,\ldots,k_{i-1},k_i+1,k_{i+1},\ldots,k_r), \\
 & &(Q f)(n,k_1,\ldots,k_r)=q^n f(n,k_1,\ldots,k_r),\\ 
 & &(Q_j f)(n,k_1,\ldots,k_r)=q^{k_j} f(n,k_1,\ldots,k_r). 
\end{aligned}$$ Then, they satisfy the relations $$\begin{aligned}
& & Q Q_i=Q_i Q,  Q_i Q_j=Q_j Q_i, E E_i=E_i E, E_i E_j=E_j E_i,\\
& & Q_i E=E Q_i,  Q_i E_j= E_j Q_i \; \mathrm{for} \; i\ne j, 
 E Q =q Q E,  E_i Q_i =q Q_i E_i, 
\end{aligned}$$

which are denoted by $(Rel_q)$. The $q$-Weyl algebra $\mathcal A$ is defined to be a noncomutative algebra with presentation $$\mathcal A=\frac {\mathbb{Z}[q^{\pm}]\langle Q, Q_1,\ldots,Q_r,E,E_1,\ldots,E_r \rangle}
           {(Rel_q)}.$$

Wilf and Zeilberger proved that

::: thm
[@Wilf/Zeilberger:INVEM92] Every proper $q$-hypergeometric function $F(n,{\bf k})$ satisfies a ${\bf k}$-free recurrence $$\sum_{i,{\bf j} \in S} \sigma_{i,{\bf j}}(q^n) F(n+i,{\bf k}+{\bf j})=0,
\label{eqn:k-free}$$ where $S$ is a finite set, ${\bf k}=(k_1,\ldots,k_r)$, ${\bf j}=(j_1,\ldots,j_r)$, and $\sigma_{i,{\bf j}}(q^n)$ are polynomials in $q^n$ with coefficients in $\mathbb{Q}(q)$.
:::

Putting $$P=P(E,Q,E_1,\ldots, E_r)
=\sum_{i,{\bf j} \in S} \sigma_{i,{\bf j}}(Q)E^i E^{\bf j},$$ where $E^{\bf j}={E_1}^{j_1}\cdots {E_r}^{j_r}$, the recurrence ([\[eqn:k-free\]](#eqn:k-free){reference-type="ref" reference="eqn:k-free"}) can be written in operator notation as $PF=0$.

Moreover, they showed that any ${\bf k}$-free recurrence can be transformed to $$P=P(E,Q,1,\ldots,1)+\sum_{i=1}^r (E_i-1) R_i(E,Q,E_1, \ldots,E_r).$$ Applying it to $F(n,k_1,\ldots,k_r)$ and summing over ${\bf k} \ge {\bf 0}$ give us $$P(E,Q,1,\ldots,1)J_K(n)=error(n),$$ where $error(n)$ is a sum of a multisum of proper $q$-hypergeometric function with $r-1$ variables. So, repeating the process, we arrive at a homogeneous recursive relation of $J_K(n)$ $$P_1(E,Q)P(E,Q,1,\ldots,1)J_K(n)=0,$$ where $P_1(E,Q)$ is a polynomial in $E$ with coefficients in $\mathbb{Q}(q) [Q]$.

On the other hand, from the fact that $F(n,k_1,\ldots,k_r)$ is proper $q$-hypergeometric, we can write $E F/F=A/B$ and $E_i F/F=A_i/B_i$ for polynomials $A, B, A_i, B_i \in \mathbb{Q}(q) [q^n,q^{k_1},\ldots,q^{k_r}]$. Then, putting $Q=q^n$ and $Q_i=q^{k_i}$, it follows that $(BE-A)F=0$, $(B_iE_i-A_i)F=0$ and that $BE-A$, $B_iE_i-A_i$ generate the annihilation ideal of $F$ in $\mathcal A$. From these generators, the Wilf-Zeilberger's algorithm finds a ${\bf k}$-free recurrence of $F(n,{\bf k})$ and then a recursive relation of the sum of $\sum_{\bf k} F(n,{\bf k})$.

Now, we apply the above algorithm to $J_{K_p}(n)$. From the equations ([\[eqn:f0\]](#eqn:f0){reference-type="ref" reference="eqn:f0"}), ([\[eqn:f1\]](#eqn:f1){reference-type="ref" reference="eqn:f1"}) and ([\[eqn:f2\]](#eqn:f2){reference-type="ref" reference="eqn:f2"}), setting $$\begin{aligned}
 & B=(1-q^{-n-1})(1-q^{-n+k}), & \;A=q^k(1-q^{-n-k-1})(1-q^{-n}),\\
 & B_1=(1-q^{k+l+2})(1-q^{k-l+1}), 
 & A_1=-q^{k+n+2}(1-q^{-n-k-1})(1-q^{-n+k+1})(1-q^k),\\
 & B_2=(q^{2l+1}-1)(1-q^{k+l+2}),
 & A_2=q^{(2p+1)l+2p}(q^{2(l+1)+1}-1)(1-q^{k-l}),
\end{aligned}$$ we have $(BE-A)F=0$, $(B_i E_i-A_i)F=0$ for $i=1,2$, with $Q=q^n$, $Q_1=q^k$ and $Q_2=q^l$. Identifying $Q$ with $m^2$, $E$ with $l$, $Q_1$ with $x$, $Q_2$ with $y$, from the definition of $f_i$ for $i=0,1,2$ in Section 2, we observe that $\varepsilon (BE-A)$ corresponds to $f_0(1,m^2,x,y)-l$ and that $\varepsilon (B_iE_i-A_i)$ with $E_i=1$ corresponds to $f_i(1,m^2,x,y)-1$ for $i=1,2$, where $\varepsilon$ is the evaluation map at $q=1$ defined in [@Garoufalidis:math.GT]. So, our result may support the AJ conjecture.

Nextly, we will present the usage of the mathematica package `qMultiSum.m` with the above theorical background, which is developed by A. Riese [@Riese:JSC03], to obtain inhomogeneous recurrences of the colored Jones polynomial of the knots $5_2$ and $6_1$. We will also relate them to the $A$-polynomial.

The formula in [@Masbaum:AGT03] allows us to write $$J_{5_2}(n)=\sum_{k=0}^{\infty}\sum_{l=0}^k (-1)^{k+1} q^{(3k^2+5k)/2}
       q^{nk}\frac {(q^{-1})_{n+k}(q^{-1})_{n-1}}
                    {(q^{-1})_{n}(q^{-1})_{n-k-1}}
       q^{-l(k+1)}\frac {(q^{-1})_k}{(q^{-1})_{l} (q^{-1})_{k-l}}.$$ We denote the summand by $F(n,k,l)$. Then, the mathematica program soft `qMultiSum.m` computes the ${\bf k}$-free recurrence of $F(n,k,l)$ $$\begin{aligned}
& & -q^{4 + 7n}\left( q - q^n \right)\left( q^2 - q^n \right) 
       \left( q^5 - q^n \right) \left( q + q^n \right) 
       \left( q^2 + q^n \right)        \left( q - q^{2n} \right) 
       \left( q^3 - q^{2n} \right) F(-5 + n,k,l) \\
& &   + q^{1 + 3n}\left( q - q^n \right) \left( q^2 - q^n \right) 
      {\left( q^4 - q^n \right) }^2
     \left( q + q^n \right) \left( q^2 + q^n \right) \left( q^4 + q^n \right)
      \left( q - q^{2n} \right) \left( q^3 - q^{2n} \right) \\
& &  \times \left( q^9 - q^{2n} \right) 
     \left( q^4 - q^n - q^{1 + n} \right) F(-4 + n,-1 + k,-1 + l) \\
& & - q^{9 + 2n}\left( q - q^n \right) \left( q^2 - q^n \right) 
    {\left( q^4 - q^n \right) }^2
     \left( q + q^n \right) \left( q^2 + q^n \right) \left( q^4 + q^n \right) 
     \left( q - q^{2n} \right) \\
& &  \times \left( q^3 - q^{2n} \right) 
     \left( q^9 - q^{2n} \right)  F(-4 + n,-1 + k,l)\\
& & - q^{5 + 6n}\left( 1 + q + q^2 + q^3 + q^4 \right) 
     \left( q - q^n \right) {\left( q^4 - q^n \right) }^2\left( q + q^n \right)      \left( q^4 + q^n \right) \left( q - q^{2n} \right) \\
& &  \times \left( q^3 - q^{2n} \right)  F(-4 + n,k,l)\\
& & + \left( q - q^n \right) \left( q^2 - q^n \right) 
     {\left( q^3 - q^n \right) }^3\left( q^4 - q^n \right) 
     \left( q + q^n \right) 
     \left( q^2 + q^n \right) \left( q^3 + q^n \right) \left( q^4 + q^n \right)      \left( q - q^{2n} \right) \\
& & \times \left( q^3 - q^{2n} \right) 
     \left( q^7 - q^{2n} \right) 
     \left( q^9 - q^{2n} \right) F(-3 + n,-2 + k,-2 + l)\\
& & + q^{2 + 2n}\left( q - q^n \right) {\left( q^3 - q^n \right) }^2
     \left( q^4 - q^n \right) 
     \left( q + q^n \right) \left( q^3 + q^n \right) \left( q^4 + q^n \right) 
     \left( q - q^{2n} \right) \left( q^3 - q^{2n} \right)\\
& &  \times \left( q^9 - q^{2n} \right) 
     \left( q^5 + q^6 + q^{2n} - q^{1 + n} - 2q^{2 + n} - 2q^{3 + n} - q^{4 + n}    \right) F(-3 + n,-1 + k,-1 + l)\\ 
& & - q^{5 + n}\left( q - q^n \right) {\left( q^3 - q^n \right) }^2
     \left( q^4 - q^n \right) \left( q + q^n \right) \left( q^3 + q^n \right) 
     \left( q^4 + q^n \right) \left( q - q^{2n} \right) 
     \left( q^3 - q^{2n} \right) \\
& &  \times 
     \left( q^9 - q^{2n} \right) \left( q^6 + q^{2n} + q^{1 + 2n} \right) 
     F(-3 + n,-1 + k,l)\\
& & - q^{6 + 5n}\left( 1 + q^2 \right) \left( 1 + q + q^2 + q^3 + q^4 \right) 
     \left( q - q^n \right) {\left( q^3 - q^n \right) }^2\left( q + q^n \right)      \left( q^3 + q^n \right) \left( q - q^{2n} \right)\\
& &  \times \left( q^9 - q^{2n} \right) F(-3 + n,k,l)\\
& & - q\left( q - q^n \right) {\left( q^2 - q^n \right) }^3
     \left( q^3 - q^n \right) \left( q^4 - q^n \right) \left( q + q^n \right) 
     \left( q^2 + q^n \right) \left( q^3 + q^n \right) \left( q^4 + q^n \right)      \\
& & \times  \left( q - q^{2n} \right)\left( q^3 - q^{2n} \right) 
     \left( q^7 - q^{2n} \right) 
     \left( q^9 - q^{2n} \right) F(-2 + n,-2 + k,-2 + l)\\
& & + q^{4 + n}\left( q - q^n \right) {\left( q^2 - q^n \right) }^2
    \left( q^4 - q^n \right) 
     \left( q + q^n \right) \left( q^2 + q^n \right) \left( q^4 + q^n \right) 
     \left( q - q^{2n} \right) \left( q^7 - q^{2n} \right)
      \\
& &  \times  \left( q^9 - q^{2n} \right)
     \left( q^5 + q^{2n} - q^{1 + n} - 2q^{2 + n} - 2q^{3 + n} - q^{4 + n}
      + q^{1 + 2n} \right) F(-2 + n,-1 + k,-1 + l)\\
& & - q^{3 + 2n}\left( q - q^n \right) {\left( q^2 - q^n \right) }^2
    \left( q^4 - q^n \right) \left( q + q^n \right) \left( q^2 + q^n \right)
     \left( q^4 + q^n \right) 
     \left( q - q^{2n} \right) \left( q^7 - q^{2n} \right)\\
& &  \times \left( q^9 - q^{2n} \right) 
     \left( q^4 + q^5 + q^{2n} \right) F(-2 + n,-1 + k,l)\\
& & - q^{7 + 4n}\left( 1 + q^2 \right) \left( 1 + q + q^2 + q^3 + q^4 \right) 
     {\left( q^2 - q^n \right) }^2\left( q^4 - q^n \right) 
     \left( q^2 + q^n \right) 
     \left( q^4 + q^n \right) \left( q - q^{2n} \right) \\
& &  \times \left( q^9 - q^{2n} \right)  F(-2 + n,k,l)\\
& & - q^{6 + n}{\left( q - q^n \right) }^2\left( q + q^2 - q^n \right) 
     \left( q^3 - q^n \right) \left( q^4 - q^n \right) \left( q + q^n \right) 
     \left( q^3 + q^n \right) \left( q^4 + q^n \right) 
     \left( q - q^{2n} \right) \\
& &  \times \left( q^7 - q^{2n} \right) \left( q^9 - q^{2n} \right) 
     F(-1 + n,-1 + k,-1 + l) \\
& &- q^{5 + 3n}{\left( q - q^n \right) }^2\left( q^3 - q^n \right) 
     \left( q^4 - q^n \right) 
     \left( q + q^n \right) \left( q^3 + q^n \right) \left( q^4 + q^n \right) 
     \left( q - q^{2n} \right) \left( q^7 - q^{2n} \right)\\
& &  \times \left( q^9 - q^{2n} \right)  F(-1 + n,-1 + k,l)\\
& & - q^{8 + 3n}\left( 1 + q + q^2 + q^3 + q^4 \right) 
     {\left( q - q^n \right) }^2\left( q^4 - q^n \right) \left( q + q^n \right)      \left( q^4 + q^n \right) \left( q^7 - q^{2n} \right) \\
& &  \times \left( q^9 - q^{2n} \right) F(-1 + n,k,l)\\
& & + q^{9 + 2n}\left( q^3 - q^n \right) \left( q^4 - q^n \right) 
     \left( -1 + q^n \right) \left( q^3 + q^n \right) \left( q^4 + q^n \right) 
     \left( q^7 - q^{2n} \right) \\
& & \times \left( q^9 - q^{2n} \right) F(n,k,l) = 0.
\end{aligned}$$ Moreover, it can be converted into the inhomogeneous recursive relation of the colored Jones polynomial of the knot $5_2$ $$\begin{aligned}
& &q^{9 + 7n} J_{5_2}(n)\\
& &+ \frac {{\left( -1 + q^{1 + n} \right) }^2\left( 1 + q^{1 + n} \right)}
           {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
            \left( 1 + q^{3 + n} \right)} \times \\
& & q^{5 + 2n}\left( 1 - q^{1 + n} - q^{1 + 2n} + q^{2 + 2n} + q^{3 + 2n} - q^{6 + 2n}
            + q^{2 + 3n} + q^{7 + 3n} + q^{5 + 4n} + q^{6 + 4n} + 2q^{7 + 4n}
    \right.\\
& & \left.- q^{8 + 4n} - q^{9 + 4n} - q^{8 + 5n} + q^{9 + 6n} + q^{10 + 6n} 
     \right) J_{5_2}(1 + n)\\
& & + \frac {{\left( -1 + q^{2 + n} \right) }^2\left( 1 + q^{2 + n} \right)
              \left( -1 + q^{1 + 2n} \right) }
            {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
             \left( 1 + q^{3 + n} \right) \left( -1 + q^{7 + 2n} \right)}
             \times  \\
& &  q\left( -1 + 2q^{2 + n} + q^{2 + 2n} - q^{4 + 2n} + q^{6 + 2n} 
            + q^{7 + 2n} - q^{4 + 3n} + q^{5 + 3n} + 3q^{6 + 3n} + 
            2q^{7 + 3n} - q^{8 + 3n} 
     \right.\\
& & - 2q^{9 + 3n} + q^{6 + 4n} - 2q^{8 + 4n} 
            - 2q^{9 + 4n} + q^{11 + 4n} - 
       q^{13 + 4n} - q^{8 + 5n} + 3q^{10 + 5n} + 3q^{11 + 5n}  
     \\
& &  - 3q^{13 + 5n}- 2  q^{14 + 5n} + q^{15 + 5n} + q^{10 + 6n} 
    + q^{11 + 6n} - q^{13 + 6n}      
     + 2q^{15 + 6n} + q^{16 + 6n} + q^{14 + 7n}  \\
& &  \left. + 3q^{15 + 7n}+ 2q^{16 + 7n} 
      - q^{17 + 7n} - q^{18 + 7n} - q^{17 + 8n} - q^{18 + 8n} + q^{20 + 9n} 
      \right) J_{5_2}(2 + n)\\
& & - \frac {\left( -1 + q^{1 + n} \right) \left( 1 + q^{1 + n} \right) 
            {\left( -1 + q^{3 + n} \right) }
             \left( -1 + q^{1 + 2n} \right)} 
            {\left( 1 + q^{n} \right)\left( -1 + q^{4 + n} \right) 
             \left( 1 + q^{4 + n} \right) \left( -1 + q^{7 + 2n} \right)}
             \times \\
& &  \left( -1 + q^{2 + n} + q^{3 + n} - q^{4 + 2n} - 3q^{5 + 2n} - 2q^{6 + 2n}             +q^{7 + 2n} + q^{8 + 2n} - q^{5 + 3n} - q^{6 + 3n} + q^{8 + 3n}
     \right.\\
& &  - 2q^{10 + 3n} - q^{11 + 3n} + q^{8 + 4n} - 3q^{10 + 4n} 
            - 3q^{11 + 4n} + 3q^{13 + 4n} + 2q^{14 + 4n} - q^{15 + 4n} 
            - q^{11 + 5n} \\
& &   + 2q^{13 + 5n} + 2q^{14 + 5n}
    - q^{16 + 5n} + q^{18 + 5n} + q^{14 + 6n} - q^{15 + 6n} 
            - 3q^{16 + 6n} - 2q^{17 + 6n} + q^{18 + 6n} \\
& &   \left.+ 2q^{19 + 6n}
            - q^{17 + 7n} + q^{19 + 7n} - q^{21 + 7n} - q^{22 + 7n} 
            - 2q^{22 + 8n} + q^{25 + 9n} \right) 
     J_{5_2}(3 + n)\\
& &  + \frac {\left( -1 + q^{1 + n} \right) 
     \left( 1 + q^{1 + n} \right) \left( -1 + q^{4 + n} \right) 
     \left( -1 + q^{1 + 2n} \right) 
     \left( -1 + q^{3 + 2n} \right)}
     {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
     \left( 1 + q^{3 + n} \right)  \left( -1 + q^{7 + 2n} \right)
     \left( -1+q^{9 + 2n} \right)} \times \\
& &  q^{1 + n}
     \left( 1 + q - q^{4 + n} + q^{6 + 2n}
      + q^{7 + 2n} + 
       2q^{8 + 2n} - q^{9 + 2n} - q^{10 + 2n} + q^{8 + 3n} + q^{13 + 3n}
     \right.\\
& &   \left. - 
       q^{12 + 4n} + q^{13 + 4n} + q^{14 + 4n} - q^{17 + 4n} - q^{17 + 5n}
        + q^{21 + 6n}
       \right) J_{5_2}(4 + n)\\
& & + \frac {\left( -1 + q^{1 + n} \right)\left( 1 + q^{1 + n} \right) 
     \left( -1 + q^{2 + n} \right) \left( 1 + q^{2 + n} \right) 
     \left( -1 + q^{5 + n} \right) 
     \left( -1 + q^{1 + 2n} \right)\left( -1 + q^{3 + 2n} \right) }
     {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
     \left( 1 + q^{3 + n} \right) \left( -1 + q^{4 + n} \right) 
     \left( 1 + q^{4 + n} \right) \left( -1 + q^{7 + 2n} \right)
     \left( -1+q^{9 + 2n} \right)}\times \\
& &     q^{4 + 2n} J_{5_2}(5 + n)
    = G(n), 
\end{aligned}$$ where $G(n)$ is a sum of sums of proper $q$-hypergeometric function. Setting $q=1$, and replacing $J_{5_2}(i + n)$ by $l^i$ and $q^n$ by $m^2$, the denominators cancell, the left hand side is changed to $$\begin{aligned}
& & (1+m^2l)^2 \times \\
& & \{m^{14}+l(m^4-m^6+2 m^{10}+2 m^{12}-m^{14})
-l^2(-1+2m^2+2m^4-m^8+m^{10})+l^3\},
\end{aligned}$$ and the second factor is equal to the $A$-polynomial of the knot $5_2$. So, this supports the AJ conjecture for the knot $5_2$.

Furthermore, the colored Jones polynomial of the knot $6_1$ can be written $$J_{6_1}(n)=\sum_{k=0}^{\infty}\sum_{l=0}^k q^{-k^2-k}
       q^{nk}\frac {(q^{-1})_{n+k}(q^{-1})_{n-1}}
                    {(q^{-1})_{n}(q^{-1})_{n-k-1}}
       q^{l(k+1)}\frac {(q)_k}{(q)_{l} (q)_{k-l}}.$$ Using `qMultiSum.m` again, we can obtain the inhomogeneous recursive relation of $J_{6_1}(n)$ $$\begin{aligned}
& &q^{8 + 4n} J_{6_1}(n) \\
& & - \frac {{\left( -1 + q^{1 + n} \right) }^2\left( 1 + q^{1 + n} \right) }
            {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
             \left( 1 + q^{3 + n} \right)}
      \times \\
& & q^{5 + 2n}\left( 1 + q - 2q^{2 + n} - q^{3 + n} - q^{1 + 2n} - 
       q^{2 + 2n} + q^{3 + 2n} - q^{6 + 2n} - q^{7 + 2n} + q^{3 + 3n}
        - q^{5 + 3n}\right. \\
& &   \left. - q^{6 + 3n} - q^{7 + 3n} + q^{8 + 3n} - q^{4 + 4n} 
         + q^{7 + 4n} + q^{8 + 4n} - 
       q^{9 + 4n} - q^{9 + 5n} + q^{10 + 6n} \right) 
       J_{6_1}(1 + n) \\
& & - \frac {{\left( -1 + q^{2 + n} \right) }^2\left( 1 + q^{2 + n} \right)
             \left( -1 + q^{1 + 2n} \right)}
            {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
             \left( 1 + q^{3 + n} \right)\left( -1 + q^{7 + 2n} \right) }
       \times \\
& &   q \left( -1 + 2q^{2 + n} + q^{3 + n} + q^{2 + 2n} + q^{3 + 2n} 
      - q^{4 + 2n} - 2q^{5 + 2n} + q^{6 + 2n} + q^{7 + 2n} - 2q^{4 + 3n}
       - q^{5 + 3n} 
      \right.\\
& &  + 2q^{6 + 3n} + 3q^{7 + 3n} - 2q^{9 + 3n} - q^{10 + 3n} - q^{5 + 4n} 
     + q^{6 + 4n} + q^{7 + 4n} - 2q^{8 + 4n} - 5q^{9 + 4n} - 3q^{10 + 4n} 
     \\
& &  + q^{12 + 4n} - q^{13 + 4n} - 2q^{8 + 5n} - 3q^{9 + 5n} + 3q^{11 + 5n} 
     + q^{12 + 5n} 
     - 2q^{13 + 5n} - 3q^{14 + 5n} + 2q^{11 + 6n}\\ 
& &  + q^{12 + 6n}- 2q^{13 + 6n} - 2q^{14 + 6n} 
     + 2q^{16 + 6n} - q^{13 + 7n} + 2q^{15 + 7n} + 3q^{16 + 7n} - q^{18 + 7n}\\
& &    \left. - 2q^{18 + 8n} + q^{20 + 9n} \right) 
      J_{6_1}(2 + n) \\
& & + \frac {\left( -1 + q^{1 + n} \right) \left( 1 + q^{1 + n} \right) 
             \left( -1 + q^{3 + n} \right) \left( -1 + q^{1 + 2n} \right) }
            {\left( -1 + q^n \right) \left( -1 + q^{4 + n} \right) 
             \left( 1 + q^{4 + n} \right) \left( -1 + q^{7 + 2n} \right) } 
      \times \\
& &   \left( -1 + 2q^{3 + n} + q^{3 + 2n} - 2q^{5 + 2n} - 3q^{6 + 2n} 
       + q^{8 + 2n} - 2q^{6 + 3n} - q^{7 + 3n} + 2q^{8 + 3n} + 2q^{9 + 3n} 
       \right.\\
& &   - 2q^{11 + 3n}+ 2q^{8 + 4n} + 3q^{9 + 4n} - 3q^{11 + 4n} - q^{12 + 4n} 
      + 2q^{13 + 4n}
      + 3q^{14 + 4n} + q^{10 + 5n} - q^{11 + 5n}   \\
&&    - q^{12 + 5n}+ 2q^{13 + 5n} + 5q^{14 + 5n}+ 3q^{15 + 5n} - q^{17 + 5n}
       + q^{18 + 5n}  + 2q^{14 + 6n} + q^{15 + 6n} - 2q^{16 + 6n} \\
& &  - 3q^{17 + 6n}+ 2q^{19 + 6n} + q^{20 + 6n} - q^{17 + 7n} - q^{18 + 7n}
     + q^{19 + 7n} + 2q^{20 + 7n} - q^{21 + 7n} - q^{22 + 7n}  
     \\
& &  \left. - 2q^{22 + 8n}- q^{23 + 8n} + q^{25 + 9n} \right) 
     J_{6_1}(3 + n) \\
& & - \frac {\left( -1 + q^{1 + n} \right) \left( 1 + q^{1 + n} \right) 
             \left( -1 + q^{4 + n} \right)\left( -1 + q^{1 + 2n} \right) 
             \left( -1 + q^{3 + 2n} \right) }
            {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
             \left( 1 + q^{3 + n} \right) \left( -1 + q^{7 + 2n} \right) 
            \left( -1 + q^{9 + 2n} \right) } \times \\
& &  q^{2 + n}
     \left( 1 - q^{4 + n} - q^{4 + 2n} + q^{7 + 2n} + q^{8 + 2n} 
     - q^{9 + 2n} + q^{8 + 3n} - q^{10 + 3n} - q^{11 + 3n} - q^{12 + 3n} 
     \right.\\
& &   + q^{13 + 3n} - q^{11 + 4n} - q^{12 + 4n} + q^{13 + 4n} - q^{16 + 4n} 
     - q^{17 + 4n} - 2q^{17 + 5n} - q^{18 + 5n}
     \\
& & \left.  + q^{20 + 6n} + q^{21 + 6n} \right) 
    J_{6_1}(4 + n) \\
& & + \frac {\left( -1 + q^{1 + n} \right) \left( 1 + q^{1 + n} \right) 
             \left( -1 + q^{2 + n} \right) \left( 1 + q^{2 + n} \right) 
             \left( -1 + q^{5 + n} \right) \left( -1 + q^{1 + 2n} \right)
             \left( -1 + q^{3 + 2n} \right)}
            {\left( -1 + q^n \right) \left( -1 + q^{3 + n} \right) 
             \left( 1 + q^{3 + n} \right) \left( -1 + q^{4 + n} \right)
             \left( 1 + q^{4 + n} \right) \left( -1 + q^{7 + 2n} \right) 
              \left( -1 + q^{9 + 2n} \right)} \times \\
& &     q^{18 + 5n}J_{6_1}(5 + n) = G'(n), 
\end{aligned}$$ where $G'(n)$ is a sum of sums of proper $q$-hypergeometric function. Setting $q=1$, and replacing $J_{6_1}(i + n)$ by $l^i$ and $q^n$ by $m^2$, the left hand side is changed to $$\begin{aligned}
& & (1+m^2l) 
    \{ m^{8}+l(-2m^4+3m^6+3m^8+2 m^{14}-m^{16})\\
& &     +l^2(1-3m^2-m^4+3m^6+6m^8+3m^{10}-m^{12}-3m^{14}+m^{16})\\
& &     +l^3(-1+m^2+m^4+3m^{10}+3m^{12}-2m^{14})+m^8l^4\},
\end{aligned}$$ and the second factor coincides with the A-polynomial of the knot $6_1$.

Finally, we discuss our result in terms of *Volume conjecture* due to Kashaev, H.Murakami and J.Murakami. (see [@Kashaev:LETMP97],[@Murakami/Murakami:volume]). Let $K$ be a hyperbolic knot in $S^3$ and $M_K$ the complement of $K$. We write $\hat{J}_K(n)$ for $J_K(n)$ evaluated at $q=\exp\frac{ 2\pi \sqrt{-1}} n$. Then, *Volume conjecture* is

::: conj
$$2\pi\lim_{n\to \infty} \frac {\log|\hat{J}_K(n)|}{n}=Vol(M_K),$$ where $Vol(M_K)$ is the hyperbolic volume of $M_K$.
:::

From the formula of $J_{K_p}(n)$ given by Masbaum, we have $$\hat{J}_{K_p}(n)=\sum_{k=0}^{\infty}\sum_{l=0}^k (-1)^{k+l} q^{k(k+3)/2}
        (q)_k(q^{-1})_k
       q^{l(l+1)p+l(l-1)/2}\frac {(q)_{2l+1}}  {(q)_{2l}}
       \frac {(q)_k}{(q)_{k+l+1} (q)_{k-l}}.$$ Computing the optimistic limit [@HMurakami:RIMS00] of $\hat{J}_K(n)$, it is conjectured that there exists a solution $(x_0,y_0)$ to the two equations $$f_1(1,1,x,y)=1, \; f_2(1,1,x,y)=1
\label{eqn:critical}$$ such that $$Vol(M_K)=3D(x_0)-D(x_0y_0)-D(\frac {x_0} {y_0}),$$ where $f_i$ is the same notation as in Section 2, and $D(z)=\mathrm{Im }(\mathrm{Li}_2(z))+\log |z| \arg (1-z)$ with $\mathrm{Li}_2(z)=-\int_{0}^z \frac {\log (1-w)} w dw$. By using Mathematica 4 and Maple V, we can numerically see that for $p=-1, 2,-2$, this conjecture is true.

In [@Yokota:volume], Y.Yokota introduced a way to construct an ideal triangulation of the complement $M_K$ of $K$ associated to Kashaev's $R$-matrices, and gave a sketch proof of *Volume conjecture*. Moreover, in [@Yokota:IIS03], he explained a method to calculate the $A$-polynomial of $K$ from the triangulation of $\partial M_K$ in [@Yokota:volume]. We hope to find a geometrical interpretation of our method to obtain the $A$-polynomial, comparing with Yokota's method.
