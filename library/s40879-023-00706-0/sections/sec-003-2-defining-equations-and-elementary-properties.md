---
doc_id: s40879-023-00706-0
doc_title: "Bring’s curve: old and new"
section_id: sec-003-2-defining-equations-and-elementary-properties
section_title: "Defining equations and elementary properties"
section_number: 2
pages: 3-4
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
toc_source: outline
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
2 Deﬁning equations and elementary properties
In this section we shall introduce Bring’s curve describing its basic properties, its
period matrix and its automorphisms. We begin with two descriptions: one as a model
in P4 and the second as a plane curve. In particular we shall construct the birational
map between these models, which we believe new. Such a map enables us to concretely
translate calculations from one model to another and will be helpful later in Sect.4
when we look at quotients of the curve.
Deﬁnition 2.1 Bring’s curve B is deﬁned in P4 by the (homogeneous) equations1
Hk ..=
5

i=1
xk
i = 0,
k = 1, 2, 3,
(1)
where we have taken the coordinates [x1 : x2 : x3 : x4 : x5] ∈P4.
We will call (1) the P4-model of Bring’s curve. Historically, this curve was attributed
to Bring by Klein in his lectures on the icosahedron [42]. Bring’s improvement on the
Tschirnhaus transformation enabled the general quintic to be brought to the Bring–
Jerrard form x5 + ex + f = 0 [1]: if xi, i = 1, . . . , 5, are the roots of this equation
then the symmetric sums 
i xk
i = 0 for k = 1, 2, 3, and so the above curve emerges.
Green [30] exploits this relation to Bring’s curve to (implicitly) solve the quintic using
automorphic forms. At this stage we may observe that S5 ⩽Aut(B).
Remark 2.2 In the above deﬁnition we have implicitly taken P4 = CP4, and indeed
this will be our deﬁnition throughout. At various junctures we will however highlight
the number ﬁelds within C that are relevant ﬁelds of deﬁnition for morphisms of the
curve, or geometrically important points on the curve.
For many calculations a plane model of a curve in P2 is useful. One of the main
tools we will utilise in this paper is the Riemann surfaces module of SageMath [64]
which requires such a model. As such we introduce the following.
Deﬁnition 2.3 The Hulek–Craig (HC) model of Bring’s curve is the (singular) plane
curve in P2 given by
F(X, Y, Z) ..= X(Y 5+ Z5) + (XY Z)2 −X4Y Z −2(Y Z)3 = 0,
(2)
taking homogeneous coordinates [X : Y : Z] ∈P2. We denote its normalisation by B.
This model was used in [15, 39] where they studied the curves modular properties.
Indeed Craig gives a parameterization of the curve in terms of modular functions
following work of Ramanujan. Craig does not identify the curve as Bring’s, whereas
Hulek ﬁnds the equation as a hyperplane section of a surface that parameterises elliptic
normal curves of degree 5, and then refers to previous results to connect it with Bring.
This connection was ﬁrst made in [52], where the curve is attributed to Klein. Indeed,
1 Note here we use the notation Hk of [11] for the symmetric sum, whereas [24] uses Sk.
3
Page 4 of 46
H.W. Braden, L. Disney-Hogg
because of this interpretation, one can write down Bring’s curve in the form of a
quotient of the upper half plane H as
H/0(2, 5)
where 0(2, 5) = 0(2) ∩(5) =
⎧
⎪⎨
⎪⎩

a b
c d
	
∈SL2(Z)

a ≡d ≡1 (mod 5)
b ≡0 (mod 5)
c ≡0 (mod 10)
⎫
⎪⎬
⎪⎭
.
To our knowledge, [39] is the ﬁrst occurrence of this plane model of the curve; Klein
will write it down in [42, pp.165, 242] but the relation to a plane model of Bring’s
curve is not made explicit. We will call (2) the HC-model of Bring’s curve. In the
following subsection we shall show the birational equivalence of (2) and (1).
Another plane model of Bring’s curve is given by (x −1) y5 −(x + 1)x2 = 0,
introduced in [66, Proposition 3.1] by considering the curve as a cyclic cover of P1,
see Sect.4.
