---
doc_id: arxiv-2605.15740v1
doc_title: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.946
doc_brief: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´e homology"
---
In 1999, Lawrence and Zagier made a prescient observation connecting quantum invariants and modular forms [@lz]. To state their result, let $Z_{\zeta}(\mathcal{M})$ denote the Witten-Reshetikhin-Turaev (WRT) invariant of a closed and oriented 3-manifold $\mathcal{M}$ at the root of unity $\zeta$. Next let $\bm{p} = (p_1, p_2, p_3)$ be a triple of pairwise coprime positive integers and $P:=p_1 p_2 p_3$. For any triple $\bm{\ell} = (\ell_1, \ell_2, \ell_3) \in \mathbb{Z}^3$ satisfying $0 < \ell_j < p_j$, define the odd periodic function $$\begin{aligned}
\chi_{\bm{p}}^{\bm{\ell}}(n) = 
\begin{cases}
-\epsilon_1 \epsilon_2 \epsilon_3 & \text{if $n \equiv P \left( 1 + \displaystyle \sum_{j=1}^{3} \frac{\epsilon_j \ell_j}{p_j} \right) \pmod{2P}$,} \\
0 & \text{otherwise}
\end{cases}
\end{aligned}$$ where $\bm{\epsilon} = (\epsilon_1, \epsilon_2, \epsilon_3) \in \{ \pm 1 \}^3$. For $q=e^{2 \pi i \tau}$, $\tau \in \mathbb{H}$, consider the Eichler integral $$\label{ei}
\widetilde{\Phi}_{\bm{p}}^{\bm{\ell}}(\tau) := \sum_{n=0}^{\infty} \chi_{\bm{p}}^{\bm{\ell}}(n) q^{\frac{n^2}{4P}}$$ of the weight $3/2$ modular form $$\Phi_{\bm{p}}^{\bm{\ell}}(\tau) := \sum_{n=0}^{\infty} n \chi_{\bm{p}}^{\bm{\ell}}(n) q^{\frac{n^2}{4P}}.$$ Their main result [@lz Theorem 1] reads as follows. For coprime positive integers $M$ and $N$, let $\zeta_N^M := e^{\frac{2 \pi i M}{N}}$. Then for the Poincaré homology sphere $\Sigma(2,3,5)$ we have $$\label{LZ0}
1 + \zeta_N^M(1-\zeta_N^M) Z_{\zeta_N^M}(\Sigma(2,3,5)) =  -\frac{1}{2} \lim_{\tau \to \frac{M}{N}} q^{-\frac{1}{120}} \widetilde{\Phi}_{(2,3,5)}^{(1,1,1)} (\tau).$$ They also established that the right-hand side of ([\[LZ0\]](#LZ0){reference-type="ref" reference="LZ0"}) has "a modular property modulo smooth functions\", a notion which would later become the defining attribute of Zagier's quantum modular forms [@zquantum]. Any Eichler integral defined by ([\[ei\]](#ei){reference-type="ref" reference="ei"}) is now known to be an example of a quantum modular form [@go Section 4.4].

Following up on the work of Lawrence and Zagier, Hikami wrote a series of papers [@hikami1; @hikami2; @hikami3; @hikami4] wherein he showed that limiting values of Eichler integrals give the WRT invariants for several families of $3$-manifolds, including the Brieskorn homology spheres. As an application, he used the modularity to find asymptotic expansions for $Z_{\zeta_N}(\mathcal{M})$ as $N \to \infty$. Hikami's results have recently been used in the study of limiting values of an SU(2) WRT function [@am; @ahlmss; @fimt] and towards progress on a quantum modularity conjecture for WRT invariants [@ps Theorem 1].

The identity [\[LZ0\]](#LZ0){reference-type="eqref" reference="LZ0"} may be recast as an identity for $q$-hypergeometric series at roots of unity using Habiro's unified WRT invariant. Habiro [@Habiro] showed that if $\mathcal{M}$ is an integral homology sphere, there is a $q$-hypergeometric series $I(\mathcal{M};q)$ such that for any root of unity $\zeta$ one has $$I(\mathcal{M};\zeta) = Z_{\zeta}(\mathcal{M}).$$ In the case of the Poincaré homology sphere, the unified WRT invariant is [@TTQLe] $$I(\Sigma(2,3,5);q) = \frac{1}{1-q}\sum_{n \geq 0} q^n(q^{n+1})_{n+1},$$ where $$(a)_n = (a;q)_n \coloneqq \prod_{k=1}^{n} (1-aq^{k-1}).$$ Thus [\[LZ0\]](#LZ0){reference-type="eqref" reference="LZ0"} says that $$\label{LZ}
H(\zeta_N^M) = -\frac{1}{2} \lim_{\tau \to \frac{M}{N}} q^{-\frac{1}{120}} \widetilde{\Phi}_{(2,3,5)}^{(1,1,1)} (\tau),$$ where $$\label{Hbase} 
H(q) := \sum_{n \geq 0} q^n (q^n)_n.$$

Explicit expressions for $I(\mathcal{M};q)$ are uncommon as they require knowledge of the cyclotomic expansion of the colored Jones polynomial of the knot $K$ from which $\mathcal{M}$ is constructed using Dehn surgery. One case where this has been fully carried out is for the Brieskorn homology spheres $\Sigma(2,3, 6p-1)$ and $\Sigma(2,3,6p+1)$, which arise from $(-1)$-surgery and $(+1)$-surgery, respectively, along the twist knot $K_p$, $p>0$ [@hikami5 Theorem C.1]. Specifically, Hikami [@hikami5] showed that one has $$\label{h1id}
(1-q) I(\Sigma(2,3,6p-1);q) = H_p^{(1)}(q)$$ for $p>1$ and $$\label{h8id}
(1-q) I(\Sigma(2,3,6p+1);q) = H_p^{(8)}(q)$$ for $p \geq 1$ where[^1] $$\label{h1}
    H_p^{(1)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{n_p} (q^{n_p + 1})_{n_p + 1} \prod_{i=1}^{p-1} q^{n_i (n_i + 1)} \begin{bmatrix}
        n_{i+1} \\ n_i \end{bmatrix}$$ and $$\label{h8}
    H_p^{(8)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{-n_p(n_p+2)} (q^{n_p + 1})_{n_p + 1} \prod_{i=1}^{p-1} q^{n_i (n_i + 1)} \begin{bmatrix}
        n_{i+1} \\ n_i \end{bmatrix}.$$ Here $$\label{qbc}
    \begin{bmatrix} n \\ k \end{bmatrix} := \frac{(q)_n}{(q)_{n-k} (q)_k}$$ is the $q$-binomial coefficient. Combining ([\[h1id\]](#h1id){reference-type="ref" reference="h1id"}) and ([\[h8id\]](#h8id){reference-type="ref" reference="h8id"}) with expressions for the WRT invariants of the Brieskorn homology spheres in terms of Eichler integrals [@hikami1], Hikami deduced the identities [@hikami5 Theorem 3.3] $$\label{h1p}
H_p^{(1)}(\zeta_N) = (1-\zeta_N) I(\Sigma(2,3, 6p-1); \zeta_N) =  -\frac{1}{2} \lim_{\tau \to \frac{1}{N}} q^{-\frac{(6p+5)^2}{24(6p-1)}} \widetilde{\Phi}_{(2,3,6p-1)}^{(1,1,1)} (\tau)$$ for $p > 1$ and [@hikami5 Theorem 2.4 and Proposition 3.2] $$\label{h8p}
H_p^{(8)}(\zeta_N) = (1-\zeta_N) I(\Sigma(2,3, 6p+1); \zeta_N) = -\frac{1}{2}  \lim_{\tau \to \frac{1}{N}} q^{1 - \frac{(6p-5)^2}{24(6p+1)}} \widetilde{\Phi}_{(2,3,6p+1)}^{(1,1,1)} (\tau)$$ for $p \geq 1$.

In [@hikami5], Hikami conjectured a number of identities for $q$-series at roots of unity which closely resemble ([\[LZ\]](#LZ){reference-type="ref" reference="LZ"}), ([\[h1p\]](#h1p){reference-type="ref" reference="h1p"}) and ([\[h8p\]](#h8p){reference-type="ref" reference="h8p"}) but for which no interpretation in terms of quantum invariants is known. These conjectures are also presented in [@tm] and two more were made in private communication [@hikami6]. To state them, we define the following families of $q$-series. For $p \geq 1$, let $$\label{h2}
H_p^{(2)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{n_p} (q^{n_p})_{n_p} \prod_{i=1}^{p-1} q^{n_i^2} \begin{bmatrix}
n_{i+1} \\ n_i \end{bmatrix},$$ $$\label{h3}
H_p^{(3)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{2n_p} (q^{n_p + 1})_{n_p} \prod_{i=1}^{p-1} q^{n_i (n_i + 1)} \begin{bmatrix}
n_{i+1} \\ n_i \end{bmatrix},$$ $$\label{h4}
H_p^{(4)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{n_p} (q^{n_p + 1})_{n_p} \prod_{i=1}^{p-1} q^{n_i (n_i + 1)} \begin{bmatrix}
n_{i+1} \\ n_i \end{bmatrix},$$ $$\label{h5}
H_p^{(5)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{n_p} (q^{n_p + 1})_{n_p} \prod_{i=1}^{p-1} q^{n_i^2} \begin{bmatrix}
n_{i+1} \\ n_i \end{bmatrix},$$ $$\label{h6}
H_p^{(6)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{-n_p^2}(q^{n_p+1})_{n_p} \prod_{i=1}^{p-1} q^{n_i^2+n_i}\begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix}$$ and $$\label{h7}
H_p^{(7)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{-n_p^2-n_p}(q^{n_p+1})_{n_p} \prod_{i=1}^{p-1} q^{n_i^2+n_i}\begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix}.$$

In [@hikami5 (3.23), (3.25b)--(3.25d), (3.35)] and [@hikami6], the following conjectures were made.

::: conjecture
[]{#hconj label="hconj"} We have $$\label{h2conj}
H_2^{(2)}(\zeta_N) = -\frac{1}{2}  \lim_{\tau \to \frac{1}{N}} q^{-\frac{1}{264}} \widetilde{\Phi}_{(2,3,11)}^{(1,1,2)} (\tau),$$

$$\label{h3conj}
H_2^{(3)}(\zeta_N) = -\frac{1}{2}  \lim_{\tau \to \frac{1}{N}} q^{-(1 + \frac{49}{264})} \widetilde{\Phi}_{(2,3,11)}^{(1,1,3)} (\tau),$$

$$\label{h41conj}
H_1^{(4)}(\zeta_N) =  -\frac{1}{2}  \lim_{\tau \to \frac{1}{N}} q^{-\frac{49}{120}} \widetilde{\Phi}_{(2,3,5)}^{(1,1,2)} (\tau),$$

$$\label{h4conj}
H_2^{(4)}(\zeta_N) = -\frac{1}{2}  \lim_{\tau \to \frac{1}{N}} q^{-\frac{169}{264}} \widetilde{\Phi}_{(2,3,11)}^{(1,1,4)} (\tau),$$

$$\label{h5pconj}
H_p^{(5)}(\zeta_N) = -\frac{1}{2}  \lim_{\tau \to \frac{1}{N}} q^{\frac{1+48p}{24(1-6p)}} \widetilde{\Phi}_{(2,3,6p-1)}^{(1,1,3p-1)} (\tau)$$ where $p \geq 1$, $$\label{h6pconj}
H_1^{(6)}(\zeta_N) = -\frac{1}{2} \lim_{\tau \to \frac{1}{N}} q^{-\frac{25}{168}}  \widetilde{\Phi}_{(2,3,7)}^{(1,1,2)}(\tau)$$ and $$\label{h7pconj}
H_1^{(7)}(\zeta_N) = -\frac{1}{2} \lim_{\tau \to \frac{1}{N}} q^{\frac{47}{168}} \widetilde{\Phi}_{(2,3,7)}^{(1,1,3)}(\tau).$$
:::

The purpose of this paper is to use the Bailey pair machinery and a novel relation between incomplete quadratic Gauss sums with periodic coefficients to construct identities between each of the infinite families in ([\[h2\]](#h2){reference-type="ref" reference="h2"})--([\[h7\]](#h7){reference-type="ref" reference="h7"}) evaluated at roots of unity and limiting values of Eichler integrals of weight 3/2 modular forms. This gives new proofs of ([\[LZ\]](#LZ){reference-type="ref" reference="LZ"}), ([\[h1p\]](#h1p){reference-type="ref" reference="h1p"}) and ([\[h8p\]](#h8p){reference-type="ref" reference="h8p"}) as well as a proof and generalization of Conjecture [\[hconj\]](#hconj){reference-type="ref" reference="hconj"}.

The Bailey pair method also leads to the discovery of further identities between $q$-series at roots of unity and Eichler integrals. We will give two examples which involve the series $$\label{h9}
    H_p^{(9)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{-n_p^2-n_p}(q^{n_p+1})_{n_p} \prod_{i=1}^{p-1} q^{n_i^2} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix}$$ and $$\label{h10}
    H_p^{(10)}(q) := \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{-n_p^2}(q^{n_p})_{n_p} \prod_{i=1}^{p-1} q^{n_i^2} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix},$$ defined for $p \geq 1$. We now state our main result.

::: theorem
[]{#main label="main"} Let $M$ and $N$ be coprime positive integers. For $p \geq 2$, we have $$\label{main1eq}
H_p^{(1)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{-\frac{(6p+5)^2}{24(6p-1)}}\widetilde{\Phi}_{(2,3,6p-1)}^{(1,1,1)} (\tau)$$ while for $p=1$ $$\label{main11eq}
H_1^{(1)}(\zeta_N^M) = -\zeta_N^{-M} - \frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{-\frac{121}{120} }\widetilde{\Phi}_{(2,3,5)}^{(1,1,1)} (\tau).$$ For $p \geq 1$, we have $$\label{main2eq}
H_p^{(2)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{-\frac{1}{24(6p-1)}} \widetilde{\Phi}_{(2,3,6p-1)}^{(1,1,p)} (\tau),$$ $$\label{main3eq}
H_p^{(3)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{-1 - \frac{(6p-5)^2}{24(6p-1)}} \widetilde{\Phi}_{(2,3,6p-1)}^{(1,1,2p-1)} (\tau),$$ $$\label{main4eq}
H_p^{(4)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{-\frac{(6p+1)^2}{24(6p-1)}} \widetilde{\Phi}_{(2,3,6p-1)}^{(1,1,2p)} (\tau),$$ $$\label{main5eq}
H_p^{(5)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{p-1 - \frac{(12p-5)^2}{24(6p-1)}} \widetilde{\Phi}_{(2,3,6p-1)}^{(1,1,3p-1)} (\tau),$$ $$\label{main6}
H_p^{(6)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{-\frac{(6p-1)^2}{24(6p+1)}} \widetilde{\Phi}_{(2,3,6p+1)}^{(1,1,2p)} (\tau),$$ $$\label{main7eq}
H_p^{(7)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{1 - \frac{(6p+5)^2}{24(6p+1)}} \widetilde{\Phi}_{(2,3,6p+1)}^{(1,1,2p+1)} (\tau),$$ $$\label{main8eq}
H_p^{(8)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{1 - \frac{(6p-5)^2}{24(6p+1)}} \widetilde{\Phi}_{(2,3,6p+1)}^{(1,1,1)} (\tau),$$ $$\label{main9eq}
H_p^{(9)}(\zeta_N^M) = -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{p-1 - \frac{(12p-1)^2}{24(6p+1)}} \widetilde{\Phi}_{(2,3,6p+1)}^{(1,1,3p)} (\tau)$$ and $$\label{main10eq}
H_p^{(10)}(\zeta_N^M) =  -\frac{1}{2}  \lim_{\tau \to \frac{M}{N}} q^{-\frac{1}{24(6p+1)}} \widetilde{\Phi}_{(2,3,6p+1)}^{(1,1,p)} (\tau).$$
:::

::: remark
Observe that the $p=1$ case of ([\[main2eq\]](#main2eq){reference-type="ref" reference="main2eq"}) recovers ([\[LZ\]](#LZ){reference-type="ref" reference="LZ"}) while the $M=1$ cases of ([\[main1eq\]](#main1eq){reference-type="ref" reference="main1eq"}) and ([\[main8eq\]](#main8eq){reference-type="ref" reference="main8eq"}) yield ([\[h1p\]](#h1p){reference-type="ref" reference="h1p"}) and ([\[h8p\]](#h8p){reference-type="ref" reference="h8p"}), respectively. We have also included ([\[main11eq\]](#main11eq){reference-type="ref" reference="main11eq"}) for completeness (cf. [@hikami5 (3.8), (3.10)]). Note that Theorem [\[main\]](#main){reference-type="ref" reference="main"} embeds Hikami's conjectures for one single value of $p$ (with the exception of ([\[h5pconj\]](#h5pconj){reference-type="ref" reference="h5pconj"})) into an infinite family of identities. Finally, our main result and [@go Section 4.4] imply that each $H_p^{(i)}(q)$ is a quantum modular form.
:::

The paper is organized as follows. In Section 2, we recall the necessary background on the Bailey pair machinery and express all of the series $H_p^{(i)}(q)$ as finite polynomial sums at roots of unity. See Theorems [\[Baileyfamily1\]](#Baileyfamily1){reference-type="ref" reference="Baileyfamily1"}--[\[Baileyfamily10\]](#Baileyfamily10){reference-type="ref" reference="Baileyfamily10"}. An elucidatory principle in this section arises from the broader perspective of quantum $q$-series identities [@love1; @love2], a recent development whose applications include new proofs for identities at roots of unity for Ramanujan's $\sigma$-function and its companion $\sigma^{*}(q)$ [@ADH; @Cohen], a "duality\" result for the Kontsevich-Zagier strange function [@bopr; @fkvy] and Zagier's strange identity and Hikami's generalization thereof [@hikamiRAMA; @z]. For further work in this direction, see [@dl; @fm; @f; @ls]. In Section 3, we prove key properties for and relations between incomplete quadratic Gauss sums. In Section 4, we convert the finite polynomial sums in Section 2 to limiting values of Eichler integrals, thereby proving Theorem [\[main\]](#main){reference-type="ref" reference="main"}.

[^1]: Here and throughout, we follow the notation $H_p^{(i)}(q)$ for the $q$-multisums ([\[h1\]](#h1){reference-type="ref" reference="h1"}) and ([\[h2\]](#h2){reference-type="ref" reference="h2"})--([\[h5\]](#h5){reference-type="ref" reference="h5"}) as given in [@tm]. We have labelled ([\[h8\]](#h8){reference-type="ref" reference="h8"}), ([\[h6\]](#h6){reference-type="ref" reference="h6"}), ([\[h7\]](#h7){reference-type="ref" reference="h7"}), ([\[h9\]](#h9){reference-type="ref" reference="h9"}) and ([\[h10\]](#h10){reference-type="ref" reference="h10"}) accordingly.
