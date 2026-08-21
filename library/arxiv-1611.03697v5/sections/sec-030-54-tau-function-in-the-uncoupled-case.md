---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-030-54-tau-function-in-the-uncoupled-case
section_title: "Tau function in the uncoupled case"
section_number: 5.4
pages: 27-29
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
Υ( w) = e−ζ ′(−1) e
3
4 w2
G(w + 1)
(2π)
w
2 w
w2
2
,
where G is the Barnes G-function [ 2], [ 30, Appendix], and ζ(s) is the Riemann zeta function. It
deﬁnes a holomorphic and nowhere vanishing function on C∗\ R<0 which we specify uniquely by
deﬁning the factor ww2/2 using the principal value of log. The asymptotic expansion of Υ( w) is
log Υ( w)∼− 1
12 log(w) +
∑
g≥2
B2g
2g(2g− 2) w−(2g−2), (31)
valid as w→∞ in the complement of any sector in C∗ containing the ray R<0. This can be
found for example in [ 2, Section 15] or [ 30, Appendix], although note that Barnes uses a diﬀerent
indexing for the Bernoulli numbers, and refers to the real number
A = e
1
12· e−ζ ′(1)
as the Glaisher-Kinkelin constant.
Lemma 5.4. There is an identity
d
dw log Υ( w) = w d
dw log Λ( w).
Proof. Note that this is obvious at the level of the asymptotic expansions. For the proof we use
the identity
d
dw log G(w + 1) = 1
2 log(2π) + 1
2− w + w d
dw log Γ( w)
which can be found in [ 2, Section 12] (see also [ 30, Formula (A.13)]) to get
d
dw log Υ( w) = 1
2 + w d
dw log Γ(w)− w log w.
The result then follows from ( 26) by taking log and diﬀerentiating. □
In the case of variations of BPS structures satisfying the conditio ns of Theorem 5.3 the following
result gives a natural choice of τ -function.
28 TOM BRIDGELAND
Theorem 5.5. Let (Γ , Zp, Ω p) be a framed, miniversal variation of ﬁnite, uncoupled, inte gral BPS
structures over a complex manifold M. Given a ray r⊂ C∗, the function
τr(p; t) =
∏
Zp(γ)∈iHr
Υ
(Z(γ)
2πit
) Ω( γ)
(32)
is a τ -function for the family of solutions of Theorem 5.3.
Proof. The expression ( 32) is holomorphic and non-zero on Hr for the same reason given in the
proof of Theorem 5.3. It is also clearly invariant under simultaneous rescaling of Z and t. Choosing
a basis ( γ1,··· , γn)⊂ Γ, and using the local co-ordinates zi = Z(γi) on M, we have
2πi·
∑
i
ǫij
∂ log τr
∂zi
=
∑
i
∑
Zp(γ)∈iHr
Ω( γ) ǫij mi(γ)
t
( d
dw
⏐
⏐
⏐
w= Z(γ )
2πit
)
log Υ( w),
where we wrote ǫij =⟨γi, γj⟩ and used the decomposition γ = ∑
i mi(γ)γi. Using Lemma 5.4 this
can be rewritten as
∑
Zp(γ)∈iHr
Ω( γ)⟨γ, γj⟩
t
(
w d
dw
⏐
⏐
⏐
w= Z(γ )
2πit
)
log Λ( w) = ∂
∂t
∑
Zp(γ)∈iHr
log Λ
(Z(γ)
2πit
) Ω( γ)⟨γj ,γ⟩
= ∂ log Yr,γj
∂t ,
which gives ( 24), and hence completes the proof that ( 32) deﬁnes a τ -function. □
Applying ( 31) we get an asymptotic expansion
log τr(p; t)∼ 1
24
∑
γ∈Γ
Ω( γ) log
( 2πit
Z(γ)
)
+
∑
g≥2
∑
γ∈Γ
Ω( γ)· B2g
4g (2g− 2)
( 2πit
Z(γ)
) 2g−2
(33)
valid as t→ 0 in the half-plane Hr. Once again this expansion is independent of the ray r⊂ C∗.
Remark 5.6. The function Υ( w) is closely related to the function γℏ(x; Λ) which plays an impor-
tant role in Okounkov and Nekrasov’s work on supersymmetric gaug e theories [ 26, Appendix A].
More precisely, they consider a function γℏ(x; Λ) which is uniquely deﬁned up to a linear function
in x by two properties: a diﬀerence equation, and the existence of an a symptotic expansion. Using
the property G(w + 1) = Γ( w)· G(w) of the Barnes G-function, and the expansion ( 31), it follows
that we can take
eγt(z;1) = e−ζ ′(−1)· G
(z
t + 1
)
· t
1
2 ( z
t )2− 1
12· (2π)− z
2t = Υ
(z
t
)
· t
1
12· e
1
t2 ( 1
2 z2 log(z)− 3
4 z2).
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 29
The term appearing in the exponential on the right-hand side gives r ise to the prepotential of the
gauge theory. We hope that a clearer understanding of the deﬁnit ion of the τ -function will enable
us to give a mathematical deﬁnition of the prepotential.
