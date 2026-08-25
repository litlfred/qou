---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-099-41-asymptotics-49
section_title: "ASYMPTOTICS 49"
section_number: 4.1
pages: 55-57
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
whence:
|f(z1)−f(z2)|≤ 2 +ρ
ρ MK|z1−z2|.
Last, let CK := max
(
M ′
K1, 2+ρ
ρ MK
)
; then, for all z1,z 2 ∈ K∪{ 0}, we
have:
|f(z1)−f(z2)|≤ CK|z1−z2|.
(ii) We deﬁne ρ, K1, CK as in (i). We set:
CK,n := sup
z∈K
⏐
⏐
⏐
⏐
⏐
⏐
f(z)−
n∑
p=0
f (p)(0)
p! zp
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐z−n−1⏐
⏐ , M ′
K1,n := sup
z∈K1
⏐
⏐
⏐f (n+1)(z)
⏐
⏐
⏐ .
The result is obviously true if f is a polynomial. Therefore, ﬁxing n∈ N it
suﬃces to prove the result when f =zn+1g, g∈ A (U∞).
As in (i) we shall consider separately the three cases (a), (b ), (c). If z2 = 0,
then the result merely comes from the following relation:
⏐
⏐
⏐
⏐
⏐
⏐
f(z1)−
n∑
p=0
f (p)(z2)
p! (z1−z2)p
⏐
⏐
⏐
⏐
⏐
⏐
=
⏐
⏐
⏐
⏐
⏐
⏐
f(z1)−
n∑
p=0
f (p)(0)
p! zp
1
⏐
⏐
⏐
⏐
⏐
⏐
≤CK,n|z1|n+1.
Next, if z2 ⁄= 0 and |z1−z2| ≤ρ|z2|, then the closed interval [ z1,z 2] is
contained in K1, so that:
⏐
⏐
⏐
⏐
⏐
⏐
f(z1)−
n∑
p=0
f (p)(z2)
p! (z1−z2)p
⏐
⏐
⏐
⏐
⏐
⏐
≤M ′
K1,n|z1−z2|n+1.
It remains to deal with the case (c), that is, when z2⁄= 0 and |z1−z2| >
ρ|z2|. If we set:
λK,n := sup
z∈K
p=0,...,n
⏐
⏐
⏐
⏐
⏐
g(p)(z)
p!
⏐
⏐
⏐
⏐
⏐ , µ K := sup
z∈K
|z|,
then, for any integer p∈ [0,n ], we ﬁnd:
⏐
⏐
⏐
⏐
⏐
f (p)(z2)
p!
⏐
⏐
⏐
⏐
⏐=
⏐
⏐
⏐
⏐
⏐
(zn+1g)(p)(z2)
p!
⏐
⏐
⏐
⏐
⏐≤λK,n
p∑
k=0
(n + 1
k
)
|z2|n+1−k≤ ˜λK,n|z2−z1|n+1−p,
where:
˜λK,n :=λK,n ρp−n−1
p∑
k=0
(n + 1
k
)
µp−k
K .
50 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
From this, it follows:
⏐
⏐
⏐
⏐
⏐
⏐
f(z1)−
n∑
p=0
f (p)(z2)
p! (z1−z2)p
⏐
⏐
⏐
⏐
⏐
⏐
≤
⏐
⏐zn+1
1 g(z1)
⏐
⏐+ (n + 1)˜λK,n |z2−z1|n+1
≤
((
1 + 1
ρ
) n+1
λK,n + (n + 1)˜λK,n
)
|z2−z1|n+1 .
To summarize, in the three cases cases we have:
⏐
⏐
⏐
⏐
⏐
⏐
f(z1)−
n∑
p=0
f (p)(z2)
p! (z1−z2)p
⏐
⏐
⏐
⏐
⏐
⏐
≤ CK,n|z1−z2|n+1,
where
CK,n := max
(
M ′
K1,n,
(
1 + 1
ρ
) n+1
λK,n + (n + 1)˜λK,n
)
.
(iii) The result follows immediately from (ii).
Before stating the next proposition, we ﬁrst recall Whitney conditions and
Whitney theorem [ 29, chap. I, §4], [ 28]. We give them here in the case
of dimension 2. Let f be a function of ( x,y ) with complex values, C∞ in
an open neighborhood U ′ of some compact subset K ′ of C. (We keep the
lettersU andK to denote respectively a Σ-invariant open subset of C and an
invariant strict subset ofU.) We shall use the following standard conventions;
for k := (k1,k 2)∈ N2, we set:
f (k) := ∂k1
∂xk1
∂k2
∂y k2
f·
We also write k! :=k1!k2!, (x,y )k :=xk1yk2,|k| :=k1 +k2, etc. We associate
to f the family (f (k))k∈N2 of its “Taylor ﬁelds” restricted to K ′.
We agree to identify theC∞ functionf onU ′⊃K ′ with theC∞ functiong
on V ′⊃K ′ if their associated families (f (k))k∈N2, (g(k))k∈N2 are equal. Such
a class of functions is called a C∞ function in the Whitney sense on K ′. We
writeC∞
W hitney(K ′) the space of C∞ functions (1) in the Whitney sense on K ′.
As is customary when dealing with germs, we sometimes write f the class of
f; likewise, we write ( f (k)) the family of restrictions to K ′ of the derivatives
1. They are not really functions, but it usually causes no pro blem; moreover, in our case,
they will be (according to the next proposition).
