# Refuted-ansatz lemmas — audit record (2026-06-17)

**Branch:** `claude/remove-deuteron-binding-prediction-2026-06-17`
**Principle (owner directive):** refuted-ansatz *lemmas* (lab-notebook
dead-ends recording that a specific construction the authors tried
*failed*) do not belong in the rendered paper — they belong here, in an
audit doc. **Formalize-first gates** (proved exclusion results of the
form "class C cannot work, here is the invariant that forbids it") are
legitimate paper content and **stay**.

A corpus sweep distinguished the two. This doc preserves the refutation
*records* for the material removed from the paper, and documents the
reclassification of three borderline blocks that turned out to be gates,
not dead-ends.

## Removed from the paper

### `rem:per-partition-k-lambda-rule` (was `mass-theory/per-partition-k-lambda-rule`)

A remark whose body is a refutation table: six candidate per-partition
`k_λ` selection ansätze, all empirically refuted:

1. **scalar-eigenvalue family** — refuted
2. **per-eigenvalue operator-valued** (uniform `k`) — refuted
3. **Type-B fold** — refuted
4. **multiplicity-refined** — refuted
5. **pair-knot product-volume** — refuted
6. **pair-knot Markov-trace** — refuted

The surviving open question — "does a structural `k_λ` / `n⋆` selector
exist?" — is **not** refuted; it is the open part of
[`conj:brane-tower-z-habiro`](../../content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md),
which the paper keeps as an honest open conjecture. Only the
failed-candidate enumeration moves here.

#### 7. **max-|contrib| outlier** (the rule actually in the compute) — **FITTED, not refuted** — added 2026-10-10

The six above are refuted candidates. This seventh is different and worse: it
is the rule the **live compute has been using**, it was recorded as *closing*
all three atoms, and it is a **fit**. It did not appear in the original table
because nobody had traced the compute's `k_λ` back to its origin.

**Origin.** PR #639 cycle 5b, `probe_phiq_per_partition_klambda.py`. Readable
commit-pinned at
`0763606e4f^:_deprecated/probes/probe_phiq_per_partition_klambda.py` —
quote the pinned form, because the `_deprecated/` tree is **no longer on
`main`** (removed 2026-10-10; it survives on branch
`cat/cat-harness/fsh-guts`).

**Why it is a fit.** The probe's own docstring states the rule under test
verbatim:

> *"Candidate rule under test: `k_λ = 1` if λ is the **maximum-|contrib|
> outlier** for the atom; `k_λ = ` atom-uniform-`k` otherwise."*

Selection by maximum-|contrib| is selection of the Wedderburn block that
**dominates the quantity being reproduced**. Per AGENTS.md §"NO FITTING,
EXCEPT CAL-1/2/3": *"Selection against the target — choosing an object because
the choice reproduces the measured value — is a fit even though no continuous
parameter is tuned."* No continuous parameter is tuned here; it is still a fit.

**The published label is also wrong, and the probe's own data refutes it.** The
rule reached the compute as *"1 iff λ is the max-|μ| partition"*. For tritium
the block it flips is **`[6, 3]`** (witness
`/data/dominant_partitions/tritium/lambda`), while the same probe's docstring
puts T's `max|μ| = 8.23` at **`[4, 3, 1, 1]`**. Two different partitions: the
rule selected by *contribution* and was later relabelled by *eigenvalue
magnitude*. At one live site the relabel could not even have been evaluated —
`derived_chi_catalogue_build.py` hardcodes `k_lambda=1` beside
`mu_eigenvalues=["?", "?"]`.

**"Closes" meant `|tower| < 2` and was never compared to AME.** The probe's
closure print reads *"atoms collapse to small-magnitude towers (|tower| < 2)"*.
It records `ame_MeV` beside each atom and does not test against it. Recomputed
from its committed witness:

