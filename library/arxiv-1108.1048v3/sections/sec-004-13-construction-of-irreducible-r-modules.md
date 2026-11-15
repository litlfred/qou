---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS"
section_id: sec-004-13-construction-of-irreducible-r-modules
section_title: "Construction of irreducible R-modules"
section_number: 1.3
pages: 10-14
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.884
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS — We give an explicit construction of irreducible modules over Khovanov-Lauda- Rouquier algebras R and their"
---
In this subsection, we give a construction of irreducible graded $R$-modules as the irreducible heads of certain induced modules, which is compatible with the Kashiwara operators. More precisely, set $I_{(n+1)} = I$ and let $I_{(k)} \subset I\ (k=1, \ldots,n)$ be subsets of $I$ such that $I_{(k)} \subseteq I_{(k+1)}$ and $|I_{(k)}| = k$. Let $\mathfrak{B}_k$ be the crystal obtained from $B(\infty)$ by forgetting the $i$-arrows for $i \notin  I_{(k)}$. Using highest weight vectors of connected components of $\mathfrak{B}_k$, we define irreducible $R$-modules $\mathcal{N}_k(v)$ for $k=1,\ldots,n$ and $v \in B(\infty)$. Then, we construct a crystal isomorphism $\Phi: B(\infty) \rightarrow \mathbb{B}(\infty)$ defined by $\Phi(v) = \mathsf{ hd}\,\mathsf {Ind}(\mathcal{N}_1(v) \boxtimes \cdots \boxtimes \mathcal{N}_n(v))$ (Proposition [\[Prop: crystal iso\]](#Prop: crystal iso){reference-type="ref" reference="Prop: crystal iso"}). We emphasize that this crystal isomorphism $\Phi$ exists for an arbitrary symmetrizable Cartan datum.

For $M \in R(\beta)\text{-}\mathsf{fmod}$, $M_k \in R(\beta_k)\text{-}\mathsf{fmod}$ ($k =1,\ldots, m$) and $d \in \mathbb{Z}_{>0}$, set $$\begin{aligned}
M^{\boxtimes 0} = \mathbb{C}, \qquad M^{\boxtimes d} = \underbrace{M\boxtimes \cdots \boxtimes M}_d \qquad
\overset{m}{\underset{k=1}{\boxtimes}}  M_k = M_1 \boxtimes \cdots \boxtimes M_m.
\end{aligned}$$

::: lemma
[]{#Lem: irr of induced module label="Lem: irr of induced module"} Let $M_k \in R(\beta_k)\text{-}\mathsf{fmod}$,  $d_k \in \mathbb{Z}_{\ge 0}$, and $\mathbf{i}_k \in I^{d_k \beta_k}$ for $k = 1, \ldots, m$. Suppose that $\mathbf{i}_k$ occurs in $\mathsf{ ch}\,\mathsf {Ind}(M_k^{\boxtimes d_k})$ with multiplicity $\xi_k \in \mathbb{Z}_{>0}$ for $k = 1, \ldots, m$. Assume

1.  $\mathsf {Ind}\left(M_k \boxtimes M_{k'}\right) \simeq \mathsf {Ind}\left(M_{k'} \boxtimes M_k\right)$ for $k,k'=1, \ldots,m$,

2.  $\mathsf {Ind}\left(M_k^{\boxtimes d_k}\right)$ is irreducible for $k=1, \ldots,m$, and

3.  $\mathbf{i} := \mathbf{i}_1 * \cdots *\mathbf{i}_m$ occurs in $\mathsf{ ch}\,\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  M_k^{\boxtimes d_k}
    \right)$ with multiplicity $\xi_1 \xi_2 \cdots \xi_m$.

Then $\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  M_k^{\boxtimes d_k}\right)$ is irreducible.
:::

::: proof
*Proof.* Let $N_k = \mathsf {Ind}\left(M_k^{\boxtimes d_k}\right)$ for $k=1, \ldots, m$, and let $Q$ be a nonzero quotient of the module $\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}} 
N_k\right)$. By (ii) and Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} (2), we have an injective homomorphism $$\overset{m}{\underset{k=1}{\boxtimes}}  N_k    \hookrightarrow {\mathsf{Res}}_{d_1 \beta_1, \ldots, d_m \beta_m} Q.$$ Hence, by (iii),  $\mathbf{i}$ occurs in $\mathsf{ ch}Q$ with multiplicity $\xi_1 \xi_2\cdots \xi_m$. Since $Q$ is arbitrary, we obtain that $\mathsf{ hd}\,\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  N_k\right)$ is irreducible.

