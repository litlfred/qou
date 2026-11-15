---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-004-32-classification-theorems
section_title: "Classification Theorems"
section_number: 3.2
pages: 10-14
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.963
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
The most immediately useful fact about KV 2-vector spaces is the following well known characterization:

::: theorem
[]{#thm:kvvn label="thm:kvvn"} Every KV 2-vector space is equivalent as a category to $\boldsymbol{\operatorname{{Vect}}}^k$ for some $k \in \mathbb{N}$.
:::

::: proof
*Proof.* Suppose $\boldsymbol{\operatorname{{K}}}$ is a KV 2-vector space with a basis of simple objects $X_1 \dots X_k$. Then we construct an equivalence $E:
\boldsymbol{\operatorname{{K}}} \mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}^k$ as follows:

$E$ should be an additive functor with $E(X_i) = V_i$, where $V_i$ is the $k$-tuple of vector spaces having the zero vector space in every position except the $i^{th}$, which has a copy of $\mathbb{C}$. But any object $X$, is a sum $\bigoplus_{i} X_i^{n_i}$, so by linearity (i.e. the fact that $E$ preserves biproducts) $X$ will be sent to the sum of the same number of copies of the $V_i$, which is just a $k$-tuple of vector spaces whose $i^{th}$ component is $\mathbb{C}^{n_i}$. So every object in $K$ is sent to an $k$-tuple of vector spaces. By $\mathbb{C}$-linearity, and the fact that hom-vector spaces of simple objects are one-dimensional, this determines the images of all morphisms.

But then the weak inverse of $E$ is easy to construct, since sending $V_i$ to $X_i$ gives an inverse at the level of objects, by the same linearity argument as above. At the level of morphisms, the same argument holds again. ◻
:::

This is a higher analog of the fact that every finite dimensional complex vector space is isomorphic to $\mathbb{C}^k$ for some $k \in
\mathbb{N}$. So, indeed, the characterization of 2-vector spaces in our example above is generic: every KV 2-vector space is equivalent to one of the form given. Moreover, our picture of 2-linear maps is also generic, as shown by this argument, analogous to the linear algebra argument for representation of linear maps by matrices:

::: lemma
[]{#lemma:kv2linmatrix label="lemma:kv2linmatrix"} Any 2-linear map $T: \boldsymbol{\operatorname{{Vect}}}^n \mathop{\rightarrow}
\boldsymbol{\operatorname{{Vect}}}^m$ is naturally isomorphic to a map of the form ([\[eq:kv2linmatrix\]](#eq:kv2linmatrix){reference-type="ref" reference="eq:kv2linmatrix"}).
:::

::: proof
*Proof.* Any 2-linear map $T$ is a $\mathbb{C}$-linear additive functor between 2-vector spaces. Since any object in a 2-vector space can be represented as a biproduct of simple objects---and morphisms likewise---such a functor is completely determined by its effect on the basis of simple objects and morphisms between them.

But then note that since the automorphism group of a simple object is by definition just all (complex) multiples of the identity morphism, there is no choice about where to send any such morphism. So a functor is completely determined by the images of the basis objects, namely the 2-vectors $V_i = (0,\dots,\mathbb{C},\dots,0) \in \boldsymbol{\operatorname{{Vect}}}^n$, where $V_i$ has only the $i^{th}$ entry non-zero.

On the other hand, for any $i$, $T(V_i)$ is a direct sum of some simple objects in $\boldsymbol{\operatorname{{Vect}}}^m$, which is just some 2-vector, namely a $k$-tuple of vector spaces. Then the fact that the functor is additive means that it has exactly the form given. ◻
:::

And finally, the analogous fact holds for natural transformations between 2-linear maps:

::: lemma
[]{#lemma:kvnattransmatrix label="lemma:kvnattransmatrix"}Any natural transformation $\alpha : T \mathop{\rightarrow}T'$ from a 2-linear map $T : \boldsymbol{\operatorname{{Vect}}}^n \mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}^m$ to a 2-linear map $T' : \boldsymbol{\operatorname{{Vect}}}^n \mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}^m$, both in the form ([\[eq:kv2linmatrix\]](#eq:kv2linmatrix){reference-type="ref" reference="eq:kv2linmatrix"}) is of the form ([\[eq:kvnattransmatrix\]](#eq:kvnattransmatrix){reference-type="ref" reference="eq:kvnattransmatrix"}).
:::

::: proof
*Proof.* By Lemma [\[lemma:kv2linmatrix\]](#lemma:kv2linmatrix){reference-type="ref" reference="lemma:kv2linmatrix"}, the 2-linear maps $T$ and $T'$ can be represented as matrices of vector spaces, which act on an object in $\boldsymbol{\operatorname{{Vect}}}^n$ as in ([\[eq:kv2linmatrix\]](#eq:kv2linmatrix){reference-type="ref" reference="eq:kv2linmatrix"}). A natural transformation $\alpha$ between these should assign, to every object $X \in \boldsymbol{\operatorname{{Vect}}}^n$, a morphism $\alpha_X : T(X) \mathop{\rightarrow}T'(X)$ in $\boldsymbol{\operatorname{{Vect}}}^m$, such that the usual naturality square commutes for every morphism $f : X \mathop{\rightarrow}Y$ in $\boldsymbol{\operatorname{{Vect}}}^n$.

Suppose $X$ is the $n$-tuple $(X_1, \dots , X_n)$, where the $X_i$ are finite dimensional vector spaces. Then $$\label{eq:TX}
T(X) = (\oplus_{k=1}^{n} V_{1,k} \otimes X_k, \dots,\oplus_{k=1}^{n} V_{m,k} \otimes X_k )$$ where the $V_{i,j}$ are the components of $T$, and similarly $$T'(X) = (\oplus_{k=1}^{n} V'_{1,k} \otimes X_k, \dots,\oplus_{k=1}^{n} V'_{m,k} \otimes X_k )$$ where the $V'_{i,j}$ are the components of $T'$.

Then a morphism $\alpha_X : T(X) \mathop{\rightarrow}T'(X)$ consists of an $m$-tuple of linear maps: $$\alpha_j : \oplus_{k=1}^{n} V_{j,k} \otimes X_k \mathop{\rightarrow}\oplus_{k=1}^{n} V'_{j,k} \otimes X_k$$ but by the universal property of the biproduct, this is the same as having an $(n \times m)$-indexed set of maps $$\alpha_{jk} : V_{j,k} \otimes X_k \mathop{\rightarrow}\oplus_{r=1}^{n} V'_{j,r} \otimes X_r$$ and by the dual universal property, this is the same as having $(n
\times n \times m)$-indexed maps $$\alpha_{jkr} : V_{j,k} \otimes X_k \mathop{\rightarrow}V'_{j,r} \otimes X_r$$ However, we must have the naturality condition for every morphism $f:X \mathop{\rightarrow}X'$: $$\xymatrix{
  T(X) \ar[d]_{\alpha_{X}} \ar[r]^{T(f)} & T(X') \ar[d]^{\alpha_{X'}} \\
  T'(X) \ar[r]_{T'(f)} & T'(X')\\ 
}$$ Note that each of the arrows in this diagram is a morphism in $\boldsymbol{\operatorname{{Vect}}}^m$, which are linear maps in each component---so in fact we have a separate naturality square for each component.

Also, since $T$ and $T'$ act on $X$ and $X'$ by tensoring with fixed vector spaces as in ([\[eq:TX\]](#eq:TX){reference-type="ref" reference="eq:TX"}), one has $T(f)_i =
\oplus_j 1_{V_{ij}} \otimes f_j$, having no effect on the $V_{ij}$. We want to show that the components of $\alpha$ affect *only* the $V_{ij}$.

Additivity of all the functors involved implies that the assignment $\alpha$ of maps to objects in $\boldsymbol{\operatorname{{Vect}}}^n$ is additive. So consider the case when $X$ is one of the standard basis 2-vectors, having $\mathbb{C}$ in one position (say, the $k^{th}$), and the zero vector space in every other position. Then, restricting to the naturality square in the $k^{th}$ position, the above condition amounts to having $m$ maps (indexed by $j$): $$\alpha_{j,k} : V_{j,k} \mathop{\rightarrow}V'_{j,k}$$ So by linearity, a natural transformation is determined by an $n\times
m$ matrix of maps as in ([\[eq:kvnattransmatrix\]](#eq:kvnattransmatrix){reference-type="ref" reference="eq:kvnattransmatrix"}). ◻
:::

The fact that 2-linear maps between 2-vector spaces are functors between categories recalls the analogy between linear algebra and category theory in the concept of an *adjoint*. If $V$ and $W$ are inner product spaces, the adjoint of a linear map $F : V \mathop{\rightarrow}W$ is a map $F^{\dagger}$ for which $\left\langle{Fx,y}\right\rangle =
\left\langle{x,F^{\dagger}y}\right\rangle$ for all $x \in V_1$ and $y \in V_2$. A (right) adjoint of a functor $F : \boldsymbol{\operatorname{{C}}} \mathop{\rightarrow}\boldsymbol{\operatorname{{D}}}$ is a functor $G : \boldsymbol{\operatorname{{D}}} \mathop{\rightarrow}\boldsymbol{\operatorname{{C}}}$ for which $\hom_D(Fx,y)
\cong \hom_C(x,Gy)$ (and then $F$ is a left adjoint of $G$).

In the situation of a KV 2-vector space, the categorified analog of the adjoint of a linear map is indeed an adjoint functor. (Note that since a KV 2-vector space has a specified basis of simple objects, it makes sense to compare it to an inner product space.) Moreover, the adjoint of a functor has a matrix representation which is much like the matrix representation of the adjoint of a linear map. We summarize this in the following (a variant of proposition 25 in [@hdaII], shown there for 2-Hilbert spaces):

::: theorem
[]{#thm:biadjoint label="thm:biadjoint"} Given any 2-linear map $F : V \mathop{\rightarrow}
W$, there is a 2-linear map $F^{\dagger} : W \mathop{\rightarrow}V$ which is both a left and right adjoint to $F$.
:::

::: proof
*Proof.* By Theorem [\[thm:kvvn\]](#thm:kvvn){reference-type="ref" reference="thm:kvvn"}, we have $V \simeq \boldsymbol{\operatorname{{Vect}}}^n$ and $W \simeq \boldsymbol{\operatorname{{Vect}}}^m$ for some $n$ and $m$. By composition with these equivalences, we can restrict to this case. But then we have by Lemma [\[lemma:kv2linmatrix\]](#lemma:kv2linmatrix){reference-type="ref" reference="lemma:kv2linmatrix"} that $F$ is naturally isomorphic to some 2-linear map given by matrix multiplication by some matrix of vector spaces $[F_{i,j}]$: $$\begin{pmatrix}
F_{1,1} & \dots & F_{1,n} \\
\vdots & & \vdots \\
F_{m,1} & \dots & F_{m,n} \\
\end{pmatrix}$$

We claim that a (two-sided) adjoint functor $F^{\dagger}$ is given by the "dual transpose matrix" of vector spaces $[F_{i,j}]^{\dagger}$: $$\begin{pmatrix}
F^{\dagger}_{1,1} & \dots & F^{\dagger}_{1,m}\\
\vdots & & \vdots \\
F^{\dagger}_{n,1} & \dots & F^{\dagger}_{n,m} \\
\end{pmatrix}$$ where $F^{\dagger}_{i,j}$ is the vector space dual $(F_{j,i})^{\ast}$ (note the transposition of the matrix).

We note that this prescription is symmetric, since $[T]^{\dagger
\dagger} = [T]$, so if $F^{\dagger}$ is always a left adjoint of $F$, then $F$ is also a left-adjoint of $F^{\dagger}$, hence $F^{\dagger}$ a right adjoint of $F$. So if this prescription gives a left adjoint, it gives a two-sided adjoint. Next we check that it does.

Suppose $x=(X_i) \in \boldsymbol{\operatorname{{Vect}}}^n$ is the 2-vector with vector space $X_i$ in the $i^{th}$ component, and $y=(Y_j) \in \boldsymbol{\operatorname{{Vect}}}^m$ has vector space $Y_j$ in the $j^{th}$ component. Then $F(x) \in \boldsymbol{\operatorname{{Vect}}}^m$ has $j^{th}$ component $\oplus_{i=1}^n F_{i,j} \otimes X_i$. Now, a map in $\boldsymbol{\operatorname{{Vect}}}^m$ from $F(x)$ to $y$ consists of a linear map in each component, so it is an $m$-tuple of maps: $$f_j: \bigoplus_{i=1}^n F_{i,j} \otimes X_i \mathop{\rightarrow}Y_j$$ for $j = 1 \dots m$. But since the direct sum (biproduct) is a categorical coproduct, this is the same as an $m \times n$ matrix of maps: $$f_{ij}: V_{i,j} \otimes X_i \mathop{\rightarrow}Y_j$$ for $k = 1 \dots n$ and $j = 1 \dots m$, and $\hom(F(x),y)$ is the vector space of all such maps.

By the same argument, a map in $\boldsymbol{\operatorname{{Vect}}}^n$ from $x$ to $F^{\dagger}(y)$ consists of an $n \times m$ matrix of maps: $$g_{ji}: X_i \mathop{\rightarrow}V_{j,i}^{\ast} \otimes Y_j \cong \hom(V_{j,i},Y_j)$$ for $i = 1 \dots n$ and $j = 1 \dots m$, and $\hom(x,F^{\dagger}(y))$ is the vector space of all such maps.

But then we have a natural isomorphism $\hom(F(x),y) \cong \hom(x,F^{\dagger}(y))$ by the duality of $\hom$ and $\otimes$, so in fact $F^{\dagger}$ is a right adjoint for $F$, and by the above argument, also a left adjoint.

Moreover, no other non-isomorphic matrix defines a 2-linear map with these properties, and since any functor is naturally isomorphic to some matrix, this is the sole $F^{\dagger}$ which works. ◻
:::
