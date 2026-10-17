---
doc_id: arxiv-2303.08330v2
doc_title: "A Cable Knot and BPS-Series II"
section_id: sec-003-example-2
section_title: "Example 2"
section_number: null
pages: 5-7
source_pdf: 2303.08330v2.pdf
source_sha256: 94981fa0a792b3fa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.989
---
The next simplest case is $K=C_{(11,2)}(\bm{4_1})$.

::: prop
The $\hbar$ expansion of the $J_{K,n}(q)$ is given by $$\begin{aligned}     
    J_{K,n}(e^{\hbar}) & = 1 + \left(11 - 11 n^2 \right)\hbar^2 + \left(-88 + 88 n^2 \right)\hbar^3 + \left(\frac{11891}{12} - 1137 n^2 + \frac{1753}{12} n^4 \right)\hbar^4\\
    & + \left(- 12826 + \frac{47036}{3} n^2 - \frac{8558}{3} n^4 \right)\hbar^5 + \left(\frac{69672971}{360} - \frac{991683}{4} n^2 + \frac{224545}{4} n^4 - \frac{630551}{360} n^6 \right)\hbar^6 + \cdots
\end{aligned}$$
:::

At each $\hbar$ order, the degree of the polynomial in $n$ is at most the order of $\hbar$, which is an equivalent characterization of the MMR expansion of the colored Jones polynomial of a knot.

The cabling formula for the Alexander polynomial of a knot $K$ is [@Hedden] $$\Delta_{C_{(p,q)}(K)}(t)= \Delta_K (t^p) \Delta_{T_{(p,q)}}(t), \quad 2 \leq p < |q| \quad \text{gcd}(p,q)=1,$$ where $\Delta(t)$ is the symmetrized Alexander polynomial and $T_{(p,q)}$ is the $(p,q)$ torus knot. Note that our convention for the parameters of the torus knot are switched (i.e. $p\equiv 2, q\equiv r$).

::: lemma
The Alexander polynomial of $C_{(11,2)}(\bm{4_1})$ is as follows. $$\begin{aligned}     
\Delta_{C_{(11,2)}{(\bm{4_1})}}(x) & = \Delta_{\bm{4_1}} (x^2) \Delta_{T_{(2,11)}}(x)\\
& = -1-\frac{1}{x^7}+\frac{1}{x^6}+\frac{2}{x^5}-\frac{2}{x^4}+\frac{1}{x^3}-\frac{1}{x^2}+\frac{1}{x}+x-x^2+x^3-2 x^4+2 x^5+x^6-x^7.
\end{aligned}$$
:::

From this Alexander polynomial its symmetric expansion about $x=0$ (in $x$) and $x=\infty$ (in $1/x$) can be computed.

::: prop
The symmetric expansion of the inverse of the Alexander polynomial of $K$ in the limit of $\hbar \rightarrow 0$ is given by $$\begin{aligned}
\lim_{q \rightarrow 1} 2F_{K}(x,q) &  =  2\, \text{s.e.} \left(\frac{x^{1/2}-x^{-1/2}}{\Delta_{K}(x)} \right)\\
 & =  x^{13/2}-\left(\frac{1}{x}\right)^{13/2}+2 x^{17/2}-2 \left(\frac{1}{x}\right)^{17/2}+5x^{21/2}-5 \left(\frac{1}{x}\right)^{21/2}+13 x^{25/2}-13 \left(\frac{1}{x}\right)^{25/2}\\
 & +34   x^{29/2}-34 \left(\frac{1}{x}\right)^{29/2}+89 x^{33/2}-89\left(\frac{1}{x}\right)^{33/2}-x^{35/2}+\left(\frac{1}{x}\right)^{35/2}+233 x^{37/2}-233\left(\frac{1}{x}\right)^{37/2}\\
 & -2 x^{39/2}+2 \left(\frac{1}{x}\right)^{39/2}+610 x^{41/2}-610\left(\frac{1}{x}\right)^{41/2}-5 x^{43/2}+5 \left(\frac{1}{x}\right)^{43/2} + \cdots \in \mathbb{Z}\left[\left[x^{\pm 1/2} \right]\right]
\end{aligned}$$ where denotes the symmetric expansion in $x$ about $x=0$ and $1/x$ about $x=\infty$.
:::

The coefficients in the expansions are integers and the Alexander polynomial is monic, which is a necessary condition for $f_m(q)$'s in (1) to be polynomials. Furthermore, the coefficients of $x^{35/2}, x^{39/2}, x^{43/2}$ etc are negative, which are reflected as negative coefficient elements in the initial data below (cf.Proposition 3.5).

From (5) we find the recursion relation for $f_{m}$.

