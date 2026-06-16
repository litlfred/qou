# Q_β / binding double-count — the vacuum channel (2026-06-16)

**Trigger.** Owner observation on PR #2363 ("we are double counting
somewhere") while reconciling two framings of the nucleon `Q`-value:

* **#2363 (counit):** `Q_β = ε(Δ)·𝔈₀`, `ε(Δ) = h²/2 − h` (`h = q − q⁻¹`).
* **#2346 (complex volume):** `𝔙 = 𝔈₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ`, with
  **binding `= Re 𝔙`** (bar-even/`cosh`) and **`Q_β = Im 𝔙`**
  (bar-odd/`sinh`), split by the bar-involution `σ : q ↦ q⁻¹` (`h ↦ −h`).

## Where the double-count is

The net difference `Δ` splits by **bar-parity** into two channels:

| channel | NF support | value | parity (`h ↦ −h`) | #2346 books as |
|---|---|---|---|---|
| **vacuum** | `γ` (identity) | `+h²/2` | **even** (`cosh`/Re) | **binding** (`Re 𝔙`) |
| **crossing** | `σ₀, σ₁` | `−h` | **odd** (`sinh`/Im) | **`Q_β`** (`Im 𝔙`) |

The #2363 counit uses the **full** sum `ε(Δ) = h²/2 − h = vacuum + crossing`.
So it carries the bar-**even vacuum channel** that #2346 independently books
as **binding**. That `h²/2` is the **double-count**: it is attributed to
binding *and* to `Q_β` at once. Machine-checked
([`qbeta_channel_split.lean`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_channel_split.lean),
`double_count`, sorry-free):

```
(h²/2 − h) − crossingChannel h = vacuumChannel h        -- counit Q_β = bar-odd Q_β + vacuum
vacuumChannel(−h) = vacuumChannel h                      -- vacuum is bar-EVEN
crossingChannel(−h) = − crossingChannel h                -- crossing is bar-ODD
```

## Why it matters numerically

The double-counted vacuum channel is **exactly** the term that makes the
counit `Q_β` match (`𝔈₀ = 4.186` MeV, CODATA `Q_β = 0.78233`):

| `Q_β` from | value | vs CODATA |
|---|---|---|
| crossing channel only (`bar-odd`, `Im 𝔙`) | `|−h|·𝔈₀ = 0.875` MeV | **+11.86%** |
| **full counit** (`+ vacuum`) | `|h²/2 − h|·𝔈₀ = 0.784` MeV | **+0.17%** |
| vacuum channel alone (the double-count) | `|h²/2|·𝔈₀ = 0.091` MeV | — |

The `+0.17%` headline match of the counit form is **not** the bar-odd
transition value (`+11.86%`); it relies on adding the bar-even vacuum
channel — the channel `#2346` assigns to binding.

## Resolution branches (the vacuum channel has one home)

The vacuum `h²/2` belongs to exactly one observable. Two clean branches:

- **(A) vacuum ∈ Q_β.** The full counit `Q_β` (`+0.17%`) is correct, and
  `#2346`'s `binding = Re 𝔙` **must exclude** the `γ` channel (else binding
  double-counts it). Then `Q_β` is *not* purely the bar-odd `Im 𝔙`.
- **(B) vacuum ∈ binding.** The bar-parity assignment (`#2346`) is correct:
  `Q_β` = bar-odd crossing channel only (`+11.86%`), the vacuum `h²/2` is a
  binding/static contribution, and the celebrated `+0.17%` counit match was
  **partly a double-count** of the binding channel into `Q_β`.

**Bar-parity is the cleaner categorical criterion** (it is an involution-
canonical splitting, not a hand assignment), and under it branch (B) holds —
which would **demote** the `+0.17%` counit result to a `+11.86%` bar-odd
prediction plus a separately-booked vacuum/binding term. The empirical pull
is the opposite (the full counit fits far better), so the physical question
is whether the `γ`/vacuum content of the neutron (the `−HA·𝟙` correction
from the `d`–`d` crossing, see `negative-debt-confinement.md`) is a
**decay-transition** contribution (branch A) or a **static/binding**
contribution (branch B).

## Next step (test before declaring)

Compute `#2346`'s `Im 𝔙 = Im(𝔈₀·tr_M((Π_free−1)∘𝓜))` numerically for the
nucleon and compare:

- if `Im 𝔙 = 0.875` MeV (+11.86%) → branch (B): the bar-odd channel is the
  true `Q_β`, the counit over-counts the vacuum;
- if `Im 𝔙 = 0.784` MeV (+0.17%) → branch (A): `Im 𝔙` already includes the
  vacuum, `#2346`'s `Re/Im` split is not strict bar-parity, and the counit
  and `Im 𝔙` agree.

Until settled, neither "the `+0.17%` counit `Q_β`" (#2363) nor "binding `=
Re 𝔙` over the full defect" (#2346) should be asserted as final — the
vacuum channel is shared and one of them is over-counting.
