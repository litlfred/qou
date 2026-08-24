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

**ANSWERED 2026-08-24, and my first hypothesis here was wrong.** This section
originally offered cyclotomic aliasing as the "likely reason" — that each
frame's exponent mixed the `z`-count with additional sources of its own
cyclotomic (`[2]_q` supplying `Φ₈`, `[2]_√q` supplying `Φ₄`). It was flagged as
a hypothesis rather than a measurement, and it is now **refuted**. The
mechanism is **cancellation**, not extra sources.

Measured by
[`d_frame_cyclotomic_exponent_probe.py`](../../computations/markov/d_frame_cyclotomic_exponent_probe.py):

| atom | Z | N | A | `m = deg_z` | `3A−1` | naive | actual | cancelled | `2N` |
|---|---|---|---|---|---|---|---|---|---|
| proton | 1 | 0 | 1 | 2 | 2 | 2 | 2 | **0** | 0 |
| D | 1 | 1 | 2 | 5 | 5 | 5 | 3 | **2** | 2 |
| T | 1 | 2 | 3 | 8 | 8 | 8 | 4 | **4** | 4 |
| ³He | 2 | 1 | 3 | 8 | 8 | 8 | 6 | **2** | 2 |

1. **The `z`-count really is `3A − 1`, in both frames.** Substituting a free
   symbol for `hecke_symbolic.z_markov` makes `tr_M_atomic` polynomial in that
   symbol; its degree is the `z`-count and is convention-independent by
   construction. **The C derivation's counting is correct.**
2. Substituting `z_D = q³/(q²+1)` into a degree-`m` polynomial gives
   `(q²+1)^m` naively — but exactly **`2N`** factors **cancel against the
   numerator**, leaving `m − 2N = 3A − 1 − 2N = 3Z + N − 1`.
3. The proton (`N = 0`) is the control: zero cancellation.

So the caution above stands, and now with a reason: **`3Z + N` is not a strand
count and not a peel count.** The exponent is `3A − 1` reduced by two per
neutron, and `3Z + N − 1` is arithmetic rewriting of that.

**A note on how the first attempt failed**, because the failure mode is
reusable. The free-symbol substitution is sound only if putting `z_D` back
reproduces the unpatched function exactly. My first attempt bound
`sp.Symbol("q")` while `hecke_symbolic` uses `sp.Symbol('q', positive=True)` —
different objects. The round-trip then built a two-`q` expression: it reported
the deuteron denominator as `192·q²⁵·(q²+1)⁵` against the true
`192·q²³·(q²+1)³`, and reported the cancellation as **zero**. Its `z`-count was
nonetheless *correct*, which is worse than wrong — a coincidence that would
have been recorded as evidence. The producer therefore asserts
`round_trip_reproduces_unpatched` **first**, and reports no degree unless it
holds.

The corroboration of `qou-cxon`'s verdict survives unchanged, and is now
sharper: the D law cannot be obtained by substituting `z_D` into the C
derivation, because the C derivation stops at `z^(n−1)` and never sees that
`2N` of those factors cancel once `z` is concrete.

## Q1 and Q2 are DIFFERENT objects — the conjecture is refuted

It was natural to guess that Q1's interface factor 12 and Q2's per-neutron
cancellation share a mechanism: both are neutron/interface-side, and both
plausibly run through `δ(q) = (q−1)²(1−q⁻⁴)/3`. **They do not.** The
`include_inter` switch separates them, in *opposite* directions:

| atom | Z | N | A | inter | `m` | actual | cancelled | `2N` |
|---|---|---|---|---|---|---|---|---|
| proton | 1 | 0 | 1 | on | 2 | 2 | 0 | 0 |
| neutron | 0 | 1 | 1 | on | 2 | **0** | **2** | 2 |
| neutron | 0 | 1 | 1 | **off** | 2 | **0** | **2** | 2 |
| D | 1 | 1 | 2 | off | 4 | 2 | **2** | 2 |
| T | 1 | 2 | 3 | off | 6 | 2 | **4** | 4 |
| ³He | 2 | 1 | 3 | off | 6 | 4 | **2** | 2 |

