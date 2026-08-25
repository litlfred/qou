# Does the derived weak-isospin `T₃` writhe-sign reproduce the mixed-sign `Δ_λ`? (2026-08-02)

**Branch:** `claude/t3-vs-deltalambda-sign-2026-08-02` · **PR:** #4623
**Bean:** `qou-buxs` (child of the convergence epic `qou-20sx`).
**Probe:** [`computations/t3_writhe_vs_delta_lambda_sign.py`](../../computations/t3_writhe_vs_delta_lambda_sign.py) (exit 0),
witness [`t3-writhe-vs-delta-lambda-sign.witness.json`](../../computations/t3-writhe-vs-delta-lambda-sign.witness.json).
**Lean:** [`T3WritheVsDeltaLambdaSign.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/T3WritheVsDeltaLambdaSign.lean)
(`lean`-direct exit 0, sorry-free, import-free core Lean).
**Serves:** the `Δ_λ` Track-A blocker and the PROBE-4 KL-positivity prune
([`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md)).

## The question

PR #4618 ([`WeakIsospinT3Grading.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/WeakIsospinT3Grading.lean))
derives a weak-isospin grading `T₃ = sign(κ)/2`, where `κ` is the **signed
writhe** of a quark's canonical `T(2,n) = σ₁^{±n}` braid: up-type gets the
positive crossing (`T₃ = +½`), down-type the negative (`T₃ = −½`). The
**per-quark datum is `sign(κ) ∈ {+1,−1}`** — the sign of the *net* writhe.

