---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-005-42-hecke-algebras
section_title: "Hecke Algebras"
section_number: 4.2
pages: 36-41
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.995
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
[]{#hecke label="hecke"}

Here we sketch how to groupoidify a Hecke algebra when the parameter $q$ is a power of a prime number and the finite reflection group comes from a Dynkin diagram in this way. More details will appear in future work [@Baez].

Let $D$ be a Dynkin diagram. We write $d \in D$ to mean that $d$ is a dot in this diagram. Associated to each unordered pair of dots $d,d'
\in D$ is a number $m_{dd'} \in \{2,3,4,6\}$. In the usual Dynkin diagram conventions:

-   $m_{dd'} = 2$ is drawn as no edge at all,

-   $m_{dd'} = 3$ is drawn as a single edge,

-   $m_{dd'} = 4$ is drawn as a double edge,

-   $m_{dd'} = 6$ is drawn as a triple edge.

For any nonzero number $q$, our Dynkin diagram gives a Hecke algebra. Since we are using real vector spaces in this paper, we work with the Hecke algebra over ${\mathbb R}$:

::: definition
Let $D$ be a Dynkin diagram and $q$ a nonzero real number. The **Hecke algebra** $H(D,q)$ corresponding to this data is the associative algebra over ${\mathbb R}$ with one generator $\sigma_d$ for each $d \in D$, and relations: $$\sigma_d^2 = (q-1)\sigma_d + q$$ for all $d \in D$, and $$\sigma_d\sigma_{d'}\sigma_d\cdots 
= \sigma_{d'} \sigma_d \sigma_{d'}\cdots$$ for all $d,d'\in D$, where each side has $m_{dd'}$ factors.
:::

Hecke algebras are $q$-deformations of finite reflection groups, also known as Coxeter groups [@Humphreys]. Any Dynkin diagram gives rise to a simple Lie group, and the Weyl group of this simple Lie algebra is a Coxeter group. To begin understanding Hecke algebras, it is useful to note that when $q = 1$, the Hecke algebra is simply the group algebra of the **Coxeter group** associated to $D$: that is, the group with one generator $s_d$ for each dot $d \in D$, and relations $$s_d^2 = 1,  \qquad (s_d s_{d'})^{m_{dd'}} = 1 .$$ So, the Hecke algebra can be thought of as a $q$-deformation of this Coxeter group.

If $q$ is a power of a prime number, the Dynkin diagram $D$ determines a simple algebraic group $G$ over the field with $q$ elements, ${\mathbb F}_q$. We choose a Borel subgroup $B \subseteq G$, i.e., a maximal solvable subgroup. This in turn determines a transitive $G$-set $X = G/B$. This set is a smooth algebraic variety called the **flag variety** of $G$, but we only need the fact that it is a finite set equipped with a transitive action of the finite group $G$. Starting from just this $G$-set $X$, we can groupoidify the Hecke algebra $H(D,q)$.

Recalling the concept of 'action groupoid' from Section [\[intro\]](#intro){reference-type="ref" reference="intro"}, we define the **groupoidified Hecke algebra** to be $$(X \times X)/\!/G.$$ This groupoid has one isomorphism class of objects for each $G$-orbit in $X \times X$: $$\underline{(X \times X)/\!/G} \cong (X \times X)/G.$$ The well-known 'Bruhat decomposition' [@Borel] of $X/G$ shows there is one such orbit for each element of the Coxeter group associated to $D$. Since the Hecke algebra has a standard basis given by elements of the Coxeter group [@Humphreys], it follows that $(X \times X)/\!/G$ degroupoidifies to give the underlying vector space of the Hecke algebra. In other words, we obtain an isomorphism of vector spaces $${\mathbb R}^{(X \times X)/G} \cong H(D,q) .$$

Even better, we can groupoidify the *multiplication* in the Hecke algebra. In other words, we can find a span that degroupoidifies to give the linear operator $$\begin{array}{ccc} 
     H(D,q) \otimes H(D,q) & \rightarrow& H(D,q)   \\
         a \otimes b       & \mapsto & ab 
\end{array}$$ This span is very simple: $$\label{multiplication}
  \def\objectstyle{\scriptstyle}
  \def\labelstyle{\scriptstyle}
   \xy
   (0,30)*+{(X \times X \times X)/\!/G}="1";
   (25,10)*+{(X\times X)/\!/G \;\,\times\;\, (X\times X)/\!/G}="2";
   (-25,10)*+{(X\times X)/\!/G}="3";
        {\ar_{(p_1,p_2)\times (p_2,p_3)} "1";"3"};
        {\ar^{(p_1,p_3)} "1";"2"};
\endxy$$ where $p_i$ is projection onto the $i$th factor.

For a proof that this span degroupoidifies to give the desired linear operator, see [@Hoffnung]. The key is that for each dot $d \in D$ there is a special isomorphism class in $(X \times X)/\!/G$, and the function $$\psi_d \colon(X \times X)/G \rightarrow{\mathbb R}$$ that equals 1 on this isomorphism class and 0 on the rest corresponds to the generator $\sigma_d \in H(D,q)$.

To illustrate these ideas, let us consider the simplest nontrivial example, the Dynkin diagram $A_2$: $$\xymatrix{ \bullet\ar@{-}[r] & \bullet}$$ The Hecke algebra associated to $A_2$ has two generators, which we call $P$ and $L$, for reasons soon to be revealed: $$P = \sigma_1 , \qquad L = \sigma_2 .$$ The relations are $$P^2 = (q-1) P + q, \qquad L^2= (q-1)P + q,  \qquad PLP=LPL  .$$ It follows that this Hecke algebra is a quotient of the group algebra of the 3-strand braid group, which has two generators $P$ and $L$ and one relation $PLP = LPL$, called the **Yang--Baxter equation** or **third Reidemeister move**. This is why Jones could use traces on the $A_n$ Hecke algebras to construct invariants of knots [@Jones]. This connection to knot theory makes it especially interesting to groupoidify Hecke algebras.

So, let us see what the groupoidified Hecke algebra looks like, and where the Yang--Baxter equation comes from. The algebraic group corresponding to the $A_2$ Dynkin diagram and the prime power $q$ is $G = \mathrm{SL}(3,{\mathbb F}_q)$, and we can choose the Borel subgroup $B$ to consist of upper triangular matrices in $\mathrm{SL}(3,{\mathbb F}_q)$. Recall that a **complete flag** in the vector space ${\mathbb F}_q^3$ is a pair of subspaces $$0 \subset V_1 \subset V_2 \subset {\mathbb F}_q^3  .$$ The subspace $V_1$ must have dimension 1, while $V_2$ must have dimension 2. Since $G$ acts transitively on the set of complete flags, while $B$ is the subgroup stabilizing a chosen flag, the flag variety $X = G/B$ in this example is just the set of complete flags in ${\mathbb F}_q^3$---hence its name.

We can think of $V_1 \subset {\mathbb F}_q^3$ as a point in the projective plane ${\mathbb F}_q{\mathrm P}^2$, and $V_2 \subset {\mathbb F}_q^3$ as a line in this projective plane. From this viewpoint, a complete flag is a chosen point lying on a chosen line in ${\mathbb F}_q {\mathrm P}^2$. This viewpoint is natural in the theory of 'buildings', where each Dynkin diagram corresponds to a type of geometry [@Brown; @Garrett]. Each dot in the Dynkin diagram then stands for a 'type of geometrical figure', while each edge stands for an 'incidence relation'. The $A_2$ Dynkin diagram corresponds to projective plane geometry. The dots in this diagram stand for the figures 'point' and 'line': $$\xymatrix{ {\rm point} \; \bullet \ar@{-}[r] & 
\bullet \; {\rm line} }$$ The edge in this diagram stands for the incidence relation 'the point $p$ lies on the line $\ell$'.

We can think of $P$ and $L$ as special elements of the $A_2$ Hecke algebra, as already described. But when we groupoidify the Hecke algebra, $P$ and $L$ correspond to *objects* of $(X \times X)/\!/
G$. Let us describe these objects and explain how the Hecke algebra relations arise in this groupoidified setting.

As we have seen, an isomorphism class of objects in $(X \times X)/\!/
G$ is just a $G$-orbit in $X \times X$. These orbits in turn correspond to spans of $G$-sets from $X$ to $X$ that are **irreducible**: that is, not a coproduct of other spans of $G$-sets. So, the objects $P$ and $L$ can be defined by giving irreducible spans of $G$-sets: $$\xymatrix{
    & P \ar[dl]\ar[dr] &    &&     & L\ar[dl]\ar[dr] & \\
X &                  &X && X &                 &X
}$$

In general, any span of $G$-sets $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p} & \\
X & & X}$$ such that $q \times p \colon S \rightarrow X \times X$ is injective can be thought of as $G$-invariant binary relation between elements of $X$. Irreducible $G$-invariant spans are always injective in this sense. So, such spans can also be thought of as $G$-invariant relations between flags. In these terms, we define $P$ to be the relation that says two flags have the same line, but different points: $$P = \{((p,\ell),(p',\ell)) \in X \times X \mid p\neq p'\}$$ Similarly, we think of $L$ as a relation saying two flags have different lines, but the same point: $$L = 
\{((p,\ell),(p,\ell')) \in X \times X \mid \ell\neq \ell'\}.$$ Given this, we can check that $$P^2 \cong (q-1) \times P + q \times 1, \qquad L^2 \cong (q-1) \times L + 
q \times 1, \qquad PLP \cong LPL .$$ Here both sides refer to spans of $G$-sets, and we denote a span by its apex. Addition of spans is defined using coproduct, while $1$ denotes the identity span from $X$ to $X$. We use '$q$' to stand for a fixed $q$-element set, and similarly for '$q-1$'. We compose spans of $G$-sets using the ordinary pullback. It takes a bit of thought to check that this way of composing spans of $G$-sets matches the product described by Equation [\[multiplication\]](#multiplication){reference-type="ref" reference="multiplication"}, but it is indeed the case [@Hoffnung].

To check the existence of the first two isomorphisms above, we just need to count. In $\mathbb{F}_q\mathrm{P}^2$, the are $q+1$ points on any line. So, given a flag we can change the point in $q$ different ways. To change it again, we have a choice: we can either send it back to the original point, or change it to one of the $q-1$ other points. So, $P^2 \cong (q-1) \times P + q \times 1$. Since there are also $q+1$ lines through any point, similar reasoning shows that $L^2 \cong
(q-1) \times L + q \times 1$.

The Yang--Baxter isomorphism $$PLP \cong LPL$$ is more interesting. We construct it as follows. First consider the left-hand side, $PLP$. So, start with a complete flag called $(p_1,\ell_1)$:

::: center
::: picture
(50,25) ![image](newflags0.eps) (-20,2)$p_1$ (0,-10)$\ell_1$
:::
:::

Then, change the point to obtain a flag $(p_2,\ell_1)$. Next, change the line to obtain a flag $(p_2,\ell_2)$. Finally, change the point once more, which gives us the flag $(p_3,\ell_2)$:

::: center
::: picture
(250,45) ![image](newflags3.eps) (-245,4)$p_1$ (-225,-10)$\ell_1$ (-185,4)$p_1$ (-165,-10)$\ell_1$ (-200,25)$p_2$ (-120,4)$p_1$ (-100,-10)$\ell_1$ (-130,23)$p_2$ (-80,35)$\ell_2$ (-40,4)$p_1$ (-20,-10)$\ell_1$ (-55,23)$p_2$ (5,35)$\ell_2$ (-15,40)$p_3$
:::
:::

The figure on the far right is a typical element of $PLP$.

On the other hand, consider $LPL$. So, start with the same flag as before, but now change the line, obtaining $(p_1,\ell'_2)$. Next change the point, obtaining the flag $(p'_2,\ell'_2)$. Finally, change the line once more, obtaining the flag $(p'_2,\ell'_3)$:

::: center
::: picture
(240,40) ![image](newflags2_3.eps) (-245,3)$p_1$ (-225,-10)$\ell_1$ (-185,3)$p_1$ (-170,-10)$\ell_1$ (-150,45)$\ell_2'$ (-120,3)$p_1$ (-100,-10)$\ell_1$ (-85,45)$\ell_2'$ (-85,20)$p_2'$ (-45,4)$p_1$ (-25,-10)$\ell_1$ (-10,43)$\ell_2'$ (-10,20)$p_2'$ (-60,25)$\ell_3'$
:::
:::

The figure on the far right is a typical element of $LPL$.

Now, the axioms of projective plane geometry say that any two distinct points lie on a unique line, and any two distinct lines intersect in a unique point. So, any figure of the sort shown on the left below determines a unique figure of the sort shown on the right, and vice versa:

::: center
::: picture
(150,50) ![image](flagcompare.eps)
:::
:::

Comparing this with the pictures above, we see this bijection induces an isomorphism of spans $PLP \cong LPL$. So, we have derived the Yang--Baxter isomorphism from the axioms of projective plane geometry!

To understand groupoidified Hecke algebras, it is important to keep straight the two roles played by spans. On the one hand, objects of the groupoidified Hecke algebra $(X \times X)/\!/G$ can be described as certain spans from $X$ to $X$, namely the injective $G$-invariant ones. Multiplying these objects then corresponds to composing spans. On the other hand, Equation [\[multiplication\]](#multiplication){reference-type="ref" reference="multiplication"} gives a span describing the multiplication in $(X \times X)/\!/G$. In fact, this span describes the process of composing spans. If this seems hopelessly confusing, remember that any matrix describes a linear operator, but there is also a linear operator describing the process of matrix multiplication. We are only groupoidifying that idea.

Other approaches to categorified Hecke algebras and their representations have been studied by a number of authors, building on Kazhdan--Lusztig theory [@KaLu]. One key step was Soergel's introduction of what are nowadays called Soergel bimodules [@Rou; @Soergel]. Also important were Khovanov's categorification of the Jones polynomial [@Kh] and the work by Bernstein, Frenkel, Khovanov and Stroppel on categorifying Temperley--Lieb algebras, which are quotients of the type $A$ Hecke algebras [@BFK; @Stroppel]. A diagrammatic interpretation of the Soergel bimodule category was developed by Elias and Khovanov [@ElKh], and a geometric approach led Webster and Williamson [@WW] to deep applications in knot homology theory. This geometric interpretation can be seen as going beyond the simple form of groupoidification we consider here, and considering groupoids in the category of schemes.
