---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-016-54-symmetries-of-the-quantum-k-bruhat-order
section_title: "Symmetries of the quantum k-Bruhat order"
section_number: 5.4
pages: 20-23
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.902
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#sec:actions-on-left-operators label="sec:actions-on-left-operators"}

Operations that preserve the $k$-Bruhat order (its symmetries) played a role in many results in [@BS-Bruhat]. We identify three operations preserving the quantum $k$-Bruhat order, which are symmetries of that order. These induce three operations on the operators ${\mathbf v}_{ab}$ that preserve equivalence to ${\mathbf 0}$ and $(u,k)$-equivalence, and which are fundamental to our proof of Theorem [\[Th:nonZero\]](#Th:nonZero){reference-type="ref" reference="Th:nonZero"}. We first define these operations and state the main result of this section before studying the quantum $k$-Bruhat order.

Let $\mathfrak o$ be the $n$-cycle $(1, 2, \dotsc, n)$. For a composition ${\mathbf v}={\mathbf v}_{a_r b_r}\cdots {\mathbf v}_{a_1 b_1}$, define $${\color{RoyalBlue}\mathfrak o({\mathbf v})}\ =\ \mathfrak o({\mathbf v}_{a_r b_r}\cdots {\mathbf v}_{a_1 b_1})
    \   \vcentcolon=\
    {\mathbf v}_{\mathfrak o(a_r),\mathfrak o(b_r)} \cdots {\mathbf v}_{\mathfrak o(a_1),\mathfrak o(b_1)}\,.$$ This cyclically shifts indices. Note that $\mathfrak o({\mathbf v}_{n,b}) = {\mathbf v}_{1,b+1}$ and $\mathfrak o({\mathbf v}_{a,n}) = {\mathbf v}_{a+1,1}$, interchanging classical and quantum operators, while other applications of $\mathfrak o$ preserve the type of the operator. When $n = 3$, we have $\mathfrak o= (1,2,3)$ and $$\arraycolsep=0.1cm
  \begin{array}{ccccccccccc}
    \valuediagram[padding=1, xmin=1, xmax=3]{{2,3}} &
     \raisebox{-3pt}{$\xrightarrow{\,\mathfrak o\,}$}&
     \valuediagram[padding=1]{{3,1}} &
     \raisebox{-3pt}{$\xrightarrow{\,\mathfrak o\,}$}&
     \valuediagram[padding=1, xmax=3]{{1,2}}
    &\raisebox{-2pt}{\quad and\quad}&
     \valuediagram[padding=1, xmin=1, xmax=3]{{3,2}} &
     \raisebox{-3pt}{$\xrightarrow{\,\mathfrak o\,}$}&
     \valuediagram[padding=1]{{1,3}} &
     \raisebox{-3pt}{$\xrightarrow{\,\mathfrak o\,}$}&
     \valuediagram[padding=1, xmax=3]{{2,1}}
   \\[1ex]
     {{\mathbf v}}_{23}&& {{\mathbf v}}_{31}&& {{\mathbf v}}_{12}&&
     {{\mathbf v}}_{32}&& {{\mathbf v}}_{13}&& {{\mathbf v}}_{21}
 \end{array}$$ Each triple cycles back to the original operator with another application of $\mathfrak o$. Let $w_0$ be the longest element in $S_n$, so that $w_0(i)=n{+}1{-}i$ for $i\in[n]$. Define $${\color{RoyalBlue}w_0({\mathbf v})}\ =\ w_0({\mathbf v}_{a_r b_r}\cdots {\mathbf v}_{a_1 b_1})
  \ \vcentcolon=\
  {\mathbf v}_{w_0(b_r), w_0(a_r)} \cdots {\mathbf v}_{w_0(b_1), w_0(a_1)}\,.$$ This replaces an index $c$ by $w_0(c)=n{+}1{-}c$ and reverses the order of indices on each ${\mathbf v}_{ab}$. It preserves quantum and classical operators as $a<b\Leftrightarrow n{+}1{-}b<n{+}1{-}a$. Finally, define ${\color{RoyalBlue}\rho({\mathbf v}_{a_r b_r}\cdots {\mathbf v}_{a_1b_1})}\vcentcolon= {\mathbf v}_{a_1b_1}\cdots{\mathbf v}_{a_r b_r}$, which reverses the order of the operators.

We introduce notation to quantify how these operations act on monomials in the $q_i$. If $q^\alpha=q_1^{\alpha_1}\dotsb q_{n-1}^{\alpha_{n-1}}$, then set ${\color{RoyalBlue}w_0(q^\alpha)}\vcentcolon={\color{RoyalBlue}q^{w_0(\alpha)}}=q_1^{\alpha_{n-1}}\dotsb q_{n-1}^{\alpha_{1}}$. For $\mathfrak o$, this requires Laurent monomials in the $q_i$. When $i<j$, we defined $q_{i,j}$ to be $q_iq_{i+1}\dotsb q_{j-1}$. When $i>j$, set $q_{i,j}=q_{j,i}^{-1}$. For $u,w\in S_n$, define ${\color{RoyalBlue}q^{\mathfrak o(u,w)}}\vcentcolon=q_{w^{-1}(n),u^{-1}(n)}$, which keeps track of how the monomial $q^\alpha$ in elements of $S_n[q]$ is affected by the cyclic shift. Note that $q^{\mathfrak o(u,w)}=q_{1,u^{-1}(n)}\cdot q_{w^{-1}(n),1}$, which shows that it is multiplicative in that $q^{\mathfrak o(u,w)}=q^{\mathfrak o(u,v)}\cdot q^{\mathfrak o(v,w)}$, for any $u,v,w\in S_n$. Observe that for $u\in S_n$ and $i<j$, if we set $w\vcentcolon= u(i,j)$, then

$$\label{Eq:qOcycle}
   q^{\mathfrak o(u,w)}\ =\ \left\{ \begin{array}{rcl} 
      q_{i,j}^{-1} &\quad&\mbox{if } u(i)=n\,,\\
      q_{i,j} &\quad&\mbox{if } u(j)=n\,,\\
      1 &\quad&\mbox{otherwise}\,. \end{array}\right.$$

For $u\in S_n$, we will often write $\mathfrak ou$ for $\mathfrak o(u)$.

::: lemma
[]{#L:symmetry_qkBO label="L:symmetry_qkBO"} Let $u\in S_n$, $1\leq i\leq k<j\leq n$, and $\alpha\in{\mathbb N}^{n-1}$. Set ${\color{RoyalBlue}w}\vcentcolon= u(i,j)$. Then the following are equivalent:

$$\begin{aligned}
    & (1)\ u\ \lessdot_k^q\ q^\alpha w, 
    & &(3)\ w_0uw_0\ \lessdot_{n-k}^q\ q^{w_0(\alpha)} w_0 w w_0, \\
    & (2)\ \mathfrak ou\ \lessdot_k^q\ q^{\mathfrak o(u,w)} q^\alpha \mathfrak ow, 
    & &(4)\ w w_0\ \lessdot_{n-k}^q\ q^{w_0(\alpha)} u w_0.
 
\end{aligned}$$
:::

That the operator $\mathfrak o$ preserves the quantum $k$-Bruhat order in this way follows from results of Postnikov [@Postnikov_symmetry]; for the order it is his Corollary 12 and the exponents $q^{\mathfrak o(u,w)}$ are related to his operator $O$ referred to as "twisted cyclic shift" in *loc. cit.* We deduce the following corollary concerning the action of the operators ${\mathbf v}_{ab}$.

::: corollary
[]{#C:symmetries-q-ops label="C:symmetries-q-ops"} Let $u,w\in S_n$, $q^\alpha w\in S_n[q]$, and $a\neq b$ in $[n]$. The following are equivalent.

$$\begin{aligned}
    & (1)\ u\ \lessdot_k^q\ {\mathbf v}_{ab}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u = q^\alpha w,
    & &(3)\ w_0uw_0\ \lessdot_{n-k}^q\ \ w_0({\mathbf v}_{ab})\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w_0uw_0 =  q^{w_0(\alpha)} w_0 w w_0,\\
    & (2)\ \mathfrak ou\ \lessdot_k^q\ \mathfrak o({\mathbf v}_{ab})\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}\mathfrak ou = q^{\mathfrak o(u,w)} q^\alpha \mathfrak ow,
    & &(4)\ w w_0\ \lessdot_{n-k}^q\ {\mathbf v}_{ab}\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} ww_0 = q^{w_0(\alpha)} u w_0.
 
\end{aligned}$$
:::

::: proof
*Proof of Lemma [\[L:symmetry_qkBO\]](#L:symmetry_qkBO){reference-type="ref" reference="L:symmetry_qkBO"}.* We will freely use Propositions [\[nothing-in-between-is-in-between\]](#nothing-in-between-is-in-between){reference-type="ref" reference="nothing-in-between-is-in-between"} and [\[prop:quantum-k-bruhat-covers\]](#prop:quantum-k-bruhat-covers){reference-type="ref" reference="prop:quantum-k-bruhat-covers"} which characterize the covers $\lessdot_k$ and $\lessdot_k^q$. Note that if $q^\alpha=1$, then $u\lessdot_k u(i,j)=w$ is a classical cover, otherwise $u\lessdot_k^q  q_{i,j}u(i,j)=q^\alpha w$, so that $q^\alpha=q_{i,j}$.

Suppose first that $q^\alpha=1$, so that $u\lessdot_k u(i,j)=w$. Thus, if $a=u(i)$ and $b=u(j)$, then $a<b$ and if $i<l<j$ then either $u(l)<a$ or $b<u(l)$. As $w_0(c)=n{+}1{-}c$, we have that $w_0u w_0 \lessdot_{n-k} w_0 w w_0$ and $w w_0 \lessdot_{n-k} u w_0$. Thus (1) implies both (3) and (4) when $q^\alpha=1$.

Still supposing that $q^\alpha=1$, if $u(j)=b<n$, then $\mathfrak ou(j)=b+1\leq n$ and we see that $\mathfrak ou \lessdot_k \mathfrak ow$. As $q^{\mathfrak o(u,w)}=1$, we have $\mathfrak ou \lessdot^q_k q^{\mathfrak o(u,w)} \mathfrak ow$. If $n=b=u(j)$, then for every $i<l<j$, $u(l)<a=u(i)$. We have that $\mathfrak ou(i)=a+1>\mathfrak ou(j)=\mathfrak o(n)=1$ and if $i<l<j$, then $\mathfrak ou(i)=a{+}1>\mathfrak ou(l)>1=\mathfrak ou(j)$, which implies that $\mathfrak ou \lessdot^q_k q_{i,j} \mathfrak ow$. By [\[Eq:qOcycle\]](#Eq:qOcycle){reference-type="eqref" reference="Eq:qOcycle"}, $q^{\mathfrak o(u,w)}=q_{i,j}$ and we again have that $\mathfrak ou \lessdot^q_k q^{\mathfrak o(u,w)} \mathfrak ow$. Thus when $q^\alpha=1$, (1) implies (2). Similar arguments show that (1) implies (2$'$), which is the statement (2), but where we use $\mathfrak o^{-1}$ in place of $\mathfrak o$ and replace $q^{\mathfrak o(u,w)}$ by $q^{\mathfrak o(\mathfrak o^{-1}(w),\mathfrak o^{-1}(u))}$.

Suppose now that $q^\alpha\neq 1$, so that $q^\alpha=q_{i,j}$ and $u\lessdot^q_k q_{i,j} w$. Then $a=u(i)>b=u(j)$ and if $i<l<j$, then $a>u(l)>b$. Multiplying by $w_0$ on the right shows that $$w w_0\ \lessdot^q_{n-k}\ q_{n+1-j,n+1-i} w w_0 (n{+}1-j,n{+}1-i)\ =\  w_0(q_{i,j})\, u w_0\,,$$ and further multiplying by $w_0$ on the left shows that $$w_0uw_0\  \lessdot^q_{n-k}\  q_{n+1-j,n+1-i} w_0 u w_0  (n{+}1-j,n{+}1-i)\ =\   w_0(q_{i,j})\, w_0 w w_0\,.$$ Thus (1) implies both (3) and (4) in this case.

Let us now consider (2). If $a\neq n$, then as before, $\mathfrak ou \lessdot_k^q  q_{i,j}\mathfrak ow=q^{\mathfrak o(u,w)} q_{i,j}\mathfrak ow$, as $q^{\mathfrak o(u,w)}=1$. If $a=n$, then $q^{\mathfrak o(u,w)}=q_{i,j}^{-1}$ [\[Eq:qOcycle\]](#Eq:qOcycle){reference-type="eqref" reference="Eq:qOcycle"}. If $i<l<j$, then $n>u(l)>b=u(j)$, and we have $n\geq u(l)+1 = \mathfrak ou(l)>\mathfrak ou(j)=b+1$. Thus $\mathfrak ou \lessdot_k \mathfrak ou(i,j)=\mathfrak ow= q^{\mathfrak o(u,w)} q_{i,j} \mathfrak ow$. Thus (1) implies (2). Similar arguments show that (1) implies (2$'$), which is the statement (2), but where we use $\mathfrak o^{-1}$ in place of $\mathfrak o$ and $q^{\mathfrak o(\mathfrak o^{-1}(w),\mathfrak o^{-1}(u))}$ in place of $q^{\mathfrak o(u,w)}$.

These arguments show that if $u\lessdot^q_k q^\alpha u(i,j)=q^\alpha w$, then (1) implies each of (2), (2$'$), (3), and (4). The implications $(3)\Rightarrow(1)$ and $(4)\Rightarrow(1)$ follow as $u\mapsto u w_0$ and $u\mapsto w_0 u w_0$ are involutions. Similarly, $\mathfrak o^{-1}\mathfrak ou=u$ and $q^{\mathfrak o(u,w)}q^{\mathfrak o(w,u)}=1$, thus $(1)\Rightarrow(2')$ for $\mathfrak ou \lessdot^q_k q^{\mathfrak o(u,w)} q^\alpha\mathfrak ow$ is $(2)\Rightarrow(1)$. This completes the proof that the four statements are equivalent. ◻
:::

We combine the equivalences of Corollary [\[C:symmetries-q-ops\]](#C:symmetries-q-ops){reference-type="ref" reference="C:symmetries-q-ops"} with the interpretation of equivalent operators corresponding to different chains in intervals of Remark [\[Rem:k-action\]](#Rem:k-action){reference-type="ref" reference="Rem:k-action"} [\[Rem:k-action:chains\]](#Rem:k-action:chains){reference-type="ref" reference="Rem:k-action:chains"} and [\[Rem:k-action:uk_equiv\]](#Rem:k-action:uk_equiv){reference-type="ref" reference="Rem:k-action:uk_equiv"}.

::: lemma
[]{#lemma:actions label="lemma:actions"}

The following statements are equivalent:

1.  []{#l:actions:a label="l:actions:a"} ${\mathbf v}$ and ${\mathbf v}'$ are $(u,k)$-equivalent with ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u = {\mathbf v}' \mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u = q^\alpha w$.

2.  []{#l:actions:b label="l:actions:b"} $\mathfrak o{\mathbf v}$ and $\mathfrak o{\mathbf v}'$ are $(\mathfrak ou, k)$-equivalent, with ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}\mathfrak ou={\mathbf v}'\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}\mathfrak ou = q^{\mathfrak o(u,w)} q^\alpha \mathfrak ow$.

3.  []{#l:actions:c label="l:actions:c"} $w_0 {\mathbf v}$ and $w_0{\mathbf v}'$ are $(w_0uw_0, n{-}k)$-equivalent with $w_0{\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w_0uw_0=w_0{\mathbf v}'\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w_0 uw_0 = q^{w_0(\alpha)} w_0 w w_0$.

4.  []{#l:actions:d label="l:actions:d"} $\rho {\mathbf v}$ and $\rho {\mathbf v}'$ are $(ww_0, n{-}k)$-equivalent with $\rho{\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w w_0=\rho{\mathbf v}'\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} ww_0 = q^{w_0(\alpha)} u w_0$.
:::

Before proving the lemma, we observe that a composition being nonzero is preserved by $\mathfrak o$, $w_0$, and $\rho$, and the same for being zero.

::: corollary
[]{#C:symmetries_bzero label="C:symmetries_bzero"} A composition ${\mathbf v}$ is equivalent to zero if and only if one (and hence all) of $\mathfrak o{\mathbf v}$, $w_0{\mathbf v}$, and $\rho{\mathbf v}$ is equivalent to zero.
:::

::: proof
*Proof of Lemma [\[lemma:actions\]](#lemma:actions){reference-type="ref" reference="lemma:actions"}.* Let $u,w\in S_n$, $\alpha\in{\mathbb N}^{n-1}$, and ${\mathbf v},{\mathbf v}'$ be compositions of left operators such that $u<_k^q {\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u={\mathbf v}'\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u = q^\alpha w$. By Remark [\[Rem:k-action\]](#Rem:k-action){reference-type="ref" reference="Rem:k-action"}[\[Rem:k-action:chains\]](#Rem:k-action:chains){reference-type="ref" reference="Rem:k-action:chains"}, ${\mathbf v}$ and ${\mathbf v}'$ each correspond to a chain in $[u,q^\alpha w]_k^q$. We apply the equivalences of Corollary [\[C:symmetries-q-ops\]](#C:symmetries-q-ops){reference-type="ref" reference="C:symmetries-q-ops"} to each step of those chains. For [\[l:actions:c\]](#l:actions:c){reference-type="ref" reference="l:actions:c"}, we have $w_0 uw_0 <_{n-k} w_0{\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w_0uw_0 =  w_0{\mathbf v}'\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w_0uw_0 = q^{w_0(\alpha)}w_0 ww_0$. For [\[l:actions:d\]](#l:actions:d){reference-type="ref" reference="l:actions:d"}, note that the chain is reversed and this shows that $w w_0 <_{n-k} \rho{\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w w_0 =  \rho{\mathbf v}'\mathop{\mathrm{{\scriptstyle \bullet}}}_{n-k} w w_0 = q^{w_0(\alpha)}u w_0$.

The argument for [\[l:actions:b\]](#l:actions:b){reference-type="ref" reference="l:actions:b"} is slightly more involved as the action of $\mathfrak o$ on monomials depends upon the cover. Let $u<_k^q {\mathbf v}u =  q^{\alpha} w$ correspond to the saturated chain in $[u,q^\alpha w]_k^q$,

$$u\ =\ q^{\alpha_0}w_0\ \lessdot_k^q\ q^{\alpha_1}w_1\ \lessdot_k^q\ q^{\alpha_2}w_2
      \ \lessdot_k^q\ \dotsb\  \lessdot_k^q\ q^{\alpha_r}w_r=q^\alpha w\,.$$

By Lemma [\[L:symmetry_qkBO\]](#L:symmetry_qkBO){reference-type="ref" reference="L:symmetry_qkBO"}(2), applying $\mathfrak o$ to $q^{\alpha_i}w_i\lessdot_k^q q^{\alpha_{i+1}}w_{i+1}$ gives $q^{\alpha_i}\mathfrak ow_i\lessdot_k^q q^{\mathfrak o(w_i,w_{i+1})}q^{\alpha_{i+1}}\mathfrak ow_{i+1}$. If we set ${\color{RoyalBlue}q^{\beta_i}}\vcentcolon=q^{\mathfrak o(u,w_i)}q^{\alpha_i}$, then, as $q^{\mathfrak o(u,w_{i+1})}=q^{\mathfrak o(u,w_i)}q^{\mathfrak o(w_i,w_{i+1})}$, we obtain the saturated chain

$$\mathfrak ou\ =\ q^{\beta_0}\mathfrak ow_0\ \lessdot_k^q\ q^{\beta_1}\mathfrak ow_1\ \lessdot_k^q\ q^{\beta_2}\mathfrak ow_2
      \ \lessdot_k^q\ \dotsb\  \lessdot_k^q\ q^{\beta_r}\mathfrak ow_r=q^{\mathfrak o(u,w)}q^\alpha \mathfrak ow\,$$

in the interval $[\mathfrak ou,q^{\mathfrak o(u,w)} q^\alpha \mathfrak ow]_k^q$, which completes the proof. ◻
:::

We have the following corollary. Here $\textit{op}$ applied to a poset gives the opposite poset, reversing all inequalities.

::: corollary
[]{#C:equivalences label="C:equivalences"} Let $u,w\in S_n$ and $\alpha\in{\mathbb N}^{n-1}$ be such that $u <_k^q q^\alpha w$. Then we have the following isomorphisms of posets, $$[u,q^\alpha w]_k^q
    \ \simeq\ 
    [\mathfrak ou, q^{\mathfrak o(u,w)} q^\alpha \mathfrak ow]_k^q
     \ \simeq\ 
    [w_0 uw_0,q^{w_0(\alpha)} w_0 w w_0]_{n-k}^q
    \ \simeq\ 
    \textit{op}\left([ww_0,q^{w_0(\alpha)} u w_0]_{n-k}^q\right)\,.$$
:::

::: example
Figure [1](#F:three_ops){reference-type="ref" reference="F:three_ops"} illustrates Corollary [\[C:equivalences\]](#C:equivalences){reference-type="ref" reference="C:equivalences"} on the rightmost interval of Figure [\[F:more_minimal\]](#F:more_minimal){reference-type="ref" reference="F:more_minimal"}.

<figure id="F:three_ops">
<div class="picture">
<p>(140,110)(-60,0) (-35,0)<span><embed src="q-int3.eps" /></span></p>
<p>(-13,100)<span><span class="math inline">$q_{1,4}q_3132\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}45$</span></span> (-10, 75)<span><span class="math inline">$q_{1,4}135\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}42$</span></span> (42,75)<span><span class="math inline">$q_3532\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}41$</span></span> (-60,50)<span><span class="math inline">$q_{1,4}125\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}43$</span></span> (-10, 50)<span><span class="math inline">$q_{1,4}134\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}52$</span></span> (42,50)<span><span class="math inline">$q_3531\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}42$</span></span> (-60,25)<span><span class="math inline">$q_{1,4}124\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}53$</span></span> (0, 25)<span><span class="math inline">$534\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}12$</span></span> (42,25)<span><span class="math inline">$q_3521\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}43$</span></span> (0, 0)<span><span class="math inline">$524\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}13$</span></span></p>
</div>
<div class="picture">
<p>(115,110)(-35,0) (-25,0)<span><embed src="q-int2.eps" /></span> (-10,100)<span><span class="math inline">$q_{1,3}23\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}541$</span></span> (0, 75)<span><span class="math inline">$53\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}241$</span></span> (35,75)<span><span class="math inline">$q_{1,3}13\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}542$</span></span> (-35,50)<span><span class="math inline">$43\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}251$</span></span> (0, 50)<span><span class="math inline">$52\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}341$</span></span> (45,50)<span><span class="math inline">$53\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}142$</span></span> (-35,25)<span><span class="math inline">$42\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}351$</span></span> (0, 25)<span><span class="math inline">$51\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}342$</span></span> (45,25)<span><span class="math inline">$43\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}152$</span></span> (0, 0)<span><span class="math inline">$41\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}352$</span></span></p>
</div>
<div class="picture">
<p>(145,110)(-50,0) (-25,0)<span><embed src="q-int4.eps" /></span> ( 0,100)<span><span class="math inline">$q_{1,3}25\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}314$</span></span> (-50,75)<span><span class="math inline">$q_{1,3}24\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}315$</span></span> ( 0, 75)<span><span class="math inline">$q_{1,3}15\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}324$</span></span> (50,75)<span><span class="math inline">$q_{1,3}23\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}514$</span></span> (-50,50)<span><span class="math inline">$q_{1,3}23\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}415$</span></span> ( 0, 50)<span><span class="math inline">$q_{1,3}14\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}325$</span></span> (50,50)<span><span class="math inline">$q_{1,3}13\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}524$</span></span> ( 0, 25)<span><span class="math inline">$q_{1,3}13\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}425$</span></span> (60,25)<span><span class="math inline">$53\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}124$</span></span> (10, 0)<span><span class="math inline">$43\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}125$</span></span></p>
</div>
<figcaption>Actions of <span class="math inline">𝔬</span>, <span class="math inline"><em>ω</em><sub>0</sub></span>, and <span class="math inline"><em>ρ</em></span> on the rightmost interval of Figure <a href="#F:more_minimal" data-reference-type="ref" data-reference="F:more_minimal">[F:more_minimal]</a>.</figcaption>
</figure>

