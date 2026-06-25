Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a
ring $R$ ([quantum observable universe](#def:quantum-observable-universe)).  Set
$A_0 = A$.  *Inductively*, define
$A_{n+1} = J^1(A_n)$ as the
([jet prolongation](#prop:jet-prolongation)) of the Frobenius--Hopf
object $A_n$.

The *brane relation* is the following recursive structure:

1. Each jet object $A_n$ serves as the base object for the next level;
   $A_n$ is the *brane* of $A_{n+1}$.
2. At each level, the comultiplication $\Delta_n$ on $A_n$ encodes
   the $n$-th level connection, inherited from the Frobenius--Hopf
   structure by [jet prolongation](#prop:jet-prolongation).

The *recursive brane tower* is the sequence
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
in $\mathbf{C}$, where each embedding is the canonical inclusion
$A_n \hookrightarrow J^1(A_n) = A_{n+1}$ via the unit section.

The mathematical content of this construction is the iterated jet
prolongation $A_{n+1} = J^1(A_n)$ alone.  We use the term *brane* for
each localized layer $A_n$ — reading it physically as a geometric
boundary that bounds the level-$n$ internal degrees of freedom, by
analogy with the extended objects of string theory — and we reserve
the qualifier *Yekutieli* for the lifting condition of
\cite{yekutieli2010} that governs when level $n$ extends to level
$n+1$, together with the nonabelian multiplicative integration of
\cite{yekutieli2015} used to integrate over the tower.  Those
Yekutieli results control how the levels assemble; they are not the
prolongation construction itself, which is the Kähler-differential jet
object defined above.  We accordingly write simply *(recursive) brane
tower* — not *Yekutieli brane tower* — for the sequence.
