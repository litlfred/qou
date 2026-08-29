# The Q_β ansatz's ε is inadmissible under convention D (2026-08-26)

**Branch**: `claude/qbeta-decay-channel-algebra-2026-08-26` · **PRs**:
[#5858](https://github.com/litlfred/qou/pull/5858) (merged),
[#5864](https://github.com/litlfred/qou/pull/5864) ·
**Beans**: `qou-cds1`, `qou-99qc`, `qou-879g` (completed), `qou-xzrj`, `qou-phlk`

## Finding, in one sentence

Step 8 of the [2026-05-24 fitting-finding audit](2026-05-24-q-beta-net-ansatz-fitting-finding.md)
— the Q_β chain's one postulate — rests on a functional that is not a trace, is
not the counit the corpus calls it, and does not survive the Temperley–Lieb
quotient the framework's own GNS proof places the convention-D theory in; the
complete set of functionals that *do* survive is two elements, and they bracket
the measured Q-value from 12 % above and 43 % below.

## The chain of measurements

Each row is a separate probe, exact-symbolic in `q` (and in `z` where it
appears), with mpmath at 50 dps for the numbers.

| # | probe | result |
|---|---|---|
| 1 | `qbeta_epsnpq_functional_mismatch_probe` (7/7) | `epsNPq` is the **coordinate sum** `σ ↦ 1`, not the augmentation `σ ↦ q` |
| 2 | `qbeta_net_trace_invariance_probe` (25/25) | `net` is **not a trace** — 8 of 36 ordered basis pairs fail cyclicity |
| 3 | `qbeta_alpha_commutator_floor_probe` (22/22) | the phase has a **z-free floor**, bar-even |
| 4 | `qbeta_phase_block_resolution_probe` (18/18) | the phase resolves per block; `χ^(2,1)(Δ) = 0` identically |
| 5 | `qbeta_net_as_trace_plus_longest_probe` (20/20) | `net = tr_M^{z=1} − h·(coefficient of w₀)` — **n = 3 only**, see row 8 |
| 6 | `qbeta_which_algebra_the_decay_channel_lives_in_probe` (11/11) | `net` does **not descend** to the TL quotient |
| 7 | `qbeta_admissible_functionals_bracket_probe` (19/19) | the admissible set is **complete at two**, and they bracket |
| 8 | `qbeta_rank_one_identity_is_n3_only_probe` (6/6) | **scope correction** — row 5 **fails at n = 4** (11 of 24) |

## Why "counit" was load-bearing, not cosmetic

The Lean docstring for `QOU.Interactions.QBetaEnergyScale` calls `ε(Δ)` the
*"Frobenius counit"* and the result a *"counit (transition) observable,
categorically distinct from the Markov-trace … mass"*. That sentence is the
stated licence for step 8.

An algebra map into a commutative ring is automatically cyclic —
`ε(xy) = ε(x)ε(y) = ε(y)ε(x) = ε(yx)` — so **a counit is a class function**. The
functional actually evaluated is not one (row 2). And `σ ↦ 1` cannot be made
multiplicative: pushing `σ² = hσ + 1` through it forces `h = 0`
(`QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one`, sorry-free).

The mislabelling then becomes structural rather than terminological. Descent to
a quotient is annihilation of the ideal; the augmentation annihilates
`J_(1³)` and the coordinate sum does not. **Had `epsNPq` been the counit the
corpus names, it would have descended.**

## The corpus had already decided the algebra

`qou-879g` was opened asking whether the D decay channel lives in `H₃(q)` or its
TL quotient, and called it an owner decision. **The four-path grep found the
answer already written**, in
[`prf:algebraic-gns-embedding`](../../content/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md):

> Under the production convention D this ideal is **not** trivial … so `N` is the
> sum of those Wedderburn blocks — the Temperley–Lieb radical — and the GNS space
> is `H_∞(q)/rad ≅ TL_∞(q)`, **not** `H_∞(q)` itself.

The bean was premature. Recorded because the discipline exists for exactly this.

## The admissible set is complete, and it brackets

The structural condition **is** `y_(1³)(z) = 0`. Solved rather than sampled it is
quadratic:

```
y_(1³)(z) = −q²(q − z)(q²z + z − q³) / ((q²+1)(q²−q+1)(q²+q+1))
         ⇒  z = q   or   z = q³/(q²+1) = z_D
```

- **The two-row forcing is not unique to `z_D`.** `z = q` kills the block too.
- **At `z = q` the Markov trace *is* the augmentation** — on all six basis
  elements, so the second root is not a third functional.

| root | functional | Q_β err vs CODATA |
|---|---|---|
| `z = z_D` | Markov trace at `z_D` | **−43.157 %** |
| `z = q` | ≡ the augmentation | **+12.470 %** |
| *(neither root)* | `epsNPq` = `tr_M` at `z = 1` | *+0.168 %* |

`z = 1` is the trivial loop value, which
[`qbeta-counit-closed-form.md`](../../content/quantum-observable-universe/nuclear-interactions/qbeta-counit-closed-form.md)
itself says *"is never attained on the substrate"*, and `y_(1³)(1) ≠ 0`, so it
does not descend either. **The +0.168 % agreement is delivered entirely by an
evaluation inadmissible on both counts.**

### The trap, named

The two admissible values bracket the target, so some convex combination
reproduces CODATA exactly. That is **one parameter against one anchor** —
numerology, not a derivation. It is deliberately not computed; any weight must
be derived from the representation.

## Scope

**Scope-(a) throughout.** Nothing here proves Q_β's number wrong, forbids
non-cyclic functionals a priori, or closes the D-frame programme. It establishes
which functional the ansatz evaluates, that it is excluded by the canonical
convention, and what the complete set of permitted replacements gives. Nothing
is wired; no value is proposed for anything.

## Lean landed alongside (all sorry-free, `lean`-direct exit 0, axioms clean)

| file | content |
|---|---|
| `QOU/QBeta/CounitSigmaOneForcesHZero.lean` | `σ ↦ 1` multiplicative ⇒ `h = 0` |
| `QOU/QBeta/PhaseBlockResolution.lean` | `χ^(2,1)(Δ) = 0`; the floor is bar-even (+ a defect lemma so that is not read as a `ring` tautology) |
| `QOU/QBeta/TwoRowRootsAndAugmentation.lean` | the two roots; at `z = q` the trace **is** the augmentation |

The tree is a **restored** olean cache (6990 oleans / 0 traces), so no
`lake build` was run.

## Corrections made to my own work in this tranche

Recorded because each was caught by a failing assertion or by the grep, not by
review.

1. **"The 92× D-frame gap forecloses the ladder re-derivation."** Retracted on
   owner instruction: a structurally-exact piece is a permanent contribution
   even while the total is inaccurate. The measurement sets an expectation on
   the re-derivation, not a verdict on running it.
2. **A calibration asserting the trace row would reproduce −15.451 %.** Failed
   at −43.157 %, correctly: that baseline evaluates `tr_M` on the **exhibited
   nucleon words**, this on the **NF vector**, and `qou-avt5` established those
   are different objects. Two numbers both called `tr_M(Δ)` are not comparable.
3. **"All three `a_λ` are bar-neither."** `a_(2,1)` is exactly bar-**odd**.
4. **"Exactly two admissible functionals" from enumeration.** True but weaker
   than the situation — solving the condition showed the set is *complete* at
   two, and that `z = q` is a root at all.
5. **`net = tr_M^{z=1} − h·δ_{w₀}` stated without an `n`.** Holds at n = 3,
   **fails at n = 4** — nonzero on 11 of 24 basis elements, four distinct values,
   and the trace at `z = 1` takes five values rather than being constant off
   `w₀`. Every conclusion drawn from it stands (each is evaluated on Δ ∈ H₃(q)),
   but the sentence read as a characterisation of the two functionals and is not
   one. Caught because [PR #5337](https://github.com/litlfred/qou/pull/5337#issuecomment-5371899738)
   had warned about generalising an n = 3 coincidence **on this very bean** —
   *"do not generalise the n=3 coincidence"* — and I tested my own claims against
   that warning instead of assuming they were exempt. Also recorded: imposing the
   Markov property only at the top generator leaves the Ocneanu trace
   **underdetermined** (rank 5 of 6 at n = 3).

## Follow-on

- `qou-99qc` — which ε. Now **asymmetric**: one branch is structurally
  disqualified under the canonical convention.
- `qou-cds1` — the D ladder re-derivation. Tightened: a ladder on either
  admissible functional starts 12–43 % out, so the rungs were never sized to
  the real gap.
- `qou-xzrj` — the 7.67 % of `epsNPq` invisible to every trace.
- `qou-phlk` — `prop:algebraic-gns-embedding` claims faithfulness on `H_∞(q)`
  while its proof gives `H_∞/rad`; true under C, false under D since
  2026-08-15. **Cone walked** (2026-08-26): five consumers, and the fix is
  smaller than filed. `QOU/Observations/AlgebraicGnsEmbedding.lean` is already
  **correct** — it states faithfulness relative to `traceIdeal` at both sites
  and its docstring says *"Faithfulness on the GNS quotient"*, so no Lean change
  is needed. Two consumers speak of the GNS **image**
  (`algebraic-gns-embedding-cfs-consequence`,
  `q-plancherel-asymptotic-skeleton`) and are unaffected. The
  `definition-index` one-liner mirrors the proposition and follows from fixing
  it. `non-commutative-probability-dictionary` carries the same quotient
  subtlety — "the Hecke algebra … operates as a `(W*, tr)` probability space",
  where under D the honest object is the quotient — and is worth one clause.
