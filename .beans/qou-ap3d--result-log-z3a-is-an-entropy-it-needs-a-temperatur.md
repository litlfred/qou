---
# qou-ap3d
title: 'RESULT: log Z(3A) is an entropy -- it needs a temperature and the framework has none'
status: completed
type: task
priority: high
created_at: 2026-08-31T04:52:37Z
updated_at: 2026-08-31T04:53:26Z
---


## The result

Probe: `computations/probes/log_z_is_an_entropy_not_an_action_probe.py`
(6 assertions, all passing). Successor to `qou-59j5`, which asked what `ℏ_q`
power `log Z` carries and whether the framework assigns it an operator class.
**Answer: `ℏ_q⁰`, and no.**

### 1. `Z(n)` is a graded dimension, not an action

Rebuilt from `markov_weights_symbolic`'s own Schur/hook components, the
normaliser's coefficients in `q^{2k}` are **exactly the binomial coefficients**
for `n = 2…6`:

    Z(n) = Σ_λ s_λ(1,q²)·f^λ = Σ_k C(n,k)·q^{2k}

That is the **weight generating function of `(ℂ²)^{⊗n}`**, `q^{2k}` counting the
`k` down-spins among `n` strands at Wenzl level `r = 2`. And

    Z(n)|_{q=1} = 2^n = dim (ℂ²)^{⊗n}

So `log Z(3A)` is a **graded log-dimension** — an entropy of the 3A-strand
Hilbert space.

### 2. The discriminator: behaviour at `q → 1`

Every operator class the `E₀` registry indexes **vanishes** in the classical
limit. Measured, not argued:

    Δ(net) = h(h−2)/2,  h = q − 1/q       →  0    exactly at q = 1
    spectral block sum, D / ⁴He / ¹²C     →  0.0  exactly at q = 1

The block sum vanishes for a visible reason: at `q = 1` every one-crossing
eigenvalue in `b_over_a_evaluator` becomes `±1`, so `|Λ_free/Λ_nuc| = 1` and its
log is zero — `H_n(q) → ℂ[S_n]` and there is no deformation left to carry an
energy.

**`log Z` does not vanish.** It tends to `n log 2`, and per strand at `q₀`

    log(1+q₀²) = 0.802922 = log 2 + (q₀−1) + O((q₀−1)³)
               = 0.693147 + 0.109979 − 0.000204

so **86.33 %** of the extensive term is the `ℏ_q⁰` piece that is still there
where the framework has no energies at all.

### 3. "But `F = −kT log Z` is an energy" — the right objection, and its answer

Entropy times temperature *is* an energy, so the claim is **not** that `log Z`
can never become one. It is sharper: **the conversion needs a temperature, `E₀`
is an action scale, and the framework has no temperature.**

* Every `E₀` convention is (scale) × (`ℏ_q`-suppressed operator), totalling
  `ℏ_q²` (`qou-59j5`). Pairing that with an `ℏ_q⁰` log-dimension breaks the
  registry's own index. `E₀` is not a `kT`.
* **The corpus already hunted for one and failed.**
  `computations/landauer_crossing_energy_probe.py` tests
  `E_H = kT_eff × (information)` against five canonical scales
  {`m_e c_q²`, `m_μ`, `E₀`, `m_e/ℏ_q`, `E₀c_q²`} = {52.05, 105.66, 4.186, 5.157,
  426.4} MeV. Its witness records `near_matches_5pct = {proton: [], neutron: []}`
  — **nothing within 5 %**, ratios running **41.9× to 4266×**. Different
  information measure (crossing information `l·η_q`, not `log Z`), so
  suggestive rather than decisive here — but it is the only attempt on record.
* Run directly for **this** measure: the `kT` that would make
  `3·log(1+q₀²)·kT = a_V` is **6.5594 MeV**, and the nearest framework scale is
  `m_e/ℏ_q = 5.157`, **27.19 % away**. Nothing within 5 %. (Back-computed from
  `a_V`, so it refutes an identification rather than establishing one — which is
  exactly its use.)

### 4. The corpus reads this same object as an entropy elsewhere

`content/quantum-observable-universe/gravity-spacetime/lqg-entropy-qdim-partition-pole.ts`
— **"Horizon entropy as the `q`-dimension partition-function pole"**, citing
`meissner2004`, `domagala-lewandowski-2004`,
`ashtekar-baez-corichi-krasnov-1998`. The gravity chapter reads a `q`-dimension
partition function as an **entropy**; the binding lane has been reading the same
kind of object as an **energy**. Both cannot be right without a temperature, and
§3 says there isn't one. Worth reconciling in the text.

## What this settles

**Every extensive-term deficit reported on 2026-08-31 — 1.57×, 6.9×, 8.38×,
12.84× — manufactured a missing conversion by choosing a scale.** The quantity
being compared to `a_V` is `3 log 2 + O(ℏ_q)` **nats** per nucleon, not MeV.

It also explains, with no new hypothesis, the pattern that has puzzled this lane:
**why the exponent test passed so cleanly while six magnitude ansätze failed
"all in the same way".** An extensive entropy and an extensive energy have the
same `A`-scaling by construction, so `qou-imcd`'s exponent test cannot
distinguish them; the magnitude ansätze were each fitting a conversion between
two different *kinds* of quantity.

## Explicitly NOT claimed

That the `ℏ_q¹` part is the energy. Stripping `log 2` leaves `(q₀−1) = 0.109979`
per strand, and converting *that* to MeV would be the same fit this lane has now
walked into three times — it is still scale-ambiguous by 5.35× (`qou-59j5`).
Recorded as a dimensionless measurement, not a candidate.

## Consequences for the lane

1. **Stop reporting magnitude deficits for the extensive term.** There is no
   determinate deficit and there will not be one until a temperature exists.
2. The **honest** statements are the scale-free ones: A-exponent exactly 1; the
   four counters exactly linear with `letters = 4 × strands`; framing factor
   exactly `q`; `b_nn/b_pp = 1.78`.
3. The successor is **not** "find the temperature" — that is the same
   scale-shopping one level further out. It is: **does the framework contain a
   thermodynamic sector at all?** If `Z` is a partition function, `Q = q²` is a
   fugacity and there should be a conjugate variable; if there is none, `Z` is a
   normaliser and nothing more, and `A1` (the un-normalised-trace attack) is dead
   on structural grounds rather than numerical ones. Either answer closes
   `qou-78pt` properly.
