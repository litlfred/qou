---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-003-harish-chandra-bimodules-over-quantized-symplect
section_title: "Harish-Chandra bimodules over quantized symplectic singularities"
section_number: null
pages: 8-10
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Ivan Losev
This talk is based on [L2].
Let A be a ﬁnitely generated positively graded Poisson algebra over C with
bracket of degree −d for some d ∈Z>0. We will assume throughout that X :=
Spec(A) has symplectic singularities. Examples include the algebras A = C[N] of
regular functions on the nilpotent cone N in a semisimple Lie algebra g and the
Enveloping Algebras and Geometric Representation Theory
3089
algebras C[V ]Γ, where V is a ﬁnite dimensional symplectic vector space and Γ is
a ﬁnite subgroup of Sp(V ).
Let A be a ﬁltered quantization of A. In the case when A = C[N] we can take
A to be the central reduction Uλ of the universal enveloping algebra U(g). Here
λ ∈h∗/W, where h is a Cartan subalgebra of g and W is the Weyl group. In the
case when A := C[V ]Γ, we can take the spherical symplectic reﬂection algebras of
Etingof and Ginzburg, [EG]. In fact, thanks to results of [L1], these families of
algebras exhaust ﬁltered quantizations of A = C[N] and A = C[V ]Γ, respectively.
Deﬁnition 1. Let B be an A-bimodule. We say that B is Harish-Chandra (shortly,
HC) if it admits a bimodule ﬁltration B = S
i⩾0 B⩽i such that [A⩽i, B⩽j] ⊂
B⩽i+j−d for all i, j, and gr B is a ﬁnitely generated A-module.
For example, the regular bimodule A is HC. The category of HC bimodules
(where the morphisms are bimodule homomorphisms) will be denoted by HC(A).
In this talk we are interested in the structure of a certain quotient category of
HC(A). Namely, to a HC bimodule B we can assign its support Supp(B) deﬁned
as the support in X of gr B with respect to any ﬁltration on B as in Deﬁnition
1. Let HC(A) be the quotient of the category HC(A) by the full subcategory of
all bimodules whose support is a proper subvariety of X. Note that HC(A) is a
monoidal category with respect to the tensor product of bimodules and HC(A)
carries an induced monoidal structure.
It turns out that HC(A) is equivalent to the category of representations of a
certain ﬁnite group. Namikawa in [N] proved that the algebraic fundamental group
πalg
1 (Xreg) is ﬁnite. For example, for X = V/Γ, this group coincides with Γ. So
we write Γ for πalg
1 (Xreg) in the general case too.
It turns out, see [L2, Section 4], that there is a natural monoidal embedding
HC(A)֒ →Rep Γ. The image depends on the choice of quantization. For example,
when X = C2/Γ is a Kleinian singularity, the parameter space for quantizations
is h∗/W, where h, W are the Cartan space and the Weyl group of the same ADE
type as Γ. In [L2, Section 5] we construct a normal subgroup Γλ ⊂Γ from a
parameter λ ∈h∗/W and prove that, for the corresponding quantization Aλ, the
image of HC(Aλ) in Rep Γ coincides with Rep(Γ/Γλ) provided Γ is not of type E8.
Now let us proceed to the case of general X. The variety X has ﬁnitely many
symplectic leaves by a result of Kaledin. Let L1, . . . , Lk be the codimension two
leaves. For i =, 1 . . ., k, we write Σi for a formal slice to Li, it is a formal neigh-
borhood of zero in C2/Γi for a suitable subgroup Γi ⊂SL2(C). Quantizing the
slice construction, we see that A gives rise to a ﬁltered quantization of C[Σi], let
us denote that quantization by Ai. The latter, in its turn, gives rise to a normal
subgroup Γi,A ⊂Γi as mentioned in the previous paragraph.
Now note that there is natural homomorphism Γi →Γ. Indeed, Γi = πalg
1 (Σi \
{0}) and Γ = πalg
1
(Xreg). The inclusion Σi \ {0}֒ →Xreg give rise to a group
homomorphism Γi →Γ to be denoted by ϕi.
Let ΓA be the minimal normal subgroup in Γ containing ϕi(Γi,A) for all i =
1, . . . , k. The following is the main result of [L2].
3090
Oberwolfach Report 52/2018
Theorem 2. Suppose that none of the subgroups Γi ⊂SL2(C) is of type E8. Then
the image of HC(A) in Rep(Γ) coincides with Rep(Γ/ΓA).
References
[EG] P. Etingof and V. Ginzburg. Symplectic reﬂection algebras, Calogero-Moser space, and
deformed Harish-Chandra homomorphism, Invent. Math. 147 (2002), 243-348.
[L1] I. Losev. Deformations of symplectic singularities and Orbit method for semisimple Lie
algebras. arXiv:1605.00592.
[L2] I.
Losev,
Harish-Chandra
bimodules
over
quantized
symplectic
singularities.
arXiv:1810.07625.
[N] Y. Namikawa, Fundamental groups of symplectic singularities. Higher dimensional algebraic
geometry–in honour of Professor Yujiro Kawamata’s sixtieth birthday, 321–334, Adv. Stud.
Pure Math., 74, Math. Soc. Japan, Tokyo, 2017.
