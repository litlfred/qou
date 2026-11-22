---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-001-2-hyperbolic-dehn-fillings-determined-by-their-v
section_title: "Hyperbolic Dehn fillings determined by their volumes"
section_number: 2
pages: 5-8
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.986
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
[]{#cusped_hyp label="cusped_hyp"}

Let $M$ be a cusped hyperbolic 3-manifold and let $T$ be a horospherical torus cross section of one of the cusps of $M$. Choose an oriented basis for $H_1(T;\mathbb{Z}) \cong \mathbb{Z}^2$, called the "meridian" and "longitude" for $T$, and let $M(a,b)$ be the result of Dehn filling along the simple closed curve with homology class $(a,b) \in H_1(T;\mathbb{Z}) \cong \mathbb{Z}^2$.

Let $A$ denote the area of $T$ and $L(a,b)$ the length of the geodesic on $T$ with homology class $(a,b)$. Then we will study the quadratic form $$\label{eq1}
Q(a,b) = {L(a,b)^2 \over A}.$$ (This gives the square of the length of $(a,b)$ when the torus $T$ is rescaled to have area 1, and is also known as the extremal length of the curve $(a,b)$.)

::: rmk
(Cusp Shape Parameters)[]{#cusp_param label="cusp_param"} *The horospherical torus $T$ is similar to the Euclidean torus $\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$, with *shape parameter* $\tau \in \mathbb{C}$ defined by $$\label{eq2}
\tau = (\text{complex translation of longitude})/
(\text{complex translation of meridian}),$$ where the torus is viewed from the cusp. Note that with the standard orientation convention for a link complement in $S^3$ or for an oriented manifold in SnapPea, this means that $\tau$ will have *negative* imaginary part.[^1] Then we have $$\label{eq3}
Q(a,b) = {  |a + b \tau|^2 \over | \text{Im}( \tau )| }.$$*
:::

The following result shows that the volume of $M(a,b)$ determines $Q(a,b)$ up to a uniformly bounded error. This observation will play a key role in our work.

::: prop
[]{#error_bound label="error_bound"} Let $V_0$ be the volume of the complete hyperbolic structure on $M$. Then there exist constants $C_1=C_1(M), C_2 =C_2(M) >0$ such that

1.  the Dehn filling $M(a,b)$ is hyperbolic whenever $L(a,b) > C_1$, and

2.  for all hyperbolic Dehn fillings $M(a,b)$, $$\label{eq4}
    \left| {\pi^2  \over \Delta V(a,b)}  - {Q(a,b)} \right| < C_2$$ where $\Delta V(a,b) = V_0 - \text{Vol} (M(a,b))$.
:::

::: proof
*Proof.* (a) follows from Thurston's hyperbolic Dehn surgery theorem [@Th].

\(b\) The asymptotic volume formula of Neumann-Zagier [@NZ] shows that the decrease in volume under Dehn filling satisfies $$\label{eq5}
\Delta V(a,b) = {\pi^2 \over Q(a,b)} +O\left({1 \over Q(a,b)^2}\right).$$ This implies the result of (b) when $Q(a,b)$ is sufficiently large. But there are only finitely many additional $(a,b)$ with $M(a,b)$ hyperbolic, so the result follows. ◻
:::

::: rmk
*(a) If $T$ is a maximal embedded horospherical torus, then we can take $C_1=6$ by the "length 6 theorem" of Agol [@agol_dehn] and Lackenby [@lack] and the Geometrization Theorem of Perelman.*

\(b\) The work of Hodgson-Kerckhoff [@HK Theorem 5.12 and Figure 2], and some numerical calculations imply that $$\label{eq6}
-7.05 \le {\pi^2  \over \Delta V(a,b)} - Q(a,b)  \le 5.82$$ whenever $Q(a,b) \ge 57.5041$ and $\Delta V \le 0.155$. Then by volume computations using SnapPy or Snap for the finite number of hyperbolic Dehn fillings with $\Delta V > 0.155$, an explicit value of $C_2$ can be determined for a given manifold $M$.

Numerical calculations using SnapPy suggest that $\left| {\pi^2  \over \Delta V(a,b)} - Q(a,b)\right|$ for hyperbolic Dehn fillings $M(a,b)$ is often considerably lower than these general bounds.
:::

We now study the quadratic form $Q(a,b)$ for a cusped hyperbolic 3-manifold $M$. Let $$\label{eq7}
S_Q= \{ Q(a,b) : a,b \text{ are relatively prime integers} \}.$$

**Key Idea.** Let $(a_0,b_0)$ be a pair of relatively prime integers such that $M(a_0,b_0)$ is hyperbolic and let $q_0 = Q(a_0,b_0)$. Assume that

1.  there is large enough 2-sided gap around $q_0$ in $S_Q$, and

2.  $Q(a,b)=q_0$ has few solutions with $(a,b)$ relatively prime integers.

Then there are few Dehn fillings $M(a,b)$ with the same volume as $M(a_0,b_0)$.

More precisely,

::: prop
[]{#few_mflds_with_vol label="few_mflds_with_vol"} Let $(a_0,b_0)$ be a pair of relatively prime integers such that $M(a_0,b_0)$ is hyperbolic and let $q_0 = Q(a_0,b_0)$. Let $C_2 = C_2(M) >0$ be as in Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}. Assume that

::: center
there exists $g > 2C_2$ such that $s \in S_Q$ and $|s-q_0|< g$ implies $s= q_0$.
:::

Then $\text{Vol} (M(a,b)) =  \text{Vol} (M(a_0,b_0)$ implies $Q(a,b)=Q(a_0,b_0)$. Hence the number of such manifolds $M(a,b)$ is at most $n(q_0)/2$, where $n(q_0)$ is the number of solutions to $Q(a,b)=q_0$ with $a,b$ relatively prime integers.
:::

::: proof
*Proof.* Assume that $M(a,b)$ is hyperbolic with $\text{Vol} (M(a,b)) =  \text{Vol} (M(a_0,b_0))$ and let $\Delta V=  V_0 - \text{Vol} (M(a_0,b_0))$. Then Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"} implies $$\left| {\pi^2  \over \Delta V}  -Q(a,b) \right| < C_2 \text{ and } \left| {\pi^2  \over \Delta V}  -Q(a_0,b_0) \right| < C_2,$$ so $$\left| Q(a,b)   - Q(a_0,b_0) \right| < 2C_2 < g.$$ Hence $Q(a_0,b_0)=Q(a,b)$ by our assumption. But $(a,b)$ and $(-a,-b)$ Dehn fillings on $M$ give the same manifold, so the result follows. ◻
:::

::: rmk
[]{#few_with_symm label="few_with_symm"}

*More generally, there is a version of the previous Proposition which applies when the horospherical torus $T = \mathbb{C}/(\mathbb{Z}+\tau \mathbb{Z})$ has symmetries other than those induced by the maps $(a,b) \mapsto \pm(a,b)$ that extend to symmetries of the cusped manifold $M$.*

Let $G_Q$ be the group of integral automorphisms of the quadratic form $Q$, $$\label{eq8}
 G_Q = \{ A \in GL(2,\mathbb{Z}) :  Q(A X )= Q( X  ) \text{ for all } X=(x,y) \in \mathbb{Z}^2 \}.$$ For each isometry $g$ of $M$ preserving the cusp corresponding to $T$, the induced action on homology gives an automorphism $g_*$ of $H_1(T) \cong \mathbb{Z}^2$. Let $G_M \subset G_Q$ be the subgroup generated by these automorphisms $g_*$ together the automorphism $(x,y) \mapsto (-x,-y)$. Then for each $\sigma \in G_M$, the Dehn fillings of $M$ along $(a,b)$ and $(a',b')=\sigma(a,b)$ give homeomorphic manifolds.

Then the previous argument shows that, with the hypotheses and notation of Proposition [\[few_mflds_with_vol\]](#few_mflds_with_vol){reference-type="ref" reference="few_mflds_with_vol"}, the number of hyperbolic manifolds $M(a,b)$ with $\text{Vol} (M(a,b)) =  \text{Vol} (M(a_0,b_0)$ is at most $n(q_0)/|G_M|$, where $n(q_0)$ is the number of solutions to $Q(a,b)=q_0$ with $a,b$ relatively prime integers.
:::

If the cusp shape parameter $\tau$ belongs to an imaginary quadratic field, then the quadratic form $$Q(x,y) = |x+\tau y|^2= (x + \tau y)(x + \bar\tau y) = x^2 + (\tau+\bar\tau) xy + |\tau|^2 y^2$$ has rational coefficients. Hence, after rescaling, we can assume that the coefficients are relatively prime integers.

If $Q$ is an *integral quadratic form* $$\label{eq9}
Q(x,y)= a x^2 + b xy + c y^2.$$ where $a,b,c \in \mathbb{Z}$, then $D = b^2 - 4ac$ is called the *discriminant* of $Q$. The following elementary result can be found, for example, in [@landau Theorem 201, p180], [@cox pp25--26] or [@buell pp49--50]. Here, and henceforth, we say that a pair of integers $(x,y)$ is *primitive* if $\gcd(x,y)=1$.

::: lem
[]{#discr_quad_res label="discr_quad_res"} Assume that $m$ has a primitive integer representation by an integral quadratic form $Q$, i.e. $Q(x_0,y_0)=m$ where $(x_0,y_0) \in \mathbb{Z}^2$ with $\gcd(x_0,y_0)=1$. Then the discriminant $D$ of $Q$ is a quadratic residue modulo $4m$. In particular, every prime divisor $p$ of $m$ has Kronecker symbol $(D/p)=+1$.
:::

[^1]: Caution: this convention agrees with that used in Snap. However, in SnapPy the 'shape' reported by the function `cusp_info()` is the *complex conjugate* $\bar \tau$.
