---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-014-51-bounds-on-cumulants-and-mod-gaussian-converge
section_title: "Bounds on cumulants and mod-Gaussian convergence"
section_number: 5.1
pages: 38-39
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
quence of real-valued centered random variables that admit moments of all order, and
such that
|κ(r)(Sn)|≤ (Cr)r αn(βn)r (24)
for all r≥ 2 and for some sequences (αn)n→∞→ +∞ and (βn)n∈N arbitrary. Assume
moreover that there exists an integer v≥ 3 such that
(1) κ(r)(Sn) = 0 for all 3≤ r < v and all n∈ N;
MOD-φ CONVERGENCE, I 39
(2) we have the following approximations for second and third cumulants:
κ(2)(Sn) = σ2 αn(βn)2
(
1 + o
(
(αn)− v−2
v
))
;
κ(v)(Sn) = L αn(βn)v(
1 + o(1)
)
. (25)
Set Xn = Sn
(αn)
1v βn
. The cumulant generating series of Xn is
log ϕn(z) = κ(2)(Sn)
2 (αn)
2
v (βn)2
z2 + κ(v)(Sn)
v! αn(βn)v zv +
∞
∑
r=v+1
κ(r)(Sn)
r! (αn)
r
v (βn)r zr
= σ2
2 (αn)
v−2
v z2 + L
v! zv +
∞
∑
r=v+1
κ(r)(Sn)
r! (αn)
r
v (βn)r zr + o(1),
where the o(1) is locally uniform. The remaining series is locally uniformly bounded
in absolute value by
∞
∑
r=v+1
Cr rr
r!
1
(αn)
r−v
v
Rr≤ αn
∞
∑
r=v+1
(
e CR
(αn)
1
v
)r
= ( αn)− 1
v
(e CR)v+1
1− e CR (αn)− 1
v
→ 0.
Hence,
ψn(z) = exp
(
−(αn)
v−2
v
σ2z2
2
)
ϕn(z)→ exp
( L
v! zv
)
locally uniformly on C, so one has again mod-Gaussian convergence, with parameters
tn = σ2 (αn)
v−2
v and limiting function ψ(z) = e
L
v! zv
.
Remark 5.1. The case of i.i.d. variables — Example 2.2 — ﬁts in this framework, with
αn = n and βn = 1.However, it includes many more examples than sums of i.i.d. vari-
ables: in particular, in Section 9, we show that such bounds on cumulants typically
occur in the framework of dependency graphs. Concrete examples are discussed in
Sections 10 and 11.
