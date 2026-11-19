---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-008-22-applications-in-the-skein-of-the-annulus
section_title: "Applications in the skein of the annulus"
section_number: 2.2
pages: 8-10
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
Applications in the skein of the annulus
The elements Qλ have a very nice interpretation as Schur functions in C.
Lukac showed in [6] that Qλ can be identiﬁed with the Schur function
sλ(
X
i≥0
citi)
of the series P citi whose coeﬃcients ci ∈C are the closures Qλ of the sin-
gle column idempotents with λ = 1i = (1, . . . , 1), under the convention that
8
c0 = 1 ∈C, represented by the empty diagram. This has been known in prin-
ciple for some time, but the proof in [1] was fairly circuitous and had to refer
at one point to quantum group work. Kawagoe [3] used these Schur functions
and proved that they were eigenvectors of ϕ, but his proof too was relatively
complicated. Lukac gave a much more satisfactory skein proof, using a fur-
ther skein-based algebra, coupled with the knowledge that the eigenvalues
of ϕ|Cn are distinct and the elements Qλ can essentially be characterised as
eigenvectors of ϕ.
The fact that Qλ is also an eigenvector of every ϕ(Y ), which is not at
all clear at ﬁrst sight for the Schur function sλ(P citi), is the feature that
allows us to complete our analysis here, using the consequence that tλ is a
homomorphism.
For the sake of brevity of notation we write λ in place of Qλ as an element
of C. As Schur functions of a power series these elements multiply according
to the Littlewood-Richardson rules for Young diagrams. We make use of
this later when we calculate the product in C of the elements ci and dj
corresponding to a single row and column respectively.
From the series Eλ(t), deﬁned in (1) above, we can ﬁnd ⟨λ, µ⟩by calcu-
lating its Schur function sµ(Eλ(t)) and using the following lemma.
Lemma 2.1 We have
sµ(Eλ(t)) =
1
⟨λ⟩⟨λ, µ⟩
for any Young diagrams λ and µ.
Proof :
Applying the homomorphism tλ to the power series P citi gives
Eλ(t) = tλ(P citi). Then
sµ(Eλ(t)) = tλ(sµ(
X
citi)) = tλ(µ) =
1
⟨λ⟩⟨λ, µ⟩.
✷
We also deﬁne
Hλ(t) =
1
⟨λ⟩
X
j≥0
⟨λ, dj⟩tj = tλ(
X
djtj)
for any Young diagram λ, taking d0 = 1.
Lemma 2.2 We have
Eλ(t)Hλ(−t) = 1
for any Young diagram λ.
9
Proof : Apply the homomorphism tλ to the two power series with coeﬃcients
in C in the equation

X
i≥0
citi



X
j≥0
dj(−t)j

= 1
proved by direct skein theory in [1]. The equation follows alternatively from
the fact that the elements dj in C are the Schur functions corresponding to
single row diagrams.
✷
3
