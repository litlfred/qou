---
doc_id: arxiv-2303.08330v2
doc_title: "A Cable Knot and BPS-Series II"
section_id: sec-005-example-3
section_title: "Example 3"
section_number: null
pages: 8-12
source_pdf: 2303.08330v2.pdf
source_sha256: 94981fa0a792b3fa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.805
latex_coverage_ratio: 0.992
---
We next consider $K=C_{(13,2)}(\bm{4_1})$.

::: prop
The $\hbar$ expansion of the $J_{K,n}(q)$ is given by $$\begin{aligned}     
    J_{K,n}(e^{\hbar}) & = 1 + \left(17 - 17 n^2 \right)\hbar^2 + \left(-156 + 156 n^2 \right)\hbar^3 + \left(\frac{24749}{12} - 2365 n^2 + \frac{3631}{12} n^4 \right)\hbar^4\\
    & + \left(- 31629 + 38662 n^2 - 7033 n^4 \right)\hbar^5 + \Big(  \frac{203413517}{360} - \frac{8687953}{12} n^2 + \frac{1969367}{12} n^4 \\
    & - \frac{1855937}{360} n^6 \Big) \hbar^6 + \cdots
\end{aligned}$$
:::

This confirms that the MMR condition is satisfied by $K$.

::: lemma
The Alexander polynomial of $C_{(13,2)}(\bm{4_1})$ is given by $$\begin{aligned}     
\Delta_{C_{(13,2)}{(\bm{4_1})}}(x) & = \Delta_{\bm{4_1}} (x^2) \Delta_{T_{(2,13)}}(x)\\
& = -t^8-\frac{1}{t^8}+t^7+\frac{1}{t^7}+2 t^6+\frac{2}{t^6}-2t^5-\frac{2}{t^5}+t^4+\frac{1}{t^4}-t^3-\frac{1}{t^3}+t^2+\frac{1}{t^2}-t-\frac{1}{t}+1.
\end{aligned}$$
:::

::: prop
The symmetric expansion of the inverse of the Alexander polynomial of $K$ in the limit of $\hbar \rightarrow 0$ is given by $$\begin{aligned}
\lim_{q \rightarrow 1} 2F_{K}(x,q) &  =  2\, \text{s.e.} \left(\frac{x^{1/2}-x^{-1/2}}{\Delta_{K}(x)} \right)\\
 & = x^{15/2}-\left(\frac{1}{x}\right)^{15/2}+2 x^{19/2}-2 \left(\frac{1}{x}\right)^{19/2}+5 x^{23/2}-5\left(\frac{1}{x}\right)^{23/2}+13 x^{27/2}-13 \left(\frac{1}{x}\right)^{27/2}\\
 & +34 x^{31/2}-34\left(\frac{1}{x}\right)^{31/2}+89 x^{35/2}-89 \left(\frac{1}{x}\right)^{35/2}+233 x^{39/2}-233\left(\frac{1}{x}\right)^{39/2}-x^{41/2}+\left(\frac{1}{x}\right)^{41/2}\\
 & +610 x^{43/2}-610\left(\frac{1}{x}\right)^{43/2}-2 x^{45/2}+2 \left(\frac{1}{x}\right)^{45/2} + \cdots \in \mathbb{Z}\left[\left[x^{\pm 1/2} \right]\right]
\end{aligned}$$
:::

The coefficients of $x^{41/2}$ and $x^{45/2}$ etc being negative is consistent with the negative coefficient elements in the initial data below (cf. Proposition 3.10).

