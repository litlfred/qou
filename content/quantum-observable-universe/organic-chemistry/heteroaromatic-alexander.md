**Conjecture.**
The Alexander polynomial of a heteroaromatic ring is identical to
that of the all-carbon analogue with the same ring size $N$:

$$
  \Delta_{T(2,N)}^{\text{heteroaromatic}}(q)
   = 
  \Delta_{T(2,N)}^{\text{all-carbon}}(q),
$$

independent of the species of vertex atom (C, N, O, S, NH, …).

**Examples.**

| Ring size $N$ | Members of the equivalence class |
|:---:|:---|
| $5$ | cyclopentadienyl, furan, thiophene, pyrrole, imidazole, pyrazole |
| $6$ | benzene, pyridine, pyrazine, pyrimidine, pyridazine, $1,2,4$-triazine |

The conjecture predicts that all members of each row share the
threading-link Alexander polynomial — and hence share the
*topological* ring-closure barrier
([ring closure barrier (quantitative)](#prop:ring-closure-barrier-quantitative))
and the *topological* hydrogen capacity
([hydrogen capacity](#prop:hydrogen-capacity)).

**Empirical verification.**
The witness `pyridine-furan-alexander.witness.json` confirms
$\Delta_{T(2,N)}(q_{0})$ equality across all 11 listed molecules;
the all-carbon Alexander polynomial depends only on $N$, by
construction.

**What the conjecture does *not* claim.**
Heteroatom substitution **does** change:

- aromaticity strength (pyridine $<$ benzene; furan $<$ pyrrole);
- basicity (pyridine $\gg$ pyrrole);
- bond enthalpies (C=O $\gg$ C=C);
- redox behaviour and reaction selectivity.

These differences arise from **per-atom Hopf weights** — a future
extension in which each vertex carries an element-dependent local
weight that modulates the global Alexander invariant.  The
conjecture asserts only that the **bare** topological invariant
$\Delta_{T(2,N)}(q)$ is heteroatom-independent.

**Strategy for proof.**
The Alexander polynomial of an oriented link depends only on the
oriented homotopy type of its complement.  A heteroaromatic ring
has the same backbone graph (cyclic $N$-vertex) as the all-carbon
analogue and thus the same threading-link complement up to
oriented homeomorphism.  A formal proof would proceed by
constructing a homeomorphism of the link complements that respects
the orientation classes; this is a standard application of Wirtinger
presentations and is left for the formalisation skill.
