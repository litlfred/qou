
By [Theorem 4.17, yekutieli2010], any central extension of gerbes
banded by an abelian sheaf on a ringed space satisfies the lifting
criterion: an object in the base gerbe admits a lift to the total gerbe
if and only if its obstruction class in $H^2$ vanishes. One verifies that
the brane tower fits this setup.

**Step 1 (jet prolongation is a gerbe).** By
[jet prolongation](#prop:jet-prolongation), the assignment
$(\mathbf{C}, A, \tau) \mapsto (\mathbf{C}, J^1(A), \tau', q)$ sends
a QOU at level $n$ to a QOU at level $n+1$. The stack of QOU-lifts
over a fixed base QOU is a gerbe: non-empty (constructed from
$J^1(A)$), and two lifts differing by an automorphism of $J^1(A)$
over $A$ are 2-isomorphic.

**Step 2 (banding by $\mathcal{B}$).** The automorphisms of a
QOU-lift over a fixed base are parameterised by the abelian sheaf
$\mathcal{B}$ of
[quantum characteristic classes](#def:quantum-characteristic-classes):
an automorphism of $J^1(A)$ compatible with the Frobenius--Hopf
structure and the fibre functor is determined by a global section
of $\mathcal{B}$. Hence the gerbe is banded by $\mathcal{B}$ in the
sense of Yekutieli 2010 §1.3.

**Step 3 (obstruction matches $\kappa_n$).** Under the banding of
Step 2, the Giraud obstruction class of the level-$(n{+}1)$ gerbe
over the level-$n$ gerbe lives in $H^2(M; \mathcal{B})$ and coincides
with the categorical characteristic class $\kappa_n$ of the brane
tower at level $n$ — both arise from the same 2-cocycle classifying
the $\mathcal{B}$-torsor structure on the set of lifts.

**Conclusion.** Theorem 4.17 of yekutieli2010 applies with
obstruction class $\kappa_n$; the lift exists iff $\kappa_n = 0$,
which is precisely the categorical lifting condition.
