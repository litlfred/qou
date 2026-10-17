---
doc_id: arxiv-1105.0091v1
doc_title: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra"
section_id: sec-005-6-pitman-operators-and-a-link-with-conditioned-r
section_title: "Pitman operators and a link with conditioned random walks and brownian matrices"
section_number: 6
pages: 42-57
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.975
doc_brief: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra — In this paper, we review the representation theory of the inﬁnite symmetric group, and"
---
[]{#oconnell label="oconnell"} In the previous paragraphs, we have shown that the rows and columns of a partition $\lambda$ of law $\mathbb{P}_{n,\omega}$ have limit frequencies $\alpha_{i}$ and $\beta_{j}$, and gaussian fluctuations when gathered for equal coordinates of the point $\omega$ of the Thoma simplex. To treat the case of equal parameters, we shall use O'Connell's theory ([@OC03]) that relates the Robinson-Schensted algorithm to an operation on multidimensional paths, and therefore random tableaux coming from $\omega$-shuffles to random walks conditioned to stay in a Weyl chamber. These random walks are also related to the processes of eigenvalues of brownian traceless Hermitian matrices. Thus, the fluctuations of a block of $d$ rows or columns corresponding to equal coordinates of $\omega$ are the same as those of the eigenvalues of a gaussian matrix in $\mathfrak{su}(d,\mathbb{C})$, up to the additional gaussian term described by Theorem [\[almostgeom\]](#almostgeom){reference-type="ref" reference="almostgeom"}; see Theorem [\[maingeom\]](#maingeom){reference-type="ref" reference="maingeom"} for a precise statement. We shall prove this progressively, starting from the toy model of $2$-shuffles, then introducing **Pitman operators** in order to treat the case of $d$-shuffles, and finally studying the general case.

## The case of $2$-shuffles

To begin with, let us treat minutely the case when $$\omega=\left(\left(\frac{1}{2},\frac{1}{2},0,0,\ldots\right),(0,0,\ldots)\right).$$ The corresponding $\omega$-shuffles (which we shall call **$\mathbf{2}$-shuffles**) are easy to describe. Indeed, for any $n$, a random permutation of law $\mathbb{Q}_{n,\omega}$ can be obtained by shuffling together two blocks of size $n_{1}$ and $n_{2}=n-n_{1}$ with $n_{1} \sim \mathcal{B}(n,\frac{1}{2})$, that is to say that $$\mathbb{P}[n_{1}=k]=\frac{1}{2^{n}}\,\binom{n}{k}.$$ We recall that all the $\binom{n}{k}$ shuffles of two blocks of sizes $k$ and $n-k$ are equiprobable. Thus, if $b_{1}, \ldots,b_{n}$ are independent identically distributed variables with $\mathbb{P}[b_{i}=1]=\mathbb{P}[b_{i}=2]=1/2$, then one can produce a permutation of law $\mathbb{Q}_{n,\omega}$ by:

-   setting $n_{1}=\mathrm{card}\,\{i \,\,|\,\, b_{i}=1\}$, $n_{2}=\mathrm{card}\,\{i \,\,|\,\, b_{i}=2\}$.

-   sending the integers of $\left[\!\left[1,n_{1}\right]\!\right]$ in this order to the positions $i$ such that $b_{i}=1$, and then sending the integers of $\left[\!\left[n_{1}+1,n_{1}+n_{2}\right]\!\right]$ in this order to the positions $i$ such that $b_{i}=2$.

For instance, if the sequence of Bernoulli variables is $121121221$, then the corresponding permutation[^1] will be $162374895$. This explicit construction of $2$-shuffles will enable us to relate them to random walks --- here, the random walk that we shall consider is:

<figure>
<div class="center">
<p><span><span> <embed src="graphic_randomwalk.pdf" /></span></span></p>
</div>
<figcaption>Random walk associated to the <span class="math inline">2</span>-shuffle <span class="math inline">162374895 = Std(121121221)</span>.</figcaption>
</figure>

Given a permutation $\sigma$ obtained by standardization from a word $w$ in $\{1,2\}^{*}$, the shape of the tableau $P(\sigma)$ is the same as the shape of the tableau $P(w)$. Actually, for any $k \leq n$, if $P_{k}(\sigma)$ (respectively, $P_{k}(w)$) is the tableau obtained after Schensted insertion of the $k$ first letters of $\sigma$ (resp., of the $k$ first letters of $w$), then $P_{k}(\sigma)$ has the same shape as $P_{k}(w)$. Hence, we will study the random process $(P(w_{k}))_{k \geq 0}$, where $w_{k}=b_{1}b_{2}\ldots b_{k}$ is a random word in $\{1,2\}^{k}$ with independent Bernoulli letters. This process takes its values in $$\mathrm{SST}\{1,2\}=\{\text{semi-standard tableaux with entries in }\{1,2\}\}.$$ A semi-standard tableau with entries in $\{1,2\}$ has at most two rows, and the entries in the second row are all equal to $2$. Thus, if one knows the size $n$ of the tableau, then it is entirely determined by the number $m_{11}$ of entries $1$ on the first row, and by the number $m_{12}$ of entries $2$ on the first row:

::: center
![image](graphic_SST2.pdf)
:::

with $m_{22}=n-m_{11}-m_{12}$. So, let us study in detail the random process $(m_{11}(k),m_{12}(k))$. For this purpose, we introduce the random walk $X_{k}=3k-2(b_{1}+b_{2}+\cdots+b_{k})$; this is a standard random walk on $\mathbb{Z}$, starting from $0$.

::: lemma
[]{#2shuffle label="2shuffle"} For any $k$, $m_{11}(k)=\frac{k+X_{k}}{2}$ and $m_{12}(k)=S_{k}-X_{k}$, where $S_{k}=\sup_{j \leq k}X_{j}$.
:::

::: proof
*Proof.* The quantity $m_{11}(k)$ is just the number of "$1$" in the sequence $b_{1},\ldots,b_{k}$. Hence, $$m_{11}(k)=\sum_{i=1}^{k} 2-b_{i}=2k-(b_{1}+b_{2}+\cdots+b_{k})=\frac{k+X_{k}}{2}.$$ As for $m_{12}(k)$, let us prove the result by induction on $k$. Supposing $m_{12}(k)=S_{k}-X_{k}$, let us compute $m_{12}(k+1)$:

1.  If $b_{k+1}=1$, one inserts a letter $1$ in the first row. Suppose that $m_{12}(k)=0$. Then, $m_{12}(k+1)$ is also equal to $0$, so $S_{k}=X_{k}$, and $X_{k+1}=X_{k}+1$, because $b_{k+1}=1$ means that we go up. This implies that $S_{k+1}=X_{k+1}$, so $m_{12}(k+1)=0=S_{k+1}-X_{k+1}.$ On the contrary, suppose that $m_{12}(k)\geq 1$. Then, the letter $1$ will replace a letter $2$, so $$m_{12}(k+1)=m_{12}(k)-1=S_{k}-X_{k}-1.$$ On the other hand, since $X_{k}=S_{k}-m_{12}(k) \leq S_{k}-1$, $X_{k+1}=X_{k}+1 \leq S_{k}$, so $S_{k}=S_{k+1}$. But then, $m_{12}(k+1)=S_{k}-(X_{k}+1)=S_{k+1}-X_{k+1}$, so the identity holds again at rank $k+1$.

2.  If $b_{k+1}=2$, one inserts a letter $2$ at the end of the first row, so $$m_{12}(k+1)=m_{12}(k)+1=S_{k}-X_{k}+1.$$ On the other hand, $b_{k+1}=2$ means that the random walk goes down, so $X_{k+1}=X_{k}-1$ and $S_{k}=S_{k+1}$. Then, $m_{12}(k+1)=S_{k}-(X_{k}-1)=S_{k+1}-X_{k+1}$.

Hence, if $\ell_{k}(\sigma)$ is the length of the longest increasing subword of $\sigma(1)\cdots \sigma(k)$, then $$\ell_{k}(\sigma)=m_{11}(k)+m_{12}(k)=\frac{k}{2}+ \frac{2S_{k}-X_{k}}{2} ,$$ and this for any $k\leq n$. ◻
:::

It is known since Pitman's works (see [@Pit75]) that if $(X_{k})_{k \in \mathbb{N}}$ is a standard random walk on $\mathbb{Z}$, then $(2S_{k}-X_{k})_{k \in \mathbb{N}}$ is a markovian random process on the non-negative integers, with $$p(k,k+1)=\frac{k+2}{2(k+1)}\qquad;\qquad p(k,k-1)=\frac{k}{2(k+1)}.$$ After scaling by $n$ on the $x$-axis and $\sqrt{n}$ on the $y$-axis, the random process $(2S_{k}-X_{k})_{k \in \left[\!\left[0,n\right]\!\right]}$ converges in law in $\mathscr{C}([0,1])$ to a **3-dimensional Bessel process** $(\mathrm{BES}^{3}_{t})_{t \in [0,1]}$, whose trajectorial laws are the same as $(2S_{t}-B_{t})_{t \in [0,1]}$, with $(B_{t})_{t \in [0,1]}$ standard brownian motion and $S_{t}=\sup_{s\leq t}B_{s}$. Alternatively, $(\mathrm{BES}^{3}_{t})_{t \in [0,1]}$ can be defined as the solution of the stochastic differential equation $$dY_{t}=dB_{t}+\frac{dt}{Y_{t}},$$ see [@RY91 Chapter 6, §3]. For this reason, and using Itô's calculus, one can show that $(\mathrm{BES}^{3}_{t})_{t \in [0,1]}$ has the same trajectorial laws as the euclidian norm $(\sqrt{X_{t}^{2}+Y_{t}^{2}+Z_{t}^{2}})_{t \in [0,1]}$ of a $3$-dimensional brownian motion. In particular, this allows to compute the density of the law of $\mathrm{BES}^{3}_{t}$: $$\mathrm{BES}^{3}_{t}\sim \mathbf{1}_{y \geq 0} \,\sqrt{\frac{2}{\pi\,t^{3}}}\,y^{2}\,\mathrm{e}^{-\frac{y^{2}}{2t}}\,dy.$$

With these classical results from probability, Lemma [\[2shuffle\]](#2shuffle){reference-type="ref" reference="2shuffle"} can be reinterpreted as follows:

::: proposition
[]{#bessel3 label="bessel3"} Let $\sigma$ be a random permutation obtained by a $2$-shuffle. We denote $$L_{t \in [0,1[}^{(n)}=\frac{2}{\sqrt{n}}\left(\left[(\lfloor nt +1\rfloor-nt)\,\ell_{\lfloor nt \rfloor}(\sigma)+ (nt-\lfloor nt\rfloor)\,\ell_{\lfloor nt \rfloor +1}(\sigma)\right]-\frac{nt}{2}\right)$$ the random process obtained by renormalization and interpolation of the process $(\ell_{k}(\sigma) - \frac{k}{2})_{k \in \left[\!\left[0,n\right]\!\right]}$. As $n$ goes to infinity, $(L_{t}^{(n)})_{t \in [ 0,1]}$ converges in law[^2] in $\mathscr{C}([0,1])$ to a 3-dimensional Bessel process $(\mathrm{BES}^{3}_{t})_{t \in [0,1]}$ (see Figure [1](#figbessel){reference-type="ref" reference="figbessel"}).

<figure id="figbessel">
<div class="center">
<p><span><span> <embed src="graphic_bessel.pdf" /></span></span></p>
</div>
<figcaption>A trajectory of the <span class="math inline">3</span>-dimensional Bessel process.<span id="figbessel" label="figbessel"></span></figcaption>
</figure>

In particular, $$\ell(\sigma)=\lambda_{1}=\frac{n}{2}+\frac{\sqrt{n}}{2}\,Y+o\left(\sqrt{n}\right), \quad\text{with }Y\sim \mathrm{BES}^{3}_{1}\sim \mathbf{1}_{y \geq 0} \,\sqrt{\frac{2}{\pi}}\,y^{2}\,\mathrm{e}^{-\frac{y^{2}}{2}}\,dy.$$
:::

To conclude this paragraph, let us give yet another representation of the $3$-dimensional Bessel process. We denote by $\mathfrak{su}(2,\mathbb{C})$ the space of traceless hermitian matrices of size $2\times 2$. An element of $\mathfrak{su}(2,\mathbb{C})$ can be written as $$M=\begin{pmatrix}m_{1} & m_{2}+\mathrm{i}m_{3}\\
m_{2}-\mathrm{i}m_{3} & -m_{1}\end{pmatrix},$$ and $\mathfrak{su}(2,\mathbb{C})$ is an euclidian space for the scalar product $\left\langle A\vphantom{B}\,\right |\left.B \vphantom{A}\right\rangle=\mathrm{tr}\,AB^{*}=2(a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3})$. A brownian motion in $\mathfrak{su}(2,\mathbb{C})$ is a continuous gaussian process $(M_{t})_{t \in \mathbb{R}_{+}}$ starting from the null matrix, and with covariances $$\mathbb{E}[\mathrm{tr}((AM_{s})(BM_{t})^{*})]=K\,(s\wedge t)\,\mathrm{tr}(AB^{*}).$$ For instance, if $X,Y,Z$ are three independent brownian motions in $\mathbb{R}$, then $$\begin{pmatrix}X_{t} & Y_{t}+\mathrm{i}Z_{t}\\
Y_{t} - \mathrm{i}Z_{t}& -X_{t}\end{pmatrix}$$ is a brownian motion in $\mathfrak{su}(2,\mathbb{C})$, with $K=3$. Now, the eigenvalues of such a matrix brownian motion are $\pm \sqrt{X_{t}^{2}+Y_{t}^{2}+Z_{t}^{2}}$, so they are described by a $3$-dimensional Bessel process. Hence, Proposition [\[bessel3\]](#bessel3){reference-type="ref" reference="bessel3"} can be restated as follows: if $\lambda=(\lambda_{1},\lambda_{2})$ is a random partition of law $\mathbb{P}_{n,\omega}$ with $\omega = ((1/2,1/2),(0))$, then $$\frac{2}{\sqrt{n}}\left(\lambda_{1}-\frac{n}{2},\lambda_{2}-\frac{n}{2}\right) \simeq_{n \to \infty} (x_{1},x_{2}),$$ where $x_{1}\geq x_{2}$ are the two eigenvalues of a brownian matrix in $\mathfrak{su}(2)$ at time $t=1$. This is the good formulation of Proposition [\[bessel3\]](#bessel3){reference-type="ref" reference="bessel3"} for a generalization to the case of $d$-shuffles.

## The case of $d$-shuffles

With a similar framework as before, we want to understand the asymptotics of **d-shuffles**, meaning that we consider the case when $$\omega=\left(\left(\frac{1}{d},\frac{1}{d},\ldots,\frac{1}{d},0,0,\ldots \right),(0)\right),$$ with $d$ coordinates equal to $\frac{1}{d}$ in $\alpha$. A generalization of the arguments of the previous paragraph to the case of $d$-shuffles has been proposed by N. O'Connell in [@OC03], in connection with previous results from [@OCY02]. Let us denote by $\Pi_{d}$ the set of paths $W : \mathbb{N}\to \mathbb{N}^{d}$, such that $W(0)=(0,0,\ldots,0)$ and $$W(k+1)-W(k) \in \{0,e_{1},e_{2},\ldots,e_{d}\}$$ for any $k$, where $e_{i}=(0_{1},0_{2},\ldots,1_{i},\ldots,0_{d})$. If $w$ is a word in $\{1,2,\ldots,d\}^{*}$ of length $n$, we associate to it a path $(W^{(k)})_{k \leq n}$ in $\Pi_{d}$, with $$W(k+1)-W(k)=e_{i}\quad\text{if }w_{k}=i.$$ Now, for any pair of sequences $(x(k))_{k\in \mathbb{N}}$ and $(y(k))_{k \in \mathbb{N}}$ in $\Pi_{1}$, we define two new sequences $$\begin{aligned}
(x \Yup y)(k) &= \min \{x(j)-y(j) +y(k) \}_{j \leq k};\\
(x \Ydown y)(k) &= \max \{ x(j)-y(j)+y(k)\}_{j \leq k}.
\end{aligned}$$ Notice that the rules $\Yup$ and $\Ydown$ are not associative. In the following, we will use the following convention: $x \Yup y \Yup z = (x \Yup y) \Yup z$ and $x \Ydown y \Ydown z = (x \Ydown y) \Ydown z$. We then define operators $D_{d} : \Pi_{d} \to \Pi_{d}$ and $T_{d} :  \Pi_{d} \to \Pi_{d-1}$: $$\begin{aligned}
D_{d}(x_{1},\ldots,x_{d})&=(x_{1},x_{1}\Yup x_{2},x_{1}\Yup x_{2}\Yup x_{3},\ldots,x_{1}\Yup x_{2}\Yup \cdots \Yup x_{d});\\
T_{d}(x_{1},\ldots,x_{d})&=(x_{2}\Ydown x_{1},x_{3}\Ydown (x_{1}\Yup x_{2}),\ldots,x_{d}\Ydown(x_{1}\Yup x_{2}\Yup \cdots \Yup x_{d-1})).
\end{aligned}$$ Finally, from a path $W$ in $\Pi_{d}$, we define new paths $D^{i}W \in \Pi_{d-i+1}$ and $T^{i}W \in \Pi_{d-i}$ by the recursive rule $$\begin{aligned}
 D^{1}W=D_{d}(W_{1},W_{2},\ldots,W_{d})\qquad&;\qquad T^{1}W=T_{d}(W_{1},\ldots,W_{d})\\
D^{i+1}W=D_{d-i}(T^{i}W)\qquad&;\qquad T^{i+1}W=T_{d-i}(T^{i}W).
\end{aligned}$$ For any path $W$, the family $(D^{1}W,D^{2}W,\ldots,D^{d}W)$ is a sequence of triangular arrays. The link between this construction and the RSK algorithm is given by the following result of O'Connell:

::: theorem
[]{#bradpitt label="bradpitt"} For any word $w \in \{1,2,\ldots,d\}^{n}$, the semi-standard tableau of size $n$ obtained from $w$ by Schensted insertion is

::: center
![image](graphic_SSTd.pdf)
:::

where[^3] $m_{ij}=(D^{j-i+1}W)_{i}(n)-(D^{j-i}W)_{i}(n)$ for any $1 \leq i \leq j \leq d$, $W$ being the path associated to the word $w$. In particular, for any $k\leq n$, the shape $(\lambda_{1},\lambda_{2},\ldots,\lambda_{d})$ of $P_{k}(w)$ is $$\left((D^{d}W)_{1}(k),(D^{d-1}W)_{2}(k),\ldots,(D^{1}W)_{d}(k)\right).$$
:::

We refer to [@OC03 Theorem 3.1] for a proof of this important result. Now, we have to understand the transformation $$\begin{aligned}
G_{d} : \Pi_{d} &\to \Pi_{d}\\
W &\mapsto \left((D^{d}W)_{1},(D^{d-1}W)_{2},\ldots,(D^{1}W)_{d}\right),
\end{aligned}$$ and what is the law of $G_{d}(W)$ when $W$ is a random path in $\mathbb{N}^{d}$ associated to a random word in $\{1,2,\ldots,d\}^{*}$. To begin with, we shall notice that the operators $\Yup$ and $\Ydown$ also make sense for any continuous or càdlàg functions $x(t)$ and $y(t)$. Thus, we can define operators $$\begin{aligned}
D_{d} : \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d}) &\to \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d})\\
T_{d} : \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d}) &\to \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d-1}) \\
 G_{d} : \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d}) &\to \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d})
 
