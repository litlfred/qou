---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-027-51-a-q-stirlings-formula
section_title: "A q-Stirling's Formula"
section_number: 5.1
pages: 96-104
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 1.0
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Before we say anything about a $q$-deformed Stirling's formula, recall that Stirling's formula says that $$n!\sim \sqrt{2\pi n}\frac{n^n}{e^n}$$ This is an asymptotic formula. We use the $\sim$ symbol to denote that $$\lim_{n\rightarrow\infty} \frac{n!}{\sqrt{2\pi n}\frac{n^n}{e^n}}=1$$ It is worthwhile to note that this formula can be proved using the Euler Maclaurin formula discussed in chapter 2.

For fixed $0<q<1$, we define $$[n]_q=\frac{1-q^n}{1-q}$$ We can then define a $q$-deformed factorial as $$[n]_q!=[n]_q[n-1]_q\dots[1]_q=\prod_{k=1}^n\frac{1-q^k}{1-q}$$ For notational convenience, we will denote $[n]_q$ by $[n]$ and $[n]_q!$ as $[n]!$, suppressing the dependence on $q$. In a work in progress with Shannon Starr, we require a Stirling type formula (or asymptotic formula) for $[n]!$. A similar formula was first proved by Moak [@Moak]. At the time this formula was proved, we were unaware of his work. As our methods and approximation are slightly different, we include our verison and proof of the $q$-Stirling formula here.

::: thm
For $\beta\in\mathbb{R}$, let $q=\exp(-\beta/n)$. Let $[n]!$ denote $[n]_q!$ for this particular $q$. Then we have $$\ln\left(\frac{[n]!}{n!}\right)=n\int_0^1\ln\left(\frac{1-e^{-\beta y}}{\beta{y}}\right)dy +\frac{\beta}{2}+\frac{1}{2}\ln\left(\frac{1-e^{-\beta}}{\beta}\right)+R_n(\beta)$$ where $R_n(\beta)$ is a remainder term and $R_n(\beta)\rightarrow 0$ as $n\rightarrow\infty$.
:::

::: proof
*Proof.* First consider $$\ln\left(\frac{[n]!}{n!}\right)$$ As mentioned previously, we want $q$ to be going to $1$ as $n\rightarrow\infty$, so we are looking at $q=e^{-\frac{\beta}{n}}$ for fixed $\beta$. Notice that $$\ln\left(\frac{[n]!}{n!}\right)=\sum_{k=1}^n \ln\left(\frac{1-q^k}{(1-q)k}\right)$$

To approximate this sum, we use the Euler-MacLaurin approach and compare the sum to

$$\int_1^n \ln\left(\frac{1-q^x}{(1-q)x}\right)dx$$

For ease of notation, let $$f(x)=\ln\left(\frac{1-q^x}{(1-q)x}\right)$$ In order to make this comparison, we will first compare $\frac{1}{2}f(k+1)+\frac{1}{2}f(k)$ to $$\int_k^{k+1} f(x)dx$$ and then sum over the $k$'s. Using the fundamental theorem of calculus, we know that $\frac{f(k)+f(k+1)}{2}$ is equal to $$\label{eq1} \int_k^{k+1}\frac{d}{dx}\left[(x-k-\frac{1}{2})(f(x))\right]dx$$ Evaluating the derivative in the integrand of [\[eq1\]](#eq1){reference-type="ref" reference="eq1"} gives

