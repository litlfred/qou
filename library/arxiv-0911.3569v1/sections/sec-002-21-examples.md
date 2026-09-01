---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-002-21-examples
section_title: "Examples."
section_number: 2.1
pages: 2-3
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
Proposition 2.1 (Proposition 2.4 of [1]) . Fori∈ [m], let Ai be an n-by-n matrix
and let xi be an indeterminate, and let B be an n-by-n matrix. If Ai is positive
semideﬁnite for all i∈ [m] and B is Hermitian then
f(x) = det(x1A1 +x2A2 +··· +xmAm +B)
MULTIVARIATE STABLE POLYNOMIALS 3
is real stable.
Proof. Let f denote the coeﬃcientwise complex conjugate of f. Since Ai =AT
i for
all i∈ [m], and B = BT, it follows that f = f, so that f∈ R[x]. By Hurwitz’s
Theorem and a routine perturbation argument, it suﬃces to prove that f is stable
when each Ai is positive deﬁnite. Consider any z = a + ib∈ Hm, with a, b∈ Rm
and bi > 0 for all i∈ [m] (abbreviated to b> 0). Now Q =∑m
i=1biAi is positive
deﬁnite, and hence has a positive deﬁnite square-root Q1/2. Also note that H =∑m
i=1aiAi +B is Hermitian, and that
f(z) = det(Q) det(iI +Q−1/2HQ−1/2).
Since det(Q)⁄= 0, iff(z) = 0 then−i is an eigenvalue ofQ−1/2HQ−1/2, contradict-
ing the fact that this matrix is Hermitian. Thus, f(z)⁄= 0 for all z∈ Hm. That is,
f is stable. □
Corollary 2.2. LetQ be an n-by-m complex matrix, and let X = diag(x1,...,x m)
be a diagonal matrix of indeterminates. Then f(x) = det(QXQ†) is real stable.
Proof. Let Q = (qij), and for j∈ [m] let Aj denote the n-by-n matrix with hi-th
entryqhjqij. That is, Aj =QjQ†
j in whichQj denotes the j-th column of Q. Since
each Aj is positive semideﬁnite and QXQ† =x1A1 +··· +xmAm, the conclusion
follows directly from Proposition 2.1. □
