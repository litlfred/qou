# The n=3 body-order term is NOT forced by the two stated anchors — one free parameter survives

**Date:** 2026-08-26 · **Bean:** `qou-hh9q` (parent epic `qou-v2om`) ·
**PR:** [#5812](https://github.com/litlfred/qou/pull/5812) ·
**Probe:** [`computations/binding_n3_forcing_probe.py`](../../computations/binding_n3_forcing_probe.py)
**Subject:** [`conj:binding-manybody-eq-jet-filtration`](../../content/quantum-observable-universe/mass-theory/binding-manybody-jet-filtration.md)

## Question

`conj:binding-manybody-eq-jet-filtration` states the binding is a body-order
series `B(K) = Σ_{n≥2} m_e·a_D^(n)` and says it is *"pinned at two body orders
already derived without fitting"* — the n=2 deuteron bond and the n=4
magic-shell term `prop:magic-A-binding-formula`. It then asserts the n=3 term is
the genuine three-body contribution.

If that pinning is rigid, n=3 is a **prediction** and the A=3 mirror pair
(³H/³He) is a genuine test. Is it rigid, and what supplies the rigidity?

## Verdict

**NOT FORCED. The two stated anchors leave exactly ONE free parameter, and the
n=3 weight is a coordinate on it.** A=3 therefore cannot test the n=3 term — it
is what *defines* it. This is a **scope-(a)** statement about what the anchors
determine; it is not a refutation of the conjecture.

Three further findings fall out, each of which weakens the anchors themselves.

## 1. The conjecture has two inequivalent readings with different arities

The displayed equation and the worked form are not the same claim.

| | reading U — the **displayed** equation | reading W — the **scope note** |
|---|---|---|
| form | `B(K) = Σ_n m_e·a_D^(n)` | `B(K) = Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K)` |
| where it appears | the `.md` display, and `term_eq` in the Lean class `QOU.Mass.BindingManyBodyJetFiltration` | the `.md` scope note, and every `w_n` probe/audit on this axis |
| free parameters | **0** | ≥ 1 |

The "Anchors" sentence is about reading W (it needs somewhere for the anchors to
land), while the equation directly above it is reading U. They are different
propositions, and the free-parameter count is exactly what differs — the
`claim-shape` check of AGENTS.md §"Grep the claim SHAPE".

**Reading U is fully rigid and is refuted at the deuteron**, measured at the
proton q₀ pin with `a_D^(n) = S(n)/n`:

| iso | A | `B_pred` (MeV) | `B_AME` (MeV) | err |
|---|---|---|---|---|
| ²H | 2 | 0.51100 | 2.22457 | **−77.0 %** |
| ³H | 3 | 1.19419 | 8.48182 | −85.9 % |
| ⁴He | 4 | 2.48843 | 28.29566 | −91.2 % |

So the corpus does not work with reading U; it works with reading W, in which a
weight appears that the displayed equation does not contain. Everything below is
reading W.

## 1b. A third reading — forced, but not realised anywhere

The displayed equation writes the period as **`a_D^{(n)}(K)`** — K-dependent, a
residue sum over the hyperbolic components of *that* braid. Read literally there
are no weights and **n=3 would be forced with zero free parameters**: the A=3
braid's own residue sum supplies it.

No such object exists in the corpus. Measured across `computations/`, **all ten**
producers that define `a_D` declare it as `a_D(n)` — body order alone, no knot
argument — and each returns `S(n)/n`, a function of `n` and `q`:

`theta_wn_kernel_derive_or_refute`, `theta_wn_jetfilt_linkvolume`,
`binding_fewbody_bondcount`, `binding_wn_kernel_derive_refute`,
`binding_wn_derive_or_refute`, `bk_crossing_coordination`,
`binding_manybody_jet_filtration`, `binding_wn_multianchor_tower_refute`,
`binding_wn_frobenius_dual_probe`, and this probe.

So the K-dependence written in the conjecture is not realised anywhere, and
`w_n(K)` was introduced in the scope note precisely to restore it. **"Forced but
not yet computed" is therefore not a live third option** — there is no per-knot
n=3 residue sum to evaluate. Building one would be the honest route to making n=3
a prediction.

## 2. The counting — one free parameter, invariant under how the n=4 anchor is read

Unknowns through A=4 are `w_2, w_3, w_4` — **three**. The conjecture supplies
**two** anchor equations. Three minus two is one, and the surviving parameter is
`w_3`:

- the n=2 anchor fixes `w_2`;
- the n=4 anchor is **one** equation in the **two** remaining unknowns,
  `m_e(a₂w₂ + a₃w₃ + a₄w₄) = B_magic(⁴He)`.

For every `w_3` there is exactly one `w_4 = (B_magic/m_e − a₂w₂ − a₃w₃)/a₄`, and
**both anchors are satisfied identically along the whole family**. The A=3
prediction along it, `B(³H) = m_e(a₂w₂ + a₃w₃)`, is an unbounded straight line in
`w_3`: every real value of `B(³H)` is reachable with both anchors exact.

The count does not depend on resolving an ambiguity in the n=4 anchor:

- read as the ⁴He **total** (what the `.md` compares to AME): one equation on the
  sum ⇒ `w_3` free — **1 parameter**;
- read as the n=4 **term alone** (`m_e·a₄·w₄ = B_magic`, pinning `w_4 = 23.145`):
  nothing then mentions `w_3` at all ⇒ **1 parameter**.

## 3. How much does a structural side constraint narrow it? — 66–78 %, measured

The conjecture's only structural statement about the weights is that they *grow*
with body order (the "ρ·A scale rule"). Taking the strongest honest reading of
that — positivity `w_3, w_4 > 0` plus monotone growth `w_2 ≤ w_3 ≤ w_4` — and
holding both anchors exact:

| `w_2` from | surviving `w_3` | induced `B(³H)` window | width vs `B_AME(³H)` |
|---|---|---|---|
| the **derived** bond (5.5437) | [5.544, 13.716] | [6.620, 12.204] MeV | **65.8 %** |
| **AME** `B(²H)` (4.3534) | [4.353, 14.024] | [5.199, 11.805] MeV | **77.9 %** |

So the anchors plus monotone growth do constrain something — but to a window
spanning about two-thirds to four-fifths of the observable's own magnitude. A
datum landing inside is worth roughly one bit, not a prediction.

It does land inside: the extracted `w_3` (8.330 / 9.220) satisfies
`w_2 ≤ w_3 ≤ w_4`. **That is the one non-circular check the anchors support** —
a monotone body-order weight sequence reproducing all three nuclei exists — and
it should be reported with its 66–78 % width attached, never as agreement.

## 4. Anchor integrity — both anchors are weaker than the conjecture says

The sentence *"already derived without fitting"* does not survive contact with
either anchor.

**n=4: `ρ_F = 2` is not derived.** Its own context block
([`magic-A-binding-formula-context.md`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula-context.md))
says so in terms: *"The categorical derivation of the integer 2 — vs. `[2]_q`,
`2cos(π/3)`, or another natural candidate — is not closed in this proposition;
the value is consumed as an input hypothesis."* An anchor carrying an
undetermined multiplicative constant is a conditional anchor.

**n=2: the corpus's `w_2` is an extraction, not the derived anchor.** The
derived single p–n bond (convention D, colour-weighted, writhe-normalised) is
`α·L_pn = 2.83282 MeV`, **+27.3 %** above `B_AME(²H) = 2.22457` — the one
negative residual `R(²H) = −0.61` of the
[2026-08-25 staleness audit](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md),
worked separately under bean `qou-39bx`. The `w_2 = 4.353` used across the
2026-07-11 `w_n` audits is `B_AME(²H)/(m_e a₂)` — the **AME** value. The derived
anchor gives `w_2 = 5.544`. The two differ by the same 27.3 %.

Consequence: the n=2 anchor as *used* is data, and as *derived* it is 27 % off
the data. Either way it is not a parameter-free pin.

## 5. The A=3 datum — Coulomb correction computed, not inherited

`E_C(Z,A) = (3/5)·Z(Z−1)·α_EM·ℏc/R`, `R = r₀A^{1/3}`, with `α_EM` **derived**
from q₀ and the canonical `r₀` the **derived** pion Compton length
`ƛ_π = ℏc/m_π = 1.413817 fm` (`computations/coulomb_energy.py`; the empirical
1.2 fm survives there only as `R0_FM_EMPIRICAL`). ³H has `Z = 1`, so `E_C = 0`
identically and only ³He is corrected.

| geometry | `E_C(³He)` | `B_strong(³H)` | `B_strong(³He)` | CSB split |
|---|---|---|---|---|
| `ƛ_π` (canonical, derived) | 0.847422 | 8.48182 | 8.56548 | **−0.0837** |
| 1.2 fm (empirical, legacy) | 0.998416 | 8.48182 | 8.71647 | −0.2347 |
| measured ³He charge radius | 0.680774 | 8.48182 | 8.39883 | +0.0830 |

The raw split is 0.763763 MeV (9.005 % of `B(³H)`) and is nearly all EM, as the
conjecture's scope note says.

**Honest note on the sign.** At the canonical *derived* `r₀` the correction
**overshoots**: ³He comes out the more bound partner and the residual
charge-symmetry breaking is ≈ **−1 %**, not the **+2.73 %** the 2026-07-11 audits
quote (those used a larger `R`, i.e. a smaller `E_C`). The measured-radius row
restores ³H as the more bound partner. The mirror-average `B_strong(A=3)` is
8.52365 MeV at the canonical geometry, and the **spread across all three
geometries is 0.1588 MeV** — two orders of magnitude below the 5.6–6.6 MeV
window of §3, so **the verdict is insensitive to the Coulomb geometry**.

## 6. What the A=3 datum actually yields — an EXTRACTION

Because `w_3` is free, solving for the `w_3` that reproduces `B_strong(A=3)` is
inversion of the datum:

| `w_2` anchor | `w_3` **[EXTRACTION]** | `w_4` (then forced by n=4) | monotone? |
|---|---|---|---|
| derived (5.5437) | 8.32981 | 16.55945 | yes |
| AME (4.3534) | 9.22013 | 16.55945 | yes |

The residual is exactly zero by construction — three unknowns, three equations.
**No agreement is being demonstrated**, and reporting one would be the banned
ansatz pattern. This is also what the corpus's own `w_2, w_3, w_4 =
4.353, 9.331, 15.919` is: an extraction from D / avg(³H,³He) / ⁴He, correctly
labelled *"three equations, three unknowns"* in the
[2026-07-11 residue-weight audit](2026-07-11-wn-residue-weight-kernel-derive-refute.md),
but sitting one paragraph away from a conjecture that calls two of those three
inputs derived anchors.

## 6b. Is the dashboard's `multi-link emit` the n=3 term? — No, structurally

A live `mass_binding_dashboard.py --group low` run (coordinator, 2026-08-26)
shows `B_sym+ent = B_sym + multi-link emit` takes A=3 from `err` 1.38/1.44 to
**1.06/1.07** while making ²H worse (0.79 → 0.56) and barely denting ⁴He
(3.26 → 2.57) — it behaves like a three-body term exactly where one is wanted.

It is **parameter-free**: `E_multilink = α·|((tr_f−tr_a) − (tr_f−tr_a)|_{q→1/q})/2|`,
the bar-odd (q↦q⁻¹-antisymmetric) part of the inter-nucleon binding defect
(`mass_binding_dashboard.py:601-614`). So the near-miss is not a fit.

**But it is not the n=3 term, and one line settles it: a body-order n=3 term is
identically zero on a two-body system.** Recomputed here in exact mpmath:

| iso | `E_multilink` (MeV) |
|---|---|
| ²H | **1.167842** ← must be 0 for an n=3 term |
| ³H | 1.859864 |
| ³He | 1.868493 |
| ⁴He | 2.343734 |

`E_multilink(²H) ≠ 0`, so it is not the n=3 body-order term. It may well be a
real object; it is not *this* one, and its A=3 agreement is therefore not
evidence about the filtration. Until its provenance is separately traced it
deserves the caution its dashboard neighbour `B_vol` earned — tagged
**"DEPRECATED 2026-08-08 postdiction near-match, NOT derived"**.

Incidental defect (not this branch's): the dashboard casts `ta, tf` to `float`
before a **near-cancelling** subtraction, which is where float64 hurts most. The
four values above survive it unchanged, but the pattern should be fixed at that
producer.

## 6c. How conditional are the anchors? — neither is unconditional

Beyond the free parameter, both anchors are weaker than "derived without
fitting" implies:

| | conditionality |
|---|---|
| **n=2** (`B_sym`) | tagged `DERIVED*` — **KVC-CONDITIONAL**. `ln\|tr_M\|` is `Vol` only via `vol-through-tau`, conditional on the **open** `conj:kashaev-volume-conjecture`. The n=2 anchor is derived *conditional on the Volume Conjecture*. |
| **n=4** (`ρ_F`) | `ρ_F = 2` consumed as an input hypothesis (§4). |
| `E_C` (the A=3 correction) | also `DERIVED*`: `α_EM` is derived but conditional on an open Witten-κ Gram-determinant `sorry`; `R = ƛ_π A^{1/3}` is a saturation assumption (the exponent solves to 0.97/0.43/0.53/0.31 at A = 2,3,3,4); coefficient-exactly-1 is a selection among four mass scales (bean `qou-usft`). |

So the phrase *"pinned at two body orders already derived without fitting"*
overstates the anchors in two independent ways — conditionality and the free
parameter — and the free-parameter count holds regardless of how the
conditionality resolves.

## 7. What would supply the rigidity

Nothing currently does. Rigidity for `w_3` would have to come from the **derived**
q-difference kernel `R(q,x)` of `G(qx;q) = R(q,x)G(x;q)` — the conjecture's own
prescription. That kernel is open: no parameter-free constant-ratio kernel
reproduces the extracted ratios to 5 % (`[n]_q²` the lone 6.9 % near-miss,
[2026-07-11](2026-07-11-wn-residue-weight-kernel-derive-refute.md)), and a
universal *scalar* kernel is refuted by the mirror pair
([2026-07-03](2026-07-03-wn-universal-kernel-refuted-mirror.md)). A tuned
recursion is the banned seventh Δ_λ ansatz.

## Recommended correction to the conjecture

The "Anchors" paragraph should say what the anchors do and do not pin. Suggested
replacement of the last sentence, which currently asserts the n=3 term is the
three-body contribution as though it followed:

> The two anchors pin `w_2` and the combination `a₃w₃ + a₄w₄`; they leave one
> free parameter, so the n=3 term is **not** determined by them and A=3 cannot
> test it. Adding positivity and monotone growth narrows the induced `B(³H)` to a
> window 66–78 % of the observable's magnitude, which the data satisfies.

## Scope

**(a) scope-limited.** This measures what the two stated anchors determine. It
does not exclude the jet-filtration identification, does not refute the
conjecture, and does not touch the derived extensive kernel `a_D^(n)`, which is
Lean-proved extensive (`QOU.Mass.JetFiltrationExtensive`, sorry-free). Nothing is
wired to production; no value is fitted.
