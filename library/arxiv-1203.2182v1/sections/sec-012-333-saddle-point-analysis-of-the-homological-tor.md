---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-012-333-saddle-point-analysis-of-the-homological-tor
section_title: "Saddle point analysis of the homological torus knot invariants"
section_number: 3.3.3
pages: 42-50
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.987
---
[]{#sec:saddle_point label="sec:saddle_point"}

In this section we analyze general $(2,2p+1)$ torus knots ($p \ge 1$). For this class of knots, the quantum refined curves $\widehat{A}^{\text{ref}}_{T^{2,2p+1}}(\widehat{x},\widehat{y};q,t)$ are not known at present (apart from the case of trefoil, *i.e.* $p=1$, with the quantum curve determined in ([\[RefineRecursion\]](#RefineRecursion){reference-type="ref" reference="RefineRecursion"})). Therefore, we cannot determine refined $A$-polynomials by taking the classical limit of $\widehat{A}^{\text{ref}}$, as we did for the trefoil knot or for the unknot. Nevertheless, we can determine refined $A$-polynomials from the asymptotic behavior of the colored superpolynomials and their specializations ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}). For general values of $p$, we determine parametric representation of such $A$-polynomials, and for several first values of $p$ we rewrite this parametric form as a polynomial $A^{\text{ref}}_{T^{2,2p+1}}(x,y;t)$, see Table [1](#table_A-poly4){reference-type="ref" reference="table_A-poly4"}.

There is one fundamental difference between the specialization $P_{n}(K;q,t)$ of the colored superpolynomial for torus knots found in ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}) and that of the unknot ([\[Pnunkot\]](#Pnunkot){reference-type="ref" reference="Pnunkot"}). Namely, the latter is given by an infinite product, whose asymptotic expansion is obtained simply from the expansion of the quantum dilogarithm ([\[q-dlog_exp\]](#q-dlog_exp){reference-type="ref" reference="q-dlog_exp"}). On the other hand, the homological invariants of torus knots are expressed as infinite sums, with each term in those sums given by infinite products. Therefore, the analysis of the asymptotic behavior for torus knots is more delicate and requires new methods.

In order to find the "refined volume" $S_0(u,t)$ for torus knots, we apply the saddle point approximation [@Hikami_exp; @Hikami:2007zz] to ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}) and replace the quantum dilogarithm function by $$\begin{aligned}
(z;q)_{k}\sim e^{\frac{1}{\hbar}\left({\rm Li}_2(z)-{\rm Li}_2(zq^k)\right)} \,.
\label{q-dilog_approx}
\end{aligned}$$ Furthermore, via an analytic continuation we can approximate the summation in ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}), in the asymptotic limit ([\[reflimit\]](#reflimit){reference-type="ref" reference="reflimit"}), by the following integral: $$\boxed{\phantom{\int^1}
P_{n}(T^{2,2p+1};q,t) \; \sim \; \int dz\; e^{\frac{1}{\hbar}\left(V_{(2,2p+1)}(z,x;t)+{\cal O}(\hbar)\right)} \,, \phantom{\int^1}}
\label{Pn-saddle}$$ with the "potential" function $$\begin{aligned}
&& V_{(2,2p+1)}(z,x;t)
:=-p\log (-t)\cdot \log x+(p+1)\pi i\log x+\log (x^{\frac{1}{2}}z^{-1})\cdot\log t
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad
+(2p+1)\Biggl(
\pi i\log z+\frac{1}{2}\left((\log x)^2-(\log z)^2\right)
+\log (x^{\frac{3}{2}}z^{-1})\cdot \log t\Biggr)
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad
+{\rm Li}_2(z)-{\rm Li}_2(x)-{\rm Li}_2(t^2z)+{\rm Li}_2(-t^3x)
+{\rm Li}_2(t^2xz)
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad
-{\rm Li}_2(-t^3xz)
+{\rm Li}_2(xz^{-1})
-{\rm Li}_2(-txz^{-1})
+{\rm Li}_2(-t)-{\rm Li}_2(1),
\end{aligned}$$ and where the parameter $z$ is related to $\ell$ in ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}) via $\ell=\frac{1}{\hbar}\log z$.

Now, the dominant contribution to this integral comes from the saddle point[^1] $$\begin{aligned}
\frac{\partial V_{(2,2p+1)}(z,x;t)}{\partial z}\Bigg|_{z=z_0}=0,
\label{saddle_point}
\end{aligned}$$ and the value of the "potential" $V(z,x;t)$ at this saddle point determines $S_0(u,t)$: $$\begin{aligned}
V_{(2,2p+1)}(z_0,x;t) \; = \; S_0(u,t) \,.
\end{aligned}$$ For the above potential $V_{T^{2,2p+1}}(z,x;t)$, the critical point condition can simply be expressed as $1=\exp\left(z\partial V_{(2,2p+1)}/\partial z\right)|_{z=z_0}$: $$\begin{aligned}
1 \; = \; -\frac{t^{-2-2p}(x-z_0)z_0^{-1-2p}(-1+t^2z_0)(1+t^3 xz_0)}{(-1+z_0)(tx+z_0)(-1 +  t^2 x z_0)} \,.
\label{braid_saddle1}
\end{aligned}$$

