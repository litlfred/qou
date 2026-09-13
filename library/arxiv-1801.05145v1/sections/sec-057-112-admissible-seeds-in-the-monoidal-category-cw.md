---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-057-112-admissible-seeds-in-the-monoidal-category-cw
section_title: "Admissible seeds in the monoidal category Cw. For 0 ≤t ≤s ≤r, we set"
section_number: 11.2
pages: 85-89
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
M(s,t ) = M(λs,λt). It is a real simple module with ch( M(s,t )) = D(s,t ).
Deﬁnition 11.2.1. Forw ∈W , let Cw be the smallest monoidal abelian full subcategory
of R-gmod satisfying the following properties:
(i) Cw is stable under the subquotients, extensions and grading sh ifts,
(ii) Cw contains M(s,s −) for all 1 ≤s ≤ℓ(w).
Then by [ 11], M ∈R-gmod belongs to Cw if and only if ch( M) belongs to Aq(n(w)).
Hence we have a Z[q±1]-algebra isomorphism
K(Cw) ≃Aq(n(w))Z[q±1].
We set
Λ := (Λ( M(i, 0), M(j, 0)))1≤i,j≤r and D = (di)1≤i≤r := (wt(M(i, 0)))1≤i≤r.
Then, by Proposition 10.2.3, S :=({M(k, 0)}1≤k≤r, −Λ, ~B,D ) is a quantum monoidal
seed in Cw. We are now ready to state the main theorem in this section:
86 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Theorem 11.2.2. The pair
(
{M(k, 0)}1≤k≤r, ~B
)
is admissible.
As we already explained, combined with Theorem 7.1.3 and Corollary 7.1.4, this
theorem implies the following theorem.
Theorem 11.2.3. The category Cw is a monoidal categoriﬁcation of the quantum clus-
ter algebra Aq1/2(n(w)).
In the course of proving Theorem 11.2.2, we omit grading shifts if there is no danger
of confusion.
We shall start the proof of Theorem 11.2.2 by proving that, for each s ∈Jex, there
exists a simple module X such that


