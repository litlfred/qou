# χ-cache drain: what landed, what is blocked, and why the `y_λ = 0` theorem does not unlock it

**Date:** 2026-08-16
**PR:** #5260
**Beans:** `qou-okl8` (producer collision), `qou-tzsp` (witness self-inconsistency), `qdzu` (corrected)
**Predecessor:** #5168 commit `45789ddf`, which added the convention fingerprint guard and
promised *"Regeneration of the nine follows; the ones too large to run here will be named
rather than quietly skipped."* This is that naming.

## The nine, and where they stand

Nine committed witnesses carried colour-**blind** symbolic χ for words that **have** a p-n
interface. The producers were never wrong — `atom_canonical_crossings` emits exactly one
`averaged_weighted` crossing for every canonical Z≥1, N≥1 word — the caches simply could not
tell that the question had changed, because they keyed on file existence or partition
coverage and not on the word.

| # | witness | n | status |
|---|---|---|---|
| 1 | `chi-tritium-h9` | 9 | ✅ #5168 (partial, 1/30) |
| 2 | `chi-deuteron-h6` | 6 | ✅ **this PR** — full, 11/11, 271.6 s |
| 3 | `chi-deuteron-h6-at-qinv-50dps` | 6 | ⛔ not run |
| 4 | `chi-tritium-h9-at-qinv-50dps` | 9 | ⛔ infeasible here |
| 5 | `chi-helium-3-h9` | 9 | ⛔ infeasible here — measured, see below |
| 6 | `chi-helium-3-h9-at-qinv-50dps` | 9 | ⛔ infeasible here |
| 7 | `chi-helium-4-h12` | 12 | ⛔ infeasible, likely anywhere |
| 8 | `chi-helium-4-h12-numeric` | 12 | ⛔ not run |
| 9 | `chi-helium-4-h12-at-qinv-50dps` | 12 | ⛔ infeasible, likely anywhere |

A **tenth** artifact of the same class was found downstream and is fixed here:
`rho-k-h3a-refinement.witness.json` carried ctype `averaged` and
`abs_tr_M = 0.38828647…`, where the colour-weighted deuteron value is `0.575172329…`.
Nothing had flagged it because it is a consumer's output, not a χ cache — the guard covers
caches only.

### What the deuteron drain actually changed

Every nonzero per-term u-pole order moved by exactly **+8**:

| λ | before | after |
|---|---|---|
| (6,) | 2 | 10 |
| (5,1) | 22 | 30 |
| (4,2) | 38 | **46** ← maximizer |
| (3,3) | 34 | 42 |

The *structure* is preserved — (4,2) remains the unique maximizer, and the gap to
next-highest is still 4 — so the Path A verdict does not flip. It was inconclusive at A=2
before (38 vs predicted 40) and remains inconclusive (46 vs 40). The miss changes sign,
−2 → +6. **Recorded, not explained.** A uniform +8 across four partitions of different
dimension is a suspiciously clean shift and may well have a one-line explanation in the
weighted interface's u-degree; nobody has derived it, and this note does not.

## Why H₉ / H₁₂ are blocked, measured rather than asserted

Symbolic χ cost is dominated by matrix-product expression swell, roughly dim³ per partition
times the crossing count. Splitting the partitions of n by row count:

| n | ℓ(λ) ≤ 2 (Σ dim³) | ℓ(λ) ≥ 3 (Σ dim³) | ratio | max dim, ℓ≥3 |
|---|---|---|---|---|
| 6 | 980 | 7,076 | 7× | 16 |
| 9 | 204,876 | 59,618,008 | **291×** | 216 |
| 12 | 53,105,976 | 2,110,524,100,840 | **39,700×** | 7,700 |

Empirically on this machine (4 cores, sympy 1.14): deuteron n=6 full = **271.6 s**;
helium-3 n=9 reached λ=(8,1) — a **dim-8** partition — in **232 s** before being stopped.
The ℓ≥3 partitions at n=9 run to dim 216, and at n=12 to dim 7,700. Full symbolic H₁₂ is not
a "long run"; it is out of reach by orders of magnitude.

