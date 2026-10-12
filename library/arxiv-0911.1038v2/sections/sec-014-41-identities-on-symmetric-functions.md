---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-014-41-identities-on-symmetric-functions
section_title: "Identities on symmetric functions"
section_number: 4.1
pages: 18-21
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.882
---
::: lemma
[]{#lem:technical1 label="lem:technical1"} The following abstract equalities hold: $$\label{sym:R'}
 \sum_{\mu \cup \rho = \nu} m_{\lambda}(\mu) \frac{(l(\mu) + 2g -2)!}{l(\mu)!}
u_{\mu} u_{\rho} = \frac{m_{\lambda}(\nu)}{l(\lambda) + 2g -1} \frac{(l(\nu) +
2g - 2)!}{l(\nu)!} u_{\nu};$$ $$\label{sym:Q'}
 \sum_{\mu \cup \rho = \nu} m_{\lambda}(\mu) (2g -1)^{l(\mu)}
z^{-1}_{\mu} z^{-1}_{\rho} = \left(\frac{2g-1}{2g}\right)^{l(\lambda)}
m_{\lambda}(\nu)(2g)^{l(\nu)} z^{-1}_{\nu}.$$
:::

::: proof
*Proof.* From the definition of the monomial symmetric function we know that $m_{\lambda}(\mu) = 0$ for all partitions $\mu$ such that $l(\mu) < l(\lambda)$. We use an identity that for every integer $n$ such that $l(\lambda)
\leq n \leq l(\nu)$ we have $$\label{sym:mon}
\binom{l(\nu) - l(\lambda)}{n - l(\lambda)} m_{\lambda}(\nu) = 
\sum_{\substack{\mu \cup
\rho = \nu, \\ l(\mu) = n}} m_{\lambda}(\mu)
\left( \prod_{i \geq 1} \frac{m_i(\nu)!}{m_i(\mu)!\ m_i(\rho)!}\right).$$ Indeed, $$\begin{gathered}
\sum_{\substack{\mu \cup
\rho = \nu, \\ l(\mu) = n}} m_{\lambda}(\mu)
\left( \prod_{i \geq 1} \frac{m_i(\nu)!}{m_i(\mu)!\ m_i(\rho)!}\right) =
\sum_{\substack{\mu \subset \nu, \\ l(\mu) = n}} m_{\lambda}(\mu) = \\
\sum_{\substack{\mu' \subset \mu \subset \nu, \\ l(\mu) = n, l(\mu') = 
l(\lambda)}} m_{\lambda}(\mu') = 
\sum_{\substack{\mu' \subset \nu, \\ l(\mu') = l(\lambda)}} \sum_{\substack{\mu'
\subset \mu \subset \nu, \\ l(\mu) = n}} m_{\lambda}(\mu') = \\
\binom{l(\nu) -
l(\lambda)}{n - l(\lambda)} \sum_{\substack{\mu' \subset \nu, \\ l(\mu') =
l(\lambda)}} m_{\lambda}(\mu') = \binom{l(\nu) - l(\lambda)}{n - l(\lambda)}
m_{\lambda}(\nu),
\end{gathered}$$ where $\sum_{\substack{\mu \subset \nu, \\ l(\mu) = n}}$ means that $\mu =
(\nu_{\sigma(1)}, \dots, \nu_{\sigma(n)})$ for some $\sigma \in \mathfrak{S}(l(\nu))$ such that $\sigma(i) < \sigma(i+1)$ for all $i \in
\{1,\dots,n-1\}$ and we are summing over all such permutations $\sigma$. Now, we can write the left hand side of [\[sym:R\'\]](#sym:R'){reference-type="eqref" reference="sym:R'"} in the following way: $$\begin{gathered}
 \sum_{l(\lambda) \leq n \leq l(\nu)} \frac{(n + 2g -2)!}{n!}
\Bigg( \sum_{\substack{\mu \cup
\rho = \nu,\\ l(\mu) = n}} m_{\lambda}(\mu) \prod_{i \geq 1}
\frac{m_i(\nu)!}{m_i(\mu)\
!m_i(\rho)!}\Bigg) \times \\ \shoveright{u_{\nu} \frac{n!\ (l(\nu) -
n)!}{l(\nu)!} =} 
\\ 
\shoveleft{ \sum_{l(\lambda) \leq n \leq l(\nu)} \frac{(n + 2g -2)!}{n!}
\frac{(l(\nu) - l(\lambda))!}{(l(\nu) - n)!(n - l(\lambda))!}
m_{\lambda}(\nu) \times }
\\ 
\shoveright{ u_{\nu} \frac{n!\ (l(\nu) -
n)!}{l(\nu)!} = }\\ \frac{(l(\nu) - l(\lambda))!}{l(\nu)!} \sum_{l(\lambda) \leq
n
\leq l(\nu)}
\frac{(n + 2g -2)!}{(n - l(\lambda))!} m_{\lambda}(\nu) u_{\nu}
\end{gathered}$$ and using the equality $$\sum_{0 \leq i \leq b} \binom{a+i}{i} = \binom{a+b+1}{b}$$ we have $$\begin{gathered}
\frac{(l(\nu) - l(\lambda))!}{l(\nu)!} \sum_{l(\lambda) \leq n \leq l(\nu)}
\frac{(n + 2g -2)!}{(n - l(\lambda))!} = \\ 
\frac{(l(\nu) -
l(\lambda))!(l(\lambda) + 2g -2)!}{l(\nu)!} \sum_{0 \leq n \leq l(\nu) -
l(\lambda)}
\frac{(n + l(\lambda) + 2g -2)!}{n!(l(\lambda) + 2g -2)!} = \\
\frac{(l(\nu) -
l(\lambda))!(l(\lambda) + 2g -2)!}{l(\nu)!} \sum_{0 \leq n \leq l(\nu) -
l(\lambda)} \binom{l(\lambda) + 2g -2 + n}{n} = \\
\frac{(l(\nu) -
l(\lambda))!\ (l(\lambda) + 2g -2)!\ (l(\nu) + 2g -1)!}{l(\nu)!\ (l(\nu) -
l(\lambda))!\ (l(\lambda) + 2g -1)!} = \frac{(l(\nu) + 2g
-1)!}{l(\nu)!(l(\lambda) + 2g -1)}
\end{gathered}$$ which finishes the proof of [\[sym:R\'\]](#sym:R'){reference-type="eqref" reference="sym:R'"}.

Using [\[sym:mon\]](#sym:mon){reference-type="eqref" reference="sym:mon"} we can write the left hand side of [\[sym:Q\'\]](#sym:Q'){reference-type="eqref" reference="sym:Q'"} in the following form: $$\begin{gathered}
 \sum_{l(\lambda) \leq n \leq l(\nu)} (2g -1)^{n}
\Bigg( \sum_{\substack{\mu \cup
\rho = \nu, \\l(\mu) = n}} m_{\lambda}(\mu) \prod_{i \geq 1}
\frac{m_i(\nu)!}{m_i(\mu)\ !m_i(\rho)!}\Bigg) z^{-1}_{\nu} = \\
\Bigg(\sum_{l(\lambda) \leq n \leq l(\nu)} (2g -1)^{n} \binom{l(\nu) -
l(\lambda)}{n - l(\lambda)}\Bigg) m_{\lambda}(\nu) z^{-1}_{\nu} = \\
(2g - 1)^{l(\lambda)} \Bigg(\sum_{0 \leq n \leq l(\nu) - l(\lambda)}
\binom{l(\nu) - l(\lambda)}{n}(2g -1)^n \Bigg) m_{\lambda}(\nu) z^{-1}_{\nu} =
\\
\left(\frac{2g-1}{2g}\right)^{l(\lambda)}
m_{\lambda}(\nu)(2g)^{l(\nu)} z^{-1}_{\nu},
\end{gathered}$$ where the last equality holds because of the binomial identity: $$\sum_{0 \leq n \leq m}\binom{m}{n}a^n = (a + 1)^m,$$ which finishes the proof. ◻
:::

## Proof of Lemma [\[lem:zerozero\]](#lem:zerozero){reference-type="ref" reference="lem:zerozero"}

::: proof
*Proof of Lemma [\[lem:zerozero\]](#lem:zerozero){reference-type="ref" reference="lem:zerozero"}.* Let $l$ be fixed; we will use backward induction over $k$. For $k=l$ we know that $f(\mu_k)=0$ for infinitely many choices of $\mu_k$. In other words, polynomial $f$ has infinitely many zeros hence $f=0$, as claimed.

Let us assume that the inductive assertion holds for some $k\leq l$. We can write $$f(x_{k-1}, \dots, x_{l})
= \sum_{0 \leq i \leq N} x_{k-1}^{i}\ f_i(x_k, \dots, x_{l})$$ for some $N$. Let us fix integers $\mu_{k}, \dots, \mu_{l}$ bigger than $1$ which satisfy [\[eq:wzrost\]](#eq:wzrost){reference-type="eqref" reference="eq:wzrost"} and [\[eq:suma\]](#eq:suma){reference-type="eqref" reference="eq:suma"}. Then we can find infinitely many integer numbers $\mu_{k-1}$ for which the vector $(\mu_{k-1},\dots,\mu_{l})$ satisfies both [\[eq:wzrost\]](#eq:wzrost){reference-type="eqref" reference="eq:wzrost"} and [\[eq:suma\]](#eq:suma){reference-type="eqref" reference="eq:suma"}; for each such a number we have $f(\mu_{k-1}, \dots, \mu_{l}) = 0$ therefore the polynomial $x_{k-1}\mapsto
f(x_{k-1},\mu_{k},\dots,\mu_{l})$ has infinitely many zeros hence it is the zero polynomial and $f_i(\mu_{k}, \dots, \mu_{l})=0$. This shows that the inductive assertion can be applied to the polynomial $f_i(x_{k},\dots,x_{l})$ and therefore $f_i(x_{k},\dots,x_{l})=0$. This finishes the proof. ◻
:::