Moreover, according to ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}), the solution of $A^{\text{ref}}_{T^{2,2p+1}}(x,y;t)=0$ is related to $S_0(u,t)$ via $$\begin{aligned}
y(x,t)&=&\exp\left(x\frac{\partial V_{(2,2p+1)}(x,z_0;t)}{\partial x}\right)
\nonumber \\
&=&\frac{t^{2 + 2 p} (-1 + x) x^{1 + 2 p} (t x + z_0) (1 + t^3 x z_0)}{(1 + t^3 x) (x - z_0) (-1 + t^2 x z_0)} \,.
\label{braid_saddle2}
\end{aligned}$$ The equations ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}) and [\[braid_saddle2\]](#braid_saddle2){reference-type="eqref" reference="braid_saddle2"} constitute our desired result: they provide an expression for the refined $A$-polynomial, parametrized by $z_0$, for a general $(2,2p+1)$ torus knot. Moreover, for a fixed value of $p$ it is possible to eliminate $z_0$ from these equations and write an explicit form of the refined $A$-polynomials $A^{\text{ref}}_{T^{2,2p+1}}(x,y;t)$. For $p=1,2,3,4$, the explicit expressions of the refined $A$-polynomials are presented in Table [1](#table_A-poly4){reference-type="ref" reference="table_A-poly4"}.

::: {#table_A-poly4}
   **Knot**   $A_K^{\text{ref}} (x,y;t)$
  ----------- ------------------------------------------------------------------------------------------------------------------------------
   $T^{2,3}$  $y^2 -$$\frac{1}{1+ x t^3}$$(1 - x t^2 + x^3 t^5 + x^4 t^6 + 2 x^2 t^2+2 x^2 t^3)y
               +$$\frac{(x-1) x^3 t^4}{1 + x t^3}$
   $T^{2,5}$  $y^3
              -$$\frac{1}{1 + t^3 x}$ $(1 - t^2 x + 2 t^2 x^2 + 2 t^3 x^2 - 2 t^4 x^3 - 2 t^5 x^3 +
               3 t^4 x^4 + 4 t^5 x^4 + t^6 x^4
              + t^7 x^5
              - t^8 x^5 + 2 t^8 x^6)y^2$
              $+$$\frac{t^6 (-1 + x) x^5}{(1 + t^3 x)^2}$ $(
              2 - t^2 x + t^3 x + 3 t^2 x^2 + 4 t^3 x^2 + t^4 x^2 + 2 t^5 x^3 +
               2 t^6 x^3 + 2 t^6 x^4
              + 2 t^7 x^4
              + t^9 x^5 + t^{10} x^6)y$
              $-$ $\frac{t^{12} (-1 + x)^2 x^{10}}{(1 + t^3 x)^2}$
   $T^{2,7}$  $y^4
              -$$\frac{1}{1+t^3x}$ $(
              1 - t^2 x + 2 t^2 x^2 + 2 t^3 x^2 - 2 t^4 x^3 - 2 t^5 x^3 +
               3 t^4 x^4
              + 4 t^5 x^4 + t^6 x^4
              - 3 t^6 x^5
              - 4 t^7 x^5$
              $\quad\quad
              - t^8 x^5 +
               4 t^6 x^6 + 6 t^7 x^6 + 2 t^8 x^6 + t^9 x^7 - 2 t^{10} x^7 + 3 t^{10} x^8
              )y^3$
              $+$$\frac{t^8 (-1 + x) x^7}{(1 + t^3 x)^2}$$(
              3 - 2 t^2 x + t^3 x + 6 t^2 x^2 + 8 t^3 x^2 + 2 t^4 x^2 - 3 t^4 x^3 -
               2 t^5 x^3 + t^6 x^3
              + 6 t^4 x^4 + 12 t^5 x^4$
              $\quad
              + 10 t^6 x^4 +
               4 t^7 x^4 + 3 t^7 x^5 + 2 t^8 x^5 - t^9 x^5 + 6 t^8 x^6 +
               8 t^9 x^6
              + 2 t^{10} x^6 + 2 t^{11} x^7
              - t^{12} x^7 + 3 t^{12} x^8
              )y^2$
              $-$$\frac{t^{16} (-1 + x)^2 x^{14}}{(1 + t^3 x)^3}$ $(
              3 - t^2 x + 2 t^3 x + 4 t^2 x^2 + 6 t^3 x^2 + 2 t^4 x^2 + 3 t^5 x^3 +
               4 t^6 x^3
              + t^7 x^3
              + 3 t^6 x^4
              + 4 t^7 x^4$
              $\quad + t^8 x^4 + 2 t^9 x^5 +
               2 t^{10} x^5 + 2 t^{10} x^6 + 2 t^{11} x^6 + t^{13} x^7 + t^{14} x^8
              )y+$$\frac{t^{24} (-1 + x)^3 x^{21}}{(1 + t^3 x)^3}$
   $T^{2,9}$  $y^5
              -$ $\frac{1}{1 + t^3 x}$ $(1 - t^2 x + 2 t^2 x^2 + 2 t^3 x^2 - 2 t^4 x^3 - 2 t^5 x^3 +
               3 t^4 x^4 + 4 t^5 x^4 + t^6 x^4
              - 3 t^6 x^5
              - 4 t^7 x^5$
              $\quad\quad
              - t^8 x^5
              +  4 t^6 x^6 + 6 t^7 x^6 + 2 t^8 x^6 - 4 t^8 x^7 - 6 t^9 x^7 -
               2 t^{10} x^7
              + 5 t^8 x^8 + 8 t^9 x^8
              + 3 t^{10} x^8 + t^{11} x^9$
              $\quad\quad
              -
               3 t^{12} x^9 + 4 t^{12} x^{10})y^4$
              $+$$\frac{t^{10} (-1 + x) x^9}{(1 + t^3 x)^2}$ $(4 - 3 t^2 x + t^3 x + 9 t^2 x^2 + 12 t^3 x^2 + 3 t^4 x^2 -
               6 t^4 x^3 - 6 t^5 x^3
              + 12 t^4 x^4
              + 24 t^5 x^4$
              $\quad
              + 18 t^6 x^4 +
               6 t^7 x^4
              - 6 t^6 x^5 - 9 t^7 x^5 - 6 t^8 x^5 - 3 t^9 x^5 +
               10 t^6 x^6
              + 24 t^7 x^6
              + 27 t^8 x^6 + 16 t^9 x^6$
              $\quad
              + 3 t^{10} x^6
              +  4 t^9 x^7 - 6 t^{11} x^7 - 2 t^{12} x^7 + 12 t^{10} x^8 + 18 t^{11} x^8
              +  6 t^{12} x^8 + 3 t^{13} x^9 - 3 t^{14} x^9 + 6 t^{14} x^{10})
              y^3$
              $-$ $\frac{t^{20} (-1 + x)^2 x^{18}}{(1 + t^3 x)^3}$$(6 - 3 t^2 x + 3 t^3 x + 12 t^2 x^2 + 18 t^3 x^2 + 6 t^4 x^2 -
               4 t^4 x^3
              + 6 t^6 x^3
              + 2 t^7 x^3 + 10 t^4 x^4$
              $\quad
              + 24 t^5 x^4 +
               27 t^6 x^4 + 16 t^7 x^4 + 3 t^8 x^4 + 6 t^7 x^5 + 9 t^8 x^5
              +
               6 t^9 x^5
              + 3 t^{10} x^5
              + 12 t^8 x^6 + 24 t^9 x^6$
              $\quad
              + 18 t^{10} x^6 +
               6 t^{11} x^6 + 6 t^{11} x^7 + 6 t^{12} x^7
              + 9 t^{12} x^8
              + 12 t^{13} x^8 +
               3 t^{14} x^8
              + 3 t^{15} x^9 - t^{16} x^9 + 4 t^{16} x^{10})
              y^2$
              $+$ $\frac{t^{30} (-1 + x)^3 x^{27}}{(1 + t^3 x)^4}$ $(4 - t^2 x + 3 t^3 x + 5 t^2 x^2 + 8 t^3 x^2 + 3 t^4 x^2 + 4 t^5 x^3 +
               6 t^6 x^3 + 2 t^7 x^3
              + 4 t^6 x^4$
              $\quad
              + 6 t^7 x^4 + 2 t^8 x^4 +
               3 t^9 x^5 + 4 t^{10} x^5 + t^{11} x^5 + 3 t^{10} x^6 + 4 t^{11} x^6 +
               t^{12} x^6
              + 2 t^{13} x^7
              + 2 t^{14} x^7 + 2 t^{14} x^8$
              $\quad
              + 2 t^{15} x^8 +
               t^{17} x^9 + t^{18} x^{10})y-$$\frac{t^{40} (-1 + x)^4 x^{36}}{(1 + t^3 x)^4}$

  : Refined A-polynomials for $p=1,2,3,4$.
:::

For $p=1$, this result is consistent with the semi-classical limit of the recursion relation ([\[deformed_A-poly_trefoil\]](#deformed_A-poly_trefoil){reference-type="ref" reference="deformed_A-poly_trefoil"}).

Further examples are also summarized in Appendix [\[sec:AppendixB\]](#sec:AppendixB){reference-type="ref" reference="sec:AppendixB"}. Note that for $t=-1$ the first equation above ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}) simply specifies the value of $z_0$ as $z_0^{2p+1}=-1$, while the second equation ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}) reduces to the well-known ordinary $A$-polynomial for $T^{2,2p+1}$ torus knot: $$y + x^{2p+1} = 0.$$

Let us also reveal some remarkable properties of the refined $A$-polynomials found above. We recall that the ordinary $A$-polynomials $A_{K}(x,y)$ are known to be reciprocal [@Apol; @DGLZ; @CCGL]: $$\begin{aligned}
A_{K} (x,y) \; = \; x^a y^b A_{K} (x^{-1},y^{-1}) \,.
\end{aligned}$$ This property can be understood either as a consequence of the Weyl reflection in $SL(2,{\mathbb C})$ Chern-Simons theory or, alternatively, as a symmetry induced by the orientation-preserving involution on the knot complement, $M = {\bf S}^3 \setminus K$, which acts as an endomorphism $(-1,-1)$ on $H_1 (\partial M) \cong {\mathbb Z}\times {\mathbb Z}$. It beautifully generalizes to the refined case: as a careful reader will notice, the equations ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}) and [\[braid_saddle2\]](#braid_saddle2){reference-type="eqref" reference="braid_saddle2"} are invariant under the following transformation: $$\begin{aligned}
t\to t \,, \quad  x\to -t^{-3}x^{-1} \,, \quad z\to t^{-2}z^{-1} \,, \quad  y\to t^{-2p}y^{-1} \,.
\end{aligned}$$ Therefore, the refined $A$-polynomials satisfies a deformed reciprocity: $$\begin{aligned}
\boxed{\phantom{\int^1}
A^{\text{ref}}_{T^{2,2p+1}}(x,y;t) \; = \; x^a y^b (-t)^c A^{\text{ref}}_{T^{2,2p+1}} (-t^{-3}x^{-1},t^{-2p} y^{-1};t) \,. \phantom{\int^1}}
\label{reciprocity_deform}
\end{aligned}$$

Once we found the refined $A$-polynomials, from ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}) we can also determine the classical action $S_0(u,t)$ by computing it iteratively around $t=-1$. The solutions $z_0 = z_j$ ($j=1,\cdots,2p$) for ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}) around $t=-1$ are[^2] $$\begin{aligned}
z_j&=&-\xi_j+\frac{(1+t)}{2p+1}\left(-\frac{(1+x)^2}{x}-(2p-1)\xi_j+\frac{2}{1+\xi_j}+\frac{x^2}{x+\xi_j}+\frac{1}{x(1+x\xi_j)}\right)
\nonumber \\
&&
+{\cal
 O}((1+t)^2),
