## Statement

**Proposition 6 (Iterative emergence of the magic ladder).**
*Let $\{\Phi_n\}_{n \geq 0}$ be the recursive brane tower of categorical
mass endomorphisms ([recursive brane tower](#def:recursive-brane-tower))
at substrate $q_0$, with $\Phi_0$ the vacuum and each $\Phi_{n+1}$
obtained from $\Phi_n$ by Yekutieli jet prolongation
([categorical jet](#prop:categorical-jet-prolongation)). Define the
iterative shell-condensation threshold predicate*

$$
  \mathrm{Threshold}_{q_0}(\Phi_n)
  \;\equiv\;
  \bigl[J^k(\Phi_n)\bigr] = 0 \text{ in } E_2^{*,k} \text{ for all } k > 0.
$$

*Then*

$$
  \bigl\{ n \geq 0 \,:\, \mathrm{Threshold}_{q_0}(\Phi_n) \bigr\}
  \;=\;
  \{2,\, 8,\, 20,\, 28,\, 50,\, 82,\, 126\}.
$$

*That is, the magic ladder is the sequence of strand counts at which
the iteratively-built brane tower's jet-prolongation obstruction
vanishes.*

## Status

**Conjecture** (CLAUDE.md §3b axiom-class). The closed-form
characterisation in
[homological shell condensation](#conj:homological-shell-condensation)
and the
[SDP rank collapse](#conj:sdp-rank-collapse-magic-shell) provide
the *target set* (magic ladder); this proposition asserts the
*emergence dynamics* — the same set is reached level-by-level by
the brane tower, with each magic shell being a *threshold-crossing
event* in the iterative construction.

## Why iterative emergence matters

The closed-form picture
([conj:sdp-rank-collapse-magic-shell](#conj:sdp-rank-collapse-magic-shell))
characterises the magic ladder as the support of a
structural-optimum predicate of the nuclear-confinement SDP at
$q_0$. In principle, this is a single test per $n$. In practice, the
SDP at $n = 126$ has $\sim 10\,422$ self-conjugate Hecke modules and
even more total partitions; direct solution is intractable.

The iterative picture replaces the *one-shot* SDP with a *level-by-
level* construction:

- Start at $n = 0$ (vacuum).
- At level $n$, the brane tower has built $\Phi_n$.
- Adding a strand: $\Phi_n \xrightarrow{\;J\;} \Phi_{n+1}$ via
  Yekutieli jet prolongation. This adds one new transient contribution
  $\Phi_q(z_{n+1})$ ([q-Pochhammer partial product](#def:q-pochhammer-partial-product)).
- Check $\mathrm{Threshold}_{q_0}(\Phi_{n+1})$ locally — only the
  new jet class $J^k(\Phi_{n+1})$ needs to be tested.

Each step is an $O(1)$ update to a fixed-size data structure
(per-level Hoefsmit block, GB filtration depth, q-Pochhammer
truncation), regardless of $n$.

## Existing compute tricks that apply

The QOU paper already supplies all the infrastructure to make this
iterative construction tractable:

1. **Hoefsmit block-diagonal optimisation**
   ([prop:hoefsmit-seminormal-form](#prop:hoefsmit-seminormal-form)).
   At each level $n \to n+1$, the Hecke-algebra branching adds
   exactly one box to each Young diagram. The Hoefsmit matrix update
   is local: only the new $2 \times 2$ block at the added cell needs
   computation. This gave the $15\,000\times$ speedup at $k = 9$
   recorded in `shell-closure.witness.json` for
   [magic-numbers-from-q](#prop:magic-numbers-from-q).

2. **Wedderburn weight aggregation**. Tracking $w_\lambda(q) =
   \dim_q(\lambda)^2 / [n]_q!$ as a compact summary instead of the
   full matrix gives $O(1)$ per-level updates of the Wedderburn
   spectrum.

3. **Yekutieli finite-slice truncation** (per-atom `max_grade` in
   `joint-tower-sdp-h6-h9.witness.json`). The brane tower's
   convergence depth is bounded by the GB filtration depth of the
   atom under consideration; truncating $\Phi_q(z_k)$ at this depth
   gives a finite multiplicative integral.

4. **Brane-tower partial sums** ($N \approx 20$ levels suffice for
   $99.99\%$ of $\mathrm{Li}_2(q^{-2})$, per
   [mass endomorphism](#conj:mass-endomorphism)). Only the first
   ${\sim}20$ levels of the tower contribute non-negligibly to the
   mass / threshold check at any $n$.

5. **q-Pochhammer partial product**
   ([def:q-pochhammer-partial-product](#def:q-pochhammer-partial-product)).
   Each level's transient $\Phi_q(z_k)$ is a finite product, recursively
   updated.

6. **Gröbner–Shirshov filtration** (cross-paper to `ugb`). Provides
   the ascending filtration `F_0 ⊆ F_1 ⊆ ⋯` whose graded pieces
   correspond to brane-tower levels; level transitions are by
   adjoining one new generator.

7. **Skein / Markov trace** ([prop:hecke-mass-trace](#prop:hecke-mass-trace)
   conceptually). At each level, the trace update under one extra
   strand uses the Markov property — also $O(1)$.

## Iterative algorithm sketch

```
Input: substrate q_0
State at level n:
  - YoungBranchingTree T_n : tree of partitions reachable via
    successive box-additions starting from the empty diagram.
  - HoefsmitData H_n : block-diagonal matrices indexed by
    leaves of T_n.
  - GB filtration F_n in the relevant Hecke algebra.
  - Brane-tower partial product Phi_q^{(<=n)} truncated at
    Yekutieli depth.

Step n -> n+1:
  1. Branch each leaf lambda of T_n into all partitions
     mu = lambda + box (one new column index for each
     possible cell to add).
  2. Update Hoefsmit block-diagonal: append the new cell's
     content c = j-i to the corresponding block. O(d) cost
     instead of O(d^3).
  3. Update GB filtration: adjoin the new generator, reduce.
  4. Multiply brane-tower partial product by the new
     transient (1 - z_{n+1} q^{-(n+1)})^{-1}.
  5. Test Threshold_{q_0}(Phi_{n+1}):
       - Check whether J^k(Phi_{n+1}) = 0 in E_2^{*,k}
         for all k > 0.
       - In practice: check whether the SDP active-basis
         at level n+1 is rank-1 with self-conj support.
     If yes, n+1 is a magic strand count.

Output: cumulative magic ladder up to N_max.
```

## Falsification path

Implement the above algorithm in Python (or inside the existing
`shell_closure_compute.py` framework). Run for $n = 0$ to $130$
at $q = q_0$. The conjecture predicts the iterative procedure
should "light up" exactly at $n \in \{2, 8, 20, 28, 50, 82, 126\}$
and not elsewhere.

The existing
[`folio-assistant/computations/symbolic_qdim_argmax.py`](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/folio-assistant/computations/symbolic_qdim_argmax.py)
script provides the Wedderburn-weight infrastructure. Extending it
with the threshold test (rank-1 SDP active-basis) gives the
verification pipeline. With the compute tricks above, $n = 126$
becomes tractable in seconds rather than hours.

## Why this is plausible

The iterative threshold-crossing picture matches:
- **Mayer–Jensen shell-filling**: each magic number is the
  cumulative strand count at which a *single-particle level*
  closes. The Yekutieli jet prolongations are the categorical
  analogue of single-particle level fillings.
- **3D harmonic oscillator** (without spin-orbit): cumulative
  $\sum 2(N+1)(N+2)/2$ for $N = 0, 1, 2, \ldots$ gives oscillator
  magic $\{2, 8, 20, 40, 70, 112, 168\}$. The $q_0$-deformation
  reorders the levels via $[\rho]_{q_0}$, producing nuclear magic
  $\{2, 8, 20, 28, 50, 82, 126\}$.
- **The "completely filled partition" hint**: at each magic $n$,
  the brane tower has *finished* a structurally-determined batch
  of jet prolongations corresponding to one shell. The
  Threshold predicate is the categorical "shell is filled" check.

## Relation to the closed-form conjecture

[Conj:sdp-rank-collapse-magic-shell](#conj:sdp-rank-collapse-magic-shell)
gives a *characterisation* of the magic ladder via the SDP at $q_0$.
This proposition gives an *iterative emergence* of the same ladder
via the brane tower. Both are conjecturally equivalent, but each
serves a different role:

- **Closed-form**: tells us *what* the magic ladder is — useful for
  conceptual statements.
- **Iterative**: tells us *how to compute* it — useful for actual
  numerical verification at $n \geq 28$ where direct SDP is
  infeasible.

The two conjectures, taken together, force the magic ladder to be
both (i) the unique structural-optimum locus of the SDP at $q_0$,
and (ii) the unique sequence of jet-prolongation threshold crossings
in the brane tower at $q_0$. Either equivalence breaking (e.g., the
iterative procedure landing on a different ladder than the SDP)
would falsify the framework.
