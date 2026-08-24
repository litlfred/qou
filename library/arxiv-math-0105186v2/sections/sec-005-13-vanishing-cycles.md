---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-005-13-vanishing-cycles
section_title: "Vanishing cycles"
section_number: 1.3
pages: 17-20
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
We have seen that all Dehn twists can be realized as monodromy maps (of
standard ﬁbrations). Conversely, the geometry of any exact Lefschetz ﬁbration
can be understood in terms in Dehn twists. This is again well- known on a
topological level, and our exposition repeats the classica l arguments while paying
more attention to symplectic forms. The results will not be u sed again in this
paper, but they are important in applications.
Let (E,π ) be an exact Lefschetz ﬁbration over S. Take z0 ∈ Scrit, and
the unique critical point x0∈ Ez0 . Let c : [a;b]→ S be a smooth embedded
path with c(b) = z0, c−1(Scrit) = {b}; and let ρc|[s,s′] : Ec(s)→ Ec(s′) be the
parallel transport maps along it, which is deﬁned for all s≤ s′ < b. Following
a suggestion of Donaldson, we deﬁne
Bc ={x∈Ec(s), a≤s<b : lim
s′→b
ρc|[s;s′](x) = x0}∪{ x0}⊂ E. (1.21)
Lemma 1.13. Bc is an embedded closed (n + 1)-ball, with ∂Bc = Bc∩Ec(a).
The function p =c−1◦π :Bc→ [a;b] has x0 as its unique critical point, which
is a nondegenerate local maximum. Moreover, Ω|Bc = 0.
Proof. Put a symplectic form Ω+ π∗β onE as in Lemma 1.5. Choose an oriented
embedding ˜c : (a−ǫ;b +ǫ)× (−ǫ;ǫ)→S such that ˜c(0,t ) = c(t). Let h be the
function deﬁned on im(˜c) with h(˜c(s,t )) =−t. The Hamiltonian vector ﬁeld X
of H =h◦π has the following properties:
17
(i) it is horizontal everywhere, Xx∈TEh
x ;
(ii) for each x⁄=x0, Dπ(X)x is a positive multiple of ∂˜c/∂s;
(iii) x0 is a hyperbolic stationary point of X, with n + 1 positive and negative
eigenvalues.
(i) and (ii) are straightforward; (iii) can be seen by lookin g atX in a holomorphic
Morse chart, where it is J0∇H. Let ˜B⊂E be the stable manifold of x0. It is
an open (n + 1)-ball, lies in π−1˜c((a−ǫ;b]×{ 0}), and the projection
˜p = ˜c−1π : ˜B−→ (a−ǫ;b]×{ 0}
is a proper map. The tangent space of ˜B at x0 is the negative eigenspace of
DXx0; one shows easily that D2 ˜p|T ˜Bx0 diﬀers from DX|T ˜Bx0 only by a positive
constant, which means that x0 is a nondegenerate maximum of ˜ p. There are
no other critical points, because elsewhere d˜p(X)x > 0 by (ii). Finally, since
the ﬂow X is symplectic and contracts the tangent spaces of ˜B, these must be
Lagrangian subspaces, so (Ω + π∗β)| ˜B = Ω| ˜B = 0.
We claim that Bc = ˜B∩π−1(im(c)), which implies all desired properties
of Bc. Let Y be the vector ﬁeld on π−1(im(˜c))\{x0} which is horizontal and
satisﬁes Dπ(Y ) = ∂˜c/∂s. From (i) and (ii) above one sees that Y = gX for
some function g, bounded from below by a positive constant, and which goes
to∞ as one approaches x0. Therefore the orbits of X and Y coincide, except
of course for {x0}. Since Y|π−1(im(c)) deﬁnes parallel transport along c, the
claim follows.
Lemma 1.14. Vc = ∂Bc is an exact Lagrangian sphere in Ec(a), and comes
with a canonical framing.
Proof. Since Bc is a ball and Θ |Bc is closed, there is a unique K∈C∞(Bc, R)
withK(x0) = 0 and dK = Θ |Bc. The restriction KVc =K|Vc makesVc into an
exact Lagrangian submanifold. It remains to explain the fra ming. In any chart
onBc aroundx0, the level sets p−1(s′) of the function from Lemma 1.13, for s′
close to b, will be strictly convex hypersurfaces, so that one can map t hem to
Sn by radial projection. On the other hand, Vc =p−1(a) can be identiﬁed with
p−1(s′) by the gradient ﬂow with respect to some metric. Combining t hese two
maps gives a diﬀeomorphism Vc→Sn, which is unique up to isotopy and action
of O(n + 1); its inverse is our framing.
The framed exact Lagrangian sphere Vc⊂Ec(a) is called the vanishing cycle
associated to c. It exists more generally for any path c : [a;b]→ S which is
smooth, not necessarily embedded, but still satisﬁes
c−1(Scrit) ={b}, c ′(b)⁄= 0. (1.22)
To construct it in this situation, one ﬁrst extends c to a map ( a−ǫ;b +ǫ)×
(−ǫ;ǫ)→S which is a local oriented diﬀeomorphism at ( b, 0), pulls back (E,π )
by that map, and then applies Lemma 1.13 to the pullback exact Lefschetz
18
ﬁbration. Note also that deforming c smoothly, rel endpoints, within the class
(1.22) yields an exact Lagrangian isotopy of the correspond ing vanishing cycles,
which is compatible with their framings.
c
c(b) l
c(a)
Figure 1:
Proposition 1.15. Letc be a path satisfying (1.22), and l the loop in S\Scrit
obtained by “doubling” c, as in Figure 1. Then the monodromy around l is
isotopic to the Dehn twist along the vanishing cycle Vc:
[ρl] = [τVc ]∈π0(Sympe(Ec(a))). (1.23)
Proof. We start with a rather special case. Let ( E,π ) be an exact Lefschetz
ﬁbration with base ¯D(r) for some r> 0, and which has exactly one critical point
x0∈ E0. Write M = Er. In addition, x0 should admit a holomorphic Morse
chart (ξ, Ξ) where Ξ is deﬁned on W ={x∈ Cn+1 : ||x||≤ 2√r,|q(x)|≤ r},
where ξ = id ¯D(r), and such that Ξ ∗Ω, Ξ ∗Θ are standard. This means that the
symplectic geometry of (E,π ) equals that of the local model ( Cn+1,q ) discussed
in Lemma 1.10, at least in a suitable neighbourhood of x0. In particular, each
ﬁbre Ez,z⁄= 0, contains an exact Lagrangian sphere Σ E
z = Ξ(Σ z), degenerating
to Σ E
0 ={x0}. Write L = Σ E
r ⊂ M ; this inherits an obvious framing from
Σ r =√rSn. We claim that the monodromy around ∂ ¯D(r), denoted by ρ∈
Sympe(M ), is isotopic to τL.
From (1.12) one deduces that parallel transport in ¯D(r)\{ 0} carries the
Σ E
z into each other. Moreover, by the same argument as in Lemma 1. 10, if
one removes Σ E = ⋃
z Σ E
z from E, parallel transport can be extended over the
singular ﬁbre. Using parallel transport in radial directio ns one constructs a
trivialization Φ E : E\ Σ E −→ ¯D(r)× (M\L) which is the identity on the
ﬁbre over r; this is such that, in radial coordinates z = seiα on the basis,
((Φ E)−1)∗Θ = θ−RE∧dα +dSE for some functions RE = RE(s,α,x ) and
SE =SE(s,α,x ) which vanish for x close to ∂M . This implies that ρ restricted
to M\ L is the time-2 π map of the ﬂow generated by the time-dependent
Hamiltonian (α,x )↦→RE(r,α,x ). Clearly, [ ρ]∈ π0(Sympe(M )) depends only
on the behaviour of this function in an arbitrarily small nei ghbourhood of L, or
equivalently on (E,π ) and Ω close to Σ E; since Σ E⊂ Ξ( W ) by deﬁnition, this
19
can be determined from the local model ( Cn+1,q ). It remains to spell out the
computation.
Deﬁne an embedding ι : T (λ)→ M , for some λ > 0, by combining Ξ r =
Ξ|(W∩q−1(r))→M with the inverse of the isomorphism φr :q−1(r)→T from
the proof of Lemma 1.10. This satisﬁes ι∗θ =θT , ι∗ω =ωT , and ι(T (0)) = L.
Because both Φ E and the trivialization Φ from (1.13) are deﬁned by radial
parallel transport, there is a commutative diagram
Cn+1\ Σ
Φ /d47/d47 C× (T\T (0))
W\ Σ
/d63/d31
/d79/d79
Ξ |W \Σ
/d15/d15
¯D(r)× (T (λ)\T (0))
/d63/d31
/d79/d79
id×(ι |T (λ)\T (0))
/d15/d15
E\ Σ E Φ E
/d47/d47 ¯D(r)× (M\L).
From this, Ξ ∗Ω = ωCn+1 and (1.14) it follows that
(id×ι)∗(θT−REdα +dSE) = (id×ι)∗((Φ E)−1)∗Θ
= (Φ −1)∗θCn+1 =θT− ˜Rs(µ)∧dα,
and in particular that RE(r,α,ι (y)) = ˜Rr(µ(y)) for all α. In view of the dis-
cussion above, and the fact that ˜Rr(−t) = ˜Rr(t)−t, this implies the desired
equality [ρ] = [ τL]. Now consider the path c : [0; r]→ ¯D(r), c(s) = r−s.
Because symplectic parallel transport takes the Σ E
z into each other, the ball Bc
from Lemma 1.13 must be the union of Σ E
z for all z∈ [0;r], and the vanishing
cycle is Vc = Σ E
r =L⊂M , with the same framing as before. Therefore, what
we have done up to now proves (1.23) for this special class of e xact Lefschetz
ﬁbrations ( E,π ) and the particular path c.
More generally, let ( E,π ) be a exact Lefschetz ﬁbration with arbitrary base
S, and x0∈Ez0 a critical point which admits a holomorphic Morse chart ( ξ, Ξ)
such that Ξ ∗Ω, Ξ ∗Θ are standard. By restricting to a suitably small disc aroun d
z0 in the base, and making the domains of ξ, Ξ smaller, one can arrive at the
situation considered before. This means that (1.23) is true at least for one
(short) path c with endpoint z0. But from that it follows easily for all other
paths with the same endpoint.
It remains to remove the assumption concerning Ξ. Let ( E,π ) be an arbitrary
exact Lefschetz ﬁbration, c a path as in (1.22), and l a corresponding loop. With
respect to the critical point in Ec(b), take smooth families Ω µ, Θ µ as in Lemma
