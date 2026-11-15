---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-004-5-higher-order-terms-in-the-neumann-zagier-asymp
section_title: "Higher order terms in the Neumann-Zagier asymptotic formula"
section_number: 5
pages: 13-15
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.973
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
[]{#degree4_NZ label="degree4_NZ"}

Let $M$ be a cusped hyperbolic 3-manifold with horospherical torus cross section $T$, and chose meridian and longitude generators for $H_1(T)=\mathbb{Z}^2$ as in section [\[cusped_hyp\]](#cusped_hyp){reference-type="ref" reference="cusped_hyp"}. Let $u,v$ denote the logarithms of the holonomies of the meridian and longitude respectively, chosen so that $u=v=0$ at the complete hyperbolic structure on $M$. Then $-v$ has a power series expansion $$\label{eq21}
 -v = \sum_{n=1}^\infty   c_n u^n ,$$ where $c_n=0$ for all even $n$ and $c_1 = -\tau$ where $\tau$ is our cusp shape parameter.[^1]

Then Neumann and Zagier [@NZ equation (62), p328]) derive the following asymptotic formula for the decrease in volume $\Delta V$ during Dehn filling for $(p,q)$ Dehn filling on one cusp $T$ of the cusped hyperbolic 3-manifold $M$: $$\label{eq22}
\Delta V = {|\text{Im}\,(c_1)| \pi^2 \over |z|^2} -
{2 \pi^4}\,\text{Im}\, \left[  {c_3  \over z^4}\right] + O \left({1 \over |z|^6}\right),$$ where $z =  p + q \tau$.

If we write $z = r e^{i \theta}$, then this becomes $$\label{eq23}\Delta V = {|\text{Im}\,(\tau)| \pi^2 \over r^2} -
{2 \pi^4 \over r^4 }\text{Im}\, \left[  c_3 e^{-4 i\theta}\right] + O \left({1 \over r^6}\right).$$

We now give some calculations for the manifolds studied in the previous sections.

::: ex
[]{#m004_NZ4 label="m004_NZ4"} *For $m004$, Neumann and Zagier ([@NZ p331]) show that $c_1 = 2 \sqrt{-3}=-\tau$ and $c_3 = {2 \sqrt{-3} \over 3}$, and obtain the following asymptotic formula: $$\label{eq24}\Delta V_{m004}(p,q) = {2 \sqrt{3} \pi^2 \over p^2+12q^2}
-{4\sqrt{3}(p^4-72p^2q^2+144q^4)\pi^4 \over 3(p^2 + 12 q^2)^4} + O \left({1 \over (p^2 + 12 q^2)^3}\right).$$ Writing $z = p + \tau q = r e^{i \theta}$ as above, this simplifies to $$\label{eq25}
\Delta V_{m004} = {2 \sqrt{3} \pi^2 \over r^2} -
{4 \pi^4 \cos(4\theta) \over \sqrt{3} r^4 }+ O \left({1 \over r^6}\right).$$*
:::

::: ex
[]{#m003_NZ4 label="m003_NZ4"}

*Let $WL$ denote the Whitehead link complement as drawn in Figure [\[fig.WL_WS\]](#fig.WL_WS){reference-type="ref" reference="fig.WL_WS"} (and in [@HMW], [@NR]), with the standard topological choice of meridians and longitudes. Then Hodgson-Meyerhoff-Weeks [@HMW Figure 8 with $p=q=1$] show that the hyperbolic Dehn fillings $WL(1,1)(m,l)$ and $WL(-5,1)(m,-l-m/2)$ have equal volumes since they have homeomorphic 2-fold covers, whenever $m,l$ are relatively prime integers with $m$ a multiple of $4$.*

Now $WL(1,1)$ and $WL(-5,1)$ are homeomorphic to $m004$ and $m003$ respectively. In fact, using SnapPy or Snap, there are isometries taking $WL(1,1)(m,l)$ to $m004(m,l)$ and $WL(-5,1)(m,-l-m/2)$ to $m003(m/2-l,2l)$. Hence we have $$\label{eq26}\text{Vol} (m004(m,l)) =  \text{Vol} (m003(a,b))$$ for hyperbolic Dehn fillings such that $(a,b)=(m/2-l,2l)$ and $(m,l)=(2a+b,b/2)$ for pairs of relatively prime integers with $m$ a multiple of 4.

Since the volume is a real analytic function on hyperbolic Dehn surgery space (using $u$ as coordinate, as in [@NZ]), it follows that ([\[eq26\]](#eq26){reference-type="ref" reference="eq26"}) holds for all large real values of $(p,q)$. Hence we can deduce the asymptotic formula for decrease in volume for $m003$: $$\begin{aligned}
\label{eq27}
\Delta V_{m003}(a,b) &= \Delta V_{m004}(2a+b,b/2) \notag\\
&=  \frac{\sqrt{3} \pi ^2}{2 \left(a^2+a b+b^2\right)}
-\frac{\pi ^4 \left(-18 b^2 (2 a+b)^2+(2 a+b)^4+9 b^4\right)}{64 \sqrt{3} \left(a^2+a
   b+b^2\right)^4}
 + \ldots
 
\end{aligned}$$ Introducing polar coordinates $r e^{i \theta} =  a+ b \omega$, this simplifies to $$\label{eq28}
\Delta V_{m003}(a,b) =   { \sqrt{3} \pi^2 \over 2 r^2} - { \pi^4 \over 4 \sqrt{3}}{ \cos(4\theta) \over r^4} + 
O\left({1 \over r^6}\right).$$
:::

::: ex
[]{#m125_NZ4 label="m125_NZ4"}

*For the Whitehead link sister $m125$, Aaber and Dunfield [@AD] study the Neumann-Zagier asymptotic expansion of volume for Dehn fillings. If $u,v$ denote the logarithms of holonomies of the meridian and longitude for the geometric basis for cusp 0 of $m125$, then they show [@AD p1019] that $$\label{eq29}
-v = i u + { -3 + i \over 48} u^3 +  \ldots$$ so $c_1 = -\tau = i$ and $c_3 = {-3 + i \over 48}$ in our notation. This gives the following asymptotic formula for decrease in volume for surgeries on cusp 0: $$\label{eq30}
\Delta V_{m125} (p,q)=  
{ \pi^2 \over |z|^2} -
{2 \pi^4}\,\text{Im}\, \left[  {-3 + i \over 48 z^4}\right] + O \left({1 \over |z|^6}\right),$$ where $z =  p + q \tau = p - q i$.*

More explicitly: $$\label{eq31}
\Delta V_{m125} (p,q)=  
{ \pi^2 \over p^2+q^2} -
\frac{\pi^4(p^4-12 p^3 q-6 p^2 q^2+12 p q^3+q^4)}{ 24\left(p^2+q^2\right)^4}
+ O \left({1 \over (p^2+q^2)^3}\right).$$
:::

::: ex
[]{#m129_NZ4 label="m129_NZ4"}

*For the Whitehead link complement $WL$ (as drawn in Figure [\[fig.WL_WS\]](#fig.WL_WS){reference-type="ref" reference="fig.WL_WS"}) we can compute the asymptotic expansion for $\Delta V$ using the work of Neumann-Reid [@NR]. Let $u,v$ denote the logarithms of holonomies of the standard meridian and longitude for the link complement. Then [@NR] shows that $$u = \log x + \log(x+1) - \log(x-1) \text{ and } v = 4 \log x - 2\pi i,$$ where $x \in \mathbb{C}$ is a suitable simplex parameter. From these equations we obtain $$e^u = { x(x+1) \over (x-1)} \text{ where } x = i e^{-v/4}.$$ This gives a quadratic equation for $x$ with the relevant solution given by $$x=\frac{1}{2} \left(\sqrt{-6 e^u+e^{2 u}+1}+e^u-1\right) = i e^{-v/4},$$ and so $$\begin{aligned}
 \label{eq32}
-v &= -4 \log\left(\frac{-i}{2} \left(\sqrt{-6 e^u+e^{2 u}+1}+e^u-1\right)\right) \notag\\
&= (-2+2i) u + {i u^3 \over 6} +  O(|u|^5) .
\end{aligned}$$ Hence $c_1 = -\tau = (-2+2i)$ and $c_3= { i \over 6}$ in our previous notation.*

This gives the following asymptotic formula for decrease in volume for Dehn filling on one cusp of $WL$: $$\label{eq33}
\Delta V_{WL} (p,q)=  
{ 2 \pi^2 \over |z|^2} -
{2 \pi^4}\,\text{Im}\, \left[  { i \over 6 z^4}\right] + O \left({1 \over |z|^6}\right),$$ where $z =  p + q \tau = p + q (2-2i)$. Hence $$\label{eq34}
\Delta V_{WL}(p,q)=
\frac{2 \pi ^2}{p^2+4 p q+8 q^2}-\frac{\pi ^4 \left(p^2-8 q^2\right) \left(p^2+8 p q+8 q^2\right)}{3 \left(p^2+4 p q+8
   q^2\right)^4} + \ldots.$$

We can convert from the standard peripheral curves for $WL$ to the geometric peripheral curves on $m129$ using: $WL(p,q)=m129(a,b)$ where $a=p+2q,  b=-q$ or $p=a+2b,q = -b$. Then the new cusp shape parameter for $m129$ is $\tau' = -2 i$ and $$\begin{aligned}
\label{eq35}
\Delta V_{m129}(a,b) &= \Delta V_{WL}(a + 2 b, -b) \notag\\
&= \frac{2 \pi ^2}{a^2+4 b^2} -\frac{\pi ^4 \left(a^4-24 a^2 b^2+16 b^4\right)}{3 \left(a^2+4 b^2\right)^4}
+ \ldots
\end{aligned}$$
:::

[^1]: In [@NZ], a non-standard orientation convention for meridian and longitude was used; this was pointed out in [@NR]. Replacing the basis in [@NZ] by $meridian, -(longitude)$ corresponding to $u,-v$ gives our version of the Neumann-Zagier formula.
