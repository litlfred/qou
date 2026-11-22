---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-019-53-sphericalization-of-a-fusion-category
section_title: "Sphericalization of a fusion category"
section_number: 5.3
pages: 28-30
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
Sphericalization of a fusion category
We have seen in Corollary 3.28 that every fusion category C over C comes
equipped with a canonical monoidal action of Z/2Z. The ‘equivariantization’
with respect to this action deﬁnes a new fusion category admitting a canonical
spherical structure.
Recall (see eg. [24]) that a monoidal action of a group G on a monoidal
category C is a monoidal functor F : BG →Aut⊗(C), where BG is the group
G thought of as a one-object category, and Aut⊗(C) is the monoidal category
of monoidal endofunctors of C.
Deﬁnition 5.12. The equivariantization CG is the monoidal category deﬁned
as follows:
• An object of CG consists of an object X ∈C together with isomorphisms
sg : Fg(X) →X for each g ∈G such that the diagram
FgFh(X)
Fg(X)
Fgh(X)
X
Fg(sh)
sg
sgh
γ(g, h)X
(33)
commutes for each g, h ∈G.
28
• A morphism in CG is a morphism f : X →Y in C satisfying
f ◦sX
g = sy
g ◦Fg(f)
(34)
for each g ∈G.
• The tensor product is deﬁned by (X, sX)⊗(Y, sY ) = (X ⊗Y, sX⊗Y ) where
sX⊗Y
g
is the composite
Fg(X ⊗Y )
Fg(X) ⊗Fg(Y )
X ⊗Y
(T g)−1
X,Y
sX
g ⊗sY
g
(35)
where T g
X,Y : Fg(X)⊗Fg(Y ) →Fg(X⊗Y ) are the coherence isomorphisms
equipping Fg as a monoidal functor.
Deﬁnition 5.13. The sphericalization ˜C of a fusion category C is its equivari-
antization with respect to the canonical Z/2Z action on it.
The advantage of our approach is that the action of Z/2Z is especially sim-
ple, as the group acts by identity functors, with the monoidal coherence isomor-
phisms encoded in the pivotal operators T i
jk.
Lemma 5.14. The sphericalization ˜C of C has simple objects Xsi
i
where Xi is
a simple object in C, and si = ±1. The fusion hom-vector spaces in ˜C compute
in terms of the decompositions of the fusion hom-sets in C (see (19)) as
Hom ˜
C(Xsi
i , Xsj
j ⊗Xsk
k ) = HomC(Xi, Xj ⊗Xk)sisjsk .
(36)
The associator in ˜C is the pullback of the associator in C. The forgetful tensor
functor F : ˜C →C sends Xσ
i 7→Xi. The pivotal symbols ˜ϵ of ˜C compute in
terms of the pivotal symbols ϵ of C as
˜ϵ(i,si)
(j,sj)(k,sk) = sisjsk .
(37)
Proof. Write Z/2Z = {1, −1}. The action of Z/2Z on C is strict as a group
action, so γ = id in (33). For a simple object Xi, write si = sXi
−1. Then (33)
becomes s2
i = 1 so si = ±1. Let eα : Xi →Xj ⊗Xk be a pivotal basis. From
(34), eα ∈Hom(Xsi
i , Xsj
j ⊗Xsk
k ) if and only if
Xi
Xj ⊗Xk
Xj ⊗Xk
Xj ⊗Xk
Xi
eα
TXj⊗Xk
sjsk
si
eα
(38)
commutes. By deﬁnition (see Corollary 3.24), TXjXk ◦eα = ϵi
jk,αeα, so that (38)
gives (36), as well as (37).
Corollary 5.15 (cf. [9, Prop 5.14]). The sphericalization ˜C of a fusion category
C carries a canonical spherical structure, in which the quantum dimension of a
simple object Xsi
i
in ˜C computes in terms of the fusion dimension di of Xi in
C as
dim(Xsi
i ) = sidi .
(39)
29
Proof. By (37), ˜C is orientable. So from Theorem 5.4, a spherical structure
amounts to a choice of signs t(i,si) = ±1 satisfying
t(j,sj)t(k,sk) = sisjskt(i,si)
whenever Hom(Xi, Xj ⊗Xk)sisjsk is nonzero. Clearly the choice t(i,si) = si
provides a solution, and (39) follows from the deﬁnition of the quantum dimen-
sion.
Example 5.16. The sphericalization of the Yang-Lee category has simple ob-
jects 1+, 1−, τ +, τ −. The fusion rules are τ +τ + = 1−, 1−1−= 1+, τ ±1−=
1−τ ± = τ ∓, and dim(τ ±) = ±dτ = ±(φ −1).
Lemma 5.17. The Frobenius-Perron and fusion dimensions in ˜C are the same
as in C, that is, d+
(Xi,si) = d+
Xi and d(Xi,si) = di.
Proof. We claim that setting d+
(Xi,si) = d+
Xi solves (13) and hence is the unique
solution, by the Frobenius-Perron theorem. Indeed,
d+
(Xj,sj)d+
(Xk,sk) = d+
j d+
k
=
X
i
N i
jkd+
i
=
X
i

(N i
jk)sjsk+ + (N i
jk)sjsk−

d+
i
for all sj, sk = ±1
=
X
(i,si)
(N i
jk)sjsksid+
(Xi,si) .
For the fusion dimensions, the associator in ˜C is the pullback of that in ˜C, so
the paired dimensions are same as in C, i.e. d{(Xi,si),(X∗
i ,si)} = d{i,i∗}.