The Option-E deuteron binding closure needs the per-partition chirality sign
$$\Delta_\lambda = \mathrm{sgn}(w_0^{S_{\lambda'}})\cdot\dim(V_\lambda),
\qquad \mathrm{sgn}(w_0^{S_{\lambda'}}) = \prod_j (-1)^{\binom{c_j}{2}},$$
where the `c_j` are the parts of the conjugate `λ'` (= column heights of `λ`).
This is **mixed-sign** (`n=3`: `1+/2−`; `n=6`: `6+/5−`). The PROBE-4 prune
proved KL/crystal multiplicities (non-negative) can supply the magnitude
`dim` but **never** the sign — it must come *exogenously from the braid
images*. `T₃` is a braid-image crossing sign, hence the natural candidate for
that exogenous source. Bean `qou-buxs` asks: does it match?

## Derive-then-check: the aggregation map is derived, not fitted

A Wedderburn block `λ` carries the standard **Young symmetrizer**: rows
symmetrize (bosonic, positive crossing), **columns antisymmetrize** (fermionic,
negative crossing). The chirality sign lives in the columns. This is not a
choice — it is the Frobenius/Wedderburn structure of `H_n(q)`.

**Chiral-EFT template (what the QCD-side literature contributes).** The task's
uploaded review (Hammer–König–van Kolck, *Nuclear EFT*,
[arXiv:1906.12122](../../library/arxiv-1906.12122v2/1906.12122v2.pdf) p.12) states the guiding
fact plainly: *"The Pauli principle dictates that only isospin-triplet `(0,1)`
and isospin-singlet `(1,0)` are allowed combinations."* The two-nucleon
isospin operator `τ₁·τ₂` has eigenvalue `+1` in the symmetric (triplet)
channel and `−3` in the antisymmetric (singlet, deuteron) channel. **The
isospin sign of a bound state is the exchange symmetry of its isospin
wavefunction** — symmetric `→ +`, antisymmetric `→ −`. That is precisely the
row(+)/column(−) Young sign. So the chiral-EFT template independently confirms
the aggregation route: aggregate the per-pair crossing sign over the
column-antisymmetrizer structure of `λ`.

The one place a *choice* could sneak in is which **statistic** of the writhe
the aggregation reads. There are two standard readings, and **they differ** —
which is the entire result:

| Reading | Per-column factor | Meaning |
|---|---|---|
| **MAP_A** crossing-**COUNT** parity | `(-1)^{C(c,2)}` | sign character / Slater-determinant / `τ₁·τ₂` pairwise |
| **MAP_B** net-writhe **SIGN** (literal `T₃`) | `sign(-C(c,2)) = -1` for `c≥2` | the actual per-quark `T₃` statistic `sign(κ)` |

`MAP_A`'s product over columns **is** `sgn(w₀^{S_{λ'}}) = (-1)^{n(λ)}`, the
target's own definition (via `ℓ(w₀^{S_m}) = C(m,2)`) — it is the target
restated, not independent information. `MAP_B` is the **literal** `T₃` grading
applied per column.

**Key arithmetic.** `sign(net writhe)` and `(-1)^{crossing count}` coincide
iff `C(c,2)` is odd (`c ≡ 2,3 mod 4`), and both are `+1` at `c ≤ 1`; they
**diverge at `c = 4,5`** (`C(4,2)=6`, `C(5,2)=10`, both even → `+1`, but the
net-writhe sign is `−1`). A height-4 column first appears in a partition of
`6`.

## Results — the full per-partition sign vectors

### `n = 3` (3 partitions; target `1+/2−`)

| `λ` | `λ'` (col heights) | `dim` | `Δ_λ` sign (target) | MAP_A | MAP_B (literal `T₃`) | `B=T`? |
|---|---|---|---|---|---|---|
| `(3)` | `(1,1,1)` | 1 | `+` | `+` | `+` | ✓ |
| `(2,1)` | `(2,1)` | 2 | `−` | `−` | `−` | ✓ |
| `(1,1,1)` | `(3)` | 1 | `−` | `−` | `−` | ✓ |

**MAP_B matches 3/3** — but coincidentally: every column height is `≤ 3`, where
the two statistics agree.

### `n = 6` (11 partitions; target `6+/5−`)

| `λ` | `λ'` (col heights) | `dim` | `Δ_λ` sign | MAP_A | MAP_B (literal `T₃`) | `B=T`? |
|---|---|---|---|---|---|---|
| `(6)` | `(1,1,1,1,1,1)` | 1 | `+` | `+` | `+` | ✓ |
| `(5,1)` | `(2,1,1,1,1)` | 5 | `−` | `−` | `−` | ✓ |
| `(4,2)` | `(2,2,1,1)` | 9 | `+` | `+` | `+` | ✓ |
| `(4,1,1)` | `(3,1,1,1)` | 10 | `−` | `−` | `−` | ✓ |
| `(3,3)` | `(2,2,2)` | 5 | `−` | `−` | `−` | ✓ |
| `(3,2,1)` | `(3,2,1)` | 16 | `+` | `+` | `+` | ✓ |
| **`(3,1,1,1)`** | **`(4,1,1)`** | 10 | `+` | `+` | **`−`** | **✗** |
| `(2,2,2)` | `(3,3)` | 5 | `+` | `+` | `+` | ✓ |
| **`(2,2,1,1)`** | **`(4,2)`** | 9 | `−` | `−` | **`+`** | **✗** |
| **`(2,1,1,1,1)`** | **`(5,1)`** | 5 | `+` | `+` | **`−`** | **✗** |
| `(1,1,1,1,1,1)` | `(6)` | 1 | `−` | `−` | `−` | ✓ |

**MAP_B matches 8/11.** The three failures — `(3,1,1,1)`, `(2,2,1,1)`,
`(2,1,1,1,1)` — are **exactly** the partitions whose conjugate contains a
column of height 4 or 5, where `sign(net writhe) = −1` but the crossing-count
parity is `+1`.

## Verdict: **PARTIAL** — the literal `T₃` is the wrong sign *statistic*

- The **literal per-quark `T₃ = sign(κ)`** (sign of net writhe), aggregated
  over the derived column-antisymmetrizer structure, reproduces the mixed-sign
  `Δ_λ` for `n = 3` (`3/3`) but **fails at `n = 6` (`8/11`)**. The failures are
  structural (height-4/5 columns), not noise.
- The object that reproduces `Δ_λ` for **all** partitions is the crossing-**count**
  parity (`MAP_A` = sign character = `(-1)^{n(λ)}`) — but that **is**
  `sgn(w₀^{S_{λ'}})` restated, so it is not new information supplied by `T₃`.
- `T₃`'s genuine contribution is the **physical crossing reading** of the
  antisymmetric channel (down-type = negative crossing), consistent with the
  chiral-EFT `τ₁·τ₂` Pauli/exchange-symmetry template. It gives `Δ_λ` a writhe
  interpretation and answers *where* the exogenous sign the PROBE-4 prune
  demanded lives (in the braid-image crossings). It does **not** independently
  reproduce the `Δ_λ` sign vector: `sign(net writhe)` is coarser than the
  crossing-count parity `Δ_λ` requires.

**Scope (per AGENTS.md "refuted" discipline): (a) scope-limited.** This is a
scope-limited negative on the *literal* `T₃` net-writhe statistic as the sole
`Δ_λ` sign source, **not** a structural exclusion of the writhe-crossing
mechanism. The crossing-count-parity reading *does* close the sign, and `T₃`'s
up/down grading is fully consistent with the fermionic column structure that
carries it; a future closure that reads the *count* parity of the
antisymmetrizer crossings (not merely the net orientation) remains open and is
in fact where the sign genuinely lives. The Lean-proved **PROBE-4 KL-positivity
prune stands** and is orthogonal to this finding.

## Anti-fit / anti-laundering statement

No aggregation map was chosen to match the sign vector. `MAP_A` and `MAP_B` are
the two standard readings of "crossing sign aggregated over the column
antisymmetrizer"; `MAP_A` is the target's own definition, `MAP_B` is the
literal `T₃` statistic `sign(κ)`. `MAP_B`'s partial match and structural
failure at `n = 6` is the honest derived result, not a tuned success. Nothing
is wired to production. The Lean file states falsifiable `≠` facts (had `T₃`
reproduced `Δ_λ`, `n6_literalT3_fails_at_3111` would be an equality; it is not).

## What the chiral-EFT literature contributed

The `τ₁·τ₂` isospin-operator structure (Hammer–König–van Kolck §II) supplied
the **derivation template** for the aggregation: the isospin sign of a bound
state is the exchange symmetry (symmetric `+` / antisymmetric `−`) of its
isospin wavefunction — the Young row/column sign. This is what justified
aggregating the crossing sign over the *column antisymmetrizer* rather than
picking an ad-hoc map, and it is why the correct statistic is a pairwise
antisymmetry **count** parity, not a net orientation. (Meißner
[1011.1343](../../library/arxiv-1011.1343v1/1011.1343v1.pdf) and Kievsky–Girlanda
[s00601-022-01745-1](../../library/s00601-022-01745-1/s00601-022-01745-1.pdf) corroborate the same
Pauli-principle spin-isospin correlation; no additional sign structure beyond
the exchange symmetry was found.)

## Next honest steps

1. **Test the count-parity reading on the real braid.** `MAP_A` matches by
   definition, but a genuine derivation would show the *actual* `H_n(q)`
   column-antisymmetrizer braid carries `C(c,2)` crossings whose product of
   per-crossing signs is `(-1)^{C(c,2)}` — i.e. read the **count** of the
   antisymmetrizer crossings, not the net writhe. That is the surviving route
   for a writhe-based `Δ_λ` sign and is *not* excluded by this negative.
2. **Feed the negative back to `qou-qpj9` / #4618:** `T₃`'s up/down grading
   remains valid for the D-vs-K meson selection (a per-quark distinction), but
   it should **not** be advertised as the `Δ_λ` binding sign.
