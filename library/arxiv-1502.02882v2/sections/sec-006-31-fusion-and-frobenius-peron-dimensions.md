---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-006-31-fusion-and-frobenius-peron-dimensions
section_title: "Fusion and Frobenius-Peron dimensions"
section_number: 3.1
pages: 7-10
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
We recall the following from [9]. In a fusion category C over C, every simple
object Xi has two canonical dimensions, which are positive real numbers: its
Frobenius-Perrondimension d+
i and its fusion dimension di.
Deﬁnition 3.1 (see [9]). The Frobenius-Perron dimensions d+
j of the simple
objects Xj are the unique positive real numbers satisfying
d+
j d+
k =
∑
i
Ni
jkd+
i (13)
where Ni
jk = dim Hom(Xi,Xj⊗Xk). That is, they furnish the unique homo-
morphism from the Grothendieck ring of C to C taking positive real values on
the simple objects Xi.
7
Note that, since taking duals is a ring anti-homomorphism from the Grothendieck
ring of C to itself, it follows from uniqueness of the Frobenius-Perron dimensions
that d+
j =d+
j∗ for all j∈I.
To deﬁne the fusion dimensions, we ﬁrst need to deﬁne paired dimensions 1.
Deﬁnition 3.2. Let Xi and X∗
i be dual simple objects in C. Their paired
dimension is
d{i,i∗} =
 , (14)
where (η,ϵ ) is some choice of unit and counit maps exhibiting X∗
i as a right
dual of Xi, and (n,e ) is some choice of unit and counit maps exhibiting X∗
i as
a left dual of Xi.
Observe that the product (14) is independent of the choices of unit and
counit maps made in the deﬁnition because it is invariant under rescaling
η↦→λη,ϵ↦→ 1
λϵ,n↦→µn,e↦→ 1
µe.
Note that the paired dimensions are certainly nonzero complex numbers. In-
deed, e◦η is zero if and only if one of e or η is zero (by semisimplicity), which
would contradict the duality equations (2). Similarly for ϵ◦n. In Section 4.2
we will show how to compute the paired dimensions explicitly in terms of the
associator matrix elements.
In fact, we will show in Theorem 3.19 that the paired dimensions are always
positive real numbers. Anticipating this, we make the following deﬁnition.
Deﬁnition 3.3. The fusion dimension di of a simple object Xi in a fusion
category over C is the positive square root of its paired dimension d{i,i∗}.
In Corollary 4.7, we show how to read oﬀ the fusion dimensions directly from
the associators.
Example 3.4. In the Yang-Lee category,d+
τ = 1
2(1 +
√
5) and we read oﬀ from
(7) that dτ = 1
2(−1 +
√
5). In category E, d+
x = 1 +
√
3 and d+
y = 1, while we
read oﬀ from (10) that dx =d+
x ; similarly dy =d+
y = 1.
The global dimension DC of a fusion category is the sum of its paired di-
mensions, DC =∑
i∈Id{i,i∗}. The Frobenius-Perron dimension FP C of a fu-
sion category is the sum of the squares of the Frobenius-Perron dimensions,
FP C =∑
i∈I(d+
i )2. The fusion category is called pseudo-unitary ifFP C =DC.
3.2 The pairing convention
Deﬁnition 3.5. A root choice on a fusion category is a symmetric choice {di}
of square roots of the paired dimensions; that is, one which satisﬁes
d2
i =d{i,i∗} and di =di∗ for all i∈I.
1The notion of a paired dimension is due to M¨ uger [18, Prop 2.4], where it is written as
d2(X), but not named explicitly. The terminology and notation is our own.
8
The utility of a root choice is that it allows the following diagrammatic
convention.
Pairing convention. Whenever a unit
 which is part of a unit-
counit pair expressing a simple object X∗
i as a right dual of Xi appears
together in some equation with a counit
 which is part of a unit-
counit pair expressing X∗
i as a left dual of Xi, it will always be under-
stood that the former is arbitrary while the latter is determined uniquely
by the requirement that
=di
Similarly (and equivalently), whenever
 appears in a diagram to-
gether with
 , the latter will always be ﬁxed uniquely by the re-
quirement that
=di.
The pairing convention is the key diagrammatic idea in this paper. Using
this convention, we only need to ﬁx a root choice (and not a pivotal struc-
ture, which is not known to exist in general) on the fusion category in order to
unambiguously perform string diagram calculations where both left and right
duals appear. Note that the pairing convention extends uniquely to the whole
category and not just the simple objects, see Section 3.5.
Remark 3.6. We will presently show in Theorem 3.19 that the paired dimen-
sionsd{i,i∗} are positive real numbers. From then on, we will always work with
the canonical root choice on a fusion category given by the positive square roots.
Although we will not need it in this paper, we can extend the pairing conven-
tion to all objects in C, not just simple ones. Namely, suppose V ∈ C. For each
representative simple object Xi, choose a basis ei,α :Xi→V for Hom(Xi,V ),
with corresponding dual basis ˆei,α :V →Xi. If, in a diagram, a unit
which is part of a unit-counit pair ( η,ϵ ) expressing V∗ as a right dual of V
appears together with a counit
which is part of a unit-counit pair ( n,e ) expressing V∗ as a left dual of V , it
9
will be understood that the former is arbitrary while the latter is deﬁned as
:=
∑
i,α
.
Note that this deﬁnition is independent of the choice of basis ei,α.
