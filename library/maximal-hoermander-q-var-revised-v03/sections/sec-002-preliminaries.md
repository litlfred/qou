---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates"
section_id: sec-002-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 8-9
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
toc_source: outline
doc_brief: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates — 12 sections: Front matter; Introduction; R-boundedness"
---
Preliminaries
In this section, we recall the notions on Banach space geometry and functional calculus that we
need in this paper. For the Hörmander functional calculus, we only need few facts that we will
use as an abstract blackbox in the remainder of the article.
2.1
R-boundedness
Deﬁnition 2.1 Let X, Y be Banach spaces. We recall that a family τ ⊆B(X, Y ) is called
R-bounded, if for a sequence (εk)k of independent Rademacher random variables, taking the
value 1 and −1 with equal probability 1
2, a constant C > 0, any n ∈N, any x1, . . . , xn ∈X and
any T1, . . . , Tn ∈τ, we have
E

n
X
k=1
εkTkxk

Y
⩽CE

n
X
k=1
εkxk

X
.
In this case, the inﬁmum over all admissible C is denoted by the R-bound R(τ).
Remark 2.2 Clearly, R({T}) = ∥T∥B(X,Y ) if τ = {T} is a singleton. In general, we have
R(τ) ⩾supT ∈τ ∥T∥B(X,Y ) above. If X and Y are (isomorphic to) Hilbert spaces, then a family
τ ⊂B(X, Y ) is R-bounded if and only if τ is bounded, the latter meaning that supT ∈τ ∥T∥B(X,Y ) <
∞.
Deﬁnition 2.3 Let X be a Banach space and (εn)n be a sequence of independent Rademacher
variables.
7
1. We say that X has Pisier’s property (α) if there are constants c1, c2 > 0 such that for
any array (xn,k)N
n,k=1 in X,(ε′
k)k a second sequence of independent Rademacher variables
independent of (εn)n, and (ε′′
n,k)n,k a doubly indexed sequence of independent Rademacher
variables, the following equivalence holds:
c1EE′

N
X
k,n=1
εnε′
kxn,k

X
⩽E′′

N
X
k,n=1
ε′′
n,kxn,k

X
⩽c2EE′

N
X
k,n=1
εnε′
kxn,k

X
.
2. Let p ∈[1, 2] and q ∈[2, ∞]. We say that X has type p if for some constant c > 0 and
any sequence (xn)N
n=1 in X, we have
E

N
X
n=1
εnxn

X
⩽c
 N
X
n=1
∥xn∥p
! 1
p
.
In this case, we write type (X) = p (not uniquely determined value). We say that X has
cotype q if for some constant c > 0 and any sequence (xn)N
n=1 in X, we have
 N
X
n=1
∥xn∥q
! 1
q
⩽cE

N
X
n=1
εnxn

X
.
In this case, we write cotype (X) = q (not uniquely determined value).
