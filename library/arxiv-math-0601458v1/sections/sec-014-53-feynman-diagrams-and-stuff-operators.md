---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-014-53-feynman-diagrams-and-stuff-operators
section_title: "Feynman Diagrams and Stuff Operators"
section_number: 5.3
pages: 38-43
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.601
latex_coverage_ratio: 0.987
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
[]{#sec:feynman label="sec:feynman"}

From a quantum mechanical point of view, we are often interested in finding inner products such as $\left\langle{ \Phi, T \Psi }\right\rangle$, and finding these inner products can be done by means of Feynman diagrams. That is, in QM, the "transition amplitude" between states $\Phi$ and $T
\Psi$ is a sum of amplitudes associated to Feynman diagrams, each showing one possible way of getting from state $\Phi$ to state $\Psi$ by process $T$. We will show how this idea can be recovered in the categorified setting, and in fact is given by exactly the algebraic ideas we have defined. In general, the groupoid $\left\langle{ \Phi, T \Psi
}\right\rangle$ has objects as shown in figure [1](#fig:stuffopinprodobject){reference-type="ref" reference="fig:stuffopinprodobject"}

<figure id="fig:stuffopinprodobject">
<div class="center">
<embed src="stuffopinprodobject.eps" />
</div>
<figcaption><span id="fig:stuffopinprodobject" label="fig:stuffopinprodobject"></span>Object of Groupoid <span class="math inline">⟨<em>Ψ</em>,<em>T</em><em>Φ</em>⟩</span></figcaption>
</figure>

We will see that we can think of these as Feynman diagrams, and finding the sum over their amplitudes is exactly the process of taking the groupoid cardinality of this inner product of stuff types - that is, a sum over Feynman diagrams of some "amplitudes". At the moment, these amplitudes are all positive reals, rather than complex numbers as is usual in quantum mechanics. When we discuss $M$-stuff types in section [1](#mstuff){reference-type="ref" reference="mstuff"}, and in particular the case $M = U(1)$ in section [\[mstuffu1\]](#mstuffu1){reference-type="ref" reference="mstuffu1"}, we will see how this can be resolved by introducing the quantum mechanical notion of *phase*.

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

From the parallel with Fock space, one operator we should want to define is the *field operator* $A + A^{\ast}$. As a stuff operator, this behaves as one might expect: the groupoid in the stuff operator is just the groupoid sum $T + T^{\ast}$ (i.e. two copies of $\boldsymbol{\operatorname{{FinSet_0}}}$), and the projections just act as the projections on $T$ and $T^{\ast}$ when applied to objects and morphisms from each of the two copies. So, the objects of the groupoid $\Phi$, following the pattern we illustrated in ([\[eq:stuffopobject\]](#eq:stuffopobject){reference-type="ref" reference="eq:stuffopobject"}), look like either objects of $A$ or of $A^{\ast}$, as shown in figure [2](#fig:fieldoperatorobject){reference-type="ref" reference="fig:fieldoperatorobject"}.

<figure id="fig:fieldoperatorobject">
<div class="center">
<embed src="fieldoperator.eps" />
</div>
<figcaption><span id="fig:fieldoperatorobject" label="fig:fieldoperatorobject"></span>Example Objects in the Categorified Field Operator</figcaption>
</figure>

In our categorified setting, this is written nearly the same way, $\left\langle{Z^n,\Phi^k Z^m}\right\rangle$, but we now have an interpretation of the inner product as a groupoid over $\boldsymbol{\operatorname{{FinSet_0}}}$, obtained by a pullback - and indeed, of the stuff operator $\Phi^k$ as a composite of stuff operators, etc. Now, this $\Phi^k$ has objects which are chains of objects of the form in figure [2](#fig:fieldoperatorobject){reference-type="ref" reference="fig:fieldoperatorobject"}, composed as in figure [\[fig:stuffopcomposition\]](#fig:stuffopcomposition){reference-type="ref" reference="fig:stuffopcomposition"}. We can draw these in various ways (different drawing styles form objects in equivalent categories), but for compactness, we will draw these in a style which omits the "internal" bijections of the composite type, and also the bijections from the $A$ and $A^{\ast}$ objects of $\Phi$ to $\boldsymbol{\operatorname{{FinSet_0}}}$. Thus, each internal finite set would have previously been drawn three times, with bijections between them. This compact style is illustrated in figure [3](#fig:phi-n){reference-type="ref" reference="fig:phi-n"}, which shows an object of $\Phi^4$. This one shows an object made from one annihilation and three creation operators, in that order. All other permutations of four $\Phi$-objects are possible also.

<figure id="fig:phi-n">
<div class="center">
<embed src="phi-n.eps" />
</div>
<figcaption><span id="fig:phi-n" label="fig:phi-n"></span>Example Object From <span class="math inline"><em>Φ</em><sup>4</sup></span></figcaption>
</figure>

For the sake of further compactness (and another drawing style depicting an equivalent category), note that what we really have here is an operation in which $k$ quanta of energy either appear or disappear, and do so in a definite order. We could really draw this with just a single "interaction" vertex, incident with $k$ strands (all other strands passing straight through the diagram, matching up a quantum in the top with a quantum in the bottom). These incidences would have to be labelled with a total ordering, so that the object shown in figure [3](#fig:phi-n){reference-type="ref" reference="fig:phi-n"} would be drawn as in figure [4](#fig:field4oplabelled){reference-type="ref" reference="fig:field4oplabelled"}.

<figure id="fig:field4oplabelled">
<div class="center">
<embed src="field4oplabelled.eps" />
</div>
<figcaption><span id="fig:field4oplabelled" label="fig:field4oplabelled"></span>Example Object From <span class="math inline"><em>Φ</em><sup>4</sup></span> (Alternate Style)</figcaption>
</figure>

There is an action of the permutation group $S_k$ on these objects, changing the order in which we encounter objects from $A$ and $A^{\ast}$ as we pass through $\Phi^k$. That is, for every object we get whose diagram has one order labelling the incidences, we will get objects with all other possible orders exactly once through the action of the permutation group $S_k$, also known as $k!$. So if we want to omit this labelling for clarity in the drawings, we can do so as long as we remember that this means we are really drawing objects of the weak quotient $\Phi^k /\,\!\!/ S_k$ (weak quotients are defined in definition [\[def:weakquotient\]](#def:weakquotient){reference-type="ref" reference="def:weakquotient"}). The objects of this weak quotient are isomorphism classes of diagrams under permutations of labellings. These permutations give the natural isomorphisms in the definition of weak quotient by taking any labelled diagram to the same diagram with permuted labels. In this new category, the cardinality of the groupoid is thus scaled by $\frac{1}{k!}$. We also need to keep in mind that an unlabelled diagram really stands in for possibly several different inequivalent labellings of the incidences by distinct orderings.

All this is really a notational convenience: really, to calculate transition amplitude between states $\psi$ and $\phi$ for which we have a description as stuff types $\Psi$ and $\Phi$, when we put the system through some process $t$ which we describe as a stuff operator $T$, we only need to find the groupoid cardinality $|\left\langle{\Psi,T\Phi}\right\rangle|$. Simplifying diagrams and finding convenient conventions for labelling them is really a way for getting a calculational convenience out of diagrams like figure [5](#fig:field4op){reference-type="ref" reference="fig:field4op"}, which shows an object from the groupoid $\Phi^4
/\,\!\!/ S_4$.

<figure id="fig:field4op">
<div class="center">
<embed src="field4op.eps" />
</div>
<figcaption><span id="fig:field4op" label="fig:field4op"></span>Example Object in <span class="math inline"><em>Φ</em><sup>4</sup>/   /<em>S</em><sub>4</sub></span></figcaption>
</figure>

Now, diagrams like this give vertices with $k$ incidences. Taking polynomials in the operators which give such diagrams gives operators which can be interpreted in terms of diagrams having several such vertices. Such a diagram is shown in figure [6](#fig:feynmaninprod){reference-type="ref" reference="fig:feynmaninprod"} - note that here we continue the practice of omitting to draw the internal finite sets in the composite stuff operator.

<figure id="fig:feynmaninprod">
<div class="center">
<embed src="feynmaninprod.eps" />
</div>
<figcaption><span id="fig:feynmaninprod" label="fig:feynmaninprod"></span>An Object in <span class="math inline">⟨<em>Ψ</em><sub>2</sub>,(<em>Φ</em><sup>3</sup>/   /<em>S</em><sub>3</sub>)<sup>6</sup><em>Ψ</em><sub>1</sub>⟩</span></figcaption>
</figure>

Given two stuff types $\Psi_1:\boldsymbol{\operatorname{{X_1}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ and $\Psi_2:\boldsymbol{\operatorname{{X_2}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$, we can take the inner product $\left\langle{\Psi_1,\Phi^{n}\Psi_2}\right\rangle$. This applies this operator to $\Psi_2$ to give compound objects involving objects of $\Phi^{n}$ and of $\boldsymbol{\operatorname{{X_2}}}$. Taking the inner product with $\Psi_1$ gives objects as illustrated in figure [6](#fig:feynmaninprod){reference-type="ref" reference="fig:feynmaninprod"}. The groupoid cardinality of this inner product amounts to a sum over all such diagrams, each with a weight related to the size of the symmetry group of the diagram.

::: example
We can use the above to show the categorical meaning of the usual calculation of the expectation value of a power of the field operator. In particular, suppose we want to calculate $\left\langle{1,\frac{\phi^6}{6!} 1}\right\rangle$, the vacuum expectation value of the 6th power of the (normalized) field operator.

To do this, we want to take a sum over objects which are equivalent to ways of matching two empty sets with diagrams like figure [5](#fig:field4op){reference-type="ref" reference="fig:field4op"}, containing one vertex of valence 6. We begin with the case where incidences are labelled (as in figure [4](#fig:field4oplabelled){reference-type="ref" reference="fig:field4oplabelled"}). Since the source and target sets are empty, all edges must form loops touching the vertex at both ends. The number of such diagrams is $(\binom{6}{2} \binom{4}{2}
\binom{2}{2})/3!=15$ (choosing the endpoints of three edges, without order). These give the objects of a groupoid one of which is shown in figure [7](#fig:6vertex){reference-type="ref" reference="fig:6vertex"}.

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
If $M$ is a monoid, $\boldsymbol{\operatorname{{MSet}}}$ is the category of "sets over $M$"[^1], or "$M$-sets". Its objects are pairs $(S,f)$, for $S \in \boldsymbol{\operatorname{{Set}}}$ and $f : S
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

We would like to extend these results about $M$-sets to a notion of $M$-groupoids and their cardinalities which is compatible with cardinalities of $M$-sets and of ordinary groupoids in the suitable special cases. One way to see the correct approach to $M$-groupoids is to take advantage our existing idea of $M$-sets and a connection we already know between sets and groupoids. This is the concept of a groupoid-coloured set. We define groupoid-coloured $M$-sets by analogy with these. Recall from [\[colouredsets\]](#colouredsets){reference-type="ref" reference="colouredsets"} that a set can be seen as groupoid whose objects are the elements of the set, and with only identity morphisms[^2]. Then we have:

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

Since stuff types (and $M$-stuff types) can be multiplied by groupoids, whose cardinalities lie in $\mathbbm{R}^+$, this action by $M$ gives another version of multiplication. This will be particularly interesting when we consider $M = U(1)$ in section [\[mstuffu1\]](#mstuffu1){reference-type="ref" reference="mstuffu1"}, but first we should define the cardinality of an $M$-stuff type:

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

Once we defined $M$-sets and hence $M$-groupoids, it was possible to define $M$-stuff types simply by substituting these for groupoids in the original definition of stuff types. The only properties of $\boldsymbol{\operatorname{{FinSet_0}}}$ which were used in the original construction of stuff types and operators was that it should be a groupoid: groupoids $\boldsymbol{\operatorname{{X}}}$ with one or two functors into it were stuff types and operators respectively. Morphisms between the objects of a stuff type were morphisms in $\boldsymbol{\operatorname{{X}}}$ together with compatible bijections of sets (recall figure [\[fig:typemorphism\]](#fig:typemorphism){reference-type="ref" reference="fig:typemorphism"}), but this depended only on the fact that these were isomorphisms in the groupoid $\boldsymbol{\operatorname{{FinSet_0}}}$. So, in the same way, a morphism in the groupoid of an $M$-stuff type consists of a morphism in its $M$-groupoid, together with a compatible bijection of underlying sets, as illustrated in figure [8](#fig:mstuffmorphism){reference-type="ref" reference="fig:mstuffmorphism"}. Notice that the objects $x$ and $x'$ are labelled by the same element, $m_1 \in M$, since $f$ is an isomorphism in $\boldsymbol{\operatorname{{X}}}$.

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

An object in the inner product groupoid looks like figure [9](#fig:mstuffinprodobject){reference-type="ref" reference="fig:mstuffinprodobject"}, where $m_i$ are elements of $M$. This figure is analogous to the previous inner product (figure [\[fig:pullbackobject\]](#fig:pullbackobject){reference-type="ref" reference="fig:pullbackobject"}). Note that, in contrast to the case in figure [8](#fig:mstuffmorphism){reference-type="ref" reference="fig:mstuffmorphism"}, the objects $x \in \boldsymbol{\operatorname{{X}}}$ and $y \in \boldsymbol{\operatorname{{Y}}}$ are not in the same groupoid, hence not related by any morphism, so there is no requirement that $m_1$ and $m_2$ should be equal. The object illustrated is labelled be the element $m_1
\cdot m_2 \in M$ (as highlighted).

<figure id="fig:mstuffinprodobject">
<div class="center">
<embed src="mstuffinprodobject.eps" />
</div>
<figcaption><span id="fig:mstuffinprodobject" label="fig:mstuffinprodobject"></span>An Object In the Inner Product of two <span class="math inline"><em>M</em></span>-Stuff Types</figcaption>
</figure>

Similar changes apply to the other constructions defined using the weak pullback, so that we have nearly identical categorical diagrams definining morphisms in the inner product, as well as the action of an $M$-stuff operator on an $M$-stuff type and the composition of two $M$-stuff operators, as in definition [\[def:stuffopdefns\]](#def:stuffopdefns){reference-type="ref" reference="def:stuffopdefns"}. The sole change at this level is the replacement of groupoids with $M$-groupoids, and thus in figures [\[fig:stuffopresult\]](#fig:stuffopresult){reference-type="ref" reference="fig:stuffopresult"} and [\[fig:stuffopcomposition\]](#fig:stuffopcomposition){reference-type="ref" reference="fig:stuffopcomposition"}, we have labels in $M$ on every groupoid object, preserved under every isomorphism.

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

[^1]: See appendix [\[sec:slicecategory\]](#sec:slicecategory){reference-type="ref" reference="sec:slicecategory"} for comments about such "over categories". The usual definition applies here by treating $M$ as a set of elements, though we get some extra structure from the monoidal operation on $M$.

[^2]: Since we are already thinking of sets as special kinds of categories here, this raises the question of what happens if we categorify $M$. We return to this in section [\[sec:categorifyingM\]](#sec:categorifyingM){reference-type="ref" reference="sec:categorifyingM"}.
