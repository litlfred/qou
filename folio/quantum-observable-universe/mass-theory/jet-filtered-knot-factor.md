**Conjecture.**
*The Bethe-Weizsäcker knot factor $a(Z, N)$ governing bulk binding evaluates directly from the jet-filtered character convergence of the nuclear quotient braid $\bar\beta$.*

At higher jet levels, the per-level invariant converges strictly to a topology-independent $q$-dimension-weighted average. The intermediate nucleon-by-nucleon normal forms align with distinct knot patterns, mapping odd $Z$ to trefoils and even $Z$ to Hopf links. Double-magic nuclei converge strongly to the unknot.

The full bulk knot factor $a(Z, N)$ equals the evaluated Jones polynomial of the nuclear quotient braid $J_{\bar\beta}(q)$. The quotient tracks exclusively the $A(A-1)/2$ inter-nucleon crossings, suppressing internal nucleon structure.

## Measured: $J_{\bar\beta}$ is not determined by the pair multiset for $A \ge 3$

The conjecture identifies $a(Z,N)$ with the Jones polynomial of the nuclear
quotient braid, and specifies that braid by its content — "the $A(A-1)/2$
inter-nucleon crossings". That is a **multiset**; a link needs a **word**, and
the non-adjacent pairs require bands that do not commute with the crossings they
span. Enumerating every ordering of the pairs, and both resolutions of the
averaged $pn$ letter (which is not a braid generator and must be resolved):

| nucleus | $A$ | orderings | distinct $J_{\bar\beta}$ |
|---|---:|---:|---:|
| $^3$H | 3 | 12 | **4** |
| $^3$He | 3 | 12 | **4** |
| $^4$He | 4 | 1440 | **30** |

So $a(Z,N)$ as written is not a function of $(Z,N)$. This is the same
ill-posedness that retired the all-pairs bond model
([the ordering ambiguity](#prop:canonical-closure-torus-chain)), measured here
on the quotient braid itself rather than inherited from the $3A$-strand word.

At $A = 2$ the specification *is* well posed — $A(A-1)/2 = A-1 = 1$, so there is
one crossing on two strands and no ordering to choose — and its closure is the
**unknot** for every bond type and both resolutions. The jet level therefore
multiplies the deuteron's knot factor by exactly $1$: where it can be evaluated,
it contributes nothing.

Nothing here retracts the conjecture. It says what a reformulation must supply:
a rule fixing the full word rather than its crossing content alone.
