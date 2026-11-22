---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-008-42-stuff-types-as-a-generalization-of-structure
section_title: "Stuff Types as a Generalization of Structure Types"
section_number: 4.2
pages: 20-24
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.981
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
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

The net step is to replace the natural numbers $\mathbbm{N}$ by the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$, so that stuff types get a richer structure - in particular, we can describe them as functors, since $\boldsymbol{\operatorname{{FinSet_0}}}$ is a groupoid rather than merely a set. Now we can think of these in several ways, including as *bundles* over the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$. In this setting, a "point" in the type $\Phi$ is an object of $\boldsymbol{\operatorname{{X}}}$ together with its underlying set - the base point in the bundle. We we can also think of the "point" as a finite set with extra "$\Psi$-stuff", which we depict as a label $x$ attached to $\Psi(x)$. This is illustrated in figure [1](#fig:typeobject){reference-type="ref" reference="fig:typeobject"}.

<figure id="fig:typeobject">
<div class="center">
<embed src="typeobject.eps" />
</div>
<figcaption><span id="fig:typeobject" label="fig:typeobject"></span>Example Object of a Stuff Type <span class="math inline"><em>Ψ</em></span></figcaption>
</figure>

If $\Psi$ is a structure type, this label can be seen as some structure put on the set $\Psi(x)$, but in general this will not be the case - the label could, for example, be other sets in a tuple of which $\Psi(x)$ is one part (this is example [\[st-ex:tuple\]](#st-ex:tuple){reference-type="ref" reference="st-ex:tuple"}). To be general, we will not specify what this label contains, and simply say that it contains "stuff".

A morphism $f$ in $\boldsymbol{\operatorname{{X}}}$ is iso, since $\boldsymbol{\operatorname{{X}}}$ is a groupoid: this gives a bijection $\Psi(f)$ of underlying sets in $\boldsymbol{\operatorname{{FinSet_0}}}$. Together, this data is a morphism in $\Psi$, show generally in ([\[eq:typemorphism\]](#eq:typemorphism){reference-type="ref" reference="eq:typemorphism"}) and illustrated by the example in figure [2](#fig:typemorphism){reference-type="ref" reference="fig:typemorphism"}.

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