\end{aligned}$$ where $\xi_j=\exp(\frac{2\pi ij}{2p+1})$, $j=1,\cdots,2p$. Plugging this solution into [\[braid_saddle2\]](#braid_saddle2){reference-type="eqref" reference="braid_saddle2"}, we find the power series expansion for $y_j (x,t)$:

$$\begin{aligned}
y_j(x,t)&=&-x^{2p+1} \\
&&
+(1+t)\frac{x^{2p+1}}{(-1+x)(x+\xi_j)(1+x\xi_j)}
(-3 x - 2 p x + 2 p x^2 - 2 \xi_j - 2 p \xi_j - x \xi_j +
 2 p x \xi_j
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad\quad\quad
- 4 x^2 \xi_j - 2 p x^2 \xi_j + x^3 \xi_j +
 2 p x^3 \xi_j - 3 x \xi_j^2 - 2 p x \xi_j^2 + 2 p x^2 \xi_j^2)
\nonumber \\
&&+{\cal O}((1+t)^2) \,. \nonumber
\end{aligned}$$ In turn, plugging this expansion into ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}), we obtain a power series expansion of the classical action $S_0(u,t)$: $$\begin{aligned}
S_0(u,t)&=&S_0(u)+\sum_{k=1}^{\infty}(t+1)^kS_0^{(k)}(u),
\nonumber \\
S_0(u)&=&\frac{1}{4p+2}\left(\log(-x^{2p+1})\right)^2,
\nonumber \\
S_0^{(1)}(u)&=&\log\left(\frac{(1-x)^3}{x^{2(p+1)}(x+\xi_j)(1+x\xi_j)}\right)
\nonumber \\
S_0^{(2)}(u)&=&\frac{1}{2}S_0^{(1)}(u)
\nonumber \\
&&-\frac{1}{2(2p+1)(-1+x)(x+\xi_j)^2(1+x\xi_j)^2}
\times (9 x^2 + 12 p x^2 + 6 p x^3 + 11 x \xi_j + 18 p x \xi_j
\nonumber \\
&&
+
 3 x^2 \xi_j + 18 p x^2 \xi_j
+ 21 x^3 \xi_j + 30 p x^3 \xi_j +
 x^4 \xi_j + 6 p x^4 \xi_j + 3 \xi_j^2 + 6 p \xi_j^2 + 2 x \xi_j^2
\nonumber \\
&&
+
 12 p x \xi_j^2 + 30 x^2 \xi_j^2 + 48 p x^2 \xi_j^2 + 6 x^3 \xi_j^2 +
 24 p x^3 \xi_j^2 + 13 x^4 \xi_j^2 + 18 p x^4 \xi_j^2 +
 11 x \xi_j^3
\nonumber \\
&&
+ 18 p x \xi_j^3 + 3 x^2 \xi_j^3
+ 18 p x^2 \xi_j^3 +
 21 x^3 \xi_j^3 + 30 p x^3 \xi_j^3 + x^4 \xi_j^3 + 6 p x^4 \xi_j^3 +
 9 x^2 \xi_j^4
\nonumber \\
&&
+ 12 p x^2 \xi_j^4 + 6 p x^3 \xi_j^4),
\nonumber \\
&&\vdots
\nonumber \\
S_0^{(k)}(u)&=&\frac{1}{k}S_0^{(1)}(u)+\frac{1}{k!}\frac{R_k(x)}{(x-1)^k(x+\xi_j)^{2(k-1)}(1+x\xi_j)^{2(k-1)}}.
\end{aligned}$$ Summing the terms $\frac{1}{k} S_0^{(1)}$, we find the following general form of the classical action: $$\begin{aligned}
S_0(u,t)&=&\frac{1}{2(2p+1)}\left(\log(-x^{2p+1})\right)^2-\log(-t)
 \log\left(\frac{(1-x)^3}{x^{2(p+1)}(x+\xi_j)(1+x\xi_j)}\right)+R(x,t).
