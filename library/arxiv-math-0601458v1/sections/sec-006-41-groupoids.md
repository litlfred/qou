---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-006-41-groupoids
section_title: "Groupoids"
section_number: 4.1
pages: 14-30
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.983
---
To begin with, we recall what kind of category we are dealing with here:

::: definition
A **groupoid** is a category in which all morphisms are invertible.
:::

A group is a special example of a groupoid, with only one object - then the elemnts of the group correspond to morphisms of the groupoid. Another special case of a groupoid is a groupoid which has only one (identity) morphism per object - such a groupoid is just equivalent to the *set* of its objects. General groupoids are different from either extreme case, since they can have many objects and many morphisms. However, the idea that a set may have a cardinality leads us to try to extend this idea to more general groupoids.

### Groupoid Cardinality

There indeed is a notion of cardinality for any groupoid, which in general can give any positive real number (though it may also be divergent). The notion of cardinality is closely related to the idea of "decategorification". This is a process which takes a category and gives the set of isomorphism classes of objects. Similarly, there is a notion of cardinality which takes a set and gives a number, one which takes a structure type and gives a formal power series, and one which takes a monoidal category and gives a monoid (a category with extra structure producing a set with extra structure).

::: definition
The **groupoid cardinality** of a groupoid $\mathcal{G}$ is $$|\mathcal{G}| = \sum_{[ x ] \in \underline{\mathcal{G}}} \frac{1}{|
     \operatorname{Aut} ( x ) |}$$ where $\underline{\mathcal{G}}$ is the set of isomorphism classes of objects of $\mathcal{G}$. We call a groupoid **tame** if this sum converges.
:::

That is, each isomorphism class of objects of $\mathcal{G}$ contributes a term inversely proportional to the size of the automorphism group of a typical element. Note that groupoid cardinalities of finite groupoids are just positive rational numbers - a finite sum of reciprocals of the sizes of finite groups. However, since a general groupoid may be infinite, its cardinality may be an infinite sum. Thus, groupoid cardinalities can be any nonnegative real number (including infinity). It is worth noting that, as with sets, this idea of cardinality agrees with two natural operations we can perform on groupoids. These are the disjoint union (sum) and product, in the following sense:

