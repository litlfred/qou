---
abstract: |
  Let $R$ be a commutative ring with unity and let $A$ be a not necessarily commutative $R$-algebra which is free as an $R$-module. If $I$ is an ideal in $A$, one can ask when $A/I$ is also free as an $R$-module. We show that if $A$ has an admissible system and $I$ has a unital Gröbner basis then $A/I$ is free as an $R$-module. We prove a version of Buchberger’s theorem over $R$ and, as a corollary, we obtain a Gröbner basis proof of the Poincaré–Birkhoff–Witt Theorem over a commutative ground ring.
author:
- Frederick Leitner
bibliography:
- references.bib
date: 2004-10-14
title: Unital Gröbner Bases over Arbitrary Commutative Ground Rings
---

<div class="center">

  
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose,  
provided appropriate credit is given, a link to the license is provided,  
and any changes made are indicated.

</div>

**Proof-status key**

|                                               |                           |                                                   |                              |
|:---------------------------------------------:|:--------------------------|:-------------------------------------------------:|:-----------------------------|
|   <span style="color: ForestGreen"></span>    | Fully proved (sorry-free) | <span style="color: BurntOrange">$\forall$</span> | Stated in Lean (has `sorry`) |
| <span style="color: OliveGreen">-0.3em</span> | Merged into Mathlib       |   <span style="color: BrickRed">$\times$</span>   | Not ready to formalize       |

# Unital Gröbner Bases over Arbitrary Commutative Ground Rings

## Introduction

There have been several generalizations of Gröbner basis theory, coming in one of two flavors: noncommutative theory and theories for working over special ground rings, e.g. Euclidean domains, PID’s or UFD’s. Over a field, one of the main uses of a Gröbner basis is to find a basis for the quotient of an algebra $A$ by a (left or two-sided) ideal $I$.

A consideration of the standard examples shows that the ground field $k$ never enters into the picture. Specifically, one does not need to invert any constants, and this leads to the notion of a *unital Gröbner basis*. We view the inability of classical Gröbner basis techniques to apply to these mild generalizations as an unsatisfactory state of affairs.

## Monomials, orderings, and admissible systems

<div id="def:monomial-basis" class="definition">

**Definition 1.1** (Monomials, monomial bases, and leading terms). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.GrobnerShirshov.AlgElement) Throughout, $R$ is a commutative ring with unity and $A$ is an $R$-algebra without quasi-zeros (i.e. elements $a \in A$ such that $bac = 0$ for all $b, c \in A$ not both $1$).*

*Choose a set of algebra generators $A = R\langle x_i \mid i \in \Lambda\rangle$ for some index set $\Lambda$.*

***Monomials.** Let $\alpha = \alpha_1 \alpha_2 \cdots \alpha_n$ be a finite-length word in $\Lambda$. A *monomial* in $A$ is the ordered product*

*$$x_\alpha := x_{\alpha_1} \cdot x_{\alpha_2} \cdots x_{\alpha_n}.$$*

***Monomial basis.** Suppose $A$ is free as an $R$-module. We say $A$ has a *monomial basis* $B$ subordinate to $\Lambda$ if $B$ is a subset of all finite-length words in $\Lambda$ such that*

*$$A = R\{x_\beta \mid \beta \in B\}.$$*

*We identify $\beta$ with $x_\beta$ to simplify notation.*

***Leading terms.** Assume $B$ is well-ordered by $<$. For $f \in A$, write $f$ uniquely as*

*$$f = c_1 b_1 + c_2 b_2 + \cdots + c_n b_n,
  \qquad c_i \in R^* := R \setminus \{0\},\;
  b_i \in B,\;
  b_1 > b_2 > \cdots > b_n.$$*

*Then define:*

- *$\mathrm{LM}(f) := b_1$ (the *leading monomial*),*

- *$\mathrm{LC}(f) := c_1$ (the *leading coefficient*),*

- *$\mathrm{LT}(f) := \mathrm{LC}(f)\,\mathrm{LM}(f)$ (the *leading term*).*

</div>

<div id="def:admissible-system" class="definition">

**Definition 1.2** (Monomial ordering and admissible system). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.GrobnerShirshov.AdmissibleOrder)*

