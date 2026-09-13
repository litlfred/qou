---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-054-102-determinantial-modules-and-t-system-we-will
section_title: "Determinantial modules and T-system. We will use the materials in § 9 to"
section_number: 10.2
pages: 80-84
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
obtain properties on the determinantial modules.
In the rest of this paper, we assume that R is symmetric and the base ﬁeld k is
of characteristic 0. Under this condition, the family of self-dual simple R-modules
corresponds to the upper global basis of Aq(n) by Theorem 2.1.4.
Let ch be the map from K(R-gmod) to Aq(n) obtained by composing ι and the
isomorphism ( 2.2) in Theorem 2.1.2.
Deﬁnition 10.2.1. For λ ∈ P+ and µ,ζ ∈ Wλ such that µ ≼ ζ, let M(µ,ζ ) be a
simple R(ζ −µ)-module such that ch(M(µ,ζ )) = D(µ,ζ ).
Since D(µ,ζ ) is a member of the upper global basis, such a module exists uniquely
due to Theorem 2.1.4. The module M(µ,ζ ) is self-dual and we call it the determinantial
module.
Lemma 10.2.2. M(µ,ζ ) is a real simple module.
Proof. It follows from ch( M(µ,ζ ) ◦ M(µ,ζ )) = ch
(
M(µ,ζ )
) 2
=q−(ζ,ζ −µ)D(2µ, 2ζ) which
is a member of the upper global basis up to a power of q. Here the last equality follows
from Corollary 9.1.3. □
Proposition 10.2.3. Letλ,µ ∈ P+, and s,s ′,t,t ′ ∈W such that ℓ(s′s) = ℓ(s′) +ℓ(s),
ℓ(t′t) = ℓ(t′) +ℓ(t), s′sλ ≼ t′λ and s′µ ≼ t′tµ. Then
(i) M(s′sλ,t ′λ) and M(s′µ,t ′tµ) commute,
(ii) Λ
(
M(s′sλ,t ′λ), M(s′µ,t ′tµ)
)
= (s′sλ +t′λ, t′tµ −s′µ),
(iii) ~Λ
(
M(s′sλ,t ′λ), M(s′µ,t ′tµ)
)
= (t′λ, t′tµ −s′µ),
~Λ
(
M(s′µ,t ′tµ), M(s′sλ,t ′λ)
)
= (s′µ −t′tµ, s′sλ).
Proof. It is a consequence of Proposition 9.1.6 (ii) and Corollary 4.1.4. □
Proposition 10.2.4. Letλ ∈ P+, µ,ζ ∈Wλ such that µ ≼ ζ and i ∈I.
(i) If n := ⟨hi,µ ⟩ ≥ 0, then
εi(M(µ,ζ )) = 0 and M(siµ,ζ ) ≃ ~Fn
i M(µ,ζ ) ≃L(in) ∇ M(µ,ζ ) in R-gmod.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 81
(ii) If ⟨hi,µ ⟩ ≤ 0 and siµ ≼ ζ, then εi(M(µ,ζ )) = −⟨hi,µ ⟩.
(iii) If m := −⟨hi,ζ ⟩ ≥ 0, then
ε∗
i (M(µ,ζ )) = 0 and M(µ,siζ) ≃ ~F ∗m
i M(µ,ζ ) ≃ M(µ,ζ ) ∇L(im) in R-gmod.
(iv) If ⟨hi,ζ ⟩ ≥ 0 and µ ≼ siζ, then ε∗
i (M(µ,ζ )) = ⟨hi,ζ ⟩.
Proof. It is a consequence of Lemma 9.1.5. □
Proposition 10.2.5. Assume that u,v ∈W andi ∈I satisfyu<us i andv <vsi ≤u.
(i) We have exact sequences
(10.6)
0 − →M(uλ,vλ ) − →q(vsi̟i,v̟i−u̟i)M(usi̟i,vsi̟i) ◦ M(u̟i,v̟i)
− →q−1+(v̟i,vsi̟i−u̟i)M(usi̟i,v̟i) ◦ M(u̟i,vsi̟i) − →0,
and
(10.7)
0 − →q1+(v̟i,vsi̟i−u̟i)M(usi̟i,v̟i) ◦ M(u̟i,vsi̟i)
− →q(v̟i,vsi̟i−usi̟i)M(u̟i,v̟i) ◦ M(usi̟i,vsi̟i) − →M(uλ,vλ ) − →0,
whereλ =si̟i +̟i.
(ii) d
(
M(u̟i,v̟i), M(usi̟i,vsi̟i)
)
= 1.
Proof. Since the proof of ( 10.6) is similar, let us only prove ( 10.7). (Indeed, they are
dual to each other.)
Set
X =q(v̟i,vsi̟i−u̟i)M(usi̟i,v̟i) ◦ M(u̟i,vsi̟i),
Y =q(v̟i,vsi̟i−usi̟i)M(u̟i,v̟i) ◦ M(usi̟i,vsi̟i),
Z = M(uλ,vλ ).
Then Proposition 9.2.1 implies that
ch(Y ) = ch(qX ) + ch(Z).
Since X and Z are simple and self-dual, our assertion follows from Lemma 3.2.19. □
10.3. Generalized T-system on determinantial module.
Theorem 10.3.1. Let λ ∈ P+ and µ1,µ 2,µ 3 ∈ Wλ such that µ1 ≼ µ2 ≼ µ3. Then
there exists a canonical epimorphism
M(µ1,µ 2) ◦ M(µ2,µ 3) ։ M(µ1,µ 3),
which is equivalent to saying that M(µ1,µ 2) ∇ M(µ2,µ 3) ≃ M(µ1,µ 3).
In particular, we have
~Λ( M(µ1,µ 2), M(µ2,µ 3)) = 0 and Λ( M(µ1,µ 2), M(µ2,µ 3)) = −(µ1 −µ2,µ 2 −µ3).
82 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Proof. (a) Our assertion follows from Theorem 9.3.3 and Theorem 4.2.1 when µ3 =λ.
(b) We shall prove the general case by induction on |λ −µ3|. By (a), we may assume
that µ3 ⁄= λ. Then there exists i such that ⟨hi,µ 3⟩< 0. The induction hypothesis
yields that
M(µ1,µ 2) ∇ M(µ2,siµ3) ≃ M(µ1,siµ3).
Since µ1 ≼ µ2 ≼ µ3 ≼ siµ3, Proposition 10.2.4 (iv) gives
ε∗
i
(
M(µ2,siµ3)
)
=ε∗
i
(
M(µ1,siµ3)
)
= −⟨hi,µ 3⟩.
Then Proposition 10.1.8 implies that
~E∗
i
max(
M(µ1,µ 2) ∇ M(µ2,siµ3)
)
≃ M(µ1,µ 2) ∇
(~E∗
i
maxM(µ2,siµ3)
)
,
from which we obtain
M(µ1,µ 3) ≃ M(µ1,µ 2) ∇ M(µ2,µ 3)
By Lemma 3.1.4, we have ~Λ
(
M(µ1,µ 2), M(µ2,µ 3)
)
= 0. Hence we obtain
Λ
(
M(µ1,µ 2), M(µ2,µ 3)
)
= −
(
wt(M(µ1,µ 2), wt(M(µ2,µ 3))
)
. □
Proposition 10.3.2. Leti ∈I and x,y,z ∈W .
(i) If ℓ(xy) = ℓ(x) +ℓ(y), zsi >z , xy ≥zsi and x ≥z, then we have
d(M(xy̟i,zsi̟i), M(x̟i,z̟i)) ≤ 1.
(ii) If ℓ(zy) = ℓ(z) +ℓ(y), xsi >x , xsi ≥zy and x ≥z, then we have
d(M(xsi̟i,zy̟ i), M(x̟i,z̟i)) ≤ 1.
Proof. In the course of proof, we omit ι−1
̟i,̟i for the sake of simplicity. If y̟i = ̟i,
then the assertion follows from Proposition 10.2.3 (i). Hence we may assume that
y′ :=ysi<y .
Let us show (i). By Proposition 9.4.1, we have
(10.8)
∆(y̟i,si̟i)∆(̟i,̟i) = q−1Gup ((uy̟i ⊗u̟i) ⊗ (usi̟i ⊗u̟i)r)
+Gup(ι−1
λ (˜e∗
ib) ⊗ur
λ),
where λ = ̟i +si̟i and b = ι̟i(uy̟i) ∈ B(∞). Let S∗
z,λ be the operator on Aq(g)
given by the application of e(a1)
j1 · · ·e(at)
jt from the right, where z =sjt · · ·sj1 is a reduced
expression of z and ak = ⟨hjk,sjk−1 · · ·sj1λ⟩. Then applying S∗
z,λ to ( 10.8), we obtain
∆(y̟i,zsi̟i)∆(̟i,z̟i) = q−1Gup ((uy̟i ⊗u̟i) ⊗ (uzsi̟i ⊗uz̟i)r)
+Gup(ι−1
λ (˜e∗
ib) ⊗ur
zλ).
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 83
Recall that µ ∈ P is called x-dominant if ck ≥ 0. Here x = sir · · ·si1 is a reduced
expression of x and ck := ⟨hik,sik−1 · · ·si1µ⟩ (1 ≤ k ≤ r). Recall that an element
v ∈Aq(g) with wt l(v) = µ is called x-highest if µ is x-dominant and
f 1+ck
ik f (ck−1)
ik−1 · · ·f (c1)
i1 v = 0 for any k (1 ≤k ≤r).
If v is x-highest, then v is a linear combination of x-highest Gup(b)’s. Moreover,
Sx,µGup(b) :=f (cr)
ir · · ·f (c1)
i1 Gup(b) is either a member of the upper global basis or zero.
Since ∆( y̟i,zsi̟i)∆(̟i,z̟i) is x-highest of weight µ :=y̟i +̟i, we obtain
∆(xy̟i,zsi̟i)∆(x̟i,z̟i) = q−1Gup ((uxy̟i ⊗ux̟i) ⊗ (uzsi̟i ⊗uz̟i)r)
+Sx,µGup(ι−1
λ (˜e∗
ib) ⊗ur
zλ).
Applying pn, we obtain
qcD(xy̟i,zsi̟i)D(x̟i,z̟i) = q−1pnGup ((uxy̟i ⊗ux̟i) ⊗ (uzsi̟i ⊗uz̟i)r)
+pnSx,µGup(ι−1
λ (˜e∗
ib) ⊗ur
zλ)
for some integer c. Hence we obtain (i) by Lemma 3.2.19 (i).
(ii) is proved similarly. By applying ϕ∗ to ( 10.8), we obtain
q(si̟ii,̟ii)−(y̟ii,̟ii)∆(si̟i,y̟i)∆(̟i,̟i) = q−1Gup ((usi̟i ⊗u̟i) ⊗ (uy̟i ⊗u̟i)r)
+Gup(uλ ⊗ (ι−1
λ ˜e∗
ib)r).
Here we used Proposition 8.1.4. Then the similar arguments as above show (ii). □
Proposition 10.3.3. Letx ∈W such that xsi >x and x̟i ⁄=̟i. Then we have
d(M(xsi̟i,x̟i), M(x̟i,̟i)) = 1.
Proof. By Proposition 10.3.2 (ii), we have d(M(xsi̟i,x̟i), M(x̟i,̟i)) ≤ 1. Assuming
d(M(xsi̟i,x̟i), M(x̟i,̟i)) = 0, let us derive a contradiction.
By Theorem 10.3.1 and the assumption, we have
M(xsi̟i,x̟i) ◦ M(x̟i,̟i) ≃ M(xsi̟i,̟i).
Hence we have
ε∗
j (M(xsi̟i,̟i)) = ε∗
j (M(xsi̟i,x̟i)) +ε∗
j (M(x̟i,̟i))
for any j ∈I. Since xsi̟i ≼ x̟i ≼ si̟i, Proposition 10.2.4 implies that
ε∗
j (M(xsi̟i,̟i)) = ε∗
j (M(x̟i,̟i)) = ⟨hj,̟i⟩.
It implies that
ε∗
j (M(xsi̟i,x̟i)) = 0 for any j ∈I.
It is a contradiction since wt
(
M(xsi̟i,x̟i)
)
=xsi̟i −x̟i does not vanish. □
84 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
