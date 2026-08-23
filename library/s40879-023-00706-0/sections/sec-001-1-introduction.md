---
doc_id: s40879-023-00706-0
doc_title: "Bring's curve: old and new"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
doc_brief: "Bring's curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
Bring’s curve, a genus 4 Riemann surface ﬁrst introduced by Erland Bring in 1786 in
relation to solutions of the quintic equation, is the unique genus 4 curve with automor-
phism group S5, the largest possible group for curves of this genus. This automorphism
group acts transitively on the Weierstrass points of the curve, which are all weight 1, a
The research of LDH is supported by a UK Engineering and Physical Sciences Research Council
(EPSRC) studentship.
B Harry W. Braden
hwb@ed.ac.uk
Linden Disney-Hogg
A.L.Disney-hogg@sms.ed.ac.uk
1 School of Mathematics and Maxwell Institute for Mathematical Sciences, The University of
Edinburgh, Edinburgh EH9 3FD, Scotland, UK
123
3 Page 2 of 46 H.W. Braden, L. Disney-Hogg
very rare property of curves. The curve can moreover be seen to be an example of an
elliptic modular surface, and has a unique (even) theta characteristic invariant under
the action of the whole automorphism group. It shares all these properties with Klein’s
curve, a genus 3 curve which has been studied extensively [ 46].
We aim to give a uniﬁed review of many of these aspects of Bring’s curve, extend
these results and provide connections between them. This will include providing an
explicit presentation of the S
5 group in terms of birational automorphisms of a plane-
curve model, using this to completely describe the quotient structure of the curve,
identifying ﬁxed points of these quotients with geometrically signiﬁcant points on the
curve including the Weierstrass points, and utilising these geometric points to describe
the orbit decomposition of odd theta characteristics on the curve.
Moreover, we will construct an explicit birational map between the canonical
embedding of the curve and a plane-curve model. This will allow us to use mod-
ern tools in SageMath, Maple, and Macaulay2 (all interfaced through Sage) to clarify
and ﬁx errors in the existing literature as well as ﬁnding the orbit decomposition of
even theta characteristics of the curve. We shall also calculate the unique invariant
theta characteristic on the curve as a vector in the Jacobian, making explicit previous
work of others. These calculations are presented in Jupyter notebooks, available at
https://github.com/DisneyHogg/Brings_Curve.
The structure of the papers is as follows, in Sect. 2 we recall basic properties from
the literature, provide the birational map between models of the curve and describe the
period matrix and automorphism group of the curve. In Sect. 3 we identify geometri-
cally relevant orbits of points under the action of the automorphism group, notably the
Weierstrass points W, for which we construct the associated holomorphic differentials
with vanishing of order 4 at W and the meromorphic functions with poles only at W ;
indeed we shall describe the divisors of these completely. (Recall, for comparison,
that while the pole of the Weierstrass ℘-function is z = 0, describing its zeros is non-
trivial.) In Sect. 4 we use the action of the automorphism group to explicitly describe
the quotient structure of the curve. Using representation theory we elucidate much of
the structure of the Jacobian of Bring’s curve, giving new derivations of previously
known results, and identifying new quotients of the curve. In doing so, we also discover
isomorphisms (as opposed to isogenies) of quotients not explained by group theory
alone, and these deserve further study. In Sect. 5 we will develop the understanding
of the theta characteristics on the curve, including explicitly the unique invariant one.
Bring’s curve has arisen in many disparate mathematical areas and we will use this
paper to also make some of these results and interconnections more widely known;
we will however not focus on either the modular aspects of Bring’s curve or extension
to positive characteristic here. Because of the wide-ranging nature of this paper we
will conclude in Sect. 6 by summarising our new results having by then placed these
in context. We draw attention here to two areas we feel merit further explanation.
This work answers questions ﬁrst raised in [ 8], and we will leave many expository
results to that paper. For a source on background classical material, see [ 27]. Unless
otherwise said explicitly, we shall assume the Riemann surfaces we discuss are all
smooth.
123
Bring’s curve: old and new Page 3 of 46 3
2 Deﬁning equations and elementary properties