\end{aligned}$$ where $\mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d})$ denotes the set of continuous functions $w(t)$ from $\mathbb{R}_{+}$ to $\mathbb{R}^{d}$, with $w(0)=(0,0,\ldots,0)$. Moreover, $G_{d}$ has the following property, see [@OC03 Lemma 2.2]: for any path $w \in \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d})$ and any time $t \in \mathbb{R}_{+}$, $$w_{1}(t)+w_{2}(t)+\cdots+w_{d}(t)=(G_{d}w)_{1}(t)+(G_{d}w)_{2}(t)+\cdots+(G_{d}w)_{d}(t).$$ In particular, $G_{d}$ stabilizes the subspace $\mathscr{C}_{0}(\mathbb{R}_{+},H)\subset \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d})$ of functions taking their values in the hyperplane $$H=\{(x_{1},x_{2},\ldots,x_{d})\,\,|\,\,x_{1}+x_{2}+\cdots+x_{d}=0\}.$$ On the other hand, for any $x,y,f$ functions in $\mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R})$, one has $$(x+f) \Yup (y+f)=(x\Yup y)+f\qquad;\qquad(x+f)\Ydown (y+f)=(x\Ydown y)+f.$$ This implies immediately that: $$G_{d}(x_{1}+f,x_{2}+f,\ldots,x_{d}+f)=G_{d}(x_{1},x_{2},\ldots,x_{d})+(f,f,\ldots,f).$$ In particular, set $f=\frac{x_{1}+x_{2}+\cdots+x_{d}}{d}$. Then, $$G_{d}(x_{1},x_{2},\ldots,x_{d})=(f,f,\ldots,f)+G_{d}(x_{1}-f,x_{2}-f,\ldots,x_{d}-f),$$ and the last term is a function in $\mathscr{C}_{0}(\mathbb{R}_{+},H)$; hence, it suffices to study the restriction of $G_{d}$ to the subspace $\mathscr{C}_{0}(\mathbb{R}_{+},H)$.