::: theorem
The recursion relation for $f_{m}(q) \in \mathbb{Z}[q^{\pm 1}]$ of $F_K (x,q)$ is given by $$\begin{aligned}
f_{v+102}\,(q) & = \frac{-1}{q^{\frac{115+v}{2}} \left(1-q^{\frac{89+v}{2}}\right)} \Big[ t_2 f_{98+v}  + t_4 f_{94+v}  + t_6 f_{90+v} + t_8 f_{86+v}  + t_{10} f_{82+v} +t_{11} f_{80+v} \\
& + t_{12} f_{78+v}   + t_{13} f_{76+v}  + t_{14} f_{74+v} + t_{15} f_{72+v}  + t_{16} f_{70+v} +  t_{17} f_{68+v} + t_{18} f_{66+v} \\
& +t_{19} f_{64+v}  + t_{20} f_{62+v}  +  t_{21} f_{60+v} +  t_{22} f_{58+v} +  t_{23} f_{56+v} + t_{24} f_{54+v}  + t_{25} f_{52+v} \\
&  + t_{26} f_{50+v}  + t_{27} f_{48+v}  + t_{28} f_{46+v}  + t_{29} f_{44+v}  + t_{30}  f_{42+v}+  t_{31} f_{40+v} + t_{32} f_{38+v}\\
& + t_{33}  f_{36+v} + t_{34} f_{34+v}  +  t_{35} f_{32+v} + t_{36} f_{30+v}  + t_{37} f_{28+v}  + t_{38} f_{26+v}  + t_{39} f_{24+v} \\
&  +  t_{40} f_{22+v} + t_{41} f_{20+v}  + t_{43} f_{16+v}  +  t_{45} f_{12+v} +  t_{47} f_{8+v} +  t_{49} f_{4+v} + t_{51} f_v \vphantom{1} \Big] 
\end{aligned}$$ where $t_{s}=t_{s}(q,q^v)$ are $\mathbb{Z}$-Laurent polynomials in $q$ and $q^v$.
:::

::: prop
The initial data for (6) consists of $\left\{f_{j} (q) \in \mathbb{Z}[q^{\pm 1}] | j=1,\cdots ,101 \right\}$. All the nonzero elements are the following. $$\begin{aligned}
f^{+}_{13} (q) & = 2\,  h_1 (q)\, q^6 \\
f^{+}_{17} (q) & = 2\, h_3 (q)\, q^{7} \\
f^{+}_{21} (q) & = 2\, h_5 (q)\, q^{8}\\
&\vdots\\
f^{+}_{57} (q) & = 2\, \left(h_{23} (q)\, q^{17 } + h_1 (q) \, q^{41}  \right)\\
f^{+}_{61} (q) & = 2\, \left(h_{ 25 } (q)\, q^{18} + h_3 (q) \, q^{46 }  \right)\\ 
f^{+}_{65} (q) & = 2\, \left(h_{27 } (q)\, q^{19} + h_5 (q) \, q^{51 }  \right)\\
&\vdots\\
f^{+}_{101} (q) & = 2\, \left(h_{ 45} (q)\, q^{28} + h_{23 } (q) \, q^{96 }  + h_1 (q) \, q^{120 }  \right)\\
&\vdots\\
f^{-}_{35} (q) & = -2\,  h_1 (q)\, q^{18} \\
f^{-}_{39} (q) & = -2\, h_3 (q)\, q^{21}  \\
f^{-}_{43} (q) & = -2\, h_5 (q)\, q^{24}\\
&\vdots\\
f^{-}_{79} (q) & = -2 \left(h_{23} \, q^{51} + h_1 \, q^{75} \right)\\
f^{-}_{83} (q) & = -2 \left(h_{25} \, q^{54} + h_3 (q) \, q^{82} \right)\\
&\vdots\\
f^{-}_{99} (q) & = -2 \left(h_{33} \, q^{66} + h_{11} (q) \, q^{110} \right)\\
\end{aligned}$$
:::

After substituting them into (6), we obtain $f_{103} (q)$ and $f_{105} (q)$ as Laurent polynomials with integer coefficients, which is non-trivial because of the denominator $(1-q^{(89+v)/2})$ in (6). Recasting them in terms of $h_s (q)$, we get $$\begin{aligned}
f^{-}_{103} (q) & = -2 \left(h_{35}(q) \, q^{69} + h_{13} (q) \, q^{117} \right)\\
f^{+}_{105} (q) & = 2\, \left(h_{ 47} (q)\, q^{29} + h_{25 } (q) \, q^{101}  + h_3 (q) \, q^{129}  \right)
\end{aligned}$$ They agree with the predictions from Conjecture 2.4 by extrapolating it beyond $f_{101}(q)$. As another check, $\hbar$ expansions of (7) and (8) match with that of $F_{C_{(11,2)}(\bm{4_1})}(x,e^{\hbar})$. They can in turn be used to confirm that subsequent $f_m (q)$'s obtained from Conjecture 2.4 agree with that of (6). $$\begin{aligned}
f^{-}_{107} (q) & = -2 \left(h_{37}(q) \, q^{72} + h_{15} (q) \, q^{124} \right)\\
f^{+}_{109} (q) & = 2\, \left(h_{ 49} (q)\, q^{30} + h_{27 } (q) \, q^{106}  + h_5 (q) \, q^{138}  \right)\\
\end{aligned}$$ Furthermore, their $\hbar$ expansions coincide with that of $F_{C_{(13,2)}(\bm{4_1})}$.

**Remark** When $h_{23}(q)$ appears in $f^{\pm}_b$ for any $b$, $h_1(q)$ is added.
