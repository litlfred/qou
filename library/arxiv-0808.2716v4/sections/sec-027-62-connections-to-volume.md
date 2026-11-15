---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-027-62-connections-to-volume
section_title: "Connections to volume"
section_number: 6.2
pages: 40-42
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.959
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#subsec:volume-jones label="subsec:volume-jones"}

Proposition [\[prop:3-braids\]](#prop:3-braids){reference-type="ref" reference="prop:3-braids"} and Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} immediately imply the following.

::: theorem
Let $K$ be a hyperbolic closed $3$--braid. From the Jones polynomial $J_K(t)$, define ${\zeta_K}, {\zeta'_K}$ as in Definition [\[def:zeta\]](#def:zeta){reference-type="ref" reference="def:zeta"}. Let $\zeta = \max \left\{ {\left\vert \zeta_K \right\vert}, {\left\vert \zeta'_K \right\vert} \right\}$. Then $$4v_3 \cdot \zeta - 281 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \:
4v_8 \, ( \zeta +1 ).$$ Furthermore, the multiplicative constants in both the upper and lower bounds are sharp. []{#thm:relations label="thm:relations"} 0◻
:::

In contrast with Proposition [\[prop:3-braids\]](#prop:3-braids){reference-type="ref" reference="prop:3-braids"}, there exist $3$--braids for which the second coefficient of the Jones polynomial is quite different from $s$.

::: prop
[]{#prop:cancelation label="prop:cancelation"} For every $s>1$ there is a knot $K = K_s$, represented by the 3--braid word $$b= C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}
\sigma_2^{-q_s},\ \ \mbox{with} \ \ p_i, q_i>0,$$

such that the second and next-to-last coefficients of the Jones polynomial $J_K(t)$ satisfy $$\beta_K \: = \: \frac{s(s+3)}{-2} + 1 ,  \qquad \beta'_K = s.$$
:::

The head and tail of the Jones polynomial for several values of $s$ is computed in Table [\[table:jones\]](#table:jones){reference-type="ref" reference="table:jones"}.

$${\setlength{\jot}{1.5ex}
\begin{array}{|c | r c l | }
\hline
s & \multicolumn{3}{c|}{\mbox{Jones polynomial } J_{K_s} } \\
\hline
2 &  2 \,t ^{-8} -4 \,t ^{-9} +9 \,t ^{-10} -14 \,t ^{-11} + & \!\! \ldots \!\! & +\, 9 \,t ^{-22} -5 \,t ^{-23} +2 \,t ^{-24} -t ^{-25} \\
3 & 3 \,t ^{-12} -8 \,t ^{-13} +20 \,t ^{-14} -39 \,t ^{-15} + & \!\! \ldots \!\!  & +\,20 \,t ^{-34} -9 \,t ^{-35} +3 \,t ^{-36} -t ^{-37}  \\
4 & 4 \,t ^{-16} -13 \,t ^{-17} +37 \,t ^{-18} -85 \,t ^{-19} + & \!\! \ldots \!\!  & +\,37 \,t ^{-46} -14 \,t ^{-47} +4 \,t ^{-48} -t ^{-49}  \\
5 & 5 \,t ^{-20} -19 \,t ^{-21} +61 \,t ^{-22} -160 \,t ^{-23} + & \!\! \ldots \!\!  & +\,61 \,t ^{-58} -20 \,t ^{-59} +5 \,t ^{-60} -t ^{-61} \\
6 & 6 \,t ^{-24} -26 \,t ^{-25} +93 \,t ^{-26} -273 \,t ^{-27} + & \!\! \ldots \!\!  & +\,93 \,t ^{-70} -27 \,t ^{-71} +6 \,t ^{-72} -t ^{-73} \\
7 & 7 \,t ^{-28} -34 \,t ^{-29} +134 \,t ^{-30} -434 \,t ^{-31} + & \!\! \ldots \!\!  & +\,134 \,t ^{-82} -35 \,t ^{-83} +7 \,t ^{-84} -t ^{-85} \\
8 & 8 \,t ^{-32} -43 \,t ^{-33} +185 \,t ^{-34} -654 \,t ^{-35} + & \!\! \ldots \!\!  & +\,185 \,t ^{-94} -44 \,t ^{-95} +8 \,t ^{-96} -t ^{-97} \\
9 & 9 \,t ^{-36} -53 \,t ^{-37} +247 \,t ^{-38} -945 \,t ^{-39} + & \!\! \ldots \!\!  & +\,247 \,t ^{-106} -54 \,t ^{-107} +9 \,t ^{-108} -t ^{-109} \\
10 & 10 \,t ^{-40} -64 \,t ^{-41} +321 \,t ^{-42} -1320 \,t ^{-43} + & \!\! \ldots \!\!  & +321 \,t ^{-118} -65 \,t ^{-119} +10 \,t ^{-120} -t ^{-121} \\\hline
\end{array}
}$$

::: proof
*Proof.* Fix $s>1$, and let $p_1 = \ldots = p_{s-1} = 2, \quad p_s = 3, \quad
q_1 = \ldots = q_{s-1} = 6, \quad q_s = 7.$

Notice that ${\bf p}= \sum p_i=2s+1$ and ${\bf q}= \sum
q_i=6s+1$; thus, in particular, they are both odd. Let $k=2s$ and let $K$ be the closure of the generic $3$--braid $$b= C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}
\sigma_2^{-q_s}.$$

Since $C^k$ is a pure braid, and each of $\sigma_1^{p_1}, \ldots,
\sigma_2^{-q_{s-1}}$ is also a pure braid (because their powers are even), $K$ will have the same number of components as the closure of $\sigma_1^{3} \sigma_2^{-7}$. Hence $K$ is a knot.

The Jones polynomial $J_K(t)$ will be the sum of equations ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) and ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}). Note that the leading terms of these equations are $$(-1)^{{\bf p}} \ t^{(3{\bf q}-{\bf p})/2-6k} \: = \: -t^{(16s+2)/2-12s} =\: - t^{-4s+1},$$