::: theorem
The recursion relation for $f_{m}(q) \in \mathbb{Z}[q^{\pm 1}]$ of the above $F_K (x,q)$ is given by $$\begin{aligned}
f_{v+106}\,(q) & = \frac{-1}{q^{\frac{121+v}{2}} \left(1-q^{\frac{91+v}{2}}\right)} \Big[ t_2 f_{v+102}+t_4 f_{v+98}+t_6 f_{v+94}+t_8 f_{v+90}+t_{10} f_{v+86}+ t_{12} f_{v+82}\\
& +t_{13} f_{v+80}+t_{14} f_{v+78}+t_{15} f_{v+76}+t_{16} f_{v+74}+t_{17} f_{v+72}+t_{18} f_{v+70}+t_{19} f_{v+68}\\
& +t_{20} f_{v+66}+t_{21} f_{v+64}+t_{22} f_{v+62}+t_{23} f_{v+60}+t_{24} f_{v+58}+t_{25}  f_{v+56}+t_{26} f_{v+54}\\
& +t_{27} f_{v+52}+t_{28} f_{v+50}+t_{29} f_{v+48}+t_{30} f_{v+46}+t_{31} f_{v+44}+t_{32} f_{v+42}+t_{33} f_{v+40} \\
& +t_{34} f_{v+38}+t_{35} f_{v+36}+t_{36} f_{v+34}+t_{37} f_{v+32}+t_{38} f_{v+30}+t_{39} f_{v+28}+t_{40} f_{v+26}\\
& +t_{41} f_{v+24}+t_{43} f_{v+20}+t_{45}f_{v+16}+t_{47} f_{v+12}+t_{49} f_{v+8}+t_{51} f_{v+4}+t_{53} f_v \vphantom{1} \Big] 
\end{aligned}$$ where $t_{s}=t_{s}(q,q^v)$ are $\mathbb{Z}$-Laurent polynomials in $q$ and $q^v$.
:::

::: prop
The initial data for (9) consists of $\left\{f_{j} (q) \in \mathbb{Z}[q^{\pm 1}] | j=1,\cdots ,105 \right\}$. All the nonzero elements of the set are the following. $$\begin{aligned}
f^{+}_{15} (q) & = 2\,  h_1 (q)\, q^7 \\
f^{+}_{19} (q) & = 2\, h_3 (q)\, q^8  \\
f^{+}_{23} (q) & = 2\, h_5 (q)\, q^9\\
&\vdots\\
f^{+}_{67} (q) & = 2\, \left(h_{27} (q)\, q^{20 } + h_1 (q) \, q^{48}  \right)\\
f^{+}_{71} (q) & = 2\, \left(h_{ 29 } (q)\, q^{21} + h_3 (q) \, q^{53}  \right)\\ 
&\vdots\\
f^{-}_{41} (q) & = -2\,  h_1 (q)\, q^{21} \\
f^{-}_{45} (q) & = -2\, h_3 (q)\, q^{24}  \\
f^{-}_{49} (q) & = -2\, h_5 (q)\, q^{27}\\
&\vdots\\
f^{-}_{93} (q) & = -2 \left(h_{27}(q) \, q^{60} + h_1 \, q^{88} \right)\\
f^{-}_{97} (q) & = -2 \left(h_{29}(q) \, q^{63} + h_3 (q) \, q^{95} \right)\\
&\vdots\\
f^{-}_{105} (q) & = -2 \left(h_{33}(q) \, q^{69} + h_{7} (q) \, q^{109} \right)\\
\end{aligned}$$
:::

After substituting them into (9), we indeed obtain $f_{107} (q)$ and $f_{109} (q)$ as Laurent polynomials with $\mathbb{Z}$-coefficients. They can be recast in terms of $h_s (q)$: $$\begin{aligned}
f^{+}_{107} (q) & = 2 \left(h_{47}(q) \, q^{30} + h_{21} (q) \, q^{98} \right)\\
f^{-}_{109} (q) & = -2\, \left(h_{ 35} (q)\, q^{72} + h_{9 } (q) \, q^{116}   \right)
\end{aligned}$$ The predictions from Conjecture 2.4 coincide with the above. Furthermore, $\hbar$ expansions of (10) and (11) agree with that of $F_{C_{(13,2)}(\bm{4_1})}(x,e^{\hbar})$. These can in turn be used to confirm that subsequent $f_m (q)$'s obtained from (9) again agree with that of Conjecture 2.4. $$\begin{aligned}
f^{+}_{111} (q) & = 2 \left(h_{49}(q) \, q^{31} + h_{23} (q) \, q^{103} \right)\\
f^{-}_{113} (q) & = -2\, \left(h_{ 37} (q)\, q^{75} + h_{11 } (q) \, q^{123}   \right)\\
\end{aligned}$$ Their $\hbar$ expansions of the above results match with that of $F_{C_{(13,2)}(\bm{4_1})}$ as well.

