---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-016-the-duality-map
section_title: "The Duality Map"
section_number: null
pages: 20-21
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
---
In order to extend this picture to the correlation functions, we need to establish a dictionary
between the observables of chiral Yang-Mills theory and those of the deformed extended
Hurwitz theory. Given an insertion U, we need to identify the unique element P
sas(U)ˆAs in
the algebra of partial permutations which behaves as
X
α⊢d
pα(U)gℓ(α)
s ˆCα (5.5)
inside genus-g, degree-d correlation functions, for all values of the genus and degree. Our
strategy is the following. Firstly, we isolate permutations with a given non-trivial structure.
That is, we look for permutations σ obtained by completing the minimal partial permutation
¯s to all possible degrees. For each such permutation σ, we have the equation
X
s
gℓ(s)
s as(U)⟨ ˆAs (... )⟩g,d =gℓ(σ)
s pσ(U)⟨ ˆCσ (... )⟩g,d, (5.6)
where the only partial permutations s relevant to the sum are the partial permutations of the
form ¯s∪ 1k, with 0≤k≤d−|d¯s|. Thus, we obtain the following equations for the coefficient
a¯s∪1k
d−|d¯s|X
k=0
gℓ(¯s)+k
s a¯s∪1k(U)
d−|d¯s|
k

=gℓ(σ)
s pσ(U). (5.7)
There is an equation for each degree d≥| d¯s|, and the coefficients as thus obey an infinite
system of linear equations. Its matrix form is lower triangular and is a version of the Pascal
19
triangle weighted by factors of the string coupling. It can be solved recursively, as explained
in appendix B. The coefficients of the partial permutation dual to an insertion U are given by
as(U) :=p¯s(U)
m1(s)X
l=0
(−1)m1(s)−lgl−m1(s)
s
m1(s)
l

p1l(U). (5.8)
We conclude that the insertion of a boundary holonomy U in the chiral Yang-Mills theory
translates to the insertion of the observable P
sas(U)ˆAs in the deformed extended Hurwitz
theory. The role of trivial sheets in the string theory is played by the power-sum polynomials
in the Yang-Mills theory. Each trivial sheet corresponds to a factor tr U.
An interesting consequence of this dictionary is that in the large N limit, a hole opera-
tor algebra can be defined for the Yang-Mills theory. The elements of this algebra are the
holonomies in the unitary group U(∞). The product is defined such that, in any given corre-
lation function, holonomies U1 and U2 may be replaced by a holonomy U3. We write
Z(U1,U 2,... ) =
Z
dU3c(U1,U 2;U3)Z(U3,... ). (5.9)
The c(U1,U 2;U3) are structure constants for the algebra and they can be written as:
c(U1,U 2;U3) :=
X
r,s,t
ˆg t
rs g|dr|+|ds|−|dt|
s ar(U1)as(U2)a⊥
t (U3). (5.10)
In this expression, the coefficients ˆgt
rs are the structure constants of the partial permutation
algebraA∞ in the renormalized basis and the a⊥
t form the basis of vectors dual to the vectors
as which means that the inner product between the two bases is a Kronecker delta:
Z
dUas(U)a⊥
t (U) =δs,t. (5.11)
These vectors a⊥
t are explicitly given by linear combinations of the power sum polynomials
a⊥
s (U) =
X
k≥m1(s)
 k
m1(s)

gm1(s)−k
s p∗
¯s∪1k(U). (5.12)
