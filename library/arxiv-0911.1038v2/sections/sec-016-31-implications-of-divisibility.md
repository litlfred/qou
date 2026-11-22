---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-016-31-implications-of-divisibility
section_title: "Implications of divisibility"
section_number: 3.1
pages: 12-16
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.864
latex_coverage_ratio: 0.971
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
At this step we proved Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"}. In order to prove Theorem [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"} we would like to show that for each integer $g
\geq 1$, functions $\tilde{f}_g$ and $\tilde{h}_g$ are divisible by the symmetric function $$(p_1 + 2g -1)\frac{(p_1 + 2g)(p_1 + 2g -1)(p_1 + 2g
-2)}{3!},$$ where $p_1$ denotes the power symmetric function. By word divisible we mean that there exist symmetric functions $f_g$ and $h_\mu$ such that $$\tilde{f}_g = (p_1 + 2g -1)\frac{(p_1 + 2g)(p_1 + 2g -1)(p_1 + 2g
-2)}{3!}f_g$$ and $$\tilde{h}_g = (p_1 + 2g -1)\frac{(p_1 + 2g)(p_1 + 2g -1)(p_1 + 2g
-2)}{3!}h_g.$$ Observe that for fixed $g \geq 1$ and for any partition $\mu$ there exists number $k$ such that $|\mu| = k + 1 - 2g$ and then $$\tilde{f}_g(\mu) = k \binom{k+1}{3}f_g(\mu),$$ $$\tilde{h}_g(\mu) = k \binom{k+1}{3}h_g(\mu)(\mu).$$ The idea of showing divisibility of symmetric function by symmetric function of degree $1$ is similar to the case of showing divisibility of some polynomial by some monomial. The main idea is dividing with a remainder and using a fact that if some integer is divisible by infinite number of primes then it has to be equal to zero. The remainning of this section is a formalisation of this idea.

The first difficulty is that we have to deal with polynomials in several variables. Hence, in order to show some generalisation of the "dividing with remainder" technique, we need the following technical lemma:

