---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-013-arikikoike-algebras
section_title: "Ariki–Koike Algebras"
section_number: null
pages: 31-32
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "Hecke algebras, generalisations and representation theory — 27 sections: Algebras of Finite Type; Blocks; Symmetrising forms and Schur eleme"
---
G(l, 1,n ) in the next chapter.
In [ChJa2], building on work by Genet and Jacon [GenJa], we generalised the above result to obtain
canonical basic sets for all groups of type G(l,p,n ) with n> 2, or n = 2 and p odd.
Finally, for the exceptional complex reﬂection groups of rank 2 ( G4,. . . ,G22), we have shown the
existence of canonical basic sets for the cyclotomic Hecke algebras appearing in [BrMa] with respect to
any specialisation θ [ChMi].
28
Chapter 4
Ariki–Koike Algebras
Ariki–Koike algebras were introduced by Ariki and Koike [ArKo] as generalisations of Iwahori–Hecke
algebras of types A and B. They can be viewed as the Hecke algebras associated with the complex
reﬂection groups of typeG(l, 1,n ). In this chapter, we will switch from the notation for the indeterminates
used in Example 3.5 to the notation more traditionally used for Ariki–Koike algebras.
LetR be a commutative integral domain with 1. Fix elementsq, Q0, ..., Ql−1 ofR, and assume that
q is invertible in R. Set q := (Q0, ..., Ql−1 ; q). The Ariki-Koike algebraHq
n is the unital associative
R-algebra with generators s, t1, ..., tn−1 and relations:
(s−Q0)(s−Q1)··· (s−Ql−1) = 0
(ti−q)(ti + 1) = 0 for 1 ⩽i⩽n− 1
st1st1 = t1st1s
titi+1ti = ti+1titi+1 for 1⩽i⩽n− 2
titj = tjti for 0⩽i<j ⩽n− 1 with j−i> 1.
The Ariki-Koike algebra Hq
n is a deformation of the group algebra of the complex reﬂection group
G(l, 1,n ).
Forw∈ Sn, if w =si1...s ir is a reduced expression for w, with si = (i,i + 1), set tw := ti1... tir.
Further, deﬁne elementsXm :=q1−mtm−1... t1st1... tm−1 form = 1, 2,...,n . Ariki and Koike [ArKo]
have proved that the set
{Xa1
1 Xa2
2 ...X an
n tw|w∈ Sn, 0⩽am⩽l− 1 for all m = 1, 2,...,n } (4.1)
is a basis of Hq
n as an R-module. In particular, Hq
n is a free R-module of rank lnn! =|G(l, 1,n )|.
In addition, whenR is a ﬁeld, Ariki and Koike have constructed anHq
n-moduleV λ for eachl-partition
λ of n, which is called the Specht module. These modules form a complete set of non-isomorphic simple
modules in the case where Hq
n is semisimple. By Ariki’s semisimplicity criterion [Ar1], the algebra Hq
n
is (split) semisimple if and only if
∏
1⩽i⩽n
(1 +q +··· +qi−1)
∏
0⩽s<t⩽l−1
∏
−n<k<n
(qkQs−Qt)⁄= 0. (4.2)
