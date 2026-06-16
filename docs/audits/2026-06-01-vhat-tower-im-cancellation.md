# Im-cancellation gate for the candidate-2 continued-Li_2^q V̂ tower

**Date:** 2026-06-01
**Branch:** `claude/vhat-tower-im-cancellation-2026-06-01` (PR #1663)
**Scope:** Resolve the SINGLE open gate flagged (not assumed) by PR #1657:
the candidate-2 analytically-continued Li_2^q brane tower of the derived
per-crossing V̂_i CONVERGES but is COMPLEX (`Li_2^q(1.146) = 2.0809 +
0.6568 i`). Does the **archimedean observable mass** `m = m_e · (tower)`
come out **real**, and — critically — is whatever real projection
emerges **DERIVED** (the τ-functor structurally dictates it) or **CHOSEN**
(taking `Re` because "the mass must be real", which is a fit)?

**Predecessor (PR #1657, merge pending):**
[`2026-06-01-convergence-safe-vhat-tower.md`](2026-06-01-convergence-safe-vhat-tower.md)
— established `z = q₀` is an integrable logarithmic branch point (not a
pole), so Li_2^q continues past it with zero free parameters; candidate 2
ACCEPTED (converges, preserves p/n +18.9%); Φ_q / reciprocal / bar-sym
refuted.

**Compute:**
[`vhat_tower_im_cancellation.py`](../../computations/vhat_tower_im_cancellation.py),
witness
[`vhat-tower-im-cancellation.witness.json`](../../computations/vhat-tower-im-cancellation.witness.json).
All values RAW @ 60 dps via `WitnessBuilder.wrap_legacy` (I14 provenance).
V̂_i recomputed self-contained from the (a, b) Hoefsmit recurrence;
∏V̂(proton) = 1.065306 (= canonical tr_M), p/n g0 split +14.17 %.

---

## VERDICT

**No free, structurally-derived real projection both (i) keeps the
continued-Li_2^q magnitude AND (ii) is dictated by the τ-functor. The
continued tower converges but its archimedean reality is NOT free.**

Two facts decide it:

1. **Only the proton carries an imaginary part.** Among all three
   particles' six per-generator factors, exactly ONE exceeds the Li_2^q
   radius `q₀ = 1.10998`: the proton's `g0 = 1.146101`. Neutron
   `g0 = 1.003852 < q₀` and electron `g0 = 1.104388 < q₀` are both inside
   the radius, so the **neutron and electron towers are purely real**.
   The proton is the *sole* complex tower (`Im(total) = +0.656782`). This
   single asymmetry kills the two "cancellation" routes outright.

2. **The two candidate real projections are mutually exclusive on the
   criteria.** `Re(Li_2^q)` keeps the magnitude but is a **CHOSEN** fit
   (drop Im because the mass must be real). The **DERIVED** archimedean
   real — the Bloch-Wigner dilogarithm `D(z) = Im Li_2(z) + log|z|·arg(1−z)`
   dictated by [`prop:vol-through-tau`](../../content/quantum-observable-universe/mass-theory/vol-through-tau.md)
   + [`archimedean-functor-uniqueness`](../../content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness.md)
   (Bloch-Suslin pentagon-uniqueness) — **vanishes on real arguments**
   (`D(real z) = 0` to 1e-62), collapsing T2 and T3 to zero and leaving
   only the real descended log-volume `T1 = ∏V̂_i`. So the Bloch-Wigner
   route IS real and IS derived, but it does **not** reproduce the
   continued-Li_2^q brane-tower magnitude — it discards it.

**Bottom line:** candidate 2 (continued Li_2^q) gives a finite, convergent,
p/n-preserving tower at the **fibre** level, but there is **no
structurally-derived archimedean real-projection of the complex fibre
value**. Either you take `Re` (a CHOSEN fit, RED by the
production-vs-exploratory discipline) or you take the DERIVED Bloch-Wigner
image, which on the real V̂_i is identically zero on the dilog terms. This
is a **genuine archimedean wall**, not a free resolution. The honest
result is a NEGATIVE: continued-Li_2^q converges but is **not
archimedean-real** through any structurally-justified projection found
here.

---

## Full COMPLEX tower (+i0 branch, RAW @ 60 dps)

`T1 = |∏V̂_i|`, `T2 = Σ_i Li_2^q_cont(|V̂_i|)`,
`T3 = z²·Σ_{i<j} Li_2^q_cont(|V̂_i V̂_j|)` (production positive-argument
form, matches PR #1657).

| particle | term | Re | Im |
|---|---|---|---|
| **proton** | T1 | 1.06530614425 | 0 |
| | T2 | 3.44369716059 | **0.65678229885** |
| | T3 | 0.46801555027 | 0 |
| | **total** | **4.97701885511** | **0.65678229885** |
| **neutron** | T1 | 0.92323322991 | 0 |
| | T2 | 2.92737586894 | 0 |
| | T3 | 0.33568238322 | 0 |
| | **total** | **4.18629148207** | **0** |
| **electron** (4₁) | T1 | 1.03737174807 | 0 |
| | T2 | 3.77457312911 | 0 |
| | T3 | 0.43034646630 | 0 |
| | **total** | **5.24229134348** | **0** |

The imaginary part enters **only** through the proton's `g0 = 1.146 > q₀`:
`Li_2^q_cont(1.146101) = 2.08085459537 + 0.65678229885 i`. All other
factors (`|V̂| < q₀`) are real series values. T1 (descended `∏V̂`) and T3
(here `|V̂₀ V̂₁| = 1.065 < q₀` for the proton, so its T3 stays inside the
radius and is real) carry no Im.

---

## Mechanism-by-mechanism (DERIVED-real vs CHOSEN-real)

### (a) Does Im cancel across generators within one particle?

**REFUTED — clean negative.** For the proton the only Im-bearing factor is
`g0`; there is no second generator past the radius to cancel against.
`Σ_i Im Li_2^q(|V̂_i|) = Im f0 + Im f1 = 0.656782 + 0 = 0.656782 ≠ 0`.
Im(proton total) = +0.656782. Neutron and electron have no Im at all
(nothing to cancel). There is **no cancellation mechanism here** — this is
a structural negative, not a rejected-because-it-doesn't-help choice.

### (b) Does Im cancel via the m_e-normalisation ratio?

**REFUTED — clean negative.** The mass formula is
`m(K) = m_e · tower(K) / tower(electron)`. For the ratio's Im to cancel,
the electron tower would need a matching imaginary part. But the
**electron figure-8 tower is purely REAL** (`|V̂_i| < q₀` for both its
generators), so:

```
  tower(proton)/tower(electron)
    = (4.977019 + 0.656782 i) / 5.242291
    = 0.949398 + 0.125285 i        (STILL COMPLEX, Im/Re = 0.132)
```

The proton's Im divides by a real denominator and survives. Im does NOT
cancel through normalisation. (Even were the electron complex, the Im
parts would have to be *forced equal* by structure to divide out — they
are not, since different `|V̂|` exceed `q₀` by different amounts; any real
ratio would be coincidental, not derived.)

### (c) What does the τ-functor DEFINITION dictate? — the core question

**The τ-functor structurally dictates a real projection, but it is NOT
`Re(Li_2^q)`, and the derived projection collapses the dilog terms.**

Two distinct archimedean rules are written into the definitions:

1. **On the multiplicative quantum-volume generator** (T1 = ∏V̂_i), the
   archimedean rule is the **absolute logarithm**, per
   [`def:algebraic-quantum-volume`](../../content/quantum-observable-universe/mass-theory/algebraic-quantum-volume.md):
   ```
     Φ_1(β) := τ_arch(Vol_q(β)) = ln|Vol_{q0}(β)| = Σ_i ln|V̂_i(q0)|.
   ```
   This is the canonical `|·|_∞ → log|·|_∞` map on the archimedean place
   of the adelic substrate — **not** `Re`, not the full complex value.
   T1 is already real (`∏V̂_i` is a real product); its archimedean image
   is `ln|∏V̂_i| = 0.063262` (proton).

2. **On the dilogarithm / brane-tower object** (T2, T3), the archimedean
   image is the **Bloch-Wigner dilogarithm**, per
   [`prop:vol-through-tau`](../../content/quantum-observable-universe/mass-theory/vol-through-tau.md)
   and
   [`archimedean-functor-uniqueness`](../../content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness.md):
   ```
     lim_{q→1} τ_arch(Φ_q(z)) = D(z) = Im Li_2(z) + log|z|·arg(1−z),
   ```
   the **unique** (Bloch-Suslin) continuous antisymmetric pentagon-coherent
   real-valued functional on `B(ℂ)`. `D` is **real by construction**.

So the functor's answer to "how do I make the complex Li_2^q archimedean"
is unambiguous: **take the Bloch-Wigner combination `D`, not `Re`.** That
is the DERIVED-real route. But the V̂_i are **real** scalars, and for real
`z` the Bloch-Wigner dilogarithm **vanishes identically** (`D` measures
the imaginary hyperbolic volume of an ideal tetrahedron with real
cross-ratio, which is zero):

```
  D(|V̂_0(proton)|) = D(1.146101) = −3.9e-62 ≈ 0
  D(|V̂_1(proton)|) = D(0.929504) = 0
```

Therefore the Bloch-Wigner-projected tower is `T1 + Σ D(|V̂_i|) +
z²·Σ D(|V̂_iV̂_j|) = T1 + 0 + 0 = T1`:

| projection | proton | neutron | p/n |
|---|---|---|---|
| **Re(Li_2^q)** (CHOSEN) | 4.977019 | 4.186291 | **+18.89 %** |
| **Bloch-Wigner D** (DERIVED) | 1.065306 (= T1) | 0.923233 (= T1) | **+15.39 %** |

The DERIVED projection just returns the **descended `∏V̂ = tr_M`** value
(its own p/n is the raw +14.17 % tr_M signal, shifted to +15.39 % by the
z² weighting that survives) — it **discards the entire brane-tower
contribution** because that contribution is precisely the part that went
complex under continuation. The continued-Li_2^q magnitude (4.977) is
**only** recovered by `Re`, which is a fit.

**Conclusion (c):** `Re(Li_2^q)` is **CHOSEN-real** (RED — a fit). The
**DERIVED-real** Bloch-Wigner image exists and is real, but it is **zero
on the brane-tower terms** for real V̂_i, so it does not validate
candidate 2 as a mass functional — it reduces it to the bare descended
volume.

### (d) Does the (+i0)+(−i0) branch average give a real value?

**Real, but CHOSEN.** The cut discontinuity is exactly `f(+i0) − f(−i0) =
2i·Im`, so `((+i0)+(−i0))/2 = Re` by construction:

| particle | avg total | Im(avg) |
|---|---|---|
| proton | 4.977019 | 3.9e-62 (= 0) |
| neutron | 4.186291 | 0 |
| electron | 5.242291 | 0 |

The average reproduces `Re` to machine zero. But **averaging the two
branches is NOT the canonical archimedean prescription**: the standard
dilogarithm continuation (and Bloch-Wigner `D`) commits to ONE branch
(+i0); the principal-value/symmetric branch is a *choice* that happens to
equal `Re`. Unless the τ-functor independently selects the symmetric
branch (it does not — it selects `D`, a different real number), the branch
average is **CHOSEN-real**, identical to mechanism (a/c)'s `Re` fit.

---

## Raw m_p (MeV) per projection — RAW, no tuning

`m(K) = m_e · tower(K)/tower(electron)`, `m_e = 0.51099895069 MeV` (CODATA,
the CAL-1 dimensional anchor — **not** a fit target). The electron figure-8
tower normalisation is itself a modelling choice (flagged); values are RAW.

| projection | raw m_p (MeV) | raw m_n (MeV) |
|---|---|---|
| Re(Li_2^q) (CHOSEN) | 0.485141 | 0.408064 |
| Bloch-Wigner D (DERIVED) | 0.524759 | 0.454775 |

**Both are ≈ 0.5 MeV — three orders of magnitude below the physical
938 MeV.** This is expected and is NOT a defect of the projection: it
reflects that the electron-tower normalisation used here (figure-8 4₁
braid, naive (σ₁σ₂⁻¹)² word) is a *placeholder* — `tower(K)/tower(e)` is
O(1) for all three particles because all three towers are O(5). The
absolute MeV scale comes from the full VolDensity / m_e chain
([`_li_2_q_util.vol_density_borromean`](../../computations/_li_2_q_util.py)),
not from this dimensionless tower ratio. **No value here is tuned to
938.27**; they are reported to show the projection does not magically
produce the physical mass — consistent with the discipline that the raw
output is whatever the structure gives.

---

## p/n signal preservation

| projection | p/n relative | preserved? |
|---|---|---|
| raw V̂ g0 (input) | +14.17 % | — |
| Re(Li_2^q) | +18.89 % | YES (amplified, as PR #1657) |
| Bloch-Wigner D | +15.39 % | YES (≈ raw tr_M, dilog discarded) |

Both real projections preserve the isospin signal. The signal is NOT the
discriminator (both keep it); the discriminator is DERIVED-vs-CHOSEN
(mechanism c) and the collapse of `D` on real arguments.

---

## What this audit does and does not claim

- **Does** compute the full complex candidate-2 tower for proton, neutron,
  and electron at 60 dps (every term's Re and Im in the witness), and show
  the imaginary part enters **only** through the proton `g0 = 1.146 > q₀`
  — the neutron and electron towers are purely real.
- **Does** refute the two cancellation routes structurally: (a) only one
  generator exceeds q₀, so there is nothing to cancel within the proton;
  (b) the electron tower is real, so the m_e-normalisation ratio stays
  complex (Im/Re = 0.132). Both are clean negatives.
- **Does** establish, from the τ-functor DEFINITION
  (`def:algebraic-quantum-volume` + `prop:vol-through-tau` +
  `archimedean-functor-uniqueness` / Bloch-Suslin), that the DERIVED
  archimedean-real projection is the **Bloch-Wigner dilogarithm `D`**, NOT
  `Re(Li_2^q)`; and that `D` **vanishes on the real V̂_i** (1e-62),
  collapsing the brane-tower terms to the bare descended `∏V̂`.
- **Does** classify `Re(Li_2^q)` and the branch-average as **CHOSEN-real**
  (a fit by the production-vs-exploratory discipline), and the
  Bloch-Wigner image as **DERIVED-real** but brane-tower-collapsing.
- **Does NOT** find a structurally-derived real projection that retains
  the continued-Li_2^q brane-tower magnitude. **This is a genuine
  archimedean wall: candidate 2 converges at the fibre level but is not
  archimedean-real through any derived projection.**
- **Does NOT** tune to m_p / B_AME / CODATA. `m_e` is the CAL-1
  dimensional anchor only; raw m_p (≈ 0.49–0.52 MeV under the placeholder
  electron-tower normalisation) is reported as-is.

**Single most decision-relevant output:** the continued tower's
complexity is **not** removed by any structurally-derived projection. The
functor's derived real-image (Bloch-Wigner `D`) is **zero on the
brane-tower dilog terms for real arguments**, returning only the bare
descended volume `∏V̂`; recovering the continued-Li_2^q magnitude requires
`Re`, which is a CHOSEN fit. Candidate 2 is convergent but **not
archimedean-real** — a real wall, not a free resolution. The productive
next direction is whether the brane-tower object should carry a genuine
**complex shape parameter** (so `D ≠ 0`), i.e. whether the V̂_i should be
evaluated at a complex cross-ratio at the fibre level (where Im is
permitted) before the τ-functor — NOT a real-projection of a real-argument
dilog.