The operators $G_{d}$ are better understood in terms of the **Pitman transforms** attached to a root system (*cf.* [@BBO05]). The hyperplane $H\subset \mathbb{R}^{d}$ contains a root system of type $A_{d-1}$, whose simple roots are $e_{1}-e_{2},e_{2}-e_{3},\ldots,e_{d-1}-e_{d}$. To each simple root $\delta_{i}=e_{i}-e_{i+1}$, we attach an operator $P_{i} : \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d}) \to \mathscr{C}_{0}(\mathbb{R}_{+},\mathbb{R}^{d})$, defined by the following formula:[]{#pitmanoperator label="pitmanoperator"} $$(P_{i}w)(t)=w(t)-\left(\min\{ \left\langle \delta_{i}\vphantom{w(s)}\,\right |\left.w(s) \vphantom{\delta_{i}}\right\rangle\}_{s \leq t}\right)\,\delta_{i}.$$ Notice that each $P_{i}$ stabilizes the subspace $\mathscr{C}_{0}(\mathbb{R}_{+},H)$. In [@BBO05], it is shown that the operators $P_{i}$ satisfy the braid relations of the generators $s_{i}=(i,i-1)$ of the Coxeter group $\mathfrak{S}_{d}$: $$\begin{aligned}
&\forall i \leq d-2,\,\,\,P_{i}P_{i+1}P_{i}=P_{i+1}P_{i}P_{i+1};\\
&\forall i,j \leq d-1,\,\,\,|i-j|\geq 2 \Rightarrow P_{i}P_{j}=P_{j}P_{i}.
\end{aligned}$$ It enables us to define $P_{\sigma}$ for any $\sigma \in \mathfrak{S}_{d}$, and it is not hard to see that $P_{\sigma}|_{\mathscr{C}_{0}(\mathbb{R}_{+},H)}$ takes its values in $$\mathscr{C}_{0}\left(\mathbb{R}_{+},\bigcap_{s_{i} \in L_{\sigma}} H_{i}^{+}\right),$$ where $L_{\sigma}= \{s_{i} \,\,|\,\, \ell(s_{i}\sigma)<\ell(\sigma)\}$, and $H_{i}^{+} =\{x \in H\,\,|\,\,\left\langle \delta_{i}\vphantom{x}\,\right |\left.x \vphantom{\delta_{i}}\right\rangle\geq 0\}$ --- *cf.* [@BBO05 Proposition 2.8]. In particular, if $\omega_{0}$ is the permutation of maximal length in $\mathfrak{S}_{d}$, that is to say $(d,d-1,\ldots,1)$, then $P_{\omega_{0}}|_{\mathscr{C}_{0}(\mathbb{R}_{+},H)}$ is an idempotent operator taking its values in $\mathscr{C}_{0}(\mathbb{R}_{+},C),$ where $C=\bigcap_{i=1}^{d-1} H_{i}^{+}$ is the closed Weyl chamber in $H$ corresponding to the simple roots. In terms of coordinates, notice that $x =(x_{1},\ldots,x_{d})$ is in $C$ if and only if $$x_{1}+\cdots+x_{d}=0 \quad\text{and}\quad x_{1}\geq x_{2}\geq \cdots \geq x_{d}.$$ Now, if $\phi_{k}^{d}$ is the projection $(x_{1},\ldots,x_{d}) \in \mathbb{R}^{d}\mapsto (x_{1},\ldots,x_{k}) \in \mathbb{R}^{k}$, then it is easily seen that $$\begin{aligned}
T_{d}(W)&=\phi_{d-1}^{d}\,P_{d-1}P_{d-2}\cdots P_{2}P_{1}(W);\\
T^{i}W&=\phi_{d-i}^{d}\,(P_{d-i}\cdots P_{1})\,(P_{d-i+1}\cdots P_{1})\,\cdots\, (P_{d-1}\cdots P_{1})(W).
\end{aligned}$$ From this, one sees that $G_{d}=P_{1}(P_{2}P_{1})\cdots(P_{d-1}\cdots P_{1})= P_{\omega_{0}}$. In particular, $G_{d}|_{\mathscr{C}_{0}(\mathbb{R}_{+},H)}$ takes its values in $\mathscr{C}_{0}(\mathbb{R}_{+},C)$, which was not clear from the first definition.

Then, let us consider the path $W$ associated to a random word $w \in \{1,2,\ldots,d\}^{*}$, where each letter of $w$ is independent of the other letters, and uniformly distributed on $\left[\!\left[1,d\right]\!\right]$. If $$\widetilde{W}(k)=W(k)-\left(\frac{k}{d},\frac{k}{d},\ldots,\frac{k}{d}\right),$$ then $\widetilde{W}$ lives in the hyperplane $H$, and by (multi-dimensional) Donsker's theorem (*cf.* [@Bil69 Chapter 2]), after time-space scaling, $\widetilde{W}$ converges to a brownian motion $(w_{t})_{t \in \mathbb{R}}$ in $H$, that is to say a continuous gaussian process in $H$ with covariances $$\mathbb{E}[\left\langle a\vphantom{w_{s}}\,\right |\left.w_{s} \vphantom{a}\right\rangle\,\left\langle b\vphantom{w_{t}}\,\right |\left.w_{t} \vphantom{b}\right\rangle]=\frac{1}{d}\,(s\wedge t)\,\left\langle a\vphantom{b}\,\right |\left.b \vphantom{a}\right\rangle.$$ Indeed, if $X$ is a random step $\widetilde{W}(n+1)-\widetilde{W}(n)$, then $\left\langle \delta_{i}\vphantom{X}\,\right |\left.X \vphantom{\delta_{i}}\right\rangle$ equals $1$ if $X=e_{i}$, $-1$ if $X=e_{i+1}$, and $0$ otherwise. From this, one sees that $\mathbb{E}[\left\langle \delta_{i}\vphantom{X}\,\right |\left.X \vphantom{\delta_{i}}\right\rangle\,\left\langle \delta_{j}\vphantom{X}\,\right |\left.X \vphantom{\delta_{j}}\right\rangle]$ equals $\frac{2}{d}$ if $i=j$, $-\frac{1}{d}$ if $i=j\pm 1$, and $0$ otherwise. But this is exactly $\frac{\left\langle \delta_{i}\vphantom{\delta_{j}}\,\right |\left.\delta_{j} \vphantom{\delta_{i}}\right\rangle}{d}$, whence the result after applying Donsker's theorem.

Let us forget for the moment the factor $\frac{1}{d}$, and consider a standard brownian motion $w$ in $H$. Then, it can be shown that $P_{\omega_{0}}(w)$ is a brownian motion conditioned in Doob's sense to stay in the Weyl chamber $C$, *cf.* [@BBO05 Theorem 5.6] or [@Bia09]. We have drawn on Figure [2](#pitmanfig){reference-type="ref" reference="pitmanfig"} a random walk in $H \subset \mathbb{R}^{3}$ corresponding to a random word (in blue), and its image by Pitman's transform $P_{\omega_{0}}=P_{1}P_{2}P_{1}$ (in violet); it approximates a brownian motion conditioned to stay in a Weyl chamber[^4].

<figure id="pitmanfig">
<div class="center">
<p><span><span> <embed src="graphic_pitman.pdf" /></span></span></p>
</div>
<figcaption>Action of Pitman’s transform on a brownian motion when <span class="math inline"><em>d</em> = 3</span>.<span id="pitmanfig" label="pitmanfig"></span></figcaption>
</figure>

This conditioned brownian motion is the Markov process on $C$ with transition probabilities $$q_{t}(x,y)=\frac{\Delta(y)}{\Delta(x)}\,\sum_{\sigma \in \mathfrak{S}_{d}} \varepsilon(\sigma)\,p_{t}(x,\sigma(y))$$ where $p_{t}(x,y)=(2\pi t)^{-\frac{d-1}{2}}\,\exp\left(-\frac{\|x-y\|^{2}}{2t}\right)$ is the transition kernel of the standard brownian motion in $H$, and $$\Delta(x)=\prod_{\alpha \text{ positive root}} \left\langle \alpha\vphantom{x}\,\right |\left.x \vphantom{\alpha}\right\rangle=\prod_{1\leq i<j\leq d}x_{i}-x_{j}$$ is (up to a multiplicative constant) the unique positive function on $C$ that is harmonic with respect to the symmetrized kernel and that vanishes at the boundary of $C$. The singularity of the transition kernel at $x=(0,0,\ldots,0)$ is solvable[^5], with $$q_{t}(0,y)=\frac{\Delta(y)^{2} }{1!\,2!\,\cdots\,d-1!\,t^{\frac{d(d-1)}{2}}}\,p_{t}(0,y).$$ This Markov process corresponds to the process of the eigenvalues $$(x_{t,1}\geq x_{t,2}\geq \cdots \geq x_{t,d})$$ of a brownian matrix in $\mathfrak{su}(d,\mathbb{C})$ with covariances $$\mathbb{E}[\mathrm{tr}((AM_{s})(BM_{t})^{*})]=\frac{d^{2}-1}{d}\,(s\wedge t)\,\mathrm{tr}(AB^{*}),$$ see [@Dys62; @Bia09], and [@AGZ09 Theorem 2.5.2] for checking that the multiplicative constant is indeed $\frac{d^{2}-1}{d}$. Taking account of the factor $\frac{1}{d}$ put aside before, we get:

::: theorem
In the following, $(M_{t})_{t \in \mathbb{R}_{+}}$ is a brownian matrix in $\mathfrak{su}(d,\mathbb{C})$ starting from the null matrix and with normalized covariances $$\mathbb{E}[\mathrm{tr}((AM_{s})(BM_{t})^{*})]= \frac{d^{2}-1}{d^{2}}\,(s\wedge t)\,\mathrm{tr}(AB^{*});$$ and $(x_{1,t}\geq x_{2,t}\geq \cdots \geq x_{d,t})$ is the set of eigenvalues of $M_{t}$. On the other hand, we consider a random permutation $\sigma$ obtained by a $d$-shuffle, and we denote $$L_{i,t}^{(n)}= \frac{1}{\sqrt{n}}\left(\left[(\lfloor nt +1\rfloor-nt)\,\Lambda_{i,\lfloor nt \rfloor}(\sigma)+ (nt-\lfloor nt\rfloor)\,\Lambda_{i,\lfloor nt \rfloor +1}(\sigma)\right]-\frac{nt}{d}\right),$$ where $(\Lambda_{1,k}(\sigma),\ldots,\Lambda_{d,k}(\sigma))$ is the shape of the tableau $P_{k}(\sigma)$ obtained by Schensted insertion from the $k$ first letters of $\sigma$. As $n$ goes to infinity, $$\left(L_{1,t}^{(n)},L_{2,t}^{(n)},\ldots,L_{d,t}^{(n)}\right)_{t \in [0,1]} \to  (x_{1,t},x_{2,t},\ldots,x_{d,t})_{t \in [0,1]},$$ where the convergence is in law and takes place in $\mathscr{C}([0,1],\mathbb{R}^{d})$. In particular, if $\lambda \sim \mathbb{P}_{n,\omega}$ with $\omega = ((1/d,1/d,\ldots,1/d),(0))$, then[^6] $$\lambda_{i}=\frac{n}{d}+\sqrt{\frac{n}{d}}\,Y_{i}+o\left(\sqrt{n}\right)$$ with $$(Y_{1},\ldots,Y_{d})\sim \mathbf{1}_{\substack{y_{1}\geq y_{2}\geq  \cdots \geq y_{d}\quad \\ y_{1}+y_{2}+\cdots+y_{d}=0}}\,\,\,\frac{\Delta(y_{1},y_{2},\ldots,y_{d})^{2}}{1!\,2!\,\cdots\,d-1!\,(2\pi)^{\frac{d-1}{2}}}\,\mathrm{e}^{-\frac{\|y\|^{2}}{2}}\,dy.$$
:::

## The general case of equal coordinates

We pursue the study of the fluctuations of rows of a tableau obtained by Schensted insertion from a generalized shuffle, and we consider now the case when $\omega=((p_{1}^{d_{1}},p_{2}^{d_{2}}, \ldots,p_{r}^{d_{r}}),(0))$ with $$p_{1}>p_{2}>\cdots>p_{r}>0 \,\,\,\text{ and }\,\,\,d_{1}p_{1}+d_{2}p_{2}+\cdots+d_{r}p_{r}=1.$$ Here, by $p_{i}^{d_{i}}$, we mean that $p_{i}$ appears $d_{i}$ times in $\alpha$. It will be clear from our reasoning that one could even consider an infinite sequence of $p_{i}$'s with the same property. So, if one understands the behaviour of rows with a finite number of parameters, the study of the general case when $\omega=(\alpha,0)$ and $\gamma=0$ will be completed. In the following, we set $d=d_{1}+d_{2}+\cdots+d_{r}$.

As before, an $\omega$-shuffle of size $n$ corresponding to parameters $p_{1}^{d_{1}},\ldots,p_{r}^{d_{r}}$ can be obtained by standardizing a random word $w=b_{1}b_{2}\ldots b_{n}$ in $\left[\!\left[1,d\right]\!\right]^{n}$, where the letters $b_{k}$ are independent and of law $$\mathbb{P}[b_{k}=i]=p_{j}\quad\text{if }d_{1}+\cdots+d_{j-1}+1\leq i \leq d_{1}+\cdots+d_{j}.$$ To such a (random) word, we attach as before a random walk $W\in \mathbb{Z}^{d}$, with $W(k+1)-W(k)=e_{i}$ if $b_{k}=i$. O'Connell's Theorem [\[bradpitt\]](#bradpitt){reference-type="ref" reference="bradpitt"} holds again, so $G_{d}(W)(k)$ is the form $\Lambda_{k}(\sigma)$ of the tableau $P_{k}(\sigma)$ (or $P_{k}(w)$) obtained by Schensted insertion from the $k$ first letters of $\sigma$. Now, we shall use the following technical lemma:

::: lemma
[]{#technical label="technical"} If $W=(x_{1},\ldots,x_{d})$ is a random walk obtained from a shuffle of parameter $p_{1}^{d_{1}},\ldots,p_{r}^{d_{r}}$, we introduce random functions $f_{1},\ldots,f_{d}$ such that $(f_{1},\ldots,f_{d})$ is the vector $$G_{d}(x_{1},\ldots,x_{d})-(G_{d_{1}}(x_{1},\ldots,x_{d_{1}}),\ldots,G_{d_{r}}(x_{d_{1}+\cdots+d_{r-1}+1},\ldots,x_{d_{1}+\cdots+d_{r}})).$$ These functions are almost surely bounded (as functions of $\mathbb{N}$).
:::

::: example
Before proving Lemma [\[technical\]](#technical){reference-type="ref" reference="technical"}, let us see study the simplest example where it applies, namely, when $\omega=((a,1-a),(0))$ with $a>1/2$. The random walk to consider is two dimensional and will be denoted $w_{n}=(x_{n},y_{n})_{n \in \mathbb{N}}$; moreover, $$(G_{2}w)_{n}= (x_{n}-\min\{x_{k}-y_{k}\}_{k \leq n},y_{n}+\min\{x_{k}-y_{k}\}_{k \leq n}).$$ However, $(z_{n}=x_{n}-y_{n})_{n \in \mathbb{N}}$ is a random walk on $\mathbb{Z}$ with $\mathbb{P}[z_{n+1}=z_{n}+1]=a$, $\mathbb{P}[z_{n+1}=z_{n}-1]=1-a$, and $z_{0}=0$ almost surely. It is well-known that such a random walk is transient, with $$\begin{aligned}
\mathbb{P}\left[\inf_{n \in \mathbb{N}}z_{n}\leq -m\right]&=\left(\frac{1-a}{a}\right)^{m}\\
\mathbb{P}\left[\min_{n \in \mathbb{N}}z_{n}=-m\right]&=\left(\frac{1-a}{a}\right)^{m}-\left(\frac{1-a}{a}\right)^{m+1}=\frac{2a-1}{a}\left(\frac{1-a}{a}\right)^{m}.
\end{aligned}$$ Thus, $(G_{2}(x,y))-(x,y)=(-z,z)$, with $|z|$ almost surely bounded by a (random) constant of expectation $\frac{1-a}{2a-1}$.
:::

::: proof
*Proof of Lemma [\[technical\]](#technical){reference-type="ref" reference="technical"}.* The example above can be generalized by using the language of Pitman operators: if $P_{i}$ acts on the random walk with $i=d_{1}+\cdots+d_{j}$ for some $j \in \left[\!\left[1,r-1\right]\!\right]$, then $P_{i}w$ differs from $w$ by almost surely bounded functions on the coordinates of index $d_{1}+\cdots+d_{j}$ and $d_{1}+\cdots+d_{j}+1$. This is exactly for the same reason: the difference of the two random walks $x_{d_{1}+\cdots+d_{j}}$ and $x_{d_{1}+\cdots+d_{j}+1}$ is almost surely bounded from below. Quite obviously, this is also true if one replaces $w$ by $w+\delta$ with $\delta$ almost surely bounded vector, so one can use this argument several times. More generally, this works also if $w$ is replaced by $P_{\sigma}(w)$, where $\sigma$ is a permutation in the Young subgroup $\mathfrak{S}_{d_{1}}\times \mathfrak{S}_{d_{2}}\times \cdots \times \mathfrak{S}_{d_{r}} \subset \mathfrak{S}_{d}$; indeed, such an operator won't change the fact that the coordinates $x_{d_{1}+\cdots+d_{j}}$ and $x_{d_{1}+\cdots+d_{j}+1}$ have different rates of growth to infinity.

In the operator $G_{d}=P_{\omega_{0}}=P_{1}(P_{2}P_{1})(P_{3}P_{2}P_{1})\cdots(P_{d-1}\cdots P_{1})$, it allows to neglict all the factors $P_{i}$ with $i=d_{1}+\cdots+d_{j}$: they will simply modify the random path by almost surely bounded functions. So, $G_{d}w\simeq J_{d}w$, where $J_{d}$ is obtained from $G_{d}$ by deleting in the reduced decomposition of $\omega_{0}$ all the $s_{i}$'s with $i=d_{1}+\cdots+d_{j}$, $j \in \left[\!\left[1,r-1\right]\!\right]$. Then, $J_{d}$ acts separately on each block of coordinates $x_{d_{1}+\cdots+d_{j-1}+1},\ldots,x_{d_{1}+\cdots+d_{j}}$, and the action corresponding to the block of size $d_{j}$ is given by the operator $$G_{d_{j}}\,(P_{d_{j}-1}\cdots P_{2}P_{1})^{k},$$ where $k=d-d_{j}$. Now, each $P_{i}$ is an idempotent operator (this is almost obvious from the definition given on page ), and on the other hand, for any $i$, there is a reduced decomposition of $\omega_{0}$ in $\mathfrak{S}_{d_{j}}$ that ends by $s_{i}$. Hence, $$G_{d_{j}}\,(P_{d_{j}-1}\cdots P_{2}P_{1})^{k}=G_{d_{j}},$$ whence the result. ◻
:::

Now, for each block $x_{d_{1}+\cdots+d_{j-1}+1},\ldots,x_{d_{1}+\cdots+d_{j}}$, one can follow the same reasoning as in the case of $d$-shuffles, with some precaution. First, notice that if $g_{j}=\frac{1}{d_{j}}\sum_{i=1}^{d_{j}} x_{d_{1}+\cdots+d_{j-1}+i}$, then:

1.  In $\mathbb{N}^{r}$, $(d_{1}g_{1},\ldots,d_{r}g_{r})$ is a random walk of parameter $d_{1}p_{1},\ldots,d_{r}p_{r}$.

2.  The vectors $$\widetilde{W}_{j}=(x_{d_{1}+\cdots+d_{j-1}+1}-g_{j},\ldots,x_{d_{1}+\cdots+d_{j-1}+d_{j}}-g_{j})$$ with $j \in \left[\!\left[1,r\right]\!\right]$ are random walks in $H \subset \mathbb{R}^{d_{j}}$, and they are all independent, and independent from the vector $(d_{1}g_{1},\ldots,d_{r}g_{r})$.

One takes account of the first vector by the standard central limit theorem: $$d_{i}g_{i}=n(d_{i}p_{i})+\sqrt{n}\,X_{i}+o\left(\sqrt{n}\right)$$ where $(X_{1},\ldots,X_{r})$ is a gaussian vector of covariance matrix $k(X_{i},X_{j})=\delta_{ij}\,d_{i}p_{i}-d_{i}d_{j}\,p_{i}p_{j}$. More precisely, one can describe asymptotically $$(d_{1}g_{1}(k)-k\,d_{1}p_{1},\ldots,d_{r}g_{r}(k)-k\,d_{r}p_{r})_{k\leq n}$$ by using the multidimensional Donsker theorem. As for the vectors $\widetilde{W}_{j}$, they can be studied with the framework of the previous paragraph on $d$-shufflles. The only difference is the multiplicative constant in the covariances of the brownian motion that is the limit of $\widetilde{W}_{j}$ after time-space scaling: it is $p_{j}$ instead of $\frac{1}{d_{j}}$. In the end, one obtains the following:

::: theorem
[]{#maingeom label="maingeom"} With the same notations as before, we fix independent brownian motions $(M_{t,j})_{t \in \mathbb{R}_{+}, 1\leq j \leq r}$ taking values in the spaces $\mathfrak{su}(d_{j},\mathbb{C})$, with covariances $$\mathbb{E}[\mathrm{tr}((AM_{s,j})(BM_{t,j})^{*})]=\frac{d_{j}^{2}-1}{d_{j}}\,p_{j}\,(s\wedge t)\,\mathrm{tr}(AB^{*});$$ $(x_{1,j,t}\geq x_{2,j,t}\geq \cdots \geq x_{d_{j},j,t})$ will denote the set of eigenvalues of $M_{t,j}$. We also consider an independent brownian motion $(B_{1,t},\ldots,B_{r,t})$ in $\mathbb{R}^{d}$, with covariances $$\mathbb{E}[\left\langle X\vphantom{B_{s}}\,\right |\left.B_{s} \vphantom{X}\right\rangle\,\left\langle Y\vphantom{B_{t}}\,\right |\left.B_{t} \vphantom{Y}\right\rangle]=(s \wedge t)\,X^{t}QY,\quad \text{where }Q=\left(\delta_{ij}\,\frac{p_{i}}{d_{i}}-p_{i}p_{j}\right)_{1\leq i,j\leq r}.$$ On the other hand, we consider a random permutation obtained by a shuffle of parameters $p_{1}^{d_{1}},\ldots,p_{r}^{m_{r}}$, and we denote as before $\Lambda_{k}(\sigma)$ the shape of the standard tableau $P_{k}(\sigma)$, and $$L_{i,t}^{(n)}= \frac{1}{\sqrt{n}}\left(\left[(\lfloor nt +1\rfloor-nt)\,\Lambda_{i,\lfloor nt \rfloor}(\sigma)+ (nt-\lfloor nt\rfloor)\,\Lambda_{i,\lfloor nt \rfloor +1}(\sigma)\right]-p_{j}nt\right),$$ assuming that $d_{1}+\cdots+d_{j-1}+1\leq i\leq d_{1}+\cdots+d_{j}$. As $n$ goes to infinity, $\left(L_{1,t}^{(n)},\ldots,L_{i,t}^{(n)},\ldots,L_{d,t}^{(n)}\right)_{t \in [0,1]}$ converges in law to $$\left(B_{1,t}+x_{1,1,t},\ldots,B_{j,t}+x_{i,j,t},\ldots,B_{r,t}+x_{d_{r},r,t}\right)_{t \in [0,1]},$$ in $\mathscr{C}([0,1],\mathbb{R}^{d})$. In particular, if $\lambda=\Lambda_{n}(\sigma)=\Lambda(\sigma)$ with $\sigma$ chosen randomly as before, then $$\lambda_{i}=np_{j}+\sqrt{np_{j}}\,(X_{j}+Y_{i,j})+o\left(\sqrt{n}\right),$$ with $$(Y_{1,j},\ldots,Y_{d_{j},j})\sim \mathbf{1}_{\substack{y_{1,j}\geq y_{2,j}\geq  \cdots \geq y_{d_{j},j}\quad \\ y_{1,j}+y_{2,j}+\cdots+y_{d_{j},j}=0}}\,\,\,\frac{\Delta(y_{1,j},y_{2,j},\ldots,y_{d_{j},j})^{2}}{1!\,2!\,\cdots\,d_{j}-1!\,(2\pi)^{\frac{d_{j}-1}{2}}}\,\mathrm{e}^{-\frac{\|y_{j}\|^{2}}{2}}\,dy_{j}$$ and $(X_{1},\ldots,X_{r})$ gaussian vector of covariance matrix $$Q'=\left(\frac{\delta_{ij}}{d_{i}}-\sqrt{p_{i}p_{j}}\right)_{1\leq i,j \leq r}.$$
:::

::: remark
At the end of Section [\[largenumbers\]](#largenumbers){reference-type="ref" reference="largenumbers"}, we have seen that the law of large numbers can be informally restated by saying that the longest increasing subsequences in a $\alpha$-shuffle are not bigger at order $n$ than the lengths of the blocks shuffled together. Theorem [\[maingeom\]](#maingeom){reference-type="ref" reference="maingeom"} ensures that it is also true at order $\sqrt{n}$, unless some blocks have the same frequency $p_{j}= \alpha_{i}=\alpha_{i'}$. Then, some of the increasing subwords become (stochastically) bigger than the sizes of the blocks to be shuffled, because of the terms $\sqrt{np_{j}} \,Y_{i,j}$.
:::

Theorem [\[maingeom\]](#maingeom){reference-type="ref" reference="maingeom"} seems to remain true when $\beta\neq 0, \gamma \neq 0$, and in this case, the fluctuations of the first renormalized columns seem to be given by analogous formulas as those given above, with fluctuations "of type $X$" described by Theorem [\[almostgeom\]](#almostgeom){reference-type="ref" reference="almostgeom"}, and fluctuations "of type $Y$" (for equal coordinates) independent of the fluctuations of the rows. We don't know how to prove this, but we can give arguments in favor of this conjecture. These arguments can be made rigorous in some cases, for instance when $\gamma=0$ and $\beta$ has only a finite number of non-zero coordinates. When performing the Schensted insertion from a permutation $\sigma$ obtained by an $\omega$-shuffle, let us mark by a point $\bullet$ the boxes containing a number coming from a block of size $m_{j}$, and by a star $\star$ the boxes containing a number coming from the block of size $l$.

::: example
Suppose $n=16$, $n_{1}=n_{2}=3$, $m_{1}=m_{2}=3$, $l=4$. We denote the "cards" to be shuffled by $\texttt{0,1,\ldots,9,A,B,\ldots,F}$. After cutting the deck, the five blocks to be shuffled are $$\texttt{012,\,\,345,\,\,678,\,\,9AB,\,\,CDEF}.$$ The blocks $\texttt{678}$ and $\texttt{9AB}$ are reversed, and $\texttt{CDEF}$ is randomized, becoming from instance $\texttt{DFCE}$. Then, all the blocks are shuffled together, and one can for instance obtain $$\texttt{8B0D3A97FC41E562}.$$ Now, the partitions appearing in the RSK algorithm are: $$\young(\bullet)\quad\young(\bullet\bullet)\quad\young(\bullet,~\bullet)\quad\young(\bullet,~\bullet\star)\quad\young(\bullet\bullet,~~\star)\quad\young(\bullet\bullet\star,~~\bullet)\quad\young(\bullet,\bullet\bullet\star,~~\bullet)\quad\young(\bullet,\bullet,\bullet\bullet\star,~~\bullet)$$

$$\young(\bullet,\bullet,\bullet\bullet\star,~~\bullet\star)\quad\young(\bullet,\bullet,\bullet\bullet\star\star,~~\bullet\star)\quad \young(\bullet,\bullet,\bullet,\bullet\bullet\star\star,~~~\star)\quad \young(\bullet,\bullet,\bullet,\bullet,~\bullet\star\star,~~~\star)\quad \young(\bullet,\bullet,\bullet,\bullet,~\bullet\star\star,~~~\star\star)$$

$$\young(\bullet,\bullet,\bullet,\bullet\star,~\bullet\star\star,~~~~\star)\quad \young(\bullet,\bullet,\bullet,\bullet\star\star,~\bullet\star\star,~~~~\bullet)
\quad\young(\bullet,\bullet,\bullet\star,\bullet\bullet\star,~~\star\star,~~~~\bullet)$$

Notice that the partition of unmarked boxes $$\yng(2,4)$$ is the one corresponding to $034152$; more generally, during the Schensted insertion, the partition of unmarked boxes evolves as the partition obtained *via* RSK from the subword containing only the letters coming from the blocks of sizes $n_{i}$. Thus, to prove that Theorem [\[maingeom\]](#maingeom){reference-type="ref" reference="maingeom"} holds again when $\beta\neq 0,\gamma \neq 0$ amounts to control the number of marked boxes appearing at the right of the first rows, and to show that it is a $o(\sqrt{n})$ --- then, by symmetry of the problem, we would obtain the fluctuations of the columns, and see that they are analogous to those of the rows.
:::

One should notice that each time a unmarked box appears in a row, it pushes a marked box $$\young(\bullet)\quad\text{or}\quad\young(\star)$$ to the next row. Moreover, marked boxes push themselves to upper rows: for instance, if $\gamma=0$ and $\beta=(\beta_{1},\ldots,\beta_{d})$, then one can not find more than $d$ marked boxes on the same row. So the idea would be to show that marked boxes are "sufficiently pushed up". Unfortunately, to do this rigorously, it seems that we would need precise estimates on the probabilities of creating a "long" increasing subword in a shuffle of parameter $\alpha=0$; and we don't have for the moment such estimates.

To conclude this section, let us look again at the partition-valued random process $(\Lambda_{k}(\sigma))_{k \in \left[\!\left[0,n\right]\!\right]}$, where $\sigma$ is obtained from an $\omega$-shuffle, and $\Lambda_{k}(\sigma)$ is the shape of the tableau obtained by Robinson-Schensted insertion from the $k$ first letters of $\sigma$. We have shown previously that after time-space scaling, and at least when $\beta=\gamma=0$, the coordinates of this process converge jointly to a markovian process that can be written in terms of (conditioned) brownian motions. It raises the following question: is $(\Lambda_{k}(\sigma))_{ k \in \left[\!\left[0,n\right]\!\right]}$ itself a markovian process in $\mathfrak{Y}=\bigsqcup_{n \in \mathbb{N}}\mathfrak{Y}_{n}$? The answer is yes, and more precisely:

::: theorem
[]{#markovpartition label="markovpartition"} The random process $(\Lambda_{k}(\sigma))_{ k \in \left[\!\left[0,n\right]\!\right]}$ is markovian, with transition probabilities equal to $$p(\lambda,\Lambda)=\mathbf{1}_{\lambda \nearrow \Lambda}\,\frac{s_{\Lambda}(\omega)}{s_{\lambda}(\omega)}.$$
:::

::: proof
*Proof.* This is a generalization of [@OC03 Theorem 6.1], and the proof is exactly the same. The statement of Theorem [\[markovpartition\]](#markovpartition){reference-type="ref" reference="markovpartition"} amounts to ask that for any sequence of partitions $\lambda^{(1)}\nearrow \cdots \nearrow \lambda^{(k)}$, $$\mathbb{P}[\Lambda_{1}(\sigma)=\lambda^{(1)},\cdots,\Lambda_{k}(\sigma)=\lambda^{(k)}]=s_{\lambda^{(k)}}(\omega).$$ However, one can expand $s_{\lambda^{(k)}}(\omega)$ by using the structure of Hopf algebra of $\mathbf{Sym}$: $$\begin{aligned}
s_{\lambda^{(k)}}(\omega)&=\left((1 \otimes \upsilon \otimes 1)\circ \Delta^{3}\right)s_{\lambda^{(k)}}(\alpha,\beta,\gamma E)\\
&=\sum_{ \nu \subset \mu \subset \lambda^{(k)}} s_{\nu}(\alpha)\,s_{\mu'\setminus \nu'}(\beta)\,s_{\lambda^{(k)}\setminus \mu}(\gamma E).
\end{aligned}$$ Then, the arguments are exactly the same as in [@OC03]. ◻
:::

[^1]: With the vocabulary of §[\[randompermutation\]](#randompermutation){reference-type="ref" reference="randompermutation"}, $\sigma$ is the standardization of the word whose letters are the Bernoulli variables.

[^2]: As usual, the interpolation is only needed in order to work in $\mathscr{C}([0,1])$; if one uses instead step *càdlàg* functions, one has the same result of convergence, but this time in Skorohod's space $\mathscr{D}([0,1])$, see [@Bil69 Chapter 3, §14].

[^3]: By convention, $D^{0}W=(0,0,\ldots,0)$ for any path $W$, so $m_{ii}=(D^{1}W)_{i}(n)$ for any $i$.

[^4]: On the drawing, it appears that an important part of the trajectory of the initial brownian motion is simply translated by Pitman's transform $P_{\omega_{0}}$. This observation can be made precise, and one obtains a generalization of Williams' decomposition of the trajectories of the $\mathrm{BES}^{3}$ process, *cf.* [@RY91 Chapter 6, Theorem 3.11].

[^5]: This is easily seen by expanding terms $\exp(-\|\eta_{i}-x_{\sigma(i)}\|^{2}/2t)$ with $\eta \to 0$, and by using the theory of antisymmetric polynomials, see [@Mac95 §1.3].

[^6]: Here, notice that $dy$ denotes the $(d-1)$-dimensional Lebesgue measure on $H$.
