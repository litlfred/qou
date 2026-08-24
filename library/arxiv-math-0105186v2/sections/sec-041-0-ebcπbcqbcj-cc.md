---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-041-0-ebcπbcqbcj-cc
section_title: "(Ebc,πbc,Qbc,J ) : C′−→C′′"
section_number: 0
pages: 65-67
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
is homotopic to c◦b by a chain homotopy which is of order (0;∞).
Proof. Suppose ﬁrst that j is induced from the complex structures on Sb,Sc,
and that J is similarly constructed from J (4) and J (6); this is automatically
horizontal. Proposition 2.22 says that for large values of t he gluing parameter
σ, J is regular; and then we have moreover CΦ 0(Ebc,πbc,Qbc,J ) = c◦b by
(2.30). On the other hand, the observations made above allow us to apply
Lemma 2.30, which shows that the maps CΦ 0 for any two choices of j and J
are homotopic by a chain homotopy of order (0; ∞).
t=
t=
t=
t=
1
-1
-2
0(0,0)
Figure 10:
The proof that c◦b is chain homotopic to zero relies on an alternative con-
struction of the same exact Lefschetz ﬁbration. Consider th e surface So from
Figure 10, embedded into R2 with coordinates ( s,t ). As in the previous sec-
tion, we divide it into So,± = So∩{t∈ R±} and take the trivial ﬁbrations
πo,± :Eo,± =So,±×M→So,±. We equip Eo,± with the forms Ω o,± pulled back
fromω, and Eo,+ with the one-form Θ o,+ pulled back from θ; while on Eo,− we
take Θ o,− =θ−d(η(t)KτL ), where η is some function with η(t) = 1 for t≥− 1,
η(t) = 0 for t≤− 2. One now identiﬁes the ﬁbres over z∈ R−×{0} =So,+∩So,−
by using τL :Eo,+
z →Eo,−
z , which yields an exact symplectic ﬁbration ( Eo,πo)
over So (it is in fact trivial, but for us it is convenient to think of i t as being
built up in this particular way). Take the pieces of ∂So labeled in Figure 11,
and construct a Lagrangian boundary condition Qo for (Eo,πo) as the union
of ∂1So,−×τL(L0), ∂2So,−×L⊂Eo,− and ∂2So,+×L, ∂3So,+×L1⊂Eo,+.
The associated function KQo is equal to KτL(L0)−η(t)KτL|τL(L0) over ∂1So,−,
65
to KL1 over ∂3So,+, and zero on the rest. κQo is equal to −(KτL|L)η′(t)dt
on∂2So,− and vanishes elsewhere; this makes sense because KτL|L is constant,
equal to−2πR(0) by (3.2). Combining this with (V) shows that
∫
∂S o
κQo = 2πR(0)∈ (−ǫ; 0]. (3.11)
Qo is modelled on (τL(L0),L ) and (L,L 1) over the positive ends, and on (L0,L 1)
over the negative end; a suitable trivialization of ( Eo,πo) over that end can be
deﬁned in the same way as in Section 3.3. The next statement is a straightfor-
ward consequence of (I):
Lemma 3.10. Take the subset Uo⊂ So shaded in Figure 11. Then there are
no horizontal sections u :Uo→Eo with u(∂So∩Uo)⊂Qo.
1
o,-S
S3
o,+
o,-S2
o,+S2
Figure 11:
For the following step, we need the ﬁbration ( Ep,πp) overSp = ¯D(1/2) from
Section 3.3, which was deﬁned as pullback of a standard ﬁbrat ion. The stan-
dard boundary condition from Section 2.3 pulls back to a Lagr angian boundary
condition Qp for it. As it stands κQp = dc(− 1
4|z|) is nonzero everywhere, but
for us it is better to modify it by some exact one-form, in such a way that it
becomes zero near −1/2∈∂Sp. This can be compensated by a change of KQp,
so that the whole remains a Lagrangian boundary condition. I t is a consequence
of Proposition 2.13 that the Φ 1-invariant of (Ep,πp,Qp) vanishes, since this can
be joined to (EL,πL,QL) by a smooth deformation of exact Lefschetz ﬁbrations
with Lagrangian boundary conditions.
Lemma 3.11. LetUp⊂Sp be the complement of a suﬃciently small neighbour-
hood of−1/2∈∂Sp. Then there are no partial horizontal sections w :Up→Ep
satisfying w(∂Sp∩Up)⊂Qp.
Proof. From the standard ﬁbration, Ep inherits a smooth family of Lagrangian
spheres Σ p
z⊂Ep
z ,z⁄= 0. These are carried into each other by parallel transport
along any path, and they degenerate to the critical point x0∈Ep
0 asz→ 0. Now
66
our boundary condition is made up of the Σ p
z forz∈∂Sp; therefore a section w
with the properties stated above would satisfy w(z)∈ Σ p
z for all z∈∂Sp∩Up,
and by parallel transport for all z∈Up⁄={0}. In the limit this yields w(0) = x0,
but that is impossible since x0 is a critical point.
One can identify the ﬁbre of Eo overζo = (0, 0)∈∂So with the ﬁbre of Ep
overζp =−1/2∈∂Sp via
(Eo)ζo∼= (Eo,+)(0,0) =M
φp
←−−Ep
1/2
∼= (Ep)ζp (3.12)
where the last isomorphism is parallel transport along the u pper semi-circle
(1/2)eit, 0 ≤ t≤ π. By putting together the various deﬁnitions, one sees that
(3.12) takes (Qo)(0,0) to (Qp)−1/2. The ﬁbrations ( Eo,πo) and (Ep,πp) are ﬂat
near the pointsζo,ζp, and the one-forms κQo,κQp vanish near those points. This
allows one to use the gluing construction discussed in Secti on 2.1 and again in
Section 2.4 to produce an exact Lefschetz ﬁbration ( E,π ) overS =So#ζo∼ζpSp,
together with a Lagrangian boundary condition Q; see Figure 12. Of course,
this is still modelled over the ends on the same Lagrangian su bmanifolds as So.
In what follows, we assume that the parameter ρ in the gluing process has been
chosen suﬃciently small.
Lemma 3.12. There is a complex structure j on S, standard over the ends,
and a J∈ Jreg,h(E,π,Q,j,J (1),J (2),J (5)), such that
CΦ rel
