---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-020-7-concluding-remarks
section_title: "Concluding remarks"
section_number: 7
pages: 41-43
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
We constructed jet bimodules Jk
A and Jk
E under the assumption of some geometric data on
the diﬀerential algebra ofA and theA-bimoduleE. We also showed that these data a available in
a wide variety of A, including a discrete space (functions on a ﬁnite group Cayley graph), and a
matrix algebra, the enveloping algebras of a solvable Lie algebra (a standard quantum spacetime)
and, perhaps surprisingly, Cq[SL2] at q a fourth root of unity. This also shows in particular
that the class of diﬀerential algebras equipped with a ﬂat torsion free connection, to which the
theory applies, is a rich class of noncommutative geometries. This class also includes fuzzy
R3 (the enveloping algebra U(su2) as ﬂat quantum spacetime relevant to 3D quantum gravity
with its quantum group invariant 4D diﬀerential structure) and the bicrossproduct Minkowski
spacetime (another enveloping algebra of the solvable type in Section 6 but with its quantum
Poincar´ e-invariant 5D diﬀerential structure). These both have an obvious quantum metric and
ﬂat QLC ∇given by zero on the basis, see [4], which one can check meets our requirements for
Theorems 3.6 and 5.9. The proof is similar to the easy case at the start of Section 6 as the
dxµ,θ′basis for the bicrossproduct Minkowski model obey the usual Grassmann exterior algebra
and ∇= 0,σ = ﬂip on the basis. The basis now is not central, but the commutation relations are
suﬃcient to move all coeﬃcients in a tensor to the left so that it suﬃces to check our conditions
on the basis. These are already plenty of examples on which it would be interesting to proceed
to the Anderson double complex and Lagrangian ﬁeld theory in a systematic way, which was so
far lacking. This will be looked at elsewhere.
On the mathematical side, a novel feature of our construction was the use of a braiding σ
obeying the braid relations on A-bimodules to construct the algebra Sσ(Ω1) for the reduced
jet bundle in Section 4.3. Both this and Ω S carry the further structure of a braided-Hopf
algebra. Indeed, given an A-bimodule Ω1 equipped with invertible σ obeying the braid relations
(ignoring the rest of the structure, i.e. what follows applies to any A-bimodule equipped with a
braiding), we have a braided category generated within the monoidal category of A-bimodules
by Ω1. The braiding σ is extended to tensor products of Ω 1 and their direct sums in the usual
way. Within this braided subcategory, we can make the braided shuﬄe algebra Sh (Ω1) (this
is TA(Ω1) = ⊕nΩ1⊗An with product given by the braided binomials as in Corollary 4.5) into a
braided-Hopf algebra with coproduct
∆(ω1⊗/uni22EF⊗ωn) =
n
/summation.disp
k=0
(ω1⊗/uni22EF⊗ωk)⊗(ωk+1⊗/uni22EF⊗ωn)
where the underlines denote the braided Hopf algebra structure and the braided tensor product
relevant to it. The k = 1,n cases should be understood as 1 ⊗id and id ⊗1 respectively. The
counit is zero except on degree 0 where it is the identity map. This is the A-bimodule version
of the construction of the braided shuﬄe algebra Sh (V ) over a ﬁeld in [20]. Our construction
restricts to ΩS making this a braided-Hopf algebra in the same way assuming the braided category
is extended to include such subobjects. Similarly, one can take TA(Ω1) with its tensor product
42 SHAHN MAJID AND FRANCISCO SIM ˜AO
algebra structure, to make it into a braided Hopf algebra by ∆ω =ω⊗A 1+1⊗Aω and counit zero
on ω ∈Ω1. Its extension to ω1⊗/uni22EF⊗ωn is then given by the braided binomials as in the original
construction [16, 19] except that now we work with A-bimodules rather than over a ﬁeld. This is
a dual construction to the ﬁrst one and this time we quotient by ker[n,σ]! as in Section 4.3 to the
algebraSσ(Ω1) which remains a braided-Hopf algebra assuming our braided category is extended
to include such quotients. This amounts to the A-bimodule of the construction of braided-linear
spaces (or Nichols-Woronowicz algebras) in the approach of [16, 19]. In the special case of A a
Hopf algebra, Sσ(Ω1) is a symmetric version of the Woronowicz exterior algebra [25].
These braided-Hopf algebra structures on Ω S and Sσ(Ω1) (classically, and often in general,
they are isomorphic) have a classical meaning as follows. Indeed, classically on a manifold M,
one can think of either of these as sections of the symmetric tensors bundle
SymC∞(M)(Ω1) =C∞
poly(TM )
where functionsφ are polynomial in the ﬁbre direction. In this case the generalised Hopf algebra
structure over C∞(M) merely represents pointwise ﬁbre addition (∆φ)((v,x),(w,x)) =φ((v+
w),x) for (v,x) ∈TxM. The braided linear space partial derivatives appear as interior product
iX for any vector ﬁeld X, extended to symmetric tensors as a derivation, which in function
terms functions amounts to diﬀerentiation in the ﬁbre direction. By contrast, the jet bimodule
action ●k of a ∈C∞(M) for each degree k acts on φ according to derivatives along the base
M, as does the jet prolongation map. This gives some insight into the classical meaning of our
construction in Section 3 and Section 4. The case of Jk
E has a little more structure which can
be similarly developed. This classical meaning of Ω S and Sσ(Ω1) opens up the possibility of
a noncommutative version of Lagrangian mechanics on TM , to be developed elsewhere and to
which the braided-Hopf algebra structure is more relevant.
In terms of further developments of the general jet bundle, there are two key directions that
should be addressed in further work. The ﬁrst, which would be important for physics is how
our constructions interact with ∗-structures needed to ensure unitarity. The natural setting here
would beA a∗-algebra, Ω, d a∗-calculus and∇∗-preserving as in [5, 4]. Another point of interest
is that variational problems as expressed via jet bundles should also relate to geodesics. There is
a parallel theory of quantum geodesics based on more general A-B-bimodule connections (with
B the coordinate algebra of the parameter space) and where the covariance of the generalised
braiding requires (as for us) that it obeys the braid relations. In this context, compatibility with
∗was resolved at least in the presence of a twisted trace [7] and it was also shown how this braid
condition could be naturally relaxed.
The second direction for general development would be to generalise our theory to allow our
background torsion free connection ∇to have curvature. This should be possible given that
the jet bundle theory is somewhat dual to the algebra of diﬀerential operators on a manifold,
as explained in [14]. This is known to be a Hopf algebroid and a quantum version of it was
constructed in the setting of ﬂat bimodule connections in [13], building on the left-module case
treated in [4, Chap 6]. In the latter work it is again useful to have a reference connection, but it
does not need to be ﬂat. We also note that there are contexts where a curvature obstruction can
be absorbed by introducing nonassociativity, for example on the semiclassical theory of quantum
diﬀerential structures. Moreover, ﬂatness of the connection only plays a limited role in our
constructions (to ensure that ∇n lands in the right place in the construction of the prolongation
maps) and is not needed for most of the other results in Section 4 at the tensor algebra level.
For example, one could drop the quantum symmetry restriction altogether and work with the
braided shuﬄe algebra Sh(Ω1) in place of ΩS, albeit this would not then have the right classical
limit. These are some directions for further work suggested by our results.
QUANTUM JET BUNDLES 43
