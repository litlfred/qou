---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-008-4-markov-traces-on-the-hecke-algebra-of-type-b
section_title: "Markov Traces on the Hecke Algebra of type $B$"
section_number: 4
pages: 14-16
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.977
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempotents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
In this section we give the necessary background on Markov traces. We refer the reader to [@gl] or [@g] for the details. A *trace* function on $H_{\infty}(q,Q)$ is a $\mathbb{C}(q,Q)$-linear map $\phi:H_{\infty}(q,Q)\longrightarrow \mathbb{C}(q,Q)$ such that $\phi (hh')=\phi (h'h)$ for all $h,h' \in H_{\infty}(q,Q)$. This definition is in fact valid for any associative algebra over a commutative ground ring. In the case of the group algebra it is clear that every trace function is constant on the conjugacy classes of the underlying group. Notice that $\phi(hh')-\phi(h'h)=0$; this means that $\phi(hh'-h'h)=\phi([h,h'])=0$, which implies that the commutators are in the kernel of a trace function in an algebra. The weights we are going to give in this paper correspond to a trace that satisfies the following definition. **Definition: ** Let $z\in \mathbb{C}(q,Q)$ and $tr : H_{\infty}(q,Q) \longrightarrow \mathbb{C}(q,Q)$ be an $\mathbb{C}(q,Q)$-linear map. Then $tr$ is called a *Markov trace* (with parameter $z$) if the following conditions are satisfied: (1) $tr$ is a trace function on $H_{\infty}(q,Q)$; (2) $tr(1)=1$ (normalization); (3) $tr(hg_n)= ztr(h)$ for all $n \geq 1$ and $h \in H_n(q,Q)$. .05in The name of these traces comes from their invariance under the Markov moves for closed braids. Remember that the Hecke Algebra is a quotient of the braid group. We note that all generators $g_i$ (for $i = 1,2, \ldots$) are conjugate in $H_{\infty}(q,Q)$. In particular, any trace function on $H_{\infty}(q,Q)$ must have the same value on these elements. This explains why the parameter $z$ is independent of $n$ in rule (3) of this definition. Geck and Pfeiffer in [@gp] showed that a trace function on the Hecke algebra is uniquely determined by its value on basis elements corresponding to representatives of minimal length in the various conjugacy classes of the underlying Coxeter group. Also representatives of minimal length in the classes of Coxeter groups of classical types are of the form $d_1 \ldots d_n$, where $d_i$ is a distinguished double coset representative of the $H_i(q,Q)$ with respect to $H_{i-1}(q,Q)$. Let $tr$ be a Markov trace with parameter $z$, and let $d_i\in \mathcal{D}_i$ for $i=1,\ldots,n$. Then $$tr(d_1\ldots d_n)=z^a tr(t'_0t'_1\ldots t'_{b-1})$$ where $a$ is the number of factors $d'_i$ which are equal to $g_{i-1}$ and $b$ is the number of factors which are equal to $t'_{i-1}$. Thus, $tr$ is uniquely determined by its parameter $z$ and the values on the elements in the set $\{t'_0t'_1\ldots t'_{i-1}\,|\,i=1,2,\ldots\}$. Conversely, given $z,\, y_1, \, y_2, \ldots \in \mathbb{C}(q,Q)$ then there exist a unique Markov trace on $H_{\infty}(q,Q)$ such that $tr(t'_0t'_1\ldots t'_{k-1})=y_k$ for all $k\geq 1$. For details on these results see [@gl], Theorem 4.3. We are particularly interested in the special case when $y_i=y^i$ for all $i\in \mathbb{N}$, this is the case when there is only two parameters. In this case, we have that if $d_i$ is a distinguished double coset representative then $tr(d_ix)=\xi tr(x)$ where $\xi=y$ or $z$. The proof of the following proposition is found in [@gl].

::: proposition
Let $z, y \in \mathbb{C}(q,Q)$ and $tr: H_{\infty}(q,Q) \longrightarrow \mathbb{C}(q,Q)$ be a Markov trace with parameter $z$ such that $tr(t^{'}_0t^{'}_1 \ldots t^{'}_{k-1}) =y^{k}$ for all $k \geq 1$ then

$tr(ht^{'}_{n,0})= ytr(h)$ for all $n \geq 0$ and $h\in H_n(q,Q)$

where $t'_{n,0}=g_n\ldots g_1tg_1^{-1}\ldots g_n^{-1}$ or $g_n^{-1}\ldots g_1^{-1}tg_1\ldots g_n$.
:::

We point out that the converse is also true. A proof of the existence of such traces for every $z\in \mathbb{C}$ is given in [@gl]. We will compute the weight vectors for this Markov trace on $H_n(q,Q)$.
