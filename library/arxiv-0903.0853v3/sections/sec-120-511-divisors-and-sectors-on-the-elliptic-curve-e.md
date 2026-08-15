---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-120-511-divisors-and-sectors-on-the-elliptic-curve-e
section_title: "Divisors and sectors on the elliptic curve E q = C∗/qZ. — The"
section_number: 5.1.1
pages: 73-75
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
projection p : C∗→ Eq and the discrete logarithmicq-spiral [λ;q] were deﬁned
in the general notations, section 1.3. In this chapter, we sh all usually shorten
1. To be more precise: note [ 42] can be seen as an abridged version of the present chapter.
It summarizes and completes [ 43], the departure point, which announces the ﬁrst part of
[59]. These ﬁrst works dealt with divisors supported at a single point, and [ 61] started the
extension to more general divisors (and more slopes).
68 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
the latter notation into [ λ] := [λ;q]. We call divisor a ﬁnite formal sum of
weighted suchq-spirals:
Λ =ν1[λ1] +··· +νm[λm], where νi∈ N∗ and [λi]⁄= [λj] if i⁄=j.
This can be identiﬁed with theeﬀective divisor∑ νi
[
λi
]
on Eq and, to simplify
notations, we shall also write ∑ νi[λi] that divisor on Eq. The support of Λ is
the union of the q-spirals [λ1],..., [λm]. We write:
|Λ| :=ν1 +··· +νm
the degree of Λ (an integer) and:
‖Λ‖ := (−1)|Λ |λν1
1 ··· λνm
m (mod qZ)
the weight of Λ, an element of Eq. It is equal, in additive notation, to∑ νip(−λi) evaluated in Eq.
For any two non zero complex numbers z and λ, we put:
dq(z, [λ]) := inf
ξ∈[λ]
⏐
⏐
⏐
⏐1− z
ξ
⏐
⏐
⏐
⏐.
This is a kind of “distance” from z to the q-spiral [λ]: one has dq(z, [λ]) = 0
if, and only if z∈ [λ].
Lemma 5.1.1 . — Let‖q‖1 := inf
n∈Z∗
|1−qn| and Mq := ‖q‖1
2+‖q‖1
. Let a∈ C be
such that |1−a|≤ Mq. Then:
dq(a; [1]) =|1−a|.
Proof. — This follows at once from the inequalities:
|1−aqn|≥| a| |1−qn|−| 1−a|≥ (1−Mq)‖q‖1−| 1−a| ≥|1−a|.
Forρ> 0, we put:
D([λ];ρ) :={z∈ C∗| dq(z, [λ])≤ρ},
Dc([λ];ρ) := C∗\D([λ];ρ),
so that D([λ]; 1) = C∗ and Dc([λ]; 1) =∅. From lemma 5.1.1, it follows that
for any ρ<M q:
D([λ];ρ) =
⋃
n∈Z
qnD(λ;|λ|ρ),
where D(λ;|λ|ρ) denotes the closed disk with center λ and radius|λ|ρ.
