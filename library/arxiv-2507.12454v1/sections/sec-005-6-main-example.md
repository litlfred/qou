---
doc_id: arxiv-2507.12454v1
doc_title: "Cohomology rings of character varieties"
section_id: sec-005-6-main-example
section_title: "Main example"
section_number: 6
pages: 17-20
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.956
doc_brief: "Cohomology rings of character varieties — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of Riemann surfaces"
---
A special case can be worked out in full detail. We take $g=0$, i.e. $C=\mathbb P^1$, and consider the $k+1$-twisted Higgs bundles, so that the Higgs field is a morphism $\mathcal E\to \mathcal E(k-1)$. Equivalently, we may consider $k+1$ marked points without any parabolic structures and conditions on the residue of the Higgs field. The corresponding specialization of the partition function is given by $$\label{eq:omega example}
        \Omega_k(z; q,t) := 
        \sum_{n=0}^\infty \sum_{\lambda\vdash n} \frac{(-1)^{(k+1)|\lambda|}\left(q^{n(\lambda')} t^{n(\lambda)}\right)^{k+1}}{
            \prod_{\square\in\lambda} (q^{a(\square)} - t^{\ell(\square)+1})(q^{a(\square)+1} - t^{\ell(\square)})} z^{n}.$$ We use the variable $z$ to keep track of the rank. In [\[eq:partition function\]](#eq:partition function){reference-type="eqref" reference="eq:partition function"} we didn't need it because the rank of each term can be extracted as the degree of the symmetric function in each set of variables. The first terms of $\Omega$ look as follows: $$1 + \frac{(-1)^{k}}{(1-t)(1-q)} z + \frac{q^{k+1}(1-t^2)-t^{k+1}(1-q^2)}{(q-t)(1-q)(1-q^2)(1-t)(1-t^2)} z^2 + \cdots,$$ and the first terms of its plethystic logarithm read: $$\label{eq:plog example}
        \mathop{\mathrm{Log}}\Omega_k(z; q,t) = -\frac{1}{(1-q)(1-t)}\left((-1)^{k+1} z + 
        z^2 \sum_{\substack{i\geq 0,\; j\geq 0,\; i+j\leq k-2, \\ i+j\equiv k\pmod{2}}} q^i t^j + \cdots\right).$$

In [\[eq:omega example\]](#eq:omega example){reference-type="eqref" reference="eq:omega example"} one can recognize the localization formula for the bundle $O(k)$ on the Hilbert scheme (see [@haiman2002vanishing]). We have $$\Omega_k(z; q,t) = \sum_{n=0}^\infty (-1)^{kn} z^n \chi(\mathrm{Hilb}_n(\mathbb{C}^2), O(k)).$$

Let $R_x=\mathbb{C}[x_1,\ldots,x_n]$, $R_{x,y}=\mathbb{C}[x_1,\ldots,x_n,y_1,\ldots,y_n]$. The symmetric group $S_n$ acts on these, permuting $x_i$ and $y_i$ simultaneously. For an $S_n$-module $M$ we denote by $M^+$ and $M^-$ the subspace of invariant and anti-invariant elements respectively. Notice that $R_{x,y}^-\subset R_{x,y}$ is a module over $R_{x,y}^+$. $(R_{x,y}^-)^k$ denotes the linear span of $k$-fold products of elements of $R_{x,y}^-$ inside $R_{x,y}$. This is also a module over $R_{x,y}^+$. Haiman obtained the following results about the bundles $O(k)$:

::: theorem
For any $k\geq 0$ we have an isomorphism of $R_{x,y}^+$-modules $$\Gamma(\mathrm{Hilb}_n(\mathbb{C}^2), O(k)) \cong (R_{x,y}^-)^k \subset R_{x,y},$$ and the $i$-th cohomology of $O(k)$ vanishes for $i>0$. $(R_{x,y}^-)^k$ is free as a module over $R_x^+$.
:::

For instance, for $k=0$ and $k=1$ we have $$\Gamma(\mathrm{Hilb}_n(\mathbb{C}^2), O) = R_{x,y}^+, \qquad
    \Gamma(\mathrm{Hilb}_n(\mathbb{C}^2), O(1)) = R_{x,y}^-.$$

From this we can obtain the following presentation for the dual of the local cohomology:

::: prop
Let $M_{n,k}:=H^n_L(O(k))\;\check{}\;$. Let $\Delta_x := \prod_{i<j\leq n} (x_i - x_j)$. For $k\geq 0$ we have $$M_{n,k} = \left\{f\in \frac{1}{\Delta_x^k} R_{x,y}^- \;\Big|\; D(x_1,\ldots,x_n,\partial_{y_1},\ldots,\partial_{y_n}) f\in R_{x,y} \; (\forall D\in (R_{x,y}^-)^k) \right\}.$$ For $k\geq 1$ we have $$M_{n,k} = \left\{f\in \frac{1}{\Delta_x^{k-1}} R_{x,y}^+ \;\Big|\; D(x_1,\ldots,x_n,\partial_{y_1},\ldots,\partial_{y_n}) f\in R_{x,y} \; (\forall D\in (R_{x,y}^-)^{k-1}) \right\}.$$
:::

For instance, we have $M_{n,0}=R_{x,y}^-$ and $M_{n,1}=R_{x,y}^+$. Equivalence of the two presentations follows from the fact that if $f\in \frac{1}{\Delta_x} R_{x,y}^-$ satisfies $Df\in R_{x,y}$ for all $D\in R_{x,y}^-$, then we have $f\in R_{x,y}^+$.

In the case $n=2$ the module $R_{x,y}^-$ is generated over $R_{x,y}^+$ by $x_1-x_2$ and $y_1-y_2$. So the condition on $f$ is equivalent to $$(x_1-x_2)^i (\partial_{y_1} - \partial_{y_2})^j f \in R_{x,y} \qquad(i+j=k-1).$$ Equivalently, in the expansion $$f = \sum_{i,j} (x_1-x_2)^i (y_1-y_2)^j f_{ij}(x_1+x_2, y_1+y_2)$$ we have $f_{ij}=0$ unless $i\geq 0$ or $i\geq -k+1+j$. Note that also $f_{ij}=0$ unless $i+j\equiv k-1\pmod{2}$. So $M_{2,k}$ has a direct sum decomposition $M_{2,k} = R_{x,y}^{(-1)^{k-1}} \bigoplus M_{2,k}'$, where $M_{2,k'}$ has the Hilbert series $$\frac{1}{(1-q)(1-t)}\sum_{\substack{i\geq 1,\,j\geq 0,\,i+j\leq k-1\\i+j\equiv k-1\pmod{2}}} q^{-i} t^j,$$ which exactly matches the $z^2$-term of [\[eq:plog example\]](#eq:plog example){reference-type="eqref" reference="eq:plog example"} after the substitution $q\to q^{-1}$.

More generally, we notice that there is a *shuffle product* $M_{n',k} \otimes M_{n'',k} \to M_{n'+n'',k}$ given by $$f\ast g =$$ $$\sum_{\sigma\in S_{n'+n''}/(S_n'\times S_{n''})} (-1)^{(k-1)|\sigma|} \sigma \left(f(x_1,\ldots,x_{n'},y_1,\ldots,y_{n'}) g(x_{n'+1},\ldots,x_{n'+n''},y_{n'+1},\ldots,y_{n'+n''})\right).$$ Supported by computer experiments, we formulate the following conjecture.

::: conjecture
[]{#conj:iso vector spaces label="conj:iso vector spaces"} Denote by $M_{n,k}^\textrm{shuffles}\subset M_{n,k}$ the span of all shuffle products of the form $f\ast g$ for $f\in M_{n',k}$ and $g\in M_{n-n',k}$, $0<n'<n$. Let the space of primitive elements be the quotient $M_{n,k}^\textrm{prim}:=M_{n,k} / M_{n,k}^\textrm{shuffles}$. We have an isomorphism of bigraded vector spaces $$H^*(X)\left[\sum_{i=1}^n x_i, \sum_{i=1}^n y_i\right] \cong M_{n,k}^\textrm{prim}.$$
:::

The ring structure of the cohomology is not immediately evident from this description, but our COHA tells us where to look for it.

::: prop
The Lie algebra $\mathscr{H}_2 \otimes H^*(\mathbb P^1)$ acts on $M_{n,k}$ by the following operations: $$(T_{r,s}\otimes \mathrm{pt}) f  = \sum_{i=1}^n x_i^{s} \partial_{y_i}^r f,$$ $$(T_{r,s}\otimes 1) f  = \sum_{i=1}^n x_i^{s-1} \partial_{y_i}^{r-1} (-s \partial_{y_i} y_i - r x_i \partial_{x_i}) f.$$ This action is compatible with the shuffle product and therefore descends to $M_{n,k}^\textrm{prim}$.
:::

Now we describe the ring structure. First we expect that the following is true:

::: conjecture
The space $M_{n,k}^\textrm{prim}$ is spanned by products of $\frac{1}{\Delta_x^{k-1}}$ and polynomials of the form $$\psi_s(\mathrm{pt}) := \sum_{i=1}^n x_i^s, \qquad \psi_s(1) := s \sum_{i=1}^n x_i^{s-1} y_i.$$
:::

This conjecture implies that $M_{n,k}^\textrm{prim}$ is isomorphic to the quotient of the ring of polynomials in the generators $\psi_s(\mathrm{pt})$, $\psi_s(1)$ by a certain ideal. So it endows $M_{n,k}^\textrm{prim}$ with a ring structure and it is natural to formulate

::: conjecture
[]{#conj:iso rings label="conj:iso rings"} The isomorphism of Conjecture [\[conj:iso vector spaces\]](#conj:iso vector spaces){reference-type="ref" reference="conj:iso vector spaces"} is an isomorphism of rings.
:::

## Some remarks

The Hilbert scheme has been the source of interesting bigraded modules. For instance, there was $(n+1)^{n-1}$ conjecture and $n!$ conjecture proved by Haiman [@haiman2002vanishing]. The $(n+1)^{n-1}$ conjecture is about the module of diagonal coinvariants.

::: theorem
[@haiman2002vanishing] $$\dim R_{x,y}/(R_{x,y}^+)_{>0} = (n+1)^{n-1}$$
:::

An explicit combinatorial presentation of the bigraded Frobenius character of $R_{x,y}/(R_{x,y}^+)_{>0}$ was known as a shuffle conjecture [@haglund2005combinatoriala] and was proved in [@carlsson2018proof]. Also in this context Haiman observed that the vector space is in a certain sense generated by the differential operators $\sum_{i=1}^n x_i^{s-1} \frac{\partial}{\partial y_i}$, which led to the operator conjectures in [@haiman1994conjectures]. The double coinvariants has been interpreted in terms of Borel-Moore cohomology of affine Springer fibers in [@carlsson2018affine].

Our story suggests that there are many more interesting bigraded modules to be constructed using the Hilbert scheme.
