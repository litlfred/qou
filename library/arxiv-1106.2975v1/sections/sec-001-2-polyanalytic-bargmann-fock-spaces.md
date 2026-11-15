---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-001-2-polyanalytic-bargmann-fock-spaces
section_title: "Polyanalytic Bargmann-Fock spaces"
section_number: 2
pages: 8-14
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.983
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
[]{#sec-polybargmann label="sec-polybargmann"}

We will consider the Bargmann-Fock space $A^2_{m,q}({\mathbb C})$ of poly-analytic functions of degree $\le q-1$, i.e., functions of the form $$f(z) = \sum_{r=0}^{q-1} \bar{z}^r f_r(z),$$ where all the components $f_r$ are entire, subject to the norm integrability condition $$\|f\|^2_{A^2_{m,q}({\mathbb C})}:=
\|f\|^2_{L^2({\mathbb C},\mathrm e^{-m|z|^2})}
=\int_{{\mathbb C}} |f(z)|^2 \mathrm e^{-m|z|^2} {\mathrm d}A(z)<+\infty.$$ Here, as always, $m>0$. We note that $A^2_{1,1}({\mathbb C})$ is the standard Bargmann-Fock space. As before, let $\mathrm{Pol}_{m,n,q}$ be the closed subspace of $A^2_{m,q}({\mathbb C})$, defined by the condition that all the components $f_r$ are polynomials of degree less or equal to $n-1$. Moreover, let $K_{m,q}$ and $K_{m,n,q}$ denote the reproducing kernels for $A^2_{m,q}({\mathbb C})$ and $\mathrm{Pol}_{m,n,q}$, respectively. We will be concerned with the asymptotic behaviour of the kernel $K_{m,n,q}$, as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$.

Bargmann-Fock-spaces of polyanalytic functions have been considered in, e.g., [@vas], where the reproducing kernels and orthonormal bases were identified. We will attempt to supply a self-contained account of these basic matters.

To begin with, we identify an orthonormal basis for the space $\mathrm{Pol}_{m,n,q}$. Here, and later as well, we will need some standard properties of the classical orthogonal polynomials. For details, we refer the reader to [@orthopo]. We need the generalized Laguerre polynomials ($(x)_j:=x(x+1)\cdots(x+j-1)$ is the Pochhammer symbol) $$L^\alpha_k(x):=\sum_{i=0}^{k}(-1)^i\binom{k+\alpha}{k-i}\frac{x^i}{i!}
=\sum_{i=0}^{k}(-1)^i\frac{(\alpha+i+1)_{k-i}}{i!(k-i)!}x^i.$$

::: prop
[]{#on-kanta label="on-kanta"} For $q\le n$, the following functions form an orthonormal basis for $\mathrm{Pol}_{m,n,q}$ ($i,r,j,k$ are all integer parameters): $$\begin{aligned}
e_{i,r}^{1}(z)&:=\sqrt{\frac{r!}{(r+i)!}} \,m^{(i+1)/2}z^i\, L_r^{i}(m|z|^2), 
\quad 0\leq i\leq n-r-1,\,\,\,0\leq r\leq q-1, 

\\
e_{j,k}^{2}(z)&:=\sqrt{\frac{j!}{(j+k)!}} 
\,m^{(k+1)/2}\bar{z}^k\, L^{k}_{j}(m|z|^2),
\quad 0\leq j\leq q-k-1,\,\,\,1\leq k\leq q-1. 
\end{aligned}$$
:::

::: proof
*Proof.* Clearly, all the above functions belong to the space $\mathrm{Pol}_{m,n,q}$. Also, all the functions $e^1_{i,r}$ are orthogonal to each of the functions $e^2_{j,k}$, for the indicated ranges of the indices, as can be seen by integrating along circles using polar coordinates. Next, we show that the functions $e^1_{i,r}$ form an orthonormal set. Any two functions there having different parameter $i$ are orthogonal, again by integrating along circles using polar coordinates. So, we fix $i$, and pick two indices $r_1,r_2$. We compute the inner product of two such functions: $$\begin{gathered}
\int_{\mathbb C}e^1_{i,r_1}(z)\overline{e^1_{i,r_2}(z)}\mathrm e^{-m|z|^2} {\mathrm d}A(z)
\\
=\sqrt{\frac{r_1!}{(r_1+i)!}} \sqrt{\frac{r_2!}{(r_2+i)!}}m^{i+1}
\int_{{\mathbb C}}
|z|^{2i}L_{r_1}^{i}(m|z|^2)L_{r_2}^{i}(m|z|^2) \mathrm e^{-m|z|^2} 
{\mathrm d}A(z) \notag \\
=\sqrt{\frac{r_1!r_2!}{(r_1+i)!(r_2+i)!}} \int_{0}^{\infty} 
L_{r_1}^{i}(t) 
L_{r_2}^{i}(t)\,t^i\mathrm e^{-t} {\mathrm d}t = \delta_{r_1,r_2},
\end{gathered}$$ where the delta is in Kronecker's sense. In a similar fashion, the functions $e^2_{j,k}$ form an orthonormal set. So, the functions $e^1_{i,r},e^2_{j,k}$ together form an orthonormal set. Next, the dimension of the span equals the total number of vectors, which we calculate to $nq$, which equals the known dimension of the space $\mathrm{Pol}_{m,n,q}$. The proof is complete. ◻
:::

For $q\leq n$, we conclude that the reproducing kernel of $\mathrm{Pol}_{m,n,q}$ equals $$\begin{gathered}
\label{eq-Kmnq}
K_{m,n,q} (z,w) = m\sum_{r=0}^{q-1} 
\sum_{i=0}^{n-r-1} \frac{r!}{(r+i)!} 
(mz\bar{w})^i L_r^{i}(m|z|^2)L_r^{i}(m|w|^2) 
\\
+ m\sum_{j=0}^{q-2}\sum_{k=1}^{q-j-1} \frac{j!}{(k+j)!} 
(m\overline{z}w)^k L^{k}_{j}(m|z|^2)L^{k}_{j}(m|w|^2).
\end{gathered}$$ We note that by plugging in $n=+\infty$ in Proposition [\[on-kanta\]](#on-kanta){reference-type="ref" reference="on-kanta"} we get an orthonormal basis for the space $A^2_{m,q}({\mathbb C})$. It follows that the same procedure of plugging in $n=+\infty$ in the above expression for $K_{m,n,q}$ gives us $K_{m,q}$, the reproducing kernel for $A^2_{m,q}({\mathbb C})$. What is probably less obvious is that $K_{m,q}$ may be written in a much simpler form (this representation is, however, known; compare with [@AIM], [@Mou]).

::: prop
[]{#prop-repkern label="prop-repkern"} We have that $$\begin{gathered}
K_{m,q} (z,w) = m\sum_{r=0}^{q-1}\sum_{i=0}^{\infty} 
\frac{r!}{(r+i)!}(mz \bar{w})^i L_r^{i}(m|z|^2)L_r^{i}(m|w|^2) \notag 
\\
+m\sum_{j=0}^{q-2} \sum_{k=1}^{q-j-1} \frac{j!}{(j+k)!} 
(m\bar{z}w)^k L^{k}_{j}(m|z|^2)L^{k}_{j}(m|w|^2) \notag 
=m\,L^{1}_{q-1}(m|z-w|^2)\mathrm e^{m z \bar{w}}.\notag
\end{gathered}$$
:::

::: proof
*Proof.* It is clear from Proposition [\[on-kanta\]](#on-kanta){reference-type="ref" reference="on-kanta"} that the double sum expression equals $K_{m,q}(z,w)$, so the only thing that needs attention is the last equality. We first do the case $w=0$. Many of the terms in the double sum vanish, so that we are left with $$K_{m,q} (z,0)=m\sum_{r=0}^{q-1}L_r^{0}(m|z|^2)L_r^{0}(0),  
\notag$$ It is well-known that $L_r^{0}(0)=1$ and that $\sum_{r=0}^{q-1} L^{\alpha}_r=L^{\alpha+1}_{q-1}$, so that the above reduces to $$K_{m,q} (z,0) = m\, L^{1}_{q-1}(m|z|^2).  
\notag$$ We turn to general $w \in{\mathbb C}$. It is well-known that the transformation $${\mathbf T}_w[f](z):=\mathrm e^{-\frac12 m|w|^2-mz\bar w}f(z+w)$$ acts unitarily on $A^2_{m,q}({\mathbb C})$; its adjoint is ${\mathbf T}_w^*={\mathbf T}_{-w}$. By the reproducing property of $K_{m,q}(z,0)$, we have, for $f\in 
A^2_{m,q}({\mathbb C})$, $$\begin{gathered}
\mathrm e^{-\frac12m|w|^2}f(w)={\mathbf T}_w[f](0)=
\int_{\mathbb C}{\mathbf T}_w f(z)\overline{K_{m,q}(z,0)}\mathrm e^{-m|z|^2}{\mathrm d}A(z)
\\
=\int_{\mathbb C}f(z)\overline{{\mathbf T}_w^*[K_{m,q}(\cdot,0)](z)}\,
\mathrm e^{-m|z|^2}{\mathrm d}A(z)
\\
=m\mathrm e^{-\frac12m|w|^2}
\int_{\mathbb C}f(z)\,L^{1}_q(m|z-w|^2)\mathrm e^{m\bar z w}\mathrm e^{-m|z|^2}{\mathrm d}A(z),
\end{gathered}$$ The claim that $K_{m,q}(z,w)= m\,L^{1}_{q-1}(m|z-w|^2) 
\mathrm e^{mz\bar{w}}$ now follows immediately. ◻
:::

We shall show that the kernel $K_{m,n,q}(z,w)$ is approximated well by $K_{m,q}(z,w)$, provided that $z,w\in{\mathbb D}$ are rather close to one another. It will be instrumental to study the asymptotic behavior of the partial sums $$E_{k}(\zeta)=\sum_{j=0}^{k}\frac{1}{j!} \zeta^j$$ of the Taylor expansion of the exponential function. In [@szego], Szegö showed that $$\begin{aligned}
\label{szego1}
\frac{E_k(k\zeta)}{\mathrm e^{k\zeta}}= 1-\frac{1}{\sqrt{2 \pi k}}
(\zeta\mathrm e^{1-\zeta})^k \frac{\zeta}{1-\zeta}
(1+\epsilon^{1}_k(\zeta)),
\end{aligned}$$ provided that $|\zeta\mathrm e^{1-\zeta}|<1$ and $|\zeta|<1$, whereas $$\begin{aligned}
\label{szego2}
\frac{E_k(k\zeta)}{\mathrm e^{k\zeta}}= \frac{1}{\sqrt{2 \pi k}}(\zeta
\mathrm e^{1-\zeta})^k \frac{\zeta}{\zeta-1}
(1+\epsilon^{2}_k(\zeta)),
\end{aligned}$$ provided that $|\zeta\mathrm e^{1-\zeta}|<1$ and $|\zeta|>1$. Here, we have the convergence $$\lim_{k\to+\infty}\epsilon^{1}_k(z)=\lim_{k\to+\infty} \epsilon^{2}_k(z)=0$$ uniformly on compact subsets of the respective domains. As for [\[szego2\]](#szego2){reference-type="eqref" reference="szego2"}, the uniform convergence $\epsilon^{2}_k(\zeta)\to0$ as $k\to+\infty$ holds also in certain unbounded subdomains; in particular, along the real line, we have uniform convergence on all intervals $[a,+\infty[$ with $a>1$.

The following elementary estimate of generalized Laguerre polynomials will prove useful.

::: lem
[]{#laguerreestimaatti label="laguerreestimaatti"}

Suppose $\alpha$ is a positive real. Then, for $k=0,1,2,\ldots$, we have that $$|L^\alpha_k(x)|\le \frac{1}{k!}(x+\alpha+k)^k,\qquad x\in
[0,+\infty[.$$ Moreover, with $\beta:=\alpha+2k-2+2\sqrt{\frac14+(k-1)(k+\alpha-1)}$, we have that $$\frac{1}{k!}(x-\beta)^k\le (-1)^k L_k^{\alpha}(x)\le\frac{1}{k!}x^k,\qquad
x\in[\beta,+\infty[.$$ Actually, the related inequality $|L_k^{\alpha}(x)|\le\frac{1}{k!}x^k$ holds for all $x\in[\frac12\beta,+\infty[$.
:::

::: proof
*Proof.* We begin with the estimate ($0\le i\le k$ is assumed) $$(\alpha+i+1)_{k-i}\le(\alpha+k)^j.$$ Next, we note that for $x\ge0$ and $k=0,1,2,\ldots$, we have $$L^\alpha_k(x)=\sum_{i=0}^k(-1)^k\frac{(\alpha+i+1)_{k-i}}{i!(k-i)!}
x^i=\sum_{i\,\,\mathrm{even}}\frac{(\alpha+i+1)_{k-i}}{i!(k-i)!}
x^i-\sum_{i\,\,\mathrm{odd}}\frac{(\alpha+i+1)_{k-i}}{i!(k-i)!}
x^i,$$ and in view of the above estimate, $$\sum_{i\,\,\mathrm{even}}\frac{(\alpha+i+1)_{k-i}}{i!(k-i)!}
\le \sum_{i\,\,\mathrm{even}}\frac{(\alpha+k)^{k-i}}{i!(k-i)!}
=\frac{1}{2\,k!}\big((\alpha+k+x)^k+(\alpha+k-x)^k\big),$$ and, analogously, $$\sum_{i\,\,\mathrm{odd}}\frac{(\alpha+i+1)_{k-i}}{i!(k-i)!}
\le \sum_{i\,\,\mathrm{odd}}\frac{(\alpha+k)^{k-i}}{i!(k-i)!}
=\frac{1}{2\,k!}\big((\alpha+k+x)^k-(\alpha+k-x)^k\big).$$ By discarding alternatively the even or odd contribution, we arrive at $$|L^\alpha_k(x)|\le\frac{1}{2\,k!}\big((x+\alpha+k)^k+|\alpha+k-x|^k\big),$$ which is slightly stronger than the first estimate.

It is well-known that $L_k^\alpha$ is a polynomial of degree $k$ all of whose zeros are distinct and real, and they all fall in the interval $]0,\beta[$ (see 18.16.13 of [@orthopo]). The second estimate follows immediately from this. ◻
:::

We estimate the difference $K_{m,n,q}-K_{m,q}$.

::: prop
[]{#kernelestimate label="kernelestimate"} Let $z,w\in{\mathbb C}$ be such that $|zw|\le\theta_1<1$ and $|zw|\mathrm e^{1-|zw|}\le\theta_2<1$. Let $M$ be a positive real number. Then, as $m,n\to+\infty$ while $|m-n|\le M$, $$|K_{m,n,q}(z,w)-K_{m,q}(z,w)| \,\mathrm e^{-m|zw|}
\le C m^{q}\theta_2^m(1-\theta_1)^{-2}[1+|z|^{2q}+|w|^{2q}],$$ where the constant $C$ depends on $q$ and $M$.
:::

::: proof
*Proof.* In view of [\[eq-Kmnq\]](#eq-Kmnq){reference-type="eqref" reference="eq-Kmnq"} and Proposition [\[prop-repkern\]](#prop-repkern){reference-type="ref" reference="prop-repkern"}, we have that for $q\le n$, $$K_{m,q}(z,w)-K_{m,n,q}(z,w)=m\sum_{r=0}^{q-1}\sum_{i=n-r}^{+\infty}
\frac{r!}{(r+i)!}(mz \bar{w})^i L_r^{i}(m|z|^2)L_r^{i}(m|w|^2).$$ By Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"}, we get that $$\begin{gathered}
\label{eq-interm1}
\bigg| \sum^{+\infty}_{i=n-r} 
\frac{r!}{(r+i)!}(mz \bar{w})^i L_r^{i}(m|z|^2)L_r^{i}(m|w|^2)\bigg| 
\\
\le \sum^{+\infty}_{i=n-r}\frac{1}{r!(r+i)!}(m|zw|)^i(m|z|^2+i+r)^r
(m|w|^2+i+r)^r 
\\  
=\frac1{r!}\sum^{+\infty}_{j=0}\frac{1}{(n+j)!}(m|zw|)^{n-r+j}
(m|z|^2+n+j)^r(m|w|^2+n+j)^r
\\
\le 
\frac{4^{r-1}}{r!}\sum^{+\infty}_{j=0}\frac{1}{(n+j)!}(m|zw|)^{n-r+j}
[(m|z|^2)^r+(n+j)^r][(m|w|^2)^r+(n+j)^r].
\end{gathered}$$ For $r$ confined to $0\le r\le q-1$ and for big $n$, say $n\ge n_0(q)$, we have $$\frac{(n+j)^{2r}}{(n+j)!}\le \frac{2}{(n+j-2r)!}\quad\text{and}\quad
\frac{(n+j)^{r}}{(n+j)!}\le \frac{2}{(n+j-r)!},$$ so that if we use the notation $$R_k(z)=\sum_{j=k+1}^{+\infty}\frac1{j!}z^j=\mathrm e^z-E_k(z),$$ we obtain from [\[eq-interm1\]](#eq-interm1){reference-type="eqref" reference="eq-interm1"} that for $0\le r\le q-1$ and $n\ge n_0(q)$, $$\begin{gathered}
\label{eq-interm2}
\bigg| \sum^{+\infty}_{i=n-r} 
\frac{r!}{(r+i)!}(mz \bar{w})^i L_r^{i}(m|z|^2)L_r^{i}(m|w|^2)\bigg| 
\\
\le
\frac{4^{r-1}m^r}{r!}\Big[
|zw|^r R_{n-1}(m|zw|)+
2(|z|^{2r}+|w|^{2r}) R_{n-r-1}(m|zw|)
+2|zw|^r R_{n-2r-1}(m|zw|)\Big].
\end{gathered}$$ Next, we see from Szegö's asymptotical expansion [\[szego1\]](#szego1){reference-type="eqref" reference="szego1"} that for large $k,l$ with $l=k+\mathrm{O}(1)$, we have $$\begin{aligned}
\label{szego3}
\frac{R_k(l\zeta)}{\mathrm e^{l\zeta}}= (2 \pi k)^{-1/2}(l/k)^{k}
\frac{\zeta}{k/l-\zeta}(z\mathrm e^{1-l\zeta/k})^k(1+\epsilon^{1}_k(l\zeta/k)),
\end{aligned}$$ as $k,l\to+\infty$ and $l=k+\mathrm{O}(1)$. By a careful application of [\[szego3\]](#szego3){reference-type="eqref" reference="szego3"} to [\[eq-interm2\]](#eq-interm2){reference-type="eqref" reference="eq-interm2"}, and summing over $0\le r\le q-1$, the assertion of the proposition follows. ◻
:::

::: cor
[]{#cor-kapprox label="cor-kapprox"} For $z,w\in{\mathbb D}$, let $1-|zw|\ge\tau>0$. Then, as $m,n\to+\infty$, while $|m-n|\le M$, $$K_{m,n,q}(z,w)=K_{m,q}(z,w)+\mathrm{O}(\mathrm e^{-\frac12m\tau^2}
\mathrm e^{m|zw|}),$$ where the "$\mathrm{O}$" constant depends on $\tau$, $q$, and $M$.
:::

::: proof
*Proof.* A Taylor series expansion of the logarithm gives that $$t\,\mathrm e^{1-t}<\mathrm e^{-\frac12(1-t)^2},\qquad 0\le t<1,$$ and, together with the fact that the exponential function grows faster than any given power, the assertion follows from Proposition [\[kernelestimate\]](#kernelestimate){reference-type="ref" reference="kernelestimate"}. ◻
:::

As we shall see, Proposition [\[kernelestimate\]](#kernelestimate){reference-type="ref" reference="kernelestimate"} implies that the Berezin density $$\berd^{\langle z\rangle}_{m,n,q}(w)= 
\frac{|K_{m,n,q}(z,w)|^2 }{K_{m,n,q}(z,z)}\mathrm e^{-m|w|^2}$$ behaves locally near $z$ like the Berezin density $$\begin{gathered}
\label{eq-interm3}
\berd^{\langle z\rangle}_{m,q}(w)= 
\frac{| K_{m,q}(z,w)|^2 }{K_{m,q}(z,z)}\mathrm e^{-m|w|^2}=
\frac{m^2L^1_{q-1}(m|z-w|^2)^2\mathrm e^{2m\operatorname{Re}z\bar w}}
{mL^1_{q-1}(0)\,\mathrm e^{m|z|^2}}\,\mathrm e^{-m|w|^2}
\\
=\frac{m}{q}L^1_{q-1}(m|z-w|^2)^2\,\mathrm e^{-m|z-w|^2}.
\end{gathered}$$ To make this precise, we recall the definition of the blow-up Berezin density: $$\hat{\berd}^{\langle z\rangle}_{m,n,q}(\xi) = 
m^{-1}\berd^{\langle z\rangle}_{m,n,q}(z+m^{-1/2}\xi).$$

::: prop
[]{#prop-berconv label="prop-berconv"} Fix $z\in{\mathbb D}$. Then $$\int_{\mathbb{C}} \big|\hat{\berd}^{\langle z\rangle}_{m,n,q}(\xi)- 
q^{-1}L^{1}_{q-1}(|\xi|^2)^2\mathrm e^{-|\xi|^2} \big| {\mathrm d}A(\xi) 
\longrightarrow 0,$$ as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$.
:::

::: proof
*Proof.* By [\[eq-interm3\]](#eq-interm3){reference-type="eqref" reference="eq-interm3"}, we have $$\hat{\berd}^{\langle z\rangle}_{m,q}(\xi) = 
m^{-1}\berd^{\langle z\rangle}_{m,q}(z+m^{-1/2}\xi)=
q^{-1}L^{1}_{q-1}(|\xi|^2)^2\mathrm e^{-|\xi|^2},$$ so the comparison is with the blow-up Berezin density for $K_{m,q}$. We write $w:=z+m^{-1/2}\xi$; since $z\in{\mathbb D}$ is fixed, we have $1-|z|^2\ge\tau>0$ for some small $\tau$, and we suppose that $w$ is close to $z$ so that $1-|zw|\ge\tau>0$ as well. Then, by Proposition [\[prop-repkern\]](#prop-repkern){reference-type="ref" reference="prop-repkern"} and Corollary [\[cor-kapprox\]](#cor-kapprox){reference-type="ref" reference="cor-kapprox"}, $$\begin{gathered}
\berd^{\langle z\rangle}_{m,n,q}(w)= 
\frac{|K_{m,n,q}(z,w)|^2}{K_{m,n,q}(z,z)}\mathrm e^{-m|w|^2} 
=\frac{|K_{m,q}(z,w)+\mathrm{O}(\mathrm e^{-\frac12 m\tau^2}\mathrm e^{m|zw|}) 
|^2}{K_{m,q}(z,z)+ \mathrm{O}(\mathrm e^{-\frac12 m\tau^2}\mathrm e^{m|z|^2})}
\mathrm e^{-m|w|^2}  
\\
=\frac{\big|mL^{1}_{q-1}(m|z-w|^2)
\mathrm e^{mz\bar{w}} + \mathrm{O}(\mathrm e^{-\frac12 m\tau^2}\mathrm e^{m|zw|})  
\big|^2}{(mq+\mathrm{O}(\mathrm e^{-\frac12 m\tau^2}))\,\mathrm e^{m|z|^2}}\mathrm e^{-m|w|^2}, 
\end{gathered}$$ so that if we we expand the square using that $$|L^1_{q-1}(m|z-w|^2)|=\mathrm{O}(m^{q-1}),$$ where the "O" depends only on $q$ (this follows from Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"}), and simplify the expression, we arrive at $$\berd^{\langle z\rangle}_{m,n,q}(w)=
\frac{m}{q}L^{1}_{q-1}(m|z-w|^2)^2
\mathrm e^{-m|z-w|^2} + 
\mathrm{O}(m^{2q-2}\mathrm e^{-\frac12 m\tau^2}\mathrm e^{-m(|z|-|w|)^2}),$$ which immediate gives that $$\berd^{\langle z\rangle}_{m,n,q}(w)=
\frac{m}{q}L^{1}_{q-1}(m|z-w|^2)^2
\mathrm e^{-m|z-w|^2} + 
\mathrm{O}(m^{2q-2}\mathrm e^{-\frac12 m\tau^2}).$$ The corresponding blow-up Berezin density then has $$\label{eq-berasympt}
\hat\berd^{\langle z\rangle}_{m,n,q}(\xi)
=m^{-1}\berd^{\langle z\rangle}_{m,n,q}(z+m^{-1/2}\xi)
=q^{-1}L^{1}_{q-1}(|\xi|^2)^2
\mathrm e^{-|\xi|^2} + 
\mathrm{O}(m^{2q-3}\mathrm e^{-\frac12 m\tau^2}).$$ As exponentials grow faster than polynomials, the error terms is negligible for big $m$. For fixed $z\in{\mathbb D}$, the requirement on $\xi$ so that $1-|zw|\ge
\tau$ for some fixed $\tau>0$ is fulfilled for big $m$ if, say, $|\xi|\le\log m$ is required. So, [\[eq-berasympt\]](#eq-berasympt){reference-type="eqref" reference="eq-berasympt"} has the immediate consequence that $$\label{eq-berasympt2}
\int_{{\mathbb D}(0,\log m)}
\big|\hat\berd^{\langle z\rangle}_{m,n,q}(\xi)
-q^{-1}L^{1}_{q-1}(|\xi|^2)^2
\mathrm e^{-|\xi|^2}\big|\,{\mathrm d}A(\xi)=
\mathrm{O}\big(m^{2q-3}(\log m)^2\mathrm e^{-\frac12 m\tau^2}\big),$$ where more generally ${\mathbb D}(z_0,\rho)$ denotes the open disk of radius $\rho$ about $z_0$. Since the associated blow-up Berezin measures $${\mathrm d}\hat B^{\langle z\rangle}_{m,n,q}(\xi):=
\hat\berd^{\langle z\rangle}_{m,n,q}(w)
{\mathrm d}A(\xi),\qquad {\mathrm d}\hat B^{\langle z\rangle}_{m,q}(\xi):=
q^{-1}L^1_{q-1}(|\xi|^2)^2\mathrm e^{-|\xi|^2}{\mathrm d}A(\xi),$$ are both probability measures, the assertion of the proposition follows from [\[eq-berasympt2\]](#eq-berasympt2){reference-type="eqref" reference="eq-berasympt2"} once it is noted that the right-hand side of [\[eq-berasympt2\]](#eq-berasympt2){reference-type="eqref" reference="eq-berasympt2"} tends to $0$ as $m\to+\infty$. ◻
:::

We note that the claimed convergence ${\mathrm d}B^{\langle z\rangle}_{m,nq}\to
{\mathrm d}\delta_z$ for $z\in{\mathbb D}$ is an immediate consequence of Proposition [\[prop-berconv\]](#prop-berconv){reference-type="ref" reference="prop-berconv"}.