$$\label{eq} \int_k^{k+1}f(x)+\left (x-k-\frac{1}{2}\right)f'(x) \:dx$$ This can be broken up into two integrals, $$\int_k^{k+1}f(x)\:dx+\int_k^{k+1}  \left(x-k-\frac{1}{2}\right)f'(x)\: dx$$where the first integral is exactly what we wanted to compare to and the second integral is an error term. Consider now only this error term $$\label{eq2}\int_k^{k+1} \left(x-k-\frac{1}{2}\right)f'(x)\:dx$$Notice that $$\int_k^{k+1} \left(x-k-\frac{1}{2}\right)\:dx=0$$so we can add or subtract any constant from $f'(x)$ without changing the value of the integral. Using this fact, [\[eq2\]](#eq2){reference-type="ref" reference="eq2"} can be written as $$\int_k^{k+1}\left(x-k-\frac{1}{2}\right)[f'(x)-f'(0)]\:dx$$ Since this equation is true for any $1\leq k\leq n-1$, we can simplify this and let $k=0$ and $k+1=1$, which gives $$\label{eq3}\int_0^1\left(x-\frac{1}{2}\right)[f'(x)-f'(0)]\:dx$$This substitution will not cause any problems, because we can always replace $f(x)$ by $f(x+k)$ later. Since $f'(x)-f'(0)$ can be rewritten as $$\int_0^x f''(y)\:dy$$ we can write [\[eq3\]](#eq3){reference-type="ref" reference="eq3"} as the double integral $$\int_0^1\int_0^x \left(x-\frac{1}{2}\right)f''(y)\:dy\:dx$$Switching the order of integration gives $$\int_0^1\int_y^1 \left(x-\frac{1}{2}\right)f''(y)\:dx\:dy$$ After integrating with respect to $x$ we are left with $$\frac{1}{2}\int_0^1 y(1-y)f''(y)\:dy$$ Using this combined with [\[eq\]](#eq){reference-type="ref" reference="eq"}, we have shown that $$\frac{1}{2}f(0)+\frac{1}{2}f(1)=\int_0^1 f(x)\:dx+\int_0^1 x(1-x)f''(x)\:dx$$At this point we can return our attention to the original problem, in which we need to sum up all of these integrals. $$\label{result}\sum_{k=1}^n f(k)=\frac{1}{2}f(n)-\frac{1}{2}f(1)+\sum_{k=1}^{n-1}\frac{1}{2}(f(k)+f(k+1))$$

From the previous calculation, $$\sum_{k=1}^n\frac{1}{2}(f(k)+f(k+1))=\int_1^nf(x)\:dx+\sum_{k=1}^n\int_0^1x(1-x)f''(k+x)\:dx$$Since we can move the summation inside the integral, we now turn our attention to $f''(x)$ to see if this sum will converge. Calculating $f''(x)$ gives $$\frac{-(\ln(q))^2q^x}{(1-q^x)^2}+\frac{1}{x^2}$$Substituting $e^{-\frac{\beta}{n}}$ for $q$ gives $$\frac{-\beta^2e^{-\frac{\beta x}{n}}}{n^2(1-e^{-\frac{\beta x}{n}})^2}+\frac{1}{x^2}$$Multiplying top and bottom of the first fraction by $e^{\frac{\beta x}{n}}$$$\frac{-\beta^2}{n^2(e^{\frac{\beta x}{2n}}-e^{-\frac{\beta x}{2n}})^2}+\frac{1}{x^2}$$ Noticing that the bottom of the first fraction is equal to $(2n\sinh(\frac{\beta x}{2n}))^2$ leaves $$\frac{-\beta^2}{4n^2\sinh^2(\frac{\beta x}{2n})}+\frac{1}{x^2}$$This term will converge pointwise to $0$ by the dominated convergence theorem as $\frac{\beta}{n}\rightarrow 0$. Going back to ([\[result\]](#result){reference-type="ref" reference="result"}) gives $$\ln\left(\frac{[n]!}{n!}\right)\sim\frac{1}{2}f(n)+\int_1^nf(x)dx+\frac{1}{2}\sum_{k=1}^{n-1}\int_0^1 x(1-x)f''(k+x)dx$$ where this last term will converge in the limit.\
If we take $q = \exp(-\beta/n)$ for some $\beta \in \mathbb{R}$, then we obtain $$\begin{aligned}
\ln\left(\frac{[n]!}{n!}\right)\, \Big|_{q = e^{-\beta/n}}\,
&=\, \frac{1}{2}\, \ln\left(\frac{1-e^{-\beta}}{(1-e^{-\beta/n})n}\right)
+ \int_1^n \ln\left(\frac{1-e^{-\beta x/n}}{(1-e^{-\beta/n})x}\right)\, dx\\
&\qquad + \frac{1}{2}\,\int_0^1 x(1-x)  \sum_{k=1}^{n-1} \left[\frac{1}{(k+x)^2} - \frac{\beta^2}{4 n^2 \sinh^2(\beta[k+x]/n)}\right]\, dx\, .
\end{aligned}$$ We can rewrite this as $$\ln\left(\frac{[n]!}{n!}\right)\, \Big|_{q = e^{-\beta/n}}\,
=\, n A(\beta) + B(\beta) + R_n(\beta)\, ,$$ where $A(\beta)$ and $B(\beta)$ do not depend on $n$ and $R_n(\beta)$ is a "small" remainder term, which vanishes for $\beta$ fixed in the limit $n \to \infty$. More precisely, $$A(\beta)\, =\, \frac{1}{n}\, \int_0^n  \ln\left(\frac{1-e^{-\beta x/n}}{\beta x/n}\right)\, dx\, ,$$ which can be seen to be independent of $n$, by making a change of variables, $x = n y$ so that $dx = n dy$: $$A(\beta)\, =\, \int_0^1 \ln\left(\frac{1-e^{-\beta y}}{\beta y}\right)\, dy\, .$$ We can write $$B(\beta)\, =\, \frac{\beta}{2} + \frac{1}{2}\, \ln\left( \frac{1-e^{-\beta}}{\beta} \right)\, .$$ We throw all of the error terms we accumulated into the last term. It is convenient to break it into three parts: $$R_n(\beta)\, =\, R_n^{(1)}(\beta) + R_n^{(2)}(\beta) + R_n^{(3)}(\beta)\, ,$$ where $$\begin{gathered}
R_n^{(1)}(\beta)\, =\, \frac{1}{2}\,\int_0^1 x(1-x)  \sum_{k=1}^{n-1} \left[\frac{1}{(k+x)^2} - \frac{\beta^2}{4 n^2 \sinh^2(\beta[k+x]/n)}\right]\, dx\, ,\\
R_n^{(2)}(\beta)\, 
=\, \int_1^n \ln\left(\frac{1-e^{-\beta x/n}}{(1-e^{-\beta/n})x}\right)\, dx - n A(\beta) - \frac{\beta}{2}\, ,\\
R_n^{(3)}(\beta)\, 
=\,  \frac{1}{2}\, \ln\left(\frac{1-e^{-\beta}}{(1-e^{-\beta/n})n}\right) - \frac{1}{2}\, \ln\left( \frac{1-e^{-\beta}}{\beta} \right)\, .
\end{gathered}$$ At this point, the proof of our theorem is complete, provided that we prove the following lemma. ◻
:::

::: lemma
For $\beta \in \mathbb{R}$ fixed, we have $$R_n^{(1)}(\beta)\, ,\ R_n^{(2)}(\beta)\, ,\ R_n^{(3)}(\beta)\, \to\, 0\, ,$$ as $n \to \infty$.
:::

::: proof
*Proof.* We immediately know that $R_n^{(1)}(\beta)$ converges to $0$, as $n \to \infty$, since $$R_n^{(1)}(\beta)\, =\, \frac{1}{2}\,\int_0^1 x(1-x)  \sum_{k=1}^{n-1} \left[\frac{1}{(k+x)^2} - \frac{\beta^2}{4 n^2 \sinh^2(\beta[k+x]/n)}\right]\, dx\, ,$$ and we may use the dominated convergence theorem.

For the next term, we notice $$\begin{aligned}
R_n^{(2)}(\beta)\, 
&=\, \int_1^n \ln\left(\frac{1-e^{-\beta x/n}}{(1-e^{-\beta/n})x}\right)\, dx - n A(\beta) - \frac{\beta}{2}\\
&=\, n \ln\left(\frac{\beta/n}{1-e^{-\beta/n}}\right) - \frac{\beta}{2} - \int_0^1 \ln\left(\frac{1-e^{-\beta x/n}}{\beta x/n}\right)\, dx\\
&=\, - n \ln \left(\frac{1-e^{-\beta/n}}{\beta/n}\right) - \frac{\beta}{2} - \int_0^1 \ln\left(\frac{1-e^{-\beta x/n}}{\beta x/n}\right)\, dx\\
&=\, - n \ln \left( \frac{1-e^{-\beta/n}}{\beta/n} \cdot e^{\beta/2n}\right) - \int_0^1 \ln\left(\frac{1-e^{-\beta x/n}}{\beta x/n}\right)\, dx\\
&=\, -n \ln \left( \frac{2n}{\beta}\, \sinh\left( \frac{\beta}{2n} \right) \right) -  \int_0^1 \ln\left(\frac{1-e^{-\beta x/n}}{\beta x/n}\right)\, dx\, .
\end{aligned}$$ We know that the integrand converges to $\ln(1) = 0$ pointwise, so that the integral converges to 0 by DCT. For the other term, we know that $$\frac{2n}{\beta}\, \sinh\left( \frac{\beta}{2n} \right)\, \to\, 1\, ,$$ as $n \to \infty$. Moreover, we have the Taylor expansion $$\sinh(x)\, =\, x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots + \frac{x^{2n+1}}{(2n+1)!} + \dots\, ,$$ which means that $$\frac{\sinh(x)}{x}\, =\, 1 + \frac{x^2}{6} + \dots\, .$$ This gives $$\frac{2n}{\beta}\, \sinh\left( \frac{\beta}{2n} \right)\, =\, 1 + \frac{\beta^2}{24n^2} + \dots\, =\,
1 + O(n^{-2})\, , \quad \text { as $n \to \infty$,}$$ where $O(n^{-2})$ means that there is a function (which depends on $\beta$ as well as $n$) which may be bounded by a finite constant $C$ (which is a function $C(\beta)$ depending on $\beta$) times $n^{-2}$ for sufficiently large values of $n$. This means $$\ln\left( \frac{2n}{\beta}\, \sinh\left( \frac{\beta}{2n} \right) \right)\,
=\, O(n^{-2})\, , \quad \text { as $n \to \infty$,}$$ since $\ln(1+x) = x + O(x^2)$, as $x \to 0$. Then $$-n \ln \left( \frac{2n}{\beta}\, \sinh\left( \frac{\beta}{2n} \right) \right)\, =\, O(n^{-1})\, , \quad \text { as $n \to \infty$,}$$ which means in particular that it converges to $0$ as $n \to \infty$, (since $1/n$ does). We have seen that $R_n^{(2)}(\beta)$ does indeed converges to $0$ as $n \to \infty$.

Finally, we have $$\begin{aligned}
R_n^{(3)}(\beta)\, 
&=\, \frac{1}{2}\, \ln\left(\frac{1-e^{-\beta}}{(1-e^{-\beta/n})n}\right) - \frac{1}{2}\, \ln\left( \frac{1-e^{-\beta}}{\beta} \right)\\
&=\, \frac{1}{2}\, \ln\left( \frac{\beta}{(1-e^{-\beta/n})n}\right)\\
&=\, - \frac{1}{2}\, \ln\left( \frac{1-e^{-\beta/n}}{\beta/n} \right)\, .
\end{aligned}$$ We know that $$\frac{1-e^{-\beta/n}}{\beta/n} \to 1\, ,$$ as $n \to \infty$. Therefore, the logarithm converges to $0$. ◻
:::
