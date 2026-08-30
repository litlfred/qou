---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-017-43-link-with-the-representation-theory-of-the-in
section_title: "Link with the representation theory of the infinite symmetric group"
section_number: 4.3
pages: 16-17
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
ﬁrst order asymptotics could alternatively have been obtai ned by using general results coming from the
representation theory of the inﬁnite symmetric group S∞, see in particular [ KV81, Ker03, KOV04].
However, it seems impossible to understand the ﬂuctuations with this approach.
Recall that the Thoma simplex
Ω =
{
(
(αi)i≥1, (βi)i≥1
)⏐
⏐ α1 ≥ α2 ≥ · · · ≥ 0, β 1 ≥ β2 ≥ · · · ≥ 0, γ = 1 −
∞∑
i=1
(αi + βi) ≥ 0
}
parametrizes the normalized irreducible characters of S∞ ([
Tho64]). Besides, to each point ω ∈ Ω , one
can associate a system (M ω
n )n∈ /C6
of probability measures on the sets Yn of Young diagrams:
M ω
n (λ) = (dim λ) sλ(ω),
where sλ(ω) is the generalized Schur function deﬁned by the following sp ecialization of the algebra of
symmetric functions:
p1(ω) = 1 ; pk≥2(ω) = pk(α − (−β)) =
∑
i≥1
(αi)k + (−1)k−1 ∑
i≥1
(βi)k.
This system is called coherent because it fulﬁlls the relati on:
∀n, ∀λ ∈ Yn, M ω
n (λ) =
∑
λրΛ
dim λ
dim Λ M ω
n+1(Λ) .
ASYMPTOTICS OF q-PLANCHEREL MEASURES 17
Moreover, one can describe all coherent systems (M m
n )n∈ /C6
of probability measures on the sets Yn: given
a probability measure m ∈ M (Ω) , let us deﬁne:
M m
n (λ) =
∫
Ω
M ω
n (λ) dm(ω) =
∫
Ω
(dim λ) sλ(ω) dm(ω).
This system is coherent and the correspondence is one-to-on e. In other terms Ω is the Martin boundary
of the Young graph ([ KOO98]). The set of probability measures M (Ω) is also in correspondence with
normalized (but non necessarily irreducible) characters o f S∞.
A deep result due to Kerov and Vershik ensures that the Thoma s implex is also in some sense the
“geometric boundary” of the Young graph. More precisely, le t us restate here Theorem 9.7.3 of [ KOV04]
(we refer also to [ KV81]). To each Young diagram λ ∈ Yn, we associate a point ωn(λ) of the Thoma
simplex by scaling its Frobenius coordinates:
ωn(λ) =
(a∗
1(λ)
n , . . . , a∗
d(λ)
n , 0, . . .; b∗
1(λ)
n , . . . , b∗
d(λ)
n , 0, . . .
)
.
We endow Ω with the compact topology of simple convergence of coordina tes.
Theorem 15. Let m be a probability measure on Ω ; we denote by (M m
n )n∈ /C6
the associated coherent
system of measures. The push-forward (ωn)⋆M m
n converges in law towards m in M (Ω) .
That said, the q-Plancherel measures (Mn,q)n∈ /C6
form the coherent system associated to the Dirac
mass at the point
ωq =
(
(1 − q), (1 − q)q, (1 − q)q2, . . .; 0, 0, . . .
)
.
Indeed, for any partition λ, the generic degree Dλ(q) can be written as Dλ(q) = {n!}q sλ(ωq), see [ Mac95,
Chapter 1,§3, examples 1-5]. So, the scaled Frobenius coord inates under q-Plancherel measures should
converge towards the vector (1 − q, (1 − q)q, (1 − q)q2, . . .; 0, 0, . . .), which is exactly our Theorem 1 and
Remark 3.