::: lemma
[]{#lem:zerozero label="lem:zerozero"} Let $m$ be a fixed integer and $f$ be a polynomial in variables $x_k,\dots,x_l$ with the property that $f(\mu_k,\dots,\mu_l)=0$ for all integers $\mu_k,\dots,\mu_l\geq 1$ which fulfill the following equations: $$\label{eq:suma}
\sum_{k \leq j \leq l}\mu_j > m,$$ $$\label{eq:wzrost}
\mu_i>\mu_{i+1}+\cdots+\mu_l$$ for all values of $i$ for which it makes sense. Then $f=0$.
:::

The proof of this lemma can be found in Section [\[sec:technical\]](#sec:technical){reference-type="ref" reference="sec:technical"}.

The next lemma is key for this section: it allows to translate information about arithmetic properties of Kerov polynomials into information about the polynomials governing the coefficients.

::: lemma
[]{#lem:sie-dzieli label="lem:sie-dzieli"} Let $f$, respectively $h$, be a symmetric function of degree at most $d$ with rational coefficients, $g\geq 1$ be an integer; we define

$$\begin{aligned}
 L_{k} =  & \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)!\ f(\mu)\ \mathcal{R}_\mu, \\
\intertext{respectively,}
L'_{k}&= \sum_{|\mu|=k+1-2g} \big(2g - 1\big)^{l(\mu)}\ h(\mu)\ \mathcal{Q}_\mu
\end{aligned}$$ and view it as a polynomial in $R_2,R_3,\dots$.

Assume that an integer $\Delta$ has a property that all coefficients of $L_{p+\Delta}$ (respectively, all coefficients of $L'_{p+\Delta}$) are integers divisible by $p$ for an infinite number of prime numbers $p$. Then there exists a symmetric function $\tilde{f}$ (respectively, $\tilde{h}$) with rational coefficients of degree at most $d-1$ such that $$\begin{aligned}
 L_{k} &= (k-\Delta) \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)!\ \tilde{f}(\mu)\ \mathcal{R}_\mu, \\
\intertext{respectively,} 
L'_k&= (k-\Delta) \sum_{|\mu|=k+1-2g}
\big(2g - 1\big)^{l(\mu)}\ \tilde{h}(\mu)\ \mathcal{Q}_\mu.
\end{aligned}$$
:::

::: proof
*Proof.* For simplicity assume that the coefficients of $f$ (respectively, $h$) are integer numbers; if this is not the case we multiply $L_{k}$ and $f$ (respectively, $L'_k$ and $h$) by some common multiple of the denominators.

Let $\mu=(\mu_1,\mu_2,\dots)$ be a sequence of indeterminates. We use the notation $|\mu|=\mu_1+\mu_2+\cdots$ and define variable $z=|\mu|+2g-1-\Delta$. The family of indeterminates $\mu$ can be alternatively parametrized by $z,\mu_2,\mu_3,\dots$; we just use the substitution $\mu_1=z+\Delta+1-2g-\mu_2-\mu_3-\cdots$. Now we can consider $f,h \in
\Lambda[z]$ as polynomials in one variable $z$ with coefficients in the ring $\Lambda$ of symmetric functions in variables $\mu_2,\mu_3,\dots$ and we can divide $f$ and $h$ by $z$ with a remainder. Hence $$\begin{aligned}
 f(\mu)&= (|\mu|+2g-1-\Delta) \tilde{f}(\mu) +
r(\mu_2,\mu_3,\dots), \\ 
h(\mu)&= (|\mu|+2g-1-\Delta) \tilde{h}(\mu) +
s(\mu_2,\mu_3,\dots)  
\end{aligned}$$ for some $\tilde{f}, \tilde{h} \in \Lambda[z]$ and for some $r, s \in \Lambda$. Below we will show that $r=s=0$. This would imply that $$\begin{aligned}
 f(\mu)&= (|\mu|+2g-1-\Delta) \tilde{f}(\mu), \\
h(\mu)&= (|\mu|+2g-1-\Delta) \tilde{h}(\mu),
\end{aligned}$$ where by substitution $z=|\mu|+2g-1-\Delta$ we view $\tilde{f},\tilde{h}\in
\Lambda[\mu_1]$ as polynomials in one variable $\mu_1$ with coefficients in $\Lambda$. For any permutation $\pi$ of the set of positive integers which moves only finitely many elements we have $$\begin{gathered}
 (|\mu|+2g-1-\Delta) \tilde{f}(\mu_1,\mu_2,\dots) =
f(\mu_1,\mu_2,\dots) =\\ f(\mu_{\pi(1)},\mu_{\pi(2)},\dots) =
(|\mu|+2g-1-\Delta) \tilde{f}(\mu_{\pi(1)},\mu_{\pi(2)},\dots)
\end{gathered}$$ hence from the cancellation property $$\tilde{f}(\mu_1,\mu_2,\dots) = \tilde{f}(\mu_{\pi(1)},\mu_{\pi(2)},\dots)$$ is a symmetric function. In an analogous way we show that $\tilde{h}$ is a symmetric function. The lemma follows now immediately.

It remains now to show that $r=s=0$. From the following on let $\mu_2> \cdots >
\mu_l$ be fixed integers bigger than $1$ which fulfill Equations [\[eq:wzrost\]](#eq:wzrost){reference-type="eqref" reference="eq:wzrost"} and [\[eq:suma\]](#eq:suma){reference-type="eqref" reference="eq:suma"} with $m =
\Delta - 2g$.

Define $\mu_1=p+\Delta+1-2g-\mu_2-\mu_3-\cdots-\mu_l$, where $p$ is a prime number. Notice that $\mu_1 - 1 < p$, because we required that $\Delta+1-2g-\mu_2-\mu_3-\cdots-\mu_l < 1$. We consider the integral vector $\mu=(\mu_1,\dots,\mu_l)$.

If $p$ is large enough, the parts of $\mu$ are all distinct and it follows that $$[R_{\mu_1} R_{\mu_2} \cdots R_{\mu_l}] L_{p+\Delta} =   (l+2g-2)!\ f(\mu)\
(\mu_1-1)(\mu_2-1)\cdots(\mu_l-1).$$ Also, if prime number $p$ is big enough then it does not divide $(l+2g-2)!\ (\mu_1-1)(\mu_2-1)\cdots(\mu_l-1)$. It follows that for infinitely many prime numbers $p$ the number $$f(\mu)=  p \tilde{f}(\mu) + r(\mu_2, \dots, \mu_l)$$ is divisible by $p$. We proved in this way that $r(\mu_2, \dots, \mu_l,
0,
\dots)$ is an integer which is divisible by an infinite number of primes hence $r(\mu_2, \dots, \mu_l, 0, \dots)=0$. Finaly Lemma [\[lem:zerozero\]](#lem:zerozero){reference-type="ref" reference="lem:zerozero"} shows that $r=0$.

If $p$ is big enough then condition [\[eq:wzrost\]](#eq:wzrost){reference-type="eqref" reference="eq:wzrost"} holds true for all $1\leq i \leq l-1$ therefore every partition resulting from $\mu$ by gluing together some of its parts cannot be obtained by gluing the parts of $\mu$ in some other way (in fact, this property is the main reason of introducing Equation [\[eq:wzrost\]](#eq:wzrost){reference-type="eqref" reference="eq:wzrost"}). From [\[eq:qi\]](#eq:qi){reference-type="eqref" reference="eq:qi"} it follows that $$[R_{\mu_1} R_{\mu_2} \cdots] L'_{p+\Delta} = 
\sum_{\nu\geq\mu}(2g-1)^{l(\nu)}\big(l(\nu)-1\big)!\ h(\nu),$$ where $\nu\geq\mu$ means that partition $\nu$ can be obtained from partition $\mu$ by gluing some parts of $\mu$.

We also know that for infinitely many prime numbers $p$ the following number $$\begin{gathered}
\sum_{\nu\geq\mu}(2g-1)^{l(\nu)}\big(l(\nu)-1\big)!\ h(\nu) = \\
p\left[ \sum_{\nu\geq\mu}(2g-1)^{l(\nu)}\big(l(\nu)-1\big)!\
\tilde{h}(\nu)\right] 
+ \sum_{\nu\geq\mu}(2g-1)^{l(\nu)}\big(l(\nu)-1\big)!\ s(\nu')
\end{gathered}$$ is divisible by $p$, where for $\nu
= (\nu_1,\nu_2,\dots)$ we denote $\nu' = (\nu_2,\nu_3,\dots)$. Notice that the set of values of $\nu'$ which contribute to the right hand side does not depend on the choice of $p$, because only $\nu_1$ depends on the choice of $p$. Thus we proved that for infinitely many prime numbers $p$ the second summand on the right hand side does not depend on the choice of $p$ and is a fixed integer divisible by all these prime numbers, hence $$\label{eq:upper-trangular}
 \sum_{\nu\geq\mu}(2g-1)^{l(\nu)}\big(l(\nu)-1\big)!\ s(\nu') = 0.$$

We will use induction over $k$ to show that $s(x_2,\dots,x_k,0,\dots)$ is equal to the zero polynomial for any $k > 1$, which proves that $s=0$. Indeed, assume, that $s(x_2,\dots,x_k,0,\dots)$ is equal to the zero polynomial for $k < l$. From the induction hypothesis it follows that all summands on the left-hand side of [\[eq:upper-trangular\]](#eq:upper-trangular){reference-type="eqref" reference="eq:upper-trangular"} vanish, except for $\nu=\mu$, which shows that $s(\mu')=0$. We use Lemma [\[lem:zerozero\]](#lem:zerozero){reference-type="ref" reference="lem:zerozero"} to show that $s=0$ as claimed. ◻
:::
