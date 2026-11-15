---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-014-423-the-region-x-tt14
section_title: "The region $x-t>>t^{1/4}$"
section_number: 4.2.3
pages: 23-25
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.635
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
[]{#subsubsec:region1 label="subsubsec:region1"} If we make the substitutions $$f(x) = h(t^2x)=h(y)$$ then ([\[eig_eqn1\]](#eig_eqn1){reference-type="ref" reference="eig_eqn1"}) becomes $$\left(y h^\prime(y) \right)^\prime - h(y) = t^{-2}\left(
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
