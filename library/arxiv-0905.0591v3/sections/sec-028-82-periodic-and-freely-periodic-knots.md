---
doc_id: arxiv-0905.0591v3
doc_title: "A SUR VEY OF TWISTED ALEXANDER POL YNOMIALS"
section_id: sec-028-82-periodic-and-freely-periodic-knots
section_title: "Periodic and freely periodic knots"
section_number: 8.2
pages: 26-27
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
q, if there exists a smooth transformation of S3 of order q which leaves K invariant and
such that the ﬁxed point set is a circle A disjoint from K. Note that A ⊂S3 is the trivial
knot by the Smith conjecture. We refer to [Ka96, Section 10.1 ] for more details on periodic
knots.
Now assume that K ⊂ S3 is a periodic knot of period q with A the ﬁxed point set of
f : S3 →S3. Note that S3/f is diﬀeomorphic to S3. We denote by π the projection map
S3 →S3/f =S3 and we write K =π(K),A =π(A).
The following two theorems of Hillman, Livingston and Naik [ HLN06, Theorems 3 and 4]
generalize results of Trotter [Tr61] and Murasugi [Mu71].
Theorem 8.2. Let K be a periodic knot of period q. Let π,A,
A and K as above. Let
γ : π1(S3 \νK) → GL(n,R ) a representation with R = Z or R = Q. Write γ = γ ◦π∗.
Then there exists a polynomial F (t,s ) ∈R[t±1,s ±1] such that
∆ γ
K(t) .= ∆
γ
K(t)
q−1∏
k=1
F (t,e 2πik/q ).
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 27
In the untwisted case the polynomial F (t,s ) is just the Alexander polynomial of the
ordered link K ∪A ⊂S3. We refer to [HLN06, Section 6] for more information on F (t,s ).
The following theorem gives an often stronger condition whe n the period is a prime power.
Theorem 8.3. Let K be a periodic knot of period q =pr where p is a prime. Let π,A, A
and K as above. Let γ :π1(S3 \νK) → GL(n, Zp) be a representation. Write γ =γ ◦π∗.
If ∆ γ
K (t) ⁄= 0, then
∆ γ
K(t) ·
(
∆ γ
K,0(t)
) q−1 .= ∆
γ
K(t)q
(
det
(
idn −γ(A)tlk(K,A)
)) q−1
∈ Zp[t±1],
where we view A as an element in π1(S3 \νK ).
(Note that Elliot [El08] gave an alternative proof for this t heorem.) These theorems are
applied in [HLN06, Section 10] to give obstructions on the pe riodicity of the Kinoshita–
Terasaka knot and the Conway knot. Note that both knots have t rivial Alexander polyno-
mial, in particular Murasugi’s obstructions are satisﬁed t rivially.
A knot K ⊂ S3 is called freely periodic of period q if there exists a free transformation
f of S3 of order q which leaves K invariant. We refer to [Ka96, Section 10.2] for more
information on freely periodic knots. Given such a freely pe riodic knot K we denote by π
the projection map S3 → Σ :=S3/f and we write K =π(K).
The following theorem is [HLN06, Theorem 5]; the untwisted c ase was ﬁrst proved by
Hartley [Hat81].
Theorem 8.4. Let K be a freely periodic knot of period q. Let π, Σ and
K as above. Let
γ :π1(Σ \K) → GL(k,R ) be a representation with R a Noetherian UFD. Write γ =γ ◦π∗.
Then
∆ γ
K(tq) .=
q−1∏
k=0
∆
γ
K(e2πik/qt).
We refer to [HLN06, Section 11] for an application of this the orem to a case which could
not be settled with Hartley’s theorem.
