---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-004-2-hecke-algebra-of-type-b-n
section_title: "Hecke Algebra of type $B_n$"
section_number: 2
pages: 7-9
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.944
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempotents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
In this context, we will mean by the Hecke algebra $H_n(q,Q)$ of type $B_n$ the free complex algebra with 1 and generators $t, g_1, g_2, \ldots, g_{n-1}$ and parameters $q,Q \in \mathbb{C}$ with defining relations

1.     $g_{i}g_{i+1}g_{i}=g_{i+1}g_{i}g_{i+1}$    for $i=1,2, \ldots, n-2$;

2.     $g_{i}g_{j}= g_{j}g_{i}$,    whenever $\mid i-j \mid \geq 2$;

3.     $g_i^2 = (q-1)g_i +q$     for $i=1,2, \ldots, n-1$;

4.     $t^2 = (Q-1)t +Q$;

5.     $tg_1tg_1=g_1tg_1t$;

6.     $tg_i=g_it$      for $i \geq 2$.

Note that for $q=1$ and $Q=1$, (H3) and (H4) become $g_i^2=1$ and $t^2=1$, respectively. In this case the generators satisfy exactly the same relations as a set of simple reflections of the hyperoctahedral group, $\mathcal{H}_n$. It is known that $H_n(q,Q)\cong \mathbb{C}\mathcal{H}_n$ (the group algebra of $\mathcal{H}_n$) if $q$ is not a root of unity and $Q\neq -q^s$ for $-n<s<n$. $\mathbb{C}\mathcal{H}_n$ is semisimple since it is a finite complex group algebra. This implies that $H_n(q,Q)$ is semisimple for generic values of $q$ and $Q$. Furthermore the simple modules are in 1-1 correspondence with double partitions. Their decomposition rule and their dimensions are the same as for $\mathcal{H}_n$. \[See Bourbarki, Groups et algebres de Lie IV, V, VI\] Hoefsmit, in [@h], has written down explicit irreducible representations of $H_n(q,Q)$ for each pair of Young diagrams. This demonstrates that dimension over $\mathbb{C}(q,Q)$ of $H_n(q,Q)$ is $2^nn!$. Let $V_{(\alpha,\beta)}$ be an $H_n(q,Q)$ module then we have the following restriction rule: $$V_{(\alpha,\beta)}{\Big|}_{H_{n-1}(q,Q)}\cong \bigoplus_{(\alpha,\beta)'\subset(\alpha,\beta)}V_{(\alpha,\beta)'},$$ where $(\alpha,\beta)'$ is the double partition obtained from $(\alpha,\beta)$ by subtracting one from one of the parts. This isomorphism follows from the bijection $t^{(\alpha,\beta)}\rightarrow t^{(\alpha,\beta)'}$ of $T_{(\alpha,\beta)}$ and $\bigcup_{(\alpha,\beta)'\subset (\alpha,\beta)}T_{(\alpha,\beta)'}$, where $t^{(\alpha,\beta)'}$ is the pair of standard tableaux obtained by removing the box containing $n$. Moreover, $\pi^{(n)}=\bigoplus_{(\alpha,\beta)\vdash n}\pi_{(\alpha,\beta)}$ is a faithful representation of $H_n(q,Q)$. Note that (H1) and (H2) are the defining relations for the braid group $\mathcal{B}_n(A)$. So representations of $H_n(q,Q)$ also yield in particular representations of $\mathcal{B}_n(A)$. Obviously we also obtain representations of the braid group of type $B$. The Hecke algebras satisfies the following embedding of algebras $H_0\subset H_1 \subset H_2 \subset \cdots$ We shall denote $$H_{\infty}(q,Q):= \bigcup_{n \geq 0}{H_n(q,Q)}$$ Observe that (H3) and (H4) imply that $t$ and $g_i$ have at most 2 eigenvalues each, hence also at most 2 projections corresponding to these eigenvalues. *Right and Double Coset Representatives* The fact that $q$ is invertible in $\mathbb{C}(q,Q)$ implies that the generators $g_i$ are also invertible in $H_n(q,Q)$. In fact, the inverse of the generators is given by $$g_i^{-1} = q^{-1}g_i + (q^{-1}-1)1 \in H_n(q,Q)$$ This implies that the following element is well-defined in $H_n(q,Q)$: $t_i^{'}=g_i\cdots g_1tg_1^{-1} \cdots g_i^{-1}$. We use this elements to define the set $\mathcal{D}_n$ as a subset of $H_n(q,Q)$. If $n=1$, we let $\mathcal{D}_1 := \{1,t\}$. For $n\geq 2$ we have $$\mathcal{D}_n:=\{1,g_{n-1},t^{'}_{n-1}\}.$$ Also the set of right coset representatives of $H_{n-1}(q,Q)$ in $H_n(q,Q)$ is given as follows: $$\mathcal{R}_n :=\{ 1,\ t'_{n-1},\  g_{n-1}g_{n-2}\ldots g_{n-k},\  g_{n-1}g_{n-2}\ldots g_{n-k}t'_{n-k-1} \ (1\leq k\leq n-1)\}.$$ Note that $\mathcal{R}_1 = \{1,t\}$. The elements $\{ r_1r_2\ldots r_n| r_i \in \mathcal{R}_i\}$ form a $\mathbb{C}(q,Q)$-basis of $H_n(q,Q)$, see [@gl].