**Remark** When $h_{27}(q)$ appears in $f^{\pm}_b$ for any $b$, $h_1(q)$ is added.

# $(3w+1,3)$-cables  $(w>3)$

The quantum (or noncommutative) A-polynomial of a class of cable knot $C_{(r,3)}(\bm{4_1})$ is qualitatively different from that of the $(2w+1,2)$-cabling in Section 2. It is given by [@Ru] $$\hat{A}_{K} (t,M,L)=(L-1)B(t,M)^{-1}Q(t,M,L) \left(t^{6s} M^{3r} L^2 - t^{-6r}M^{-3r}, \right)\quad gcd(r,3)=1, \quad |r| > 12.$$ The definitions of $Q(t,M,L)$ and $B(t,M)$ are written in Appendix A. Using (3) together with (12) yields $$\begin{split}
\phantom{A} & \phantom{=} c_0 (x,q)F_K(x,q) + c_1 (x,q)F_K(xq,q)+ c_2 (x,q)F_K(xq^2,q) + c_3 (x,q) F_K(xq^3,q)\\
 & + c_4 (x,q) F_K(xq^4,q) + c_5 (x,q) F_K(xq^5,q)=0,
\end{split}$$ where $c_0  ,c_1 ,c_2 , c_3 , c_4 , c_5$ are rational functions. We state the nonzero initial data needed for (13).