| atom | flipped block | tower (fitted) | AME `B` (MeV) | miss |
|---|---|---:|---:|---:|
| deuteron | `[2,2,1,1]` | 0.8764 | 2.2246 | **−60.6 %** |
| tritium | `[6,3]` | 1.9370 | 8.4818 | **−77.2 %** |
| ³He | `[5,4]` | 1.0659 | 7.7181 | **−86.2 %** |

So the criterion is satisfied by driving the tower **toward zero**, while the
AME bindings are 2.22 / 8.48 / 7.72 — the closure test is **anti-correlated**
with the data it was taken to close. "Closes all 3 atoms" was a magnitude
threshold, not an agreement. `docs/coordination/2026-05-10-non-calibrated-q-beta-mass.md`
carried the `**closes**` verdict until 2026-10-10 and is corrected in place.

**Scope.** This is a statement about the *selection rule*, not about the
brane tower. Per AGENTS.md §"Before declaring refuted": **scope (a)** — this
rule, as implemented, is a fit and its recorded closure does not test the
data. No ingredient is excluded, and the open question above is untouched.

**Live state.** `k_λ` is emitted by three witnesses and **read numerically by
nothing**; the three producers now label it a fit in place. The third witness,
`delta-lambda-categorical-verification`, carries a `k_lambda` field that is a
**different object** — a jet-prolongation order, per that producer's own
docstring — so the name is a collision, not a third consumer of this rule.

**What would replace it:** a *derived* structural selector `λ ↦ k_λ`, or a
proof that none exists. Bean `qou-9f4h`, which stays open per §13a (the
question is part of an open conjecture). The one route the May ledger left
unexplored is the **full off-diagonal-Gram SDP**, still recorded `UNTESTED`
there; the diagonal-Gram simplification is already refuted (1/3). Whatever
replaces it may **not** be selected against AME.

### Refuted `n⋆` families split out of `conj:brane-tower-z-habiro`

The brane-tower conjecture stays in the paper (it is an *open*
conjecture, not a refuted lemma, and is referenced by ~33 sibling
blocks). The conjecture asserts a canonical level-selection rule `n⋆`
*exists*; that existence claim is open. The empirical record of which
specific `n⋆` candidates were *tried and refuted* is moved here:

**Uniform-`k` sweep** (`probe_phiq_uniform_k.py`, atoms {D, T, ³He},
`k ∈ {1,2,3,4,5,6,8,10}`):

- **Absolute form** `B = m_e·ρ·(tr_M + tower^(k) + σ_{3A})` overshoots at
  every uniform `k`; error grows monotonically (+775 % at `k=1` to
  +1.27×10⁶ % at `k=10`). No uniform absolute-form `k` closes the gap.
- **Subtractive form** `B = E₀·(tower_free^(k) − tower_atom^(k))` has a
  sign-flip at `k=2`: `Δtower^(k=1) < 0`, `Δtower^(k≥2) > 0`. At `k=2`:
  B(D) ≈ +1.74 MeV (−22 %), B(T) ≈ +5.18 MeV (−39 %),
  B(³He) ≈ +18.05 MeV (+134 %).
