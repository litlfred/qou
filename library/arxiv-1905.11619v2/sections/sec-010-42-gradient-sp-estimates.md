---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-010-42-gradient-sp-estimates
section_title: "Gradient-Sp estimates"
section_number: 4.2
pages: 11-16
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.779
latex_coverage_ratio: 0.956
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
Let $[n]$ be the set $\{ 1, \ldots, n \}$, with $n\in \mathbb{N}$. $[n]$ has its natural order. We will consider the operator $\Psi^{a,b}$ associated to the Ornstein-Uhlenbeck semigroup. We will need a formula for products of Wick words to be able to work with this operator. We will follow Effros-Popa [@EffrosPopa] (see also [@DeyaSchott]).

::: dfn
Let $n_1,\dots,n_k$ be natural numbers. By $P^{\leqslant 2}(n_1\otimes\dots\otimes n_k)$ we denote the set of partitions of the set $[n]$, where $n=n_1+\dots+n_k$, with blocks of size at most two, such that there is no pairing inside the sets $\{1,\dots,n_1\}, \{n_1+1,\dots,n_1+n_2\},\dots, \{n-n_k+1,\dots, n\}$. For $\pi \in P^{\leqslant 2}(n_1\otimes\dots\otimes n_k)$ we will define the number of crossings $cr (\pi)$. Let $\pi = (l_1,r_1),\dots, (l_{m}, r_{m}), s_1,\dots, s_l$ be the blocks of the partition, so $2m+l=n$; we will denote by $P(\pi)$ the set of pairs and by $S(\pi)$ the set of singletons. We will denote by $c(\pi)$ the usual crossing number, i.e. the number of pairs $(l_i, r_i)$ and $(l_j,r_j)$ such that $l_i<l_j<r_i<r_j$. The symbol $d(\pi)$ will denote the set of degenerate crossings, i.e. the number of triples $x<y<z$ such that $(x,z)=(l_i,r_i)$ for some $i$ and $y=s_j$ for some $j$, i.e. $y$ is not paired with anything. The crossing number $cr(\pi)$ is defined to be $cr(\pi)=c(\pi) + d(\pi)$.
:::

While cumbersome to formally define, the crossing number is easy to compute, provided that we have a graphical representation of the partition available:

<figure>

</figure>

For this partition $\pi$ there are two regular crossings (i.e. $c(\pi)=2$) and $5$ degenerate crossings, so $cr(\pi)=7$.

We are now ready to state the multiplication formula for Wick words (cf. [@EffrosPopa Theorem 3.3]).