::: conjecture
For a $(3w+1,3)$-cabling of $\bm{4_1}\, (w > 3)$ in $\mathbb{Z}HS^3$, nonzero initial data $\left\{f_m (q) \in \mathbb{Z}[q^{\pm 1}] \right\}= \left\{f^{+}_i (q)  |\, \text{all coefficients are positive} \right\}\bigsqcup \left\{f^{-}_j (q) |\, \text{all coefficients are negative}  \right\}$ for (13) are determined by the coefficient functions $\left\{h_s (q) \right\}$ of $F_{\bm{4_1}}(x,q)$ as follows. $$\begin{aligned}
f^{+}_{6w+5} (q) & = 2\,  h_1 (q)\, q^n \qquad ( h_1 (q)=1)\\
f^{+}_{6w+11} (q) & = 2\, h_3 (q)\, q^{n+2}  \qquad ( h_3 (q)=2)\\
f^{+}_{6w+17} (q) & = 2\, h_5 (q)\, q^{n+4}\\
&\vdots\\
f^{+}_{24w+11} (q) & = 2\, \left(h_{6w+3 } (q)\, q^{n+ 6 w + 2  } + h_1 (q) \, q^{n+ 6 w + 2 +  \Delta}  \right)\\
f^{+}_{24w+17} (q) & = 2\, \left(h_{ 6w+5 } (q)\, q^{n + 6 w + 4 } + h_3 (q) \, q^{n + 6 w + 10 + \Delta }  \right)\\ 
f^{+}_{24w+23} (q) & = 2\, \left(h_{ 6w+7 } (q)\, q^{n+  6 w + 6 } + h_5 (q) \, q^{n + 6 w + 18  + \Delta }  \right)\\
&\vdots\\
f^{+}_{42w+17} (q) & = 2\, \left(h_{ 12w+5  } (q)\, q^{n+  12w + 4 } + h_{6w+3 } (q) \, q^{n + 30w +10 +  \Delta }  + h_1 (q) \, q^{n +  30w +10 + 2\Delta }  \right)\\
f^{+}_{42w+23} (q) & = 2\, \left(h_{12w+7} (q)\, q^{n+12w +6 } + h_{6w+5} (q) \, q^{n + 30w +18 +  \Delta }  + h_3 (q)\, q^{n + 30w +24 + 2\Delta }  \right)\\
&\vdots\\
f^{+}_{60w+23} (q) & = 2\, \left(h_{ 18w+ 7} (q)\, q^{n+ 18w + 6} + h_{12w+5 } (q) \, q^{n + 54w +18  + \Delta }  + h_{6w+3} (q) \, q^{n + 72w+24  + 2\Delta } \notag\right. \\
& \notag\left. + h_{1} (q) \, q^{n + 72w+24  + 3\Delta } \right)\\
f^{+}_{60w+29} (q) & = 2\, \left(h_{18w+9} (q)\, q^{n+12w +8 } + h_{12w+7} (q) \, q^{n + 54w +26 +  \Delta } + h_{6w+5} (q) \, q^{n + 72w + 38  + 2\Delta }\notag\right.\\
& \notag\left. + h_3 (q)\, q^{n + 72w + 44 + 3\Delta }  \phantom{1} \right)\\
&\vdots\\
f^{+}_{78w+29} (q) & = 2\, \left(h_{24w+9} (q)\, q^{n+ 24w + 8} + h_{18w+7 } (q) \, q^{n + 78w + 26 + \Delta }  + h_{12w+5} (q) \, q^{n + 114w + 38 + 2\Delta} \notag\right. \\
& \notag\left. + h_{6w+3} (q) \, q^{n + 132w + 44 + 3\Delta } + h_{1} (q) \, q^{n + 132w + 44 + 4\Delta }  \phantom{1}\right)\\
f^{+}_{78w+35} (q) & = 2\, \left(h_{24w+11} (q)\, q^{n+ 24w + 10} + h_{18w+9 } (q) \, q^{n + 78w + 34 + \Delta }  + h_{12w+7} (q) \, q^{n + 114w + 52 + 2\Delta } \notag\right.\\
& \notag\left. + h_{6w+5} (q) \, q^{n + 132w + 64 + 3\Delta } + h_{3} (q) \, q^{n + 132w + 70 + 4\Delta }  \phantom{1}\right)\\
&\vdots\\
f^{-}_{12w+7} (q) & = -2\,  h_1 (q)\, q^{2n} \\
f^{-}_{12w+13} (q) & = -2\, h_3 (q)\, q^{2n+4}  \\
f^{-}_{12w+19} (q) & = -2\, h_5 (q)\, q^{2n+8}\\
&\vdots\\
f^{-}_{30w+13} (q) & = -2 \left(h_{6w+3}(q) \, q^{2n+12 w + 4  } + h_1 (q) \, q^{2n+ 12 w + 4   + \Delta} \right)\\
f^{-}_{30w+19} (q) & = -2 \left(h_{6w+5}(q) \, q^{2n+12 w + 8 } + h_3 (q) \, q^{2n+ 12 w + 14  + \Delta} \right)\\
&\vdots\\
f^{-}_{48w+19} (q) & = -2\, \left(h_{12w+5} (q)\, q^{2n+ 24w +8 } + h_{6w+3 } (q) \, q^{2n + 42w + 14 +  \Delta }  + h_1 (q) \, q^{2n + 42w + 14 + 2\Delta }  \right)\\
f^{-}_{48w+25} (q) & = -2\, \left(h_{12w+7} (q)\, q^{2n+ 24w +12 } + h_{6w+5 } (q) \, q^{2n + 42w + 24 +  \Delta }  + h_3 (q) \, q^{2n +  42w +30 + 2\Delta }  \right)\\
&\vdots\\
f^{-}_{66w+25} (q) & = -2\, \left(h_{18w+7} (q)\, q^{2n+ 36w +12 } + h_{12w+5 } (q) \, q^{2n + 72w + 24 +  \Delta }  + h_{6w+3} (q) \, q^{2n + 90w +30 + 2\Delta } \notag\right.\\
& \notag\left. + h_1 (q) \, q^{2n + 90w +30 + 3\Delta }  \phantom{1}\right)\\
f^{-}_{66w+31} (q) & = -2\, \left(h_{18w+9} (q)\, q^{2n+ 36w +16 } + h_{12w+7 } (q) \, q^{2n + 72w + 34 +  \Delta }  + h_{6w+5} (q) \, q^{2n + 90w + 46 + 2\Delta } \notag\right.\\
& \notag\left. + h_3 (q) \, q^{2n + 90w +52 + 3\Delta }  \phantom{1}\right)\\
&\vdots\\
\end{aligned}$$ where $n \in \mathbb{Z}$ and $\Delta =9w+6$.
:::

