---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-009-321-methods
section_title: "Methods"
section_number: 3.2.1
pages: 18-21
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
The problem of quantization can be approached in many diﬀerent ways. Each approach
has its advantages and disadvantages, but in the end all methods are expected to yield
the same result. The classic approach of geometric quantization (cf. [31]) starts by
deﬁning a prequantum line bundle L→M with a unitary connection of curvature 1
ℏω.
Note that such a line bundle only exists for
1
2πℏω∈H2(M; Z), (3.15)
9There is an ambiguity in choosing θ, directly related to the choice of coordinates of M (positions
versus momenta) that elements ofH are to depend on.
17
which can lead to a quantization of ℏ−1 (i.e. a restriction of ℏ to a discrete set of values
in C∗). The local choice of “position” versus “momentum” coordinates is encoded in
the choice of a set of 1
2 dimRM vector ﬁeldsPj, called a polarization, and the Hilbert
spaceH is then deﬁned as the set of square-integrable,Pj-invariant sections ofL. This
gives a very concrete deﬁnition of H, although it can be very hard to show that the
construction is independent of the choice of polarization. (The problem becomes more
manageable ifM is K¨ ahler.) Moreover, it is often diﬃcult in geometric quantization
to ﬁnd the full quantum expressions for operators Ofi.
An alternative, deformation quantization [32] partially solves this latter problem.
It describes a formal ℏ-deformation of the ring of functions onM, using a noncommu-
tative product of the type
f ⋆ℏg = fg + ℏ
∑
i,j
αij∂i(f)∂j(g) + ℏ2
2
∑
i,j,k,l
αijαkl∂i∂k(f)∂j∂l(g)
+ ℏ2
3
(∑
i,j,k,l
αij∂j(αkl)(∂i∂k(f)∂l(g)−∂k(f)∂i∂l(g))
)
+..., (3.16)
whereα =ω−1 is the Poisson structure corresponding to the symplectic formω. In local
coordinates{f,g} = αij∂i(f)∂j(g). One important advantage of deformation quanti-
zation is that it is completely canonical and does not require any auxiliary choices. In
particular, there is an explicit formula for the⋆ℏ-product (3.16) due to Kontsevich [33],
that allows one to express it as a sum over admissible graphs,
f ⋆ℏg :=
∞∑
n=0
ℏn
∑
graphs Γ
of order n
w(Γ)BΓ(f,g ), (3.17)
where w(Γ) is a weight (number) assigned to Γ, and BΓ(f,g ) are bilinear diﬀerential
operators whose coeﬃcients are diﬀerential polynomials, homogeneous of degree n in
the components of the bivector ﬁeld α onM. By deﬁnition, an admissible graph of
order n is an ordered pair of maps i,j :{1,...,n }→{ 1,...,n,L,R } where neither
map has ﬁxed points and both maps are distinct at every point. There are nn(n + 1)n
such graphs.
For example, the graph of order 2 corresponding to the ﬁrst term in the second line
of eq. (3.16) has 4 vertices and 4 edges:
Γ =
RL
1 2
j
i
ji
1
1
2 2
i1 = (1, 2)
j1 = (1,L )
i2 = (2,L )
j2 = (2,R )
(3.18)
18
An example of a more complicated admissible graph (of order 4) is shown on Figure 5.
The corresponding bidiﬀerential operator is
BΓ(f,g ) =
∑
αi4j4(∂i3αi1j1)(∂j1∂j4αi2j2)(∂i2∂i4αi3j3)(∂i1∂j3f)(∂j2g). (3.19)
When the Poisson structure is ﬂat, a graph with an edge ending in a vertex other
thanL orR will have zero contribution to the sum (3.17), since it will involve derivatives
of α. In this case the ⋆ℏ-product (3.17) becomes the usual Moyal product
f ⋆ℏg(x) = exp
(
ℏαij ∂
∂xi
∂
∂yj
)
f(x)g(y)|y=x (3.20)
i2
L R
2
4
3
1
i
j1
i
i
j
j j
4
4
3
3 2
1
Figure 5: An example of an admissible graph of order 4.
Deformation quantization is a powerful method for ﬁnding the operators Ofi. It
is important to stress, however, that, by itself, it does not explain how to construct
the spaceH (it is not an honest quantization), and can not capture the fact that ℏ−1
should ever be discretized.
A third option, brane quantization [34], is a marriage of geometric and deformation
quantizations in a physical context. It approaches the problem of quantization by
complexifyingM and ω, and constructing a certain (secondary) topological quantum
ﬁeld theory on the resulting space MC. It has the advantage of easily characterizing
the various choices that one must make in quantization, and provides simple geometric
criteria that describe quantizable (M,ω ; ℏ). In this approach, the Hilbert space H is
constructed as the space of morphisms (space of open strings),
H = Hom(Bcc,B′), (3.21)
whereBcc andB′ are objects (branes) of a certain category associated to the symplectic
manifoldMC. Moreover, in this approach, independence ofH on various choices can be
reformulated as a problem of constructing a ﬂat connection on the space of such choices,
19
which identiﬁes the space of ground states in the secondary TQFT. In a closely related
context, this problem has been studied in the mathematical physics literature [35, 36],
and leads to a beautiful story that involves integrable systems and tt∗ equations.
