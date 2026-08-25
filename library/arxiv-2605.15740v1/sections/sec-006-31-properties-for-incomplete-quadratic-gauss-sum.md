---
doc_id: arxiv-2605.15740v1
doc_title: "BAILEY P AIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS"
section_id: sec-006-31-properties-for-incomplete-quadratic-gauss-sum
section_title: "Properties for incomplete quadratic Gauss sums"
section_number: 3.1
pages: 13-14
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
doc_brief: "BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´ e homology"
---
an incomplete quadratic Gauss sum. For simplicity, we writeχ=χ ℓ
p. Recall thatP:=p 1p2p3.
Lemma 3.1.Assume that
(i)P≡2 (mod 4),
(ii) ifχ(n)̸= 0, thennis odd
(iii)χis even moduloP, i.e.,χ(P−n) =χ(n).
Ifqis a primitiveNth root of unity, then
2
PNX
n=0

1− n
PN

χ(n)q
n2
4P =
PNX
n=0
χ(n)q
n2
4P.
Proof.We have
2
PNX
n=0

1− n
PN

χ(n)q
n2
4P
=
PNX
n=0

1− n
PN

χ(n)q
n2
4P +
PNX
n=0

1− n
PN

χ(n)q
n2
4P
=
PNX
n=0

1− n
PN

χ(n)q
n2
4P +
PNX
n=0

1− (PN−n)
PN

χ(PN−n)q
(PN−n) 2
4P
=
PNX
n=0

1− n
PN

χ(n)q
n2
4P +
PNX
n=0
n
PN χ(PN−n)q
(P 2N 2−2nPN+n 2)
4P
14 JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
=
PNX
n=0

1− n
PN

χ(n)q
n2
4P +
PNX
n=0
n
PN q
n2
4Pχ(PN−n)q
N(PN−2n)
4 .(3.1)
Consider the term
χ(PN−n)q
N(PN−2n)
4 .
We have two cases according to the parity ofN. First, ifNis odd then sinceP≡2 (mod 4)
andnis odd we have thatPN−2nis a multiple of 4. Thereforeq
N(PN−2n)
4 = 1. Moreover, by
(iii) we haveχ(PN−n) =χ(n). Hence
χ(PN−n)q
N(PN−2n)
4 =χ(n).
IfNis even, thenPN−2n≡2 (mod 4) and soq
N(PN−2n)
4 =−1. Now sinceNis even we have
χ(PN−n) =−χ(n). Once again, we find that
χ(PN−n)q
N(PN−2n)
4 =χ(n).
Using this in (3.1) we have
2
PNX
n=0

1− n
PN

χ(n)q
n2
4P =
PNX
n=0

1− n
PN

χ(n)q
n2
4P +
PNX
n=0
n
PN q
n2
4Pχ(n)
=
PNX
n=0
χ(n)q
n2
4P,
as desired. □
Remark 3.2.Note that (i) and (ii) in Lemma 3.1 are satisfied for all of the functionsχ ℓ
p
considered in Theorem 1.2. Moreover,p 1 = 2 and so by [18, (3.8)] the involutionσ 1 fixes
ℓ= (1,1,ℓ 3), i.e.,χ ℓ
p(n+P) =−χ ℓ
p(n). Now replacenwith−nand use the fact thatχ ℓ
p is odd
to obtain (iii) in Lemma 3.1. Finally, note thatχ ℓ
p is odd moduloNPfor all evenNand even
moduloNPfor all oddN.
Next, we recall a result (see [16, Proposition 3] or [29, Corollary 3.9]) which explicitly computes
the limiting values of the Eichler integrals eΦℓ
p(τ) asτ→ M
N .
Proposition 3.3.LetMandNbe coprime positive integers. We have
lim
τ→M
N
eΦℓ
p(τ) =
PNX
n=0
χℓ
p

1− n
PN

ζ
Mn2
4P
N .