Now it follows from (i) that $$\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  N_k\right) \simeq \mathsf {Ind}\left(N_m \boxtimes N_{m-1} \boxtimes \cdots \boxtimes N_1\right).$$ Let $L$ be a nonzero submodule of $\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  N_k\right)$. By $\rm (ii)$ and Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"}, there exists a surjective homomorphism $${\mathsf{Res}}L \twoheadrightarrow \overset{m}{\underset{k=1}{\boxtimes}}  N_k,$$ which implies that $\mathbf{i}$ occurs in $\mathsf{ ch}L$ with multiplicity $\xi_1 \xi_2\cdots \xi_m$ by $\rm (iii)$. Therefore, we conclude $\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  N_k\right) = \mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  M_k^{\boxtimes d_k}\right)$ is irreducible. ◻
:::

::: lemma
[]{#Lem: sum of fi label="Lem: sum of fi"} Let $\emptyset = I_{(0)} \subsetneq I_{(1)} \subsetneq I_{(2)} \subsetneq \cdots \subsetneq I_{(m)} \subset I$, and assume $\beta_k \in \sum_{i \in I_{(k)}} \mathbb{Z}_{\ge0}\alpha_i$ for $k=1,\ldots, m$. Let $M_k \in R(\beta_{k})\text{-}\mathsf{fmod}\ \ (1 \le k \le m)$ be such that

1.  $\varepsilon_i(M_k)=0$ for $i \in I_{(k-1)}$,

2.  $\mathsf{ hd}M_k$ is irreducible, and

3.  $\mathsf{ hd}M_k$ occurs with multiplicity one as a composition factor of $M_k$.

Then

1.  $\mathsf{ hd}\,\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}} M_k\right)$ is irreducible,

2.  $\mathsf{ hd}\,\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}} M_k\right)$ occurs with multiplicity one as a composition factor of $\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}} M_k\right)$,

3.  if $\tilde{f}_{\mathbf{i}_k} \mathbf{1} \simeq \mathsf{ hd}M_k$ for some $\mathbf{i}_k \in I^{\beta_{k}}$, then $\tilde{f}_{\mathbf{i}_1} \tilde{f}_{\mathbf{i}_2} \cdots  \tilde{f}_{\mathbf{i}_{m}} \mathbf{1} \simeq \mathsf{ hd}\,\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}} M_k\right)$.
:::

::: proof
*Proof.* We may assume that $M_k \ne \mathbf{1}$ for $k=1, \ldots, m$. Let $d_k = |\beta_k|$ for $k=1,\ldots,m$, and set $d = d_1 + \cdots + d_m$. For $w\in S_d$ and a reduced expression $w = \sigma_{i_1}\cdots \sigma_{i_s}$, let $$\tau_w = \tau_{i_1}\cdots \tau_{i_s}.$$ For $k=1,\ldots,m$, take $\mathbf{i}_k = (i_{k,1}, \ldots,  i_{k,d_{k}}) \in I^{\beta_{k}}$ such that $e({\mathbf{i}_k}) M_k \ne 0$. It follows from (i) that $i_{k,1} \in I_{(k)} \setminus I_{(k-1)}$. Since $M_k \in R(\beta_{k})\text{-}\mathsf{fmod}$, we have $$e({\beta_1, \ldots, \beta_{m}}) \tau_w e({\mathbf{i}_1* \cdots *\mathbf{i}_{m}}) \ne 0 \ \ \text{ if and only if } w =  \mathsf{id}$$ for $w \in S_{d} / S_{d_1} \times \cdots \times S_{d_m}$. Therefore, $${\mathsf{Res}}_{\beta_1, \ldots, \beta_m} \Big(\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}} M_k\Big) \Big) \simeq \overset{m}{\underset{k=1}{\boxtimes}} M_k.$$

Let $L =  \overset{m}{\underset{k=1}{\boxtimes}}  \mathsf{ hd}M_k$. It follows from (ii) and (iii) that $[L]$ occurs with multiplicity one in $[
{\mathsf{Res}}_{\beta_1, \ldots, \beta_m} \Big(\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}} M_k\Big)
\Big) ]$ in the Grothendieck group $G_0(R(\beta_1) \otimes \cdots
\otimes R(\beta_m))$. Let $Q$ be a nonzero quotient of $\mathsf {Ind}\Big(
\overset{m}{\underset{k=1}{\boxtimes}} M_k\Big)$. By Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"}, we have a nontrivial homomorphism $$\overset{m}{\underset{k=1}{\boxtimes}} M_k  \rightarrow {\mathsf{Res}}_{\beta_1, \ldots, \beta_m} Q,$$ which implies that $[L]$ occurs in $[{\mathsf{Res}}_{\beta_1, \ldots, \beta_m} Q]$ with multiplicity one. Since $Q$ is arbitrary, we obtain assertions (1) and (2).

