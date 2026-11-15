---
doc_id: s10052-023-11923-y-a
doc_title: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-007-42-the-left-multiplication-algebra-of-mathbbcoti
section_title: "The left multiplication algebra of mathbbCotimesmathbbS"
section_number: 4.2
pages: 6-7
source_pdf: s10052-023-11923-y_a.pdf
source_sha256: 73d1a03532d62ef7
toc_source: outline
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
duplicate_of: "arxiv-2306.13098v2"
---
Despite the algebra S being non-associative and non-
alternative, just as for O, we can consider the left actions
of S on itself as linear operators generating an associative
algebra.
4 Note that this is a new feature that appears with S. There are three
new, (that is excluding the original H with basis {e0, e1, e2, e3} used to
generate O) H subalgebras of O that do no contain e4. For S there are
no new O that do not contain e8.
5 The Moufang identities, describing a weaker notion of associativity,
are essentially equivalent to left and right alternativity, and ﬂexibility.
The generalisation from (C ⊗O)L to (C ⊗S)L is not
immediately obvious because the identities which held for
(C ⊗O)L, namely
Li1 Li2 Li3 Li4 Li5 Li6x = Li7x,
(8)
...Lib Lia Lia Lic....x = −...Lib Lic....x,
(9)
...Lia Lib...x = −...Lib Lia...,
(10)
where a, b, c = 1, . . . , 7 are no longer satisﬁed by general
composition of sedenion left multiplications. Although one
ﬁnds a new identify
Ls1 Ls2...Ls14w = Ls15w,
(11)
the two identities (9) and (10), crucial for generating a
Clifford algebra, no longer hold in general. For example,
s3(s14(s1)) = −s14(s3(s1)), but s3(s14(s2)) = +s14(s3(s2).
Consequently, the left multiplications of the (complex) sede-
nions do not generate Cℓ(14), as one might initially expect.
However, since the linear operators corresponding to each
complex sedenion left multiplication can be written as a
16×16 matrix with complex entries acting on C⊗S written
as a column vector, one would expect to be able to gener-
ate Mat(16, C) ∼= Cℓ(8). It then remains to ﬁnd a suitable
set of sedenion elements that generate Cℓ(8) via their left
multiplication. Closer inspection reveals that all the left mul-
tiplications of the original octonion elements e0 = i0 =
s0, . . . , e7 = i7 = s7 do satisfy the identities (9) and (10)
(where now the action is on C ⊗S instead of C ⊗O), as do
all new sedenion basis elements e9 = s9, . . . , e15 = s15:
ei(e jw) = −e j(eiw),
(12)
ei(eiw) = −w,
(13)
ei+8(e j+8w) = −e j+8(ei+8w),
(14)
ei+8(ei+8w) = −w,
(15)
where i, j = 1, . . . , 7, ∀w ∈C ⊗S. However, ei and ei+8
fail to anti-commute (or commute) with each other as left
actions
ei(e j+8w)̸ = −e j+8(eiw).
(16)
The left action of e8 however anti-commutes with the left
action of every other basis element. One possible generat-
ing basis for Cℓ(8) is therefore given by the left multipli-
cations of {e1, . . . , e8}. Another possible generating basis is
{e8, . . . , e15}.
Accepting some abuse of notation, we now simple write
Lei = ei and take e0, e1, . . . , e8 as our generating basis for
Cℓ(8). We will also no longer explicitly write w to indicate
that Cℓ(8) acts on w ∈S from the left via composition.
The left action of the remaining sedenion basis elements
e9, . . . , e15 then need to be expressed as the left action of
some element of Cℓ(8). After careful consideration one ﬁnds
that
123
e9 = 1
2(−e123458 + e123678 + e145678 −e18),
e10 = 1
2(−e123468 −e123578 + e245678 −e28),
e11 = 1
2(−e123478 + e123568 + e345678 −e38),
e12 = 1
2(e124568 + e134578 + e234678 −e48),
e13 = 1
2(e124578 −e134568 + e235678 −e58),
e14 = 1
2(e124678 −e135678 −e234568 −e68),
e15 = 1
2(e125678 + e134678 −e234578 −e78),
(17)
where we can see that e18 = e1e8 = Le1 Le8, e123458 =
e1e2e3e4e5e8 = Le1 Le2 Le3 Le4 Le5 Le8 etc are elements of
Cℓ(8).