## The `y_λ = 0 ⟺ ℓ(λ) ≥ 3` theorem — real, and not the unlock

#5217's theorem is confirmed empirically against the Wenzl-bridge table at **every** n from
2 to 12: the set `{λ : y_λ ≡ 0}` equals `{λ : ℓ(λ) ≥ 3}` exactly, with no exceptions —
70 of 77 at n=12.

Read against the table above, this is tantalising: the partitions that contribute **nothing**
to the trace are precisely the ones carrying **essentially all** the cost. A consumer that
only ever forms `Σ_λ y_λ χ^λ` could skip 291× of the n=9 work and 39,700× of the n=12 work,
which is what would make H₉/H₁₂ tractable at all.

**It does not transfer to these caches, because at least one consumer reads χ^λ alone.**
[`rho_k_h3a_frobenius_pairing.py:231`](../../computations/rho_k_h3a_frobenius_pairing.py):

```python
chi_over_d = r["chi_lambda"] / r["d_lambda"]
delta_G    = target * chi_over_d / S
```

`Δ_λ^G` is a **per-partition reported quantity** built from χ^λ divided by d_λ — not
multiplied by y_λ. It is well-defined for ℓ(λ) ≥ 3 even though those rows contribute zero to
the sum, and it is printed and stored per partition. Dropping their χ would not make the
`Δ_λ^G` column zero; it would make it **undefined**, silently truncating 70 of 77 rows at
n=12. `delta_lambda_empirical_tabulation.py:412` likewise records `chi_q_at_q0` as its own
column alongside `contribution`.

So the saving is real for the *pole* consumer (`per_irrep_pole_atom.py`, whose per-term
`ord(y_λ · χ^λ)` is genuinely 0 wherever y_λ is) and unavailable for the *shared cache*,
which is the thing that would have to be regenerated. This is the caveat flagged when the
item was queued, now resolved in the negative and with the reason located in a specific line.

**Three ways forward**, none taken here — this is a measurement, not a design decision:

1. **Split the cache by consumer contract** — a `trace-only` variant holding ℓ(λ) ≤ 2, and
   the existing full variant. Makes H₉/H₁₂ pole work tractable immediately; costs a second
   cache and a way to keep the two from being confused for each other, which is the class of
   bug this whole note is about.
2. **Mark skipped entries explicitly** — one cache, with `chi_q_symbolic: null` plus a reason
   for ℓ(λ) ≥ 3. A consumer reading χ alone then fails loudly rather than silently seeing a
   short table. Cheaper, but every consumer needs teaching.
3. **Run the full thing off-session.** Correct for H₉; H₁₂ full symbolic looks out of reach
   regardless of scheduling, so a numeric route (cf. `chi-helium-4-h12-numeric`) is the more
   plausible path there.

## Two defects found in passing

**`qou-okl8` — two producers, one witness filename.** `per_irrep_pole_atom.py:364` emits
`per-irrep-pole-{atom}-h{n}`, which for the deuteron is `per-irrep-pole-deuteron-h6`; that is
the same name `per_irrep_pole_deuteron_h6.py:226` writes directly. The atom producer's schema
is strictly richer. Running the deuteron-specific one over a committed atom-produced witness
silently deletes `cemetery_class_signed_power_projection`, `net_signed_power`,
`is_pure_power_in_cemetery` and the per-`gen_idx` breakdown — 230 deletions against 39
insertions. Triggered here, caught in the diff, restored; nothing lost, but nothing warned.
The two agree on the physics (both give 46/42/30/10), so this is ownership, not arithmetic.

**`qou-tzsp` — the tr_M witness disagrees with itself.**
`atomic-tr-m-mpfr-50dps.witness.json` carries two deuteron values differing by `1.852e-9`,
and an independent Schur–Weyl route matches the `peel_cross_check` branch to `3.1e-49` while
missing the `primary` branch by exactly that amount. `primary` is the field consumers read.
Evidence that `primary` is the wrong number — **scope-(a)**: a localisation, not a proof;
a third independent route is what would settle it.
