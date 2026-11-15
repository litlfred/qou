---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-029-42-links-in-s2times-s1-and-rozanskys-proposal
section_title: "Links in $S^2\times S^1$ and Rozansky's proposal"
section_number: 4.2
pages: 60-63
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.938
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
[]{#sec:Roz label="sec:Roz"}

For $M_3=S^2\times S^1$, the theory $T[M_3]$ is a particular case of ([\[TCircFib\]](#TCircFib){reference-type="ref" reference="TCircFib"}) with $p=0$ and $g=0$, that is the theory of 3d ${\mathcal N}=2$ vector multiplet with gauge group ${\mathcal G}=G=SU(2)$. In this case $\mathrm{Tor}\,H_1(M_3,{\mathbb Z})=0$ and the only independent Wilson loop in $T[M_3]$ is the trivial Wilson loop. Also, there is only one homological block $\widehat{Z}_0$. Therefore, for an arbitrary representation $\lambda$ of $SU(2)$, the decomposition [\[WilsonDec\]](#WilsonDec){reference-type="eqref" reference="WilsonDec"} allows to write the Wilson loop $W_\lambda$ as [\[babyexmpl\]](#babyexmpl){reference-type="eqref" reference="babyexmpl"}: $$W_\lambda \; = \; W_0\otimes {\mathcal H}_{\lambda}^{0;i,j;\ell} \,.$$ In other words, in this case we expect a factorization $${\mathcal H}_a[S^2\times S^1;K^{\lambda},{\mathcal R}_\lambda] \; = \; \bigoplus_{i,j,\ell\in{\mathbb Z}}{\mathcal H}_{\lambda}^{0;i,j;\ell}\otimes {{\mathcal H}}_a[S^2\times S^1]$$ where the first factor on the right-hand side is the $S^2\times S^1$ analogue of the Khovanov-Rozansky homology of the corresponding link $K^{\lambda}$ colored by ${\mathcal R}_{\lambda}$. What is $K^{\lambda}$? And, what is ${\mathcal R}_{\lambda}$?

As we shall see below, already in this relatively simple case of $M_3 = S^1 \times S^2$ the map between colored knots and links in $M_3$ and the UV line operators $W_{\lambda}$ in $T[M_3]$ is rather non-trivial. Since Wilson loops in $T[M_3]$ come from M2-branes wrapping the $S^1$ circle of $S^1 \times S^2$, we expect that the precise dictionary $W_{\lambda} \leftrightarrow (K^{\lambda}, {\mathcal R}_{\lambda})$ maps $\lambda$ to a certain link in $M_3$ that winds around $S^1$, and the total winding number (counted with multiplicities given by ${\mathcal R}_{\lambda}$) is equal to $|\lambda|$. Regarding $M_3 = S^1 \times S^2$ as a special case of the Hopf fibration (namely, the trivial fibration), in the rest of this section we present evidence for the following identification[^1] $$\boxed{\phantom{\int}
W_\lambda \quad \leftrightarrow \quad (K^{\lambda}, {\mathcal R}_{\lambda}) \; = \; \text{``$\lambda$-cable'' of the unknot along the Hopf fiber}
\phantom{\int}}
\label{Gamma-Lp1}$$ Specifically, $\lambda = {\square}^{\otimes 2n}$ corresponds to a link $L_{2n}$ made of $2n$ copies of the unknot along the Hopf fiber, all colored by the fundamental representation of $SU(2)$. And $(K^{\lambda}, {\mathcal R}_{\lambda})$ for general $\lambda$ is a linear combination of $L_{2n}$'s that replicates the decomposition of $\lambda$ into ${\square}^{\otimes 2n}$'s. Such decomposition is usually referred to as the "cabling formula" (see Appendix [\[app:cabling\]](#app:cabling){reference-type="ref" reference="app:cabling"}).

Curiously, a similar problem was already considered by Rozansky from a purely mathematical point of view in [@rozansky2010categorification]. Specifically, the Conjecture 6.10 in [@rozansky2010categorification] gives a concrete description for the homological invariant of the link $L_{2n}$. We shall verify that Rozansky's proposal[^2] matches exactly with the quantum field theory computation if the generators $a_i$ and $\theta_i$ are assigned flavor charges $i$, that is $$\mathrm{deg}_t \, a_i=\mathrm{deg}_t \, \theta_i=i.$$

Using the decomposition of tensor products of $SU(2)$ representations, we can write the expectation value of $2n$ Wilson loops in $T[M_3]$ as a sum over expectation values of Wilson loops labeled by irreducible representations. Only even representations with highest weight $2l=0,2,\ldots,2n$ appear in this decomposition: $$\label{WilsonDec1}
\langle W_{{\square}^{\otimes 2n}}\rangle =\sum_{l=0}^n \left[{{2n}\choose {n-l}}-{{2n}\choose {n-l-1}}\right] \langle W_{2l}\rangle.$$ The expectation value of the Wilson loop $W_{2l}$ in $T[M_3]$, which gives the graded Euler characteristic of ${\mathcal H}_\lambda$,[^3] $$\sum_{i,j,\ell}(-1)^jq^it^\ell\dim{\mathcal H}_\lambda^{0;i,j,\ell} \equiv\chi_{q,t}({\mathcal H}_\lambda)=\langle W_{2l}\rangle\equiv \frac{\widehat{Z}_0(q,t;W_{2l})}{\widehat{Z}_0(q,t)}$$ can be computed using [\[BlockKnot\]](#BlockKnot){reference-type="eqref" reference="BlockKnot"}, with $T[S^1\times S^2,SU(2)]$ now being the 3d ${\mathcal N}=4$ super-Yang-Mills theory. We obtain $$\langle W_{2l}\rangle \; = \; \frac{(qt)^{l} (1/t;q)_l}{(q^2t;q)_l},$$ and the expectation values of $W_{2l+1}$ all vanish.

On the other hand, as a vector space, the homological invariant $H^\bullet(S^1\times S^2,L_{2n})$ proposed in Conjecture 6.10 of [@rozansky2010categorification] admits a similar decomposition into subspaces of pure ${\bf x}$-degree[^4] $$H^\bullet_{\text{Rozansky}}(L_{2n})=\bigoplus_{l=0}^{n} V_l \otimes {\mathbb Q}[a_1,\theta_1,a_2,\theta_2,\ldots, a_l,\theta_l].$$ Here, $V_l$ is a quotient of the vector space spanned by monomials of $x_1,\ldots,x_{2n}$, with degree $n-l$, by the relations $$x_i^2=0 \quad \text{and} \quad \sum_{i=1}^{2n} x_i=0.$$ It is easy to check that[^5] $$\dim V_l= {{2n}\choose {n-l}}-{{2n}\choose {n-l-1}}$$ are exactly the coefficients in [\[WilsonDec1\]](#WilsonDec1){reference-type="eqref" reference="WilsonDec1"}. In particular, $V_j$ with $j<0$ is empty, and the dimension of $V_0$ is given by the $n$-th Catalan number. Then $$\label{EquiEuler2}
\chi_t(H^\bullet)=\sum_{j=0}^n \dim V_l\cdot{\mathfrak q}^{2n-2j}\cdot\frac{(t;t{\mathfrak q}^{-2})_j}{(t{\mathfrak q}^{-4};t{\mathfrak q}^{-2})_j},$$ where we have used the ${\mathfrak q}$-degree of the generators, $$\begin{aligned}
\mathrm{deg}_{{\mathfrak q}} x_i=& \quad 2,\\
\mathrm{deg}_{{\mathfrak q}} a_i=&-2i-2,\\
\mathrm{deg}_{{\mathfrak q}} \theta_i=&-2i+2.
\end{aligned}$$ If we shift the overall ${\mathfrak q}$-degree of $H^\bullet$ by $-2n$ units to remove the ${\mathfrak q}^{2n}$ factor in [\[EquiEuler2\]](#EquiEuler2){reference-type="eqref" reference="EquiEuler2"}, what remains is in perfect agreement with the expectation value of Wilson loops in 3d theory $T[M_3]$: $$\langle W_{2l}\rangle= (qt)^j\cdot \frac{(1/t;q)_j}{(tq^2;q)_j}={\mathfrak q}^{-2j}\cdot\frac{(t,t{\mathfrak q}^{-2})_j}{(t{\mathfrak q}^{-4};t{\mathfrak q}^{-2})_j},$$ with a typical relation between $q$ and ${\mathfrak q}$ [@Fuji:2012pm]: $${\mathfrak q}^2 \; = \; qt \,.$$ So, we have verified the conjecture by Rozansky at the level of equivariant Euler characteristics for this link $L_{2n}$, $$\chi_{q,t}({\mathcal H}_{\text{BPS}}) \; = \; \chi_{q,t}(H_{\text{Rozansky}})$$ presenting some evidence for the isomorphism between $H^\bullet_{\text{Rozansky}} (S^1\times S^2,L_{2n}) \{ -2n \}$ and ${\mathcal H}_{\lambda} \; : = \; \bigoplus_{i,j,\ell\in{\mathbb Z}}{\mathcal H}_{\lambda}^{0;i,j;\ell}$ with $\lambda = {\square}^{\otimes 2n}$.

As a side remark, positivity also features in the invariants $\widehat{Z}_a(M_3; K_{{\mathcal R}})$ of three manifolds with knots, in a way similar to the case without knot ([\[block-pos\]](#block-pos){reference-type="ref" reference="block-pos"}). For example, in our case of $M_3 = S^2 \times S^1$, $$\begin{gathered}
    -\widehat{Z}_0(q,-t;W_{6})=
    \left(2 t^3+2 t^2\right) q^3+\left(2 t^4+4 t^3+4 t^2+2 t\right) q^4+\\
    \left(2 t^5+6 t^4+10 t^3+10 t^2+4 t\right) q^5+
    \left(2 t^6+8 t^5+16
       t^4+22 t^3+18 t^2+8 t+2\right) q^6+
       \\
       \left(2 t^7+8 t^6+20 t^5+36 t^4+44 t^3+34 t^2+14 t+2\right) q^7+O\left(q^8\right)
\end{gathered}$$ has only positive coefficients.

[^1]: Note, in the unrefined / decategorified setting, $K^{\lambda}$ is simply the unknot colored by ${\mathcal R}_{\lambda} = \lambda$. Although this is no longer the case in homological world, there is still a close relation between "cabling" and "color" [@khovanov2005categorifications; @Gukov:2005qp].

[^2]: The Conjecture 6.10 in [@rozansky2010categorification] contains a typo in the description of the ideal $I_{\text{rel}}$. Namely, $$\label{OldRelation}
    a_i p_i({\bf x})=\theta_i p_i({\bf x})=0$$ should be replaced by $$\label{NewRelation}
    a_i p_{n-i+1}({\bf x})=\theta_i p_{n-i+1}({\bf x})=0.$$

[^3]: In this normalization, we have $$\label{WilsonNorm}
    \langle W_0\rangle=1,$$ enabling us to directly extract the information about the space ${\mathcal H}_{\lambda}^{i,j;\ell}$.

[^4]: This decomposition doesn't respect the ring structure as each subspace is not closed under multiplication.

[^5]: Basically, there are ${{2n}\choose {n-l}}$ non-vanishing degree $(n-l)$ monomials, and they are subject to ${{2n}\choose {n-l-1}}$ independent relations, obtained by multiplying $\sum_i x_i$ with degree $(n-l-1)$ monomials.
