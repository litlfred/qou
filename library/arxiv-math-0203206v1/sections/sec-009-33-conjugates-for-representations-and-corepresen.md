---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-009-33-conjugates-for-representations-and-corepresen
section_title: "Conjugates for Representations and Corepresentations"
section_number: 3.3
pages: 17-20
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.953
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
Suppose that $(A,\Delta)$ is a discrete aqg with counit $\varepsilon$ and coinverse $S$. We now show that the semisimple tensor $*$-categories $\mathrm{Rep}_f (A,\Delta)$ and $\mathrm{Corep}_f (\hat{A},\hat{\Delta} )$ have conjugates, and provide a conjugate object for every non-zero object.

Suppose $\pi$ is a non-zero non-degenerate $*$-representation on the finite dimensional Hilbert space $K$. Let $f\in M(A)$ be as in Theorem [\[t-disc2\]](#t-disc2){reference-type="ref" reference="t-disc2"} and consider the positive operator $\pi(f^{-1})\in B(K)$. Pick any Hilbert space $\overline{K}$ and any invertible antilinear operator $J:K\rightarrow\overline{K}$ such that $J^* J=\pi (f^{-1})$. This can clearly be done. Now pick an orthonormal basis $(e_i )$ for $K$ and define linear maps $r: {\mathbb C}\rightarrow \overline{K}\otimes K$ and $\overline{r} :{\mathbb C}\rightarrow K\otimes\overline{K}$ by $$r(1)=\sum_i Je_i\otimes e_i \quad \mbox{and} \quad  \overline{r}(1)=\sum_i e_i\otimes J^{*-1}e_i,$$ respectively. Next define $$\overline{\pi}:\ A\rightarrow B(\overline{K}), \quad a \mapsto J\pi S(a^* )J^{-1}.$$ As $J$ and $J^{-1}$ both are antilinear, $\overline{\pi}(a)$ is linear and thus $\overline{\pi}(a)\in B(\overline{K})$ for all $a\in A$. By the following proposition, $\overline{\pi}$ is indeed a conjugate to $\pi$ and $r$ and $\overline{r}$ are normalized solutions of the conjugate equations for $\pi$ and $\overline{\pi}$.

::: prop
[]{#p-conj label="p-conj"} Let $(A,\Delta)$ be a discrete aqg and $\pi$ a non-zero object of $\mathrm{Rep}_f (A,\Delta)$. Then $\overline{\pi}$ is a non-zero object of $\mathrm{Rep}_f (A,\Delta)$. Moreover, the following hold:

1.  $r\in\mathrm{Hom}(\varepsilon, \overline{\pi}\times\pi )$,

2.  $\overline{r}\in\mathrm{Hom}(\varepsilon, \pi\times\overline{\pi})$,

3.  $\overline{r}^*\otimes\mathrm{id}_{\pi}\,\circ\,\mathrm{id}_{\pi}\otimes r=\mathrm{id}_{\pi}$,

4.  $r^*\otimes\mathrm{id}_{\overline{\pi}}\,\circ\,\mathrm{id}_{\overline{\pi}}\otimes
        \overline{r}=\mathrm{id}_{\overline{\pi}}$,

5.  $r^* \,\circ\,r=\overline{r}^*\,\circ\,\overline{r}$.
:::

*Proof. *Claims 3 and 4 hold for any invertible antilinear map $J$, as is easily verified. Claim 5 is simply a restatement of the fact $\mathrm{Tr} \pi(f)=\mathrm{Tr} \pi(f^{-1})$ stated in Theorem [\[t-disc2\]](#t-disc2){reference-type="ref" reference="t-disc2"}. To show that $\overline{\pi}\in \mathrm{Rep}_f (A,\Delta)$, we first note that $\overline{\pi}$ is linear (as $Ad\,J$ and $*$ are both antilinear), multiplicative and non-degenerate, thus non-zero. To see that $\overline{\pi}$ is $*$-preserving, first notice that $S(a^*)^* =S^{-1}(a)$ and $S^2 (a)=faf^{-1}$ for all $a\in A$, and then calculate $$\overline{\pi}(a)^* =J^{*-1}\pi S^{-1}(a)J^* =J\pi (f)\pi S^{-1}(a)\pi (f^{-1})J^{-1}
=J\pi S(a)J^{-1}=\overline{\pi}(a^* ),$$ for all $a\in A$.

It remains to show relations 1 and 2. We prove only the first, the second being proved similarly. Now $r\in\mathrm{Hom}(\varepsilon, \overline{\pi}\times\pi )$ simply means that $\varepsilon (a)r(1)=(\overline{\pi}\times\pi )(a)r(1)$, for all $a\in A$. By the non-degeneracy of $\pi$ it thus suffices to show that $$(\varepsilon (a)r(1),J^{*-1}e_j\otimes \pi (b^* )e_l )
=((\overline{\pi}\times\pi )(a)r(1),J^{*-1}e_j\otimes \pi (b^* )e_l )$$ for all $a,b\in A$ and all $j,l$. On the l.h.s. we have $$(\varepsilon (a)r(1),J^{*-1}e_j\otimes \pi (b^* )e_l )=\varepsilon (a)\sum_i (Je_i, J^{*-1}e_j)
   (e_i, \pi (b^* )e_l )$$ $$=\varepsilon (a)\sum_i \delta_{ij}(e_i, \pi (b^* )e_l )
=\varepsilon (a)(e_j, \pi (b^* )e_l )
=(\pi (\varepsilon (a)b )e_j, e_l ).$$ To see that the r.h.s. coincides with this expression, first write $(1\otimes b)\Delta(a)=\sum_k a_k\otimes b_k$ and notice that $$\sum_k b_k S(a_k^* )^* =\sum_k b_k S^{-1}(a_k )=m(\iota\otimes S^{-1})(\sum_k b_k\otimes a_k )
=m(\iota\otimes S^{-1})((b\otimes 1)\Delta^{op} (a))=\varepsilon (a)b.$$ Hence $$\begin{aligned}
 \lefteqn{ 
   ((\overline{\pi}\times\pi )(a)r(1),J^{*-1}e_j\otimes \pi (b^* )e_l )
=\sum_i ((\overline{\pi}\otimes\pi )\Delta(a)(Je_i\otimes e_i ),J^{*-1}e_j\otimes \pi (b^* )e_l ) } \\
 &=& \sum_i ((\overline{\pi}\otimes\pi )(1\otimes b)(\overline{\pi}\otimes\pi )\Delta(a)(Je_i\otimes e_i ),J^{*-1}e_j\otimes e_l ) \\ 
&=& \sum_i ((\overline{\pi}\otimes\pi )((1\otimes b)\Delta(a))(Je_i\otimes e_i ),J^{*-1}e_j\otimes e_l ) \\
 &=& \sum_{ik} (\overline{\pi}(a_k )Je_i \otimes\pi (b_k )e_i, J^{*-1}e_j\otimes e_l )
=\sum_{ik} (J\pi S(a_k^* )e_i \otimes\pi (b_k )e_i, J^{*-1}e_j\otimes e_l ) \\
 &=& \sum_{ik} (J\pi S(a_k^* )e_i, J^{*-1}e_j )(\pi (b_k )e_i, e_l )
=\sum_{ik} (e_j, \pi S(a_k^* )e_i )(\pi (b_k )e_i, e_l )\\
 &=& \sum_{ik} (\pi S(a_k^* )^* e_j, e_i)(\pi (b_k )e_i, e_l )
=\sum_k (\pi (b_k )\sum_i (\pi S(a_k^* )^* e_j, e_i )e_i, e_l ) \\
 &=& \sum_k (\pi (b_k )\pi S(a_k^* )^* e_j,  e_l )
=(\pi (\sum_k b_k S(a_k^* )^* )e_j,  e_l ) 
=(\pi (\varepsilon (a)b )e_j, e_l ),
\end{aligned}$$ as desired.

Note that for a discrete aqg $(A,\Delta)$, the intrinsic dimension $d(\pi)$ of an irreducible object $\pi\in \mathrm{Rep}_f (A,\Delta)$ is then given by $$d(\pi) =r^* \,\circ\,
  r=\overline{r}^*\,\circ\,\overline{r}=\mathrm{Tr}\,\pi(f)=\mathrm{Tr}\,\pi(f^{-1}).$$ In fact, the latter two expressions can be thought of as the quantum dimension of $\pi$ [@RT] and gives the intrinsic dimension for any $\pi\in\mathrm{Rep}_f (A,\Delta)$. By the Schwarz inequality for the inner product given by $\mathrm{Tr}$ it follows that if $d(\pi )$ equals the dimension of the Hilbert space on which $\pi$ acts, then $\pi (f)=1$. Thus the von Neumann extension of $(A,\Delta)$ is a Kac algebra iff the intrinsic dimension of any finite dimensional representation coincides with the dimension of the Hilbert space on which it acts.

Suppose now that $(A,\Delta)$ is a compact agq with counit $\varepsilon$ and coinverse $S$. We would like to find an expression for the conjugate unitary corepresentation $\overline{V}$ of a non-zero object $V\in \mathrm{Corep}_f (A,\Delta)$. To this end, we will use the correspondence between $\mathrm{Rep}_f(\hat{A},\hat{\Delta} )$ and $\mathrm{Corep}_f (A,\Delta)$ established in Theorem [\[t-dualcor\]](#t-dualcor){reference-type="ref" reference="t-dualcor"}. Recall that the dual $(\hat{A},\hat{\Delta})$ of $(A,\Delta)$ is a discrete aqg. Let $\hat{\varepsilon}$ denote its counit, $\hat{S}$ its coinverse, and let $\hat{f}\in M(\hat{A})$ be as in Theorem [\[t-disc2\]](#t-disc2){reference-type="ref" reference="t-disc2"}.

Let $V\in A\otimes B(K)$ be a non-zero unitary corepresentation of $(A, \Delta)$ on a finite dimensional Hilbert space $K$. Pick a finite dimensional Hilbert space $\overline{K}$ and a antilinear map $J:K\rightarrow\overline{K}$ such that $J^* J=\pi_V (\hat{f}^{-1})\in B(K)$. Given any invertible antilinear map $J$ we define a linear map $j :B(K)\rightarrow B(\overline{K})$ by $j(x)=J x^*J^{-1}$, for all $x\in B(K)$.

::: prop
Suppose $(A,\Delta)$ is a compact aqg. Let $V$ be a unitary corepresentation of $(A,\Delta)$ on a finite dimensional Hilbert space $K$ with $J^* J=\pi_V (\hat{f}^{-1})\in B(K)$. Define $\overline{V}\in A\otimes B(\overline{K})$ by $\overline{V}=(S^{-1}\otimes j)V$. Then the following hold:

1.  $V (1\otimes J^* J )=(1\otimes J^* J)(S^2\otimes \iota )V$,

2.  $\overline{V}\in \mathrm{Corep}_f (A,\Delta)$,

3.  $\overline{\pi_V}=\pi_{\overline{V}}$. (Here it is understood that the same $J: K\rightarrow\overline{K}$ is used in both constructions.)
:::

*Proof. * To prove 1., observe that $$(\omega\otimes\iota )V J^* J=\pi_V (\omega )\pi_V (\hat{f}^{-1})=\pi_V (\omega\hat{f}^{-1} )
=\pi_V (\hat{f}^{-1} )\pi_V (\hat{f}\omega\hat{f}^{-1} )$$ $$=J^* J\pi_V (\hat{S}^2 (\omega )) =J^* J (\hat{S}^2 (\omega )\otimes\iota )V
=J^* J (\omega\otimes\iota )(S^2\otimes \iota )V$$ for all $\omega\in\hat{A}$.

To prove 3., note first that $\hat{S}(\omega)(a)=\omega S(a)$ and $\omega^* (a)=\overline{\omega (S(a)^*)}$ for all $a\in A$ and $\omega\in\hat{A}$. Writing $V=\sum_k a_k\otimes x_k$ we compute $$\begin{aligned}
\sum_k \hat{S}(\omega^* )(a_k )x_k &=& \sum_k \omega^* S(a_k )x_k 
  =(\omega^*\otimes\iota )(S\otimes\iota )V =(\omega^*\otimes\iota )(V^* ) \\
  &=& \sum_k \omega^* (a_k^* )x_k^* = \sum_k \overline{\omega (S(a_k^* )^* )}x_k^*
  =\sum_k \overline{\omega S^{-1}(a_k)}x_k^*. 
\end{aligned}$$ Since $(S\otimes\iota )V =V^*$, we thus obtain $$\begin{aligned}
  \overline{\pi_V}(\omega ) &=& J\pi_V \hat{S}(\omega ^* )J^{-1}
   = J(\hat{S}(\omega^* )\otimes\iota )VJ^{-1}
   =\sum_k J(\hat{S}(\omega^* )(a_k )x_k )J^{-1}
   =\sum_k J(\overline{\omega S^{-1}(a_k )}x_k^* )J^{-1} \\
  &=& \sum_k \omega S^{-1}(a_k )Jx_k^* J^{-1} 
  =(\omega\otimes\iota)(S^{-1}\otimes j)(\sum_k a_k \otimes x_k )
  =(\omega\otimes\iota)(S^{-1}\otimes j)V =\pi_{\overline{V}} (\omega )
\end{aligned}$$ for all $\omega\in\hat{A}$, proving 3. Now 3., together with Proposition [\[p-functP\]](#p-functP){reference-type="ref" reference="p-functP"} and Proposition [\[p-conj\]](#p-conj){reference-type="ref" reference="p-conj"}, imply 2., completing the proof.

This suggests the following proposition, which is a formulation more intrinsic to the category $\mathrm{Corep}_f (A,\Delta)$.

::: prop
Let $(A,\Delta)$ be a compact aqg and $V\in \mathrm{Corep}_f (A,\Delta)$ be non-zero. Pick a finite dimensional Hilbert space $\overline{K}$ and any antilinear map $J:K\rightarrow\overline{K}$ such that $V (1\otimes J^* J )=(1\otimes J^* J)(S^2\otimes \iota )V$. Then $\overline{V}\in A\otimes B(\overline{K})$ given by $\overline{V}=(S^{-1}\otimes j)V$ belongs to $\mathrm{Corep}_f (A,\Delta)$. It is a conjugate of $V$ with normalized solutions $r\in\mathrm{Hom}(1\otimes 1,\overline{V}\times V )$, $\overline{r}\in\mathrm{Hom}(1\otimes 1, V\times\overline{V})$ of the conjugate equations for $V$ and $\overline{V}$ given by $$r(1)=\sum_i Je_i\otimes e_i\  \  \  \  \ and \  \  \  \  \overline{r}(1)=\sum_i e_i\otimes
   J^{*-1}e_i.$$
:::

*Proof. *The irreducible case follows from Proposition [\[p-conj\]](#p-conj){reference-type="ref" reference="p-conj"}, Theorem [\[t-dualcor\]](#t-dualcor){reference-type="ref" reference="t-dualcor"} and the fact that $J^* J$ is the unique (up to a positive scalar) positive operator in $B(K)$ with the property $V (1\otimes J^* J )=(1\otimes J^* J)(S^2\otimes \iota )V$ [@woro1; @RT]. We content ourselves with proving one of the least obvious parts of the proposition, namely that $r$, defined above, belongs to $\mathrm{Hom}(1\otimes 1,\overline{V}\times V )$. In other words we must show that $r(\omega\otimes\iota )(1\otimes 1)=(\omega\otimes\iota\otimes\iota )(\overline{V}\times V)r$ or $\omega (1)r(1)=(\omega\otimes\iota\otimes\iota )(\overline{V}\times V)r(1)$ for all $\omega\in\hat{A}$. Write $V=\sum_k a_k\otimes x_k \in A\otimes B(K)$, so $\overline{V}=\sum_k S^{-1}(a_k )\otimes Jx_k^* J^{-1}$. For any $\omega\in\hat{A}$ and any elements $e_j, e_r$ in the chosen orthonormal basis for $K$, we then get $$\begin{aligned}
 \lefteqn{
  ((\omega\otimes\iota\otimes\iota )(\overline{V}\times V)r(1),J^{*-1} e_j\otimes e_r ) 
  =\sum_i ((\omega\otimes\iota\otimes\iota )(\overline{V}_{12}V_{13})(Je_i\otimes e_i ),J^{*-1}
   e_j\otimes e_r ) } \\ 
&=& \sum_{ikl} \omega(S^{-1}(a_k )a_l )(Jx_k^* J^{-1} Je_i, J^{*-1}e_j )(x_l e_i, e_r )
\quad=\quad\sum_{ikl} \omega(S^{-1}(a_k )a_l )(Jx_k^* e_i, J^{*-1}e_j )(x_l e_i, e_r ) \\
&=& \sum_{ikl} \omega(S^{-1}(a_k )a_l )( e_j, x_k^* e_i )(x_l e_i, e_r )
\quad=\quad\sum_{ikl} \omega(S^{-1}(a_k )a_l )(x_k  e_j, e_i )(x_l e_i, e_r ) \\
&=& \sum_{kl} \omega(S^{-1}(a_k )a_l )(x_l \sum_i (x_k  e_j, e_i )e_i, e_r )
\quad=\quad\sum_{kl} \omega(S^{-1}(a_k )a_l )(x_l x_k  e_j, e_r ) \\
&=& \sum_{kl} \omega S^{-1}(S(a_l )a_k )(x_l x_k  e_j, e_r )
\quad=\quad\sum_{kl} \omega S^{-1}(a_l^* a_k )(x_l^* x_k  e_j, e_r ) \\
&=& (\omega S^{-1}\otimes \omega_{ e_j, e_r})(V^* V)
\quad=\quad(\omega\otimes \omega_{ e_j, e_r})(1\otimes 1 )
\quad=\quad\omega (1)( e_j, e_r ) \\
&=& \sum_i \omega (1)(Je_i, J^{*-1}e_j )(e_i, e_r ) 
\quad=\quad(\omega (1)r(1), J^{*-1}e_j \otimes e_r ),
\end{aligned}$$ where $$\omega_{ e_j, e_r}:\ B(K)\rightarrow{\mathbb C}, \quad x\mapsto (xe_j, e_r ).$$ Thus $$(\omega\otimes\iota\otimes\iota )(\overline{V}\times V)r(1)=\omega (1)r(1),$$ completing the proof.

::: rema
In the last two results, the conjugates can be expressed alternatively in terms of the unitary antipode $R$ and an antiunitary $J$ [@BMT].
:::
