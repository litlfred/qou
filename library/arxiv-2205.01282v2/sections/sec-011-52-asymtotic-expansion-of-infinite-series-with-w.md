---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI"
section_id: sec-011-52-asymtotic-expansion-of-infinite-series-with-w
section_title: "Asymtotic expansion of infinite series with weighted Gauss sums"
section_number: 5.2
pages: 13-15
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed"
---
we study a family of infinite series F (f;t) with weighted Gauss sums, which involves both WRT
invariants and homological blocks. We start with the following asymptotic formula following from
Proposition 5.4. In the following statement, we use notations ε,S,Q and so on, which we prepared in
Sections 2 and 4.
Corollary 5.7. For e∈{± 1}V≥3 and a C∞ function f : RV≥2→ C of rapid decay as xv→∞ for
eachv∈V≥2, let
Fe(f;t) :=
X
α∈S
ε(α)
X
n∈Z
V≥3
≥0
e
1
kQ(e(n +α))

P (n)f(t(n +α))
be a series for a variable t∈ R>0. Then, it holds that
Fe(f;t)∼
X
n∈ZV≥2
ce,nf (n)(0)t
P
v∈V≥2nv
14 Y. MURAKAMI
as t→ +0, where we define
ce,n =
X
α∈S
ε(α)

Y
v∈V2
αnv
v
nv!

 X
m∈Z
V≥3
≥0
pm

 Y
v∈V≥3
kmv+nv

 X
λ∈{0,...,k−1}V≥3
e
1
kQ(e(λ +α))

Bm,n(α,λ )
for n∈ ZV≥2.
We define two C∞ function of rapid decay f1,f 2 : RV≥2 → C as f1(x) := exp(−P
v∈V≥2xv) and
f2 := exp(−Q(x)) respectively. Then, WRT invariants and limit values of homological blocks can
be written as limit values of F (f1;t) and F (f2;t) as t→ 0 shown later in Propositions 5.8 and 6.3,
respectively.
Here, we need to prove that F (f;t) has a limit as t→ 0, that is, cn vanishes forn∈ ZV≥3 with non-
positive components. Such a result is called “a vanishing result of weighted Gauss sums” in [MM22],
and it is the most important part in a proof of the conjecture of Gukov–Pei–Putrov–Vafa [GPPV20,
Conjecture 2.1, Equation (A.28)]. In the previous works [BMM20, MM22], it is proved by direct
calculations ([BMM20, Theorem 4.1],[MM22, Proposition 4.2]). On the other hand, our proof is based
on the above asymptotic expansion in Corollary 5.7. Since cn is independent of f in this asymptotic
expansion, it suffices to consider not for any f, but for f1. Since F (f1;t) is a rational function shown
later in Lemma 5.10, vanishings results of cn is equivalent to holomorphy of F (f1;t), which is proved
in Section 6.
The homological block bZΓ(ζke−t2
) can be written in term of F (f2;t) as follows.
Proposition 5.8. It holds that

(−1)|V1|q−(P
v∈V (wv+3)+P
i∈V1 1/wi)/4bZΓ(q)


q=ζke−t2 =
X
e∈{±1}V≥3

 Y
v∈V≥3
edeg(v)+|v|
v

Fe(f2;t).
This proposition follows from Proposition 4.2 for C(n) = e (Q(e(n +α))/k).
In the last of this subsection, we prove thatF (f1;t) is a rational function related to WRT invariants.
To begin with, we replace quadratic formsQ(n+α) as linear forms in the indices ofζk in the definition
of F (f;t).
Lemma 5.9. Fore∈{± 1}V≥3 and a C∞ function f : RV≥2→ C of rapid decay as xv→∞ for each
v∈V≥2, it holds that
Fe(f;t) = e (|V≥2|/8)
√
2k|V≥2|Q
i∈V1
p
|wi|
X
µ∈ZV≥2/2kS

ZV≥2

e

− 1
4k
tµS−1µ

X
α∈S
ε(α)
X
n∈Z
V≥3
≥0
e
1
k
tµe(n +α)

P (n)f(t(n +α)).
Proof. Let
G(2kS) :=
X
µ∈ZV≥2/2kS

ZV≥2

e

− 1
4k
tµS−1µ

.
Then, we have G(2kS) =
√
2ke (−1/8)
|V≥2|√
detS by Proposition 3.3. Here we remark det S =Q
i∈V1|wi| by Proposition 2.2 (ii). Then, we can write
G(2kS)Fe(f;t)
=
X
µ∈ZV≥2/2kS

ZV≥2

X
α∈S
ε(α)
X
n∈Z
V≥3
≥0
e
1
k

Q(e(n +α))− 1
4
tµS−1µ

P (n)f(t(n +α)).
By replacing µ byµ− 2Se(n +α), we obtain the claim. □
By this lemma, we obtain the following representation.
WRT INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES 15
Lemma 5.10. Fore∈{± 1}V≥3,
Fe(f1;t) =edeg(v)+|v|
v
e (|V≥2|/8)
(2k)|V≥2|Q
i∈V1
p
|wi|
X
µ∈ZV≥2/2kS

ZV≥2

e

− 1
4k
tµS−1µ
 Y
v∈V≥2
Gv

ζµv
2kMve−evt/2Mv

.
In particular, Fe(f1;t) is a meromorphic function.
Proof. By Lemma 5.9, we have
G(2kS)Fe(f1;t) =
X
µ∈ZV≥2/2kS

ZV≥2

e

− 1
4k
tµS−1µ

X
α∈S
ε(α)
X
n∈Z
V≥3
≥0
e
1
k
tµe(n +α)

P (n) exp

−
X
v∈V≥3
tv(nv +αv)

.
By applying Lemma 2.11 for this, we have
G(2kS)Fe(f1;t) =
X
µ∈ZV≥2/2kS

ZV≥2

e

− 1
4k
tµS−1µ
 Y
v∈V≥2
Gv

ζevµv
2kMve−t/2Mv

.
By Remark 2.8, we obtain the claim. □
