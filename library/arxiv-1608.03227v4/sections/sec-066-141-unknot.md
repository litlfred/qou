---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-066-141-unknot
section_title: "Unknot"
section_number: 14.1
pages: 78-81
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.962
---
[]{#sec:unknot label="sec:unknot"}

Let us evaluate our knot invariant on the unknot $L(1)$, $1\in \Brgr_1$.

::: proposition
The Poincare polynomial of $L(1)$ is $$\sum_{i,j,k}\mathcal{H}^{i,j,k}q^it^j a^i=\frac{a^{-1}+at}{q^{-1}-q}.$$
:::

::: proof
*Proof.* We have $X=\calXr_2(G_1)=\frg_1\times G_1\times 0$. Respectively $\bar{\mathcal{C}}_1=\mathcal{O}_X$ and since $\calX_1(G_1)=\frg_1\times 0$, we have $\mathbb{S}_1=j^*_e(\bar{\mathcal{C}}_1)=\mathcal{O}_{\frg_1}$. Since weight of $T_{sc}$-action along $\frg_1=\CC$ is $q^2$ and $\mathcal{B}=\CC$ is the trivial vector bundle of weight $t$, we conclude the formula from the statement. ◻
:::

## HOMFLY-PT polynomial specialization

The space $\calH^k(\beta)$ is doubly-graded with $q,t$ gradings induced by the action of $T_{sc}$ on $\Hilb^{free}_{1,n}$. We denote by $\calH^{i,j,k}(\beta)$ the subspace of $\calH^k(\beta)$ of degree $t^iq^j$. Respectively we introduce the super-polynomial: $$\SymbolPrint{\calP}(L(\beta)):= \sum_{i,j,k} t^iq^j a^k \calH^{i,j,k}(\beta),$$ where $\beta\in \Brgr_n$. In this section we explain why our super polynomial $\calP(L)$ specializes to the HOMFLY-PT polynomial $P(L)$.

First of all let us notice that $\calP(L(\beta))$ has a well defined specialization at $t=-1$. The space $\mathbb{H}^k(\beta)$ is infinite dimensional doubly-graded space with each graded piece is finite-dimensional. However if we forget about one of the gradings the last property might stop being true but it does not happen under the specialization $t=-1$.

Indeed, only coordinates $Y$ along $\frn$ have non-trivial $t$-weights in coordinate ring of $\widetilde{\Hilb}_{1,n}^{free}$. On the other hand since $Y$ is strictly upper triangular all these variables have non-trivial positive weights with respect to the maximal torus $T\subset B$. The other coordinates on $\widetilde{\Hilb}_{1,n}^{free}$ have nonnegative weights with respect to the maximal torus and positive $q$-weight. Thus only finitely many powers of $Y_{ij}$ could possibly contribute to $\mathbb{H}^k(\beta)$ which is constructed out of $T$-isotypical components of the rings of functions on the open Cech charts of $\widetilde{\Hilb}_{1,n}^{free}$.

Let us fix conventions about the HOMFLY-PT polynomial $P(L)$: $$aP(L_+)-a^{-1} P(L_-)=(q-q^{-1})P(L_0), \quad P(\mathrm{unknot})=1,$$ where $L_+$ and $L_-$ are positive and negative crossings.

::: theorem
[]{#thm:HOMFLYPT label="thm:HOMFLYPT"} For any $\beta\in \Brgr_n$ we have $$P(L(\beta))= \calP(L(\beta))|_{t=-1}$$
:::

::: proof
*Proof.* First, let us notice that the theorem [\[thm: main\]](#thm: main){reference-type="ref" reference="thm: main"} implies that the map $$\Tr_n: \Brgr_n\to \calP(L(\beta))|_{t=-1}$$ is a trace map: $\Tr_n(ab)=\Tr_n(ba)$. Also, the construction of the elements $\calC_{\pm}^{(i)}$ and the description of $\calC_+$ and $\calC_-$ as cones in proposition [\[prop: cones\]](#prop: cones){reference-type="ref" reference="prop: cones"} implies that $\Tr_n$ satisfies the skein relations: $$a\Tr_n(\tau\sigma_i)-a^{-1}\Tr_n(\tau\sigma_i^{-1})=(q-q^{-1})\Tr_{n}(\tau),$$ $\tau\in \Brgr_{n-1}$.

Let us spell out the details for the skein relations. Since we imposed condition that all differentials in our matrix factorizations have degree $t$, setting $t=-1$ corresponds to passing to the K-theory of the category matrix factorizations. We denote by $[\calC]$ the corresponding class of the matrix factorization in the K-theory. Thus the statement in proposition [\[prop: cones\]](#prop: cones){reference-type="ref" reference="prop: cones"} implies the linear relations in K-theory: $$[\calC_+]=-\mathrm{q}^{-1}\left([\calC_\parallel]-[\calC_\bullet\langle-1,-1\rangle]\right),$$ $$[\calC_-]=-\mathrm{q}^{-1}\left(-\mathrm{q}^2[\calC_\parallel]+[\calC_\bullet\langle-1,-1\rangle]\right).$$ Taking into account the shift $k-\mathrm{wr}(\beta)+n-1$ in the definition of $\mathcal{H}^k(\beta)$ we the skein relation by canceling the terms related to class $[\calC_\bullet\langle-1,-1\rangle]$.

Since $L(\tau\sigma)=L(\tau\sigma^{-1})$ the inductive argument shows that the skein relations imply that $\Tr_{n}(1)=A^{n}$ where $A=\Tr_1(1)=(a^{-1}-a)/(q^{-1}-q)$. Indeed, since $L(\sigma_n^{\pm 1}1_{n+1})=L(1_n)$, $1_n\in\Brgr_n$ and $Tr_n(\beta)$ is an isotopy invariant of $L(\beta)$, we can use the skein relations: $$a\Tr_{n+1}(\sigma_n)-a^{-1}\Tr_{n+1}(\sigma_n^{-1})=(a-a^{-1})\Tr_n(1)=(q-q^{-1})\Tr_{n+1}(1).$$

Let us defined renormalized trace $$\label{eq: trace OJ}
 \textup{tr}'_n(\beta):=\left(\frac{a}{q}\right)^{\xwr(\beta)}A^{-n}\Tr_n(\beta),$$ where $\xwr(\sigma_{i_1}^{\epsilon_1}\dots \sigma_{i_\ell}^{\epsilon_\ell})=\sum_{i=1}^{\ell} \epsilon_i.$

The Hecke algebra $H_n$ is generated by $g_i$, $i=1,\dots,n-1$ modulo relations: $$g_ig_{i+1}g_{i}=g_{i+1}g_ig_{i+1},
  \quad i=1,\dots,n-2,$$ $$g_i-g_i^{-1}=q-q^{-1},\quad i=1,\dots, n-1.$$

There is a natural algebra homomorphism $\pi:\Brgr_n\to H_n$, $\sigma_i\mapsto g_i$. The skein relations imply that the map $\textup{tr}'_n$ factors through the projection $\pi$: $\textup{tr}_n=\textup{tr}_n\circ \pi$ where $\textup{tr}'_n: H_n\to \CC(a,q)$ is the trace on $H_n$. Since the trace $\Tr_n$ satisfies the Markov move $\Tr_n(\tau\sigma_{n-1}^{\pm1 })=\Tr_{n-1}(\tau)$ we see that the sequence of traces $\textup{tr}_n$ satisfies the same restrictions as Ocneanu-Jones trace (see section 5 of [@Jones]):

1.  $\textup{tr}_n(1)=1$

2.  $\textup{tr}_n(\alpha\beta)=\textup{tr}(\beta\alpha)$

3.  $\textup{tr}_n(\tau g_{n-1})=z\textup{tr}_{n-1}(\tau),$ $g\in H_{n-1}$

where $z=aq^{-1}A^{-1}$. The factor $z$ appears in the last formula because $$\textup{tr}_n(\tau g_{n-1})=\left(\frac{a}{q}\right)^{\mathrm{wr}(\tau g_{n-1})}A^{-n}\Tr_n( \tau g_{n-1})=
\left(\frac{a}{q}\right)^{\xwr(\tau)}A^{-n+1} \Tr_{n-1}(\tau) aq^{-1}A^{-1}.$$

According to the section 5 of [@Jones] the trace on $\cup H_n$ with such properties is unique and according to the section 6 of [@Jones] the renormalized trace $\Tr_n$ as in equation [\[eq: trace OJ\]](#eq: trace OJ){reference-type="ref" reference="eq: trace OJ"} defines the HOMFLY-PT polynomial. ◻
:::

## $gl(m|n)$-homology differential

Recall that the vector bundle $\calB_n^\vee$ over $\widetilde{\Hilb}^{free}_{1,n}$ is a vector bundle with the fiber $V$ over the point $(X,Y,v)$ where $V=\CC^n$ and $v$ is the cyclic vector. Define a section $\varphi_{m|n}$ of $\calB_n^\vee$ with the value $X^mY^n v\in V$ at the fiber at the point $(X,Y,v)$. Contraction with this section $$i_{\varphi_{m|n}}: \Lambda^\bullet \calB_n\to \Lambda^{\bullet-1}\calB_n.$$

induces the differential $d_{m|n}: \bbS_\beta\otimes \Lambda^\bullet\calB_n\to \bbS_\beta\otimes \Lambda^{\bullet-1}\calB_n$, which

commutes with the Čech differential $d_c$, the Chevalley-Eilenberg differential $d_{ce}$, the equivariant correction differentials $\partial_l+\partial_r$ and the matrix factorization differential $D$. Thus we can define following homology $$\mathbb{H}_{m|n}(\beta)=(\oplus_{i=0}^n \bbS_\beta\otimes \Lambda^\bullet\calB_n, D_{tot}^{m|n}),\quad D_{tot}^{m|n}:=D+\partial_l+\partial_r+d_{ce}+d_{c}+d_{m|n}.$$ The homology $\mathbb{H}_{m|n}(\beta)$ is only doubly graded. In forthcoming paper we prove the following

::: theorem
[@OR] $\mathbb{H}_{m|n}(\beta)$ is an isotopy invariant of $L(\beta)$.
:::

The differential $d_{m|n}$ is very much in spirit of the conjectures in the papers [@ORS; @GGS] and thus we propose the conjecture:

::: conjecture
The homology $\mathbb{H}_{m|n}$ categorifies the quantum invariant of type $gl(m|n)$.
:::
