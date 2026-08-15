# The c₃ front's deliverable is a measurement ask

**Date:** 2026-08-15 · **Bean:** `qou-dvlt` (option D) · **PR:** #5100
**Probe:** [`qbeta_c3_measurement_proposal_budget.py`](../../computations/qbeta/qbeta_c3_measurement_proposal_budget.py)

After roughly sixty probes the c₃ front has produced no decidable test, and
today's work established why: it is **precision-blocked, not idea-blocked**.
This note states the resulting ask in the form a nuclear-physics reader can act
on — which number to improve, by how much, and what each level buys.

## The lever

Every c₃ claim passes through one extraction and one amplification:

```
c₃ = (Q_β^exp / Q_N2(q) − 1) / u(q)³
⟹  dc₃/dQ_β = 1 / (Q_N2 · u³) ≈ 2.0688 × 10⁶  per MeV
```

At `u(q₀) = 0.0085172` the inversion carries `1/u³ = 1.618 × 10⁶`. So the
experimental uncertainty on the neutron β-decay Q-value arrives at c₃ multiplied
by two million:

| | |
|---|---|
| `Q_β` (CAL-3) | `0.78233341(61)` MeV |
| `σ(Q_β)` | **0.61 eV** |
| `σ(c₃) = σ(Q_β) · 2.07e6` | **±1.262** |
| `\|c₃\|` | ≈ 2.02 |
| relative | **61 %** |

That is the whole situation. The corpus's headline — *"c₃ agrees with −Vol(4₁)
to ≈0.48 %"* — is a comparison of central values on a 61 %-uncertain quantity,
and in σ it is worth **0.03 σ**. Not weak evidence: no evidence.

## Which number

`Q_β` is reachable two ways, and the corpus carries both.

| route | σ |
|---|---|
| direct CAL-3 (PDG 2024 / AME 2020) | **0.61 eV** |
| `Q_β = m_n − m_p − m_e`, in quadrature | 0.561 eV |

**The second is not a free 9 % improvement.** Quadrature assumes the three
inputs are independent, and they are not: AME2020 is a *global least-squares
adjustment*, so `m_n`, `m_p` and the neutron Q-value are correlated outputs of
one fit. Without the covariance — which this repository does not carry — 0.561 eV
is a **lower bound**, not the route's precision. Everything below is therefore
quoted against the direct 0.61 eV, which needs no covariance to be meaningful.

The variance budget of the mass-difference route is nonetheless informative
about *where the uncertainty lives*:

| | σ | share of variance |
|---|---|---|
| `m_n` | 0.48 eV | **73.3 %** |
| `m_p` | 0.29 eV | 26.7 % |
| `m_e` | 0.00016 eV | 8.1e-6 % |

**An improvement programme that does not touch the neutron mass cannot deliver
the factors below.**

## What each level buys

| target | required σ(Q_β) | factor |
|---|---|---|
| the zero-location test resolves at the μ–p scale | 0.0238 eV | **25.7×** |
| `c₃ ≈ −Vol(4₁)` reaches 1 σ at the **proton** anchor | 0.0191 eV | **32.0×** |
| `c₃ ≈ −Vol(4₁)` reaches 1 σ at the **muon** anchor | 0.0047 eV | **130.3×** |

These were computed by three independent routes and order sensibly, which is a
check on all three rather than a restatement of one. The first is the cheapest
meaningful threshold: below it, the framework cannot distinguish `Vol(4₁)` from
the seven unrelated constants already known to place a zero between the anchors —
the entire genericity window maps into an interval **25.7× narrower** than one
error bar on `q*_S`.

## One measurement or two — the routes differ, and it is not a detail

The mass-difference route adds in quadrature, so **each input must individually
fall below the target**. `σ(m_p) = 0.29 eV` alone already exceeds every target
above. So the two routes ask for different programmes:

| target | direct `Q_β` | `m_n` | `m_p` |
|---|---|---|---|
| zero-location resolves at μ–p scale | **25.7×** | 20.2× | 12.2× |
| `c₃ ≈ −Vol(4₁)` at 1 σ (proton) | **32.0×** | 25.2× | 15.2× |
| `c₃ ≈ −Vol(4₁)` at 1 σ (muon) | **130.3×** | 102.6× | 62.0× |

- **direct route** — one measurement improved ~26×;
- **mass-difference route** — *two* measurements improved, ~20× and ~12×.

