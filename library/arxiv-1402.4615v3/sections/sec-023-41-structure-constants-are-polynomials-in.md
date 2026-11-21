---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-023-41-structure-constants-are-polynomials-in
section_title: "Structure constants are polynomials in"
section_number: 4.1
pages: 31-32
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.991
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#SubsectStructPol label="SubsectStructPol"}

In this section we are going to prove our main result for the structure constants of the algebra $\Lambda_\star^{(\alpha)}$ of $\alpha$-polynomial functions which was stated as Theorem [\[theo:struct-const\]](#theo:struct-const){reference-type="ref" reference="theo:struct-const"}.

::: proof
*Proof of Theorem [\[theo:struct-const\]](#theo:struct-const){reference-type="ref" reference="theo:struct-const"}:.* First observe that for each $i \in \{1,2,3\}$ one has: $$n_i(\mu) = \deg_i(\mathop{\mathrm{Ch}}_\mu),$$ hence our bound on the degree of structure constants can be equivalently formulated using three gradations introduced in Section [\[SectPolynomial\]](#SectPolynomial){reference-type="ref" reference="SectPolynomial"}.

Let us consider the bound involving $\deg_1$ (the case of $\deg_3$ is similar). We know by Proposition [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"} that $$\mathop{\mathrm{Ch}}_\mu = \sum_\rho a_\rho^\mu M_\rho,$$ where each $a_\rho^\mu$ is a polynomial in $\gamma$ of degree $\deg_1(\mathop{\mathrm{Ch}}_\mu)-\deg_1(M_\rho)$. Hence, we have $$\mathop{\mathrm{Ch}}_\mu \cdot \mathop{\mathrm{Ch}}_\nu = \sum_\rho b_\rho^{\mu,\nu} M_\rho,$$ where each $b_\rho^{\mu,\nu}$ is a polynomial in $\gamma$ of degree $\deg_1(\mathop{\mathrm{Ch}}_\mu)+\deg_1(\mathop{\mathrm{Ch}}_\nu)-\deg_1(M_\rho)$. In particular $\mathop{\mathrm{Ch}}_\mu \cdot \mathop{\mathrm{Ch}}_\nu$ has degree at most $\deg_1(\mathop{\mathrm{Ch}}_\mu)+\deg_1(\mathop{\mathrm{Ch}}_\nu)$ and hence, thanks to the remark of Section [\[SubsectDegCh\]](#SubsectDegCh){reference-type="ref" reference="SubsectDegCh"}, $g_{\mu,\nu;\pi}=0$ whenever $$n_1(\mu) + n_1(\nu) < n_1(\pi).$$ The structure constants are obtained by solving the linear system: $$\sum_\tau a_\rho^\tau g_{\mu,\nu;\tau} = b_\rho^{\mu,\nu}.
        \tag{S}\label{EqSystStructure}$$ In this system, $\mu$ and $\nu$ are fixed, there is one equation for each partition $\rho$ without parts equal to $1$. In each equation, the sum runs over partitions $\tau$ such that $n_1(\tau) \le n_1(\mu) + n_1(\nu)$. Finally, the unknown are $g_{\mu,\nu;\tau}$, for $\tau$ as above.

We will prove our statement by induction over $$\deg_1(\mathop{\mathrm{Ch}}_\mu) + \deg_1(\mathop{\mathrm{Ch}}_\nu) - \deg_1(\mathop{\mathrm{Ch}}_\pi).$$ Fix some partitions $\mu$,$\nu$ and $\pi$. If the quantity above is negative, the coefficient $g_{\mu,\nu;\pi}$ is equal to $0$ and the statement is true. Otherwise we suppose that for all partitions $\tau$ bigger than $\pi$ (in the sense that $\deg_1(\mathop{\mathrm{Ch}}_{\tau}) > \deg_1(\mathop{\mathrm{Ch}}_{\pi})$), the degree of $g_{\mu,\nu;\tau}$ is bounded from above by $\deg_1(\mathop{\mathrm{Ch}}_\mu) + \deg_1(\mathop{\mathrm{Ch}}_\nu) - \deg_1(\mathop{\mathrm{Ch}}_\tau)$.

Note that $a_\rho^\tau$ vanishes as soon as $\deg_1(\mathop{\mathrm{Ch}}_\tau) < \deg_1(M_\rho)$. Then from [\[EqSystStructure\]](#EqSystStructure){reference-type="eqref" reference="EqSystStructure"} we extract a subsystem $$\sum_{\substack{\tau, \\ \deg_1(\mathop{\mathrm{Ch}}_\tau)=\deg_1(\mathop{\mathrm{Ch}}_{\pi})}} a_\rho^\tau g_{\mu,\nu;\tau} =
        b_\rho^{\mu,\nu} - \sum_{\substack{\tau, \\ \deg_1(\mathop{\mathrm{Ch}}_\tau)>\deg_1(\mathop{\mathrm{Ch}}_{\pi})}}
        a_\rho^\tau g_{\mu,\nu;\tau},      
        \tag{$S'$}
        \label{syst:Sp}$$ where $\rho$ runs over partitions such that $\deg_1(M_\rho)=\deg_1(\mathop{\mathrm{Ch}}_\pi)$. The variables are $g_{\mu,\nu;\tau}$ for $\tau$ with $\deg_1(\mathop{\mathrm{Ch}}_\tau)=\deg_1(\mathop{\mathrm{Ch}}_{\pi})$. This system is invertible (because $(\mathop{\mathrm{Ch}}_\pi)$ is a basis of $\Lambda_\star^{(\alpha)}$) and the coefficients on the left-hand side of [\[syst:Sp\]](#syst:Sp){reference-type="eqref" reference="syst:Sp"} are rational numbers (by Proposition [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"}). Besides, all terms on the right-hand side are polynomials in $\gamma$ of degree at most $\deg_1(\mathop{\mathrm{Ch}}_\mu) + \deg_1(\mathop{\mathrm{Ch}}_\nu) - \deg_1(\mathop{\mathrm{Ch}}_\pi)$ which finishes the proof.

The proof of the parity follows in the same way.

The bound involving $\deg_2$ is obtained in a slightly different way. First note that if $\mu$ and $\nu$ do not have any parts equal to $1$, this bound is weaker that the one with $\deg_3$. Hence, it holds in this case. Then the general case follows, using the fact that $\mathop{\mathrm{Ch}}_{\mu \cup (1)}=(|\lambda| - |\mu|)\mathop{\mathrm{Ch}}_\mu$. ◻
:::
