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

#### 🛑 CORRECTION (2026-10-11) — the May towers rest on HARDCODED inputs, and my own table above used |tower|

Three separate defects, in increasing order of how much they matter. The first
is mine.

**(i) My table reported `abs(total_tower)`, which hides a sign.** The witness's
signed `total_tower` for tritium is **−1.9370**, not `1.9370`, against an AME
binding of **+8.4818**. A negative tower against a positive binding is not a
"77.2 % shortfall" — it is the **wrong sign**, which is a different and worse
statement. Deuteron (+0.8764) and ³He (+1.0659) are positive; only T flips.

**(ii) The May probe's inputs are partly INVENTED, verbatim in its source.**
`DOMINANT_PARTITION` is a hand-written literal dict, and three of its nine
entries were never computed:

```python
DOMINANT_PARTITION = {
    "deuteron": {"lambda": [2, 2, 1, 1], "dim": 9,
                 "contrib_k1": 0.0,      # negligible
                 "contrib_k2": -6.2203,
                 "contrib_k3": -65.0},   # approximate (eigenvalue spectrum recomputed)
    "tritium":  {"lambda": [6, 3], "dim": 48,
                 "contrib_k1": 0.05,
                 "contrib_k2": -3.0006,
                 "contrib_k3": -27.0},   # approximate
    # ... he3 omitted; its three k entries are all computed
}
```

**For deuteron this voids the result entirely.** The rule sets `k_λ = 1` on the
cut block, so the tower is `non_dominant_sum + contrib_k1(cut)` — and the
witness records exactly `0.87640 + 0.00000 = 0.8764`. **The rule's whole effect
on deuteron was a literal `0.0` annotated "negligible".** The deuteron
"closure" is the non-dominant sum alone; it never measured the rule.

**(iii) Recomputed at 60 dps, the towers move — relayed, not measured here.**
From a sibling session (two independent routes agreeing to 2e-58, rebuilt from
the braid word at `e2204a4a5d55` with Hoefsmit σ and Wenzl `y_λ`), under the
May setup (convention C, muon CODATA-2018): **D 0.2550**, **T −1.9719**,
**³He 1.0656**, with D's real `contrib_k1` = **−0.62148** rather than 0. That
also reports the PR #638 witness's `y_λ` wrong by up to **1.15e-4** relative at
`n = 9`, and the uncomputed `k=3` entries as **D −32.94** (hardcoded −65) and
**T −23.50** (hardcoded −27).

I did **not** recompute these. What I can check is that they are arithmetically
consistent with the committed witness: `0.87640 + (−0.62148) = 0.25492`, against
the relayed `0.2550`. Treat the 60-dps figures as relayed-and-consistent, and
the hardcoding in (ii) as verified from source.

**So the corrected comparison is:**

| atom | cut block | rows | May tower (signed) | provenance of that number | AME `B` (MeV) |
|---|---|---:|---:|---|---:|
| deuteron | `[2,2,1,1]` | **4** | +0.8764 | **cut block's `k=1` term hardcoded `0.0`** — non-dominant sum alone; relayed 60-dps value 0.2550 | 2.2246 |
| tritium | `[6,3]` | 2 | **−1.9370** | `k=3` hardcoded `−27.0 # approximate`; relayed −1.9719 | 8.4818 |
| ³He | `[5,4]` | 2 | +1.0659 | the only atom whose three `k` entries are all its own data; relayed 1.0656 | 7.7181 |

The conclusion is unchanged and **strengthened**: no atom's tower approaches its
binding, T has the wrong sign, and the `|tower| < 2` criterion is still
satisfied by driving the tower toward zero. What changes is that for deuteron
there was never a computation to be anti-correlated with.

