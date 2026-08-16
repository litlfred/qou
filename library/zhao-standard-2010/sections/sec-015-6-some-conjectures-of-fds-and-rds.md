---
doc_id: zhao-standard-2010
doc_title: "Documenta Math. 1 Standard Relations of Multiple Polylogarithm V alues at Roots of Unity Dedicated to Prof. Keqin Feng on his 70th birthday Jianqiang Zhao"
section_id: sec-015-6-some-conjectures-of-fds-and-rds
section_title: "Some conjectures of FDS and RDS"
section_number: 6
pages: 16-17
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Documenta Math. 1 Standard Relations of Multiple Polylogarithm Values at Roots of Unity Dedicated to Prof. Keqin Feng on his 70th birthday Jianqiang Zhao — Let N be a positive integer."
---
Fix a level N . Let R be a commutative Q-algebra with 1 and a homomorphism
ZR : A0 − →R such that the ﬁnite double shuﬄe (FDS) property holds:
ZR(ω1xω2) = ZR(ω1 ∗ ω2) = ZR(ω1)ZR(ω2).
We then extend ZR to Zx
R and Z ∗
R as before. Deﬁne an R-module automor-
phism ρR of R[T ] by
ρR(eT u) = AR(u)eT u
where
AR(u) = exp
( ∞∑
n=2
(−1)n
n ZR(an−1b0)un
)
∈ R[ [u] ].
If a map ZR : A0 − →R satisﬁes the FDS and ( Zx
R − ρR ◦ Z ∗
R)(ω) = 0 for all
ω ∈ A1 then we say that ZR has the regularized double shuﬄe (RDS) property.
Let RRDS be the universal algebra (together with a map ZRDS : A0 − →RRDS )
such that for every Q-algebra R and a map ZR : A0 − →R satisfying RDS there
always exists a map ϕR to make the following diagram commutative:
A0
ZR
/d35/d35/d70/d70/d70/d70/d70/d70/d70/d70/d70
ZRDS /d47/d47RRDS
ϕR
/d15/d15
R
When N = 2 computation by Bl¨ umlein, Broadhurst and Vermaseren [5] shows
that the ﬁnite distribution relations and the regularized d istribution relations
(18) contribute non-trivially when the weight w = 8 and w = 11, respectively.
When N = 3 computation shows that the lifted relations contribute n on-
trivially when the weight w = 4 (see §5) and w = 5: we can only get d(5, 3) ≤ 33
instead of the conjecturally correct dimension 32 without u sing the lifted re-
lations. Note that in this case there are 612 FDS of weight ﬁve , 191 RDS of
weight ﬁve, 8 FDT and 7 RDT.
One may use the fact that ZR is an algebra homomorphism to produce lifted
ﬁnite double shuﬄe and lifted regularized double shuﬄe relations as follows: for
all ω1 ∈ A1, ω0, ω′
0, ω′′
0 ∈ A0 with lg(ω1) + lg(ω0) = lg( ω0) + lg(ω′
0) + lg(ω′′
0 ) = w
Zx
R (ω1xω0)−ρR ◦Z ∗
R(ω1)Zx
R (ω0) = 0 , Z R
(
(ω0 ∗ω′
0)∗ω′′
0 −(ω0xω′
0)∗ω′′
0
)
= 0.
In general, one can deﬁne the universal objects ZSR and RSR corresponding
to the standard relations similar to ZRDS and RRDS such that for every Q-
algebra R and a map ZR : A0 − →R satisfying the standard relations there
always exists a map ϕR to make the following diagram commutative:
A0
ZR
/d34/d34/d69/d69/d69/d69/d69/d69/d69/d69
ZSR /d47/d47
RSR
ϕR
/d15/d15
R
(20)
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 17
Recall that one has the evaluation map Z : A0 − → C by Prop. 2.8 which
extends (5).
Conjecture 6.1. Let (R, ZR) = ( R, Z) if N = 1 , and (R, ZR) = ( C, Z) if
N = 2 , 3 or N = pn with prime p ≥ 5. If N = 1 (resp. N = 2 ) then the map
ϕR is injective, namely, the algebra of MPVs of level one or two i s isomorphic
to RRDS (resp. RSR). If N = 3 or N = pn (p ≥ 5) then the map ϕC is injective
so the algebra of MPVs of level N is isomorphic to RSR.
The above conjecture generalizes [24, Conjecture 1]. It mea ns that all the
linear relations among MPVs can be produced by RDS when N = 1 or 2, and
by the standard ones when N = 3 or pn with prime p ≥ 5. When N = p ≥ 5,
p a prime, this is proved in Thm. 8.6 under the assumption of a va riant of
Grothendieck’s period conjecture.
Computation in many cases such as those listed in Remark 8.2 a nd Conjec-
ture 8.5 show that MPVs must satisfy some other relations apa rt from the
standard ones when N has at least two distinct prime factors, so a naive gener-
alization of Conjecture 6.1 to all levels does not exist at pr esent. However, when
N = 4 one can show that octahedral symmetry of P1 − ({0, ∞} ∪ µ 4) provide
all the non-standard relations under the standard assumpti on (see Thm. 9.1).
But since we only have numerical evidence in weight three and weight four it
may be a little premature to form a conjecture for level four.
