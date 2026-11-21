---
doc_id: arxiv-hep-th-9408099v1
doc_title: "Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD"
section_id: sec-019-171-the-meaning-of-the-residues
section_title: "The Meaning Of The Residues"
section_number: 17.1
pages: 71-73
source_pdf: 9408099v1.pdf
source_sha256: b534faddd2e3aa71
toc_source: inferred
doc_brief: "Seiberg–Witten, Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD (1994) — exact metric on the moduli space of quantum vacua and exact stable-state spectrum for SU(2) with…"
---
The Nf = 4 theory is controlled by a curve y2 = F(x, u, mi, τ) and a diﬀerential form
λ obeying
dλ
du = ω + exact form in x
(17.2)
with
ω =
√
2
8π
dx
y .
(17.3)
For N = 4 the structure is the same, except that 8π is replaced by 4π. F should be such
that the residues of λ are linear in the quark bare masses. This is a severe restriction
on F; we will see that it determines F uniquely (up to the usual changes of variables)
independently of most of the arguments that we have used up to this point.
As a preliminary, let us write (17.2) in a more symmetrical form. If λ = dx a(x, u),
then (17.2) means
√
2
8π
dx
y = dx ∂a
∂u + dx ∂
∂xf(x, u);
(17.4)
the arbitrary total x-derivative dx ∂f/∂x is allowed because it does not contribute to
the periods. (17.4) can be understood much better if written symmetrically in x and u.
Henceforth, instead of using a one-form ω = (
√
2/8π) · dx/y, we will use a two-form
ω =
√
2
8π
dx du
y
.
(17.5)
Similarly, we combine the functions a, f appearing in (17.4) into a one-form λ =
−a(x, u)dx + f(x, u)du. The change in notation for ω and λ should cause no confusion.
Then equation (17.4) can be more elegantly written
ω = dλ.
(17.6)
The meaning of the problem of ﬁnding λ can now be stated. Let X be the (noncom-
pact) complex surface deﬁned by the equation y2 = F(x, u) (we suppress the parameters
mi and τ). Being closed, ω deﬁnes an element [ω] ∈H2(X, C). A smooth diﬀerential
λ obeying (17.6) exists if and only if [ω] = 0. Moreover, by standard theorems, in the
absence of restrictions on the growth of λ at inﬁnity, if λ exists it can be chosen to be
holomorphic and of type (1, 0).
70
If on the other hand [ω]̸ = 0, then (17.6) has no smooth, much less holomorphic,
solution. However, X has the property that if one throws away a suﬃcient number of
complex curves Ca, then X′ = X −∪aCa has H2(X′, C) = 0. (The necessary Ca are
explicitly described later.) So if we restrict to X′, the cohomology class of ω vanishes
and λ exists. λ may however have poles on the Ca, perhaps with residues, which we call
ResCa(λ).12 If λ does have residues, then dλ contains delta functions, and if one works on
X instead of X′, one really has not (17.6) but
ω = dλ −2πi
X
a
ResCa(λ) · [Ca]
(17.7)
where [Ca] (which represents the cohomology class known as the Poincar´e dual of Ca) is a
delta function supported on Ca.
In cohomology, (17.7) simply means
[ω] = −2πi
X
a
ResCa(λ) · [Ca].
(17.8)
Thus, if we pick the Ca so that the [Ca] are a basis of H2(X, C), then the residues ResCa(λ)
are simply the coeﬃcients of the expansion of [ω] in terms of the [Ca]. To ﬁnd the residues
we need not actually ﬁnd λ; it suﬃces to understand the cohomology class of ω by any
method that may be available.
For instance, if X were compact, we could proceed as follows. First compute the
intersection matrix
Mab = #(Ca · Cb)
(17.9)
(that is, the number of intersection points of Ca and Cb, after perhaps perturbing the Ca
so that they intersect generically). This is an invertible matrix. Second, calculate the
periods
ca =
Z
Ca
ω.
(17.10)
Then
[ω] =
X
a,b
caM −1
ab[Cb].
(17.11)
12 The residues of λ along Ca are constants, since dResCa(λ) = ResCadλ = ResCaω = 0.
71
Comparing to (17.8), we get
ResCa(λ) = −1
2πi
X
b
M −1
ab cb.
(17.12)
We will eventually follow that strategy after compactifying X and modifying ω so as
to have no pole at inﬁnity. With this in view, we will somewhat loosely and prematurely
call the cb the “periods” of ω.
