---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-023-74-ray-and-interval-stability
section_title: "Ray and Interval Stability"
section_number: 7.4
pages: 26-31
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.723
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#Jops_subsect label="Jops_subsect"}

We now apply the above results to projectively convex regions of the form $\mathcal{H}_+\cup J^c$, where $J \subset \overline{\mathbb{R}}$ is some connected set. From this, we obtain a classification of operators which both preserve strong $J$-rootedness and weak real-rootedness (a polynomial $p \in V(n)$ is $J$-rooted if all its roots lie in $J$). This of course does not completely solve the open problem of providing a classification of interval- and ray-stability preserving operators (see, e.g., [@bba]). However, it does seem to be the natural corollary obtained by applying proof methods similar to that of [@bb1].

That said, we now proceed to prove the main result of this subsection, Theorem [\[Jops_graces\]](#Jops_graces){reference-type="ref" reference="Jops_graces"}. We first start with a short-hand definition in order to simplify the proof.

::: definition
Fix $\lambda,\alpha \in \mathbb{N}_0^m$ and a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ such that $T$ restricts to a real linear operator and preserves weak real-stability. We say $T$ is *degenerate* if it satisfies condition $(ii)(c)$ of Corollary [\[bb_Rops\]](#bb_Rops){reference-type="ref" reference="bb_Rops"}.
:::

We now prove two lemmas. The first is straightforward, but rather interesting in its own right.

::: lemma
[]{#conv_lemma label="conv_lemma"} Fix a closed bounded interval $J \subset \mathbb{R}$ and a subspace $W \subseteq V_\mathbb{R}(n)$ consisting of weakly real-rooted polynomials. Let $S \subseteq W$ denote the subset of top-degree monic $J$-rooted polynomials. There exist $p,q \in S$ such that $p \ll q$ and $S$ is the convex hull of $p$ and $q$.
:::

::: proof
*Proof.* Lemma [\[dim_lemma\]](#dim_lemma){reference-type="ref" reference="dim_lemma"} implies $W$ is of dimension at most two, and so then Lemma [\[total_order_lemma\]](#total_order_lemma){reference-type="ref" reference="total_order_lemma"} implies the relation $\ll$ is a total order on $S$. Applying the root ordering property of Lemma [\[total_order_lemma\]](#total_order_lemma){reference-type="ref" reference="total_order_lemma"}, the closedness of $S$ implies there are $p,q \in S$ such that $p \ll q$ and $p \ll r \ll q$ for all $r \in S$. Basic sign arguments and the fact that $S$ is contained in the span of $\{p,q\}$ then imply $S$ is the the convex hull of $\{p,q\}$. ◻
:::

The second lemma is perhaps less straightforward in terms of proof, but follows from the following intuitive idea: an open ball in some complex subspace of polynomials yields, roughly speaking, an open ball of zeros.

::: lemma
Fix $n,m \in \mathbb{N}_0$ and a linear operator $T \in \mathop{\mathrm{Hom}}(V(n),V(m))$ which restricts to a real linear operator and preserves weak real-rootedness. If there exist some $\overline{\mathcal{H}_+}$-stable $p_0 \in V(n)$ and some $(x_0:y_0) \in \overline{\mathbb{R}}$ such that $T(p_0)(x_0,y_0) = 0$, then one of the following holds:

1.  $T(p_0)$ is real-rooted or identically zero.

2.  $T(p)(x_0,y_0) = 0$ for all $p \in V(n)$.
:::

::: proof
*Proof.* Let $q_0,r_0 \in V_\mathbb{R}(m)$ be such that $T(p_0) = q_0 + ir_0$. Also suppose that $T(p_0) \not\equiv 0$ and that $(b)$ does not hold, and let $p_1$ be such that $T(p_1)(x_0,y_0) \neq 0$. WLOG, we may also assume $p_1 \in V_\mathbb{R}(n)$ by considering its real or imaginary part. We will now prove that $T(p_0)$ must be real-rooted.

First, suppose further that $T(p_0)$ has a multiple root at $(x_0,y_0)$. For small fixed $\epsilon$, $p_0 + \epsilon p_1$ is $\overline{\mathcal{H}_+}$-stable and so Lemma [\[rs_lemma\]](#rs_lemma){reference-type="ref" reference="rs_lemma"} implies $T(p_0 + \epsilon p_1)$ is either $\mathcal{H}_+$-stable or $\mathcal{H}_-$-stable. Hermite-Biehler (Proposition [\[hermite-biehler\]](#hermite-biehler){reference-type="ref" reference="hermite-biehler"}) then implies $q_0 + \epsilon T(p_1)$ and $r_0$ have interlacing roots. However, since $T$ restricts to a real linear operator, it must be that $q_0$ and $r_0$ both have a multiple root at $(x_0,y_0)$. The fact that $q_0 + \epsilon T(p_1)$ has no root at $(x_0,y_0)$ yields a contradiction, as interlacing is then impossible.

Otherwise, $T(p_0)$ has a simple root at $(x_0,y_0)$. Define $R \in \mathop{\mathrm{Hom}}(V(n),V(1))$ via $R := d_\phi^{n-1} \circ T$, where $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$ is such that $(x_0:y_0)$ is the pole of $\phi$. We have that $R(p_0)(x_0,y_0) = 0$, but $R(p_0) \not\equiv 0$ since the root is simple. Further, $R(p_1)(x_0,y_0) \neq 0$, and therefore $R$ is a surjective continuous linear map. By the open mapping theorem, there exists a one-real-dimensional curve $\Gamma \subset V(n)$ through $p_0$, for which $R(\Gamma)$ contains elements with root in $\mathcal{H}_+$ on one side of $p_0$ (call this side $\Gamma_+$) and elements with root in $\mathcal{H}_-$ on the other side (call it $\Gamma_-$). So by Laguerre's theorem (Proposition [\[laguerre_prop\]](#laguerre_prop){reference-type="ref" reference="laguerre_prop"}), elements of $T(\Gamma_+)$ have some roots in $\mathcal{H}_+$ and elements of $T(\Gamma_-)$ have some roots in $\mathcal{H}_-$. Since polynomials near $p_0$ are $\overline{\mathcal{H}_+}$-stable, Lemma [\[rs_lemma\]](#rs_lemma){reference-type="ref" reference="rs_lemma"} implies elements of $T(\Gamma \cap B_\epsilon(p_0))$ are all $\mathcal{H}_+$-stable or $\mathcal{H}_-$-stable for some small ball $B_\epsilon(p_0)$ about $p_0$. So elements of $T(\Gamma_+ \cap B_\epsilon(p_0))$ are $\mathcal{H}_-$-stable and elements of $T(\Gamma_- \cap B_\epsilon(p_0))$ are $\mathcal{H}_+$-stable, and therefore $T(p_0)$ is real-rooted. ◻
:::

We now prove our main result on ray- and interval-stability preserving operators. First we state the theorem for closed bounded output intervals, as it clarifies the proof quite a bit. We will then extend the result to other connected regions in $\overline{\mathbb{R}}$.

::: theorem
[]{#Jops_graces label="Jops_graces"} Fix $n,m \in \mathbb{N}_0$ and a linear operator $T \in \mathop{\mathrm{Hom}}(V(n),V(m))$ which restricts to a real linear operator. Further, let $I \subseteq \mathbb{R}$ be any interval, and let $J \subset \mathbb{R}$ be any closed bounded interval. The following are equivalent.

1.  $T$ preserves weak real-rootedness and maps $I$-rooted polynomials to nonzero $J$-rooted polynomials.

2.  One of the following holds:

    1.  $\mathop{\mathrm{Symb}}(T)$ is $(\mathcal{H}_-\cup I) \times (\overline{\mathcal{H}_+} \setminus J)$-stable.

    2.  $\mathop{\mathrm{Symb}}(T)$ is $(\mathcal{H}_-\cup I) \times (\overline{\mathcal{H}_-} \setminus J)$-stable.

    3.  $T$ has image of dimension at most two, and is of the form $$T: p \mapsto q \cdot \psi_1(p) + r \cdot \psi_2(p)$$ where $q,r \in V_\mathbb{R}(m)$ are top-degree monic and weakly $J$-rooted such that $q \ll r$, and $\psi_1$ and $\psi_2$ are real linear functionals such that $\psi_1(p) \cdot \psi_2(p) \geq 0$ (not both zero) holds for any $I$-rooted $p$.
:::

::: proof
*Proof.* $(i) \Rightarrow (ii)$. Suppose $T$ is nondegenerate. So, $\mathop{\mathrm{Symb}}(T)$ is either $(\mathcal{H}_-\times \mathcal{H}_+)$-stable or $(\mathcal{H}_-\times \mathcal{H}_-)$-stable by Corollary [\[bb_Rops\]](#bb_Rops){reference-type="ref" reference="bb_Rops"}. By Lemma [\[bb_Rlink\]](#bb_Rlink){reference-type="ref" reference="bb_Rlink"}, either $T$ maps $\overline{\mathcal{H}_+}$-stable evaluation symbols entirely to nonzero $\mathcal{H}_+$-stable polynomials or entirely to nonzero $\mathcal{H}_-$-stable polynomials. If for some $(z_0:w_0) \in \mathcal{H}_-$ we have that $T[(w_0x-z_0y)^n]$ has a root in $\overline{\mathbb{R}}$, then we can apply the previous lemma. If condition $(a)$ of the lemma holds, then $T[(w_0x-z_0y)^n]$ is real-rooted or identically zero. The proof of Lemma [\[bb_Rlink\]](#bb_Rlink){reference-type="ref" reference="bb_Rlink"} then implies $T$ is degenerate, a contradiction. Otherwise condition $(b)$ of the lemma holds, and therefore the real roots of $T[(w_0x-z_0y)^n]$ must be in $J$. So in fact, $T$ maps $\overline{\mathcal{H}_+}$-stable evaluation symbols entirely to nonzero $(\overline{\mathcal{H}_+} \setminus J)$-stable polynomials or entirely to nonzero $(\overline{\mathcal{H}_-} \setminus J)$-stable polynomials. Finally, $T$ maps $I$-rooted evaluation symbols to nonzero $(\overline{\mathcal{H}_+} \setminus J)$-stable and $(\overline{\mathcal{H}_-} \setminus J)$-stable polynomials by assumption. The complex characterization (Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}) then implies $(a)$ or $(b)$.

Otherwise, $T$ is degenerate and $T[V_\mathbb{R}(n)]$ consists entirely of real-rooted polynomials. Condition $(c)$ follows from Lemma [\[conv_lemma\]](#conv_lemma){reference-type="ref" reference="conv_lemma"}.

$(ii) \Rightarrow (i)$. By Corollary [\[bb_Rops\]](#bb_Rops){reference-type="ref" reference="bb_Rops"}, $T$ preserves weak real-rootedness. If $(a)$ or $(b)$ holds, then the complex characterization (Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}) and the fact that $T$ restricts to a real operator imply $T$ maps $I$-rooted polynomials to nonzero $J$-rooted polynomials.

Otherwise $(c)$ holds. For any real-rooted $p$, let $\lambda(p)$ and $\mu(p)$ denote the largest and smallest roots of $p$, respectively. Since $q,r$ are top-degree monic, every convex combination of $q$ and $r$ has all its roots in the interval $[\mu(q), \lambda(r)] \subseteq J$. Since $\psi_1 \cdot \psi_2 \geq 0$ (not both zero) holds for $I$-rooted polynomials, we have that $T$ maps $I$-rooted polynomials to nonzero $J$-rooted polynomials. ◻
:::

Notice that this result immediately holds for other closed, connected regions $I,J \subset \overline{\mathbb{R}}$ by the action of some appropriate $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{R})$. In fact, one can directly apply the action of $\phi$ to conditions $(ii)(a)$ and $(ii)(b)$, due to the fact that our definition of the "universal" symbol works for any projectively convex regions. The only significant change comes when applying $\phi$ to condition $(ii)(c)$. Further, the only issue with $(ii)(c)$ as it is written now is the requirement that $p_1$ and $p_2$ be top-degree monic polynomials. Having zeros at infinity, for instance, means that a polynomial cannot ever be top-degree monic (as the leading homogeneous coefficient is 0). There are ways to rewrite $(ii)(c)$ that avoids this problem, but it is probably more intuitive to state the result as above and apply $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{R})$.

Additionally, the result holds for open and half-open bounded intervals $J \subset \mathbb{R}$, with a bit of tweaking to condition $(ii)(c)$. (Again, the universality of the symbol means that $(ii)(a)$ and $(ii)(b)$ remain unchanged.) We state this in the following, where the action of $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{R})$ can be used to obtain similar results regarding open and half-open connected regions in $\overline{\mathbb{R}}$.

::: corollary
[]{#Jops_graces_cor label="Jops_graces_cor"} The previous theorem holds when $J \subset \mathbb{R}$ is an open (or half-open) bounded interval, given the following alterations to condition $(ii)(c)$: if the image of $T$ is of dimension exactly two, then $p_1,p_2 \in V_\mathbb{R}(m)$ are top-degree monic $\overline{J}$-rooted polynomials such that the largest root of $p_1$ and the smallest root of $p_2$ are in $J$ (for $p_1 \ll p_2$), and $\psi_1 \neq 0$ (resp. $\psi_2 \neq 0$) whenever $p_2$ (resp. $p_1$) is not $J$-rooted.
:::

::: proof
*Proof.* The condition that the largest root of $p_1$ and the smallest root of $p_2$ are in $J$ (and the fact that $p_1 \ll p_2$) implies that $\alpha p_1 + \beta p_2$ is $J$-rooted for all $\alpha,\beta > 0$. Applying Lemma [\[conv_lemma\]](#conv_lemma){reference-type="ref" reference="conv_lemma"} to $\overline{J}$ completes the proof. ◻
:::

We now give a few examples. The first demonstrates the necessity of the premise that $T$ preserves weak real-rootedness.

::: example
Consider the operator $T_n: V(n) \to V(n)$ defined via: $$T_n: x^ky^{n-k} \mapsto \mathop{\mathrm{Hmg}}_n[x(x-1)(x-2)\cdots(x-k+1)]$$ By Proposition 7.31 in [@fisk2006polys], $T_n$ preserves positive-rootedness for all $n$. However, $T_2$ does not preserve real-rootedness, for example. In particular: $$T_2(x^2+2xy+y^2) = x(x-y) + 2xy + y^2 = x^2 + xy + y^2$$ We now compute the symbol of $T_2$: $$\mathop{\mathrm{Symb}}(T_2) = T_2[(xw-zy)^2] = x(x-y)w^2 - 2xzyw + z^2y^2 = \mathop{\mathrm{Hmg}}_{(2,2)}[(x-z)^2 - x]$$ Notice that for $x = -1$, we have that $(-1-z)^2 + 1$ is not real rooted. Therefore, $\mathop{\mathrm{Symb}}(T_2)$ is neither $(\mathcal{H}_-\cup (0,\infty)) \times (\overline{\mathcal{H}_+} \setminus (0,\infty))$-stable nor $(\mathcal{H}_-\cup (0,\infty)) \times (\overline{\mathcal{H}_-} \setminus (0,\infty))$-stable when the variables are ordered $(z,w),(x,y)$. That is, the operator $T_2$ does not contradict the previous theorem.
:::

In the second example, we demonstrate root preservation properties of $f(\partial_x)$ for real-rooted $f$. These are standard results of the classical theory: see, e.g., Corollary 5.4.1 in [@rahman2002anthpoly].

::: example
For any real-rooted $f \in \mathbb{C}[x]$, consider the operator $D_f \in \mathop{\mathrm{Hom}}(V(n),V(n))$ defined via $D_f: g \mapsto f(y\partial_x)g$ (i.e., the homogenized version of $f(\partial_x)$). To determine properties of this operator, we first write: $$f(y\partial_x) = c_0 \prod_{j=1}^m (y\partial_x - \alpha_j)$$ Here, the $\alpha_j \in \mathbb{R}$ are the roots of $f$. Next, we compute the symbol of $(y\partial_x - \alpha_j) \in \mathop{\mathrm{Hom}}(V(n),V(n))$ for $j \in [m]$: $$\begin{split}
            \mathop{\mathrm{Symb}}(y\partial_x - \alpha_j) &= (y\partial_x - \alpha_j)(zy-xw)^n \\
                &= -(\alpha_j (zy-xw) + nwy)(zy-xw)^{n-1} \\
                &= \mathop{\mathrm{Hmg}}_{(n,n)}\left[-(\alpha_j(z-x)+n)(z-x)^{n-1}\right]
        \end{split}$$ We now have three cases, depending on the sign of $\alpha_j$. If $\alpha_j > 0$, we have that $\mathop{\mathrm{Symb}}(y\partial_x - \alpha_j)$ is both $(\mathcal{H}_-\cup [a,\infty]) \times (\overline{\mathcal{H}_+} \setminus [a,\infty])$-stable and $(\mathcal{H}_-\cup [-\infty,a]) \times (\overline{\mathcal{H}_+} \setminus [-\infty,a+\frac{n}{\alpha_j}])$-stable for any $a \in \mathbb{R}$. (As usual, we order the variables $(z,w),(x,y)$.) Using Theorem [\[Jops_graces\]](#Jops_graces){reference-type="ref" reference="Jops_graces"} and the discussion following the proof, this implies $(y\partial_x - \alpha_j)$ preserves $[a,\infty]$-rootedness and maps $[-\infty,a]$-rooted polynomials to $[-\infty,a+\frac{n}{\alpha_j}]$-rooted polynomials. So, if the (non-infinite) roots of $g$ are contained in the interval $[b,c]$, then the (non-infinite) roots of $(y\partial_x - \alpha_j)g$ are contained in the interval $[b,c+\frac{n}{\alpha_j}]$.

If $\alpha_j < 0$, we have that $\mathop{\mathrm{Symb}}(y\partial_x - \alpha_j)$ is both $(\mathcal{H}_-\cup [a,\infty]) \times (\overline{\mathcal{H}_+} \setminus [a+\frac{n}{\alpha_j},\infty])$-stable and $(\mathcal{H}_-\cup [-\infty,a]) \times (\overline{\mathcal{H}_+} \setminus [-\infty,a])$-stable for any $a \in \mathbb{R}$. As above, this implies $(y\partial_x - \alpha_j)$ preserves $[-\infty,a]$-rootedness and maps $[a,\infty]$-rooted polynomials to $[a+\frac{n}{\alpha_j},\infty]$-rooted polynomials. So, if the (non-infinite) roots of $g$ are contained in the interval $[b,c]$, then the (non-infinite) roots of $(y\partial_x - \alpha_j)g$ are contained in the interval $[b+\frac{n}{\alpha_j},c]$.

Finally for $\alpha_j = 0$, the operator $(y\partial_x - \alpha_j) = y\partial_x$ weakly preserves any interval in which the (non-infinite) roots reside. The main difference for this case is that $y\partial_x$ only preserves weak real-rootedness. Combining these three cases, we are lead to the following root preservation property of $f(\partial_x): \mathbb{C}^n[x] \to \mathbb{C}^n[x]$. Let $\alpha_j^+$ and $\alpha_j^-$ be the positive and negative roots of $f$, respectively. We then have the following, which refers to non-infinite roots: $$f(\partial_x): [b,c]\text{-rooted} \to \left[b + \sum_j \frac{n}{\alpha_j^-}, c + \sum_j \frac{n}{\alpha_j^+}\right]\text{-rooted}$$ If $f$ has zeros at 0, then $f(\partial_x)$ may map some nonzero $[b,c]$-rooted polynomials to 0. Otherwise, $f(\partial_x)$ is invertible on $\mathbb{C}^n[x]$.
:::

# Acknowledgements

We would like to thank Nick Ryder for many graduate school conversations on stable polynomials and linear stability preservers. We would also like to thank an anonymous referee for a thorough reading of this paper and many helpful comments.
