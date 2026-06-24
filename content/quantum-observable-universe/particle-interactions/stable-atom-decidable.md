**Proposition.**
*[Stability of an atom](#def:stable-atom) at fixed $q$ is
**decidable**: there is an algorithm that, given an atom-knot $K$
of type $(Z, N)$ and a substrate parameter $q$ in the generic
locus, returns `True` if $K$ is stable at $q$ and `False` otherwise.*

*

**Complexity.**
*The bottleneck is step 4 (ILP feasibility) — exponential in $N$
in general, polynomial in fixed dimension.  For nuclear
applications ($N = O(k_{\max}^2)$ ~ tens of primitive operators),
ILP is tractable.*
