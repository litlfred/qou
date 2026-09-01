---
# qou-ssz6
title: 'RESULT: Q = q0^2 is a fugacity -- the temperature is structurally absent, so A1 dies'
status: completed
type: task
priority: high
created_at: 2026-08-31T06:48:14Z
updated_at: 2026-08-31T06:48:56Z
---


## The result

Probe: `computations/probes/fugacity_conjugate_sector_probe.py` (4 assertions,
all passing). Successor to `qou-ap3d`, which asked whether the framework has a
thermodynamic sector at all.

**It has a full conjugate pair, and no energy anywhere in it.**

### 1. `Z(n) = (1+Q)ⁿ` is a grand partition function

`Q = q₀²` is a **fugacity**, conjugate to `k` — the number of strands in the
second state. Everything follows:

| quantity | value |
|---|---|
| field `log Q = βμ = 2η₀` | `0.208681440639` |
| `⟨k⟩/n = ∂log Z/∂log Q = Q/(1+Q) = (1+tanh η₀)/2` | `0.55198185502620507284` |
| `S/n = log Z/n − (⟨k⟩/n)·log Q` | `0.68773317650021572977` |
| `Var(k)/n = Q/(1+Q)²` (susceptibility) | `0.247297886748` |

The first is checked against an **explicit first moment** over the rebuilt
`Z(12)` coefficients — a finite sum over the partition data — not against
itself. The Legendre transform really is an entropy: it matches the binary
Shannon entropy `H(p)` of the measured occupancy to **1.1e-41**, the precision
floor. And

    S/n = log 2 − η₀²/2 + O(η₀⁴)

with residual `2.95e-5` against `η₀⁴ = 1.19e-4` — the entropy deficit from
maximal is `η₀²/2 = 0.005444` nats/strand.

### 2. And that is exactly why there is no temperature

The coefficients of `Q^k` are the **bare binomials `C(n,k)` — pure integers with
no `q`-dependence**. A partition function with a Hamiltonian carries
`Ω_k·e^{−βE_k}` there; this one carries multiplicity only. So

* the spectrum is **linear in `k`** — the only `q` is the fugacity, no
  interaction, no reference energy;
* only the **product** `βμ = 2η₀` is determined. `β` appears nowhere alone, and
  a linear spectrum has no intrinsic scale: rescale `β` and `μ` inversely and
  `Z` is unchanged.

**The temperature is structurally absent, not merely unfound.** `qou-ap3d`
recorded an *empirical* negative — the corpus's Landauer probe found no
candidate `kT` within 5 %, off by 41.9× to 4266×. This is the **reason** there
was nothing to find.

### 3. A1 dies on structural grounds — and `qou-78pt` can close properly

A1 is "the extensive term is the Markov normalisation; stop dividing it out".
What that retains is

    log Z = S + βμ·⟨k⟩

— a Shannon entropy plus a dimensionless field term, both pure numbers **by
construction**. No member of the normalisation family, and no choice among the
four `E₀` conventions, can make it an energy, because the framework contains no
`1/β`.

`qou-78pt` was reopened on 2026-08-31 when its numerical refutation was withdrawn
(the 6–15× deficit was an `m_e`-vs-`E₀` artifact, `qou-59j5`). It closes now for
the right reason: not *"no family member reaches the target"* — a numerical claim
that did not survive — but **"no family member is an energy"**.

## A cross-check that is NOT a new constant

The polarization of this two-level system is

    2·⟨k⟩/n − 1 = (Q−1)/(Q+1) = tanh η₀ = 0.1039637100524101457

which is, to all 20 digits, the corpus's **already-derived "Coulomb/strong
ratio"** (`def:coulomb-charge`; used by `charge_coulomb_tn3he_derived`,
`em_linking_invariant_probe`, the `mirror_split_*` family, and others).

**Not a new derivation.** The corpus reaches it from the sinh/cosh channel split
of the crossing energy `𝔈_cross = n₊q − n₋q⁻¹`, whose antisymmetric/symmetric
ratio at `n₋ = 0` is `(q−q⁻¹)/(q+q⁻¹)`; multiply top and bottom by `q` and that
*is* `(Q−1)/(Q+1)`. One line of algebra, reached from two different places.

What is new is the **reading**: the same ratio is simultaneously an energy ratio
and a thermal polarization. Being a *ratio* it is scale-free either way — which
is precisely why it survives while the extensive magnitude does not. **The
framework's derived quantities are ratios and polarizations; its one attempt at
an absolute magnitude is the one with no scale.** That is the shape of the whole
mass/binding gap, stated structurally rather than as a list of failed ansätze.

## Disambiguation

Not to be confused with `qou-m1fx` ("rotated index IS fugacity basis"), which is
the DGG/GGM magnetic-electric flux basis `Ind^rot(m,ζ;q) = Σ_e I(m,e)ζ^e` in the
3d-3d correspondence / Route C knot-index lane. Different object, different
lane; the shared word is a coincidence.

## What this closes and what it leaves

**Closed:** the extensive-term magnitude question. There is no deficit to
measure, no scale to pin, and no convention to choose — `log Z` is not an energy
and cannot be made one inside this framework. `qou-59j5`, `qou-ap3d` and this
bean form the chain.

**Left open, and it is a different question:** whether the *`ℏ_q`-suppressed*
observables (Δ(net), the trace differences) can carry the binding magnitude.
Those DO vanish classically and DO pair with `E₀` consistently — they are the
right kind of object. That lane is `t7qv` and it is untouched by any of this.