Now assume that $N = \mathsf{ hd}\,\mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}} M_k\Big )$, and let $N_k = \mathsf{ hd}M_k$ for $k=1,\ldots, m$. Then there is a surjective homomorphism $$\mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}} M_k\Big) \twoheadrightarrow \mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}} N_k\Big) ,$$ which implies that $N = \mathsf{ hd}\,\mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}} N_k\Big)$. We will use induction on $|\mathsf{wt}(N)|$. If $|\mathsf{wt}(N)|=0$, there is nothing to prove, so suppose that $|\mathsf{wt}(N)|>0$. Since $N_1$ is nontrivial, we can take $i \in I_{(1)}$ such that $\varepsilon_i(N_1) \ne 0$. Let $\varepsilon = \varepsilon_i(N_1).$ Then, by $\rm (i)$ and Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"}, we have $$\varepsilon = \varepsilon_i\Big(\mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}} N_k\Big)\Big) = \varepsilon_i(N) .$$ Since $e_i$ is exact, there is a surjective homomorphism $$e_i^\varepsilon \left( \mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}} N_k\Big) \right) \twoheadrightarrow e_i^{\varepsilon}N.$$ Then, by [@KP10 Lem. 3.9], we know that $[e_i^{\varepsilon} N]  = q_{i}^{-\varepsilon + 1}\, [\varepsilon]_{q_i} !\,[  \tilde{e}_i^{\varepsilon}N]$ and $$\begin{aligned}
\Big[e_i^\varepsilon\Big ( \mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}} N_k\Big)\Big)\Big] & =  [\mathsf {Ind}\left((e_i^\varepsilon N_1)\boxtimes N_2 \boxtimes \cdots \boxtimes N_{m})\right] \\
& = q_i^{-\varepsilon + 1} [\varepsilon]_{q_i} ! \, [\mathsf {Ind}\left(( \tilde{e}_i^\varepsilon N_1)\boxtimes N_2 \boxtimes \cdots \boxtimes N_{m}\right)]
\end{aligned}$$ at the level of the Grothendieck group $G_0(R( \beta_1 + \cdots + \beta_m - \varepsilon \alpha_i))$. Since $\mathsf{ hd}\,\mathsf {Ind}( ( \tilde{e}_i^\varepsilon N_1)\boxtimes N_2 \boxtimes \cdots \boxtimes N_{m})$ is irreducible by $(1)$, we obtain $$\mathsf{ hd}\,\mathsf {Ind}( \tilde{e}_i^{\varepsilon}N_1 \boxtimes \cdots \boxtimes N_{m}) \simeq  \tilde{e}_i^{\varepsilon} N.$$ Therefore, assertion (3) follows from a standard induction argument. ◻
:::

Let $n = |I|$ be the rank of $U_q(\mathfrak{g})$, and let $I_{(k)} \subset I\ (k=1,\ldots,n)$ be subsets of $I = I_{(n+1)}$ such that $I_{(k)} \subset I_{(k+1)}$ and $|I_{(k)}|=k$ for all $k$. We denote by $U_q(\mathfrak{g}_k)$ the subalgebra of $U_q(\mathfrak{g})$ generated by $e_i,\ f_i\ (i\in I_{(k)})$ and $q^h\ (h \in \mathsf{P}^{\vee})$. Let $\mathfrak{B}_k$ be the crystal obtained from $B(\infty)$ by forgetting the $i$-arrows for $i \notin  I_{(k)}$. Then $\mathfrak{B}_k$ can be viewed as a $U_q(\mathfrak{g}_k)$-crystal.

::: lemma
For each $k=1,\ldots, n$, every connected component of $\mathfrak{B}_k$ has a unique highest weight vector.
:::

::: proof
*Proof.* Let $\mathcal{C}$ be a connected component of $\mathfrak{B}_k$. For $\lambda \in \mathsf{P}^+$, let $\iota_\lambda : B(\lambda) \rightarrow B(\infty)\otimes T_\lambda \otimes C$ be the embedding in $\eqref{Eq: crystal embedding}$ and let $$\widetilde{ \mathcal{C}} = \{ v \otimes t_\lambda \otimes c \mid  v \in \mathcal{C} \} \subset B(\infty) \otimes T_\lambda \otimes C.$$ By taking $\lambda \gg 0$, we can assume that $\widetilde{ \mathcal{C}} \cap {\mathsf {im}}(\iota_\lambda) \ne \emptyset.$ Since $\mathcal{C}_\lambda: = \iota_\lambda^{-1}(\widetilde{ \mathcal{C}})$ is a nontrivial highest weight subcrystal of the crystal obtained from $B(\lambda)$ by forgetting the $i$-arrows with $i \notin I_{(k)}$, there is an element $u_{\mathcal{C}} \in \mathcal{C}$ such that $\iota_\lambda^{-1}(u_{\mathcal{C}} \otimes t_\lambda \otimes c)$ is the highest weight vector of the subcrystal $\mathcal{C}_\lambda$. Note that $u_\mathcal{C}$ does not depend on the choice of $\lambda$ if $\widetilde{ \mathcal{C}} \cap {\mathsf {im}}(\iota_\lambda) \ne \emptyset$. By construction, the element $u_\mathcal{C}$ is a unique highest weight vector of $\mathcal{C}$. ◻
:::

