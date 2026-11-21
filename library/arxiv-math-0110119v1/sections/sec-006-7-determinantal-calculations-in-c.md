---
doc_id: arxiv-math-0110119v1
doc_title: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus"
section_id: sec-006-7-determinantal-calculations-in-c
section_title: "Determinantal calculations in C′"
section_number: 7
pages: 11-17
source_pdf: 0110119v1.pdf
source_sha256: 4904a86e8a340f59
toc_source: inferred
doc_brief: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus — The Hecke algebra Hn contains well known idempotents Eλ which are indexed by Young diagrams with n cells."
---
Determinantal calculations in C′
Lemma 7.1 For any integer r ≥2 and integers i1, i2, . . . , ir we have an equality
of (r × r)-determinants in C′+

hi1e
· · ·
hi1+r−2e
ti1+r−1
...
...
...
hire
· · ·
hir+r−2e
tir+r−1

= s2(r−1)

ehi1
· · ·
ehi1+r−2
ti1+r−1
...
...
...
ehir
· · ·
ehir+r−2
tir+r−1

.
Proof Since ti = hie −ehi, we deduce from lemma 6.4 by the multilinearity of
the determinant that

hie
ti+1
hje
tj+1

 = s2

ehi
ti+1
ehj
tj+1

(7.1)
and

ti
ti+1
tj
tj+1

 = (1 −s−2)

hie
ti+1
hje
tj+1

 .
(7.2)
We remark that equation (7.1) is our claim in the case r = 2.
From now on let r ≥3. We see that

ti1
ti1+1
ti1+2
· · ·
ti1+r−1
...
...
...
...
tir
tir+1
tir+2
· · ·
tir+r−1

= (1 −s−2)

hi1e
ti1+1
ti1+2
· · ·
ti1+r−1
...
...
...
...
hire
tir+1
tir+2
· · ·
tir+r−1

by developing the determinant on the left hand side by the ﬁrst two columns,
applying equation (7.2) to each summand, and redeveloping the determinant. By
11
doing this successively for the columns 1 and 2, 2 and 3, ..., (r −1) and r, we
deduce that

ti1
· · ·
ti1+r−2
ti1+r−1
...
...
...
tir
· · ·
tir+r−2
tir+r−1

= (1 −s−2)r−1

hi1e
· · ·
hi1+r−2e
ti1+r−1
...
...
...
hire
· · ·
hir+r−2e
tir+r−1

.
On the other hand, if we use the equation from lemma 6.4 instead of equation
(7.2) in the above argument, we get

ti1
· · ·
ti1+r−2
ti1+r−1
...
...
...
tir
· · ·
tir+r−2
tir+r−1

= (s2 −1)r−1

ehi1
· · ·
ehi1+r−2
ti1+r−1
...
...
...
ehir
· · ·
ehir+r−2
tir+r−1

.
The above two equations imply that

hi1e
· · ·
hi1+r−2e
ti1+r−1
...
...
...
hire
· · ·
hir+r−2e
tir+r−1

= s2(r−1)

ehi1
· · ·
ehi1+r−2
ti1+r−1
...
...
...
ehir
· · ·
ehir+r−2
tir+r−1

.
⋄
The ring of symmetric functions (in countably many variables) is freely gen-
erated as a commutative algebra by the complete symmetric functions h1, h2, . . ..
We therefore have a well deﬁned map from the ring of symmetric functions to
the skein of the annulus by mapping the complete symmetric function hi to the
skein element hi ∈C. We denote the image of the Schur function sλ by Sλ. The
Schur function sλ can be expressed in terms of the complete symmetric functions
via the formula sλ = det(hλi+j−i)1≤i,j≤l(λ) from [8]. We therefore have
Sλ = det(hλi+j−i)1≤i,j≤l(λ) ∈Cn
where n = |λ|. We recall the linear map Γ from section 4.
Theorem 7.2 We have Γ(Sλ) = qλSλ in C+ with the scalar
qλ = v−1 −v
s −s−1 + vs−1
l(λ)
X
k=1
(s2(k−λk) −s2k).
Proof For any elements α and β of the skein of the annulus C we have (αe)·(βe) =
(αβ)e in C′ where e is the identity of C′. Hence
Sλe = det(hλi+j−ie)1≤i,j≤l(λ).
12
Similarly
eSλ = det(ehλi+j−i)1≤i,j≤l(λ).
We denote l(λ) by n from now on. We remark that the closure (eSλ)∧is equal
to Sλ with a disjoint circle which can be removed at the expense of the scalar
(v−1 −v)/(s −s−1). The closure (Sλe)∧is equal to Γ(Sλ).
By the multilinearity of the determinant we can write the diﬀerence of any
two (n × n)-determinants as a telescope sum of n (n × n)-determinants.