\nonumber \\
&&
\end{aligned}$$ For $p=1$, this result agrees with ([\[S0ut-trefoil\]](#S0ut-trefoil){reference-type="ref" reference="S0ut-trefoil"}), which was derived from the refined quantum curve ([\[trefoil-Aqt\]](#trefoil-Aqt){reference-type="ref" reference="trefoil-Aqt"}). Therefore, this agreement proves the consistency of our conjectures in the case of the trefoil knot.

We also note that, because the values of the classical action $S_0(u,t)$ for $z_0=z_j$ and $z_0=z_{j+p}$ coincide, there are in total $p$ independent solutions. This indicates that the non-abelian branch of the character variety in the unrefined theory "splits" into $p$ independent branches in the refined / categorified theory. The same splitting and the same number of solutions can be seen more directly from the form of the refined $A$-polynomials for $(2,2p+1)$ torus knots.

### Asymptotic behavior in different grading conventions {#sec:saddle_DGR}

It is instructive to study the asymptotic behavior of the colored superpolynomial and its specialization [\[Pq2special\]](#Pq2special){reference-type="eqref" reference="Pq2special"} in different grading conventions. For example, another popular set of grading conventions is the one

where differentials $d_{N<0}$ have degree $(-2,2N,2N-1)$, see [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"}. One important lesson of this exercise will be the fact that the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"} has to be slightly modified depending on which grading conventions one chooses. Conceptually, and also as a simple way to remember which limit to take, one wants $$q^{\beta} t^{\gamma}  = e^{\hbar} \; \to \; 1 \,,
\label{gradreflimit}$$ where the exponents $\beta$ and $\gamma$ represent the degree[^3] of the colored differential, *cf.* [\[superright\]](#superright){reference-type="eqref" reference="superright"}, $$\deg (d_{\text{colored}}) \; = \; (0 , \beta, \gamma) \,.$$ Indeed, with the refined volume conjectures [\[VCquantref\]](#VCquantref){reference-type="eqref" reference="VCquantref"} and [\[VCparamref\]](#VCparamref){reference-type="eqref" reference="VCparamref"} we wish to probe the "large volume" asymptotics of the homological knot invariants $P_n (q,t)$, as $n$ goes to infinity. On the other hand, as we explained in section [\[sec:homological\]](#sec:homological){reference-type="ref" reference="sec:homological"}, the dependence of homological knot invariants on the "color" $R = S^{n-1}$ is controlled by the colored differentials which (in the basic case) change the value of $n$ by one unit, see *e.g.* [\[coloredPa\]](#coloredPa){reference-type="eqref" reference="coloredPa"}.

Therefore, in order to study the asymptotic behavior of the homological knot invariants under $n \to n+1$ for sufficiently large $n$, one needs to take a limit in which discrete values of $n$ are replaced by a continuous variable $x = e^u$ and different terms in the chain complex [\[VCsequence\]](#VCsequence){reference-type="eqref" reference="VCsequence"} are clumped together in a continuous distribution, described by $S_0 (u,t)$. Therefore, this continuous limit *is* precisely the limit in which $d_{\text{colored}}$ changes gradings by a tiny amount, *i.e.* the limit [\[gradreflimit\]](#gradreflimit){reference-type="eqref" reference="gradreflimit"}.

For example, in the grading conventions of [@DGR], the first colored differential listed in [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"} has $(a,q,t)$-degree $(0,2,2)$. Therefore, the right limit to take in this case is the limit [\[gradreflimit\]](#gradreflimit){reference-type="eqref" reference="gradreflimit"} with $\beta = 2$ and $\gamma=2$ or, more precisely, $$q^2 t^2 = e^{\hbar} \to 1 \,, \qquad t = \text{fixed} \,, \qquad x \equiv e^u = e^{n \hbar} = \text{fixed} \,.
\label{gradlimit}$$

In order to make this a little bit more concrete and to understand the issue better, let us illustrate how it all works in the large class of examples associated with $(2,2p+1)$ torus knots. We already computed the colored superpolynomial ([\[Symmetric_DGR_refined\]](#Symmetric_DGR_refined){reference-type="ref" reference="Symmetric_DGR_refined"}) for these knots in the grading conventions of [@DGR], and now to study its asymptotic behavior we will need a couple of useful identities. First, applying the Euler-Maclaurin formula [@Kirillov]: $$\begin{aligned}
\sum_{m=M}^Nf(m)&=&\int_M^Nf(t)dt+\frac{1}{2}(f(N)+f(M))
+\sum_{k=1}^{n}\frac{B_{2k}}{(2k)!}\left\{
f^{(2k-1)}(N)
\right\}
\nonumber \\
&&-\int_M^N\frac{\overline{B}_{2n}(t)}{(2n)!}f^{(2n)}(t)dt.
\end{aligned}$$ to the function $f(m)=\log\left(1-X(q^2t^2)^m\right)$, we find $$\begin{aligned}
\log(X;q^2t^2)_{\infty}=
\frac{1}{\hbar+\epsilon}{\rm Li}_2(X)+\frac{1}{2}\log(1-X)+\sum_{k=1}^{\infty}
\frac{B_{2k}}{(2k)!}\frac{U_{2k-1}(X)}{(1-X)^{2k-1}}(\hbar+\epsilon)^{2k-1}
\end{aligned}$$ where we temporarily introduced $\epsilon:=\log t$. In particular for $X=e^{\frac{s}{\hbar}}$, one finds the following expansion: $$\begin{aligned}
\log(X;q^2t^2)_{\infty} \; = \; -\frac{s}{2}\hbar^2-i\pi s\hbar+\frac{\pi^2}{3} +{\cal O}(e^{-\hbar s}) \,,
\end{aligned}$$ which we can apply to our result for the superpolynomial ([\[Symmetric_DGR_refined\]](#Symmetric_DGR_refined){reference-type="ref" reference="Symmetric_DGR_refined"}) or, to be more precise, to its specialization [\[Pq2special123\]](#Pq2special123){reference-type="eqref" reference="Pq2special123"} at $a = q^2$.

First, let us see what would happen if, instead of the correct limit [\[gradlimit\]](#gradlimit){reference-type="eqref" reference="gradlimit"} that comes from the gradings of colored differentials, we naively used the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"} (suitable for the homological invariants in the grading conventions of [@GS], where $\deg (d_{\text{colored}}) = (0,1,0)$). We would find that the desired specialization of the colored superpolynomial ([\[Symmetric_DGR_refined\]](#Symmetric_DGR_refined){reference-type="ref" reference="Symmetric_DGR_refined"}) can be approximated by an integral, much like in [\[Pn-saddle\]](#Pn-saddle){reference-type="eqref" reference="Pn-saddle"}, $${\cal P}^{S^{n-1}}_{\text{DGR}}(T^{2,2p+1};a=q^2,q,t)
\; \sim \; \int dz\; e^{\frac{1}{\hbar^2}V_{(2,2p+1)}^{\text{DGR}}(z,x;t)+{\cal O}(\hbar^{-1})} \,,$$ with a very simple potential function $V_{T^{2,2p+1}}^{\text{DGR}} (z,x;t)$: $$V_{(2,2p+1)}^{\text{DGR}}(z,x;t)
\; = \; (2p+1)\epsilon\left((\log x)^2-(\log z)^2\right) \,.$$ Clearly, the critical point of this potential is $z_0 = 1$ and, therefore, the colored superpolynomial in this grading and in the limit $\hbar\to 0$ behaves as $$\begin{aligned}
{\cal P}^{S^{n-1}}_{\text{DGR}}(T^{2,2p+1};a=q^2,q,t) \; \sim \; e^{\frac{1}{\hbar^2}V_{(2,2p+1)}^{\text{DGR}}(z_0,x;t)} \,.
\end{aligned}$$ This behavior is way too simple to learn anything non-trivial about the "large color" behavior of the colored superpolynomial and is not even in the expected form ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a), which is yet another signal that one needs to be very careful passing from one set of grading conventions to another.

Now, let us consider the asymptotic behavior of the same object in the correct limit [\[gradlimit\]](#gradlimit){reference-type="eqref" reference="gradlimit"}. Again, as in [\[Pn-saddle\]](#Pn-saddle){reference-type="eqref" reference="Pn-saddle"}, we can write $${\cal P}_{\text{DGR}}^{S^{n-1}}(T^{2,2p+1};a=q^2,q;t)
\; \sim \; \int dz\; e^{\frac{1}{\hbar} \biggl(V_{(2,2p+1)}^{\text{DGR}}(z,x,t) +{\cal O}(\hbar)\biggr)} \,,$$ with $$\begin{aligned}
&&V_{(2,2p+1)}^{\text{DGR}}(z,x;t)=
{\rm Li}_2(-t^{-1}) - {\rm Li}_2(x) + {\rm Li}_2(-xt^{-3}) +
{\rm Li}_2(xz^{-1}) - {\rm Li}_2(-xt^{-1}z^{-1})
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad\;
+ {\rm Li}_2(z) - {\rm Li}_2(zt^{-2}) - {\rm Li}_2(-x zt^{-3})
+ {\rm Li}_2(x zt^{-2})-\frac{\pi^2}{6}
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad\;
+  (2p+1)\Bigl[ (\log (-t^{-2}))\cdot(\log x) +
    \frac{(\log x)^2 - (\log z)^2}{2}-\pi i\log z\Bigr]
\nonumber \\
&& \quad\quad\quad\quad\quad\quad\quad\;
+(\log t)\cdot  (\log z) \,.
\end{aligned}$$ From this potential function, the saddle point condition ([\[saddle_point\]](#saddle_point){reference-type="ref" reference="saddle_point"}) and the first line of ([\[braid_saddle2\]](#braid_saddle2){reference-type="ref" reference="braid_saddle2"}) we find the equations for the saddle point that dominates the above integral:

$$\begin{aligned}
&&1=\frac{ (t^2 - z) z^{-1 - 2 p} (-x + z) (t^3 + x z)}{t (-1 + z) (x + t z) (t^2 - x z)},
\nonumber \\
&&y=-\frac{ t^{-1 - 4 p} (-1 + x) x^{1 + 2 p} (x + t z) (t^3 + x z)}
{(t^3 + x) (x - z) (t^2 - x z)}.
\label{Saddle_DGR2}
\end{aligned}$$ Eliminating the variable $z$, we find the refined A-polynomial $A^{\text{DGR}}_{T^{2,2p+1}} (x,y;t)$. For $p=1$, the refined A-polynomial will be described in Appendix [\[sec:AppendixB\]](#sec:AppendixB){reference-type="ref" reference="sec:AppendixB"}. For $t=-1$ we find the same behavior as in the analysis of ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}) and ([\[braid_saddle2\]](#braid_saddle2){reference-type="ref" reference="braid_saddle2"}): the first equation above only specifies the value $z_0^{2p+1}=1$, and the second one reduces to ordinary unrefined $A$-polynomial equation for $T^{2,2p+1}$ knot $y+x^{2p+1}=0$.

The algebraic equations ([\[Saddle_DGR2\]](#Saddle_DGR2){reference-type="ref" reference="Saddle_DGR2"}) can be easily solved around $t=-1$: $$\begin{aligned}
z_j&=&\xi_j+\frac{\xi_j(1+\xi_j)(-2 x + \xi_j + 2 x \xi_j + x^2 \xi_j - 2 x \xi_j^2)}{(1 + 2 p) (x - \xi_j) (-1 + \xi_j) (-1 + x \xi_j)}(1+t)
\nonumber \\
&&+{\cal O}((1+t)^2),
\end{aligned}$$ with $\xi_j=e^{\frac{2\pi ij}{2p+1}}$. Plugging this solution into the second equation of ([\[Saddle_DGR2\]](#Saddle_DGR2){reference-type="ref" reference="Saddle_DGR2"}), we find the approximate solution for $y$ (as a function of $x$ and $t$): $$\begin{aligned}
y&=&-x^{2p+1}\Bigl[
1+(1+t)
(-3 x - 4 p x + 4 p x^2 + 2 \xi_j + 4 p \xi_j + x \xi_j -
 4 p x \xi_j + 4 x^2 \xi_j + 4 p x^2 \xi_j
\nonumber \\
&&\quad\quad\quad\quad\quad\quad\quad
- x^3 \xi_j -
 4 p x^3 \xi_j - 3 x \xi_j^2 - 4 p x \xi_j^2 + 4 p x^2 \xi_j^2)


/(-1 + x) (x - \xi_j) (-1 + x \xi_j)
\nonumber \\
&&\quad\quad\quad\quad
+{\cal O}(1+t)^2\Bigr].
\end{aligned}$$ From ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}), one can also find the refined classical action $S_0(u,t)$: $$\begin{aligned}
S_0(u,t)&=&S_0(u)+\sum_{a=1}^{\infty}(1+t)^aS_0^{(a)}(u),
\nonumber \\
S_0(u)&=&\frac{1}{2(2p+1)}\log(-x^{2p+1})^2,
\nonumber \\
S_0^{(1)}(u)&=&\log\frac{x^{4p+2}(x-\xi_j)(1-x\xi_j)}{(1-x)^3},
\nonumber \\
S_0^{(2)}(u)&=&\frac{1}{2}S_0^{(1)}
\nonumber \\
&&
+\frac{1}{2(2p+1)(-1 + x) (x - \xi_j)^2 (-1 + x \xi_j)^2}
\nonumber \\
&&\times\bigl(
-7 x^2 - 8 p x^2 - 2 x^3 - 10 p x^3 + 9 x \xi_j + 14 p x \xi_j +
 5 x^2 \xi_j + 22 p x^2 \xi_j + 19 x^3 \xi_j
\nonumber \\
&&
+ 26 p x^3 \xi_j +
 3 x^4 \xi_j + 10 p x^4 \xi_j - 3 \xi_j^2 - 6 p \xi_j^2 -
 2 x \xi_j^2 - 12 p x \xi_j^2 - 30 x^2 \xi_j^2 - 48 p x^2 \xi_j^2
\nonumber \\
&&
-
 6 x^3 \xi_j^2 - 24 p x^3 \xi_j^2 - 13 x^4 \xi_j^2 -
 18 p x^4 \xi_j^2 + 13 x \xi_j^3 + 22 p x \xi_j^3 + x^2 \xi_j^3 +
 14 p x^2 \xi_j^3
\nonumber \\
&&
+ 23 x^3 \xi_j^3 + 34 p x^3 \xi_j^3 - x^4 \xi_j^3 +
 2 p x^4 \xi_j^3 - 11 x^2 \xi_j^4 - 16 p x^2 \xi_j^4 +
 2 x^3 \xi_j^4 - 2 p x^3 \xi_j^4
\bigr),
\nonumber
\\
&&
\end{aligned}$$ and the general form of the classical action: $$\begin{aligned}
S_0(u,t)&=&\frac{1}{2(2p+1)}\left(\log(-x^{2p+1})\right)^2-\log(-t)
 \log\left(\frac{x^{4p+2}(x-\xi_j)(1-x\xi_j)}{(1-x)^3}\right)+R(x,t).
\nonumber \\
&&
\end{aligned}$$

[^1]: To be more precise, there can be subtleties in the treatments of the analytic continuation [@Wit-anal], and the convergence and non-perturbative contributions like ${\cal O}(e^{\hbar})$ of the contour integrals should be discussed more carefully. Luckily, none of these subtleties affect our derivation of the refined $A$-polynomial in the asymptotic limit $\hbar\to 0$ around the exponential growth point. For this reason, we will only discuss the saddle point approximation in a sense of the *optimistic limit*, relegating a more detailed analysis *a la* [@Kashaev_Tirkkonen; @Murakami_torus; @Hikami_Murakami1; @Hikami_Murakami2] to future work.

[^2]: There are also the other solutions: $$\begin{aligned}
    z_0=\pm \frac{1}{t}.
    \end{aligned}$$ Plugging these solutions into ([\[braid_saddle1\]](#braid_saddle1){reference-type="ref" reference="braid_saddle1"}), we find $$\begin{aligned}
    y(x,t)=\frac{t^{2 + 2 p} (-1 + x) x^{1 + 2 p} (\pm 1 + t^2 x)^2}{(\mp 1 + t x)^2 (1 + t^3 x)}.
    \end{aligned}$$ We assume that these factors correspond to the solutions $z_0$ which are not the saddle points but the critical points of the potential $V_{(2,2p+1)}(z,x;t)$. To treat this point in more detail, we need to specify the integration path more carefully. Since for $p=1$ this solution is not included in ([\[deformed_A-poly_trefoil\]](#deformed_A-poly_trefoil){reference-type="ref" reference="deformed_A-poly_trefoil"}), we conclude that these solutions do not describe the saddle points relevant to us.

[^3]: For simplicity, here we assume that the $a$-degree of $d_{\text{colored}}$ is equal to zero, as for the first set of colored differentials in [\[gradingtabl\]](#gradingtabl){reference-type="eqref" reference="gradingtabl"}.
