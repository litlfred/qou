---
doc_id: lee-vanderveen-colored-jones-polynomials-without-tails
doc_title: "COLORED JONES POLYNOMIALS WITHOUT TAILS"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: lee-vanderveen-colored-jones-polynomials-without-tails.pdf
source_sha256: fcc45aebd34e25dc
toc_source: undetermined
doc_brief: "COLORED JONES POLYNOMIALS WITHOUT TAILS — We exhibit an inﬁnite family of knots with the property that the ﬁrst coeﬃcient of the n-colored Jones polynomial grows linearly with n."
---
COLORED JONES POLYNOMIALS WITHOUT TAILS
The colored Jones polynomial of any KTG can now be deﬁned by the following three equations.
(1)
⟨F e
±(Γ), σ⟩= f(σ(e))±1⟨Γ, σ⟩
Here F e
±(Γ) means the result after applying framing change to edge e of the KTG Γ.
(2)
⟨U e(Γ), σ′⟩= ⟨Γ, σ⟩
X
σ(e)
Oσ(e)
θ(σ(e), σ(b), σ(d))
The two colorings σ and σ′ agree on all edges except that U e(Γ) does not have edge e. The four edges
in Γ adjacent to e must have the same colors as b and d in U e(Γ). Also, the summation is over all
possible values of color of the missing edge σ(e). Most values yield zero because the factorials vanish.
The only values that may be non-zero are when σ(e) is between |σ′(b) −σ′(d)| and σ′(b) + σ′(d) and
has the same parity. Finally,
(3)
⟨Aw(Γ), σ′⟩= ⟨Γ, σ⟩∆(σ′(a), σ′(b), σ′(c), σ′(α), σ′(β), σ′(γ))
In this equation the colorings σ and σ′ again agree on all edges where it makes sense. The colors of
the six new edges are denoted a, α, b, β, c, γ as shown in Figure 2 and ∆is deﬁned above.
Deﬁnition 2.2. As noted above a 0-framed knot K is a special case of a KTG with a single edge e.
In this case we denote its colored Jones polynomial by JK,n = ⟨K, σ⟩, where σ(e) = n −1.
We study the family of Montesinos knots C(r, s, t, u) shown in Figure 1. For technical reasons we
restrict ourselves to s ≤−3 ≤3r, t, u all odd. And u < 0. A similar family was studied in [14].
A, A
A, F
2(−r + s + t + u)
u
−u
−u
−u −s
−u −s
s
−r −s
−s −t
−r −t
=
−1
−1
1
r
t
Figure 3.
Starting from a theta graph (left), we ﬁrst apply the A-move to both
vertices, and again on one of the newly created vertices. Next change the framing on
many edges. The numbers on each edge indicate the number of half twists present.
Finally unzip the four edges (shown thickened) marked with r, s, t, u, respectively, to
obtain the 0-framed diagram for the knot C(r, s, t, u).
To compute the colored Jones polynomial of K = C(r, s, t, u) we take the following steps (see also
[13]). The ﬁrst step is to generate our knot K from the theta graph by KTG moves. One way to
achieve this is shown in Figure 3. All edges should be thought of as bands with blackboard framing.
The numbers indicate half twists (not colors). Note that the unzip applied to a twisted edge produces
two twisted bands that form a crossing as shown in the ﬁgure on the right. This is natural considering
that the black lines stand for actual strips. Reading backwards and applying the above equations we
may compute JK,n+1 as follows. The unzips yield four summations, the framing change multiplies
everything by the factors f, the A moves produce the ∆terms and ﬁnally we are left with a single
θ(2a, 2b, 2c). Note we have scaled the summation variables a, b, c, d to make them integers instead of
even integers.
JC(r,s,t,u),n+1 = f(n)−2Wr(r,s,t)−2r−2s−2t+2u
X
a,b,c,d∈nP∩Z
∆(2a, 2b, 2c, n, n, n)2×
∆(2b, n, n, 2d, n, n)O2aO2bO2cO2df(2a)rf(2b)sf(2c)tf(2d)−uθ(2a, 2b, 2c)
θ(2a, n, n)θ(2b, n, n)θ(2c, n, n)θ(2d, n, n)