y11
· · ·
y1n
...
...
yn1
· · ·
ynn

−

z11
· · ·
z1n
...
...
zn1
· · ·
znn

=
n
X
k=1

y1 1
· · ·
y1 k−1
(y1 k −z1 k)
z1 k+1
· · ·
z1 n
...
...
...
...
...
yn 1
· · ·
yn k−1
(yn k −zn k)
zn k+1
· · ·
zn n

.
Applying this formula to the determinants for Sλe and eSλ we get
Sλe −eSλ =
n
X
k=1

hλ1e
· · ·
hλ1+k−2e
tλ1+k−1
ehλ1+k
· · ·
ehλ1+n−1
...
...
...
...
...
hλn+1−ne
· · ·
hλn+k−1−ne
tλn+k−n
ehλn+k+1−n
· · ·
ehλn

.
By lemma 7.1 we deduce that
Sλe −eSλ =
n
X
k=1
s2(k−1)

ehλ1
· · ·
ehλ1+k−2
tλ1+k−1
ehλ1+k
· · ·
ehλ1+n−1
...
...
...
...
...
ehλn+1−n
· · ·
ehλn+k−1−n
tλn+k−n
ehλn+k+1−n
· · ·
ehλn

.
The n determinants appearing here are very special because each of them is a
sum of terms of the form of a ti above a product of hj’s. Therefore the closure of
each determinant is ˆti above a product of hj’s. Explicitly,
(Sλe)∧−(eSλ)∧=
n
X
k=1
s2(k−1)

hλ1
· · ·
hλ1+k−2
ˆtλ1+k−1
hλ1+k
· · ·
hλ1+n−1
...
...
...
...
...
hλn+1−n
· · ·
hλn+k−1−n
ˆtλn+k−n
hλn+k+1−n
· · ·
hλn

.
13
We know by corollary 6.3 that ˆti is a scalar multiple of hi. Hence
(Sλe)∧−(eSλ)∧=
n
X
k=1

hλ1
· · ·
hλ1+k−2
β1 khλ1+k−1
hλ1+k
· · ·
hλ1+n−1
...
...
...
...
...
hλn+1−n
· · ·
hλn+k−1−n
βn khλn+k−n
hλn+k+1−n
· · ·
hλn

where βi k = s2(k−1)(s1−2(λi+k−i) −s)v. We use the notation ρi = s2i−2λi−1v and
γk = −s2k−1v, hence βi k = ρi + γk. By the multilinearity of the determinant we
get
(Sλe)∧−(eSλ)∧= (γ1 + . . . + γn)Sλ +
n
X
k=1

hλ1
· · ·
hλ1+k−2
ρ1hλ1+k−1
hλ1+k
· · ·
hλ1+n−1
...
...
...
...
...
hλn+1−n
· · ·
hλn+k−1−n
ρnhλn+k−n
hλn+k+1−n
· · ·
hλn

.
We bring the sum over the determinants in a more appropriate form via the
general formula for variables wij and ρk,
n
X
k=1

w1 1
· · ·
w1 k−1
ρ1w1 k
w1 k+1
· · ·
w1 n
...
...
...
...
...
wn 1
· · ·
wn k−1
ρnwn k
wn k+1
· · ·
wn n

=
(ρ1 + · · · + ρn)

w1 1
· · ·
w1 n
...
...
wn 1
· · ·
wn n

