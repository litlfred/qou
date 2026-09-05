---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-004-crossed-modules
section_title: "Crossed modules"
section_number: null
pages: 9-11
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
All Lie groups and Lie algebras are taken to be ﬁnite-dimensional.
Deﬁnition 3 (Lie crossed module) A crossed module G = (∂ : E →G,⊲ ) is
given by a group morphism ∂ : E →G together with a left action ⊲ of G on E
by automorphisms, such that:
1. ∂(X⊲e ) = X∂ (e)X −1; ∀X ∈G, ∀e ∈E,
2. ∂(e)⊲f =efe −1; ∀e,f ∈E.
If both G and E are Lie groups, ∂ :E →G is a smooth morphism, and the left
action of G on E is smooth then G will be called a Lie crossed module.
A morphism G → G ′ between the crossed modules G = (∂ : E →G,⊲ ) and
G′ = (∂′ : E′ → G′,⊲ ′) is given by a pair of maps φ : G → G′ and ψ : E → E′
making the diagram:
E
∂
− − − − →G
ψ
↓
↓φ
E′ ∂′
− − − − →G′
commutative. In addition we must have ψ(X⊲e ) = φ(X)⊲′ψ(e) for each e ∈E
and each X ∈G.
Given a Lie crossed module G = (∂ : E →G,⊲ ), then the induced Lie algebra
map ∂ : e → g, together with the derived action of g on e (also denoted by ⊲)
is a diﬀerential crossed module, in the sense of the following deﬁnition - see
[BS, B, BC].
Deﬁnition 4 (Diﬀerential crossed module) A diﬀerential crossed module,
say G = (∂ : e → g,⊲ ), is given by a Lie algebra morphism ∂ : e → g together
with a left action of g on the underlying vector space of e, such that:
1. For any X ∈ g the map e ∈ e ↦→X ⊲e ∈ e is a derivation of e, in other
words
X⊲ [e,f ] = [X⊲e,f ] + [e,X⊲f ]; ∀X ∈ g, ∀e,f ∈ e.
2. The map g → Der(e) from g into the derivation algebra of e induced by
the action of g on e is a Lie algebra morphism. In other words:
[X,Y ]⊲e =X⊲ (Y ⊲e) −Y ⊲(X ⊲e); ∀X,Y ∈ g, ∀e ∈ e.
3. ∂(X⊲e ) = [X,∂ (e)]; ∀X ∈ g, ∀e ∈ e.
4. ∂(e)⊲f = [e,f ]; ∀e,f ∈ e.
9
Note that the map ( X,e ) ∈ g × e ↦→X⊲e ∈ e is necessarily bilinear.
Therefore, given a diﬀerential crossed module, G = (∂ : e → g,⊲ ) there exists
a unique crossed module of simply connected Lie groups G = (∂ : E →G,⊲ )
whose diﬀerential form is G, up to isomorphism. The proof of this result is
standard Lie theory, together with the lift of the Lie algebra action to a Lie
group action, which can be found in [K], Thm 1.102.
Example 5 LetG be a Lie group with a left action ⊲ on an abelian group V by
automorphisms, for example take V to be any representation of G on a vector
space. If we put ∂ = 1 G then (∂ : V → G,⊲ ) is a Lie crossed module. Its
diﬀerential form is given by the derived action of g on V and the zero map
V → g.
Example 6 LetG be any Lie group. Let Ad denote the adjoint action of G on
G. Then (id :G →G, Ad) is a Lie crossed module.
Example 7 LetG and E be Lie groups, and let ∂ : E →G be a surjective map
such that ker(∂) is central in E. Deﬁne a left action of G onE asg⊲e =g0eg−1
0 ,
whereg0 ∈E is such that ∂(g0) = g ∈G, and e ∈E. Then G = (∂ : E →G,⊲ )
is a Lie crossed module.
Example 8 In the previous example, we can take the universal covering m ap
SU(2) → SO(3), whose kernel is {±1}. The diﬀerential form of this crossed
module is given by the adjoint action of su(2) on su(2) and the identity map.
Example 9 More generally, take the universal cover ∂ : E → G of the Lie
groupG. Then the construction in example 7 can be applied since the k ernel of
∂ is necessarily central in E.
Example 10 LetH be the group of upper triangular matrices in R which only
have 1’s in the main diagonal. Deﬁne a Lie group map ∂ : H → R2 as
∂


1 a b
0 1 c
0 0 1

 = (a,c ),
wherea,b,c ∈ R. Then the kernel of ∂ : H → R2 is central in H, and therefore
the construction in example 7 can be applied.
Example 11 Let E be any Lie group. Let Aut(E) be the group of automor-
phisms of E. Then Aut(E) is a Lie group, in fact it is a Lie subgroup of GL(e) if
E is simply connected. Consider the map Ad :E → Aut(E) that sends e ∈E to
the automorphism Ad(e) :E →E. The group Aut(E) acts on E asφ⊲e =φ(e)
where φ ∈ Aut(E) and e ∈ E. Then (Ad :E → Aut(E),⊲ ) is a Lie crossed
module.
The previous construction yields several examples of Lie crossed m odules. For
instance, example 8 is obtained this way since Aut(SU(2)) = SO(3). T o get new
examples, however, we need to consider non-semisimple Lie groups.
10
Example 12 In example 11, take E =H, the group of upper triangular 3 × 3
matrices in R, which only have 1’s in the main diagonal. Then the crossed
module (Ad :H → Aut(H),⊲ ) is highly non-trivial. In fact, Ad(E) is isomorphic
to R2, whereas the cokernel Out(E) of Ad is isomorphic to GL(2, R), see [KH].
The kernel of Ad is a central subgroup of H isomorphic to R; see example 10.