- **Q1's factor 12 lives ON the interface** — absent at `A = 1`, and gone
  entirely with `include_inter=False`.
- **Q2's 2-per-neutron cancellation is INTRA-nucleon** — the **lone neutron**
  carries it with no inter-nucleon crossing whatsoever, and D/T/³He still
  cancel exactly `2N` with the interface off.

Opposite dependence on the same switch. The conjecture that they were one
object is **refuted**.

**The sharpest statement of what remains.** Under `bring_color_weighted` at
convention D, a **lone neutron's trace denominator carries no power of
`(q²+1)` at all** (`actual = 0`), while a lone proton's carries 2. That
proton/neutron asymmetry in the cyclotomic content of a *single nucleon* is
the whole of Q2's residue — a much smaller target than the many-body framing
it began in.

Incidental, and it explains the `m` column: with the interface off `m = 2A`
(A separate closures, each `3 − 1 = 2`); with it on `m = 3A − 1` (one joint
closure of `3A` strands). The difference `A − 1` is the linking that fuses A
closures into one.

## Q2's residue closed: the rule is co-location on one generator

Producer:
[`d_frame_neutron_cyclotomic_rule_probe.py`](../../computations/markov/d_frame_neutron_cyclotomic_rule_probe.py)
— 12 configurations, 5/5 assertions.

**Cancellation fires iff some generator carries ≥ 2 averaged crossings.**

| `g0avg` | `g1avg` | cancelled |
|---|---|---|
| 1 | 1 | 0 — **proton (uud)** |
| 2 | 0 | 2 — **neutron (udd)** |
| 1 | 0 | 0 |
| 0 | 0 | 0 |
| 0 | 2 | 2 |
| 3 | 0 | 2 |
| 2 | 1 | 2 |

Not `gen0`-specific — two averaged on `gen1` behaves identically. And it
**saturates**: three on one generator still cancels 2, not 3.

**Composition does not determine it**, which is the crux. Two count-matched
controls, in opposite directions:

- a proton word with one `zero → full` has **exactly the neutron's
  composition** (5 zero, 2 avg, 4 full) and still cancels **0**;
- a neutron word with one `full → zero` has **exactly the proton's
  composition** (6 zero, 2 avg, 3 full) and still cancels **2**.

**Physical content.** The neutron (udd) puts both averaged ud-couplings on one
generator; the proton (uud) spreads its two across both. **Both nucleons have
exactly two** — the p/n asymmetry is where they sit, not how many.

**Interpretation, flagged as such.** Two averaged crossings on the same
generator multiply to a quadratic in it, which the Hecke relation
`σ² = hσ + 1` collapses; two on different generators never meet under that
relation. That reading is *not proved here* — the falsifiable content is the
`max(g0avg, g1avg) ≥ 2` criterion and its saturation.

**Two wrong turns, recorded because the correction was itself the error.** I
first said "same averaged count, different placement" — right instinct, but I
had not checked the other counts. I then corrected that to "not placement; the
neutron trades one identity for one full crossing", which the count-matched
controls refute. Placement was right all along, sharpened to *co-location*.

## An exact relation worth recording

$$
z_D(q) \;=\; q^2 \cdot z_C(q^2)
$$

verified symbolically (`sympy.simplify(z_D − q²·z_C(q²)) = 0`). At `q = u²` this
reads `z_C = u/(1+u²)` against `z_D = u⁶/(1+u⁴)`: convention D is convention C
under `u ↦ u²` followed by multiplication by `u⁴`. The monomial factor moves
only the `u`-exponent, and the squaring maps `Φ₄ ↦ Φ₈` — which is why the two
laws' cyclotomic *bases* correspond while their *exponents* do not.