We state several remarks.\
**Remark 1** As in the previous cabling, the above sequence terminates for a fixed $w$.\
**Remark 2** $n$ can be found easily from the $\hbar$ series of $F_{C_{(r,2)}(\bm{4_1})}(x,q)$. We propose a formula for $n$ below.\
**Remark 3** A power of each $q$-monomial increases by multiples for a positive integer from $f^{\pm}_{m}$ to $f^{\pm}_{m+6}$\
**Remark 4** Coefficient functions $f_d (q)$ that do not fit into the above pattern vanish.\
**Remark 5** $h_1 (q) q^{s}$ is added when $h_{6w+3}$ appears in $f^{\pm}_{b}(q)$ for any $b$.

::: conjecture
For the above family of knots, the power $n \in \mathbb{Z}$ in Conjecture 4.1 is given by $3w+2$.
:::

As in the $(2w+1,2)$-cabling case, we get $f_m(q)$ for the mirror knot $m(K)$.

::: cor
For a $(3w+1,3)$-cabling of $\bm{4_1}$ where $w < -3$, its nonzero initial data $\left\{f_m (q) \right\}= \left\{f^{+}_m (q) \right\}\bigsqcup \left\{f^{-}_m (q) \right\}$ for a recursion relation are given by $q \longleftrightarrow q^{-1}$ in Conjecture 4.1.
:::

::: conjecture
For the family of the cable knots $K_w =C_{(3w+1,3)}(\bm{4_1})$ in $\mathbb{Z}HS^3$ for $w>3$, all of their coefficient functions $f^{\pm}_m (q) \in \mathbb{Z}[q^{\pm 1}]$ of $F_{K_w}(x,q)$ can be expressed as linear combinations of the coefficient functions $\left\{h_s (q) \right\}$ of $F_{\bm{4_1}}(x,q)$ following the pattern of Conjecture 4.1.
:::

# Examples

## Example 1

We begin with the simplest example $K=C_{(13,3)}(\bm{4_1})$.

::: prop
The $\hbar$ expansion of the $J_{K,n}(q)$ is given by $$\begin{aligned}
    J_{K,n}(e^{\hbar}) & = 1 + \left(47 - 47 n^2 \right)\hbar^2 + \left(-624 + 624 n^2 \right)\hbar^3 + \left(\frac{151919}{12} - 14605 n^2 + \frac{23341}{12} n^4 \right)\hbar^4\\
    & + \left(- 294528 + 361088 n^2 - 66560 n^4 \right)\hbar^5 + \Big(  \frac{2864712407}{360} - \frac{122607733}{12} n^2 + \frac{28027787}{12} n^4 \\
    & - \frac{27314027}{360} n^6 \Big) \hbar^6 + \cdots
\end{aligned}$$
:::

::: lemma
The Alexander polynomial of $C_{(13,3)}(\bm{4_1})$ is given by $$\begin{aligned}     
\Delta_{C_{(13,3)}{(\bm{4_1})}}(x) & = \Delta_{\bm{4_1}} (x^3) \Delta_{T_{(3,13)}}(x)\\
& = -t^{15}-\frac{1}{t^{15}}+t^{14}+\frac{1}{t^{14}}+2 t^{12}+\frac{2}{t^{12}}-2 t^{11}-\frac{2}{t^{11}}+t^9+\frac{1}{t^9}-t^8-\frac{1}{t^8}+t^6+\frac{1}{t^6}\\
& -t^5-\frac{1}{t^5}+t^3+\frac{1}{t^3}-2 t^2-\frac{2}{t^2}+t+\frac{1}{t}+1\\
\end{aligned}$$
:::

