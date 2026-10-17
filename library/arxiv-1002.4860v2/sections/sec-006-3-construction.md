---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-006-3-construction
section_title: "Construction"
section_number: 3
pages: 5-7
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.992
doc_brief: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL — We develop a diagrammatic formalism for calculating the Alexander polynomial of the closure of a braid as a state-sum."
---
[]{#sec constr label="sec constr"}

Begin with a word $w \in \Sigma_n^\bullet$ in the braid generators $\sigma_1, \ldots, \sigma_{n-1}$ and their inverses, which we picture as a diagram drawn up the page as the word is read from right to left. $$\sigma_r = \; \vcenter{
\xy 0;/r.10pc/:
(0,15)*{},
(0,0);(0,10)**@{-},
(10,5)*{\cdots},
(20,0);(20,10)**@{-},
(30,0);(40,10)**@{-},
(40,0);(36,4)**@{-},
(34,6);(30,10)**@{-},
(30,-4)*{_{\phantom{+1} r \phantom {+1}}},
(40,-4)*{_{r+1}},
(50,0);(50,10)**@{-},
(60,5)*{\cdots},
(70,0);(70,10)**@{-}
\endxy
} \qquad \qquad
\sigma_r^{-1} = \; \vcenter{
\xy 0;/r.10pc/:
(0,15)*{},
(0,0);(0,10)**@{-},
(10,5)*{\cdots},
(20,0);(20,10)**@{-},
(30,0);(34,4)**@{-},
(36,6);(40,10)**@{-},
(40,0);(30,10)**@{-},
(30,-4)*{_{\phantom{+1} r \phantom {+1}}},
(40,-4)*{_{r+1}},
(50,0);(50,10)**@{-},
(60,5)*{\cdots},
(70,0);(70,10)**@{-}
\endxy
}$$

Construct *permutation diagrams* from the braid diagram by replacing each crossing by one of two resolutions: $$\begin{aligned}
\vcenter{
\xy
(0,0);(10,10)**@{-},
(10,0);(6,4)**@{-},
(4,6);(0,10)**@{-}
\endxy
} \qquad &\longmapsto& \qquad \vcenter{
\xy
(0,0);(0,10)**@{-},
(10,0);(10,10)**@{-}
\endxy
} \qquad \text{or} \qquad \vcenter{
\xy
(0,0);(10,10)**@{-},
(10,0);(0,10)**@{-}
\endxy
} \\ \\
\vcenter{
\xy
(0,0);(4,4)**@{-},
(6,6);(10,10)**@{-},
(10,0);(0,10)**@{-}
\endxy
} \qquad &\longmapsto& \qquad \vcenter{
\xy
(0,0);(0,10)**@{-},
(10,0);(10,10)**@{-}
\endxy
} \qquad \text{or} \qquad \vcenter{
\xy
(0,0);(10,10)**@{-},
(10,0);(0,10)**@{-}
\endxy
}
\end{aligned}$$ A permutation diagram $\mathbf{x}$ is *admissible* if

P1

:   the first (leftmost) strand goes straight through without crossing any other strands, and

P2

:   the underlying permutation is the identity.

A *state* is a pair $(\mathbf{x},\varepsilon)$, where $\mathbf{x}$ is an admissible permutation diagram and $\varepsilon$ is an assignment of a sign $\pm$ to each strand such that

S1

:   the first (leftmost) sign is $+$, and

S2

:   no two strands of the same sign cross.

Let $\mathcal{S}(w)$ denote the set of states for $w$. To a state $(\mathbf{x},\varepsilon) \in \mathcal{S}(w)$, we associate a weight $M(w, \mathbf{x}, \varepsilon) \in \mathbb{C}(v)$ defined by multiplying together certain scalars, one for each resolved crossing. The scalar associated to a positive crossing of strands in positions $r$ and $r+1$ is given in ([\[scalars\]](#scalars){reference-type="ref" reference="scalars"}). For a negative crossing, replace $v$ by $v^{-1}$ in each expression.

$$\label {scalars}
\vcenter{
\xy
(0,0);(10,10)**@{-},
(10,0);(6,4)**@{-},
(4,6);(0,10)**@{-},
(0,-2)*={_r},
(10,-2)*={_{r+1}},
\endxy
} \quad \longmapsto \quad \left \{
\begin {array} {r c r}
v \quad \vcenter{
\xy
(0,-2)*={_+},
(0,0);(0,10)**@{-},
(10,-2)*={_+},
(10,0);(10,10)**@{-}
\endxy
} & \qquad &
-v^{-1} \quad \vcenter{
\xy
(0,-2)*={_-},
(0,0);(0,10)**@{-},
(10,-2)*={_-},
(10,0);(10,10)**@{-}
\endxy
} \\ & & \\ & & \\
\dfrac {v^r} {[r]} \quad \vcenter{
\xy
(0,-2)*={_-},
(0,0);(0,10)**@{-},
(10,-2)*={_+},
(10,0);(10,10)**@{-}
\endxy
} & \qquad &
\dfrac {-v^{-r}} {[r]} \quad \vcenter{
\xy
(0,-2)*={_+},
(0,0);(0,10)**@{-},
(10,-2)*={_-},
(10,0);(10,10)**@{-}
\endxy
} \\ & & \\ & & \\
\dfrac {[r+1]} {[r]} \quad \vcenter{
\xy
(0,-2)*={_-},
(0,0);(10,10)**@{-},
(10,-2)*={_+},
(10,0);(0,10)**@{-}
\endxy
} & &
\dfrac {[r-1]} {[r]} \quad \vcenter{
\xy
(0,-2)*={_+},
(0,0);(10,10)**@{-},
(10,-2)*={_-},
(10,0);(0,10)**@{-}
\endxy
}
\end {array}
\right.$$\
Define $A(w) \in \mathbb{C}(v)$ by $$\label {state-sum}
A(w)=\frac 1 {[n]} \sum_{(\mathbf{x}, \varepsilon) \in \mathcal{S}(w)} \langle \varepsilon\rangle M(w,\mathbf{x},\varepsilon)$$ where $\langle \varepsilon\rangle \in \{ \pm 1 \}$ is the product of the signs $\varepsilon_1, \ldots, \varepsilon_n$ attached to the strands.

::: thm
[]{#main thm label="main thm"} Let $L$ be an oriented link, and let $w \in \Sigma_n^\bullet$ represent a braid in $B_n$ whose closure is $L$. Then, $A(w)$ is a polynomial in $v-v^{-1}$, and $$A(w) = \Delta(L),$$ where $\Delta(L)$ is the Conway-normalized Alexander polynomial.
:::

::: proof
*Proof.* To avoid confusion when switching between the generators $H_r$ and $T_r = vH_r$ of $\mathcal{H}_n$, let us write $\varphi: B_n \twoheadrightarrow\mathcal{H}_n^\times$ for the group homomorphism given by $\varphi(\sigma_r) = H_r$ and $\psi: B_n \twoheadrightarrow\mathcal{H}_n^\times$ for the one with $\psi(\sigma_r) = T_r$. Formula (7.2) in [@Jones] gives the Alexander polynomial for a link $L$ as $$\Delta(L) = (-1)^{n-1} \left( \frac 1 q \right)^{(e-n+1)/2} \frac {1-q} {1-q^n} \sum_{k=0}^{n-1} (-1)^k \chi_{n-1-k} \bigl( \psi(w) \bigr)$$ where $\chi_\ell = \operatorname {tr}\circ  \rho_{\ell}$ is the character of $\mathcal{H}_n$ arising from the irreducible representation $\rho_\ell: \mathcal{H}_n \to \operatorname {End}(S(\lambda_\ell))$ indexed by the hook partition $(n-\ell, 1^\ell)$, and $e$ is the exponent sum of $w$. Put $q = v^2$ and $T_r=vH_r$ for each $r$, so that $\psi(w) = v^e \varphi(w)$. Reindex the sum over $\ell = n-1-k$ to get $$\begin{aligned}
    \Delta(L) &=& (-1)^{n-1} \left( \frac 1 v \right)^{e-n+1} \frac {1-v^2} {1-v^{2n}} \sum_{\ell=0}^{n-1} (-1)^{n-1-\ell} \chi_\ell \bigl( v^e \varphi(w) \bigr) \nonumber \\
    &=&  \frac 1 {[n]} \sum_{\ell=0}^{n-1} (-1)^\ell \chi_\ell \bigl( \varphi(w) \bigr).
\end{aligned}$$

Now we compute $\chi_\ell$ by using the semi-normal form for $S(\lambda_\ell)$. The action of the generators $H_r$, $H_r^{-1}$ on $x_{\varepsilon}$ from Theorem [\[signs irrep thm\]](#signs irrep thm){reference-type="ref" reference="signs irrep thm"} are pictured in ([\[s-n signs\]](#s-n signs){reference-type="ref" reference="s-n signs"}). $$\label {s-n signs}
\begin {array} {c c c}
\vcenter{
\xy
(0,0);(10,10)**@{-},
(10,0);(6,4)**@{-},
(4,6);(0,10)**@{-},
(0,-3)*{_r},
(10,-3)*{_{r+1}},
(0,13)*{}
\endxy
} \quad &\longmapsto& \quad a_r(\varepsilon) \vcenter{
\xy
(0,0);(0,10)**@{-},
(10,0);(10,10)**@{-},
(0,-3)*{\varepsilon_r},
(0,13)*{\varepsilon_r},
(10,-3)*{\varepsilon_{r+1}},
(10,13)*{\varepsilon_{r+1}}
\endxy
} \quad + \quad b_r(\varepsilon) \vcenter{
\xy
(0,0);(10,10)**@{-},
(10,0);(0,10)**@{-},
(0,-3)*{\varepsilon_r},
(10,13)*{\varepsilon_r},
(10,-3)*{\varepsilon_{r+1}},
(0,13)*{\varepsilon_{r+1}}
\endxy
} \\
&& \\
\vcenter{
\xy
(0,0);(4,4)**@{-},
(6,6);(10,10)**@{-},
(10,0);(0,10)**@{-},
(0,-3)*{_r},
(10,-3)*{_{r+1}},
(0,13)*{}
\endxy
} \quad &\longmapsto& \quad \bar a_r(\varepsilon) \vcenter{
\xy
(0,0);(0,10)**@{-},
(10,0);(10,10)**@{-},
(0,-3)*{\varepsilon_r},
(0,13)*{\varepsilon_r},
(10,-3)*{\varepsilon_{r+1}},
(10,13)*{\varepsilon_{r+1}}
\endxy
} \quad + \quad b_r(\varepsilon) \vcenter{
\xy
(0,0);(10,10)**@{-},
(10,0);(0,10)**@{-},
(0,-3)*{\varepsilon_r},
(10,13)*{\varepsilon_r},
(10,-3)*{\varepsilon_{r+1}},
(0,13)*{\varepsilon_{r+1}}
\endxy
}
\end {array}$$ Moreover, if $r = 1$, the second term on the right hand side should be omitted. Only diagonal entries of the matrix $\rho_\ell(\varphi(w))$ contribute to the trace. Hence, for each $\ell$ we need only consider those permutation diagrams that represent the identity permutation and whose first strand goes straight through. The theorem follows on comparing formulas ([\[diag coeff\]](#diag coeff){reference-type="ref" reference="diag coeff"}) and ([\[off-diag coeff\]](#off-diag coeff){reference-type="ref" reference="off-diag coeff"}) with ([\[scalars\]](#scalars){reference-type="ref" reference="scalars"}). ◻
:::
