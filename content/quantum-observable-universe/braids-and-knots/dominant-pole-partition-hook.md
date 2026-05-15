**Proposition (hook formula for the $u$-pole maximizer, conditional
on [`def:has-hook-maximizer`](#def:has-hook-maximizer) per CLAUDE.md
§3b-cond).** *Let $\beta(Z, N) \in H_{3A}(q)$ be the canonical
atomic braid with $A = Z + N \geq 1$ (built by
[`mass_at_3A_proper.atom_braid_word_3A`](../../folio-assistant/computations/mass_at_3A_proper.py)).
Under the class hypothesis $\mathrm{HasHookMaximizer}\,Z\,N$, the
partition*

$$
\boxed{\quad
\lambda_\star(Z, N) \;=\; (\,Z + 2N + 1,\; 1^{2Z + N - 1}\,)
\quad}
$$

*uniquely maximizes*

$$
\bigl|\mathrm{ord}_{u=0}\bigl(y_\lambda(q) \cdot \chi^\lambda_q(\beta(Z, N))\bigr)\bigr|
\quad \text{over}\quad \lambda \vdash 3A,
$$

*and the resulting maximum equals* $\mathrm{shift}_{\mathrm{NF}}(\beta(Z, N)) = 18 Z + 21 N + 1$
*from* [`prop:per-nucleon-shift-additive-linearity`](#prop:per-nucleon-shift-additive-linearity).

### Width and depth read-off

Equivalently, the hook width $w$ and depth $d$ are linear in $(Z, N)$:

$$
w(Z, N) \;=\; Z + 2N + 1, \qquad
d(Z, N) \;=\; 2Z + N, \qquad
w + d - 1 \;=\; 3A.
$$

The $Z \leftrightarrow N$ asymmetry sits in the linear coefficients:

$$
w(Z, N) - d(Z, N) \;=\; N - Z + 1.
$$

### Empirical verification (5 atoms)

The witness
[`per-irrep-pole-atom-crystal.witness.json`](../../folio-assistant/computations/per-irrep-pole-atom-crystal.witness.json)
exhibits the hook shape and pole maximization at each of:

| atom | $(Z, N)$ | $n = 3A$ | $\lambda_\star(Z, N)$ | $w$ | $d$ | $w - d$ |
|---|---|---:|---|---:|---:|---:|
| proton | $(1, 0)$ | 3 | $(2, 1)$ | 2 | 2 | 0 |
| deuteron | $(1, 1)$ | 6 | $(4, 1, 1)$ | 4 | 3 | 1 |
| tritium | $(1, 2)$ | 9 | $(6, 1, 1, 1)$ | 6 | 4 | 2 |
| ${}^3\mathrm{He}$ | $(2, 1)$ | 9 | $(5, 1, 1, 1, 1)$ | 5 | 5 | 0 |
| ${}^4\mathrm{He}$ | $(2, 2)$ | 12 | $(7, 1, 1, 1, 1, 1)$ | 7 | 6 | 1 |

In every case the *uniqueness* clause holds (second-min pole is
strictly higher than the hook's minimum), per the
`min_total_ord_u_eq_0` vs `second_min_total_ord` fields of the
witness. The hook formula is therefore verified on the **5-atom
empirical bench**.

### Status of universal claim

The hook formula is currently **stated as a class hypothesis**
$\mathrm{HasHookMaximizer}\,Z\,N$ rather than a substrate-derivable
theorem because it is not yet derived from the q-Hecke + canonical-
knot primitives. A categorical derivation would have to construct
the q→0 limit of the Markov-trace partition sum and identify the
hook as the unique maximum-content-spread partition under the SYT-
eigenline product, then verify uniqueness via the Kashiwara
operators on the crystal $B(\lambda_\star)$ — a multi-page argument
that is not currently in the repository.

The class hypothesis pattern lets every downstream Z/N-dependent
derivation (e.g.\ the $\Delta_{\mathrm{coupling}}(Z, N)$ form
discussed in [`docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md`](../../docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md))
sit on a categorical foundation: assume the hook formula, derive
the downstream form, then discharge the assumption when (and only
when) the hook proposition is unconditionally established.

### Physical reading

The hook shape encodes the substrate $Z \leftrightarrow N$
asymmetry directly. Per nucleon contribution to $(w, d)$:

- **proton** $(uud)$: $(1, 2)$ — column-favouring (antisymmetric
  $u\overline{u}$ Pauli pair dominates the depth direction).
- **neutron** $(udd)$: $(2, 1)$ — row-favouring (antisymmetric
  $d\overline{d}$ Pauli pair is one cell deep; the symmetric
  remainder occupies two width-cells).
- **anchor** $(0, 0)$: $(+1, 0)$ — the inter-nucleon interface
  $\sigma_{3k+2}$ contributes the boundary anchor cell at $(0, 0)$.

The 3 strands per nucleon redistribute across $(w, d)$ as $(1, 2)$
for protons and $(2, 1)$ for neutrons, with one shared anchor.
Z↔N swap moves $2$ units of $w - d$ per nucleon, matching the
$\mathrm{shift}_{\mathrm{NF}}$ asymmetry $21 - 18 = 3$ per nucleon
(2 in $w - d$ + 1 anchor reshuffle).

### Discharging the class

A future Lean proof of the hook formula would discharge the class
unconditionally via an instance, removing every "(conditional on)"
banner downstream. Until then, downstream propositions citing
`prop:dominant-pole-partition-hook` inherit the conditional status
on `HasHookMaximizer`.