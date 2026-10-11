---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-004-iv-asymptotics
section_title: "ASYMPTOTICS"
section_number: IV
pages: 17-21
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
text_source: latex
latex_prose_ratio: 0.781
latex_coverage_ratio: 1.0
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