::: lem
[]{#Lem=WickProduct label="Lem=WickProduct"} Let $\bm{\xi}=\xi_1\otimes \dots\otimes\xi_n \in H^{\otimes n}$, where $n=n_1+\dots+n_k$. Let us call $\bm{\xi}_1, \dots, \bm{\xi}_k$ the tensors that arise from this decomposition of $n$, i.e. $\bm{\xi}_1= \xi_1\otimes\dots\otimes \xi_{n_1}$, $\bm{\xi}_2= \xi_{n_1+1} \otimes \dots \otimes \xi_{n_1+n_2}$, etc. We have the following formula $$\label{Eqn=WickProduct}
        W_q(\bm{\xi}_1)\dots W_q(\bm{\xi}_{k}) = \sum_{\pi \in P^{\leqslant 2}(n_1\otimes\dots\otimes n_k)}
    q^{cr(\pi)}\left(\prod_{(l,r)\in P(\pi)} \langle  I\xi_l, \xi_r \rangle\right)  W_q(\bm{\xi}_{S(\pi)}),$$ where $\bm{\xi}_{S(\pi)}:= \xi_{s_1}\otimes\dots\otimes \xi_{s_l}$ if $S(\pi)=\{s_1<s_2<\dots< s_l\}$.
:::

This formula will be instrumental in the proof of the next proposition.

::: prop
[]{#Prop=GradientQComp label="Prop=GradientQComp"} Take operators in $\mathcal{A}_q$ of the form $$a = W_q(\bm{\xi}) = W_q(\xi_1 \otimes \ldots \otimes \xi_n), b = W_q(\bm{\eta}) = W_q(\eta_1 \otimes \ldots \otimes \eta_k), x = W_q(\bm{\mu}) = W_q(\mu_1 \otimes \ldots \otimes \mu_m ),$$ where each $\xi_i, \eta_i, \mu_i \in H$; define also $\bm{v}:=\bm{\xi}\otimes \bm{\mu}\otimes \bm{\eta}$. Then we have $$\begin{aligned}
\label{Eqn=Laplaceformula}
    &\Delta(axb)- \Delta(ax)b + a \Delta(x) b - a\Delta(xb) \\
&= -2\sum_{\pi \in P^{\leqslant 2}(n\otimes m \otimes k)} \left|(l,r)\in P(\pi): l\in [n], r\in[k]\right|q^{cr(\pi)}    \left(\prod_{(l,r)\in P(\pi)} \langle  Iv_l, v_r \rangle\right) W_q(\bm{v}_{S(\pi)}). \notag
    
\end{aligned}$$
:::

::: proof
*Proof.* We determine the four summands in $$\label{Eqn=DeltaFour}
    \Delta(axb) + a \Delta(x) b - \Delta(ax)b - a \Delta(xb).$$ Note that the formula for a triple product from the Lemma [\[Lem=WickProduct\]](#Lem=WickProduct){reference-type="ref" reference="Lem=WickProduct"} can be obtained by applying the formula for double products twice. It means that we can compute $axb$ as either $(ax)b$ or $a(xb)$. The fact that the crossings that we compute on the way add up to the crossing number of the whole partition is not hard to check, but not immediate. For instance, if we compute $axb$ as $(ax)b$, then first we get a sum over partitions of $n\otimes m$ and then over partitions of $(n+m)\otimes k$, where you remove the nodes from $[n+m]$ that have already been paired; you have to check that the sum of the crossing numbers of these partitions is equal to the crossing number of the resulting partition of $n\otimes m \otimes k$.

Once we have this observation, it is not hard to arrive at the formula. Indeed, each of the four terms in [\[Eqn=DeltaFour\]](#Eqn=DeltaFour){reference-type="eqref" reference="Eqn=DeltaFour"} will feature a sum as in the formula for a triple product of Wick words, but with coefficients coming from the Laplacian. In case of $\Delta(axb)$ the coefficient is equal to $n+m+k - 2|P(\pi)|$. For $\Delta(ax)b$ the coefficient is equal to $n+m - 2|\{(l,r)\in P(\pi): l\in[n], r\in [m]\}|$. The term $a\Delta(x) b$ just yields $m$. The last one, $a\Delta(xb)$, produces $m+k - 2|\{(l,r)\in P(\pi): l\in[m], r\in[k]\}|$. If we compute $\Delta(axb) - \Delta(ax)b + a\Delta(x)b -a\Delta(xb)$ then the result is $-2|\{(l,r)\in P(\pi): l\in [n], r\in [k]\}|$. Indeed, the pairings between $[n]$ and $[m]$ are accounted for by $\Delta(ax)b$, the ones between $[m]$ and $[k]$ by $a\Delta(xb)$, and only pairings between $[n]$ and $[k]$ are left. ◻
:::

We now have a formula for $\Psi^{a,b}(x)$. In order to estimate the $\mathcal{S}_p$-norm of this map, we will estimate separately the $\mathcal{S}_p$-norms of $\Psi^{a,b}$ restricted to $H_q^{\otimes m}$ for each $m\geqslant 0$. Recall that on an $N$-dimensional Hilbert space we can estimate the $\mathcal{S}_p$-norm by the operator norm, namely $\|T\|_{p} \leqslant N^{\frac{1}{p}} \|T\|$. Therefore we will be concerned only with the operator norm of $\Psi^{a,b}$ restricted to $H^{\otimes m}$.

::: prop
[]{#Prop=Normestimate label="Prop=Normestimate"} Let $\bm{\xi}:=\xi_1\otimes\dots\otimes\xi_n \in H^{\otimes n}$, $\bm{\eta}:=\eta_1\otimes\dots\otimes \eta_n \in H^{\otimes k}$ and consider $a:=W(\bm{\xi})$ and $b:=W(\bm{\eta})$. Then the norm of $\Psi^{a,b}$ restricted to $H_q^{\otimes m}$ can be estimated as follows $$\|\Psi^{a,b}_{|H_q^{\otimes m}}\| \leqslant C(q, \bm{\xi}, \bm{\eta}, \dim(H) ) |q|^{m}.$$
:::

In order to obtain useful estimates, we need to replace the formula [\[Eqn=WickProduct\]](#Eqn=WickProduct){reference-type="eqref" reference="Eqn=WickProduct"} by a new one, which takes into account the $q$-deformed inner products. We will only consider the case of $2$ or $3$ Wick words for simplicity. We will need operators $R_{n,k}^{\ast}\colon H^{\otimes n+k} \to H^{\otimes n+k}$ given by $$R_{n,k}^{\ast}(v_1\otimes \dots \otimes v_n) = \sum_{A\subset [n+k]: |A|=n} q^{i(A)} v_{A}\otimes v_{[n]\setminus A},$$ where $i(A) = \sum_{l=1}^{n} (i_{l}-l)$ if $A=\{i_1<i_2<\dots < i_{n}\}$; one can interpret this number as the cost of moving elements of $A$ to the left of $[n+k]$ or, equivalently, cost of moving its complement to the right. Now we can rewrite the formula for the double product of Wick words.

::: lem
For ($\bm{\mu}=\mu_1\otimes\dots\otimes \mu_m$ and $\bm{\eta}=\eta_1\otimes \dots \otimes \eta_k$) we have $$\label{Eqn=NewWickproduct}
W(\bm{\mu})W(\bm{\eta})\Omega = \sum_{j=0}^{m\wedge k} ({\rm Id}_{m-j}\otimes m_j \otimes {\rm Id}_{k-j})(R_{m-j,j}^{\ast}(\bm{\mu})\otimes R_{j,k-j}^{\ast}(\bm{\eta})),$$ where $m_j: H_q^{\otimes j} \otimes H_q^{\otimes j} \to \mathbb{C}$ is the inner product pairing given by $m_j(v\otimes w) = \langle Iv, w\rangle$.
:::

::: proof
*Proof.* Note that in Lemma [\[Lem=WickProduct\]](#Lem=WickProduct){reference-type="ref" reference="Lem=WickProduct"} the crossings of partitions come from two sources; from pairing a subset of $[m]$ with a subset of $[k]$ (the degenerate crossings) and from crossings inside these subsets. If you fix the subsets and sum over all partitions that pair these two subsets, the crossings can be incorporated into the definition of the $q$-deformed inner product, and the numbers $i(A)$ appearing in the definition of $R_{n,k}^{\ast}$ count exactly the number of degenerate crossings. ◻
:::

We can iterate this to obtain a formula for $W(\bm{\xi})W(\bm{\mu})W(\bm{\eta})$. But if we do not introduce a simpler notation, it will get very complicated. We will start from an element of a triple tensor product $H^{\otimes n}\otimes H^{\otimes m} \otimes H^{\otimes k}$. One thing that we will have to do is to apply inner product pairing between any two of them, and we need a notation for that. So we will use the notation $m_{j}^{ab}$ to denote the pairing of $H^{\otimes j}$ from between the $a$-th and $b$-th space, e.g. $m_{j}^{13}$ will first split $H^{\otimes n} \otimes H^{\otimes m} \otimes H^{\otimes k}$ into $H^{\otimes n-j}\otimes H^{\otimes j} \otimes H^{\otimes m} \otimes H^{\otimes j} \otimes H^{\otimes k-j}$ and then pair the two $H^{\otimes j}$ spaces. Another thing is that operators $R_{n,k}^{\ast}$ only split the tensor power into two factors, but we will have to do it again, so we need a notation for that as well. The defining property of operators $R_{n,k}^{\ast}$ is $P_q^{n+k}= (P_q^{n}\otimes P_q^{k}) R_{n,k}^{\ast}$ (cf. [@Ilona Lemma 5]). It motivates the following definition.

::: dfn
We define the operator $R_{n,k,l}^{\ast}\colon H^{\otimes n+k+l}\to H^{\otimes n+k+l}$ to be the unique operator such that $P_q^{n+k+l} = (P_q^{n}\otimes P_q^{k}\otimes P_q^{l})R_{n,k,l}^{\ast}$.
:::

Later on we will have to use boundedness of these operators. In order to achieve that goal we will need the following simple lemma.

::: lem
[]{#Lem=Splitting label="Lem=Splitting"} We have $$R_{n,k,l}^{\ast} = (R_{n,k}^{\ast}\otimes {\rm Id}_{l}) R_{n+k,l}^{\ast} = ({\rm Id}_n\otimes R_{k,l}^{\ast})R_{n,k+l}^{\ast}.$$
:::

::: proof
*Proof.* The equality $P_q^{n+k} = (P_q^{n}\otimes P_q^{k})R_{n,k}^{\ast}$ means exactly that $R_{n,k}^{\ast}$ is the adjoint of the 'identity' map $R_{n,k}\colon H_{q}^{\otimes n} \otimes H_q^{\otimes k} \to H_{q}^{\otimes n+k}$. By the same token $R_{n,k,l}^{\ast}$ is the adjoint of the identity map $R_{n,k,l}\colon H_q^{\otimes n}\otimes H_q^{\otimes k} \otimes H_q^{\otimes l}  \to H_q^{\otimes n+k+l}$, which can be obtained by composition $R_{n+k,l}(R_{n,k}\otimes {\rm Id}_{l})$ or $R_{n,k+l}({\rm Id}_{n} \otimes R_{k,l})$. ◻
:::

We are ready to state a new formula for a triple product.

::: prop
[]{#Prop=Tripleproduct label="Prop=Tripleproduct"} Let $\bm{\xi}\in H^{\otimes n}$, $\mu\in H^{\otimes m}$, and $\bm{\eta} \in H^{\otimes k}$. Then we have $$\label{Eqn=Tripleproduct}
W(\bm{\xi})W(\bm{\mu})W(\bm{\eta})\Omega = \sum_{j,r,s} q^{r(m-j-s)} m_{r}^{13}m_{s}^{12}m_j^{23}(R_{n-r-s,r,s}^{\ast}(\bm{\xi})\otimes R_{s,m-s-j,j}^{\ast}(\bm{\mu}) \otimes R_{j,r,k-j-r}^{\ast}(\bm{\eta}))$$
:::

::: proof
*Proof.* The first step is to apply formula [\[Eqn=NewWickproduct\]](#Eqn=NewWickproduct){reference-type="eqref" reference="Eqn=NewWickproduct"} to $W(\bm{\mu})W(\bm{\eta})$. It means that we apply the operator $\sum_{j}m_{j}(R_{m-j,j}^{\ast}\otimes R_{j,k-j}^{\ast})$ to $\bm{\mu}\otimes \bm{\eta}$. We denote the result by $\bm{\mu}\otimes_{W}\bm{\eta}=\sum_{j}\bm{\mu}\otimes_{W}^{j} \bm{\eta}$. And then we repeat the procedure to obtain a formula for the triple product, but we have to be careful at this point. If we just used the formula for a double product, we would have to apply the operator $\sum_{p} m_{p}(R_{n-p,p}^{\ast}\otimes R_{p,m+k-2j}^{\ast})$ to $\bm{\xi}\otimes (\bm{\mu}\otimes_{W}^{j}\bm{\eta})$ and sum over $j$. Now the tensors $\bm{\mu}$ and $\bm{\eta}$ are mixed and we do not want to let that happen. So we will pair a subset of $[n]$ with a subset of $[m+k-2j]$ (with some elements removed by the first pairing) but we will split the latter into parts lying in $[m]$ and $[k]$; say they have cardinalities $s$ and $r$ (so $p=r+s$). The issue is that we have to move this whole subset to the left of $[m+k-2j]$, pair with the corresponding subset of $[n]$ and compute the inner product in $H_q^{\otimes s+r}$, which is not what we want; we prefer $H_q^{\otimes s}\otimes H_q^{\otimes r}$. Because of the formula $P_q^{s+r} = (P_q^{s}\otimes P_q^r)R^{\ast}_{s,r}$, we can achieve this goal by applying $({\rm Id}_{n-r-s} \otimes R^{\ast}_{s,r})$ to $R_{n-p,p}^{\ast}(\bm{\xi})$. Note that our pairing $m$ involves a second ingredient, the complex conjugation $I$, which reverses the order of the tensor (i.e. $I(v_1\otimes\dots\otimes v_n) = Iv_n\otimes\dots\otimes Iv_1$). So we should consider the operator $I P_q^{s+r}$ instead. To make things easier, we will denote by $I^{j}$ the conjugation $I$ acting on $H^{\otimes j}$. We have to compute $I^{s+r} P_q^{s+r} = I^{s+r}(P_q^{s}\otimes P_q^r) R_{s,r}^{\ast}$. Because $I^{s+r}$ reverses the order, we get $I^{s+r}(P_q^s\otimes P_q^r)R_{s,r}^{\ast} = (I^{r}P_q^{r} \otimes I^{s}P_q^{s})R_{r,s}^{\ast}$. Thus we can write $m_{s+r} = m_r m_s (R_{r,s}^{\ast}\otimes {\rm Id}_{s+r})$. It follows that we can replace the pairing $m_{s+r}$ by $m_r m_s$ at the cost of applying ${\rm Id}_{n-r-s}\otimes R_{r,s}^{\ast}$ to $R_{n-p,p}^{\ast}(\bm{\xi})$; by Lemma [\[Lem=Splitting\]](#Lem=Splitting){reference-type="ref" reference="Lem=Splitting"} this is the same as $R^{\ast}_{n-r-s,r,s}(\bm{\xi})$.

Look now at the part coming from $\bm{\mu}\otimes_{W}^{j} \bm{\eta}$; we have a tensor of rank $s$ coming from $\bm{\mu}$ and a tensor of rank $r$ coming from $\bm{\eta}$. We have to think about the cost of moving it to the left of $[m+k-2j]$. The $\bm{\mu}$ part we can simply move to the left and it is accounted for by applying the operator $R_{s,m-j-s}^{\ast}$. The $\bm{\eta}$ part we move to the left of $[k-j]$ using the operator $R_{r,k-j-r}^{\ast}$ and then we have to move it to be adjacent to the $\bm{\mu}$ part. There are $m-j-s$ nodes that we have to cross, and the subset has cardinality $r$, so the cost is equal to $r(m-j-s)$. It means that our formula can be written as $$\sum_{j,r,s} q^{r(m-j-s)} m_{r}^{13}m_{s}^{12} (R_{m-r-s,r,s}^{\ast}(\bm{\xi})\otimes (R_{s,m-j-s}^{\ast}\otimes R_{r,k-j-r}^{\ast})(\bm{\mu}\otimes_{W}^{j}\bm{\eta})).$$ It is not yet exactly the formula [\[Eqn=Tripleproduct\]](#Eqn=Tripleproduct){reference-type="eqref" reference="Eqn=Tripleproduct"}, but it is very close to it. Recall that $\bm{\mu}\otimes_{W}^{j}\bm{\eta}$ is equal to $m_{j}(R_{m-j,j}^{\ast}(\bm{\mu})\otimes R^{\ast}_{j,k-j}(\bm{\eta}))$. So we arrive at $$(R_{s,m-j-s}^{\ast}\otimes R_{r,k-j-r}^{\ast})(m_{j}(R_{m-j,j}^{\ast}(\bm{\mu})\otimes R^{\ast}_{j,k-j}(\bm{\eta}))).$$ Note that we can either apply the pairing immediately, just like in the formula above, but we can also first apply identities on the spaces that will be paired, and apply the pairing afterwards. Thus we get $$m_j((R_{s,m-j-s}^{\ast}\otimes {\rm Id}_j)R_{m-j,j}^{\ast}(\bm{\mu}) \otimes ({\rm Id}_j\otimes R_{r,k-j-r}^{\ast})R_{j,k-j}^{\ast}(\bm{\eta})).$$ By Lemma [\[Lem=Splitting\]](#Lem=Splitting){reference-type="ref" reference="Lem=Splitting"}, we get $(R_{s,m-j-s}^{\ast}\otimes {\rm Id}_j)R_{m-j,j}^{\ast} = R_{s,m-j-s,j}^{\ast}$ and $({\rm Id}_j\otimes R_{r,k-j-r}^{\ast})R_{j,k-j}^{\ast}= R_{j,r,k-j-r}^{\ast}$. In order to finish the proof, it suffices to add the decoration $23$ to $m_j$ to make it $m_j^{23}$, which exactly matches the formula [\[Eqn=Tripleproduct\]](#Eqn=Tripleproduct){reference-type="eqref" reference="Eqn=Tripleproduct"}. ◻
:::

::: rmk
In order to pass to the formula for $\Psi^{a,b}(\bm{\mu})$ we just need to multiply each summand in [\[Eqn=Tripleproduct\]](#Eqn=Tripleproduct){reference-type="eqref" reference="Eqn=Tripleproduct"} by $-2r$.
:::

In order to finish the proof of Proposition [\[Prop=Normestimate\]](#Prop=Normestimate){reference-type="ref" reference="Prop=Normestimate"}, we just need bounds for the inner product pairings and the operators $R_{n,k}^{\ast}$.

::: lem
Let $H$ be a Hilbert space. The inner product pairing $m\colon \overline{H}\otimes H \to \mathbb{C}$ has norm $\sqrt{ \dim(H)}$.
:::

::: proof
*Proof.* Let $(e_{i})_{i\in I}$ be an orthonormal basis of $H$. Then the norm of $v:=\sum_{i\in I} \overline{e_i} \otimes e_{i}$ is equal to $\sqrt{|I|}$, while $m(v)=|I|$, so the norm is at least $\sqrt{|I|}$. On the other hand, a simple Cauchy-Schwarz estimate shows that it is not larger than that. ◻
:::

::: lem
Recall that the norm of $R_{n,k}^{\ast}\colon H^{\otimes n+k} \to H^{\otimes n+k}$ is bounded by $C(q)$. Then the norm $R_{n,k}^{\ast}: H_{q}^{\otimes n+k} \to H_q^{\otimes n} \otimes H_q^{\otimes k}$ is not greater than $\sqrt{C(q)}$.
:::

::: proof
*Proof.* Because of the formula $P_q^{n+k} = (P_q^{n}\otimes P_q^{k})R_{n,k}^{\ast}$, we get $P_{q}^{n+k} \leqslant C(q) P_q^{n}\otimes P_q^{k}$. Indeed, if we have an equality $A=BT$ for positive operators $A$ and $B$ then $A^2 = B TT^{\ast}B \leqslant \|T\|^2 B^2$, hence $A\leqslant \|T\|B$, as square root is an operator monotone function. The majorisation $P_{q}^{n+k} \leqslant C(q) P_q^{n}\otimes P_q^{k}$ shows that $\|R_{n,k}\|\leqslant \sqrt{C(q)}$, therefore also $\|R_{n,k}^{\ast}\|\leqslant C(q)$. ◻
:::

::: cor
We have $\|R_{n,k,l}^{\ast}\|\leqslant C(q)$, where $R_{n,k,l}^{\ast}$ is viewed as an operator from $H_q^{\otimes n+k+l}$ to $H_q^{\otimes n}\otimes H_q^{\otimes k} \otimes H_q^{\otimes l}$.
:::

::: proof
*Proof.* By Lemma [\[Lem=Splitting\]](#Lem=Splitting){reference-type="ref" reference="Lem=Splitting"} we can express $R_{n,k,l}^{\ast}$ as $(R_{n,k}^{\ast}\otimes {\rm Id}_{l}) R_{n+k,l}^{\ast}$, and then we can appeal to the lemma above. ◻
:::

::: proof
*Proof of Proposition [\[Prop=Normestimate\]](#Prop=Normestimate){reference-type="ref" reference="Prop=Normestimate"}.* Let $\bm{\mu} \in H_q^{\otimes m}$ and consider $\Psi^{a,b}(\bm{\mu})$. According to Proposition [\[Prop=Tripleproduct\]](#Prop=Tripleproduct){reference-type="ref" reference="Prop=Tripleproduct"} we have $$\Psi^{a,b}(\bm{\mu}) = -2\sum_{j,r,s}rq^{r(m-j-s)} m_{r}^{13}m_s^{12}m_j^{23}(R_{n-r-s,r,s}^{\ast}(\bm{\xi})\otimes R_{s,m-s-j,j}^{\ast}(\bm{\mu}) \otimes R_{j,r,k-j-r}^{\ast}(\bm{\eta})).$$ We may assume that $r\geqslant 1$ (otherwise the corresponding summand is equal to zero), so the (absolute value of the) factor $q^{r(m-j-s)}$ is bounded above by $|q|^m$, up to a constant depending on $q$, $n$, and $k$. As each of $j$, $r$, and $s$ is bounded by either $n$ or $k$, the range of summation is finite, so it suffices to bound uniformly the norm of each summand. If we treat $R_{n,k}^{\ast}$ as a map from $H_q^{\otimes n+k}$ to $H_q^{\otimes n}\otimes H_q^{\otimes k}$, then each summand in [\[Eqn=Tripleproduct\]](#Eqn=Tripleproduct){reference-type="eqref" reference="Eqn=Tripleproduct"} should be thought of as an element of the space $H_{q}^{\otimes n-r-s} \otimes H_q^{\otimes m-s-j} \otimes H_q^{\otimes k-j-r}$ and this norm is bounded by a constant depending on $q$ and $\dim(H)$ (coming from the inner product pairing). Because the norm of the identity map $R_{n-r-s,m-s-j, k-j-r}\colon H_{q}^{\otimes n-r-s} \otimes H_q^{\otimes m-s-j} \otimes H_q^{\otimes k-j-r} \to H_q^{\otimes m+n+k - 2(j+r+s)}$ has norm at most $C(q)$, the norm in $H_q^{\otimes m+n+k - 2(j+r+s)}$ is bounded uniformly as well, which ends the proof. ◻
:::

::: thm
[]{#Thm=QGaussianSp label="Thm=QGaussianSp"} Suppose that $\vert q \vert < \dim(H)^{-\frac{1}{p}}$. Then the Ornstein-Uhlenbeck quantum Markov semi-group $(\Phi_t)_{t \geq 0}$ is gradient-$\mathcal{S}_{p}$. If $\vert q \vert \leqslant  \dim(H)^{-\frac{1}{p}}$ then $(\Phi_t)_{t \geq 0}$ is immediately gradient-$\mathcal{S}_{p}$.
:::

::: proof
*Proof.* We we will estimate the $\mathcal{S}_{p}$ norm of $\Psi^{a,b}$ by $\sum_{m=0}^{\infty} \|\Psi^{a,b}_{|H_q^{\otimes m}}\|_{p}$. Because $\dim(H_q^{\otimes m}) = \dim(H)^{m}$, we may estimate $\|\Psi^{a,b}_{|H^{\otimes m}}\|_{p}$ by $\dim(H)^{\frac{m}{p}}\|\Psi^{a,b}_{|H_q^{\otimes m}}\|$. The bound for this norm is provided by Proposition [\[Prop=Normestimate\]](#Prop=Normestimate){reference-type="ref" reference="Prop=Normestimate"}, so we get $$\|\Psi^{a,b}\|_{p} \leqslant C(q,\bm{\xi},\bm{\eta},\dim(H)) \sum_{m=0}^{\infty} \left(|q| \dim(H)^{\frac{1}{p}}\right)^{m}.$$ This series is convergent if $|q|< \dim(H)^{-\frac{1}{p}}$.

If $|q| = \dim(H)^{-\frac{1}{p}}$, then we want to show that the maps $\Psi^{a,b}_{t}$ are in $\mathcal{S}_p$ for any $t>0$. Running again the same computation, we get the estimate $$\begin{aligned}
\|\Psi_{t}^{a,b}\|_{p} &\leqslant C(q,\bm{\xi},\bm{\eta},\dim(H)) \sum_{m=0}^{\infty}e^{-tm} \left(|q| \dim(H)^{\frac{1}{p}}\right)^{m} \\
&= C(q,\bm{\xi},\bm{\eta},\dim(H)) \sum_{m=0}^{n} e^{-tm},
\end{aligned}$$ and this series is convergent. ◻
:::
