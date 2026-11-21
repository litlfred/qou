---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-007-42-proof-of-theorems-and
section_title: "Proof of Theorems ?? and ??"
section_number: 4.2
pages: 10-11
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
Theorem 3.1 is a special case of Theorem 3.4. This is because any probability measure µ on Bn may
be viewed as the law of a point process on the n element set [n], where the random counting measure
9
Z(ω) is deﬁned by Z(ω)(S) = P
j∈S ωj. Informally, the points of the process are the coordinates of
the ones in the sample ω. With this interpretation, the SCP on Bn is inherited from the SCP for
the point process Z, whence Theorem 3.4 with S = R (or any other standard Borel space containing
[n]) implies Theorem 3.1. It remains to prove Theorem 3.4.
Let (Ω, F, P) be a probability space on which is constructed the generalized sampling scheme
described in Lemma 3.3. Let Fj := σ(X1, . . . , Xj) and let
Mj := E(f | Fj) −Ef .
(4.19)
denote the martingale of sequential revelation. Applying the method of bounded diﬀerences is now
mostly a matter of bookkeeping. At a sample point where Xi = xi, 1 ≤i ≤k, the quantity Mj may
be written as the integral of f against the law of the point process
Zx1,...,xj +
j
X
i=1
δxi .
By the SCP, we have Zx1,...,xj ⊲Zx1,...,xj+1 whence
d∞
 
Zx1,...,xj +
j
X
i=1
δxi , Zx1,...,xj+1 +
j+1
X
i=1
δxi
!
≤2 .
By the Lipschitz assumption on f, it follows that |Mj+1 −Mj| ≤2.
We now apply the basic
Azuma-Hoeﬀding inequality (4.16) to {Mj/2}1≤j≤k yielding
P(f −Ef ≥a) = P
Mk
2
> a
2

≤exp

−a2
8k

.
□
4.3
