---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
Bring’s curve, a genus-4 Riemann surface ﬁrst introduced by Erland Bring in 1786 in
relation to solutions of the quintic equation, is the unique genus-4 curve with automorphism
group S5, the largest possible group for curves of this genus. This automorphism group
acts transitively on the Weierstrass points of the curve, which are all weight one, a very
rare property of curves. The curve can moreover be seen to be an example of an elliptic
modular surface, and has a unique (even) theta characteristic invariant under the action of
the whole automorphism group. It shares all these properties with Klein’s curve, a genus-3
curve which has been studied extensively [Lev01].
We aim to give a uniﬁed review of many of these aspects of Bring’s curve, extend these
results and provide connections between them. This will include providing an explicit pre-
sentation of theS5 group in terms of birational automorphisms of a plane-curve model, using
this to completely describe the quotient structure of the curve, identifying ﬁxed points of
these quotients with geometrically signiﬁcant points on the curve including the Weierstrass
points, and utilising these geometric points to describe the orbit decomposition of odd theta
characteristics on the curve.
Moreover, we will construct an explicit birational map between the canonical embedding
of the curve and a plane-curve model. This will allow us to use modern tools in SageMath,
Maple, and Macaulay2 (all interfaced through Sage) to clarify and ﬁx errors in the existing
literature as well as ﬁnding the orbit decomposition of even theta characteristics of the curve.
We shall also calculate the unique invariant theta characteristic on the curve as a vector in
the Jacobian, making explicit previous work of others. These calculations are presented in
Jupyter notebooks, available at https://github.com/DisneyHogg/Brings Curve.
The structure of the papers is as follows, in §2 we recall basic properties from the lit-
erature, provide the birational map between models of the curve and describe the period
matrix and automorphism group of the curve. In §3 we identify geometrically relevant orbits
of points under the action of the automorphism group, notably the Weierstrass pointsW , for
which we construct the associated holomorphic diﬀerentials with vanishing of order 4 at W
and the meromorphic functions with poles only atW ; indeed we shall describe the divisors of
2020 Mathematics Subject Classiﬁcation. 14E07, 14H55, 14Q05, 14K02, 14K25.
1
arXiv:2208.13692v1  [math.AG]  29 Aug 2022
2 H. W. BRADEN AND LINDEN DISNEY-HOGG
these completely. (Recall, for comparison, that while the pole of the Weierstrass ℘-function
is z = 0, describing its zeros is nontrivial.) In §4 we use the action of the automorphism
group to explicitly describe the quotient structure of the curve. Using representation theory
we elucidate much of the structure of the Jacobian of Bring’s curve, giving new derivations
of previously known results, and identifying new quotients of the curve. In doing so, we also
discover isomorphisms (as opposed to isogenies) of quotients not explained by group theory
alone, and these deserve further study. In §5 we will develop the understanding of the theta
characteristics on the curve, including explicitly the unique invariant one. Bring’s curve has
arisen in many disparate mathematical areas and we will use this paper to also make some of
these results and interconnections more widely known; we will however not focus on either
the modular aspects of Bring’s curve or extension to positive characteristic here. Because of
the wide-ranging nature of this paper we will conclude in §6 by summarising our new results
having by then placed these in context. We draw attention here to two areas we feel merit
further explanation.
This work answers questions ﬁrst raised in [BN12], and we will leave many expository
results to that paper. For a source on background classical material, see [FK92]. Unless
otherwise said explicitly, we shall assume the Riemann surfaces we discuss are all smooth.
Acknowledgements. We are grateful to Vanya Cheltsov for discussions. The research of
LDH is supported by a UK Engineering and Physical Sciences Research Council (EPSRC)
studentship.