- **³He overshoots at every `k≥2`** in subtractive form (two near-pole
  `|V̂| ≈ 0.989` entries vs D's one).
- **5 naive N=0 → N=1 structural lifts** all failed (PR #637 commit
  e1b005b2).

The sign-flip at `k=2` (smallest depth including the Hecke quadratic
slice `σ²=(q−q⁻¹)σ+1`) is recorded as a structural observation, not a
closure.

**Operator-valued per-eigenvalue probe** (`probe_phiq_operator_valued.py`):
Φ_q applied per eigenvalue of `ρ_λ(β)` in each Hecke irrep, operator-traced
and Wedderburn-weighted by signed `y_λ`. D finds a near-AME value at `k=1`
(−6.87 %) and T at `k=2` (−8.00 %), but ³He never gets within 50 % at any
uniform `k ∈ {1..10}`, and the (D,T) sweet spots are at *different* `k` —
no single uniform `k` closes all three (per-atom retuning is the excluded
signature). **Refuted.**

**Pair-knot magic-shell probe** (`probe_phiq_pair_knot_magic_shell.py`):
collapse each magic intra-block to a composite `Φ_q(|V̂_shell|)`. ⁴He at
−19.4 % is the closest any probed form came to uniform closure, but
collapse alone does not close the sample (³He still +219 %), and the
extracted shell corrections break `Z=2`/`N=2` symmetry under the
product-volume convention: `Δ_shell(Z=2) = −16.88 MeV` vs
`Δ_shell(N=2) = +22.38 MeV` (opposite signs, 1.326× magnitude). **Refuted
as formulated** — but it surfaced the kept structural findings (LP-dual
pair-knot selection at closed shells; the `1.326×` asymmetry is a
product-volume artifact, with Z↔N symmetry exact at the Markov-trace level).

**Pair-knot Markov-trace refinement** (`probe_phiq_pair_knot_markov_trace.py`,
full Frobenius Gram + SDP): LP+SDP confirm strong duality but the refined
tower still does not close the sample; ³He is a structural deficit of the
brane-tower formula at the `A=3` / `n_0=9` regime, not an operator-volume
choice. **Refuted.**

**The six probed `n⋆` families, all refuted** (combined in the sibling
`brane-tower-z-habiro.lean` as `nStar_all_probed_forms_refuted`):
scalar uniform-`k`; scalar `ℓ·n_0+k`; per-eigenvalue operator-valued;
multiplicity / Type-B-folded-crystal; pair-knot product-volume; pair-knot
Markov-trace (full Gram + SDP). The two **structural findings** that
survive (LP-dual pair-knot selection at closed shells; Z↔N isospin
symmetry) are kept in the paper as gates (brane-tower `.md`
§"Structural finding…").

**Convergence half (now PROVED — promoted to a theorem).** Independent of
`n⋆`, the analytic statement that the brane tower
`Φ_q(z) = ∏_{k≥1}(1−q^{-k}z)^{-1}` is a well-defined positive real on
`|z| < q` is **proved sorry-free** in
[`PhiQConvergence.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean):
`summable_q_inv_geometric` + `quantumDilog_factors_nonzero` +
`quantumDilog_denom_multipliable` + **`quantumDilog_multipliable`** (the
Multipliable statement, via `Real.multipliable_one_add_of_summable`). This
is now promoted to the proposition
[`prop:quantum-dilog-convergence`](../../content/quantum-observable-universe/mass-theory/quantum-dilog-convergence.md)
(2026-06-18). The `n⋆` half remains open/refuted. NB the convergence
theorem does **not** wire to the production mass table: at the physical
`z = |V̂_i| < 1` the product is convergent but enormous, so the canonical
tower uses the bounded `−Li₂^q` form — see
[`2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md`](2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md).

## Reclassified as gates — KEPT in the paper

Two blocks the prose-scan flagged as dead-ends are in fact
exclusion/open-gate documentation that other blocks depend on:

- **`rem:alpha-em-derivation-open-problems`** — `em-coupling-projection.md`
  cites it specifically for *"the multiplicative-family ruling"*
  (block-diagonal Gram deformations **cannot** close the 1.55×10⁻³ α_EM
  gap). That is a proved exclusion result a sibling block leans on — a
  gate, not a dead-end. **Kept.**
- **`alg:delta-lambda-closure`** (`mba-sidecar-delta-lambda-closure`) —
  the appendix's honest open-gate documentation (title: "Track-A blocker
  — open gate"), under the mass-binding-algorithms sync contract;
  `mba-step09b-per-isotope-binding` cites it as the conjectural input.
  Open-problem documentation, not a refuted-lemma-as-result. **Kept.**

Net: **1 clean removal** (`per-partition-k-lambda-rule`) **+ 1 split**
(`brane-tower-z-habiro` refuted-`n⋆` material → this doc); the other two
candidates are gates and stay.
