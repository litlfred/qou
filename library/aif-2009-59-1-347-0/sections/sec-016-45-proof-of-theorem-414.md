---
doc_id: aif-2009-59-1-347-0
doc_title: "L’INSTITUT FOURIER"
section_id: sec-016-45-proof-of-theorem-414
section_title: "Proof of Theorem 4.14"
section_number: 4.5
pages: 45-46
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "ANNALESDEL’INSTITUTFOURIER ANNALES L’INSTITUT FOURIER — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
We start by proving the following preparatory result:
Proposition 4.24. — If ˆf ∈xC[[x]] is a generic q-Gevrey series, then
its q-Borel transform belongs to H.
Proof. — Let ∆ be a linear analytic q-diﬀerence operator such that ∆ ˆf =
g ∈ xC{x}. We know that ∆ admits an analytic factorization ( cf. [20,
Prop. 5.1.4], [ 18, Thm. 1.2.1]):
(4.11)
∆ = (xσq −λ1)h1(xσq −λ2)h2...(xσq −λn)hn, λ j ∈ C, hj ∈ C{x}, hj(0) = 1.
We suppose that we have chosen n minimal and let us prove the statement
by induction on n. We consider ﬁrst of all the case n = 1: we suppose that
(xσq −λ1)h1 ˆf = g, with Bq(g) ∈ H (7) . This implies that Bq(h1 ˆf ) ∈ H,
sinceBq((xσq −λ1)h1 ˆf ) = (qξ −λ1)Bq(h1 ˆf ). Therefore Bq( ˆf ) ∈H, in fact
Bq( ˆf ) = Bq(h−1) ∗q Bq(h1 ˆf ), with Bq(h−1
1 ) ∈ Eq and Bq(h1f ) ∈H.
Forn> 1, the inductive hypothesis implies that Bq((xσq −λn)hn ˆf ) ∈H,
and hence that Bq( ˆf ) ∈H. □
Proof of Theorem 4.14. — Applying Theorem 4.20 to Bq( ˆf ), we can
write ˆf as follows:
ˆf =f0 + ˆe0 +f1ˆe1 +... +fnˆen,
where f0,...,f n ∈ xC{x}, Bq(ˆe0) ∈ K and, for i = 1 ,..., n, Bq(ˆei) =
1
(ξ−λi)νi . So it is enough to prove Theorem 4.14 for a modiﬁed Tschakaloﬀ
series ( cf. [12, Prop. 1.4.2]), i.e. under the assumption Bq( ˆf ) = 1
(ξ−λ)n .
By replacing ξ by −λξ, we can suppose that λ = −1. The case n = 1
corresponds exactly to the Tschakaloﬀ divergent series ˆE, and the result is
stated in Proposition 4.16. If n> 1, by considering
ˆf (x) = (−1)n−1
(n − 1)!xn−1∂n−1∂an−1 ˆE(ax)‖a=1,
(7) Notice that we are assuming that Bq(g) ∈ H and not Bq(g) ∈ Eq.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 391
we can easily deduce the wanted result by the help of the dominated con-
vergence theorem.
Concerning the second part of the statement of Theorem 4.14, the de-
composition above allows once again to reduce to the case of the Tschakaloﬀ
series. The dominated convergence theorem applies with no diﬃculties to
this explicit case ( cf. Remark 4.13). □
