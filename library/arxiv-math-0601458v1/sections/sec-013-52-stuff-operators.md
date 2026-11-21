---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-013-52-stuff-operators
section_title: "Stuff Operators"
section_number: 5.2
pages: 34-38
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.973
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
So far we have described stuff types, and implied that they, as extensions of structure types, are a useful way of categorifying functions - in the setting where these functions are seen as states of a certain quantum system. The inner product defined in section [\[stuffinnerprod\]](#stuffinnerprod){reference-type="ref" reference="stuffinnerprod"} gives these some of the structure of a Hilbert space, and also makes a connection to Feynman diagrams for energy quanta of a harmonic oscillator. We want to describe more of the structure of the 2-rig of stuff types - in particular its linear structure, demanding a definition for the equivalent of a linear operator. We call such a thing a *stuff operator*. There will be a category of these, called $\boldsymbol{\operatorname{{StuffOps}}}$, with higher-dimensional algebraic structure similar to that of the algebra of linear operators on a Hilbert space, with an action on the category $\boldsymbol{\operatorname{{StuffTypes}}}$.

We need to describe this action: a stuff operator $T$, given a stuff type $\Psi:X\rightarrow\boldsymbol{\operatorname{{FinSet_0}}}$, ought to produce another stuff type $T(\Psi):T(X)\rightarrow\boldsymbol{\operatorname{{FinSet_0}}}$, using natural category-theoretic operations, in a way that reflects the fact that $T$ is the categorified equivalent of a linear operator on a Hilbert space of states. One way to motivate our approach to constructing this is to remember that for a Hilbert space $H$, a linear operator $T$ can be thought of as an element of the tensor product $H \otimes H^{\ast}$ of $H$ with its dual, and given a basis of $H$, $T$ can be represented as a matrix (a two-index tensor). To put this into the same framework as the stuff type $\Psi$, recall that this can be seen as a vector in a space of states[^1], and the equivalent of resolving it in a basis arises by taking the preimages of elements of $\boldsymbol{\operatorname{{FinSet_0}}}$ as the components in the basis. In this setting, applying $T$ to a vector $\boldsymbol{v}$ (using the $H^{\ast}$ in the description in terms of $H \otimes H^{\ast}$) amounts to applying covectors in any decomposition of $T$ to $\boldsymbol{v}$, which (since $H \cong H^{\ast}$) amounts to taking the inner product of $\boldsymbol{v}$ with a vector in $H$. Since we have already seen a natural definition of inner product for stuff types, we will use a similar construction.

A stuff type $\Psi: \boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ can be variously seen as the projection map of a groupoid-bundle on finite sets, and also as a way of picking out an index for some component of a vector in a categorified equivalent of a Hilbert space. A stuff *operator* should have *two* such maps, since it is to correspond to a linear operator. We should think of this as "resolving $T$ in the same basis".

The analogy with matrices suggests that $T$ acts on stuff types in the same way as the inner product, just as matrices act on vectors (resolved in a basis) by way of the inner product in each index. So indeed, $T \Psi$ is defined as a weak pullback:

::: definition
A **stuff operator** is a groupoid $T$ with two projection maps into $\boldsymbol{\operatorname{{FinSet_0}}}$: $$\xymatrix{
   & T\ar_-{p_1}[ld]\ar^-{p_2}[rd] & \\
  \boldsymbol{\operatorname{{FinSet_0}}}& & \boldsymbol{\operatorname{{FinSet_0}}}\\
 }$$
:::

We have seen the internal picture of objects of $\Psi$ in figure [\[fig:typeobject\]](#fig:typeobject){reference-type="ref" reference="fig:typeobject"}, so we next look at a similar description for $T$. An object $t \in T$ is somewhat similar to an object of $\Psi$, but this object has not just one underlying set, but two possibly distinct ones, which we call $p_1(t)$ and $p_2(t)$, which in general need not have the same cardinality. We can think of this as two sets sharing a common label, which we may think of as a "process" connecting $p_1(t)$ with $p_2(t)$, where the label $t$ contains *stuff* associated to this transition, shown generally in ([\[eq:stuffopobject\]](#eq:stuffopobject){reference-type="ref" reference="eq:stuffopobject"}) and illustrated in figure [1](#fig:stuffopobject){reference-type="ref" reference="fig:stuffopobject"}.

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
\boldsymbol{\operatorname{{FinSet_0}}}$, and also of $p_2 : T \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$. Its objects will be pairs of objects $x \in \boldsymbol{\operatorname{{X}}}$ and $t \in T$ together with isomorphisms $\alpha_{x,t}:\Psi(x) \rightarrow p_2(t)$. These are isomorphisms of the underlying sets, so in particular they only exist if these sets have the same cardinality. Thus, an object of $T\Psi$ looks like an object of $T$ connected by a bijection of underlying sets to an object of $\Psi$ (using the "right-hand" underlying set of $T$). The general form is shown in ([\[eq:stuffopresult\]](#eq:stuffopresult){reference-type="ref" reference="eq:stuffopresult"}) and an example is illustrated in figure [2](#fig:stuffopresult){reference-type="ref" reference="fig:stuffopresult"}.

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

Now as for the composite of $T$ and $T'$, similar reasoning holds except that we have another stuff operator $T'$ in place of $\Psi$, so the general form of an object of $TT'$ is as shown in ([\[eq:stuffopcomposition\]](#eq:stuffopcomposition){reference-type="ref" reference="eq:stuffopcomposition"}), and an example is illustrated in figure [3](#fig:stuffopcomposition){reference-type="ref" reference="fig:stuffopcomposition"}.

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

[^1]: Strictly speaking, the "ground field" here is not $\mathbbm{C}$ but rather the setting for cardinalities of groupoids, $\mathbbm{R}^+$, so we do not yet have a vector space. When we introduce $M$-stuff and get cardinalities in something like $\mathbbm{C}$, we will really have a vectorspace.
