# Three blocks say the q-deformed weights sum to 1. They do not.

Started from bean `msc1` item 3, which reports a single block —
`prf:phi-q-categorical-truncation` — writing `w_λ` for the q-deformed quantity
that the notation register reserves the name `\tilde w_λ` for, and records
*"This block is the only one wrong."*

Checking that against the corpus turned up something larger, and different in
kind.

## The naming split is 18–7, not 1

Every `.md` in the paper that **defines** `w_λ`, classified by which quantity it
defines it as ([`wlambda_normalisation_census.py`](scripts/wlambda_normalisation_census.py)):

| definition | blocks |
|---|---|
| **q-deformed** — `dim_q(λ)²/[n]_q!`, or the equivalent `[n]_q!/H_q(λ)²` | **18** |
| **classical** — `(dim V_λ)²/n!` | **7** (two of which are the notation register itself) |

So the register's rule — `w_λ` = classical Plancherel, `\tilde w_λ` = q-deformed
Wedderburn — is followed by five content blocks and contradicted by eighteen.
`msc1` treats `prf:phi-q-categorical-truncation` as an outlier; it is squarely in
the majority. What is unusual about it is only that it sits next to
`prf:spectral-sequence-collapse`, which uses the other convention, so the clash
is visible within one neighbourhood.

**This part is a naming decision and not mine to make.** Either the register
changes to match the corpus, or eighteen blocks are renamed to match the
register. Both are defensible; they have different costs and only the author
should pick. Filed as a bean rather than fixed.

## The part that is not a naming decision

Three of the eighteen do something else: they define `w_λ` q-deformed **and**
assert it sums to 1.

| block | the assertion |
|---|---|
| [`knot-factor-spectral-derivation`](../../content/quantum-observable-universe/mass-theory/knot-factor-spectral-derivation.md) | *"The Plancherel weights `w_λ = dim_q² V_λ/[n]_q!` sum to 1. The identity holds exactly in R."* |
| [`gram-kappa-spectral-interpretation`](../../content/quantum-observable-universe/predicted-spectra/gram-kappa-spectral-interpretation.md) | *"Plancherel ensures `Σ_λ w_λ = 1` at every q"*, and separately *"convergent by Plancherel (`Σ w_λ = 1`)"* |
| [`h3-markov-wenzl-weights-context`](../../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-context.md) | *"`w_λ(q) = [n]_q!/H_q(λ)²` — Plancherel measure … normalised by `Σ_λ w_λ = 1`"* |

[`prf:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse-proof.md)
says the opposite in as many words: *"q-deformed Wedderburn weights `\tilde w_λ`,
bounded but `Σ \tilde w_λ ≠ 1` at `q ≠ 1` in general."*

At most one of these can be right. The classical identity is RSK,
`Σ_λ (f^λ)² = n!`; the question is whether it q-deforms to
`Σ_λ dim_q(λ)² = [n]_q!`.

## It does not

Evaluated at the substrate `q₀` (experimental / proton pin), `dim_q` from the
q-hook-length formula, 65 dps:

| n | `Σ_λ dim_q(λ)²/[n]_q!` | classical |
|---|---|---|
| 3 | 0.98744 | 1 |
| 4 | 0.98217 | 1 |
| 5 | 0.98222 | 1 |
| 6 | 0.99108 | 1 |
| 7 | **1.01243** | 1 |
| 8 | **1.05056** | 1 |

Two controls, because a wrong implementation would produce exactly this shape:

- **The `q → 1` limit returns exactly 1** at n = 3, 4, 5. So the deviation is the
  q-deformation, not a bug in the hook lengths or the factorial.
- **The verdict does not depend on the quantum-integer convention.** The corpus is
  not uniform about whether `[n]_q` is balanced `(qⁿ − q⁻ⁿ)/(q − q⁻¹)` or
  unbalanced `(qⁿ − 1)/(q − 1)`. Under the unbalanced convention the sums land
  *further* from 1 — 0.868 at n = 5 — so the claim fails either way.

Note the n = 7 and n = 8 rows: the sum **exceeds** 1. The quantity is therefore
not a sub-probability distribution either, which forecloses the weaker reading
that the blocks meant `≤ 1` and wrote `= 1`.

`prf:spectral-sequence-collapse` is right, and the three blocks are wrong.

## Why it matters where it appears

In two of the three the normalisation is decorative — it names the weights
"Plancherel" and adds that they sum to 1. In
`gram-kappa-spectral-interpretation` it is load-bearing: the block's comparison
table lists *"2-jet truncation chosen by hand"* against *"Full `λ ⊢ n` sum,
**convergent by Plancherel** (`Σ w_λ = 1`)"*. The normalisation is what licenses
replacing the hand-chosen truncation. Remove it and the *convergence* argument
needs a different ground — boundedness of the weights, which
`prf:spectral-sequence-collapse` does assert, is the obvious candidate but is a
weaker statement and is not what the block currently claims.

That is why this audit stops at the measurement rather than editing the three
blocks: fixing the first two is a wording change, fixing the third changes what
the argument rests on.

## Re-checked against main four days later — and the detection gap that implies

Re-run 2026-08-15, ~690 commits later, including a corpus-wide per-block
language-trap audit wave (`qou-ujp8`) that swept `brings-surface` and
`information-theory` in batches and did surface real defects, *"8 anomalies incl.
a false Hecke claim"* among them.

**Every number above is unchanged.** Still 18–7. Still the same three blocks.

That is not reassurance, it is a finding. The three blocks are not
under-inspected:

| block | QA criteria on its sidecar |
|---|---|
| `h3-markov-wenzl-weights-context` | 61 |
| `knot-factor-spectral-derivation` | 101 |
| `gram-kappa-spectral-interpretation` | 78 |

240 criteria across the three, and none of them caught it — because **no
criterion evaluates a stated identity.** The checkers read voice, status leaks,
notation register, forward references, `q`-regime, witness pinning, base ring.
A sentence of the form *"X = 1"* where X is a computable expression is prose to
every one of them.

The gap is narrow and mechanisable: a criterion that extracts closed-form
numeric assertions about defined quantities and evaluates them at `q₀` would
have flagged all three on the day they were written. Not proposed here — it is
a checker-authoring task, and the corpus-wide false-positive rate would need
measuring first — but it is the class this defect belongs to, and it is the
reason 690 commits of active QA did not find it.

## Scope

Following the "before declaring refuted" discipline, both findings are
**scope-(a)**:

- The 18–7 split is a measurement of current usage. It does not say the register
  is wrong, only that it is not what the corpus does.
- `Σ dim_q² ≠ [n]_q!` at `q₀` is a numerical refutation of the three blocks'
  stated identity at the anchor, corroborating a claim the corpus already makes
  elsewhere. It is **not** a claim that no normalised q-weight family exists —
  a different normalisation (dividing by `Σ_λ dim_q(λ)²` rather than by
  `[n]_q!`) would of course sum to 1, and nothing here excludes that being the
  intended object in one or more of the three blocks.

## Not checked

- Whether the compute layer uses a normalised or unnormalised weight, and hence
  whether any witness inherits the error. The probe measures the corpus prose
  only.
- The other `msc1` items (the mis-aimed citations, the hook-length attribution,
  the Yang–Mills squeeze). Untouched here.
