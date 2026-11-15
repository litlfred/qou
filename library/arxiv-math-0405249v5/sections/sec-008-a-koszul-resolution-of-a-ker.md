---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL(2)"
section_id: sec-008-a-koszul-resolution-of-a-ker
section_title: "a koszul resolution of A/ ker"
section_number: null
pages: 10-20
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
doc_brief: "Twisted homology of quantum SL(2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra o f the quan- tum SL(2) group"
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.918
---
Using the above facts it is easy to see that $\mathrm{ker}\,\varepsilon$ is generated as both a left and right $\mathcal{A}$-module by $x_{1,1}:=a-1,\; x_{1,2}:=b, \;x_{1,3}:=c$. For these elements there exists a Koszul complex $(K_\ast,k)$, $K_n:=K_n(x_{i,j},\mathcal{A})$, in the sense of section [\[koszull\]](#koszull){reference-type="ref" reference="koszull"} with the $x_{i,j}$ given by $$\left(\begin{array}{ccc} 
    a-1 & b & c\\
    q^{-1}a-1 & b & c\\
    q^{-2}a-1 & b & c 
    \end{array}\right).$$

We check by explicit calculation that this Koszul complex is acyclic:

::: prop
[]{#resolution label="resolution"} The left $\mathcal{A}$-module $\mathcal{A}/\mathrm{ker}\, \varepsilon$ possesses a resolution $(K_\ast,k)$ of the form $$0 \rightarrow \mathcal{A}\rightarrow^{k_3} \mathcal{A}^3 \rightarrow^{k_2} \mathcal{A}^3
    \rightarrow^{k_1} \mathcal{A}\rightarrow \mathcal{A}/ \mathrm{ker}\,\varepsilon \rightarrow 0.$$ The augmentation map $K_0=\mathcal{A}\rightarrow k = \mathcal{A}/ \mathrm{ker}\,\varepsilon$ is given by the counit $\varepsilon$. The left $\mathcal{A}$-module morphisms $k_n : K_n \rightarrow K_{n-1}$, $n=1,2,3$, are given by $$k_1 : 
\left(\begin{array}{c} 1 \\0 \\ 0 \end{array} \right),
\left(\begin{array}{c} 0 \\1 \\ 0 \end{array} \right),
\left(\begin{array}{c} 0 \\0 \\ 1 \end{array} \right) 
\mapsto a-1,b,c$$ $$k_2 : 
\left(\begin{array}{c} 1 \\0 \\ 0 \end{array} \right),
\left(\begin{array}{c} 0 \\1 \\ 0 \end{array} \right),
\left(\begin{array}{c} 0 \\0 \\ 1 \end{array} \right) 
\mapsto
\left(\begin{array}{c}
    b\\1-q^{-1}a\\0\end{array}\right),
    \left(\begin{array}{c}
    c\\0\\1-q^{-1}a\end{array}\right),
    \left(\begin{array}{c} 0 \\ c\\ -b\end{array}\right),$$ $$\begin{aligned}
 k_3 : 1 \mapsto 
    \left(\begin{array}{c} c \\ -b \\ q^{-2}a-1 \end{array}\right).\nonumber
\end{aligned}$$
:::

::: pf
It follows from Proposition [\[serrek\]](#serrek){reference-type="ref" reference="serrek"} (or directly) that this is a complex. Let $(x,y,z)^t \in \mathrm{ker}(k_1)$, i.e. $x(a-1)+yb+zc=0$. Then $\pi_{bc}(x(a-1))=0$. Using the $\mathbb{Z}$-grading we have $\pi_{bc}(x)=0$, so $x=x'b+x''c$. Subtracting $k_2(x',x'' ,0)^t$ from $(x,y,z)^t$ we get a new element of $\mathrm{ker}(k_1)$ with $x=0$. Hence $\pi_c(y)=\pi_b(z)=0$, so $y=y'c$, $z=z'b$, $z'=-y'$ and this element is a multiple of $k_2(0,0,1)^t$. In a similar manner $$x \left(\begin{array}{c}
    b\\1-q^{-1}a\\0\end{array}\right)+
    y \left(\begin{array}{c}
    c\\0\\1-q^{-1}a\end{array}\right)+
    z   
    \left(\begin{array}{c} 0 \\ c\\ -b\end{array}\right) = 0$$ implies $x=x'c$, $y=-x'b$, $x'(q^{-2}a-1)=z$ for some $x' \in \mathcal{A}$.
:::

::: cor
[]{#coro label="coro"} If $n>3$, then $HH_n^\sigma(\mathcal{A})=0$ for all automorphisms $\sigma$.
:::

The morphism between the resulting short complex ${}_\sigma\mathcal{A}' \otimes_\mathcal{A}K_\ast$ and the standard complex for $\mathrm{Tor}_n^\mathcal{A}({}_\sigma\mathcal{A}', k)$ yielding an isomorphism in homology is given explicitly by:\

1.   The map $\varphi_0 : \mathcal{A}\rightarrow C_0=\mathcal{A}$ is the identity.\

2.   The map $\varphi_1 : \mathcal{A}^3 \rightarrow C_1=\mathcal{A}^{\otimes 2}$ is given by $$\label{phi_1}
        \left(\begin{array}{c} x \\ y \\ z \end{array}\right) \mapsto
        (x,a-1)+(y,b) + (z,c).$$ Since $d(x,1,1) = (x,1)$ for any $x$, we have $[(x, a-1)] = [(x,a)]$ in $\mathrm{Tor}_1^\mathcal{A}({}_\sigma\mathcal{A}',k)$.\

3.   The map $\varphi_2 : \mathcal{A}^3 \rightarrow C_2=\mathcal{A}^{\otimes 3}$ is given by $$\left(\begin{array}{c} x \\ y \\ z \end{array}\right) \mapsto
        (x,b,a-1) - (x, q^{-1}a-1, b) +$$ $$\label{phi_2}
    + (y,c,a-1) - (y, q^{-1}a-1, c) + (z,c,b) - (z,b,c)$$\

4.   Finally, the map $\varphi_3 : \mathcal{A}\rightarrow C_3=\mathcal{A}^{\otimes 4}$ in the complex for the $\mathrm{Tor}$-groups is given by $x \mapsto x \otimes v$, where $$v = -(q^{-2}a-1, b, c) + (q^{-2}a-1, c , b) - (c, q^{-1}a-1, b) +$$ $$\label{phi_3}
        +(c, b, a-1) -
        (b,c,a-1) +
        (b, q^{-1}a-1, c).$$

One sees by direct computation that this is a morphism of complexes, and by the comparison theorem (see [@weibel], Theorem 2.2.6) this is a quasi-isomorphism.

## Computation of $HH_n^\sigma(\mathcal{A})$, $n \leq 3$

All automorphisms arising from finite-dimensional calculi are of the form $\sigma=\sigma_{\lambda, \mu}$, and from now on we will only consider automorphisms of this type. In fact, they are of the form $\sigma(x)=$ $\sigma_{mod}^{-1} (f \ast x)$, where $f$ is a functional in the dual Hopf algebra $\mathcal{A}^\circ$ acting on $x$ by $f \ast x=\sum f(x_{(2)})x_{(1)}$ (see Theorems 4.1, 4.3 and 4.8 in [@kmt]). It is clear that such automorphisms do not exchange $b$ and $c$. By Corollary [\[crucial_isomorphism\]](#crucial_isomorphism){reference-type="ref" reference="crucial_isomorphism"} we have $HH_n^\sigma(\mathcal{A}) \cong H_n (\mathcal{A}, {}_\sigma\mathcal{A})$, and the homologies $H_* (\mathcal{A},{}_\sigma\mathcal{A})$ can be calculated via our noncommutative Koszul resolution.

So let $\lambda,\mu \in k^\times$ and $\sigma=\sigma_{\lambda, \mu}$. We apply ${}_\sigma\mathcal{A}'  \otimes_\mathcal{A}\cdot$ to our resolution and obtain the complex $(F_\ast,f)$ of vector spaces $$\label{complex}
    0 \rightarrow \mathcal{A}\rightarrow^{f_3} \mathcal{A}^3 \rightarrow^{f_2} 
    \mathcal{A}^3 \rightarrow^{f_1} \mathcal{A}\rightarrow 0,$$ with morphisms $f_n$ given by $$\begin{aligned}
&&
 f_1 \left(\begin{array}{c} x_1 \\ y_1 \\ z_1 \end{array}\right) 
    = x_1 \blacktriangleleft a- x_1+
    y_1 \blacktriangleleft b+ z_1 \blacktriangleleft c,\nonumber\\
&&
 f_2 \left(\begin{array}{c} x_2 \\ y_2 \\ z_2 \end{array}\right)  
    = \left(\begin{array}{c}
    x_2 \blacktriangleleft b + y_2 \blacktriangleleft c\\
    x_2 - q^{-1}x_2 \blacktriangleleft a + z_2 \blacktriangleleft c\\
    y_2 - q^{-1}y_2 \blacktriangleleft a - z_2 \blacktriangleleft b 
    \end{array}\right),\nonumber\\
&&
\label{defn_f_3}
\label{defn_f_2}
\label{defn_f_1}
 f_3 (x_3 ) = 
    \left(\begin{array}{c} x_3 \blacktriangleleft c 
    \\ -x_3 \blacktriangleleft b \\ q^{-2}x_3
    \blacktriangleleft a-x_3 \end{array}\right).
\end{aligned}$$ Writing $\varepsilon_{i,j,k}:=q^{i+j+k+2} \lambda \mu^{-1}$ we have $$\begin{aligned}
\label{sindwiederda}
\label{right_action_of_a_b_c}
    \lambda q^{j+k} e_{i,j,k} \blacktriangleleft a 
&=& e_{i,j,k} + q^{-1-i-|i|}(1-\varepsilon_{|i|,j,k}) e_{i,j+1,k+1},\nonumber\\
    \lambda^{-1} e_{i,j,k} \blacktriangleleft b 
&=& (1-\varepsilon_{i,j,k}^{-1}) 
    e_{i+1,j+1,k} \nonumber\\
&&+\left\{
    \begin{array}{ll}
    0\quad & : i \ge 0\\
    q^{-2i-1}(1-\varepsilon_{-i,j,k}^{-1})
    e_{i+1,j+2,k+1} \quad & : i<0
    \end{array}\right.,\nonumber\\
    \lambda e_{i,j,k} \blacktriangleleft c 
&=& (1-\varepsilon_{-i,j,k})e_{i-1,j,k+1} \nonumber\\
&&+\left\{
    \begin{array}{ll}
    q^{-2i+1}(1-\varepsilon_{i,j,k})
    e_{i-1,j+1,k+2} \quad & : i>0\\
    0 \quad & : i \le 0
    \end{array}\right.
\end{aligned}$$ For $q=\lambda=\mu=1$ we have $f_n=0$ and we recover the Hochschild-Kostant-Rosenberg theorem for $SL(2,k)$. The cotangent bundle of an algebraic group is trivial, so in the classical case $HH_n(\mathcal{A})=\mathcal{A}\otimes \Lambda^n k^3$. It is clear, however, that for $q \neq 1$ there is no twisting automorphism for which this happens.

The calculations lead to five distinct cases:

1.   []{#case_1 label="case_1"} $\mu=1$, $\lambda\notin \{ q^{-(N+2)} \}_{ N \geq 0}$, and $\mu \neq 1$, $\lambda=1$.

2.   []{#case_2 label="case_2"} $\mu =1$, $\lambda= q^{-(N+2)}$, $N \geq 0$.

3.   []{#case_3 label="case_3"} $\mu = q^{M+1}$, $\lambda=q^{-(N+1)}$, $M$, $N \geq 0$.

4.   []{#case_4 label="case_4"} $\mu = q^{-(M+1)}$, $\lambda= q^{-(N+1)}$, $M$, $N \geq 0$.

5.   []{#case_5 label="case_5"} $\mu = q^{\pm(M+1)}$, $M \geq 0$, $\lambda\notin q^{-\mathbb{N}}$, and $\mu \notin q^\mathbb{Z}$, $\lambda\neq 1$.

The computation of $HH_0^\sigma(\mathcal{A})$ and $HH_1^\sigma(\mathcal{A})$ is done most easily "by hand\" using the original Hochschild complex, but for $HH_2^\sigma(\mathcal{A})$ and $HH_3^\sigma(\mathcal{A})$ the calculations are done via the Koszul resolution.

## $HH_0^\sigma(\mathcal{A})$

We calculate from first principles the twisted Hochschild homology $HH_0^\sigma(\mathcal{A})$ for all automorphism $\sigma= \sigma_{\lambda,\mu}$. We start with the observation that: $$b(a_1,a_2a_3)=
    b(a_1a_2,a_3)+
    b(\sigma(a_3)a_1,a_2) \quad \forall \; a_1,\, a_2, \, a_3 \in\mathcal{A}$$ So for any $a_1$, $a_2 \in\mathcal{A}$, there exist $x_a$, $x_b$, $x_c$, $x_c \in \mathcal{A}$ such that $$b( a_1 , a_2 ) = b[ (x_a, a) + (x_b ,b) + (x_c, c) + (x_d ,d)]$$ Hence the image of the twisted Hochschild boundary is spanned by $$\begin{aligned}
    A_{i,j,k}
&:=& e_{i,j,k}a - \lambda a e_{i,j,k} \nonumber\\ 
&=& (q^{-(j+k)}- \lambda) e_{i+1,j,k} \nonumber\\ 
&& + \left\{\begin{array}{ll}
     0 & : i \ge 0\\
    (q^{-(j+k+1)}- \lambda q^{-2i-1}) e_{i+1,j+1,k+1}  & : i<0
    \end{array}\right. \nonumber\\ 
    B_{i,j,k}
&:=& e_{i,j,k} b - \mu b e_{i,j,k} = (1 - \mu q^{-i}) e_{i,j+1,k},\nonumber\\
    C_{i,j,k}
&:=&e_{i,j,k} c - \mu^{-1} c e_{i,j,k} =    (1-\mu^{-1} q^{-i}) e_{i,j,k+1},\nonumber\\
    D_{i,j,k}
&:=& e_{i,j,k} d - \lambda^{-1} d e_{i,j,k} \nonumber\\  
&=& (q^{j+k}- \lambda^{-1}) e_{i-1,j,k} \nonumber\\
&& +     \left\{\begin{array}{ll}
     0 \quad & : i \le 0\\
    (q^{j+k+1}- \lambda^{-1}q^{-2i+1}) e_{i-1,j+1,k+1} \quad & :  i>0
    \end{array}\right..\nonumber
\end{aligned}$$ For given $(i,j,k)$, the elements $B_{i,j,k}$ and $C_{i,j,k}$ both vanish if and only if $i=0$ and $\mu=1$. Therefore, for all $\lambda$, $\mu$, $\mathrm{im}\, b$ contains the basis elements $$\label{diesinddrin}
    e_{i,j,k},\quad i \neq 0,\; j,k>0.$$ Omitting the span of these terms from the above list of generators we see that $\mathrm{im}\, b$ is spanned by ([\[diesinddrin\]](#diesinddrin){reference-type="ref" reference="diesinddrin"}) together with $$\begin{aligned}
&& A_{-1,j,k} = (q^{-(j+k)}- \lambda) e_{0,j,k} +
    (q^{-(j+k+1)}- \lambda q) e_{0,j+1,k+1} 
    \nonumber\\ 
&& \tilde A_{i,j,k} = (q^{-(j+k)}- \lambda) e_{i+1,j,k},\quad
    i \neq -1 \nonumber\\
&& B_{i,j,0} = (1 - \mu q^{-i}) e_{i,j+1,0},\quad
    B_{0,j,k} = (1 - \mu ) e_{0,j+1,k},\nonumber\\
&& C_{i,0,k} =(1-\mu^{-1} q^{-i}) e_{i,0,k+1},\quad
    C_{0,j,k} = (1-\mu^{-1}) e_{0,j,k+1},\nonumber\\
&& D_{1,j,k} = (q^{j+k}- \lambda^{-1}) e_{0,j,k} +
    (q^{j+k+1}- \lambda^{-1}q^{-1}) e_{0,j+1,k+1} \nonumber\\
&& \tilde D_{i,j,k} = (q^{j+k}- \lambda^{-1}) e_{i-1,j,k},\quad
    i \neq 1.\nonumber
\end{aligned}$$ Since $\tilde D_{i+2,j,k}$ is proportional to $\tilde A_{i,j,k}$ and both vanish if and only if $\lambda = q^{-(j+k)}$, we can omit $\tilde D_{i,j,k}$ from this list. We also have $$A_{-1,j,k} = - \lambda q^{-(j+k)} D_{1,j,k},$$ so the $D_{1,j,k}$ can be omitted as well. Finally, $C_{0,j,k}$ is for $j>0$ a nonzero multiple of $B_{0,j-1,k+1}$ and can be omitted. Thus the degree $0$ part (with respect to the $\mathbb{Z}$-grading) of $\mathrm{im}\, b$ is spanned by $$(1- \lambda q^{j+k}) e_{0,j,k} + (q^{-1}- \lambda q^{j+k+1}) e_{0,j+1,k+1},$$ $$(1 - \mu ) e_{0,r,s},\quad r+s>0$$ and the nonzero degrees by ([\[diesinddrin\]](#diesinddrin){reference-type="ref" reference="diesinddrin"}) together with $$(1- \lambda q^{j+k}) e_{i,j,k},\quad
    (1 - \mu q^{-i}) e_{i,j+1,0},\quad
    (1-\mu^{-1} q^{-i}) e_{i,0,k+1}.$$ where $i \neq 0$, and $j$, $k \geq 0$. Dually, $$HH^0_\sigma(\mathcal{A}) = \{ \; \mathrm{linear}\; h : \mathcal{A}\rightarrow k \; : \; h(a_1 a_2 ) = h( \sigma(a_2 ) a_1 ) \; \}$$ For $\lambda\notin q^{-\mathbb{N}}$ we have $h( e_{i,j,k}) =0$ for $i \neq 0$, and $$\label{cohom_lambda_notin_q^-N}
    h ( b^j c^k ) =  \left\{
    \begin{array}{ll}
    (-q)^{-k} {\frac{f(j-k)}{ f(j+k)}} h( b^{j-k} ) :& j \geq k\\
    {} & {}\\
    (-q)^{-j} {\frac{f(k-j)}{f(j+k)}}  h( c^{k-j}) :& j \leq k
    \end{array}\right.$$ where $f(n) = \lambda- q^{-n}$.

We now present the generating twisted 0-cycles, together with dual twisted 0-cocycles. Our calculations now break down into five cases:\
**Case 1:** $\mu=1$, $\lambda\notin \{ q^{-(N+2)} \}_{N \geq 0}$ and $\mu \neq 1$, $\lambda=1$. Then $$\label{HH_0_case_1}
HH_0^\sigma(\mathcal{A}) = k[1] \oplus \bigoplus_{x \in \{ a,b,c,d \}, \; \sigma(x) = x} ( \; \sum_{r \geq 0}^\oplus \; k [ x^{r+1} ] \; )$$ For $\mu = 1 = \lambda$ (i.e. $\sigma= \mathrm{id}$) this agrees with [@mnw]. The dual $\sigma$-twisted 0-cocycles are defined on basis elements $x = e_{i,j,k}$ with $\sigma(x) =x$ as follows: $$\label{h_1}
h_{[ 1 ]} (x) = \left\{
    \begin{array}{ll}
    1 & : x=1\\
    (-q)^{s+1} {\frac{f(0)}{f(2j+2)}} & : x = (bc)^{j+1}\\
    0 &: \mathrm{otherwise}
    \end{array}\right.$$ (if $\lambda=1$, obviously $f(0)=0$). For $y = [ a^{r+1}]$, $[ d^{r+1}]$ define $$\label{h_1_a^r+1_d^r+1}
    h_{[y]} (x) = \left\{
    \begin{array}{ll}
    1 & : x=y\\
    0 &: \mathrm{otherwise}
    \end{array}\right.$$ For $y = [ b^{s+1}]$, $[ c^{t+1}]$ define $$\label{h_b^s+1}
    h_{[ b^{s+1} ]} (x) = \left\{
    \begin{array}{ll}
    (-q)^k {\frac{f(s+1)}{ f(s+1+2k)}} & : x= b^{s+1} (bc)^k\\  
    0 &: \mathrm{otherwise}
    \end{array}\right.$$ $$\label{h_c^t+1}
    h_{[ c^{t+1} ]} (x) = \left\{
    \begin{array}{ll}
    (-q)^j  {\frac{f(t+1)}{f(t+1+2j)}}   & : x= (bc)^j c^{t+1}\\
    0 &: \mathrm{otherwise}
    \end{array}\right.$$ These all satisfy ([\[cohom_lambda_notin_q\^-N\]](#cohom_lambda_notin_q^-N){reference-type="ref" reference="cohom_lambda_notin_q^-N"}). For any $[x]$, $[y]$ in ([\[HH_0_case_1\]](#HH_0_case_1){reference-type="ref" reference="HH_0_case_1"}), we have $h_{[y]} ( x ) = \delta_{[x],[y]}$, so the 0-cycles given in ([\[HH_0_case_1\]](#HH_0_case_1){reference-type="ref" reference="HH_0_case_1"}) are linearly independent, hence a basis.\
**Case 2:** $\mu =1$, $\lambda= q^{-(N+2)}$, $N \geq 0$. We have $$\label{HH_0_case_2}
HH_0^\sigma(\mathcal{A}) = 
( \sum_{s \in S}^\oplus  \; k[ b^s ] ) \oplus 
( \sum_{t \in S}^\oplus  \; k[ c^t ] ) \oplus 
( \sum_{0 \leq i \leq N+2}^\oplus  \; k[ b^i c^{N+2-i} ] )$$ where $S = \{ \mathrm{integers}\geq N+3 \} \cup \{ N+1, N-1, N-3, \ldots \geq 0 \}$, with the convention that if $0 \in S$, we include only one copy of $k[1]$. Dual 0-cocycles are $h_{[y]}$, defined for $[y] = [b^i c^{N+2-i}]$ on the basis $e_{i,j,k}$ by $$\label{h_b^i_c^N+2-i}
h_{[y]} (x) = \left\{
    \begin{array}{ll}
    1 & : x=y\\
    0 &: \mathrm{otherwise}
    \end{array}\right.$$ and for $[y] = [ b^s]$, $[ c^t]$, $s$, $t \in S$ by $$h_{[ b^s ]} (x) = \left\{
    \begin{array}{ll}
    (-q)^k {\frac{f(s)}{ f(s+2k)}} & : x= b^s (bc)^k\\  
    0 &: \mathrm{otherwise}
    \end{array}\right.$$ $$\label{h_b^s}
\label{h_c^t}
h_{[ c^t ]} (x) = \left\{
    \begin{array}{ll}
    (-q)^j  {\frac{f(t)}{f(t+2j)}}   & : x= (bc)^j c^t\\
    0 &: \mathrm{otherwise}
    \end{array}\right.$$ So for each pair $[x]$, $[y]$ appearing in ([\[HH_0_case_2\]](#HH_0_case_2){reference-type="ref" reference="HH_0_case_2"}), we have $h_{[y]} ( x ) = \delta_{ [x], [y]}$.\
**Case 3:** $\mu = q^{M+1}$, $\lambda= q^{-(N+1)}$, $M$, $N \geq 0$. $$\label{HH_0_oldcase_6}
HH_0^\sigma(\mathcal{A}) \cong k^2 = k[ d^{M+1} c^{N+1} ]  \oplus k [ a^{M+1} b^{N+1} ]$$ Also $HH^0_\sigma(\mathcal{A}) \cong k^2$, with basis the twisted 0-cocycles $h_{[y]}$, $[y] = [ d^{M+1} c^{N+1} ]$, $[ a^{M+1} b^{N+1} ]$, defined on elements $x=e_{i,j,k}$, with $\sigma(x)=x$ by $$\label{case_6_HH^0}
    h_{[y]} (x) = \left\{
    \begin{array}{ll}
    1 & : x=y\\
    0 &: \mathrm{otherwise}
    \end{array}\right.$$

**Case 4:** $\mu = q^{-(M+1)}$, $\lambda= q^{-(N+1)}$, $M$, $N \geq 0$. We have $$HH_0^\sigma(\mathcal{A}) \cong k^2 = 
k[ d^{M+1} b^{N+1} ] \oplus k [ a^{M+1} c^{N+1} ]$$ with $HH^0_\sigma(\mathcal{A}) \cong k^2$ with basis $h_{[y]}$, $[y] = [ d^{M+1} b^{N+1} ]$, $[ a^{M+1} c^{N+1} ]$, defined as in ([\[case_6_HH\^0\]](#case_6_HH^0){reference-type="ref" reference="case_6_HH^0"}).\
**Case 5:** $\mu = q^{\pm( M+1)}$, $M \geq 0$, $\lambda\notin q^{- \mathbb{N}}$, and $\mu \notin q^{\mathbb{Z}}$, $\lambda\neq 1$. Then $$HH_0^\sigma(\mathcal{A}) =0 = HH^0_\sigma(\mathcal{A})$$

## Twisted cocycles defined by derivations

Before proceeding with $HH_1^\sigma(\mathcal{A})$, we present a general construction of $\sigma$-twisted Hochschild $n$-cocycles. It is essentially a variant of the characteristic map of [@como; @cup].

Let $\mathcal{A}$ be a $k$-algebra and $\sigma$ be an automorphism. A $\sigma$-derivation of $\mathcal{A}$ is a $k$-linear map $\partial: \mathcal{A}\rightarrow\mathcal{A}$, such that $\partial( a_0 a_1 ) = a_0 \partial(a_1 ) + \partial( a_0 ) \sigma(a_1)$. The following is straightforward:

::: prop
[]{#hoch_n_cocycle label="hoch_n_cocycle"} If $h$ is a $\sigma_1$-twisted 0-cocycle, $\partial_1$, \..., $\partial_{n-1}$ derivations of $\mathcal{A}$, and $\partial_n$ is a $\sigma_2$-derivation, then $$\label{defn_phi_n}
    \phi_n ( a_0, a_1, \ldots , a_n ) = 
    h( a_0 \partial_1 (a_1) \ldots \partial_n (a_n) )$$ is a $\sigma_1 \circ \sigma_2$-twisted Hochschild n-cocycle
:::

In general there is no reason for such a cocycle to represent a nontrivial element of Hochschild cohomology, nor for it also to be cyclic. However:

::: lemma
[]{#cyclic_1_cocycle label="cyclic_1_cocycle"} Suppose $\mathcal{A}$ is a unital algebra, $h$ a $\sigma_1$-twisted $0$-cocycle and $\partial$ a $\sigma_2$-derivation of $\mathcal{A}$. Defining $\phi_1$ by $\phi_1 (x,y) = h( x \partial(y))$, then $\phi_1$ is a $\sigma_1 \circ \sigma_2$-twisted cyclic cocycle if and only if $h ( \partial(a) ) = 0$ for all $a \in \mathcal{A}$.
:::

For $\mathcal{A}= \mathcal{A}( SL_q (2))$ there are obvious derivations $\partial_a$, $\partial_b$ defined by $$\partial_a (a) = a, \quad
\partial_a (b) = 0, \quad
\partial_a (c) = 0, \quad
\partial_a (d) = -d$$ $$\label{der_a}
\label{der_b}
\partial_b (a) = 0, \quad
\partial_b (b) = b, \quad
\partial_b (c) = -c, \quad
\partial_b (d) = 0$$ and extended via the Leibniz rule.

For any $x \in \mathcal{A}$ define an inner derivation $\partial'_x$ by $\partial'_x (y) = [x,y] = xy-yx$. The following is straightforward:

::: prop
The vector space of all derivations of $\mathcal{A}( SL_q (2))$ is spanned by $\partial_a$, $\partial_b$ together with the inner derivations.
:::

In the sequel we will use the derivation $\partial_0 = \partial_a + \partial_b$, which satisfies $$\label{der}
\label{der_0}
\partial_0 (a) = a, \quad
\partial_0 (b) = b, \quad
\partial_0 (c) = -c, \quad
\partial_0 (d) = -d$$ and also the $\sigma_{\lambda,1}$-derivation defined by $$\label{sigma_der}
\partial(a) = a, \quad \partial(b)= 0 = \partial(c), \quad \partial(d) = - \lambda^{-1} d.$$

## $HH_1^\sigma(\mathcal{A})$

The second twisted Hochschild boundary is given by $$b(a_1,a_2,a_3)=
    (a_1a_2,a_3)-(a_1,a_2a_3)+
    (\sigma(a_3)a_1,a_2).$$ In particular (take $a_2=a_3=1$) the image of $b$ contains all elementary tensors of the form $(a_1,1)$, and the residue classes of $$(e_{i,j,k},a),\quad
    (e_{i,j,k},b),\quad
    (e_{i,j,k},c),\quad
    (e_{i,j,k},d)$$ generate $\mathcal{A}\otimes \mathcal{A}/ \mathrm{im}\, b$. Now, $HH_1^\sigma(\mathcal{A})$ is the kernel of the map $\mathcal{A}\otimes \mathcal{A}/ \mathrm{im}\, b \rightarrow \mathcal{A}$ induced by the first twisted Hochschild boundary. This sends the classes of the above elements to $A_{i,j,k},B_{i,j,k},C_{i,j,k},D_{i,j,k}$ from the previous section. It is straightforward to check for triviality and linear dependence.

We now present generators of $HH_1^\sigma(\mathcal{A})$ and dual twisted 1-cocycles. From Proposition [\[hoch_n_cocycle\]](#hoch_n_cocycle){reference-type="ref" reference="hoch_n_cocycle"}, for any $\sigma$-twisted 0-cocycle $h$ and derivation $\partial$, defining $\phi_1(x,y) = h( x \partial(y) )$ gives a $\sigma$-twisted Hochschild 1-cocycle. For $\mathcal{A}(SL_q (2))$ all automorphisms $\sigma_{\lambda,\mu}$ commute with the derivations $\partial_a$, $\partial_b$ ([\[der_a\]](#der_a){reference-type="ref" reference="der_a"}), and the $e_{i,j,k}$ are eigenvectors for these derivations. By Lemma [\[cyclic_1_cocycle\]](#cyclic_1_cocycle){reference-type="ref" reference="cyclic_1_cocycle"}, $\phi_1$ is cyclic if and only if $h \circ \partial=0$. We take $\partial_0 = \partial_a + \partial_b$ defined by ([\[der\]](#der){reference-type="ref" reference="der"}).\
**Case 1:** $\mu=1$, $\lambda\notin \{ q^{-(N+2)} \}_{N \geq 0}$ and $\mu \neq 1$, $\lambda=1$. Then $$\label{HH_1_case_1}
HH_1^\sigma(\mathcal{A}) = k[\omega_1] \; \oplus \bigoplus_{x \in \{ a,b,c,d \}, \; \sigma(x) = x} ( \; \sum_{r \geq 0}^\oplus k [ (x^r ,x)] )$$ where $\omega_1 = (\mu^{-1} -1) (d,a) + (q - q^{-1})(b,c)$. We note that, for all $\mu$ and for $\lambda\neq q^{-2}$, we have $[(c,b)] = - \mu [(b,c)]$, $[(d,a)] = - \lambda[(a,d)]$. For $\mu = 1 =\lambda$ this is in agreement with [@mnw], apart from the sign change in $\omega_1$. Now recall the 0-cocycles $h_{[x]}$ defined in ([\[h_1\]](#h_1){reference-type="ref" reference="h_1"})-([\[h_c\^t+1\]](#h_c^t+1){reference-type="ref" reference="h_c^t+1"}).

Given such an $x$, define a Hochschild 1-cocycle $\phi_{[x]}$ by $$\label{phi_[x]}
    \phi_{[x]} ( y,z) = h_{[x]} ( y \partial_0 (z) )$$ Then the Hochschild 1-cocycles dual to the generators of $HH_1^\sigma(\mathcal{A})$ are: $$\phi_{[ x^{r+1} ]} \leftrightarrow ( x^r ,x), \quad 
        x \in \{ a,b,c,d \}, \quad \sigma(x) = x.$$ Dual to $\omega_1$ we have $$\label{phi_omega_1}
        \phi_{\omega_1} (x,y) =
        h_{[1]} (x \partial_0(y))$$ with $h_{[1]}$ defined in ([\[h_1\]](#h_1){reference-type="ref" reference="h_1"}) and $\partial_0$ defined in ([\[der_0\]](#der_0){reference-type="ref" reference="der_0"}). Then for $\lambda=1$ we have $\phi_{\omega_1}(d,a)=1$, and for $\lambda\neq q^{-2}$ we have $\phi_{\omega_1}(b,c)=\frac{q(1-\lambda)}{\lambda q^2-1}$. Since $h_{[1]} \circ \partial_0 =0$, by Lemma [\[cyclic_1_cocycle\]](#cyclic_1_cocycle){reference-type="ref" reference="cyclic_1_cocycle"} $\phi_{\omega_1}$ is in fact a $\sigma$-twisted cyclic 1-cocycle.\
**Case 2.** $\mu =1$, $\lambda=q^{-(N+2)}$, $N \geq 0$. Then $$HH_1^\sigma(\mathcal{A}) = 
( \sum_{s \in S'}^\oplus \; k[( b^s ,b)] ) \oplus
( \sum_{t \in S'}^\oplus \; k[( c^t ,c)] ) \oplus$$ $$\label{HH_1_case_3a}
( \sum_{0 \leq i \leq N}^\oplus \; k[( b^i c^{N+1-i} ,b )] ) \oplus
( \sum_{0 \leq i \leq  N}^\oplus \; k[( b^{i+1} c^{N-i} ,c )] ) \oplus
k [ \omega_1 ]$$ Here $S' = \{ \mathrm{integers}\geq N \} \cup \{ N-2, N-4, \ldots \geq 0 \}$, and for $N \geq 1$ we have $[ \omega_1] = [(b,c)] = - [(c,b)]$ for $N$ odd, $[\omega_1]=0$ for $N$ even. For $\lambda= q^{-2}$, $[(b,c)]$ and $[(c,b)]$ are linearly independent.

Recall the 0-cocycles $h_{[x]}$, with $[x] =[b^s]$, $[c^t]$, defined in ([\[h_b\^s+1\]](#h_b^s+1){reference-type="ref" reference="h_b^s+1"}), ([\[h_c\^t+1\]](#h_c^t+1){reference-type="ref" reference="h_c^t+1"}). The dual Hochschild 1-cocycles ([\[phi\_\[x\]\]](#phi_[x]){reference-type="ref" reference="phi_[x]"}) are $$\phi_{[b^{s+1}]} \leftrightarrow (b^s ,b), \quad
\phi_{[c^{t+1}]} \leftrightarrow (c^t ,c)$$ together with the twisted cyclic 1-cocycle $\phi_{\omega_1}$ ([\[phi_omega_1\]](#phi_omega_1){reference-type="ref" reference="phi_omega_1"}) dual to $\omega_1$. To define twisted 1-cocycles dual to $[( b^i c^{N+1-i} ,b )]$, $[( b^{i+1} c^{N-i} ,c )]$ we need to work a little harder. It is straightforward to show that any $\sigma$-twisted Hochschild 1-cocycle is uniquely defined by its values $\phi(y,t)$, for $t = a,b,c,d$ and basis elements $y = e_{i,j,k}$.

::: lemma
For $\lambda= q^{-(N+2)}$, $\mu=1$ defining $\phi_1$, $\phi_2$ on basis elements $y=e_{i,j,k}$ by

$$\begin{aligned}
&& \phi_1 ( b^i c^{N+1-i} ,b) = \beta_{N,i}, \quad \phi_1 ( d b^i c^{N-i} , a) = q^{-(N+1)} \beta_{N,i},\nonumber\\
&& \phi_1 (y,b) = 0 = \phi_1 (y,a) \quad \mathrm{otherwise}, \quad  \phi_1 (y,c) = 0 = \phi_1 (y,d) \quad \forall \; y\nonumber\\
&& \phi_2 ( a b^i c^{N-i} , d) = q^{N+1} \gamma_{N,i}, \quad \phi_2 ( b^{i+1} c^{N-i} , c) = \gamma_{N,i} \nonumber\\
&& \phi_2 (y,d) = 0 = \phi_2 (y,c) \quad \mathrm{otherwise}, \quad  \phi_2 (y,a) = 0 = \phi_1 (y,b) \quad \forall \; y\nonumber
\end{aligned}$$ for arbitrary $\beta_{N,i}$, $\gamma_{N,i}$, $0 \leq i \leq N$, gives well-defined $\sigma$-twisted Hochschild 1-cocycles.
:::

Setting each $\beta_{N,i}$, $\gamma_{N,i}$ to 1 in turn, and all others to zero, we see that the twisted Hochschild 1-cycles $[( b^i c^{N+1-i} ,b )]$, $[( b^{i+1} c^{N-i} ,c )]$ are nontrivial and linearly independent. This extends to $N+1$ linearly independent twisted cyclic 1-cocycles. Define $\phi = \phi_1 + \phi_2$. Cyclicity requires

$$\phi( xc ,b) = - \phi( b, xc) = -i \phi( xc,b) - (N+1-i) \phi ( bx ,c)$$ where $x = b^i c^{N-i}$. Hence for $\phi$ to be cyclic, we need $$(i+1) \beta_{N,i} = -(N+1-i) \gamma_{N,i} \quad 0 \leq i \leq N$$ i.e. $\gamma_{N,i} = {\frac{-(i+1)}{N+1-i}} \beta_{N,i}$ for $0 \leq i \leq N$. Then:

::: lemma
For each $0 \leq i \leq N$, defining $\phi_{N,i} = \phi_1 + \phi_2$ with $$\beta_{N,i} = N+1-i, \quad \gamma_{N,i} = -(i+1)$$ gives a well-defined twisted cyclic 1-cocycle satisfying $$\begin{aligned}
&& \phi_{N,i} ( xc ,b) = N+1-i,\quad \phi_{N,i} ( bx ,c) = -(i+1)\nonumber\\
&& \phi_{N,i} (ax,d) = -q^{N+1} (i+1), \quad \phi_{N,i} (dx,a) = q^{-(N+1)} (N+1-i)\nonumber
\end{aligned}$$ for $x= b^i c^{N-i}$, and $\phi_{N,i} (y,t) = 0$ for all basis elements $y$ and $t=a,b,c,d$ otherwise.\
:::

**Case 3.** $\mu = q^{M+1}$, $\lambda=q^{-(N+1)}$, $M$, $N \geq 0$. Then $HH_1^\sigma(\mathcal{A})  \cong k^4$, with basis given by the Hochschild cycles $$\label{case6_HH1}
( a^M b^{N+1} ,a), \quad
( a^{M+1} b^N ,b), \quad
( d^{M+1} c^N ,c), \quad
( d^M c^{N+1} ,d)$$ The dual basis for $HH^1_\sigma(\mathcal{A}) \cong k^4$ is given by the 1-cocycles $\phi_{[x],t}$, for $[x] = [ a^{M+1} b^{N+1} ]$, $[d^{M+1} c^{N+1}]$, and $t = a, b$ defined by $$\label{phi_[x]_t}
 \phi_{[x],t} (y,z) = h_{[x]} ( y \partial_t (z) )$$ where the $h_{[x]}$ were defined in ([\[case_6_HH\^0\]](#case_6_HH^0){reference-type="ref" reference="case_6_HH^0"}) and $\partial_a$, $\partial_b$ in ([\[der_a\]](#der_a){reference-type="ref" reference="der_a"}). We have $$\begin{aligned}
&& \phi_{ [ a^{M+1} b^{N+1} ], a} ( a^M b^{N+1} ,a) = q^{-(N+1)} \nonumber\\ 
&& \phi_{ [ a^{M+1} b^{N+1} ],b} ( a^{M+1} b^N ,b) = 1 \nonumber\\
&& \phi_{[d^{M+1} c^{N+1}] ,b}( d^{M+1} c^N ,c) = -1 \nonumber\\
&& \phi_{[d^{M+1} c^{N+1}],a} ( d^M c^{N+1} ,d) = -q^{N+1} \nonumber
\end{aligned}$$ with all other pairings being zero.\
**Case 4.** $\mu = q^{-(M+1)}$, $\lambda= q^{-(N+1)}$, $M$, $N \geq 0$. $HH_1^\sigma(\mathcal{A}) \cong k^4$, with basis given by the Hochschild cycles $$( a^M c^{N+1} ,a ), \quad 
 ( d^{M+1} b^N ,b), \quad
( a^{M+1} c^N , c), \quad
( d^M b^{N+1} ,d)$$ Analogously to Case 3, the dual basis for $HH^1_\sigma(\mathcal{A}) \cong k^4$ is given by the 1-cocycles $\phi_{[x],t}$, ([\[phi\_\[x\]\_t\]](#phi_[x]_t){reference-type="ref" reference="phi_[x]_t"}) for $[x] = [ a^{M+1} c^{N+1} ]$, $[d^{M+1} b^{N+1}]$, and $t = a$, $b$.\
**Case 5.** For $\mu = q^{\pm(M+1)}$, $M \geq 0$, $\lambda\notin q^{-\mathbb{N}}$, and $\mu \notin q^\mathbb{Z}$, $\lambda\neq 1$, $HH_1^\sigma(\mathcal{A}) =0$ and $HH^1_\sigma(\mathcal{A}) =0$.\

## $HH_2^\sigma(\mathcal{A})$

We now compute $HH_2^\sigma(\mathcal{A})$. The first step is to describe the kernel of $$\psi : \mathcal{A}^2 \rightarrow \mathcal{A},\quad (x,y) \mapsto \psi_+(x)+\psi_-(y)$$ If $\mathrm{ker}\, \psi_\pm^c \subset \mathcal{A}$ are fixed complements to $\mathrm{ker}\, \psi_\pm$ and $$\phi_\pm : 
    \mathrm{im}\, \psi_\pm \rightarrow 
    \mathrm{ker}\, \psi_\pm^c$$ are the inverses of $\psi_\pm |_{\mathrm{ker}\, \psi_\pm^c}$, then the linear map $$\begin{aligned}
&& \mathrm{ker}\, \psi_+ \oplus 
    (\mathrm{im}\, \psi_+ \cap \mathrm{im}\, \psi_-) \oplus
    \mathrm{ker}\, \psi_- \rightarrow  
    \mathrm{ker}\, \psi,\nonumber\\ 
&& (x,y,z) \mapsto 
    (x+\phi_+(y),z-\phi_-(y)) \nonumber
\end{aligned}$$ is an isomorphism of vector spaces. Using ([\[sindwiederda\]](#sindwiederda){reference-type="ref" reference="sindwiederda"}) one determines a basis of $\mathrm{im}\, \psi_+ \cap \mathrm{im}\, \psi_-$ and obtains:

::: prop
[]{#eswird label="eswird"} The set $$\begin{aligned}
&& {\mathcal{B}}_{\mathrm{ker}\,\psi} :=   \{(x_+,0),(0,x_-)\,|\,x_\pm \in {\mathcal{B}}_{\mathrm{ker}\,\psi_\pm}\}\nonumber\\
&& \cup \{(-\lambda^{-2}(
    \frac{1-\varepsilon_{-i,j,k}}{1-\varepsilon_{i-2,j,k}^{-1}}e_{i-2,j-1,k+1}
    -\varepsilon_{-i,j,k+1}e_{i-2,j,k+2}),e_{i,j,k}),\nonumber\\
&& \quad(e_{-i,k,j},-\lambda^2(
    \frac{1-\varepsilon_{-i,j,k}^{-1}}{1-\varepsilon_{i-2,j,k}}e_{-i+2,k+1,j-1}
    -\varepsilon_{-i,j,k+1}^{-1}e_{-i+2,k+2,j}))\,|\,\nonumber\\ 
&& \quad i \ge 2,j \ge 1,k \ge 0,\varepsilon_{i-2,j,k} \neq 1\} 
    \nonumber\\
&&\cup \{(\lambda^{-2}qe_{i-2,0,j+2},e_{i,0,j}),
    (e_{-i,j,0},\lambda^2q^{-1} e_{-i+2,j+2,0})\,|\, 
    i \ge 2,j \ge 0,\varepsilon_{-i,0,j}=1\} 
    \nonumber\\
&& \cup \{(e_{-1,j,k},\lambda^2 \varepsilon_{-1,j,k}^{-1} e_{1,j+1,k-1})\,|\,
    j \ge 0,k \ge 1\}.\nonumber
\end{aligned}$$ is a vector space basis of $\mathrm{ker}\, \psi$.
:::

Now we can compute which of these remain nontrivial and linearly independent modulo the image of the map $\varphi : x \mapsto (\psi_-(x),-\psi_+(x))$.

::: prop
The classes of $$\begin{aligned}
&& \{ (e_{i,j,0},0), \; (0,e_{-i,0,j}) \; | \; i \ge 0,\; j \ge 0,\; \varepsilon_{i,0,j}=1\; \}
    \nonumber\\
&& \cup \; \{ (\lambda^{-2}qe_{i-2,0,k+2}, \; e_{i,0,k}) \; | \; 
    i \ge 2,\; k \ge 0,\; \varepsilon_{-i,0,k}=1\; \} 
    \nonumber\\
&& \cup \;  
    \{ (e_{i,j,0}, \; \lambda^2 q^{-1} e_{i+2,j+2,0}) \; | \; 
    i \le -2, \; j \ge 0, \; \varepsilon_{i,j,0}=1 \; \} 
    \nonumber\\
&& \cup \; \{ (e_{-1jk},\lambda^2 e_{1,j+1,k-1}) \; | \;
    j \ge 0,\; k \ge 1,\varepsilon_{-1,j,k}=1 \; \}\nonumber
\end{aligned}$$ form a vector space basis of $\mathrm{ker}\, \psi / \mathrm{im}\, \varphi$.
:::

Next we check for which linear combinations $(x,y) \neq (0,0)$ of these there exists $z$ with $(x,y,z) \in \mathrm{ker}\, f_2$, and determine those $z$ with $(0,0,z) \in \mathrm{ker}\, f_2$, giving a generating set for $HH_2^\sigma(\mathcal{A})$:

::: prop
The classes of $$\begin{aligned}
&& \{\; (0,0,e_{0,j,k}) \; | \; j, k \ge 0,\; \varepsilon_{0,j,k}=1\; \}\nonumber\\
&& \cup \; \{\; (e_{i,j,0},0,0),\; (0,e_{-i,0,j},0) \; | \; i \ge 0,\; j \ge 0, \; 
    \lambda=q^{-j-1},\; \mu=q^{i+1} \; \}
    \nonumber\\
&& \cup \{ (\lambda^{-2} q e_{i-2,0,k+2}, e_{i,0,k},
    \lambda^{-1} q^{-1} e_{i-1,0,k+1}) \; | \; 
    i \ge 2,k \ge 0,\lambda=q^{-k-1},\mu=q^{-i+1} \} 
    \nonumber\\
&& \cup \{ (e_{i,j,0}, \; \lambda^2 q^{-1} e_{i+2,j+2,0},
    \lambda q^{-1} e_{i+1,j+1,0}) \; | \;  
    i \le -2,j \ge 0,\lambda=q^{-j-1},\mu=q^{i+1} \} 
    \nonumber\\
&& \cup \{\; (e_{-1,j,k},\; \lambda^2 e_{1,j+1,k-1},
    \lambda q^{-1} e_{0,j+1,k}) \; | \;
    j \ge 0,\; k \ge 1,\; \lambda=q^{-j-k-1},\; \mu=1\; \}\nonumber
\end{aligned}$$ generate $HH_2^\sigma(\mathcal{A})$.
:::

The classes of the elements in the first line are trivial for $\mu \neq 1$, and for $\mu=1$ they contain those from the last line. It follows directly from the definition of $f_3$ that the remaining classes are independent. Hence: $$\label{HH_2}
    HH_2^\sigma(\mathcal{A}) \cong \left\{
    \begin{array}{ll}
    {k}^{N+1} \quad & : 
    \lambda=q^{-(N+2)}, N \ge 0,\; \mu=1,\\
    {k}^2 \quad & : 
    \lambda=q^{-(N+1)}, \;
    \mu=q^{\pm (M+1)}, M, N \geq 0,\\
    0 \quad & : \mathrm{otherwise}.
    \end{array}\right.$$

To calculate $HC_\ast^\sigma(\mathcal{A})$ we need generators in the original Hochschild complex. In Case 2 we compute generators from the above using $\varphi_2$ ([\[phi_2\]](#phi_2){reference-type="ref" reference="phi_2"}) and $\xi$ ([\[fetsimo\]](#fetsimo){reference-type="ref" reference="fetsimo"}). In Cases 3 and 4 we use simpler generators that are directly verified to be homologous to those obtained from the above ones:\
**Case 2.** $\mu=1$, $\lambda= q^{-(N+2)}$, $N \geq 0$. Then $HH_2^\sigma(\mathcal{A}) \cong k^{N+1}$. Taking $x = b^i c^{N-i}$ ($0 \leq i \leq N$), a basis is given by $$\omega_2 (N,i) = (bcx,a,d) - (bcx,d,a) -q (dbx,a,c) + q (bdx,c,a)$$ $$\label{HH_2_case_3}\label{omega_2_N_i}
    + (dax,b,c) -(adx,c,b) - q^{-1} (cax,b,d) + q^{-1} (acx,d,b)$$\
**Case 3.** $\mu = q^{M+1}$, $\lambda=q^{-(N+1)}$, $M$, $N \geq 0$. Then $HH_2^\sigma(\mathcal{A}) \cong k^2$, with basis given by the Hochschild cycles $$\begin{aligned}
\label{case6_w2}\label{case6_w2p}
&\omega_2 = &(a^M b^N ,b,a) - q^{-1} ( a^M b^N ,a,b) \nonumber\\
&\omega_2^{'} = &( d^M c^N ,c,d) - q( d^M c^N ,d,c)
\end{aligned}$$

**Case 4.** $\mu = q^{-(M+1)}$, $\lambda= q^{-(N+1)}$, $M$, $N \geq 0$. $HH_2^\sigma(\mathcal{A}) \cong k^2$, with basis given by the Hochschild cycles $$\begin{aligned}
&\omega_2 = &( a^M c^N ,c,a) - q^{-1} ( a^M c^N ,a,c) \nonumber\\
&\omega_2^{'} = &(d^M b^N ,b,d) - q( d^M b^N ,d,b)
\end{aligned}$$

Finally, $HH_2^\sigma(\mathcal{A})=0$ for all other $\sigma= \sigma_{\lambda,\mu}$.

## $HH_3^\sigma(\mathcal{A})$

The third homology $HH_3^\sigma(\mathcal{A})$ can be determined easily using the Koszul resolution. We abbreviate: $$\psi_+: \mathcal{A}\rightarrow \mathcal{A},\quad x \mapsto x \blacktriangleleft b,
    \quad 
    \psi_- : \mathcal{A}\rightarrow \mathcal{A},\quad x \mapsto x \blacktriangleleft c.$$ From ([\[right_action_of_a_b_c\]](#right_action_of_a_b_c){reference-type="ref" reference="right_action_of_a_b_c"}) we obtain in a straightforward way:

::: prop
[]{#ersterkern label="ersterkern"} The sets $${\mathcal{B}}_{\mathrm{ker}\,\psi_\pm} := 
    \{ \; e_{i,j,k} \; | \; \pm i \ge 0,\; \varepsilon_{\pm i,j,k}=1 \; \}$$ are vector space bases of $\mathrm{ker}\,\psi_\pm$. Hence the sets $${\mathcal{B}}_{\mathrm{im}\,\psi_\pm} := 
    \{ \; E^\pm_{i,j,k} \; | \; e_{i,j,k} \notin \mathrm{ker}\, \psi_\pm \; \},\quad
    E^\pm_{i,j,k}:=\psi_\pm(e_{i,j,k})$$ are vector space bases of $\mathrm{im}\,\psi_\pm$.
:::

If $x \in HH_3^\sigma(\mathcal{A})=\mathrm{ker}\,f_3$, then $x \in \mathrm{ker}\, \psi_+ \cap \mathrm{ker}\, \psi_-$, so by Proposition [\[ersterkern\]](#ersterkern){reference-type="ref" reference="ersterkern"}, $\pi_{i,j,k}(x) \neq 0$ implies $i=0$. Insertion in $q^{-2}x \blacktriangleleft a=x$ gives $$x \in 
    \left\{
    \begin{array}{ll}
    \mathrm{span}\, \{b^i c^{N-i}\}_{i=0,\ldots,N} \quad & :
    \lambda=q^{-N-2},\mu=1,\\
    0 \quad & : \mathrm{otherwise}.
    \end{array}\right.$$ Conversely, all these monomials are elements of $\mathrm{ker}\, f_3$. Hence:\
**Case 2:** For $\mu =1$, $\lambda= q^{-(N+2)}$, $N \geq 0$ we have $HH_3^\sigma(\mathcal{A}) \cong k^{N+1}$.\
**Cases 1, 3, 4, 5:** $HH_3^\sigma(\mathcal{A})=0$.\
It is also straightforward that $HH_3^\sigma(\mathcal{A})=0$ for all $\sigma= \tau_{\lambda,\mu}$. Therefore:

::: thm
[]{#HH_3_for_any_sigma label="HH_3_for_any_sigma"} For any automorphism $\sigma$, we have $$HH_3^\sigma(\mathcal{A})=\left\{
    \begin{array}{ll}
    {k}^{N+1} \quad & : \sigma= \sigma_{\lambda, \mu}, \;
    \lambda=q^{-(N+2)},N \geq 0,\; \mu=1,\\
    0 \quad & : \mathrm{otherwise}.
    \end{array}\right.$$
:::

Note that the $N=0$ case ($\lambda= q^{-2}$, $\mu=1$) is precisely the modular automorphism ([\[smod_slq2\]](#smod_slq2){reference-type="ref" reference="smod_slq2"}). For $\lambda= q^{-(N+2)}$ we translate the generators back to the original Hochschild complex using the maps $\varphi_3$ ([\[phi_3\]](#phi_3){reference-type="ref" reference="phi_3"}) and $\xi$ ([\[fetsimo\]](#fetsimo){reference-type="ref" reference="fetsimo"}), giving $$\label{omega_3_N_i}
    \omega_3 (N,i) = A(N,i) - B(N,i),\quad
    0 \leq i \leq N,$$ $$\begin{aligned}
&A(N,i) = &dx \otimes (a \wedge b \wedge c) 
+ cx \otimes (b \wedge a \wedge d) \nonumber\\
&B(N,i) = &-qdbx \otimes (1 \wedge a \wedge c) - q^{-1} cax \otimes (1 \wedge b \wedge d) \nonumber\\
&&+ dax \otimes (1 \wedge b \wedge c) + bcx \otimes ( 1 \wedge a \wedge d) \nonumber\\
&& + (q - q^{-1}) bcx \otimes ( (c,b,1) - (1,c,b) + (c,1,b)) \nonumber
\end{aligned}$$ with $x= b^i c^{N-i}$, and the terms $``a_0 \wedge a_1 \wedge a_2"$ are given by: $$\begin{aligned}
&a \wedge b \wedge c =& (a,b,c) - (a,c,b) + q(c,a,b) - q^2(c,b,a) +
q^2 (b,c,a) - q(b,a,c) \nonumber\\
&b \wedge a \wedge d =& (b,a,d) - (b,d,a) + q (d,b,a) - (d,a,b) + (a,d,b) - q^{-1}(a,b,d)\nonumber\\
&1 \wedge a \wedge c =& (1,a,c) - q(1,c,a) + q (c,1,a)
- q(c,a,1) + (a,c,1) - (a,1,c)\nonumber\\
&1 \wedge b \wedge d =& (1,b,d) - q (1,d,b) - (b,1,d) + (b,d,1) - q(d,b,1) + q (d,1,b)\nonumber\\
&1 \wedge b \wedge c =& (1,b,c) - (1,c,b) - (b,1,c) + (b,c,1) + (c,1,b) - (c,b,1)\nonumber\\
&1 \wedge a \wedge d =& (1,a,d) - (1,d,a) + (d,1,a) - (d,a,1) + (a,d,1) - (a,1,d)\nonumber
\end{aligned}$$ and throughout we denote $a_0 \otimes a_1 \otimes a_2$ by $(a_0, a_1,a_2)$.

In the normalized complex this becomes $\omega_3(N,i)=A(N,i)$ since $B(N,i)$ is degenerate.

# Twisted cyclic homology of $\mathcal{A}( SL_q (2))$ {#section_tc_slq2}

We calculate the twisted cyclic homology of $\mathcal{A}(SL_q (2) )$ as the total homology of Connes' mixed $(b,B)$-bicomplex ([\[mixed_b_B_bicomplex\]](#mixed_b_B_bicomplex){reference-type="ref" reference="mixed_b_B_bicomplex"}) coming from the underlying cyclic object, as in section [\[section:cyclic_module\]](#section:cyclic_module){reference-type="ref" reference="section:cyclic_module"}. Having found the twisted Hochschild homology, we can now complete the spectral sequence calculation. We remind the reader that throughout we are working with the normalized mixed complex.
