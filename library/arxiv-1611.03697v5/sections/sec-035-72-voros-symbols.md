---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-035-72-voros-symbols
section_title: "Voros symbols"
section_number: 7.2
pages: 35-36
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
above BPS structures can be solved using exact WKB analysis of an a ssociated Schr¨ odinger equa-
tion. This was essentially proved by Iwaki and Nakanishi [ 20] following Gaiotto, Moore and Neitzke
[17].
Suppose given a quadratic diﬀerential ( S, q) as above. Let us also choose a projective structure on
the Riemann surface S.2 We can then invariantly consider the holomorphic Schr¨ odinger equa tion
ℏ2 d2
dz2 y(z, ℏ) = q(z)· y(z, ℏ),
where z is a co-ordinate in the chosen projective structure. The WKB meth od involves substituting
y(z1, ℏ) = exp
(∫ z1
z0
T (z) dz
)
, T (z) =
∑
k≥0
Tk(z)· ℏk−1,
and then solving for Tj(z) order by order. This gives rise to a recursion
dTk−1
dz +
∑
i+j=k
Ti(z)Tj(z) = 0 , k > 0,
together with the initial condition T0(z)2 = q(z). Depending on the choice of square-root taken to
deﬁne T0(z) one then obtains two systems of solutions T ±
k (z). The diﬀerences
ωk(z) = 1
2
(
T +
k (z)− T −
k (z)
)
dz
are single-valued meromorphic one-forms on the spectral cover ˆS, which vanish unless k is even.
One has ω0 =
√
q(z) dz.
The formal cycle Voros symbol associated to a class γ∈ Γ is the formal sum
exp(Vγ) = exp
(1
ℏ
∫
γ
ω0
)
· exp
(∑
g≥1
ℏ2g−1
∫
γ
ω2g
)
. (42)
Iwaki and Nakanishi, relying on analytic results of [ 22], show that if r⊂ C∗ is a non-active ray
for the BPS structure deﬁned by ( S, q), then the sum over g≥ 1 in the above formal expressions
can be Borel summed in the direction r. This results in Voros symbols which are holomorphic
functions of t = ℏ deﬁned in a neighbourhood of 0 in the half-plane Hr. They also compute the
wall-crossing behaviour for these Borel sums as one varies the act ive ray r⊂ C∗.
2 If the quadratic diﬀerential q has a double pole at a point p∈ S one should assume that this projective structure
(represented in [ 20] by the term Q2(z)) also has a pole of a particular form [ 20, Assumption 2.5].
36 TOM BRIDGELAND
Claim 7.2. Given a quadratic diﬀerential (S, q) as above, the Borel sums of the cycle Voros symbols
give a solution to the corresponding weak Riemann-Hilbert p roblem with t = ℏ.
Sketch proof. For the deﬁnition of the weak Riemann-Hilbert problem see Remark 4.6(iii). The
claim should follow from the work of Iwaki and Nakanishi [ 20], although a careful proof would re-
quire additional continuity arguments to take care of diﬀerentials w ith multiple saddle connections.
See particularly Theorem 2.18, Theorem 3.4 and formula (2.21). □
It is interesting to ask whether given a suitable choice of base proje ctive structure, the Voros
symbols in fact give solutions to the full Riemann-Hilbert problem as st ated in Section 4.2. Another
interesting topic for further research is the connection with topo logical recursion [ 12], which is
known to be closely related to exact WKB analysis. In particular, it is in teresting to ask whether
the τ -function computed by topological recursion gives a τ -function in the sense of this paper.
Appendix A. V ariations of BPS structure
For BPS structures satisfying the conditions of Proposition 4.2, the BPS automorphisms S(ℓ)
can be realised as birational automorphisms of the twisted torus T. In general however, even
for BPS structures coming from quivers with potential, this is not th e case. Thus we need some
other approach to deﬁning a variation of BPS structures. If we wa nt to avoid making unnecessary
assumptions, the only way to proceed is via formal completions of th e ring C[T]. In this section
we give a rigorous deﬁnition along these lines following Kontsevich and S oibelman [ 23, Section 2].
