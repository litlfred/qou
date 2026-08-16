---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-009-1-analytic-continuation-topological-point-of-vie
section_title: "ANALYTIC CONTINUATION; TOPOLOGICAL POINT OF VIEW. 11"
section_number: 1
pages: 14-15
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
Abstract: Thanks to Berkovich’s presentation of p-adic analytic geometry, it
is possible to make sense of the familiar monodromy principl e in the exotic world
of p-adic manifolds. Its application is however more limited th an in the classical
case, because (1) sheaves of solutions of linear diﬀerentia l equations are usually not
locally constant, and (2) many spaces (for instance, annuli ) are simply connected.
1.1. The Monodromy principle.
Let S be a topological space, and F an abelian sheaf on S. For an
open set U⊆ S and a section f∈ Γ(U,F), the support of f is the subset
Supp(f ) ={u∈U| fu⁄= 0}, which is easily seen to be closed in U .
Deﬁnition 1.1.1. We say that the sheaf F satisﬁes the principle of unique
continuation if for any open set U ⊆ S and any section f ∈ Γ(U,F) the
support Supp(f ) is open in U .
Note that the principle of unique continuation is a local pro perty.
Lemma 1.1.2. IfF satisﬁes the principle of unique continuation, then any
two sections f,g ∈ Γ(U,F) on a connected open subset U⊆ S coincide if
(and only if ) their germs fs, gs at some point s∈U coincide. The converse
also holds if S is locally connected.
Proof. The ﬁrst assertion is clear. For the converse, let u be a point
adherent to the complement of Supp( f ). There exists a suﬃciently small
connected open neighborhood V of u contained in U . Since fs = 0 at some
point s∈V , f≡ 0 on V . Hence u⁄∈Supp(f ). This shows that Supp( f ) is
open.
Lemma 1.1.3. Let p : F → S be the local homeomorphism canonically
attached to F: F(U ) is the set of (continuous) sections of p over U . If
F is separated (i.e. Hausdorﬀ ), then F satisﬁes the principle of unique
continuation. The converse also holds if S is separated.
Proof. If F is separated, then for any two sections f,g of p over an open
subset U⊂ S, the set of s∈ U such that f (s) = g(s) is closed. Applying
this to the zero-section g = 0, we see that the support of f is open.
Conversely, letx,y be two points of F . If p(x)⁄=p(y), there are disjoint
open neighborhoods Vx,V y of p(x) and p(y) respectively in the separated
space S; then p−1Vx and p−1Vy are disjoint open neighborhoods of x and y
respectively. If p(x) = p(y), there are open neighborhoods Ux,U y of x and
y respectively, an open subset V ⊂ S, and sections f,g of p over V , such
thatf (V ) = Ux, g(V ) = Uy. By the principle of unique continuation, f⁄=g
deﬁnes an open subset W⊂V containingp(x) = p(y); then f (W ) andg(W )
are disjoint open neighborhoods of x and y respectively.
Deﬁnition 1.1.4. We say that the sheaf F satisﬁes the monodromy prin-
ciple if it has the following property:
1. ANALYTIC CONTINUATION; TOPOLOGICAL POINT OF VIEW. 11
let Γ : [ a,b ]× [0, 1]→ S be any continuous map with Γ( {a}× [0, 1]) =
{xa}, Γ({b}× [0, 1]) ={xb}. Let fxa be an element of the stalk Fxa. Assume
that for any t∈ [0, 1], fxa extends to a global section f Γ t of Γ ∗
tF on [a,b ].
Then this extension is unique and f Γ t(b)∈F xb is independent of t.
In this situation, the section f Γ t of Γ∗
tF is called the continuation of fxa
along the path Γ t, and f Γ t(b)∈F xb its value at xb.
Proposition 1.1.5. IfF satisﬁes the principle of unique continuation, then
it satisﬁes the principle of monodromy. The converse also ho lds if S is locally
arcwise connected.
Proof. Assume thatF satisﬁes the principle of unique continuation. This
guarantees the uniqueness of the continuation f Γ t of fxa along the path Γ t
for any t. Moreover, by a special case of the proper base change theore m
(applied to the ﬁrst projection [ a,b ]× [0, 1]→ [a,b ], cf. [Iv86, IV, 1.4]) f Γ t
extends to a section of Γ ∗F on a suitable subset of the form [a,b ]×(t−ǫ,t +ǫ).
By unicity, these sections glue together to a global section of Γ ∗F. The
restriction of this sheaf to {b}× [0, 1] is the constant sheaf with stalk Fxb.
Therefore the value f Γ t(b)∈F xb is independent of t.
Conversely, let U be an arcwise connected open subset of S, let xa,x b
be two points of U , and let f be a section of F overU . Let γ : [a,b ]→ S
be any path from xa to xb. It follows from the unicity of continuation of
fxa along γ (requested in the monodromy principle) that if fxa is 0, so is
fxb.
Example 1.1.6. (1) Any locally constant abelian sheaf F on a topological
spaceS satisﬁes the principle of unique continuation, hence the pr inciple of
monodromy.
In fact, for any Γ : [ a,b ]× [0, 1]→ S as in Lemma 1.1.3, the inverse
image Γ ∗F is locally constant, hence constant and canonically isomor phic
to the constant sheaf attached to Fxa. Therefore the extension f γ of any
fxa ∈F xa along any path γ exists, and the value at the other extremity
xb =γ(b) depends only on the homotopy class of γ.
(2) When S is a complex manifold, the structure sheaf OS satisﬁes the
principle of unique continuation, hence the principle of mo nodromy.
