---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-038-33-the-qhi-of-cusped-manifolds-the-aim-of-this-s
section_title: "The QHI of cusped manifolds. The aim of this section is to introduce some general"
section_number: 3.3
pages: 31-32
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
features of the QHI, provide links to the literature (thus ex plaining notations), and to explain
the splitting formula of the QHI into the symmetry defects an d the reduced QHI. We refer to
[4] for the deﬁnition of the QHI of cusped manifolds by means o f state sums over geometric
branched ideal triangulations, and to [7] for the general si tuation of non necessarily branched
triangulations. The QHI of cusped manifolds used in this pap er are those of [7, Theorem
1.1], in the case where the bulk weights hf,hc are zero, or are determined by the boundary
weights kf,kc (as for link complements). (By [8, Corollary 1.8 (1)], anoth er choice of bulk
weight would at worst modify these QHI by multiplication wit h a 4N -th root of unity, which
has no consequence on the results of this paper.)
LetM be a cusped manifold. As usual we denote by ¯M the compact manifold with interior M ,
X(M ) is the variety of PSL (2, C)-characters of M , andXhyp(M ) ⊂X(M ) is the “geometric”
irreducible component, containing the character ρhyp of the complete hyperbolic holonomy
(see Section 2.2.2).
The QHI of M are sequences of complex numbers HN (M,ρ,k c,kf ) modulo multiplication
by 2N -th roots of unity, indexed by the odd positive integers N ≥ 3. The arguments of
HN (M,ρ,k c,kf ) are:
(i) a character ρ ∈Xhyp(M ),
(ii) classes kc ∈H 1(∂ ¯M, Z) and kf ∈H 1(∂ ¯M, C) satisfying (20).
The invariant HN (M,ρ,k c,kf ) is computed by the total contractions, denoted HN,(T,b,c ) and
called QHI state sums , of certain tensor networks associated to the ideal triangu lations T of
M , similarly as in the Turaev-Viro TQFTs. The QHI state sums ar e functions of combinato-
rial data on T encoding ρ ∈X(M ) and kc,kf as in (i)-(ii): ρ is encoded by a point wρ of the
gluing variety G(T,b ) (for some b), which is possible for most characters ρ in Xhyp(M ) (see
Remark 2.9), and the classes kf and kc are a ﬂattening weight and a charge weight, encoded
by ﬂattenings f and charges c as in Remark 2.4-2.5. When ρ is contained in Xhyp(M ) all
the choices of ( T,b,w ρ,c,f ) eventually give the QHI state sums the same value, which by
deﬁnition is HN (M,ρ,k c,kf ).
It is shown in [8] that, up to a possible stronger ambiguity mo dulo multiplication by 4 N th-
roots of unity, which we denote by = µ4N , we have a factorization into reﬁned invariants (recall
that lκ :=kf −iπkc)
(76) HN (M,ρ,k f,kc) =µ4N αN (M,ρ,k c; s)Hred
N (M,ρ,lκ ; s),
called respectively the symmetry defect and the reducedQHI. These reﬁned invariants depend
on an additional structure s onM , called a non ambiguous structure, which is of topological
nature ( s is an equivalence class of ideal triangulations under a rest ricted set of branched
Pachner 2 − 3 moves). The argument lκ on the right side is the log weight, see (18) and (21)
(in [8] it was denoted κ, and called a fused weight).
Remark 3.9. When M ﬁbers over S1, any ﬁbration ψ : M → S1 (with oriented ﬁbers)
deﬁnes a canonical non ambiguous structure sψ on M , carried by the ideal triangulations of
M which are layered triangulations for the ﬁbration ([8, Prop . 6.3(1)]). Such triangulations
are taut, which allows to associate to them a canonical charg e, as in Remark 2.4, whence a
canonical charge weight kψ, as in Remark 2.5, to the ﬁbration ([8, Prop. 4.3(2) and 4.8(2 )]).
From the deﬁnition of the symmetry defect ([8, page 808]), it is quite immediate to check that
αN (M,ρ,k ψ; sψ) = 4N 1 for every ρ, whence HN (M,ρ,k f,kψ) =µ4N Hred
N (M,ρ,k f −iπkψ; sψ).
Note, however, that the classes kψ are very peculiar, and a layered triangulation can carry
several (possibly taut) non ambiguous structures, that the symmetry defect αN (M,ρ,k c; s)
can distinguish (see the examples in [8, Section 9]).
32 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
Recall the relations (16)-(17). By setting
