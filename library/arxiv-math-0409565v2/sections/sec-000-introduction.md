---
doc_id: arxiv-math-0409565v2
doc_title: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings"
section_id: sec-000-introduction
section_title: "Introduction."
section_number: null
pages: 1-10
source_pdf: 0409565v2.pdf
source_sha256: 236704063f12c05e
doc_brief: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings — Let R be a commutative ring with unity and a let A be a not necessarily commutative R-algebra which is free as an R-module."
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.893
---
There have been several generalizations of Gröbner basis theory, coming in one of two flavors: noncommutative theory and theories for working over special ground rings, e.g. Euclidean domains, PID's or UFD's. For an overview of the theory of such rings see [@adams]. Over a field, one of the main uses of a Gröbner basis is to find a basis for the quotient of an algebra $A$ by a (left or two-sided) ideal $I$. Let us consider two examples for $k$ a (commutative) field (with unity) whose quotient algebras can be readily described through the known Gröbner basis theory.

::: eExample
Let $A$ be the polynomial algebra $k[x_1,\cdots,x_n]$ and consider the ideal $m=(x_1,\cdots,x_n)$. Taking a graded lexicographic ordering on $A$ with $x_i < x_j$ if $i < j$, $m^2$ has a Gröbner basis given by $\{x_i x_j\}$. Thus the quotient $A/m^2$ is an $n+1$-dimensional $k$-vector space with a basis given by: $$A/m^2=k\{1,x_1,\cdots,x_n \}$$

If ${\mathfrak{g}}$ is a lie algebra with lie bracket $[ \ , \ ]_{{\mathfrak{g}}}$ over $k$ then one forms the universal enveloping algebra ${\mathfrak{U}}{\mathfrak{g}}$ as the quotient of the tensor or free algebra $T{\mathfrak{g}}$ on ${\mathfrak{g}}$ by the two sided ideal $J$: $$J=\left( xy-yx -[x,y]_{{\mathfrak{g}}} \ | x,y \in {\mathfrak{g}}\hookrightarrow T{\mathfrak{g}}\right)$$ If one chooses a total ordering $<$ on the index set $I$ for a $k$-basis ${\mathfrak{g}}=k<x_i | i \in I>$ then a Gröbner basis argument yields the Poincare-Birkhoff-Witt(PBW) theorem which says that ${\mathfrak{U}}{\mathfrak{g}}$ has a basis of non-decreasing words ([@Mora] [@DeGraaf]).
:::

A consideration of the first example shows the fact that $k$ was a field was not important -- one would have a similar statement with the integers ${\mathbb{Z}}$, though not through Gröbner basis techniques. The same holds for the second example if we replace $k$ by an arbitrary (commutative) ring. However, in this more general setting, one cannot make use of Gröbner basis techniques -- one must prove this by "ad-hoc" methods as in [@Serre]. However, these arguments bear a close relation to those used in the Gröbner basis theory. We view the inability of Gröbner basis techniques to apply to these mild generalizations as an unsatisfactory state of affairs.

If one regards the above two examples closely, one sees that the ground field $k$ never enters into the picture. Specifically, one does not need to invert any constants, and this leads to the notion of a *unital Gröbner basis*. We will prove the following:

::: Theorem
[]{#thm label="thm"} Let $R$ be a commutative algebra with unity. Let $A$ be an $R$-algebra which is free as an $R$-module and without quasi-zeros. Let $({\mathcal{B}},<)$ be an admissible system on $A$ and let $I$ be a two-sided ideal of $A$ with a unital Gröbner basis ${\mathcal{G}}$. Define $\tilde{O}({\mathcal{G}})$ to be the free $R$-module spanned by the monomials which do not occur as leading monomials of members of ${\mathcal{G}}$. Then:

1.  []{#thm1 label="thm1"} There is a $k$-module isomorphism $A/I\simeq \tilde{O}({\mathcal{G}})$ of free $R$-modules.

2.  []{#thm2 label="thm2"} $A=I\oplus \tilde{O}({\mathcal{G}})$
:::

For the case of a left ideal $I$, or for the case where $A$ has quasi-zeros, one only need to combine the techniques in [@Li] with ours. As a corollary we obtain the PBW theorem over an arbitrary commutative ring with unity. In particular, if $R$ is a ${\mathbb{Q}}$-algebra we have a Gröbner basis proof of the equivalence of the category of (finite dimensional) lie algebras over $R$ and (finite dimensional) smooth formal groups over $R$.

# Unital Gröbner Bases.

Throughout this section $R$ is a commutative ring with unity and $A$ an $R$-algebra with no quasi-zeros, i.e. elements $a\in A$ such that for all $b,c \in A$ not both $1$ one has $bac=0$. For brevity, we only state and prove the results in the case of a two-sided ideal. We take time to fix notation, following closely that of ([@Li]),

::: eDefinition
Let $A$ be an $R$-algebra with multiplication $\cdot$ (and without quasi-zeros). Choose a set of (algebra) generators $A=R\langle x_i | i\in \Lambda\rangle$ for some index set $\Lambda$.

Let $\alpha$ be a finite length word in $\Lambda$, i.e. an ordered expression: $$\alpha=\alpha_1 \alpha_2 \cdots \ \alpha_n \ \ \ \alpha_i \in \Lambda$$ Then a *monomial* in $A$ is the ordered product: $$x^{\alpha}:= x_{\alpha_1} \cdot x_{\alpha_2} \cdots \ x_{\alpha_n}$$

Suppose that $A$ is a free $R$-module. We say that $A$ has a *monomial basis ${\mathcal{B}}$ sub-ordinate to $\Lambda$* if ${\mathcal{B}}$ is a subset of all words of finite length in $\Lambda$ such that $A$ has an $R$-basis: $$A=R\{ x^{\beta} \ | \ \beta \in {\mathcal{B}}\}$$ We identify $\beta$ with $x^{\beta}$ to simplify notation.

Assume that ${\mathcal{B}}$ is well ordered by $<$. Let $f\in A$, then we may write $f$ uniquely as the finite sum: $$f= c_1 b_1 + c_2 b_2 \cdots + c_n b_n \mbox{ for }
                    c_i \in R^{\ast}:=R\setminus\{0\} 
                \mbox{ and }b_i \in {\mathcal{B}}.$$ such that $b_1 > b_2 > \cdots > b_n$. Then the *leading (or head) monomial of $f$ with respect to ${\mathcal{B}}$ and $<$* is defined as: $$\mathbf{LM}_{{{}}}\left({f}\right) := \mathbf{LM}_{{{<}}}\left({f}\right):= b_1$$ i.e. the largest basis element appearing. The *leading (or head) coefficient of $f$ with respect to ${\mathcal{B}}$ and $<$* is defined as: $$\mathbf{LC}_{{{}}}\left({f}\right) := \mathbf{LC}_{{{<}}}\left({f}\right):= c_1$$ while the *leading (or head) term of $f$ with respect to ${\mathcal{B}}$ and $<$* is defined as: $$\mathbf{LT}_{{{}}}\left({f}\right) := \mathbf{LT}_{{{<}}}\left({f}\right):= \mathbf{LC}_{{{}}}\left({f}\right)\mathbf{LM}_{{{}}}\left({f}\right)$$

A *monomial ordering* for a basis ${\mathcal{B}}$ of an algebra $B$ is a well ordering $<$ on ${\mathcal{B}}$ such that for $b,b',r,s \ \in {\mathcal{B}}$ we have:

1.  if $b < b'$ then $r\cdot b\cdot s < r  \cdot b' \cdot s$ whenever: $$r\cdot b \cdot s \mbox{ and } \mathbf{LM}_{{{}}}\left({r \cdot b' \cdot s}\right) \ne 0$$

2.  if $b' =\mathbf{LM}_{{{}}}\left({r \cdot b \cdot s}\right)\ne 0$ with $r \mbox{ or } s \ne 1$ then $b < \mathbf{LM}_{{{}}}\left({b'}\right)$

If ${\mathcal{B}}$ admits a monomial ordering $<$, then the pair $({\mathcal{B}},<)$ is an *admissible system*.

If $(B,<)$ is an admissible system, and $0\ne f\in A$, then we say that $\beta \in {\mathcal{B}}$ divides $f$ ( and write $\beta|f$) if there are $u,v\in {\mathcal{B}}$ and $\lambda \in R^{\ast}$ such that: $$\lambda \mathbf{LT}_{{{}}}\left({u\cdot \beta \cdot v}\right) = \mathbf{LT}_{{{}}}\left({f}\right)$$
:::

We now describe for a subset $I\subseteq A$, $I$ not necessarily an ideal, a "division algorithm." We have put quotations to emphasize that this algorithm does not in general have a meaning. In fact, one may view the statement of (Theorem [\[thm\]](#thm){reference-type="ref" reference="thm"}) as ascribing a meaning to this algorithm when we make the assumption of the existence of a *unital Gröbner basis* for $I$. A second reason for putting this in quotations is that we give no prescription for choosing the elements of $I$ with which to divide. However, this need not be a hindrance and is in fact a benefit in view of (Lemma [\[lem\]](#lem){reference-type="ref" reference="lem"}). We need one more set of definitions at this point:

::: Definition
Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module and without quasi-zeros, $({\mathcal{B}},<)$ an admissible system on $A$, and a subset $I\subseteq A$. Then define a $R$-submodule $O(I)$ of $A$ to be the $R$-submodule spanned by the set: $$o(I) := \{ \lambda \beta \ | \ \lambda \in R^{\ast}, \  \beta \in {\mathcal{B}}, \ \forall h\in I
            \mbox{ we have  }
            \mathbf{LT}_{{{}}}\left({h}\right) \ne \lambda \beta \}$$ We also define the $R$-module $\tilde{O}(I)$ as the $R$-submodule spanned by the set: $$\tilde{o}(I) := {\mathcal{B}}\setminus \{ \mathbf{LM}_{{{}}}\left({h}\right) \ | \ h \in I \}$$ Clearly $\tilde{O}(I)$ is a free $R$-module.
:::

::: algorithmic
$R$ a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module and without quasi-zeros, $({\mathcal{B}},<)$ an admissible system on $A$, a subset $I\subseteq A$, and $f\in A$. $\tilde{f} \in I$ and $r\in O(I)$ the *remainder of $f$ on division by $I$* so that $f=r + \tilde{f}$ $i:=0$ $f_0 := f$. $i:=i+1$ $r_i := \mathbf{LT}_{{{}}}\left({f}\right)$ $f_i := f_{i-1} - r_i$ Choose some $h_i \in I$ such that $0\ne\mathbf{LT}_{{{}}}\left({h_i}\right) | f_{i-1}$ Choose some $\lambda_i \in R^{\ast}$ $u_i,v_i\in {\mathcal{B}}$ so that: $\lambda_i\mathbf{LT}_{{{}}}\left({u_i\cdot h_i \cdot v_i}\right) = \mathbf{LT}_{{{}}}\left({f_{i-1}}\right)$ $f_i := f_{i-1} - \lambda_i u_i\cdot h_i \cdot v_i$ $r_i := 0$ $r:= \sum_{i} r_i$ $\tilde{f}:=\sum_i \lambda_i u_i \cdot h_i \cdot v_i = f - r$
:::

We note that, because we do not specify how to choose the $h_i$ (nor the $u_i$ and $v_i$) we do not in general have a unique output.

::: eDefinition
Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as a $R$-module and without quasi-zeros, and let $({\mathcal{B}},<)$ be an admissible system on $A$.

[]{#gbdef label="gbdef"} Let $I$ be a (two-sided) ideal in $I$. Let $I$ have a set of generators: $${\mathcal{G}}=\{ g_\gamma \ | \ \gamma \in \Gamma \} \mbox{ for some index set } \Gamma$$ Then we say that ${\mathcal{G}}$ is a *Gröbner basis with respect to $({\mathcal{B}},<)$* if for every $h\in I$ we have a representation: $$h = \sum_{k\in K} \lambda_{k} u_{k}\cdot g_{\gamma_k} \cdot v_{k}$$ for $K$ an index set, $\gamma_k \in \Gamma$, $\lambda_{k}\in R^{\ast}$ and $u_{k},v_{k} \in {\mathcal{B}}$ such that $\mathbf{LM}_{{{}}}\left({u_{k}\cdot g_{\gamma_k}\cdot  v_{k}}\right) \le \mathbf{LM}_{{{}}}\left({f}\right)$ whenever $u_{k}\cdot g_{\gamma_k}\cdot v_{k}\ne 0$

We call a subset ${\mathcal{G}}\subseteq A$ *unital* if:

1.  For all $\gamma \in \Gamma$ we have: $$\mathbf{LC}_{{{}}}\left({g_{\gamma}}\right)\in R^{\times}:= \mbox{ units of } R$$

2.  For all $\gamma \in \Gamma$ and for all $\alpha,\beta \in {\mathcal{B}}$ we have $$\mathbf{LC}_{{{}}}\left({\alpha\cdot g_{\gamma} \cdot \beta}\right) \in R^{\times} \mbox{ whenever } \alpha\cdot g_{\gamma} \cdot \beta \ne 0$$

For $f,f'\in A$ we say that an *S-polynomial is constructible about $f$ and $g$* if there is some $u,u',v',v' \in {\mathcal{B}}$, $\lambda,\lambda' \in R^{\ast}$ such that: $$\lambda \mathbf{LT}_{{{}}}\left({u\cdot \mathbf{LT}_{{{}}}\left({f}\right)\cdot v}\right) =
                \lambda' \mathbf{LT}_{{{}}}\left({u'\cdot \mathbf{LT}_{{{}}}\left({f'}\right)\cdot v'}\right)$$ In which case we write: $$S:=S(f,f'):= \lambda u \cdot f \cdot v - \lambda' u' \cdot f' \cdot v'$$ We say that $S$ is an *$S$-polynomial about $f$ and $f'$*. The choices of $u,u',v,v'$ are not in general unique.
:::

The extra conditions of a Gröbner basis being unital are not that strong: If the ground ring is a field, then a Gröbner basis is automatically a unital Gröbner basis. If ${\mathcal{B}}$ is closed under multiplication, then the third condition follows if the second condition holds. We also note that the construction of a $S$-polynomial ensures that: $$\mathbf{LM}_{{{}}}\left({S}\right) < \mathbf{LM}_{{{}}}\left({u\cdot \mathbf{LM}_{{{}}}\left({f}\right)\cdot v}\right) = \mathbf{LM}_{{{}}}\left({u'\cdot \mathbf{LM}_{{{}}}\left({f'}\right)\cdot v'}\right)$$

::: Lemma
[]{#lem label="lem"} Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module, $({\mathcal{B}},<)$ an admissible system on $A$, and let $I$ be a two sided ideal of $A$ which is generated by a unital Gröbner basis: $${\mathcal{G}}= \{ g_{\gamma} \ | \ \gamma \in \Gamma \}.$$ Then in the division algorithm, we may choose $h_i \in I$ so that $h_i = g_{\gamma_i}$ for some $\gamma_i \in \Gamma$.
:::

::: proof
*Proof.* Let us set $h:=h_i$, $f:=f_i$ to stop the proliferation of subscripts. Then since ${\mathcal{G}}=\{ g_{\gamma} \ | \ \gamma \in {\mathcal{G}}\}$ is a Gröbner basis, we may write: $$\label{eqn}
            h=\sum_{k \in K} \lambda_k u_k \cdot g_{\gamma_k} \cdot v_k$$ with $\lambda_k \in R^{\ast}$, $u_k, v_k \in {\mathcal{B}}$ and $\gamma_k\in \Gamma$. Denote: $$\alpha := \mathbf{LM}_{{{}}}\left({h}\right)$$ As we are free to choose our representation (Equation [\[eqn\]](#eqn){reference-type="ref" reference="eqn"}) of $h$ as we wish, we may choose one so that $\alpha$ is minimal with respect to the ordering $<$. Denote: $$T:= \{ k \in K \ | \ \mathbf{LM}_{{{}}}\left({u_k \cdot g_{\gamma_k} \cdot v_k}\right) = \alpha \}$$ We can further choose a representation of $h$ so that $|T|$ is minimal. If $|T| =  1$ we are done. Otherwise, let $k_1\ne k_2\in T$, and denote $c_{k_i}:= \mathbf{LC}_{{{}}}\left({u_{k_i} \cdot g_{\gamma_{k_i}}\cdot v_{k_i}}\right)$. By the assumption that ${\mathcal{G}}$ was a unital Gröbner basis, we have that $c_{k_i} \in R^{\times}$ so that we may form the $S$-polynomial: $$S:=\lambda_{k_2}\frac{c_{k_2}}{c_{k_1}} u_{k_1}\cdot g_{\gamma_{k_1}}\cdot v_{k_1}
            -\lambda_{k_2} u_{k_2}\cdot g_{\gamma_{k_2}}\cdot v_{k_2}$$ Then we have: $$\begin{aligned}
            \lefteqn{h= 
                \lambda_{k_1} u_{k_1}\cdot g_{\gamma_{k_1}}\cdot u_{k_1}
                +\lambda_{k_2} u_{k_2}\cdot g_{\gamma_{k_2}}\cdot u_{k_2}
                + \sum_{k\ne k_1,k_2} \lambda_{k} u_{k}\cdot g_{\gamma_{k}}\cdot u_{k}}
            \\
            &=&
                \lambda_{k_1} u_{k_1}\cdot g_{\gamma_{k_1}}\cdot u_{k_1}
                + \left(  \begin{array}{c}
                    \lambda_{k_2}\frac{c_{k_2}}{c_{k_1}} u_{k_1}\cdot g_{\gamma_{k_1}}\cdot v_{k_1} \\
                    -\lambda_{k_2}\frac{c_{k_2}}{c_{k_1}} u_{k_1}\cdot g_{\gamma_{k_1}}\cdot v_{k_1}
                      \end{array}
                \right)
                +\lambda_{k_2} u_{k_2}\cdot g_{\gamma_{k_2}}\cdot u_{k_2}
            \\
            &&
                + \sum_{k\ne k_1,k_2} \lambda_{k} u_{k}\cdot g_{\gamma_{k}}\cdot u_{k}
            \\
            &=&
            \left(\lambda_{k_1} -\lambda_{k_2}\frac{c_{k_2}}{c_{k_1}}\right)u_{k_1}\cdot g_{\gamma_{k_1}} \cdot v_{k_1}
            -S 
                + \sum_{k\ne k_1,k_2} \lambda_{k} u_{k}\cdot g_{\gamma_{k}}\cdot u_{k}
        
\end{aligned}$$

We have two possibilities. The first is that we may have succeeded in canceling all terms with leading monomial $\alpha$, which contradicts the minimality of $\alpha$. Otherwise, as $\mathbf{LM}_{{{}}}\left({S}\right) < \alpha$, we have written $h$ with no more than $|T|-1$ terms containing $\alpha$, contradicting the minimality of $T$. Thus we conclude that for such a minimal representation we must have $|T|=1$ as desired. ◻
:::

Now we may proceed with the proof of our theorem.

::: proof
*Proof.* (Theorem [\[thm\]](#thm){reference-type="ref" reference="thm"}) Let $f$ be an element of $A$. Then the division algorithm allows us to write: $$f = r+ \tilde{f}$$ with $r\in O(I)$ and $\tilde(f) \in I$. By (Lemma [\[lem\]](#lem){reference-type="ref" reference="lem"}) we see that we can take $r \in \tilde{O}({\mathcal{G}})$. As $f$ is arbitrary in $A$, we then have $$A = I + \tilde{O}({\mathcal{G}})$$ The theorem will follow if we can show that this sum is direct, which in turn will follow from showing that $r$ is unique. So suppose that the division algorithm produces two representations for $f$: $$f = \tilde{f} + r = \tilde{f}' + r'$$ Then we have $\tilde{f}-\tilde{f'} \in I$ so that $r-r' \in I$. Now assume that $r-r'\ne 0$, then (Lemma [\[lem\]](#lem){reference-type="ref" reference="lem"}) shows that if there is some $h\in I$ such that $\mathbf{LT}_{{{}}}\left({h}\right) | r - r'$ then there is some $g_{\gamma} \in {\mathcal{G}}$ such that $\mathbf{LT}_{{{}}}\left({g_{\gamma}}\right) | r- r'$. But then, by construction of $r$ and $r'$, we know that there is no such $g_{\gamma}$ and we will have a contradiction by taking $h = r - r'$. ◻
:::

::: Proposition
[]{#prop label="prop"} Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module, $({\mathcal{B}},<)$ an admissible system on $A$. Let $\alpha \in {\mathcal{B}}$ and suppose that $f_1, \cdots,f_n \in A$ satisfy $\mathbf{LM}_{{{}}}\left({f_i}\right) = \alpha$ and $\mathbf{LC}_{{{}}}\left({f_i}\right) \in R^{\times}$. Then if: $$f:= \sum_{i} c_i f_i \ \ \ c_i \in R^{\ast}$$ satisfies $\mathbf{LM}_{{{}}}\left({f}\right) < \alpha$ then we may write: $$f = \sum_{i\ne j} d_{i,j} S_{i,j}$$ where the $S_{i,j}$ are the $S$-polynomials about $f_i$ and $f_j$ given by: $$S_{i,j} := \frac{1}{a_i} f_i - \frac{1}{a_j} f_j \ \ \ a_i := \mathbf{LC}_{{{}}}\left({f_i}\right),a_j:=\mathbf{LC}_{{{}}}\left({f_j}\right) \in R^{\times}$$
:::

::: proof
*Proof.* Because we have a cancellation of the terms of $f_i$ involving $\alpha$ we have that $\sum_{i} c_i = 0$. Then: $$\begin{aligned}
        \lefteqn{f= c_1 f_1 + \cdots + c_n f_n} \\
        &=& c_1 a_1 \left(\frac{1}{a_1}f_1\right) + \cdots + c_n a_n\left(\frac{1}{a_n} f_n\right) \\
        &=& c_1 a_1 \left( \frac{1}{a_1} f_1 - \frac{1}{a_2} f_2\right) + (c_1 a_1 + c_2 a_2)\left(\frac{1}{a_2}f_2 - \frac{1}{a_3} f_3\right)
            + \cdots \\
        && + ( c_1 a_1 + \cdots c_{n-1} a_{n-1})\left(\frac{1}{a_{n-1}}f_{n-1} - \frac{1}{a_n} f_n\right)
            + (c_1 a_1 + \cdots c_n a_n)\frac{1}{a_n} f_n 
        \\
        & = & 
           c_1 a_1 S_{1,2} + (c_1 a_1 + c_2 a_2) S_{2,3} + \cdots 
        \\
        & & 
            +(c_1 a_1 + \cdots + c_{n-1} a_{n-1}) S_{n-1,n} + 0 \frac{1}{a_n} f_n
    
\end{aligned}$$ which gives the desired result. ◻
:::

::: Theorem
[]{#buch label="buch"} Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an $R$-module, $({\mathcal{B}},<)$ an admissible system on $A$. Let $I\le A$ be an ideal generated by a unital set: $${\mathcal{G}}:=\{ g_{\gamma} \ | \ \gamma \in \Gamma \}$$ for some index set $\Gamma$. Then ${\mathcal{G}}$ is a Gröbner basis for $I$ if and only if all $S$-polynomials for ${\mathcal{G}}$ have zero remainder under the division algorithm.
:::

::: proof
*Proof.* We show that if all $S$-polynomials reduce to zero and $f\in  I$ then $f$ has a Gröbner basis representation -- i.e a representation satisfying (Definition [\[gbdef\]](#gbdef){reference-type="ref" reference="gbdef"}). As ${\mathcal{G}}$ generates $I$ we may choose a representation of $f$ as: $$\label{eqnREP}
        f= \sum_{i} h_i \cdot g_{\gamma_i} \cdot h_i ' \ \ \ h_i, \ h_i'\in A \ \ \ \gamma_i \in \Gamma$$ As $A$ has an $R$-basis given by ${\mathcal{B}}$ then we may write $h_i=\sum_{k\in K} c_k \beta_k$, $h_i=\sum_{k'\in K'} c'_{k'} \beta'_{k'}$ with $c_k, c'_{k'} \in R^{\ast}$ and $\beta_k, \beta'_{k'} \in {\mathcal{B}}$, so that we have: $$f= \sum_{i,k,k'} c_k c'_{k'} \beta_k \cdot g_i \cdot \beta'_{k'}$$ If for some representation of $f$ as in (Equation [\[eqnREP\]](#eqnREP){reference-type="ref" reference="eqnREP"}) we have for all $\beta_k\cdot g_i \cdot \beta'_{k'} \ne 0$ that $\mathbf{LM}_{{{}}}\left({\beta_k\cdot g_i \cdot \beta'_{k'}}\right) \le \mathbf{LM}_{{{}}}\left({f}\right)$ then we are done. Otherwise, let us suppose that for all such representations of $f$ we have the maximal term appearing $\alpha:= \max{\{\mathbf{LM}_{{{}}}\left({h_i\cdot g_i \cdot h'_{i}}\right)\}}$ is such that $\alpha > \mathbf{LM}_{{{}}}\left({f}\right)$. Over all such representations we may choose one so that $\alpha$ is minimal. We will now produce a new representation for $f$ whose corresponding maximal term is strictly less than $\alpha$, thereby obtaining a contradiction. To this end, let us define $T:=\{ i | \mathbf{LM}_{{{}}}\left({h_i\cdot g_i \cdot h'_{i}}\right) = \alpha \}$ and: $$\begin{aligned}
        g&:= &\sum_{i\in T} \mathbf{LT}_{{{}}}\left({h_i}\right) \cdot g_i \cdot \mathbf{LT}_{{{}}}\left({h_i'}\right)\\
        &=& \sum_{i\in T} \mathbf{LC}_{{{}}}\left({h_i}\right)\mathbf{LC}_{{{}}}\left({h'_i}\right) \mathbf{LM}_{{{}}}\left({h_i}\right) \cdot g_i \cdot \mathbf{LM}_{{{}}}\left({h'_i}\right)
    
\end{aligned}$$ so that each term of $f-g$ has leading monomial less than $\alpha$. As ${\mathcal{G}}$ is assumed to be unital, we have that $a_i:=\mathbf{LC}_{{{}}}\left({\mathbf{LM}_{{{}}}\left({h_i}\right)\cdot g_i \cdot\mathbf{LM}_{{{}}}\left({h'_i}\right)}\right)\in R^{\times}$ so that we may apply to (Proposition [\[prop\]](#prop){reference-type="ref" reference="prop"}) to $g$ and write: $$\label{eqnA}
        g = \sum_{i\ne j \in T} d_{i,j} S_{i,j}$$ where the $S_{i,j}$ are the the $S$-polynomials about $\mathbf{LM}_{{{}}}\left({h_i}\right)\cdot g_i \cdot \mathbf{LM}_{{{}}}\left({h'_i}\right)$ and $\mathbf{LM}_{{{}}}\left({h_j}\right)\cdot g_j\cdot \mathbf{LM}_{{{}}}\left({h'_j}\right)$ given by: $$S_{i,j}:=\frac{1}{a_i}\mathbf{LM}_{{{}}}\left({h_i}\right)\cdot g_i \cdot \mathbf{LM}_{{{}}}\left({h'_i}\right) -
             \frac{1}{a_j}\mathbf{LM}_{{{}}}\left({h_i}\right)\cdot g_j \cdot \mathbf{LM}_{{{}}}\left({h'_j}\right)$$ But then, the $S_{i,j}$'s are also $S$-polynomials about $g_i$ and $g_j$, so that we have, by assumption, that they reduce to zero on the division algorithm, i.e. that: $$\label{eqnB}
       S_{i,j} = \sum_l \lambda_{l_{i,j}} u_{l_{i,j}}\cdot g_{l_{i,j}} \cdot v_{l_{i,j}} \ \ \ u_{l_{i,j}},v_{l_{i,j}}\in {\mathcal{B}}, \ \ 
       \lambda_{l_{i,j}}\in R^{\ast}
       \ \ g_{l_{i,j}} \in {\mathcal{G}}$$ As $\mathbf{LM}_{{{}}}\left({S_{i,j}}\right) < \alpha$ we see that by substituting (Equation [\[eqnB\]](#eqnB){reference-type="ref" reference="eqnB"}) into (Equation [\[eqnA\]](#eqnA){reference-type="ref" reference="eqnA"}) we are able to write $g$, and thus $f$, in the form of (Equation [\[eqnREP\]](#eqnREP){reference-type="ref" reference="eqnREP"}) such that the leading monomial of each term is strictly less than $\alpha$, our desired contradiction. ◻
:::

::: Corolary
Let ${\mathfrak{g}}$ be a lie algebra over $R$, a commutative ring with unity, with lie bracket $[ \ , \ ]_{{\mathfrak{g}}}$. Then: $${\mathfrak{U}}{\mathfrak{g}}= T{\mathfrak{g}}/J \mbox{ where } 
            J=\left( xy-yx -[x,y]_{{\mathfrak{g}}} \ | x,y \in {\mathfrak{g}}\hookrightarrow T{\mathfrak{g}}\right)$$ is isomorphic as an $R$-module to $S{\mathfrak{g}}$, the symmetric algebra on ${\mathfrak{g}}$.
:::

::: proof
*Proof.* Choosing a well ordered basis $\{x_i \ |  \ i \in I \}$ for ${\mathfrak{g}}$ then $T{\mathfrak{g}}$ has a multiplicative monomial basis consisting of the words of finite length in the $x_i$'s with the graded lexicographic ordering. Also $S{\mathfrak{g}}$ has a basis of words of finite length written in non-decreasing order. The ideal $J$ is generated by: $${\mathcal{G}}:= \{ g_{i,j}:=x_i x_j - x_j x_i - [x_i, x_j]_{{\mathfrak{g}}}  \ | \ x_i > x_j \}$$ The argument that ${\mathcal{G}}$ is a Gröbner basis is exactly as in [@Mora] or [@DeGraaf] which makes use of (Theorem [\[buch\]](#buch){reference-type="ref" reference="buch"}). As the leading terms $\mathbf{LT}_{{{}}}\left({g_{i,j}}\right) = x_i x_j$ are monic and the basis is multiplicative we have that ${\mathcal{G}}$ is a unital Gröbner basis. The corollary follows. ◻
:::
