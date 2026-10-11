---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-007-5-stuff-types-and-quantum-mechanics
section_title: "Stuff Types And Quantum Mechanics"
section_number: 5
pages: 30-56
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
text_source: latex
latex_prose_ratio: 0.744
latex_coverage_ratio: 0.984
---
[]{#stuff-quantum-sec label="stuff-quantum-sec"}

Now we will return to our original motivation - seeing stuff types as a categorification of states of the quantum harmonic oscillator. We have already seen how stuff types can take the role of formal power series, at least up to the level of linear structure. The space of formal power series should be the Hilbert space of states of the quantum oscillator: so composition of stuff types, which we have explored, will not enter into this picture, though the linear structure will. If stuff types are categorified power series, and the 2-category $\boldsymbol{\operatorname{{StuffTypes}}}$ is a categorified Fock space some of the basic structure for a Hilbert space[^1]. One difficulty is that we do not have additive inverses, and another is that we lack an inner product (which any Hilbert space must have, and which we need to calculate probabilities in a quantum system).

Interestingly, while the additive inverses are rather tricky to define, and will have to wait until section [1](#mstuff){reference-type="ref" reference="mstuff"} when we define $M$-stuff types, the inner product does not even need to be defined as a special construction, or imposed as extra structure: a canonical one arises directly from the categorified framework as a (in part because by describing stuff types as functors into $\boldsymbol{\operatorname{{Set}}}$, we are in effect choosing an ordered basis for this categorified equivalent of a Hilbert space). What is more, a Hilbert space should have an algebra of linear operators - endofunctions - which acts on it. We need to see what the equivalents of operators on stuff types are before we can use them to categorify the oscillator. We will see that these are directly related to the inner product.

## Inner Product of Stuff Types {#stuffinnerprod}

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

## Stuff Operators

So far we have described stuff types, and implied that they, as extensions of structure types, are a useful way of categorifying functions - in the setting where these functions are seen as states of a certain quantum system. The inner product defined in section [0.1](#stuffinnerprod){reference-type="ref" reference="stuffinnerprod"} gives these some of the structure of a Hilbert space, and also makes a connection to Feynman diagrams for energy quanta of a harmonic oscillator. We want to describe more of the structure of the 2-rig of stuff types - in particular its linear structure, demanding a definition for the equivalent of a linear operator. We call such a thing a *stuff operator*. There will be a category of these, called $\boldsymbol{\operatorname{{StuffOps}}}$, with higher-dimensional algebraic structure similar to that of the algebra of linear operators on a Hilbert space, with an action on the category $\boldsymbol{\operatorname{{StuffTypes}}}$.

We need to describe this action: a stuff operator $T$, given a stuff type $\Psi:X\rightarrow\boldsymbol{\operatorname{{FinSet_0}}}$, ought to produce another stuff type $T(\Psi):T(X)\rightarrow\boldsymbol{\operatorname{{FinSet_0}}}$, using natural category-theoretic operations, in a way that reflects the fact that $T$ is the categorified equivalent of a linear operator on a Hilbert space of states. One way to motivate our approach to constructing this is to remember that for a Hilbert space $H$, a linear operator $T$ can be thought of as an element of the tensor product $H \otimes H^{\ast}$ of $H$ with its dual, and given a basis of $H$, $T$ can be represented as a matrix (a two-index tensor). To put this into the same framework as the stuff type $\Psi$, recall that this can be seen as a vector in a space of states[^2], and the equivalent of resolving it in a basis arises by taking the preimages of elements of $\boldsymbol{\operatorname{{FinSet_0}}}$ as the components in the basis. In this setting, applying $T$ to a vector $\boldsymbol{v}$ (using the $H^{\ast}$ in the description in terms of $H \otimes H^{\ast}$) amounts to applying covectors in any decomposition of $T$ to $\boldsymbol{v}$, which (since $H \cong H^{\ast}$) amounts to taking the inner product of $\boldsymbol{v}$ with a vector in $H$. Since we have already seen a natural definition of inner product for stuff types, we will use a similar construction.

A stuff type $\Psi: \boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ can be variously seen as the projection map of a groupoid-bundle on finite sets, and also as a way of picking out an index for some component of a vector in a categorified equivalent of a Hilbert space. A stuff *operator* should have *two* such maps, since it is to correspond to a linear operator. We should think of this as "resolving $T$ in the same basis".

The analogy with matrices suggests that $T$ acts on stuff types in the same way as the inner product, just as matrices act on vectors (resolved in a basis) by way of the inner product in each index. So indeed, $T \Psi$ is defined as a weak pullback:

::: definition
A **stuff operator** is a groupoid $T$ with two projection maps into $\boldsymbol{\operatorname{{FinSet_0}}}$: $$\xymatrix{
   & T\ar_-{p_1}[ld]\ar^-{p_2}[rd] & \\
  \boldsymbol{\operatorname{{FinSet_0}}}& & \boldsymbol{\operatorname{{FinSet_0}}}\\
 }$$
:::

We have seen the internal picture of objects of $\Psi$ in figure [\[fig:typeobject\]](#fig:typeobject){reference-type="ref" reference="fig:typeobject"}, so we next look at a similar description for $T$. An object $t \in T$ is somewhat similar to an object of $\Psi$, but this object has not just one underlying set, but two possibly distinct ones, which we call $p_1(t)$ and $p_2(t)$, which in general need not have the same cardinality. We can think of this as two sets sharing a common label, which we may think of as a "process" connecting $p_1(t)$ with $p_2(t)$, where the label $t$ contains *stuff* associated to this transition, shown generally in ([\[eq:stuffopobject\]](#eq:stuffopobject){reference-type="ref" reference="eq:stuffopobject"}) and illustrated in figure [3](#fig:stuffopobject){reference-type="ref" reference="fig:stuffopobject"}.

$$\label{eq:stuffopobject}
 \xymatrix{
  *+[F-,]{\bullet \dots \bullet} &
  *++[o][F-]{t}\ar^-{p_1}[l]\ar_-{p_2}[r] &
  *+[F-,]{\circ \dots \circ} \\
 }$$

<figure id="fig:stuffopobject">
<div class="center">
<embed src="stuffopobject.eps" />
</div>
<figcaption><span id="fig:stuffopobject" label="fig:stuffopobject"></span>Object in the Groupoid of Stuff Operator <span class="math inline"><em>T</em></span></figcaption>
</figure>

We are not yet at the point of recovering Feynman diagrams, but we can already see an object which contains some sort of label for a process connecting an $n$-element set of "quanta" (in the convention we have already applied to the harmonic oscillator) to an $m$-element set of "quanta". First we should see how these act like linear operators.

We can define an algebraic structure of stuff operators, when we recall how the the categorical product and coproduct work for groupoids $\boldsymbol{\operatorname{{X}}}$ and $\boldsymbol{\operatorname{{Y}}}$ in $\boldsymbol{\operatorname{{Gpd}}}$. The coproduct $\boldsymbol{\operatorname{{X}}} + \boldsymbol{\operatorname{{Y}}}$ is just the direct sum of groupoids, whose objects and morphisms are all objects and morphisms of either $\boldsymbol{\operatorname{{X}}}$ or $\boldsymbol{\operatorname{{Y}}}$ (in a way which distinguishes where they came from). Their categorical product of has objects and morphisms both consisting of ordered pairs of those from $\boldsymbol{\operatorname{{X}}}$ and $\boldsymbol{\operatorname{{Y}}}$. We have seen that these operations are compatible with groupoid cardinalities.

::: definition
Given two stuff operators $T$, $T'$ with projection operators $p_1$, $p_2$ and $p'_1$, $p'_2$, respectively, the **sum** has groupoid $T + T'$ whose projection functors $p_i + p'_i$ act like $p_i$ or $p'_i$ as appropriate. The **product of $T$ by a groupoid** $\boldsymbol{\operatorname{{G}}}$, $\boldsymbol{\operatorname{{G}}}T$ has objects is the product groupoid $\boldsymbol{\operatorname{{G}}} \times
T$ (with projection operators acting on the $T$ component).
:::

These naturally have the properties that $(T + T')\Psi \cong T\Psi +
T'\Psi$ and $(\boldsymbol{\operatorname{{G}}}T)\Psi \cong \boldsymbol{\operatorname{{G}}}(T\Psi)$ in the sense of the sum and "scalar product" of stuff types, and thus the corresponding facts hold "on the nose" (i.e. as equations) for cardinalities. On the other hand, if we think of the stuff operators as the categorified equivalent of infinite matrices (with projection operators the equivalent of indexing), we can think of these as the sum and scalar product for matrices, defining the linear structure of the algebra of operators. We leave the proof of this to the interested reader.

More interesting is its internal multiplication, and the action on our categorified Hilbert space, the 2-category $\boldsymbol{\operatorname{{StuffTypes}}}$.

::: definition
[]{#def:stuffopdefns label="def:stuffopdefns"} There is also an **action of $T$ on a stuff type** $\Psi$ giving a stuff type $T\Psi$ given by a weak pullback: $$\xymatrix{
   & & T\Psi\ar_-{P_T}[ld]\ar^-{P_X}[rd]\ar@/_2pc/_-{P_T;p_1}[ddll] & \\
   & T\ar^-{p_1}[ld]\ar_-{p_2}[rd]\ar@{<=}[rr]_{\alpha}^{\sim} & & X\ar^-{\Psi}[ld] \\
   \boldsymbol{\operatorname{{FinSet_0}}}& & \boldsymbol{\operatorname{{FinSet_0}}}&\\
 }$$ and a **composite** of $T$ and $T'$ given similarly: $$\xymatrix{
   & & TT'\ar_-{P_T}[ld]\ar^-{P_T'}[rd]\ar@/_2pc/_-{P_T;p_1}[ddll]\ar@/^2pc/^-{P_T';p'_2}[ddrr] & & \\
   & T\ar^-{p_1}[ld]\ar_-{p_2}[rd]\ar@{<=}[rr]_{\alpha}^{\sim} & & T'\ar^-{p'_1}[ld]\ar_-{p'_2}[rd] & \\
   \boldsymbol{\operatorname{{FinSet_0}}}& & \boldsymbol{\operatorname{{FinSet_0}}}& & \boldsymbol{\operatorname{{FinSet_0}}}\\
 }$$
:::

Here, we note that $(TT')\Psi \cong T(T'\Psi)$, which can be seen by considering the isomorphisms $\alpha$ of the weak pullbacks in the diagrams for these two constructs.

Now, the groupoid $T \Psi$ resulting from the action of $T$ naturally becomes a stuff type (a groupoid over $\boldsymbol{\operatorname{{FinSet_0}}}$) by composition of the projections $P_T;p_2 = p_2 \circ P_T$, where $P_T$ is the projection onto $T$ from $T \Psi$, which is the pullback of the functor $\Psi$ from $\boldsymbol{\operatorname{{X}}}$ onto $\boldsymbol{\operatorname{{FinSet_0}}}$ along the projection $P$ from $T$ to the same copy of $\boldsymbol{\operatorname{{FinSet_0}}}$. To understand this construction better, we should see what the objects and morphisms of the groupoid $T \Psi$ are like internally.

The stuff type $T \Psi$ is a weak pullback of $T$ and $\Psi$, over the copy of $\boldsymbol{\operatorname{{FinSet_0}}}$ which is the target of $\Psi : \boldsymbol{\operatorname{{X}}} \rightarrow
\boldsymbol{\operatorname{{FinSet_0}}}$, and also of $p_2 : T \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$. Its objects will be pairs of objects $x \in \boldsymbol{\operatorname{{X}}}$ and $t \in T$ together with isomorphisms $\alpha_{x,t}:\Psi(x) \rightarrow p_2(t)$. These are isomorphisms of the underlying sets, so in particular they only exist if these sets have the same cardinality. Thus, an object of $T\Psi$ looks like an object of $T$ connected by a bijection of underlying sets to an object of $\Psi$ (using the "right-hand" underlying set of $T$). The general form is shown in ([\[eq:stuffopresult\]](#eq:stuffopresult){reference-type="ref" reference="eq:stuffopresult"}) and an example is illustrated in figure [4](#fig:stuffopresult){reference-type="ref" reference="fig:stuffopresult"}.

$$\label{eq:stuffopresult}
 \xymatrix{
  *+[F-,]{\bullet \dots \bullet} & 
  *++[o][F-]{t}\ar^-{p_1}[l]\ar_-{p_2}[r] & 
  *+[F-,]{\circ \dots \circ} &   & \\
   &   &  *+[F-,]{\circ \dots \circ}\ar_-{\alpha_{x,t}}[u] &
  *++[o][F-]{x}\ar^-{\Psi}[l] \\
 }$$

<figure id="fig:stuffopresult">
<div class="center">
<embed src="stuffopresult.eps" />
</div>
<figcaption><span id="fig:stuffopresult" label="fig:stuffopresult"></span>Object of Stuff Type <span class="math inline"><em>T</em><em>Ψ</em></span></figcaption>
</figure>

Since this is to be an object of $T\Psi$, we should see it as a stuff type it its own right, over the copy of $\boldsymbol{\operatorname{{FinSet_0}}}$ mapped to under the projection $p_1$ from $T$. That is, everything in this picture - the $t$ object, $x$ object, and the specific bijection $\alpha_{x,t}$ between the appropriate underlying sets - can be regarded as "$T\Psi$-stuff" attached to the underlying set $p_1(t)$.

Now as for the composite of $T$ and $T'$, similar reasoning holds except that we have another stuff operator $T'$ in place of $\Psi$, so the general form of an object of $TT'$ is as shown in ([\[eq:stuffopcomposition\]](#eq:stuffopcomposition){reference-type="ref" reference="eq:stuffopcomposition"}), and an example is illustrated in figure [5](#fig:stuffopcomposition){reference-type="ref" reference="fig:stuffopcomposition"}.

$$\label{eq:stuffopcomposition}
 \xymatrix{
  *+[F-,]{\bullet \dots \bullet} & 
  *++[o][F-]{t}\ar^-{p_1}[l]\ar_-{p_2}[r] & 
  *+[F-,]{\circ \dots \circ} & & & \\
   &   &  *+[F-,]{\circ \dots \circ}\ar_-{\alpha_{t,t'}}[u] &
  *++[o][F-]{t'}\ar^-{p'_1}[l]\ar^-{p'_2}[r] & *+[F-,]{\diamond \dots \diamond}\\
 }$$

<figure id="fig:stuffopcomposition">
<div class="center">
<embed src="stuffopcomposition.eps" />
</div>
<figcaption><span id="fig:stuffopcomposition" label="fig:stuffopcomposition"></span>Object of Stuff Type <span class="math inline"><em>T</em><em>T</em>′</span></figcaption>
</figure>

The construction we have described for stuff operators is an example of a "span": in particular, as morphisms from $\boldsymbol{\operatorname{{FinSet_0}}}$ to itself. The composition we have described above, as well as being analogous to matrix multiplication of linear operators, satisfies the axioms for composition of morphisms. But in fact we have seen that these operators also have an action on the category $\boldsymbol{\operatorname{{StuffTypes}}}$, derived from the fact that it is a category over $\boldsymbol{\operatorname{{FinSet_0}}}$. In fact, we can interpret stuff operators as endofunctors of $\boldsymbol{\operatorname{{StuffTypes}}}$, just as linear operators are endofunctions of a vector space. We describe this in more detail in appendix [\[sec:2cat\]](#sec:2cat){reference-type="ref" reference="sec:2cat"}.

## Feynman Diagrams and Stuff Operators {#sec:feynman}

From a quantum mechanical point of view, we are often interested in finding inner products such as $\left\langle{ \Phi, T \Psi }\right\rangle$, and finding these inner products can be done by means of Feynman diagrams. That is, in QM, the "transition amplitude" between states $\Phi$ and $T
\Psi$ is a sum of amplitudes associated to Feynman diagrams, each showing one possible way of getting from state $\Phi$ to state $\Psi$ by process $T$. We will show how this idea can be recovered in the categorified setting, and in fact is given by exactly the algebraic ideas we have defined. In general, the groupoid $\left\langle{ \Phi, T \Psi
}\right\rangle$ has objects as shown in figure [6](#fig:stuffopinprodobject){reference-type="ref" reference="fig:stuffopinprodobject"}

<figure id="fig:stuffopinprodobject">
<div class="center">
<embed src="stuffopinprodobject.eps" />
</div>
<figcaption><span id="fig:stuffopinprodobject" label="fig:stuffopinprodobject"></span>Object of Groupoid <span class="math inline">⟨<em>Ψ</em>,<em>T</em><em>Φ</em>⟩</span></figcaption>
</figure>

We will see that we can think of these as Feynman diagrams, and finding the sum over their amplitudes is exactly the process of taking the groupoid cardinality of this inner product of stuff types - that is, a sum over Feynman diagrams of some "amplitudes". At the moment, these amplitudes are all positive reals, rather than complex numbers as is usual in quantum mechanics. When we discuss $M$-stuff types in section [1](#mstuff){reference-type="ref" reference="mstuff"}, and in particular the case $M = U(1)$ in section [1.2](#mstuffu1){reference-type="ref" reference="mstuffu1"}, we will see how this can be resolved by introducing the quantum mechanical notion of *phase*.

Since we are motivated here by the use of the algebra of stuff types as a categorification of the Weyl algebra, we examine the stuff operators $A$ and $A^{\ast}$, the annihilation and creation operators. The annihilation operator $A$ can be realized in this form, with $T =
\boldsymbol{\operatorname{{FinSet_0}}}$ with two projection functors to $\boldsymbol{\operatorname{{FinSet_0}}}$, one of which is the identity, the other of which is the functor whose action on objects is to take a set $S$ and produce $S + \{ \star \}$: $$\boldsymbol{\operatorname{{FinSet_0}}}\mathop{\longleftarrow}\limits^{\boldsymbol{1}}
  \boldsymbol{\operatorname{{FinSet_0}}}\mathop{\longrightarrow}\limits^{+ \{ \star \}}
  \boldsymbol{\operatorname{{FinSet_0}}}$$

To see that this reduces to our previous definition for $A$ (definition [\[structladder\]](#structladder){reference-type="ref" reference="structladder"}) on stuff types which happen to be structure types, first recall that it said an $A F$-structure on a set $S$ is an $F$-structure on the set $S \cup \{\star\}$. If our stuff type $\Psi$ happens to be a structure type $F$ whose groupoid is just a set of $F$-structured finite sets, then we have:

$$\xymatrix{
   & & A S \ar_-{P_1}[ld]\ar^-{P_2}[rd]\ar@/_2pc/_-{AF=P_1}[ddll] & \\
   & \boldsymbol{\operatorname{{FinSet_0}}}\ar^-{\boldsymbol{1}}[ld]\ar_-{+\{\star\}}[rd]\ar@{<=>}[rr]_-{\alpha} & & S\ar^-{F}[ld] \\
   \boldsymbol{\operatorname{{FinSet_0}}}& & \boldsymbol{\operatorname{{FinSet_0}}}&\\
 }$$

Tracing the map in the new type $A F$ from $A S$ to $\boldsymbol{\operatorname{{FinSet_0}}}$, we note that we can pass through $S$ so that $A F = P_2;\alpha$, in which case we see that since $\alpha$ must make the lower triangle commmute so that $\alpha;+\{\star\}=F$ we get that the preimage of a given finite set $S$ under $A F$ must correspond to the preimage of $S+\{\star\}$ under $F$. So indeed, putting an $A F$-structure on $S$ amounts to putting an $F$-structure on $S+\{\star\}$.

Similar reasoning shows that $A^{\ast}$, the adjoint of $A$, can be realized in the same way, with groupoid $T^{\ast} = \boldsymbol{\operatorname{{FinSet_0}}}$ but with the projections reversed: $$\boldsymbol{\operatorname{{FinSet_0}}}\mathop{\longleftarrow}\limits^{+ \{ \star \}}
  \boldsymbol{\operatorname{{FinSet_0}}}\mathop{\longrightarrow}\limits^{\boldsymbol{1}}
  \boldsymbol{\operatorname{{FinSet_0}}}$$ Moreover, this acts like $A^{\ast}$, so that in the event that $\Psi=F$ is a structure type, a $A^{\ast}F$-structure on a finite set $S$ amounts to choosing an element of $S$ and putting an $F$ structure on what remains.

From the parallel with Fock space, one operator we should want to define is the *field operator* $A + A^{\ast}$. As a stuff operator, this behaves as one might expect: the groupoid in the stuff operator is just the groupoid sum $T + T^{\ast}$ (i.e. two copies of $\boldsymbol{\operatorname{{FinSet_0}}}$), and the projections just act as the projections on $T$ and $T^{\ast}$ when applied to objects and morphisms from each of the two copies. So, the objects of the groupoid $\Phi$, following the pattern we illustrated in ([\[eq:stuffopobject\]](#eq:stuffopobject){reference-type="ref" reference="eq:stuffopobject"}), look like either objects of $A$ or of $A^{\ast}$, as shown in figure [7](#fig:fieldoperatorobject){reference-type="ref" reference="fig:fieldoperatorobject"}.

<figure id="fig:fieldoperatorobject">
<div class="center">
<embed src="fieldoperator.eps" />
</div>
<figcaption><span id="fig:fieldoperatorobject" label="fig:fieldoperatorobject"></span>Example Objects in the Categorified Field Operator</figcaption>
</figure>

In our categorified setting, this is written nearly the same way, $\left\langle{Z^n,\Phi^k Z^m}\right\rangle$, but we now have an interpretation of the inner product as a groupoid over $\boldsymbol{\operatorname{{FinSet_0}}}$, obtained by a pullback - and indeed, of the stuff operator $\Phi^k$ as a composite of stuff operators, etc. Now, this $\Phi^k$ has objects which are chains of objects of the form in figure [7](#fig:fieldoperatorobject){reference-type="ref" reference="fig:fieldoperatorobject"}, composed as in figure [5](#fig:stuffopcomposition){reference-type="ref" reference="fig:stuffopcomposition"}. We can draw these in various ways (different drawing styles form objects in equivalent categories), but for compactness, we will draw these in a style which omits the "internal" bijections of the composite type, and also the bijections from the $A$ and $A^{\ast}$ objects of $\Phi$ to $\boldsymbol{\operatorname{{FinSet_0}}}$. Thus, each internal finite set would have previously been drawn three times, with bijections between them. This compact style is illustrated in figure [8](#fig:phi-n){reference-type="ref" reference="fig:phi-n"}, which shows an object of $\Phi^4$. This one shows an object made from one annihilation and three creation operators, in that order. All other permutations of four $\Phi$-objects are possible also.

<figure id="fig:phi-n">
<div class="center">
<embed src="phi-n.eps" />
</div>
<figcaption><span id="fig:phi-n" label="fig:phi-n"></span>Example Object From <span class="math inline"><em>Φ</em><sup>4</sup></span></figcaption>
</figure>

For the sake of further compactness (and another drawing style depicting an equivalent category), note that what we really have here is an operation in which $k$ quanta of energy either appear or disappear, and do so in a definite order. We could really draw this with just a single "interaction" vertex, incident with $k$ strands (all other strands passing straight through the diagram, matching up a quantum in the top with a quantum in the bottom). These incidences would have to be labelled with a total ordering, so that the object shown in figure [8](#fig:phi-n){reference-type="ref" reference="fig:phi-n"} would be drawn as in figure [9](#fig:field4oplabelled){reference-type="ref" reference="fig:field4oplabelled"}.

<figure id="fig:field4oplabelled">
<div class="center">
<embed src="field4oplabelled.eps" />
</div>
<figcaption><span id="fig:field4oplabelled" label="fig:field4oplabelled"></span>Example Object From <span class="math inline"><em>Φ</em><sup>4</sup></span> (Alternate Style)</figcaption>
</figure>

There is an action of the permutation group $S_k$ on these objects, changing the order in which we encounter objects from $A$ and $A^{\ast}$ as we pass through $\Phi^k$. That is, for every object we get whose diagram has one order labelling the incidences, we will get objects with all other possible orders exactly once through the action of the permutation group $S_k$, also known as $k!$. So if we want to omit this labelling for clarity in the drawings, we can do so as long as we remember that this means we are really drawing objects of the weak quotient $\Phi^k /\,\!\!/ S_k$ (weak quotients are defined in definition [\[def:weakquotient\]](#def:weakquotient){reference-type="ref" reference="def:weakquotient"}). The objects of this weak quotient are isomorphism classes of diagrams under permutations of labellings. These permutations give the natural isomorphisms in the definition of weak quotient by taking any labelled diagram to the same diagram with permuted labels. In this new category, the cardinality of the groupoid is thus scaled by $\frac{1}{k!}$. We also need to keep in mind that an unlabelled diagram really stands in for possibly several different inequivalent labellings of the incidences by distinct orderings.

All this is really a notational convenience: really, to calculate transition amplitude between states $\psi$ and $\phi$ for which we have a description as stuff types $\Psi$ and $\Phi$, when we put the system through some process $t$ which we describe as a stuff operator $T$, we only need to find the groupoid cardinality $|\left\langle{\Psi,T\Phi}\right\rangle|$. Simplifying diagrams and finding convenient conventions for labelling them is really a way for getting a calculational convenience out of diagrams like figure [10](#fig:field4op){reference-type="ref" reference="fig:field4op"}, which shows an object from the groupoid $\Phi^4
/\,\!\!/ S_4$.

<figure id="fig:field4op">
<div class="center">
<embed src="field4op.eps" />
</div>
<figcaption><span id="fig:field4op" label="fig:field4op"></span>Example Object in <span class="math inline"><em>Φ</em><sup>4</sup>/   /<em>S</em><sub>4</sub></span></figcaption>
</figure>

Now, diagrams like this give vertices with $k$ incidences. Taking polynomials in the operators which give such diagrams gives operators which can be interpreted in terms of diagrams having several such vertices. Such a diagram is shown in figure [11](#fig:feynmaninprod){reference-type="ref" reference="fig:feynmaninprod"} - note that here we continue the practice of omitting to draw the internal finite sets in the composite stuff operator.

<figure id="fig:feynmaninprod">
<div class="center">
<embed src="feynmaninprod.eps" />
</div>
<figcaption><span id="fig:feynmaninprod" label="fig:feynmaninprod"></span>An Object in <span class="math inline">⟨<em>Ψ</em><sub>2</sub>,(<em>Φ</em><sup>3</sup>/   /<em>S</em><sub>3</sub>)<sup>6</sup><em>Ψ</em><sub>1</sub>⟩</span></figcaption>
</figure>

Given two stuff types $\Psi_1:\boldsymbol{\operatorname{{X_1}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ and $\Psi_2:\boldsymbol{\operatorname{{X_2}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, we can take the inner product $\left\langle{\Psi_1,\Phi^{n}\Psi_2}\right\rangle$. This applies this operator to $\Psi_2$ to give compound objects involving objects of $\Phi^{n}$ and of $\boldsymbol{\operatorname{{X_2}}}$. Taking the inner product with $\Psi_1$ gives objects as illustrated in figure [11](#fig:feynmaninprod){reference-type="ref" reference="fig:feynmaninprod"}. The groupoid cardinality of this inner product amounts to a sum over all such diagrams, each with a weight related to the size of the symmetry group of the diagram.

::: example
We can use the above to show the categorical meaning of the usual calculation of the expectation value of a power of the field operator. In particular, suppose we want to calculate $\left\langle{1,\frac{\phi^6}{6!} 1}\right\rangle$, the vacuum expectation value of the 6th power of the (normalized) field operator.

To do this, we want to take a sum over objects which are equivalent to ways of matching two empty sets with diagrams like figure [10](#fig:field4op){reference-type="ref" reference="fig:field4op"}, containing one vertex of valence 6. We begin with the case where incidences are labelled (as in figure [9](#fig:field4oplabelled){reference-type="ref" reference="fig:field4oplabelled"}). Since the source and target sets are empty, all edges must form loops touching the vertex at both ends. The number of such diagrams is $(\binom{6}{2} \binom{4}{2}
\binom{2}{2})/3!=15$ (choosing the endpoints of three edges, without order). These give the objects of a groupoid one of which is shown in figure [12](#fig:6vertex){reference-type="ref" reference="fig:6vertex"}.

<figure id="fig:6vertex">
<div class="center">
<embed src="6vertex.eps" />
</div>
<figcaption><span id="fig:6vertex" label="fig:6vertex"></span>Example Object in <span class="math inline">⟨1,<em>Φ</em><sup>6</sup>/   /<em>S</em><sub>6</sub>1⟩</span></figcaption>
</figure>

The isomorphisms of this groupoid are given by permutations of the labels. Since this permutation group is $S_6$ with $720$ elements, the groupoid cardinality should be $\frac{15}{720}=\frac{1}{48}$. The automorphism group of any such diagram is of size 48: there are 6 ways to map the set of loops to themselves, each with the same orientation, or reversed orientation. Equivalently, we can think of the objects of the groupoid as diagrams like this, but without labels. In this case, there is only one such diagram, with the automorphism group as just described. So we have $\left\langle{1,\frac{\phi^6}{6!}1}\right\rangle =
|\left\langle{1,\Phi^5 /\,\!\!/S_6 1}\right\rangle| = \frac{1}{48}$.
:::

Now, the transition amplitude between two states in a quantum harmonic oscillator which undergoes an interaction described by a given operator in the Weyl algebra can be calculated, in part using a sum over Feynman diagrams. We have now seen how, in this categorified setting, we can find a direct combinatorial interpretation for this fact.

Unfortunately, some features of the diagrams used in quantum mechanics are missing from this interpretation. In particular, we do not have any way to express the notion of "phase", or operators involving propagators without interactions. In quantum mechanics, states exist in superpositions - linear combinations - having complex coefficients. Non-interacting propagation in time involves the rotation of those coefficients by a phase - that is, a unit complex number. Thus, both $\mathbbm{C}$ and the group $U(1)$ of phases are important. We will see in section [1](#mstuff){reference-type="ref" reference="mstuff"} how to incorporate this into our combinatorial picture. As we shall see, this involves an explicit decomposition of complex numbers into amplitudes and phases.

# $M$-Stuff Types And Quantum Mechanics {#mstuff}

We have described various entities under the heading *types*, namely stuff, structure, and property types, and hinted at the possibility that this sequence of classifications will continue as we move into the setting of increasingly higher-dimensional categories. For physical purposes, though, we are still missing some essential properties which we would like a categorified version of quantum mechanics to have. In particular, all of our cardinalities, and hence coefficients of our types, lie in *rigs*, rather than rings - they can be added and multiplied, but not subtracted and divided. It is possible to handle this in the abstract setting of structure types by defining *virtual structure types* as equivalence classes of formal differences of structure types (and similarly for stuff types) to make subtraction possible (see [@BLL]). For quantum mechanics, however, the coefficients of the power series which represent states are complex numbers, and the physical significance of *phase* is of paramount importance, so we will still need something more. So for our purposes, it makes more sense to treat the question in a different way.

## $M$-Stuff Types

Now we will see an analog of a stuff type which can carry a phase - or more generally, a weighting of some kind. To reproduce some of the features of quantum mechanics which don't appear in the picture of stuff types as "categorified states", we should consider what is missing. First, states of a quantum system should form a Hilbert space, and in particular a vector space. Since we already have something like an inner product, what is missing is the ability to take linear combinations of states. For this, they need to have a notion of scalar product and of addition. If we allow the categorified states to carry a weight, this weight can play the role of a scalar multiple, but these weights need to form a monoid, which we think of as multiplicative.

This is the motivation for defining a notion of "$M$-Stuff Types" for some monoid $M$, and in particular $M = U(1)$, the group of phases. This is the case which is most interesting for quantum mechanics. We'll do this in general, since the construction does not require $M = U(1)$.

### $M$-Sets

Before we can talk about $M$-Stuff Types, we should start with a more basic definition:

::: definition
If $M$ is a monoid, $\boldsymbol{\operatorname{{MSet}}}$ is the category of "sets over $M$"[^3], or "$M$-sets". Its objects are pairs $(S,f)$, for $S \in \boldsymbol{\operatorname{{Set}}}$ and $f : S
  \rightarrow M$. Morphisms between two $M$-sets $f_1 : S_1
  \rightarrow M$ and $f_2 : S_2 \rightarrow M$ are maps $g : S_1
  \rightarrow S_2$ in $\boldsymbol{\operatorname{{Set}}}$ giving commuting triangles: $$\xymatrix{
    S_1\ar_{f_1}[d]\ar^{g}[r] & S_2\ar^{f_2}[dl] \\
    M & \\
   }$$
:::

By abuse of notation, we will sometimes call the object just $S$ or just $f$ if the meaning is clear by context. A similar definition can be made for $\boldsymbol{\operatorname{{MFinSet}}}$ or $\boldsymbol{\operatorname{{MFinSet_0}}}$, where the sets $S$ lie in $\boldsymbol{\operatorname{{FinSet}}}$ or $\boldsymbol{\operatorname{{FinSet_0}}}$.

Note that for each set $S$ of cardinality $n$, the set of all $M$-sets with "overlying set" $S$ is just $M^S$, equivalent to $M^n$. The morphisms which make this into an over category provide some extra structure, however.

We also note that this definition is similar to that for a $Z_0$-coloured set for a groupoid $Z_0$ - in fact, the image one should have of an $M$-coloured set is just the same as figure [\[fig:colouredset\]](#fig:colouredset){reference-type="ref" reference="fig:colouredset"}. One difference is that in this case, the picture we have for morphisms is different from that for $Z_0$-coloured sets: for $M$-Sets, morphisms are just set maps which are compatible with the labelling. We could, of course, define a weak over category of sets "weakly over $M$", as we did with groupoid-coloured sets, for which strands of morphisms are also labelled by elements of $M$, but as we shall see, this is not what we want to do. One result of this is that we lose some of the desirable features of the category of sets, while retaining others. For example, we have the following:

::: theorem
$\boldsymbol{\operatorname{{MSet}}}$ is a category with all colimits (in particular, it has coproducts).

::: proof
*Proof.* First, consider any diagram in $\boldsymbol{\operatorname{{MSet}}}$, and take the underlying diagram in $\boldsymbol{\operatorname{{Set}}}$. Since $\boldsymbol{\operatorname{{Set}}}$ is a cocomplete category, every diagram, and in particular this one, has a colimit $S$. The diagram in $\boldsymbol{\operatorname{{MSet}}}$ has a colimit provided we can construct a map from $S$ to $M$ which is compatible with the set-maps from the objects of the diagram in $\boldsymbol{\operatorname{{MSet}}}$. For any given element in $S$, every element taken to it by one of the maps in $\boldsymbol{\operatorname{{Set}}}$ must have the same image in $M$ under the map for the corresponding object in $\boldsymbol{\operatorname{{MSet}}}$, since if there is more than one, they must be taken to some common element by maps in the diagram. Thus, we can consistently define $f(s)$ for any element in the colimit to be equal to the value for any preimage, and so all the maps in $\boldsymbol{\operatorname{{Set}}}$ are compatible with the function into $M$, and the colimit in $\boldsymbol{\operatorname{{Set}}}$ becomes a colimit in $\boldsymbol{\operatorname{{MSet}}}$. ◻
:::
:::

Coproducts in $\boldsymbol{\operatorname{{MSet}}}$ can be interpreted as direct sums of $M$-sets - and this makes it possible to define a cardinality for $M$-sets. We note that since $M$ has only one monoidal operation, we could consider two interesting kinds of cardinality, depending on whether we want this operation to look like addition or multiplication.

For our purposes, it is better to think of $M$ as a multiplicative monoid, since we will later want to take $M=U(1)$, thought of as a subgroup of $\mathbbm{C}$. So we would like to have a notion of cardinality which gets along with multiplication in an analogous way. We should define a notion of cardinality which reduces to set cardinality when we think of $M$ as multiplicative. Then we will find a "tensor product" compatible with this notion of cardinality.

::: definition
The **cardinality** of an $M$-set $S
\mathop{\rightarrow}\limits^{f} M$ is an element of $\mathbbm{N} \otimes M$ given by $$|S| = \sum_{s \in S} f(s)$$ where the sum is taken in $\mathbbm{N}$.
:::

This cardinality operator is a kind of decategorification: it takes a set $S$ labelled with values in $M$, and gives a formal sum of values in $M$, each taken the number of times it appears in $S$. Note that this is again not compatible with the cartesian product in $\boldsymbol{\operatorname{{MSet}}}$, by the same argument as for the additive cardinality. Instead, we should take the following product:

::: definition
The **tensor product** of two $M$-sets $S
\mathop{\rightarrow}\limits^{f} M$ and $S' \mathop{\rightarrow}\limits^{f'} M$ is an $M$-set $S
\otimes S'$ has underlying set $\underline{S} \times \underline{S'}$ (the cartesian product of underlying sets in $\boldsymbol{\operatorname{{Set}}}$). The map $(f \otimes f'): S \times S' \rightarrow M$ is given by $(f
\otimes f')(s,s') = f(s)\cdot f'(s')$.
:::

::: theorem
The tensor product of $M$-sets satisfies $|S \otimes
S'| = |S| \times |S'|$. When $M$ is commutative, the tensor product is symmetric.

::: proof
*Proof.* $$\begin{aligned}
    |S \otimes S'| & = & \sum_{(s,s')\in \underline{S} \times \underline{S'}} f(s)f'(s') \\
   \nonumber & = & \bigl{(}\sum_{s \in \underline{S}} f(s) \bigr{)} \bigl{(} \sum_{s' \in \underline{S'}} f(s') \bigr{)}\\
   \nonumber & = & |S| \times |S'|
  
\end{aligned}$$ When $M$ is commutative, there is an obvious isomorphism between $S \times S'$ and $S' \times S$ taking $(s,s')$ to $(s',s)$; the labelling is unchanged, since $f(s) f'(s') = f'(s')
  f(s)$. ◻
:::
:::

These constructions for sets can be extended to groupoids, where cardinalities start to look like complex numbers.

### $M$-Groupoids

We would like to extend these results about $M$-sets to a notion of $M$-groupoids and their cardinalities which is compatible with cardinalities of $M$-sets and of ordinary groupoids in the suitable special cases. One way to see the correct approach to $M$-groupoids is to take advantage our existing idea of $M$-sets and a connection we already know between sets and groupoids. This is the concept of a groupoid-coloured set. We define groupoid-coloured $M$-sets by analogy with these. Recall from [\[colouredsets\]](#colouredsets){reference-type="ref" reference="colouredsets"} that a set can be seen as groupoid whose objects are the elements of the set, and with only identity morphisms[^4]. Then we have:

::: definition
Given a groupoid $Z_0$, a **$Z_0$-coloured $M$-set** is an $M$-set $S$ equipped with a **colouring** map $c:S \rightarrow
  Z_0$. **Maps of $Z_0$-coloured $M$-sets** are $M$-set bijections $\sigma: S \rightarrow S'$ together with, for each $x \in
  S$), a morphism $f_x \in \hom(c(x),c'(\sigma(x))$. That is, $$\xymatrix{
    S \ar^{\sigma}[r] \ar_c[d] & S' \ar^{c'}[d] \\
    Z_0 \ar@2{->}[r]_{\{f_x\}} & Z_0
   }$$
:::

This is essentially the same definition as appeared in [\[colouredsets\]](#colouredsets){reference-type="ref" reference="colouredsets"}, but we note that now $\sigma$ is a bijection of $M$-sets - that is, it is a set bijection *which is compatible* with the $M$-labelling. But notice that groupoid-coloured $M$-sets are just sets with two maps, one into a groupoid, and one into a monoid: $$\xymatrix{
   & S \ar_{c}[dl] \ar^{f}[dr] & \\
  Z_0 & & M \\
}$$ Since the elements of this $Z_0$-coloured $M$-set are just elements of $S$ labelled by both an object of $Z_0$ and an element of $M$, we would like to be able to think of this as a set labelled by objects of an "$M$-groupoid", which would look like objects of the groupoid $Z_0$ labelled by element of $M$. A consideration of what morphisms of $Z_0$-coloured $M$-sets must be reveals how to define this:

::: definition
Given a monoid $M$, an **$M$-groupoid** is a groupoid $\mathcal{G}$ with a functor $f$ from $\mathcal{G}$ into the set $M$ regarded as a groupoid. The **cardinality** of an $M$-groupoid $\mathcal{G}_M$ is an element of $\mathbbm{R}^+ \otimes M$, where $\mathbbm{R}^+$ and $M$ are thought of as multiplicative monoids. The cardinality of $\mathcal{G}_M$ is given by the formal sum: $$|\mathcal{G}_M| = \sum_{[x] \in \underline{\mathcal{G}_M}} \frac{f(x)}{|\operatorname{Aut}(x)|}$$
:::

::: remark
Note that $\mathbbm{R}^+ \otimes M$ consists of all formal $\mathbbm{R}^+$-linear sums of formal products $r \otimes m$ for $r
\in \mathbbm{R}^+$ and $m \in M$, subject to the distributive law $(r+r')\otimes m = r \otimes m + r'\otimes m$. It becomes a rig with the obvious multiplication $(r\otimes m)(r' \otimes m') = (rr'
\otimes mm')$.

Since we are thinking of $M$ as a groupoid with only identity morphisms, functoriality of $f$ means that for any $a$ and $b$ in $\mathcal{G}$ and $g \in \operatorname{hom}(a,b)$, we have $f\circ g = f$. That is, the following diagram commutes: $$\xymatrix{
    a \ar^{g}[r] \ar_{f}[d] & b \ar^{f}[dl] \\
    M & \\
  }$$ We see also that $f(x)$ is well defined for elements of any given isomorphism, since any two objects with an isomorphism between them will be sent under $f$ to the same element of $M$. It should be clear that in the case where the "overlying" groupoid of an $M$-groupoid happens to be a set (i.e. groupoid with only trivial morphisms), this reduces to the definition of an $M$-set and its cardinality. In the case where $M$ is the trivial groupoid, this cardinality reduces to the usual groupoid cardinality.
:::

Given two $M$-groupoids, we define their product as with $M$-sets:

::: definition
The **tensor product** of two $M$-groupoids $X
\mathop{\rightarrow}\limits^{f} M$ and $X' \mathop{\rightarrow}\limits^{f'} M$ is an $M$-groupoid $X
\otimes X'$ which has underlying groupoid $\underline{X} \times \underline{X'}$ (the cartesian product of underlying groupoids in $\boldsymbol{\operatorname{{Gpd}}}$). The map $(f \otimes f'): X \times X' \rightarrow M$ is given by $(f
\otimes f')(x,x') = f(x)\cdot f'(x')$.
:::

As with $M$-sets, this product gets along with $M$-groupoid cardinalities. The proof is essentially the same, except that cardinalities involve factors of $|\operatorname{Aut}(x)|$. This depends on the fact that the automorphism group of an object $(x,x')$ in $\underline{X} \times \underline{X'}$ is just the product of the automorphism groups of $x$ and $x'$.

### $M$-Stuff Types and their Cardinalities

We begin with a definition:

::: definition
An **$M$-stuff type** is an $M$-groupoid $\boldsymbol{\operatorname{{X}}} \mathop{\rightarrow}\limits^{f} M$ equipped with a functor $\Psi :
\boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, where $\boldsymbol{\operatorname{{X}}} \in \boldsymbol{\operatorname{{Gpd}}}$.
:::

Typically, we will just think of $\boldsymbol{\operatorname{{X}}}$ as an object of $\boldsymbol{\operatorname{{MGpd}}}$ and blur the details, but this definition is what we always mean. So as with stuff types, we may think of $M$-stuff types as functors from $M$-sets of "$\Psi$-stuffed finite sets" to their underlying finite sets. In the case where $\Psi$ is faithful we can say it is an $M$-structure type. Note that we are still thinking of $\boldsymbol{\operatorname{{X}}}$ as lying over $\boldsymbol{\operatorname{{FinSet_0}}}$, not $\boldsymbol{\operatorname{{MFinSet_0}}}$ - we will return to this shortly.

Since stuff types (and $M$-stuff types) can be multiplied by groupoids, whose cardinalities lie in $\mathbbm{R}^+$, this action by $M$ gives another version of multiplication. This will be particularly interesting when we consider $M = U(1)$ in section [1.2](#mstuffu1){reference-type="ref" reference="mstuffu1"}, but first we should define the cardinality of an $M$-stuff type:

::: definition
The **cardinality** of an $M$-stuff type $\Psi : \boldsymbol{\operatorname{{X}}}
  \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ is $$|\Psi| = \sum_{n \in \underline{\boldsymbol{\operatorname{{FinSet_0}}}}} |\Psi_n|z^n$$ where $|\Psi_n|$ is now the $M$-groupoid cardinality of the preimage of $n$ under $\Psi$.
:::

(As with a stuff type, this definition requires us to take $\boldsymbol{\operatorname{{FinSet_0}}}$ to be skeletal to be well defined - or else to consider only the *essential preimage*. We will do the former.) This cardinality is an element of $(\mathbbm{R}^+ \otimes M)[\![z]\!]$: a formal power series in $z$ whose coefficients are formal combinations of pairs of groupoid cardinalities and elements of $M$.

::: theorem
There are natural left and right actions of the monoid $M$ on the $M$-stuff type $\Psi$. If $M$ is abelian, these are the same action, which satisfies $$|m\Psi|(z) = m|\Psi|(z)$$

::: proof
*Proof.* We define the map $(m,\Psi) \mapsto m\Psi$, where $m\Psi :
  m\boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ acts as follows. If $x\in
  \boldsymbol{\operatorname{{X}}}$ is an object of $\boldsymbol{\operatorname{{X}}}$ whose weight is $f(x)$, then the corresponding element $mx$ in $m\boldsymbol{\operatorname{{X}}}$ has weight $m\cdot f(x)$. Then $m\Psi(mx)=\Psi(x)$. This is a left action on stuff types because it is a left action on $M$-groupoids together with a compatible map to $\boldsymbol{\operatorname{{FinSet_0}}}$. The right action of $M$ is defined similarly.

If $M$ is abelian, a left and right action are the same, and the result follows by direct calculation. ◻
:::
:::

### $M$-Stuff Type Inner Product and $M$-Stuff Operators

Once we defined $M$-sets and hence $M$-groupoids, it was possible to define $M$-stuff types simply by substituting these for groupoids in the original definition of stuff types. The only properties of $\boldsymbol{\operatorname{{FinSet_0}}}$ which were used in the original construction of stuff types and operators was that it should be a groupoid: groupoids $\boldsymbol{\operatorname{{X}}}$ with one or two functors into it were stuff types and operators respectively. Morphisms between the objects of a stuff type were morphisms in $\boldsymbol{\operatorname{{X}}}$ together with compatible bijections of sets (recall figure [\[fig:typemorphism\]](#fig:typemorphism){reference-type="ref" reference="fig:typemorphism"}), but this depended only on the fact that these were isomorphisms in the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$. So, in the same way, a morphism in the groupoid of an $M$-stuff type consists of a morphism in its $M$-groupoid, together with a compatible bijection of underlying sets, as illustrated in figure [13](#fig:mstuffmorphism){reference-type="ref" reference="fig:mstuffmorphism"}. Notice that the objects $x$ and $x'$ are labelled by the same element, $m_1 \in M$, since $f$ is an isomorphism in $\boldsymbol{\operatorname{{X}}}$.

<figure id="fig:mstuffmorphism">
<div class="center">
<embed src="mstuffmorphism.eps" />
</div>
<figcaption><span id="fig:mstuffmorphism" label="fig:mstuffmorphism"></span>A Morphism in the Groupoid of an <span class="math inline"><em>M</em></span>-Stuff Type</figcaption>
</figure>

Now, the inner product of stuff types $\Psi:\boldsymbol{\operatorname{{X}}} \rightarrow
\boldsymbol{\operatorname{{FinSet_0}}}$ and $\Phi:\boldsymbol{\operatorname{{Y}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ was defined to be a weak pullback, as described in ([\[eq:weakpullback\]](#eq:weakpullback){reference-type="ref" reference="eq:weakpullback"}). The same definition will apply if we let these be $M$-stuff types, allowing $\boldsymbol{\operatorname{{X}}}$ and $\boldsymbol{\operatorname{{Y}}}$ to be $M$-groupoids.

So we have a weak pullback of $\Psi$ along $\Phi$, which gives a groupoid $\left\langle{\Psi,\Phi}\right\rangle$, and can define canonical projection maps to $\boldsymbol{\operatorname{{X}}}$ and $\boldsymbol{\operatorname{{Y}}}$. The groupoid is the fibrewise product $\boldsymbol{\operatorname{{X}}} \times_{\boldsymbol{\operatorname{{FinSet_0}}}} \boldsymbol{\operatorname{{Y}}}$, where we must use the tensor product of $M$-groupoids rather than the cartesian product of groupoids to assign elements of $M$ to its objects.

::: definition
The given two $M$-stuff-types $\Psi: \boldsymbol{\operatorname{{X}}}
\rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, and $\Phi: \boldsymbol{\operatorname{{Y}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, the $M$-groupoid $\left\langle{ \Psi, \Phi }\right\rangle = \boldsymbol{\operatorname{{X}}} \otimes_{\boldsymbol{\operatorname{{FinSet_0}}}}
\boldsymbol{\operatorname{{Y}}}$ is the weak pullback of $\Psi$ and $\Phi$ over $\boldsymbol{\operatorname{{FinSet_0}}}$. It has objects which are pairs $(x,y) \in \boldsymbol{\operatorname{{X}}} \otimes
\boldsymbol{\operatorname{{Y}}}$ equipped with an isomorphism $\alpha_{(x,y)} : \Psi(x)
\tilde{\rightarrow} \Phi(y)$. A morphism in $\left\langle{\Psi,\Phi}\right\rangle$ is a morphism in $\boldsymbol{\operatorname{{X}}} \otimes \boldsymbol{\operatorname{{Y}}}$, say $(f,g) : (x,y)
\rightarrow (x',y')$, such that

$$\label{eq:M-inprodnaturality}
\xymatrix{   
\Psi(x) \ar^-{\Psi(f)}[r] \ar_-{\alpha_{x,y}}[d] & \Psi(x') \ar^-{\alpha_{x',y'}}[d] \\   
\Phi(y) \ar_-{\Phi(g)}[r] & \Phi(y') }$$ commutes. That is, $\alpha_{x',y'} \circ \Psi(f) = \Phi(g) \circ \alpha_{x,y}$.
:::

An object in the inner product groupoid looks like figure [14](#fig:mstuffinprodobject){reference-type="ref" reference="fig:mstuffinprodobject"}, where $m_i$ are elements of $M$. This figure is analogous to the previous inner product (figure [1](#fig:pullbackobject){reference-type="ref" reference="fig:pullbackobject"}). Note that, in contrast to the case in figure [13](#fig:mstuffmorphism){reference-type="ref" reference="fig:mstuffmorphism"}, the objects $x \in \boldsymbol{\operatorname{{X}}}$ and $y \in \boldsymbol{\operatorname{{Y}}}$ are not in the same groupoid, hence not related by any morphism, so there is no requirement that $m_1$ and $m_2$ should be equal. The object illustrated is labelled be the element $m_1
\cdot m_2 \in M$ (as highlighted).

<figure id="fig:mstuffinprodobject">
<div class="center">
<embed src="mstuffinprodobject.eps" />
</div>
<figcaption><span id="fig:mstuffinprodobject" label="fig:mstuffinprodobject"></span>An Object In the Inner Product of two <span class="math inline"><em>M</em></span>-Stuff Types</figcaption>
</figure>

Similar changes apply to the other constructions defined using the weak pullback, so that we have nearly identical categorical diagrams definining morphisms in the inner product, as well as the action of an $M$-stuff operator on an $M$-stuff type and the composition of two $M$-stuff operators, as in definition [\[def:stuffopdefns\]](#def:stuffopdefns){reference-type="ref" reference="def:stuffopdefns"}. The sole change at this level is the replacement of groupoids with $M$-groupoids, and thus in figures [4](#fig:stuffopresult){reference-type="ref" reference="fig:stuffopresult"} and [5](#fig:stuffopcomposition){reference-type="ref" reference="fig:stuffopcomposition"}, we have labels in $M$ on every groupoid object, preserved under every isomorphism.

::: definition
An **$M$-stuff operator** is an $M$-groupoid $T$ with two functors from the underlying groupoid of $T$ into $\boldsymbol{\operatorname{{FinSet_0}}}$: $$\xymatrix{
   & T\ar_-{p_1}[ld]\ar^-{p_2}[rd] & \\
  \boldsymbol{\operatorname{{FinSet_0}}}& & \boldsymbol{\operatorname{{FinSet_0}}}\\
 }$$ It acts on an $M$-stuff type to give another $M$-stuff type by weak pullback over one copy of $\boldsymbol{\operatorname{{FinSet_0}}}$.
:::

Just as with the former constructions, we have:

::: theorem
If $\Psi$ and $\Phi$ are two $M$-stuff types, then $|\left\langle{\Psi,\Phi}\right\rangle|=\left\langle{|\Psi|,|\Phi|}\right\rangle$.

::: proof
*Proof.* At the level of the underlying sets and groupoids, every product over a finite set in the (skeletal version of) $\boldsymbol{\operatorname{{FinSet_0}}}$ in the fibrewise product looks just the same as for regular stuff types. Each of these products is a product of $M$-groupoids, which are compatible with cardinality. So the result holds. ◻
:::
:::

## Quantum Mechanics: $M=U(1)$ {#mstuffu1}

As remarked earlier, the notion of a *phase* is crucial in quantum mechanics. Stuff types, and in particular stuff operators and the inner product of stuff types, proved in the last section to have a close connection to entities which resemble Feynman diagrams, but the only notion of cardinality we had for these was groupoid cardinality, which yields positive real values. We would like to be able to do more, since in quantum mechanics, these diagrams should have not a real cardinality, but a complex amplitude, which has both a magnitude and a phase. This leads us to the idea of $U(1)$-stuff types, since $U(1)$ is the group of phases, corresponding to the unit circle in $\mathbbm{C}$.

### $U(1)$-Stuff Types

From here on, we take $M=U(1)$ - an abelian monoid, and in fact an abelian group - we know that $U(1)$-stuff types exist, and that they have cardinalities in $(\mathbbm{R}^+ \otimes U(1))[\![z]\!]$, which has the obvious homomorphism into $\mathbbm{C}[\![z]\!]$. As we have seen, the cardinalities of $M$-sets for an abelian monoid $M$ lie in $M$, which we can think of ; cardinalities for $M$-groupoids lie in $\mathbbm{R}^+ \otimes M$; cardinalities for $M$-stuff types lie in $(\mathbbm{R}^+ \otimes M)[\![z]\!]$. When $M=U(1)$, this gives $\mathbbm{R}^+ \otimes U(1)$, which has a homomorphism onto $\mathbbm{C}$ $$h : \mathbbm{R}^+ \otimes U(1)\rightarrow \mathbbm{C}$$

We should note that this description of $\mathbbm{C}$ in terms of $\mathbbm{R}^+ \otimes U(1)$ explicitly separates complex numbers into a magnitude and a phase, and while it has a multiplication resembling that for $\mathbbm{C}$, but it fails to capture the addition, which is formal. However, the homomorphism $h$ just imposes the relations which define complex addition. The derived rig homomorphism $h: (\mathbbm{R}^+ \otimes U(1))[\![z]\!]\rightarrow
\mathbbm{C}[\![z]\!]$ behaves similarly. This homomorphism loses information, just as the process of taking cardinalities does, so in fact, when $M=U(1)$, we can define a new cardinality operator:

::: definition
If $\boldsymbol{\operatorname{{X}}}$ is a $U(1)$-groupoid and $\Psi:\boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ a $U(1)$-stuff type, the **complex cardinality** of $\Psi$ is $h$ applied to the usual $M$-stuff-type cardinality: $$|\Psi|_{\mathbbm{C}} = h \left( \sum_{S \in \mathbbm{N}} |\Psi_n| z^n \right) = \sum_{S \in \mathbbm{N}} h|\Psi_n| z^n$$ where $|\Psi_n|$ is the usual $M$-stuff cardinality, $h$ is the above homomorphism, and addition is in $\mathbbm{C}$.
:::

The complex cardinality is a map which takes a $U(1)$-stuff type and yields a power series in $\mathbbm{C}[\![z]\!]$, namely Fock space. When dealing with $U(1)$-stuff types, we will write $|\Psi|_{\mathbbm{C}}$ as $|\Psi|$, unless otherwise noted.

::: remark
Note that a type which consists of two states over $U(1)$-sets of the same set cardinality but opposite phase will have a cardinality in $(\mathbbm{R}^+ \otimes U(1))[\![z]\!]$ which contains a formal linear combination which is in the *kernel* of $h$. This is the critical fact that when we represent states in Fock space, there can be *interference* between states with opposite phases. In particular, the amplitude for a (categorified) state containing only those two objects will be zero.
:::

### Conjugation and The Inner Product

There is a property of $U(1)$-stuff types which is not generally shared by $M$-stuff types for arbitrary $M$, resulting from the fact that it is an Abelian group. This follows from the fact that there is a nontrivial monoid isomorphism between $U(1)$ and itself, taking each element of $U(1)$ to its multiplicative inverse. There will be such an isomorphism whenever $M$ is an Abelian group. Viewing $U(1)$ as the unit complex numbers, however, allows us to see this as complex conjugation, which is how we will think of it. Thus, there is an operation special to $U(1)$-stuff types:

::: definition
If $\boldsymbol{\operatorname{{X}}}$ is a groupoid with $U(1)$ labelling $f:\boldsymbol{\operatorname{{X}}}\rightarrow U(1)$, its **conjugate** groupoid is the $U(1)$ groupoid whose groupoid is labelling is $\overline{f}$, given by $\overline{f}(x)=\overline{f(x)}$. When we write $\boldsymbol{\operatorname{{X}}}$ for the $U(1)$-groupoid, we write the conjugate as $\overline{\boldsymbol{\operatorname{{X}}}}$. If $\Psi:\boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ is a $U(1)$-stuff type, its conjugate $\overline{\Psi}$ is the type which acts like $\Psi$ on the objects of the underlying groupoid of $\boldsymbol{\operatorname{{X}}}$.
:::

This allows us to define a variant of the inner product which has the conjugate-linearity of the usual complex inner product on Fock space. To distinguish this from the (bilinear) inner product $\left\langle{\Psi,\Phi}\right\rangle$, and call it $\left\langle{ \Psi | \Phi }\right\rangle$, also a more familiar notation to physicists:

::: definition
The **Fock space inner product** is given by $$\left\langle{ \Psi | \Phi }\right\rangle = \left\langle{ \overline{\Psi} , \Phi }\right\rangle$$
:::

::: theorem
The Fock space inner product, for $U(1)$-stuff types $\Psi$ and $\Phi$ satisfies $|\left\langle{\Psi | \Phi}\right\rangle| =
\left\langle{|\Psi| | |\Phi|}\right\rangle$, giving the usual conjugate-linear inner product on $\mathbbm{C}[\![z]\!]$.

::: proof
*Proof.* $$\begin{aligned}
|\left\langle{\Psi | \Phi}\right\rangle| & = & \sum_{n\in\mathbbm{N}} |\left\langle{\Psi | \Phi}\right\rangle_n|\\
   \nonumber & = & \sum_{n\in\mathbbm{N}} |\overline{\Psi_n}| \cdot |\Phi_n|\\
   \nonumber & = & \left\langle{\,|\Psi|\, |\, |\Phi|\,}\right\rangle
\end{aligned}$$ ◻
:::
:::

So for $U(1)$-stuff types, we might want to define a new inner product given in terms of the usual $M$-stuff type inner product as $\left\langle{\Psi|\Phi}\right\rangle$. We will discuss briefly in section [\[sec:conjtimereversal\]](#sec:conjtimereversal){reference-type="ref" reference="sec:conjtimereversal"} how to interpret this seemingly arbitrary innovation.

It is worth noting here that the inner product between two states of a $U(1)$-stuff type may be zero. Of course, this can happen with stuff types in any case: for instance, if $\Psi$ is the stuff type for which there is one object in $\boldsymbol{\operatorname{{X}}}$ over every even-cardinality set, with automorphism group the same as that of the set, and no others; and $\Phi$ is similar, but has objects over odd-cardinality sets. These have cardinalities (generating functions) $\cosh(z)$ and $\sinh(z)$ respectively. They are examples of what we called "property types" in section [\[sec:forgetful\]](#sec:forgetful){reference-type="ref" reference="sec:forgetful"} - namely, these types can be interpreted as the properties "being an even set" and "being an odd set". These two stuff types are orthogonal in the sense that their inner product is zero. Here, the interpretation is that there are *no* sets having both properties, and so the stuff-type inner product is the empty groupoid.

However, the situation with $U(1)$-types is more subtle: we may have a nonempty inner product groupoid whose $U(1)$-groupoid cardinality happens to be zero. This arises because we may now have negative (and indeed complex) contributions to the sum giving this cardinality. This is related to the quantum mechanical phenomenon of "destructive interference" between states. In our formalism, this interference occurs when we apply the homomorphism $h: \mathbbm{R}^+ \otimes U(1)\rightarrow \mathbbm{C}$ and its derived variants.

We interpret the cardinality of the groupoid inner product as the usual inner product in quantum-mechanics. This is the amplitude for finding our system in a given state $\Phi$ after setting it up in a state $\Psi$, so this says this amplitude (and hence the probability) is zero.

So the transition amplitudes between some of the "pure" (decategorified) states of which $\psi$ and $\phi$ are superpositions may be nonzero, but the phases with which they appear may allow the transition between $\psi$ and $\phi$ to have zero amplitude. Thus, introducing phases allows destructive interference which makes otherwise feasible transitions impossible. We will see in the next section that this issue of phase is closely related to the concept of *time evolution* in quantum mechanics, and the *propagator*.

In particular, in the harmonic oscillator, the phase of a state changes over time, with a frequency proportional to the energy of that state. This is the effect of the *free propagator* for a system, and it is an operator. So we must describe $U(1)$-stuff operators next, and this propagator in particular.

### $U(1)$-Stuff Operators and Time

We have already noted that $M$-stuff operators act on $M$-stuff types just like ordinary stuff operators acting on stuff types, except that the groupoids are now replaced by $M$-groupoids. The groupoid $T\Psi$ for an $M$-stuff operator $T$ and type $\Psi$ then consists of pairs of objects $t \in T$ and $x \in \boldsymbol{\operatorname{{X}}}$ together with a bijection of their underlying sets. As with the product groupoid, this object is labelled by an element in $M$ given by the product of the labels on $t$ and $x$. This is well defined when $M$ is Abelian, as in the case when $M = U(1)$.

One class of $U(1)$-stuff operators which is particularly relevant to quantum mechanics is that of the *time evolution* operators. These are operators which, when applied to an $M$-stuff type $\Psi$, produce an $M$-stuff type $\Psi'$ for which the $M$-labels on the elements of the underlying sets have labels multiplied by a fixed phase in $U(1)$. An example of an object in such an operator, designated $\theta$, is shown in figure [15](#fig:timeevol){reference-type="ref" reference="fig:timeevol"}. Here, we are showing the operator $E_T$, "time evolution by $T$". We show an object which will evolve a state with three quanta of energy. Here, $\mathrm{e}^{iT}$ is the change of phase corresponding to time evolution of a one-energy-quantum state by $T$. A state with three energy quanta changes phase by $\mathrm{e}^{3iT}$.

<figure id="fig:timeevol">
<div class="center">
<embed src="timeevol.eps" />
</div>
<figcaption><span id="fig:timeevol" label="fig:timeevol"></span>An Object in The <span class="math inline"><em>U</em>(1)</span>-Stuff Operator <span class="math inline"><em>E</em><sub><em>T</em></sub></span></figcaption>
</figure>

Any object in $E_T$ has two projections - each to an underlying set of the same size. This corresponds to the fact that in unperturbed time evolution no interactions are occurring which would change the energy level of the system. An object $t$ in the groupoid of $E_T$, lying over sets with $k$ quanta of energy. There will be just one such object in $E_T$ for each finite set. It is labelled by the phase by which a state with $k$ quanta will change in time $T$. The operator $E_T$ acts on any $U(1)$-stuff type (categorified state) to give state to which this has evolved after a time $T$. An object of the resulting stuff type is shown in figure [16](#fig:timeevolresult){reference-type="ref" reference="fig:timeevolresult"}.

<figure id="fig:timeevolresult">
<div class="center">
<embed src="timeevolresult.eps" />
</div>
<figcaption><span id="fig:timeevolresult" label="fig:timeevolresult"></span>An Object in The <span class="math inline"><em>U</em>(1)</span>-Stuff Type <span class="math inline"><em>E</em><sub><em>T</em></sub><em>Ψ</em></span></figcaption>
</figure>

The object in the groupoid of $E_T \Psi$ is the entire ensemble associated to the finite set $p_2(t)$. It includes the object $t \in
E_T$ itself, as well as $x \in \boldsymbol{\operatorname{{X}}}$, their underlying sets and the bijection $\alpha_{x,t}$ between them, and also their associated labels $\mathrm{e}^{3i \theta}$ and $\mathrm{e}^{i \theta_1}$. This is an object in a product $U(1)$-groupoid: $U(1)\boldsymbol{\operatorname{{Gpd}}}$ is a weak 2-category with (weak) products, of which this is an example. This object in the product groupoid $E_T \times \boldsymbol{\operatorname{{X}}}$ is labelled by the product of the labels on $t$ and $x$, namely $\mathrm{e}^{i \theta_1}
\mathrm{e}^{3i \theta}$.

Suppose the $U(1)$-stuff type in question happens to just be $Z^k$ - the categorified state with just $k$ quanta of energy and no phase angle, or the property type "being an $k$-element finite set labelled by $1
\in U(1)$". Then we get $E_T(Z^k) \cong (\mathrm{e}^{i \theta} Z)^k$, and the same fact holds as an equation for the complex cardinalities. So the $U(1)$-cardinality of a $k$-element $U(1)$-set changes by $\mathrm{e}^{i k
\theta}$ in time $T$, since each quantum picks up a phase rotation of $\mathrm{e}^{i \theta}$ in time $T$. In particular, the phase of an object in a categorified state changes with a frequency proportional to its energy (the size of the underlying set).

Choosing time units so that $\theta=T$, we get a phase change of $\mathrm{e}^{iTk}$ on a state of energy $k$. We can write this as $E_T=\mathrm{e}^{iTN}$, where $N$ is the number operator. To prove this equality at the categorified level (using a categorification of the exponential such as we have already discussed) would require a fully categorified version of the complex numbers. However, for now we can observe that this will be true at the level of cardinalities, and take it as a definition. This arises physically from the Hamiltonian formulation of quantum mechanics. We will not enter into this in detail, but note that the free Hamiltonian is just $H_0 = N$, the number operator in the exponent of the propagator, which measures the energy of a state.

Since $\mathrm{e}^{iTN}$ has exactly one object for each cardinality, the product groupoid $\mathrm{e}^{iTN} \Psi$ is equivalent to the groupoid whose objects are the same as those of $\boldsymbol{\operatorname{{X}}}$, but whose $U(1)$-labellings have been multiplied by phases $\mathrm{e}^{iTk}$, for an object with underlying set $\boldsymbol{k}$. This is the groupoid of the state $\Psi$, time-evolved by $T$. Note that time-evolution by $-T$ will be given by a similar operator $E_{-T} = \mathrm{e}^{-iTN}$: all the object-labels are the inverses of those of $E_T$. We will return to this point in section [\[sec:conjtimereversal\]](#sec:conjtimereversal){reference-type="ref" reference="sec:conjtimereversal"}.

In any case, using these propagators, and the $U(1)$ version of inner product groupoids whose objects resemble Feynman diagram for interactions, we recover a combinatorial interpretation for many of the standard features of the quantum mechanics of the harmonic oscillator.

### Feynman Diagrams And Perturbation

Having found a categorification of the quantum harmonic oscillator, we know that transition amplitudes such as $\left\langle{\psi,p(\frac{\phi^n}{n!})\psi '}\right\rangle$ as a sum over Feynman diagrams. In physically realistic settings, this sort of amplitude often arises when we consider the time-evolution of an oscillator which is perturbed. The *free* oscillator evolves in time according to the operator $E_T=\mathrm{e}^{-iTN}$ described above. The *perturbed* oscillator, on the other hand, describes a situation where the energy of the oscillator is modified by another term: it only approximately matches the description of the free oscillator we have been using. Physically, this represents a potential in which the oscillator is moving. This means that the energy of the oscillator is changed by the addition of an extra term, $V$, which is some function of position, which we think of as a *potential energy*, in addition to the energy in the oscillator proper.

In this case, time evolution can be calculated using the new energy, $H = H_0 + V$. If $V$ is a function of position, then since the position is proportional to $\operatorname{a} + \operatorname{a}^{\ast} = \phi$, we have $V = f(\phi)$, for some function $f$. We will consider the case where $f=p$ is some polynomial (though naturally any analytic function can be approximated this way to some degree, so we can obtain successive approximations by taking a sequence of $p_k$ converging to $f$). Since the energy for the free oscillator is already quadratic in position, we assume that $f$ has minimum degree at least 3. In this case, at the decategorified level, the amplitudes for time evolution by time $t$ associated to the Hamiltonian $H = N + V$, are: $$\label{eq:perturbfeynman}
\left\langle{Z^k|\mathrm{e}^{-iTH}Z^l}\right\rangle = \sum_{n=0}^{\infty} \int_{0 \leq t_1 \leq \dots \leq t_n \leq T} \left\langle{Z^k|\mathrm{e}^{-i(T-t_n)N}V\mathrm{e}^{-i(t_n-t_{n-1})N}V \dots V\mathrm{e}^{-it_1N} Z^l}\right\rangle$$ To avoid considering questions of convergence, we think of this purely as a statement about power series in $T$. It would take us too far afield to derive this standard quantum-mechanical fact in full detail, though background can be found in [@bjordrel], and one derivation of this equation in our setting can be found in [@catquan]. However, we will point out here that it follows from the fact that the evolution of a state is governed by the Schrödinger equation, which amounts to: $$\partial_t \psi = -i (\mathrm{e}^{itH_0}V\mathrm{e}^{-itH_0})$$ Integrating this equation over time, we get $$\psi(t) = -i \int_0^t (\mathrm{e}^{itH_0}V\mathrm{e}^{-itH_0})\psi(t_0) \mathrm{d}t_0 + \psi(0)$$ and by repeated substitution of this expression for $\psi(t)$ into the integral, we get the sum of integrals which appear in the expression above. Taking the inner product with this operator, we finally get the whole expression.

Ideally, we would like to derive this equation entirely at the categorified level. However this would require a more complete understanding of the categorified version of the complex numbers than we have constructed here. To recover time evolution by a phase from an expression of the form $\mathrm{e}^{itH_0}$, we would need to see that the result is indeed a phase in $U(1)$.

However, knowing that the equation holds at the decategorified level allows us to give a simple interpretation for the formula.

::: theorem
The transition amplitude $\left\langle{z^k|\mathrm{e}^{-iTH}z^l}\right\rangle$ for the perturbed harmonic oscillator with potential $V=f(\phi)$ is given by a sum over all Feynman diagrams given as composites of those associated with $V$, from a state with $k$ quanta to one with $l$ quanta. The sum is of an integral over all labellings of the edges of the diagrams such that the total phase along all paths is $\mathrm{e}^{-iT}$.

::: proof
*Proof.* This transition amplitude is the $U(1)$-groupoid cardinality of the inner product $\left\langle{Z^k|E^{iTH}Z^l}\right\rangle$, and given by [\[eq:perturbfeynman\]](#eq:perturbfeynman){reference-type="ref" reference="eq:perturbfeynman"}. Consider the operator in that equation, $$O=\mathrm{e}^{-i(T-t_n)N}V\mathrm{e}^{-i(t_n-t_{n-1})N}V \dots V\mathrm{e}^{-it_1N}$$ We know that the terms $\mathrm{e}^{-i(t_i-t_{i-1})N}$ are just free propagators, which contribute a phase of $\mathrm{e}^{-i()}$ for each quantum of energy. We can think of these operators as having objects given by any number of "strands", one for each quantum, and each strand labelled by a phase $\mathrm{e}^{-i(t_i-t_{i-1})}$, the total number giving the total phase change associated to that energy.

Now consider the $U(1)$-stuff operators $V$. Each of these operators has a groupoid whose objects are naturally identified with Feynman diagrams of the sort associated with $V$. These do not affect phases.

Composing the operators together, we get all possible composites of Feynman diagrams of the type associated to $V$, connected by diagrams whose effect is to label strands by phases associated to the time intervals between interactions. To find the total phase associated to such a composite, we multiply all phases. This is clearly equivalent to multiplying the phases on any labelled edges which are joined by the composition to get a phase on the resulting edge, then multiplying the product of all edges thus produced.

The transition amplitude we want to recover is: $$\sum_{n=0}^{\infty} \int_{0 \leq t_1 \leq \dots \leq t_n \leq T} \left\langle{Z^k|O Z^l}\right\rangle$$ The sum taken over all $n$ simply means that we are taking a groupoid containing all possible $n$-fold composites of this form. The integral over all $n$-part partitions of the interval $[0,T]$ means each such diagram contributes a phase found by integrating over all possible ways of dividing the interval into free and interaction parts. This contribution is weighted by the size of the symmetry group, since the inner product inside the integral is just a $U(1)$-groupoid cardinality.

This proves the statement. ◻
:::
:::

This recovers the usual Feynman rules for calculating transition amplitudes in the oscillator.

[^1]: A treatment of the construction of Hilbert spaces from structure types appears in [@maassen].

[^2]: Strictly speaking, the "ground field" here is not $\mathbbm{C}$ but rather the setting for cardinalities of groupoids, $\mathbbm{R}^+$, so we do not yet have a vector space. When we introduce $M$-stuff and get cardinalities in something like $\mathbbm{C}$, we will really have a vectorspace.

[^3]: See appendix [\[sec:slicecategory\]](#sec:slicecategory){reference-type="ref" reference="sec:slicecategory"} for comments about such "over categories". The usual definition applies here by treating $M$ as a set of elements, though we get some extra structure from the monoidal operation on $M$.

[^4]: Since we are already thinking of sets as special kinds of categories here, this raises the question of what happens if we categorify $M$. We return to this in section [\[sec:categorifyingM\]](#sec:categorifyingM){reference-type="ref" reference="sec:categorifyingM"}.