::: prop
The symmetric expansion of the inverse of the Alexander polynomial of $K$ in the limit of $\hbar \rightarrow 0$ is given by $$\begin{aligned}
\lim_{q \rightarrow 1} 2F_{K}(x,q) &  =  2\, \text{s.e.} \left(\frac{x^{1/2}-x^{-1/2}}{\Delta_{K}(x)} \right)\\
& = 2 x^{29/2} -\frac{2}{x^{29/2}} +4 x^{35/2} -\frac{4}{x^{35/2}} +10 x^{41/2} -\frac{10}{x^{41/2}} +26 x^{47/2} -\frac{26}{x^{47/2}} +68 x^{53/2}\\
& -\frac{68}{x^{53/2}} -2 x^{55/2} +\frac{2}{x^{55/2}} +178 x^{59/2} -\frac{178}{x^{59/2}} -4 x^{61/2} +\frac{4}{x^{61/2}} +466x^{65/2} \\
& -\frac{466}{x^{65/2}}-10 x^{67/2}+\frac{10}{x^{67/2}} +1220 x^{71/2}-\frac{1220}{x^{71/2}} + \cdots \in \mathbb{Z}\left[\left[x^{\pm 1/2} \right]\right]
\end{aligned}$$
:::

In this case, the coefficients of $x^{55/2}, x^{61/2}, x^{67/2}$ and so forth are negative, which are reflected as negative coefficient elements in the initial data.

::: prop
The initial data for the recursion relation of $K$ consists of $I=\left\{f_{j} (q) \in \mathbb{Z}[q^{\pm 1}] | j=1,\cdots ,353 \right\}$. The nonzero elements in $I$ are obtained by setting $w=4$ and hence $n=14$ in Conjecture 4.1.
:::

We extrapolate Conjecture 4.1 beyond $I$. $$\begin{aligned}
f^{-}_{355}(q) & = -2 \left(h_{101}\, q^{228} + h_{75}\, q^{492} + h_{49}\, q^{678} + h_{23}\, q^{786} \right)\\
f_{357}(q) & = 0
\end{aligned}$$ $f^{-}_{355}$ indeed agree with that of the recursion result and the vanishing of $f_{357}$ is consistent with the recursion method as well. We confirm that several subsequent $f_m (q)$'s match with the results of the recursion. For example, $$\begin{aligned}
f^{+}_{359}(q) & = 2 \left(h_{111}\, q^{124} + h_{85}\, q^{418}+ h_{59}\, q^{634}+ h_{33}\, q^{772} + h_7 \, q^{832} \right)\\
f^{-}_{361}(q) & = -2 \left(h_{103}\, q^{232} +  h_{77}\, q^{502} + h_{51}\, q^{694} + h_{25}\, q^{808} \right)
\end{aligned}$$

We perform Dehn surgeries along $-1/r$ slopes for a few $r$. $$\begin{aligned}
\hat{Z}_0 [S^{3}_{-1}(C_{13,3}(4_1));q] & = q^{\frac{419}{2}} \Big( -2+2 q^{29}-4 q^{95}+4 q^{130}-2 q^{207}-6 q^{208}-2 q^{209}+2 q^{248}+6 q^{249}\\
& +2   q^{250}-4 q^{337}-4 q^{338}-10 q^{339}-4 q^{340}-4 q^{341}+4 q^{384}+4 q^{385} + \cdots  \Big)\\
\hat{Z}_0 [S^{3}_{-\frac{1}{2}}(C_{13,3}(4_1));q] & = q^{\frac{839}{2}}  \Big( -2+2 q^{29}-4 q^{191}+4 q^{226}-2 q^{417}-6 q^{418}-2 q^{419}+2 q^{458}\\
& +6 q^{459}+2 q^{460}-4 q^{679}-4 q^{680}-10 q^{681}-4 q^{682}-4 q^{683}+4 q^{726}+4 q^{727} + \cdots  \Big)\\
\hat{Z}_0 [S^{3}_{-\frac{1}{3}}(C_{13,3}(4_1));q] & = q^{\frac{1259}{2}} \Big( -2+2 q^{29}-4 q^{287}+4 q^{322}-2 q^{627}-6 q^{628}-2 q^{629}+2 q^{668}\\
& +6 q^{669}+2 q^{670}-4 q^{1021}-4 q^{1022}-10 q^{1023}-4 q^{1024}-4 q^{1025}+4 q^{1068}+ \cdots  \Big)\\
\end{aligned}$$

