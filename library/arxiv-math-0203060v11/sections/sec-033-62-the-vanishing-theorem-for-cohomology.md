---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-033-62-the-vanishing-theorem-for-cohomology
section_title: "The vanishing theorem for cohomology"
section_number: 6.2
pages: 25-27
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
dimensional semisimple (and hence, cosemisimple) weak Hopf algebra.
Lemma 6.2. Suppose that A is indecomposable. Let qi be a primitive idempotent
in Z(At) and let χ := χi be the corresponding canonical left integral in A∗from
Proposition 4.9. Then u = 1(1)χ(1(2)) is an invertible scalar.
Proof. Since χ is a left integral in A∗, we have
(32)
u = 1(1)χ(1(2)) = S(1(1))χ(1(2)) = S(u) ∈As ∩At.
Next, the following identities hold in every weak Hopf algebra A:
∆(1)(h ⊗1) = (id ⊗εt)∆(h),
(h ⊗1)∆(1) = (id ⊗εop
t )∆(h),
h ∈A,
where εop
t
is the target counital map in Aop.
Using Proposition 4.9 we compute for all h ∈A :
1(1)hχ(1(2))
=
h(1)χ(εt(h(2))) = h(1)χ(h(2)S(h(3)))
=
h(1)χ(S−1(h(3))h(2)) = h(1)χ(εop
t (h(2)))
=
h1(1)χ(1(2)),
hence, u ∈As ∩At ∩Z(A) = k1A.
For any primitive central idempotent qj in At we have
χ(qj) = Tr(S2|qjAS(qi)) = dim(Rep(A))n2
i n2
j̸ = 0,
where n2
i = dimk(qiAt) and n2
j = dimk(qjAt). Therefore, χ|At̸ = 0 and u̸ = 0.
□
Theorem 6.3. Let C be the complex associated to A, B as above. Then H0(A, B) =
At ∩As ∩Z(A) and Hn(A, B) = 0 for all n ≥1.
26
PAVEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Proof. It suﬃces to prove this theorem in the case when A is indecomposable. In
this case we have H0(A, B) = Ker(δ0) = At∩As∩Z(A) = k. Let f ∈Cn(A, B), n ≥
1 be a cycle, i.e., δn(f) = 0. We will show by a direct computation that
(33)
˜f = (idn−1 ⊗χ)(f)
belongs to Cn−1(A, B) and that f is a scalar multiple of the diﬀerential δn−1( ˜f).
We will write f = f (1) ⊗· · · ⊗f (n), where a sum of some set of tensors is
understood. We have :
Ad(1) ˜f =
=
1(1)f (1)S(1(2n−2)) ⊗· · · ⊗1(n−1)f (n−1)S(1(n))χ(f (n))
=
∆n−1(1(1)1′
(1))(f (1) ⊗· · · ⊗f (n−1))∆n−1(S(1(2)1′
(4)))χ(1′
(2)f (n)S(1′
(3)))
=
∆n−1(1′
(1))(f (1) ⊗· · · ⊗f (n−1))∆n−1(S(1′
(4)))χ(1′
(2)f (n)S(1′
(3))) = ˜f,
where 1′ stands for a second copy of 1 and we use that in any regular weak Hopf
algebra one has (1(1) ⊗1 ⊗1 ⊗1(2))∆4(1) = ∆4(1). Next, we have for all h ∈B :
Ad(h) ˜f =
=
h(1)f (1)S(h(2n−2)) ⊗· · · ⊗h(n−1)f (n−1)S(h(n))χ(f (n))
=
h(1)f (1)S(h(2n−1)) ⊗· · · ⊗h(n−1))f (n−1)εs(h(n))S(h(n+1))χ(f (n))
=
h(1)f (1)S(h(2n−1)) ⊗· · · ⊗h(n−1)f (n−1)S(h(n+1))χ(f (n)S(εs(h(n))))
=
h(1)f (1)S(h(2n)) ⊗· · · ⊗h(n−1)f (n−1)S(h(n+2))χ(h(n)f (n)S(h(n+1)))
=
(idn−1 ⊗χ)(Ad(h)f) = (idn−1 ⊗χ)(Ad(εt(h))f) = Ad(εt(h)) ˜f.
Here we used that
(34)
f = (1 ⊗· · · ⊗1 ⊗∆(1))f
for all f ∈Cn(A, B), the weak Hopf algebra identities
x(1)εs(x(2)) = x
and
(y ⊗1)∆(1) = (1 ⊗S−1(y))∆(1)
for all x ∈A and y ∈As (cf. [NV]), and Proposition 4.9.
Hence, ˜f ∈Cn−1(A, B). Next, since (idn ⊗χ)(δn(f)) = 0, we get
0
=
(idn ⊗χ)Ad(1){1 ⊗f (1) ⊗· · · ⊗f (n) −∆(f (1)) ⊗· · · ⊗f (n) +
· · · + (−1)nf (1) ⊗· · · ⊗∆(f (n)) + (−1)n+1f (1) ⊗· · · ⊗f (n) ⊗1}
=
Ad(1){1 ⊗f (1) ⊗· · · ⊗f (n−1)χ(f (n)) −∆(f (1)) ⊗· · · ⊗f (n−1)χ(f (n)) +
· · · + (−1)nf (1) ⊗· · · ⊗(id ⊗χ)∆(f (n))} + (−1)n+1f∆n(1(1))χ(1(2)).
Let u = 1(1)χ(1(2)). Then
f ∆n(u)
=
(−1)nδn−1( ˜f)
+Ad(1){f (1) ⊗· · · ⊗(id ⊗χ)∆(f (n)) −f (1) ⊗· · · ⊗f (n−1) ⊗χ(f (n))1}.
Let us show that
(35)
Ad(1){(idn−1 ⊗χ)(f) ⊗1 −(idn ⊗χ)(idn−1 ⊗∆)(f)} = 0
ON FUSION CATEGORIES
27
for all f ∈Cn(A, B). Observe that both sides of (35) belong to Cn+1(A, B). We
compute :
Ad(1){f (1) ⊗· · · ⊗f (n−1) ⊗f (n)
(1)χ(f (n)
(2))} =
=
f (1) ⊗· · · ⊗f (n−1) ⊗S(1(1))χ(1(2)f (n))
=
f (1) ⊗· · · ⊗1′
(1)f (n−1) ⊗1′
(2)S(1(1))χ(1(2)f (n))
=
f (1) ⊗· · · ⊗1′
(1)1(1)f (n−1) ⊗1′
(2)χ(1(2)f (n))
=
f (1) ⊗· · · ⊗1(1)f (n−1) ⊗1(2)χ(f (n)
=
Ad(1){f (1) ⊗· · · ⊗f (n−1) ⊗χ(f (n))1}.
