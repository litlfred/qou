---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-008-42-skein-interaction-between-hn-a-and-c
section_title: "Skein interaction between Hn, A and C."
section_number: 4.2
pages: 18-21
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
Skein interaction between Hn, A and C.
We can make use of wiring diagrams, as described in [13], to induce linear
maps between skeins. A wiring diagram W is an inclusion of one surface F
into another F ′, along with a ﬁxed diagram of curves in F ′ which avoid F,
and connect any distinguished input and output points on the boundaries
of both, respecting orientation. A wiring W induces a linear map, denoted
S(W) : S(F) →S(F ′), using W to extend any diagram in F to a diagram
in F ′.
To avoid over-elaborate notation I shall write W in place of S(W) where
there is no risk of confusion.
The diagram
Wn =
with n strings running around the annulus then induces a linear map Wn :
Rn+1
n+1 →A, by inserting an (n + 1)-tangle in the empty box.
When an element S ∈Hn is included in Hn+1 in the standard way, using
their skein versions, we can see from a diagram that Wn(S) = Wn−1(S)a.
Then Wn(1) = an, where a ∈A is the element shown above.
Theorem 4.3 The elements Wn(hn+1), Wn(hn) and l(hn, e) in A satisfy the
linear relation
[n + 1]Wn(hn+1) = s−1[n]Wn(hn) + l(hn, e).
18
Proof :
The relation
γ n+1
=
γ n
+ sn
gives Wn(hnγn+1) = Wn(γnhn) + snWn(hnσn · · · σ1), after taking γn from the
second diagram around the strings of the wiring.
Now γnhn = sn−1[n]hn and Wn(hnσn · · ·σ1) = l(hn, e). Combined with
the equation sn[n + 1]hn+1 = hnγn+1 from corollary 3.4 the result follows at
once.
✷
Now write Yn = [n + 1]Wn(hn+1) and set Y (t) =
P∞
n=0 Yntn.
Corollary 4.4 As power series with coeﬃcients in A we have
l(H(t), e) = (e −s−1at)Y (t).
Proof : Since Wn(hn) = Wn−1(hn)a = aWn−1(hn) the relation can be written
Yn = s−1aYn−1+l(hn, e). This gives Y (t) = s−1atY (t)+l(H(t), e), and hence
the result.
✷
The mirror map, switching crossings and inverting s and v, when applied
to l(X, e) for any X ∈C gives r(e, X). Now H(t) = H(t) and so Y (t) = Y (t),
giving
r(e, H(t)) = (e −sat)Y (t).
Subtracting this from the equation in corollary 4.4 then gives [H(t), e] =
(s −s−1)atY (t), a result used by Lukac in [10].
Proof of theorem 4.2:
Take logarithms of the equations and then subtract.
Then
ln(e −s−1at) −ln(e −sat)
=
ln (l(H(t), e)) −ln (r(e, H(t)))
=
l(ln(H(t)), e) −r(e, ln(H(t)))
=
∞
X
m=1
[Pm
m tm, e].
Now ln(e −s−1at) = −P∞
m=1 s−mamtm/m, and it only remains to compare
the coeﬃcients of tm to see that [Pm, e] = (sm −s−m)am.
✷
19
Proof of theorem 3.9:
Use the wiring
Vn =
with n −1 strings passing through the annulus to carry A into Rn
n. Then for
any X in C we have Vn(l(X, e)) = ψn(X) and Vn(r(e, X)) = ψn−1(X) with the
standard inclusion. We can also see that Vn(a) = v−1T(n), and extend this
to Vn(am) = v−mT(n)m. Then ψn(Pm) −ψn−1(Pm) = (sm −s−m)v−mT(n)m.
Induction on n completes the proof that
ψn(Pm) −ψ0(Pm) = (sm −s−m)v−m
n
X
j=1
T(j)m.
✷
To conclude this paper I give the proof of theorem 3.6, using one ﬁnal
wiring, this time to induce a map from A to C.
Write
C =
for the wiring diagram shown, which provides a form of closure for an element
of A, and determines a linear map C : A →C. It is clear that C(am) = Am+1
for every m ≥0. We can also see readily that
C(F r(e, X)) = C(r(F, X)) = C(F)X
for every F ∈A and X ∈C.
Proof of theorem 3.6:
The relation (e −sat)Y (t) = r (e, H(t)) gives
Y (t) =
 ∞
X
m=0
smamtm
!
r (e, H(t)) .
20
Then
C (Y (t))
=
C
 ∞
X
m=0
smamtm
!
H(t)
=
 ∞
X
m=0
smAm+1tm
!
H(t),
giving
zstC (Y (t)) = (A(st) −1) H(t).
Now C (Wn(hn+1)) is the closure of the (n + 1)-tangle σ1σ2 · · · σnhn+1 =
snhn+1. Then C(Yn) = [n + 1]snhn+1 ∈C. It follows that
zstC (Y (t))
=
∞
X
n=0
(sn+1 −s−(n+1))sn+1hn+1tn+1
=
∞
X
n=0
(s2n+2 −1)hn+1tn+1
=
H(s2t) −H(t).
This gives H(s2t)−H(t) = A(st)H(t)−H(t), and thus H(st) = A(t)H(s−1t),
to complete the proof.
✷
Version 1.2, February 2001.
