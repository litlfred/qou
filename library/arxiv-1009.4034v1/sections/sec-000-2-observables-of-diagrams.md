---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2"
section_id: sec-000-2-observables-of-diagrams
section_title: "Observables of diagrams"
section_number: 2
pages: 5-12
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.992
---
[]{#obs label="obs"} In the setting of random partitions, the algebra of polynomial functions[^1] on Young diagrams and its various bases play an extremely important role that can be compared to the one played by the moments of a real random variable. Hence, the **generating function** of a Young diagram $\lambda$ is defined by $$G_{\lambda}(z)=\frac{\prod_{i=1}^{v-1}z-y_{i}}{\prod_{i=1}^{v}z-x_{i}},$$ where $x_{1}<y_{1}<x_{2}<y_{2}<\cdots<x_{v-1}<y_{v-1}<x_{v}$ are the **interlacing coordinates** of $\lambda$, that is to say, the sequences of local minima and local maxima of the function $s\mapsto \lambda(s)$. Alternatively, if $\sigma(s)=\frac{\lambda(s)-|s|}{2}$, then $$G_{\lambda}(z)=\frac{1}{z}\exp\left(-\int_{\R}\frac{\sigma'(s)}{z-s}\,ds\right).$$ This latter definition allows to consider the generating function of more general objects such as **continuous Young diagrams**, *i.e.*, functions $s\mapsto \omega(s)$ that satisfy the two following properties:

1.  $\omega$ is Lipschitz with constant $1$, *i.e.*, $|\omega(s)-\omega(t)|\leq |s-t|$ for all $s,t$.

2.  $\omega(s)=|s|$ for $s$ big enough.

Given a (continuous) diagram $\lambda$, the coefficients $\tilh_{n}(\lambda)$ of the power serie $z^{-1}G_{\lambda}(z^{-1})$ generate an algebra $\obs$ of **observables of diagrams**. One may also consider as an algebraic basis for $\obs$ the coefficients $\tilp_{n}(\lambda)$ given by the formula $$z^{-1}G_{\lambda}(z^{-1})=1+\sum_{n=1}^{\infty} \tilh_{n}(\lambda)\,z^n=\exp\left(\sum_{n=1}^{\infty} \frac{\tilp_{n}(\lambda)}{n}\,z^{n}\right).$$ For a true Young diagram $\lambda$, $\tilp_{n}(\lambda)=\sum_{i=1}^{v}(x_{i})^{n}-\sum_{i=1}^{v-1}(y_{i})^{n}$ is the $n$-th moment of the interlacing coordinates, whereas for a continuous diagram, one can give the following formula: $$\tilp_{n}(\omega)=\int_{\R} \sigma''(s)\,s^{n}\,ds=\frac{1}{(n+1)(n+2)}\int_{\R}\sigma(s)\,s^{n+2}\,ds$$ Notice that $\tilh_{1}(\lambda)=\tilp_{1}(\lambda)=0$ for any (continuous) diagram $\lambda$; on the other hand, one can show that the other coefficients are algebraically independant (viewed as functions on diagrams). So, $$\obs=\C[\tilh_{2},\tilh_{3},\ldots]=\C[\tilp_{2},\tilp_{3},\ldots],$$ see [@IO02 §2]. The **weight grading** on this algebra is then defined by setting $\wt(\tilp_{k\geq 2})=k$, and it provides a filtration of algebra on $\obs$ that is well-behaved with respect to scaling of continuous diagrams. More precisely, if $\omega$ is a continuous diagram and if $\omega^{t}$ is the scaled diagram defined by $$\omega^{t}(s)=\frac{\omega(st)}{t}$$ (see figure [\[scaling\]](#scaling){reference-type="ref" reference="scaling"}), then for any homogeneous observable $f$ of weight $k$, $f(\omega^{t})=t^{k}\,f(\omega)$. In particular, if $\lambda$ is a true Young diagram and if $\lambda^{*}=\lambda^{1/\sqrt{|\lambda|}}=\lambda^{1/\sqrt{n}}$, then $f(\lambda^{*})=n^{-\frac{k}{2}}\,f(\lambda)$.

Another algebraic basis of $\obs$ consists in the **free cumulants** of the transition measures of the continuous Young diagrams. First, if $\lambda$ is a (continuous) Young diagram, we define its **transition measure** $\mu_{\lambda}$ by $$G_{\lambda}(z)=\int_{\R}\frac{\mu_{\lambda}(s)}{z-s}.$$ In other words, the generating function of $\lambda$ is the Stieltjes transform of the transition measure. Notice that the $\tilh_{n}(\lambda)$'s are precisely the moments of the compactly supported measure $\mu_{\lambda}$. Then, the free cumulants of the measure $\mu_{\lambda}$ are the coefficients of the formal inverse $R_{\lambda}$ of $G_{\lambda}$ in a neighboorhood of infinity: $$R_{\lambda}(G_{\lambda}(z))=z \,\,\,\text{for }z\text{ big enough}\qquad;\qquad R_{\lambda}(z)=\frac{1}{z}\left(1+\sum_{n=1}^{\infty}R_{n}(\mu_\lambda)\,z^{n}\right)$$ see [@VDN92] for the uses of this notion in free probability. By Lagrange inversion, the free cumulants also satisfy the formula $$R_{n+1}(\lambda)=R_{n+1}(\mu_{\lambda})=-\frac{1}{n}[z^{-1}](G_{\lambda}(z))^{-n},$$ and $R_{n+1}$ is therefore an observable of diagrams that is homogeneous with weight $n+1$. R. Speicher has given a simple combinatorial interpretation of the change of basis formulas between the $\tilh$'s and the $R$'s, see [@NS06]. These formulas implie in particular that the $R_{k\geq 2}$'s are algebraically independant, so $\obs=\C[R_{2},R_{3},\ldots]$.

Finally, another algebraic basis comes from the so-called **central characters**, that allow to relie the algebra $\obs$ to the representation theory of the symmetric groups. If $\lambda$ and $\mu$ are two partitions of same size $n$, one denotes by $\chi^{\lambda}(\mu)$ the value of the normalized irreducible character of $\sym_{n}$ of label $\lambda$ on a permutation $\sigma_{\mu}$ of cycle type $\mu$. Then, if $\lambda$ and $\mu$ are two partitions of sizes $n$ and $k$, one sets: $$\varSigma_{\mu}(\lambda)=\begin{cases} n^{\downarrow k}\,\chi^{\lambda}(\mu\sqcup 1^{n-k})&\text{if }n\geq k,\\
0&\text{otherwise}.
\end{cases}$$ Here, $\mu\sqcup 1^{n-k}$ is the completed partition obtained by adding parts of size $1$ to $\mu$, and $n^{\downarrow k}$ is the falling factorial $n(n-1)\cdots(n-k+1)$. It is true, although totally non trivial, that the $\varSigma_{\mu}$'s are observables of diagrams; *cf.* [@IO02 §3-4]. More precisely, $\wt(\varSigma_{\mu})=|\mu|+\ell(\mu)$, and the top homogeneous component of $\varSigma_{\mu}$ is $$R_{\mu+1}=R_{\mu_{1}+1}R_{\mu_{2}+1}\cdots R_{\mu_{r}+1},$$ see [@Bia98] and [@IO02 §10]. As a consequence, $\obs=\C[\varSigma_{1},\varSigma_{2},\ldots]$ is freely generated by the central characters of cycles, and one has a factorization property of characters in top homogeneous component: $$\varSigma_{\mu_{1}}\,*\,\varSigma_{\mu_{2}}=\varSigma_{\mu_{1}\sqcup \mu_{2}}+\big(\text{observable of weight less than }\mu_{1}+\mu_{2}+\ell(\mu_{1})+\ell(\mu_{2})-2\big)$$ In fact, there exists multivariate polynomials with non-negative integer coefficients $K_{k}$ such that $\varSigma_{k}=K_{k}(R_{k+1},R_{k},\ldots,R_{2})$ for any $k \geq 1$; these **Kerov polynomials** are studied for instance in [@DFS08]. In §[\[core\]](#core){reference-type="ref" reference="core"}, we will rather have to exprime the $\tilp$'s as polynomials in the $\varSigma$'s. We refer to [@IO02 Proposition 3.7] for a proof of the following result:

::: proposition
[]{#changeofbasis label="changeofbasis"} For $k \geq 2$, $\tilp_{k}$ is the top homogeneous component of weight $k$ of the observable $$\sum_{\substack{\mu=1^{m_{1}}2^{m_{2}}\cdots s^{m_{s}}\\|\mu|+\ell(\mu)=k }} \frac{k^{\downarrow \ell(\mu)}}{\prod_{i\geq 1} m_{i}!}\prod_{i\geq 1}(\varSigma_{i})^{m_{i}}\,.$$
:::

::: examples
Let us write the first $\tilp_{k}$'s in the linear basis of central characters $(\varSigma_{\mu})_{\mu \in \bigsqcup_{n \in \N}\Part_{n}}$: $$\begin{aligned}
\tilp_{1}&=0\quad\qquad\,;\qquad\tilp_{2}=2\varSigma_{1}\\
\tilp_{3}&=3\varSigma_{2}\qquad;\qquad\tilp_{4}=4\varSigma_{3}+6\varSigma_{1,1}+2\varSigma_{1}\\
\tilp_{5}&=5\varSigma_{4}+20\varSigma_{2,1}+15\varSigma_{2}\\
\tilp_{6}&=6\varSigma_{5}+30\varSigma_{3,1}+15\varSigma_{2,2}+20\varSigma_{1,1,1}+30\varSigma_{1,1}+60\varSigma_{3}+2\varSigma_{1}
\end{aligned}$$ Hence, one sees for instance that $\tilp_{6}$ is the top homogeneous component of $6\varSigma_{5}+30\varSigma_{3,1}+15\varSigma_{2,2}+20\varSigma_{1,1,1}$, and if one uses the factorization property of the central characters, one sees that these formulas agree with Proposition [\[changeofbasis\]](#changeofbasis){reference-type="ref" reference="changeofbasis"}.
:::

# Some computations around the limit shapes $\Omega_{c}$ {#limitshape}

By using observables of diagrams, it is very easy to prove Theorem [\[firstasymptotic\]](#firstasymptotic){reference-type="ref" reference="firstasymptotic"}; let us recall briefly this proof. If $\lambda$ is a partition of size $n$ picked randomly according to a Schur-Weyl measure, then any observable of diagram $f \in \obs$ yields a random variable $f(\lambda)$. When $f=\varSigma_{\mu}$, the expectation of the random variable $\varSigma_{\mu}(\lambda)$ is easy to compute: $$\begin{aligned}
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

[^1]: In the same setting, another fruitful approach relie on determinantal point processes, see *e.g.* [@BO00] and [@BO05].
