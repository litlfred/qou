---
doc_id: 1104248094
doc_title: "Hochschild and cyclic homology of quantum groups"
section_id: sec-003-3-quantum-groups
section_title: "Quantum Groups"
section_number: 3
pages: 8-13
source_pdf: 1104248094.pdf
source_sha256: c1fdb4791afcad3b
toc_source: inferred
doc_brief: "Hochschild and cyclic homology of quantum groups — For an arbitrary complex linear semisimple Lie group G, we consider Hopf algebras of the deformations of the formal and algebraic functions on G."
---
later in Sect. 6.
3. Quantum Groups
By quantum group we mean the Hopf algebra (over C[[/z]]) of the formal
deformation of the functions on a group. We will start with a connected, complex,
semi-simple Lie group G and consider the formal deformation of formal functions
Hochschild and Cyclic Homology of Quantum Groups 
489
C
f(G) and algebraic functions C[G], resulting in respectively quantum formal
group C{(G) and quantum algebraic group Cή[G]. The data we need for the formal
deformation is a Poisson Lie group structure on G, which we refer to as the
quasίclassical limit of quantum groups. Dually this is equivalent to specifying a
Lie bialgebra structure on g, the formal deformation of which results in the
quantized universal enveloping algebra Uh(g).
We start with a description of the quasiclassical limit of quantum groups. Much
of what we state here can be found in [12, 28].
Definition (3.1). A Lie group G is called a Poisson Lie Group if it is a Poisson manifold
such that the group multiplication G x G -> G is a Poisson map, where G x G is
equipped with the product Poisson structure. The Poisson structure is specified by
a bivect or field π, the Poisson tensor,
V/, 06C°°(M). 
(3.1)
A map φ:M-+N 
between 
two 
Poisson 
manifolds 
is a Poisson 
map 
if
{Φ*f,Φ*g}M = {f,g}N
Definition (3.2). Let g be a Lie algebra over C, g* iίs dual We say that (g) is a
Lie bialgebra if there is a Lie algebra structure on g* such the map <5:g-> Λ
2g
dual to the Lie bracket [,]: Λ
2g*->g* is a 1-cocycle with the adjoint action of g
on Λ
2g.
The following theorem states the relations between Poisson Lie groups and Lie
bialgebras.
Theorem (3.3). [11]
1) Let G be connected and simply connected, then there is one to one correspondence
between Poisson Lie group structures on G and Lie bialgebra structures on g;
2. Let G be connected and semi-simple, then every Poisson Lie group structure on G
has the following form:
π(g) = lg*R-rg*R, 
(3.2)
where Re Λ
2g^ /\
2TG(e\ #eG, l^ and rg* are push-forward maps of left and right
translations, and R is such that
<#,#>:= [#
12,#
13] + [Λ
12,Λ
23] + [Λ
13,K
23]e Λ
3#
is invariant under adjoint action o/g. 
(3.3)
The corresponding Lie bialgebra (g, δ) is given by
δ(x) = zdx(R\ 
Vxeg, 
(3.4)
where ad is adjoint action. Condition (3.3) ensures the dual map of (3.4) 
satisfies
Jacobi identify.
3. For the Lie bialgebra (g, g*) there is a unique Lie algebra structure on the vector
space g Θ g* such that
(a) g>S* are Lie subalgebras,
(b) The symmetric bilinear form < , ) on g 0 g* given by
<*ι + yι,X2 + ^2) = <xί9y2> + <*2»3>ιX 
Vx 1,x 2eg, and yl9
is invariant.
490 
P. Feng and B. Tsygan
The Lie algebra structure on g φ g* is given by
[x,y] = -adJOO + ad*(x), Vxeg, yeg*, 
(3.5)
where ad* is the coadjoint action. This Lie algebra mil be denoted by g Ng* as in
[28]. (g,g*,g Ng*) is called Manin triple.
We now describe the Lie bialgebras we are going to study. First of all, a few
words about notations.
G is a connected, complex, semi-simple Lie group, g its Lie algebra, K is a
compact real form of G, with Lie algebra k, τ0 the complex conjugation of g with
respect to k, B(,) the Killing form of g, h a Cartan subalgebra of g, Φ the root
system of (g,h), Φ
+ a choice of positive root system. Let g = hφl ©g
α I be the
VαeΦ 
/
root space decomposition of g. For each αeΦ we may choose £αeg
α, and //αeh,
such that [19]
(a)
(b)
(c) [£.,£,] = 0 if α
(d) [Ea,Eβ] = NΛtβEΛ+β if α + /?eΦ, where NΛtβ are non-zero real constants
such that N_ β f_0=-ΛΓ β t0; also Natβ = Nβty = NγtΛ9 whenever α,β,yeΦ,
α + β + y^O;
(e) 
τ0(EΛ)=-E_a,τ0(Ha)=-Ha.
Consider the complexification of g,gc = C(χ)Rg = g©g as R vector space. We
choose the complex structure J on gΘg to be such that J(x,y) = (JQX,J0y\ where
J0 is the complex structure of g. We identify g as a real form of gc:g<=->g®g,
xh->(x,'τ0x). The complex conjugation of gc with respect to g is σ(x9y) = (τ0y,τ0x).
Obviously k φ k c=_> g © g is the compact real form of gc, the corresponding complex
conjugation 
is τ(x, y) = (τ0x, τ0y). 
The Cartan 
involution is 
θ = τσ = στ,
θ(x, y) = (y, x). The Iwasawa decomposition of gc is gc = kc φ ac © nc, where
ac={(x,-x)|xeh}, 
(3.6)
andn± = 0g±α.
α > 0
Let tc = {(x,x)|xeh). Then hc = tc©ac is a Cartan subalgebra of gc. For every
αeΦ(g,h), we have α
1,α
2eΦ(gc,hc), such that
α
1^, -H) = <x
l(H,H) = <x(H)9
α
2(H, -H) = - α
2(H,//) - α(#), 
VHeh. 
(3.7)
Actually gf = C(£α,0), and gf = C(0,£_J. This obviously exhausts all the roots
of (gc, hc). We say the root α
f, i = 1, 2 is positive if and only if α is positive. Φ(gc, ac)
and Φ*(gc,ac) are those of (gc,hc) restricted to ac, they coincide with Φ, Φ
+, but
with multiplicity 2. Note with this choice of Φ
 + (gc, ac), nc corresponds to negative
roots. Let
P= 
Σ 
*; ρ
l= 
Σ 
α''>' = U; pa- 
Σ
 
α; (3.8)
αeΦ
 + (g,h) 
αeΦ
 + (g,h) 
αeΦ
 + (gc,ac)
Hochschild and Cyclic Homology of Quantum Groups 
491
we have natural identification pa = p
1 + p
2, specifically,
pΛ(H, H) = 0, pΛ(H, -H) = 2p(H). 
(3.9)
Lemma (3.4). The bilinear form < , > on gc ^ g 0 g defined by
<(*ι,yι),(*2,}>2)>= &B(xι,x2) -B(yl9y2)) 
(3.10)
identifies a c©n c with k*.
Proof. It is straightforward, we simply give the dual bases. Let αj? j = 1, 2, . . . , rk g,
be the simple roots, bjk = B(H^H^ b^
1 the matrix element of (bjk)~
l. HjyE±Λ,
where α > 0, is a basis for g. The following are the bases of kc and ac © nc, and
they are dual to each other:
kc:
(Hj9Hj)
k9-
(2£_α,0) 
'
 
(*
 
}
(E_ α,E_ α) 
(0,-2£α)
where α > 0.
Lemma (3.5)* The Lie bracket o/g*^a c©n c, [,]:Λ
2g*->g* induces a map
δ:g-+ Λ
2g of the following form:
adx(R), 
Vxeg, 
(3.12)
and
R = * Σ E α Λ E _ α . 
(3.13)
^α>0
The proof is left to the reader. We write down the map δ here:
) = £_ βΛfί β— - 
Σ 
Nβι1E_βΛE_Γ 
(3.14)
2 
2/?,y>0,0 + y = α
where α > 0.
Lemma (3.6). For any xeg = kc c gc, yeg* ^ a cφn c c gc,
[x,y]:=-(adj();)-ady*(x)), 
(3.15)
coincides with the Lie bracket ofgc = k c©a c©n c.
Proposition (3.7).
1) (kc, ac © nc, gc) is a Manin triple',
2) (G, π), π(g) = lg*R — rg*R,for geG, is a Poisson Lie group.
Definition (3.8). A Poisson Hopf algebra is a commutative Hopf algebra with a
compatible Poisson bracket, i.e., {a,bc} = b{a,c} + {a,b}c. We also have the dual
object, co-Poisson Hopf algebra.
492 
p. Feng and B. Tsygan
Theorem (3.9). [11]
1) The Lie bialgebra structure (g,(5) induces a unique co-Poisson Hopf algebra
structure on (7(g);
2) The Poisson Lie group structure (G, π) induces a unique Poisson Hopf algebra
structure on C[G], and on C
f(G); C
f(G) is dual to l/(g).
This gives the quasiclassical limit of our quantum groups.
Definition (3.10). A quantization of Poisson Hopf algebra A0 over C is a Hopf
algebra A over C [[/*]] such that
(a) A/hA = A0 as Hopf algebra over C,
(b) A is a free C[[/z]]-wodw/£,
(c) Vα, be A, (ab — ba)/hmod(h)= (αmod(/ι), ft mod (/z)}, where {,} 
is the
Poisson bracket of AQ.
The notion of quantization of co-Poisson Hopf algebra is similar.
Theorem (3.11). [11] The co-Poisson 
Hopf 
algebra 
(U(g),δ) 
has a unique
quantization UΛ(g).
This is the quantized universal enveloping algebra of Drinfeld and Jimbo
[11,21].
Corollary (3.12). The Poisson Hopf algebra (C
f(G), π) has a unique quantization
Theorem (3.13). The Poisson Hopf algebra (C[G],π) has a quantization Ah[G~\.
Definition (3.14). Let C{(G) be the h-adic completion of A
f
h(G)®C[[h]]C((h)) 
and
Ch[G] the h-adic completion o/^[G]®C[[fj]]C((/0).
See [31, 29, 35] for more discussion of Cft[G]. It is called quantum coordinate
algebra there. For the purpose of this paper we do not need an explicit construction
ofCΛ[G].
Example (3.15). G = SL(2, C), g = s/(2, C).
t/h(g) is a Hopf algebra generated by H,E
+, E~ via
em
=-H, S(£±)=-e
±fΈ±. 
(3.16)
Ch[G] is a Hopf algebra generated by a,b,c,d via
ab = e~
 hba, ac = e~
Hca, db = e
hbd, dc = e
kcd,
Hochschild and Cyclic Homology of Quantum Groups 
493
be = cb, ad-da = (e'
h - e
h)bc, ad - e'
hbc = 1,
4
a i)-( χ ί) 
<
3
 ">
\c d/ 
\c d/ 
\c a)
where " indicates matrix multiplication,
| = α, S(ft)=-Λ, S(c)=-έΓ*c.
