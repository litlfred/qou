---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS"
section_id: sec-005-2-description-of-nkv-for-finite-type-via-adapted
section_title: "Description of Nk(v) for Finite Type Via Adapted Strings"
section_number: 2
pages: 14-17
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.913
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS — We give an explicit construction of irreducible modules over Khovanov-Lauda- Rouquier algebras R and their"
---
[]{#Sec: Description Nk label="Sec: Description Nk"}

In this section, we give an explicit description of the modules $\mathcal{N}_k(v)$ for finite type. To that end, we choose a particular reduced expression of the longest element $w_0$ of the Weyl group $W$. Using the notion of adapted strings for crystals given in [@Lit98] with respect to these specially chosen expressions, we describe $\mathcal{N}_k(v)$ explicitly in terms of Kashiwara operators $\tilde{f}_i$ (Proposition [\[Prop: description of Nk\]](#Prop: description of Nk){reference-type="ref" reference="Prop: description of Nk"}).

Throughout the section, we assume that the Cartan datum $(\mathfrak{A},\mathsf{P}, \Pi,\mathsf{P}^{\vee},\Pi^{\vee})$ is of finite type. For a sequence $\mathbf{m} = (m_1, \ldots, m_k)$ of elements in $I$, we write $r_\mathbf{m} = r_{m_1} r_{m_2} \cdots r_{m_k}$ for the corresponding element in the Weyl group. Using this convention, we fix a particular reduced expression for the longest element $w_0$ of $W$ $$\label{eq:reduced} w_0  = r_{\mathbf{s}_1}r_{\mathbf{s}_2} \cdots r_{\mathbf{s}_n} = r_{s_1} r_{s_2} \cdots r_{s_\ell}$$ where the sequences $\mathbf{s}_k$ are displayed in Table $\ref{Tb: w0}$ below. Let $l_k$ be the length of the sequence $\mathbf{s}_k$ in [\[eq:reduced\]](#eq:reduced){reference-type="eqref" reference="eq:reduced"} for $k=1,\ldots,n$. Then $r_{\mathbf{s}_1} = r_{s_1} \cdots r_{s_{l_1}}$, $r_{\mathbf{s}_2} = r_{s_{l_1+1}} \cdots r_{s_{l_1 + l_2}}$ and so forth. Note that $\ell$ is the length of the reduced expression.

::: definition
Let $v \in B(\infty)$ (resp. $v \in B(\lambda)$). An $\ell$-tuple $\mathbf{a}(v)=(a_1, \ldots, a_\ell) \in (\mathbb{Z}_{\ge0})^\ell$ is called the *adapted string* of $v$ with respect to the expression $r_{s_1} \cdots r_{s_\ell}$ if $$a_1 =  \varepsilon_{s_1}(v),\ \   a_2 =  \varepsilon_{s_2}\left(  \tilde{e}_{s_1}^{a_1} v\right), \ \ \ldots\,,\ \ a_\ell =  \varepsilon_{s_\ell}\left(  \tilde{e}_{s_{\ell-1}}^{a_{\ell-1}} \cdots  \tilde{e}_{s_{1}}^{a_{1}} v\right) .$$ We denote by $\mathcal{S} = \{ \mathbf{a}(v) \mid v \in B(\infty) \}$ (resp. $\mathcal{S}^\lambda = \{ \mathbf{a}(v) \mid v \in B(\lambda) \}$) the set of all adapted strings of elements in $B(\infty)$ (resp. $B(\lambda)$).
:::

::: {#Tb: w0}
                      Dynkin diagrams  $w_0 = r_{\mathbf{s}_1} \cdots r_{\mathbf{s}_n}$
  ------------------ ----------------- ---------------------------------------------------------------------------
                                       
   $(\mathsf{A}_n)$                    $\mathbf{s}_k = (n+1-k, \ldots, n-1,n)$ for $k=1,\ldots,n$
                                       $\mathbf{s}_k = (n+1-k, \ldots, n-1,n,n-1,\ldots,n+1-k)$
                                         for $k=1,\ldots,n$
   $(\mathsf{C}_n)$                    $\mathbf{s}_k$ is the same as for type $\mathsf{B}_n$ for $k=1,\ldots,n$
                                       $\mathbf{s}_1 = (n)$, $\mathbf{s}_2 = (n-1)$,
                                       $\mathbf{s}_k = (n+1-k,\ldots,n-2,n,n-1,n-2,\ldots,n+1-k)$
                                         for $k=3,\ldots,n$
                                       $\mathbf{s}_k$ is the same as for type $\mathsf{D}_5$ for $k=1,\ldots,5$,
                                       $\mathbf{s}_6 = (6,5,3,4,2,1,3,2,5,3,4,6,5,3,2,1)$,
                                       $\mathbf{s}_k$ is the same as for type $\mathsf{E}_6$ for $k=1,\ldots,6$,
                                       $\mathbf{s}_7 = (7,6,5,3,4,2,1,3,2,5,3,4,6,5,3,2,1,7,6,5,3,4,2,$
                                         $3,5,6,7)$
                                       $\mathbf{s}_k$ is the same as for type $\mathsf{E}_7$ for $k=1,\ldots,7$,
                                       $\mathbf{s}_8 = (8,7,6,5,3,4,2,1,3,2,5,3,4,6,5,3,2,1,7,6,5,3,4,$
                                         $2,3,5,6,7,8,7,6,5,3,4,2,1,3,2,5,3,4,6,5,3,2,1,$
                                         $7,6,5,3,4,2,3,5,6,7,8)$
                                       $\mathbf{s}_k$ is the same as for type $\mathsf{B}_3$ for $k=1,\ldots,3$,
                                       $\mathbf{s}_4 = (4,3,2,1,3,2,3,4,3,2,1,3,2,3,4)$
   $(\mathsf{G}_2)$                    $\mathbf{s}_1 = (1), \ \mathbf{s}_2 = (2,1,2,1,2)$
                                       

  : 
:::

[]{#Tb: w0 label="Tb: w0"}

Observe that if $\iota_{\lambda}(v) = v' \otimes t_\lambda \otimes c$ for some $v\in B(\lambda)$ and $v' \in B(\infty)$, then $\mathbf{a}(v) = \mathbf{a}(v')$. It follows from [@Kash93a; @Lit94] that $\mathcal{S}$ and $\mathcal{S}^\lambda$ are in one-to-one correspondence with the crystals $B(\infty)$ and $B(\lambda)$, respectively, by the maps $$\label{Eq: one to one}
 \begin{aligned}
\mathcal{S} &\buildrel \text{1-1} \over\longrightarrow B(\infty) \ \ \text{ given by } \ \  \mathbf{a}=(a_1, \ldots, a_\ell) \mapsto  \tilde{f}^{a_1}_{s_1} \cdots  \tilde{f}^{a_\ell}_{s_\ell}  \mathsf{1}, \\
 \mathcal{S}^\lambda &\buildrel \text{1-1} \over\longrightarrow B(\lambda) \ \ \ \text{ given by } \ \   \mathbf{a}=(a_1, \ldots, a_\ell) \mapsto  \tilde{f}^{a_1}_{s_1} \cdots  \tilde{f}^{a_\ell}_{s_\ell} b_\lambda.
 \end{aligned}$$

For $\mathbf{a} = (a_1, \ldots, a_\ell) \in (\mathbb{Z}_{\ge 0})^\ell$, set $$\begin{aligned}
 \label{Eq: subseq of a}
\mathsf{a}_{k,j} = a_{l_1 + \cdots + l_{k-1}+j} \quad \hbox{\rm and} \quad
\mathbf{a}_k = (\mathsf{a}_{k,1}, \mathsf{a}_{k,2}, \ldots,  \mathsf{a}_{k,l_k}  ),
\end{aligned}$$ where $l_k$ is, as above, the length of $\mathbf{s}_k$. Then $\mathbf{a} = \mathbf{a_1} * \cdots * \mathbf{a_n}$.

In particular, for $v \in B(\infty)$, we have $\mathbf{a}(v) = \mathbf{a}(v)_1 * \cdots * \mathbf{a}(v)_n$ and $$v =  \tilde{f}_{\mathbf{s}_1}^{\mathbf{a}(v)_1}  \tilde{f}_{\mathbf{s}_2}^{\mathbf{a}(v)_2} \cdots  \tilde{f}_{\mathbf{s}_n}^{\mathbf{a}(v)_n} \mathsf{1}.$$

::: proposition
[]{#Prop: adapted strings label="Prop: adapted strings"} Let $(\mathfrak{A}, \mathsf{P}, \Pi, \mathsf{P}^{\vee}, \Pi^{\vee})$ be a Cartan datum of finite type. Then $\mathcal{S}$ has the following description: $$\begin{aligned}
(\mathsf{A}_n): \ \   \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid & \  \mathsf{a}_{i,1} \ge \mathsf{a}_{i,2} \ge \cdots \ge \mathsf{a}_{i,i}\  (1 \le i \le n) \}\\
(\mathsf{B}_n): \ \  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid & \  2\mathsf{a}_{i,1} \ge \cdots \ge 2\mathsf{a}_{i,i-1} \ge \mathsf{a}_{i,i} \ge 2\mathsf{a}_{i,i+1} \ge \cdots \ge 2\mathsf{a}_{i,2i-1}\ (1 \le i \le n) \}  \\
(\mathsf{C}_n): \ \ \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid & \  \mathsf{a}_{i,1} \ge \cdots \ge \mathsf{a}_{i,i-1} \ge \mathsf{a}_{i,i} \ge \mathsf{a}_{i,i+1} \ge \cdots \ge \mathsf{a}_{i,2i-1}\  (1 \le i \le n) \}  \\
(\mathsf{D}_n): \ \  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid & \  \mathsf{a}_{i,1} \ge \cdots \ge \mathsf{a}_{i,i-1}, \mathsf{a}_{i,i} \ge \mathsf{a}_{i,i+1} \ge \cdots \ge \mathsf{a}_{i,2i-2}\  (3 \le i \le n) \}  \\
(\mathsf{E}_6): \ \  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid &\ \mathsf{a}_{6,1} \ge \mathsf{a}_{6,2} \ge \mathsf{a}_{6,3} \ge \mathsf{a}_{6,4}, \mathsf{a}_{6,5} \ge \mathsf{a}_{6,7} \ge \mathsf{a}_{6,8}, \mathsf{a}_{6,9} \ge \mathsf{a}_{6,10}
\ge \mathsf{a}_{6,11},\mathsf{a}_{6,13} \\
 &\ \ge \mathsf{a}_{6,14} \ge \mathsf{a}_{6,15} \ge \mathsf{a}_{6,16};\ \mathsf{a}_{6,5} \ge \mathsf{a}_{6,6} \ge \mathsf{a}_{6,8};\ \mathsf{a}_{6,9} \ge \mathsf{a}_{6,12} \ge \mathsf{a}_{6,13}; \\
&\ \text{$\mathsf{a}_{i,j}$'s satisfy the inequalities for $\mathsf{D}_5$ for $i=1,\ldots,5$} \}\\
 (\mathsf{E}_7): \ \  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid &\ \mathsf{a}_{7,1} \ge \mathsf{a}_{7,2} \ge \mathsf{a}_{7,3} \ge \mathsf{a}_{7,4} \ge \mathsf{a}_{7,5}, \mathsf{a}_{7,6}  \ge \mathsf{a}_{7,8} \ge \mathsf{a}_{7,9}, \mathsf{a}_{7,10}  \\
 &\ \ge \mathsf{a}_{7,11} \ge \mathsf{a}_{7,12},\mathsf{a}_{7,14} \ge \mathsf{a}_{7,15} \ge \mathsf{a}_{7,16}, \mathsf{a}_{7,20} \ge \mathsf{a}_{7,21}\ge \mathsf{a}_{7,22}, \mathsf{a}_{7,23}  \\
 &\ \ge \mathsf{a}_{7,24} \ge \mathsf{a}_{7,25} \ge \mathsf{a}_{7,26} \ge \mathsf{a}_{7,27};\ \mathsf{a}_{7,6} \ge \mathsf{a}_{7,7}\ge \mathsf{a}_{7,8} ;\ \\
 &\ \mathsf{a}_{7,10} \ge \mathsf{a}_{7,13}\ge \mathsf{a}_{7,14}, \mathsf{a}_{7,18} \ge \mathsf{a}_{7,19} \ge \mathsf{a}_{7,20};\ \mathsf{a}_{7,16} \ge \mathsf{a}_{7,17} \ge \mathsf{a}_{7,23}; \\
&\ \text{$\mathsf{a}_{i,j}$'s satisfy the inequalities for $\mathsf{E}_6$ for $i=1,\ldots,6$} \} \\
(\mathsf{E}_8): \ \  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid &\ (\mathsf{a}_{8,2}, \ldots, \mathsf{a}_{8,28}) \ \text{and} \ (\mathsf{a}_{8,30}, \ldots, \mathsf{a}_{8,56}) \text{ satisfy the inequalities of $\mathbf{a}_7$ for $\mathsf{E}_7$};\\
&\hspace{-.4truein} \mathsf{a}_{8,1} \ge \mathsf{a}_{8,2};\ \mathsf{a}_{8,29} \ge \mathsf{a}_{8,30};\ \mathsf{a}_{8,56} \ge \mathsf{a}_{8,57};  \\
&\hspace{-.4truein} \mathsf{a}_{8,19} \ge \mathsf{max}\{ \mathsf{a}_{8,30}, \mathsf{a}_{8,29} - \mathsf{a}_{8,28} \};\  \mathsf{min}\{ \mathsf{a}_{8,23}, \mathsf{a}_{8,25} +\mathsf{a}_{8,33} - \mathsf{a}_{8,34} \} \ge \mathsf{a}_{8,35}; \\
&\hspace{-.4truein}  \mathsf{a}_{8,20} \ge \mathsf{max}\{ \mathsf{a}_{8,31}, \mathsf{a}_{8,28} + \mathsf{a}_{8,30} - \mathsf{a}_{8,27} \};\  \mathsf{min}\{ \mathsf{a}_{8,25}, \mathsf{a}_{8,26} +\mathsf{a}_{8,32} - \mathsf{a}_{8,33} \} \ge \mathsf{a}_{8,37}; \\
&\hspace{-.4truein} \mathsf{a}_{8,21} \ge \mathsf{max}\{ \mathsf{a}_{8,32}, \mathsf{a}_{8,27} + \mathsf{a}_{8,31} - \mathsf{a}_{8,26} \};\  \mathsf{min}\{ \mathsf{a}_{8,26}, \mathsf{a}_{8,27} +\mathsf{a}_{8,31} - \mathsf{a}_{8,32} \} \ge \mathsf{a}_{8,39}; \\
&\hspace{-.4truein} \mathsf{a}_{8,22} \ge  \mathsf{max}\{ \mathsf{a}_{8,33}, \mathsf{a}_{8,26} + \mathsf{a}_{8,32} - \mathsf{a}_{8,25} \};\  \mathsf{min}\{ \mathsf{a}_{8,27}, \mathsf{a}_{8,28} +\mathsf{a}_{8,30} - \mathsf{a}_{8,31} \} \ge \mathsf{a}_{8,42}; \\
&\hspace{-.4truein}  \mathsf{a}_{8,24} \ge  \mathsf{max}\{ \mathsf{a}_{8,34}, \mathsf{a}_{8,25} + \mathsf{a}_{8,33} - \mathsf{a}_{8,23} \};\  \mathsf{min}\{ \mathsf{a}_{8,28}, \mathsf{a}_{8,29} - \mathsf{a}_{8,30} \} \ge \mathsf{a}_{8,47};   \\
&\hspace{-.4truein} \text{$\mathsf{a}_{i,j}$'s satisfy the inequalities for $\mathsf{E}_7$ for $i=1,\ldots,7$} \}  \allowdisplaybreaks  \\
(\mathsf{F}_4): \ \  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid &\ \mathsf{a}_{4,1} \ge \mathsf{a}_{4,2} \ge \mathsf{a}_{4,3} \ge \mathsf{a}_{4,4}, \mathsf{a}_{4,5} \ge \mathsf{a}_{4,6} \ge \mathsf{a}_{4,7}; \\
 &\ \mathsf{a}_{4,9} \ge \mathsf{a}_{4,10} \ge \mathsf{a}_{4,11},\mathsf{a}_{4,12}  \ge \mathsf{a}_{4,13} \ge \mathsf{a}_{4,14} \ge \mathsf{a}_{4,15}; \\
&\ \mathsf{a}_{4,5} \ge \mathsf{a}_{4,9};\ \mathsf{a}_{4,7} \ge \mathsf{a}_{4,12};\ \mathsf{a}_{4,5} + \mathsf{a}_{4,7} \ge \mathsf{a}_{4,8} \ge \mathsf{a}_{4,9} + \mathsf{a}_{4,12};\\
&\  2\mathsf{a}_{4,6} \ge \mathsf{a}_{4,7} + \mathsf{a}_{4,9} \ge 2\mathsf{a}_{4,10}; \\
&\ \text{$\mathsf{a}_{i,j}$'s satisfy the inequalities for $\mathsf{B}_3$ for $i=1, 2, 3$} \}   \\
(\mathsf{G}_2): \ \  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid &\ 6\mathsf{a}_{2,1} \ge 2\mathsf{a}_{2,2} \ge 3\mathsf{a}_{2,3} \ge 2\mathsf{a}_{2,4} \ge 6\mathsf{a}_{2,5} \}.
\end{aligned}$$
:::

We now give a description of $\mathcal{N}_k(v)$ using Proposition [\[Prop: adapted strings\]](#Prop: adapted strings){reference-type="ref" reference="Prop: adapted strings"}.

::: proposition
[]{#Prop: description of Nk label="Prop: description of Nk"} Let $(\mathfrak{A}, \mathsf{P}, \Pi, \mathsf{P}^{\vee}, \Pi^{\vee})$ be a Cartan datum of finite type. For $v \in B(\infty)$ and $k=1,\ldots, n$, the module $\mathcal{N}_k(v)$ defined by $\eqref{Eq: def of Nk}$ is given by $$\mathcal{N}_k(v) =  \tilde{f}_{\mathbf{s}_k} ^{\mathbf{a}(v)_k} \mathbf{1},$$ where $\mathbf{a}(v)$ is the adapted string of $v$ with respect to the expression $w_0 = r_{\mathbf{s}_1} \cdots r_{\mathbf{s}_n}$ in Table $\ref{Tb: w0}$.
:::

::: proof
*Proof.* Let $I_{(k)} = \{ n+1-k, \ldots, n-1,n \}$ for $k=1,\ldots, n$ and set $I_{(0)} = \emptyset$. Let $\mathfrak{B}_k$ denote the crystal obtained from $B(\infty)$ by forgetting the $i$-arrows with $i \notin I_{(k)}$. Take $v \in B(\infty)$ and let $\mathbf{a} = \mathbf{a}(v) = \mathbf{a}_1 * \cdots * \mathbf{a}_n$ be the adapted string of $v$ with respect to the expression $w_0 = r_{\mathbf{s}_1} \cdots r_{\mathbf{s}_n}$ in Table $\ref{Tb: w0}$. For $k=1,\ldots, n$, let $\mathbf{0}_k = (\underbrace{0,\ldots, 0}_{l_k})$ where $l_k$ is the length of $\mathbf{s}_k$ as before. Then, by Proposition [\[Prop: adapted strings\]](#Prop: adapted strings){reference-type="ref" reference="Prop: adapted strings"}, $$\mathbf{b}_k :=  \mathbf{0}_1 *  \ldots *  \mathbf{0}_{k} * \mathbf{a}_{k+1} * \ldots *  \mathbf{a}_{n-1} * \mathbf{a}_n$$ is contained in $\mathcal{S}$. Let $u_k =  \tilde{f}_{\mathbf{s}_{k+1}}^{\mathbf{a}_{k+1}} \cdots  \tilde{f}_{\mathbf{s}_{n}}^{\mathbf{a}_{n}} \mathsf{1}$ for $k=0,\ldots, n-1$ and let $u_n = \mathsf{1}$. Since $\mathbf{b}_k$ is the adapted string of $u_k$, by the definition of adapted strings we have $$v =  \tilde{f}_{\mathbf{s}_{1}}^{\mathbf{a}_{1}} \cdots  \tilde{f}_{\mathbf{s}_{k}}^{\mathbf{a}_{k}} u_k , \qquad  \varepsilon_i(u_k)=0 \ \text{ for }i \in I_{(k)},$$ which implies that $u_k$ is the highest weight vector of the connected component $\mathcal{C}_k$ of $\mathfrak{B}_k$ containing $v$. Therefore, $\mathcal{N}_k(v) =  \tilde{f}_{\mathbf{s}_k} ^{\mathbf{a}_k} \mathbf{1}$ for $k=1,\ldots,n$. ◻
:::
