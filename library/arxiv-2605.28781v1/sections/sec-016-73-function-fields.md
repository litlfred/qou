---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-016-73-function-fields
section_title: "Function fields"
section_number: 7.3
pages: 17-23
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.961
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
We now construct counterexamples to the sum-product conjecture in fields of characteristic $p$. The constructions will lie in a sequence of fields $\mathbb F_q(C_i)$ for a sequence of algebraic curves $C_i$, and hence give counterexamples to the sum-product conjecture in any field containing all of them as subfields, such as $\overline{\mathbb F_q(t)}$ or $\mathbb F_q((t))$ (since our curves $C_i$ will have rational points so that $\mathbb F_q(C_i) \subseteq \mathbb F_q((t))$).

The rational places of $C_i$ will play the role that the infinite places play in the main argument of this paper, or that the small split primes play in the original unit distance argument. Hence we rely on constructions of curves with many rational points.

Let $C$ be a smooth projective geometrically connected curve over a finite field $\mathbb F_q$, and let $\mathbb F_q(C)$ be a field of rational functions on $C$. A convenient way to produce a subset $A \subset \mathbb F_q(C)$ is to construct a subset $A \subseteq H^0(C,L)$ of the global sections $H^0(C,L)$ of a line bundle $L$ on $C$. Dividing by any nonzero section of $L$ identifies $A \subset H^0(C,L)$ with a subset of $\mathbb F_q(C)$. This operation is compatible with taking sums and products, so to find a counterexample to sum-product it suffices to find a subset $A \subseteq H^0(C,L)$ such that $A + A \subseteq H^0(C,L)$ and $AA \subseteq H^0(C,L^{ 2})$ are both small.

Our construction is as follows. Let $L_P$ be a line bundle of degree $d_P$ and $L_G$ be a line bundle of degree $d_G$. Let $$P = \{ f \in H^0(C, L_P) \mid f \textrm{ does not vanish at any point in } C(\mathbb F_q)\}$$ and $$G = \{ g \in H^0(C, L_G) \mid g \textrm{ vanishes only at points in } C(\mathbb F_q)\}.$$ Since the $0$ section vanishes everywhere, $0$ is contained in neither $P$ nor $G$.

Let $A = P G \subseteq H^0(C, L_P \otimes L_G)$.

To understand the analogy between this construction and our original construction with number fields, one should think of $C(\mathbb F_q)$ as analogous to the set of infinite places and $H^0(C,L)$ as analogous to the set of elements of the ring of integers with bounded absolute value at each infinite place, with the exact bound depending on the line bundle $L$. Then $P$ is analogous to the set of elements of the ring with bounded absolute value at each infinite place, that are also not too small at each infinite place (since the nonvanishing at $x\in C(\mathbb F_q)$ forces the $x$-adic absolute value to not be too large), which is exactly how the set $P$ in the number field case can be described. The elements of $G$ are analogous to the set of elements of the ring of integers with bounded absolute value at each infinite place that are not divisible by any finite prime (since vanishing at a point is equivalent to being divisible by the corresponding prime ideal), in other words, units of bounded absolute value, which is similar to the construction of $G$ in the number field case. (We have dropped the lower bound on the absolute value that was used in the number field case.)

