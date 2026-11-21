---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-017-62-strong-stability-preservation
section_title: "Strong Stability Preservation"
section_number: 6.2
pages: 19-22
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.986
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#str_Cstab_subsect label="str_Cstab_subsect"}

We now state one of our main characterization results, the strong stability preservation characterization. We then derive the Borcea-Brändén characterization as a corollary.

::: theorem
[]{#Cops_graces label="Cops_graces"} Fix $\lambda \in \mathbb{N}_0^m$, $\alpha \in \mathbb{N}_0^l$, a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$, any disjoint Grace pair $(C_1 \times \cdots \times C_m, B_1 \times \cdots \times B_m)$, and any sets $S_1,\ldots,S_l \subseteq \mathbb{CP}^1$. The following are equivalent.

1.  $T$ maps $(C_1 \times \cdots \times C_m)$-stable polynomials to nonzero $(S_1 \times \cdots \times S_l)$-stable polynomials.

2.  $T$ maps $(C_1 \times \cdots \times C_m)$-stable evaluation symbols to nonzero $(S_1 \times \cdots \times S_l)$-stable polynomials.

3.  $\mathop{\mathrm{Symb}}(T)$ is $(B_1 \times \cdots \times B_m) \times (S_1 \times \cdots \times S_l)$-stable.
:::

One should notice the generality of this result in terms of stability regions. First note that any disjoint Grace pair can be considered, without altering the symbol in any way (e.g., via conjugation by Möbius transformations). And further, the output sets that can be considered have no restrictions whatsoever. The power of these extra features can be seen in the following examples, which demonstrate classical results regarding polynomial convolutions in a very symbol-oriented way.

::: example
[]{#add_conv_ex1 label="add_conv_ex1"} Fix $p,q \in V(n)$, so that $(z_j:1)$ are the roots in $\mathbb{CP}^1$ of $q$ for $j \in [n]$. So, $q$ has no roots at $\infty$. The additive (Walsh) convolution of $p$ and $q$ is defined via: $$p *_+^n q := \frac{1}{n!} \sum_{k=0}^n \partial_x^k p \cdot (\partial_x^{n-k} q)(0,1)$$ With this, $T_q(p) := p *_+^n q$ is a linear operator in $\mathop{\mathrm{Hom}}(V(n),V(n))$, and we have: $$\mathop{\mathrm{Symb}}(T_q) = \prod_{j=1}^n (xw - (z + z_jw)y) = \mathop{\mathrm{Hmg}}_{(n,n)}\left[\prod_{j=1}^n (x - (z + z_j))\right]$$ Let $C \subset \mathbb{CP}^1$ be any projectively convex region, and define $S := \bigcup_j (C + z_j)$. If we order the input variables of $\mathop{\mathrm{Symb}}(T_q)$ as $(z,w,x,y)$, it is then straightforward to show that $\mathop{\mathrm{Symb}}(T_q)$ is $C \times (\mathbb{CP}^1 \setminus S)$-stable. (First deal with possible $(x:y) = (1:0)$ or $(z:w) = (1:0)$ cases, and then assume $y = w = 1$ to simplify the remaining cases.) Applying the previous theorem, this implies $T_q$ maps polynomials with roots in $C$ to polynomials with roots in $S$. (This is Theorem 5.3.1 in [@rahman2002anthpoly].) Picking $C = \overline{\mathcal{H}_-}$ and real-rooted $q$ implies $T_q$ maps $\mathcal{H}_+$-stable polynomials to $\mathcal{H}_+$-stable polynomials. Restricting to $p \in V_\mathbb{R}(n)$ then shows that $T_q$ preserves real-rootedness.
:::

::: example
[]{#mult_conv_ex1 label="mult_conv_ex1"} Fix $p,q \in V(n)$, so that $(z_j:1) \neq 0$ are the roots of $q$ for $j \in [n]$. So, $q$ has no roots at $0$ or $\infty$. The multiplicative (Grace-Szegő) convolution of $p$ and $q$ (with coefficients $p_k$ and $q_k$, respectively) is defined via: $$p *_\times^n q := \sum_{k=0}^n \binom{n}{k}^{-1} (-1)^k p_k q_k x^k y^{n-k}$$ With this, $T_q(p) := p *_\times^n q$ is a linear operator in $\mathop{\mathrm{Hom}}(V(n),V(n))$, and we have: $$\mathop{\mathrm{Symb}}(T_q) = \prod_{j=1}^n (xw - z_jzy) = \mathop{\mathrm{Hmg}}_{(n,n)}\left[\prod_{j=1}^n (x - z_j z)\right]$$ Let $C \subset \mathbb{CP}^1$ be any projectively convex region, and define $S := \bigcup_j (z_j \cdot C)$. If we order the input variables of $\mathop{\mathrm{Symb}}(T_q)$ as $(z,w,x,y)$, it is then straightforward to show that $\mathop{\mathrm{Symb}}(T_q)$ is $C \times (\mathbb{CP}^1 \setminus S)$-stable. (As above, first deal with possible $(x:y) = (1:0)$ or $(z:w) = (1:0)$ cases, and then assume $y = w = 1$ to simplify the remaining cases.) Applying the previous theorem, this implies $T_q$ maps polynomials with roots in $C$ to polynomials with roots in $S$. (This is Theorem 3.4.1d in [@rahman2002anthpoly].) Picking $C = \mathcal{H}_-\cup \mathbb{R}_+$ and $q$ with only positive roots implies $T_q$ maps $(\mathcal{H}_+\cup \overline{\mathbb{R}_-})$-stable polynomials to $(\mathcal{H}_+\cup \overline{\mathbb{R}_-})$-stable polynomials. Restricting to $p \in V_\mathbb{R}(n)$ then shows that $T_q$ preserves positive-rootedness.
:::

In order to prove the above theorem, we need an operator-theoretic corollary to Grace's theorem. The following result is the main motivation for the symbol lemma (Lemma [\[symb_lemma\]](#symb_lemma){reference-type="ref" reference="symb_lemma"}), and demonstrates just how closely Grace's theorem relates to stability properties of linear operators. Further, it gives a slightly stronger result in one direction of the above characterization, as Grace pair disjointness is not a required premise.

::: proposition
[]{#Cops_prop label="Cops_prop"} Fix $\lambda \in \mathbb{N}_0^m$, $\alpha \in \mathbb{N}_0^l$, a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$, any Grace pair $(C_1 \times \cdots \times C_m, B_1 \times \cdots \times B_m)$, and any sets $S_1,\ldots,S_l \subseteq \mathbb{CP}^1$. If $\mathop{\mathrm{Symb}}(T)$ is $(B_1 \times \cdots \times B_m) \times (S_1 \times \cdots \times S_l)$-stable, then $T$ maps $(C_1 \times \cdots \times C_m)$-stable polynomials to nonzero $(S_1 \times \cdots \times S_l)$-stable polynomials.
:::

::: proof
*Proof.* Fix any $(C_1 \times \cdots \times C_m)$-stable $q \in V(\lambda)$ and any $(c,d) = (c_1,d_1,\ldots,c_l,d_l) \in \mathbb{C}^{2l}$ such that $(c_j:d_j) \in S_j$ for all $j \in [l]$. Let $k_{\lambda,\alpha} := (-1)^\alpha(\lambda!)^2(\alpha!)^2$. The evaluation symbol lemma (Lemma [\[ev_lemma\]](#ev_lemma){reference-type="ref" reference="ev_lemma"}) and the symbol lemma (Lemma [\[symb_lemma\]](#symb_lemma){reference-type="ref" reference="symb_lemma"}) then give us the following expression of $T(q)$ evaluated at $(c,d) = (c_1,d_1,\ldots,c_l,d_l)$: $$\begin{split}
            k_{\lambda,\alpha} T(q)(c,d) &= k_{\lambda,0} D^\alpha\big(T(q) \otimes (dx-cy)^\alpha\big) \\
                &= D^{\lambda \sqcup \alpha}\big(\mathop{\mathrm{Symb}}(T) \otimes q \cdot (dx-cy)^\alpha\big) \\
                &= k_{0,\alpha} D^\lambda\big(\mathop{\mathrm{Symb}}(T)(z,w,c,d) \otimes q(z,w)\big)
        \end{split}$$ In the last expression above, $D^\lambda$ acts on the variables $(z,w) = (z_1,w_1,\ldots,z_m,w_m)$. Since $r(z,w) := \mathop{\mathrm{Symb}}(T)(z,w,c,d)$ is $(B_1 \times \cdots \times B_m)$-stable and $q(z,w)$ is $(C_1 \times \cdots \times C_m)$-stable, we have that the last expression above is nonzero by definition of Grace pair (Definition [\[grace_pair_def\]](#grace_pair_def){reference-type="ref" reference="grace_pair_def"}). This implies $T(q)$ is $(S_1 \times \cdots \times S_l)$-stable. ◻
:::

With this, we now give the proof of Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}.

::: proof
*Proof of Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}.* The statement of this result, as well as its proof, is quite similar to that of the evaluation symbol version of Grace's theorem given in Corollary [\[ev_graces\]](#ev_graces){reference-type="ref" reference="ev_graces"}. We explicitly give the proof anyway, as it is rather short and straightforward.

$(i) \Rightarrow (ii)$. Immediate.

$(ii) \Rightarrow (iii)$. Fix $(a,b) = (a_1,b_1,\ldots,a_m,b_m) \in \mathbb{C}^{2m}$ such that $(a_j:b_j) \in B_j$ for all $j \in [m]$, and fix $(c,d) = (c_1,d_1,\ldots,c_l,d_l) \in \mathbb{C}^{2l}$ such that $(c_j:d_j) \in S_j$ for all $j \in [l]$. Let $k_{\lambda,\alpha} := (-1)^\alpha(\lambda!)^2(\alpha!)^2$. Since $B_j$ and $C_j$ are disjoint, we have that $(a_j:b_j) \not\in C_j$ for all $j$, and therefore $\mathop{\mathrm{Symb}}(\mathop{\mathrm{ev}}_{(a,b)}) = (bx-ay)^\lambda \in V(\lambda)$ is an evaluation symbol which is $(C_1 \times \cdots \times C_m)$-stable. Using the evaluation symbol lemma (Lemma [\[ev_lemma\]](#ev_lemma){reference-type="ref" reference="ev_lemma"}) and the symbol lemma (Lemma [\[symb_lemma\]](#symb_lemma){reference-type="ref" reference="symb_lemma"}), we compute: $$(-1)^\lambda k_{\lambda,\alpha} \mathop{\mathrm{Symb}}(T)(a,b,c,d) = D^{\lambda \sqcup \alpha}(\mathop{\mathrm{Symb}}(T) \otimes (bx-ay)^\lambda (dx-cy)^\alpha) = k_{\lambda,\alpha} T[(bx-ay)^\lambda](c,d)$$ By $(ii)$ the last expression is nonzero, and thus $\mathop{\mathrm{Symb}}(T)(a,b,c,d) \neq 0$. This implies $\mathop{\mathrm{Symb}}(T)$ is $(B_1 \times \cdots \times B_m) \times (S_1 \times \cdots \times S_l)$-stable.

$(iii) \Rightarrow (i)$. Proposition [\[Cops_prop\]](#Cops_prop){reference-type="ref" reference="Cops_prop"} above. ◻
:::

As mentioned above, the previous proposition gives a slightly stronger result in the (symbol stability $\Rightarrow$ operator stability) direction. Using it, we revisit the additive and multiplicative convolutions with a more algebraic/symbolic mentality.

::: example
By Definition [\[symb_def\]](#symb_def){reference-type="ref" reference="symb_def"}, the $\mathop{\mathrm{Symb}}$ map gives a bijection between certain spaces of linear operators and polynomials. So, we can uniquely define a linear operator by giving its symbol. Using this idea, we specify $T \in \mathop{\mathrm{Hom}}(V(n,n), V(n))$ by defining its symbol in $V(n,n,n)$ with variables $(z,w),(t,s),(x,y)$ as follows: $$\mathop{\mathrm{Symb}}(T) := \mathop{\mathrm{Hmg}}_{(n,n,n)}\left[(x - (z+t))^n\right] = (xws - (zs + tw)y)^n$$ Now, let us consider the additive convolution $*_+^n$ as an element of $\mathop{\mathrm{Hom}}(V(n,n),V(n))$ in the following way. Since $V(n,n) \cong V(n) \boxtimes V(n)$, we define $*_+^n$ on elements $p \boxtimes q \in V(n) \boxtimes V(n)$ via $*_+^n(p \boxtimes q) := p *_+^n q$ and extend linearly. We then compute $\mathop{\mathrm{Symb}}(*_+^n)$ as follows: $$\mathop{\mathrm{Symb}}(*_+^n) = *_+^n\left[(zy-xw)^n \boxtimes (ty-xs)^n\right] = (xws - (zs + tw)y)^n$$ That is, $*_+^n$ is the operator that has our desired symbol. Fixing any $a,b,c,d \in \mathbb{R}$ such that $a<b$ and $c<d$, we define the sets $C_1 := \overline{\mathcal{H}_+} \setminus (a,b)$, $C_2 := \overline{\mathcal{H}_+} \setminus (c,d)$, $B_1 := \mathcal{H}_-\cup [a,b]$, $B_2 := \mathcal{H}_-\cup [c,d])$, and $S := \overline{\mathcal{H}_+} \setminus [a+c,b+d]$. Proposition [\[Cops_prop\]](#Cops_prop){reference-type="ref" reference="Cops_prop"} then implies $p *_+^n q$ has all its roots in $[a+c,b+d]$ whenever $p,q \in V_\mathbb{R}(n)$ have all their roots in $(a,b)$ and $(c,d)$, respectively. For real-rooted $p,q$ of degree $n$, this implies: $$\mathop{\mathrm{minroot}}(p) + \mathop{\mathrm{minroot}}(q) \leq \mathop{\mathrm{minroot}}(p *_+^n q) \leq \mathop{\mathrm{maxroot}}(p *_+^n q) \leq \mathop{\mathrm{maxroot}}(p) + \mathop{\mathrm{maxroot}}(q)$$ Notice that we actually get a bit more. For $(C_1 \times C_2)$-stable $r := \sum_j p_j \boxtimes q_j \in V(n) \boxtimes V(n) \cong V(n,n)$, we have that $*_+^n[r]$ is $S$-stable. That is, $*_+^n$ has stability properties as an operator in $\mathop{\mathrm{Hom}}(V(n,n),V(n))$, not just as a convolution between two polynomials in $V(n)$.
:::

::: example
As in the previous example, we can consider the multiplicative convolution $*_\times^n$ as an element of $\mathop{\mathrm{Hom}}(V(n,n),V(n))$ by defining $*_\times^n(p \boxtimes q) := p *_\times^n q$ on elements $p \boxtimes q \in V(n) \boxtimes V(n) \cong V(n,n)$ and extending linearly. We then compute its symbol in $V(n,n,n)$ with variables $(z,w),(t,s),(x,y)$ as follows: $$\mathop{\mathrm{Symb}}(*_\times^n) = *_\times^n\left[(zy-xw)^n \boxtimes (ty-xs)^n\right] = (xws - zty)^n = \mathop{\mathrm{Hmg}}_{(n,n,n)}\left[(x-zt)^n\right]$$ Fixing any $a,b,c,d \in \mathbb{R}_+$ such that $0<a<b$ and $0<c<d$, we define the sets $C_1$, $C_2$, $B_1$, and $B_2$ as in the previous example. We then define $S := \overline{\mathbb{R}} \setminus [ac, bd]$. Proposition [\[Cops_prop\]](#Cops_prop){reference-type="ref" reference="Cops_prop"} then implies $p *_\times^n q$ has all its real roots in $[ac,bd]$ whenever $p,q \in V_\mathbb{R}(n)$ have all their roots in $(a,b)$ and $(c,d)$, respectively. (Notice that we could not apply the proposition if $\mathcal{H}_+\subset S$ or $\mathcal{H}_-\subset S$.) Since Example [\[mult_conv_ex1\]](#mult_conv_ex1){reference-type="ref" reference="mult_conv_ex1"} implies $p *_\times^n q$ is positive-rooted (and hence, real-rooted) whenever $p$ and $q$ are, this implies: $$\mathop{\mathrm{minroot}}(p) \cdot \mathop{\mathrm{minroot}}(q) \leq \mathop{\mathrm{minroot}}(p *_\times^n q) \leq \mathop{\mathrm{maxroot}}(p *_\times^n q) \leq \mathop{\mathrm{maxroot}}(p) \cdot \mathop{\mathrm{maxroot}}(q)$$ As in the previous example, we also obtain stability properties for $*_\times^n$ as an operator in $\mathop{\mathrm{Hom}}(V(n,n),V(n))$, and not just as a polynomial convolution.
:::

Using similar techniques, we can also circumvent the issue that arises from the fact that $\partial_x$ only preserves weak stability.

::: example
[]{#deriv_ex label="deriv_ex"} For fixed $n \geq 1$, consider the operator $\partial_x \in \mathop{\mathrm{Hom}}(V(n),V(n-1))$. We compute: $$\mathop{\mathrm{Symb}}(\partial_x) = \partial_x[(zy-xw)^n] = -nw(zy-xw)^{n-1} = \mathop{\mathrm{Hmg}}_{(n,n-1)}\left[-n(z-x)^{n-1}\right]$$ For any $a,b \in \mathbb{R}$ such that $a<b$, it is straightforward to see that $\mathop{\mathrm{Symb}}(\partial_x)$ is $(C \times B)$-stable for $C := \mathcal{H}_-\cup (a,b)$ and $B := \overline{\mathcal{H}_+} \setminus (a,b)$, where the variables are ordered $(z,w),(x,y)$. (Notice that this does not hold when $\infty \in C$, due to the $w$ factor in the symbol.) Since $(C,B)$ is a disjoint Grace pair, the Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"} implies $\partial_x$ preserves strong $B$-stability.

With this, let $f \in \mathbb{C}^n[x]$ be a $\mathcal{H}_+$-stable polynomial of degree $1 \leq m \leq n$, and let $p \in V(m)$ be its degree-$m$ homogenization. Then $p$ has no roots at infinity, and therefore there exists $a < b$ such that $p$ is $\big(\overline{\mathcal{H}_+} \setminus (a,b)\big)$-stable. The previous discussion implies $\partial_x p$ is $\big(\overline{\mathcal{H}_+} \setminus (a,b)\big)$-stable, and in particular $\partial_x p$ is $\mathcal{H}_+$-stable. Since $\partial_x$ commutes with homogenization, this also implies $\partial_x f$ is $\mathcal{H}_+$-stable.
:::

Other issues related to weak stability preservation can be dealt with in a similar way, by considering stability regions with small intervals in $\overline{\mathbb{R}}$ about $\infty$ attached. More generally though, the Borcea-Brändén characterization ends up being a corollary of Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}, which we discuss and demonstrate now.
