# The uniform 6 in the D-frame prefactor lives in one crossing

**Date:** 2026-08-24
**Bean:** `qou-cxon` (Q1 of its two open sub-questions)
**Producer:** [`computations/markov/d_frame_prefactor_localisation_probe.py`](../../computations/markov/d_frame_prefactor_localisation_probe.py)
**Witness:** `computations/d-frame-prefactor-localisation.witness.json`

## The question

`qou-cxon` adjudicated `qou-iayk` and left this explicitly open:

> The `2^(2A+1)` prefactor is derived by crossing-counting, which is
> convention-FREE — yet it moves 32 → 192. So crossing-counting alone does not
> determine it. That needs a real derivation, not a re-count.

The `192/32 = 6` was recorded as uniform but unexplained.

## What was measured

`tr_M_atomic(Z, N)` is an integer-coefficient rational function of `q` with no
anchor in it. Its denominator's integer content is the prefactor. Measured with
the inter-nucleon crossing on and off:

| atom | A | inter=ON | ratio vs C | inter=OFF | ratio vs C | ON/OFF |
|---|---|---|---|---|---|---|
| proton | 1 | 4 | 1/2 | 4 | 1/2 | 1 |
| neutron | 1 | 4 | 1/2 | 4 | 1/2 | 1 |
| D | 2 | 192 | **6** | 16 | 1/2 | **12** |
| T | 3 | 768 | **6** | 64 | 1/2 | **12** |
| ³He | 3 | 768 | **6** | 64 | 1/2 | **12** |
| ⁴He | 4 | 3072 | **6** | 256 | 1/2 | **12** |

"ratio vs C" is against the convention-C law `2^(2A+1)` from
[`d_u_closed_form_proof.py`](../../computations/d_u_closed_form_proof.py),
which derives that exponent by counting averaged crossings: each averaged
crossing contributes `(σ + σ⁻¹)/2`, giving `2A` halvings for the nucleons plus
`+1` for the single mixed (p,n) interface of canonical `pppnnn` ordering.

## Three findings

**1. The intra-nucleon half of the C derivation transfers to D unchanged.**
With the interface off, the D prefactor is exactly `2^(2A)` in all six cases —
ratio `1/2`, uniform in A, Z and N. So `2A` of the C law's `2A+1` is correct in
both frames. Only the `+1` is not.

**2. The entire discrepancy is one crossing, and it does not scale.** Switching
the interface on multiplies the prefactor by exactly **12**, identically for
every `A ≥ 2` regardless of A, Z or N. A contribution that is independent of
the nucleon count is one object, not a per-nucleon or per-strand factor — which
rules out any explanation of the form "each z picks up something". The C law
assigns that same crossing a single halving, i.e. a factor 2. **`12 / 2 = 6`**
accounts for the whole of the uniform 6.

**3. A = 1 confirms it without using the switch.** A single nucleon has no
second nucleon, so no interface exists at all — and proton and neutron already
sit at ratio `1/2` with `include_inter` nominally on. That is independent of
whether the `include_inter` flag does what it says.

## Why a crossing count could not have found it

`12 = 2² · 3`, and **the 3 is not a count of anything.** Under the canonical
`bring_color_weighted` p/n convention the inter-nucleon crossing carries the
colour weight

$$
\delta(q) \;=\; \frac{(q-1)^2\,(1 - q^{-4})}{3}
$$

([`markov_peel.py:100`](../../computations/markov/markov_peel.py), the symbolic
mirror of `_li_2_q_util.flavor_split_leading`). Its rational coefficient has a
3 in the denominator.

So the C proof's `2^(2A+1)` is not *wrong* about the crossings. It is **silent
about the coefficient the interface crossing carries**, and that coefficient is
where the discrepancy lives. A crossing count sees a crossing; it cannot see a
colour weight. That resolves the apparent paradox in `qou-cxon` — a
convention-free derivation appearing to move under a convention change — without
either side being in error: the two are counting different things.

## What this does NOT do

**It does not derive 12.** It relocates the open question from *"why does a
convention-free count move?"* — which had no well-posed answer — to *"derive the
interface factor 12 from `δ(q)`"*, which is a single crossing and a single known
coefficient. That is a much smaller target, but it is still open. **Do not cite
this as a derivation of the prefactor**, and do not wire `6 · 2^(2A+1)` as a
canonical law on the strength of it.

Per the AGENTS.md refuted/ruled-out discipline, every claim here is
**scope-(a)**: a measurement of these six configurations under
`bring_color_weighted` at convention D. Nothing is excluded from any closure.

## Bearing on the second sub-question (the cyclotomic exponent)

Measured alongside, from
[`d_frame_closed_form_law_probe.py`](../../computations/markov/d_frame_closed_form_law_probe.py):

| atom | Z | N | A | D exponent `k_D` | `3Z + N − 1` | C law `3A − 1` | `k_C − k_D` | `2N` |
|---|---|---|---|---|---|---|---|---|
| D | 1 | 1 | 2 | 3 | 3 | 5 | 2 | 2 |
| T | 1 | 2 | 3 | 4 | 4 | 8 | 4 | 4 |
| ³He | 2 | 1 | 3 | 6 | 6 | 8 | 2 | 2 |
| ⁴He | 2 | 2 | 4 | 7 | 7 | 11 | 4 | 4 |

`k_D = 3Z + N − 1` exactly (fitted on three, exact on held-out ⁴He), and
`k_C − k_D = 2N` exactly on all four. The two agree only when `N = 0`.

**A caution against the tempting reading.** The C derivation obtains `3A − 1` as
`n_strands − 1` with `n_strands = 3A`. Applying that reading to `k_D` would give
`n_strands = 3Z + N` — three strands per proton, **one** per neutron — which is
not a plausible strand count, since the atomic braid word carries three strands
per nucleon regardless of isospin. So **the "cyclotomic power = strand count −
1" reading does not survive the frame change**, and `3Z + N` must not be read as
a strand count.

The likely reason is that quantum integers alias onto different cyclotomics in
the two frames. At `q = u²`,

$$
[2]_q = \frac{u^4+1}{u^2}, \qquad [2]_{\sqrt q} = \frac{u^2+1}{u},
$$

so a `[2]_q` factor contributes `Φ₈ = 1 + u⁴` — the **D** cyclotomic — while
`[2]_{\sqrt q}` contributes `Φ₄ = 1 + u²` — the **C** one. The total power of
each frame's cyclotomic therefore mixes the `z` count with different additional
sources, and the two need not decompose the same way. That is a hypothesis, not
a measurement, and is flagged as the next thing to test.

Either way it is independent corroboration of `qou-cxon`'s verdict from the
exponent side: **the D law cannot be obtained by substituting `z_D` into the C
derivation**, because the step that produces the exponent — clearing `z^(n−1)` —
is precisely the step that does not transfer.

## An exact relation worth recording

$$
z_D(q) \;=\; q^2 \cdot z_C(q^2)
$$

verified symbolically (`sympy.simplify(z_D − q²·z_C(q²)) = 0`). At `q = u²` this
reads `z_C = u/(1+u²)` against `z_D = u⁶/(1+u⁴)`: convention D is convention C
under `u ↦ u²` followed by multiplication by `u⁴`. The monomial factor moves
only the `u`-exponent, and the squaring maps `Φ₄ ↦ Φ₈` — which is why the two
laws' cyclotomic *bases* correspond while their *exponents* do not.
