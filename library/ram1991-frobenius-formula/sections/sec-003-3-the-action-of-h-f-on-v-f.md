---
doc_id: ram1991-frobenius-formula
doc_title: "A Frobenius formula for the characters of the Hecke algebras"
section_id: sec-003-3-the-action-of-h-f-on-v-f
section_title: "The action of H_f on V^{⊗f}"
section_number: "3"
pages: 7-10
source_pdf: ram1991-frobenius-formula.pdf
source_sha256: 26b2fc85338d9150
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
---
3 The action of H, on V@f
For the remainder of this paper fix positive integers f and n with n > f.
An n-composition of fis a sequence of nonnegative integers c = (c1, C2, . . : , Cn),
Ci ≥ O, such that Ci + C2 + . . . + Cn = f. Note that an n-composition of f is not
a true composition of f since we allow c; =- O. Let x1, X2, : . : , Xn be n independent
(commuting) variables. For any n-composition, c = (c1, C2,. . :, Cn), of f, define
xc= xix?. ..xn.
Let Vi, V2, . . :, Un be an alphabet of n letters (noncommuting variables). The
content c(w) of a word w = Vi, Viz . . . Vi, of length f is the n-composition of f,
c(w) =- (ci, C2, . . : , Cn), such that c; is the number of letters equal to v; in the word w.
words of length f from the alphabet V1, V2, . . . , Un.
For each n-composition c of f define a projection operator E. on V@f by
if c(w) = c ,
otherwise .
Note that for any n-composition c of f, E = Ec, and that if c and c' are
two n-compositions of f such that c  c', then E.Ec. = O. The identity operator
on V@f is
I =ZEc
where the sum is over all n-compositions of f. Let D be the operator
D-ZxE., (3.1)
where, as before, the sum is over all n-compositions of f. For each word
The symmetric group S, acts on the words w = vi, Viz2 : : . Vig, 1 ≤ij = n, of
length f by permuting the letters vi, of w. We shall write the elements of S, as
operators which act on the right so that
Vi, Vi2 ·. . VifSj = Vii ·. . Vij-↓ Vij+1 VijVij+2 ·. . Vif *
gives the action of the simple transposition Sj.
For each generator g; of H, and each word w = Vi, Viz2 : . . Vi, of length f, define
the action of g; on w by
qw if ij =ij+1 ,
wgj (q - 1)w + q1/2 ws; if ij<ij+1 , (3.2)
q1/2 wsj if ij >ij+1 .
(3.3) Proposition. The action defined above extends to a well defined action of H,
JO4 uo
Proof. Checking that the above action satisfies the defining relations for Hf is
a straight forward, albeit slightly lengthy, calculation which we leave to the
reader. 
468 A. Ram
The action above was obtained by rewriting the solutions of the quantum
Yang-Baxter equation. M. Jimbo [Ji] observed that this gives a representation of
the Hecke algebra.
Note that the action of gi, and therefore of Hf, commutes with the action of
D and of E. for each n-composition c of f, since all words in the expansion of wgj
have the same content as w.
Since the words of length f form a basis of v@f, the trace of a linear operator
L on V@f can be given by
tr(L) = Z L(w)lw , (3.4)
where the sum is over all words w of length fand alw, ae V@f denotes the coefficient
of w in the expansion of a as a linear combination of words.
The setup here is analogous to that in [Wz2, Sect. 5]. In particular the following
lemma is a special case of Lemma 5.2 in [Wz2].
(3.5) Lemma. For any idempotent pe Hf, tr(Dp) =- Zw Dwplw is independent of q.
Proof. Let c be an n-composition of f. Since the actions of Hf and Ec commute,
(Ecp)2 = EcpE.p = E p² = E.p. The trace of any idempotent operator is just the
independent of q. Since tr(Dp) = Zcx tr(Ecp), tr(Dp) is also independent of q. 
Lemma 3.5 shows that, for an idempotent pe Hf, one can compute tr(Dp) by
specializing q - 1. When q - 1, the relations in the definition of H, reduce to the
relations defining S, and the action of H, on words reduces to the S, action on
words.
(3.6) Lemma. Recall that Y, = Sr-1 Sr-2 . . . S E Sr. Then, viewing Dy, as an oper-
J@A uo doip
tr(Dyr) = pr(x) = Z xi,
i=1
where pr(x) is the power symmetric function in the variables x1, : . : , Xn.
Proof. It is sufficient to note that
DVit .. . Vi'?rlv... , - Dvi, Vit.. . Vir- lvi.
if i=iz···= i
otherwise. 
(3.7) Lemma. Let pa be a minimal idempotent of CS, such that paza = pa, where
za is the minimal central idempotent of CSy indexed by a. Then
tr(Dpa) = Sa(x) ,
where Sa(x) is the Schur function in the variables X1, X2, . . ., Xn.
A Frobenius formula for the characters of the Hecke algebras 469
Proof. Let d, be the dimension of the irreducible representation of CS, corres-
ponding to . Using (1.2) we have that
tr(Dpa) _tr(Dz
1 da
d, f! Z xs,(0)tr(Do) .
qeSf
Since both xs,(o) and tr(Do) are constant on conjugacy classes Cμ in Sf,
tr(Dpa) : Z x^(μ) tr(Du)ICul
μf
μf u?
where μ? is given by (1.1). Thus, by [Mac, (7.6)J, tr(Dpa) is the Schur function
Sa(x). 
(3.8) Theorem. For any he Hf,
tr(Dh) = Z x^(h)sa(x) ,
where, for each   f, ×~ is the corresponding irreducible character of Hf and sa(x) is
the corresponding Schur function in the variables X1, : . . , Xn.
Proof. Let {pi), a ←f, 1 ≤ i ≤ da be a partition of unity in H, with the property
a partition of unity of CSf. Partitions of unity for H, that satisfy this property are
known, see the remark below. For each a and each 1 ≤ i ≤ d let hi be the constant
in C(q) such that p?hp? =- hip?. Note that the hä are the diagonal elements of the
matrix of h in the irreducible representation corresponding to a determined by this
partition of unity. Thus, for each a, Z;hi - x^(h).
Since the action of D and pä commute in all cases, the trace property gives that
tr(Dpihp) = tr(Dp’pih) = O unless α= μ and i = j.
tr(Dh) - tr(Dphp*)
2, uFf
1≤ijda
tr(Dp hp)
af
1≤ida
Z。ht tr(Dpt).
af
1≤ida
By virtue of Lemma 3.5, tr(Dpi) = sa(x) for all 1 ≤ i ≤ da. Since Z,hi = x^(h) we
have that
tr(Dh) = Z x^(h)sa(x) . 
470 A. Ram
Remark. Some possible choices for the partition of unity in the proof of the above
the property that at q -- 1 it reduces to the partition of unity given by the Young
orthogonal minimal idempotents of Sf. [GyJ constructs a partition of unity in
H, with the property that at q =- 1 it is the partition of unity in CS, given by Young
symmetrizers. Either of these is sufficient for our purposes. The only advantage of
the [Gy] approach is that it is immediate from the definition of the minimal
