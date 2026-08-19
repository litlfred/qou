---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-009-44-inner-automorphism-2-groups
section_title: "Inner Automorphism 2-Groups"
section_number: 4.4
pages: 37-40
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
There is also a Lie 2-group where:
• G is any Lie group,
• H = G,
• t is the identity map,
• α is conjugation:
α(g)h = ghg −1.
Following Roberts and Schreiber [79] we call this the inner automorphism
2-group of G, and denote it by IN N (G). We explain this terminology in the
next section.
A 2-connection on the trivial IN N (G)-2-bundle over a manifold consists of
a g-valued 1-form A and a g-valued 2-form B such that
B = F
since t
is now the identity. Intriguingly, 2-connections of this sort show up as
solutions of a slight variant of 4d BF theory. In a move that he later called his
biggest blunder, Einstein took general relativity and threw an extr a term into
the equations: a ‘cosmological constant’ term, which gives the vac uum nonzero
energy. We can do the same for topological gravity, or indeed 4d BF theory for
any group G. After all, what counts as a blunder for Einstein might count as a
good idea for lesser mortals such as ourselves.
So, ﬁx a 4-dimensional oriented manifold M as our spacetime. As in ordinary
BF theory, take the ﬁelds to be a connection A on the trivial principal G-bundle
over M , together with a g-valued 2-form B. The action for BF theory ‘with
cosmological constant’ is deﬁned to be
S(A, B) =
∫
M
tr(B ∧ F − λ
2 B ∧ B).
37
Setting the variation of the action equal to zero, we obtain these ﬁ eld equations:
dB + [A, B] = 0 , F = λB.
When λ = 0, these are just the equations we saw in the previous section. Bu t
let us consider the case λ ⁄= 0. Then these equations have a drastically diﬀerent
character! The Bianchi identity dF + [ A, F ] = 0, together with F = λB,
automatically implies that dB + [A, B] = 0. So, to get a solution of this theory
we simply take any connection A, compute its curvature F and set B = F/λ.
This may seem boring: a ﬁeld theory where any connection is a solution .
But in fact it has an interesting relation to higher gauge theory. To s ee this,
it helps to change variables and work with the ﬁeld β = λB. Then the ﬁeld
equations become
dβ + [A, β] = 0 , F = β.
Any solution of these equations gives a 2-connection on the trivial p rincipal
IN N (G)-2-bundle over M !
There is also a tantalizing relation to the cosmological constant in gen eral
relativity. If the B ﬁeld arises from a cotetrad as explained in the previous
section:
B = e ∧ e,
then the above action becomes
S =
∫
M
tr(e ∧ e ∧ F − λ
2 e ∧ e ∧ e ∧ e).
When we choose the bilinear form ‘tr’ correctly, this is the action for general
relativity with a cosmological constant proportional to λ.
There is some evidence [4] that BF theory with nonzero cosmological con-
stant can be quantized to obtain the so-called Crane–Yetter mode l [35, 37],
which is a spin foam model based on the category of representation s of the
quantum group associated to G. Indeed, in some circles this is taken almost
as an article of faith. But a rigorous argument, or even a fully convin cing
argument, seems to be missing. So, this issue deserves more study .
The λ → 0 limit of BF theory is fascinating but highly singular, since for
λ ⁄= 0 a solution is just a connection A, while for λ = 0 a solution is a ﬂat
connection A together with a B ﬁeld such that dB + [ A, B] = 0. At least
in some rough intuitive sense, as λ → 0 the group H in the crossed module
corresponding to IN N (G) ‘expands and ﬂattens out’ from the group G to its
tangent space g. Thus, IN N (G) degenerates to the tangent 2-group T G. It
would be nice to make this precise using a 2-group version of the theo ry of group
contractions.
4.5 Automorphism 2-Groups
The inner automorphism group of the previous section is closely relat ed to the
automorphism 2-group AU T (H), deﬁned using the crossed module where:
38
• G = Aut(H),
• H is any Lie group,
• t: H → Aut(H) sends any group element to the operation of conjugating
by that element,
• α: Aut(H) → Aut(H) is the identity.
We use the term ‘automorphism 2-group’ because AU T (H) really is the 2-group
of symmetries of H. Lie groups form a 2-category, any object in a 2-category
has a 2-group of symmetries, and the 2-group of symmetries of H is naturally
a Lie 2-group, which is none other than AU T (H). See [13] for details.
A principal AU T (H)-2-bundle is usually called a nonabelian gerbe [28].
Nonabelian gerbes are a major test case for ideas in higher gauge th eory. Indeed,
almost the whole formalism of 2-connections was worked out ﬁrst fo r nonabelian
gerbes by Breen and Messing [30]. The one aspect they did not cons ider is the
one we have focused on here: parallel transport. Thus, they did n ot impose the
equation t(B) = F , which we need to obtain holonomies satisfying the conditions
of Theorem 3. Nonetheless, the quantity F − t(B) plays an important role in
Breen and Messing’s formalism: they call it the fake curvature. Generalizing
their ideas slightly, for any Lie 2-group G, we may deﬁne a connection on a
trivial principal G-2-bundle to be a pair consisting of a g-valued 1-form A and
an h-valued 2-form. A 2-connection is then a connection with vanishing f ake
curvature.
The relation between the automorphism 2-group and the inner auto mor-
phism 2-group is nicely explained in the work of Roberts and Schreiber [79]. As
they discuss, for any group G there is an exact sequence of 2-groups
1 → Z (G) → IN N (G) → AU T (G) → OU T (G) → 1
where Z(G) is the center of G and OU T (G) is the group of outer automorphisms
of G, both regarded as 2-groups with only identity 2-morphisms.
Roberts and Schreiber go on to consider an analogous sequence of 3-groups
constructed starting from a 2-group. Among these, the ‘inner au tomorphism
3-group’ IN N (G) of a 2-group G plays a special role [86]. The reason is that
any connection on a principal G-2-bundle, not necessarily obeying t(B) = F ,
gives a ﬂat 3-connection on a principal IN N (G)-3-bundle! This in turn allows
us to deﬁne a version of parallel transport for particles, strings and 2-branes .
This may give a way to understand general relativity in terms of highe r gauge
theory. As we have already seen in Section 4.3, Palatini gravity in 4d s pacetime
involves an so(3, 1)-valued 1-form A and an so(3, 1)-valued 2-form B = e ∧ e.
This is precisely the data we expect for a connection on a principal G-2-bundle
where G is the tangent 2-group of the Lorentz group. Typically this connec tion
fails to obey the equation t(B) = F . So, it is not a 2-connection. But, it gives a
ﬂat 3-connection on an IN N (T SO(3, 1))-3-bundle. So, we may optimistically
call IN N (T SO(3, 1)) the gravity 3-group .
39
Does the gravity 3-group actually shed any light on general relativit y? The
work of Martins and Picken [70] establishes a useful framework for studying
these issues. They deﬁne a path 3-groupoid P3(M ) for a smooth manifold M .
Given a Lie 3-group G, they describe 3-connections on the trivial G-3-bundle
over M as 3-functors
hol: P3(M ) → G
Moreover, they show how to construct these functors from a 1- form, a 2-form,
and a 3-form taking values in three Lie algebras associated to G. In the case
where G = IN N (T SO(3, 1)) and hol is a ﬂat 3-connection, this data reduces
to an so(3, 1)-valued 1-form A and an so(3, 1)-valued 2-form B.
