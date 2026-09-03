# The jet-filtration SCOPE section lists three open inputs; one of them is open

**Date:** 2026-08-29 · **Bean:** `qou-u8oy` · **PR:** [#6051](https://github.com/litlfred/qou/pull/6051)
**Subject:** [`jet-filtration-binding-extensive.md`](../../content/quantum-observable-universe/mass-theory/jet-filtration-binding-extensive.md) §Scope
**Re-measured, not quoted:** `sw_period_bessel_half_falling_factorial_probe.py`,
`sw_period_qinvolution_identification_probe.py` (both exit 0 on today's `main`)

## Why this exists

Bean `qou-u8oy` established that the multi-level jet tower scaffold is **not**
open — `conj:binding-manybody-eq-jet-filtration` already carries it — and closed
with an explicit caveat about its own scope:

> This bean asserts only that the SCAFFOLD is not open. It does not claim (1)–(3)
> are open — that claim would need its own corpus-grep, which has not been run here.

That corpus-grep is what this audit is. The three inputs are the ones
`jet-filtration-binding-extensive.md` §Scope names, and its closing sentence is
*"The magnitude that matches experiment depends on (1)–(3), which remain open."*

**Result: one of the three is open.** The other two were settled, one of them by a
sibling branch on the same day this was written.

## Per-input verdict

| input | §Scope says | corpus says |
|---|---|---|
| (1) super-exponential magnitude of `a_D^(n)` | open | **growth class settled 2026-06-25**; object positively identified; and the *form* §Scope names is measured **not** to reproduce it |
| (2) keystone `a_D^(n) = lw(n−1)` | open, conjectural | **open** — correct as stated |
| (3) per-atom residue weight `w_n(K)` | open | **scope-(b) excluded** 2026-08-29, invariant cited, and actively owned |

### (1) — settled as a growth class, and its stated form is refuted

Three independent things are true here and the §Scope line conflates them.

**The growth class is settled.**
[`2026-06-25-sw-jet-prolongation-explicit-and-fork.md`](2026-06-25-sw-jet-prolongation-explicit-and-fork.md)
(PR #2795) resolves it structurally: `γ` encircles branch points where
`disc_X = 0`, two sheets collide, so `X ~ X_k + c(z−z_k)^{1/2}` and
`X^(n) ~ (z−z_k)^{1/2−n}` — the period grows super-exponentially, and the depth-2
SL₂ recurrence (ratio → `λ₊ ≈ 2.18`) cannot produce it. The same audit records a
second, corpus-internal route to the same verdict via `prop:sw-period-residue-sum`,
whose residues are per-block Wedderburn `dim_q` weights, making the residue sum
`lw` by construction.

**The object is positively identified.** `sw_period_qinvolution_identification_probe.py`
(#2822) identifies `T_q(n) := Σ_{λ⊢n} dim_q(λ) = n·lw(n−1)` as the **q-deformed
involution number**: `T_q(n) → I(n)` (OEIS A000085) as `q → 1`, by RSK plus the
q-hook → hook reduction. Re-run today: exact for `n = 1..12`.

**But the form §Scope names does not reproduce it.** §Scope glosses input (1) as
*"the √-branch falling-factorial growth"*. That bridge was tested and **pruned** —
[`2026-06-26-bessel-half-falling-factorial-bridge-pruned.md`](2026-06-26-bessel-half-falling-factorial-bridge-pruned.md).
Re-measured today:

| n | `lw(n−1)` | `\|∏[1/2−k]_q\|` | ratio | succ. ratio |
|--:|---:|---:|---:|---:|
| 2 | 1.0 | 0.2493207961 | 4.010897 | — |
| 4 | 2.5327796564 | 0.9460191918 | 2.677303 | 0.750604 |
| 6 | 13.5598271251 | 15.7419189692 | 0.861383 | 0.541399 |
| 8 | 115.826224199 | 638.46593672 | 0.181413 | 0.442982 |
| 10 | 1436.0657902 | 50934.2876316 | 0.028194 | 0.382995 |

The rescaling ratio decays by a factor of 142 across `n = 2..10`, and — the part
that matters — the **successive** ratios are themselves monotone decreasing
(0.889 → 0.383), so no constant geometric factor `R^n` absorbs the gap either. The
falling factorial **outgrows** `lw`. So "falling-factorial growth" is not merely an
unclosed bridge; it is the wrong rate, measured.

This is a **scope-(a)** result, not a structural exclusion: the ν = 1/2 q-Bessel
*order* is untouched, and the √-branch argument for super-exponentiality stands.
What is excluded is the falling factorial as a closed form for `lw`.

**What is genuinely left in (1)** is the exact q-statistic / closed kernel, and
even that is bounded from one side: `sw_period_qholonomic_kernel_search.py` finds
**no q-holonomic recurrence** for `T_q(n)` at depth ≤ 3 and Laurent degree ≤ 3, and
establishes it decisively — the held-out residual is *precision-independent*
(identical at 70 and 140 dps), so it is approximation error, not numerical noise.

**Reproduction note.** The falling-factorial witness re-ran with a **byte-identical
numeric payload** under `mpmath 1.3.0 → 1.4.1`; the only diff was provenance
(timestamps, shas, an added `invocation` block). Both witnesses were restored
rather than committed, per the no-provenance-churn discipline.

### (2) — open, and correctly stated

`QOU.Mass.NaStokesKeystone.ProlongationPeriodMeanQuantumDim` axiomatises
`aD (c+1) = lw c` as a §3b conjecture class with **no instance**. Everything
downstream of it — the depth-2 `τ` assembly — is unconditional Lean algebra. This
is the honest shape, and §Scope describes it correctly.

One thing has changed underneath it this week. The keystone is consumed **only at
`c = 1, 2, 3`**, and those three `lw` values were, until PR #6051, fed in as
literals whose hook-length provenance lived in a docstring. #6051 derives all
three from the q-hook-length formula (`QOU.Mass.QHookDimension`), and they
reproduce the probe's own first three rows exactly:

| c | derived closed form | value at `q₀` | probe's `lw` |
|--:|---|---|---|
| 1 | `1` | 1.0 | 1.0 |
| 2 | `(q+1)²/(3q)` | 1.336966 | 1.33696562224 |
| 3 | `5/2 + (3/4)h²` | 2.532780 | 2.5327796564 |

So the conditional `τ` result now rests on the hook-length formula rather than on
hand-substituted numbers. The conjecture itself is no less open for it.

### (3) — excluded, and owned by a sibling

[`2026-08-29-w3-closeability.md`](2026-08-29-w3-closeability.md) (bean `qou-1xne`,
PR [#5967](https://github.com/litlfred/qou/pull/5967), **same day as this audit**)
finds `w_3` is not a closeable gap but a **required boundary condition of a rank-2
problem**, with the invariant cited: `no_scalar_kernel_on_carrier` (sorry-free) —
the q-Borel-normalised carrier is pure isoclinic of Newton slope `1/2`, every
rank-1 q-difference module has integer slope, and `2u − 2p = 1` is unsolvable over
`ℤ`. That is a proper scope-(b) exclusion.

Nothing here re-derives or re-tests it. It is read and cited, and the §Scope edit
points at it.

## What changed, and what deliberately did not

The §Scope section's **primary claim is true and is kept**: the three inputs really
are carried as non-negativity hypotheses and really are not derived in that
proposition. That is a statement about the Lean, and it is accurate.

What was stale is the corpus-status clause appended to it — *"which remain open"* —
plus the gloss on (1) naming a refuted form. Only those are edited. The proposition,
its proof, and its Lean are untouched.

## Reproduce

```bash
cd computations
python3 -u sw_period_bessel_half_falling_factorial_probe.py
python3 -u sw_period_qinvolution_identification_probe.py
git checkout -- .   # both witnesses differ only in provenance
```
