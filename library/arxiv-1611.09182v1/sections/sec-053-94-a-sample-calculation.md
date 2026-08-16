---
doc_id: arxiv-1611.09182v1
doc_title: ""
section_id: sec-053-94-a-sample-calculation
section_title: "A sample calculation"
section_number: 9.4
pages: 84-89
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? C. Furey A thesis presented to the University of Waterloo in fulfillment of the thesis requirement for the degree of Doctor of Philosophy Physics — 57 sections"
---
We introduce to the reader how calculations are carried out in C⊗← −O by working through
an example. Let us ﬁnd the action of the ﬁrst SU (3) generator of the form Λ ν, which we
will deﬁne as Λ1ν≡ i
2 (e15−e34)ν, in accordance with equation (6.26). Let Λ 1ν act onqR
1 ,
as deﬁned in equations (9.8):
[
Λ1ν, qR
1
]
=
[
i
2 (e15−e34)ν, (−ie12−e16 +e23 +ie36)ν
]
= i
2
(
(e15−e34) (−ie12−e16 +e23 +ie36)
− (−ie12−e16 +e23 +ie36) (e15−e34)
)
ν
= i
2
(
−ie1512−e1516 +e1523 +ie1536
+ie3412 +e3416−e3423−ie3436
+ie1215 +e1615−e2315−ie3615
−ie1234−e1634 +e2334 +ie3634
)
ν
= i
2
(
−ie52−e56 +e1235−ie1356
+ie1234 +e1346 +e42−ie46
+ie25 +e65−e1235 +ie1356
−ie1234−e1346−e24 +ie64
)
ν
= i
(
ie25−e56−e24−ie46
)
ν =qG
1.
(9.17)
This is the result we would expect for the ﬁrst of thesu(3) Gell-Mann matrices, ΛGM
1 , from
the standard model, acting to convert a red basis vector, R≡ (1, 0, 0)⊤, into a green basis
76
vector,G≡ (0, 1, 0)⊤.
ΛGM
1 R =


0 1 0
1 0 0
0 0 0




1
0
0

 =


0
1
0

 =G. (9.18)
