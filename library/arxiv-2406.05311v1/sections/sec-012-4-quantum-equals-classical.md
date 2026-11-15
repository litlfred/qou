---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-012-4-quantum-equals-classical
section_title: "Quantum equals classical"
section_number: 4
pages: 12-15
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.97
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#quantum-equals-classical label="quantum-equals-classical"}

A recurring theme in quantum Schubert calculus is that oftentimes the numerical part ${\color{RoyalBlue}N^{w,\alpha}_{u,v}}\vcentcolon=q^{-\alpha}C^{q^\alpha w}_{u,v}(\in{\mathbb N})$ of a quantum Littlewood--Richardson number (a Gromov--Witten invariant) is naturally identified with a related classical Littlewood--Richardson number $c^{w'}_{u',v'}$. This is seen in the quantum Monk formula [\[quantum-Monk-formula\]](#quantum-Monk-formula){reference-type="eqref" reference="quantum-Monk-formula"} in which these numerical parts are all 1 as in the classical Monk formula [\[classical-Monk-formula\]](#classical-Monk-formula){reference-type="eqref" reference="classical-Monk-formula"}. Bertram's quantum Giambelli formula [@Bertram] and the results of Buch, Kresch, and Tamvakis [@BKT] are other examples. Leung and Li [@LeungLi2012] discuss this thoroughly and then establish very general results, including some that naturally identify different Gromov--Witten invariants on the same flag variety. Their result is type-free and expressed in the language of algebraic groups, and they use it to deduce a weaker version of the result we need, Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"}. We first state some results from [@LeungLi2012] for the type A flag variety using the notation from Section [\[S:qCoh\]](#S:qCoh){reference-type="ref" reference="S:qCoh"} and extract a useful statement from one of their proofs, from which we deduce Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"}.

Fix $i\in[n{-}1]$. Let ${\color{RoyalBlue}e_i}\vcentcolon=(0,\dotsc,0,1,0,\dotsc,0)$ be the $i$th standard basis vector, so that $q^{e_i}=q_i$. Write ${\color{RoyalBlue}s_i}\vcentcolon=(i,i{+}1)$, the $i$th simple transposition. We will also need the linear map $\varpi_i\colon{\mathbb Z}^{n-1}\to{\mathbb Z}$, defined by ${\color{RoyalBlue}\varpi_i}(\alpha)\vcentcolon=-\alpha_{i-1}+2\alpha_i-\alpha_{i+1}$, where $\alpha_0=\alpha_n=0$. Thus

$$\begin{gathered}
   \qquad  q_{2,4}=q^{(01100)}=q^{e_2+e_3}\,,   \qquad
   6{\color{red}\underline{35}}214 s_2\ =\ 6{\color{red}\underline{53}}214\,,\quad
   63{\color{red}\underline{52}}14 s_3\ =\ 63{\color{red}\underline{25}}14\,, \\
   \varpi_2(\underline{122}32)\ =\ -1+4-2=1\,,\quad \mbox{ and }\quad  \varpi_4(12\underline{232})\ =\ -2+6-2=2\,.\qquad 
 
