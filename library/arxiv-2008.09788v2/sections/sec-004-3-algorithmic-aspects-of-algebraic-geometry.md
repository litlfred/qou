---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETR Y"
section_id: sec-004-3-algorithmic-aspects-of-algebraic-geometry
section_title: "Algorithmic aspects of algebraic geometry"
section_number: 3
pages: 23-25
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
The section contains two subsections: the ﬁrst one is devote d to noncommutative Finite
Gr¨ obner basis issues and the second one is devoted to algorithmic inclusion undecidability.
3.1. Finite Gr¨ obner basis algebras with unsolvable nilpotency problem and
zero divisors problem.
3.1.1. The sketch of construction. Let A be an algebra over a ﬁeld K.
The set of all words in the alphabet {a1, . . . , a N } is a semigroup. The main idea of
the construction is a realization of a universal Turing mach ine in this semigroup. We use
the universal Turing machine constructed by Marvin Minsky i n [66]. This machine has 7
states and 4-color tape. The machine can be completely deﬁne d by 28 instructions.
Note that 27 of them have a form
(i, j ) → (L, q (i, j ), p (i, j )) or ( i, j ) → (R, q (i, j ), p (i, j )),
where 0 ≤ i ≤ 6 is the current machine state, 0 ≤ j ≤ 3 is the current cell color, L or R
(left or right) is the direction of a head moving after execut ion of the current instruction,
q(i, j ) is the state after current instruction, p(i, j ) is the new color of the current cell.
Thus, the instruction (2 , 3) → (L, 3, 1) means the following: “If the color of the current
cell is 3 and the state is 2, then the cell changes the color to 1 , the head moves one cell to
the left, the machine changes the state to 3.
The last instruction is (4 , 3) → STOP. Hence, if the machine is in state 4 and the
current cell has color 3, then the machine halts.
Letters. By Qi, 0 ≤ i ≤ 6 denote the current state of the machine. By Pj, 0 ≤ j ≤ 3
denote the color of the current cell.
The action of the machine depends on the current state Qi and current cell color Pj.
Thus every pair Qi and Pj corresponds to one instruction of the machine.
The instructions moving the head to the left (right) are call ed left (right) ones. There-
fore there are left pairs (i, j ) for the left instructions, right pairs for the right ones and
instruction STOP for the pair (4 , 3).
All cells with nonzero color are said to be non-empty cells . We shall use letters a1,
a2, a3 for nonzero colors and letter a0 for color zero. Also, we use R for edges of colored
area. Hence, the word Rau1 au2 . . . a uk QiPjav1 av2 . . . a vl R presents a full state of Turing
machine.
We model head moving and cell painting using computations wi th powers of ai (cells)
and Pi and Qi (current cell and state of the machine’s head).
We use the universal Turing machine constructed by Minsky. T his machine is deﬁned
by the following instructions:
(0, 0) → (L, 4, 1) (0 , 1) → (L, 1, 3) (0 , 2) → (R, 0, 0) (0 , 3) → (R, 0, 1)
(1, 0) → (L, 1, 2) (1 , 1) → (L, 1, 3) (1 , 2) → (R, 0, 0) (1 , 3) → (L, 1, 3)
(2, 0) → (R, 2, 2) (2 , 1) → (R, 2, 1) (2 , 2) → (R, 2, 0) (2 , 3) → (L, 4, 1)
(3, 0) → (R, 3, 2) (3 , 1) → (R, 3, 1) (3 , 2) → (R, 3, 0) (3 , 3) → (L, 4, 0)
(4, 0) → (L, 5, 2) (4 , 1) → (L, 4, 1) (4 , 2) → (L, 4, 0) (4 , 3) → STOP
(5, 0) → (L, 5, 2) (5 , 1) → (L, 5, 1) (5 , 2) → (L, 6, 2) (5 , 3) → (R, 2, 1)
(6, 0) → (R, 0, 3) (6 , 1) → (R, 6, 3) (6 , 2) → (R, 6, 2) (6 , 3) → (R, 3, 1)
We use the following alphabet:
{t, a 0, . . . a 3, Q 0, . . . Q 6, P 0 . . . P 3, R }
24 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
For every pair except (4 , 3) the following functions are deﬁned: q(i, j ) is a new state,
p(i, j ) is a new color of the current cell (the head leaves it).
3.1.2. Deﬁning relations for the nilpotency question. Consider the following deﬁn-
ing relations:
tRal = Rtal; 0 ≤ l ≤ 3 ⟨3.1⟩
talR = alRt; 0 ≤ l ≤ 3 ⟨3.2⟩
takaj = aktaj; 0 ≤ k, j ≤ 3 ⟨3.3⟩
takQiPj = Qq(i,j )Pktap(i,j ); for left pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.4⟩
tRQiPj = RQq(i,j )P0tap(i,j ); for left pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.5⟩
talQiPjakan = alap(i,j )Qq(i,j )Pktan; for right pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.6⟩
talQiPj akR = alap(i,j )Qq(i,j )PkRt; for right pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.7⟩
tRQiPjakan = Rap(i,j )Qq(i,j )Pktan; for right pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.8⟩
tRQiPj akR = Rap(i,j )Qq(i,j )PkRt; for right pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.9⟩
talQiPjR = alap(i,j )Qq(i,j )P0Rt; for right pairs ( i, j ) and 0 ≤ l ≤ 3 ⟨3.10⟩
tRQiPj R = Rap(i,j )Qq(i,j )P0Rt; for right pairs ( i, j ) ⟨3.11⟩
Q4P3 = 0. ⟨3.12⟩
The relations ⟨3.1⟩ and ⟨3.3⟩ are used to move t from the left edge to the last letter al
standing before QiPj which represent the head of the machine. The relations ⟨3.4⟩–⟨3.11⟩
represent the computation process. The relation ⟨3.2⟩ is used to move t through the
ﬁnishing letter R.
Finally, the relation ⟨3.12⟩ halts the machine.
Let us call tRau1 au2 . . . a uk QiPj av1 av2 . . . a vl R the main word .
Theorem 3.1. Consider an algebra A presented by the deﬁning relations ⟨3.1⟩–⟨3.12⟩.
The word tRU QiPj V R is nilpotent in A if and only if machine M (i, j, U, V ) halts.
Actually we can prove that multiplication on the left by an el ement t leads to the
transition to the next state of the machine.
3.1.3. Deﬁning relations for a zero divisors question. We use the following alphabet:
Ψ = {t, s, a 0, . . . a 3, Q 0, . . . Q 6, P 0 . . . P 3, L, R }.
For every pair except (4 , 3) the following functions are deﬁned: q(i, j ) is a new state,
p(i, j ) is a new color of the current cell (the head leaves it).
Consider the following deﬁning relations:
tLak = Ltak; 0 ≤ k ≤ 3 ⟨3.13⟩
takal = aktal; 0 ≤ k, l ≤ 3 ⟨3.14⟩
sR = Rs; ⟨3.15⟩
sak = aks; 0 ≤ k ≤ 3 ⟨3.16⟩
takQiPj = Qq(i,j )Pkap(i,j )s; for left pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.17⟩
tLQiPj = LQq(i,j )P0ap(i,j )s; for left pairs ( i, j ) ⟨3.18⟩
talQiPjak = alap(i,j )Qq(i,j )Pks; for right pairs ( i, j ) and 0 ≤ k, l ≤ 3 ⟨3.19⟩
tLQiPj ak = Lap(i,j )Qq(i,j )Pks; for right pairs ( i, j ) and 0 ≤ k ≤ 3 ⟨3.20⟩
talQiPjR = alap(i,j )Qq(i,j )P0Rs; for right pairs ( i, j ) and 0 ≤ l ≤ 3 ⟨3.21⟩
tLQiPjR = Lap(i,j )Qq(i,j )P0Rs; for right pairs ( i, j ) ⟨3.22⟩
Q4P3 = 0; ⟨3.23⟩
SOME LOGICAL ASPECTS 25
The relations ⟨3.13⟩–⟨3.14⟩ are used to move t from the left edge to the letters Qi, Pj which
present the head of the machine. The relations ⟨3.15⟩–⟨3.16⟩ are used to move s from the
letter Qi, Pj to the right edge. The relations ⟨3.17⟩–⟨3.21⟩ represent the computation
process. Here we use relations of the form tU = V s.
Finally, the relation ⟨3.23⟩ halts the machine.
3.1.4. Zero divisors and machine halt. Let us call Lau1 au2 . . . a uk QiPj av1 av2 . . . a vl R
the main word .
Theorem 3.2. The machine halts if and only if the main word is a zero divisor in the
algebra presented by the deﬁning relations ⟨3.13⟩–⟨3.23⟩.
Remark. We can consider two semigroups corresponding to our algebra s: in both algebras
each relation is written as an equality of two monomials. The refore the same alphabets
together with the same sets of relations deﬁne semigroups. I n both semigroups the equality
problem is algorithmically solvable, since it is solvable i n algebras. However in the ﬁrst
semigroup a nilpotency problem is algorithmically unsolva ble, and in the second semigroup
a zero divisor problem is algorithmically unsolvable.
The entire proofs can be found at [29].
