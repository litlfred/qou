---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-016-case-2
section_title: "Case 2"
section_number: null
pages: 21-24
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.96
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
::: prop
[]{#HC_case_2 label="HC_case_2"} In case 2, $\mu =1$, $\lambda= q^{-(N+2)}$, $N \geq 0$, we have $HC_0^\sigma(\mathcal{A})$ infinite dimensional, while $$HC_1^\sigma(\mathcal{A}) \cong   
    \left\{
    \begin{array}{ll}
     k^{N+1} &: N \; \mathrm{even}\\
     k^{N+2} &: N \; \mathrm{odd}
    \end{array}\right., \quad HC_2^\sigma(\mathcal{A}) \cong k^{N+2}, \quad N \; \mathrm{odd}$$
:::

::: pf
Recall from ([\[HH_0_case_2\]](#HH_0_case_2){reference-type="ref" reference="HH_0_case_2"}) that $$HH_0^\sigma(\mathcal{A}) = 
( \sum_{s \in S}^\oplus  \; k[ b^s ] ) \oplus 
( \sum_{t \in S}^\oplus  \; k[ c^t ] ) \oplus 
( \sum_{0 \leq i \leq N+2}^\oplus  \; k[ b^i c^{N+2-i} ] )$$ where $S = \{ \mathrm{integers}\geq N+3 \} \cup \{ N+1, N-1, N-3, \ldots \geq 0 \}$, with the convention that if $0 \in S$, we include only one copy of $k[1]$. From ([\[HH_1_case_3a\]](#HH_1_case_3a){reference-type="ref" reference="HH_1_case_3a"}) $$HH_1^\sigma(\mathcal{A}) = 
( \sum_{s \in S'}^\oplus \; k[( b^s ,b)] ) \oplus
( \sum_{t \in S'}^\oplus \; k[( c^t ,c)] ) \oplus$$ $$( \sum_{0 \leq i \leq N}^\oplus \; k[( b^i c^{N+1-i} ,b )] ) \oplus
( \sum_{0 \leq i \leq  N}^\oplus \; k[( b^{i+1} c^{N-i} ,c )] ) \oplus
k [ \omega_1 ]$$ Here $S' = \{ \mathrm{integers}\geq N \} \cup \{ N-2, N-4, \ldots \geq 0 \}$, and $[ \omega_1]=[(b,c)] = - [(c,b)]$ for $N$ odd, $[\omega_1]=0$ for $N$ even. Now, for $s$, $t \geq 0$, $$B_0 [ b^{s+1} ] = (s+1) [ (b^s ,b)], \quad B_0 [ c^{t+1} ] = (t+1) [ (c^t ,c)]$$ Note that, for $s \geq 0$, $s+1 \in S$ if and only if $s \in S'$. We also have $$B_0 [1] = [(1,1)] = [ b (1,1,1)] =0$$ By Lemma [\[lemma:B_0_x\^s_y\^t\]](#lemma:B_0_x^s_y^t){reference-type="ref" reference="lemma:B_0_x^s_y^t"}, for $0 \leq i \leq N$ $$B_0 [ b^{i+1} c^{N+1-i} ]  = (N+1-i) [(b^{i+1} c^{N-i} , c)] + (i+1) [(b^i c^{N+1-i} ,b)]$$ Hence $\mathrm{ker}(B_0) = k[1]$ if $N$ is odd, 0 if $N$ is even. Further, $$\label{HC_1_case_3}
 \label{HH_1_quotient_im_B_0}
 HH_1^\sigma(\mathcal{A}) / \mathrm{im}(B_0) \cong 
  \left\{
    \begin{array}{ll}
     k^{N+1} = \sum_{0 \leq i \leq N}^\oplus k [ \omega_1 (N,i) ]  &: N \; \mathrm{even}\\
     {} & {}\\
     k^{N+2} = \sum_{0 \leq i \leq N}^\oplus k [ \omega_1 (N,i) ]  \oplus k[ \omega_1 ] &: N \; \mathrm{odd}
    \end{array}\right.$$ with generators $$\label{omega_1_N_i}
[\omega_1 (N,i) ] = [(xc,b)] = [(bx,c)], \quad x= b^i c^{N-i}, \quad 0 \leq i \leq N$$ together with (if $N$ is odd) $[\omega_1] = [(c,b)] = -[(b,c)]$.

::: prop
[]{#B_1= label="B_1="} For $N$ odd, $B_1 =0$. For $N$ even, $\mathrm{im}(B_1)$ is at most one-dimensional, spanned by $[B_1 ( \omega_1 (N , {\frac{1}{2}} N))]$.
:::

::: pf
Recall that $HH_2^\sigma(\mathcal{A}) \cong k^{N+1}$, with generators $\omega_2 (N,i)$, $0 \leq i \leq N$ given in ([\[HH_2_case_3\]](#HH_2_case_3){reference-type="ref" reference="HH_2_case_3"}). We use the construction of $\sigma$-twisted Hochschild $n$-cocycles of Proposition [\[hoch_n_cocycle\]](#hoch_n_cocycle){reference-type="ref" reference="hoch_n_cocycle"}. Using ([\[h_1\]](#h_1){reference-type="ref" reference="h_1"})-([\[h_c\^t+1\]](#h_c^t+1){reference-type="ref" reference="h_c^t+1"}), for each $n \in \mathbb{Z}$ define a trace $h_n$ by $$\label{h_n}
h_n ( a^{i+1} ) = 0 = h_n ( d^{i+1}),  \quad h_n (b^j ) = \delta_{n,j}, \quad h_n ( c^j ) = \delta_{-n,j}$$ for $i$, $j \geq 0$. For the derivation $\partial_b$ ([\[der_b\]](#der_b){reference-type="ref" reference="der_b"}) and $\sigma$-derivation $\partial$ ([\[sigma_der\]](#sigma_der){reference-type="ref" reference="sigma_der"}) define a $\sigma$-twisted Hochschild 2-cocycle $\phi_{2,n}$ by $$\label{phi_2_n}
 \phi_{2,n}  (x,y,z) = h_n ( x \partial_b (y) \partial(z))$$

::: lemma
$< \phi_{2,n},   \omega_2 (N,i) > = 0$, unless $n = 2i-N$. For $i \neq {\frac{1}{2}} N$, we have $< \phi_{2,2i-N},   \omega_2 (N,i) > \neq 0$.
:::

::: pf
Directly, $< \phi_{2,n},   \omega_2 (N,i) > = < \phi_{2,n},   q (bdx,c,a) - q^{-1} (cax,b,d)>$ (considering only potentially nonzero terms) $$\begin{aligned}
&&=h_n ( qbdx (-c) a - q^{-1} cax b (- \lambda^{-1} d)) = h_n ( q^{-1} \lambda^{-1} caxb d - q bdxca )\nonumber\\
&&= h_n ( q^N \lambda^{-1} bcx ad - q^{-N} bcx da) = h_n ( q^{-N} bcx ( q^{3N+2} ad - da) )\nonumber\\
&&= q^{N+2} ( q^N - q^{-N}) h_n ( bcxad) = q^{N+2} ( q^N - q^{-N}) h_n ( bcx (1 + qbc))\nonumber\\
&&= {\frac{ q^2 ( q^{2N} - 1) ( q^2 -1)}{( q^{N+4} -1)}} h_n ( bcx)\nonumber
\end{aligned}$$ Since $bc x = b^{i+1} c^{N+1-i}$, it's clear from ([\[h_b\^s+1\]](#h_b^s+1){reference-type="ref" reference="h_b^s+1"}), ([\[h_c\^t+1\]](#h_c^t+1){reference-type="ref" reference="h_c^t+1"}) that $h_n (bcx) =0$ unless $n = (i+1) - (N-i+1) = 2i -N$, and $h_{2i-N} (bcx) \neq 0$ unless $2i = N$.
:::

To find $\mathrm{im}(B_1)$, since $B_1 \circ B_0 =0$, we need only consider $B_1$ applied to $\omega_1$ and the $\omega_1 (N,i)$. For $[\omega_1] = [(c,b)] = -[(b,c)]$, which is nonzero if and only if $N$ is odd, we have $\deg( \omega_1 ) = (0,0)$ for the $\mathbb{Z}^2$-grading ([\[Z\^2_grading\]](#Z^2_grading){reference-type="ref" reference="Z^2_grading"}). The maps $B_n$ preserve the grading, so $\deg( B_1 ( \omega_1 ) ) = (0,0)$ also. Now, $\deg( \omega_2 (N,i)) = (0,2i-N) \neq (0,0)$ for any $N$, $i$ since $N$ is odd. The Hochschild boundary maps $b$ also preserve the grading, so $B_1 (\omega_1)$ cannot be cohomologous to any nontrivial element of $HH_2^\sigma(\mathcal{A})$.

Now consider the generators $\omega_1 (N,i)$ ([\[omega_1_N_i\]](#omega_1_N_i){reference-type="ref" reference="omega_1_N_i"}). These contain only $b$'s and $c$'s, so combining this with ([\[B_n\]](#B_n){reference-type="ref" reference="B_n"}), it is immediate that each $\phi_{2,n}$ vanishes on $\mathrm{im}(B_1)$. So for $i \neq {\frac{1}{2}}N$, we have $[ B_1 ( \omega_1 (N,i))] =0$.
:::

The second page of the spectral sequence reads:

$$\begin{CD}
    @ V{} VV @ V{} VV @ V{} VV @ . @ . @ . @ .\\
    {0} @ <<< {HH_3^\sigma(\mathcal{A})/ \mathrm{im}(B_2) } @ <<< {\mathrm{ker}(B_2) / \mathrm{im}( B_1)} @ <<< {} @ . @ . @ . @ .\\
    @ V{} VV @ V{} VV @ V{} VV @ . @ . @ . @ .\\
    {HH_3^\sigma(\mathcal{A}) / \mathrm{im}(B_2)  } @ <<< {\mathrm{ker}(B_2) / \mathrm{im}( B_1)} @ <<< {\mathrm{ker}(B_1) / \mathrm{im}( B_0)} @ <<< {}  @ . @ . @ . @ .\\
    @ VVV @ V{} VV @ V{} VV @ . @ . @ . @ .\\
    {HH_2^\sigma(\mathcal{A}) / \mathrm{im}(B_1)} @ <<< {\mathrm{ker}(B_1) / \mathrm{im}( B_0)} @ <<< {\mathrm{ker}(B_0)}  @ . @ . @ . @ . @ .\\
    @ V{} VV @ V{} VV @ . @ . @ . @ . @ .\\
{HH_1^\sigma(\mathcal{A}) / \mathrm{im}(B_0)} @ <<< {\mathrm{ker}(B_0)} @ . @ . @ . @ . @ . \\
    @ V{} VV @ . @ .  @ . @ . @ . @ .\\
    {HH_0^\sigma(\mathcal{A})} @ . @ . @ . @ . @ . @ .\\
        \end{CD}$$\
The only potentially nonzero differential is $f : \mathrm{ker}(B_0) \rightarrow HH_3^\sigma(\mathcal{A}) / \mathrm{im}(B_2)$, and after this step the spectral sequence stabilises, giving $$\begin{aligned}
&&HC_0^\sigma(\mathcal{A}) = HH_0^\sigma(\mathcal{A}),\quad HC_1^\sigma(\mathcal{A}) = HH_1^\sigma(\mathcal{A}) / \mathrm{im}(B_0),\nonumber\\
&&HC_2^\sigma(\mathcal{A}) = (HH_2^\sigma(\mathcal{A}) / \mathrm{im}(B_1)) \oplus \mathrm{ker}(B_0)\nonumber\\
&&HC_{2n+3}^\sigma(\mathcal{A}) = ((HH_3^\sigma(\mathcal{A}) / \mathrm{im}(B_2) )/ \mathrm{im}f ) \oplus (\mathrm{ker}(B_1) / \mathrm{im}(B_0)),\nonumber\\
&&HC_{2n+4}^\sigma(\mathcal{A}) = (\mathrm{ker}(B_2) / \mathrm{im}( B_1)) \oplus \mathrm{ker}( f)\nonumber
\end{aligned}$$ Hence $HC_0^\sigma(\mathcal{A})$ is infinite-dimensional, given by ([\[HH_0_case_2\]](#HH_0_case_2){reference-type="ref" reference="HH_0_case_2"}), whilest $HC_1^\sigma(\mathcal{A})$ is given by ([\[HC_1_case_3\]](#HC_1_case_3){reference-type="ref" reference="HC_1_case_3"}). Now, $\mathrm{ker}(B_0) = k[1]$, which is nonzero if and only if $N$ is odd. So for $N$ even, $\mathrm{ker}(f) = 0 = \mathrm{im}(f)$. For $N$ odd, $\mathrm{im}(B_1) =0$, hence $HC_2^\sigma(\mathcal{A}) = HH_2^\sigma(\mathcal{A}) \oplus k[1] \cong k^{N+2}$. This completes the proof of Proposition [\[HC_case_2\]](#HC_case_2){reference-type="ref" reference="HC_case_2"}.
:::

Recall that $HH_2^\sigma(\mathcal{A})$ and $HH_3^\sigma(\mathcal{A})$ are both isomorphic to $k^{N+1}$ with generators $\omega_2 (N,i)$ ([\[omega_2_N_i\]](#omega_2_N_i){reference-type="ref" reference="omega_2_N_i"}), $\omega_3 (N,i)$ ([\[omega_3_N_i\]](#omega_3_N_i){reference-type="ref" reference="omega_3_N_i"}) ($0 \le i \le N$) respectively. By symmetry and the $\mathbb{Z}^2$-grading ($\deg(\omega_2 (N,i)) = (0, 2i-N) = \deg( \omega_3 (N,i))$) we expect, but do not have a proof for:

::: conj
1.  For $N$ even, $[B_1 ( \omega_1 (N, {\frac{1}{2}}N))] \neq 0 \in HH_2^\sigma(\mathcal{A})$, and is proportional to $[\omega_2 (N, {\frac{1}{2}N})]$.

2.  For all $N$, $B_2 :  HH_2^\sigma(\mathcal{A}) / \mathrm{im}(B_1)  \rightarrow HH_3^\sigma(\mathcal{A})$ is injective. It follows that for $N$ odd, $f : \mathrm{ker}(B_0 ) \rightarrow HH_3^\sigma(\mathcal{A})$ is the zero map.
:::

From this it would follow that, for $N$ even, $HC^\sigma_2 (\mathcal{A}) \cong k^N$, generated by $[\omega_2 (N,i)]$ for $i \neq {\frac{1}{2}}N$, $HC_{2n+3}^\sigma(\mathcal{A}) \cong k^{N+2}$, generated by $[\omega_3 (N, {\frac{1}{2}}N)]$ together with ([\[HH_1_quotient_im_B_0\]](#HH_1_quotient_im_B_0){reference-type="ref" reference="HH_1_quotient_im_B_0"}), and $HC_{2n+4}^\sigma(\mathcal{A}) \cong k[\omega_2 (N, {\frac{1}{2}}N)]$. For $N$ odd we would have $HC_{2n+3}^\sigma(\mathcal{A}) \cong k^{N+2}$, given by ([\[HH_1_quotient_im_B_0\]](#HH_1_quotient_im_B_0){reference-type="ref" reference="HH_1_quotient_im_B_0"}), and $HC_{2n+4}^\sigma(\mathcal{A}) \cong k[1]$.
