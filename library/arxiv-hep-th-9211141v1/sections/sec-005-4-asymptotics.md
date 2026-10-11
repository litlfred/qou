---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-005-4-asymptotics
section_title: "ASYMPTOTICS"
section_number: 4
pages: 17-34
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.99
---
[]{#sec:asy label="sec:asy"}

## Asymptotics via Painlevé {#subsec:asy_painleve}

Hastings and McLeod [@hastings_mcleod] (see also [@clarkson_mcleod1; @clarkson_mcleod2]) have shown that $q(s;1)$, the unique solution to equation ([\[p2\]](#p2){reference-type="ref" reference="p2"}) which is asymptotic to ${\rm Ai}(s)$ as $s\rightarrow +\infty$, is asymptotically equal to $\sqrt{-s/2}$ as $s\rightarrow -\infty$. In fact there is a complete asymptotic expansion in decreasing powers of $-s$, beginnning with this term [@mcleod_private]. Successive terms are easily computed. This result and later ones, become a little easier to state if we write $s=-t/2$: $$q(-t/2;1)={1\over 2}\sqrt{t}\left( 1 - {1\over t^3} - {73\over 2t^6}
-{10657\over 2 t^9} - {13912277\over 8 t^{12}}
+{\rm O}({1\over t^{15}})\right) \ \ \
(t\rightarrow +\infty)
\label{p2_asy}$$ Squaring and integrating and using ([\[Rq_relation\]](#Rq_relation){reference-type="ref" reference="Rq_relation"}) we deduce $$R(s) = {1\over 4} s^2 + c - {1\over 8\, s} + {9\over 64\,  s^4} -
{189\over 128 \, s^7} + {21663\over 512\,  s^{10}} + {\rm O}({1\over s^{13}})
\ \ \ (s\rightarrow -\infty)$$ where $c$ is a constant. Substituting this into ([\[rDE\]](#rDE){reference-type="ref" reference="rDE"}) shows that $c=0$. Thus we obtain ([\[R_exp\]](#R_exp){reference-type="ref" reference="R_exp"}) and then, after integrating and exponentiating, ([\[E0_exp\]](#E0_exp){reference-type="ref" reference="E0_exp"}).

To obtain the asymptotic expansions of $q_n(s)$ in ([\[qn_defn\]](#qn_defn){reference-type="ref" reference="qn_defn"}), we differentiate ([\[p2\]](#p2){reference-type="ref" reference="p2"}) with respect to $\lambda$ and set $\lambda=1$. We obtain $$q_1^{\prime\prime}-\left(s+6q_0^2\right) q_1=0$$ (where $q_0(s)=q(s;1)$). Using ([\[p2_asy\]](#p2_asy){reference-type="ref" reference="p2_asy"}) we find two linearly independent solutions of this equation, one exponentially large at $-\infty$ and one exponentially small. Assuming the exponentially large one actually appears with a nonzero factor we obtain the asymptotic expansion $$q_1(-t/2)=c_1 {\exp({1\over 3} t^{3/2})\over t^{1/4}}
\left( 1 + {17\over 24\,  t^{3/2}} +{1513\over 2^7 3^2\,  t^3} +
{850193\over 2^{10} 3^4\,  t^{9/2}}+{407117521\over 2^{15} 3^5\,  t^{6}}
 + \cdots
\right)
\label{q1_asy}$$ where $c_1$ is a constant factor to be determined.

Successive differentiations of ([\[p2\]](#p2){reference-type="ref" reference="p2"}) with respect to $\lambda$, followed by setting $\lambda=1$, yields a sequence of linear differential equations for the $q_n$, $$q_n^{\prime\prime}-\left(s+6q_0^2\right) q_n= \varphi_n(q_0,\cdots,
q_{n-1}),$$ where $\varphi_n$ is a polynomial in the $q_m$ with $m<n$. For $n>1$ a particular solution dominates all solutions of the homogeneous equation. Therefore, in the asymptotics, no new unknown constant factors are introduced (unless we want to go "beyond all orders").

To deduce expansions for the $r(n;s)$ we must differentiate ([\[det_p2\]](#det_p2){reference-type="ref" reference="det_p2"}) $n$ times with respect to $\lambda$ and set $\lambda=1$. We find expressions of the form $$r(n;s)=\int_s^\infty (x-s) \psi(q_0,\cdots,q_n)\, dx
\label{r_integral}$$ where $\psi_n$ is a polynomial in $q_0, \cdots, q_n$. In particular we obtain (after setting $s=-t/2$) $$r(1;-t/2)={1\over 2}\int_{-\infty}^t (t-x) q_0(-x/2) q_1(-x/2)\, dx\, .$$ Substituting ([\[p2_asy\]](#p2_asy){reference-type="ref" reference="p2_asy"}) and ([\[q1_asy\]](#q1_asy){reference-type="ref" reference="q1_asy"}) into this integral gives the asymptotic expansion for $r(1;-t/2)$. The first order result is $$r(1;-t/2) \sim c_1 {\exp(t^{3/2}/3)\over t^{3/4}}$$ and comparing this with ([\[r_asy\]](#r_asy){reference-type="ref" reference="r_asy"}) reveals that $$c_1={1\over 2\sqrt{2\pi}}\, .$$

We now state the expansions we have obtained in this way with the help of Mathematica. For $q_n$ with $n>2$, as $t\rightarrow +\infty$ $$\begin{aligned}
q_n(-t/2)&=& {n!\over 2^{3n/2}\, \pi^{n/2}}\,
{ \exp({n\over 3} t^{3/2}) \over
t^{3n/4-1/2}}
\Biggl( 1 +{59n-36\over 24}\>  t^{-3/2} + \nonumber \\
&& \quad {3481 n^2+8244 n -8496\over 1152 }\>  t^{-3} +
 {\rm O}(t^{-9/2})\Biggr).
\label{qn_asy}
\end{aligned}$$ For $n=1, 2$ the leading order term is as above. For $n=1$ the correction terms are given above in ([\[q1_asy\]](#q1_asy){reference-type="ref" reference="q1_asy"}). For $n=2$ the coefficient of $t^{-3/2}$ is as given above but the coefficient of $t^{-3}$ is ${5461/ 288}$. (Similar exceptional values of $n$ occurred in analogous expansions for the sine kernel [@btw].)  These expansions have been computed for $n\leq 10$ and are undoubtedly correct for all $n$. (In [@btw] the analogous expansions were proved for all $n$ by a backwards induction argument---such arguments should extend to the present case of $q_n$.)

For $r(n;s)$ we have obtained the following sharpening of ([\[r_asy\]](#r_asy){reference-type="ref" reference="r_asy"}): as $t\rightarrow +\infty$ $$\begin{aligned}
r(n;-t/2)& =& {1! 2! \cdots (n-1)!\over 2^{n^2+n/2} \pi^{n/2} } \,
{\exp({n\over 3} t^{3/2})\over t^{3n^2/4}}
 \Biggl(
1+
{n(34 n^2 +31)\over 24}\>  t^{-3/2} + \nonumber \\
&& \quad {n^2(1156 n^4+6608 n^2 +11509)\over 1152 }\>  t^{-3}+
{\rm O}(t^{-9/2}) \Biggr).
\label{r_asy2}
\end{aligned}$$ This was established for $n\leq 6$. As was mentioned in the Introduction, when we substitute expansions ([\[qn_asy\]](#qn_asy){reference-type="ref" reference="qn_asy"}) into ([\[r_integral\]](#r_integral){reference-type="ref" reference="r_integral"}) a large amount of cancellation takes place, so that $r(n;s)$ is much smaller than might be anticipated. This also means that to deduce even the first-order asymptotics in ([\[r_asy2\]](#r_asy2){reference-type="ref" reference="r_asy2"}) for moderate values of $n$ one has to go very far out in the expansions ([\[qn_asy\]](#qn_asy){reference-type="ref" reference="qn_asy"}). Thus it is important that we have an alternative approach which yields asymptotic results for all values of $n$.

## Asymptotics via the Commuting Differential Operator {#subsec:asy_diffop}

We begin with the integral identity $$K(x,y)=\int_0^\infty A(x+z) A(y+z)\, dz \, .
\label{K_identity}$$ This appears in [@clarkson_mcleod1] but we give a simple proof here. Think of ([\[partial_K\]](#partial_K){reference-type="ref" reference="partial_K"}) as a differential equation for the "unknown" function $K(x,y)$. Since $$\left({\partial\over\partial x}+{\partial\over \partial y}\right)
A(x+z) A(y+z) = {\partial\over\partial z} A(x+z) A(y+z)$$ one solution is the right side of ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) and, of course, another solution is the Airy kernel $K(x,y)$. The difference is therefore of the form $\varphi(x-y)$ for some function $\varphi$. Since both sides of ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) tend to zero as $x$ and $y$ tend to $+\infty$ independently, we must have $\varphi\equiv 0$.

Rewriting ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) as $$K(x,y) = \int_s^\infty A(x+z-s) A(z+y-s) \, dz$$ shows that $K$ as an operator on $(s,\infty)$ is the square of the operator with kernel $A(x+y-s)$.

Integration by parts shows that an integral operator with kernel $L(x,y)$ on $(s,\infty)$ commutes with a differential operator $${d\over dx} \alpha(x) {d\over dx} + \beta(x)$$ if $\alpha(s)=0$ and if $$\alpha(y) {\partial^2L\over \partial y^2} + \alpha^\prime(y)
{\partial L\over \partial y} + \beta(y) L =
\alpha(x) {\partial^2 L\over \partial x^2} + \alpha^\prime(x)
{\partial L\over \partial x}+\beta(x) L \, .$$ (Of course we also require, in the end, appropriate vanishing at $\infty$.)  If we set $L(x,y)=A(x+y-s)$ and use the fact $A^{\prime\prime}(x)=xA(x)$ we can easily check that a solution is given by $$\alpha(x)=x-s, \ \ \ \beta(x)=-x(x-s)$$ and so we obtain the commuting differential operator ([\[L_operator\]](#L_operator){reference-type="ref" reference="L_operator"}).

Here is an outline of how ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}) is found. If we let $f_1$, $f_2, \cdots$ denote the eigenfunctions of $L$ then the logarithmic derivative of each $\lambda_i$ (thought of as a function of $s$) is expressible very simply in terms of the corresponding $f_i$. The asymptotics of these eigenfunctions, and so of the logarithmic derivative, is established by WKB techniques. Integrating, and using the fact that each $\lambda_i\rightarrow 1$ as $s\rightarrow -\infty$, gives ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}). The WKB argument we give is quite heuristic although it could very likely be made rigorous.

We make a preliminary change of variables, replacing $x$ by $x+s$ (so that $L$ acts on $(0,\infty)$) and $s$ by $-2t$. The eigenvalue problem can then be written as $$\left(x f^\prime(x)\right)^\prime +\left(\mu-(x-t)^2\right)f(x)=0
\label{eig_eqn1}$$ or in the equivalent form $$x g^{\prime\prime}(x) +\left\lbrack \mu - (x-t)^2 +{1\over 4x}
\right\rbrack g(x)=0\, , \ \ \ \left(g(x)=\sqrt{x} f(x)\right)
\label{eig_eqn2}$$ The eigenvalues satisfy $0<\mu_0<\mu_1<\cdots$ and oscillation considerations applied to ([\[eig_eqn2\]](#eig_eqn2){reference-type="ref" reference="eig_eqn2"}) show that $\mu_i={\rm O}(t^{1/2})$, for each $i$ as $t\rightarrow\infty$. So we think of $\mu$ in our equations as ${\rm O}(t^{1/2})$, we normalize our eigenfunctions so that $f(0)=1$, and proceed to find asymptotics for large $t$.

### The region $x<<t^{-1/2}$ {#subsubsec:region1}

If we make the substitutions $$f(x) = h(t^2x)=h(y)$$ then ([\[eig_eqn1\]](#eig_eqn1){reference-type="ref" reference="eig_eqn1"}) becomes $$\left(y h^\prime(y) \right)^\prime - h(y) = t^{-2}\left(
{y^2\over t^4} -2 {y\over t} -\mu\right) h(y)\, .$$ The solution of the equation with the right hand side replaced by $0$ which satisfies $h(0)=1$ is $I_0(2\sqrt{y})$ where $I_0$ is the usual modified Bessel function. The actual solution $h(y)$ will be asymptotic to this in any interval over which the integral of the factor of $h(y)$ on the right hand side of the equation is ${\rm o}(1)$. Recalling that $\mu={\rm O}(t^{1/2})$ we see that $y<<t^{3/2}$ suffices. Hence $$f(x)\sim I_0\left(2t\sqrt{x}\right)\, , \ \ \ (x<<t^{-1/2})
\label{appx1}$$

###  The region $x>>t^{-2}$, $t-x>>t^{1/4}$ {#subsubsec:region2}

If in equation ([\[eig_eqn2\]](#eig_eqn2){reference-type="ref" reference="eig_eqn2"}) we set $$\alpha(x)={(t-x)^2-\mu\over x}, \ \ \  y=\int_0^x\sqrt{\alpha(z)}\, dz\, ,
\ \ \ h(y)=\alpha(x)^{1/4} g(x)$$ then the equation for $h(y)$ is $$h^{\prime\prime}(y)-h(y)=\left\lbrack {1\over 4} {\alpha^{\prime\prime}\over
\alpha^2} - {5\over 16} {{\alpha^\prime}^2\over \alpha^3}
-{1\over 4 x^2  \alpha}
\right\rbrack h(y)\, ,$$ where on the right side $^\prime= {d\over dx}$. Since $dy=\alpha(x)^{1/2}\, dx$, the integral with respect to $y$ (of the factor of $h(y)$ on the right side of the equation) over any interval equals $$\int \left( {1\over 4} {\alpha^{\prime\prime}\over \alpha^{3/2}}
-{5\over 16}{{\alpha^\prime}^2\over\alpha^{5/2}}-
{1\over 4 x^2 \alpha^{1/2}}\right)\, dx$$ over the corresponding $x$ interval. This will be ${\rm o}(1)$ as long as, in this interval, $x>>t^{-2}$ and $t-x>>t^{1/4}$.

In this same region $y>>1$ and so $$h(y)\sim a e^y
\label{appx2}$$ for some constant $a=a(t)$. In case $x<<1$ we have $y=2t\sqrt{x} +
{\rm o}(1)$ and so $$f(x)=x^{-1/2} g(x)\sim a t^{-1/2} x^{-1/4} e^{2t\sqrt{x}}\, ,
\ \ \ (t^{-2}<<x<<1).$$ Comparing this result with ([\[appx1\]](#appx1){reference-type="ref" reference="appx1"}) in the overlapping region $t^{-2}<<x<<t^{-1/2}$ and using the known asymptotics of $I_0(z)$ as $z\rightarrow\infty$ shows that $a\sim 1/2\sqrt{\pi}$. Hence from ([\[appx2\]](#appx2){reference-type="ref" reference="appx2"}) $$f(x)\sim {1\over 2\sqrt{\pi}} {(t-x)^{-1/2}\over x^{1/4}}
\exp\left\lbrace\int_0^x\sqrt{{(t-z)^2-\mu\over z}}\, dz\right\rbrace\, ,
\ \  (x>>t^{-2}, t-x>>t^{1/4})\, .$$ We also used here once again the estimate $\mu={\rm O}(t^{1/2})$. Because of this same estimate we can write the integral in the exponential as $$\int_0^x {t-z\over\sqrt{z}}\left\lbrace 1 - {1\over 2}
{\mu\over (t-z)^2}+{\rm O}\left({\mu^2\over (t-z)^4}\right)\right\rbrace
\, dz\, .$$ Because $t-x>>t^{1/4}$ the last term in brackets contributes ${\rm o}(1)$ to the integral, and so we obtain $$2t x^{1/2} -{2\over 3} x^{3/2} -{\mu\over 2}\int_0^x {dz\over
\sqrt{z} (t-z)} \, .$$ Replacing $z$ by $tz^2$ shows that the integral here equals $$t^{-1/2} \log {\left(\sqrt{t}+\sqrt{x}\right)^2\over t-x} \, .$$ Thus $$\begin{aligned}
 f(x)&\sim &  {1\over 2\sqrt{\pi}}{\left(t-x\right)^{{1\over 2} t^{-1/2}\mu -
{1\over 2}}\over x^{1/4} \left(\sqrt{t}+\sqrt{x}\right)^{
t^{-1/2}\, \mu}}\, \exp\left\lbrace 2 t x^{1/2} - {2\over 3} x^{3/2}\right
\rbrace
\label{appx3}\\
&&\hspace{3in} (x>>t^{-2}, t-x>>t^{1/4}).
\nonumber
\end{aligned}$$

Let us see what happens if $x$ is not far from $t$, if $$t^{1/4}<<t-x<<t^{1/2} \, .$$ Then since $$2t x^{1/2} -{2\over 3} x^{3/2} = {4\over 3} t^{4/3} - {1\over 2}
(x-t)^2 + {\rm o}(1)$$ in this region, we find $$\begin{aligned}
f(x)&\sim & {1\over 2\sqrt{\pi}} 2^{-t^{-1/2}\mu} t^{-3/4}
\left( t\over t-x\right)^{-{1\over 2} t^{-1/2}\mu+{1\over 2}}
\exp\left\lbrace {4\over 3} t^{4/3}-{1\over 2} (x-t)^2\right\rbrace
\label{appx4}\\
&&\hspace{3in} (t^{1/4}<<t-x<<t^{1/2})
\nonumber
\end{aligned}$$

### The region $x-t>>t^{1/4}$ {#subsubsec:region3}

This is quite similar to the preceding. The main difference is that instead of making the variable change $y=\int \alpha(x)^{1/2}\, dx$ in ([\[eig_eqn2\]](#eig_eqn2){reference-type="ref" reference="eig_eqn2"}) we now set $$y={2\over 3} x^{3/2} -2 t x^{1/2} - \int_x^\infty
\left\lbrack \sqrt{\alpha(z)} - z^{1/2} + t z^{-1/2}\right\rbrack \, dz\, .$$ Since an eigenfunction cannot grow exponentially at $\infty$ only the negative exponential $e^{-y}$ can appear in the asymptotics and we find that $$f(x)\sim b {(x-t)^{-1/2}\over x^{1/4}} \exp\left\lbrace
2 t x^{1/2} - {2\over 3} x^{3/2} + \int_x^\infty
\left\lbrack \sqrt{{(z-t)^2-\mu\over z}}-z^{1/2} + t z^{-1/2}\right\rbrack
\, dz\right\rbrace$$ for some constant $b=b(t)$. Now the integral in the exponential is $$-{\mu\over 2} t^{-1/2} \log{\left(\sqrt{x}+\sqrt{t}\right)^2\over
x-t} + {\rm o}(1)$$ and so $$f(x)\sim b {\left(x-t\right)^{{1\over 2}t^{-1/2}\mu-{1\over 2}}\over
x^{1/4} \left(\sqrt{x}+\sqrt{t}\right)^{t^{-1/2}\mu}}
\exp\left\lbrace 2 t x^{1/2} - {2\over 3} x^{3/2}\right\rbrace
\ \ \ (x-t>>t^{1/4})
\label{appx5}$$ and specializing to the region $t^{1/4}<<x-t<<t^{1/2}$ gives $$\begin{aligned}
f(x)&\sim& b\,  2^{-t^{-1/2}\mu} t^{-3/4} \left({t\over x-t}\right)^{
-{1\over 2} t^{-1/2}\mu +{1\over 2}}\exp\left\lbrace
{4\over 3} t^{3/2} - {1\over 2} (x-t)^2\right\rbrace\label{appx6} \\
&&\hspace{3in}  (t^{1/4}<<x-t<<t^{1/2}) \nonumber
\end{aligned}$$

### The region $\vert x-t \vert <<t$ {#subsubsec:region4}

If in equation ([\[eig_eqn2\]](#eig_eqn2){reference-type="ref" reference="eig_eqn2"}) we set $$g(x)=h\left(\sqrt{2} t^{-1/4}(t-x)\right)=h(y)$$ and write $\varepsilon = (\sqrt{2} t^{3/4})^{-1}$ then the equation becomes $$\left(1-\varepsilon y\right) h^{\prime\prime}(y)
+\left\lbrack {\mu\over 2 t^{1/2}} - {y^2\over 4} + {\varepsilon^2\over
4(1-\varepsilon y)}\right\rbrack h(y)=0\, .$$ Now we expect that for bounded $y$, and therefore also if $\vert y \vert
\rightarrow\infty$ at some rate (depending upon $\varepsilon$), the solution of this will be asymptotic to a solution of $$h^{\prime\prime}(y) +\left( {\mu\over 2 t^{1/2}}-{y^2\over 4}\right)
h(y)=0\, ,$$ Weber's equation. Now unless $${\mu\over 2 t^{1/2}} = i + {1\over 2} \ \ \ (i=0,1,\cdots)$$ there is no solution which vanishes at both $\pm\infty$. But ([\[appx4\]](#appx4){reference-type="ref" reference="appx4"}) and ([\[appx6\]](#appx6){reference-type="ref" reference="appx6"}) show that in their regions of validity (which overlap with our present region) $f(x)$ is a factor depending on $t$ times a factor tending exponentially to $0$ as $x-t\rightarrow\pm\infty$. Hence our eigenvalues must satisfy $${\mu_i\over 2 t^{1/2}}= i +{1\over 2} + {\rm o}(1)$$ and $h(y)$ is asymptotically a constant times the parabolic cylinder function $D_i(y)$ (see, e.g. [@erdelyi], Chp. 8). Thus (since $x\sim t$ in the present situation) $$f(x)\sim c\,  D_i\left(\sqrt{2} t^{-1/4} (t-x)\right)
\label{appx7}$$ for some constant $c=c(t)$. Using the known asymptotics of $D_i$ we find $$f(x)\sim c \left(\sqrt{2} t^{-1/4}(t-x)\right)^i \exp\left\lbrace
-{1\over 2} t^{-1/2} (t-x)^2\right\rbrace
\label{appx8}$$ Comparing this with ([\[appx4\]](#appx4){reference-type="ref" reference="appx4"}) gives $$c\sim {2^{-{5\over 2}i-2}\over \sqrt{\pi}} t^{-{3\over 4}i - {3\over 4}}
\exp\left({4\over 3} t^{3/2}\right)\, .
\label{appx9}$$ We also find, using ([\[appx6\]](#appx6){reference-type="ref" reference="appx6"}), that $b\sim 1/2\sqrt{\pi}$.

### The asymptotics of $\lambda_i$

If we look at the asymptotics of $f_i(x)$ (the eigenfunction associated with the eigenvalue $\mu_i$ of $L$, normalized so that $f_i(0)=1$) given by ([\[appx1\]](#appx1){reference-type="ref" reference="appx1"}), ([\[appx3\]](#appx3){reference-type="ref" reference="appx3"}), ([\[appx5\]](#appx5){reference-type="ref" reference="appx5"}), and ([\[appx8\]](#appx8){reference-type="ref" reference="appx8"}) we see that the main contribution to $\int_0^\infty f_i(x)^2\,dx$ comes from any region $$t^{-1/4}\vert t-x \vert < \eta(t)$$ as long as $\eta(t)\rightarrow\infty$. For some such region we have, by ([\[appx7\]](#appx7){reference-type="ref" reference="appx7"}) and ([\[appx9\]](#appx9){reference-type="ref" reference="appx9"}), $$f_i(x) \sim {2^{-{5\over 2}i-2}\over\sqrt\pi} t^{-{3\over 4}i - {3\over 4}}
D_i\left(\sqrt{2} t^{-1/4}(t-x)\right) \, .$$ Using this, and the fact $\int_{-\infty}^\infty D_i(x)\, dx =\sqrt{2\pi} i!$, we deduce $$\int_0^\infty f_i(x)^2\, dx \sim {i!\over\sqrt\pi} 2^{-5i-4}
t^{-{3\over 2}i-{5\over 4}} \exp\left({8\over 3}t^{3/2}\right)\, .
\label{appx10}$$ This was the goal of all that went before.

Since $L$ has simple eigenvalues and commutes with our integral operator $K$ (translated to $(0,\infty)$) the set $\lbrace f_i\rbrace$ is the set of eigenfunctions of $K$ corresponding to its eigenvalues $\lbrace \lambda_i\rbrace$. However $f_i$ corresponds to $\mu_i$ and there is no assurance that the corresponding eigenvalue of $K$ is its $i^{\rm th}$ largest, which we have denoted by $\lambda_i$. We shall eventually show that this is actually the case. The first lemma of this section shows that the eigenvalues of $K$ are simple, and this is crucial for the argument we shall later use. (The proof of the corresponding result for the sine kernel is in [@slepian_pollak].)

::: lemma
If $f_1$ and $f_2$ are eigenfunctions of $L$ corresponding to distinct eigenvalues, then they are eigenfunctions of $K$ corresponding to distinct eigenvalues.
:::

Proof. The eigenvalues of $K$ are the squares of the eigenvalues of the operator on $(0,\infty)$ with kernel $A(x+y-2t)$. So we have to show that if for some $\nu$ we have either $$\int_0^\infty A(x+y-2t) f_i(y)\, dy = \nu f_i(x) \ \ \ (i=1,2)
\label{eig1}$$ or $$\int_0^\infty A(x+y-2t) f_1(y)=\nu f_1(x)\, , \ \ \int_0^\infty
A(x+y-2t) f_2(y)\, dy = -\nu f_2(x)
\label{eig2}$$ then $f_1=f_2$. (Recall that all eigenfunctions are normalized to satisfy $f(0)=1$.)

Assuming first that ([\[eig1\]](#eig1){reference-type="ref" reference="eig1"}) holds, apply $d^2/dx^2$ to both sides of the identity with $i=1$ and integrate the resulting integral by parts twice. What results is $$\nu f_1^{\prime\prime}(x)=-A^\prime(x-2t)+A(x-2t)f_1^\prime(0)+
\int_0^\infty A(x+y-2t) f_1^{\prime\prime}(y)\, dy\, .$$ If we multiply both sides by $f_2(x)$ and integrate we obtain, using ([\[eig1\]](#eig1){reference-type="ref" reference="eig1"}) with $i=2$ (and its differentiated version), $$\nu \int_0^\infty f_1^{\prime\prime}(x) f_2(x)\, dx =
-\nu f_2^\prime(0)+\nu f_1^\prime(0) +\nu\int_0^\infty f_2(y)
f_1^{\prime\prime}(y)\, dy\, .$$ Thus, since $\nu\neq 0$ (this follows easily from the fact that the Fourier transform of $A(x)$ is nonzero), we have $f_1^\prime(0)=f_2^\prime(0)$. But it is clear from ([\[eig_eqn1\]](#eig_eqn1){reference-type="ref" reference="eig_eqn1"}) that for any eigenfunction $f$ we have $f^\prime(0)=t^2-\mu$. Thus $f_1$ and $f_2$ correspond to the same eigenvalue of $L$ and so are equal.

The case when ([\[eig2\]](#eig2){reference-type="ref" reference="eig2"}) holds is even easier. Differentiating both sides of the first relation once and integrating by parts gives $$\nu f_1^\prime(x) = - A(x-2t)-\int_0^\infty A(x+y-2t) f_1^\prime(y)
\, dy\, .$$ Multiplying both sides of this by $f_2(x)$ and integrating, using the second relation of ([\[eig2\]](#eig2){reference-type="ref" reference="eig2"}), we obtain $$\nu \int_0^\infty f_1^\prime(x) f_2(x)\, dx =
-\nu+\nu \int_0^\infty f_2(y) f_1^\prime(y)\, dy\, ,$$ contradicting $\nu\neq 0$. 0◻

Since, as we now know, the eigenvalues of $K$ are simple, there is a permutation $\sigma$ of ${\rm{\bf N}}=\lbrace 0,1,2,\cdots\rbrace$ such that $f_i$ is the eigenfunction of $K$ corresponding to its $\sigma(i)^{th}$ largest eigenvalue $\lambda_{\sigma(i)}$; this permutation is independent of $t$ or else, by the continuity of the eigenvalues in $t$, there would be a multiple eigenvalue for some $t$.

Up to now our kernel $K$ corresponded to an arbitrary factor $\lambda$. Of course formula ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}) refers to the case $\lambda=1$.

::: lemma
[]{#lemma:two label="lemma:two"} For each $i$ we have $\lambda_i\rightarrow 1$ as $s\rightarrow -\infty$.
:::

Proof. In this case $\lambda=1$ formula ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) reads $$K(x,y)=\int_0^\infty {\rm Ai}(x+z) {\rm Ai}(z+y) \, dz \, .
\label{K_identity2}$$ For the purposes of this proof we denote by $A$ (resp. $K$) the operator on $(-\infty,\infty)$ with kernel ${\rm Ai}(x+y)$ (resp. $K(x,y)$) and by $P_s$ the projection from $L_2(-\infty,\infty)$ to $L_2(s,\infty)$. So the $\lambda_i$ are the eigenvalues of $P_s K P_s$. Now it is known [@hastings_mcleod] that $A^2=I$, and ([\[K_identity2\]](#K_identity2){reference-type="ref" reference="K_identity2"}) says that $K=A P_0 A$. Thus $K^2=A P_0 A^2 P_0 A = A P_0 A = K$. In other words, $K$ is a projection operator. (This is not surprising since its kernel is a scaling limit of the kernels $K_N(x,y)$ of projection operators.)  Clearly it has infinite-dimensional range. It now follows easily from the minimax characterization of the eigenvalues that, for each $i$, the $i^{\rm th}$ largest eigenvalue of $P_s K P_s$ tends to $1$ as $s\rightarrow -\infty$. 0◻

We now state a lemma which is the basis of a trick used by Fuchs [@fuchs64] in his derivation of the asymptotics of the eigenvalues of the sine kernel.

::: lemma
Let $J(x,y)$ be a symmetric kernel, on a fixed interval, depending smoothly on a parameter $t$. Let $g$ be an eigenfunction normalized so that $\int g(x)^2\, dx = 1$ and let $\lambda$ be the corresponding eigenvalue. Then, with the subscript $t$ denoting $\partial/\partial t$, we have $$\lambda_t = \int\int J_t(x,y) g(y) g(x) \,dydx\, .$$
:::

Proof. From $$\int J(x,y) g(y)\, dy = \lambda g(x)
\label{J_eqn}$$ we get $$\int J_t(x,y) g(y)\, dy +\int J(x,y) g_t(y)\, dy =
\lambda_t g(x)+  \lambda g_t(x) \, .$$ Multiplying both sides by $g(x)$ and integrating over $x$, we obtain (using the normalization of $g$ and ([\[J_eqn\]](#J_eqn){reference-type="ref" reference="J_eqn"})) $$\begin{aligned}
\int\int J_t(x,y) g(y) g(x)\, dydx + \int\int J(x,y) g_t(y) g(x) \, dx dy
&=&\lambda_t + \lambda \int g_t(x) g(x)\, dx \\
&=&\lambda_t + \int\int J(x,y) g(y) g_t(x)\, dy dx\, .
\end{aligned}$$ By symmetry of $J$ the two double integrals involving it cancel, and we obtain the statement of the lemma. 0◻

We apply the lemma to the opertor with kernel $A(x+y-2t)$ on $(0,\infty)$ whose square is our Airy operator (translated to act on $(0,\infty)$). Thus we may write its eigenvalues as $\sqrt{\lambda_{\sigma(i)}}$, where the square roots might have either sign. The lemma gives $${\partial\over\partial t}\sqrt{\lambda_{\sigma(i)}} = -2 \int_0^\infty\int_0^\infty
A^\prime(x+y-2t) g_i(y) g_i(x)\, dy dx
\label{lambda_eqn}$$ where $$g_i(x) = f_i(x)\biggl/   \left\lbrace \int_0^\infty f_i(y)^2\, dy
\right\rbrace^{1/2}\, .$$ But from $$\int_0^\infty A(x+y-2t) g_i(y)\, dy = \sqrt{\lambda_{\sigma(i)}} g_i(x)$$ we obtain upon differentiation that $$\int_0^\infty A^\prime(x+y-2t) g_i(y)\, dy = \sqrt{\lambda_{\sigma(i)}} g_i^\prime(x)$$ so ([\[lambda_eqn\]](#lambda_eqn){reference-type="ref" reference="lambda_eqn"}) may be rewritten $${\partial\over\partial t}\sqrt{\lambda_{\sigma(i)}} = -2 \sqrt{\lambda_{\sigma(i)}}
\int_0^\infty g_i^\prime(x) g_i(x)\, dx\, .$$ The integral is of course $-{1\over 2} g_i(0)^2$. Recalling that $f_i(0)=1$ we see that we have established the relation $${\partial\over\partial t}\sqrt{\lambda_{\sigma(i)}} =\sqrt{\lambda_{\sigma(i)}}\biggl/ \left\lbrace
\int_0^\infty f_i(x)^2\, dx \right\rbrace \, ,$$ or $${\partial\over\partial t}\log\lambda_{\sigma(i)}= 2\biggl/ \left\lbrace
\int_0^\infty f_i(x)^2\, dx \right\rbrace \,$$

We now use ([\[appx10\]](#appx10){reference-type="ref" reference="appx10"}) and integrate the resulting relation with respect to $t$ from $t$ to $\infty$. Recalling Lemma [\[lemma:two\]](#lemma:two){reference-type="ref" reference="lemma:two"}, we deduce $$-\log\lambda_{\sigma(i)}\sim {\sqrt\pi\over i!} 2^{5i+3} t^{{3\over 2}i+{3\over 4}}
\exp\left(-{8\over 3} t^{3/2}\right)\, ,$$ precisely the right side of ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}).

All that remains now is to show that $\sigma(i)=i$ for all $i$. But it is clear from this asymptotic relation that $i<j$ implies $\lambda_{\sigma(i)}>\lambda_{\sigma(j)}$ for large $t$ (and so for all $t$), so that $\sigma(i)<\sigma(j)$. Thus $\sigma$ is order preserving, and since $\sigma:{\rm{\bf  N}}\rightarrow {\rm{\bf  N}}$ is onto we must have $\sigma(i)=i$ for all $i$.

This concludes the derivation of ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}). The deduction of ([\[r_asy\]](#r_asy){reference-type="ref" reference="r_asy"}) from ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}) is completely analogous to the corresponding deduction for the sine kernel in ref. [@tw1], Sec. VIIB.

We wish to thank E. Brézin, P. J. Forrester, F. A. Grünbaum and J. Harnad for helpful comments. This work was supported in part by the National Science Foundation, DMS--9001794 and DMS--9216203, and this support is gratefully acknowledged.

::: references
M. J. Ablowitz and H. Segur, *Exact linearization of a Painlevé transcendent*, Phys. Rev. Letts. **38** (1977) 1103--1106.

E. L. Basor, C. A. Tracy, and H. Widom, *Asymptotics of level spacing distributions for random matrices*, Phys. Rev. Letts. **69** (1992) 5--8.

M. J. Bowick and E. Brézin, *Universal scaling of the tail of the density of eigenvalues in random matrix models*, Phys. Letts. **B268** (1991) 21--28.

A. Erdélyi (ed.), *Higher Transcendental Functions*, Vol. II (McGraw-Hill, New York, 1953).

P. A. Clarkson and J. B. McLeod, *A connection formula for the second Painlevé transcendent*, Arch. Rat. Mech. Anal. **103** (1988) 97--138.

P. A. Clarkson and J. B. McLeod, *Integral equations and connection formulae for the Painlevé equations*, in *Painlevé Transcendents: Their Asymptotics and Physical Applications*, eds. D. Levi and P. Winternitz (Plenum Press, New York, 1992), pgs. 1--31.

F. J. Dyson, *Statistical theory of energy levels of complex systems, I, II, and III*, J. Math. Phys. **3** (1962) 140--156; 157--165; 166--175.

F. J. Dyson, *Fredholm determinants and inverse scattering problems*, Commun. Math. Phys. **47** (1976) 171--183.

F. J. Dyson, *The Coulomb fluid and the fifth Painlevé transcendent*, IASSNSS-HEP-92/43 preprint, to appear in the proceedings of a conference in honor of C. N. Yang, ed. S.-T. Yau.

P. J. Forrester, *The spectrum edge of random matrix ensembles*, preprint.

W. H. J. Fuchs, *On the eigenvalues of an integral equation arising in the theory of band-limited signals*, J. Math. Anal. and Applic. **9** (1964) 317--330.

J. Harnad, C. A. Tracy, and H. Widom, *Hamiltonian structure of equations appearing in random matrices*, in preparation.

S. P. Hastings and J. B. McLeod, *A boundary value problem associated with the second Painlevé transcendent and the Korteweg-de Vries equation*, Arch. Rat. Mech. Anal. **73** (1980) 31--51.

E. L. Ince, *Ordinary Differential Equations*, (Dover, New York, 1956).

A. R. Its, A. G. Izergin, V. E. Korepin, and N. A. Slavnov, *Differential equations for quantum correlation functions*, Int. J. Mod. Physics B **4** (1990) 1003--1037.

K. Iwasaki, H. Kimura, S. Shimomura, and M. Yoshida, *From Gauss to Painlevé: A Modern Theory of Special Functions* (Vieweg, Braunschweig, 1991).

M. Jimbo, T. Miwa, Y. Môri, and M. Sato, *Density matrix of an impenetrable Bose gas and the fifth Painlevé transcendent*, Physica **1D** (1980) 80--158.

B. M. McCoy, C. A. Tracy, and T. T. Wu, *Connection between the KdV equation and the two-dimensional Ising model*, Phys. Letts. **61A** (1977) 283--284.

J. B. McLeod, private communication.

M. L. Mehta, *Random Matrices*, 2nd edition (Academic, San Diego, 1991).

M. L. Mehta, *A non-linear differential equation and a Fredholm determinant*, J. de Phys. I France, **2** (1992) 1721--1729.

M. L. Mehta and G. Mahoux, *Level spacing functions and non-linear differential equations*, preprint.

G. Moore, *Matrix models of 2D gravity and isomonodromic deformation*, Prog. Theor. Physics Suppl. No. **102** (1990) 255--285.

J. Moser, *Geometry of quadrics and spectral theory*, in *Chern Symposium 1979* (Springer, Berlin, 1980), 147--188.

P. Painlevé, *Sur les équations différentielles du second ordre et d'ordre supérieur dont l'intégrale générale est uniforme*, Acta Math. **25** (1902) 1--85.

C. E. Porter, *Statistical Theory of Spectra: Fluctuations* (Academic, New York, 1965).

D. Slepian and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty-I*, Bell Systems Tech. J. **40** (1961) 43--64.

C. A. Tracy and H. Widom, *Introduction to random matrices*, to appear in the proceedings of the $8^{th}$ Scheveningen Conference, Springer Lecture Notes in Physics.

C. A. Tracy and H. Widom, *Level spacing distributions and the Airy kernel*, submitted to Phys. Letts. B.

H. Widom, *The strong Szegö limit theorem for circular arcs*, Indiana Univ. Math. J. **21** (1971) 277--283.

H. Widom, *The asymptotics of a continuous analogue of orthogonal polynomials*, to appear in J. Approx. Th.
:::
