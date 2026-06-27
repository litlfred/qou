An atom $\mathcal{A}(p,n)$ is a **noble gas** if and only if
its electron cloud $p \cdot T_{2,3}$ decomposes as a disjoint
union of closed sub-Hopf links — that is, every shell is
topologically **full of curls**.

**Statement.**
Let $\mathcal{A}(p,n)$ be a stable atom
([stable nucleus](#def:stable-nucleus)) with electron cloud
$\mathcal{E} = p \cdot T_{2,3}$.  Then $\mathcal{A}$ is
chemically inert (noble) if and only if there exists a
partition $\mathcal{E} = S_1 \sqcup S_2 \sqcup \cdots \sqcup S_k$
such that:

1. **Closure**: each $S_i = 2n_i^2 \cdot T_{2,3}$ is a
   closed sub-Hopf link at level $n_i$ — the trefoil chain
   within $S_i$ admits no additional linking without
   increasing the total linking number.

2. **Exhaustion**: every electron belongs to some $S_i$;
   there are no unlinked trefoils left over.

3. **Monotone nesting**: $n_1 < n_2 < \cdots < n_k$, and the
   linking of $S_{i+1}$ threads through $S_i$ without
   disrupting its closure.

The six noble gases are then characterised by cumulative
shell closure:

See [Table](#tbl:noble-gas-characterization-table-data).

**Relation to ionization energy.**

The crossing energy
([crossing energy](#def:crossing-energy)) of a closed sub-link
is a **local maximum** among atoms in the same period.  To
remove an electron from a noble gas, one must break a crossing
in a fully interlocked chain, which costs more energy than
removing an electron from an incomplete sub-link (where some
crossings are unmatched).  This explains the well-known
experimental pattern: noble gases sit at ionization-energy
peaks across each row of the periodic table.

**Relation to electron affinity.**

Dually, a noble gas has near-zero electron affinity because
attaching a new trefoil would require starting a fresh
sub-link at level $n_{k}+1$.  The new trefoil is only weakly
Hopf-linked to the outermost closed shell — the linking
number is minimal, so the binding energy is negligible
compared to thermal fluctuations.

**Proof sketch.**

The forward direction (closed partition $\Rightarrow$ inertness)
follows from the
[Hopf stability proposition](#prop:torus-hopf-stability):
a closed sub-Hopf link is stable under small perturbations of
the linking matrix, so no single crossing change can open or
close a linking site.

The reverse direction (inertness $\Rightarrow$ closed partition)
uses the [shell conjecture](#rem:electron-shells-hopf):
if the electron cloud is *not* a union of closed sub-links,
then at least one trefoil has an available linking site, and
the atom can lower its energy by capturing an additional
electron — contradicting chemical inertness.
