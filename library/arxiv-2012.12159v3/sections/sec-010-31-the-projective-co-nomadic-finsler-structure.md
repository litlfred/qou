---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-010-31-the-projective-co-nomadic-finsler-structure
section_title: "The projective co-nomadic Finsler structure"
section_number: 3.1
pages: 8-11
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.968
---
We start with some terminology.

::: Definition
[]{#def:conomadic label="def:conomadic"} Two Finsler structures $F_1$, $F_2$ on $M$ are *co-translate* if $F_2-F_1$ is a $1$-form on $M$. A *co-nomadic Finsler structure* on a manifold is an equivalence class of co-translate Finsler structures. Similarly, we define an *exact co-nomadic Finsler structure* to be the equivalence class of Finsler norms up to an exact $1$-form on $M$.
:::

Geometrically, a co-nomadic Finsler structure is the data of all cotangent unit balls, fixed up to translation in each cotangent space. Given a co-nomadic Finsler structure $[F]$, represented by a Finsler norm $F$, its symmetrization $F^S(v):=\frac{1}2(F(v)+F(-v))$ is clearly a reversible Finsler metric that is independent of $F$. The Holmes-Thompson volume element of a co-nomadic Finsler structure is similarly well-defined. Furthermore, if $N\subset M$ is a $k$-dimensional submanifold, it inherits a co-nomadic Finsler structure, in particular its $k$-dimensional Holmes-Thompson volume is well-defined.

::: Lemma
[]{#lem:exact_property label="lem:exact_property"} Given an *exact* co-nomadic Finsler structure $[F]$ on a manifold $M$, represented by the Finsler norm $F$, and an oriented closed curve, its length only depends on $[F]$. Moreover, the geodesics of $F$ only depend on $[F]$.
:::

The first statement is clear. For the second, recall that a geodesic is any curve that locally extremizes the length functional of a curve with fixed endpoints. Modifying the norm by an exact $1$-form simply adds a constant to the length functional.

Take $x\in \mathop{\mathrm{int}}(K)$, and consider the cone $K^\vee\subset V^*$. For any non-zero $\xi\in V^*$, set $B_\xi:=K^\vee\cap (x^\perp +\xi)-\xi\subset x^\perp$. It is a convex body (projectively equivalent to $K^\vee$). Furthermore, $B_{t\xi}=tB_{\xi}$ for all $t\neq 0$. Finally if $\xi=\xi_1-\xi_2\in x^\perp$, we get $B_{\xi_2}=B_{\xi_1}+\xi$. Consequently, $B_\bullet$ defines a convex set in $(V^*/x^\perp)^*\otimes x^\perp=T^*_x\mathbb{P}$, up to translation. Let us call it the *projective co-nomadic Finsler structure on $\mathop{\mathrm{int}}(K)$*.

To obtain a true Finsler structure, one can proceed in several ways.

1.  Fix a Euclidean structure on $V$. One can then take $\xi=x^\perp$ and obtain the fixed cotangent ball $K^\vee\cap (x^\perp + x)-x\subset T^*_x\mathbb{P}=T_x\mathbb{P}=x^\perp$. We call it the orthogonal Finsler structure.

2.  Fix $\eta\in \mathop{\mathrm{int}}(K^\vee)$, and take $B_x^*K:=K^\vee\cap (x^\perp +\eta_0)-\eta_0$ for any $\eta_0\in\eta\subset V^*$. As we will see, this is simply the reverse Funk metric, see Proposition [\[prop:projective_funk\]](#prop:projective_funk){reference-type="ref" reference="prop:projective_funk"}.

3.  Fix an affine-equivariant point selector $S$ in the interior of convex bodies (which need only be defined on projective images of $K^\vee$), such as the center of mass or Santaló point. We then get a projectively invariant construction of a Finsler metric on $\mathop{\mathrm{int}}(K)$ which is co-translate to the reverse Funk metric.

Given an extra input $\alpha$ from the above list, we will say that the projective co-nomadic Finsler structure is *anchored* by it.

The following lemma relates the notions of linear and projective polarity. It assumes $V=\mathbb{R}^{n+1}$ is equipped with the standard Euclidean structure, and so all linear spaces are identified with their duals.

::: Lemma
[]{#lem:two_dualities label="lem:two_dualities"} Identify a convex body $K\subset \mathbb{R}\mathbb{P}^n$ with the cone $\tilde K\subset V=\mathbb{R}^{n+1}$, and with $K_t=\tilde K\cap \{x_{n+1}=t\}$. For $x\in V\setminus \{0\}$, write $[x]=\mathbb{R}x\in \mathbb{R}\mathbb{P}^n$. Then for $\hat p=(p,1)\in \mathop{\mathrm{int}}(K_1)\subset\mathbb{R}^n$, the set $-(K_1-\hat p)^o\subset \mathbb{R}^n=\{x_{n+1}=0\}$ coincides with $\pi_n(K^\vee\cap ([\hat p]^\perp+e_{n+1}))$, where $\pi_n$ projects orthogonally to $\mathbb{R}^n$.
:::

Consider $(-y,z)\in \mathbb{R}^n\oplus \mathbb{R}$ which lies in $K^\vee\cap ([\hat p]^\perp+e_{n+1})$. Then for all $(\kappa,1)\in K_1$ we have $\langle (-y, z-1), (p,1)\rangle=\langle -y,p\rangle +(z-1)=0$, and $\langle (-y,z),(\kappa,1)\rangle =\langle -y,\kappa\rangle +z\geq 0$. Thus $z=1+\langle y,p\rangle$, and $\langle y,\kappa-p\rangle \leq 1$. That is, $\pi_n(K^\vee\cap ([\hat p]^\perp+e_{n+1}))\subset \{(-y,1): y\in (K_1-\hat p)^o\}$. For the opposite inclusion, start with $(y,1)\in (K_1-\hat p)^o$, and verify that $(-y,1+\langle y, p\rangle )\in K^\vee\cap ([\hat p]^\perp+e_{n+1})$. In particular if $K\subset \mathbb{R}\mathbb{P}^n$ is given in the affine chart $\{x_{n+1}=1\}=\mathbb{R}^n+e_{n+1}$ by $K_1\subset \mathbb{R}^n$, then $K^\vee\cap \{x_{n+1}=1\}=-K_1^o+e_{n+1}$.

::: Proposition
[]{#prop:projective_funk label="prop:projective_funk"} Let $K\subset \mathbb{R}\mathbb P^n$ be a convex set, and fix $\eta\in \mathop{\mathrm{int}}(K^\vee)$. The $\eta$-anchored projective Finsler metric then coincides with $\mathop{\mathrm{RFunk}}_K^{\eta}$.
:::

Using a Euclidean structure to identify $T_x\mathbb P(V)=T_x^*\mathbb P(V)=x^\perp$, the cotangent ball of the Euclidean-anchored Finsler metric is $K^\vee\cap (x^\perp +x)$, where $x\in S^n$ is identified with $x\in \mathbb P(V)$.

Assume $\eta=e_{n+1}$. The affine chart is $\{x_{n+1}=1\}$, where the Funk cotangent unit ball at $\hat p =(p,1)=\frac{x}{x_{n+1}}=:A(x)$ is $(K_1-p)^o\subset e_{n+1}^\perp=T_p^*K_1]$. The identification between the two tangent spaces is the differential at $x$ of the map $A:S^{n}\to \{x_{n+1}=1\}$, namely $d_xA(v)=\frac{v}{x_{n+1}}-\frac{x}{x_{n+1}^2}v_{n+1}: x^\perp \to e_{n+1}^\perp$. The dual map is $$d_xA^*:e_{n+1}^\perp \to x^\perp,\quad  d_xA^*(u)=\frac{u}{x_{n+1}}-\frac{1}{x_{n+1}^2}\langle x,u\rangle e_{n+1}.$$ That is, $d_xA^*$ is a projection to $x^\perp$ parallel to $e_{n+1}$, followed by a $\frac{1}{x_{n+1}}$- homothety. Thus the inverse map $(d_xA^*)^{-1}$ is just the orthogonal projection on $e_{n+1}^\perp$, followed by an $x_{n+1}$-homothety: $$(d_xA^*)^{-1}=x_{n+1}\pi_n.$$

Observe that $K^\vee\cap (x^\perp +e_{n+1})=x_{n+1}(K^\vee\cap (x^\perp +x))$. The image of the $\eta$-anchored cotangent ball at $x$, viewed inside $x^\perp=T_x^*\mathbb{R}\mathbb P^n$, is therefore

$$(x^\perp +x)\cap K^\vee -\frac{e_{n+1}}{x_{n+1}} = (x^\perp +\frac{e_{n+1}}{x_{n+1}})\cap K^\vee -\frac{e_{n+1}}{x_{n+1}},$$ which is mapped by $(d_xA^*)^{-1}$ to

$$x_{n+1}\pi_n ((x^\perp +\frac{e_{n+1}}{x_{n+1}})\cap K^\vee ) =\pi _n((x^\perp+e_{n+1})\cap K^\vee)= -(K_1-\hat p)^o$$ using Lemma [\[lem:two_dualities\]](#lem:two_dualities){reference-type="ref" reference="lem:two_dualities"}. In light of the discussion following Definition [\[def:conomadic\]](#def:conomadic){reference-type="ref" reference="def:conomadic"}, Theorem [\[main:projective_invariants\]](#main:projective_invariants){reference-type="ref" reference="main:projective_invariants"} part i) follows.

::: Corollary
The symmetrization of the projective co-nomadic Finsler metric is the Hilbert metric.
:::

Since the Hilbert metric is the symmetrization of the Funk metric, this follows immediately from Proposition [\[prop:projective_funk\]](#prop:projective_funk){reference-type="ref" reference="prop:projective_funk"}

::: Remark
Thus we obtain a construction of the Hilbert metric which is transparently projectively invariant and Finslerian at the same time. An equivalent description can be found in [@vernicos_yang section 3].
:::

A careful examination reveals that the Funk metric itself is projectively invariant, up to the addition of an *exact* 1-form.

::: Proposition
[]{#prop:funk_exact label="prop:funk_exact"} Fix $\eta, \theta\in \mathop{\mathrm{int}}(K^\vee)$, and let $F_\eta, F_\theta$ be the corresponding Funk metrics on $\mathop{\mathrm{int}}(K)$. Then $F_\theta-F_\eta$ is an exact 1-form on $\mathop{\mathrm{int}}(K)$. The same holds for the reverse Funk metric.
:::

The statements for the Funk and reverse Funk metrics are trivially equivalent. Assume $\eta=e_{n+1}$, and use a Euclidean structure to identify $T_x^*K$ with $x^\perp$. Examining the proof of Proposition [\[prop:projective_funk\]](#prop:projective_funk){reference-type="ref" reference="prop:projective_funk"} and using the notation therein, the corresponding cotangent balls differ by a shift of $w=\frac{\theta}{\langle x,\theta\rangle}-\frac{e_{n+1}}{x_{n+1}}$. To represent this translation in the fixed affine hyperplane $\{y_{n+1}=1\}$, we put $\hat y=(y,1)$ , $x=\frac{\hat y}{|\hat y|}$, $\theta=(\alpha, \beta)\in \mathbb{R}^n\oplus \mathbb{R}$. Now apply $(d_xA^*)^{-1}=x_{n+1}\pi_n$ to $w$ to get $$s(y):=(d_xA^*)^{-1}w=\frac{x_{n+1}} {\langle x,\theta\rangle}\pi_n(\theta)=\frac{1}{\langle y, \alpha\rangle +\beta}\alpha.$$ Considered as a $1$-form, $s(y)$ is exact: $$s(y)=d\log(\langle y,\alpha\rangle+\beta),$$ concluding the proof. Thus the exact co-nomadic class of the Funk metric is projectively invariant.
