---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-023-63-description-of-blocks-via-martin
section_title: "Description of blocks via Martin"
section_number: 6.3
pages: 40-41
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.881
latex_coverage_ratio: 0.967
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
In this section we give a general description of the nontrivial blocks based on the results of Martin. We start by reviewing the main result in [@MR1399030].

Assume $d\not=0$ and let $\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots$ denote the Young diagrams associated to a fixed nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. For each $m\geq|\lambda^{(n)}|$, let $E_m^{(n)}$ denote the simple $FP_m(d)$-module associated to $\lambda^{(n)}$ (see Theorem [\[idemP\]](#idemP){reference-type="ref" reference="idemP"}(1)), and let $P_m^{(n)}$ denote its projective cover. According to [@MR1399030 Proposition 9], these modules have Loewy structure $$\label{loewy}\begin{array}{l}
P_m^{(0)}=\begin{array}{c}
 E^{(0)}_m \\
E^{(1)}_m
\end{array}\quad(m\geq|\lambda^{(1)}|),\\
\\
P_m^{(n)}=\begin{array}{rcl}
& E^{(n)}_m &\\
E^{(n-1)}_m & & E^{(n+1)}_m\\
& E^{(n)}_m &
\end{array}\quad(n>0, m\geq|\lambda^{(n+1)}|).
\end{array}$$ In other words, for $m>0$, $P_m^{(0)}$ has a maximal simple submodule $B_0\cong E_m^{(1)}$ with $P_m^{(0)}/B_0\cong E^{(0)}_m$. Moreover, for each $m\geq|\lambda^{(n+1)}|$ there exists a chain of submodules $$\includegraphics{diss73.pdf}$$ with $P_m^{(n)}/A_n\cong E^{(n)}_m, A_n/B_n^{\pm}\cong E^{(n\mp1)}_m, B_n^{\pm}/C_n\cong E^{(n\pm1)}_m$, and $C_n\cong E^{(n)}_m$ for $n>0$. Using the notation above, define the following maps[^1]: $$\label{martinmaps}\begin{array}{ll}
\alpha_0=\alpha_{0, m}:P^{(0)}_m\twoheadrightarrow P^{(0)}_m/B_0\cong C_1\hookrightarrow P^{(1)}_m\\
\beta_0=\beta_{0, m}:P^{(1)}_m\twoheadrightarrow P^{(1)}/B_1^+\cong P_m^{(0)}\\
\alpha_n=\alpha_{n,m}: P_m^{(n)}\twoheadrightarrow P_m^{(n)}/B^-_n\cong B^-_{n+1}\hookrightarrow P_m^{(n+1)} &  (n>0) \\
\beta_n=\beta_{n,m}:P_m^{(n+1)}\twoheadrightarrow P_m^{(n+1)}/B^+_{n+1}\cong B^+_n\hookrightarrow P_m^{(n)}  &  (n>0)\\
\gamma_n=\gamma_{n,m}: P_m^{(n)}\twoheadrightarrow P_m^{(n)}/A_n\cong C_n\hookrightarrow P_m^{(n)}  &  (n>0)
\end{array}$$

We are now ready to give a general description of the nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$.

::: theorem
[]{#blocksviamartin label="blocksviamartin"} Suppose $d$ is a nonnegative integer and $\mathcal{B}$ is a nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. Then $\mathcal{B}$ is equivalent as an additive category to the nontrivial block described in Theorem [\[zeroblock\]](#zeroblock){reference-type="ref" reference="zeroblock"}.
:::

::: proof
*Proof.* We may assume $d\not=0$. Notice $$\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)}(L(\lambda^{(n)}), L(\lambda^{(n')}))=\operatorname{Hom}_{FP_m(d)}(P_m^{(n)}, P_m^{(n')})$$ whenever $m\geq |\lambda^{(n)}|, |\lambda^{(n')}|$. Hence, by Proposition [\[dimstuff\]](#dimstuff){reference-type="ref" reference="dimstuff"}(2), it suffices to prove the maps defined by ([\[martinmaps\]](#martinmaps){reference-type="ref" reference="martinmaps"}) satisfy equations (1)-(7) in Lemma [\[calculations\]](#calculations){reference-type="ref" reference="calculations"}. Equations (1)-(5) are clearly satisfied. The fact that equations (6) and (7) are satisfied follows from the observation that the maps $B^\mp_{n\pm1}\hookrightarrow P_m^{(n\pm1)}\twoheadrightarrow P_m^{(n\pm1)}/B^\pm_{n\pm1}\cong B^\pm_n$ factor through the maps $B^\mp_{n\pm1}\twoheadrightarrow B^\mp_{n\pm1}/C_{n\pm1}\cong C_n\hookrightarrow B^\pm_n$. ◻
:::

::: remark
Our proof of Theorem [\[blocksviamartin\]](#blocksviamartin){reference-type="ref" reference="blocksviamartin"} is a bit unsatisfactory since it is based on rather deep results from [@MR1399030]. On the other hand Theorem [\[blocksviamartin\]](#blocksviamartin){reference-type="ref" reference="blocksviamartin"} follows from Theorem [\[zeroblock\]](#zeroblock){reference-type="ref" reference="zeroblock"}, Proposition [\[blocksfixd\]](#blocksfixd){reference-type="ref" reference="blocksfixd"}, along with Conjecture [\[conjecture\]](#conjecture){reference-type="ref" reference="conjecture"}. Hence a proof of Conjecture [\[conjecture\]](#conjecture){reference-type="ref" reference="conjecture"} would complete a proof of Theorem [\[blocksviamartin\]](#blocksviamartin){reference-type="ref" reference="blocksviamartin"} which is independent from [@MR1399030].
:::

[^1]: The equations in ([\[martinmaps\]](#martinmaps){reference-type="ref" reference="martinmaps"}) are only defined when $m$ is sufficiently large.
