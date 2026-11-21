---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-014-33-main-result
section_title: "Main Result"
section_number: 3.3
pages: 41-44
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.979
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Using these results, along with the method of Chatterjee and Ledoux, we are able to prove the following result:

::: thm
Take any $1\leq k\leq n$ and an $n$-dimensional Hermitian matrix $G$. Let $A$ be the $k\times k$ matrix consisting of the first $k$ rows and $k$ columns of the matrix obtained by conjugating $G$ by a rotation matrix $R^{\theta}_{ij}\in SO(n)$ chosen uniformly at random. If we let $F$ be the expected spectral distribution of $A$, then for each $r>0$, $$\mathbb{P}\left(\|F_A-F\|_{\infty}\geq \frac{1}{\sqrt{k}}+r\right)\leq 12\sqrt{k}\exp\left(-r\sqrt{\frac{k}{32}}\right)$$
:::

::: proof
*Proof.* The proof of this theorem uses the method introduced by Chatterjee and Ledoux [@ChatLed] with appropriate changes made to apply to the situation we are considering.\
\
Let $R_{ij}(\theta)\in\mathrm{SO}(n)$ and let $A$ be as stated above. Note that since $A$ is a compression of a Hermitian operator, it will also be Hermitian. Fix $x\in\mathbb{R}$. Let $f(A):=F_A(x)$, where $F_A(x)$ is the empirical spectral distribution of $A$. Let $Q$ be the transition operator as defined in (1) and let $|||.|||_\infty$ be as in (2). Using Lemma 2.2 from [@Bai], we know that for any two Hermitian matrices $A$ and $B$ of order $k$, $$\|F_A-F_B\|_{\infty}\leq\frac{\mathrm{rank}(A-B)}{k}$$ In our case, taking one step in Kac's walk is equivalent to rotation in a random plane by a random angle. Hence $A$ and $R_{ij}^{\theta}A$ will differ in at most two rows and two columns, bounding the difference in rank by $2$, so $$\|f(A)-f(R_{ij}^{\theta}A)\|_{\infty}\leq\frac{2}{k}$$ Using (2), $$|||f|||_\infty^2 = \frac 1 {2\binom{n}{2}} \sup_{A\in SO(n)}\sum_{1\leq i<j\leq n} \mathbb{E}[f(A)-f(R_{ij}^{\theta}A)]^2$$ $$\leq \frac 1 {2} \left(\frac{2}{k}\right)^2\left(\frac{2k}{n}\right)=\frac{4}{kn}$$ where the $\frac{2k}{n}$ comes from the probability that both $i$ and $j$ are greater than $k$, in which case, $A$ and $R^{\theta}_{ij}A$ will be the same. From Theorems 2.1 and 2.2, we have that $$\mathbb{P}(|F_A(x)-F(x)|\geq r)\leq 6\exp\left(-\frac{r}{2}\frac{\sqrt{\frac{1}{2}\frac{n+2}{(n-1)n}}}{\sqrt{\frac{4}{kn}}}\right)$$ $$=6\exp\left(-r/2\sqrt{\frac{1}{8}\frac{k(n+2)}{n-1}}\right)\leq 6\exp\left(-r/2\sqrt{\frac{k}{8}}\right)$$ This is true for any $x$. Now, if we let $F_A(x-):=\lim_{y\uparrow x}F_A(y)$, then we have $\mathbb{E}F_A(x-)=\lim_{y\uparrow x}F(y)=F(x-)$. Hence, for $r>0$, $$\mathbb{P}(|F_A(x-)-\mathbb{E}F_A(x-)|>r)\leq \lim_{y\uparrow x}\mathbb{P}(|F_A(y)-F(y)|>r)$$ $$\leq 6\exp\left(-r/2\sqrt{\frac{k}{8}}\right)$$ This holds for all $r$, so we can replace $>$ by $\geq$. Next we will fix $\ell\in\mathbb{Z}_{\geq 2}$. For $1\leq i<\ell$, let $$t_i:=\inf\{x:F(x)\geq i/\ell\}$$ and $t_0=-\infty$, $t_\ell=\infty$. Then for each $i$, $F(t_{i+1})-F(t_i)\leq 1/\ell$. Let $$\triangle=(\max_{1\leq i<\ell}|F_A(t_i)-F(t_i)|)\wedge (\max_{1\leq i<\ell}|F_A(t_i-)-F(t_i-)|)$$ Take any $x\in\mathbb{R}$. Let $i$ be an index where $t_i\leq x<t_{i+1}$. Then $$F_A(x)\leq F_A(t_{i+1}-)\leq F(t_{i+1}-)+\triangle\leq F(x)+1/\ell +\triangle$$ and $$F_A(x)\geq F_A(t_i)\geq F(t_i)-\triangle\geq F(x)-1/\ell-\triangle$$ Using these two facts, we get that $$\|F_A-F\|_{\infty}\leq 1/\ell+\triangle$$ Then for any $r>0$, we have $$\mathbb{P}(\|F_A-F\|_{\infty}\geq 1/\ell+r)\leq 12(\ell-1)\exp\left(-r\sqrt{\frac{k}{32}}\right)$$ Letting $\ell=k^{1/2}+1$, we have $$\mathbb{P}(\|F_A-F\|_{\infty}\geq \frac{1}{\sqrt{k}}+r)\leq 12\sqrt{k}\exp\left(-r\sqrt{\frac{k}{32}}\right)$$ which concludes the proof of our theorem. ◻
:::
