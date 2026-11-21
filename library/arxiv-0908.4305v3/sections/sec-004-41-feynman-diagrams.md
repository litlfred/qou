---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-004-41-feynman-diagrams
section_title: "Feynman Diagrams"
section_number: 4.1
pages: 29-36
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.98
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
[]{#feynman label="feynman"}

One of the first steps in developing quantum theory was Planck's new treatment of electromagnetic radiation. Classically, electromagnetic radiation in a box can be described as a collection of harmonic oscillators, one for each vibrational mode of the field in the box. Planck 'quantized' the electromagnetic field by assuming that the energy of each oscillator could only take discrete, evenly spaced values: if by fiat we say the lowest possible energy is $0$, the allowed energies take the form $n \hbar \omega$, where $n$ is any natural number, $\omega$ is the frequency of the oscillator in question, and $\hbar$ is Planck's constant.

Planck did not know what to make of the number $n$, but Einstein and others later interpreted it as the number of 'quanta' occupying the vibrational mode in question. However, far from being particles in the traditional sense of tiny billiard balls, quanta are curiously abstract entities---for example, all the quanta occupying a given mode are indistinguishable from each other.

In a modern treatment, states of a quantized harmonic oscillator are described as vectors in a Hilbert space called 'Fock space'. This Hilbert space consists of formal power series. For a full treatment of the electromagnetic field we would need power series in many variables, one for each vibrational mode. But to keep things simple, let us consider power series in one variable. In this case, the vector $z^n/n!$ describes a state in which $n$ quanta are present. A general vector in Fock space is a convergent linear combination of these special vectors. More precisely, the **Fock space** consists of $\psi \in {\mathbb C}[[z]]$ with $\langle \psi, \psi \rangle < 
\infty$, where the inner product is given by $$\label{fock_inner_product} 
         \left\langle 
         \sum a_n z^n \, , \,
         \sum b_n z^n 
         \right\rangle 
\; = \;
\sum n! \,\,  \overline{a}_n b_n \, .$$

But what is the meaning of this inner product? It is precisely the inner product in $L^2(E)$, where $E$ is the groupoid of finite sets! This is no coincidence. In fact, there is a deep relationship between the mathematics of the quantum harmonic oscillator and the combinatorics of finite sets. This relation suggests a program of *groupoidifying* mathematical tools from quantum theory, such as annihilation and creation operators, field operators and their normal-ordered products, Feynman diagrams, and so on. This program was initiated by Dolan and one of the current authors [@BaezDolan:2001]. Later, it was developed much further by Morton [@Morton:2006]. Guta and Maassen [@GM:2002] and Aguiar and Maharam [@AM:2008] have also done relevant work. Here we just sketch some of the basic ideas.

First, let us see why the inner product on Fock space matches the inner product on $L^2(E)$ as described in Theorem [\[innerprod_theorem\]](#innerprod_theorem){reference-type="ref" reference="innerprod_theorem"}. We can compute the latter inner product using a convenient basis. Let $\Psi_n$ be the groupoid with $n$-element sets as objects and bijections as morphisms. Since all $n$-element sets are isomorphic and each one has the permutation group $S_n$ as automorphisms, we have an equivalence of groupoids $$\Psi_n \simeq 1 /\!/S_n .$$ Furthermore, $\Psi_n$ is a groupoid over $E$ in an obvious way: $$v \colon\Psi_n \rightarrow E .$$ We thus obtain a vector $\utilde{\Psi}_n \in {\mathbb R}^{\underline{E}}$ following the rule described in Definition [\[degroupoidification_of_vectors\]](#degroupoidification_of_vectors){reference-type="ref" reference="degroupoidification_of_vectors"}. We can describe this vector as a formal power series using the isomorphism $${\mathbb R}^{\underline{E}} \cong {\mathbb R}[[z]]$$ described in Example [\[power_series\]](#power_series){reference-type="ref" reference="power_series"}. To do this, note that $$v^{-1} (m) \simeq 
\begin{cases}
 1 /\!/S_n  &  m = n  \\
  0         &  m \ne n 
\end{cases}$$ where $0$ stands for the empty groupoid. It follows that $$|v^{-1} (m)| =
\begin{cases}
  1/n!  &  m = n  \\
  0         &  m \ne n 
\end{cases}$$ and thus $$\utilde{\Psi}_n = \sum_{m \in {\mathbb N}} |v^{-1}(m)| \, z^m = 
\frac{z^n}{n!}  .$$

Next let us compute the inner product in $L^2(E)$. Since finite linear combinations of vectors of the form $\utilde{\Psi}_n$ are dense in $L^2(E)$ it suffices to compute the inner product of two vectors of this form. We can use the recipe in Theorem [\[innerprod_theorem\]](#innerprod_theorem){reference-type="ref" reference="innerprod_theorem"}. So, we start by taking the weak pullback of the corresponding groupoids over $E$: $$\xymatrix{
& \langle \Psi_m,\Psi_n \rangle \ar[dl] \ar[dr] & \\
\Psi_m \ar[dr] & & \Psi_n \ar[dl] \\
& E &
}$$ An object of this weak pullback consists of an $m$-element set $S$, an $n$-element set $T$, and a bijection $\alpha \colon S \rightarrow T$. A morphism in this weak pullback consists of a commutative square of bijections: $$\xymatrix{
S \ar[d]_{f} \ar[r]^{\alpha} & T \ar[d]^{g} \\
S' \ar[r]_{\alpha'} & T'
}$$ So, there are no objects in $\langle \Psi_m,\Psi_n \rangle$ when $n \ne m$. When $n = m$, all objects in this groupoid are isomorphic, and each one has $n!$ automorphisms. It follows that $$\langle \utilde{\Psi}_m, \utilde{\Psi}_n \rangle = 
| \langle \Psi_m, \Psi_n \rangle | = 
\begin{cases}
 1/n! &  m = n  \\
  0           & m \ne n 
\end{cases}$$ Using the fact that $\utilde{\Psi}_n = z^n/n!$, we see that this is precisely the inner product in Equation [\[fock_inner_product\]](#fock_inner_product){reference-type="ref" reference="fock_inner_product"}. So, as a complex Hilbert space, Fock space is the complexification of $L^2(E)$.

It is worth reflecting on the meaning of the computation we just did. The vector $\utilde{\Psi}_n = z^n/n!$ describes a state of the quantum harmonic oscillator in which $n$ quanta are present. Now we see that this vector arises from the groupoid $\Psi_n$ over $E$. In Section [\[intro\]](#intro){reference-type="ref" reference="intro"} we called a groupoid over $E$ a **stuff type**, since it describes a way of equipping finite sets with extra stuff. The stuff type $\Psi_n$ is a very simple special case, where the stuff is simply 'being an $n$-element set'. So, groupoidification reveals the mysterious 'quanta' to be simply elements of finite sets. Moreover, the formula for the inner product on Fock space arises from the fact that there are $n!$ ways to identify two $n$-element sets.

The most important operators on Fock space are the annihilation and creation operators. If we think of vectors in Fock space as formal power series, the **annihilation operator** is given by $$(a \psi)(z) = \frac{d}{dz} \psi(z)$$ while the **creation operator** is given by $$(a^* \psi)(z) = z \psi(z)  .$$ As operators on Fock space, these are only densely defined: for example, they map the dense subspace ${\mathbb C}[z]$ to itself. However, we can also think of them as operators from ${\mathbb C}[[z]]$ to itself. In physics these operators decrease or increase the number of quanta in a state, since $$az^n = n z^{n-1}  , \qquad a^* z^n = z^{n+1}.$$ Creating a quantum and then annihilating one is not the same as annhilating and then creating one, since $$a a^* = a^* a + 1  .$$ This is one of the basic examples of noncommutativity in quantum theory.

The annihilation and creation operators arise from spans by degroupoidification, using the recipe described in Theorem [\[PROCESS1\]](#PROCESS1){reference-type="ref" reference="PROCESS1"}. The annihilation operator comes from this span: $$\xymatrix{
& E\ar[dl]_{1} \ar[dr]^{S \mapsto S+1} & \\
E & & E
}$$ where the left leg is the identity functor and the right leg is the functor 'disjoint union with a 1-element set'. Since it is ambiguous to refer to this span by the name of the groupoid on top, as we have been doing, we instead call it $A$. Similarly, we call its adjoint $A^*$: $$\xymatrix{
& E\ar[dl]_{S \mapsto S+1} \ar[dr]^{1} & \\
E & & E
}$$ A calculation [@Morton:2006] shows that indeed: $$\utilde{A} = a, \qquad \utilde{A}^* = a^*  .$$ Moreover, we have an equivalence of spans: $$AA^* \simeq A^*A + 1 .$$ Here we are using composition of spans, addition of spans and the identity span as defined in Section [\[degroupoidification\]](#degroupoidification){reference-type="ref" reference="degroupoidification"}. If we unravel the meaning of this equivalence, it turns out to be very simple [@BaezDolan:2001]. If you have an urn with $n$ balls in it, there is one more way to put in a ball and then take one out than to take one out and then put one in. Why? Because in the first scenario there are $n+1$ balls to choose from when you take one out, while in the second scenario there are only $n$. So, the noncommutativity of annihilation and creation operators is not a mysterious thing: it has a simple, purely combinatorial explanation.

We can go further and define a span $$\Phi = A + A^*$$ which degroupoidifies to give the well-known **field operator** $$\phi = \utilde{\Phi} = a + a^*$$ Our normalization here differs from the usual one in physics because we wish to avoid dividing by $\sqrt{2}$, but all the usual physics formulas can be adapted to this new normalization.

The powers of the span $\Phi$ have a nice combinatorial interpretation. If we write its $n$th power as follows: $$\xymatrix{
& \Phi^n \ar[dl]_{q} \ar[dr]^{p} & \\
E & & E
}$$ then we can reinterpret this span as a groupoid over $E \times E$: $$\xymatrix{
\Phi^n \ar[d]_{q \times p} \\
E \times E
}$$ Just as a groupoid over $E$ describes a way of equipping a finite set with extra stuff, a groupoid over $E \times E$ describes a way of equipping a *pair* of finite sets with extra stuff. And in this example, the extra stuff in question is a very simple sort of diagram!

More precisely, we can draw an object of $\Phi^n$ as a $i$-element set $S$, a $j$-element set $T$, a graph with $i+j$ univalent vertices and a single $n$-valent vertex, together with a bijection between the $i+j$ univalent vertices and the elements of $S + T$. It is against the rules for vertices labelled by elements of $S$ to be connected by an edge, and similarly for vertices labelled by elements of $T$. The functor $p \times q \colon\Phi^n \rightarrow E \times E$ sends such an object of $\Phi^n$ to the pair of sets $(S,T) \in E \times E$.

An object of $\Phi^n$ sounds like a complicated thing, but it can be depicted quite simply as a **Feynman diagram**. Physicists traditionally read Feynman diagrams from bottom to top. So, we draw the above graph so that the univalent vertices labelled by elements of $S$ are at the bottom of the picture, and those labelled by elements of $T$ are at the top. For example, here is an object of $\Phi^3$, where $S = \{1,2,3\}$ and $T = \{4,5,6,7\}$:

::: center
::: picture
(110,120) ![image](feynman_1.eps) (-96,110)$5$ (-66,110)$4$ (-36,110)$7$ (-6,110)$6$ (-76,-13)$1$ (-46,-13)$3$ (-16,-13)$2$
:::
:::

0.5em In physics, we think of this as a process where 3 particles come in and 4 go out.

Feynman diagrams of this sort are allowed to have **self-loops**: edges with both ends at the same vertex. So, for example, this is a perfectly fine object of $\Phi^5$ with $S = \{1,2,3\}$ and $T = \{4,5,6,7\}$:

::: center
::: picture
(110,120) ![image](feynman_2.eps) (-96,110)$5$ (-66,110)$4$ (-36,110)$6$ (-6,110)$7$ (-76,-13)$2$ (-46,-13)$3$ (-16,-13)$1$
:::
:::

0.5em To eliminate self-loops, we can work with the **normal-ordered powers** or 'Wick powers' of $\Phi$, denoted $\! \colon \!\Phi^n\,\! \colon \!\,$. These are the spans obtained by taking $\Phi^n$, expanding it in terms of the annihilation and creation operators, and moving all the annihilation operators to the right of all the creation operators 'by hand', ignoring the fact that they do not commute. For example: $$\begin{aligned}
          \! \colon \!\Phi^0\,\! \colon \!&=& 1    \\
          \! \colon \!\Phi^1\,\! \colon \!&=& A + A^*  \\
          \! \colon \!\Phi^2\,\! \colon \!&=& A^2 + 2A^* A + {A^*}^2 \\
          \! \colon \!\Phi^3\,\! \colon \!&=& A^3 + 3A^* A^2 + 3{A^*}^2 A + {A^*}^3 
\end{aligned}$$ and so on. Objects of $\! \colon \!\Phi^n \! \colon \!$ can be drawn as Feynman diagrams just as we did for objects of $\Phi^n$. There is just one extra rule: self-loops are not allowed.

In quantum field theory one does many calculations involving products of normal-ordered powers of field operators. Feynman diagrams make these calculations easy. In the groupoidified context, a product of normal-ordered powers is a span $$\xymatrix{
&       \! \colon \!\Phi^{n_1}\,\! \colon \!\; \cdots\; \! \colon \!\Phi^{n_k}\,\! \colon \!
\ar[dl]_>>>>>>>{q} \ar[dr]^>>>>>>>{p} & \\
E & & E \, .
}$$ As before, we can draw an object of the groupoid $\! \colon \!\Phi^{n_1}\,\! \colon \!\;
\cdots\; \! \colon \!\Phi^{n_k}\,\! \colon \!$ as a Feynman diagram. But now these diagrams are more complicated, and closer to those seen in physics textbooks. For example, here is a typical object of $\! \colon \!\Phi^3 \! \colon \!\,
\! \colon \!\Phi^3 \! \colon \!\, \! \colon \!\Phi^4 \! \colon \!$, drawn as a Feynman diagram:

::: center
::: picture
(110,130) ![image](feynman_3.eps) (-100,125)$5$ (-68,125)$8$ (-36,125)$7$ (-6,125)$6$ (-101,-11)$1$ (-68,-11)$4$ (-36,-11)$2$ (-5,-11)$3$
:::
:::

0.5em In general, a **Feynman diagram** for an object of $\! \colon \!\Phi^{n_1}\,\! \colon \!
\; \cdots\; \! \colon \!\Phi^{n_k}\,\! \colon \!$ consists of an $i$-element set $S$, a $j$-element set $T$, a graph with $k$ vertices of valence $n_1, \dots,
n_k$ together with $i+j$ univalent vertices, and a bijection between these univalent vertices and the elements of $S+T$. Self-loops are forbidden; it is against the rules for two vertices labelled by elements of $S$ to be connected by an edge, and similarly for two vertices labelled by elements of $T$. As before, the forgetful functor $p \times q$ sends any such object to the pair of sets $(S,T)
\in E \times E$.

The groupoid $\! \colon \!\Phi^{n_1}\,\! \colon \!\; \cdots\; \! \colon \!\Phi^{n_k}\,\! \colon \!$ also contains interesting automorphisms. These come from *symmetries* of Feynman diagrams: that is, graph automorphisms fixing the univalent vertices labelled by elements of $S$ and $T$. These symmetries play an important role in computing the operator corresponding to this span: $$\xymatrix{
&       \! \colon \!\Phi^{n_1}\,\! \colon \!\; \cdots\; \! \colon \!\Phi^{n_k}\,\! \colon \!
\ar[dl]_>>>>>>>{q} \ar[dr]^>>>>>>>{p} & \\
E & & E \, .
}$$ As is evident from Theorem [\[matrix1\]](#matrix1){reference-type="ref" reference="matrix1"}, when a Feynman diagram has symmetries, we need to divide by the number of symmetries when determining its contribution to the operator coming from the above span. This rule is well-known in quantum field theory; here we see it arising as a natural consequence of groupoid cardinality.
