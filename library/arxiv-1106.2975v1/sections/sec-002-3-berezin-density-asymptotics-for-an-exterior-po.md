---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-002-3-berezin-density-asymptotics-for-an-exterior-po
section_title: "Berezin density asymptotics for an exterior point"
section_number: 3
pages: 14-21
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.975
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
We show that the Berezin measures have the convergence ${\mathrm d}B^{\langle z\rangle}_{m,n,q}\to{\mathrm d}\omega_z$ for $z\in{\mathbb D}^e$ as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$. Here, $\omega_z$ is harmonic measure with respect to the point $z$ and the exterior disk $\mathbb{D}^e$.

We first study the concentration of the Berezin measure to neighborhoods of the closed unit disk $\bar{\mathbb D}$. We recall the standard notation ${\mathbb D}(z_0,\rho)$ for the open disk of radius $\rho$ centered at $z_0$.

::: lem
Suppose $z\in{\mathbb D}^e$ and that $\rho>1$. Then $$\int_{{\mathbb C}\setminus{\mathbb D}(0,\rho)}\berd^{\langle z\rangle}_{m,n,q}(w)\,
{\mathrm d}A(w) \to 0,$$ as $m,n\to+\infty$ while $n\leq m+\mathrm{O}(1)$.
:::

::: proof
*Proof.* Let $w\in{\mathbb C}\setminus{\mathbb D}(0,\rho)$. We note that $$n-1\le m+\mathrm{O}(1)\le 2m
\label{eq-triv1}$$ for sufficiently big $m$, and so, by Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"},

$$\begin{gathered}
\label{isonosanestimaatti}
\sum_{i=0}^{n-r-1} \frac{r!}{(r+i)!} 
\big|(mz\bar{w})^iL_r^{i}(m|z|^2)L_r^{i}(m|w|^2)\big| 
\\
\le\sum_{i=0}^{n-r-1} \frac{1}{r!(r+i)!} 
(m|zw|)^i(m|z|^2+i+r)^r(m|w|^2+i+r)^r 
\\



\leq \frac{9^{r}}{r!}\sum_{i=0}^{n-r-1} \frac{1}{(r+i)!}(m|zw|)^{i+2r}
\le\frac{9^{r}}{r!}(m|zw|)^{r}\,E_{n-1}(m|zw|). 
\end{gathered}$$