(a) there exists a surjective homomorphism (up to a grading shift)
X ◦ M(s, 0) ։ ◦t;bt,s>0M(t, 0)◦bt,s,
(b) there exists a surjective homomorphism (up to a grading shift)
M(s, 0) ◦X ։ ◦t; bt,s<0M(t, 0)◦−bt,s,
(c) d(X, M(s, 0)) = 1.
(11.2)
We set
x :=is ∈I,
Is := {ik |s<k <s +} ⊂ I \ {x},
A := ◦
t<s<t+<s+
M(t, 0)◦|ais,it | = ◦
y∈Is
M(s−(y), 0)◦|ax,y|.
Then A is a real simple module.
Now we claim that the following simple module X satisﬁes the conditions in ( 11.2):
X := M(s+,s ) ∇A.
Let us show ( 11.2) (a). The incoming arrows to s are
• t
|ax,it |
− − − →s for 1 ≤t<s<t + <s +,
• s+ − − →s.
Hence we have
◦t;bt,s>0M(t, 0)◦bt,s ≃A ◦M(s+, 0).
Then the morphism in (a) is obtained as the composition:
X ◦ M(s, 0) ֌A ◦ M(s+,s ) ◦ M(s, 0) ։A ◦ M(s+, 0).(11.3)
Here the second epimorphism is given in Theorem 10.3.1, and Lemma 3.1.5 asserts that
the composition ( 11.3) is non-zero and hence an epimorphism.
Let us show ( 11.2) (b). The outgoing arrows from s are
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 87
• s
|ax,it |
− − − − →t for s<t<s +<t + ≤r + 1.
• s − →s− if s− > 0.
Hence we have
◦
t;bt,s<0
M(t, 0)◦−bt,s ≃ M(s−, 0) ◦
(
◦
y∈Is
M((s+)−(y), 0)◦−ax,y
)
.(11.4)
Lemma 11.2.4. There exists an epimorphism (up to a grading )
Ω : M(s, 0) ◦ M(s+,s ) ◦A ։ ◦t;bt,s<0M(t, 0)◦−bt,s.
Proof. By the dual of Theorem 10.3.1 and the T -system ( 10.7) with i =is, u =us+−1
and v =us−1, we have morphisms
M(s, 0) ֌ M(s−, 0) ◦ M(s,s −),
M(s,s −) ◦ M(s+,s ) ։ ◦y∈I\{x}M((s+)−(y),s −(y))◦−ax,y
≃ ◦y∈IsM((s+)−(y),s −(y))◦−ax,y.
Here the last isomorphism follows from the fact that ( s+)−(y) = s−(y) for any y ⁄∈
{x} ∪Is = {ik |s ≤k <s+}.
Thus we have a sequence of morphisms
M(s, 0) ◦ M(s+,s ) ◦A /d47/d47ϕ1 /d47/d47M(s−, 0) ◦ M(s,s −) ◦ M(s+,s ) ◦A
ϕ2 /d47/d47/d47/d47M(s−, 0) ◦
(
◦y∈IsM((s+)−(y),s −(y))◦−ax,y
)
◦A.
By Lemma 3.1.5 (i), the composition ϕ :=ϕ2 ◦ϕ1 is non-zero.
Since A = ◦y∈IsM(s−(y), 0)◦−ax,y, Theorem 10.3.1 gives the morphisms
M(s, 0) ◦ M(s+,s ) ◦A
ϕ /d47/d47M(s−, 0) ◦
(
◦y∈IsM((s+)−(y),s −(y))◦−ax,y
)
◦A
φ /d47/d47/d47/d47M(s−, 0) ◦
(
◦y∈IsM((s+)−(y), 0)◦−ax,y
)
≃ ◦t;bt,s<0M(t, 0)◦−bt,s.
Here we have used Lemma 3.2.22 to obtain the morphism φ. Note that the module
◦y∈IsM((s+)−(y),s −(y))◦−ax,y is simple. By applying Lemma 3.1.5 once again, φ ◦ϕ is
non-zero, and hence it is an epimorphism. □
Lemma 11.2.5. We have d(X, M(s, 0)) = 1 .
Proof. SinceA and M(s, 0) commute and d
(
M(s+,s ), M(s, 0)
)
= 1 by Proposition 10.3.3,
we have
d
(
X, M(s, 0)
)
≤ d
(
M(s+,s ), M(s, 0)
)
+ d
(
A, M(s, 0)
)
≤ 1
by Proposition 3.2.10 and Lemma 3.2.3. If X and M(s, 0) commute, then ( 11.2) (a)
would imply that ch
(
◦t; bt,s>0M(t, 0)◦bt,s
)
belongs to K(R-gmod) ch(M(s, 0)). It con-
tradicts the result in [ 10] that all the ch( M(k, 0))’s are prime at q = 1. □
88 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Proposition 11.2.6. The map Ω factors through M(s, 0) ◦X; that is,
M(s, 0) ◦ M(s+,s ) ◦A
τ
/d42/d42/d42/d42❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯
Ω /d47/d47/d47/d47◦t;bt,s<0M(t, 0)◦−bt,s.
M(s, 0) ◦X
Ω
/d52/d52/d52/d52✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐
Hereτ is the canonical surjection.
Proof. We have 1 = d
(
M(s, 0), M(s+,s ) ∇A
)
by Lemma 11.2.5, and
d
(
M(s, 0), M(s+,s )
)
+ d
(
M(s, 0),A
)
= 1
by Proposition 10.3.3 withx =us+−1, i=is. Hence M(s, 0) ◦ M(s+,s ) ◦A has a simple
head by Proposition 3.2.16 (iii). □
End of the proof of Theorem 11.2.2. By the above arguments, we have proved the ex-
istence of X which satisﬁes ( 11.2). By Proposition 3.2.17 and ( 11.2) (c), M(s, 0) ◦X
has composition length 2. Moreover, it has a simple socle and simple hea d. On the
other hand, taking the dual of ( 11.2) (a), we obtain a monomorphism
⨀
t;bt,s>0
M(t, 0)⊙bt,s ֌ M(s, 0) ◦X
in R-mod. Together with ( 11.2) (b), there exists a short exact sequence in R-gmod:
0 →qc ⨀
t;bt,s>0
M(t, 0)⊙bt,s →q
~Λ( M(s,0),X)M(s, 0) ◦X → ⨀
t;bt,s<0
M(t, 0)⊙(−bt,s) → 0
for some c ∈ Z. By Lemma 3.2.18 c must be equal to 1.
It remains to prove that X commutes with M(k, 0) (k ⁄=s). For any k ∈J, we have
Λ( M(k, 0),X ) = Λ( M(k, 0), M(s, 0) ∇X) − Λ( M(k, 0), M(s, 0))
=
∑
t;bt,s<0
Λ( M(k, 0), M(t, 0))(−bt,s) − Λ( M(k, 0), M(s, 0))
and
Λ(X, M(k, 0)) = Λ( X ∇ M(s, 0), M(k, 0)) − Λ( M(s, 0), M(k, 0))
=
∑
t;bt,s>0
Λ( M(t, 0), M(k, 0))bt,s − Λ( M(s, 0), M(k, 0)).
Hence we have
2 d(M(k, 0),X ) = −2 d(M(k, 0), M(s, 0)) −
∑
t;bt,s<0
Λ( M(k, 0), M(t, 0))bt,s
−
∑
t;bt,s>0
Λ( M(k, 0), M(t, 0))bt,s
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 89
= −
∑
1≤t≤r
Λ( M(k, 0), M(t, 0))bt,s
= 2δk,s,
We conclude that X commutes with M(k, 0) if k ⁄=s. Thus we complete the proof of
Theorem 11.2.2. □
As a corollary, we prove the following conjecture on the cluster mon omials.
Theorem 11.2.7. ([11, Conjecture 12.9] , [23, Conjecture 1.1(2)] ) Every cluster vari-
able in Aq(n(w)) is a member of the upper global basis up to a power of q1/2.
Theorem 11.2.2 also implies [ 11, Conjecture 12.7] in the reﬁned form as follows:
Corollary 11.2.8. Z[q±1/2] ⊗Z[q±1]Aq(n(w))Z[q±1] has a quantum cluster algebra struc-
ture associated with the initial quantum seed [S ] = ( {q−(di,di)/4D(i, 0)}1≤i≤r,L, ~B); i.e.,
Z[q±1/2] ⊗
Z[q±1]
Aq(n(w))Z[q±1] ≃ Aq1/2([S ]).
