---
doc_id: arxiv-math-0006051v1
doc_title: "Finite and p-adic polylogarithms"
section_id: sec-001-2-the-proof
section_title: "The proof"
section_number: 2
pages: 2-5
source_pdf: 0006051v1.pdf
source_sha256: 10483e75bd3655ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.935
doc_brief: "Finite and p-adic polylogarithms — 4 sections: Front matter; Introduction; The proof"
---
[]{#sec:proof label="sec:proof"}

The connection between $p$-adic and finite polylogarithms is made by the following

::: proposition
Let $\operatorname{Li}^{(p)}_n(z):= \operatorname{Li}_n(z)- \operatorname{Li}_n(z^p)/p^n$. Then $\operatorname{Li}^{(p)}_n(X) \subset
  W$ and the function $\operatorname{Li}^{(p)}_n$ reduces modulo $p$ to $(1-z^p)^{-1}
  \operatorname{li}_n(z)$.
:::

::: proof
*Proof.* According to [@Col82], the function $\operatorname{Li}^{(p)}_n(z)$ can be computed as $$\operatorname{Li}^{(p)}_n(z)= \int_{\mathbb{Z}_p^\times}x^{-n} d\mu_z(x)\;,$$ where $\mu_z$ is the measure on $\mathbb{Z}_p$ defined by $$\mu_z(a+p^m \mathbb{Z}_p) = \frac{z^a}{1-z^{p^m}}\quad a=0,1,\ldots,p^m-1\;.$$ Since for $z\in X$ $\mu_z$ takes integral values, this shows the first statement. Reducing modulo $p$ we may replace the function $x\mapsto x^{-k}$ by the function $x\mapsto a^{-k}$ if $x\equiv a
\pmod{p}$, which is congruent to it modulo $p$ on $\mathbb{Z}_p^\times$. This implies that $\operatorname{Li}^{(p)}_n(z)$ is congruent modulo $p$ to $$\sum_{a=1}^{p-1} a^{-n} \mu_z(a+p\mathbb{Z}_p)=
  \sum_{a=1}^{p-1} a^{-n} \frac{z^a}{1-z^p}\;.$$ ◻
:::

::: corollary
[]{#reduction label="reduction"} Let $\alpha\in X$ be a root of unity. Then we have $\operatorname{Li}_n(\alpha)\in p^n W$ and $p^{-n} \operatorname{Li}_n(\alpha) \equiv
  -\operatorname{li}_n(\sigma(\alpha))/(1-\alpha) \pmod{p}$.
:::

::: proof
*Proof.* Since $\alpha\in X\subset W$ the order of $\alpha$ is prime to $p$ and we have $\alpha^{p^k}=\alpha$ for some $k$. By using the definition of $\operatorname{Li}^{(p)}_n$ repeatedly we find $$\begin{aligned}
  \operatorname{Li}_n(\alpha)&=\operatorname{Li}^{(p)}_n(\alpha)+p^{-n} \operatorname{Li}_n(\alpha^p)\\
               &=\operatorname{Li}^{(p)}_n(\alpha)+p^{-n}
               \operatorname{Li}^{(p)}_n(\alpha^p)+p^{-2n} \operatorname{Li}_n(\alpha^{p^2})\\
        \cdots &=\sum_{i=0}^{k-1} p^{-in}\operatorname{Li}^{(p)}_n(\alpha^{p^i})
                  + p^{-kn} \operatorname{Li}_n(\alpha^{p^k})\;.
\end{aligned}$$ Since $\alpha^{p^k}=\alpha$ we may move the last term to the left hand side of the equation and obtain $$\begin{aligned}
  \operatorname{Li}_n(\alpha)&= \frac{1}{1-p^{-kn}}\sum_{i=0}^{k-1}
                  p^{-in}\operatorname{Li}^{(p)}_n(\alpha^{p^i})\\
               &= \frac{p^n}{p^{kn}-1}\sum_{i=0}^{k-1}
  p^{(k-1-i)n}\operatorname{Li}^{(p)}_n(\alpha^{p^i})\in p^n W \;,
\end{aligned}$$ and dividing by $p^n$ and reducing modulo $p$ we obtain using the proposition $$- \operatorname{Li}^{(p)}_n(\alpha^{p^{k-1}}) \equiv (1-(\alpha^{p^{k-1}})^p)^{-1}
  \operatorname{li}_n(\alpha^{p^{k-1}}) \equiv -\operatorname{li}_n(\sigma(\alpha))/(1-\alpha)
  \pmod{p}\;.$$ ◻
:::

::: proposition
[]{#maincong label="maincong"} Let $\alpha$ be a root of unity in $X$. Set $\widetilde{\operatorname{Li}}_n(\alpha)= p^{-n} \operatorname{Li}_n(\alpha)$. Then for $w\in W$ we have $$p^{-n} \operatorname{Li}_n(\alpha(1+pw))\equiv \sum_{k=0}^n
    \widetilde{\operatorname{Li}}_{n-k}(\alpha)\frac{w^k}{k!}\pmod{p}\;.$$
:::

::: proof
*Proof.* Let $g_n(w)=p^{-n} \operatorname{Li}_n(\alpha(1+pw))$. Then one finds $$g_0(w)=\frac{\alpha(1+pw)}{1-\alpha(1+pw)}=
  \frac{\alpha}{1-\alpha}\frac{1+pw} {1-\frac{\alpha}{1-\alpha}pw}
  =\widetilde{\operatorname{Li}}_0(\alpha)+\sum_{k=1}^\infty b_k (pw)^k$$ with $b_n \in W$. Write $$g_n(w)= \widetilde{\operatorname{Li}}_n(\alpha)+\sum_{k=1}^\infty d_k^n w^k\;.$$ It is easy to verify that $$\frac{d}{dw} g_n(w)= g_{n-1}(w)\frac{1}{1+pw}=
  g_{n-1}(w)(1+\sum_{k=1}^\infty c_k (pw)^k)\; ,$$ with $c_k \in W$. To find the coefficients $d_k^n$ modulo $p$ for $k<p$ one can simply reduce the above equations modulo $p$ and one easily finds that $$d_k^n \equiv
  \begin{cases}
    \frac{\widetilde{\operatorname{Li}}_{n-k}(\alpha)}{k!} &\text{ when } k\le n \\
        0 & \text{ when } n<k<p\;.
  \end{cases}$$ It thus remains to show that also for $k\ge p$ the coefficient $d_k^n$ is divisible by $p$. For this it is easier to consider the function $f_n(u)=\operatorname{Li}_n(\alpha+u)$ which satisfies $f_0(u)\in W[[u]]$, $d/du
f_{n+1}(u) = g(u)f_n(u)$ with $g(u)\in W[[u]]$ and $f_n(0)\in
W$.

::: lemma
In the situation above we have $v_p(a_k) \ge -v_p(k!)$, where $v_p$ is the $p$-adic valuation and $a_k$ is the $k$-th coefficient in the power series expansion with respect to $u$ of any of the functions $f_n$.
:::

::: proof
*Proof.* Let $a_k(h)$ be the $k$-th coefficient of $h$ for any power series $h$. We have $$v_p(a_k(f_n g)) \ge \min_{l\le k}[ v_p(a_l(f_n))]\;.$$ This implies that $$v_p(a_k(f_{n+1})) \ge \min_{l< k} [v_p(a_l(f_n))] -v_p(k)\;.$$

The lemma is clearly true for $n=0$. Suppose it is true for $n$. Then $$v_p(a_k(f_{n+1})) \ge \min_{l\le k} [-v_p(l!)] -v_p(k) \ge -v_p((k-1)!)
  -v_p(k)= -v_p(k!)\;.$$ ◻
:::

Since $g_n(w) = p^{-n} f_n(\alpha pw)$, to finish the proof we have to check that for every $k\ge p$ we have $k-n-v_p(k!) >0$. The well known estimate $v_p(k!)\le k/(p-1)$ and the assumption $n<p$ imply that it is sufficient to require $k(1-1/(p-1))\ge p$, and this is satisfied for $k\ge p+1$. The case $k=p$ is also OK according to this analysis unless $n=p-1$. ◻
:::

::: proof
*Proof of Theorem [\[thetheorem\]](#thetheorem){reference-type="ref" reference="thetheorem"}.* Using the fact that $D$ is a derivation and that $$D \log^k(z) = z(1-z) \frac{d}{dz} \log^k(z)=z(1-z) k
  \log^{k-1}(z)\frac{1}{z} = (1-z) k \log^{k-1}(z)$$ and $$D \operatorname{Li}_k(z) = z(1-z) \frac{d}{dz} \operatorname{Li}_k(z) = z(1-z) \operatorname{Li}_{k-1}(z)
  \frac{1}{z} = (1-z) \operatorname{Li}_{k-1}(z)$$ we see that $$\begin{aligned}
  DF_n(z)&=D \sum_{k=0}^{n-1} a_k \log^k(z) \operatorname{Li}_{n-k}(z)\\&=
  (1-z) \sum_{k=0}^{n-1} a_k(k \log^{k-1}(z) \operatorname{Li}_{n-k}(z) + \log^k(z)
  \operatorname{Li}_{n-k-1}(z)) \\&=
  (1-z) \sum_{k=0}^{n-1} \log^k(z) \operatorname{Li}_{n-k-1}(z) (a_k + (k+1) a_{k+1})\;.
\end{aligned}$$ Here we understand that $a_n=0$. Every $z\in X$ can be written as $\alpha (1+pw)$ with $\alpha$ a root of unity in $X$ and $w\in W$. We have $$p^{-1} \log(\alpha(1+pw)) = p^{-1} \log(1+pw) \equiv w \pmod{p}\;.$$ If we assume that $a_k\in Z[1/(n+1)!]$ we now find from the last computation and from proposition [\[maincong\]](#maincong){reference-type="ref" reference="maincong"}, $$\begin{aligned}
  p^{1-n} &DF_n(\alpha(1+pw))\\ &\equiv 
  (1-\alpha) \sum_{k=0}^{n-1} w^k(a_k+ (k+1)
  a_{k+1})\sum_{m=0}^{n-k-1} \frac{1}{m!} \widetilde{\operatorname{Li}}_{n-k-1-m}(\alpha) w^m \\
  &\equiv
  (1-\alpha) \sum_{l=0}^{n-1} w^l \sum_{k=0}^l (a_k + (k+1) a_{k+1})
  \frac{1}{(l-k)!} \widetilde{\operatorname{Li}}_{n-l-1}(\alpha)\;.
\end{aligned}$$ It follows that to make the reduction of $p^{1-n} DF_n$ independent of $w$ for all $p>n+1$ it is necessary and sufficient that for $l=1,\ldots,n-1$ we have $$\label{conds}
  \sum_{k=0}^l (a_k + (k+1) a_{k+1})
  \frac{1}{(l-k)!} =0\;.$$ If this is satisfied then the reduction of $p^{1-n} DF_n(\alpha(1+pw))$ is $(a_0+a_1) (1-\alpha) \widetilde{\operatorname{Li}}_{n-1}(\alpha)\equiv -(a_0+a_1)
\operatorname{li}_{n-1}(\sigma(\alpha))$ so we should also require $a_0+a_1=-1$.

Let $A(t) = \sum_{k=0}^{n-1} a_k t^k$. Then the relations [\[conds\]](#conds){reference-type="eqref" reference="conds"} can be written as $e^t (A(t) + dA(t)/dt) \equiv a \pmod{t^n}$ where $a$ is a constant. This implies that $A(t)+dA(t)/dt \equiv ae^{-t} \pmod{t^n}$ and after solving the resulting differential equation that the $n-2$ first equations in [\[conds\]](#conds){reference-type="eqref" reference="conds"} are equivalent to $A(t) \equiv (at+b) e^{-t} \pmod{t^{n-1}}$ for some other constant $b$. We have $-1=a_0+a_1=b+(a-b)=a$. Now, in $(b-t)e^{-t}$ the coefficient of $t^n$ is $$b \frac{(-1)^{n}}{n!} -\frac{(-1)^{n-1}}{(n-1)!} =
  \frac{(-1)^{n-1}}{(n-1)!}(1-b/n)\;.$$ It is easy to see that for the equation [\[conds\]](#conds){reference-type="eqref" reference="conds"} with $l=n-1$ to be satisfied, this coefficient must be $0$ and hence $b=n$. This gives the choice of the coefficients in the theorem and shows that they are the unique choice in $\mathbb{Z}[1/(n+1)!]$. Now if we have coefficients in $\mathbb{Q}$ satisfying the theorem, then we may clear denominators not dividing $(n+1)!$ and using only independence of $w$ we obtain that these must be a rational multiple of our $a_k$. But since the reduction of $p^{1-n} DF_n$ is non-trivial the multiplier must be $1$. ◻
:::

::: remark
We have the equation $F_n(z) =-n L_n(z) - L_{n-1}(z) \log(z)$, where $$L_n(z)= \sum_{m=0}^{n-1}\frac{(-1)^m}{m!}\operatorname{Li}_{n-m}(z) \log^m(z)$$ is the function defined in [@Bes-deJ98]. By loc. cit. the function $F_n$ satisfies $F_n(z) + (-1)^n
F_n(1/z)=0$. Differentiating this relation one gets the relation $z DF_n(1/z)+ (-1)^n DF_n(z)=0$. Reducing modulo $p$ we find $z \operatorname{li}_{n-1}(1/z) + (-1)^n \operatorname{li}_{n-1}(z) = 0$. This relation is easily verified directly.
:::
