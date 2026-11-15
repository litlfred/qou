---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-012-51-inner-product-of-stuff-types
section_title: "Inner Product of Stuff Types"
section_number: 5.1
pages: 30-34
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.957
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
[]{#stuffinnerprod label="stuffinnerprod"}

The first feature of a Hilbert space we need to recover is its inner product.

### Inner Product as Pullback

When we were discussing the Hilbert space of states of the quantum harmonic oscillator, we described the inner product on this Hilbert space, which gave us, on the basis of pure states $z^k$, the form $\left\langle{ z^n, z^m }\right\rangle = \delta_{n, m} n!$. We would like to give this a combinatorial, or categorified, interpretation in terms of our categorified states - stuff types. The inner product for stuff types (now thought of as categorified states) will turn out to satisfy the property that $| \left\langle{ \Phi, \Psi }\right\rangle | = \left\langle{ | \Phi |, | \Psi |
}\right\rangle$ just as we saw for composition of types.

Previously we described the categorification of formal power series in two steps - first replacing the complex numbers by some groupoid $\boldsymbol{\operatorname{{X}}}$, then replacing the natural numbers by $\boldsymbol{\operatorname{{FinSet_0}}}$. We follow the same two-step process to describe the categorified inner product.

Now, in a quantum mechanical setting, the space of states of a system is a space of $L^2$ functions over some configuration space. In the case of the harmonic oscillator, the configuration space is just a set of energy levels, equivalent to $\mathbbm{N}$, and so the space of states can be seen as $\ell^2$, the space of square-summable sequences (of complex numbers).

In the categorified space of states, a natural way to get an inner product is to extend the definition $\left\langle{ \psi, \phi }\right\rangle = \sum_{n
\in \mathbbm{N}} \psi_n \phi_n$ in the case of complex numbers to become $$\left\langle{ \psi,\phi }\right\rangle = \sum_{n \in \mathbbm{N}} \psi_n \times \phi_n$$ where the sum is now a coproduct in $\boldsymbol{\operatorname{{Set}}}$ (i.e. a disjoint union) and the multiplication is the categorical (Cartesian) product. This way of looking at the inner product gives a set, and the equivalent condition to square-summability is the finiteness of this set. The cardinality operator gives us a notion of square-summability in the decategorified setting: we can dispense with this condition in the categorified setting, just as we can treat structure types with infinite sets as coefficients. In the case where the set we get is finite, it should be clear that when we take cardinalities, we just get that the cardinality $|\left\langle{\psi,\phi}\right\rangle|$ is just $\left\langle{|\psi|,|\phi|}\right\rangle$. So this is naturally seen as an inner product in the sense that when we take cardinalities, we get a number which will be the inner product of the vectors in the space of power series which are the cardinalities of the two types. In the finite case these are just polynomials: this is as yet not very interesting since we are dealing with sets, whose cardinalities are just integers. We will address this when we pass to the case of a groupoid over $\boldsymbol{\operatorname{{FinSet_0}}}$.

To see how this will work, note that, just as structure types and stuff types themselves, we can treat the inner product as a "bundle over $\mathbbm{N}$", with projection maps taking the individual elements of this disjoint union of products down to $\mathbbm{N}$ by the obvious projection taking an element of $\psi_n \times \phi_n$ to $n$ (which is well defined, since all elements of the inner product are of this form). So if we think of the two states $\psi,
\phi$ as corresponding to two bundles $F : S \rightarrow \mathbbm{N}$ and $G :
S' \rightarrow \mathbbm{N}$ for $S, S' \in \operatorname{Set}$ we have, as we've seen: $$\left\langle{ F, G }\right\rangle = \sum_{n \in \mathbbm{N}} \psi_n \times
  \phi_n = \sum_{n \in \mathbbm{N}} F^{- 1} ( n ) \times G^{- 1} ( n )$$ This can be understood in categorical terms as the fibered product of the two bundles, also written as $X \times_{\mathbbm{N}} Y$ where the projection maps $F, G$ of the bundles are understood. Another way to say this is to describe it as a *pullback* of the two projections $X \mathop{\rightarrow}\limits^F \mathbbm{N} \mathop{\leftarrow}\limits^G Y$, which is to say an object which is initial among objects of the form $X
\mathop{\leftarrow}\limits^{P_x} O \mathop{\rightarrow}\limits^{P_y} Y$ making the square $$\xymatrix{
  O \ar[r]^-{P_x}\ar[d]_-{P_y} & X\ar[d]^-{F} \\
  \boldsymbol{\operatorname{{Y}}} \ar[r]_-{G} & {\mathbbm{N}}
 }$$ commute. (That is, given any other such object $O'$ with maps into $\boldsymbol{\operatorname{{X}}}$ and $\boldsymbol{\operatorname{{Y}}}$, there is a unique map from $O$ to $O'$ making the combined diagram commute.)

### The Categorified Case: Inner Product As Weak Pullback

The next level of categorification of this description will give us a definition of the inner product of two stuff types as a groupoid - namely the pullback of the two functors from groupoids $\boldsymbol{\operatorname{{X}}}$ and $\boldsymbol{\operatorname{{Y}}}$ into $\boldsymbol{\operatorname{{FinSet_0}}}$. The inner product on this space is the same one we described when talking about the harmonic oscillator (equation [\[innerproductuncat\]](#innerproductuncat){reference-type="ref" reference="innerproductuncat"}). To get this more fully categorified inner product - now an inner product of stuff types - we should replace $\mathbbm{N}$, the "base space" by $\boldsymbol{\operatorname{{FinSet_0}}}$, which is the free symmetric monoidal category on one generator, just as $\mathbbm{N}$ is the free commutative monoid on one generator.

So suppose we have two stuff types, namely functors $\Psi : X
\rightarrow \text{$\boldsymbol{\operatorname{{FinSet_0}}}$}$ and $\Phi : \boldsymbol{\operatorname{{Y}}} \rightarrow \text{$\boldsymbol{\operatorname{{FinSet_0}}}$}$, for some groupoids $X, \boldsymbol{\operatorname{{Y}}} \in \boldsymbol{\operatorname{{Gpd}}}$. We want to do the equivalent of taking the pullback of these two functors: $$\boldsymbol{\operatorname{{X}}} \mathop{\rightarrow}\limits^{\Psi} \boldsymbol{\operatorname{{FinSet_0}}}\mathop{\leftarrow}\limits^{\Phi} \boldsymbol{\operatorname{{Y}}}$$ Since these are not just functions between sets, but functors between categories, the pullback is in the 2-category $\boldsymbol{\operatorname{{Cat}}}$, or indeed in $\boldsymbol{\operatorname{{Gpd}}}$. So defining a pullback becomes slightly more complicated - in fact, we can and should weaken the requirement that the pullback square

$$\xymatrix{
   & \left\langle{ \Psi, \Phi }\right\rangle \ar[rd]^-{P_X}\ar[ld]_-{P_Y} & \\
  \boldsymbol{\operatorname{{Y}}} \ar[rd]_-{\Phi} & & X\ar[dl]^-{\Psi} \\
   & \boldsymbol{\operatorname{{FinSet_0}}}& \\
 }$$ commutes exactly, and allow it to commute only up to a 2-isomorphism between the two composite projections, so that what we want is the *weak pullback* (an example of a "pseudo-limit" in a 2-category; see [@street]) :

$$\label{eq:weakpullback}
  \xymatrix{ 
     & \left\langle{ \Psi, \Phi }\right\rangle \ar[rd]^-{P_X}\ar[ld]_-{P_Y} & \\ 
    \boldsymbol{\operatorname{{Y}}} \ar[rd]_-{\Phi} & & X\ar[dl]^-{\Psi}\ar@{=>}[ll]^{\alpha}_{\sim} \\
     & \boldsymbol{\operatorname{{FinSet_0}}}& \\ 
  }$$

This is like the fibrewise product over $\mathbbm{N}$ which we described above, and we can also denote this by $\boldsymbol{\operatorname{{X}}}
\times_{\boldsymbol{\operatorname{{FinSet_0}}}} \boldsymbol{\operatorname{{Y}}}$, emphasizing the groupoids rather than the functors. Let's understand this weak pullback better by seeing what this groupoid actually looks like internally, and then seeing that the groupoid cardinality of this inner product of stuff types corresponds to the inner product of two states $| \Psi |$ and $| \Phi|$.

::: definition
The groupoid $\left\langle{ \Psi, \Phi }\right\rangle = \boldsymbol{\operatorname{{X}}}
\times_{\boldsymbol{\operatorname{{FinSet_0}}}} \boldsymbol{\operatorname{{Y}}}$ has objects which are pairs $(x,y) \in
\boldsymbol{\operatorname{{X}}} \times \boldsymbol{\operatorname{{Y}}}$ equipped with an isomorphism $\alpha_{(x,y)} : \Psi(x)\tilde{\rightarrow}\Phi(y)$. A morphism in $\left\langle{\Psi,\Phi}\right\rangle$ is a morphism in $\boldsymbol{\operatorname{{X}}} \times
\boldsymbol{\operatorname{{Y}}}$, say $(f,g) : (x,y) \rightarrow (x',y')$, such that

$$\label{inprodnaturality}
\xymatrix{   
\Psi(x) \ar^-{\Psi(f)}[r] \ar_-{\alpha_{x,y}}[d] & \Psi(x') \ar^-{\alpha_{x',y'}}[d] \\   
\Phi(y) \ar_-{\Phi(g)}[r] & \Phi(y') }$$ commutes. That is, $\alpha_{x',y'} \circ \Psi(f) = \Phi(g) \circ \alpha_{x,y}$.
:::

The isomorphism $\alpha$ is from the definition of weak pullback; in a strict pullback, $\alpha_{( x, y )}$ would always be the identity - that is, we would require that $\Psi(x)=\Phi(y)$.

Now, what does this all mean? The isomorphism $\alpha$ is a bijection of underlying sets - so an object of $\left\langle{ \Psi, \Phi }\right\rangle$ is a pair of objects $(x,y)$, ($\Psi$- and $\Phi$-stuff respectively on their underlying sets), together with a bijection between the underlying sets, as shown generall in ([\[eq:pullbackobject\]](#eq:pullbackobject){reference-type="ref" reference="eq:pullbackobject"}) and illustrated in figure [1](#fig:pullbackobject){reference-type="ref" reference="fig:pullbackobject"}.

$$\label{eq:pullbackobject}
 \xymatrix{
  *+[F-,]{\bullet \dots \bullet}\ar_-{\alpha_{x,y}}^{\wr}[d] & *++[o][F-]{x}\ar^-{\Psi}[l] \\
  *+[F-,]{\bullet \dots \bullet} & *++[o][F-]{y}\ar^-{\Phi}[l] \\
 }$$

<figure id="fig:pullbackobject">
<div class="center">
<embed src="pullbackobject.eps" />
</div>
<figcaption><span id="fig:pullbackobject" label="fig:pullbackobject"></span>Object of an Inner Product (Pullback) Groupoid</figcaption>
</figure>

A morphism between two such objects includes morphisms of the form ([\[eq:typemorphism\]](#eq:typemorphism){reference-type="ref" reference="eq:typemorphism"}) between the objects of $\Psi$ and $\Phi$; this gives bijections between the underlying sets which must be compatible with those which are part of the $\left\langle{\Psi,\Phi}\right\rangle$ objects (of the form ([\[eq:pullbackobject\]](#eq:pullbackobject){reference-type="ref" reference="eq:pullbackobject"})) themselves. The general result is illustrated in ([\[eq:pullbackmorphism\]](#eq:pullbackmorphism){reference-type="ref" reference="eq:pullbackmorphism"}) and an example appears in figure [2](#fig:pullbackmorphism){reference-type="ref" reference="fig:pullbackmorphism"}.

$$\label{eq:pullbackmorphism}
 \xymatrix{
   & *++[o][F-]{x}\ar_-{\Psi}[ld]\ar^-{f}_{\sim}[rr] & & *++[o][F-]{x'}\ar^-{\Psi}[ld]  \\
  *+[F-,]{\bullet \dots \bullet}\ar_-{\alpha_{x,y}}^{\wr}[dd]\ar^-{\Psi(f)}_{\sim}[rr] & & *+[F-,]{\bullet \dots \bullet}\ar^(.3){\alpha_{x',y'}}_(.3){\wr}[dd] & \\
   & *++[o][F-]{y}\ar_-{\Phi}[ld]\ar^(.3){g}_(.3){\sim}[rr] & & *++[o][F-]{y'}\ar^-{\Phi}[ld]  \\
  *+[F-,]{\bullet \dots \bullet}\ar^-{\Phi(g)}_{\sim}[rr] & & *+[F-,]{\bullet \dots \bullet} & \\
 }$$

<figure id="fig:pullbackmorphism">
<div class="center">
<embed src="pullbackmorphism.eps" />
</div>
<figcaption><span id="fig:pullbackmorphism" label="fig:pullbackmorphism"></span>A Morphism in an Inner Product (Pullback) Groupoid</figcaption>
</figure>

So the naturality square ([\[inprodnaturality\]](#inprodnaturality){reference-type="ref" reference="inprodnaturality"}) means that the inner square of set bijections in ([\[eq:pullbackmorphism\]](#eq:pullbackmorphism){reference-type="ref" reference="eq:pullbackmorphism"}) commutes: in other words, that we have given a way to identify all these underlying sets. We can see this in the figure as the fact that following strands of the set bijections (of 3-element sets) around the square reveals that there are exactly three complete squares of strands.

### Stuff Type and Fock Space Inner Products Related

The key example of the inner product which makes clear the connection with the inner product on Fock space developed in section [\[fockinnerprod\]](#fockinnerprod){reference-type="ref" reference="fockinnerprod"} is the inner product of stuff types $Z^n$ and $Z^m$, which also happen to be structure types. The stuff type (in fact, structure type) $Z^n$ is the type of *total orders on an $n$-element set*, or "being a totally ordered $n$-element set". An object of the inner product groupoid $\left\langle{ Z^n, Z^m }\right\rangle$ is thus a pair $( x, y )$ which are $n$- and $m$-element totally-ordered sets respectively, equipped with an isomorphism between the underlying sets. We may think of these as the sets $n = \{ 0, \ldots, n - 1 \}$ and $m = \{ 0, \ldots, m - 1\}$, and the isomorphism is just any bijection $\alpha$ between these. If $n \neq m$, there are no such objects since there are no such bijections. If $n = m$, then there are $n!$ such bijections, given by the permutations of $\{ 1,
\ldots, n \}$. The morphisms of $\left\langle{ Z^n, Z^m }\right\rangle$ are just the identity morphisms on these objects, since the only morphisms in the groupoid of totally ordered sets are order-preserving bijections - that is, objects have no nontrivial automorphisms. Thus, we get: $$\left\langle{ Z^n, Z^m }\right\rangle = n! \delta_{n, m}$$ where $n!$ is the groupoid with $n!$ objects (one per permutation of $n$) and only identity morphisms, and $\delta_{n, m}$ is analogous to the usual Kronecker delta, being a groupoid with no objects if $n \neq m$ and with one object and one morphism if $n = m$. Thus, $$| \left\langle{ Z^n, Z^m }\right\rangle | = \left\langle{ |Z^n |, |Z^m | }\right\rangle$$ so that the inner product we found on Fock space is natural in this setting. This also illustrates the reason for the factor $n!$ which shows up in the $n^{\operatorname{th}}$ term in the expansion of a structure type, or the power series which is its generating function. This $n!$ is the cardinality of the group $S_n$, the group of permutations of the underlying $n$-element set.
