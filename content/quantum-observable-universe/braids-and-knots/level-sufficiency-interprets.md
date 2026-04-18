**Remark.**
*[Level sufficiency](#prop:level-sufficiency) is the formal
justification for a **hierarchical default-coarse computational
strategy** across the confinement stack.  The confinement hierarchy
has at least four levels relevant to this paper:*

| *Level* | *Strand object* | *Default count $n_0$* |
|---|---|---|
| *Compound atom / molecule* | *atom-knot* | *# atoms* |
| *Atom* | *nucleon-knot* | *# nucleons $A$* |
| *Nucleon* | *quark-knot* | *3* |
| *Quark* | *elementary* | *1* |

*At each level, [prop:level-sufficiency](#prop:level-sufficiency)
implies that any trace-class invariant — mass
$\mathfrak{m}(K)$, binding $B(K)$, Jones polynomial — is **exact**
at the coarsest representation satisfying
$k_{\max}(K, q, n_0) \le n_0$.*

**Default-coarse rule.**
*Every computational pipeline (mass, binding, stability, decay
channel) should:*

1. *Start at the coarsest level at which $K$ is naturally expressed
   (atoms as nucleon-strand braids, molecules as atom-strand
   braids).*
2. *Read $k_{\max}(K, q, n_0)$ from the witness data
   ([confinement level](#def:confinement-level) paragraph "per-atom
   truncation").*
3. *If $k_{\max} \le n_0$, compute $\mathrm{tr}_M$ there and halt.*
4. *If $k_{\max} > n_0$, unfold one level and repeat.*

**Unfolding triggers.**
*Only two categories of structure force unfolding at a given level:*

- ***Magic shell closure.** *Atoms at $A \in \{2, 8, 20, 28, 50, 82, 126\}$
  have $k_{\max}(K, q, A)$ jumping above $A$ because the closed-shell
  structure requires additional partition content to encode
  (see [confinement level](#def:confinement-level), magic
  configurations).  These atoms must be computed at quark level
  ($3A$ strands).*
- ***SDP cross-channel demand.** *When a cross-channel SDP
  constraint couples two Wedderburn blocks $\lambda_1, \lambda_2$
  with $\max(|\lambda_1|, |\lambda_2|) > n_0$, the coarse
  representation cannot express the coupling and unfolding is
  required.*

*Non-magic atoms and molecules without SDP couplings are computed
at their natural coarse level — this is not an approximation, it is
the **minimal exact representation**.  The earlier remark
[nucleon-as-unit justification](#rem:confinement-nucleon-unit)
is the special case of this proposition at the atom→nucleon
transition; [prop:level-sufficiency](#prop:level-sufficiency)
generalises it uniformly across the full hierarchy and any
knot-operator content.*

**Computational implication.**
*For a non-magic atom with $A$ nucleons, the Hecke algebra
dimension drops from $|H_{3A}(q)| \sim (3A)!$
(quark-level) to $|H_A(q)| \sim A!$ (nucleon-level).  Partition
enumeration drops from $p(3A)$ to $p(A)$: for $A = 20$, a factor of
$p(60)/p(20) \approx 966{,}000/627 \approx 1540$. Default-coarse
computation is not a performance heuristic — it is the
computational content of [prop:level-sufficiency](#prop:level-sufficiency).*
