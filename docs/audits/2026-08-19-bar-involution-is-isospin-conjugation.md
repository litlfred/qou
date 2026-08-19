# The bar involution is isospin conjugation

**Date:** 2026-08-19
**Bean:** `qou-e58e` (option D of the fibre workplan)
**Probe:** [`computations/substrate/bar_involution_is_isospin_probe.py`](../../computations/substrate/bar_involution_is_isospin_probe.py) — ASSERTIONS PASS
**Workplan:** [`2026-08-19-frakv-fibre-workplan-options.md`](2026-08-19-frakv-fibre-workplan-options.md)

Option D was opened to make `tr_M(q₀⁻¹)` computable, on the stated ground that
the canonical color-weighted atom word is `q₀`-baked and cannot re-lift. **That
premise was false**, and the work that replaced it produced a structural result
the corpus did not have.

---

## 1. The premise was false, and the false statement was load-bearing

`tr_m_atom_via_transfer.tr_m_atom_zn`'s docstring said two contradictory things
about the same function, thirty lines apart:

> *"the canonical color-weighted atom word is **q₀-baked** … passing `q ≠ q₀`
> with that convention raises `ValueError` (a true q-sweep needs a
> q-parameterised word builder)"*

> *"q-parameterised core: build the word AT q … so `q≠q₀` (e.g. `q₀⁻¹`,
> simulator N-grids) re-lifts cleanly instead of raising"*

The second is true. `tr_m_atom_zn(1, 1, q=1/q₀)` returns in **milliseconds**, and
12 of the deuteron word's 23 letters change under the substitution. The first
paragraph predated the q-parameterisation and was never updated.

This was not a cosmetic staleness. The sentence was read — by me, in the
predecessor audit — as evidence that the bar image is uncomputable, and a whole
workplan item was opened on it. Both sites are corrected in this commit.

A second, independent site said the same thing:
`complex_volume_witness.py`'s bar-norm guard cited that docstring as its reason
for returning `None`. **It is not the reason.** The `try`/`except` never fires;
what fires is `bar_prod > 0` failing, because

| quantity | value |
|---|---|
| `tr_M^atom(q₀)·tr_M^atom(q₀⁻¹)` | **−8.5174e-4** |
| `tr_M^free(q₀)·tr_M^free(q₀⁻¹)` | **−3.2974e-3** |

Both negative. So the "principled bar-norm mass modulus" is not *"not yet
computable"* — **as a real number it does not exist for this word**. That is a
stronger claim than the one the guard was making, and it should be recorded as
such rather than left looking like a tooling gap someone might close.

## 2. The Jones–Markov weights are exactly bar-even

Measured at five values of `q`, over all 11 partitions of 6:
`max |y_λ(q) − y_λ(1/q)| / |y_λ(q)| = 0` — bit-identical, not merely close.

The values do vary with `q` (`y₍₆₎` runs 0.1153 → 0.1630 → 0.3495 across the
grid), so this is bar-evenness, not a constant or a cache hit.

The reason is structural: `y_λ` is built from ratios of `q`-integers
`[k]_q = (q^k − q^{−k})/(q − q^{−1})`, whose numerator and denominator are each
bar-**odd**, so every such ratio is bar-**even**.

**Consequence.** No bar-odd material can enter `tr_M` through the Wedderburn
weights. All bar parity lives in the **word**. This generalises the
convention-D two-row observation (`y₍₃₎ = (q⁴+1)/(q²+1)²`,
`y₍₂,₁₎ = q²/(q²+1)²`, both manifestly bar-even) from `n = 3` to a measured
statement at `n = 6` with a reason that holds at every `n`.

## 3. The result: bar exchanges mirror nuclei

Write `L(Z,N; q) = ln(tr_M^free / tr_M^atom)` — the argument of the log-trace
binding `𝔈_bind = E₀·L`. Then

> **`L(Z, N; q) − L(N, Z; 1/q) = δ(q)`, with `δ` independent of `(Z,N)`.**

Measured over `A = 2 … 6`, both orientations of every mirror pair (11 nuclei),
at five values of `q`:

| `q` | `δ(q)` | spread over nuclei |
|---|---|---|
| `q₀` | 3.2828999269244323183e-5 | 7.9e-24 |
| `1+π/30` | 2.6018423704218041749e-5 | 6.6e-24 |
| `√5/2` | 4.5864264788095878698e-5 | 1.6e-22 (well-conditioned subset) |
| `√2/1.1` | 2.5986147556136785145e-3 | 5.5e-30 |
| `e^{1/3}` | 1.0437444437813325899e-2 | 2.4e-30 |

