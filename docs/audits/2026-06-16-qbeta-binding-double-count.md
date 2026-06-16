# Q_β / binding "double-count" — investigated and RETRACTED (2026-06-16)

> **RESOLUTION (branch A — no double-count).** The double-count hypothesis
> below was **tested and refuted**. #2346's witness
> `computations/habiro/habiro-exact-qbeta.witness.json` reports
> `Q_A = Im 𝔙 = 0.7836458028 MeV`, which equals the **full** counit
> `|ε(Δ)|·𝔈₀` to `2·10⁻¹⁶`. So #2346's `Q_β = Im 𝔙` is the *whole* counit
> value (+0.17%), **not** the bar-odd part alone (+11.86%). The two framings
> **agree**; there is **no double-count**, and the #2363 counit `Q_β` headline
> stands. The error was conflating the counit's *internal* bar-parity split
> with #2346's *separate* Re/Im split of the single-knot confinement defect.

## What was hypothesised (and why it was wrong)

Owner observation on PR #2363 ("we are double counting somewhere"), against
two framings:

* **#2363 (counit):** `Q_β = ε(Δ)·𝔈₀`, `ε(Δ) = h²/2 − h`.
* **#2346 (complex volume):** `𝔙 = 𝔈₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ`,
  `binding = Re 𝔙`, `Q_β = Im 𝔙`, split by the bar-involution.

The (incorrect) hypothesis was that #2346's `Im 𝔙` is the **bar-odd part of
the same `Δ`** (`−h`, giving +11.86%), so the counit's bar-even `h²/2` would
be a vacuum channel **double-booked** as binding. The bar-decomposition of
the counit is real algebra — `ε(Δ) = (h²/2)_{even} + (−h)_{odd}`, machine-
checked in
[`qbeta_channel_split.lean`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_channel_split.lean)
— but the **identification of `Im 𝔙` with the bar-odd part was unjustified**.

## The test that settled it

`#2346`'s `Im 𝔙` is **not** the bar-odd part of the `n−p` counit. Per
`im-complex-volume-intro.md`, `Q_β = Im 𝔙` is the **transfer-matrix / Habiro
`Q`-value chain** (the `sinh` channel of the **single-knot confinement
defect** `(Π_free−1)∘𝓜`, a different object from `Δ = NF(n)−NF(p)`),
evaluated at the substrate. Its witnessed value:

| quantity | value | source |
|---|---|---|
| `#2346` `Q_A = Im 𝔙` | `0.7836458028` MeV | `habiro-exact-qbeta.witness.json` |
| `#2363` counit `|ε(Δ)|·𝔈₀` | `0.7836458028` MeV | this session |
| difference | `2·10⁻¹⁶` MeV | — |
| bar-odd-only `|−h|·𝔈₀` (the wrong guess) | `0.875` MeV (+11.86%) | refuted |

So `Im 𝔙 = ε(Δ)·𝔈₀` exactly. **Branch A.** The two Q_β framings are the same
number to machine precision — complementary presentations (Form A counit ↔
`Im 𝔙` of the confinement defect), related through the known
Form-A/Form-B bridge, **not** a double-count.

## Consequences

- The `+0.17%` counit `Q_β` (#2363) and `Q_β = Im 𝔙` (#2346) **cross-validate**.
- The counit's internal bar-split (`barEven`/`barOdd` in the Lean) is an
  *internal* decomposition; it does **not** correspond to #2346's
  binding/Q_β split (which is Re/Im of a different, confinement defect).
- `#2346`'s binding (`Re 𝔙`) is the confinement-defect real part — a separate,
  large quantity — and is **not** the counit's `h²/2`. No channel is shared.
- The earlier owner comment flagging my `+0.17%` as "provisional / possibly a
  double-count" is **withdrawn**; the headline stands.

Recorded for the audit trail: the hypothesis was reasonable, formalize-first
testing (compute `Im 𝔙`, compare) refuted it cheaply before it propagated
into the paper.
