---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-026-the-dependence-of-a-categorical-connection-holon
section_title: "The dependence of a categorical connection holonomy on the elements of the fibre"
section_number: null
pages: 39-41
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
elements of the ﬁbre
Choose u,v ∈P . We want to relate F(ω,m,u) with F(ω,m,v). Suppose ﬁrst that
u,v each belong to the ﬁbre Px of P at a certain point x ∈ M . Let g ∈ G be
the unique element such that u = vg. Let γ be a 1-path of M starting and
ending at x. Then Hω(γ, 1,u ) = Hω(γ, 1,vg ) = Hω(γ, 1,v )g. Therefore since
Hω(γ, 1,u )F 1
(ω,u)(γ) = u and Hω(γ, 1,v )F 1
(ω,v)(γ) = v we have the well-known
formula:
F 1
(ω,v)(γ) = gF 1
(ω,u)(γ)g−1, (31)
forγ a smooth curve starting and ending at x andu =vg, where u,v ∈Px and
g ∈G.
Let us now see how F 2
(m,ω,u) is related to F 2
(m,ω,v).
Lemma 45 For any 2-path Γ in M , with ∂l(Γ) = ∂r(Γ) = x, we have:
F 2
(ω,m,v)(Γ) = g⊲F 2
(ω,m,u)(Γ), (32)
whereu,v belong to the ﬁbre Px of P , and g ∈G is such that u =vg.
Proof. As usual, put Γ( t,s ) = γs(t);s,t ∈ [0, 1]. LeteΓ (s) and fΓ (s) be deﬁned
by the diﬀerential equations:
d
dseΓ (s) = eΓ (s)
∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt,
and
d
dsfΓ (s) = fΓ (s)
∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,v)
dt;
39
with initial conditions eΓ (0),f Γ (0) = 1E; see equation 19. Then:
d
dsg−1⊲f Γ (s) = g−1⊲ d
dsfΓ (s)
=g−1⊲
(
fΓ (s)
∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,v)
dt
)
=
(
g−1⊲f Γ (s)
) (
g−1⊲
∫ 1
0
m
( ~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,v)
dt
)
=
(
g−1⊲f Γ (s)
) ∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,ug−1)g
dt
=
(
g−1⊲f Γ (s)
) ∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,u)
dt.
The fourth equation follows from (30). Therefore g−1⊲f Γ (s) = eΓ (s), for each
s ∈ [0, 1], thus, in particular, F 2
(ω,m,v)(Γ) = g⊲F 2
(ω,m,u)(Γ).
There is a natural left action of G onG⋉E, given byg⊲ (h,e ) = (ghg −1,g⊲e ).
Using this, we can summarise the results of this subsection, equatio ns (31) and
(32), in the following:
Theorem 46 If v ∈Px then
F(ω,m,vg ) =g−1⊲F (ω,m,v) (33)
for any g ∈G.
2.5.2 The dependence of a categorical connection holonomy o n the
point in the principal bundle
Let G = (∂ : E →G,⊲ ) be a Lie crossed module. Fix a smooth manifold M ,
and a smooth principal G-bundle P →M with a connection ω ∈ A1(P, g). Let
(ω,m ) be a G-categorical connection on P . Let x,y ∈ M . Choose v ∈ Py.
Let µ be a 1-path connecting y with x. This curve µ deﬁnes a categorical
group isomorphismTµ : P2(M,y ) → P 2(M,x ) in the obvious way, by considering
horizontal compositions. More precisely let Γ µ be the 2-path such that Γµ(t,s ) =
µ(t); ∀s,t ∈ [0, 1]. Let also Γ µ−1 (t,s ) = µ−1(t); ∀s,t ∈ [0, 1]. Then Tµ([Γ]) .=
[Γµ−1 ] ◦h [Γ] ◦h [Γµ] ∈ P2(M,x ) for each [Γ] ∈ P2(M,y ), and Tµ([γ]) = [µ−1γµ]
for [µ] ∈π1
1(M,y ).
Theorem 47 Letu = Hω(µ, 1,v ). We have:
F(ω,m,v) =F(ω,m,u) ◦Tµ. (34)
Proof. Let [Γ] ∈ P2(M,y ). Then [Γ] = [Γ µ] ◦h Tµ([Γ]) ◦h [Γµ−1]. Let Γ 1 =
Γµ ◦h Γµ−1 ◦h Γ ◦h Γµ ◦h Γµ−1, thus [Γ 1] = [Γ]. Put γs(t) = Γ 1(t,s ); ∀s,t ∈ [0, 1].
40
Let also Γ ′ = Γµ−1 ◦h Γ ◦h Γµ, thus [Γ ′] = Tµ[Γ]. Putγ′
s(t) = Γ ′(t,s ); ∀s,t ∈ [0, 1].
We have
d
dseΓ 1(s) = eΓ 1(s)
∫ 1
0
m
(
~∂
∂tγs(t),
~∂
∂sγs(t)
)
Hω (γs,t,v)
dt
=eΓ 1(s)
∫ 1
0
m
( ~∂
∂tγ′s(t),
~∂
∂sγ′s(t)
)
Hω (γ′s,t,Hω (µ,1,v))
dt
=eΓ 1(s)
∫ 1
0
m
( ~∂
∂tγ′s(t),
~∂
∂sγ′s(t)
)
Hω (γ′s,t,u)
dt
The second equation follows since Γ µ(s,t ) does not depend on s. Comparing
with equation 19 it follows that eΓ 1(s) = eΓ ′ (s), for each s ∈ [0, 1]. Therefore:
F 2
(ω,m,v)([Γ]) = F 2
(ω,m,v)([Γ 1]) = eΓ 1 =eΓ ′ =F 2
(ω,m,u)([Γ ′]) = F 2
(ω,m,u)(Tµ([Γ])).
This ﬁnishes the proof of the result at the level of the elements of P2(M,y ).
The proof at the level of the elements of π1
1(M,y ) is similar.