So on the canonical color-weighted convention, **`q ↦ q⁻¹` acts as
proton↔neutron conjugation**, exactly, up to one universal `q`-dependent offset.
Self-mirror nuclei (`Z = N`) are bar-even up to `δ`; mirror pairs map to each
other. ³H at `q₀` and ³He at `q₀⁻¹` agree to 22 digits after subtracting `δ`.

**Conditioning, stated rather than hidden.** `L` is a log, so a nucleus whose
`tr_M` sits near a zero at the bar image has an ill-conditioned `L`. At `q = √5/2`
five of the eleven nuclei have `|tr_M(1/q)|` down to 8.9e-18 and their deviations
rise to 5.3e-16 accordingly. The probe asserts strictly on the well-conditioned
subset and reports the rest with `|dev|·|tr_M|min` bounded by 1e-25 (measured
range 3e-30 … 3e-27). That product spans three decades, so it is a **bound**, not
a sharp `1/|tr_M|` scaling law, and the probe says so. Raising `mp.dps` does not
help — the values are bit-identical at 60 and 140 dps, so the precision cap is
internal to the transfer path, which is worth knowing independently.

## 4. How big is `δ`, and why it matters

`δ(q) = O(h⁵)` with `h = q − q⁻¹` — the mirror asymmetry vanishes to fifth order
at the classical point. At the substrate anchor:

- `δ(q₀) = 3.2829e-5`
- `L(deuteron; q₀) = 0.67682`
- **relative: 4.85e-5**

The L2 100× target for `Q_β` is 7.8 ppb. **`δ/L` is 6219× that target.** The
mirror asymmetry is therefore not a negligible correction at the precision the
framework aims for — it is four orders of magnitude above the target for the
observable it most plausibly bears on.

**Not identified.** `δ/h⁵` is 0.0822 at `q₀` but 0.0723 by `q = 1.396`, so `h⁵` is
the leading *order* only. No closed form is asserted; naming a constant against
this five-point sample would be a fit, and the corpus forbids it.

## 5. What this does and does not say about `conj:binding-qbeta-complex-volume`

The conjecture assigns the bar-even channel to binding (`Re 𝔙`) and the bar-odd
channel to `Q_β` (`Im 𝔙`). The result above says the bar-odd partner of the
bar-even binding is the **mirror-pair difference** — and ³H → ³He *is* a β decay.
The channel the conjecture assigns to `Im 𝔙` is exactly the channel the bar
involution turns out to generate.

That is a **consistency, not a derivation**, and the distinction is the whole
point of recording it carefully:

- Nothing here derives `Im 𝔙`. `complex_volume_witness.py` still **assigns** it
  from `q_beta_substrate`.
- The identification of the mirror difference with `Q_β` is **not made**. The
  free-neutron `Q_β` (0.784 MeV) and the ³H→³He `Q`-value (18.6 keV) are
  different numbers; relating them needs an argument this probe does not have.
- The observable-level degeneracy is untouched: `Im(q₀) = 0` still gives
  `Im 𝔙 ≡ 0` after `τ`.

What it does change is the workplan. Option D was scoped as compute-engineering
to unblock bar-parity checks. The unblocking was already done; what the checks
then showed is that **bar has a meaning on these words** — isospin conjugation —
which is a structural input the other options can use, and which nothing in the
corpus stated.

## 6. Follow-on

1. **Formalize the mirror law.** `L(Z,N;q) − L(N,Z;1/q) = δ(q)` with `δ`
   nucleus-independent is a clean statement for Lean, and it is exactly the
   formalize-first shape: prove the invariant, then let it prune. Deriving `δ`'s
   closed form symbolically from the deuteron word is the honest route to
   identifying it — the five-point numeric sample is not.
2. **Re-scope the four bar-oddness sites** (`qou-sglq`) with this in hand: the
   supporting quantity *is* computable, and what it shows is a mirror law, not
   the bar-oddness those sites assert.
3. **The bar-norm claim should be retired, not repaired.** It is negative.

## What this audit did not do

- It did **not** identify `δ(q)`, and deliberately did not scan a basis for it.
- It did **not** derive `Im 𝔙`, nor connect the mirror difference to `Q_β`.
- It did **not** re-run or refresh `complex-volume-unification.witness.json`.
  The edit there is comment-only and every emitted number is byte-identical; a
  regeneration in this container drops `scipy` and `clarabel` from the
  environment block, trading a richer provenance record for nothing. The
  `scriptHash` drift is accepted and noted here instead.
