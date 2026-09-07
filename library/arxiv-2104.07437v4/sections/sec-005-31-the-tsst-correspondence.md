---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-005-31-the-tsst-correspondence
section_title: "The TS/ST correspondence"
section_number: 3.1
pages: 11-15
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
review and references can be found in [58].
3.1 The TS/ST correspondence
The simplest case of the TS/ST correspondence corresponds to the case of toric CYs X with
one single true modulus, and we will only consider this type of examples in this paper. In
this case, the mirror curve Σ X has genus one. As shown in [18], there is a canonical way to
obtain an operator on L2(R), ρX, by Weyl quantization of this curve. The mass parameters
of X become parameters of the operator ρX. The quantization procedure introduces a Planck
constant ℏ∈ R>0. It can be shown that, for appropriate values of the mass parameters, the
operator ρX is self-adjoint and of trace class, therefore its spectral determinant
ΞX(κ, ℏ) = det(1 +κρX) (3.1)
3The simplest toric CY manifold is the resolved conifold. However, in that case the series Φ N(gs) has a ﬁnite
radius of convergence, there are no singularities in the Borel plane, and the Stokes constants vanish. Non-trivial
Stokes constants only arise when the toric CY has compact four-cycles.
– 10 –
exists and deﬁnes an entire function of κ. Its expansion around the origin
ΞX(κ, ℏ) = 1 +
∑
N≥1
ZN(ℏ)κN (3.2)
deﬁnes “fermionic spectral traces”ZN(ℏ), which depend on ℏ and on the possible mass parameters
ofX. It is easy to show that these fermionic traces are polynomials in the conventional “bosonic”
traces
Trρn
X. (3.3)
In the more general case in which the toric CY has r true moduli, one can deﬁne a generalized
spectral determinant depending on r variablesκ = (κ1,··· ,κr), with an expansion of the form
[19, 39]
ΞX(κ, ℏ) = 1 +
∑
N
ZN(ℏ)κN1
1 ··· κNr
r . (3.4)
The TS/ST correspondence postulates, among other things, that the fermionic spectral traces
ZN(ℏ) have an asymptotic expansion as ℏ→∞ which is essentially given by the formal power
series (2.11) 4
ZN(ℏ)∼cNgνN
s ΦN(gs), ℏ =−g−1
s ≫ 1. (3.5)
Here, cN and νN are constants. Since the fermionic spectral traces are well-deﬁned for ℏ∈
R>0, this deﬁnes a rigorous non-perturbative completion of topological string theory at the
conifold point. This particular consequence of the TS/ST correspondence has been tested in
detail and extensively studied in e.g. [19, 39, 42, 43, 59, 60]. It should be noted that the
asymptotic conjecture (3.5) is itself the consequence of a stronger conjecture which provides
an exact expression for the spectral determinant and the fermionic spectral traces in terms of
topological string data (and, in particular, of BPS invariants of the CY X). One can obtain in
this way exact quantization conditions for the spectral problem of the quantum mirror curve (see
also [61–64] for related developments).
As we will show, the relation (3.5) turns out to be very useful to study the resurgent structure
of the formal power series Φ N(gs). However, to understand this structure, we have to consider
the case in which gs (or, equivalently, ℏ) is complex. The complexiﬁcation of ℏ in the TS/ST
correspondence was addressed in diﬀerent forms in [65–68]. In [66, 67] it was shown in some
examples that the spectral problem associated to the operator ρX is well-deﬁned when ℏ is of
the form ℏ = 2πeiθ, where θ∈ (0,π ). The spectrum of the operator ρX is in this case discrete
and complex.
In this paper we will assume that TS/ST correspondence can be extended to the complex
ℏ-plane minus the negative real axis,
ℏ∈ C′ = C\R≤0, (3.6)
in such a way that the relevant operators remain of trace class, and the fermionic spectral traces
ZN(ℏ) are analytic functions on C′. Although we do not know how to establish this on general
grounds, we will show that it is possible to perform the analytic continuation to C′ in explicit
expressions for theZN(ℏ). It turns out that the resulting picture shares many formal similarities
with complex Chern–Simons theory on the complement of a hyperbolic knot K. More precisely,
we have the following parallelisms:
4We choose this convention for gs because we want to treat ℏ and gs as modular-like parameters, and the
relation ℏ =−g−1
s is the analogue of an S-type modular transformation.
– 11 –
1. The spectral determinant Ξ X(κ, ℏ) and the fermionic spectral traces ZN(ℏ) correspond to
state integral invariants of the knot [26, 27], also known as Andersen–Kashaev invariants
[28]. For the complement of a hyperbolic knot, the Andersen–Kashaev invariant is a func-
tionZK(u,τ ) of the holonomyu around the knot, and a complex coupling constantτ which
plays the rˆ ole of Planck’s constant. Therefore, we expect that the full spectral determinant
ΞX(κ, ℏ), as function of the modulus κ, corresponds to the state integral as a function of
u. Note that both are entire functions of the moduli (for ZK(u,τ ), this was proved in [12]
in the case of the ﬁrst two non-trivial hyperbolic knots). Accordingly, the spectral traces
ZN(ℏ) correspond to the coeﬃcients of ZK(u,τ ) in a Taylor expansion around u = 0. The
ﬁrst non-trivial coeﬃcient in this expansion, which is ZK(τ) =ZK(u = 0,τ ), was studied in
[11] (the case with more than one modulus in topological string theory would correspond
to the case of links in complex CS theory).
2. The asymptotic expansion (3.5) of ZN(ℏ), involving the perturbative topological string
series, corresponds to the expansion of the Andersen–Kashaev invariant at large positive
values ofτ. This is given by the asymptotic expansion of complex CS theory around the so-
called conjugate connection (which is the complex conjugate to the geometric connection).
3. The volume conjecture for the Andersen–Kashaev invariant [28] states that its asymptotics
at τ → 0+ involves the complexiﬁed volume 5 VK of the three sphere complement of the
hyperbolic knotK:
ZK(τ)∼ exp
(
−VK
τ
)
, τ → 0+. (3.7)
In this equation, we have set u = 0 in ZK(u,τ ), but there is a generalization to arbitrary u
[28, 69]. The conjecture (3.7), which is closely related to the original Kashaev conjecture
[70], relates a “quantum” invariant of the knot in the l.h.s., to a “classical” geometric
invariant in the r.h.s. Interestingly, the TS/ST correspondence implies a conifold volume
conjecture for toric CYs ,
ZN(−g−1
s )∼ exp
(
1
gs
r∑
i=1
NiVi
)
, g s→ 0−, (3.8)
whereVi, i = 1,··· ,r are the values of the K¨ ahler parameters of the CY at the conifold
point. This can be also regarded as a relation between the asymptotics of a “quantum”
invariant on the l.h.s. (a spectral trace obtained by quantizing the mirror curve), to a
“classical” geometric property of the CY. Let us note as well that the Vi can be regarded
as the “minimal” values of the volumes of the CY manifold. The conifold volume conjecture
(3.8) for toric CY manifolds was checked in one and two-moduli examples in [19, 39, 42,
43, 71].
4. The state integral has a factorization property, namely, it can be written as a sum of
products of holomorphic and anti-holomorphic blocks [11, 12, 72–75]. Moreover, the blocks
are given by q and ˜q-series, where
q = e2πiτ, ˜q = e−2πi/τ. (3.9)
As we will see, the fermionic spectral traces also factorize in various examples, and can be
written as a sum of products of q and ˜q series. There is however an important diﬀerence
5The imaginary part of the complexiﬁed volume is the Chern-Simons action.
– 12 –
complex CS theory TS/ST correspondence
state integral spectral determinant and traces
expansion around conjugate connection perturbative topological string
volume conjecture conifold volume conjecture
(symmetric) factorization (non-symmetric) factorization
DGG index new integer invariants
Table 1. Similarities between structures appearing in complex CS theory and in the TS/ST correspon-
dence.
between the state integral and the fermionic spectral traces. The former is symmetric under
the S-duality transform
τ→− 1
τ (3.10)
which exchanges q and ˜q. This leads to a symmetry between the holomorphic and anti-
holomorphic blocks, which involve the same functions (with diﬀerent arguments). In con-
trast, the fermionic spectral traces do not have this symmetry, and sending ℏ to−1/ℏ
exchanges the conventional topological string with the NS topological string. As a conse-
quence, the holomorphic and anti-holomorphic blocks are given by diﬀerent functions, as
we will see in examples.
5. As shown in [11, 12], the Stokes constants associated to the diﬀerent asymptotic series in
complex CS theory are integer invariants, and they turn out to be closely related to the
DGG index of the knot [3]. In the case of the topological string, the Stokes constants are
precisely the new integer invariants that we deﬁne in this paper, therefore we can regard
these as analogues of the DGG index.
We summarize these parallelisms in Table 1. The formal similarities between the two theories
suggest a reinterpretation of topological string theory on toric CYs in terms of a topological gauge
theory, or perhaps of a superconformal ﬁeld theory in 3d, in view of the 3d/3d correspondence
[31, 76] 6. We should note that, even at the formal level, the topological string story seems to
be much more involved than the complex CS counterpart. For example, in complex CS, the
diﬀerent formal power series have a simple semiclassical interpretation in terms of expansions
around diﬀerent saddle points, and this makes their calculation a relatively easy task. We do
not have such a physical interpretation for the topological string series (2.31). Another crucial
diﬀerence is that the full moduli-dependent state integral ZK(u,τ ) can be represented in terms
of an integral, which can be in addition calculated explicitly in many interesting examples.
In the case of the topological string, we are not aware of integral expressions for the spectral
determinant.
As a ﬁnal comment on the formal similarities between CS and topological string theory, let
us point out the following. One could think that ZK(u,τ ), being a wavefunction, corresponds
rather to an open topological string theory. However, as noted in [58], it is likely that Ξ( κ, ℏ)
has an interpretation as a wavefunction on the moduli space of the closed CY moduli, in line
with the suggestion of [77]. One important open problem is to ﬁnd the analogue of the quantum
diﬀerential equation satisﬁed by Ξ(κ, ℏ), similar to the AJ equation satisﬁed byZK(u,τ ). Inspired
6The possible relationship with a 3d superconformal ﬁeld theory was already pointed out in [18], where it was
also noted that the spectral traces at large N and ﬁxed ℏ satisfy a N 3/2 scaling typical of many 3d theories.
– 13 –
u mF0
