---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-002-21-cohomology-of-the-flag-manifold
section_title: "Cohomology of the flag manifold"
section_number: 2.1
pages: 3-3
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.899
latex_coverage_ratio: 0.991
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#cohomology-ring-of-the-flag-manifold label="cohomology-ring-of-the-flag-manifold"}

Let $n\in{\mathbb N}$ be a positive integer and write ${\mathbb F}\ell_n$ for the manifold of complete flags in ${\mathbb C}^n$. We let $H^*{\mathbb F}\ell_n$ denote its cohomology ring with coefficients in ${\mathbb Z}$. This is a free ${\mathbb Z}$-module with a distinguished basis $\{{\mathfrak S}_w\}_{w \in S_n}$ of which are indexed by elements of the symmetric group $S_n$. Borel [@Borel] described the ring structure of $H^*{\mathbb F}\ell_n$ as a quotient of a polynomial ring,

$$\label{borel-presentation}
    H^* {\mathbb F}\ell_n\ \simeq\ {\mathbb Z}[x_1,\dotsc,x_n] / I_n\,,
    \qquad I_n\ =\ \big\langle e_a(x_1,\dotsc,x_n)\mid a \in [n] \big\rangle\,,$$

where $e_a$ is the $a$th elementary symmetric polynomial and ${\color{RoyalBlue}[n]}\vcentcolon=\{1,\dots,n\}$. Lascoux and Schützenberger [@LaSch82] defined a set of polynomials in ${\mathbb Z}[x_1, \ldots, x_n]$ called that correspond to the Schubert classes ${\mathfrak S}_w$ under Borel's isomorphism. We write ${\mathfrak S}_w(x)$ for the Schubert polynomial corresponding to ${\mathfrak S}_w$ on the set of variables $x: = \{x_1, \ldots, x_n\}$.

Every Schur polynomial $s_\lambda(x_1, \ldots, x_k)$ is a Schubert polynomial. Let $w\in S_n$ be a permutation with a unique descent at position $k$. Then the sequence $(w(k){-}k,\dotsc, w(2){-}2,w(1){-}1)$ is a partition contained in the of $k(n{-}k)$ into $k$ parts with each part of size $n{-}k$. This is a bijection and for $\lambda \subseteq R_{k, n-k}$ we write ${\color{RoyalBlue}v(\lambda,k)}\in S_n$ for the corresponding permutation. Then ${\mathfrak S}_{v(\lambda, k)}(x) = s_\lambda(x_1, \ldots, x_k)$. For example, when $n=7$,

$$v((3,1,0),3)\ =\ 136\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}2457
  \qquad\mbox{and}\qquad
  v((1,0,0,0),4)\ =\ 1235\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}467\ =\ (4,5)\,.$$

Observe that we may write permutations using both one-line and cycle notation. The " $\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}$ " is written after the $k$-th position in a permutation in one-line notation.

It remains an important open problem in Schubert calculus to find a combinatorial rule expressing ${\mathfrak S}_u \cdot {\mathfrak S}_v$ in terms of the basis $\{ {\mathfrak S}_w \}_{w \in S_n}$ of $H^*{\mathbb F}\ell_n$. That is, one seeks a combinatorial rule for the coefficients ${\color{RoyalBlue}c_{u,v}^{w}}\in{\mathbb Z}$ in the product

$$\label{eq:classical-coeffs}
    {\mathfrak S}_u \cdot {\mathfrak S}_v\ =\ \sum_{w} c_{u, v}^{w} {\mathfrak S}_w\,.$$

A remarkable property of Schubert polynomials is that this computation can be performed directly in the polynomial ring as the resulting coefficients $c_{u, v}^w$ are the same.

Although this problem remains open in general, several special cases are known.  [@Monk] treats the case where $v$ is the simple transposition $(k, k{+}1)$. For any $u \in S_n$,

$$\label{classical-Monk-formula}
    {\mathfrak S}_u(x) \cdot {\mathfrak S}_{(k,k+1)}(x)
       \ =\ 
    \sum_{\substack{1 \leq i \leq k < j \leq n \\ \ell(u) + 1 = \ell(u(i,j))}} {\mathfrak S}_{u (i,j)}(x)\,,$$

where ${\color{RoyalBlue}\ell(u)}\vcentcolon=\#\{i<j\mid u(i)>u(j)\}$ denotes the length of the permutation $u$. In this case, ${\mathfrak S}_{(k, k+1)}(x) = s_{(1)}(x_1, \ldots, x_k)$. Proposition [\[pieri-formulas-version-2\]](#pieri-formulas-version-2){reference-type="ref" reference="pieri-formulas-version-2"} below describes the special case of multiplying by $s_{(b, 1^{a-1})}(x_1, \ldots, x_k)$ in terms of the *$k$-Bruhat order*, which we define next. Here, $(b,1^{a-1})$ is the of $a{+}b{-}1$ into $a$ parts, the first of size $b$, and the remaining all of size $1$.
