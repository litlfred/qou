---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-031-33-quantum-dilogarithm
section_title: "Quantum dilogarithm"
section_number: 3.3
pages: 33-35
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
be described in the next subsection. Assuming that
∫ idq
4πℏ|q⟩⟨q| =
∫
dp|p⟩⟨p| = 1 and
⟨p|q⟩ = e
pq
2iℏ (the exact normalizations are not important for the ﬁnal inv ariant), one
obtains via Fourier transform
⟨p1,p 3|S|p2,p 4⟩ = δ(p1 +p3−p2)√
−4πiℏ Φ ℏ (p4−p3 +iπ + ℏ)e
1
2ℏ
“
p1(p4−p3)+ iπ ℏ
2 − π 2−ℏ 2
6
”
, (3.13)
⟨p2,p 4|S−1|p1,p 3⟩ = δ(p1 +p3−p2)√
−4πiℏ
1
Φ ℏ (p4−p3−iπ− ℏ)e
1
2ℏ
“
p1(p3−p4)− iπ ℏ
2 + π 2−ℏ 2
6
”
. (3.14)
In the classical limit ℏ → 0, the quantum dilogarithm has the asymptotic Φ ℏ(p) ∼
1
2ℏ Li2(−ep). One therefore sees that the classical limits of the above m atrix elements look
very much like exponentials of 1
2ℏ times the complexiﬁed hyperbolic volumes of tetrahe-
dra. For example, the asymptotic of (3.13) coincides with ex p(L(z;·,·)/(2ℏ)) if we identify
ep4−p3 with z and e−2p1 with 1/(1−z). For building a quantum invariant, however, only
half of the variables pj really “belong” to a single tetrahedron. Hikami’s claim [26 , 27] is
that if we only identify a shape parameter
z(i) =ep(i)
4 −p(i)
3 , (3.15)
for every tetrahedron ∆ i, the classical limit of the resulting quantum invariant wil l com-
pletely reproduce the hyperbolic structure and complexiﬁe d hyperbolic volume on M .15
To ﬁnish calculating the invariant of M , one glues the tetrahedra back together and
takes inner products in every pair V andV ∗ corresponding to identiﬁed faces. This amounts
to multiplying together all the matrix elements (3.13) or (3 .14), identifying the p(i)
j variables
on identiﬁed faces (with matching head-to-tail normal vect ors), and integrating over the
2N remainingp’s. To account for possible toral boundaries of M , however, one must revert
back to the hyperbolic structure. This allows one to write th e holonomy eigenvalues{euk}
as products of shape parameters ( z(i), 1− 1/z(i), 1/(1−z(i))), and, using (3.15), to turn
every cusp condition into a linear relation of the form ∑ p’s = 2uk. These relations are
15Eqn. (3.15) is a little diﬀerent from the relation appearing in [26, 27], because our convention for
assigning shape parameters to edges based on orientation di ﬀers from that of [26, 27].
– 32 –
then inserted as delta functions in the inner product integr al, enforcing global boundary
conditions. In the end, noting that each matrix element (3.1 3)-(3.14) also contains a delta
function, one is left with N−b0(Σ) nontrivial integrals, where b0(Σ) is the number of
connected components of Σ = ∂M . For example, specializing to hyperbolic 3-manifolds
with a single torus boundary Σ = T 2, the integration variables can be relabeled so that
Hikami’s invariant takes the form
H(M ; ℏ,u ) = 1
(4πℏ)N/2
∫ N∏
i=1
Φ ℏ
(
gi(p, 2u) +ǫi(iπ + ℏ)
) ǫi
ef (p,2u,ℏ)/2ℏ dp1...dp N −1.
(3.16)
The gi are linear combinations of ( p1,...,p N −1, 2u) with integer coeﬃcients, and f is a
quadratic polynomial, also with integer coeﬃcients for all terms involving pk’s oru. In the
classical limit, this integral can naively be evaluated in a saddle point approximation, and
Hikami’s claim is that the saddle point relations coincide p recisely with the consistency
conditions for the triangulation on M . There is more to this story, however, as we will see
in Section 3.4.
3.3 Quantum dilogarithm
Since quantum dilogarithms play a key role here, we take a lit tle time to discuss some of
their most important properties.
Somewhat confusingly, there are at least three distinct—th ough related—functions
which have occurred in the literature under the name “quantu m dilogarithm”:
i) the function Li 2(x;q) deﬁned for x, q∈ C with|x|,|q|< 1 by
Li2(x;q) =
∞∑
n=1
xn
n (1−qn), (3.17)
whose relation to the classical dilogarithm function Li 2(x) =
∞∑
n=1
xn
n2 is that
Li2
(
x; e2ℏ)
∼ −1
2ℏ Li2(x) as ℏ→ 0 ; (3.18)
ii) the function ( x;q)∞ deﬁned for |q|< 1 and all x∈ C by
(x;q)∞ =
∞∏
r=0
(
1−qrx), (3.19)
which is related to Li 2(x;q) for|x|< 1 by
(x;q)∞ = exp
(
−Li2(x;q)
)
; (3.20)
and ﬁnally
iii) the function Φ( z;τ ) deﬁned for Re ( τ )> 0 and 2|Re (z)|< 1 + Re (τ ) by
Φ(z;τ ) = exp
(1
4
∫
R(+)
e2xz
sinhx sinhτx
dx
x
)
(3.21)
– 33 –
(here R(+) denotes a path from −∞ to∞ along the real line but deformed to pass over
the singularity at zero), which is related to ( x;q)∞ by
Φ(z;τ ) =











(
− e(z +τ/ 2); e(τ )
)
∞
(
− e((z− 1/2)/τ ); e(−1/τ )
)
∞
if Im (τ )> 0,
(
− e((z + 1/2)/τ ); e(1/τ )
)
∞(
− e(z−τ/ 2); e(−τ )
)
∞
if Im (τ )< 0.
(3.22)
(Here and in future we use the abbreviation e(x) = e2πix.)
It is the third of these functions, in the normalization
Φ ℏ(z) = Φ
(z
2πi ; ℏ
iπ
)
, (3.23)
which occurs in our “state integral” and which we will take as our basic “quantum dilog-
arithm,” but all three functions play a role in the analysis, so we will describe the main
properties of all three here. We give complete proofs, but on ly sketchily since none of this
material is new. For further discussion and proofs, see, e.g., [13, 14, 15, 51, 20], and [57]
(subsection II.1.D).