::: lemma
[]{#ff-pg label="ff-pg"} We have $|PG| = \frac{|P| |G|}{q-1}.$
:::

::: proof
*Proof.* If $f_1,f_2 \in P$ and $g_1,g_2\in G$ satisfy $f_1g_1=f_2g_2$ then we have $f_1/f_2=g_2/g_1$. Since $f_1/f_2$ is a rational function with no zeroes or poles at points of $C(\mathbb F_q)$, and $g_2/g_1$ is a rational function with only zeroes and poles at points of $C(\mathbb F_q)$, they must both have no zeroes or poles and hence be elements of $\mathbb F_q^\times$. Thus $PG = (P \times G)/\mathbb F_q^\times$. ◻
:::

Let $g$ be the genus of $C$.

::: lemma
[]{#ff-rr label="ff-rr"} As long as $d_P \geq 2g-1 +\mathopen{}\left| C(\mathbb F_q)\mathclose{}\right|$ we have $$\label{ff-P-bound} |P| = q^{ d_P + 1-g} (1-q^{-1})^{|C(\mathbb F_q)|}$$ and $$\label{ff-sum-bound}|PG + PG| \leq q^{ d_P+d_G  + 1-g} .$$
:::

::: proof
*Proof.* These follow by the Riemann-Roch formula.

For [\[ff-sum-bound\]](#ff-sum-bound){reference-type="eqref" reference="ff-sum-bound"}, note that $PG+ PG$ is a subset of $H^0(C, L_P \otimes L_G)$. If $G$ is non-empty we have $d_G\geq 0$ so the assumption implies $d_P +d_G \geq   2g-1 +\mathopen{}\left|  C(\mathbb F_q)\mathclose{}\right|\geq 2g-1$ and thus $$|PG + PG|  \leq |H^0(C,L_P \otimes L_G)| =q^{ \deg( L_P \otimes L_G )+ 1-g} = q^{d_P +d_G +1-g}$$ by Riemann-Roch.

For [\[ff-P-bound\]](#ff-P-bound){reference-type="eqref" reference="ff-P-bound"}, we use inclusion-exclusion to obtain $$|P|= \sum_{S \subseteq C(\mathbb F_q)} (-1)^{|S|} |\{ f\in H^0(C, L_P) | f \textrm{ vanishes at all points in } S\}|$$$$=  \sum_{S \subseteq C(\mathbb F_q)}  (-1)^{|S|} |H^0(C, L_P (- \sum_{x\in S}[x]))| =  \sum_{S \subseteq C(\mathbb F_q)}  (-1)^{|S|}  q^{ \deg L_P(- \sum_{x\in S}[x])+1-g}$$$$= \sum_{S \subseteq C(\mathbb F_q)}  (-1)^{|S|} q^{ d_P - |S| + 1-g}= q^{ d_P + 1-g} (1-q^{-1})^{|C(\mathbb F_q)|}$$ since $\deg L_P(- \sum_{x\in S}[x]) = d_P - |S| \geq d_P - |C(\mathbb F_q)|  \geq 2g-1$ by assumption. ◻
:::

Let $\operatorname{Pic}^0(C)(\mathbb F_q)$ be the degree-zero Picard group of $C$ (which goes by other names, including the $\mathbb F_q$-points of the Jacobian of $C$ and the class group of $\mathbb F_q(C)$) and let $\operatorname{Pic}^0(C)(\mathbb F_q)[2]$ be its $2$-torsion subgroup. For $L$ a line bundle, let $$N_{\mathbb F_q}(L) = |\{ g \in H^0(C, L) \mid g \textrm{ vanishes only at points in } C(\mathbb F_q)\}|.$$

::: lemma
[]{#ff-pm label="ff-pm"} For each $d_G \geq 0$ there exists a line bundle $L_G$ of degree $d_G$ such that $$\label{ff-G-bound} N_{\mathbb F_q}(L_G) \geq \frac{ (q-1)   \binom{d_G + |C(\mathbb F_q)|-1}{d_G}}{ 2|\operatorname{Pic}^0(C)(\mathbb F_q)|}$$ and $$\label{ff-almost-product-bound} \frac{ N_{\mathbb F_q}(L_G^2)}{N_{\mathbb F_q}(L_G)} \leq \frac{ 2 |\operatorname{Pic}^0(C)(\mathbb F_q)[2]| \binom{2d_G + |C(\mathbb F_q)|-1}{2d_G}}{ \binom{d_G + |C(\mathbb F_q)|-1}{d_G}}.$$
:::

::: proof
*Proof.* If we choose $L_G$ uniformly at random among isomorphism classes of line bundles $L_G$ of degree $d_G$, letting $\mathbb E$ be the expectation, we have $$\mathbb E[ N_{\mathbb F_q}(L_G)] =\frac{ (q-1)   \binom{d_G + |C(\mathbb F_q)|-1}{d_G}}{ |\operatorname{Pic}^0(C)(\mathbb F_q)|}$$ since there are $\binom{d_G + |C(\mathbb F_q)|-1}{d_G}$ divisors of degree $d_G$ supported at the points of $C(\mathbb F_q)$, each divisor defines $q-1$ sections of $L_G$ if its divisor class equals the divisor class of $L_G$ and $0$ sections otherwise, and the number of divisor classes of degree $d_G$ is $|\operatorname{Pic}^0(C)(\mathbb F_q)|$.

If we choose $L_G$ uniformly at random, then the divisor class of $L_G^{2}$ is chosen uniformly at random from the divisor classes of degree $2d_G$ that are divisible by $2$, the number of which is $\frac{| \operatorname{Pic}^0(C)(\mathbb F_q)|}{|\operatorname{Pic}^0(C)(\mathbb F_q)[2]|}$. Thus $$\hspace{-.5in} \mathbb E[ N_{\mathbb F_q}(L_G^2) ] \leq \frac{ (q-1)   \binom{2d_G + |C(\mathbb F_q)|-1}{2d_G} |\operatorname{Pic}^0(C)(\mathbb F_q)[2]| }{ |\operatorname{Pic}^0(C)(\mathbb F_q)|}$$ by the same reasoning. Hence we can choose $L_G$ of degree $d_G$ with $$\label{ff-expectation-inequality} \frac{ |\operatorname{Pic}^0(C)(\mathbb F_q)|}{ (q-1)   \binom{d_G + |C(\mathbb F_q)|-1}{d_G}}N_{\mathbb F_q}(L_G) - \frac{ |\operatorname{Pic}^0(C)(\mathbb F_q)|}{2 (q-1)   \binom{2d_G + |C(\mathbb F_q)|-1}{2d_G} |\operatorname{Pic}^0(C)(\mathbb F_q)[2]| }N_{\mathbb F_q}(L_G^2) \geq \frac{1}{2}$$ as the expectation of the left hand side of [\[ff-expectation-inequality\]](#ff-expectation-inequality){reference-type="eqref" reference="ff-expectation-inequality"} is at least $\frac{1}{2}$ when $L_G$ is chosen uniformly at random and thus we can choose an $L_G$ where the left hand side is at least $\frac{1}{2}$.

[\[ff-expectation-inequality\]](#ff-expectation-inequality){reference-type="eqref" reference="ff-expectation-inequality"} immediately implies [\[ff-G-bound\]](#ff-G-bound){reference-type="eqref" reference="ff-G-bound"} by dropping the $N_{\mathbb F_q}(L_G^2)$ term and implies [\[ff-almost-product-bound\]](#ff-almost-product-bound){reference-type="eqref" reference="ff-almost-product-bound"} by dropping the $\frac{1}{2}$ term. ◻
:::

::: lemma
[]{#ff-product label="ff-product"} Choosing $L_G$ as in Lemma [\[ff-pm\]](#ff-pm){reference-type="ref" reference="ff-pm"}, we have $$\label{ff-G-product-bound} \frac{ |GG|}{|G|} \leq \frac{ 2 |\operatorname{Pic}^0(C)(\mathbb F_q)[2]| \binom{2d_G + |C(\mathbb F_q)|-1}{2d_G}}{ \binom{d_G + |C(\mathbb F_q)|-1}{d_G}}$$ and as long as $d_P \geq 2g-1 +\# C(\mathbb F_q)$ we have $$\label{ff-product-bound} \frac{|PGPG|}{|PG|}\leq \frac{ 2 |\operatorname{Pic}^0(C)(\mathbb F_q)[2]| \binom{2d_G + |C(\mathbb F_q)|-1}{2d_G} q^{ d_P + 1-g} (1-q^{-1})^{|C(\mathbb F_q)|}}{ \binom{d_G + |C(\mathbb F_q)|-1}{d_G}}.$$
:::

::: proof
*Proof.* We have $$\{g \in H^0(C, L_G) \mid g \textrm{ vanishes only at points in } C(\mathbb F_q)\}^2$$$$\subseteq \{ h \in H^0(C, L_G^2) \mid h \textrm{ vanishes only at points in } C(\mathbb F_q)\}$$ which together with [\[ff-almost-product-bound\]](#ff-almost-product-bound){reference-type="eqref" reference="ff-almost-product-bound"} implies [\[ff-G-product-bound\]](#ff-G-product-bound){reference-type="eqref" reference="ff-G-product-bound"}.

We have $|PGPG| \leq |PP| |GG|/(q-1) \leq |P|^2 |GG|/(q-1)$ since both $PP$ and $GG$ are stable under multiplication by $\mathbb F_q^\times$ and we have $|PG|=|P||G|/(q-1)$ by Lemma [\[ff-pg\]](#ff-pg){reference-type="ref" reference="ff-pg"} so we have $$\frac{ |PGPG|}{|PG|} \leq \frac{ |P| |GG|}{|G|}$$ so that [\[ff-product-bound\]](#ff-product-bound){reference-type="eqref" reference="ff-product-bound"} follows from [\[ff-G-product-bound\]](#ff-G-product-bound){reference-type="eqref" reference="ff-G-product-bound"} and [\[ff-P-bound\]](#ff-P-bound){reference-type="eqref" reference="ff-P-bound"}. ◻
:::

Putting this together, we set $A = PG$ and then embed $A$ into $\mathbb F_q(C)$. Using Lemma [\[ff-pg\]](#ff-pg){reference-type="ref" reference="ff-pg"}, [\[ff-P-bound\]](#ff-P-bound){reference-type="eqref" reference="ff-P-bound"}, and [\[ff-G-bound\]](#ff-G-bound){reference-type="eqref" reference="ff-G-bound"}, we obtain

$$\label{ff-a} |A| \geq \frac{ \binom{d_G + |C(\mathbb F_q)|-1}{d_G} q^{ d_P + 1-g} (1-q^{-1})^{|C(\mathbb F_q)|}}{ 2|\operatorname{Pic}^0(C)(\mathbb F_q)|}.$$ Using [\[ff-sum-bound\]](#ff-sum-bound){reference-type="eqref" reference="ff-sum-bound"}, we obtain $$\label{ff-a-sum} | A + A |\leq q^{ d_P+d_G  + 1-g}.$$ Using [\[ff-product-bound\]](#ff-product-bound){reference-type="eqref" reference="ff-product-bound"}, we obtain $$\label{ff-a-product}\frac{|AA|}{|A|} \leq \frac{ 2 |\operatorname{Pic}^0(C)(\mathbb F_q)[2]| \binom{2d_G + |C(\mathbb F_q)|-1}{2d_G} q^{ d_P + 1-g} (1-q^{-1})^{|C(\mathbb F_q)|}}{ \binom{d_G + |C(\mathbb F_q)|-1}{d_G}}.$$

We first give a counterexample to the sum-product theorem in $\mathbb F_p((t))$, though with the exponent getting worse as the characteristic grows. This argument is not particularly optimized. Afterwards, we give an argument that gets a more optimized exponent in $\mathbb F_q((t)))$ for specific finite fields $\mathbb F_q$. This second result is specialized to the case of $q$ a perfect square, to take advantage of known constructions of curves with many rational points over finite fields of square order.

We begin with an asymptotic formula for binomial coefficients For $x,y$ positive reals, let $F_q(x,y) = (x+y)\log_q(x+y) - x \log_q(x) - y\log_q(y)$.

We have the asymptotic $$\label{binomial-asymptotic} \binom{n+m}{n} = q^{ F_q (x,y) g + o(g)} \textrm{ when} n =xg +o(g) \textrm{ and } m=yg + o(g)$$ that follows from Stirling's formula.

::: theorem
[]{#th-ffspec label="th-ffspec"} There is an absolute constant $c>0$ such that for any prime $p$, there exist finite subsets $A \subset \mathbb F_{p}((t))$ of arbitrarily large cardinality such that $|A + A| \leq |A|^{2 -\frac{c}{\log p}}$ and $|AA| \leq |A|^{2-\frac{c}{\log p}}$.
:::

Theorem [\[th-ffmain\]](#th-ffmain){reference-type="ref" reference="th-ffmain"} immediately follows, since for $q$ a power of $p$, $\mathbb F_{q}((t))$ contains $\mathbb F_{p}((t))$ and so the $p$ case implies the general case.

::: proof
*Proof.* It was proven by Serre [@Serre83] (but see [@Elkies2004 Appendix] for the proof) that there exists an absolute constant $d>0$ such that for each finite field $\mathbb F_q$ there exists $C$ over $\mathbb F_p$ with genus $g(C)$ arbitrarily large such that $$\label{points-on-curve-serre} \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right|  \geq d g(C) \log(q)$$

We have $$\label{jacobian-trivial} \mathopen{}\left| \operatorname{Pic}^0(C)(\mathbb F_q)\mathclose{}\right| \leq (\sqrt{q}+1)^{2g}$$ by Weil's Riemann hypothesis for curves.

Finally, we have the bound $$\label{2-torsion-trivial} \mathopen{}\left| \operatorname{Pic}^0(C)[2](\mathbb F_q)\mathclose{}\right|\leq 2^{2 g(C)}$$ valid since $\operatorname{Pic}^0(C)$ is an abelian variety of dimension $g(C)$ and thus has at most $2^{2g(C)}$ two-torsion points.

We take $q=p$ and take $d_P = d_G = x  \mathopen{}\left|  C(\mathbb F_p)\mathclose{}\right|$ for some absolute but sufficiently large integer $x$. We have $$d_P = x \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right| \geq xd g(C) \log (q) \geq xd g(C) \log 2 \geq 2g$$ for $x$ sufficiently large.

From [\[ff-a\]](#ff-a){reference-type="eqref" reference="ff-a"}, [\[binomial-asymptotic\]](#binomial-asymptotic){reference-type="eqref" reference="binomial-asymptotic"}, [\[jacobian-trivial\]](#jacobian-trivial){reference-type="eqref" reference="jacobian-trivial"}, and [\[points-on-curve-serre\]](#points-on-curve-serre){reference-type="eqref" reference="points-on-curve-serre"} we get $$\log_q \mathopen{}\left| A\mathclose{}\right|= \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right| (F_q(x,1) + x + \log_q(1-q^{-1}) +o(1))  - g(C) ( 1+ 2\log_q (\sqrt{q}+1))$$ $$=\mathopen{}\left| C(\mathbb F_q)\mathclose{}\right| \left(F_q(x,1) + x + O\left( \frac{1}{\log q} \right) + o(1) \right)$$ since $2\log_q (\sqrt{q}+1)=O(1)$ and $g(c) = O ( \frac{1}{\log q} ) \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right|$ and $\log_q(1-q^{-1})= O ( \frac{1}{\log q} )$ also.

By [\[ff-a-sum\]](#ff-a-sum){reference-type="eqref" reference="ff-a-sum"}, we get $$\log_q \mathopen{}\left| A+A\mathclose{}\right| \leq  2x \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right| .$$

Using [\[ff-a-product\]](#ff-a-product){reference-type="eqref" reference="ff-a-product"}, [\[2-torsion-trivial\]](#2-torsion-trivial){reference-type="eqref" reference="2-torsion-trivial"}, [\[binomial-asymptotic\]](#binomial-asymptotic){reference-type="eqref" reference="binomial-asymptotic"}, and [\[points-on-curve-serre\]](#points-on-curve-serre){reference-type="eqref" reference="points-on-curve-serre"}, we get $$\log_q \left(\frac{\mathopen{}\left| AA\mathclose{}\right|}{\mathopen{}\left| A\mathclose{}\right|}\right) \leq  \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right| ( F_q(2x,1) - F_q(x,1) +x+ o(1) )  + g ( 2 \log_q(2) )$$ $$= \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right| ( F_q(2x,1) - F_q(x,1) +x+O\left(\frac{1}{\log q}\right) +o(1) ).$$

Now $$F_q(x,1) =\frac{ ( (x+1) \log(x+1)-x\log x)}{\log q} = {\log(x+1) + x \log(1+1/x)} {\log q}.$$ We can choose $x$ sufficiently large that $F_q(x,1)$ is greater than the $O(\frac{1}{\log q})$ term by some positive multiple of $\frac{1}{\log q}$, in which case $\frac{\log_q \mathopen{}\left| A+A\mathclose{}\right|}{\log_q \mathopen{}\left| A\mathclose{}\right|}$ will be at most $2-c/\log q$ for some $c>0$, as desired. We have $$\log_q\left( \frac{ \mathopen{}\left| A\mathclose{}\right|^2}{\mathopen{}\left| AA\mathclose{}\right|} \right) \geq \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right| ( 2F_q(x,1) - F_q(2x,1) +O \left(\frac{1}{\log q}+o(1)\right)$$ and $$2F_q(x,1) - F_q(2x,1) ={ 2 \log x -\log(x+1) + 2x \log(1+1/x)- 2x \log(1+1/(2x))}{\log q}.$$ We can choose $x$ sufficiently large that $2F_q(x,1) - F_q(2x,1)$ is greater than the $O(\frac{1}{\log q})$ term by some positive multiple of $\frac{1}{\log q}$, in which case we have $$\frac{ \log_q( \frac{ \mathopen{}\left| A\mathclose{}\right|^2}{\mathopen{}\left| AA\mathclose{}\right|} )}{\log_q(\mathopen{}\left| A\mathclose{}\right|)}  \geq \frac{c}{\log q}$$ for some $c>0$, as desired, since the denominator is $O( \mathopen{}\left| C(\mathbb F_q)\mathclose{}\right|)$. ◻
:::

Finally, we give a more optimized version of the proof of Theorem [\[th-ffspec\]](#th-ffspec){reference-type="ref" reference="th-ffspec"} over fields of perfect square order. As promised, this argument delivers exponents close to $1.9$ for some values of $q$.

::: theorem
[]{#ff-complicated label="ff-complicated"} Let $q$ be a prime power that is a perfect square. Let $a,b \in (1,2)$. Then there exist finite subsets $A \subset \mathbb F_{q}((t))$ of arbitrarily large cardinality such that $|A + A| \leq |A|^a$ and $|AA| \leq |A|^b$ as long as there exist $\beta>0$ and $\alpha> \sqrt{q}+1$ such that $$\label{ff-a-condition} a >\frac{ \alpha + \beta - 1}{ F_q(\beta, \sqrt{q}-1) + \alpha + 2(\sqrt{q}-1) \log_q (1- q^{-1}) -2 }$$ $$\label{ff-b-condition} b > 1 + \frac{2 \log_q( 2) + F_q(2\beta, \sqrt{q}-1) - F_q(\beta, \sqrt{q}-1) + \alpha -1+ ( \sqrt{q}-1) \log_q(1-q^{-1} )  }{ F_q(\beta, \sqrt{q}-1) + \alpha +  2(\sqrt{q}-1) \log_q (1- q^{-1}) -2 }.$$

If $q$ is a power of $2$, we may replace [\[ff-b-condition\]](#ff-b-condition){reference-type="eqref" reference="ff-b-condition"} by the weaker $$\label{ff-b-condition-char2}  b > 1 + \frac{\frac{ \log_q( 2) }{\sqrt{q}+1} + F_q(2\beta, \sqrt{q}-1) - F_q(\beta, \sqrt{q}-1) + \alpha + ( \sqrt{q}-1) \log_q(1-q^{-1} )  -1}{ F_q(\beta, \sqrt{q}-1) + \alpha +  2(\sqrt{q}-1) \log_q (1- q^{-1}) -2}.$$
:::

::: proof
*Proof.* Note that under the assumptions, the denominator $F_q(\beta, \sqrt{q}-1) + \alpha + 2(\sqrt{q}-1) \log_q (1- q^{-1}) -2$ is always at least $\sqrt{q}-1 + 2(\sqrt{q}-1) \log_q(1-q^{-1})$ and thus always positive since $\log_q(1-q^{-1}) \geq \log_4(3/4) > -\frac{1}{2}$ as $q\geq 4$.

We choose a sequence of curves $C_i$ with $g_i$ tending to $\infty$ and $$\label{points-on-curve-limit}\lim_{i \to \infty} \frac{ |C_i(\mathbb F_q)|}{g(C_i)} = \sqrt{q}-1.$$ That such a sequence exists for $q$ a perfect square was proven independently by Ihara [@Ih82] and by Tsfasman, Vlăduţ, and Zink [@Tsfasman1982]. That this is optimal was proven by Drinfeld and Vlăduţ [@Vladut1983]. For such a sequence, the limit $$\label{jacobian-limit} \lim_{i \to \infty} \frac{\log_q  |\operatorname{Pic}^0(C_i)(\mathbb F_q)|}{g(C_i)} = 1- ( \sqrt{q}-1) \log_q (1- q^{-1})$$ was established by Rosenbloom and Tsfasman [@Rosenbloom1990 Lemma A.2].

We choose $d_{P_i} = \lceil \alpha g(C_i) \rceil$ and $d_{G_i} = \lceil \beta g(C_i) \rceil$ and construct a set $A_i =P_iG_i$ as described above. We have $A_i \subseteq \mathbb F_q(C_i)$. For $i$ sufficiently large, we can embed $\mathbb F_q(C_i)$ into $\mathbb F_q((t))$ using any rational point of $C_i$, of which there are many by [\[points-on-curve-limit\]](#points-on-curve-limit){reference-type="eqref" reference="points-on-curve-limit"}, so $A_i$ will indeed define a subset of $\mathbb F_q((t))$.

We have $d_{P_i} \geq 2g(C_I)-1+ |C_i(\mathbb F_q)|$ for $i$ sufficiently large since $\alpha> \sqrt{q}+1$.

From [\[ff-a\]](#ff-a){reference-type="eqref" reference="ff-a"}, [\[binomial-asymptotic\]](#binomial-asymptotic){reference-type="eqref" reference="binomial-asymptotic"}, [\[points-on-curve-limit\]](#points-on-curve-limit){reference-type="eqref" reference="points-on-curve-limit"}, and [\[jacobian-limit\]](#jacobian-limit){reference-type="eqref" reference="jacobian-limit"}, we have that $$\frac{ \log_q( |A_i|)}{g(C_i)} \geq  F_q(\beta, \sqrt{q}-1) + \alpha -1 + (\sqrt{q}-1) \log_q (1- q^{-1})  - 1 + (\sqrt{q}-1) \log_q(1-q^{-1})+o(1)$$ $$= F_q(\beta, \sqrt{q}-1) + \alpha +2(\sqrt{q}-1) \log_q (1- q^{-1}) -2+o(1) .$$

From [\[ff-a-sum\]](#ff-a-sum){reference-type="eqref" reference="ff-a-sum"} we see that $$\frac{\log_q( |A_i+A_i|)}{g(C_i)} \leq \alpha + \beta -1+o(1).$$ From [\[ff-a-product\]](#ff-a-product){reference-type="eqref" reference="ff-a-product"}, [\[2-torsion-trivial\]](#2-torsion-trivial){reference-type="eqref" reference="2-torsion-trivial"}, [\[binomial-asymptotic\]](#binomial-asymptotic){reference-type="eqref" reference="binomial-asymptotic"}, and [\[points-on-curve-limit\]](#points-on-curve-limit){reference-type="eqref" reference="points-on-curve-limit"}, we see that $$\frac{\log_q( |A_iA_i|) -\log_q(|A_i|)}{g(C_i)}$$ $$\leq 2 \log_q(2) + F_q(2\beta, \sqrt{q}-1) + \alpha -1 +  (\sqrt{q}-1) \log_q(1-q^{-1})  - F_q(\beta, \sqrt{q}-1)+o(1).$$

From these and [\[ff-a-condition\]](#ff-a-condition){reference-type="eqref" reference="ff-a-condition"} it follows that $|A_i+A_i|\leq |A_i|^a$ for $i$ sufficiently large, and from these and [\[ff-b-condition\]](#ff-b-condition){reference-type="eqref" reference="ff-b-condition"} it follows that $|A_i A_i| \leq |A_i|^b$ for $i$ sufficiently large.

Finally, in the case when $q$ is a power of $2$, there exists a sequence $C_i$ satisfying [\[points-on-curve-limit\]](#points-on-curve-limit){reference-type="eqref" reference="points-on-curve-limit"} and thus [\[jacobian-limit\]](#jacobian-limit){reference-type="eqref" reference="jacobian-limit"} but also $$\label{2-torsion-char2-bound} \lim_{i \to \infty} \frac{\log_q  |\operatorname{Pic}^0(C_i)[2](\mathbb F_q)|}{g(C_i)} = \frac{\log_q(2)}{\sqrt{q}+1}$$ was proven by Cascudo, Cramer, and Xing [@CCX Theorem 2.3(iii)]. Replacing [\[2-torsion-trivial\]](#2-torsion-trivial){reference-type="eqref" reference="2-torsion-trivial"} with [\[2-torsion-char2-bound\]](#2-torsion-char2-bound){reference-type="eqref" reference="2-torsion-char2-bound"} in the above argument, we obtain the same conclusion under [\[ff-b-condition-char2\]](#ff-b-condition-char2){reference-type="eqref" reference="ff-b-condition-char2"}. ◻
:::

In small characteristic, one can obtain explicit exponents close to $1.9$, as long as the finite field size is large enough. For example, if $q=1024$ we can take $a=b=1.906$ since we may take $\alpha=33.01$ and $\beta=40.53$. For $q=41^2$ we can take $a=1.910$ and $b=1.912$ since we may take $\alpha=42.01$ and $b=51.5$.

Over very small finite fields, the exponents are slightly worse. For example, if $q=4$ we can take $a=1.939$ and $b=1.941$ since we may take $\alpha=10.75$ and $\beta=11.25$. If $q=9$ we can take $a=1.964$ and $b=1.972$ since we may take $\alpha=11.5$ and $\beta=13$.
