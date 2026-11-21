---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-010-42-relations-between-quotients
section_title: "Relations between Quotients"
section_number: 4.2
pages: 20-21
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 1.0
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: relations between quotients label="subsec: relations between quotients"} We now consider the various relationships we might expect between the quotient curves of Bring's curve. Recall (again from Riemann-Hurwitz) that if $\mathcal{C}$ is a curve of genus $g\ge2$ and $H\le \mathop{\mathrm{Aut}}(\mathcal{C})$ is such that $|H|>4(g-1)$, a so called 'large automorphism group', then the genus of the quotient curve $g_{\mathcal{C}/H}=0$. For Brings's curve we are therefore interested in subgroups of $S_5$ of order less than or equal to $12$, and as we have seen the quotient by a 5-cycle leads to genus $0$ we may exclude subgroups containing such. The relevant conjugacy classes of subgroups are then[^1]

(a) $\left\langle (12)(34) \right\rangle\cong C_2$, $\left\langle (12),(34) \right\rangle\cong V_4$, $\left\langle (1324) \right\rangle\cong C_4$, $\left\langle (1324),(12) \right\rangle\cong D_8$. Each of these groups $H$ have the same normaliser: $N_{S_5}(H)=\left\langle (1324),(12) \right\rangle\cong D_{8}$.

(b) $\left\langle (12) \right\rangle\cong C_2$, $\left\langle (345) \right\rangle\cong C_3$, $\left\langle (345),(12) \right\rangle\cong C_6$, $\left\langle (345), (34) \right\rangle\cong S_3$, $\left\langle (345),(12)(34) \right\rangle\cong  S_3'$, $\left\langle (345),(12),(34) \right\rangle\cong D_{12}\cong S_3\times C_2$. Each of these groups $H$ have the same normaliser: $N_{S_5}(H)=\left\langle (345),(12),(34) \right\rangle\cong D_{12}$.

(c) $\left\langle (12)(34), (13)(24) \right\rangle\cong V_4$, $\left\langle (234),(12)(34) \right\rangle\cong A_4$. Each of these groups $H$ have the same normaliser: $N_{S_5}(\left\langle (234),(12)(34) \right\rangle) = \left\langle (234), (12), (34) \right\rangle \cong S_4$.

The groupings here are such that if $H$, $H'$ are from the same item then they share the same normaliser $N=N_{S_5}(H)=N_{S_5}(H')$. In particular each of $H$, $H'$ and $HH'=H'H$ are normal in $N$ and we have commutativity of the following diagram of quotients

::: center
:::

where the arrows are labelled by the symmetry being quotiented; by an isomorphism theorem we have of course that $HH'/H\cong H'/(H\cap H')$ and $HH'/H' \cong H/(H\cap H')$. If, say $H\le H'$, then $HH'=H'$ and one side of this diagram collapses.

Now a Riemann-Hurwitz calculation shows that the each of the quotients by $\left\langle (12),(34) \right\rangle$, $\left\langle (1324),(12) \right\rangle$, $\left\langle (345), (34) \right\rangle$ and $\left\langle (345),(12),(34) \right\rangle$ is of genus $0$ and so not being considered. Thus from the preceding discussion we have the following relations amongst quotients for the subgroups of (a), (b) and (c):

::: center
:::

Here $\mathcal{C}, \mathcal{C}^\prime$ are genus 2 curves and $\mathcal{E}$,...,$\mathcal{E}\sp{(v)}$ elliptic curves that we cannot yet specify purely on group theoretic grounds. We turn now to their specification and indeed we shall find some interesting identities between them, which will then be summarised in §[\[subsec: summarising quotients\]](#subsec: summarising quotients){reference-type="ref" reference="subsec: summarising quotients"}.

[^1]: Note that here we are using the GAP convention for the dihedral group that $|{D_n}|=n$. This is the opposite convention to Sage which uses $|{D_{n}}|=2n$.
