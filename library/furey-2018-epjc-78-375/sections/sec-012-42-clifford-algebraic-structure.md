---
doc_id: furey-2018-epjc-78-375
doc_title: "as a symmetry of division algebraic ladder operators"
section_id: sec-012-42-clifford-algebraic-structure
section_title: "Clifford algebraic structure"
section_number: 4.2
pages: 6-7
source_pdf: furey-2018-epjc-78-375.pdf
source_sha256: 4258820f00014b03
toc_source: outline
doc_brief: "SU(3)_C x SU(2)_L x U(1)_Y (x U(1)_X) as a symmetry of division algebraic ladder operators — We demonstrate a model which captures certain attractive features of SU(5) theory, while providing a pos- sible escape from proton decay."
---
In parallel with the case of C ⊗H, we will now consider the
left action of C ⊗O on itself. It can be conﬁrmed that com-
plex linear combinations of octonions repeatedly left multi-
plying f ∈C ⊗O may always be written in the canonical
form
M f ≡c0 f +
6

i=1
ciei f +
6

j=2
j−1

i=1
ci jei(e j f )
+
6

k=3
k−1

j=2
j−1

i=1
ci jkei(e j(ek f )) + · · ·
+ c123456e1(e2(e3(e4(e5(e6 f ))))),
(15)
where the coefﬁcients c0, ci, . . . ∈C. Readers may note that
the octonionic imaginary unit e7 is not explicitly expressed
in these maps. This is due to the fact that
e7 f = e1(e2(e3(e4(e5(e6 f )))))
∀f ∈C ⊗O,
(16)
thereby making e7 redundant as a left-action map. Of course,
e7 itself holds no preferred status within the octonions, and
the space of left-action maps may equivalently be described
by chains built from any six of the seven imaginary units.
By using the identity (16), the Eq. (15) may then be written
more compactly as
M f = c0 f +
7

i=1
ci←−
ei f +
7

j=2
j−1

i=1
ci j←−−
eie j f
+
7

k=3
k−1

j=2
j−1

i=1
ci jk←−−−
eie jek f,
(17)
where the arrows indicate the direction of bracketing, as in
←−−−
eie jek f = ←−
ei ←−
e j ←−
ek f = ei(e j(ek f )).
It can be verﬁed that
←−
ei ←−
e j f + ←−
e j ←−
ei f = ei(e j f ) + e j(ei f ) = −2δi j f
(18)
Fig. 3 The left action of C ⊗O on itself provides a faithful repre-
sentation of Cl(6), and is hence isomorphic to the 8 × 8 C matrices.
Here, left-action maps, i←−
e j , for j = 1, . . . 6, form the generating space
(1-vectors)
for i, j = 1, . . . 6, and ∀f ∈C⊗O, and furthermore that the
left action of C ⊗O on itself gives a faithful representation
of the Clifford algebra Cl(6). Please see Fig. 3. Here, multi-
plication is understood to be given by the composition of left
action maps, and hence is associative by deﬁnition. The Clif-
ford algebra Cl(6) is isomorphic to the 8×8 C matrices. This
scenario closely emulates our earlier example where the left
action of C⊗H on itself gave a faithful representation of the
Clifford algebra Cl(2), isomorphic to the 2 × 2 C matrices.
Now, the generating space given in Fig. 3 may be rewritten
in terms of a new basis,
←−
a1 ≡1
2

−←−
e5 + i←−
e4

,
←−
a2 ≡1
2

−←−
e3 + i←−
e1

,
←−
a3 ≡1
2

−←−
e6 + i←−
e2

,
←−
a1 † ≡1
2
←−
e5 + i←−
e4

,
←−
a2 † ≡1
2
←−
e3 + i←−
e1

,
←−
a3 † ≡1
2
←−
e6 + i←−
e2

.
(19)
Here, we deﬁne the conjugation † to map i →−i and ←−
e j →
−←−
e j for j = 1 . . . 7. As with the hermitian conjugation of
matrices, † also reverses the order of multiplication, that is,
the order of left action maps: (←−
x ←−y )† = ←−y †←−
x †.
Under anti-commutation, these operators behave as
{←−
ai , ←−
a j } f ≡ai(a j f ) + a j(ai f ) = 0,
{←−
ai †, ←−
a j †} f ≡a†
i (a†
j f ) + a†
j(a†
i f ) = 0,
{←−
ai , ←−
a j †} f ≡ai(a†
j f ) + a†
j(ai f ) = δi j f,
∀f ∈C ⊗O,
(20)
which is simply a higher-dimensional analogue of equa-
tions (7).
From this point forward, we will not be interested in the
object f ∈C⊗O, only the maps ←−
ai and ←−
a j † which act on it.
Hence, we will no longer refer to f explicitly. Furthermore,
in the interest of simplifying notation, we will forfeit the use
123
of arrows on our left action maps, although their presence
should be implicitly understood. Equations (20) can then be
rewritten more succinctly as
{ai, a j} = 0,
{a†
i , a†
j} = 0,
{ai, a†
j} = δi j.
(21)
