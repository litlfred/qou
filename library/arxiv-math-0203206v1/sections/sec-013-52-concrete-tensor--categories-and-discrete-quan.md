---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-013-52-concrete-tensor--categories-and-discrete-quan
section_title: "Concrete Tensor $*$-Categories and Discrete Quantum Semigroups"
section_number: 5.2
pages: 28-32
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.982
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
From now on, ${\cal C}$ will be a semisimple strict tensor $*$-category. (As discussed in the Introduction, the strictness assumption does not entail a loss of generality.) We will introduce other requirements as we proceed. By Theorem [\[t-equiv\]](#t-equiv){reference-type="ref" reference="t-equiv"} we have associated a $*$-algebra $A$ to a $*$-preserving functor $E: {\cal C}\rightarrow{\cal H}$. The aim of this subsection is to endow $A$ with the structure of a discrete aqg under suitable conditions on ${\cal C}$ and $E$. To bring out the special rôle of the target category ${\cal H}$, we work in a more general setting as far as seems justifiable.

Let $E: {\cal C}\rightarrow{\cal D}$ be a $*$-preserving tensor functor into some tensor $*$-category ${\cal D}$. Recall that by Proposition [\[p-defprod\]](#p-defprod){reference-type="ref" reference="p-defprod"}, $\mathrm{Nat}\,E$ is a unital $*$-algebra for every $*$-preserving functor $E: {\cal C}\rightarrow{\cal D}$.

::: prop
Let ${\cal C}, {\cal D}$ be tensor $*$-categories, ${\cal C}$ being strict, and let $E: {\cal C}\rightarrow{\cal D}$ be a $*$-preserving tensor functor. Then $$\tilde{\Delta}: \mathrm{Nat}\,E\rightarrow\mathrm{Nat}\,E\otimes, \quad b=(b_X) \ \mapsto \ \tilde{\Delta}(b)\ =\ 
   (\tilde{\Delta}(b)_{Y,Z}), \quad \tilde{\Delta}(b)_{Y,Z}=b_{Y\otimes Z}$$ defines a unital $*$-homomorphism.
:::

*Proof. *The morphisms in ${\cal C}\times{\cal C}$ are of the form $s\times t$ where $s: Y\rightarrow Y',\ t: Z\rightarrow Z'$. Then $s\otimes t\in\mathrm{Mor}(Y\otimes Z,Y'\otimes Z')$. We compute $$(E\otimes) (s\times t) \, \,\circ\,\tilde{\Delta}(b)_{Y,Z} = 
   E(s\otimes t) \, \,\circ\,\, b_{Y\otimes Z} = b_{Y'\otimes Z'} \, \,\circ\,E(s\otimes t) = 
   \tilde{\Delta}(b)_{Y',Z'} \,\circ\,(E\otimes) (s\times t),$$ where we used $b=(b_X)\in\mathrm{Nat}\,E$. We conclude that $\tilde{\Delta}(b)\in\mathrm{Nat}\,E\otimes$. That $b\mapsto\tilde{\Delta}(b)$ is a unital $*$-homomorphism follows immediately from Proposition [\[p-defprod\]](#p-defprod){reference-type="ref" reference="p-defprod"}.

We now consider the analogues of $(\Delta\otimes\iota)$, ${\cal C}$ being strict, and $(\iota\otimes\Delta)$ in the present general setting. $\otimes^2$ will denote the functor $\otimes\,\circ\,(\otimes\times Id)=\otimes\,\circ\,(Id\times\otimes):{\cal C}\times{\cal C}\times{\cal C}\rightarrow{\cal C}$, where we have used the strictness of ${\cal C}$.

::: prop
[]{#p-coassoc label="p-coassoc"} Let ${\cal C}, {\cal D}$ be tensor $*$-categories and let $E: {\cal C}\rightarrow{\cal D}$ be a $*$-preserving tensor functor. There are unital $*$-homomorphisms $\widetilde{\Delta\otimes\iota}, \widetilde{\iota\otimes\Delta}: \ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E\otimes^2$ defined by $$\begin{aligned}
   \widetilde{\Delta\otimes\iota}: \ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E\otimes^2, &&  b=(b_{X,Y})\ \mapsto\      (\widetilde{\Delta\otimes\iota})(b)=((\widetilde{\Delta\otimes\iota})(b)_{U,V,W}), \quad
    (\widetilde{\Delta\otimes\iota})(b)_{U,V,W}=b_{U\otimes V,W}, \\
   \widetilde{\iota\otimes\Delta}: \ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E\otimes^2, &&
   b=(b_{X,Y})\ \mapsto\ (\widetilde{\iota\otimes\Delta})(b)=((\widetilde{\iota\otimes\Delta})(b)_{U,V,W}), \quad
    (\widetilde{\iota\otimes\Delta})(b)_{U,V,W}=b_{U,V\otimes W}.
\end{aligned}$$ These morphisms satisfy $(\widetilde{\Delta\otimes\iota})\tilde{\Delta}=(\widetilde{\iota\otimes\Delta})\tilde{\Delta}$.
:::

*Proof. *That $(\widetilde{\Delta\otimes\iota})(b)\in\mathrm{Nat}\,E\otimes^2$ for $b\in\mathrm{Nat}\,E\otimes$ follows from the following computation: $$\begin{aligned}
 \lefteqn{(E\otimes^2) (s\times t\times u) \, \,\circ\,(\widetilde{\Delta\otimes\iota})(b)_{Y,Z,W} = 
   E(s\otimes t\otimes u) \, \,\circ\,\, b_{Y\otimes Z,W}  } \\ 
  && = b_{Y'\otimes Z',W'} \, \,\circ\,E(s\otimes t\otimes u) = (\widetilde{\Delta\otimes\iota})(b)_{Y',Z',W'} \,\circ\,(E\otimes^2) (s\times t\times u), 
\end{aligned}$$ whenever $s: U\rightarrow U', t: V\rightarrow V', u: W\rightarrow W'$. The argument for $(\widetilde{\iota\otimes\Delta})(b)$ is completely analogous. Clearly, both maps $(\widetilde{\Delta\otimes\iota}), (\widetilde{\iota\otimes\Delta})$ are unital $*$-homomorphisms. The coassociativity property follows from $$(\widetilde{\Delta\otimes\iota})\tilde{\Delta}(b)_{U,V,W}=\tilde{\Delta}(b)_{U\otimes V,W}=b_{(U\otimes V)\otimes W}
   =b_{U\otimes (V\otimes W)}=\tilde{\Delta}(b)_{U,V\otimes W}=(\widetilde{\Delta\otimes\iota})\tilde{\Delta}(b)_{U,V,W}$$ with $b\in\mathrm{End}\,E$, where we have used the strictness of ${\cal C}$.

::: prop
[]{#p-ve label="p-ve"} There are unital $*$-homomorphisms $\tilde{\varepsilon}: \ \mathrm{Nat}\,E\rightarrow\mathrm{End}(E({\bf 1}))$ and $\widetilde{\varepsilon\otimes\iota}, \widetilde{\iota\otimes\varepsilon}:\ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E$ defined by $$\begin{array}{lll}
  \displaystyle\tilde{\varepsilon}: & \mathrm{Nat}\,E\rightarrow\mathrm{End}(E({\bf 1})), & b=(b_X)\ \mapsto\ b_{\bf 1}, \vspace{4pt}\\
  \displaystyle\widetilde{\varepsilon\otimes\iota}: & \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E, & b=(b_{X,Y})\ \mapsto\ (\widetilde{\varepsilon\otimes\iota})(b)=
   ((\widetilde{\varepsilon\otimes\iota})(b)_X), \quad (\widetilde{\varepsilon\otimes\iota})(b)_X=b_{{\bf 1},X},   \vspace{4pt} \\
  \displaystyle\widetilde{\iota\otimes\varepsilon}: & \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E, & b=(b_{X,Y})\ \mapsto\ (\widetilde{\iota\otimes\varepsilon})(b)=
   ((\widetilde{\iota\otimes\varepsilon})(b)_X), \quad (\widetilde{\iota\otimes\varepsilon})(b)_X=b_{X,{\bf 1}}. 
\end{array}$$ They satisfy $(\widetilde{\varepsilon\otimes\iota})\tilde{\Delta}=(\widetilde{\iota\otimes\varepsilon})\tilde{\Delta}=\iota$.
:::

*Proof. *Clearly, the map $\tilde{\varepsilon}: b=(b_X)\ \mapsto\ b_{\bf 1}\in\mathrm{End}\,E({\bf 1})$ is a unital $*$-homomorphism. The proofs that $(\widetilde{\varepsilon\otimes\iota})(b),(\widetilde{\iota\otimes\varepsilon})(b)$ are in fact in $\mathrm{Nat}\,E$ and that the maps $b\mapsto(\widetilde{\varepsilon\otimes\iota})(b), \ b\mapsto(\widetilde{\iota\otimes\varepsilon})(b)$ are $*$-homomorphisms proceed along the same lines as for coproducts and are therefore omitted. For $b\in\mathrm{Nat}\,E$ the computation $$(\widetilde{\varepsilon\otimes\iota})\tilde{\Delta}(b)= \tilde{\Delta}(b)_{{\bf 1},X}=b_{{\bf 1}\otimes X}=b_X
  =b_{X\otimes{\bf 1}}= \tilde{\Delta}(b)_{X,{\bf 1}} = (\widetilde{\iota\otimes\varepsilon})\tilde{\Delta}(b),$$ where we used the strictness of the unit ${\bf 1}$, concludes the proof.

We have thus seen that we can define a 'coproduct' $\tilde{\Delta}: \mathrm{Nat}\,E\rightarrow\mathrm{Nat}\,E\otimes$ and a 'counit' $\tilde{\varepsilon}: \mathrm{Nat}\,E\rightarrow\mathrm{End}E({\bf 1})$ satisfying analogues of the usual properties. A priori, however, $\mathrm{Nat}\,E\otimes$ has nothing to do with $\mathrm{Nat}\,E\otimes\mathrm{Nat}\,E$, regardless of how we interpret the tensor product. The following result indicates how to proceed. We now assume that ${\cal C}$ is semisimple. As before, by $I_{\cal C}$ we denote the set of isomorphism classes of irreducible objects of ${\cal C}$. For every $i\in I_{\cal C}$ we pick a representative $X_i$.

::: defin
Given a tensor $*$-category ${\cal C}$, an embedding functor (for ${\cal C}$) is a faithful $*$-preserving tensor functor $E: {\cal C}\rightarrow{\cal H}$. A concrete tensor $*$-category is a tensor $*$-category together with an embedding functor.
:::

::: prop
[]{#p-canon-isom label="p-canon-isom"} Let ${\cal C}$ be a semisimple tensor $*$-category and $E: {\cal C}\rightarrow{\cal H}$ an embedding functor. With the $*$-algebra $A=\bigoplus_{i\in I_{\cal C}} B(E(X_i))$ we have the following canonical $*$-isomorphisms: $$\begin{array}{lclcl}
  \displaystyle\mathrm{Nat}\,E & \stackrel{\psi_1}{\longrightarrow}& M(A) & = & \prod_{i\in I_{\cal C}}
     B(E(X_i)), \vspace{5pt}\\ 
  \displaystyle\mathrm{Nat}\,E \otimes & \stackrel{\psi_2}{\longrightarrow}& M(A\otimes A) & = & \prod_{i,j\in I_{\cal C}} B(E(X_i))\otimes                   B(E(X_j)), \vspace{5pt}\\
  \displaystyle\mathrm{Nat}\,E\otimes^2 &\stackrel{\psi_3}{\longrightarrow} & M(A\otimes A\otimes A) & =& \prod_{i,j,k\in I_{\cal C}}          B(E(X_i))\otimes B(E(X_j))\otimes B(E(X_k)).
\end{array}$$
:::

*Proof. *The isomorphism $\psi_1$ was established in Propositions [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"} and [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"} and suppressed subsequently. As to $\psi_2$, we have $$\begin{array}{cclclcc} 
  \displaystyle\mathrm{Nat}\,E\otimes  & = & \prod_{i,j\in I_{\cal C}} \mathrm{End}\,E(X_i\otimes X_j) 
  & \cong & \prod_{i,j\in I_{\cal C}} \mathrm{End}\,(E(X_i)\otimes E(X_j))  \\ 
\displaystyle& = & \prod_{i,j\in I_{\cal C}} B(E(X_i)\otimes E(X_j)) &=& \prod_{i,j \in I_{\cal C}} 
      B(E(X_i))\otimes B(E(X_j))\ &=& M(A\otimes A). 
\end{array}$$ Here we used the identification $B(H\otimes K)\equiv B(H)\otimes B(K)$ for finite dimensional Hilbert spaces and the identifications made after Propositions [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"} and [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"}. The isomorphism between $\mathrm{End}\,E(X_i\otimes X_j)$ and $\mathrm{End}\,E(X_i)\otimes E(X_j)$ is induced in the canonical way from the isomorphism $d^E_{X_i,X_j}: E(X_i)\otimes E(X_j)\rightarrow E(X_i\otimes X_j)$ which makes $E$ monoidal. Unitarity of the $d^E_{X_i,X_j}$ implies that $\psi_2$ is $*$-preserving. The argument for $\psi_3$ is completely analogous.

::: rema
In the above proof it was crucial that the canonical $*$-homomorphisms $\otimes: \ \mathrm{End}\,X\otimes_{\mathbb C}\mathrm{End}\,Y \rightarrow\mathrm{End}(X\otimes Y)$ are $*$-isomorphisms for all $X,Y\in{\cal H}$. A semisimple tensor $*$-category has this property iff every object is a finite direct sum of copies of the tensor unit ${\bf 1}$. \[*Proof.* The 'if' clause is easy. As to the 'only if' part, let $Z$ be irreducible and consider $X\cong Y\cong {\bf 1}\oplus Z$, thus $X\otimes Y\cong{\bf 1}\oplus Z\oplus Z\oplus Z^2$. If $Z\not\cong{\bf 1}$ then $\mathrm{End}\,X\otimes_{\mathbb C}\mathrm{End}\,Y\cong{\mathbb C}^2\otimes{\mathbb C}^2$ is commutative whereas $\mathrm{End}(X\otimes Y)$ is non-commutative since $X\otimes Y$ contains the irreducible $Z$ with multiplicity at least two. This contradicts $\mathrm{End}\,X\otimes_{\mathbb C}\mathrm{End}\,Y \cong\mathrm{End}(X\otimes Y)$.\] This property is known to characterize the (semisimple) tensor $*$-category ${\cal H}$ uniquely up to equivalence. We thus see that with $E=Id :{\cal C}\rightarrow{\cal C}$, we cannot conclude that $\mathrm{Nat}\,E\otimes \ \cong \ M(A\otimes A)$. This is consistent with the computation of $\mathrm{Nat}\,\otimes$ in Example [\[e-otimes\]](#e-otimes){reference-type="ref" reference="e-otimes"}.
:::

From now on we restrict ourselves to the case we are ultimately interested in.

::: defin
[]{#d-ve-D label="d-ve-D"} Let ${\cal C}$ be a semisimple tensor $*$-category and let $E: {\cal C}\rightarrow{\cal H}$ be an embedding functor. Using the preceding results we define unital $*$-homomorphisms as follows. $$\begin{array}{ll}
  \displaystyle\overline{\varepsilon}: \ M(A)\rightarrow{\mathbb C}, & \quad a\mapsto \tilde{\varepsilon}\,\circ\,\psi_1^{-1}(a), \vspace{4pt}\\
  \displaystyle\overline{\Delta}: \ M(A)\rightarrow M(A\otimes A), & \quad a\mapsto \psi_2\,\circ\,\tilde{\Delta}\,\circ\,\psi_1^{-1}(a).
\end{array}$$ Here we have implicitly used the irreducibility of $E({\bf 1}_{\cal C})\cong{\bf 1}_{\cal H}\cong{\mathbb C}$, giving rise to the isomorphism $\psi_0:\mathrm{End}\,E({\bf 1})\rightarrow{\mathbb C},\ c\,\mathrm{id}_{E({\bf 1})}\mapsto c$.
:::

::: rema
1\. In the sequel we will usually use the isomorphisms $\psi_1, \psi_2$ to identify $M(A)\equiv\mathrm{Nat}\,E,\ M(A\otimes A)\equiv\mathrm{Nat}\,E\otimes$ and suppress the symbols $\psi_1, \psi_2$. Thus for $a\in M(A), i\in I,\  a_i$ will denote both the $i$-component of $a$ in $\prod_{i\in I} B(E(X_i))$ and the action $a_{X_i}$ on $E(X_i)$ of the natural transformation $\psi_1^{-1}(a)\in\mathrm{Nat}\,E$.

2\. Let $a\in M(A)$. As $\Delta(a)_{ij}=a_{X_i\otimes X_j}$ and $(a\otimes a)_{ij}=a_i\otimes a_j$ we find $$\Delta(a)=a\otimes a \quad\Leftrightarrow\quad a_{X_i\otimes X_j}=a_{X_i}\otimes a_{X_j} \quad\forall i,j\in I.$$ Thus the grouplike elements of $M(A)$ are in one-to-one correspondence with those natural transformations of the embedding functor which respect the tensor structure.
:::

::: lem
[]{#l-nondeg label="l-nondeg"} The restriction $\Delta=\overline{\Delta}\upharpoonright A$ is a non-degenerate $*$-homomorphism from $A$ to $M(A\otimes A)$, i.e. $\Delta(A)(A\otimes A)=(A\otimes A)\Delta(A)=(A\otimes A)$.
:::

*Proof. *To simplify the notation we write $H_i=B(E(X_i))$ and use the isomorphisms $\psi_1, \psi_2$ to identify $M(A)$ with $\mathrm{Nat}\,E$ and $M(A\otimes A)$ with $\mathrm{Nat}\,E\otimes$. We will only prove $\Delta(A)(A\otimes A)=(A\otimes A)$, the proof of the other identity being completely analogous. As $A=\oplus_i B(H_i)$, it suffices to show that for every $i,j\in I_{\cal C}$ there is a $c\in A$ with $\Delta(c)(I_i\otimes I_j)=I_i\otimes I_j$, since this implies $a_i\otimes b_j=\Delta(c)(I_i\otimes I_j)(a_i\otimes b_j)\in\Delta(A)(A\otimes A)$ for all $a_i\in B(H_i), b_j\in B(H_j)$. Recall from the Propositions [\[p-canon-isom\]](#p-canon-isom){reference-type="ref" reference="p-canon-isom"} and [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"} that $M(A)$ is isomorphic to the $*$-algebra of natural transformations of $E$, and these are uniquely determined by their actions on the irreducibles: $M(A)\ni b\leftrightarrow (b_i)$, where $b_i\equiv b_{X_i}$. Similarly, $M(A\otimes A)\ni b\leftrightarrow (b_{ij})$ with $b_{ij}\equiv b_{X_i,X_j}$. By the definition of $\tilde{\Delta}$ we have $\tilde{\Delta}(b)_{ij}=b_{X_i\otimes X_j}$. As usual, let $(v_{ij}^{k\alpha}, \alpha=1,\ldots,N_{ij}^k)$ be an orthonormal basis in $\mathrm{Mor}(X_k,X_i\otimes X_j)$ for all $i,j,k\in I_{\cal C}$. Since $b\in M(A)\equiv\mathrm{End}\,E$ is a natural transformation we have $$\tilde{\Delta}(b)_{ij}=b_{X_i\otimes X_j}= b_{X_i\otimes X_j}\,\circ\,\mathrm{id}_{E(X_i\otimes X_j)}=
   b_{X_i\otimes X_j}\,\circ\,E\left(\sum_{k\alpha} v_{ij}^{k\alpha}\,\circ\,v_{ij}^{k\alpha*}\right)
   = \sum_{k\alpha} E(v_{ij}^{k\alpha})\,\circ\,b_k\,\circ\,E(v_{ij}^{k\alpha*}).$$ Now fix $i_0, j_0\in I_{\cal C}$ and let $b_k=\mathrm{id}_{E(X_k)}$ if $X_k$ is contained in $X_{i_0}\otimes X_{j_0}$ and $b_k=0$ otherwise. Since $X_k\prec X_{i_0}\otimes X_{j_0}$ only for finitely many $k$ we have $b=(b_k)\in A$ and $$\tilde{\Delta}(b)_{i_0j_0}=\sum_{k\alpha} E(v_{i_0j_0}^{k\alpha})\,\circ\,\mathrm{id}_{E(X_k)}\,\circ\,
   E(v_{i_0j_0}^{k\alpha*}) =\sum_{k\alpha} E(v_{i_0j_0}^{k\alpha}\,\circ\,v_{i_0j_0}^{k\alpha*})
  = E(\mathrm{id}_{X_{i_0}\otimes X_{j_0}}) = \mathrm{id}_{E(X_{i_0}\otimes X_{j_0})}.$$ Having identified $\mathrm{Nat}\,E\otimes\equiv M(A\otimes A)$ this precisely means that the $(i_0,j_0)$-component of $\Delta(b)\in M(A\otimes A)=\prod_{ij} B(H_i)\otimes B(H_j)$ is the identity $I_{i_0}\otimes I_{j_0}$ and therefore $\Delta(b)(I_{i_0}\otimes I_{j_0})=(I_{i_0}\otimes I_{j_0})$ as desired.

::: cor
[]{#c-extens label="c-extens"} Defining $*$-homomorphisms $\varepsilon: A\rightarrow{\mathbb C}$ and $\Delta: A\rightarrow M(A\otimes A)$ by $\varepsilon=\overline{\varepsilon}\upharpoonright A$ and $\Delta=\overline{\Delta}\upharpoonright A$, $\overline{\varepsilon}$ and $\overline{\Delta}$ are the unique extensions of $\varepsilon$ and $\Delta$, respectively, to $M(A)$.
:::

*Proof. *It is clear that $\varepsilon$ is not identically zero, thus non-degenerate. Non-degeneracy of $\Delta$ has been proven in Lemma [\[l-nondeg\]](#l-nondeg){reference-type="ref" reference="l-nondeg"}. Now the claim follows from the fact [@VD2] that a non-degenerate $*$-homomorphism $\phi: A\rightarrow M(B)$ has a unique extension to a unital $*$-homomorphism $\overline{\phi}: M(A)\rightarrow M(B)$.

::: prop
[]{#p-cdisc label="p-cdisc"} Let ${\cal C}$ be a semisimple tensor $*$-category and $E:{\cal C}\rightarrow{\cal H}$ an embedding functor. Then the $*$-algebra $A=\oplus_{i\in I_{\cal C}} B(E(X_i))$ is a discrete quantum semigroup, i.e. has a non-degenerate coproduct $\Delta: A\rightarrow M(A\otimes A)$ in the sense of [@VD2] and a counit $\varepsilon: A\rightarrow{\mathbb C}$.
:::

*Proof. *By Lemma [\[l-nondeg\]](#l-nondeg){reference-type="ref" reference="l-nondeg"}, $\Delta$ is non-degenerate, thus also $\Delta\otimes\iota: A\otimes A\rightarrow M(A\otimes A)\otimes A\subset M(A\otimes A\otimes A)$ is non-degenerate and extends uniquely to $\overline{\Delta\otimes\iota}: M(A\otimes A)\rightarrow M(A\otimes A\otimes A)$. Another unital $*$-homomorphism $M(A\otimes A)\rightarrow M(A\otimes A\otimes A)$ is given by $\psi_3\,\circ\,(\widetilde{\Delta\otimes\iota})\,\circ\,\psi_2^{-1}$. The latter clearly restricts to $\Delta\otimes\iota$ on $A\otimes A$, thus it coincides with $\overline{\Delta\otimes\iota}$ on all of $M(A\otimes A)$. In the same way we make sense of $\overline{\iota\otimes\Delta}: M(A\otimes A)\rightarrow M(A\otimes A\otimes A)$ and see that it coincides with $\psi_3\,\circ\,(\widetilde{\iota\otimes\Delta})\,\circ\,\psi_2^{-1}$. Now, the coassociativity property proved in Proposition [\[p-coassoc\]](#p-coassoc){reference-type="ref" reference="p-coassoc"} implies $$\overline{\Delta\otimes\iota}\,\circ\,\overline{\Delta}= \overline{\iota\otimes\Delta}\,\circ\,\overline{\Delta}:\
    M(A)\rightarrow M(A\otimes A\otimes A),$$ which is the proper formulation of coassociativity for $(A,\Delta)$.

As observed earlier, the $*$-homomorphism $\varepsilon: A\rightarrow{\mathbb C}$ is non-degenerate, thus $\varepsilon\otimes\iota,\, \iota\otimes\varepsilon:\ A\otimes A\rightarrow A$ are non-degenerate too and have unique extensions $\overline{\varepsilon\otimes\iota},\, \overline{\iota\otimes\varepsilon}$ to $M(A\otimes A)$. Again, it is clear that $\overline{\varepsilon\otimes\iota}=\psi_1\,\circ\,(\widetilde{\varepsilon\otimes\iota})\,\circ\,\psi_2^{-1}$ and similarly for $\overline{\iota\otimes\varepsilon}$. Thus with Proposition [\[p-ve\]](#p-ve){reference-type="ref" reference="p-ve"} we conclude $$\overline{\varepsilon\otimes\iota}\,\circ\,\overline{\Delta}=\overline{\iota\otimes\varepsilon}\,\circ\,
   \overline{\Delta}=\mathrm{id}: \ M(A)\rightarrow M(A).$$ We conclude that $(A,\Delta)$ is a discrete quantum semigroup.

::: thm
[]{#t-mon-equiv label="t-mon-equiv"} Let ${\cal C}$ be a semisimple tensor $*$-category and $E:{\cal C}\rightarrow{\cal H}$ an embedding functor. Let $(A,\Delta)$ be the corresponding discrete quantum semigroup. Then the functor $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ defined by $$F(X)=(E(X),\pi_X), \quad \pi_X(a)=a_X \ \forall a\in A, \quad\quad F(s)=E(s)$$ provides an equivalence of tensor $*$-categories such that $K\,\circ\,F= E$.
:::

*Proof. *With $A$ and $F: {\cal C}\rightarrow\mathrm{Rep}_f A$ as defined in Theorem [\[t-equiv\]](#t-equiv){reference-type="ref" reference="t-equiv"} we have an equivalence of categories. It remains to show that $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ is monoidal for the monoidal structure of $\mathrm{Rep}_f(A,\Delta)$ in Definition [\[d-repf\]](#d-repf){reference-type="ref" reference="d-repf"}. Thus we must exhibit isomorphisms $d^F_{X,Y}: F(X)\otimes F(Y)\rightarrow F(X\otimes Y)$ satisfying the conditions of Definition [\[d-mon-func\]](#d-mon-func){reference-type="ref" reference="d-mon-func"}. In view of $F(X)=(E(X),\pi_X)$, an obvious candidate is the isomorphism $d^E_{X,Y}: E(X)\otimes E(Y)\rightarrow E(X\otimes Y)$ which we have by virtue of the assumed monoidality of $E$. If we set $d^F_{X,Y}=d^E_{X,Y}$ for all $X,Y\in {\cal C}$, the equations in Definition [\[d-mon-func\]](#d-mon-func){reference-type="ref" reference="d-mon-func"} are clearly satisfied. It only remains to prove that $d^F_{X,Y}$ is in $\mathrm{Mor}_{\mathrm{Rep}_f(A,\Delta)}(F(X)\otimes F(Y), F(X\otimes Y))$, i.e. $$d^F_{X,Y} \,\circ\,(\pi_X\times\pi_Y)(a)=\pi_{X\otimes Y}(a)\,\circ\,d^F_{X,Y} \quad\forall
   a\in A.$$

Keeping in mind the various identifications we have made so far, we get $$d^F_{X,Y} \,\circ\,(\pi_X\times\pi_Y)(a)=d^F_{X,Y} \,\circ\,\overline{(\pi_X\otimes\pi_Y)}\Delta(a)
=d^F_{X,Y} \,\circ\,\overline{(\pi_X\otimes\pi_Y)}\overline{\Delta}(a)$$ $$=d^F_{X,Y} \,\circ\,\overline{(\pi_X\otimes\pi_Y)}\psi_2\tilde{\Delta}(a)
=\pi_{X,Y}\tilde{\Delta}(a)\,\circ\,d^F_{X,Y}
=a_{X\otimes Y}\,\circ\,d^F_{X,Y} =\pi_{X\otimes Y}(a)\,\circ\,d^F_{X,Y}$$ for all $a\in A$. (The reader is invited to check the required identity explicitly for $X=X_i, Y=X_j$, as suffices by naturality of the isomorphisms $d^F$.)
