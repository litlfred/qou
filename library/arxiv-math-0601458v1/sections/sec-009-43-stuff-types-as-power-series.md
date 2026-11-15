---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-009-43-stuff-types-as-power-series
section_title: "Stuff Types As Power Series"
section_number: 4.3
pages: 24-27
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.988
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
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
: \boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, and we have a way of evaluating a stuff type at a groupoid, we get a notion of composition for stuff-types. We have seen in section [\[colouredsets\]](#colouredsets){reference-type="ref" reference="colouredsets"} that there is a groupoid of $Z_0$-coloured finite sets, whose morphisms are bijections of sets with strands labelled by morphisms in $Z_0$. We saw in ([\[ex:compcolour\]](#ex:compcolour){reference-type="ref" reference="ex:compcolour"}) that its cardinality is $\mathrm{e}^{|Z_0|}$.

We should think of this as an illustration of the above where $F$ is the structure type, in which we had the stuff type "being a finite set" composed with the type $Z_0 \times Z$ - $Z_0$-coloured one-element sets, but we can generalize this to any stuff types $F$ and $G$, to obtain stuff types $F \circ G = F ( G )$ and in such a way that $|F \circ G| = |F| \circ |G|$.

<figure id="fig:compositetypeobject">
<div class="center">
<embed src="compositetypeobject.eps" />
</div>
<figcaption><span id="fig:compositetypeobject" label="fig:compositetypeobject"></span>An Object in a Composite Stuff Type</figcaption>
</figure>

We can describe what we get here as a type which, evaluated at $Z_0$, gives "$F$-stuffed $G(Z_0)$-labelled finite sets". This has objects (as shown in figure [1](#fig:compositetypeobject){reference-type="ref" reference="fig:compositetypeobject"}) which consist of finite sets equipped with $F$-stuff (say $F: \boldsymbol{\operatorname{{X}}} \rightarrow S$). The elements of $F$ are labelled by objects of $G(Z_0)$: that is, the labels themselves consist of finite sets labelled with $G$-stuff, denoted by capital letters in the figure, whose elements are themselves labelled in turn by objects from $Z_0$, denoted by lower-case letters.

<figure id="fig:compositetypemorphism">
<div class="center">
<embed src="compositetypemorphism.eps" />
</div>
<figcaption><span id="fig:compositetypemorphism" label="fig:compositetypemorphism"></span>A Morphism in a Composite Stuff Type</figcaption>
</figure>

Morphisms in the groupoid of $F$-stuffed $G(Z_0)$-coloured finite sets (illustrated in figure [2](#fig:compositetypemorphism){reference-type="ref" reference="fig:compositetypemorphism"}) consist of maps between the objects of $F$'s groupoid of stuff, which project down to morphisms of the underlying $G(Z_0)$-coloured sets. This has its top level as a bijection of the underlying sets. The strands of the top-level bijection are labelled by morphisms of the groupoid of $G(Z_0)$-coloured finite sets. These include morphisms of the objects associated to the $G$-stuffed $Z_0$-coloured sets (the dotted lines), which are associated to bijections of the $Z_0$-coloured sets - with strands labelled by morphisms of $Z_0$.

Clearly, we could in principle continue this sort of construction recursively, to define the composite of any number of stuff types.
