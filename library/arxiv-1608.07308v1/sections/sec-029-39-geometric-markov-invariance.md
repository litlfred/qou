---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-029-39-geometric-markov-invariance
section_title: "Geometric Markov invariance"
section_number: 3.9
pages: 27-30
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.873
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:markov label="sub:markov"}

In the category of Soergel bimodules, equation [\[eqn: R1 upgraded\]](#eqn: R1 upgraded){reference-type="eqref" reference="eqn: R1 upgraded"} governs the behavior of objects under Markov moves: $$\label{eqn:markov}
\alpha \leadsto i(\alpha), \qquad \alpha \leadsto i(\alpha) \cdot \sigma_n, \qquad \alpha \leadsto i(\alpha) \cdot \sigma^{-1}_n$$ where $i$ is the operation of adding an extra strand to a braid $\alpha$ on $n$ strands. We will now study how the complexes of sheaves $\mathcal{B}(\alpha) = \iota_*(\alpha) \in D^b(\mathrm{Coh}_{\mathbb{C}^{*} \times \mathbb{C}^*}(\mathrm{FHilb}_n^\text{dg}(\mathbb{C}))$ behave under the same moves. Throughout this Subsection, we write $\mathrm{FHilb}_n^\text{dg}= \mathrm{FHilb}_n^\text{dg}(\mathbb{C})$ and: $$\pi:\mathrm{FHilb}_{n+1}^{\text{dg}}  \rightarrow \mathrm{FHilb}_n^{\text{dg}} \times \mathbb{C}$$ for the standard projection. The following Corollary is an easy consequence of Conjecture [\[conj:main\]](#conj:main){reference-type="ref" reference="conj:main"}, as we will show in Subsection [\[sub:proof\]](#sub:proof){reference-type="ref" reference="sub:proof"}.

::: corollary
[]{#cor:markov 1 label="cor:markov 1"} For any braid $\alpha$ on $n$ strands, we have: $$\label{eqn:markov 0}
\mathcal{B}(i(\alpha)) = \pi^*(\mathcal{B}(\alpha)) .$$
:::

To tackle the second and third Markov moves of [\[eqn:markov\]](#eqn:markov){reference-type="eqref" reference="eqn:markov"}, we consider the dg subscheme: $$\label{eqn:def zn}
Z_n \subset \mathrm{FHilb}_{n+1}^\text{dg}$$ $$\mathcal{O}_{Z_n} := \left[\ldots \xrightarrow{y_{n,n+1}} \frac {q^2t\mathcal{L}_n}{\mathcal{L}_{n+1}} \xrightarrow{x_n-x_{n+1}} \frac {qt\mathcal{L}_n}{\mathcal{L}_{n+1}} \xrightarrow{y_{n,n+1}}  q\mathcal{O}\xrightarrow{x_n-x_{n+1}} \mathcal{O}\right],$$ where $y_{n,n+1}$ denotes the last subdiagonal entry of the matrix $Y$ of [\[eqn:triple matrices\]](#eqn:triple matrices){reference-type="eqref" reference="eqn:triple matrices"}, regarded as an endomorphism $t\mathcal{L}_n \rightarrow \mathcal{L}_{n+1}$ on $\mathrm{FHilb}_{n+1}^{\text{dg}}$. The fact that $\mathcal{O}_{Z_n}$ is a complex follows from: $$0 = [X,Y]_{n,n+1} = x_n y_{n,n+1} - y_{n,n+1} x_{n+1}$$

::: conjecture
[]{#conj:markov label="conj:markov"} For any braid $\alpha$ on $n$ strands, we have: $$\label{eqn:markov 1}
\mathcal{B}(i(\alpha) \cdot \sigma_n) = \pi^*(\mathcal{B}(\alpha)) \otimes \mathcal{O}_{Z_n} .$$
:::

::: corollary
[]{#cor:markov 2 label="cor:markov 2"} Conjecture [\[conj:markov\]](#conj:markov){reference-type="ref" reference="conj:markov"} implies that for any braid $\alpha$ on $n$ strands: $$\label{eqn:markov 2}
\mathcal{B}(i(\alpha) \cdot \sigma^{-1}_n) = \pi^*(\mathcal{B}(\alpha)) \otimes \mathcal{O}_{Z_n} \otimes \frac {\mathcal{L}_n}{\mathcal{L}_{n+1}} .$$
:::

::: proof
*Proof.* Note the following the equation in the braid group: $$L_{n+1} = \sigma_n \cdot L_n \cdot \sigma_n \Rightarrow \sigma_{n}^{-1} = L_{n+1}^{-1} \cdot \sigma_n \cdot L_{n} \Rightarrow$$ $$i(\alpha) \cdot  \sigma_n^{-1} = i(\alpha) \cdot L_{n+1}^{-1}\cdot \sigma_n  \cdot L_{n} = L_{n+1}^{-1}\cdot i(\alpha) \cdot \sigma_n  \cdot L_{n}.$$ since $L_{n+1}$ commutes with the image of $i$. Applying $\mathcal{B}(-)$ to the above equation implies: $$\mathcal{B}(i(\alpha)\cdot \sigma_n^{-1}) = \iota_*( i(\alpha)  \otimes  \sigma_n^{-1})  = \iota_*(L_{n+1}^{-1}\otimes i(\alpha)  \otimes \sigma_n  \otimes L_n))$$ As in Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"}, we have $L_k = \iota^*(\mathcal{L}_k)$ for all $k$, and therefore [\[eqn:sk\]](#eqn:sk){reference-type="eqref" reference="eqn:sk"} implies [\[eqn:markov 2\]](#eqn:markov 2){reference-type="eqref" reference="eqn:markov 2"}. ◻
:::

Equations [\[eqn:markov 0\]](#eqn:markov 0){reference-type="eqref" reference="eqn:markov 0"}--[\[eqn:markov 2\]](#eqn:markov 2){reference-type="eqref" reference="eqn:markov 2"} are compatible with the stabilization invariance of $\mathop{\mathrm{HHH}}$ at the level of equivariant Euler characteristic.

::: proposition
[]{#prop:markov integrals label="prop:markov integrals"}

For any braid $\alpha$ on $n$ strands, we have: $$\label{eqn:markov int 0}
\chi \left( 

\mathcal{B}(i(\alpha)) \otimes \wedge^\bullet \mathcal{T}_{n+1}^\vee  \right) = \frac {1-a}{1-q} \chi \left( 

 \mathcal{B}(\alpha) \otimes \wedge^\bullet \mathcal{T}_n^\vee \right)$$ Assuming Conjecture [\[conj:markov\]](#conj:markov){reference-type="ref" reference="conj:markov"}, we further have: $$\label{eqn:markov int 1}
\chi \left( 

\mathcal{B}(i(\alpha) \cdot \sigma_n) \otimes \wedge^\bullet \mathcal{T}_{n+1}^\vee \right)\ \ = \ \ \chi \left(

  \mathcal{B}(\alpha) \otimes \wedge^\bullet \mathcal{T}_n^\vee \right)$$ $$\label{eqn:markov int 2}
\chi \left(

  \mathcal{B}(i(\alpha) \cdot \sigma^{-1}_n) \otimes \wedge^\bullet \mathcal{T}_{n+1}^\vee \right) =  \frac a{qt} \chi \left( 
  
   \mathcal{B}(\alpha) \otimes \wedge^\bullet \mathcal{T}_n^\vee \right)$$
:::

::: proof
*Proof.* We replace the sheaves in [\[eqn:markov int 0\]](#eqn:markov int 0){reference-type="eqref" reference="eqn:markov int 0"}--[\[eqn:markov int 2\]](#eqn:markov int 2){reference-type="eqref" reference="eqn:markov int 2"} by their $K$--theory classes and write: $$[\mathcal{T}_{n+1}] = \pi^*\left(  [\mathcal{T}_n] \right) + [\mathcal{L}_{n+1}]$$ and: $$\label{eqn:k-theory zn}
[\mathcal{O}_{Z_n}] = (1-q) \left(1-\frac {qt[\mathcal{L}_n]}{[\mathcal{L}_{n+1}]} \right)^{-1}$$ Since $\int$ is just pushforward to a point, it can be decomposed along the projection map $\pi: \mathrm{FHilb}_{n+1}^\text{dg}\rightarrow \mathrm{FHilb}_n^\text{dg}\times \mathbb{C}$. In other words, for all sheaves $\mathcal{A}$ one has: $$\int_{\mathrm{FHilb}_{n+1}^\text{dg}} \mathcal{A}= \int_{\mathrm{FHilb}_{n}^\text{dg}\times \mathbb{C}}\pi_*\mathcal{A}$$ We will apply this equality for the $K$--theory class: $$[\mathcal{A}] = [\mathcal{B}(i(\alpha))] \cdot \wedge^\bullet [\mathcal{T}_{n+1}^\vee] = \pi^*\left( [\mathcal{B}(\alpha)] \cdot  \wedge^\bullet [\mathcal{T}_{n}^\vee] \right) \cdot \left(1- \frac a{[\mathcal{L}_{n+1}]} \right)$$ where in the second equality we have used [\[eqn:markov 0\]](#eqn:markov 0){reference-type="eqref" reference="eqn:markov 0"}. Then we may prove [\[eqn:markov int 0\]](#eqn:markov int 0){reference-type="eqref" reference="eqn:markov int 0"} by noting that: $$\chi \left( 

[\mathcal{B}(i(\alpha))] \cdot \wedge^\bullet [\mathcal{T}_{n+1}^\vee] \right)= \chi \left(  

 \pi_* \left[ \pi^*\left( [\mathcal{B}(\alpha)] \cdot \wedge^\bullet [\mathcal{T}_{n}^\vee] \right) \cdot \left(1- \frac a{[\mathcal{L}_{n+1}]} \right) \right] \right)=$$ $$\label{eqn:above formula}
= \chi \left( 

[\mathcal{B}(\alpha)] \cdot \wedge^\bullet [\mathcal{T}_{n}^\vee] \cdot \pi_*\left(1- \frac a{[\mathcal{L}_{n+1}]} \right) \right)= (1-a) \chi \left( 

[\mathcal{B}(\alpha)] \cdot \wedge^\bullet [\mathcal{T}_{n}^\vee]\right)$$ (the additional factor of $1-q$ in the right hand side of [\[eqn:markov int 0\]](#eqn:markov int 0){reference-type="eqref" reference="eqn:markov int 0"} comes from integrating over $\mathbb{C}$). To establish the last equality in [\[eqn:above formula\]](#eqn:above formula){reference-type="eqref" reference="eqn:above formula"}, we note that it holds at the categorified level: $$\label{eqn:f1}
\pi_*\left(\mathcal{O}_{\mathrm{FHilb}_{n+1}^\text{dg}} \right) = \mathcal{O}_{\mathrm{FHilb}_{n}^\text{dg}\times \mathbb{C}} = \pi_* \left(\mathcal{O}_{\mathrm{FHilb}_{n+1}^\text{dg}} \otimes \mathcal{L}_{n+1}^{-1}  \right)$$ where the first equality is a consequence of the fact that $\pi$ is the projectivization of $\mathcal{E}^\vee_n$, and the second equality follows from the first and [\[eqn:serre\]](#eqn:serre){reference-type="eqref" reference="eqn:serre"} for $\mathcal{A}= \mathcal{O}$. Similarly, if we assume formula [\[eqn:markov 1\]](#eqn:markov 1){reference-type="eqref" reference="eqn:markov 1"} (which would also imply [\[eqn:markov 2\]](#eqn:markov 2){reference-type="eqref" reference="eqn:markov 2"}, according to Corollary [\[cor:markov 2\]](#cor:markov 2){reference-type="ref" reference="cor:markov 2"}), then relations [\[eqn:markov int 1\]](#eqn:markov int 1){reference-type="eqref" reference="eqn:markov int 1"} and [\[eqn:markov int 2\]](#eqn:markov int 2){reference-type="eqref" reference="eqn:markov int 2"} follow from: $$\label{eqn:f2}
\pi_*(\mathcal{O}_{Z_n}) = \left[q\mathcal{O}\xrightarrow{x_n-x_{n+1}}\mathcal{O}\right], \qquad \pi_* \left(\mathcal{O}_{Z_n} \otimes \frac 1{\mathcal{L}_{n+1}} \right) = 0$$ $$\label{eqn:f3}
\pi_* \left(\mathcal{O}_{Z_n} \otimes \frac 1{\mathcal{L}^2_{n+1}} \right) = \left[\frac 1{t \mathcal{L}_n} \xrightarrow{x_n-x_{n+1}} \frac 1{qt \mathcal{L}_n} \right][1]$$ We will only prove these equalities at the level of $K$--theory, by using [\[eqn:k-theory zn\]](#eqn:k-theory zn){reference-type="eqref" reference="eqn:k-theory zn"}. Indeed, since the map $\pi$ is $\mathbb{P}\mathcal{E}^\vee_n$, the push-forwards of the powers of $\mathcal{L}_{n+1} = \mathcal{O}(1)$ are encoded by: $$\label{eqn:expansion}
\pi_* \left( \delta\left(\frac {\mathcal{L}_{n+1}}z \right) \right) = S^*_{z \sim \infty} [\mathcal{E}_n] - S^*_{z \sim 0} [\mathcal{E}_n] =$$ $$= \frac {\wedge^*_{z \sim \infty} [qt\mathcal{T}_n] \wedge^*_{z \sim \infty} [\mathcal{T}_n]}{(1-z^{-1})\wedge^*_{z \sim \infty} [q\mathcal{T}_n] \wedge^*_{z \sim \infty} [t\mathcal{T}_n]} - \frac {\wedge^*_{z \sim 0} [qt\mathcal{T}_n] \wedge^*_{z \sim 0} [\mathcal{T}_n]}{(1-z^{-1})\wedge^*_{z \sim 0} [q\mathcal{T}_n] \wedge^*_{z \sim 0} [t\mathcal{T}_n]}$$ where the $\delta$ function is $\delta(z) = \sum_{k=-\infty}^{\infty} z^k$. In the right hand side, we write: $$S^*_z[\mathcal{V}] = \sum_{k=0}^\infty (-z)^{-k} \cdot S^k\mathcal{V}, \qquad \wedge^*_z[\mathcal{V}] = \sum_{k=0}^\infty (-z)^{-k} \cdot \wedge^k\mathcal{V}$$ and the notations $S^*_{z\sim 0}, \wedge^*_{z\sim 0}$ and $S^*_{z\sim \infty}, \wedge^*_{z\sim \infty}$ refer to expanding the rational functions $S^*_z, \wedge^*_z$ in the domains $z\sim 0$ and $z\sim \infty$, respectively. Applying [\[eqn:k-theory zn\]](#eqn:k-theory zn){reference-type="eqref" reference="eqn:k-theory zn"}, we obtain: $$\pi_*\left( [\mathcal{O}_{Z_n}] \cdot \delta\left(\frac {\mathcal{L}_{n+1}}z \right) \right) = \pi_*\left( \frac {1-q}{1-\frac {qt[\mathcal{L}_n]}{[\mathcal{L}_{n+1}]}} \cdot \delta\left(\frac {\mathcal{L}_{n+1}}z \right) \right) = \frac {1-q}{1-\frac {qt[\mathcal{L}_n]}z} \cdot \pi_* \left( \delta\left(\frac {\mathcal{L}_{n+1}}z \right) \right)$$ and we can compute the right hand side using [\[eqn:expansion\]](#eqn:expansion){reference-type="eqref" reference="eqn:expansion"}. To obtain [\[eqn:f2\]](#eqn:f2){reference-type="eqref" reference="eqn:f2"} and [\[eqn:f3\]](#eqn:f3){reference-type="eqref" reference="eqn:f3"}, we must extract the coefficients of $z^0$, $z^{1}$, $z^2$ in the right hand side of the above equality, and it is easy to see that one obtains $1-q$, $0$ and $\frac {q-1}{qt[\mathcal{L}_n]}$, respectively. ◻
:::