\end{gathered}$$ For $i\in[n{-}1]$, we also define a map ${\color{RoyalBlue}{\mbox{\rm sg}}_i}\colon S_n\to\{0,1\}$ which records whether or not $u\lessdot_i
 us_i$, $${\mbox{\rm sg}}_i(u)\ \vcentcolon=\ \left\{ \begin{array}{rcl}
       1& &\mbox{if\ } u s_i\lessdot_i  u     \quad\mbox{equivalently, if\ } u(i+1)<u(i)
      \\
       0& &\mbox{if\ } u    \lessdot_i  u s_i \quad\mbox{equivalently, if\ } u(i)<u(i+1)
    \end{array}\right. .$$ That is, ${\mbox{\rm sg}}_i(u)=1$ when $u$ has a descent at $i$ and it equals $0$ when $u$ has an ascent at $i$.

::: proposition
 [@LeungLi2012 Theorem 1.1][]{#P:LL_Th1.1 label="P:LL_Th1.1"} Let $x,y,z\in S_n$ and $\alpha\in{\mathbb N}^{n-1}$.

1.  We have that $N^{z, \alpha}_{x,y}=0$ unless ${\mbox{\rm sg}}_i(z)+\varpi_i(\alpha) \leq {\mbox{\rm sg}}_i(x)+{\mbox{\rm sg}}_i(y)$ for all $i\in[n{-}1]$.

2.  Suppose that ${\mbox{\rm sg}}_i(z)+\varpi_i(\alpha) = {\mbox{\rm sg}}_i(x)+{\mbox{\rm sg}}_i(y)=2$ for some $i\in[n{-}1]$, then $$N^{z,\alpha}_{x,y}\ =\ N^{z,\alpha-e_i}_{x s_i, y s_i}\ =\ \left\{ \begin{array}{lcl}
                     N^{z s_i, \alpha-e_i}_{x, ys_i}& &\mbox{if\/\ } {\mbox{\rm sg}}_i(z)=0\vspace{5pt}\\
                     N^{z s_i, \alpha}_{x, ys_i}&  &\mbox{if\/\ } {\mbox{\rm sg}}_i(z)=1\end{array}\right. .$$
:::

Note that if $N^{w,\alpha}_{u,v}\neq 0$, then by part (1), we have $\varpi_i(\alpha)\leq 2$ for each $i\in[n{-}1]$. This also constrains $u,v,w$. For example, if $N^{w,\alpha}_{u,v(\lambda,k)}\neq 0$ and $i\neq k$, then ${\mbox{\rm sg}}_i(v(\lambda,k))=0$ and Proposition [\[P:LL_Th1.1\]](#P:LL_Th1.1){reference-type="ref" reference="P:LL_Th1.1"}(1) becomes

$$\label{Eq:Grass_bound}
  {\mbox{\rm sg}}_i(w)\ +\ \varpi_i(\alpha)\ \leq\ {\mbox{\rm sg}}_i(u)\ \leq\ 1\,.$$

We first recall two lemmas from [@LeungLi2012].

::: proposition
[]{#P:LL_lemmas label="P:LL_lemmas"} Suppose that $\alpha\in{\mathbb N}^{n-1}$ is a nonnegative nonzero exponent vector.

1.  *([@LeungLi2012 Lemma 2.8])* There is an $i\in[n{-}1]$ with $\varpi_i(\alpha)>0$.

2.  *([@LeungLi2012 Lemma 2.10])* If $\varpi_i(\alpha)>0$ for a unique $i\in[n{-}1]$, then $\varpi_i(\alpha)\geq 2$.
:::

If $N^{w,\alpha}_{u,v(\lambda,k)}\neq 0$ and $i\neq k$ in Proposition [\[P:LL_lemmas\]](#P:LL_lemmas){reference-type="ref" reference="P:LL_lemmas"}(1), then $\varpi_i(\alpha)=1$ as $\varpi_i(\alpha)>1$ contradicts [\[Eq:Grass_bound\]](#Eq:Grass_bound){reference-type="eqref" reference="Eq:Grass_bound"}, and this implies that ${\mbox{\rm sg}}_i(u)=1$ and ${\mbox{\rm sg}}_i(w)=0$.

Theorem 1.2 in [@LeungLi2012] is their "quantum equals classical" result. It states that if $N^{w, \alpha}_{u,v(\lambda,k)}\neq 0$, then there exist $w',u'\in S_n$ such that $N^{w, \alpha}_{u,v(\lambda,k)}=N^{w', {{\mathbf 0}}}_{u',v(\lambda,k)}= c^{w'}_{u',v(\lambda,k)}$. A consequence of their proof is that $w u^{-1}=w'(u')^{-1}$, but we require more than that. We state and prove the result we will need; this is extracted from the proof of Theorem 1.2 in [@LeungLi2012].

::: proposition
[]{#P:LLThm1.2 label="P:LLThm1.2"} Suppose that $u,w\in S_n$, $\lambda$ is a partition, $\alpha\in{\mathbb N}^{n-1}$ is nonzero, and $N^{w,\alpha}_{u,v(\lambda,k)}\neq 0$.

1.  There exists $i\in[n{-}1]$ such that ${\mbox{\rm sg}}_i(u)=1$, ${\mbox{\rm sg}}_i(w)=0$, and $$\mbox{either }\ \varpi_i(\alpha) = 1\ \mbox{if }i\neq k
        \quad\mbox{or}\quad
        \varpi_i(\alpha) = 2\ \mbox{if }i= k    \,.$$

2.  For any partition $\mu$ with $|\mu|=|\lambda|$, with $i$ as in (1), we have $N^{w,\alpha}_{u,v(\mu,k)}=N^{ws_i, \alpha-e_i}_{us_i,v(\mu,k)}$.
:::

::: proof
*Proof.* We first prove statements (1) and (2) in the case when $\mu=\lambda$. By Proposition [\[P:LL_lemmas\]](#P:LL_lemmas){reference-type="ref" reference="P:LL_lemmas"}(1), there is an $i\in[n{-}1]$ such that $\varpi_i(\alpha)>0$. Suppose that $i$ is not unique with this property. Then we may assume that $i\neq k$, from which it follows that ${\mbox{\rm sg}}_i(v(\lambda, k)) = 0$. As $N^{w,\alpha}_{u,v(\lambda,k)}\neq 0$, Equation [\[Eq:Grass_bound\]](#Eq:Grass_bound){reference-type="eqref" reference="Eq:Grass_bound"} implies that ${\mbox{\rm sg}}_i(u)=1=\varpi_i(\alpha)$ and ${\mbox{\rm sg}}_i(w)=0$. Thus ${\mbox{\rm sg}}_i(ws_i)=1={\mbox{\rm sg}}_i(v(\lambda,k)s_i)$, so that $${\mbox{\rm sg}}_i(ws_i)\ +\ \varpi_i(\alpha)\ =\ {\mbox{\rm sg}}_i(u)\ +\ {\mbox{\rm sg}}_i(v(\lambda,k) s_i)\ =\ 2\,.$$ By Proposition [\[P:LL_Th1.1\]](#P:LL_Th1.1){reference-type="ref" reference="P:LL_Th1.1"}(2) with $x=u$, $y=v(\lambda,k) s_i$, and $z=w s_i$, we have that $$N^{ ws_i,\alpha}_{u, v(\lambda,k) s_i}\ =\ N^{ws_i, \alpha-e_i}_{u s_i, v(\lambda,k)}\ =\ N^{w,\alpha}_{u,v(\lambda,k)}\,.$$ (As $s_i^2=1$ and ${\mbox{\rm sg}}_i(z)={\mbox{\rm sg}}_i(ws_i)=1$).

Now suppose that there is a unique $i$ with $\varpi_i(\alpha)>0$. Then by Proposition [\[P:LL_lemmas\]](#P:LL_lemmas){reference-type="ref" reference="P:LL_lemmas"}(2), we have $\varpi_i(\alpha)\geq 2$. As $N^{w,\alpha}_{u,v(\lambda,k)}\neq  0$, Proposition [\[P:LL_Th1.1\]](#P:LL_Th1.1){reference-type="ref" reference="P:LL_Th1.1"}(1) implies that $${\mbox{\rm sg}}_i(w)\ =\ 0\,,\ \ \ 
     \varpi_i(\alpha)\ =\ 2\,,\ \ \mbox{and}\ \
     {\mbox{\rm sg}}_i(u)\ =\ {\mbox{\rm sg}}_i(v(\lambda,k))\ = \ 1\,.$$ Since ${\mbox{\rm sg}}_i(v(\lambda,k))=1$, we must have that $i=k$, as $v(\lambda,k)$ has a unique descent at $k$. As ${\mbox{\rm sg}}_i(w)=0$, Proposition [\[P:LL_Th1.1\]](#P:LL_Th1.1){reference-type="ref" reference="P:LL_Th1.1"}(2) with $x=v(\lambda,k)$, $y=u$, and $z=w$ implies that $N^{w,\alpha}_{v(\lambda,k), u}=N^{w s_i, \alpha-e_i}_{v(\lambda,k), u s_i}$. As commutativity implies that $N^{z,\alpha}_{x,y}=N^{z,\alpha}_{y,x}$, we have $N^{ws_i, \alpha-e_i}_{u s_i,v(\lambda,k)}=N^{w,\alpha}_{u,v(\lambda,k)}$.

This proves statement (1) and statement (2), in the case when $\mu=\lambda$. The assumption that $|\mu|=|\lambda|$ implies that for all $i\in[n{-}1]$, ${\mbox{\rm sg}}_i(v(\lambda,k))={\mbox{\rm sg}}_i(v(\mu,k))$, as $v(\mu,k)$ is the identity permutation when $|\mu|=0$, and otherwise it has a unique descent at $k$. The arguments we gave for $N^{w,\alpha}_{u,v(\lambda,k)}$ will then also hold for $N^{w,\alpha}_{u,v(\mu,k)}$, which completes the proof. ◻
:::

::: lemma
[]{#L:Quantum_is_Classical label="L:Quantum_is_Classical"} Suppose that $u,w\in S_n$, $\lambda$ is a partition, $\alpha\in{\mathbb N}^{n-1}$, and $C^{q^\alpha w}_{u,v(\lambda,k)}\neq 0$. Then there exist $y,z\in S_n$ with $y\leq_k z$, $\ell(z)-\ell(y)=|\lambda|$, and $zy^{-1}=wu^{-1}$ such that for every partition $\mu$ with $|\mu|=|\lambda|$, we have $q^{-\alpha}C^{q^\alpha w}_{u,v(\mu,k)}=N^{w,\alpha}_{u,v(\mu,k)}=c^{z}_{y,v(\mu,k)}$.
:::

::: proof
*Proof.* We use induction on $|\alpha|$. Let $\alpha\in{\mathbb N}^{n-1}$. When $|\alpha|=0$, $\alpha={{\mathbf 0}}$ and $C^{q^{\bf 0}w}_{u,v(\mu,k)}=c^w_{u,v(\mu,k)}$. Suppose that $\alpha\neq{\mathbf 0}$. Let $i\in[n{-}1]$ be the index guaranteed by Proposition [\[P:LLThm1.2\]](#P:LLThm1.2){reference-type="ref" reference="P:LLThm1.2"}(1). By Proposition [\[P:LLThm1.2\]](#P:LLThm1.2){reference-type="ref" reference="P:LLThm1.2"}(2), if $\mu$ is a partition with $|\mu|=|\lambda|$, then $N^{w,\alpha}_{u,v(\mu,k)}=N^{ws_i, \alpha-e_i}_{us_i,v(\mu,k)}$. In particular, $wu^{-1}=ws_i(u s_i)^{-1}$ and $N^{ws_i, \alpha-e_i}_{us_i,v(\lambda,k)}\neq 0$, which implies that $us_i\leq_k^q q^{\alpha-e_i}w s_i$. This completes the proof. ◻
:::

::: example
[]{#Ex:q-minimal label="Ex:q-minimal"} We illustrate these results. In Example [\[Ex:MN_example\]](#Ex:MN_example){reference-type="ref" reference="Ex:MN_example"}, the term $q_{5,8}{\mathfrak S}_{(1,6,7,3,5)u}$ appears in the product ${\mathfrak S}_{u}\ast p^q_4(x_1,\dotsc,x_5)$. As $78251\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}346=(1,6,7,3,5)u$, by Equation [\[Eq:Q-powerSum\]](#Eq:Q-powerSum){reference-type="eqref" reference="Eq:Q-powerSum"}, there is a hook partition $\lambda\subseteq R_{5,3}$ with $|\lambda|=4$ such that $N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}346, q_{5,8}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}741, v(\lambda,5)}\neq 0$.

Since $q_{5,8}=q^\alpha$ for $\alpha=(0,0,0,0,1,1,1)$, we have $\varpi_7(\alpha)=1$, so that by Proposition [\[P:LLThm1.2\]](#P:LLThm1.2){reference-type="ref" reference="P:LLThm1.2"}(2), $N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}3{\color{red}46}, q_{5,{\color{red}8}}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}7{\color{red}41}, v(\lambda,5)}= N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}3{\color{red}64}, q_{5,{\color{red}7}}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}7{\color{red}14}, v(\lambda,5)}$, as $q^{\alpha-e_7}=q_{5,7}$. We may apply Proposition [\[P:LLThm1.2\]](#P:LLThm1.2){reference-type="ref" reference="P:LLThm1.2"}(2) again as $\varpi_6(\alpha-e_7)=1$ to obtain that $N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}{\color{red}36}4, q_{5,{\color{red}7}}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}{\color{red}71}4, v(\lambda,5)}= N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}{\color{red}63}4, q_{5,6}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}{\color{red}17}4, v(\lambda,5)}$.

If $\beta=\alpha-e_7-e_6$, so that $q^\beta=q_{5,6}=q_5$, then $i=5=k$ is the only index with $\varpi_i(\beta)>0$ and we have $\varpi_5(\beta)=2$. By Proposition [\[P:LLThm1.2\]](#P:LLThm1.2){reference-type="ref" reference="P:LLThm1.2"}(2) again, $N^{7825{\color{red}1\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}6}34, q_5}_{6823{\color{red}5\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}1}74, v(\lambda,5)}= c^{7825{\color{red}6\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}1}34}_{6823{\color{red}1\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}5}74, v(\lambda,5)}$. Figure [1](#F:qminimal){reference-type="ref" reference="F:qminimal"} shows the interval $[68231\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}574, 78256\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}134]_5$, which has one peakless chain (the vertical one in blue, with labels $6,3,1,3$).

<figure id="F:qminimal">
<div class="picture">
<p>(145,122)(-50,-2) (-31,0)<span><embed src="qminimal_2.eps" /></span> (0,112)<span><span class="math inline">$78256\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}134$</span></span> (-50, 84)<span><span class="math inline">$78236\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}154$</span></span> (0, 84)<span><span class="math inline">$7825{\color{red}\underline{3}}\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}164$</span></span> (-50, 56)<span><span class="math inline">$78235\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}164$</span></span> (0, 56)<span><span class="math inline">$7825{\color{red}\underline{1}}\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}364$</span></span> (50,56)<span><span class="math inline">$68253\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}174$</span></span> (-50, 28)<span><span class="math inline">$68235\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}174$</span></span> (0, 28)<span><span class="math inline">$782{\color{red}\underline{3}}1\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}564$</span></span> (50,28)<span><span class="math inline">$68251\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}374$</span></span> (0, 0)<span><span class="math inline">${\color{red}\underline{6}}8231\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}574$</span></span></p>
</div>
<div class="picture">
<p>(175,122)(-60,-2) (-41.5,0)<span><embed src="qminimal_1.eps" /></span> (-6,112)<span><span class="math inline">$q^\alpha78251\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}346$</span></span> (-60, 84)<span><span class="math inline">$78256\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}341$</span></span> (-6, 85)<span><span class="math inline">$q^\alpha78231\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}546$</span></span> (54,84)<span><span class="math inline">$q^\alpha68251\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}347$</span></span> (-60, 56)<span><span class="math inline">$78236\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}541$</span></span> (-6, 56)<span><span class="math inline">$q^\alpha68231\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}547$</span></span> (60,56)<span><span class="math inline">$68257\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}341$</span></span> (-60, 28)<span><span class="math inline">$78235\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}641$</span></span> ( 0, 28)<span><span class="math inline">$68237\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}541$</span></span> ( 0, 0)<span><span class="math inline">$68235\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}741$</span></span></p>
</div>
<figcaption>Two minimal intervals in the quantum 5-Bruhat order on <span class="math inline"><em>S</em><sub>8</sub>[<em>q</em>]</span>.</figcaption>
</figure>

