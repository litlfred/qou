---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-010-34-curvature-2-functors
section_title: "Curvature 2-Functors"
section_number: 3.4
pages: 22-25
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
In this section we provide a class of examples of transport 2-funct ors coming from transport functors,
i.e. ﬁbre bundle with connections. If P is a principal G-bundle with connection ω over M , one can
– 22 –
compare the parallel transport maps along two paths γ1,γ 2 : x /d47/d47 y by an automorphism of Py,
namely the holonomy around the loop γ2 ◦γ−1
1 ,
τγ2 = Holω(γ2 ◦γ−1
1 ) ◦τγ1 .
If the paths γ1 andγ2 are the source and the target of a bigon Σ : γ1 /d43/d51 γ2, this holonomy is related
to the curvature of ∇. So, a principal G-bundle with connection does not only assign ﬁbres Px to
points x ∈ M and parallel transport maps τγ to paths, it also assigns a curvature-related quantity to
bigons Σ.
Under the equivalence between principal G-bundles with connection and transport functors on X
with BG-structure (Theorem 2.4.2), the principal bundle ( P,ω ) corresponds to the transport functor
traP : P1(M ) /d47/d47 G-Tor
that assigns the ﬁbres Px to points x ∈ M and the parallel transport maps τγ to paths γ. Adding an
assignment for bigons yields a “curvature 2-functor”
K(traP ) : P2(M ) /d47/d47 ˆG-Tor
where ˆG-Tor is the category G-Tor regarded as a strict 2-category with a unique 2-morphism bet ween
each pair of 1-morphisms. The uniqueness of the 2-morphisms expr esses the fact that the curvature is
determined by the parallel transport.
More generally, let us start with a transport functor tra : P1(M ) /d47/d47 T with BG-structure for some
Lie group G and some functor i : BG /d47/d47 T . The curvature 2-functor of tra is the strict 2-functor
K(tra) : P2(M ) /d47/d47 ˆT
which is on objects and 1-morphisms equal to tra and on 2-morphism s determined by the fact that ˆT
has a exactly one 2-morphism between each pair of 1-morphisms. In the same way, we obtain a strict
2-functor
K(i) :ˆBG /d47/d47 ˆT
We observe that the Lie 2-groupoids ˆBG and BEG (see Section 3.3) are canonically isomorphic under
the assignment
∗
g1
/d27/d27
g2
/d67/d67∗
/d11/d19
∗ ✤ /d47/d47 ∗
g1
/d27/d27
g2
/d66/d66g2g−1
1
/d11/d19
∗,
so that we obtain a 2-functor BEG /d47/d47 ˆBG /d47/d47 ˆT . Now we are in the position to introduce our
explicit example of a transport 2-functor.
Theorem 3.4.1. The curvature 2-functor K(tra) is a transport 2-functor with BEG-structure.
Proof. We construct a local trivialization of K(tra) starting with a local trivialization (triv ,t ) of
tra with respect to some surjective submersion π : Y /d47/d47 M . Let dtriv : P2(Y ) /d47/d47 BEG be the
derivative 2-functor associated to triv [SW11]: on objects and 1- morphisms it is given by triv, and it
sends every bigon Σ : γ1 /d43/d51 γ2 inY to the unique 2-morphism in BEG between the images of γ1 and
γ2 under triv. A pseudonatural equivalence
K(t) : π∗K(tra) /d47/d47 K(i) ◦ dtriv
– 23 –
is deﬁned as follows. Its component at a point a ∈ Y is the 1-morphism
K(t)(a) := t(a) : tra(π(a)) /d47/d47 i(∗)
in T . Its component t(γ) at a path γ :a /d47/d47 b is the unique 2-morphism in ˆT . Notice that since t is
a natural transformation, we have a commutative diagram
tra(π(a))
tra(π(γ)) /d47/d47
t(a)
/d15/d15
tra(π(b))
t(b)
/d15/d15
i(∗)
trivi(γ)
/d47/d47i(∗)
meaning that t(γ) = id. This deﬁnes the pseudonatural transformation t as required.
Now we assume that the descent data (triv ,gt) associated to the local trivialization (triv ,t ) is
smooth, and show that then also the descent object (dtriv ,gK(t),ψ,f ) is smooth. As observed in
[SW11], the derivative 2-functor dtriv is smooth if and only if triv is smo oth. To extract the remaining
descent data according to the procedure described in Section 2.2. It turns out that the only non-trivial
descent datum is the pseudonatural transformation
gK(t) :π∗
1 dtrivK(i) /d47/d47 π∗
2 dtrivK(i).
Its component at a point α ∈ Y [2] is given by gK(t)(α) := gt(α), and its component at some path
Θ : α /d47/d47 α′ is the identity.
The last step is to show that
F (gK(t)) : P1(Y [2]) /d47/d47 ΛK(i)ˆT
is a transport functor with Λ BEG-structure. To do so we have to ﬁnd a local trivialization with smooth
descent data. This is here particulary simple: the functor F (gK(t)) is globally trivial in the sense that
it factors through the functor
ΛK(i) : Λ BEG /d47/d47 ΛK(i)ˆT .
To see this we use the smoothness condition on the natural transf ormation gt, namely that it factors
through a smooth natural transformation ˜ gt. We obtain a smooth pseudonatural transformation
˜gK(t) :π∗
1 dtriv /d47/d47 π∗
2 dtriv such that gK(t) =K(i)(˜gK(t)). This ﬁnally gives us
F (gK(t)) = Λ K(i) ◦ F (˜gK(t))
meaning that F (gK(t)) is a transport functor with Λ BEG-structure. □
Since the value of the curvature 2-functor K(tra) on bigons does not depend on the bigon itself
but only on its source and target path, we have the following.
Proposition 3.4.2. The curvature 2-functor K(tra) of any transport functor is ﬂat.
This proposition gains a very nice interpretation when we relate the c urvature of a connection ω in
a principal G-bundlep :P /d47/d47 M to the curvature 2-functor K(traP ) associated to the corresponding
transport functor tra P . First we show:
Lemma 3.4.3. The curvature 2-functor K(traP ) : P2(M ) /d47/d47 ˆG-Tor has a canonical smooth p-local
trivialization (p,t, triv). The classical curvature curv(ω) ∈ Ω 2(P, g) is the 2-curving of K(traP ) with
respect to the trivialization (p,t, triv).
– 24 –
Proof. As described in detail in [SW09, Section 5.1], tra P admits local trivializations with respect to
the surjective submersionp :P /d47/d47 M and with smooth descent data (triv ′,g ) such that the connection
1-form ω ∈ Ω 1(P, g) of the bundle P corresponds to the smooth functor triv ′ : P1(P ) /d47/d47 BG under
the bijection of [SW09, Proposition 4.7]. Then, by [SW11, Lemma 3.5], th e 2-form B′ associated to
dtriv′ under the bijection (3.3.1), which is by Deﬁnition 3.3.5 (i) the 2-curving ofK(traP ), is given by
B′ = dω + [ω ∧ω].
The latter is by deﬁnition the curvature of the connection ω. □
The announced interpretation of Proposition 3.4.2 now is as follows: u sing Lemma 3.4.3 one can
calculate the curvature curv(K(traP )) of the curvature 2-functor of tra P . The calculation involves the
second Bianchi identity for the connection ω on the principal G-bundle P , and the result is
curv(K(traP )) = 0,
which is according to Proposition 3.3.6 an independent proof of Propo sition 3.4.2. In other words,
Proposition 3.4.2 is equivalent to the second Bianchi identity for connections on ﬁbre bundles.