::: theorem
If $\mathcal{G}$ and $\mathcal{G'}$ are tame groupoids, then so are $\mathcal{G}+\mathcal{G}'$ and $\mathcal{G} \times \mathcal{G}'$, and we have $| \mathcal{G} + \mathcal{G}' | = | \mathcal{G}
  | + | \mathcal{G}' |$ and $| \mathcal{G} \times \mathcal{G}' | = |
  \mathcal{G} | \times | \mathcal{G}' |$. If $\mathcal{G}$ and $\mathcal{G'}$ are equivalent, $| \mathcal{G} | = | \mathcal{G'} |$.
:::

::: proof
*Proof.* The groupoid $\mathcal{G} + \mathcal{G'}$ is the category whose set of objects is the disjoint union of the sets of objects of $\mathcal{G}$ and $\mathcal{G'}$, and since all morphisms are internal to these groupoids, so is the set of isomorphism classes of objects. So the fact that $|
  \mathcal{G} + \mathcal{G}' | = | \mathcal{G} | + | \mathcal{G}' |$ follows directly from the definition.

The groupoid $\mathcal{G} \times \mathcal{G}'$ has objects which are ordered pairs of objects from $\mathcal{G}$ and $\mathcal{G'}$, and morphisms likewise ordered pairs of morphisms, which are iso precisely when both elements of the pair are iso. So the isomorphism classes of objects are again ordered pairs of isomorphism classes of objects from $\mathcal{G}$ and $\mathcal{G'}$. The automorphism group of any object $( g, g' ) \in
  \mathcal{G} \times \mathcal{G}'$ is the direct product $\operatorname{Aut} ( g )
  \times \operatorname{Aut} ( g' )$, so $$\begin{aligned}
        |\mathcal{G} \times \mathcal{G}' | & = & \sum_{[ ( g, g' ) ] \in
       \mathcal{\underline{G \times \mathcal{G}'}}} \frac{1}{| \operatorname{Aut} ( g,
       g' ) |}\\
        \nonumber & = & \sum_{[ g ] \in \underline{\mathcal{G}}} \sum_{[ g' ] \in
       \underline{\mathcal{G'}}} \frac{1}{| \operatorname{Aut} ( g ) \times \operatorname{Aut}
       ( g' ) |}\\
        \nonumber & = & \left( \sum_{[ g ] \in \underline{\mathcal{G}}} \frac{1}{|
       \operatorname{Aut} ( g ) |} \right) \times \left( \sum_{[ g' ] \in
       \mathcal{\underline{G'}}} \frac{1}{| \operatorname{Aut} ( g' ) |} \right)\\
       \nonumber & = & | \mathcal{G} | \times | \mathcal{G}' |
    
\end{aligned}$$ To see that cardinality is preserved under equivalence, just note that there is a 1-1 correspondence between isomorphism classes of their objects, and equivalent objects have isomorphic automorphism groups, since an equivalence is a full, faithful, and essentially surjective functor. ◻
:::

This allows us to begin to elide the distinction between groupoids and their cardinalities, passing back and forth as convenient (part of the intent of categorification, just as when we conflate $\mathbbm{N}$ and $\boldsymbol{\operatorname{{FinSet_0}}}$).

We can make an analogy with sets here: in a set seen as a category with only identity morphisms, an element of the set is exactly the same as an isomorphism class of objects, so we might think of these classes as "elements" of a groupoid $\mathcal{G}$. In this case, the cardinality function (decategorification) which we have described gives us potentially fractional values for each "element" of a groupoid $\mathcal{G}$, so we can think of a groupoid as a way of getting a "fractional" set - at least from the point of view of this cardinality function. So we can think of a groupoid as an entity whose cardinality is a nonnegative extended real number (given by a possibly infinite sum of positive rationals), and so if a structure type is an entity whose cardinality is a formal power series with natural number coefficients, it should not be too surprising that we can view this structure type as a function which takes a groupoid and produces another groupoid, just as a power series can be evaluated at a real number and yields another real number. Moreover, although groupoid cardinalities can diverge, creating a problem of well-definedness, by passing to the categorified setting, we can eliminate this problem, and deal directly with the groupoids instead. The way we do this is to define $$F ( Z_0 ) = \sum_{n \in \mathbbm{N}} (F_n \times Z_0^n)/\,\!\!/S_n$$ where the sum is interpreted as a coproduct, $F_n$ is the groupoid whose object set is the $n^{\operatorname{th}}$ coefficient of $F$ (as a set of structures) and whose morphisms are as above (the groupoid of $F$-structured finite sets is a direct sum of groupoids $F_n$, of structures whose underlying sets have size $n$). In this definition, $Z_0^n$ is a product of $n$ copies of $Z_0$, and $S_n$ is the permutation group on $n$ elements. The quotient which appears inside the sum (coproduct) is a weak quotient of the groupoid $F_n
\times Z_0^n$ by the group $S_n$. This requires some explanation. First we will describe groupoid-coloured sets, then we will describe the construction of a weak quotient.

### Groupoid-Coloured Sets {#colouredsets}

For any groupoid $Z_0$, we can speak of "$Z_0$-coloured" sets. It is easier to understand what these are if we think of sets as groupoids themselves. In particular, given a set $S$, we can think of it as a groupoid whose objects are the elements of $S$, and the only morphisms present are the identity morphisms (which must exist by definition). This is clearly a groupoid. Then a map from a set into a groupoid is just a functor. So:

::: definition
A **$Z_0$-coloured set** is a set $S$ equipped with a **colouring** map $c:S \rightarrow Z_0$. **Maps of $Z_0$-coloured sets** in $\hom((S,c),(S',c'))$ are bijections $\sigma: S \rightarrow S'$ together with, for each $x \in S$, a morphism $f_x \in \hom(c(x),c'(\sigma(x))$. That is, $$\xymatrix{
    S \ar^{\sigma}[r] \ar_c[d] & S' \ar^{c'}[d] \\
    Z_0 \ar@2{->}[r]_{\{f_x\}} & Z_0
   }$$
:::

We can think of these as sets having each element $x \in S$ "coloured" by an object of $Z_0$, namely its image under the map $f$, which is a functor between two groupoids. The general form of such a thing is shown in ([\[eq:colouredset\]](#eq:colouredset){reference-type="ref" reference="eq:colouredset"}), and an illustration of a coloured set is shown in figure [1](#fig:colouredset){reference-type="ref" reference="fig:colouredset"}.

$$\label{eq:colouredset}
 \xymatrix{
   Z_0 & *+[F-,]{\bullet \dots \bullet} \ar^f[l]
 }$$

<figure id="fig:colouredset">
<div class="center">
<embed src="colouredset.eps" />
</div>
<figcaption><span id="fig:colouredset" label="fig:colouredset"></span>A <span class="math inline"><em>Z</em><sub>0</sub></span>-Coloured Set</figcaption>
</figure>

Morphisms of $Z_0$-coloured sets can be seen as bijections $\alpha$ of the underlying sets where "strands" of the bijections are labelled by morphisms of $Z_0$ between the $Z_0$-objects colouring the elements of $S$ and $S'$ they connect, as shown in figure [2](#fig:colouredsetmap){reference-type="ref" reference="fig:colouredsetmap"}, where all the $g_i$ and $g'_i$ are in $\mathcal{G}$, and $f_i \in \hom(g_i,g'_i)$.

$$\label{eq:colouredsetmap}
  \xymatrix{
    Z_0 \ar@2{->}_{\{f_i\}}[d] & *+[F-,]{\bullet \dots \bullet} \ar^{c}[l] \ar^{\alpha}[d] \\
    Z_0 & *+[F-,]{\bullet \dots \bullet} \ar^{c'}[l] \\
 }$$

<figure id="fig:colouredsetmap">
<div class="center">
<embed src="colsetmap.eps" />
</div>
<figcaption><span id="fig:colouredsetmap" label="fig:colouredsetmap"></span>A Morphism of <span class="math inline">𝒢</span>-Coloured Sets</figcaption>
</figure>

::: theorem
The collection of $Z_0$-coloured finite sets forms the object set of a category $Z_0$-$\boldsymbol{\operatorname{{Set}}}$ whose morphisms are as described. Moreover, $Z_0$-$\boldsymbol{\operatorname{{Set}}}$ is a groupoid.

::: proof
*Proof.* The morphisms described can be composed in the obvious way - composing bijections of the sets, and labelling strands of the result with the composites of the $Z_0$-morphisms labelling each strand: $$\xymatrix{
    S\ar^{\sigma}[r] \ar_{c}[d] \ar@/^1pc/^{\sigma ; \sigma'}[rr] & S'\ar^{\sigma'}[r] \ar_{c'}[d] & S'' \ar_{c''}[d] \\
    Z_0 \ar@2{->}[r]^{\{f_x\}} \ar@2{->}@/_1pc/_{\{f_x;f'_{x'}\}}[rr] & Z_0 \ar@2{->}[r]^{\{f'_x\}} & Z_0 \\
  }$$ This notion of composition is well defined since if the strand $\sigma(x) = x'$ is labelled by $f \in \hom(x,x')$ and $\sigma '(x') =
x''$ by $f' \in
\hom(x',x'')$, the strand in the composite $\sigma '\sigma(x)=x''$ can be labelled by $f'f$ since these are composable. This composition rule inherits all the usual properties (e.g. associativity) from bijections in $\boldsymbol{\operatorname{{Set}}}$ and morphisms in $Z_0$.

The identity morphism from a $Z_0$-coloured set to itself is clearly the morphism with identity bijection whose strands are labelled by identity morphisms on the labels - again, properties of the identity are inherited from $\boldsymbol{\operatorname{{Set}}}$ and $Z_0$. So in fact $Z_0$-$\boldsymbol{\operatorname{{Set}}}$ is a category.

Moreover all morphisms of this kind are invertible, since both bijections $\sigma$ and all morphisms from $Z_0$ labelling strands are invertible (i.e. $Z_0$-$\boldsymbol{\operatorname{{Set}}}$ inherits the property of being a groupoid from the fact that both $Z_0$ and $\boldsymbol{\operatorname{{Set}}}$ are. ◻
:::
:::

In short, $Z_0$-$\boldsymbol{\operatorname{{Set}}}$ is a groupoid of sets labelled by objects of $Z_0$ in a way compatible with the groupoid structure of $Z_0$.

::: remark
In the special case where $Z_0$ is a trivial groupoid with only identity morphisms, (which can be seen as a set) the definition of a morphism reduces to bijections compatible with the colourings, that is $\sigma : S \rightarrow S'$ gives a morphism between the $Z_0$-coloured sets $c : S \rightarrow Z_0$ and $c' : S' \rightarrow
  Z_0$ provided $\phi \circ c' = c$), i.e. that: $$\xymatrix{    
      S\ar_{c}[d]\ar^{\sigma}[r] & S'\ar^{c'}[dl] \\
      Z_0 & \\
    }$$ commutes.

This is an example of an "over category", also known as a "slice" category. See appendix [\[sec:slicecategory\]](#sec:slicecategory){reference-type="ref" reference="sec:slicecategory"} for more comments on this.
:::

Having constructed a groupoid $Z_0$-$\boldsymbol{\operatorname{{Set}}}$ from $Z_0$, it makes sense to ask about its cardinality. However, this is a special case of what we really wish to do: given a stuff type $\Phi$, find the cardinality of $\Phi$-stuffed, $Z_0$-coloured finite sets. In particular, if $\Phi$ is the stuff type (in fact, structure type) "being a finite set", then this is exactly the cardinality of $Z_0$-$\boldsymbol{\operatorname{{Set}}}$. To describe the general case, we need to understand the weak quotient of groupoids by groups, which will account for the effect of the permutations $\sigma$ in the above construction.

### Weak Quotients of Groupoids by Groups

We want to define the weak quotient of any groupoid $\mathcal{G}$ by a group $G$ which acts on it, giving a groupoid $\mathcal{G} / G$. This will be particularly nice in the special case where $\mathcal{G}$ is just a trivial groupoid - i.e. a set $S$, seen as a category - and in this case we can also speak of the quotient of a set by a group, which will be a groupoid $S / G$.

::: definition
A **strict action** of a group $G$ on a category $C$ is a map $A$ which for every $g \in G$ gives a functor $A ( g ) : C \rightarrow C$ such that $A ( g h ) = A ( g ) A ( h )$ and $A ( 1 ) = \operatorname{Id}_C$. If there is such a strict action, then the **strict quotient** of $C$ by $G$ is a category $C / G$ together with a quotient functor $j : C \rightarrow C /
  G$ such that $j \circ A ( g ) = j$ for all $g \in G$.
:::

Clearly, in the special case where $\mathcal{G}$ is a groupoid, so is $\mathcal{G}/\,\!\!/G$, since all morphisms are generated, by composition, from invertible morphisms. Moreover, when $C$ is a trivial groupoid - i.e., a set - the definition of a strict action of $G$ on $C$ is identical to the usual definition of a group action on a set, but when there are nontrivial morphisms, it carries more information because $A(g)$ must be functorial. A strict quotient agrees with the usual intuition of how a quotient should work on objects, in that if there is a group element taking an object $x \in
C$ to $y \in C$, then $j(x)=j(y)$: the objects of $C / G$ are just equivalence classes of objects in $C$ which are equivalent if they lie in the same orbit under the action $A$. Also, the fact that $A$ and $j$ are functorial means that morphisms of $C$ are taken to morphisms of $C / G$ compatibly with composition.

This strict action, and strict quotient, require too much to be very useful. More generally, it is not necessary that $j \circ A ( g )$ actually be equal to $j$, so long as they are isomorphic in a reasonable way.

::: definition
[]{#def:weakquotient label="def:weakquotient"} A **weak quotient** of a category $C$ by a group $G$, acting on $C$ by an action $A$ (as above), is a groupoid $C/\,\!\!/G$ whose objects are objects of $C$. Its morphisms are generated by composition from morphisms in $C$ with morphisms of the form $A(h,g): g \rightarrow g'$, whenever $A(h)(g)=g'$, where $g, g' \in
  C$, $h \in G$. Any relations which hold in $C$ hold in $C/\,\!\!/G$, together with relations: $A(h',g')\circ A(h,g)=
  A(h'h,g)$ whenever $A(h)g=g'$; and $A(h)f \circ A(h,g'') = A(h,g)
  \circ f$ for all $f: g'' \rightarrow g$ (the action $A$ is functorial).
:::

Notice that all the morphisms added by the group action are invertible, since $h \in G$ is invertible. Now we illustrate the weak quotent $C/\,\!\!/G$ showing a few representative morphisms: $$\xymatrix{
  \bullet_{g}\ar@/_3pc/[rrrr]_{A(h,g)} & \bullet_{g''}\ar@/_1pc/[l]^f\ar@/^1pc/[rrr]^{A(h)f \circ A(h,g'') = A(h,g) \circ f} \ar@/_1pc/[r]_{A(h,g'')} & \bullet \ar@/_1pc/[rr]_{A(h)f} & \bullet & \bullet_{g'} \\
 }$$

::: remark
It is possible to describe a weak quotient by means of a (weak) universal property. It will be a groupoid $C /\,\!\!/ G$ together with a quotient functor $j : C \rightarrow C /\,\!\!/ G$ such that there is a natural isomorphism $\tau ( g ) : j \circ A ( g )
\mathop{\longrightarrow}\limits^{\sim} j$ for all $g \in G$. We require that the natural isomporphism satisfy the coherence condition $\tau ( g h ) =
\tau ( g ) \circ \tau ( h )$, and that the weak quotient should be "weakly initial" among all groupoids with these properties. We will not describe this in detail here, however, since we have a concrete construction.
:::

Once we have this concept of the weak quotient of a groupoid by a group, we naturally want to find its groupoid cardinality; this will generally be smaller than $|\mathcal{G}|$ since we have added new isomorphisms, hence potentially increased $|\operatorname{Aut}(x)|$ for some objects $x$. In fact, we have a better result:

::: theorem
The cardinality of the weak quotient of a groupoid $\mathcal{G}$ by a group $G$ satisfies $$|\mathcal{G}/\,\!\!/G| = \frac{|\mathcal{G}|}{|G|}$$

::: proof
*Proof.* We have by definition that $$|\mathcal{G}/\,\!\!/G| = \left( \sum_{[ g ] \in \underline{\mathcal{G}/\,\!\!/G}} \frac{1}{|\operatorname{Aut}(g)|\cdot|\operatorname{Stab}(g)|} \right)$$ where $\operatorname{Stab}(g)$ is the stabilizer subgroup of a representative $g$ in $\mathcal{G}$. This is since the isomorphism classes in $\underline{\mathcal{G}/\,\!\!/G}$ are given by considering the isomorphism classes in $\mathcal{G}$ and identifying any which are related by the action of $G$. For each of these isomorphism classes, the automorphism group consists of transformations taking one equivalent object to another. Any given object $[g]$ in such a class will have as automorphism group the product of the automorphism of a corresponding object in $\mathcal{G}$ with its stabilizer subgroup $\operatorname{Stab}([g])$ in $G$. So each isomorphism class contributes a term $\frac{1}{|\operatorname{Aut}(g)|\cdot|\operatorname{Stab}(g)|}$.

On the other hand, $$\frac{|\mathcal{G}|}{|G|} = \frac{1}{|G|} \sum_{g \in \underline{\mathcal{G}}} \frac{1}{|\operatorname{Aut}(g)|}$$ Here the isomorphism classes are in $\mathcal{G}$: for each isomorphism class in $\mathcal{G}/\,\!\!/G$, there will be $|G|/|\operatorname{Stab}(g)|$ isomorphism classes in $\mathcal{G}$, since each object $g \in \mathcal{G}$ is acted on by each element of $G$ and taken to one of these classes. So in fact this is the same as $|\mathcal{G}/\,\!\!/G|$. ◻
:::
:::

::: remark
It is worth noting what happens in the special case where $\mathcal{G}$ is just a discrete groupoid (i.e. a set, whose groupoid cardinality is just its set cardinality). If the group action happens to be free, this result just says that the number of orbits is the cardinality of the set divided by the size of the group - but the result holds even when the action is not free, as in this picture illustrating a $\mathbb{Z}_2$ action on a 3-element set, giving a groupoid with cardinality $\frac{3}{2}$:

$$\xymatrix{
  \bullet\ar@/^2pc/@{<->}[rr]\ar@(dr,dl)[]^{id} & \bullet\ar@(dr,dl)[]^{id}\ar@{<->}
@(ul,ur)[] & \bullet\ar@(dr,dl)[]^{id} \\
 }$$
:::

## Stuff Types as a Generalization of Structure Types

We are now ready to describe stuff types and some of their properties.

### Stuff Types {#stufftypes}

We have already described *structure types* as functors $$F : \boldsymbol{\operatorname{{FinSet_0}}}\rightarrow \boldsymbol{\operatorname{{Set}}}$$ and also as special functors (in particular, faithful ones) $$\tilde{F} : \boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$$ where $\boldsymbol{\operatorname{{X}}}$ is the groupoid of $F$-structures on finite sets, and the functor $\tilde{F}$ takes each to its underlying set. Faithfulness means that we do not have two distinct morphisms in $\boldsymbol{\operatorname{{X}}}$ with the same image in $\boldsymbol{\operatorname{{FinSet_0}}}$ - that is, that a map between structures is completely determined by its effects on the underlying set. So we say that we have "forgotten structure" - since there may be morphisms in $\boldsymbol{\operatorname{{FinSet_0}}}$ which do not correspond to any in $\boldsymbol{\operatorname{{X}}}$ (because they do not "preserve $F$-structure"). In section [\[sec:forgetful\]](#sec:forgetful){reference-type="ref" reference="sec:forgetful"}, we describe in more detail what is meant by saying that a functor forgets *properties*, *structure*, and *stuff*. For the moment, we extend the notion of structure types, and describe property types, structure types, and stuff types, all of which are functors from some groupoid $\boldsymbol{\operatorname{{X}}}$ to $\boldsymbol{\operatorname{{FinSet_0}}}$ which forget the given sort of information.

::: definition
A **stuff type** is a functor $\Phi : \boldsymbol{\operatorname{{X}}} \rightarrow
  \boldsymbol{\operatorname{{FinSet_0}}}$, where $\boldsymbol{\operatorname{{X}}}$ is a groupoid. If $\Phi$ is faithful but perhaps not full or essentially surjective (forgets structure) we say it is a **structure type**; if it is full and faithful, but perhaps not essentially surjective (forgets properties) it is a **property type**; if it is an equivalence (forgets nothing), it is a **vacuous property type**.
:::

We think of these functors as giving the "underlying sets" of the stuff type in question. We can think of a stuff type $\text{$\Phi : \boldsymbol{\operatorname{{X}}} \rightarrow
\boldsymbol{\operatorname{{FinSet_0}}}$}$ as a "groupoid over $\boldsymbol{\operatorname{{FinSet_0}}}$", so that any object of the groupoid $\boldsymbol{\operatorname{{X}}}$ has an underlying set in $\boldsymbol{\operatorname{{FinSet_0}}}$, and by analogy with the terminology "$F$-structured finite set", we will describe it as a "$\Phi$-stuffed finite set". This should suggest the idea that a stuff type gives us a collection of objects which correspond to finite sets $S$, but which possibly have extra information associated with them (the "stuff" forgotten by $\Phi$).

Returning to our connection with the quantum harmonic oscillator, if we view stuff types this way, and think of the dual entity, $\Phi^{\ast} : \boldsymbol{\operatorname{{FinSet_0}}}\rightarrow \boldsymbol{\operatorname{{Set}}}$, taking each finite set $\boldsymbol{n}$ to the set of ways of putting "$\Phi$-stuff" on it - in this context, this represents the set of ways for a state with energy $n$ to occur in $X$, the groupoid associated with the state (which, however, we just denote $\Phi$).

We can see how this connection develops in two steps. First, we replace a function $\psi :\mathbbm{N} \rightarrow \mathbbm{C}$ function $\psi : \mathbbm{N} \rightarrow \boldsymbol{\operatorname{{Set}}}$: that is, a structure type described as a map giving, for any finite set, the set of all $\Psi$-structures on it. The category of sets takes the role of the complex numbers (in the first stage), which we understand in the following way. The complex values $\psi_n$, which in quantum mechanics represent the "amplitude" for the particular pure state with energy $n$ to occur are replaced in this first stage by sets of $\Psi$-structures on a particular finite set $S$ of size $n$. We can think of these as "the set of ways for possibility $n$ to occur". (In section [\[mstuff\]](#mstuff){reference-type="ref" reference="mstuff"} we will see how amplitudes arise).

The net step is to replace the natural numbers $\mathbbm{N}$ by the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$, so that stuff types get a richer structure - in particular, we can describe them as functors, since $\boldsymbol{\operatorname{{FinSet_0}}}$ is a groupoid rather than merely a set. Now we can think of these in several ways, including as *bundles* over the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$. In this setting, a "point" in the type $\Phi$ is an object of $\boldsymbol{\operatorname{{X}}}$ together with its underlying set - the base point in the bundle. We we can also think of the "point" as a finite set with extra "$\Psi$-stuff", which we depict as a label $x$ attached to $\Psi(x)$. This is illustrated in figure [3](#fig:typeobject){reference-type="ref" reference="fig:typeobject"}.

<figure id="fig:typeobject">
<div class="center">
<embed src="typeobject.eps" />
</div>
<figcaption><span id="fig:typeobject" label="fig:typeobject"></span>Example Object of a Stuff Type <span class="math inline"><em>Ψ</em></span></figcaption>
</figure>

If $\Psi$ is a structure type, this label can be seen as some structure put on the set $\Psi(x)$, but in general this will not be the case - the label could, for example, be other sets in a tuple of which $\Psi(x)$ is one part (this is example [\[st-ex:tuple\]](#st-ex:tuple){reference-type="ref" reference="st-ex:tuple"}). To be general, we will not specify what this label contains, and simply say that it contains "stuff".

A morphism $f$ in $\boldsymbol{\operatorname{{X}}}$ is iso, since $\boldsymbol{\operatorname{{X}}}$ is a groupoid: this gives a bijection $\Psi(f)$ of underlying sets in $\boldsymbol{\operatorname{{FinSet_0}}}$. Together, this data is a morphism in $\Psi$, show generally in ([\[eq:typemorphism\]](#eq:typemorphism){reference-type="ref" reference="eq:typemorphism"}) and illustrated by the example in figure [4](#fig:typemorphism){reference-type="ref" reference="fig:typemorphism"}.

$$\label{eq:typemorphism}
 \xymatrix{
  *+[F-,]{\bullet \dots \bullet}\ar_-{\Psi(f)}^{\wr}[d] & *++[o][F-]{x}\ar_-{f}^{\wr}[d]\ar^-{\Psi}[l] \\
  *+[F-,]{\bullet \dots \bullet} & *++[o][F-]{x'}\ar^-{\Psi}[l] \\
 }$$

<figure id="fig:typemorphism">
<div class="center">
<embed src="typemorphism.eps" />
</div>
<figcaption><span id="fig:typemorphism" label="fig:typemorphism"></span>Morphism In the Groupoid of Stuff Type <span class="math inline"><em>Ψ</em></span></figcaption>
</figure>

::: example
We've seen that the structure type "being a finite set" can be represented as $E^Z$, since there is exactly one way to put this structure on any finite set $S$ (in fact, it is the "vacuous property type"). We might ask if there is a structure type "$E^{E^Z}$" - shorthand for "being a finite set of finite sets". But, in fact, this is impossible. Certainly, this will not have cardinality $\mathrm{e}^{\mathrm{e}^z}$, since there are an infinite number of ways of putting this structure on a given finite set $S$ - that is, taking a finite set of (disjoint) finite sets such that their union is $S$. In particular, any number of copies of the empty set may be in an "$E^{E^Z}$-structure" on $S$. A worse problem is that there are distinct morphisms of such structure, differing only in their effect on these empty sets, which correspond to the same morphism on the underlying set $S$. So these empty sets constitute extra "stuff", and this $E^{E^Z}$ must be a stuff type which is not a structure type.
:::

This example, $E^{E^Z}$, highlights two points which we should address about stuff types. First, it is a special case of something we would like to be able to do more generally, namely given two types $F$ and $G$, to find a type $F \circ G$ which is in some reasonable sense the composite of $F$ and $G$. In this example, both $F$ and $G$ are the vacuuous property type $E^Z$, yet even in this elementary case, their composite already needs to be a stuff type. The second issue is cardinality: our concept of composition should include the fact that when we take cardinalities, we should have that $|F \circ G| = |F|
\circ |G|$. This does not work with the cardinality operation we have developed for structure types - at least when we try to generalize it naively. The stuff type we are optimistically calling $F \circ G =
E^{E^Z}$ is well defined, for any finite set $S$, but the set of these structures has infinite cardinality, so the corresponding generating function is not $\mathrm{e}^{\mathrm{e}^z}$. So we need a new concept of cardinality for stuff types, which should be consistent with the old definition in the special case where they are structure types. We will deal with this issue first.

### Cardinality of Stuff Types

We have said that a stuff type is a groupoid over $\boldsymbol{\operatorname{{FinSet_0}}}$. By analogy with the situation for structure types, then, we can define a notion of cardinality for stuff types. For structure types, we had a notion of cardinality for which $$|F| = \sum_{n \in \underline{\boldsymbol{\operatorname{{FinSet_0}}}}} \frac{|F_n |}{n!} z^n$$ Here, as before, $\underline{\boldsymbol{\operatorname{{FinSet_0}}}}$ is the set of isomorphism classes of $\boldsymbol{\operatorname{{FinSet_0}}}$ (that is, $\mathbbm{N}$), and $|F_n |$ is the cardinality of the set of $F$-structures on $n$ - where this is now the usual cardinality function on sets. The use of a common notation for both cardinality operators emphasizes that any notion of cardinality $| \cdot |$ is in some sense a decategorification operation. For simplicity, we will replace $\underline{\boldsymbol{\operatorname{{FinSet_0}}}}$ with $\mathbbm{N}$, but we should remember that it derives from the original groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$.

In the same way, we can define the cardinality of a stuff type:

::: definition
[]{#def:stuffcard label="def:stuffcard"} Given a stuff type $\text{$\Phi : \boldsymbol{\operatorname{{X}}} \rightarrow
  \boldsymbol{\operatorname{{FinSet_0}}}$}$, we define its cardinality by $$| \Phi | = \sum_{n \in \underline{\mathbbm{N}}} | \Phi_n |z^n$$ where $|\Phi_n|$ is the *groupoid cardinality* of the preimage of $n$ under $\Phi$.
:::

::: remark
Note that this really only makes sense if we are working with a "skeletal" version of $\boldsymbol{\operatorname{{FinSet_0}}}$, so that the preimage of a set of size $n$ is well defined. This is a category which is equivalent as a category to the standard version of $\boldsymbol{\operatorname{{FinSet_0}}}$ from set theory - that is, there are functors between them whose composites are naturally isomorphic to the identities. However, the skeletal version of $\boldsymbol{\operatorname{{FinSet_0}}}$ has only one object per isomorphism class - that is, per finite cardinal number. We will assume $\boldsymbol{\operatorname{{FinSet_0}}}$ is skeletal whenever convenient.
:::

::: remark
Definition ([\[def:stuffcard\]](#def:stuffcard){reference-type="ref" reference="def:stuffcard"}) is consistent with the definition of structure types, since if we think of a structure type as a groupoid over $\boldsymbol{\operatorname{{FinSet_0}}}$, its morphisms all arise from permutations of the underlying sets, and so the groupoid cardinality of the preimage of $n$ is precisely $| \Phi_n | / n!$, since the groupoid is equivalent to the weak quotient $\Phi_n /\,\!\!/ S_n$. Just as structure types had cardinalities which were power series whose $n^{\operatorname{th}}$ coefficients were integers divided by $n!$, stuff types have cardinalities which are power series with nonnegative real coefficients.
:::

An example shows that stuff types significantly generalize structure types, at least as concerns the kinds of generating functions (power series) which can appear as their cardinalities:

::: example
The stuff type "being the first of a $k$-tuple of equal-sized finite sets", for any value $k > 1$, is a stuff type which is not a structure type. This can be represented as a functor $\Phi : \boldsymbol{\operatorname{{X}}}
  \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, where $\boldsymbol{\operatorname{{X}}}$ is the groupoid whose objects are $k$-tuples of finite sets of the same size, and whose morphisms are $k$-tuples of bijections. The components of $\boldsymbol{\operatorname{{X}}}$ are $X_n$, which are the groupoids of $k$-tuples of $n$-element sets. The cardinality of $\Phi$ is $$\begin{aligned}
     | \Phi | & = & \sum_{n \in \mathbbm{N}} |X_n |z^n\\
     \nonumber & = & \sum_{n \in \mathbbm{N}} | 1 /\,\!\!/ S_n |^k z^n\\
     \nonumber & = & \sum_{n \in \mathbbm{N}} \left( \frac{1}{n!} \right)^k z^n
  
\end{aligned}$$ This cardinality cannot appear as that of any structure type, since the coefficients of $z^n$ in such power series must be of the form $\frac{a_n}{n!}$ for $a_n \in \mathbbm{N}$, which is not the case here unless $k = 1$.
:::

## Stuff Types As Power Series

Once we have the mechanics of groupoids, stuff types, and their cardinalities, it becomes possible to extend the analogy with formal power series which began structure types. Although for the purposes of quantum mechanics, we are mainly interested in the *Hilbert space* structure of formal power series, it is worth pointing out that more of the algebraic and arithmetical properties of power series can also be recovered. In particular, we will next see that the cardinality maps for stuff types and groupoids lets us find analogs of the evaluation of a power series at a real number - and, by extension, the composition of two power series. These could not, in general, be done with just structure types.

In section [\[stuff-quantum-sec\]](#stuff-quantum-sec){reference-type="ref" reference="stuff-quantum-sec"} we return to features specially relevant to quantum mechanics.

### Evaluation of Stuff Types

One useful fact about stuff types is that we can define a sensible notion of evaluation, which brings us back to the fact that we had two ways of looking at power series as functions: either by the evaluation map $z \mapsto f ( z )$ or by the map picking out coefficients in the power series expansion, $n \mapsto f_n$. Structure types have given us a good categorified way of looking at the latter, but with stuff types we will be able to do the former as well. This also lets us talk sensibly about the composition of types, just as we might talk about composition of functions. Since this is one motivation for passing from structure types to stuff types, let's consider an example of an algebraic operation with power series which can't be extended to the setting of structure types in a way which is compatible with the correspondence between structure types and power series:

This example of a stuff type suggests the way we speak of evaluating stuff types at groupoids - by "colouring" elements of a set with objects of the groupoid. That is:

::: definition
Given a groupoid $Z_0$ and a stuff type $\Phi : \boldsymbol{\operatorname{{X}}}
  \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, the **evaluation of $\Phi$ at $Z_0$**. is the groupoid $\Phi ( Z_0 )$ of $\Phi$-stuffed, $Z_0$-coloured finite sets, whose objects are pairs $( \phi, z_0 ) \in \Phi_n \times
  Z_0^n$, where $\phi$ is a way of equipping an $n$-element set with $\Phi$-stuff, and $z_0$ is a map $f : n \mathop{\rightarrow}\limits Z_0$ equipping each element of $n$ with an object of $Z_0$. The morphisms of $\Phi ( Z_0 )$ are bijections of the underlying $n$-element sets with strands labelled by morphisms in $Z_0$ between the objects labelling corresponding elements.
:::

Notice that there is an action of $S_n$ on the objects of $\Phi ( Z_0
)_n$ - the ways of putting $\Phi$-stuff on a set of size $n$, together with a $Z_0$-colouring of this set - which comes immediately from the action of $S_n$ on the underlying set.

In the case where $\Phi$ is a structure type $F$, the groupoid $F(Z_0)_n$ is just a weak quotient $(F_n \times Z_0^n) /\,\!\!/ S_n$. That is, its objects consist of pairs: $F$-structures which can be put on an $n$-element set, together with colourings of an $n$-element set by $Z_0$ objects. These have an action of the permutation group on the underlying set (two such objects are isomorphic by reindexing the sets in in the $F$-structure and the colouring in the same way). So then the groupoid cardinality of $F(Z_0)$ is $$| \sum_{n = 0}^\infty (F_n \times Z_0^n) /\,\!\!/ S_n | = \sum_{n=0}^\infty \frac{|F_n| |Z_0|^n}{n!} = |F|(|Z_0|)$$ where the first "sum" is a categorical coproduct. This formula is consistent with the formula for the generating function of a structure type which we've seen before in equation ([\[eq:strtypecard\]](#eq:strtypecard){reference-type="ref" reference="eq:strtypecard"}). The analogous fact is true for any stuff type, though recall that in that case we will not explicitly refer to the action of $S_n$ on the groupoid. However, just as above, we have $$| \Phi(Z_0) | = |\Phi|(|Z_0|)$$

::: example
[]{#ex:compcolour label="ex:compcolour"} Take a groupoid $\mathcal{G}$, and say $\boldsymbol{\operatorname{{X}}}$ is the groupoid of $\mathcal{G}$-coloured finite sets, and consider this groupoid as the stuff type $$\Phi : \boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$$ where $\Phi$ is the forgetful functor which takes a $\mathcal{G}$-coloured finite set to its underlying set. An object in $X_n$ (the preimage of $n$ in $\boldsymbol{\operatorname{{X}}}$) consists of $n$ objects from $\mathcal{G}$, and morphisms of $X_n$ are $n$-tuples of morphisms in $\mathcal{G}$ composed with permutations of the $n$ elements. Thus, $X_n \simeq
  G_0^n / S_n$, the weak quotient by the action we have described. Taking its cardinality, we find that $$\begin{aligned}
\label{eq:compcolour}
     |\Phi| & = & \sum_{n \in \mathbbm{N}} |X_n |z^n\\
     \nonumber & = & \sum_{n \in \mathbbm{N}} | {\mathcal{G}^n}/\,\!\!/{S_n}
     | z^n\\
     \nonumber & = & \sum_{n \in \mathbbm{N}} \frac{|\mathcal{G}|^n}{n!} z^n\\
     \nonumber & = & \mathrm{e}^{| \mathcal{G} |z}
  
\end{aligned}$$ This follows since groupoid cardinalities are compatible with both powers and weak quotients.

Both the parallel with the generating function $\mathrm{e}^{|
  \mathcal{G} |z}$ and the notion that $F$ is the type of "$\mathcal{G}$-coloured finite sets" suggests that it makes sense $F$ should be seen as $E^{\mathcal{G} \times Z}$ - that is, composition of the type $E^{\Box}$ ("finite sets of") with $\mathcal{G} \times Z$ (the product type whose objects are one-element sets together with objects of $\mathcal{G}$ - i.e. $\mathcal{G}$-coloured one-element sets).

Some interesting special cases of this example: when $\mathcal{G}$ is a groupoid which is just a set $k$ with only identity morphisms, we have a *structure type* of "$k$-coloured finite sets"; $\mathcal{G}$ is a group $G$ seen as a one-object groupoid, we have a notion of $(1/\,\!\!/G)$-coloured sets.

Furthermore, the calculation above gives us the cardinality of the groupoid $\boldsymbol{\operatorname{{X}}}$ of $\mathcal{G}$-colored finite sets itself (i.e. not as a stuff type) to be simply $\mathrm{e}^{|\mathcal{G}|}$ (since no powers of $z$ appear, but the calculation is otherwise the same). So we can see this groupoid as the evaluation of $E^{\Box}$ at $\mathcal{G}$.
:::

### Composition of Stuff Types

At last we can return to the question of how to compose stuff types. We have seen how to evaluate stuff types at groupoids - given a groupoid $Z_0$, evaluating the stuff type $\Phi$ at it gives $\Phi(Z_0)$, the groupoid of "$\Phi$-stuffed $Z_0$-coloured finite sets". Since evaluating a stuff type at a groupoid (whose cardinality is a real number) yields another groupoid (whose cardinality is again a real number), we should be able to repeat this process as many times as we like. In principle, for instance, we should be able to describe $\Psi \circ \Phi ( Z_0 )$ as "$\Psi$-stuffed, $\Phi ( Z_0 )$-coloured finite sets" - a set with $G$-stuff, whose elements are labelled by finite sets with $F$-stuff and elements labelled with objects of $Z_0$.

Since a stuff type $\Phi$ is itself a groupoid over finite sets, $\Phi
: \boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, and we have a way of evaluating a stuff type at a groupoid, we get a notion of composition for stuff-types. We have seen in section [0.0.2](#colouredsets){reference-type="ref" reference="colouredsets"} that there is a groupoid of $Z_0$-coloured finite sets, whose morphisms are bijections of sets with strands labelled by morphisms in $Z_0$. We saw in ([\[ex:compcolour\]](#ex:compcolour){reference-type="ref" reference="ex:compcolour"}) that its cardinality is $\mathrm{e}^{|Z_0|}$.

We should think of this as an illustration of the above where $F$ is the structure type, in which we had the stuff type "being a finite set" composed with the type $Z_0 \times Z$ - $Z_0$-coloured one-element sets, but we can generalize this to any stuff types $F$ and $G$, to obtain stuff types $F \circ G = F ( G )$ and in such a way that $|F \circ G| = |F| \circ |G|$.

<figure id="fig:compositetypeobject">
<div class="center">
<embed src="compositetypeobject.eps" />
</div>
<figcaption><span id="fig:compositetypeobject" label="fig:compositetypeobject"></span>An Object in a Composite Stuff Type</figcaption>
</figure>

We can describe what we get here as a type which, evaluated at $Z_0$, gives "$F$-stuffed $G(Z_0)$-labelled finite sets". This has objects (as shown in figure [5](#fig:compositetypeobject){reference-type="ref" reference="fig:compositetypeobject"}) which consist of finite sets equipped with $F$-stuff (say $F: \boldsymbol{\operatorname{{X}}} \rightarrow S$). The elements of $F$ are labelled by objects of $G(Z_0)$: that is, the labels themselves consist of finite sets labelled with $G$-stuff, denoted by capital letters in the figure, whose elements are themselves labelled in turn by objects from $Z_0$, denoted by lower-case letters.

<figure id="fig:compositetypemorphism">
<div class="center">
<embed src="compositetypemorphism.eps" />
</div>
<figcaption><span id="fig:compositetypemorphism" label="fig:compositetypemorphism"></span>A Morphism in a Composite Stuff Type</figcaption>
</figure>

Morphisms in the groupoid of $F$-stuffed $G(Z_0)$-coloured finite sets (illustrated in figure [6](#fig:compositetypemorphism){reference-type="ref" reference="fig:compositetypemorphism"}) consist of maps between the objects of $F$'s groupoid of stuff, which project down to morphisms of the underlying $G(Z_0)$-coloured sets. This has its top level as a bijection of the underlying sets. The strands of the top-level bijection are labelled by morphisms of the groupoid of $G(Z_0)$-coloured finite sets. These include morphisms of the objects associated to the $G$-stuffed $Z_0$-coloured sets (the dotted lines), which are associated to bijections of the $Z_0$-coloured sets - with strands labelled by morphisms of $Z_0$.

Clearly, we could in principle continue this sort of construction recursively, to define the composite of any number of stuff types.

## Forgetful Functors: Properties, Structure, and Stuff[]{#sec:forgetful label="sec:forgetful"}

Here we take a detour through some ideas from category theory which apply directly to stuff types. The first is a classification of functors by degrees of forgetfulness, which is the source of the term "stuff" in "stuff type". In fact, we want to explain the terms "structure" and "stuff" which appear before the word "type" in our terminology. We began by trying to categorify a certain rigs, replacing it by a 2-rig of functors - and now we look at a classification of functors to see how we generalized this process. In particular, we are interested in functors which are, respectively: faithful; full and faithful; or full and faithful and essentially surjective:

::: definition
A functor $F : \mathcal{C} \rightarrow \mathcal{D}$ is ***essentially surjective*** if the images of objects in $\mathcal{C}$ cover all objects of $\mathcal{D}$ in the sense that for any $d \in \operatorname{Ob} ( \mathcal{D} )$, there is some $c \in
  \mathcal{C}$ with $F(c) \cong d$. It is ***full*** if for any $c, c' \in \mathcal{C}$, the map between the sets of morphisms, $F : \operatorname{Hom}_{\mathcal{C}} ( c, c' ) \rightarrow
  \operatorname{Hom}_{\mathcal{D}} (F(c), F(c'))$, is surjective (in the set-theoretic sense). The functor $F$ is ***faithful*** if for morphisms in its image, $F(f), F(f') \in
  \operatorname{Hom}_{\mathcal{D}} (F(c), F(c'))$, we have $F(f) = F(f')
  \Rightarrow f = f' \operatorname{in} \operatorname{Hom}_{\mathcal{C}} (c,c')$.
:::

Each of these can be seen as a form of surjectivity. The notion of essential surjectivity is a version of *onto* for categories at the level of objects. Fullness means that a functor is "*onto* for morphisms"; faithfulness is "*onto* for equations between morphisms" in the sense that any equation between morphisms in $\operatorname{Hom}_{\mathcal{D}} ( F ( c ), F
( c' ) )$ comes from some equation between the preimage morphisms in $\operatorname{Hom}_{\mathcal{C}} ( c, c' )$.

We have a classification of functors, then, by which of these it satisfies (which we will attempt to explain next):

::: center
                **Functor**                 **Forgets**
  ---------------------------------------- --------------
   essentially surjective, full, faithful    "nothing"
               full, faithful               "properties"
                  faithful                  "structure"
                    all                       "stuff"
:::

When we move to the setting of $n$-categories, we have not only objects and morphisms, and the possibility that morphisms may be equal, but also 2-morphisms between morphisms (so that they may be 2-isomorphic, rather than merely equal, or indeed might have non-iso 2-morphisms between them), and 3-morphisms between 2-morphisms, and so on. Important to notice is that essential surjectivity involves a weakening (a functor is essentially surjective if it is surjective onto isomorphism classes, but not necessarily objects). This is because we should not distinguish between equivalent categories, and since every category is equivalent to a skeletal category with only one object in each equivalence class. We will, in fact, want similarly weakened versions of *full*, *faithful*, and their higher-dimensional counterparts, when we use $n$-categories.

For now, though, we will explain the second column of this table, and see how it applies to structure types. The intuition begins with the commonplace fact that a map between sets is an isomorphism if it is both injective and surjective. For functors between categories, essential surjectivity is the natural analog of surjectivity, but *full* functors are the natural analogs of injective maps. A map is injective if no two distinct objects have the same image - that is, any equation of objects in the image comes from an equation in the domain. A functor is full if every morphism between objects in the image comes from a morphism in the domain, so injectivity of set maps is a special case, considering a set as a category with only identity morphisms. In this trivial sort of category, every functor is faithful.

So a bijection between sets is a full, faithful, essentially surjective functor, and if such a functor exists, we should treat the sets as "the same" - the functor has lost no important information (of which there is very little, for a set), which is reflected in the fact that it is invertible. If we have more general categories, with nontrivial morphisms, then in much the same way, we have that a functor $F : \mathcal{C \rightarrow \text{D}}$, is an equivalence of $\mathcal{C}$ and $\mathcal{D}$ (i.e. there is a functor $F^{-
1}$ which is an inverse to $F$ up to natural isomorphism) if $F$ is full, faithful, and essentially surjective. Similar results are true for higher-dimensional categories ($n$-categories, for any $n$), while functors which fail to have these properties are in various senses "forgetful" - not being equivalences, they must forget information about the source category. This gives a "periodic table" of grades of "stuff" forgotten by functors which fail to be onto for objects, morphisms, 2-morphisms (between morphisms), 3-morphisms (between 2-morphisms), and so on. We restrict our attention to the case $n = 1$, but note that the pattern we will develop continues for higher $n$.

We see that these classes of functor can be used to talk about classes of "type": structure types and stuff types are functors from groupoids into the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$ - in fact, they are functors which forget "structure" and "stuff" respectively.

### Examples of Forgetful Functors

Some examples illustrate the classes of functors we have described. So for instance, if a functor $F : \mathcal{C} \rightarrow \mathcal{D}$ is not essentially surjective, but is full and faithful, we have a subcategory of $\mathcal{C}$ in $\mathcal{D}$, namely the image of $F$, which is equivalent to $\mathcal{C}$, but which does not exhaust the isomorphism classes of $\mathcal{D}$:

::: example
The functor $$I : \boldsymbol{\operatorname{{AbGrp}}} \rightarrow \boldsymbol{\operatorname{{Grp}}}$$ embeds the category of abelian groups and their homomorphisms into the category of all groups and homomorphisms. This functor has "forgotten a property", namely the property of being Abelian. The category $\boldsymbol{\operatorname{{Grp}}}$ does not discriminate between objects with and without this property, whereas $\boldsymbol{\operatorname{{AbGrp}}}$ is distinguished by the fact that it does.
:::

If a functor fails to be essentially surjective *and* fails to be full, we can have not only the sort of situation above, but the target category can have morphisms which do not correspond to those in the source:

::: example
The functor $$I : \boldsymbol{\operatorname{{OrdFinSet_0}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$$ takes any element in the groupoid $\boldsymbol{\operatorname{{OrdFinSet_0}}}$ of totally ordered finite sets (whose morphisms are order-preserving bijections) into $\boldsymbol{\operatorname{{FinSet_0}}}$ - taking ordered sets and order-preserving maps to the underlying sets and set-maps. This fails to be full since there can be bijections between the underlying sets of two ordered sets which fail to preserve order. This functor "forgets structure" - namely, that structure which must be preserved by morphisms in $\boldsymbol{\operatorname{{OrdFinSet_0}}}$, the total ordering on its objects.
:::

Both of these examples are faithful functors, in the sense that each morphism in the source category is sent to a distinct morphism in the target. There are functors which lack this property as well:

::: example
Consider the functor: $$P_1 : \boldsymbol{\operatorname{{Vect^2}}} \rightarrow
  \boldsymbol{\operatorname{{Vect}}}$$ The objects and morphisms in $\boldsymbol{\operatorname{{Vect^2}}}$ are ordered pairs of those in $\boldsymbol{\operatorname{{Vect}}}$, namely vector spaces and linear transformations between them, while the functor $P_1$ is just projection onto the first component of these pairs. Clearly, this is not faithful, since there are many pairs morphisms in $\boldsymbol{\operatorname{{Vect^2}}}$ with the same first component. What this functor has "forgotten" is, for each object, an entire vector space, and all the information about morphisms associated to these. More than simply forgetting about properties shared by all objects, or structure which must be preserved by morphisms, we say this functor forgets "stuff" - parts of objects, in this case.
:::

::: example
[]{#st-ex:tuple label="st-ex:tuple"}Our previous example of a completely forgetful functor involved the category of vector spaces, but similarly, there is an obvious class of stuff types associated to the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}^n$, whose objects and morphisms are $n$-tuples of finite sets and bijections: $$P_j : \boldsymbol{\operatorname{{FinSet_0}}}^n \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$$ where $P_j$ is the projection onto the $j^{\operatorname{th}}$ coordinate. The set in this entry is the "underlying set", and the "stuff" being forgotten consists of all the other sets in the tuple. This stuff type is a completely forgetful functor.
:::
