---
# qou-wg3c
title: 'GAP: three inconsistent Wigner coefficients, and the [5]_q! block conflicts with the k=5 row cap'
status: todo
type: task
priority: normal
created_at: 2026-10-11T07:35:00Z
updated_at: 2026-10-11T08:45:00Z
parent: qou-8lxd
---

Found 2026-10-11 while testing whether the Wigner term derives `a_asym`
(bean `qou-nxvg`; it does not). Opened on owner instruction.

## The three coefficients (proton q0, mp.dps 30)

    prop:wigner-np-pairing             Delta_(2,2) = m_e [3]_q [2]_q^2      6.2893 MeV
    prop:wigner-coefficient-derivation [5]_q! m_e                           67.1008 MeV
    prop:wigner-2-coefficient          C_(2,2) = w h/2, w = dim_q^2/[4]_q!  0.017357 (dimensionless)

`dim_q(2,2) = 2.04371`, `w_(2,2) = 0.166049`, `h = q - 1/q`. All three are
named "the Wigner coefficient" for `-Delta_W T(T+1)/A`. They differ in value
and in q-form, so at most one can be the coefficient of that term, unless
they are proven to be different objects (e.g. a dimensionless shadow price
vs its MeV realisation) with a stated map between them.

## The k = 5 conflict

`prop:wigner-coefficient-derivation` sets the scale at Hecke level k = 5
(`[5]_q!`). Under convention D the row cap `l(lambda) <= 2` admits no
self-conjugate shape at k >= 5 (`qou-a5jk`, `no_selfConj_two_row_of_five_le`,
sorry-free), and `w = 0 -> C = 0 -> u* = 0` (`qou-w06d`). So a level-5
self-conjugate Wigner shadow price is zero. The block's proof asserts the
k = 5 scale ("set by the Hecke-level scale at k = 5") and supports it by
agreement with a fitted 68.9 MeV, which is not a derivation.

## Open (owner decision before any edit)

1. Which, if any, of the three is the canonical Wigner coefficient.
2. Whether the [5]_q! block should be scoped as superseded by the k=4 cap.

Nothing edited. Status stays todo: this tracks an open identification.


---

# 2026-10-11 — CORRECTION to the table above (my own error)

The third row is mislabelled. `prop:wigner-2-coefficient` is not a (2,2)
coefficient. It is a general theorem for self-conjugate shapes,
`tr(sigma_g^lambda)/dim(lambda) = h/2` (Lean `paired_sum_identity`,
`self_conjugate_trace`), with headline case `[3,2,1]` at k = 6, and its
interpretation block says `[3,2,1]` scales as `(Z-N)(A-1)`, not `T(T+1)`. So
it is a different term ("Wigner-2"). The 0.017357 figure is that formula
evaluated at (2,2) by me, not a value the block states. Under convention D
`[3,2,1]` has three rows, so its Markov weight is zero as well.

Lean status of the other two, measured:

- `prop:wigner-np-pairing` -> `ConfinedKnotBinding.wigner_energy_from_22`
  is `w*v*a*Z = a*w*Z*v := by ring`, a commutativity identity that says
  nothing about `[3]_q[2]_q^2`. `uses: []`. The value is stated, not derived.
- `prop:wigner-coefficient-derivation` -> `wigner_coefficient` is discharged
  by `wigner_coefficient_axiom`, an axiom asserting
  `|[5]_q! m_e - 68.896|/68.896 < 0.03` at the muon-era q0. That is an
  empirical comparison inside a formal proof.


---

# 2026-10-11 — Can either candidate be derived? (owner: "explore 1 2"; 3 stands)

**Neither, from the corpus as it stands.** And the comparison exposes the root:
the corpus gives the symbol `C_lambda` **two inconsistent definitions**.

    unified-iterative-correction-proof.md:5   C_lambda = m_e . H_q(lambda)      (hook product)
    mass-coefficient-shadow-price.lean:94     C_eq : C lam = w lam * (h/2)       (class field)

At (2,2): `m_e H_q = m_e [3][2]^2 = 6.2893 MeV` versus `m_e w h/2 = 0.00887 MeV`.
Since `w = dim_q^2/[4]!` and `dim_q = [4]!/H_q`, the hook product is
`H_q = dim_q / w`, so the two are not related by any scale the corpus states.

## Route 1 (shadow price) — not derived

- `h/2 = tr(sigma)/dim` for self-conjugate shapes is a real theorem
  (`self_conjugate_trace`). `w` is a definition. So `C = w h/2` is fine **as a
  definition**.
- The step that makes it a binding coefficient, `u*_lambda = C_lambda S_lambda(Z,N,A)`,
  is the class field `factor`, not a theorem. It cannot come from the stated
  program: the dual constraints are `u_0 + (w/d) u_lambda <= w/d`,
  `u_lambda >= 0`, which contain **no nuclear datum**. The dual optimum is
  `u_0* = min_lambda (w/d)` with the `u_lambda*` degenerate, the same set for
  every (Z, N). So no `S_lambda(Z,N,A)` is produced by this LP. The block's own
  note agrees: the compute it names "solves no program".
- `S_lambda`'s form (`T(T+1)/A^p` for content sum 0) and its normalisation are
  asserted. With `S` normalised to `T(T+1)/A`, the MeV coefficient would be
  `0.00887 MeV`.

## Route 2 (hook product) — not derived

- The selection of (2,2) **is** derived given "isospin class at the quartet
  level": it is the only content-zero partition of 4 (`qou-ld2a`,
  `IsospinClassSingleton.lean`).
- The value `C = m_e H_q(lambda)` is asserted as universal and fails for 6 of
  the 7 BW coefficients (`qou-orjl`); the bridge that might rescue it,
  `wedderburnEmbed`, is `opaque` and registers as an extra axiom (`qou-qb7p`).
- `m_e [2]^2[3]` is also the corpus's **shell** coefficient `delta_S`. The same
  number is used for two terms.
- The scaling shape is not settled either: `derived-mass-formula-light-isotopes.md:18`
  uses `min(Z,N)/A`, the Wigner blocks use `T(T+1)/A`.

## Successor

The sharp question is no longer "which Wigner coefficient" but **which
definition of `C_lambda` the corpus means**. Owner decision; nothing edited.


---

# 2026-10-11 — Option 3 applied (owner "1 2")

Caveat authorNotes added to `prop:wigner-np-pairing`, `prop:wigner-coefficient-derivation`,
`prop:wigner-2-coefficient`, `prop:mass-coefficient-shadow-price` and
`prop:unified-iterative-correction`. No values, statements or Lean changed. Validate: valid
(11 pre-existing warnings). Stays todo: which definition of C_lambda is meant is open.
