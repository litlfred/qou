---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2)"
section_id: sec-002-3-decomposition-of-tensor-powers-of-t1-over-uqsl
section_title: "Decomposition of tensor powers of T(1) over Uq(sl2)"
section_number: 3
pages: 9-11
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
toc_source: outline
text_source: latex
latex_prose_ratio: 0.761
latex_coverage_ratio: 0.921
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of unity into direct sums"
---
[]{#tp label="tp"} We are interested in the tensor powers of the module $L(1)$ over the quantum group $U_q(\mathfrak{sl}_2)$, given explicitly by the following action of the generators: $$F v_1  = v_{-1} \quad \quad F v_{-1} =0 , \quad \quad Ev_1= 0, \quad \quad Ev_{-1} =   v_1 .$$ $$Kv_1 =  q v_1, \quad \quad  Kv_{-1} = q^{-1} v_{-1} .$$ $$E^{(l)} v_i =0, \quad \quad F^{(l)} v_i =0, \quad \quad i=1, -1 .$$ Since $L(1) \simeq T(1)$ is a tilting module, its tensor powers decompose into a direct sum of indecomposable tilting modules over $U_q(\mathfrak{sl}_2)$.

Let $V(n)$ be the simple module of highest weight $n \in \mathbb{Z}_{\geq 0}$ over the Lie algebra $\mathfrak{sl}(2, \mathbb{C})$. Define the coefficients $F_k^{(N)}$ as multiplicities in the following decomposition: $$\label{sl2} 
 V(1)^{\otimes N} = \bigoplus_{\substack{0 \leq k \leq N\\ k \equiv N\,{\rm mod}\,{2}}}  \; V(k)^{\oplus F_k^{(N)}}  \; .$$ i.e. $F_k^{(N)}=\dim\mathrm{Hom}(V(1)^{\otimes N}, V(k))$. It is known that $F_k^{(N)}$ are $$\label{tkN} 
F_k^{(N)} = {N\choose{\frac{N+k}{2}}} \frac{2k+2}{N+k+2}= {N\choose{\frac{N-k}{2}}}-{N\choose{\frac{N-k-2}{2}}} .$$

The following theorem provides the mutliplicities of $T(m)$ in $(L(1))^{\otimes N}$ over the algebra $U_q(\mathfrak{sl}_2)$.

::: theorem
see also [@And17], Corollary 3.5. []{#comb_coef label="comb_coef"} Using the classical coefficients $F_k^{(N)}$ defined in ([\[tkN\]](#tkN){reference-type="ref" reference="tkN"}), we have $$T(1)^{\otimes N} =  \bigoplus_{\substack{0 \leq k \leq N\\ k \equiv N\,{\rm mod}\,{2}}}  \; T(k)^{\oplus M_{k}^{(l)}(N)}  \; ,$$ where

1.  If $k = k_1 l -1 \leq N$ for $k_1 \geq 1$, then $M_{k_1 l -1}^{(l)}(N) = F_{k_1l-1}^{(N)}$,

2.  If $k = k_1 l + k_0 \leq N$ with $k_1 \geq 0$ and $0 \leq k_0 \leq l-2$, then $$\begin{aligned}
    \label{p-numbers}
    M_{k_1 l +k_0}^{(l)}(N) =   
     \sum\limits_{m=0}^{\lfloor\frac{N-k}{2l}\rfloor} F_{(k_1+2m)l + k_0}^{(N)}-  \sum\limits_{n=0}^{\lfloor\frac{N-(k_1+ 2)l +k_0+2}{2l}\rfloor} F_{(k_1+2n +2)l -k_0-2}^{(N)} .  \nonumber
    \end{aligned}$$ Here $\lfloor a\rfloor$ denotes the integer part (floor) of $a$. If the upper limit for $n$ is negative, the sum is void.
:::

::: proof
*Proof.* By Theorem [\[tilt_prop1\]](#tilt_prop1){reference-type="ref" reference="tilt_prop1"}, the tensor power of $T(1)  = L(1)$ is a tilting module whose decomposition into the indecomposable tilting modules is determined by its character. Denote by $M_{k}^{(l)}(N)$ the multiplicity of the tilting module $T(k)$ in the decomposition of the tensor power $T(1)^{\otimes N}$ over $U_q(\mathfrak{sl}_2)$.

Note that the formula [\[sl2\]](#sl2){reference-type="ref" reference="sl2"} provides the coefficients $F_k^{(N)}$ of the decomposition of the character of $T(1)^{\otimes N}$ in terms of the characters of the Weyl modules over $U_q(\mathfrak{sl}_2)$. Therefore our task reduces to rewriting this decomposition in the basis of the tilting characters.

The decomposition of the basis of tilting characters in terms of the Weyl characters is given by Corollary [\[tilt_char\]](#tilt_char){reference-type="ref" reference="tilt_char"}. Consider the vector space $Q_N$ spanned by the characters $\{ {\rm ch}_{W(k)} \}_{0 \leq k \leq N}$. Then the subspace $Q_{N, l-1} \subset Q_N$ spanned by $\{{\rm ch}_{W(k_1l-1)}\}_{0 < k_1l-1 \leq N}$ coincides with the subspace spanned by $\{{\rm ch}_{T(k_1l-1)}\}_{0 < k_1l-1 \leq N}$, and we have ${\rm ch}_{W(k_1l -1)} = {\rm ch}_{T(k_1l -1)}$, so that the change of basis matrix on $Q_{N, l-1}$ is trivial. This proves (a).

The subspace $Q_{\rm tilt}$ of $Q_N= Q_{\rm tilt} \oplus Q_{N, l-1}$ spanned by the characters $\{{\rm ch}_{W(k_1l + k_0)} \}_{\substack{0 \leq k_0 \leq l-2,\\ k_1l + k_0 \leq N}}$ splits into a direct sum of subspaces $$Q_{\rm tilt} =  \bigoplus_{0\leq k_0 \leq l-2} \; Q_{N, k_0}$$ spanned by the Weyl characters of dominant highest weights in the orbit of $k_0$ with respect to the reflections about the weights of the form $\{ jl-1\}_{ j \in \mathbb{Z}}$. This follows from the formula for the tilting character ${\rm ch}_{T(lk_1 + k_0)}$, $0 \leq k_0 \leq l-2$ in Corollary [\[tilt_char\]](#tilt_char){reference-type="ref" reference="tilt_char"} and is a manifestation of the *linkage principle* (cf. [@AT], 2.4). Let us fix $k_0$ such that $0  \leq k_0 \leq l-2$. Then the weights of the Weyl (or tilting) characters spanning $Q_{N, k_0}$ are the following: $$\begin{array}{ll} 
 \{ \lambda_{k_1} =   k_1 l + k_0 \}_{0 \leq k_1l + k_0 \leq N},   &    k_1   \; {\rm even}  \\
 \{ \lambda_{k_1} =  k_1 l + l-j_0 -2\}_{ 0 \leq  k_1 l + l - k_0 -2 \leq N}    &  k_1  \; {\rm odd} 
   \end{array}$$ Let $k_{\rm max}$ denote the maximal value of $k_1$ satisfying the above conditions. Then the Weyl characters that span $Q_{N, k_0}$ are enumerated by all integers $k_1$ such that $0 \leq k_1 \leq k_{\rm max}$, namely they are $\{{\rm ch}_{W(\lambda_{k_1})} \}_{0 \leq k_1 \leq k_{\rm max}}$. The same space is also spanned by the characters $\{ {\rm ch}_{T(\lambda_{k_1})} \}_{0 \leq k_1 \leq k_{\rm max}}$, and we can rewrite Corollary [\[tilt_char\]](#tilt_char){reference-type="ref" reference="tilt_char"} as follows: $$\begin{array}{l} 
 {\rm ch}_{T(\lambda_0)} = {\rm ch}_{W(\lambda_0)} , \\ 
  {\rm ch}_{T(\lambda_{k_1})} = {\rm ch}_{W(\lambda_{k_1})} + {\rm ch}_{W(\lambda_{k_1-1})}   , \;\;\;\;  1 \leq k_1 \leq k_{\rm max}  . 
  \end{array}$$ This defines the change of basis matrix between the tilting and Weyl characters and its inverse: $$\begin{array}{lll} 
  A = \left( \begin{array}{ccccc} 
              1 & 1 & 0 & 0 & 0 \\ 
                 & 1 & 1 & 0 & 0 \\ 
               \ldots  &   \ldots  &  \ldots & \ldots   & \ldots    \\
                 &    &    &  1  & 1  \\
                  &    &   &     &  1 \\    
                  \end{array} \right)  ,    &  \;\;\;\;\;   &
     A^{-1} = \left( \begin{array}{ccccc} 
              1 & -1 & 1 & -1 & 1 \\ 
                 & 1 & -1 & 1 & -1 \\ 
          \ldots  &   \ldots  &  \ldots & \ldots   & \ldots    \\
                 &    &    &  1  & -1  \\
                  &    &   &     &  1 \\    
                  \end{array} \right)     
                  \end{array}$$ Applying the matrix $A^{-1}$ to the column of classical coefficients $\{ t_{k, N}\}$, we obtain the formula given in part (b) of the theorem. ◻
:::

# Restriction from $U_q(\mathfrak{sl}_2)$ to $u_q(\mathfrak{sl}_2)$ {#restUu}

Let $U_q^0 \subset U_q({\mathfrak{s}l}_2)$ denote the subalgebra of $U_q({\mathfrak{s}l}_2)$ generated by $K^{\pm 1}$, $\left[  \begin{array}{c}  K ; c \\ t  \end{array}  \right]$ for $t \geq 0, c \in \mathbb{Z}$. Let $u_q^{\pm} \subset u_q$ denote the subalgebras of $u_q$ generated by $F$ and $E$ respectively. Using Theorem [\[tilt_prod\]](#tilt_prod){reference-type="ref" reference="tilt_prod"}, we can obtain the following result for the restriction of the tilting modules over the algebra $u_q^- U_q^0 u_q^+$:

::: corollary
[]{#restr label="restr"} Restricting Theorem [\[comb_coef\]](#comb_coef){reference-type="ref" reference="comb_coef"} over the algebra $u_q^- U_q^0 u_q^+$, we obtain after a change of variables $$T(k_1 l + (l-1) + k_0) \big\vert_{u_q^- U_q^0 u_q^+} \cong \bigoplus_{\substack{-k_1 \leq j \leq k_1\\  j\equiv k_1 \,{\rm mod}\, 2}} \mathbb{C}[lj]  \otimes  T((l-1) +k_0) .$$ Here $k_1 \in \mathbb{Z}_{\geq 0}$, $0 \leq k_0 \leq l-1$, and $\mathbb{C}[lj]$ is the one-dimensional module of weight $lj$.
:::

Note that $$K \mathbb{C}[lj] = q^{lj} \mathbb{C}[lj] = \left\{  \begin{array}{cl} 
                                          \mathbb{C}[lj] ,   &    j \; {\rm even}  \\
                                          -\mathbb{C}[lj],  & j \; {\rm odd }   
                                          \end{array}    \right.    
                                          \quad \quad  \quad   E \mathbb{C}[lj] = F \mathbb{C}[lj] = 0.$$

Here is the list of indecomposable modules that can occur in the tensor powers of $L(1) \cong  T(1)$ over $u_q^- U_q^0 u_q^+$: $$\{ T(k_0)  \}_{0 \leq k_0 \leq l-2 } , \quad   \{  \mathbb{C}[lj] \otimes T(l-1) \}_{j \in \mathbb{Z}} , \quad  
\{ \mathbb{C}[lj] \otimes T(l + k_0) \}_{j \in \mathbb{Z}, \; 0 \leq k_0 \leq l-2} .$$ Note that $T(k_0) \cong L(k_0)$, $0 \leq k_0 \leq l-2$ and $T(l-1)\cong L(l-1)$ are simple modules.

By Corollary [\[restr\]](#restr){reference-type="ref" reference="restr"} we have the following decomposition over $u_q^- U_q^0 u_q^+$: $$T(1)^{\otimes N} \cong \bigoplus_{0 \leq k_0 \leq l-2, \; k_0 \leq N} T(k_0)^{\oplus M_{k_0}^{(l)}(N)} \oplus \bigoplus_{j \in \mathbb{Z}, \; l|j| + l-1 \leq N}  (\mathbb{C}[lj] \otimes T(l-1))^{\oplus m^{(l)}_{l-1,j}(N)}  \oplus$$ $$\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;  \bigoplus_{j \in \mathbb{Z}, \; 
0 \leq k_0 \leq l-2, \; l|j| + l + k_0 \leq N} (\mathbb{C}[lj] \otimes T(l + k_0))^{\oplus m^{(l)}_{l+k_0,j}(N)} .$$ Here we denoted by $m^{(l)}_{l-1,j}(N)$ and $m^{(l)}_{l+k_0,j}(N)$ the multiplicities of $\mathbb{C}[lj] \otimes T(l-1)$ and $\mathbb{C}[lj] \otimes T(l + k_0)$ respectively.

::: theorem
[]{#uUu label="uUu"} Let $j \in \mathbb{Z}_{\geq 0}$, and $0 \leq k_0 \leq l-2$. The multiplicities $m^{(l)}_{l-1, \pm j}( N)$ and $m^{(l)}_{l+k_0, \pm j}( N)$ are given by the formulae $$m^{(l)}_{l-1,\pm j}(N) =  \sum_{s \geq \lfloor \frac{j}{2} \rfloor}  M^{(l)}_{l-1+ j({\rm mod}2)l + 2sl}(N) ;$$ $$m^{(l)}_{l+k_0,\pm j}(N)  = \sum_{s \geq \lfloor \frac{j}{2} \rfloor} M^{(l)}_{l+k_0+ j({\rm mod}2)l + 2sl}(N) .$$ The upper limit for $s$ can be calculated as $\lfloor \frac{N-(l-1+ j({\rm mod}2)l)}{2l}\rfloor$ or $\lfloor \frac{N-(l+k_0+ j({\rm mod}2)l)}{2l}\rfloor$, but in fact this is unnecessary because for higher $s$ the coefficients $M^{(l)}_\bullet(N)$ under the sum are zero.
:::

The proof of this is a direct consequence of Theorem [\[comb_coef\]](#comb_coef){reference-type="ref" reference="comb_coef"} and Corollary [\[restr\]](#restr){reference-type="ref" reference="restr"}.

Let $T(l + k_0)$, $0 \leq k_0 \leq l-2$ and $T(l-1)$ be the restrictions of the tilting modules with given highest weights to the small quantum group $u_q$. Following [@APW2], we conclude that these are indecomposable injective modules. Over the small quantum group $u_q(\mathfrak{sl}_2)$, define the modules $T_{\pm}(m)$, $m \geq l-1$ as follows: $$\mathbb{C}[lj] \otimes T(l+ k_0) \cong T_+(l+ k_0), \quad   \mathbb{C}[lj] \otimes T(l-1) \cong T_+(l-1)  \quad j  \; {\rm even}  ;$$ $$\mathbb{C}[lj] \otimes T(l+ k_0) \cong T_-(l+ k_0), \quad   \mathbb{C}[lj] \otimes T(l-1) \cong T_-(l-1)  \quad j  \; {\rm odd}  ;$$ Notes that we have natural isomorphisms $T_-(k)\simeq T_+(k)\otimes 1_{-}$ where $1_-$ is a 1-dimensional representation $K\mapsto -1, E,F\mapsto 0$.

Then over the small quantum group we obtain the following decomposition.

::: theorem
[]{#small_mult label="small_mult"} $$T(1)^{\otimes N} \cong \bigoplus_{0 \leq k_0 \leq l-2} T(k_0)^{\oplus M^{(l)}_{k_0}(N)} \oplus  T_+(l-1)^{\oplus m^{(l)}_{l-1,+}(N)}   \oplus  T_-(l-1)^{\oplus m^{(l)}_{l-1,-}(N)}  \oplus$$ $$\oplus  \bigoplus_{0 \leq k_0 \leq l-2}T_+(l + k_0)^{\oplus m^{(l)}_{l+k_0,+}(N)}    
 \oplus  \bigoplus_{0 \leq k_0 \leq l-2}T_-(l + k_0)^{\oplus m^{(l)}_{l+k_0,-}(N)} ,$$ where $$m^{(l)}_{l-1,+}(N) = \sum_{j \in \mathbb{Z}, \,{\rm even}} m^{(l)}_{l-1,j}(N) ,  \quad \quad  m^{(l)}_{l-1,-}(N) = \sum_{j \in \mathbb{Z}, \,{\rm odd}} m^{(l)}_{l-1,j}(N) ,$$ $$m^{(l)}_{l+k_0,+}(N)  = \sum_{j \in \mathbb{Z}, \,{\rm even} } m^{(l)}_{l+k_0,j}(N)  \quad \quad  m^{(l)}_{l+k_0,-}(N) = \sum_{j \in \mathbb{Z}, \,{\rm odd} } m^{(l)}_{l+k_0,j}(N) .$$
:::

This theorem follows directly from Theorem [\[uUu\]](#uUu){reference-type="ref" reference="uUu"} and the definition of the modules $T_\pm (l + k_0)$, $T_\pm(l-1)$.
