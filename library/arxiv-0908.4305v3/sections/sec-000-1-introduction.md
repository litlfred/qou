---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-25
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
text_source: latex
latex_prose_ratio: 0.715
latex_coverage_ratio: 0.997
---
[]{#intro label="intro"}

'Groupoidification' is an attempt to expose the combinatorial underpinnings of linear algebra---the hard bones of set theory underlying the flexibility of the continuum. One of the main lessons of modern algebra is to avoid choosing bases for vector spaces until you need them. As Hermann Weyl wrote, "The introduction of a coordinate system to geometry is an act of violence\". But vector spaces often come equipped with a natural basis---and when this happens, there is no harm in taking advantage of it. The most obvious example is when our vector space has been defined to consist of formal linear combinations of the elements of some set. Then this set is our basis. But surprisingly often, the elements of this set are *isomorphism classes of objects in some groupoid*. This is when groupoidification can be useful. It lets us work directly with the groupoid, using tools analogous to those of linear algebra, without bringing in the real numbers (or any other ground field).

For example, let $E$ be the groupoid of finite sets and bijections. An isomorphism class of finite sets is just a natural number, so the set of isomorphism classes of objects in $E$ can be identified with ${\mathbb N}$. Indeed, this is why natural numbers were invented in the first place: to count finite sets. The real vector space with ${\mathbb N}$ as basis is usually identified with the polynomial algebra ${\mathbb R}[z]$, since that has basis $z^0, z^1, z^2, \dots.$ Alternatively, we can work with *infinite* formal linear combinations of natural numbers, which form the algebra of formal power series, ${\mathbb R}[[z]]$. So, the vector space of formal power series is a kind of stand-in for the groupoid of finite sets.

Indeed, formal power series have long been used as 'generating functions' in combinatorics [@Wilf]. Given any combinatorial structure we can put on finite sets, its generating function is the formal power series whose $n$th coefficient says how many ways we can put this structure on an $n$-element set. André Joyal formalized the idea of 'a structure we can put on finite sets' in terms of *espèces de structures*, or 'structure types' [@BLL; @Joyal; @Joyal2]. Later his work was generalized to 'stuff types' [@BaezDolan:2001], which are a key example of groupoidification.

Heuristically, a stuff type is a way of equipping finite sets with a specific type of extra stuff---for example a 2-coloring, or a linear ordering, or an additional finite set. Stuff types have generating functions, which are formal power series. Combinatorially interesting operations on stuff types correspond to interesting operations on their generating functions: addition, multiplication, differentiation, and so on. Joyal's great idea amounts to this: *work directly with stuff types as much as possible, and put off taking their generating functions.* As we shall see, this is an example of groupoidification.

To see how this works, we should be more precise. A **stuff type** is a groupoid over the groupoid of finite sets: that is, a groupoid $\Psi$ equipped with a functor $v \colon\Psi \rightarrow E$. The reason for the funny name is that we can think of $\Psi$ as a groupoid of finite sets 'equipped with extra stuff'. The functor $v$ is then the 'forgetful functor' that forgets this extra stuff and gives the underlying set.

The generating function of a stuff type $v \colon\Psi \rightarrow E$ is the formal power series $$\label{eq:generating_function}
       \utilde{\Psi}(z) = \sum_{n = 0}^\infty |v^{-1}(n)| \, z^n .$$ Here $v^{-1}(n)$ is the 'full inverse image' of any $n$-element set, say $n \in E$. We define this term later, but the idea is straightforward: $v^{-1}(n)$ is the groupoid of $n$-element sets equipped with the given type of stuff. The $n$th coefficient of the generating function measures the size of this groupoid.

But how? Here we need the concept of *groupoid cardinality*. It seems this concept first appeared in algebraic geometry [@Behrends:1993; @Kim:1995]. We rediscovered it by pondering the meaning of division [@BaezDolan:2001]. Addition of natural numbers comes from disjoint union of finite sets, since $$|S + T| = |S| + |T|  .$$ Multiplication comes from cartesian product: $$|S \times T| = |S| \times |T|  .$$ But what about division?

If a group $G$ acts on a set $S$, we can 'divide' the set by the group and form the quotient $S/G$. If $S$ and $G$ are finite and $G$ acts freely on $S$, $S/G$ really deserves the name 'quotient', since then $$|S/G| = |S|/|G|.$$ Indeed, this fact captures some of our naive intuitions about division. For example, why is $6/2 = 3$? We can take a 6-element set $S$ with a free action of the group $G = {\mathbb Z}/2$ and construct the set of orbits $S/G$:

Since we are 'folding the 6-element set in half', we get $|S/G| = 3$.

The trouble starts when the action of $G$ on $S$ fails to be free. Let's try the same trick starting with a 5-element set:

We don't obtain a set with $2\frac{1}{2}$ elements! The reason is that the point in the middle gets mapped to itself. To get the desired cardinality $2 \frac{1}{2}$, we would need a way to count this point as 'folded in half'.

To do this, we should first replace the ordinary quotient $S/G$ by the 'action groupoid' or **weak quotient** $S/\!/G$. This is the groupoid where objects are elements of $S$, and a morphism from $s \in
S$ to $s' \in S$ is an element $g \in G$ with $gs = s'$. Composition of morphisms works in the obvious way. Next, we should define the 'cardinality' of a groupoid as follows. For each isomorphism class of objects, pick a representative $x$ and compute the reciprocal of the number of automorphisms of this object; then sum the result over isomorphism classes. In other words, define the **cardinality** of a groupoid $X$ to be $$\label{eq:groupoid_cardinality}
      |X| = \sum_{\rm isomorphism\; classes \; of \; objects\; [x]}
\frac{1}{|{\rm Aut}(x)|} \;.$$ With these definitions, our problematic example gives a groupoid $S/\!/G$ with cardinality $2\frac{1}{2}$, since the point in the middle of the picture gets counted as 'half a point'. In fact, $$|S/\!/G| = |S|/|G|$$ whenever $G$ is a finite group acting on a finite set $S$.

The concept of groupoid cardinality gives an elegant definition of the generating function of a stuff type---Equation [\[eq:generating_function\]](#eq:generating_function){reference-type="ref" reference="eq:generating_function"}---which matches the usual 'exponential generating function' from combinatorics. For the details of how this works, see Example [\[generating_function\]](#generating_function){reference-type="ref" reference="generating_function"}.

Even better, we can vastly generalize the notion of generating function, by replacing $E$ with an arbitrary groupoid. For any groupoid $X$ we get a vector space: namely ${\mathbb R}^{\underline{X}}$, the space of functions $\psi \colon\underline{X} \rightarrow{\mathbb R}$, where $\underline{X}$ is the set of isomorphism classes of objects in $X$. Any sufficiently nice groupoid over $X$ gives a vector in this vector space.

The question then arises: what about linear operators? Here it is good to take a lesson from Heisenberg's matrix mechanics. In his early work on quantum mechanics, Heisenberg did not know about matrices. He reinvented them based on this idea: a matrix $S$ can describe a quantum process by letting the matrix entry $S_i^j \in {\mathbb C}$ stand for the 'amplitude' for a system to undergo a transition from its $i$th state to its $j$th state.

The meaning of complex amplitudes was somewhat mysterious---and indeed it remains so, much as we have become accustomed to it. However, the mystery evaporates if we have a matrix whose entries are natural numbers. Then the matrix entry $S_i^j \in {\mathbb N}$ simply counts the *number of ways* for the system to undergo a transition from its $i$th state to its $j$th state.

Indeed, let $X$ be a set whose elements are possible 'initial states' for some system, and let $Y$ be a set whose elements are possible 'final states'. Suppose $S$ is a set equipped with maps to $X$ and $Y$: $$\xymatrix{
 & S\ar[dl]_q\ar[dr]^p & \\
 Y & & X \\
}$$ Mathematically, we call this setup a span of sets. Physically, we can think of $S$ as a set of possible 'events'. Points in $S$ sitting over $i \in X$ and $j \in Y$ form a subset $$S_i^j = \{ s \colon \; q(s) = j, \; p(s) = i \}  .$$ We can think of this as the *set of ways* for the system to undergo a transition from its $i$th state to its $j$th state. Indeed, we can picture $S$ more vividly as a matrix of sets:\
\
$$\begin{picture}(230,125)(0,25)
 \includegraphics[scale=0.5]{matrix.eps}
 \put(-138,88){$q$}
 \put(-52,88){$p$}
 \put(-8,98){$X$}
 \put(-180,98){$Y$}
 \put(-80,170){$S$}
\end{picture}$$ If all the sets $S_i^j$ are finite, we get a matrix of natural numbers $|S_i^j|$.

Of course, matrices of natural numbers only allow us to do a limited portion of linear algebra. We can go further if we consider, not spans of sets, but *spans of groupoids*. We can picture one of these roughly as follows:

$$\begin{picture}(230,145)(0,30)
 \includegraphics[scale=0.5]{grpdmatrix.eps}
 \put(-138,88){$q$}
 \put(-52,88){$p$}
 \put(-8,98){$X$}
 \put(-180,98){$Y$}
 \put(-80,170){$S$}
\end{picture}$$ If a span of groupoids is sufficiently nice---our technical term will be 'tame'---we can convert it into a linear operator from ${\mathbb R}^{\underline X}$ to ${\mathbb R}^{\underline Y}$. Viewed as a matrix, this operator will have nonnegative real matrix entries. So, we have not succeeded in 'groupoidifying' full-fledged quantum mechanics, where the matrices can be complex. Still, we have made some progress.

As a sign of this, it turns out that any groupoid $X$ gives not just a vector space ${\mathbb R}^{\underline X}$, but a real Hilbert space $L^2(X)$. If $X = E$, the complexification of this Hilbert space is the Hilbert space of the quantum harmonic oscillator. The quantum harmonic oscillator is the simplest system where we can see the usual tools of quantum field theory at work: for example, Feynman diagrams. It turns out that large portions of the theory of Feynman diagrams can be done with spans of groupoids replacing operators [@BaezDolan:2001]. The combinatorics of these diagrams then becomes vivid, stripped bare of the trappings of analysis. We sketch how this works in Section [\[feynman\]](#feynman){reference-type="ref" reference="feynman"}. A more detailed treatment can be found in the work of Jeffrey Morton [@Morton:2006].

To get complex numbers into the game, Morton generalizes groupoids to 'groupoids over ${\rm U}(1)$': that is, groupoids $X$ equipped with functors $v \colon X \rightarrow{\rm U}(1)$, where ${\rm U}(1)$ is the groupoid with unit complex numbers as objects and only identity morphisms. The cardinality of a groupoid over ${\rm U}(1)$ can be complex.

Other generalizations of groupoid cardinality are also interesting. For example, Leinster has generalized it to categories [@Leinster:2008]. The cardinality of a category can be negative! More recently, Weinstein has generalized the concept of cardinality to Lie groupoids [@Weinstein:2008]. Getting a useful generalization of groupoids for which the cardinality is naturally complex, without putting in the complex numbers 'by hand', remains an elusive goal. However, the work of Fiore and Leinster suggests that it is possible [@FioreLeinster:2005].

In the last few years James Dolan, Todd Trimble and the authors have applied groupoidification to better understand the process of '$q$-deformation' [@Baez]. Many important algebraic structures can be systematically deformed in a way that depends on a parameter $q$, with $q = 1$ being the 'default' case of no deformation at all. A beautiful story has begun to emerge in which $q$-deformation arises naturally from replacing the groupoid of pointed finite sets by the groupoid of finite-dimensional vector spaces over the field with $q$ elements, ${\mathbb F}_q$, where $q$ is a prime power. We hope to write up this material and develop it further in the years to come. This paper is just a first installment.

For example, any Dynkin diagram with $n$ dots gives rise to a finite group of linear transformations of ${\mathbb R}^n$ which is generated by reflections, one for each dot of the Dynkin diagram, which satisfy some relations, one for each edge. These groups are called 'Coxeter groups' [@Humphreys]. The simplest example is the symmetry group of the regular $n$-simplex, which arises from a Dynkin diagram with $n$ dots in a row, like this: $$\xymatrix{ \bullet\ar@{-}[r] & \bullet \ar@{-}[r] & \bullet}$$ This group is generated by $n$ reflections $s_d$, one for each dot $d$. These generators obey the Yang--Baxter equation: $$s_d s_{d'} s_d = s_{d'} s_d s_{d'}$$ when the dots $d$ and $d'$ are connected by an edge, and they commute otherwise. Indeed the symmetry group of the regular $n$-simplex is just the symmetric group $S_{n+1}$, which acts as permutations of the vertices, and the generator $s_d$ is the transposition that switches the $d$th and $(d+1)$st vertices.

Coxeter groups are a rich and fascinating subject, and part of their charm comes from the fact that the group algebra of any Coxeter group admits a $q$-deformation, called a 'Hecke algebra', which has many of the properties of the original group (as expressed through its group algebra). The Hecke algebra again has one generator for each dot of the Dynkin diagram, now called $\sigma_d$. These generators obey the same relation for each edge that we had in the original Coxeter group. The only difference is that while the Coxeter group generators are reflections, and thus satisfy $s_d^2 = 1$, the Hecke algebra generators obey a $q$-deformed version of this equation: $$\sigma_d^2 = (q-1)\sigma_d + q  .$$

Where do Hecke algebras come from? They arise in a number of ways, but one enlightening description involves the theory of 'buildings', where each Dynkin diagram corresponds to a type of geometry [@Brown; @Garrett]. For example, the Dynkin diagram shown above (with $n$ dots) corresponds to the geometry of projective $n$-space. Projective $n$-space makes sense over any field, and when $q$ is a prime power, the Hecke algebra arises in the study of $n$-dimensional projective space over the field ${\mathbb F}_q$. We shall explain this in detail in the case of the projective plane. But the $n$-simplex can be thought of as a '$q \rightarrow 1$ limit' of an $n$-dimensional projective space over ${\mathbb F}_q$. The idea is that the vertices, edges, triangles, and so on of the $n$-simplex play the role of points, lines, planes, and so on in a degenerate sort of projective space. In this limiting case, the Hecke algebra reduces to the group algebra of the symmetric group. As it turns out, this fact can be understood more clearly when we *groupoidify* the Hecke algebra. We shall sketch the idea in this paper, and give more details in the next paper of this series. In the meantime, see [@Hoffnung].

Any Dynkin diagram also gives a geometry over the field $\mathbb{C}$, and the symmetries of this geometry form a simple Lie group. The symmetry transformations close to the identity are described by the Lie algebra ${\mathfrak g}$ of this group---or equally well, by the universal enveloping algebra $U{\mathfrak g}$, which is a Hopf algebra. This universal enveloping algebra admits a $q$-deformation, a Hopf algebra $U_q {\mathfrak g}$ known as a 'quantum group'. There has been a lot of work attempting to categorify quantum groups, from the early ideas of Crane and Frenkel [@CF], to the work of Khovanov, Lauda and Rouqier [@Kh2; @KL; @Rou2], and beyond.

Here we sketch how to groupoidify, not the whole quantum group, but only its 'positive part' $U_q^+ {\mathfrak g}$. When $q = 1$, this positive part is just the universal enveloping algebra of a chosen maximal nilpotent subalgebra of ${\mathfrak g}$. The advantage of restricting attention to the positive part is that $U_q^+ {\mathfrak g}$ has a basis in which the formula for the product involves only *nonnegative* real numbers---and any such number is the cardinality of some groupoid.

The strategy for groupoidifying $U_q^+ {\mathfrak g}$ is implicit in Ringel's work on Hall algebras [@Ringel]. Suppose we have a 'simply-laced' Dynkin diagram, meaning one where two generators of the Coxeter group obey the Yang-Baxter equation whenever the corresponding dots are connected by an edge. If we pick a direction for each edge of this Dynkin diagram, we obtain a directed graph. This in turn freely generates a category, say $Q$. The objects in this category are the dots of the Dynkin diagram, while the morphisms are paths built from directed edges.

For any prime power $q$, there is a category ${\rm Rep}(Q)$ whose objects are 'representations' of $Q$: that is, functors $$R \colon Q \rightarrow{\rm FinVect}_q,$$ where ${\rm FinVect}_q$ is the category of finite-dimensional vector spaces over ${\mathbb F}_q$. The morphisms in ${\rm Rep}(Q)$ are natural transformations. Thanks to the work of Ringel, one can see that the underlying groupoid of ${\rm Rep}(Q)$---which has only natural *isomorphisms* as morphisms---groupoidifies the vector space $U_q^+ {\mathfrak g}$. Even better, we can groupoidify the product in $U_q^+ {\mathfrak g}$. The same sort of construction with the category of pointed finite sets replacing ${\rm FinVect}_q$ lets us handle the $q = 1$ case [@Szczesny]. So yet again, $q$-deformation is related to the passage from pointed finite sets to finite-dimensional vector spaces over finite fields.

The plan of the paper is as follows. In Section [1](#degroupoidification){reference-type="ref" reference="degroupoidification"}, we present some basic facts about 'degroupoidification'. We describe a process that associates to any groupoid $X$ the vector space ${\mathbb R}^{\underline{X}}$ consisting of real-valued functions on the set of isomorphism classes of objects of $X$, and associates to any 'tame' span of groupoids a linear operator. In Section [\[homology\]](#homology){reference-type="ref" reference="homology"}, we describe a slightly different process, which associates to $X$ the vector space ${\mathbb R}[\underline{X}]$ consisting of formal linear combinations of isomorphism classes of objects of $X$. Then we turn to some applications. Section [\[feynman\]](#feynman){reference-type="ref" reference="feynman"} describes how to groupoidify the theory of Feynman diagrams, Section [\[hecke\]](#hecke){reference-type="ref" reference="hecke"} describes how to groupoidify the theory of Hecke algebras, and Section [\[hall\]](#hall){reference-type="ref" reference="hall"} describes how to groupoidify Hall algebras. In Section [\[processes\]](#processes){reference-type="ref" reference="processes"} we prove that degroupoidifying a tame span gives a well-defined linear operator. We also give an explicit criterion for when a span of groupoids is tame, and an explicit formula for the operator coming from a tame span. Section [\[properties\]](#properties){reference-type="ref" reference="properties"} proves many other results stated earlier in the paper. Appendix [\[appendix\]](#appendix){reference-type="ref" reference="appendix"} provides some basic definitions and useful lemmas regarding groupoids and spans of groupoids. The goal is to make it easy for readers to try their own hand at groupoidification.

# Degroupoidification

In this section we describe a systematic process for turning groupoids into vector spaces and tame spans into linear operators. This process, 'degroupoidification', is in fact a kind of functor. 'Groupoidification' is the attempt to *undo* this functor. To 'groupoidify' a piece of linear algebra means to take some structure built from vector spaces and linear operators and try to find interesting groupoids and spans that degroupoidify to give this structure. So, to understand groupoidification, we need to master degroupoidification.

We begin by describing how to turn a groupoid into a vector space. In what follows, all our groupoids will be **essentially small**. This means that they have a *set* of isomorphism classes of objects, not a proper class. We also assume our groupoids are **locally finite**: given any pair of objects, the set of morphisms from one object to the other is finite.

::: definition
Given a groupoid $X$, let $\underline{X}$ be the set of isomorphism classes of objects of $X$.
:::

::: definition
[]{#vectorspace label="vectorspace"} Given a groupoid $X$, let the **degroupoidification** of $X$ be the vector space $${\mathbb R}^{\underline{X}} = \lbrace \Psi \colon\underline{X} \rightarrow{\mathbb R}\rbrace.$$
:::

A nice example is the groupoid of finite sets and bijections:

::: example
[]{#power_series label="power_series"} [Let $E$ be the groupoid of finite sets and bijections. Then $\underline{E}\cong{\mathbb N}$, so $${\mathbb R}^{\underline{E}} \cong\lbrace \psi \colon{\mathbb N}\rightarrow{\mathbb R}\rbrace 
\cong {\mathbb R}[[z]] ,$$ where the formal power series associated to a function $\psi
\colon{\mathbb N}\rightarrow{\mathbb R}$ is given by: $$\sum_{n\in{\mathbb N}}\psi(n)z^n.$$]{.upright}
:::

A sufficiently nice groupoid over a groupoid $X$ will give a vector in ${\mathbb R}^{\underline{X}}$. To construct this, we use the concept of groupoid cardinality:

::: definition
The **cardinality** of a groupoid $X$ is $$|X| = \sum_{[x]\in \underline{X}} \frac{1}{|{\rm Aut}(x)|}$$ where $|{\rm Aut}(x)|$ is the cardinality of the automorphism group of an object $x$ in $X$. If this sum diverges, we say $|X| = \infty$.
:::

The cardinality of a groupoid $X$ is a well-defined nonnegative rational number whenever $\underline{X}$ and all the automorphism groups of objects in $X$ are finite. More generally, we say:

::: definition
A groupoid $X$ is **tame** if it is essentially small, locally finite, and $|X| < \infty$.
:::

We show in Lemma [\[EQUIVGRPD\]](#EQUIVGRPD){reference-type="ref" reference="EQUIVGRPD"} that given equivalent groupoids $X$ and $Y$, $|X| = |Y|$. We give a useful alternative formula for groupoid cardinality in Lemma [\[ALTCARD\]](#ALTCARD){reference-type="ref" reference="ALTCARD"}.

The reason we use ${\mathbb R}$ rather than ${\mathbb Q}$ as our ground field is that there are interesting groupoids whose cardinalities are irrational numbers. The following example is fundamental:

::: example
[The groupoid of finite sets $E$ has cardinality $$|E| ~=~ \sum_{n \in {\mathbb N}} \frac{1}{|S_n|} ~=~ 
\sum_{n \in {\mathbb N}} \frac{1}{n!} ~=~ e.$$]{.upright}
:::

With the concept of groupoid cardinality in hand, we now describe how to obtain a vector in ${\mathbb R}^{\underline{X}}$ from a sufficiently nice groupoid over $X$.

::: definition
Given a groupoid $X$, a **groupoid over $X$** is a groupoid $\Psi$ equipped with a functor $v \colon\Psi \rightarrow X$.
:::

::: definition
Given a groupoid over $X$, say $v \colon\Psi \rightarrow X$, and an object $x \in X$, we define the **full inverse image** of $x$, denoted $v^{-1}(x)$, to be the groupoid where:

-   an object is an object $a \in \Psi$ such that $v(a) \cong x$;

-   a morphism $f \colon a \rightarrow a'$ is any morphism in $\Psi$ from $a$ to $a'$.
:::

::: definition
A groupoid over $X$, say $v \colon\Psi \rightarrow X$, is **tame** if the groupoid $v^{-1}(x)$ is tame for all $x \in X$.
:::

We sometimes loosely say that $\Psi$ is a tame groupoid over $X$. When we do this, we are referring to a functor $v \colon\Psi \rightarrow X$ that is tame in the above sense. We do not mean that $\Psi$ is tame as a groupoid.

::: definition
[]{#degroupoidification_of_vectors label="degroupoidification_of_vectors"} Given a tame groupoid over $X$, say $v \colon\Psi\rightarrow X$, there is a vector $\utilde{\Psi} \in {\mathbb R}^{\underline{X}}$ defined by: $$\utilde{\Psi}([x]) = |v^{-1}(x)|.$$
:::

As discussed in Section [\[intro\]](#intro){reference-type="ref" reference="intro"}, the theory of generating functions gives many examples of this construction. Here is one:

::: example
[]{#generating_function label="generating_function"} [Let $\Psi$ be the groupoid of 2-colored finite sets. An object of $\Psi$ is a '2-colored finite set': that is a finite set $S$ equipped with a function $c: S \rightarrow 2$, where $2 = \{0,1\}$. A morphism of $\Psi$ is a function between 2-colored finite sets preserving the 2-coloring: that is, a commutative diagram of this sort: $$\xymatrix{
& S \ar[dr]_{c} \ar[rr]^{f} && S' \ar[dl]^{c'}  \\
 & & \{0,1\} & & 
}$$ There is a forgetful functor $v \colon\Psi \rightarrow E$ sending any 2-colored finite set $c \colon S \rightarrow 2$ to its underlying set $S$. It is a fun exercise to check that for any $n$-element set, say $n$ for short, the groupoid $v^{-1}(n)$ is equivalent to the weak quotient $2^n/\!/S_n$, where $2^n$ is the set of functions $c: n \rightarrow 2$ and the permutation group $S_n$ acts on this set in the obvious way. It follows that $$\utilde{\Psi}(n) = |v^{-1}(n)| = |2^n /\!/ S_n | = 2^n/n!$$ so the corresponding power series is $$\utilde{\Psi} = \sum_{n \in {\mathbb N}} \frac{2^n}{n!}z^n = 
e^{2z} \in {\mathbb R}[[z]].$$ We call this the **generating function** of $v \colon\Psi \rightarrow E$, and indeed it is the usual generating function for 2-colored sets. Note that the $n!$ in the denominator, often regarded as a convention, arises naturally from the use of groupoid cardinality.]{.upright}
:::

Both addition and scalar multiplication of vectors have groupoidified analogues. We can add two groupoids $\Phi$, $\Psi$ over $X$ by taking their coproduct, i.e., the disjoint union of $\Phi$ and $\Psi$ with the obvious map to $X$: $$\xymatrix{
\Phi + \Psi \ar[d] \\
X
}$$ We then have:

::: proposition*
Given tame groupoids $\Phi$ and $\Psi$ over $X$, $$\utilde{\Phi + \Psi} = \utilde{\Phi} + \utilde{\Psi}.$$
:::

::: proof
*Proof.* This will appear later as part of Lemma [\[addvectors\]](#addvectors){reference-type="ref" reference="addvectors"}, which also considers infinite sums. ◻
:::

We can also multiply a groupoid over $X$ by a 'scalar'---that is, a fixed groupoid. Given a groupoid over $X$, say $v \colon\Phi\rightarrow X$, and a groupoid $\Lambda$, the cartesian product $\Lambda\times \Psi$ becomes a groupoid over $X$ as follows: $$\xymatrix{
\Lambda\times \Psi \ar[d]^{v\pi_2}\\ X\\ }$$ where $\pi_2 \colon\Lambda\times \Psi\rightarrow\Psi$ is projection onto the second factor. We then have:

::: proposition*
Given a groupoid $\Lambda$ and a groupoid $\Psi$ over $X$, the groupoid $\Lambda \times \Psi$ over $X$ satisfies $$\utilde{\Lambda \times \Psi} = |\Lambda|\utilde{\Psi}.$$
:::

::: proof
*Proof.* This is proved as Proposition [\[scalarmult1\]](#scalarmult1){reference-type="ref" reference="scalarmult1"}. ◻
:::

We have seen how degroupoidification turns a groupoid $X$ into a vector space ${\mathbb R}^{\underline{X}}$. Degroupoidification also turns any sufficiently nice span of groupoids into a linear operator.

::: definition
Given groupoids $X$ and $Y$, a **span** from $X$ to $Y$ is a diagram $$\xymatrix{
 & S\ar[dl]_q\ar[dr]^p & \\
 Y & & X \\
}$$ where $S$ is groupoid and $p\colon S\rightarrow X$ and $q \colon S\rightarrow Y$ are functors.
:::

To turn a span of groupoids into a linear operator, we need a construction called the 'weak pullback'. This construction will let us apply a span from $X$ to $Y$ to a groupoid over $X$ to obtain a groupoid over $Y$. Then, since a tame groupoid over $X$ gives a vector in ${\mathbb R}^{\underline{X}}$, while a tame groupoid over $Y$ gives a vector in ${\mathbb R}^{\underline{Y}}$, a sufficiently nice span from $X$ to $Y$ will give a map from ${\mathbb R}^{\underline{X}}$ to ${\mathbb R}^{\underline{Y}}$. Moreover, this map will be linear.

As a warmup for understanding weak pullbacks for groupoids, we recall ordinary pullbacks for sets, also called 'fibered products'. The data for constructing such a pullback is a pair of sets equipped with functions to the same set: $$\xymatrix{
& T \ar[dr]_{q} & & S \ar[dl]^{p} & \\
 & & X & & 
}$$ The pullback is the set $$P = \lbrace (s,t) \in S \times T \, | \; p(s) = q(t) \rbrace$$ together with the obvious projections $\pi_S \colon P \rightarrow S$ and $\pi_T \colon P \rightarrow T$. The pullback makes this diamond commute: $$\xymatrix{
& & P \ar[dl]_{\pi_T} \ar[dr]^{\pi_S} & &\\
& T \ar[dr]_{q} & & S \ar[dl]^{p} & \\
 & & X & & 
}$$ and indeed it is the 'universal solution' to the problem of finding such a commutative diamond [@Mac; @Lane].

To generalize the pullback to groupoids, we need to weaken one condition. The data for constructing a weak pullback is a pair of groupoids equipped with functors to the same groupoid: $$\xymatrix{
& T \ar[dr]_{q} & & S \ar[dl]^{p} & \\
 & & X & & 
}$$ But now we replace the *equation* in the definition of pullback by a *specified isomorphism*. So, we define the weak pullback $P$ to be the groupoid where an object is a triple $(s,t,\alpha)$ consisting of an object $s \in S$, an object $t \in T$, and an isomorphism $\alpha \colon p(s) \rightarrow q(t)$ in $X$. A morphism in $P$ from $(s,t,\alpha)$ to $(s',t',\alpha')$ consists of a morphism $f \colon s \rightarrow s'$ in $S$ and a morphism $g \colon t \rightarrow t'$ in $T$ such that the following square commutes: $$\xymatrix{
p(s) \ar[d]_{p(f)} \ar[r]^{\alpha} & q(t) \ar[d]^{q(g)} \\
p(s') \ar[r]_{\alpha'} & q(t')
}$$ Note that any set can be regarded as a **discrete** groupoid: one with only identity morphisms. For discrete groupoids, the weak pullback reduces to the ordinary pullback for sets. Using the weak pullback, we can apply a span from $X$ to $Y$ to a groupoid over $X$ and get a groupoid over $Y$. Given a span of groupoids: $$\xymatrix{
& S\ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ and a groupoid over $X$: $$\xymatrix{
   & \Psi \ar[dl]_{v} \\
   X &  
}$$ we can take the weak pullback, which we call $S\Psi$: $$\xymatrix{
& & S\Psi \ar[dl]_{\pi_S}\ar[dr]^{\pi_{\Psi}} & \\
& S \ar[dl]_{q} \ar[dr]^{p} & & \Psi \ar[dl]_{v} \\
Y & & X &  
}$$ and think of $S\Psi$ as a groupoid over $Y$: $$\xymatrix{
& S\Psi \ar[dl]_{q \pi_S}  \\
Y  
}$$ This process will determine a linear operator from ${\mathbb R}^{\underline{X}}$ to ${\mathbb R}^{\underline{Y}}$ if the span $S$ is sufficiently nice:

::: definition
A span $$\xymatrix{
& S\ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ is **tame** if $v \colon\Psi \rightarrow X$ being tame implies that $q\pi_{S} \colon S\Psi \rightarrow Y$ is tame.
:::

::: theorem*
Given a tame span: $$\xymatrix{
& S\ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ there exists a unique linear operator $$\utilde{S} \colon{\mathbb R}^{\underline{X}} \rightarrow{\mathbb R}^{\underline{Y}}$$ such that $$\utilde{S}\utilde{\Psi} = \utilde{S\Psi}$$ whenever $\Psi$ is a tame groupoid over $X$.
:::

::: proof
*Proof.* This is Theorem [\[PROCESS1\]](#PROCESS1){reference-type="ref" reference="PROCESS1"}. ◻
:::

Theorem [\[matrix1\]](#matrix1){reference-type="ref" reference="matrix1"} provides an explicit criterion for when a span is tame. This theorem also gives an explicit formula for the the operator corresponding to a tame span $S$ from $X$ to $Y$. If $\underline{X}$ and $\underline{Y}$ are finite, then ${\mathbb R}^{\underline{X}}$ has a basis given by the isomorphism classes $[x]$ in $X$, and similarly for ${\mathbb R}^{\underline{Y}}$. With respect to these bases, the matrix entries of $\utilde{S}$ are given as follows: $$\label{matrix_entry}
\utilde{S}_{[y][x]} = 
\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)} }\frac{|{\rm Aut}(x)|}{|{\rm Aut}(s)|}$$ where $|{\rm Aut}(x)|$ is the set cardinality of the automorphism group of $x \in X$, and similarly for $|{\rm Aut}(s)|$. Even when $\underline{X}$ and $\underline{Y}$ are not finite, we have the following formula for $\utilde S$ applied to $\psi \in {\mathbb R}^{\underline{X}}$: $$\label{operator_formula}
(\utilde{S} \psi)([y]) = 
\sum_{[x] \in \underline{X}} \;\,
\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)}}
\frac{|{\rm Aut}(x)|}{|{\rm Aut}(s)|} \,\, \psi([x]) \, .$$

As with vectors, there are groupoidified analogues of addition and scalar multiplication for operators. Given two spans from $X$ to $Y$: $$\xymatrix{
& S\ar[dl]_{q_S} \ar[dr]^{p_S} & & & T\ar[dl]_{q_T} \ar[dr]^{p_T} & \\
Y & & X & Y & & X
}$$ we can add them as follows. By the universal property of the coproduct we obtain from the right legs of the above spans a functor from the disjoint union $S + T$ to $X$. Similarly, from the left legs of the above spans, we obtain a functor from $S + T$ to $Y$. Thus, we obtain a span $$\xymatrix{
& S + T\ar[dl] \ar[dr] & \\
Y & & X
}$$ This addition of spans is compatible with degroupoidification:

::: proposition*
If $S$ and $T$ are tame spans from $X$ to $Y$, then so is $S + T$, and $$\utilde{S+T} = \utilde{S} + \utilde{T} .$$
:::

::: proof
*Proof.* This is proved as Proposition [\[add_spans\]](#add_spans){reference-type="ref" reference="add_spans"}. ◻
:::

We can also multiply a span by a 'scalar': that is, a fixed groupoid. Given a groupoid $\Lambda$ and a span $$\xymatrix{
& S\ar[dl]_q \ar[dr]^p & \\
Y & & X
}$$ we can multiply them to obtain a span $$\xymatrix{
& \Lambda \times S \ar[dl]_{q\pi_2} \ar[dr]^{p\pi_2} & \\
Y & & X
}$$ Again, we have compatibility with degroupoidification:

::: proposition*
Given a tame groupoid $\Lambda$ and a tame span $$\xymatrix{
& S\ar[dl] \ar[dr] & \\
Y & & X
}$$ then $\Lambda \times S$ is tame and $$\utilde{\Lambda \times S} = |\Lambda| \, \utilde{S}.$$
:::

::: proof
*Proof.* This is proved as Proposition [\[scalarmult2\]](#scalarmult2){reference-type="ref" reference="scalarmult2"}. ◻
:::

Next we turn to the all-important process of *composing* spans. This is the groupoidified analogue of matrix multiplication. Suppose we have a span from $X$ to $Y$ and a span from $Y$ to $Z$: $$\xymatrix{
& T\ar[dl]_{q_T} \ar[dr]^{p_T} & & S \ar[dl]_{q_S} \ar[dr]^{p_S}& \\
Z & & Y & & X
}$$ Then we say these spans are **composable**. In this case we can form a weak pullback in the middle: $$\xymatrix{
& & TS \ar[dl]_{\pi_T} \ar[dr]^{\pi_S} & &\\
& T\ar[dl]_{q_T} \ar[dr]^{p_T} & & S \ar[dl]_{q_S} \ar[dr]^{p_S}& \\
Z & & Y & & X
}$$ which gives a span from $X$ to $Z$: $$\xymatrix{
 & TS \ar[dl]_{q_T \pi_T} \ar[dr]^{p_S\pi_S} & \\
 Z & & X \\
}$$ called the **composite** $TS$.

When all the groupoids involved are discrete, the spans $S$ and $T$ are just matrices of sets, as explained in Section [\[intro\]](#intro){reference-type="ref" reference="intro"}. We urge the reader to check that in this case, the process of composing spans is really just matrix multiplication, with cartesian product of sets taking the place of multiplication of numbers, and disjoint union of sets taking the place of addition: $$(TS)^k_j = \coprod_{j \in Y} T^k_j \times S^j_i .$$ So, composing spans of groupoids is a generalization of matrix multiplication, with weak pullback playing the role of summing over the repeated index $j$ in the formula above.

So, it should not be surprising that degroupoidification sends a composite of tame spans to the composite of their corresponding operators:

::: proposition*
If $S$ and $T$ are composable tame spans: $$\xymatrix{
& T\ar[dl]_{q_T} \ar[dr]^{p_T} & & S \ar[dl]_{q_S} \ar[dr]^{p_S}& \\
Z & & Y & & X
}$$ then the composite span $$\xymatrix{
 & TS \ar[dl]_{q_T \pi_T} \ar[dr]^{p_S\pi_S} & \\
 Z & & X \\
}$$ is also tame, and $$\utilde{TS} = \utilde{T} \utilde{S}  .$$
:::

::: proof
*Proof.* This is proved as Lemma [\[composition\]](#composition){reference-type="ref" reference="composition"}. ◻
:::

Besides addition and scalar multiplication, there is an extra operation for groupoids over a groupoid $X$, which is the reason groupoidification is connected to quantum mechanics. Namely, we can take their inner product:

::: definition
Given groupoids $\Phi$ and $\Psi$ over $X$, we define the **inner product** $\langle \Phi,\Psi \rangle$ to be this weak pullback: $$\xymatrix{
& \langle \Phi,\Psi \rangle \ar[dl] \ar[dr] & \\
\Phi \ar[dr] & & \Psi \ar[dl] \\
& X &
}$$
:::

::: definition
[]{#L2 label="L2"} A groupoid $\Psi$ over $X$ is called **square-integrable** if $\langle \Psi,\Psi \rangle$ is tame. We define $L^2(X)$ to be the subspace of ${\mathbb R}^{\underline{X}}$ consisting of finite real linear combinations of vectors $\utilde{\Psi}$ where $\Psi$ is square-integrable.
:::

Note that $L^2(X)$ is all of ${\mathbb R}^{\underline{X}}$ when $\underline{X}$ is finite. The inner product of groupoids over $X$ makes $L^2(X)$ into a real Hilbert space:

::: theorem*
Given a groupoid $X$, there is a unique inner product $\langle \cdot,\cdot \rangle$ on the vector space $L^2(X)$ such that $$\langle \utilde{\Phi},\utilde{\Psi} \rangle = |\langle \Phi,\Psi \rangle|$$ whenever $\Phi$ and $\Psi$ are square-integrable groupoids over $X$. With this inner product $L^2(X)$ is a real Hilbert space.
:::

::: proof
*Proof.* This is proven later as Theorem [\[innerprod_theorem\]](#innerprod_theorem){reference-type="ref" reference="innerprod_theorem"}. ◻
:::

We can always complexify $L^2(X)$ and obtain a complex Hilbert space. We work with real coefficients simply to admit that groupoidification as described here does not make essential use of the complex numbers. Morton's generalization involving groupoids over ${\rm U}(1)$ is one way to address this issue [@Morton:2006].

The inner product of groupoids over $X$ has the properties one would expect:

::: proposition*
Given a groupoid $\Lambda$ and square-integrable groupoids $\Phi$, $\Psi$, and $\Psi'$ over $X$, we have the following equivalences of groupoids:

1.  $$\langle \Phi,\Psi \rangle \simeq \langle \Psi,\Phi \rangle.$$

2.  $$\langle \Phi,\Psi + \Psi' \rangle \simeq \langle \Phi,\Psi \rangle + \langle \Phi,\Psi' \rangle.$$

3.  $$\langle \Phi,\Lambda \times \Psi \rangle \simeq \Lambda \times \langle \Phi,\Psi \rangle.$$
:::

::: proof
*Proof.* Here equivalence of groupoids is defined in the usual way---see Definition [\[equivalence_of_groupoids\]](#equivalence_of_groupoids){reference-type="ref" reference="equivalence_of_groupoids"}. This result is proved below as Proposition [\[innerprodandadjointprops\]](#innerprodandadjointprops){reference-type="ref" reference="innerprodandadjointprops"}. ◻
:::

Just as we can define the adjoint of an operator between Hilbert spaces, we can define the adjoint of a span of groupoids:

::: definition
Given a span of groupoids from $X$ to $Y$: $$\xymatrix{
& S\ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ its **adjoint** $S^{\dagger}$ is the following span of groupoids from $Y$ to $X$: $$\xymatrix{
& S\ar[dl]_{p} \ar[dr]^{q} & \\
X & & Y
}$$
:::

We warn the reader that the adjoint of a tame span may not be tame, due to an asymmetry in the criterion for tameness, Theorem [\[matrix1\]](#matrix1){reference-type="ref" reference="matrix1"}. But of course a span of finite groupoids is tame, and so is its adjoint. Moreover, we have:

::: proposition*
Given a span $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ and a pair $v \colon\Psi \rightarrow X$, $w \colon\Phi \rightarrow Y$ of groupoids over $X$ and $Y$, respectively, there is an equivalence of groupoids $$\langle \Phi,S\Psi \rangle 
\simeq \langle S^\dagger\Phi,\Psi \rangle.$$
:::

::: proof
*Proof.* This is proven as Proposition [\[innerprod_adjoint\]](#innerprod_adjoint){reference-type="ref" reference="innerprod_adjoint"}. ◻
:::

We say what it means for spans to be 'equivalent' in Definition [\[EQUIVALENCE\]](#EQUIVALENCE){reference-type="ref" reference="EQUIVALENCE"}. Equivalent tame spans give the same linear operator: $S \simeq T$ implies $\utilde{S} = \utilde{T}$. Spans of groupoids obey many of the basic laws of linear algebra---up to equivalence. For example, we have these familiar properties of adjoints:

::: proposition*
Given spans $$\xymatrix{
& T \ar[dl]_{q_T} \ar[dr]^{p_T} & & & S \ar[dl]_{q_S} \ar[dr]^{p_S} & \\
Z & & Y & Y & & X
}$$ and a groupoid $\Lambda$, we have the following equivalences of spans:

1.  $(TS)^\dagger \simeq S^\dagger T^\dagger$

2.  $(S+T)^\dagger \simeq S^\dagger + T^\dagger$

3.  $(\Lambda S)^\dagger \simeq \Lambda S^\dagger$
:::

::: proof
*Proof.* These will follow easily after we show addition and composition of spans and scalar multiplication are well defined. ◻
:::

In fact, degroupoidification is a functor $$\utilde{\;\;\;} \,\colon{\rm Span}\rightarrow{\rm Vect}$$ where ${\rm Vect}$ is the category of real vector spaces and linear operators, and ${\rm Span}$ is a category with

-   groupoids as objects,

-   equivalence classes of tame spans as morphisms,

where composition comes from the method of composing spans we have just described. We prove this fact in Theorem [\[functor\]](#functor){reference-type="ref" reference="functor"}. A deeper approach, which we shall explain elsewhere, is to think of ${\rm Span}$ as a weak 2-category (i.e., bicategory) with:

-   groupoids as objects,

-   tame spans as morphisms,

-   isomorphism classes of maps of spans as 2-morphisms

Then degroupoidification becomes a functor between weak 2-categories: $$\utilde{\;\;} \, \colon{\rm Span}\rightarrow{\rm Vect}$$ where ${\rm Vect}$ is viewed as a weak 2-category with only identity 2-morphisms. So, groupoidification is not merely a way of replacing linear algebraic structures involving the real numbers with purely combinatorial structures. It is also a form of 'categorification' [@BaezDolan:1998], where we take structures defined in the category ${\rm Vect}$ and find analogues that live in the weak 2-category ${\rm Span}$.

We could go even further and think of ${\rm Span}$ as a weak 3-category with

-   groupoids as objects,

-   tame spans as morphisms,

-   maps of spans as 2-morphisms,

-   maps of maps of spans as 3-morphisms.

However, we have not yet found a use for this further structure.

Lastly we would like to say a few words about tensors and traces. We can define the **tensor product** of groupoids $X$ and $Y$ to be their cartesian product $X \times Y$, and the **tensor product** of spans $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p} & & & S' \ar[dl]_{q'} \ar[dr]^{p'} & \\
Y & & X & Y' & & X'
}$$ to be the span $$\xy
(0,15)*{S\times S'}="B";(-15,0)*{Y\times Y'}="A";(15,0)*{X\times X'}="C";
{\ar_{q \times q'} (-2,13);(-13,2)};
{\ar^{p \times p'} (2,13);(13,2)};
\endxy$$ Defining the tensor product of maps of spans in a similar way, we conjecture that ${\rm Span}$ actually becomes a *symmetric monoidal* weak 2-category[@McCrudden]. If this is true, then degroupoidification should be a 'lax symmetric monoidal functor', thanks to the natural map $${\mathbb R}^{\underline{X}} \otimes{\mathbb R}^{\underline{Y}} \rightarrow{\mathbb R}^{\underline{X \times Y}} \, .$$ The word 'lax' refers to the fact that this map is not an isomorphism of vector spaces unless either $X$ or $Y$ has finitely many isomorphism classes of objects. In the next section we present an alternative approach to degroupoidification that avoids this problem. The idea is simple: instead of working with the vector space ${\mathbb R}^{\underline{X}}$ consisting of all functions on $\underline{X}$, we work with the vector space ${\mathbb R}[\underline{X}]$ having $\underline{X}$ as its basis. Then we have $${\mathbb R}[\underline{X}] \otimes{\mathbb R}[\underline{Y}] \cong{\mathbb R}[\underline{X \times Y}]  .$$ In fact both approaches to groupoidification have their own advantages, and they are closely related, since $${\mathbb R}^{\underline{X}} \cong{\mathbb R}[\underline{X}]^*  \, .$$

Regardless of these nuances, the important thing about the 'monoidal' aspect of degroupoidification is that it lets us mimic all the usual manipulations for tensors with groupoids replacing vector spaces. Physicists call a linear map $$S \colon V_1 \otimes\cdots \otimes V_m \rightarrow
                    W_1 \otimes\cdots \otimes W_n$$ a **tensor**, and denote it by an expression $$S^{j_1 \cdots j_n}_{i_1 \cdots i_m}$$ with one subscript for each 'input' vector space $V_1, \dots, V_m$, and one superscript for each 'output' vector space $W_1, \dots, W_n$. In the traditional approach to tensors, these indices label bases of the vector spaces in question. Then the expression $S^{j_1 \cdots
j_n}_{i_1 \cdots i_m}$ stands for an array of numbers: the components of the tensor $S$ with respect to the chosen bases. This lets us describe various operations on tensors by multiplying such expressions and summing over indices that appear repeatedly, once as a superscript and once as a subscript. In the more modern 'string diagram' approach, these indices are simply names of input and output wires for a black box labelled $S$:

::: center
::: picture
(60,115)(0,-10) ![image](transformation.eps) (-62,-5)$i_1$ (-43,-9)$i_2$ (-20,-9)$i_3$ (-1,-5)$i_4$ (-51,96)$j_1$ (-33,98)$j_2$ (-14,96)$j_3$ (-32,44)$S$
:::
:::

Here we are following physics conventions, where inputs are at the bottom and outputs are at the top. In this approach, when an index appears once as a superscript and once as a subscript, it means we attach an output wire of one black box to an input of another.

The most famous example is matrix multiplication: $$(TS)^k_i = T_j^k S_i^j.$$ Here is the corresponding string diagram:

::: center
::: picture
(60,110)(-20,0) ![image](composite.eps) (-20,94)$k$ (-20,50)$j$ (-20,8)$i$ (-16,71)$T$ (-16,28)$S$
:::
:::

Another famous example is the trace of a linear operator $S \colon V \rightarrow V$, which is the sum of its diagonal entries: $${\rm tr}(S) = S^i_i$$ As a string diagram, this looks like:

::: center
::: picture
(60,120)(12,0) ![image](trace.eps) (-51,66)$i$ (-51,16)$i$ (-49,40)$S$
:::
:::

Here the sum is only guaranteed to converge if $V$ is finite-dimensional, and indeed the full collection of tensor operations is defined only for finite-dimensional vector spaces.

All these ideas work just as well with spans of groupoids $$\xy
(0,15)*{S}="B";(-15,0)*{Y_1 \times \cdots \times Y_n}="A";(15,0)*{X_1 \times \cdots \times X_m}="C";
{\ar_{q} (-2,13);(-13,2)};
{\ar^{p} (2,13);(13,2)};
\endxy$$ taking the place of tensors. The idea is that *weak pullback takes the place of summation over repeated indices*. Even better, there is no need to impose any finiteness or tameness conditions until we degroupoidify.

We have already seen the simplest example: composition of spans via weak pullback is a generalization of matrix multiplication. For a trickier one, emphasized by Urs Schreiber [@Urs], consider the trace of a span: $$\xymatrix{
& S \ar[dl]_q \ar[dr]^p & \\
X & & X  
}$$ Here it is a bit hard to see which weak pullback to do! We can get around this problem using an alternate formula for the trace of a linear map $S \colon V \rightarrow V$: $$\label{trace}
            {\rm tr}(S) = g_{jk} S^j_i g^{ik}$$ Here $g_{jk}$ is the tensor corresponding to an arbitrary inner product $g \colon V \otimes V \rightarrow{\mathbb R}$. In the finite-dimensional case, any such inner product determines an isomorphism $V \cong V^*$, so we can interpret the adjoint of $g$ as a linear map $\tilde{g} \colon{\mathbb R}\rightarrow
V \otimes V$, and the tensor for this is customarily written as $g$ with superscripts: $g^{ik}$. Equation [\[trace\]](#trace){reference-type="ref" reference="trace"} says that the operator $${\mathbb R}\stackrel{\tilde{g}}{\longrightarrow}
        V \otimes V \stackrel{S \otimes 1}{\longrightarrow}
        V \otimes V \stackrel{g}{\longrightarrow}
       {\mathbb R}$$ is multiplication by ${\rm tr}(S)$. We can draw $g$ as a 'cup' and $\tilde{g}$ as a 'cap', giving this string diagram:

::: center
::: picture
(60,120)(12,0) ![image](trace.eps) (-0,66)$k$ (-0,17)$k$ (-51,66)$j$ (-51,17)$i$ (-49,40)$S$
:::
:::

Now let us see how to implement this formula for the trace at the groupoidified level, to define the trace of a span of groupoids. Any groupoid $X$ automatically comes equipped with a span $$\xy
(0,15)*{\emph{ }X\emph{ }}="B";(-15,0)*{1}="A";(15,0)*{X\times X}="C";
{\ar_{} (-2,13);(-13,2)};
{\ar^{\Delta} (2,13);(13,2)};
\endxy$$ where $\Delta$ is the diagonal map and the left-hand arrow is the unique functor to the **terminal groupoid**---that is, the groupoid $1$ with one object and one morphism. We can check that at least when $\underline{X}$ is finite, degroupoidifying this span gives an operator $$\begin{array}{cccl}
g \colon& {\mathbb R}^{\underline{X}} \otimes{\mathbb R}^{\underline{X}} & \rightarrow& {\mathbb R}\\
        &  \phi \otimes\psi        & \mapsto & \langle \phi, \psi \rangle 
\end{array}$$ corresponding to the already described inner product on ${\mathbb R}^{\underline{X}}$. Similarly, the span $$\xy
(0,15)*{\emph{ }X\emph{ }}="B";(-15,0)*{X\times X}="A";(15,0)*{1}="C";
{\ar_{} (-2,13);(-13,2)};
{\ar^{\Delta} (2,13);(13,2)};
\endxy$$ degroupoidifies to give the operator $$\tilde{g} \colon{\mathbb R}\rightarrow{\mathbb R}^{\underline{X}} \otimes{\mathbb R}^{\underline{X}} \, .$$ So, to implement Equation [\[trace\]](#trace){reference-type="ref" reference="trace"} at the level of groupoids and define the trace of this span: $$\xymatrix{
& S \ar[dl]_q \ar[dr]^p & \\
X & & X  
}$$ we should take the composite of these three spans: $$\xy
(0,15)*{S \times X}="B";(-15,0)*{X\times X}="A";(15,0)*{X\times X}="C";
{\ar_{q\times 1} (-2,13);(-13,2)};
{\ar^{p\times 1} (2,13);(13,2)};
(-30,15)*{X}="D";(-45,0)*{1}="E";
{\ar_{} (-32,13);(-43,2)};
{\ar^{\Delta} (-28,13);(-17,2)};
(30,15)*{X}="F";(45,0)*{1}="G";
{\ar_{\Delta} (28,13);(17,2)};
{\ar^{} (32,13);(43,2)};
\endxy$$ The result is a span from $1$ to $1$, whose apex is a groupoid we define to be the **trace** ${\rm tr}(S)$. We leave it as an exercise to check the following basic properties of the trace:

::: proposition*
Given a span of groupoids $$\xymatrix{
& S \ar[dl]_q \ar[dr]^p & \\
X & & X  
}$$ its trace ${\rm tr}(S)$ is equivalent to the groupoid for which:

-   an object is a pair $(s,\alpha)$ consisting of an object $s \in S$ and a morphism $\alpha \colon p(s) \rightarrow q(s)$;

-   a morphism from $(s,\alpha)$ to $(s',\alpha')$ is a morphism $f \colon s \rightarrow s'$ such that $$\xymatrix{
    p(s) \ar[d]_{p(f)} \ar[r]^{\alpha} & q(s) \ar[d]^{q(f)} \\
    p(s') \ar[r]_{\alpha'} & q(s')
    }$$ commutes.
:::

::: proposition*
Given a span of groupoids $$\xymatrix{
& S \ar[dl]_q \ar[dr]^p & \\
X & & X  
}$$ where $\underline{X}$ is finite, we have $$|{\rm tr}(S)| = {\rm tr}({\utilde{S}}) .$$
:::

::: proposition*
Given spans of groupoids $$\xymatrix{
& S \ar[dl]_{q_S} \ar[dr]^{p_S} & & & T \ar[dl]_{q_T} \ar[dr]^{p_T} & \\
X & & X & X & & X
}$$ and a groupoid $\Lambda$, we have the following equivalences of groupoids:

1.  ${\rm tr}(S + T) \simeq {\rm tr}(S) + {\rm tr}(T)$

2.  ${\rm tr}(\Lambda \times S) \simeq \Lambda \times {\rm tr}(S)$
:::

::: proposition*
Given spans of groupoids $$\xymatrix{
& T \ar[dl]_{q_T} \ar[dr]^{p_T} & & & S \ar[dl]_{q_S} \ar[dr]^{p_S} & \\
X & & Y & Y & & X
}$$ we have an equivalence of groupoids $${\rm tr}(ST) \simeq {\rm tr}(TS) .$$
:::

We could go even further generalizing ideas from vector spaces and linear operators to groupoids and spans, but at this point the reader is probably hungry for some concrete applications. For these, proceed directly to Section [\[applications\]](#applications){reference-type="ref" reference="applications"}. Section [\[homology\]](#homology){reference-type="ref" reference="homology"} can be skipped on first reading, since we need it only for the application to Hall algebras in Section [\[hall\]](#hall){reference-type="ref" reference="hall"}.
