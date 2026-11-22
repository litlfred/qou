---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-022-42-different-kinds-of-q-exponential-summation
section_title: "Different kinds of q-exponential summation"
section_number: 4.2
pages: 38-41
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
The classical Borel-Laplace exponential summation is based on the Eu-
ler’s integral representation of the Gamma function, namely
(4.4)
n! =
Z ∞
0
e−ttn+1 dt
t .
In the deﬁnition of a q-summation procedure one must be guided by the
q-analogs of this last integral, question investigated since Jackson, Wigeret,
Watson, etc...
We recall the following q-analogs of the integral representation of the
Euler Gamma function.
Proposition 4.8. — For d ∈(−π, π) and λ /∈(−qZ) we have:
(4.5)
[n]!
q = q −1
ln q
Z ∞eid
0
tn
eq(qt)dt = q −1
ln q
Z ∞eid
0
tnep(−qt)dt,
(4.6)
[n]!
q = q
Z
λpZ
tn
eq(qt)dpt = q
Z
λpZ tnep(−qt)dpt,
(4.7)
qn(n−1)/2 =
q
ln q
Z ∞eid
0
tn
θp(qt)dt,
(4.8)
qn(n−1)/2 =
q
1 −p
Z
λpZ
tn
θp(qt)dpt.
Proof. — For the proof of the identities above cf. [1, pages 549-550]. More
precisely, letting c →n + 1, b →1 and a →0 (resp. letting c →n + 1,
b, a →0) in
Z ∞
0
xc−1 (−ax; p)∞(−pb/x; p)∞
(−x; p)∞(−p/x; p)∞
dx =
(ab; p)∞(pc; p)∞(p1−c; p)∞π
(bpc; p)∞(ap−c; p)∞(p; p)∞sin(πc),
TOME 59 (2009), FASCICULE 1
384
Lucia DI VIZIO & Changgui ZHANG
one gets the formula
Z ∞
0
xn
(−x; p)∞
dx = (ln q)(p; p)np−n(n+1)/2

resp.
Z ∞
0
xn
(−x; p)∞(−p/x; p)∞
dx = (ln q) p−n(n+1)/2

,
which yields (4.5) (resp. (4.7)). Similarly, the formulae (4.6) and (4.8) can
be viewed as special cases of
Z ∞
0
xc−1 (−ax; p)∞(−bp/x; p)∞
(−x; p)∞(−p/x; p)∞
dpx =
(1 −p)(p; p)∞(−pc; p)∞(−p1−c; p)∞(ab; p)∞
(−1; p)∞(−p; p)∞(ap−c; p)∞(bpc; p)∞
.
□
Remark 4.9. —
In particular, (4.8) and (4.7) have been studied in [15]
and [23] as starting points for the corresponding summation procedures.
Other kinds of q-summation are considered in [20] and [12].
Let d ∈[−π, π). We will identify d to the half line [0, ∞eid) := R+eid.
Definition 4.10. — We set Hd
q = ∩λ∈(0,∞eid)H[λ;q].
Remark 4.11. —
The functional space Hd
q is exactly the space Hd
q;1 in-
troduced in [20].
Let λ ∈C∗and d ∈[−π, π). According to Proposition 4.8, the following
four q-Laplace transforms are well deﬁned:
∀φ ∈H[λ;q],
L[λ]
q φ =
q
1 −p
Z
λpZ
φ(ξ)
θp(q ξ
x)
dpξ;
∀φ ∈H[λ/(1−p);q],
L[λ]
q φ =
q
1 −p
Z
λpZ
φ(ξ/(1 −p))
eq(q
ξ
(1−p)x)
dpξ;
∀φ ∈Hd
q,
Ld
qφ =
q
ln q
Z eid∞
0
φ(ξ)
θp(q ξ
x)
dξ,
Ld
qφ = q −1
ln q
Z eid∞
0
φ(ξ)
eq(q ξ
x)
dξ.
Definition 4.12. —
(1) If ˆf ∈C{x}[λ;q]
q
, we deﬁne its sums in the
direction [λ; q] as follows:
S[λ]
q
ˆf = L[λ]
q (Bq ˆf),
S[λ]
q
ˆf = L[λ]
q (Bq ˆf).
(2) If ˆf ∈C{x}d
q, deﬁne its sums in the direction d as follows:
Sd
q ˆf = Ld
q(Bq ˆf),
Sd
q ˆf = Ld
q(Bq ˆf).
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
385
Remark 4.13. —
• The summation procedures ˆf →S[λ;q] ˆf and ˆf →Sd ˆf are introduced in
[23] and [21]: they have many good asymptotic properties.
• Suppose that ˆf is q-summable and that d is not a singular direction. Then
we have the following formal equality (meaning that we exchange carelessly
the inﬁnite sum and the integral):
(4.9)
Sd
q ˆf =
1
ln q
Z qeid
eid
S[λ]
q
ˆf dλ
λ
and
(4.10)
Sd
q ˆf =
1
ln q
Z qeid
eid
S[λ]
q
ˆf dλ
λ .
To prove that this identity is not only formal, but analytic, one would like
to apply the dominated convergence theorem: unfortunately the dominated
convergence is a little bit delicate for a general ˆf, since we don’t really
control the spirals of poles of the discrete q-Borel sums. Anyway, we will
prove (4.9) and (4.10) for a generic q-Gevrey series (cf. Theorem 4.14).
At this stage a natural question arises:
Do we have S[λ;q] ˆf = S[λ;q] ˆf and Sd ˆf = Sd ˆf?
The answer is clear, and trivially positive, if ˆf(x) is a germ of analytic
function at zero: in this case all the sums of ˆf(x) coincide with f.
The rest of the paper is devoted to the proof of the following theorem:
Theorem 4.14. — Let ˆf be a generic q-Gevrey series and let λ ∈C∗,
d ∈[−π, π). Assume that λ /∈DS( ˆf) and (0, eid∞) ∩DS( ˆf) = ∅. Then
(1) S[λ]
q
ˆf = S[λ]
q
ˆf, on a convenient domain Ω.
(2) Sd
q ˆf = Sd
q ˆf on a convenient sector containing the direction d.
Moreover we have:
Sd
q ˆf =
1
ln q
Z qeid
eid
S[λ]
q
ˆf dλ
λ .
Remark 4.15. —
Theorems 3.3 and 3.10 are a special case of Theo-
rem 4.14.
Before giving a proof of Theorem 4.14 in §4.5, we make a digression
about two essential ingredients of the proof: ﬁrst we prove the theorem in
the special case of the Tschakaloﬀseries; then we introduce a functional
space that allows to read, in certain sense, any q-Gevrey series as a ﬁnite
linear combination of some modiﬁed Tschakaloﬀseries.
TOME 59 (2009), FASCICULE 1
386
Lucia DI VIZIO & Changgui ZHANG