Take $v \in B(\infty)$. Let $u_0 = v$ and let $u_k$ be the highest weight vector of the connected component $\mathcal{C}_k$ of $\mathfrak{B}_k$ containing $v$ for $k=1,\ldots, n$. By construction, there is a chain of injective maps $$\mathcal{C}_1 \hookrightarrow \mathcal{C}_2 \hookrightarrow \cdots \hookrightarrow \mathcal{C}_{n-1} \hookrightarrow B(\infty).$$ For $k=1,\ldots, n$, let $\mathbf{i}_k$ be a sequence of $I$ such that $u_{k-1} =  \tilde{f}_{\mathbf{i}_k} u_{k}$. Note that $v =  \tilde{f}_{\mathbf{i}_1}  \tilde{f}_{\mathbf{i}_1} \cdots  \tilde{f}_{\mathbf{i}_{n}} \mathsf{1}$. Let $$\begin{aligned}
 \label{Eq: def of Nk}
\mathcal{N}_k(v) =  \tilde{f}_{\mathbf{i}_k} \mathbf{1} \in \mathbb{B}(\infty) .
\end{aligned}$$ Hence, for each $v\in B(\infty)$, we have the corresponding $n$-tuple $(\mathcal{N}_1(v), \mathcal{N}_2(v), \ldots, \mathcal{N}_{n}(v))$ of modules in $\mathbb{B}(\infty)$.

::: proposition
[]{#Prop: crystal iso label="Prop: crystal iso"}  

1.  For $v \in B(\infty)$, let $\mathcal{N}_k(v)$ be the irreducible module defined by $\eqref{Eq: def of Nk}$. Then $\mathsf{ hd}\,\mathsf {Ind}\left( \overset{n}{\underset{k=1}{\boxtimes}}  \mathcal{N}_k(v)\right)$ is irreducible.

2.  The map $\Phi: B(\infty) \longrightarrow \mathbb{B}(\infty)$ defined by $$\Phi(v) = \mathsf{ hd}\,\mathsf {Ind}\left( \overset{n}{\underset{k=1}{\boxtimes}}  \mathcal{N}_k(v)\right) \ \  \text{ for } v \in B(\infty)$$ is a crystal isomorphism.
:::

::: proof
*Proof.* Since it is obvious that $\Phi(\mathsf{1}) = \mathbf{1}$, we assume $\mathsf{1} \ne v \in B(\infty)$ and let $\mathcal{N}_k(v) =  \tilde{f}_{\mathbf{i}_k} \mathbf{1}$ be the corresponding irreducible module given in $\eqref{Eq: def of Nk}$ for $k=1, \cdots, n$. By construction, we have $$v =  \tilde{f}_{\mathbf{i}_1}  \tilde{f}_{\mathbf{i}_1} \cdots  \tilde{f}_{\mathbf{i}_{n}} \mathsf{1}\ \  \text{ and }\ \   \varepsilon_i( \mathcal{N}_k(v)) = 0
\ \ \text{ for all }  i\in I_{(k-1)}.$$ Therefore, it follows from Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"} that $\mathsf{ hd}\,\mathsf {Ind}\left( \overset{n}{\underset{k=1}{\boxtimes}}  \mathcal{N}_k(v) \right)$ is irreducible and $$\Phi(   \tilde{f}_{\mathbf{i}_1}  \tilde{f}_{\mathbf{i}_2} \cdots  \tilde{f}_{\mathbf{i}_{n}} \mathsf{1} )
= \mathsf{ hd}\,\mathsf {Ind}\left( \overset{n}{\underset{k=1}{\boxtimes}}  \mathcal{N}_k(v)\right) =  \tilde{f}_{\mathbf{i}_1}  \tilde{f}_{\mathbf{i}_2}
\cdots  \tilde{f}_{\mathbf{i}_{n}} \Phi(\mathsf{1}).$$ ◻
:::
