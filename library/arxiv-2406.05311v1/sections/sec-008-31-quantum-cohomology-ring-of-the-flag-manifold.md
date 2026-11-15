---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-008-31-quantum-cohomology-ring-of-the-flag-manifold
section_title: "Quantum cohomology ring of the flag manifold"
section_number: 3.1
pages: 8-9
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.937
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
As a ${\mathbb Z}$-module, we have

$$qH^*{\mathbb F}\ell_n\ =\  {\mathbb Z}[q_1,\dotsc,q_{n-1}] \otimes_{\mathbb Z}H^*{\mathbb F}\ell_n\,,$$

where $q_1,\dotsc,q_{n-1}$ are indeterminates. To simplify notation, write ${\mathbb Z}[q]$ for ${\mathbb Z}[q_1,\dotsc,q_{n-1}]$, and use multiindex notation, for $\alpha\in{\mathbb N}^{n-1}$, we have ${\color{RoyalBlue}q^\alpha}\vcentcolon= q_1^{\alpha_1}\dotsb q_{n-1}^{\alpha_{n-1}}$. The Schubert classes $\{{\mathfrak S}_w\}_{w \in S_n}$ in $H^*{\mathbb F}\ell_n$ form a ${\mathbb Z}[q]$-basis of $qH^*{\mathbb F}\ell_n$. We write ${\color{RoyalBlue}{\mathfrak S}_u \ast {\mathfrak S}_v}$ for the product of Schubert classes ${\mathfrak S}_u$ and ${\mathfrak S}_v$ in $qH^*{\mathbb F}\ell_n$ to distinguish it from the product ${\color{RoyalBlue}{\mathfrak S}_u \cdot {\mathfrak S}_v}$ in $H^*{\mathbb F}\ell_n$.

The ring structure of $qH^*{\mathbb F}\ell_n$ is determined by the  [@FGP]. For every $u\in S_n$ and $1\leq k<n$ we have,

$$\label{quantum-Monk-formula}
    {\mathfrak S}_u * {\mathfrak S}_{(k,k+1)}
    \ =\ 
    \sum_{\substack{1 \leq i \leq k < j \leq n \\ \ell(u) + 1 = \ell(u(i,j))}} {\mathfrak S}_{u (i,j)}\ 
    \ +\ 
    \sum_{\substack{1 \leq i \leq k < j \leq n \\ \ell(u) + 1 = \ell(u(i,j)) + 2(j - i)}} q_{i,j} {\mathfrak S}_{u (i,j)}$$

where ${\color{RoyalBlue}q_{i,j}}\vcentcolon=q_iq_{i+1}\dotsb q_{j-1}$ for $i < j$. The summand on the left above comes from the classical Monk formula [\[classical-Monk-formula\]](#classical-Monk-formula){reference-type="eqref" reference="classical-Monk-formula"}. For example, in $qH^*{\mathbb F}\ell_4$ we have,

$$\label{Eq:q-Monk}
    {\mathfrak S}_{1432} * {\mathfrak S}_{(2,3)}
    \ =\  {\mathfrak S}_{3412} \ +\ {\mathfrak S}_{2431}
    \ +\ q_{2}{\mathfrak S}_{1342} \ +\  q_{2,3} {\mathfrak S}_{1234}\,.$$

Givental and Kim [@GiventalKim] proved that $qH^*{\mathbb F}\ell_n\simeq {\mathbb Z}[q][x] / I^q_n$ for a certain ideal $I^q_n$, establishing an analog to Borel's presentation [\[borel-presentation\]](#borel-presentation){reference-type="eqref" reference="borel-presentation"}. Fomin, Gelfand, and Postnikov [@FGP] defined ${\color{RoyalBlue}{\mathfrak S}^q_w(x)}$ in ${\mathbb Z}[q][x]$ so that the quantum product of Schubert classes satisfies ${\mathfrak S}_u \ast {\mathfrak S}_v \mapsto ({\mathfrak S}^q_u(x) + I^q_n) ({\mathfrak S}^q_v(x) + I^q_n)$, for $u,v\in S_n$, under this isomorphism. To simplify notation, for $f(x) \in {\mathbb Z}[q][x]$, we will write ${\mathfrak S}_u \ast f(x)$ for ${\mathfrak S}^q_u(x) f(x) + I^q_n$.

As explained in Section [\[cohomology-ring-of-the-flag-manifold\]](#cohomology-ring-of-the-flag-manifold){reference-type="ref" reference="cohomology-ring-of-the-flag-manifold"}, every Schur polynomial is a Schubert polynomial: more precisely, $s_\lambda(x_1, \ldots, x_k) = {\mathfrak S}_{v(\lambda, k)}(x)$, where $\lambda \subseteq R_{k, n-k}$. Analogously, we define the , for $\lambda \subseteq R_{k, n-k}$, to be ${s_\lambda^q(x_1,\dotsc,x_k)} \vcentcolon= {\mathfrak S}^q_{v(\lambda,k)}(x)$. Following Equation [\[Eq:PowerSumHook\]](#Eq:PowerSumHook){reference-type="eqref" reference="Eq:PowerSumHook"}, the is defined to be

$$\begin{gathered}
    \label{Eq:Q-powerSum}
    \qquad  {\color{RoyalBlue}p^q_r(x_1,\dotsc,x_k)}\ \vcentcolon= \\
        s^q_{(r)}(x_1,\dotsc,x_k) - s^q_{(r-1,1)}(x_1,\dotsc,x_k) +
                   \dotsb + (-1)^{r+1} s^q_{(1^r)}(x_1,\dotsc,x_k)\,.
    \qquad
\end{gathered}$$