.
Applying this formula we get
(Sλe)∧−(eSλ)∧
=
(γ1 + · · · + γn)Sλ + (ρ1 + · · · + ρn)Sλ
=
(β1 1 + · · · + βn n)Sλ.
Since (eSλ)∧= (v−1 −v)/(s −s−1)Sλ, as mentioned above, we deduce that
(Sλe)∧= qλSλ with
qλ
=
v−1 −v
s −s−1 + β1 1 + · · · + βn n
=
v−1 −v
s −s−1 + vs−1
n
X
k=1
(s2(k−λk) −s2k).
⋄
14
8
Proof that Sλ = Qλ
We have to introduce some notation. Let λ be a Young diagram. A standard
tableau of λ is a labelling of the cells of λ with the integers 1, 2, . . . , |λ| which is
increasing in each row from left to right and in each column from top to bottom.
The Young diagram underlying a standard tableau t is denoted by λ(t). The
number of diﬀerent standard tableaux for a Young diagram λ is denoted by d(λ).
Theorem 8.1 Sλ is equal to Qλ for any Young diagram λ.
Proof Qλ is non-zero in C. Since the scalars qλ and cλ from theorem 7.2 and
from lemma 4.1 are equal, we have that Sλ and Qλ are eigenvectors with the
same eigenvalue under the map Γ. Possibly, Sλ = 0. The set of Qλ for all Young
diagrams λ with n cells is a linear basis for Cn by lemma 4.2. Furthermore, the
eigenvalues cλ are pairwise diﬀerent.
Hence, we deduce that Sλ is a scalar multiple of Qλ for any Young diagram
λ with n cells. This scalar is a rational function in x, v and s, and it is possibly
equal to zero.
We denote the Young diagram consisting of a single cell by ✷. We have that
S✷= Q✷is the single core circle of the annulus. Hence, Sn
✷= Qn
✷are n parallel
copies of the core circle of the annulus.
Macdonald states in [8] example I.3.11 the multiplication rule for the Schur
function sλ with the ﬁrst power sum p1 (which is equal to s✷). This is a special
case of the Littlewood-Richardson rule for the multiplication of Schur functions.
In this case, the rule is
sµs✷=
X
µ⊂η
|η|=|µ|+1
sη.
By applying this successively we get
sn
✷=
X
|λ|=n
dλsλ
where dλ is the number of standard tableaux of λ. Therefore,
Sn
✷=
X
|λ|=n
dλSλ
(8.3)
in Cn.
Blanchet describes in [3] an explicit semi-simple decomposition of Rn
n. The
lemmas he uses for his construction are also contained in [2] as explained in
15
[7]. Generalizing results of Wenzl [12], Blanchet constructs elements αtβτ ∈Rn
n
(which are denoted αtτ here) for standard tableaux t and τ with λ(t) = λ(τ).
These elements satisfy αtταsσ = δτsαtσ where δτs is the Kronecker-Delta, i.e. the
elements αtτ multiply like matrix-units. An important observation is that the
closure ∆(αtτ) ∈C+ is equal to zero if t̸ = τ, and ∆(αtτ) = Qλ(t) if t = τ.
Furthermore, the identity braid idn ∈Rn
n is equal to the sum of all αtt, i.e.
idn =
X
|λ(t)|=n
αtt.
We apply the closure map ∆: Rn
n →Cn to the above equation and we get that
Qn
✷=
X
|λ|=n
dλQλ.
(8.4)
Since S✷= Q✷, equations (8.3) and (8.4) imply that
X
|λ|=n
dλ(Qλ −Sλ) = 0.
Since any Sλ diﬀers from Qλ by a scalar, and {Qλ | λ has n cells} is a basis of Cn
by lemma 4.2, we get that Qλ = Sλ.
⋄
Theorem 8.1 together with the deﬁnition of Sλ implies that
Theorem 8.2 The linear map induced by sλ 7→Qλ from the ring of symmetric
functions to the skein of the annulus C is a ring homomorphism.
Acknowledgements The results are part of my PhD thesis. I thank my super-
visor Prof. Hugh Morton for his guidance and help. The thesis was funded by
the DAAD by a HSP-III-grant.
16