## Example 2

We move onto $K=C_{(16,3)}(\bm{4_1})$.

::: prop
The $\hbar$ expansion of the $J_{K,n}(q)$ is given by $$\begin{aligned}
    J_{K,n}(e^{\hbar}) & = 1 + \left(111 - 111 n^2 \right)\hbar^2 + \left(-2128 + 2128 n^2 \right)\hbar^3 + \left(\frac{253477}{4} - 73197 n^2 + \frac{39311}{4} n^4 \right)\hbar^4\\
    & + \left(- 2159616 + \frac{7947776}{3} n^2 - \frac{1468928}{3} n^4 \right)\hbar^5 + \cdots
\end{aligned}$$
:::

::: lemma
The Alexander polynomial of $C_{(16,3)}(\bm{4_1})$ is given by $$\begin{aligned}     
\Delta_{C_{(16,3)}{(\bm{4_1})}}(x) & = t^{21}-\frac{1}{t^{21}}+t^{20}+\frac{1}{t^{20}}+2 t^{18}+\frac{2}{t^{18}}-2t^{17}-\frac{2}{t^{17}}+t^{15}+\frac{1}{t^{15}}-t^{14}-\frac{1}{t^{14}}+t^{12}\\
& +\frac{1}{t^{12}} -t^{11}-\frac{1}{t^{11}}+t^9+\frac{1}{t^9}-t^8-\frac{1}{t^8}+t^6+\frac{1}{t^6}-t^5-\frac{1}{t^5}+t^3+\frac{1}{t^3}-2 t^2-\frac{2}{t^2}\\
& +t+\frac{1}{t}+1\\
\end{aligned}$$
:::

::: prop
The symmetric expansion of the inverse of the Alexander polynomial of $K$ in the limit of $\hbar \rightarrow 0$ is given by $$\begin{aligned}
\lim_{q \rightarrow 1} 2F_{K}(x,q) &  =  2\, \text{s.e.} \left(\frac{x^{1/2}-x^{-1/2}}{\Delta_{K}(x)} \right)\\
& = 2 x^{35/2} -\frac{2}{x^{35/2}} +4 x^{41/2} -\frac{4}{x^{41/2}} +10 x^{47/2} -\frac{10}{x^{47/2}} +26 x^{53/2} -\frac{26}{x^{53/2}} +68 x^{59/2}\\
& -\frac{68}{x^{59/2}}  +178 x^{65/2} -\frac{178}{x^{65/2}} -2 x^{67/2} +\frac{2}{x^{67/2}} +466 x^{71/2} -\frac{466}{x^{71/2}} -4 x^{73/2} +\frac{4}{x^{73/2}} \\
& +1220x^{77/2} -\frac{1220}{x^{77/2}}-10 x^{79/2}+\frac{10}{x^{79/2}} +3194 x^{83/2}-\frac{3194}{x^{83/2}} + \cdots \in \mathbb{Z}\left[\left[x^{\pm 1/2} \right]\right]
\end{aligned}$$
:::

In this case, the coefficients of $x^{67/2}, x^{73/2}, x^{79/2}$ etc are negative, which coincide with the negative coefficient elements in the initial data in Conjecture 4.1.

::: prop
The initial data for the recursion relation of $K$ consists of $I=\left\{f_{j} (q) \in \mathbb{Z}[q^{\pm 1}] | j=1,\cdots ,387 \right\}$. The nonzero elements in $I$ are obtained by setting $w=5$ and thus $n=17$ in Conjecture 4.1.
:::

We verified that $f_{389}$ and $f_{391}$ obtained from the recursion match with those from the applications of Conjecture 4.4. Furthermore, vanishing of $f_{393}$ is consistent with Conjecture 4.4.

**Acknowledgments.** I would like to thank the referee for helpful suggestions.
