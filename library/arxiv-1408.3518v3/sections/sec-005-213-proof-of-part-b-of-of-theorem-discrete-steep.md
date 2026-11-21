---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-005-213-proof-of-part-b-of-of-theorem-discrete-steep
section_title: "Proof of part (b) of of Theorem ??: Discrete steepest descent."
section_number: 2.1.3
pages: 9-11
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
toc_source: outline
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond — 13 sections: Front matter; Introduction.; Our Contributions"
---
We begin with
a series of lemmas. Note that the proof for the LP case follows exactly the same lines, since we do
not use integrality of the components in our arguments.
Lemma 4.
Let xk be a feasible solution, and let z be an associated steepest descent direction.
Then there is some augmentation direction g ∈G(A) from xk, with −c⊺g/∥g∥1 ≥−c⊺z/∥z∥1.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
10
Proof. There is a sign-compatible representation z = Pαigi via elements gi ∈G(A). Observe
that due to the sign-compatible representation, xk +αigi is also feasible for all i. (The components
of xk + αigi lie between those of xk and xk + z, implying that 0 ≤xk + αigi ≤u.) In other words,
all αigi are applicable augmentations at xk.
It remains for us to show that there exists some index i with −c⊺gi/∥gi∥1 ≥−c⊺z/∥z∥1. Assume
to the contrary that we have −c⊺gi/∥gi∥1 < −c⊺z/∥z∥1 for all i. This yields
−c⊺z = −
X
αic⊺gi
=
X
αi∥gi∥1
−c⊺gi
∥gi∥1
<
X
αi∥gi∥1
−c⊺z
∥z∥1
= −c⊺z
∥z∥1
X
αi∥gi∥1
= −c⊺z
∥z∥1
∥z∥1
= −c⊺z,
a contradiction.
□
Lemma 4 states that among all steepest-descent directions applicable at a feasible solution xk,
there is always one in G(A). Or in other words, the discrete steepest-descent rule is a steepest
descent rule as claimed in Theorems 1 and 2, parts(c).
Lemma 5.
Let xk be a feasible solution, let αs be a steepest-descent augmentation relative to
xk, and let xk+1 := xk + αs. Let βt be a steepest-descent augmentation relative to xk+1. Then we
have −c⊺s/∥s∥1 ≥−c⊺t/∥t∥1.
Proof. Suppose on the contrary that −c⊺s/∥s∥1 < −c⊺t/∥t∥1. First observe that αs + βt is an
applicable augmentation at xk. Moreover, we have
−c⊺(αs + βt) = α∥s∥1
−c⊺s
∥s∥1
+ β∥t∥1
−c⊺t
∥t∥1
> α∥s∥1
−c⊺s
∥s∥1
+ β∥t∥1
−c⊺s
∥s∥1
= (α∥s∥1 + β∥t∥1)−c⊺s
∥s∥1
,
≥(∥αs + βt∥1)−c⊺s
∥s∥1
,
and therefore
−c⊺(αs + βt)
∥αs + βt∥1
> −c⊺s
∥s∥1
.
This contradicts the fact that s was a steepest descent direction for xk.
□
Lemma 5 states that the steepness of steepest-descent augmentations never increases.
Lemma 6.
Let xk be a feasible solution and let α1z1,...,αjzj be the following steepest-descent
augmentations applied to xk. If z1 and zj do not have the same sign-pattern from {≤0,≥0}
n,
then we have −c⊺z1/∥z1∥1 > −c⊺zj/∥zj∥1.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
11
Proof. Assume on the contrary that −c⊺z1/∥z1∥1 ≤−c⊺zj/∥zj∥1. By monotonicity, Lemma 5,
we must have −c⊺z1
∥z1∥1 = −c⊺z2
∥z2∥1 = ··· =
−c⊺zj
∥zj∥1 . We conclude that
−c⊺Pj
i=1 αizi

= Pj
i=1 αi∥zi∥1
−c⊺zi
∥zi∥1
= Pj
i=1 αi∥zi∥1
−c⊺z1
∥z1∥1
=
Pj
i=1 αi∥zi∥1

−c⊺z1
∥z1∥1
>

Pj
i=1 αizi

1
−c⊺z1
∥z1∥1 ,
since z1 and zj do not have the same sign-pattern. This implies that
−c⊺Pj
i=1 αizi

∥Pj
i=1 αizi∥1
> −c⊺z1
∥z1∥1
.
As by assumption Pj
i=1 αizi is an applicable augmentation at xk. This contradicts the fact that z1
was a steepest-descent augmentation for xk.
□
Lemma 6 states that once the sign pattern of a steepest-descent augmentation strictly changes,
the steepness must decrease. This lemma has a surprising consequence if we only apply steepest-
descent directions from G(A):
Corollary 7.
For discrete steepest descent, no direction from G(A) is chosen twice as an
augmenting direction. Therefore, the number of steepest-descent augmentations needed to reach an
optimal solution is bounded by |G(A)| and thus is independent of b, c and the initial solution z0.
Proof. Let xk be a feasible solution and let α1z1,...,αjzj, with z1,...,zj ∈G(A), be the following
steepest-descent augmentations applied to xk with αi chosen maximally in each augmentation.
Moreover assume that zj = z1. Then, by Lemma 6, all intermediate augmentations must have the
same sign-pattern as z1, as otherwise the steepness of the augmentations would have dropped.
As all vectors α1z1,...,αjzj have the same sign-pattern, the components of xk + α1z1 + αjzj lie
between the components of xk and xk + Pj
i=1 αizi and therefore also between 0 and u. Thus,
xk + α1z1 + αkzj = xk + (α1 + αj)z1 is a feasible solution. This contradicts the fact that α1 was
chosen maximally.
□
