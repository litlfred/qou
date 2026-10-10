---
doc_id: ram1991-frobenius-formula
doc_title: "A Frobenius formula for the characters of the Hecke algebras"
section_id: sec-005-5-formulas-for-the-irreducible-characters-of
section_title: "Formulas for the irreducible characters of H_f"
section_number: "5"
pages: 16-19
source_pdf: ram1991-frobenius-formula.pdf
source_sha256: 26b2fc85338d9150
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "A Frobenius formula for the characters of the Hecke algebras — This paper uses the theory of quantum groups and the quantum Yang-Baxter equation as a guide in order to produce a method of computing"
---
5 Formulas for the irreducible characters of H f
(5.1) Theorem. For each T., e Sf, there exists a Z[q] linear combination
Co = Z aou T. ,
μf
aoue Z[q], such that x(T.) = x(co) for all characters x of Hf.
Proof. Let c be a composition of f and let u be the partition of f determined by
rearranging the parts of c in decreasing order. Then by Theorem 4.2 we know that
tr(DT,.) = tr(DT,.). Since the Schur functions Sa(x1, X2, : : : , xn) are linearly inde-
pendent, it follows from Theorem 3.8 that ×^(T,.) = x(T,.) for all irreducible
characters x~ of Hf. This shows that it is sufficient to prove that there exists a Z[q]
linear combination
d。=  bocT,
cf
bacEC(q), such that x(T) = x(d.) for all characters × of Hf:
Let x be a character of Hr and let eSf. Let i be the first i such that
o(i) > i + 1. The proof is by induction on i and reverse induction on o(i). Note that
any  that does not have such an i is of the form ?c for some c f.
  =()  ( s ()=   that
t(osj) < t(o) and thus T = Ts;9j.
Case 1 t(s;osi) > t(os;):
Then
x(T) = x(Tsj9j)
= x(g;Ts;)
= x(Tsjos;) .
Note now that for the permutation o' - Sjos; we have o'(i) = j = o(i) - 1.
Case 2 t(sjos;) < t(os;):
Then Tas, = g;Tsjos; and thus T。 = gj;Tsjs;9j. So
x(T) = x(g;Tsjas;9j)
= x(g} Tjasj)
= (q - 1)x(g;Tsjos;) + qx(Tsjosj)
= (q - 1)x(Tas,) + qx(Tsjas;) .
Here again, for each of the permutations o' - os; and o' - Sjos; we have that
g'(i) = j = (i) - 1.
Thus x(T) can be written as a linear combination of x(T.) where for each o' we
have that o'(i) =- o(i) -- 1. This completes the induction. 
A Frobenius formula for the characters of the Hecke algebras 477
The following corollary is an immediate consequence of Theorem 5.1.
(5.2) Corollary. Any character of H, is determined by its values on the elements Tr..
μf.
Since H  is semisimple and its irreducible components are indexed by partitions
of f, every character of Hf must be a linear combination of the irreducible
characters ×, a  f, of Hf. This implies that the set of values x(T,), a  f, is actually
a minimal set of values necessary to determine the character x of Hf.
The following is an example to illustrate the algorithm used for finding the
linear combination c. in Theorem 5.1. The notation is such that 3421 denotes the
permutation in two line notation.
x(T3421) = (q - 1)x(T2431) + qx(T2341)
= (q - 1)((q - 1)x(T2341) + qx(T2314)) + qx(T2341)
= ((q - 1)2 + q)T, + (q - 1)qT2×1 :
A formula in terms of characters of the symmetric group
For each partition a = (ai, . . :, ak) of f let Φ^: CSf -→C be the character of the
representation of S, given by inducing the trivial representation of the group
Sa, × . . . × San to Sg. Let Φ"(μu) denote the value Φa on elements of S, of cycle type
μ. It is well known that the βa(μ) are the coefficients in the expansion,
pμ(x) = ZΦ^(μ)ma(x) , (5.3)
of the power symmetric functions pμ(x) in terms of the monomial symmetric
functions ma(x) in the variables X1, . . : , Xn.
(5.4) Theorem. Let   f and let × be the irreducible character of the Hecke algebra
Hr corresponding to 2. Then
x~(T, I(qi - 1) xs,(v)Φu(v) ,
(g - 1)(m)
where v? is given by (1.1) and x$, is the irreducible character of S corresponding to the
partition μ. The Vi are the parts of the partition v.
Proof. Using the expansions in (4.10),
hu(X(1 - t)s(X) = Z hu(X(1 - t)mμ(Y)is(X)m()
I(1 - t")
p(X)p(Y)Is;(X)m(Y) :
478 A. Ram
By the expansion
pu(X) = Z xs,(μu)sa(X)
and (5.3),
1l:(1  tvi)
hu(X(1 - t)Is;(X) = Z v? E xs,(v)sa(X) E (v)mu(Y)
sa(X)mμ(Y)
Ii(1 - tvi) xs,(v)pu(v) .
The result follows from Theorem 4.13(f) and the Frobenius formula.
Remark. For each permutation π e S, define t(π) = (t1, :. :. : , tk) to be the cycle type
of π and for each μ f define a class function @u: S, -→ Z[q] by
Φ"(π), I:(q - 1)
Φu(π) :
(q -- 1)(m) T(π)?
The usual inner product on class functions is given by
reSf
for class functions X1, X2 on Sf. Using this one can restate Theorem 5.4 in the form
x(T) =<xs+,Φu>,
where, as before, xs, denotes the irreducible character of Sf corresponding to the
partition a.
A formula in terms of multiplicities
(5.5) Theorem. Let cauy denote the Kronecker coeffcient and let Kau be the Kostka
number. Then the irreducible character of the Hecke algebra corresponding to the
partition a is given by the formula
m= 1
Proof. Using the product formula for Schur functions and then Lemma 4.12 we
have that
hu(X(1 - t) = Z s,(X(1 - t)Kvμ
ZZZcvapsa(X)sp(1 - t)Kvu
-Zsa(X)Z Z Cva(1 -mm)S(1f-mm)(1 - t)Kyμ
vm=1
=Esa(X) Z (1 - t)(- t)-mZcva(1-mm)Kvu
m=1
A Frobenius formula for the characters of the Hecke algebras 479
Then, by Theorem 4.13(f) and the Frobenius formula.
Z (1 -q=1)(-q=1)5-mZcva(1-mm)Kvμ. [
m= 1
