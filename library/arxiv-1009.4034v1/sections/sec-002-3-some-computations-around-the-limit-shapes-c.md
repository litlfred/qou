---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2"
section_id: sec-002-3-some-computations-around-the-limit-shapes-c
section_title: "Some computations around the limit shapes c"
section_number: 3
pages: 8-12
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.976
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young diagrams under the"
---
[]{#limitshape label="limitshape"} By using observables of diagrams, it is very easy to prove Theorem [\[firstasymptotic\]](#firstasymptotic){reference-type="ref" reference="firstasymptotic"}; let us recall briefly this proof. If $\lambda$ is a partition of size $n$ picked randomly according to a Schur-Weyl measure, then any observable of diagram $f \in \obs$ yields a random variable $f(\lambda)$. When $f=\varSigma_{\mu}$, the expectation of the random variable $\varSigma_{\mu}(\lambda)$ is easy to compute: $$\begin{aligned}
\SWa[\varSigma_{\mu}]&=\begin{cases}n^{\downarrow |\mu|}\,\tr_{(\C^{N})^{\otimes n}}(\sigma_{\mu\sqcup 1^{n-|\mu|}}) &\text{if }n \geq |\mu|,\\
0&\text{otherwise},
\end{cases}\\
&\simeq_{n \to \infty} n^{|\mu|}\,N^{\ell(\mu)-|\mu|} \simeq c^{|\mu|-\ell(\mu)}\,n^{\frac{|\mu|+\ell(\mu)}{2}},
\end{aligned}$$ assuming that $\alpha=1/2$ and $c>0$. In particular, $\SWa[\varSigma_{\mu}]$ is a $O\big(n^{\frac{\wt(\varSigma_{\mu})}{2}}\big)$, and since the $\varSigma_{\mu}$'s form a linear basis of $\obs$, one concludes that for any observable $f$, $$\SWa[f]=O\left(n^{\frac{\wt(f)}{2}}\right).$$ Now, $\varSigma_{\mu}$ and $R_{\mu+1}$ have the same top homogeneous component, so if $R_{\mu}=R_{\mu_{1}}R_{\mu_{2}}\cdots R_{\mu_{r}}$, then $$\SWa[R_{\mu}]\simeq c^{|\mu|-2\ell(\mu)}\,n^{\frac{|\mu|}{2}}\qquad;\qquad \SWa[R_{\mu}(\lambda^{*})] \simeq c^{|\mu|-2\ell(\mu)}$$ for any partition $\mu$ without part of size $1$. It implies the convergence in probability $R_{k}(\lambda^{*}) \to c^{k-2}$ for any $k \geq 2$, whence the existence of limit shapes $\Omega_{c}$ with $$\begin{aligned}
R_{\Omega_{c}}(z)&=R_{c}(z)=\frac{1}{z}\left(1+\sum_{n=2}^{\infty}c^{n-2}z^{n}\right)=\frac{1}{z}+\frac{z}{1-cz}\\
G_{\Omega_{c}}(z)&=G_{c}(z)=\frac{c+z-\sqrt{(z-c)^{2}-4}}{2(1+cz)}=\frac{2}{z+c+\sqrt{(z-c)^{2}-4}}
\end{aligned}$$ where the holomorphic square root is defined on $\C \setminus \R^{-}$ and chosen so that $\sqrt{1}=1$.

A careful analysis shows that these generating functions are indeed those of the continuous diagrams of Theorem [\[firstasymptotic\]](#firstasymptotic){reference-type="ref" reference="firstasymptotic"}, *cf.* [@Bia01 §3]. In the following, we are rather interested in the computation of the transition measures $\mu_{c}=\mu_{\Omega_{c}}$ and of the observables $\tilh_{n}(\Omega_{c})$ and $\tilp_{n}(\Omega_{c})$. Let us begin with the transition measures:

::: proposition
[]{#deformwigner label="deformwigner"} The transition measure $\mu_{c}$ is up to an homothetic transformation the Marčenko-Pastur distribution of parameter $c$: $$\begin{aligned}
d\mu_{c\leq 1}(s)&=\mathbb{1}_{s \in [c-2,c+2]}\,\frac{\sqrt{4-(s-c)^{2}}}{2\pi(1+cs)}\,ds\\
d\mu_{c> 1}(s)&=\mathbb{1}_{s \in [c-2,c+2]}\,\frac{\sqrt{4-(s-c)^{2}}}{2\pi(1+cs)}\,ds+\left(1-\frac{1}{c^{2}}\right)\delta_{-\frac{1}{c}}(s)
\end{aligned}$$ Notice that one recovers the Wigner semicircle law when $c=0$.
:::

These Marčenko-Pastur distributions are in fact well-known, since they play the same role for Wishart ensembles as the Wigner semicircle law for the GUE, see [@MP67].

::: proof
*Proof.* One uses the Perron-Stieltjes inversion formula: $$\frac{d\mu_{c}(s)}{ds}=\lim_{\eps \to 0^{+}}\frac{G_{c}(s-\I\eps)-G_{c}(s+\I\eps)}{2\I\pi}$$ which comes essentially from the calculus of residue. This formula holds for any real number $s$ such that $G_{c}$ stays bounded in the vicinity of $s$. Suppose first that $c< 1$. Then, the singularity of $G_{c}(z)$ at $z=-1/c$ is removable, so the Perron-Stieltjes formula holds for any $s$. If $s \in\, ]c-2,c+2[$, then $(s-c)^{2}-4$ is a negative real number, so $$\lim_{\eps \to 0^{\pm}}\sqrt{(s+\I\eps)^{2}-4}=\pm \I\sqrt{4-(s-c)^{2}}.$$ The other terms in $G_{c}(z)$ are continuous at $z=s$, so $$\frac{d\mu_{c}(s \in \,]c-2,c+2[)}{ds}=\frac{(\I\sqrt{4-(s-c)^{2}}) - (-\I\sqrt{4-(s-c)^{2}})}{4\I\pi(1+cs)}=\frac{\sqrt{4-(s-c)^{2}}}{2\pi(1+cs)}.$$ If $|s-c|\geq 2$, then $(s-c)^{2}-4$ is a non-negative real number, so the square root is continuous in a vicinity of $s$. Consequently, $$\frac{d\mu_{c}(s \notin \,]c-2,c+2[)}{ds}=0,$$ whence the formula for $\mu_{c<1}$. Now, if $c\geq 1$, then the Perron-Stieltjes formula do not hold anymore at $s=-1/c$, and one has to add a Dirac to take account of the singularity of $G_{c}(z)$ at this point. Since the residue of $G_{c}(z)$ at $z=-1/c$ is $$\frac{-1/c+c-\sqrt{(c+1/c)^{2}-4}}{2c}=\frac{-(c-1/c)-\sqrt{(c-1/c)^{2}}}{2c}=-\left(1-\frac{1}{c^{2}}\right),$$ one obtains indeed the formula given by Proposition [\[deformwigner\]](#deformwigner){reference-type="ref" reference="deformwigner"}. ◻
:::

Now, let us compute the observables $\tilh_{n}(\Omega_{c})$ and $\tilp_{n}(\Omega_{c})$. Of course, it amounts to expand in power series the functions $$H_{c}(z)=z^{-1}G_{c}(z^{-1})=\frac{2}{1+cz+\sqrt{(1-cz)^{2}-4z^{2}}}$$ and $P_{c}(z)=zH_{c}'(z)/H_{c}(z)$, but the calculations are not at all trivial, and we shall need in particular the following hypergeometric identity:

::: lemma
[]{#whatever label="whatever"} For any non-negative integer $m$ and $k$, $$\sum_{l=0}^{k}\sum_{u=0}^{m} \frac{(2k+2+u-2l)\,\,m+2l+2-u!\,2k-2l+u!}{(m-u+l+2)(m-u+l+1)\,m-u!\,u!\,l!\,l+1!\,k-l!\,k-l+1!}=  \frac{m+2k+4}{m+k+2}\,\times\,\frac{m+2k+2!}{m!\, k!\,k+2!}.$$
:::

::: proof
*Proof.* For such (multivariate) hypergeometric identities, one can use the theory of Wilf-Zeilberger, see [@PWZ97], [@WZ92a] and [@WZ92b]. More precisely, there is an algorithm that provides recurrence relations satisfied by both sides of the identity, and on the other hand, it is easy to show that the identity holds for certain values of $m$ and $k$. Consequently, the identity is indeed true for all $m$ and $k$; we leave the details of the computation of the recurrence relations to any computer algebra system. ◻
:::

::: proposition
[]{#obslimitshape label="obslimitshape"} The $n$-th moment of the law $\mu_{c}$ is $$\tilh_{n}(\Omega_{c})=\mu_{c}(s^{n})=\sum_{k=1}^{\lfloor \frac{n}{2}\rfloor} \frac{n^{\downarrow 2k}}{(n-k+1)(n-k)\,k!\,k-1!}\,c^{n-2k},$$ and the $n$-th moment of interlacing coordinates is $$\tilp_{n}(\Omega_{c})=\sum_{k=1}^{\lfloor \frac{n}{2}\rfloor} \frac{n^{\downarrow 2k}}{(n-k)\,k!\,k-1!}\,c^{n-2k}.$$
:::

When $c=0$, one recovers the fact that the even moments of the semicircle law are the Catalan numbers: $\tilh_{2n}(\Omega_{0})=C_{n}$.

::: proof
*Proof.* The expansion of $2/H_{c}(z)$ gives $$\begin{aligned}
\frac{2}{H_{c}(z)}&=1+cz+(1-cz)\sqrt{1-4\left(\frac{z}{1-cz}\right)^{2}}\\
&=1+cz+(1-cz)\left(1-2\sum_{m=0}^{\infty}C_{m}\left(\frac{z}{1-cz}\right)^{2(m+1)}\right)\\
&=2\left(1-\sum_{m=0}^{\infty}C_{m}\,\frac{z^{2m+2}}{(1-cz)^{2m+1}}\right)
\end{aligned}$$ because $\sum_{m=0}^{\infty}C_{m}\,x^{m}=\frac{1-\sqrt{1-4x}}{2x}$. Then, $$H_{c}(z)=1+\sum_{m=0}^{\infty}\sum_{r=1}^{\infty}\left\{\sum_{m_{1}+m_{2}+\cdots+m_{r}=m}\!\!\!\!\! C_{m_{1}}C_{m_{2}}\cdots C_{m_{r}}\right\}\frac{z^{2m+2r}}{(1-cz)^{2m+r}}.$$ Let us denote by $f(m,r)$ the sum between brackets. One has $f(m,0)=0$, $f(m,1)=C_{m}$ and $f(m,r)=f(m+1,r-1)-f(m+1,r-2)$ because of the recurrence relation satisfied by Catalan numbers. Consequently, one can show by induction that $$f(m,r)=r\,\frac{2m+r-1!}{m!\,m+r!}.$$ Finally, one can use the expansion $\frac{1}{(1-cz)^{2m+r}}=\sum_{l=0}^{\infty} \binom{2m+r+l-1}{l}\,c^{l}z^{l}$ to obtain: $$\begin{aligned}
H_{c}(z)&=1+\sum_{m=0}^{\infty}\sum_{r=1}^{\infty}\sum_{l=0}^{\infty} r\frac{2m+r+l-1!}{l!\,2m+r-1!}\,\frac{2m+r-1!}{m!\,m+r!}\,c^{l}\,z^{2m+2r+l}\\
&=1+\sum_{n=2}^{\infty}z^{n}\left\{\sum_{k=1}^{\lfloor \frac{n}{2}\rfloor }\left(\sum_{r=1}^{k}r\, \frac{(n-r-1)^{\downarrow 2k-r-1}}{k!\,k-r!}\right)c^{n-2k}\right\}
\end{aligned}$$ For any positive integers $a$, $b$ and $c$, $\binom{a+1}{b+c+1}=\sum_{j\geq 1} \binom{j}{b}\binom{a-j}{c}$ --- this identity can be obtained combinatorially by grouping the parts of size $b+c+1$ of $\lle 1,a+1\rre$ according to the value of their $(b+1)$-th element. In particular, $$\sum_{j\geq 1}\,j\binom{n-j-1}{n-k-1}=\binom{n}{n-k+1}$$ if one takes $a=n-1$, $b=1$ and $c=n-k-1$. As a consequence, the term between parentheses in the previous expression is just $\frac{n^{\downarrow 2k}}{(n-k+1)(n-k)\,k!\,k-1!}$, whence the formula for the $\tilh_{n}(\Omega_{c})$'s.

As for the $\tilp_{n}(\Omega_{c})$'s, one can use Newton relations between the power sums and the complete homogeneous functions in the algebra of symmetric functions, or expand in power serie the function $P_{c}(z)$ --- it leads to the same computations. First, one sees that: $$\begin{aligned}
P_{c}(z)&=-\frac{z}{1+cz+\sqrt{(1-cz)^{2}-4z^{2}}}\left(c - \frac{c(1-cz)+4z}{\sqrt{(1-cz)^{2}-4z^{2}}}\right)\\
&=\frac{z\,H_{c}(z)}{2}\left(\frac{c(1-cz)+4z}{\sqrt{(1-cz)^{2}-4z^{2}}}-c\right)
\end{aligned}$$ $$\begin{aligned}
&=\frac{z\,H_{c}(z)}{2}\left(c\sum_{n=1}^{\infty}\binom{2n}{n}\left(\frac{z}{1-cz}\right)^{2n}+4\sum_{n=0}^{\infty}\binom{2n}{n}\left(\frac{z}{1-cz}\right)^{2n+1}\right)\\
&=\frac{z\,H_{c}(z)}{2}\left(\sum_{n=0}^{\infty}\sum_{r=0}^{\infty}\left\{cz\binom{2n+1+r}{r}\binom{2n+2}{n+1}+ 4\binom{2n+r}{r}\binom{2n}{n}\right\}c^{r}z^{2n+1+r}\right)
\end{aligned}$$ If $n_{1}\geq 2$, then the coefficient of $z^{n_{1}}$ in $zH_{c}(z)$ is $\tilh_{n-1}(\Omega_{c})$, that is to say: $$\sum_{k=1}^{\lfloor \frac{n_{1}-1}{2}\rfloor} \frac{n_{1}-1!}{(n_{1}-k)(n_{1}-k-1)\,k!\,k-1!\,n_{1}-1-2k!}\,c^{n_{1}-2k-1}$$ On the other hand, if $n_{2} \geq 1$, then the coefficient of $z^{n_{2}}$ in the second term $T_{c}(z)$ of the product $P_{c}(z)$ is: $$\sum_{l=0}^{\lfloor \frac{n_{2}}{2}\rfloor-1}\!\!\!\!\frac{n_{2}-1!}{n_{2}-2l-2!\,l!\,l+1!}\,c^{n_{2}-2l-1}+\,\,2\!\!\sum_{l=0}^{\lfloor\frac{n_{2}-1}{2} \rfloor}\!\!\!\!\frac{n_{2}-1!}{n_{2}-2l-1!\,l!\,l!}\,c^{n_{2}-2l-1}=\frac{1}{n_{2}}\!\!\sum_{l=0}^{\lfloor\frac{n_{2}-1}{2}\rfloor}\!\!\!\! \frac{n_{2}+1!}{n_{2}-2l-1!\,l!\,l+1!}\,c^{n_{2}-2l-1}$$ One also has to take account of the coefficient of $z$ in $zH_{c}(z)$, that is equal to $1$. So, for $n \geq 3$, the coefficient of $z^{n}$ in $P_{c}(z)$ is equal to the sum of the following expressions: $$\begin{aligned}
A&=\frac{1}{n-1}\sum_{k=1}^{\lfloor\frac{n}{2} \rfloor} \frac{n!}{n-2k!\,k!\,k-1!}\,c^{n-2k}\\
B&=\!\!\!\!\!\!\sum_{\substack{n_{1}+n_{2}=n\\n_{1}\geq 2,\,\,n_{2}\geq 1\\2\leq 2k_{1}\leq n_{1}-1\\ 0 \leq 2k_{2} \leq n_{2}-1}}\frac{(n_{2}+1)\,n_{1}-1!\,n_{2}-1!\,n_{1}-k_{1}-2!}{n_{1}-k_{1}!\,k_{1}!\,k_{1}-1!\, n_{1}-2k_{1}-1!\,n_{2}-2k_{2}-1!\,k_{2}!\,k_{2}+1!}\,c^{n-2k_{1}-2k_{2}-2}\\
&=\!\!\!\!\!\!\sum_{\substack{n_{1}+n_{2}=n-3\\n_{1}\geq 0,\,\,n_{2}\geq 0\\0\leq 2k_{1}\leq n_{1}-1\\ 0 \leq 2k_{2} \leq n_{2}}}\frac{(n_{2}+2)\,n_{1}+1!\,n_{2}!\,n_{1}-k_{1}-1!}{n_{1}-k_{1}+1!\,k_{1}!\,k_{1}+1!\, n_{1}-2k_{1}-1!\,n_{2}-2k_{2}!\,k_{2}!\,k_{2}+1!}\,c^{n-2k_{1}-2k_{2}-4}\\
&=\!\!\!\!\!\!\sum_{\substack{0\leq u \leq n-4-2k\\0\leq k = k_{1}+k_{2}}} \frac{f(k_{1},k_{2},u,n)\,n-2k_{2}-2-u!\,2k_{2}+u!}{n-u-2k-4!\,u!\,k_{1}!\,k_{1}+1!\,k_{2}!\,k_{2}+1!}\,c^{n-2k-4}
\end{aligned}$$ where $f(k_{1},k_{2},u,n)=\frac{2k_{2}+2+u}{(n-u-k_{1}-2k_{2}-2)(n-u-k_{1}-2k_{2}-3)}$. Consequently, $\tilp_{n}(\Omega_{c})$ is indeed a polynomial in $c$ with all terms of even degree or all terms of odd degree. The term of degree $n-2$ comes exclusively from $A$, and is $$\frac{1}{n-1}\,\frac{n!}{n-2!}=n=\frac{n^{\downarrow 2} }{n-1\,1!\,0!},$$ so the formula of Proposition [\[obslimitshape\]](#obslimitshape){reference-type="ref" reference="obslimitshape"} is true for the coefficient of $c^{n-2}$. For the other coefficients, one has to show that if $k\geq 0$ and $n-2k-4 \geq 0$, then $$\sum_{\substack{0\leq u \leq n-4-2k\\ k = k_{1}+k_{2}}} \frac{f(k_{1},k_{2},u,n)\,n-2k_{2}-2-u!\,2k_{2}+u!}{n-u-2k-4!\,u!\,k_{1}!\,k_{1}+1!\,k_{2}!\,k_{2}+1!}=\frac{n^{\downarrow 2k+4}}{(n-k-2)(n-1)\,k+2!\,k!}.$$ Indeed, the left-hand side comes from $B$, and the right-hand side is the difference of the coefficient in the formula of Proposition [\[obslimitshape\]](#obslimitshape){reference-type="ref" reference="obslimitshape"} and of the coefficient coming from $A$. Up to a change of index, this last identity is exactly Lemma [\[whatever\]](#whatever){reference-type="ref" reference="whatever"}. Finally, it is easy to verify that the formula for the moments $\tilp_{n}(\Omega_{c})$ remains true for $n=1,2$. ◻
:::

These calculations are of course unessential, but we shall need the precise expression of the moments $\tilp_{n}(\Omega_{c})$ in our study of the fluctuations $\Delta_{\lambda,c}(s)=\lambda^{*}(s)-\Omega_{c}(s)$.