As this has height 3 (as does the minimal permutation $(1,6,7,3,5)$), we see that $c^{7825{\color{red}6\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}1}34}_{6823{\color{red}1\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}5}74, v((2,1,1,0,0),5)}=1$, and thus all of the other coefficients considered above are 1.

Results in [@BS-Bruhat] also show that $c^{78256\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}134}_{68231\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}574, v((2,2,0,0,0),5)}=1$, and thus

$$\begin{aligned}
    1\ =\ c^{78256\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}134}_{68231\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}574, v((2,2,0,0,0),5)}
    &=&  N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}634, q_{5,6}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}174, v((2,2,0,0,0),5)}\\
    &=&  N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}364, q_{5,7}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}714, v((2,2,0,0,0),5)}
    \ =\ N^{78251\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}346, q_{5,8}}_{68235\raisebox{-0.3pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{6pt}}\hspace{0.55pt}741, v((2,2,0,0,0),5)}\,,
 
\end{aligned}$$

by Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"}. For $\lambda\neq(2,1,1,0,0), (2,2,0,0,0)$ with $|\lambda|=4$, these coefficients vanish.$\diamond$
:::

Observe that the intervals may change when applying a reduction as in Proposition [\[P:LLThm1.2\]](#P:LLThm1.2){reference-type="ref" reference="P:LLThm1.2"}(2), even though these reductions do not change $wu^{-1}$. Indeed, the two intervals in Figure [1](#F:qminimal){reference-type="ref" reference="F:qminimal"} demonstrate this. (In [@BS-Bruhat], it was shown that the classical interval $[u,w]_k$ depends only on $wu^{-1}$.) We show that the coefficient $N^{w,\alpha}_{u,v(\lambda,k)}$ depends only upon $wu^{-1}$.

::: theorem
[]{#Th:quantumIndependence label="Th:quantumIndependence"} For a partition $\lambda$, permutations $w,u,\overline{w},\overline{u}$ in $S_n$, exponent vectors $\alpha,\overline{\alpha}\in{\mathbb N}^{n-1}$ and indices $k,l<n$ if both coefficients $N^{w,\alpha}_{u,v(\lambda,k)}$ and $N^{\overline{w},\overline{\alpha}}_{\overline{u},v(\lambda,l)}$ are nonzero and $wu^{-1}=\overline{w}\,\overline{u}^{-1}$, then the coefficients are equal.
:::

::: proof
*Proof.* Suppose that $N^{w,\alpha}_{u,v(\lambda,k)}\neq 0$. By Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"}, there exist $y,z\in S_n$ with $y\leq_k z$ such that $\ell(z)-\ell(y)=|\lambda|$, $zy^{-1}=wu^{-1}$ and $N^{w,\alpha}_{u,v(\lambda,k)}=c^{z}_{y,v(\lambda,k)}$.

Suppose also that $N^{\overline{w},\overline{\alpha}}_{\overline{u},v(\lambda,l)}\neq 0$. By Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"} again, there exist $\overline{y},\overline{z}\in S_n$ with $\overline{y}\leq_l \overline{z}$ such that $\ell(\overline{z})-\ell(\overline{y})=|\lambda|$, $\overline{z}\,\overline{y}^{-1}=\overline{w}\,\overline{u}^{-1}$ and $N^{\overline{w},\alpha}_{\overline{u},v(\lambda,l)}=c^{\overline{z}}_{\overline{y},v(\lambda,l)}$.

Since $w u^{-1}= \overline{w}\,\overline{u}^{-1}$, we have that $zy^{-1}=\overline{z}\,\overline{y}^{-1}$. Then [@BS-Bruhat Thm. E] implies that $c^{z}_{y,v(\lambda,k)}=c^{\overline{z}}_{\overline{y},v(\lambda,l)}$, which completes the proof. ◻
:::
