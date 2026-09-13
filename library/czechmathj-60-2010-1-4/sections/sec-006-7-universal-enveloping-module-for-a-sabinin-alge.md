---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: sec-006-7-universal-enveloping-module-for-a-sabinin-alge
section_title: "Universal enveloping module for a Sabinin algebra"
section_number: 7
pages: 14-18
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
---
In this section we give a Gröbner-Shirshov basis for a univer sal enveloping module
for a Sabinin algebra. By using this result and Lemma 3.2, we ﬁ nd a linear basis for
such a module.
Deﬁnition 7.1 ([21]). A vector space V is called a Sabinin algebra if it is en-
dowed with a multilinear operation ⟨; ⟩such that for any x1, x 2, . . . , x m, y, z ∈ V and
any m /greaterorequalslant0,
⟨x1, x 2, . . . , x m; y, z ⟩
71
satisﬁes the identities
⟨x1, x 2, . . . , x m; y, z ⟩= −⟨x1, x 2, . . . , x m; z, y ⟩,
⟨x1, x 2, . . . , x r, a, b, x r+1, . . . , x m; y, z ⟩ − ⟨x1, x 2, . . . , x r, b, a, x r+1, . . . , x m; y, z ⟩
+
r∑
k=0
∑
α
⟨xα1 , . . . , x αk , ⟨xαk+1 , . . . , x αr ; a, b ⟩, . . . , x m; y, z ⟩= 0,
σ x,y,z (⟨x1, x 2, . . . , x r, x ; y, z ⟩+
r∑
k=0
∑
α
⟨xα1 , . . . , x αk ; ⟨xαk+1 , . . . , x αr ; y, z ⟩, x ⟩) = 0 ,
where α runs over the set of all bijections of type α : {1, 2, . . . , r } → { 1, 2, . . . , r },
i ↦→α i, α 1 < α 2 < . . . < α k, α k+1 < . . . < α r, r /greaterorequalslant0 and σ x,y,z denotes the cyclic
sum by x, y, z .
Let X = {ai | i ∈ Λ } be a well ordered basis of V . We deﬁne the deg-lex ordering
on X ∗. Let ∆ : V → V ⊗ V be a linear map which satisﬁes ∆( ai) = 1 ⊗ ai + ai ⊗ 1,
(Id ⊗∆)∆ = (∆ ⊗ Id)∆ (coassociativity) and if τ ∆ = ∆ then τ (x ⊗ y) = y ⊗ x
(cocommutativity). It is customary to write ∆( x) = ∑ x(1) ⊗ x(2).
Let T (V ) be the tensor algebra over V endowed with its natural structure of
cocommutative Hopf algebra, that is, V ⊆ Prim (T (V )) (the primitive element of
T (V )). Let ⟨; ⟩: T (V ) ⊗ V ⊗ V → V be a map. Then we may shortly write the
deﬁnition of a Sabinin algebra as
⟨x; a, b ⟩= −⟨x; b, a ⟩, ⟨x[a, b ]y; c, e ⟩+
∑
⟨x(1)⟨x(2); a, b ⟩y; c, e ⟩= 0,
σ a,b,c(⟨xc; a, b ⟩+
∑
⟨x(1); ⟨x(2); a, b ⟩, c ⟩) = 0 ,
where [a, b ] = ab − ba.
Deﬁnition 7.2 ([21]). Let (V, ⟨; ⟩) be a Sabinin algebra. Then
˜S(V ) = T (V )/ span
⟨
xaby − xbay +
∑
x(1)⟨x(2); a, b ⟩y|x, y ∈ T (V ), a, b ∈ V
⟩
is called the universal enveloping module for V .
Since T (V ) ≃ k⟨X⟩as k-algebras, we can view ˜S(V ) as a right k⟨X⟩-module:
˜S(V ) = mod ⟨X|I⟩k⟨X⟩,
where I = {xab − xba + ∑ x(1)⟨x(2); a, b ⟩ |x ∈ X ∗, a > b, a, b ∈ X}.
For the right module, we have a right compatible well orderin g ≺ on XX ∗ by a
similar deﬁnition as in (∗). Then we have the following theorem.
72
Theorem 7.3. Let I be as above. Then, with the ordering ≺ on XX ∗ as above,
I is a Gröbner-Shirshov basis in mod⟨X⟩k⟨X⟩.
P r o o f. There are two kinds of compositions: w1 = xabc (a > b > c ) and
w2 = ucdvab (c > d , a > b ). Denote
f1 = xabc − xacb +
∑
(xa)(1)⟨(xa)(2); b, c ⟩,
f2 = xab − xba +
∑
x(1)⟨x(2); a, b ⟩,
f3 = ucdvab − ucdvba +
∑
(ucdv)(1)⟨(ucdv)(2); a, b ⟩,
f4 = ucd − udc +
∑
u(1)⟨u(2); c, d ⟩.
Then, since σ a,b,c(⟨xc; a, b ⟩+ ∑ ⟨x(1); ⟨x(2); a, b ⟩, c ⟩) = 0 , we have
(f1, f 2)w1 = xabc − xacb +
∑
x(1)a⟨x(2); b, c ⟩+
∑
x(1)⟨x(2)a; b, c ⟩
− xabc + xbac −
∑
x(1)⟨x(2); a, b ⟩c
≡ −xcab +
∑
x(1)⟨x(2); a, c ⟩b +
∑
x(1)a⟨x(2); b, c ⟩+
∑
x(1)⟨x(2)a; b, c ⟩
+ xbca −
∑
x(1)b⟨x(2); a, c ⟩ −
∑
x(1)⟨x(2)b; a, c ⟩ −
∑
x(1)⟨x(2); a, b ⟩c
≡
∑
x(1)c⟨x(2); a, b ⟩+
∑
x(1)⟨x(2)c; a, b ⟩+
∑
x(1)⟨x(2); a, c ⟩b
+
∑
x(1)a⟨x(2); b, c ⟩+
∑
x(1)⟨x(2)a; b, c ⟩ −
∑
x(1)⟨x(2); b, c ⟩a
−
∑
x(1)b⟨x(2); a, c ⟩ −
∑
x(1)⟨x(2)b; a, c ⟩ −
∑
x(1)⟨x(2); a, b ⟩c
≡
∑
x(1)⟨x(2)a; b, c ⟩+
∑
x(1)⟨x(2); ⟨x(3); b, c ⟩, a ⟩+
∑
x(1)⟨x(2)b; c, a ⟩
+
∑
x(1)⟨x(2)c; a, b ⟩+
∑
x(1)⟨x(2); ⟨x(3); c, a ⟩, b ⟩
+
∑
x(1)⟨x(2); ⟨x(3); a, b ⟩, c ⟩
≡ 0
and since ⟨x[a, b ]y; c, e ⟩+ ∑ ⟨x(1)⟨x(2); a, b ⟩y; c, e ⟩= 0,
(f3, f 4)w2
= ucdvab − ucdvba +
∑
u(1)v(1)⟨u(2)cdv(2); a, b ⟩+
∑
u(1)cv(1)⟨u(2)dv(2); a, b ⟩
+
∑
u(1)dv(1)⟨u(2)cv(2); a, b ⟩+
∑
u(1)cdv(1)⟨u(2)v(2); a, b ⟩
− ucdvab + udcvab −
∑
u(1)⟨u(2); c, d ⟩vab
73
≡ −udcvba +
∑
u(1)⟨u(2); c, d ⟩vba +
∑
u(1)v(1)⟨u(2)cdv(2); a, b ⟩
+
∑
u(1)cv(1)⟨u(2)dv(2); a, b ⟩+
∑
u(1)dv(1)⟨u(2)cv(2); a, b ⟩
+
∑
u(1)cdv(1)⟨u(2)v(2); a, b ⟩+ udcvba −
∑
u(1)v(1)⟨u(2)dcv(2); a, b ⟩
−
∑
u(1)cv(1)⟨u(2)dv(2); a, b ⟩ −
∑
u(1)dv(1)⟨u(2)cv(2); a, b ⟩
−
∑
u(1)dcv(1)⟨u(2)v(2); a, b ⟩+
∑
u(1)v(1)⟨u(2)⟨u(3); c, d ⟩v(2); a, b ⟩
+
∑
u(1)⟨u(2); c, d ⟩v(1)⟨u(3)v(2); a, b ⟩ −
∑
u(1)⟨u(2); c, d ⟩vba
≡
∑
u(1)v(1)⟨u(2)[c, d ]v(2); a, b ⟩+
∑
u(1)[c, d ]v(1)⟨u(2)v(2); a, b ⟩
+
∑
u(1)v(1)⟨u(2)⟨u(3); c, d ⟩v(2); a, b ⟩+
∑
u(1)⟨u(2); c, d ⟩v(1)⟨u(3)v(2); a, b ⟩
≡
∑
(u(1)[c, d ] + u(1)⟨u(2); c, d ⟩)v(1)⟨u(3)v(2); a, b ⟩
+
∑
u(1)v(1)⟨u(2)[c, d ]v(2); a, b ⟩+
∑
u(1)v(1)⟨u(2)⟨u(3); c, d ⟩v(2); a, b ⟩
≡ 0.
Hence, I is a Gröbner-Shirshov basis in mod⟨X⟩k⟨X⟩. □
Remark. From the above proof we can easily see that for ˜S(V ) = mod ⟨X|I⟩k⟨X⟩,
the minimal Gröbner-Shirshov basis is
G =
{
xab − xba +
∑
x(1)⟨x(2); a, b ⟩
⏐⏐⏐ x = ai1 . . . a in
(i1 ⩽ . . . ⩽ in, n /greaterorequalslant0), a > b, a, b ∈ X
}
.
Now, by Lemma 3.2 and Theorem 7.3, we can easily get the follow ing theorem.
Theorem 7.4 ([21], Poincaré-Birkhoﬀ-Witt basis). Let {ai | i ∈ Λ } be a well
ordered basis of V . Then {ai1 . . . a in | i1 ⩽ i2 ⩽ . . . ⩽ in, n /greaterorequalslant0} is a basis of ˜S(V ).
Acknowledgement. The authors would like to express their deepest gratitude
to Professor L. A. Bokut for his guidance, useful discussion s and enthusiastic encour-
agement. We also thank Professor J. M. Perez-Izquierdo for g iving us some useful
remarks.
74