If we plug in $n=q$ in [\[isonosanestimaatti\]](#isonosanestimaatti){reference-type="eqref" reference="isonosanestimaatti"}, we obtain

$$\label{pienenosanestimaatti}
\sum_{k=1}^{q-j-1} \frac{j!}{(j+k)!} 
\big|(m\bar{z}w)^k L^{k}_{j}(m|z|^2)L^{k}_{j}(m|w|^2)\big|  
\leq \frac{9^j}{j!}(m|zw|)^j E_{q-1}(m|zw|).$$

We may restrict to $q\le n$; after, we are considering the limit as $n\to+\infty$. As $E_{q-1}\le E_{n-1}$ on the positive half-axis for $q\le n$, an application of [\[isonosanestimaatti\]](#isonosanestimaatti){reference-type="eqref" reference="isonosanestimaatti"} and [\[pienenosanestimaatti\]](#pienenosanestimaatti){reference-type="eqref" reference="pienenosanestimaatti"} to [\[eq-Kmnq\]](#eq-Kmnq){reference-type="eqref" reference="eq-Kmnq"} gives $$\label{isonosanestimaatti4}
|K_{m,n,q}(z,w)| 
\leq 2m\mathrm e^9(m|zw|)^{q-1}E_{n-1}(m|zw|).$$ Next, we observe that $\mathrm{Pol}_{m,n,1}\subset \mathrm{Pol}_{m,n,q}$ (since $q\ge1$), which implies that $$K_{m,n,q}(z,z) \geq K_{m,n,1}(z,z)=mE_{n-1}(m|z|^2).$$ We conclude that the Berezin density may be estimated as follows: $$\begin{aligned}
\label{suttuvertausanalyyttiseen}
\berd^{\langle z\rangle}_{m,n,q}(w) \leq  
4m\,\mathrm e^{18}(m|zw|)^{2q-2}\frac{E_{n-1}(m|zw|)^2}{E_{n-1}(m|z|^2)}
\mathrm e^{-m|w|^2}.
\end{aligned}$$ Finally, we see from Szegö's asymptotical expansion [\[szego2\]](#szego2){reference-type="eqref" reference="szego2"} that $$\begin{aligned}
\label{szego4}
\frac{E_k(l\zeta)}{\mathrm e^{l\zeta}}= (2 \pi k)^{-1/2}(l/k)^{k}
\frac{\zeta}{z-k/l}(\zeta\mathrm e^{1-l\zeta/k})^k(1+\epsilon^{2}_k(l\zeta/k)).
\end{aligned}$$ $k\le l+\mathrm{O}(1)$, where the convergence $\epsilon^{2}_k(l\zeta/k)\to0$ is uniform if $\zeta$ is real with $\zeta\ge a$ for some fixed $a>1$. This leads to $$\frac{E_{n-1}(m|zw|)^2}{E_{n-1}(m|z|^2)}=[2\pi(n-1)]^{-1/2}[(n-1)/m]^{n-1}
\mathrm e^{n-1}|w|^{2n-2}(1+\mathrm{o}(1)),$$ where the "$\mathrm{o}$" term is uniform in the convergence. As we implement this estimate in [\[suttuvertausanalyyttiseen\]](#suttuvertausanalyyttiseen){reference-type="eqref" reference="suttuvertausanalyyttiseen"}, and integrate over ${\mathbb C}\setminus
{\mathbb D}(0,\rho)$, the claim follows. ◻
:::

We follow the approach of [@ahm1], and calculate a certain principal value integral.

::: lem
Fix $z\in{\mathbb D}^e$. For any $l=0,1,2,\ldots$, we have $$\operatorname{\mathrm{pv}}
\int_{\mathbb{C}}w^{-l} \berd^{\langle z\rangle}_{m,n,q}(w){\mathrm d}A(w)
\to z^{-l},$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$.
:::

::: proof
*Proof.* The case $q=1$ was treated in [@ahm1], so we may from now on assume that $q\ge2$. We write $$K_{m,n,q}=K_{m,n,q}^I+K_{m,n,q}^{II},$$ where $$K_{m,n,q}^I(z,w):=m\sum_{r=0}^{q-1}\sum_{i=0}^{n-r-1} 
\frac{r!}{(r+i)!}(mz \bar{w})^i L_r^{i}(m|z|^2)L_r^{i}(m|w|^2)$$ and $$K_{m,n,q}^{II}(z,w):=
m\sum_{j=0}^{q-2} \sum_{k=0}^{q-j-1} \frac{j!}{(j+k)!} 
(m\bar{z}w)^k L^{k}_{j}(m|z|^2)L^{k}_{j}(m|w|^2).$$ It follows that the expression $|K_{m,n,q}|^2$ decomposes accordingly: $$|K_{m,n,q}(z,w)|^2
=|K_{m,n,q}^I(z,w)|^2+|K_{m,n,q}^{II}(z,w)|^2
+2\operatorname{Re}[ K_{m,n,q}^I(z,w)\overline{K_{m,n,q}^{II}(z,w)}].
\label{eq-decomp}$$ We first consider the following integral involving $|K_{m,n,q}^I|^2$: $$\begin{gathered}
\operatorname{\mathrm{pv}}\int_{\mathbb{C}} w^{-l} 
|K^I_{m,n,q}(z,w)|^2\mathrm e^{-m|w|^2} {\mathrm d}A(w) 
\label{extpoint-rivi5} 
\\
=m^2 \sum_{r_1,r_2=0}^{q-1}\sum_{i_1=0}^{n-r_1-1} \sum_{i_2=0}^{n-r_2-1}
\operatorname{\mathrm{pv}}\int_{{\mathbb C}} w^{-l} 
\frac{r_1!r_2!}{(r_1+i_1)!(r_2+i_2)!}(mz\bar{w})^{i_1}(m\bar{z}w)^{i_2}
\\
\times L_{r_1}^{i_1}(m|z|^2)L^{i_1}_{r_1}(m|w|^2)L^{i_2}_{r_2}(m|z|^2)
L^{i_2}_{r_2}(m|w|^2) \mathrm e^{-m|w|^2}{\mathrm d}A(w)
\\
=m^2 z^{-l}
\sum_{r_1,r_2=0}^{q-1}\sum_{i_1=0}^{n-r_1-1}\sum_{i_2=0}^{n-r_2-1}
\frac{m^{i_1+i_2}r_1!r_2!}{(r_1+i_1)!(r_2+i_2)!}\delta_{i_2,i_1+l}\,|z|^{2i_2}
L_{r_1}^{i_1}(m|z|^2)L^{i_2}_{r_2}(m|z|^2)
\\
\times\int_{{\mathbb C}} |w|^{2i_1} L^{i_1}_{r_1}(m|w|^2)
L^{i_2}_{r_2}(m|w|^2) \mathrm e^{-m|w|^2}{\mathrm d}A(w),
\end{gathered}$$ where the delta is understood in Kronecker's sense. The identity (for $p=1,2,3,\ldots$) $$\label{recurrencerelation}
L^{\alpha+p}_r(x)= \sum_{s=0}^r \binom{r-s+p-1}{p-1}\,
L_{s}^{\alpha}(x)$$ plus the standard orthogonality properties of the Laguerre polynomials gives that $$\int_0^{+\infty}t^{i_1}L_{r_1}^{i_1}(t)L_{r_2}^{i_1+l}(t)\mathrm e^{-t}{\mathrm d}t=
\frac{(r_1+i_1)!(r_2-r_1+l-1)!}{r_1!(r_2-r_1)!(l-1)!},$$ where the right-hand side should be interpreted as $0$ for $r_2<r_1$. By polar coordinates, then, we have $$\int_{\mathbb C}|w|^{2i_1}L_{r_1}^{i_1}(m|w|^2)L_{r_2}^{i_1+l}(m|w|^2)\mathrm e^{-m|w|^2}
{\mathrm d}A(w)=
m^{-i_1-1}\frac{(r_1+i_1)!(r_2-r_1+l-1)!}{r_1!(r_2-r_1)!(l-1)!},$$ and [\[extpoint-rivi5\]](#extpoint-rivi5){reference-type="eqref" reference="extpoint-rivi5"} simplifies to $$\begin{gathered}
\label{extpoint-rivi5.5}
\operatorname{\mathrm{pv}}\int_{\mathbb{C}} w^{-l} 
|K^I_{m,n,q}(z,w)|^2\mathrm e^{-m|w|^2} {\mathrm d}A(w) 

\\
=m\,z^{-l}
\sum_{r_1=0}^{q-1}\sum_{r_2=r_1}^{q-1}\sum_{i_1=0}^{n-l-r_2-1}
\frac{r_2!(r_2-r_1+l-1)!}{(r_2-r_1)!(l-1)!(r_2+i_1+l)!}
\,(m|z|^{2})^{i_1+l}L_{r_1}^{i_1}(m|z|^2)L^{i_1+l}_{r_2}(m|z|^2),
\end{gathered}$$ provided $n$ is so big that $q+l\le n$. Next, we apply Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"} and [\[eq-triv1\]](#eq-triv1){reference-type="eqref" reference="eq-triv1"} (using that $z\in{\mathbb D}^e$) to arrive at $$\begin{gathered}
\label{extpoint-rivi5.6}
\sum_{i_1=0}^{n-l-r_2-1}\frac{r_1!r_2!}{(r_2+i_1+l)!} 
\,(m|z|^{2})^{i_1+l}\big|L_{r_1}^{i_1}(m|z|^2)L^{i_1+l}_{r_2}(m|z|^2)\big|
\\
\le\sum_{i_1=0}^{n-l-r_2-1}\frac{1}{(r_2+i_1+l)!} 
\,(m|z|^{2})^{i_1+l}(m|z|^2+i_1+r_1)^{r_1}(m|z|^2+i_1+l+r_2)^{r_2}
\\
\le 3^{r_1+r_2}\sum_{i_1=0}^{n-l-r_2-1}\frac{1}{(r_2+i_1+l)!} 
\,(m|z|^{2})^{r_1+r_2+i_1+l}\le 3^{r_1+r_2}(m|z|^2)^{r_1}E_{n-1}(m|z|^2).
\end{gathered}$$

On the other hand, by the estimate from below in Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"}, $$\begin{gathered}
\label{berezin-outside-onepointestimate}
K_{m,n,q}(z,z) \geq K^{I}_{m,n,q}(z,z)=
m\sum_{r=0}^{q-1} \sum_{i=0}^{n-r-1} \frac{r!}{(r+i)!} 
(m|z|^2)^i L^{i}_{r}(m|z|^2)^2
\\
\ge m\sum_{r=0}^{q-1} \sum_{i=0}^{n-r-1} \frac{1}{r!(r+i)!} 
(m|z|^2)^i [m|z|^2-\beta(n)]^{2r}
\end{gathered}$$ provided that $m|z|^2\ge\beta(n)$, where $$\beta(n):=n+q-4+2\sqrt{\tfrac14+(q-2)(n-1)}=n+\mathrm{O}(\sqrt{n}).$$ As we assume $z\in{\mathbb D}^e$ and $n=m+\mathrm{O}(1)$, we must have $$m|z|^2-\beta(n)=m(|z|^2-1)+m-\beta(n)\ge \tfrac12 m(|z|^2-1)$$ for big enough $m,n$, and so, by [\[berezin-outside-onepointestimate\]](#berezin-outside-onepointestimate){reference-type="eqref" reference="berezin-outside-onepointestimate"}, $$\begin{gathered}
\label{berezin-outside-onepointestimate2}
K_{m,n,q}(z,z) \geq K^{I}_{m,n,q}(z,z)
\ge m\sum_{r=0}^{q-1} \sum_{i=0}^{n-r-1} \frac{4^{-r}}{r!(r+i)!} 
(m|z|^2)^{i+2r} 
\\
\ge\frac{4^{1-q}m}{(q-1)!}(m|z|)^{q-1}[E_{n-1}(m|z|^2)-
E_{q-2}(m|z|^2)]\ge\frac{4^{-q}m}{(q-1)!}(m|z|)^{q-1}E_{n-1}(m|z|^2).
\end{gathered}$$ Here, we used that the $E_{n-1}(m|z|^2)$ is much bigger than $E_{q-2}(m|z|^2)$ as $m,n$ both grow. Let us look at the contribution from $0\le r_1\le q-2$ in the right-hand side of [\[extpoint-rivi5.5\]](#extpoint-rivi5.5){reference-type="eqref" reference="extpoint-rivi5.5"} using the estimate [\[extpoint-rivi5.6\]](#extpoint-rivi5.6){reference-type="eqref" reference="extpoint-rivi5.6"}: $$\begin{gathered}
m\,|z|^{-l}
\sum_{r_1=0}^{q-2}\sum_{r_2=r_1}^{q-1}\sum_{i_1=0}^{n-l-r_2-1}
\frac{r_2!(r_2-r_1+l-1)!}{(r_2-r_1)!(l-1)!(r_2+i_1+l)!}
\,(m|z|^{2})^{i_1+l}\big|L_{r_1}^{i_1}(m|z|^2)L^{i_1+l}_{r_2}(m|z|^2)\big|
\\
\le 
m\,\frac{|z|^{-l}}{(l-1)!}\sum_{r_1=0}^{q-2}\sum_{r_2=r_1}^{q-1}
\frac{(r_2-r_1+l-1)!}{r_1!(r_2-r_1)!}3^{r_1+r_2}(m|z|^2)^{r_1}E_{n-1}(m|z|^2)
\\
\le m C_1(q,l)(m|z|^2)^{q-2}E_{n-1}(m|z|^2),
\end{gathered}$$ for an appropriate positive constant $C_1(q,l)$. As we combine this estimate with [\[berezin-outside-onepointestimate2\]](#berezin-outside-onepointestimate2){reference-type="eqref" reference="berezin-outside-onepointestimate2"}, we obtain $$\begin{gathered}
m\,\frac{|z|^{-l}}{K_{m,n,q}(z,z)}
\sum_{r_1=0}^{q-2}\sum_{r_2=r_1}^{q-1}\sum_{i_1=0}^{n-l-r_2-1}
\frac{r_2!(r_2-r_1+l-1)!}{(r_2-r_1)!(l-1)!(r_2+i_1+l)!}
\\
\times(m|z|^{2})^{i_1+l}\big|L_{r_1}^{i_1}(m|z|^2)L^{i_1+l}_{r_2}(m|z|^2)\big|
\le C_2(q,l)m^{-1}=\mathrm{O}(m^{-1})\longrightarrow0,
\end{gathered}$$ as $m,n\to+\infty$ in the prescribed fashion. So the contribution to [\[extpoint-rivi5.5\]](#extpoint-rivi5.5){reference-type="eqref" reference="extpoint-rivi5.5"} which comes from $0\le r_1\le q-2$ is negligible from the point of view of the Berezin density. It remains to consider the contribution from $r_1=q-1$. The corresponding part of the sum in the right-hand side of [\[extpoint-rivi5.5\]](#extpoint-rivi5.5){reference-type="eqref" reference="extpoint-rivi5.5"} equals $$m\,z^{-l}
\sum_{i_1=0}^{n-l-q}
\frac{(q-1)!}{(q+i_1+l-1)!}
\,(m|z|^{2})^{i_1+l}L_{q-1}^{i_1}(m|z|^2)L^{i_1+l}_{q-1}(m|z|^2),$$ and we now claim that $$\label{extpoint-rivi5.7}
m\,\frac{z^{-l}}{K_{m,n,q}(z,z)}
\sum_{i_1=0}^{n-l-q}
\frac{(q-1)!}{(q+i_1+l-1)!}
\,(m|z|^{2})^{i_1+l}L_{q-1}^{i_1}(m|z|^2)L^{i_1+l}_{q-1}(m|z|^2)
\longrightarrow z^{-l},$$ as $m,n\to+\infty$ in the given fashion. We use the recurrence relation ([\[recurrencerelation\]](#recurrencerelation){reference-type="ref" reference="recurrencerelation"}) to write $$\label{eq-triv2}
L^{i_1}_{q-1}(x) = L^{i_1+l}_{q-1}(x)- \sum_{s=0}^{q-2} 
\binom{q+l-s-2}{l-1}\, L^{i_1}_s(x).$$ A straightforward argument allows us to show that as insert this into [\[extpoint-rivi5.7\]](#extpoint-rivi5.7){reference-type="eqref" reference="extpoint-rivi5.7"}, the sum that is subtracted on the right-hand side of [\[eq-triv2\]](#eq-triv2){reference-type="eqref" reference="eq-triv2"} makes asymptotically no contribution to the sum in [\[extpoint-rivi5.7\]](#extpoint-rivi5.7){reference-type="eqref" reference="extpoint-rivi5.7"}. Consequently, [\[extpoint-rivi5.7\]](#extpoint-rivi5.7){reference-type="eqref" reference="extpoint-rivi5.7"} is equivalent to having $$\begin{aligned}
\label{eq-triv3}
m\,\frac{z^{-l}}{K_{m,n,q}(z,z)}\sum_{i_1=0}^{n-l-q} \frac{(q-1)!}
{(q+i_1+l-1)!} (m|z|^2)^{i_1+l} L^{i_1+l}_{q-1}(m|z|^2)^2
\longrightarrow z^{-l}  
\end{aligned}$$ as $m,n\to+\infty$ in the given fashion. If we insert the expression [\[eq-Kmnq\]](#eq-Kmnq){reference-type="eqref" reference="eq-Kmnq"} defining $K_{m,n,q}(z,z)$, we see that (there is some cancellation of terms) $$\begin{gathered}
z^{-l}-m\,\frac{z^{-l}}{K_{m,n,q}(z,z)}\sum_{i_1=0}^{n-l-q} 
\frac{(q-1)!}
{(q+i_1+l-1)!} (m|z|^2)^{i_1+l} L^{i_1+l}_{q-1}(m|z|^2)
L^{i_1+l}_{q-1}(m|z|^2)  
\\
=\frac{z^{-l}}{K_{m,n,q}(z,z)}\Bigg\{
m\sum_{r=0}^{q-2}\sum_{i=0}^{n-r-1} \frac{r!}{(r+i)!} 
(m|z|^2)^i L_r^{i}(m|z|^2)^2 
\\
+m \sum_{j=1}^{q-2}\sum_{k=1}^{q-j-1} \frac{j!}{(j+k)!} 
(m|z|^2)^k L^{k}_{j}(m|z|^2)^2 
+m\sum_{i_1=0}^{l-1} \frac{(q-1)!}
{(q+i-1)!} (m|z|^2)^{i} L^{i}_{q-1}(m|z|^2)^2
\Bigg\}.
\end{gathered}$$ By careful application of Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"} to all the Laguerre polynomials in this expression, while inserting [\[berezin-outside-onepointestimate\]](#berezin-outside-onepointestimate){reference-type="eqref" reference="berezin-outside-onepointestimate"} to control the denominator, we indeed get [\[eq-triv3\]](#eq-triv3){reference-type="eqref" reference="eq-triv3"}. So, after a lot of effort, we have obtained that $$\label{eq-triv5}
\operatorname{\mathrm{pv}}
\int_{\mathbb{C}} w^{-l} 
\frac{|K^I_{m,n,q}(z,w)|^2}{K_{m,n,q}(z,z)}\mathrm e^{-m|w|^2} {\mathrm d}A(w) 
\longrightarrow z^{-l}$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$. Analogous but slightly easier arguments (left to the interested reader) show that $$\operatorname{\mathrm{pv}}
\int_{\mathbb{C}}w^{-j}\frac{|K^{II}_{m,n,q}(z,w)|^2}{K_{m,n,q}(z,z)} 
\mathrm e^{-|w|^2}{\mathrm d}A(w) \longrightarrow 0$$ and $$\int_{\mathbb{C}}w^{-j}\operatorname{Re}\Bigg\{\frac{K^{I}_{m,n,q}(z,w)
\overline{K^{II}_{m,n,q}(z,w)}}{K_{m,n,q}(z,z)}\Bigg\}
\,\mathrm e^{-|w|^2}{\mathrm d}A(w) \longrightarrow 0,$$ again as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$. Finally, we put everything together based on the decomposition [\[eq-decomp\]](#eq-decomp){reference-type="eqref" reference="eq-decomp"}: $$\operatorname{\mathrm{pv}}\int_{\mathbb{C}}w^{-j}\berd^{\langle z\rangle}_{m,n,q}(w)=\operatorname{\mathrm{pv}}\int_{{\mathbb C}}
\frac{|K_{m,n,q}(z,w)|^2}{K_{m,n,q}(z,z)}\,\mathrm e^{-|w|^2}{\mathrm d}A(w) 
\longrightarrow z^{-l},$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$. This ends the proof. ◻
:::

We now show that even in the principal value sense, the Berezin density tends to avoid the interior of the unit disk.

::: lem
Fix a real parameter $\rho$ with $0<\rho<1$ and a point $z\in{\mathbb D}^e$. Then, for $l=0,1,2,\ldots$, we have the convergence $$\operatorname{\mathrm{pv}}\int_{{\mathbb D}(0,\rho)}w^{-l}\berd^{\langle z\rangle}_{m,n,q}(w){\mathrm d}A(w) 
\longrightarrow0,$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$.
:::

::: proof
*Proof.* In terms of the decomposition [\[eq-decomp\]](#eq-decomp){reference-type="eqref" reference="eq-decomp"}, we will focus on the the term $|K^I_{m,n,q}|^2$ and leave the other two to the reader (the necessary arguments are similar but slightly easier). The analogue of [\[extpoint-rivi5\]](#extpoint-rivi5){reference-type="eqref" reference="extpoint-rivi5"} reads $$\begin{gathered}
\label{eq-triv7}
\operatorname{\mathrm{pv}}\int_{{\mathbb D}(0,\rho)} w^{-l} 
|K^I_{m,n,q}(z,w)|^2\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\\
= m^{2} z^{-l} \sum_{r_1,r_2=0}^{q-1}
\sum_{i_1=0}^{\min\{n-r_1-1,n-l-r_2-1\}}
\frac{r_1!r_2!}{(r_1+i_1)!(r_2+i_1+l)!}
m(|z|^2)^{i_1+l}L^{i_1}_{r_1}(m|z|^2)L^{i_1+l}_{r_2}(m|z|^2) 
\\
\times\int_{{\mathbb D}(0,\rho)} (m|w|^2)^{i_1}L^{i_1}_{r_1}(m|w|^2)
L^{i_1+l}_{r_2}(m|w|^2)\mathrm e^{-m|w|^2} {\mathrm d}A(w). 
\end{gathered}$$ By Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"}, we have $$\begin{gathered}
\int_{{\mathbb D}(0,\rho)} (m|w|^2)^{i_1}\big|L^{i_1}_{r_1}(m|w|^2)
L^{i_1+l}_{r_2}(m|w|^2)\big|\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\\
\le\frac{1}{r_1!r_2!}\int_{{\mathbb D}(0,\rho)} (m|w|^2)^{i_1}(m|w|^2+i_1+r_1)^{r_1}
(m|w|^2+i_1+l+r_2)^{r_2}\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\\
\le
\frac{2^{r_1+r_2-2}}{r_1!r_2!}\int_{{\mathbb D}(0,\rho)} (m|w|^2)^{i_1}
[(m|w|^2)^{r_1}+(i_1+r_1)^{r_1}][
(m|w|^2)^{r_2}+(i_1+l+r_2)^{r_2}]\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\\
=\frac{2^{r_1+r_2-2}}{r_1!r_2!m}\Bigg\{
\int_0^{m\rho^2}t^{i_1+r_1+r_2}\mathrm e^{-t}{\mathrm d}t+
(i_1+r_1)^{r_1}\int_0^{m\rho^2}t^{i_1+r_2}\mathrm e^{-t}{\mathrm d}t
\\
+(i_1+l+r_2)^{r_2}\int_0^{m\rho^2}t^{i_1+r_1}\mathrm e^{-t}{\mathrm d}t
+(i_1+r_1)^{r_1}(i_1+l+r_2)^{r_2}\int_0^{m\rho^2}t^{i_1}\mathrm e^{-t}{\mathrm d}t\Bigg\}.
\end{gathered}$$ In terms of the function $$\chi(a,b):=\frac{1}{\Gamma(a+1)}\int_0^b t^a \mathrm e^{-t}{\mathrm d}t,
\qquad a,b\in[0,+\infty[,$$ which takes values in the interval $[0,1[$, the estimate becomes $$\begin{gathered}

\int_{{\mathbb D}(0,\rho)} (m|w|^2)^{i_1}\big|L^{i_1}_{r_1}(m|w|^2)
L^{i_1+l}_{r_2}(m|w|^2)\big|\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\\
\le\frac{2^{r_1+r_2-2}}{r_1!r_2!m}\Bigg\{
(i_1+r_1+r_2)!\chi(i_1+r_1+r_2,m\rho^2)+
(i_1+r_1)^{r_1}(i_1+r_2)!\chi(i_1+r_2,m\rho^2)
\\
+(i_1+l+r_2)^{r_2}(i_1+r_1)!\chi(i_1+r_1,m\rho^2)
+(i_1+r_1)^{r_1}(i_1+l+r_2)^{r_2}i_1!\chi(i_1,m\rho^2)\Bigg\}.
\end{gathered}$$ and if we use that $a\mapsto\chi(a,b)$ is decreasing for fixed $b$ (a direct calculation involving derivatives suffices to verify this), we get $$\begin{gathered}
\label{eq-triv8}
\int_{{\mathbb D}(0,\rho)} (m|w|^2)^{i_1}\big|L^{i_1}_{r_1}(m|w|^2)
L^{i_1+l}_{r_2}(m|w|^2)\big|\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\\
\le\frac{2^{r_1+r_2-2}}{r_1!r_2!m}\Bigg\{
(i_1+r_1+r_2)!+
(i_1+r_1)^{r_1}(i_1+r_2)!
\\
+(i_1+l+r_2)^{r_2}(i_1+r_1)!
+(i_1+r_1)^{r_1}(i_1+l+r_2)^{r_2}i_1!\Bigg\}\chi(i_1,m\rho^2).
\end{gathered}$$ Next, since $z\in{\mathbb D}^e$, $n=m+\mathrm{O}(1)$, and $i_1+l\le n-1$, we may use another aspect of Lemma [\[laguerreestimaatti\]](#laguerreestimaatti){reference-type="ref" reference="laguerreestimaatti"} to see that $$\label{eq-triv9}
\big|L^{i_1}_{r_1}(m|z|^2)L^{i_1+l}_{r_2}(m|z|^2)\big|\le\frac{1}{r_1!r_2!}
(m|z|^2)^{r_1+r_2},$$ provided $m,n$ are big enough. As we combine the equality [\[eq-triv7\]](#eq-triv7){reference-type="eqref" reference="eq-triv7"} with the estimates [\[eq-triv8\]](#eq-triv8){reference-type="eqref" reference="eq-triv8"} and [\[eq-triv9\]](#eq-triv9){reference-type="eqref" reference="eq-triv9"}, and use some well-understood comparisons of factorials and powers, we arrive at $$\begin{gathered}
\label{eq-triv10}
\bigg|\operatorname{\mathrm{pv}}\int_{{\mathbb D}(0,\rho)} w^{-l} 
|K^I_{m,n,q}(z,w)|^2\mathrm e^{-m|w|^2} {\mathrm d}A(w)\bigg|
\\
\le m\,C_3(q,l)|z|^{-l+2q-2}\sum_{i_1=0}^{n-l-1}
\frac{(m|z|^2)^{i_1+l}}{(i_1+l)!}\chi(i_1,m\rho^2),
\end{gathered}$$ for some appropriate positive constant $C_3(q,l)$. The function $\chi(i_1,m\rho^2)$ drops off exponentially quickly to $0$ as $i_1$ exceeds $m\rho^2$ by a margin greater than $\mathrm{O}(m^{1/2})$, as can be seen, e.g., by an application of the Central Limit Theorem (compare with the next section). This means that effectively we are summing up to $m|\rho|^2+\mathrm{O}(m^{1/2})$ in the right-hand side expression of [\[eq-triv10\]](#eq-triv10){reference-type="eqref" reference="eq-triv10"}, which does not permit the sum to compare with the size of $K_{m,n,q}(z,z)$; cf. [\[berezin-outside-onepointestimate2\]](#berezin-outside-onepointestimate2){reference-type="eqref" reference="berezin-outside-onepointestimate2"}. This results in the convergence $$\operatorname{\mathrm{pv}}\int_{{\mathbb D}(0,\rho)} w^{-l} 
\frac{|K^I_{m,n,q}(z,w)|^2}{K_{m,n,q}(z,z)}\,\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\longrightarrow0$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$. Together with the estimates which were left as an exercise to the reader, we get $$\operatorname{\mathrm{pv}}\int_{{\mathbb D}(0,\rho)} w^{-l} 
\frac{|K_{m,n,q}(z,w)|^2}{K_{m,n,q}(z,z)}\,\mathrm e^{-m|w|^2} {\mathrm d}A(w)
\longrightarrow0$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$, which amounts to the assertion of the lemma. ◻
:::

As in the proof of the Theorem 2.11 in [@ahm1], we may now conclude the following.

::: thm
Fix $z\in{\mathbb D}^e$ and a bounded continuous function $g$ on $\mathbb{C}$. Then $$\int_{{\mathbb C}}g(w)\berd^{\langle z\rangle}_{m,n,q}(w){\mathrm d}A(w)\to\int_{{\mathbb C}}g(w)
{\mathrm d}\omega(w,z, \mathbb{D}^*) ,$$ as $m,n \to+\infty$ with $n=m+\mathrm{O}(1)$. Here, ${\mathrm d}\omega(w,z, \mathbb{D}^*)$ is harmonic measure with respect to the point $z$ and the domain ${\mathbb D}^e$.
:::
