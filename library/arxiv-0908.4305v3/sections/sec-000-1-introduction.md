---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.996
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
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

The plan of the paper is as follows. In Section [\[degroupoidification\]](#degroupoidification){reference-type="ref" reference="degroupoidification"}, we present some basic facts about 'degroupoidification'. We describe a process that associates to any groupoid $X$ the vector space ${\mathbb R}^{\underline{X}}$ consisting of real-valued functions on the set of isomorphism classes of objects of $X$, and associates to any 'tame' span of groupoids a linear operator. In Section [\[homology\]](#homology){reference-type="ref" reference="homology"}, we describe a slightly different process, which associates to $X$ the vector space ${\mathbb R}[\underline{X}]$ consisting of formal linear combinations of isomorphism classes of objects of $X$. Then we turn to some applications. Section [\[feynman\]](#feynman){reference-type="ref" reference="feynman"} describes how to groupoidify the theory of Feynman diagrams, Section [\[hecke\]](#hecke){reference-type="ref" reference="hecke"} describes how to groupoidify the theory of Hecke algebras, and Section [\[hall\]](#hall){reference-type="ref" reference="hall"} describes how to groupoidify Hall algebras. In Section [\[processes\]](#processes){reference-type="ref" reference="processes"} we prove that degroupoidifying a tame span gives a well-defined linear operator. We also give an explicit criterion for when a span of groupoids is tame, and an explicit formula for the operator coming from a tame span. Section [\[properties\]](#properties){reference-type="ref" reference="properties"} proves many other results stated earlier in the paper. Appendix [\[appendix\]](#appendix){reference-type="ref" reference="appendix"} provides some basic definitions and useful lemmas regarding groupoids and spans of groupoids. The goal is to make it easy for readers to try their own hand at groupoidification.