These operators act on each chain in the respective orders. Each row in Figure [2](#F:symmetry-chains){reference-type="ref" reference="F:symmetry-chains"} shows

<figure id="F:symmetry-chains">
<p><span class="math inline">$\begin{array}{rccccccccc}
    &amp;\valuediagram[padding=1]{{4,1},{1,2},{3,4},{4,5}}&amp;\ &amp;\valuediagram[padding=1]{{4,1},{3,4},{1,2},{4,5}}&amp;\ &amp;
    \valuediagram[padding=1]{{4,1},{3,4},{4,5},{1,2}}&amp;\ &amp;\valuediagram[padding=1]{{4,5},{5,1},{3,5},{1,2}}&amp;\ &amp;
    \valuediagram[padding=1]{{4,5},{5,1},{1,2},{3,5}}\\[1ex]
    \raisebox{5pt}{$\mathfrak o$}
    &amp;\valuediagram[padding=1]{{5,2},{2,3},{4,5},{5,1}}&amp;\ &amp;\valuediagram[padding=1]{{5,2},{4,5},{2,3},{5,1}}&amp;\ &amp;
    \valuediagram[padding=1]{{5,2},{4,5},{5,1},{2,3}}&amp;\ &amp;\valuediagram[padding=1]{{5,1},{1,2},{4,1},{2,3}}&amp;\ &amp;
    \valuediagram[padding=1]{{5,1},{1,2},{2,3},{4,1}}\\[1ex]    
    \raisebox{5pt}{$\omega_0$}
    &amp;\valuediagram[padding=1]{{5,2},{4,5},{2,3},{1,2}}&amp;\ &amp;\valuediagram[padding=1]{{5,2},{2,3},{4,5},{1,2}}&amp;\ &amp;
    \valuediagram[padding=1]{{5,2},{2,3},{1,2},{4,5}}&amp;\ &amp;\valuediagram[padding=1]{{1,2},{5,1},{1,3},{4,5}}&amp;\ &amp;
    \valuediagram[padding=1]{{1,2},{5,1},{4,5},{1,3}}\\[1ex]   
    \raisebox{5pt}{$\rho$}
    &amp;\valuediagram[padding=1]{{4,5},{3,4},{1,2},{4,1}}&amp;\ &amp;\valuediagram[padding=1]{{4,5},{1,2},{3,4},{4,1}}&amp;\ &amp;
    \valuediagram[padding=1]{{1,2},{4,5},{3,4},{4,1}}&amp;\ &amp;\valuediagram[padding=1]{{1,2},{3,5},{5,1},{4,5}}&amp;\ &amp;
    \valuediagram[padding=1]{{3,5},{1,2},{5,1},{4,5}}
    \end{array}$</span></p>
<figcaption>Actions of <span class="math inline">𝔬</span>, <span class="math inline"><em>ω</em><sub>0</sub></span>, and <span class="math inline"><em>ρ</em></span> on chains from rightmost interval of Figure <a href="#F:more_minimal" data-reference-type="ref" data-reference="F:more_minimal">[F:more_minimal]</a>.</figcaption>
</figure>

the diagrams for all five chains in one of the four intervals, with the first row from the rightmost interval of Figure [\[F:more_minimal\]](#F:more_minimal){reference-type="ref" reference="F:more_minimal"} and subsequent rows for the indicated interval in Figure [1](#F:three_ops){reference-type="ref" reference="F:three_ops"}.$\diamond$
:::

As mentioned in Section [\[quantum-equals-classical\]](#quantum-equals-classical){reference-type="ref" reference="quantum-equals-classical"}, we are often able to reduce to the classical (no quantum operators) case, which is the origin of our interest in these operators $\mathfrak o$, $\omega_0$ and $\rho$.