*A *monomial ordering* for a [monomial basis](#def:monomial-basis) $B$ of an algebra $A$ is a well-ordering $<$ on $B$ such that for $b, b', r, s \in B$:*

1.  *If $b < b'$ then $r \cdot b \cdot s < r \cdot b' \cdot s$ whenever $r \cdot b \cdot s \neq 0$ and $\mathrm{LM}(r \cdot b' \cdot s) \neq 0$.*

2.  *If $b' = \mathrm{LM}(r \cdot b \cdot s) \neq 0$ with $r$ or $s \neq 1$, then $b < \mathrm{LM}(b')$.*

*If $B$ admits a monomial ordering $<$, then the pair $(B, <)$ is an *admissible system*.*

***Divisibility.** If $(B, <)$ is an admissible system and $0 \neq f \in A$, we say $\beta \in B$ *divides* $f$ (written $\beta \mid f$) if there exist $u, v \in B$ and $\lambda \in R^*$ such that*

*$$\lambda\,\mathrm{LT}(u \cdot \beta \cdot v) = \mathrm{LT}(f).$$*

</div>

<div id="def:remainder-module" class="definition">

**Definition 1.3** (Remainder modules \$O(I)\$ and \$\\}tilde{O}(I)\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.GrobnerShirshov.isNormalForm)*

*Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module and without quasi-zeros, $(B, <)$ an [admissible system](#def:admissible-system) on $A$, and $I \subseteq A$ a subset.*

*Define the $R$-submodule $O(I)$ of $A$ as the $R$-submodule spanned by the set*

*$$o(I) := \bigl\{\lambda\beta \;\big|\;
    \lambda \in R^*,\; \beta \in B,\;
    \forall\, h \in I\colon \mathrm{LT}(h) \neq \lambda\beta\bigr\}.$$*

*Define also the $R$-module $\tilde{O}(I)$ as the $R$-submodule spanned by*

*$$\tilde{o}(I) := B \setminus \{\mathrm{LM}(h) \mid h \in I\}.$$*

*Clearly $\tilde{O}(I)$ is a free $R$-module.*

</div>

## Division algorithm and Gröbner bases

<div id="def:division-algorithm" class="definition">

**Definition 1.4** (Division algorithm). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.GrobnerShirshov.reduce)*

***Input:** $R$ a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module and without quasi-zeros, $(B, <)$ an [admissible system](#def:admissible-system) on $A$, a subset $I \subseteq A$, and $f \in A$.*

***Output:** $\tilde{f} \in I$ and $r \in O(I)$ (the *remainder* of $f$ on division by $I$) so that $f = r + \tilde{f}$.*

1.  *Set $i := 0$, $f_0 := f$.*

2.  ***While** $f_i \neq 0$:*

    - *Set $i := i + 1$.*

    - ***If** there is no $h \in I$ with $\mathrm{LT}(h) \mid f$: set $r_i := \mathrm{LT}(f)$ and $f_i := f_{i-1} - r_i$.*

    - ***Else**: choose $h_i \in I$ with $0 \neq \mathrm{LT}(h_i) \mid f_{i-1}$; choose $\lambda_i \in R^*$, $u_i, v_i \in B$ so that $\lambda_i \mathrm{LT}(u_i \cdot h_i \cdot v_i) = \mathrm{LT}(f_{i-1})$; set $f_i := f_{i-1} - \lambda_i u_i \cdot h_i \cdot v_i$ and $r_i := 0$.*

3.  *Return $r := \sum_i r_i$ and $\tilde{f} := \sum_i \lambda_i u_i \cdot h_i \cdot v_i = f - r$.*

*Because we do not specify how to choose $h_i$ (nor $u_i, v_i$), the output is not in general unique.*

</div>

<div id="def:groebner-basis" class="definition">

**Definition 1.5** (Gröbner basis and unital Gröbner basis). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.GrobnerShirshov.IsGrobnerShirshovBasis)*

*Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module and without quasi-zeros, $(B, <)$ an [admissible system](#def:admissible-system), and $I$ a two-sided ideal in $A$.*

***Gröbner basis.** A set of generators $G = \{g_\gamma \mid \gamma \in \Gamma\}$ for $I$ is a *Gröbner basis* with respect to $(B, <)$ if for every $h \in I$ we have a representation*

*$$h = \sum_{k \in K} \lambda_k\, u_k \cdot g_{\gamma_k} \cdot v_k$$*

*for $K$ an index set, $\gamma_k \in \Gamma$, $\lambda_k \in R^*$, $u_k, v_k \in B$, such that $\mathrm{LM}(u_k \cdot g_{\gamma_k} \cdot v_k) \leq \mathrm{LM}(h)$ whenever $u_k \cdot g_{\gamma_k} \cdot v_k \neq 0$.*

***Unital.** A subset $G \subseteq A$ is *unital* if:*

1.  *For all $\gamma \in \Gamma$: $\mathrm{LC}(g_\gamma) \in R^\times$ (the units of $R$).*

2.  *For all $\gamma \in \Gamma$ and $\alpha, \beta \in B$: $\mathrm{LC}(\alpha \cdot g_\gamma \cdot \beta) \in R^\times$ whenever $\alpha \cdot g_\gamma \cdot \beta \neq 0$.*

***$S$-polynomial.** For $f, f' \in A$, an *$S$-polynomial* is constructible about $f$ and $f'$ if there exist $u, u', v, v' \in B$, $\lambda, \lambda' \in R^*$ such that*

*$$\lambda\,\mathrm{LT}(u \cdot \mathrm{LT}(f) \cdot v)
  = \lambda'\,\mathrm{LT}(u' \cdot \mathrm{LT}(f') \cdot v').$$*

*In this case,*

*$$S(f, f') := \lambda\, u \cdot f \cdot v
    - \lambda'\, u' \cdot f' \cdot v'.$$*

*If the ground ring is a field, every Gröbner basis is automatically unital. If $B$ is closed under multiplication, condition (b) follows from (a).*

</div>

## Main results

<div id="lem:generator-choice" class="lemma">

**Lemma 1.6** (Generator choice in the division algorithm).

*Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module, $(B, <)$ an [admissible system](#def:admissible-system), and let $I$ be a two-sided ideal of $A$ generated by a unital [Gröbner basis](#def:groebner-basis) $G = \{g_\gamma \mid \gamma \in \Gamma\}$.*

*Then in the [division algorithm](#def:division-algorithm), we may choose $h_i \in I$ so that $h_i = g_{\gamma_i}$ for some $\gamma_i \in \Gamma$.*

</div>

<div class="proof">

*Proof.* <span id="prf:generator-choice" label="prf:generator-choice"></span>

Set $h := h_i$, $f := f_i$. Since $G$ is a Gröbner basis, write

$$h = \sum_{k \in K} \lambda_k\, u_k \cdot g_{\gamma_k} \cdot v_k$$

with $\lambda_k \in R^*$, $u_k, v_k \in B$, $\gamma_k \in \Gamma$. Set $\alpha := \mathrm{LM}(h)$.

Choose a representation with $\alpha$ minimal, and define $T := \{k \in K \mid \mathrm{LM}(u_k \cdot g_{\gamma_k} \cdot v_k) = \alpha\}$. Further choose so that $|T|$ is minimal. If $|T| = 1$, we are done.

Otherwise, let $k_1 \neq k_2 \in T$ and set $c_{k_i} := \mathrm{LC}(u_{k_i} \cdot g_{\gamma_{k_i}} \cdot v_{k_i})$. By unitality, $c_{k_i} \in R^\times$, so we may form the $S$-polynomial

$$S := \lambda_{k_2}\,\frac{c_{k_2}}{c_{k_1}}\,
    u_{k_1} \cdot g_{\gamma_{k_1}} \cdot v_{k_1}
    - \lambda_{k_2}\, u_{k_2} \cdot g_{\gamma_{k_2}} \cdot v_{k_2}.$$

Substituting back, either all terms with leading monomial $\alpha$ cancel (contradicting minimality of $\alpha$) or we reduce $|T|$ by at least one (contradicting minimality of $|T|$). Thus $|T| = 1$. ◻

</div>

<div id="thm:unital-groebner-decomposition" class="theorem">

**Theorem 1.7** (Free module decomposition via unital Gröbner bases).

*Let $R$ be a commutative ring with unity. Let $A$ be an $R$-algebra which is free as an $R$-module and without quasi-zeros. Let $(B, <)$ be an [admissible system](#def:admissible-system) on $A$ and let $I$ be a two-sided ideal of $A$ with a unital [Gröbner basis](#def:groebner-basis) $G$. Define $\tilde{O}(G)$ to be the [free $R$-module](#def:remainder-module) spanned by the monomials which do not occur as leading monomials of members of $G$. Then:*

1.  *There is an $R$-module isomorphism $A/I \cong \tilde{O}(G)$ of free $R$-modules.*

2.  *$A = I \oplus \tilde{O}(G)$.*

</div>

<div class="proof">

*Proof.* <span id="prf:unital-groebner-decomposition" label="prf:unital-groebner-decomposition"></span>

Let $f \in A$. The [division algorithm](#def:division-algorithm) writes $f = r + \tilde{f}$ with $r \in O(I)$ and $\tilde{f} \in I$. By [Lemma (generator choice)](#lem:generator-choice), we can take $r \in \tilde{O}(G)$. As $f$ is arbitrary, $A = I + \tilde{O}(G)$.

It remains to show the sum is direct, which follows from uniqueness of $r$. Suppose the division algorithm produces two representations:

$$f = \tilde{f} + r = \tilde{f}' + r'.$$

Then $\tilde{f} - \tilde{f}' \in I$, so $r - r' \in I$. If $r - r' \neq 0$, then by [Lemma (generator choice)](#lem:generator-choice) there exists $g_\gamma \in G$ with $\mathrm{LT}(g_\gamma) \mid (r - r')$. But by construction of $r$ and $r'$, no such $g_\gamma$ exists — contradiction. Thus $r = r'$ and the sum is direct. ◻

</div>

<div id="prop:s-polynomial-decomposition" class="proposition">

**Proposition 1.8** (\$S\$-polynomial decomposition of cancelling sums).

*Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module, $(B, <)$ an [admissible system](#def:admissible-system). Let $\alpha \in B$ and suppose $f_1, \ldots, f_n \in A$ satisfy $\mathrm{LM}(f_i) = \alpha$ and $\mathrm{LC}(f_i) \in R^\times$. If*

*$$f := \sum_i c_i f_i, \qquad c_i \in R^*,$$*

*satisfies $\mathrm{LM}(f) < \alpha$, then we may write*

*$$f = \sum_{i \neq j} d_{i,j}\, S_{i,j}$$*

*where the $S_{i,j}$ are the $S$-polynomials about $f_i$ and $f_j$:*

*$$S_{i,j} := \frac{1}{a_i} f_i - \frac{1}{a_j} f_j,
  \qquad a_i := \mathrm{LC}(f_i),\; a_j := \mathrm{LC}(f_j) \in R^\times.$$*

</div>

<div class="proof">

*Proof.* <span id="prf:s-polynomial-decomposition" label="prf:s-polynomial-decomposition"></span>

Because all terms involving $\alpha$ cancel, $\sum_i c_i = 0$. Then:

$$f = c_1 a_1 \cdot \frac{1}{a_1} f_1 + \cdots + c_n a_n \cdot \frac{1}{a_n} f_n.$$

Telescoping:

$$f = c_1 a_1\, S_{1,2}
    + (c_1 a_1 + c_2 a_2)\, S_{2,3}
    + \cdots
    + (c_1 a_1 + \cdots + c_{n-1} a_{n-1})\, S_{n-1,n}
    + \underbrace{(c_1 a_1 + \cdots + c_n a_n)}_{= 0} \cdot \frac{1}{a_n} f_n,$$

giving the desired result. ◻

</div>

<div id="thm:buchberger" class="theorem">

**Theorem 1.9** (Buchberger’s theorem over commutative rings).

*Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module, $(B, <)$ an [admissible system](#def:admissible-system). Let $I \leq A$ be an ideal generated by a unital set $G := \{g_\gamma \mid \gamma \in \Gamma\}$.*

*Then $G$ is a [Gröbner basis](#def:groebner-basis) for $I$ if and only if all $S$-polynomials for $G$ have zero remainder under the [division algorithm](#def:division-algorithm).*

</div>

<div class="proof">

*Proof.* <span id="prf:buchberger" label="prf:buchberger"></span>

We show that if all $S$-polynomials reduce to zero and $f \in I$, then $f$ has a Gröbner basis representation. Since $G$ generates $I$, choose a representation

$$f = \sum_i h_i \cdot g_{\gamma_i} \cdot h_i', \qquad
  h_i, h_i' \in A,\; \gamma_i \in \Gamma.$$

Expanding in the monomial basis $B$, write $f = \sum_{i,k,k'} c_k c_{k'}' \beta_k \cdot g_i \cdot \beta_{k'}'$.

If for some representation all terms satisfy $\mathrm{LM}(\beta_k \cdot g_i \cdot \beta_{k'}') \leq \mathrm{LM}(f)$, we are done. Otherwise, define $\alpha := \max\{\mathrm{LM}(h_i \cdot g_i \cdot h_i')\}$ with $\alpha > \mathrm{LM}(f)$; choose $\alpha$ minimal over all representations.

Set $T := \{i \mid \mathrm{LM}(h_i \cdot g_i \cdot h_i') = \alpha\}$ and $g := \sum_{i \in T} \mathrm{LT}(h_i) \cdot g_i \cdot \mathrm{LT}(h_i')$. By unitality, the leading coefficients are units, so [Proposition ($S$-polynomial decomposition)](#prop:s-polynomial-decomposition) applies:

$$g = \sum_{i \neq j \in T} d_{i,j}\, S_{i,j}.$$

The $S_{i,j}$ are also $S$-polynomials about $g_i, g_j$; by assumption they reduce to zero, i.e.  
$S_{i,j} = \sum_l \lambda_l^{i,j}\, u_l^{i,j} \cdot g_{l}^{i,j}
\cdot v_l^{i,j}$ with $\mathrm{LM}(S_{i,j}) < \alpha$. Substituting back gives a new representation of $f$ with strictly smaller maximal term — contradiction. ◻

</div>

<div id="cor:pbw" class="corollary">

**Corollary 1.10** (Poincaré–Birkhoff–Witt theorem over commutative rings).

*Let $\mathfrak{g}$ be a Lie algebra over $R$, a commutative ring with unity, with Lie bracket $[\,{,}\,]_{\mathfrak{g}}$. Then the universal enveloping algebra*

*$$U\mathfrak{g} = T\mathfrak{g} / J, \qquad
  J = \bigl(xy - yx - [x,y]_{\mathfrak{g}}
    \;\big|\; x, y \in \mathfrak{g} \hookrightarrow T\mathfrak{g}\bigr)$$*

*is isomorphic as an $R$-module to $S\mathfrak{g}$, the symmetric algebra on $\mathfrak{g}$.*

*In particular, if $R$ is a $\mathbb{Q}$-algebra, we obtain a Gröbner basis proof of the equivalence of the category of (finite-dimensional) Lie algebras over $R$ and (finite-dimensional) smooth formal groups over $R$.*

</div>

<div class="proof">

*Proof.* <span id="prf:pbw" label="prf:pbw"></span>

Choose a well-ordered basis $\{x_i \mid i \in I\}$ for $\mathfrak{g}$. Then $T\mathfrak{g}$ has a multiplicative monomial basis consisting of the words of finite length in the $x_i$’s with the graded lexicographic ordering. The symmetric algebra $S\mathfrak{g}$ has a basis of words written in non-decreasing order.

The ideal $J$ is generated by

$$G := \{g_{i,j} := x_i x_j - x_j x_i - [x_i, x_j]_{\mathfrak{g}}
    \mid x_i > x_j\}.$$

The argument that $G$ is a Gröbner basis is exactly as in the classical setting, using [Buchberger’s theorem](#thm:buchberger). As the leading terms $\mathrm{LT}(g_{i,j}) = x_i x_j$ are monic and the basis is multiplicative, $G$ is a *unital* Gröbner basis. The corollary then follows from the [main decomposition theorem](#thm:unital-groebner-decomposition). ◻

</div>
