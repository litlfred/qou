---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-007-41-groupoids
section_title: "Groupoids"
section_number: 4.1
pages: 14-20
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.984
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
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