Which is the cheaper programme is a domain question this repository cannot
answer. But the choice is now stated in the form an experimentalist works in,
rather than as a single factor on a derived quantity.

## How far the repository can take this on its own — and where it stops

`m_n` is determined through the deuteron: `m_n = m_d − m_p + B_d`. The corpus's
own masses are mutually consistent with that route —

```
m_n + m_p − m_d  =  2.22456637 MeV      (the deuteron binding energy)
```

— so the determination chain is visible from inside the repository. **But the
corpus carries no `M_D_..._ERR`.** Only `m_n` and `m_p` have committed
uncertainties, so the budget **cannot be decomposed past `σ(m_n) = 0.48 eV`**
here. That is the floor of what this repository knows, and the boundary is
stated rather than papered over.

Decomposing further — which of `m_d`, `B_d`, or the ¹²C-relative calibration
actually limits `σ(m_n)` — requires the primary evaluation, below.

## The literature question this note deliberately leaves open

**Is `σ(m_n) = 0.48 eV` improvable by 20×+, and by what technique?** That is the
question a reader needs answered next, and it is not answerable from inside this
repository. It was **attempted here and blocked**: the sandbox's literature
tools return zero results for every query (a bare `"quantum"` search on arXiv
returns nothing), and the egress proxy answers `403` to `CONNECT`, so no
literature was consulted.

Recording that explicitly because the alternative — writing plausible-sounding
sentences about crystal-diffraction γ-ray spectrometry or Penning-trap limits
from memory — is exactly the failure this note is otherwise about. Nothing above
depends on it: every number here traces to a committed witness.

**What to fetch, for whoever has network.** Both are already cited in
`content/schema/references.ts`, and neither PDF is in `uploads/`:

| ref id | what it answers |
|---|---|
| `ame2020` — Wang, Huang, Kondev, Audi, Naimi, *"The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures"*, Chin. Phys. C **45** 030002 (2021) | **the** source: which input data determine `m_n`, and what limits each |
| `codata2022` — *CODATA Recommended Values of the Fundamental Physical Constants: 2022* | the adjustment `m_n`, `m_p` come out of, and their correlations |

Note for an arXiv-based workflow: **AME2020 is published in Chinese Physics C
and is not, as far as this repository can tell, an arXiv preprint** — it is
distributed by the AMDC. Worth knowing before searching arXiv for it.

What is wanted is the **prose on precision limits**, not the mass tables: the
numbers are already committed here (`M_N_MEV_VALIDATION_ERR` etc.). The open
question is *what limits them*, which only the evaluation text answers.

## What is not claimed

Whether any of these targets is experimentally reachable, by what technique, or
at what cost, is **outside what this repository can assess**. This note reports
required σ; a domain reader supplies the feasibility. Saying which number to
improve is useful; pretending to know how is not.

Nor does any of this bear on **(H1)** `c₃^even = −Vol(4₁)` in either direction.
0.03 σ is not evidence *for* (H1), and it is equally not evidence *against* it.
Nothing is being measured. Scope-(a) throughout.

## Why it took ~60 probes to reach this

`σ(c₃) = σ(Q_β)/(Q_N2·u³)` is one line of error propagation, and the `1/u³`
amplification was **the headline result** of the 2026-07-12 capstone
([`2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md`](2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md)).
The derivative was known and much discussed. Nobody multiplied it by the input
error. The same formula was read for its consequence for *signal* and never for
*noise*.

Worth recording as a general lesson, not a local one: a corpus that computes
sensitivity without also computing the induced uncertainty will accumulate
agreements that look strong and are not. The check is cheap and should be
routine wherever an extractor amplifies an experimental input.

## Cross-references

- **σ(c₃) derivation and the 0.03 σ finding** — PR #5093,
  [`qbeta_h1_significance_against_cal3_band.py`](../../computations/qbeta/qbeta_h1_significance_against_cal3_band.py)
- **the zero-location test's 25.7× shortfall** — PR #5084,
  [`qbeta_habiro_evaluation_dichotomy_and_test_power.py`](../../computations/qbeta/qbeta_habiro_evaluation_dichotomy_and_test_power.py)
- **the front-level consolidation and option ranking** — bean `qou-dvlt`
- **why the structural route out is closed** — PR #5100,
  [`qbeta_modular_double_reciprocity.py`](../../computations/qbeta/qbeta_modular_double_reciprocity.py)
