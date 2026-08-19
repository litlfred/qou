---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-012-51-gauge-transformations
section_title: "Gauge Transformations"
section_number: 5.1
pages: 44-46
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
or nontrivial 2-bundles. Now it is time to begin correcting these over sights.
5.1 Gauge Transformations
First consider ordinary gauge theory. Suppose that M is a manifold and G is
a Lie group. Then a gauge transformation on the trivial principal G-bundle
over M simply amounts to a smooth function
g: M → G,
while a connection on this bundle can be seen as a g-valued 1-form. A gauge
transformation g acts on a connection A to give a new connection A′ as follows:
A′ = gAg −1 + g dg−1.
This formula makes literal sense if G is a group of matrices: then g also consists
of matrices, so we can freely multiply elements of G with elements of g. If G
is an arbitrary Lie group the formula requires a bit more careful inte rpretation,
but it still makes sense. A well-known calculation says the curvature F ′ =
dA′ + A′ ∧ A′ of the gauge-transformed connection is just the curvature of t he
original connection conjugated by g:
F ′ = gF g−1.
In higher gauge theory the formulas are similar, but a bit more complic ated.
Suppose M is a manifold and G is a Lie 2-group with crossed module ( G, H, t, α).
It will be helpful to take everything in this crossed module and diﬀere ntiate it.
Doing this, we get:
• the Lie algebra g of G,
• the Lie algebra h of H,
• the Lie algebra homomorphism t
: h → g obtained by diﬀerentiating t: H →
G, and
• the Lie algebra homomorphism α: g → aut(H) obtained by diﬀerentiating
α: G → Aut(H).
44
Here aut(H) is the Lie algebra of Aut( H). It is best to think of this as the Lie
algebra of derivations of h: that is, linear maps D: h → h such that
D[x, y] = [ Dx, y] + [x, Dy].
If we diﬀerentiate the two equations in the deﬁnition of a crossed mo dule, we
obtain the g-equivariance of t:
t(α(x)(y)) = [ x, t(y)]
and the inﬁnitesimal Peiﬀer identity :
α(t(y))(y′) = [ y, y′]
where x ∈ g and y, y′ ∈ h. In case the reader is curious: we write t and α instead
of dt and dα because later we will do computations involving these maps and
also diﬀerential forms, where d stands for the exterior derivatve.
A quadruple ( g, h, t, α) of Lie algebras and homomorphisms obeying these
two equations is called an inﬁnitesimal crossed module . Just as crossed
modules are a way of working with 2-groups, inﬁnitesimal crossed mo dules are
a way of working with Lie 2-algebras [7]. Any inﬁnitesimal crossed modu le
comes from a Lie 2-group, and this Lie 2-group is unique if we demand t hat G
and H be connected and simply connected.
But we digress! We have introduced inﬁnitesimal crossed modules in o rder to
say how gauge transformations act on 2-connections. A gauge transformation
of the trivial G-2-bundle over M consists of two pieces of data:
• a smooth function g: M → G,
• an h-valued 1-form a on M .
Why two pieces of data? Perhaps this should not be so surprising. Remember ,
a 2-connection also consists of two pieces of data:
• a g-valued 1-form A on M ,
• an h-valued 2-form B on M satisfying t(B) = F .
Breen and Messing [30] worked out how gauge transformations act on connec-
tions on nonabelian gerbes, and their work was later generalized to 2 -connections
on arbitrary principal 2-bundles [16, 88]. Here we merely present th e formulas.
A gauge transformation ( g, a) acts on a 2-connection ( A, B) to give a new 2-
connection ( A′, B′) as follows:
A′ = gAg −1 + g dg−1 + t(a)
B′ = α(g)(B) + α(A′) ∧ a + da − a ∧ a
The second formula requires a bit of explanation. In the ﬁrst term w e compose
α: G → Aut(H) with g: M → G and obtain an Aut( H)-valued function α(g),
45
which then acts on the h-valued 2-form B to give a new h-valued 2-form α(g)(B).
In the second term we start by composing A′ with α to obtain an aut(H)-valued
1-form α(A′). Then we wedge this with a, letting aut(H) act on h as part of
this process, and obtain an h-valued 2-form.
As a kind of consistency check and test of our understanding, let u s see
why the gauge-transformed 2-connection ( A′, B′) satisﬁes the equation t(B′) =