9.5 Summary for SU (3)c
Finally, we conclude by summarizing the main result of this chapter in Figure 9.1: the
breakdown of the 64-dimensional C⊗← −O into irreducible representations of SU (3).
iΛν
iΛν- * *
l l
q q
l l
q q
l l
q q
l l
q q
l l
q q
l l
q q
**
* * * *
- -
-
- -
-
a b
*
a b
c
c
d
d
e
e
f
f
1
1
2
2
3
3
4
4
5
5
6
6
ν  ν
ν  ν ν  ν
ν  ν
* *
*
*
a a
a a
Figure 9.1: The 64-dimensional octonionic chain algebra splits into two sets of SU (3)
generators of the form iΛν and−iΛ∗ν∗, six SU (3) singlets 𝓁j, six triplets qk, and their
complex conjugates. These objects are sectioned oﬀ above into four quadrants according
to their forms: νaν,ν∗aν,νaν∗ andν∗aν∗ fora in the chain algebra. Transforming particles
into anti-particles, and vice versa, requires only the complex conjugate ∗: i↦→− i in our
formalism.
Using only the eight-dimensional complex octonions, C⊗ O, we have explained how to
build up a 64-complex-dimensional associative algebra. The SU (3) generators identiﬁed
77
within this algebra then break down the remaining space into six singlets, six triplets, and
their antiparticles, with no extra particles beyond these.
These representations are a curious ﬁnding. They eﬀortlessly suggest the existence of
exactly three generations, they relate particles to antiparticles by using only the complex
conjugate i↦→−i, and ﬁnally, they ﬁll these tall orders while working from but a modest
eight-complex-dimensional algebra.
9.6 Three generations under SU (3)c and U (1)em
Since the time that these irreducible representations ofSU (3)c were identiﬁed withinC⊗← −O,
more standard model structure has been uncovered in the algebra. It turns out that we
can extend our three-generation results for SU (3)c to includeU(1)em as well (presented for
the ﬁrst time here).
That is, our SU (3)c action on C⊗← −O given by
[ Λjν, aν], [−Λ∗
jν∗, aν∗ ] (9.19)
can be generalized, so as to include electric charges. Furthermore, we will be able to
incorporateU(1)em by making use of theQ we had already introduced in our one-generation
model of Section 6.8,
Q = N
3 =
3∑
i=1
α†
iαi. (9.20)
Consider the following action for the SU (3)c generators,
[ Λjν, S∗aν ],
[
−Λ∗
jν∗, Saν∗]
,
[ Λjν, Saν ],
[
−Λ∗
jν∗, S∗aν∗]
,
(9.21)
where S is the projector given by
S≡ 1
2− ie7
4 + i
4 (e13 +e26 +e45). (9.22)
78
Clearly, S +S∗ = 1, so that we see that this new action (9.21) is no diﬀerent from the
original action (9.19). Although it has not been mentioned before, S is a projector which
has come up frequently in complex-octonionic work; it is nothing more than the right-
multiplication analogue of ν = 1
2 (1 +ie7). Or in other words,
f 1
2 (1 +ie7) =Sf ∀f∈ C⊗ O. (9.23)
It so happens that −Λ∗
j = Λj∀j = 1... 8, so that the action (9.21) may be rewritten
as
[ Λjν, S∗aν ],
[
−Λ∗
jν∗, Saν∗]
,
[
−Λ∗
jν, Saν
]
, [ Λjν∗, S∗aν∗ ].
(9.24)
Now, an action for electric charge may be found, which matches the SU (3)c action of
(9.24). Namely,
[Qν, S∗aν ], [−Q∗ν∗, Saν∗ ],
[−Q∗ν, Saν ], [Qν∗, S∗aν∗ ].
(9.25)
Under these actions (9.24) and (9.25), we ﬁnd SU (3)c and U(1)em charge assignments,
which are consistent with three generations of standard model particles. Below, we relabel
the states given earlier in equations (9.7)-(9.16), so as to now specify their electric charges.
At this level, we are not specifying which generation each state belongs to, so for
i = 1, 2, 3, the three states with electric charge of -1 will be labelled e−
i ; the three states
with electric charge of +1 will be labelled e+
i ; the three states with electric charge of 2 /3
will be labelledui; the three states with electric charge of−2/3 will be labelled ¯ui; the three
states with electric charge−1/3 will be labelleddi, and the three states with electric charge
1/3 will be labelled ¯di. Since SU (3)c and U(1)em do not distinguish between neutrinos, νi
and anti-neutrinos, ¯νi, we will then label the six states with electric charge of zero as ni
and ¯ni, where the symbol ni could represent either a neutrino or anti-neutrino.
79
n1←−𝓁a≡ (1 +ie13 +ie26 +ie45)ν =S𝓁 aν,
n2←−𝓁b≡ (3−ie13−ie26−ie45)ν =S∗𝓁bν,
n3←−𝓁c≡ (−ie124−e125 +e146−ie156)ν =S∗𝓁cν,
e+
1 ←−𝓁d≡ (−ie1−e3 +e126 +e145)ν =S𝓁 dν,
e+
2 ←−𝓁e≡ (ie2 +e6 +e123 +ie136)ν =S𝓁 eν,
e+
3 ←−𝓁f≡ (ie4 +e5−e134 +ie135)ν =S𝓁 f ν,
(9.26)
uR
1 ←−qR
1 ≡ (−ie12−e16 +e23 +ie36)ν =S∗qR
1 ν
uG
1 ←−qG
1 ≡ (−ie24−e25 +e46−ie56)ν =S∗qG
1 ν
uB
1 ←−qB
1 ≡ (ie14 +e15 +e34−ie35)ν =S∗qB
1 ν
(9.27)
¯uR
2 ←− ¯qR
2 ≡ (ie12−e16 +e23−ie36)ν =S ¯qR
2 ν
¯uG
2 ←− ¯qG
2 ≡ (ie24−e25 +e46 +ie56)ν =S ¯qG
2 ν
¯uB
2 ←− ¯qB
2 ≡ (−ie14 +e15 +e34 +ie35)ν =S ¯qB
2 ν,
(9.28)
¯uR
3 ←− ¯qR
3 ≡ (ie4 +e5 +e134−ie135)ν =S∗ ¯qR
3 ν
¯uG
3 ←− ¯qG
3 ≡ (ie1 +e3 +e126 +e145)ν =S∗ ¯qG
3 ν
¯uB
3 ←− ¯qB
3 ≡ (ie2 +e6−e123−ie136)ν =S∗ ¯qB
3 ν,
(9.29)
¯dR
1 ←− ¯qR
4 ≡ (ie1−e3 +e126−e145)ν =S ¯qR
4 ν
¯dG
1 ←− ¯qG
4 ≡ (−ie4 +e5 +e134 +ie135)ν =S ¯qG
4 ν
¯dB
1 ←− ¯qB
4 ≡ (ie124−e125−e146−ie156)ν =S ¯qB
4 ν,
(9.30)
¯dR
2 ←− ¯qR
5 ≡ (−ie2 +e6 +e123−ie136)ν =S ¯qR
5 ν
¯dG
2 ←− ¯qG
5 ≡ (ie124−e125 +e146 +ie156)ν =S ¯qG
5 ν
¯dB
2 ←− ¯qB
5 ≡ (ie4−e5 +e134 +ie135)ν =S ¯qB
5 ν,
(9.31)
¯dR
3 ←− ¯qR
6 ≡ (ie124 +e125 +e146−ie156)ν =S ¯qR
6 ν
¯dG
3 ←− ¯qG
6 ≡ (ie2−e6 +e123−ie136)ν =S ¯qG
6 ν
¯dB
3 ←− ¯qB
6 ≡ (−ie1 +e3 +e126−e145)ν =S ¯qB
6 ν.
(9.32)
80
Taking the complex conjugate,∗: i↦→−i, of these 32 basis vectors gives 32 new linearly
independent basis vectors:
¯n1←−𝓁∗
a = (1−ie13−ie26−ie45)ν∗ =S∗𝓁∗
aν∗,
¯n2←−𝓁∗
b = (3 +ie13 +ie26 +ie45)ν∗ =S𝓁∗
b ν∗,
¯n3←−𝓁∗
c = (ie124−e125 +e146 +ie156)ν∗ =S𝓁∗
c ν∗,
e−
1 ←−𝓁∗
d = (ie1−e3 +e126 +e145)ν∗ =S∗𝓁∗
dν∗,
e−
2 ←−𝓁∗
e = (−ie2 +e6 +e123−ie136)ν∗ =S∗𝓁∗
eν∗,
e−
3 ←−𝓁∗
f = (−ie4 +e5−e134−ie135)ν∗ =S∗𝓁∗
f ν∗,
(9.33)
¯uR
1 ←−qR∗
1 = (ie12−e16 +e23−ie36)ν∗≡ ¯qR
1 =S ¯qR
1 ν∗
¯uG
1 ←−qG∗
1 = (ie24−e25 +e46 +ie56)ν∗≡ ¯qG
1 =S ¯qG
1 ν∗
¯uB
1 ←−qB∗
1 = (−ie14 +e15 +e34 +ie35)ν∗≡ ¯qB
1 =S ¯qB
1 ν∗
(9.34)
uR
2 ←− ¯qR∗
2 = (−ie12−e16 +e23 +ie36)ν∗≡qR
2 =S∗qR
2 ν∗
uG
2 ←− ¯qG∗
2 = (−ie24−e25 +e46−ie56)ν∗≡qG
2 =S∗qG
2 ν∗
uB
2 ←− ¯qB∗
2 = (ie14 +e15 +e34−ie35)ν∗≡qB
2 =S∗qB
2 ν∗
(9.35)
and so on.