and $$(-1)^{{\bf p}-{\bf q}} \  t^{({\bf q}-{\bf p})/2-3k+1} \: = \: t^{(4s)/2-6s+1} \: = \: t^{-4s+1},$$

which will cancel. Thus, continuing along equations ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) and ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}), one can see that the leading monomial of $J_{K_b}(t)$ will be $(-1)^{{\bf p}+1} s\, t^{-4s}$, and the second term will be $$(\gamma_{K_a}) t^{-4s-1} + (-1)^{({\bf p}-{\bf q})}\ t^{-4s-1} \: =
\: \left( \gamma_{K_a} + 1 \right) t^{-4s-1}.$$ Since $s>1$ and $p_i, q_i > 1$ for all $i$, Lemma [\[lemma:alternating\]](#lemma:alternating){reference-type="ref" reference="lemma:alternating"}(c) implies that $$\gamma_{K_a} \:=\: (-1)^{{\bf p}}\, \left( \frac{s(s+3)}{2} \right) 
\:=\: \frac{s(s+3)}{-2},
\qquad \mbox{hence} \qquad
\beta_K \: = \:  \frac{s(s+3)}{-2}+1.$$

Now we consider the term $\beta'_K$. The two lowest--degree terms of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) are $$(-1)^{{\bf q}} \ t^{({\bf q}-3{\bf p})/2 -6k} \: = \: - t^{(-2)/2 - 12s }  \: = \: -t^{-12s-1} \qquad
\mbox{and} \qquad
(-1)^{{\bf q}+1}s \, t^{-12s} \: = \: s \, t^{-12s}.$$ The remaining terms of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) are $$(-1)^{{\bf p}-{\bf q}+1} t^{({\bf q}-{\bf p})/2-6k\pm 1} \: =\: 
t^{(4s)/2 - 12s \pm 1} \: = \:  -t^{-10s \pm 1} .$$ Since $-12s < -10s-1$ for all positive $s$, no term of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) can affect either of the two lowest--degree terms of $J_{K_b}(t)$. Therefore, $$\alpha'_K = (-1)^{{\bf q}} = -1 \qquad \mbox{and} \qquad
\beta'_K = (-1)^{{\bf q}+1} s = s.$$ ◻
:::