**(iv) Under convention D the criterion itself fails — and for deuteron the cut
is provably a NO-OP.** Relayed, at the proton pin: towers **0.2222 / 2.8116 /
−0.0098**, so **tritium fails `|tower| < 2`** under the canonical convention.
Independently of any compute, verifiable from the corpus: deuteron's cut block
`[2,2,1,1]` has **four rows**, and
`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (sorry-free,
general `n`) gives `y_λ = 0` for every shape with a third row. **So under
convention D the block the rule flips for deuteron carries zero Ocneanu weight,
and changing its truncation order cannot change the tower at all.** T `[6,3]`
and ³He `[5,4]` are two-row and survive. That is a structural statement and does
not depend on the 60-dps numbers.

**(v) "max-|μ|" is more broadly wrong than stated above — and its origin is a
FALSE POST-HOC OBSERVATION inside the probe, not a careless rename.** The entry
above cites the probe's docstring sentence placing T's `max|μ| = 8.23` at
`[4,3,1,1]`. The actual origin is one line of the probe's own witness prose:

> *"Numerical signal: outlier partitions are the **max-|μ|** ones in
> `ρ_λ(β_atom)`."*

The rule selected by **max-|contrib|** (its own "Candidate rule under test");
the probe then *remarked* that the outliers "are the max-|μ| ones"; and that
remark was promoted into the rule's identity downstream, arriving at the
catalogue as *"1 iff λ is the max-|μ| partition"*. **The remark is false** —
relayed from the float64 data, `argmax|μ|` differs from the cut block for **all
three** atoms (D `[3,3]`, T `[3,3,3]`, ³He `[3,3,3]`). So this is a wrong claim
*inside* the probe that nothing re-derived, which is the same class as the rest
of this entry.

**(vi) On the CURRENT production word the rule fails its own verdict** (relayed,
convention D at the proton pin, 60 dps, cross-checks ≤ 1e-52; word
`atom_braid_word_3A`, borromean intra order `7db032fb48`, colour-weighted p-n
letter). Fitted towers **D 10.29 / T 31.85 / ³He 2.53** — **all three fail
`|tower| < 2`**, by 5×, 16× and 1.3×, and the cut block is not `argmax|μ|` for
D or ³He.

**(vii) The obstruction may not be the selector at all — hypothesis, scope (a).**
Relayed: **7 of the 14 live blocks** (corrected from 8, and the May word is
not pole-free either — it has 1) have an eigenvalue within `0.007` of a `Φ_q`
pole `μ = q^j` (closest T `(7,2)` at `8.9e-4`), with roughly **1000×**
amplification. Verified here, the May probe had already named this for *one*
block — ³He's `[5,4]` is *"structurally over-twisted … carries the dominant
near-pole multiplicity"* — and used `m_near_pole` as one of the failed 2-input
scalar parameters. If the 8-of-14 figure holds, the difficulty is that `Φ_q` is
being evaluated near its own poles, where **any** truncation is ill-conditioned
and a one-block integer flip is the wrong instrument. 🛑 Hold it as a
hypothesis: no invariant is yet named, so this is scope (a), and two relayed
threads would decide it (whether the proximity is structural or accidental, and
which word change causes it).

**(viii) The pole proximity is ACCIDENTAL, and item (vii)'s mechanism is
withdrawn.** Relayed, for all 10 `(eigenvalue, j)` pairs with `d < 0.01` where
`d(q) = |1 − q^{−j}μ(q)|`: `d` drifts smoothly when the word is rebuilt at each
`q`; each crossing is a **simple zero away from `q₀`** (`q*/q₀ − 1 ∈
[−8.3e-3, +1.6e-2]`, closest T `(7,2)` at `−1.340e-3`); `μ ≠ c·q^j`, with
`dlog μ/dlog q` running 1.40–3.94; `|μ/q^j| − 1 ~ 1e-3`, **not** `~1e-60`; and
the proton→muon pin moves `d` by `≤ 8.8e-6` relative. So item (vii)'s *"any
truncation is ill-conditioned"* is **withdrawn as a mechanism** — the near-poles
are a coincidence of this word's spectrum. Their report leaves two gaps: the ³He
`(6,3)` `j=2` crossing (secant non-convergent) and poles with `j ≥ 4` — the
latter is real, since at the proton pin `q⁴ = 1.517953` against D `(4,2)`'s
`max|μ| = 1.514`, a gap of `0.0040`.

**Cause, isolated with the producer's own switches** (verified: `atom_braid_word_3A`
at `computations/mass_at_3A_proper.py:456` takes `intra_order` and
`pn_convention`): the `intra_order` change **grouped → borromean alone** produces
all 7 near-poles; the colour-weighted p-n letter alone shifts distances `≤ 8 %`.
**That change is the owner-ruled correctness fix of 2026-09-05** (`qou-hu1f`) —
the grouped word was not `β_Bor`, the alternating one is, matched to `5e-60`
against the Lean closed form. The near-poles are a side effect of a change that
was right for an independent reason, and are **not** evidence against it.

**(ix) Seven PRE-REGISTERED q-only rules, all failing.** `PREREGISTRATION.md`
sha256 `3d3f628a2318b0c4790bedc785d4fea3f74e33d73b211f581db01c69d9cbd832`, frozen
**2026-10-11T05:41:29Z before any tower was computed** — which is what makes
these predictions rather than selections. Rules: **R1a/b/c** pole index
`⌊log_q max|μ|⌋` (three variants); **R2** cyclotomic termination; **R3**
Garoufalidis–Zagier optimal truncation; **R3′** smallest-term truncation; **R4** a
Habiro-degree bound, flagged by its author as *their own construction, because
the corpus defines no Habiro selector*.

The criterion is **the conjecture's own**, verified verbatim at
`brane-tower-z-habiro.md` §52-60 — within `∼5 %` of AME
`{2.224566, 8.481798, 7.71806}` MeV *"without per-atom retuning"*. **All 7 fail
on all 3 atoms**, on both words, under both unit maps; the uniform `k = 1/2/3`
baselines and the fitted May rule fail too. **Best cell anywhere: 26 %.** Each is
**scope (a)** for that rule alone.

**(x) 🛑 TRUNCATION IS CUTTING A CONVERGENT PRODUCT — and this is the finding.**
`Φ_q^{[≤k]}(μ) = Π_{j≤k}(1 − q^{−j}μ)^{−1}` **converges** at `q₀ > 1`: verified,
and elementary — `q^{−j} → 0` geometrically, so the factors → 1 and
`Σ|q^{−j}μ| < ∞`. The untruncated tower is `~1e8–1e9` for every atom (relayed).
Every q-intrinsic rule picks `k_λ = 2…22` and lands at `1e2–1e9`; **only `k ≈ 1`
gives an O(1) tower.**

**Under §NO FITTING that is decisive.** If no rule derivable from `q` reaches
`k ≈ 1`, and only `k ≈ 1` yields a number of the right order, then *"the right
`k`"* is not a function of the mathematics — it is whatever makes the output
small. **That is selection against the target by construction**, and it explains
why every candidate for five months has been a fit. The failure is not that the
right invariant is still unfound; it is that the quantity being chosen is fixed
by the answer.

**A GAP IN THE CONJECTURE'S OWN STATEMENT, not in a candidate.** R2 cannot fire
— `q₀` is not a root of unity and no eigenvalue sits *on* a pole — and `Φ_q` is
**not a class in any `R/(P_k)`**, since `P_∞ ≡ 0` there. So the conjecture's
*"cyclotomic projection evaluated at `z = μ`"* is **undefined at generic
eigenvalues without an extra choice**. That belongs on
`conj:brane-tower-z-habiro`. Separately, the conjecture **never specifies the
dimensionless → MeV map**, so every MeV comparison above inherits an unstated
convention; the `n⋆` claim gets no support, and the Cauchy-limit claim is
untouched.

**What would replace it:** a *derived* structural selector `λ ↦ k_λ`, or a
proof that none exists. Bean `qou-9f4h`, which stays open per §13a (the
question is part of an open conjecture). 🛑 **The route the May ledger left unexplored is now itself
excluded in the block basis** (relayed 2026-10-11, scope **(b)**, invariant
named): the `e_λ` are *central orthogonal idempotents*, so
`tr_M(e_λ e_μ) = δ_λμ · tr_M(e_λ)` and the Gram is **diagonal by
construction** — measured max off-diagonal `1.7e-52`. The LP therefore
degenerates to "pick the cheapest block" and agrees with the fitted rule
**0 / 3**. So the "full off-diagonal-Gram SDP" that the ledger still records as
`UNTESTED | next probe` has no off-diagonal structure to find.

**Scope that exclusion carefully.** It is stated *in the block basis*. The
ledger's own phrasing is `tr_M(b_i · b_j)` over **braid-word** elements
`b_i`, which are not idempotents and whose Gram need not be diagonal — so what
is excluded is the idempotent/block-basis reading, not every reading of that
sentence. Both surviving routes in the ledger (this, and the Hoefsmit
hook-content asymptotic along a reduced braid word) should be re-stated in the
basis they are meant in before either is called dead. Whatever replaces the rule
may **not** be selected against AME.

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
