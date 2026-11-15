---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-021-41-two-formal-q-borel-transforms
section_title: "Two formal q-Borel transforms"
section_number: 4.1
pages: 36-38
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
The classical Borel transform associates to each power series
X
n⩾0
anxn+1
the more convergent (or less divergent) power series P
n⩾0
an
n! ξn. For the
solutions of a q-diﬀerence equations, the Gevrey “scaling factor” (n!)s is
replaced by the q-Gevrey one: (qsn2/2) (cf. [4],[13],[20],[21]). Indeed, in the
literature there are (at least) two q-analogs of the factorial n!, namely [n]!
q
and qn(n−1)/2. The reason for this dichotomy is the identity
[n]!
q = (q; q)n
(1 −q)n = (p; p)n
(1 −p)n qn(n−1)/2 = [n]!
pqn(n−1)/2,
which implies that
(4.3)
[n]!
q ∼qn(n−1)/2
(1 −p)n , when n →+∞.
TOME 59 (2009), FASCICULE 1
382
Lucia DI VIZIO & Changgui ZHANG
Let us consider the following two formal Borel transforms, associated to
those q-factorials:
Bq :
xC [[x]] →C [[ξ]] ,
X
n⩾0
anxn+1 7−→
X
n⩾0
an
[n]!q
ξn
and
Bq :
xC [[x]] →C [[ξ]] ,
X
n⩾0
anxn+1 7−→
X
n⩾0
an
qn(n−1)/2 ξn.
Following J.P. Ramis [13] we set:
Definition 4.2. — An entire function φ is said to have q-exponential
growth of order 1 at ∞if there exist two constants K > 0 and µ > 0 such
that
|φ(x)| < K|x|µeq(|x|),
|x| →∞.
Remark that the function eq(|x|) can be replaced by eln2 |x|/(2 ln q).
Lemma 4.3 ([13, Prop. 2.1]). — Let Eq be the set of all the entire
functions having a q-exponential growth of order 1 at ∞, and let C{x}
be the set of all power series having a positive convergence radius. Then
Eq = Bq(xC{x}) = Bq(xC{x}).
The following function space Hq has been introduced in [23] and [15]; see
also [20].
Definition 4.4. — For any λ ∈C∗, let [λ; q] = λqZ.
(1) A germ of function φ analytic at 0 is said to belong to H[λ;q] if there
exist a domain Ω⊂C and a real number r > 0 such that:
• ∪m⩾0{x ∈C : |x −λqm| < rqm} ⊂Ω;
• φ can be continued to be an analytic function on Ωwith a
q-exponential growth of order 1 at inﬁnity.
(2) A germ of function φ analytic at 0 is said to belong to Hq if there
exist a ﬁnite set Λ ⊂C∗such that φ ∈H[λ;q] for any λ ∈C∗\ Λ.
Proposition 4.5. — Let ˆf ∈xC[[x]], λ ∈C∗and let ψ = Bq ˆf, φ =
Bq ˆf. Then ψ ∈H[λ;q] if and only if φ ∈H[(1−p)λ;q].
Moreover, the map P
n⩾0 anxn 7→P
n⩾0 an[n]!
pxn induces an automor-
phism of the vector space Hq.
Proof. — Use the integral representation for the corresponding Hadamard
product.
□
Definition 4.6. — Let λ ∈C∗and let ˆf ∈xC[[x]].
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
383
(1) We set C{x}[λ;q]
q
= B−1
q H[λ/(1−p);q] = B−1
q H[λ;q]. We say that ˆf ∈
C{x}[λ;q]
q
is q-Borel summable along [λ; q].
(2) Each element of DS ˆf := {[λ; q] : ˆf /∈C{x}[λ;q]
q
} will be called singu-
lar direction of ˆf.
(3) If DS ˆf is ﬁnite, ˆf is called q-Borel summable and we denote C{x}q
the set of q-Borel summable series.
Theorem 4.7 ([23, Thm. 1.2.1]). — Every generic q-Gevrey series is
q-Borel summable.