::: theorem
[]{#thm:counterexample label="thm:counterexample"} There does not exist a function $f(\cdot, \cdot)$ of two variables, together with positive constants $C_1, \ldots, C_4$ such that $$C_1 f(\beta_K, \beta'_K) - C_2 \: < \: {\rm vol}(S^3{\smallsetminus}K) \:<\: C_3
f(\beta_K, \beta'_K) + C_4$$ for every hyperbolic knot $K$. In other words, the second and next-to-last coefficients of the Jones polynomial do not coarsely predict the volume of a knot.
:::

::: proof
*Proof.* Suppose, for a contradiction, that such a function $f(\cdot, \cdot)$ does exist. Then it will follow that for every pair of knots $K$ and $L$, such that $\beta_K = \beta_L$ and $\beta'_K = \beta'_L$, $$\label{eqn:volume-ratio}
{\rm vol}(S^3 {\smallsetminus}L) \: < \: \frac{C_3}{C_1} \, {\rm vol}(S^3 {\smallsetminus}K)
+ \frac{C_2 C_3}{C_1} + C_4 .$$ On the other hand, we shall construct an infinite sequence of such pairs $K_s$ and $L_s$, such that the volumes ${\rm vol}(S^3 {\smallsetminus}
L_s)$, ${\rm vol}(S^3 {\smallsetminus}K_s)$, as well as the ratio ${\rm vol}(S^3 {\smallsetminus}
L_s) / {\rm vol}(S^3 {\smallsetminus}K_s)$ go to infinity as $s$ goes to infinity. This will contradict the existence of $f$.

The sequence $K_s$ is the one given by Proposition [\[prop:cancelation\]](#prop:cancelation){reference-type="ref" reference="prop:cancelation"}, where we require that $s \equiv 3 \mod 4$ and $s >10$. By Proposition [\[prop:cancelation\]](#prop:cancelation){reference-type="ref" reference="prop:cancelation"}, these knots satisfy $$\beta_{K_s} = \frac{s(s+3)}{-2} + 1 , \qquad \mbox{and} \qquad
\beta'_{K_s} = s.$$

The sequence $L_s$ will consist of $(3, \ldots, 3, -3, \ldots, -3)$ pretzel knots, where there are $$n = \left( \frac{s(s+3)}{2} - 2 \right) \quad \mbox{positive 3's} \quad \mbox{and}
\quad m = \left( s-1 \right) \quad \mbox{negative 3's}.$$

When $s \equiv 3 \mod 4$, it follows that $n$ is odd, $m$ is even, and thus $L_s$ is indeed a knot.

It is easy to check that the standard pretzel diagram $D_s$ of one these knots is adequate. Computing the graphs ${\mathbb{G}_A}(D_s)$, ${\mathbb{G}_B}(D_s)$ gives $$v_A = n+2m, \qquad e'_A = n+3m, \qquad v_B = 2n+m, \qquad e'_B =
3n+m.$$ Also, we may compute the writhe of $D_s$ to be $w(D) = 3m-3n$. Now, Lemma [\[lemma:adequate-jones\]](#lemma:adequate-jones){reference-type="ref" reference="lemma:adequate-jones"} gives $$\beta_{L_s}  \:=\: (-1)^{v_B + w(D)} (e'_B - v_B + 1) 
\:=\: (-1)^{-n + 4m} (n+1)
\:=\: (-1)^n(n+1) \:=\: \frac{s(s+3)}{-2} + 1,$$

since $n$ is odd. Similarly, $$\qquad \beta'_{L_s} \:=\: (-1)^{v_A + w(D)} (e'_A - v_A + 1) \:=\:
(-1)^m(m+1) \:=\: s.$$

Therefore, $\beta_{K_s} = \beta_{L_s}$ and $\beta'_{K_s} =
\beta'_{L_s}$ for all $s \equiv 3 \mod 4$.

Now, consider the volumes of these links. By Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"}, $$4v_3\,s -277 < {\rm vol}(S^3 {\smallsetminus}K_s) < 4 v_8 \, s.$$

On the other hand, the pretzel diagram $D_s$ contains $(n+m) > s^2/2$ twist regions and is built by joining together $(n+m) > s^2/2$ rational tangles. Thus, by [@fkp:conway Theorem 1.5], $${\rm vol}(S^3 {\smallsetminus}L_s) \: \geq \: \frac{v_8}{2} \left(1 - \left(
\frac{8\pi}{11.524 + s^2 \sqrt[4]{2} /2 } \right)^2 \right)^{\!3/2}
\!\! \left(\frac{s^2}{2} -3\right) \: > \: \frac{v_8 \, s^2}{8} \qquad
\mbox{for } s >10.$$

Hence ${\rm vol}(S^3 {\smallsetminus}L_s) / {\rm vol}(S^3 {\smallsetminus}K_s) \geq s/32$. Since both volumes are eventually large enough that the additive constants in equation ([\[eqn:volume-ratio\]](#eqn:volume-ratio){reference-type="ref" reference="eqn:volume-ratio"}) do not matter, this contradicts equation ([\[eqn:volume-ratio\]](#eqn:volume-ratio){reference-type="ref" reference="eqn:volume-ratio"}). Thus the function $f$ cannot exist. ◻
:::
