---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.991
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
[]{#sec:intro label="sec:intro"}

In this paper, I will describe an extension of the *groupoidification* program of Baez and Dolan [@hdaVII]. Groupoidification refers to the program of treating parts of linear algebra as arising from spans of groupoids (categories whose morphisms are all invertible) by a process of "degroupoidification", which produces complex vector spaces associated to groupoids, and linear maps associated to spans. The extension described here shows a connection of the setting of groupoids and spans with 2-vector spaces and 2-linear maps, a categorical analog of linear algebra. (We will assume that all groupoids are essentially finite - that is, equivalent to finite groupoids - although there is work in progress on how to extend these results to infinite groupoids, and in particular Lie groupoids.)

A simple example of the groupoidification program can be seen in terms of spans of finite sets (i.e. finite trivial groupoids). In that program, groupoids give corresponding vector spaces and spans of groupoids give corresponding linear maps. In particular, the special case of trivial groupoids (equivalently, sets) gives a useful illustration. Given a finite set $S$, there is a finite dimensional vector space $L(S)$ consisting of all complex linear combinations of elements of $S$. Now, consider a span in $\boldsymbol{\operatorname{{FinSet}}}$: that is, a diagram of the form: $$\xymatrix{
 & X \ar[dl]_{s} \ar[dr]^{t} & \\
Y & & Z
}$$ To the span, there is a corresponding to a linear map $L(X) : L(Y)
\rightarrow L(Z)$, represented by a matrix $T$ whose $(i,j)$-component is $|(s,t)^{-1}(y_i,z_j)$

<figure id="fig:set-span">
<div class="center">
<embed src="set-span.eps" />
</div>
<figcaption><span id="fig:set-span" label="fig:set-span"></span>A Span of Sets</figcaption>
</figure>

So the set in Figure [1](#fig:set-span){reference-type="ref" reference="fig:set-span"} gives rise to the linear transformation: $$\begin{aligned}
\nonumber y_1 \mapsto z_1 \\
y_2 \mapsto z_1 + z_2 \\
\nonumber y_3 \mapsto z_2
\end{aligned}$$

This makes sense for spans of finite sets. Similarly, we will be considering an analogous construction for spans of *essentially finite* groupoids.

There is a physical motivation here in quantum mechanics. If $Y$ is the (discrete) set of classical (pure) states of a system, then $L(Y) =
\mathbb{C}[Y]$, the space of linear combinations of states in $Y$, is the Hilbert space of the corresponding quantum mechanical system. (More generally, if $Y$ is a measure space, one takes $L^2(Y)$). In the span, we think of $X$ as a set of "processes" $x$, each with a designated "source" or starting state $s(x) \in Y$ and "target" or ending state $t(x) \in Z$. Then the linear transformation described by the matrix $T$ can be seen in the following way, which we shall generalize later on:

Given a linear combination of elements of $Y$ (that is, a function $f
: Y \rightarrow \mathbb{C}$), transport $f$ to $X$ by "pulling back" along $s$. That is, $s^{\ast}f(x) = f(s(x))$. Then "push forward" to $Z$ by taking the sum over all elements of $X$ mapping down to a chosen one in $Z$: $$t_{\ast} s^{\ast} f (z) = \sum_{t(x) = z} s^{\ast}f (x)$$ This precisely gives matrix multiplication by the matrix described above, and can clearly also be seen as a "sum over histories": the value of $t_{\ast} s^{\ast} f(z)$ is a sum, over all histories $x$ ending at $z$, of the value of $f$ at the source $s(x)$. This illustrates a contrast between classical and quantum *processes*. Classically, states succeed each other by exactly one process. In the quantum picture, *every* possible process contributes to evolution of a state. In particular, there is an interpretation of quantum processes in terms of "matrix mechanics", which takes a sum (in the form of matrix multiplication) over all histories joining fixed start and end states. This is exactly what is shown in our example.

It is not too difficult to check that the linearization of spans of sets gets along with composition, so that the composite of spans (by pullback, giving a set of *composite paths*) agrees with composition of linear maps. That is, that the process is *functorial*. This fact makes it possible to think of categorifying this process, in order to explicitly include symmetries of both states and histories as fundamental concepts. A categorified version of this process should be a 2-functor.

One way to generalize spans of sets, which is seen in [@hdaVII], uses groupoids (categories whose morphisms are all invertible) instead of sets. One reason to consider this is that it often happens that the configuration space can naturally be thought of not as a set but as a groupoid. This happens particularly when there are symmetry operations acting on the set of configurations, and we explicitly represent such symmetries as morphisms of the groupoid. The existence of a group action on the set would be one example. In such a categorified picture, $X$ has objects which represent states of a system, and morphisms denoting *symmetries* of states. Then $L$ gives vector spaces which are linear combinations of *isomorphism classes of objects* of the groupoids. The components of the linear maps uses groupoid cardinality instead of set cardinality: $$\begin{aligned}
\label{eq:baezgpdify} L(X)_{[y_i],[z_k]} & = \sum_{x \in \underline{(s,t)^{-1}(y_i,z_k)}}\frac{\#(\operatorname{Aut}(y_i))}{\#(\operatorname{Aut}(x))} \\ 
\nonumber & = |\widehat{(y_i,z_k)}| \cdot \# (\operatorname{Aut}(y_i))
\end{aligned}$$ where $\widehat{(y_i,z_k)}$ is the *essential preimage* of $y_i$ and $z_k$, and its cardinality is the groupoid cardinality described by Baez and Dolan [@finfeyn] (the other cardinality is the order of the group). This uses a weighting of contributions from intermediate elements depending on the size of their symmetry group. The groupoid cardinality of a finite groupoid $X$ is: $$\label{eq:gpdcard}
|X| = \sum_{[x] \in \underline{X}} \frac{1}{\# \operatorname{Aut}(x)}$$ where the cardinality in the sum denotes the order of the group.

Here, however, we want to do something a little different: this process is still a functor, and we wanted a *2-functor*. Since we want to think of $X$ as a category, rather than look at functions from the objects of $X$ into $\mathbb{C}$, we should look at functors from $X$ into some category which plays the role of $\mathbb{C}$. In particular, this category will be $\boldsymbol{\operatorname{{Vect}}}$, whose objects are vector spaces over $\mathbb{C}$, and whose morphisms are linear maps. When categorifying, therefore, we will want to find an analogous 2-functor, which requires specifying more data.

Then there will be a "free 2-vector space" $\Lambda(X)$ of all functors from $X$ into $\boldsymbol{\operatorname{{Vect}}}$. We think of the objects as "2-linear combinations" of classical states, each with an *internal state space* which carries a representation of the symmetry group of that state. For most physically realistic systems, $X$ would be an infinite set with a measure, and in fact a symplectic manifold. In general, to deal with $L^2$ spaces involves some issues in analysis, such as the measure on $X$. Then instead of $L(X)$ we consider $L^2(X)$. A similar caveat should apply in the categorified setting. Restricting to the situation of a finite groupoid helps to more clearly illustrate some of the purely category-theoretic aspects of the "free 2-vector space" construction. We do expect that for well-behaved smooth groupoids, for example, similar results to those considered in this paper will hold, involving infinite dimensional 2-vector spaces one could denote $2L^2(X)$. But this will be addressed in a companion paper.

Finally, we remark that this construction is used in the construction of an Extended Topological Quantum Field Theory (ETQFT) in the author's Ph.D. thesis [@mortonthesis], where the groupoids in question are topological invariants of manifolds. By analogy, it could be used to give "extended quantum theories" in other settings where spans of groupoids appear.

Another view of a related process involves the 2-functor into additive categories (which, in the $\mathbb{C}$-linear case, are the KV 2-vector spaces) from a 2-category $\boldsymbol{\operatorname{{Bim}}}$, whose objects are rings, morphisms in $\hom_{\boldsymbol{\operatorname{{Bim}}}}(R,S)$ are $(R,S)$-bimodules, and whose 2-morphisms are bimodule homomorphisms. This is a dual picture to that of spans. Indeed, the type of "pull-push" construction given here is ubiquitous (as its appearance in linear algebra suggests), due to the universal properties of categories of spans (see [@unispan]). Similar notions also appear in the theory of Mackey functors (see [@elango]), and in the study of "correspondences" in noncommutative geometry, algebraic geometry, and elsewhere.

In this paper, we will begin by describing the source and target categories, $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$ in section [1](#sec:spangpd){reference-type="ref" reference="sec:spangpd"}, and $\boldsymbol{\operatorname{{2Vect}}}$ in section [\[sec:KV\]](#sec:KV){reference-type="ref" reference="sec:KV"}. In particular, to categorify the functor $L$, we need a 2-category to correspond to $\boldsymbol{\operatorname{{Vect}}}$, and this will be the 2-category of all Kapranov-Voevodsky 2-vector spaces. A KV 2-vector space is an abelian category with some extra structure, just as a vector space is a special type of abelian group. In section [\[sec:KV\]](#sec:KV){reference-type="ref" reference="sec:KV"} we give some background and collect some fundamental results about them which are widely known, but whose proofs are seldom given. For example, we show that 2-vector spaces, understood as a semisimple $\mathbb{C}$-linear additive category, are all equivalent to $\boldsymbol{\operatorname{{Vect}}}^k$ for some nonnegative integer $k$.

In section [\[sec:kv2vsgrpd\]](#sec:kv2vsgrpd){reference-type="ref" reference="sec:kv2vsgrpd"}, we give the object level of our construction for a 2-functor $\Lambda$, which, to (essentially finite) groupoids assigns KV 2-vector spaces. Analogously with sets, we obtain 2-linear maps for spans of groupoids. In fact, just as with sets, this is a consequence of an even simpler correspondence. Namely, there is the "pullback" and "push-forward" of a function mentioned in the description of the linear map from a span of sets as a *sum over histories* (the sum occurs in the "push-forward" operation, and corresponds to the sum in matrix multiplication). The groupoid situation is more complicated than that for sets, however, because of the existence of automorphisms of the objects, and the condition that maps between groupoids are functors. This means, in particular, that for each object $x$ in a groupoid, the functor determines a homomorphism from the automorphism group of $x$ to that of its image. The push-forward operation can be interpreted as a Kan extension and has both an object and a morphism level.

Section [\[sec:spans\]](#sec:spans){reference-type="ref" reference="sec:spans"} describes how these results define 2-linear maps associated to spans of groupoids. It begins with a brief discussion of the bicategory whose objects are groupoids, whose morphisms are spans of groupoids, and whose 2-morphisms are span maps. This is followed by an explicit construction of the morphism level of the 2-functor $\Lambda: \operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}}) \rightarrow \boldsymbol{\operatorname{{2Vect}}}$ and shows that it preserves composition of spans in the weak sense: that is, up to a specified isomorphism. (Technical details of this proof are reserved for appendix [\[ax:composproof\]](#ax:composproof){reference-type="ref" reference="ax:composproof"}). Finally, using Frobenius reciprocity, it describes a simple explicit matrix representation for the 2-functor constructed.

Section [\[sec:spanspan\]](#sec:spanspan){reference-type="ref" reference="sec:spanspan"} then continues by describing how this representation works at the level of 2-morphisms. This is analogous to the 1-morphism level, in that it consists of a "pullback and pushforward" process. This is most easily described in terms of the linear maps between corresponding vector spaces which appear in the matrix representation of the 2-linear maps associated to a pair of spans from $A$ to $B$. We give this construction and show it preserves both vertical and horizontal composition of 2-morphisms in the appropriate ways.

The results shown in sections [\[sec:spans\]](#sec:spans){reference-type="ref" reference="sec:spans"} and [\[sec:spanspan\]](#sec:spanspan){reference-type="ref" reference="sec:spanspan"} do much of the work involved in showing that our representation is really a 2-functor. The remainder of this proof is given in section [\[sec:maintheorem\]](#sec:maintheorem){reference-type="ref" reference="sec:maintheorem"}.

Now we begin to describe the 2-linearization process by collecting some key facts about the bicategory of 2-vector spaces, including a canonical construction of one for each (essentially finite) groupoid.

# The Bicategory $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$ {#sec:spangpd}

The main purpose of this paper is to describe a weak 2-functor $$\Lambda: \operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}}) \mathop{\rightarrow}\boldsymbol{\operatorname{{2Vect}}}$$ In this section, we will describe the source bicategory, $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$.

First, the objects of $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$.

::: definition
[]{#def:essfingpd label="def:essfingpd"} An **essentially finite** groupoid is one which is equivalent to a finite groupoid. A **finitely generated** groupoid is one with a finite set of objects, and all of whose morphisms are generated under composition by a finite set of morphisms. An **essentially finitely generated** groupoid is one which is equivalent to a finitely generated one.
:::

Note that, in particular, essentially finitely generated groupoids must be essentially finite, since every object has an identity morphism. We will use the term "essentially finite" to mean both of these conditions. Next we describe the morphisms of $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$.

In any category $\boldsymbol{\operatorname{{C}}}$, a *span* is a diagram of the form: $$\label{eq:spandiag}
\xymatrix{
  & X \ar[dl]^{s} \ar[dr]_{t} & \\
A_1  & & A_2  \\
}$$

In particular, we want to reproduce the "linearization" associated to spans of sets which we discussed in the introduction. The idea is that given a span of groupoids, as in Figure [2](#fig:grpd-span){reference-type="ref" reference="fig:grpd-span"} (which suppresses the homomorphisms labelling the strands in the span, but should be compared with Figure [1](#fig:set-span){reference-type="ref" reference="fig:set-span"}), there will be a "transfer" 2-linear map from the KV 2-vector space associated to the source of the span, to that associated to the target.

<figure id="fig:grpd-span">
<div class="center">
<embed src="grpd-span.eps" />
</div>
<figcaption><span id="fig:grpd-span" label="fig:grpd-span"></span>A Span of Groupoids</figcaption>
</figure>

If $\boldsymbol{\operatorname{{C}}}$ has pullbacks, we can define composition of spans using them: $$\label{xy:spancomposite}
  \xymatrix{
     & & X' \circ X \ar[dl]_{S} \ar[dr]^{T} & & \\
     & X \ar[dl]_{s} \ar[dr]^{t} & & X' \ar[dl]_{s'} \ar[dr]^{t'} & \\ 
   A_1 & & A_2 & & A_3 \\ 
  }$$ where we define $X' \circ X$ to be the object, unique up to isomorphism, which makes the central square a pullback square. That is, it is a terminal occupant of this niche. If $\boldsymbol{\operatorname{{C}}}$ is, in addition, a concrete category, the pullback is a subobject of the product $X
\times X'$. $$X' \circ X = X \times_{A_2} X' = \bigcup_{a \in A_2} t^{-1}(a) \times (s')^{-1}(a)$$ the fibred product of $X'$ and $X$ over $A_2$. (Indeed, if $\boldsymbol{\operatorname{{C}}}$ is Cartesian, any span can be factored through a product.)

Now, for any category $\boldsymbol{\operatorname{{C}}}$ with pullbacks, there is a category $\operatorname{Span}(\boldsymbol{\operatorname{{C}}})$ whose objects are the objects of $\boldsymbol{\operatorname{{C}}}$, and whose morphisms are isomorphism classes spans in $\boldsymbol{\operatorname{{C}}}$ composed by pullback. Here we are taking spans up to isomorphisms $\alpha : X_1 \rightarrow X_2$ which are commuting diagrams of the form: $$\label{xy:spanmap}
\xymatrix{
  & X_1 \ar[dl]_{s_1} \ar[d]^{\alpha} \ar[dr]^{t_1} & \\
A_1 & X_2 \ar[l]^{s_2} \ar[r]_{t_2} & A_2 \\
}$$

However, we will do something slightly different. We will be interested in spans of groupoids. Since groupoids naturally form a 2-category, we should weaken the notion of composition, and give an appropriate notion of 2-morphism, for a bicategory $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$.

Given any 2-category $\boldsymbol{\operatorname{{C}}}$ with weak pullbacks, one can again form a bicategory $\operatorname{Span}(\boldsymbol{\operatorname{{C}}})$ with the same objects as $\boldsymbol{\operatorname{{C}}}$ and with spans for morphisms. T composite of spans $A_1 \mathop{\mathop{\leftarrow}}\limits^{s} X \mathop{\mathop{\rightarrow}}\limits^{t} A_2$ and $A_2 \mathop{\mathop{\leftarrow}}\limits^{s'} X' \mathop{\mathop{\rightarrow}}\limits^{t'} A_3$ is an object $X' \circ X$ together with a 2-morphism $\alpha$ making this diagram commute, and terminal for such choices: $$\label{xy:wkpb}
 \xymatrix{
   & & {X'\circ X} \ar_{S}[ld]\ar^{T}[rd]\ar@/_2pc/_{s \circ S}[ddll]\ar@/^2pc/^{t' \circ T}[ddrr] & & \\
   & {X}\ar^{s}[ld]\ar_{t}[rd] \ar@{=>}[rr]^{\alpha}_{\sim} & & {X'}\ar^{s'}[ld]\ar_{t'}[rd] & \\
   {A_1} & & {A_2} & & {A_3} \\
}$$

A 2-morphism in $\operatorname{Span}(\boldsymbol{\operatorname{{C}}})$ will be an isomorphism class of *spans of span maps*. That is, consider a span of *2-morphisms* in the usual $\operatorname{Span}(\boldsymbol{\operatorname{{C}}})$. This is a diagram of the form: $$\label{xy:spanmapspan}
\xymatrix{
  & X_1 \ar[dl]^{s_1}  \ar[dr]_{t_1} & \\
A_1 & Y \ar[l] \ar[r] \ar[d]^{t} \ar[u]_{s}& A_2 \\
  & X_2 \ar[ul]_{s_2}  \ar[ur]^{t_2} & \\
}$$

In principle we need only require this diagram commute weakly: that is, there are isomorphisms $\zeta_s : s_1 \circ s \mathop{\rightarrow}s_2 \circ t$ and $\zeta_t : t_1 \circ s \mathop{\rightarrow}t_2 \circ t$. For the most part, since the construction we mean to give is invariant under equivalence of groupoids, and taking the $A_i$ to be skeletal makes this strict, we will assume strict commutativity, though we shall indicate where the argument must be changed to accommodate the weak case.

We are considering such diagrams only *up to isomorphism*: that is, the inner span $X_1 \mathop{\leftarrow}Y \mathop{\rightarrow}X_2$ in the 2-morphism [\[xy:spanmapspan\]](#xy:spanmapspan){reference-type="ref" reference="xy:spanmapspan"} is only considered up to an isomorphism of spans in the sense of [\[xy:spanmap\]](#xy:spanmap){reference-type="ref" reference="xy:spanmap"}.

The reason for considering these is as follows. First, taking a category $\boldsymbol{\operatorname{{C}}}$ and passing to $\operatorname{Span}(\boldsymbol{\operatorname{{C}}})$ amounts to formally adjoining duals for morphisms in $\boldsymbol{\operatorname{{C}}}$. The dual of any span is the span which has the same maps, considered in the reverse orientation, exchanging the role of source and target object. When we apply $\Lambda$, these duals will in fact become adjoints, as we shall see.

Now, we are interested in the case $\boldsymbol{\operatorname{{C}}}= \boldsymbol{\operatorname{{FinGpd}}}$, so the diagram for the composite of spans between groupoids contains a weak pullback square: composition is only preserved up to isomorphism. In particular, the objects are now groupoids, which are themselves categories with objects and morphisms. Since it makes sense to speak of two objects of a groupoid being isomorphic, the weakest meaningful condition is that objects of groupoids $X$ and $X'$ should need only project to isomorphic objects on $A_2$. But there are potentially different isomorphisms between those objects. So the weak pullback is a larger groupoid than a strict pullback, since its objects come with a specified isomorphism between the two restrictions.

That this is a weak pullback square of functors between groupoids means that this diagram commutes up to the natural isomorphism $\alpha
: t \circ S \longrightarrow s' \circ T$. (The fact that $\alpha$ is iso is what makes this a *weak* pullback rather than a *lax* pullback, where $\alpha$ is only a natural transformation.) This is an example of a *comma category* (the concept, though not the name, was introduced by Lawvere in his doctoral thesis [@lawverethesis]). We recall some background about this construction in Appendix [\[sec:commacat\]](#sec:commacat){reference-type="ref" reference="sec:commacat"}.

Now, the process of finding higher morphisms by taking spans of span maps could obviously be continued: each new level of span naturally gives maps of spans as morphisms. We could repeat the process of adjoining duals by passing to spans of such span maps, and so on recursively as far as we wish. For our purposes here, however, we will stop at 2-morphisms for two reasons. First, we want to describe a representation into $\boldsymbol{\operatorname{{2Vect}}}$, which is a 2-category. This in turn is since the objects of $\boldsymbol{\operatorname{{FinGpd}}}$ are themselves categories, and our 2-functor $\Lambda$ will represent them as categories - so a 2-category is the natural setting for them.

Collecting the definition together, we then have the following.

::: definition
[]{#def:spangpd label="def:spangpd"} The bicategory $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$ has:

-   **Objects**: Essentially finite groupoids

-   **Morphisms**: Spans of groupoids, composed by weak pullback

-   **2-Morphisms**: Isomorphism classes of spans of span maps, composed by weak pullback both horizontally and vertically
:::

Having defined $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$, the source bicategory of the 2-functor $\Lambda$ we aim to describe here, we next describe its target, $\boldsymbol{\operatorname{{2Vect}}}$.
