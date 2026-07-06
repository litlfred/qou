# Convergence-safe brane tower for the derived per-crossing V̂_i — four candidates

**Date:** 2026-06-01
**Branch:** `claude/convergence-safe-vhat-tower-2026-06-01` (PR #1657)
**Scope:** Find a DERIVATION-MOTIVATED tower functional `F(V̂_i)` that
accepts the genuine derived per-crossing factor `V̂_i = z·a_i + b_i`
(including `|V̂_0| = 1.146 > q₀`), CONVERGES, reduces to the working
tower in overlap, and lets the p/n signal flow — with ZERO free
parameters. Or a clean negative. No fit, no tuning to m_p / B_AME;
`{e⁻, p, n}` masses are the FALSIFICATION TEST.

**Predecessors (merged):**
[`2026-06-01-vhat-per-crossing-transfer-chain.md`](2026-06-01-vhat-per-crossing-transfer-chain.md)
(#1631 — V̂_i is DERIVED, ∏V̂=tr_M, carries p/n signal) +
[`2026-06-01-vhat-std-channel-fix.md`](2026-06-01-vhat-std-channel-fix.md)
(#1635 — feeding the genuine std V̂_i diverges the Rogers tower at
`Li_2^q(|V̂_0|) = +∞`, root-caused to the radius `|z| < q₀`).

**Compute:**
[`convergence_safe_vhat_tower.py`](../../computations/convergence_safe_vhat_tower.py),
witness
[`convergence-safe-vhat-tower.witness.json`](../../computations/convergence-safe-vhat-tower.witness.json).
All values RAW @ 60 dps. The genuine std V̂_i are recomputed self-
contained from the (a, b) Hoefsmit recurrence and cross-checked
∏V̂(proton) = 1.065306 (= canonical tr_M to 4e-6), p/n g0 split +14.17 %.

---

## VERDICT

**Candidate 2 (analytic continuation of Li_2^q) is the derivation-motivated
convergence-safe tower.** `z = q₀` is **NOT a pole** of `Li_2^q`; it is an
**integrable logarithmic branch point**, so the proton σ₀ divergence is a
**series-truncation artifact, not a real divergence**. The continuation is
unique (`+i0` principal branch, zero free parameters), matches the series
to 1e-30 inside the radius, accepts `|V̂_0| = 1.146 > q₀` with a finite
value `Li_2^q(1.146) = 2.0809 + 0.6568 i`, gives a finite raw tower for
BOTH proton and neutron, and **preserves the p/n signal** (+18.9 %).

The other three candidates fail on structural grounds:
- **Candidate 1 (Φ_q):** structurally refuted by the canonical proof
  (the tower integral IS `Li_2^q`, not `Φ_q`) AND diverges identically
  (same radius `|z| < q₀`) — proton `Φ_q(|V̂_0|) = +∞`.
- **Candidate 3 (bar-symmetrization):** converges but **destroys the p/n
  signal** (washes it to −0.001 %) — fails requirement (d).
- **Candidate 4 (reciprocal V̂↦1/V̂):** **not the bar/antipode image** —
  `1/V̂_0 = 0.873` but the genuine bar image is `V̂(q→q⁻¹) = −0.113`. The
  reciprocal is chosen BECAUSE it lands inside the radius → a FIT (RED).

---

## The analytic-continuation answer (pole vs series-boundary) — the core result

The Rogers q-dilogarithm `Li_2^q(z) = Σ_{n≥1} z^n / (n·[n]_q)` has series
radius `|z| < q₀` because `[n]_q ~ q₀^{n-1}/(q₀−q₀⁻¹)`. The question is
whether `z = q₀` is a **genuine pole** or merely the **series boundary**.

**Derivation.** `Li_2^q' (z) = −ln_q(1−z)/z` where
`ln_q(1−z) = −Σ z^n/[n]_q`. Using the exact Lambert expansion

```
  1/[n]_q = (q − q⁻¹) · Σ_{m≥0} q^{−(2m+1)n}
  ⇒  Σ_n z^n/[n]_q = (q − q⁻¹) · Σ_{m≥0}  (z q^{−(2m+1)}) / (1 − z q^{−(2m+1)})
```

each `m`-term is a Lambert kernel with a **simple pole** at `z = q^{2m+1}`;
the outer sum over `m` converges for any `z ∉ {q, q³, q⁵, …}`. So
`ln_q(1−z)` (hence `Li_2^q'`) is **meromorphic** with simple poles at
`z = q^{2m+1}`, nearest at `z = q₀`.

**Order test (witness `candidate2_analytic_structure`).** The integrand
`−ln_q(1−u)/u`, multiplied by `(q−u)`, converges to a constant (~0.21)
as `u → q₀⁻`:

| `u` | integrand | `integrand·(q−u)` |
|---|---|---|
| 0.9 q₀ | 3.517 | 0.390 |
| 0.99 q₀ | 20.77 | 0.231 |
| 0.999 q₀ | 190.3 | 0.211 |

⇒ the integrand has a **simple pole** at `u = q₀`, so
`Li_2^q(z) = −∫_0^z (integrand) du` has an **integrable logarithmic
singularity** (∫ du/(q−u) = −ln(q−u)) — a **branch point**, NOT a pole.

**Therefore `z = q₀` is the series boundary, not a divergence of the
function.** `Li_2^q` continues past `q₀` along a branch cut on `[q₀, ∞)`.
The `+i0` (upper-semicircle) continuation — the standard principal branch
of the dilogarithm, **zero free parameters** — gives, at the genuine
proton σ₀ factor `|V̂_0| = 1.146101` (`= 1.0325 q₀`):

```
  Li_2^q(1.146101)  =  2.080855  +  0.656782 i      (finite)
```

**Continuation method validated** to full precision: inside the radius
the path-integrated value matches the direct series to **1e-30** at
`z = 0.5 q₀` and `z = 0.9 q₀` (`overlap_match_*` fields). So requirement
(c) — reduces to the working tower in the domain of overlap — holds
exactly.

### Im(q) framing (per AGENTS.md "Im(q) at fibre vs observable level")

The continuation produces a **complex** value with `Im = 0.6568`. This is
consistent with the fibre/observable distinction: the per-generator
`Li_2^q(|V̂_i|)` lives in the **fibre** (pre-τ, formal-q, complex residues
permitted — `term6_full_pole_sum.py` precedent), where `Im` is
unconstrained. The branch-cut imaginary part is a genuine fibre feature.
The **archimedean** (post-τ) mass must be real; whether the
`Σ_i Im Li_2^q` cancels across generators (and across the m_e
normalisation chain) to leave a real observable is the open question this
audit surfaces — it is NOT resolved here and must NOT be assumed. The raw
tower totals below use `Re Li_2^q` only (the honest reporting choice); the
imaginary parts are recorded per generator in the witness.

---

## Per-candidate results (RAW, dimensionless tower T1+T2+T3)

The dimensionless tower is `T1 + T2 + T3` with
`T1 = |∏V̂_i|`, `T2 = Σ_i F(|V̂_i|)`, `T3 = z²·Σ_{i<j} F(|V̂_i V̂_j|)`
(production positive-argument form; the canonical
`prop:mass-endomorphism-tower` negative-argument form `−Li_2^q(−|V̂|)`
shares the same radius, so the finite/divergent verdict is identical).
The MeV `m_p` is `(tower / electron-tower) × m_e`; the finite/divergent
question is dimension-independent, so the dimensionless tower is the
decisive quantity.

| candidate | proton tower | neutron tower | p/n signal | finite? |
|---|---|---|---|---|
| baseline std Li_2^q | **+∞** | 4.18629 | divergent | NO (proton) |
| **cand 1 — Φ_q** | **+∞** | 1.17×10⁶ | divergent | NO (proton) |
| **cand 2 — Li_2^q continued** | **4.97702** | **4.18629** | **+18.89 %** | **YES** |
| cand 3 — bar-symmetrized | 2.70772 | 2.70775 | **−0.001 %** | yes (signal lost) |
| cand 4 — reciprocal 1/V̂ | 3.99736 | 4.15909 | −3.89 % | yes (not derived) |

---

## Candidate 1 — Faddeev Φ_q (mass-channel dilog)

**Structural justification under test.** Cheat-sheet §4 sorts `Li_2^q`
(Rogers, bar-symmetric, BINDING channel) vs `Φ_q` (Faddeev, bar-asymmetric,
MASS channel). Since the V̂_i tower is a MASS contribution (m_p absolute),
should it use `Φ_q`?

**Refuted on TWO independent grounds:**

1. **The canonical proof says the tower integral IS `Li_2^q`, not `Φ_q`.**
   [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/mass-theory/mass-endomorphism-tower.md)
   §"Resolution" + the boxed proposition + its proof: the brane-tower term
   is `−Li_2^q(−|V̂_i|)`, derived as `∫_0^V (ln_q(1+t)/t) dt = −Li_2^q(−V)`
   from the Briggs–Klein chart integration over each resolved defect
   `E_i ≅ ℙ¹(ℂ)`. An **earlier version used `Φ_q` and was explicitly
   corrected** (the `kashaev-integration-identity.witness.json` probe shows
   the literal integration evaluates to `Li_2^q` in the symmetric `[n]_q`
   convention; `Φ_q` differs by 6 orders of magnitude at V=0.989). The
   cheat-sheet's mass/binding sorting governs *which dilog appears in
   absolute-mass vs difference contexts at the M_N / Δm level* — it does
   NOT override the proven identity that **this specific tower integral is
   `Li_2^q`**. Using `Φ_q` here is the historical bar-symmetry bug
   (`mass-endomorphism-tower.md` SUPERSEDED banner; isospin diagnosis).

2. **`Φ_q` diverges identically.** `Φ_q(z) = ∏(1−q⁻ᵏz)⁻¹` has the **same
   radius** `|z| < q₀` (`_phi_q_util.phi_q` returns `+inf` for `|z| ≥ q₀`):
   the `k=1` factor `(1 − z/q₀)` vanishes at `z = q₀`, and for the genuine
   proton `|V̂_0| = 1.146 > q₀` it has already changed sign / passed the
   pole, so `Φ_q(1.146) = +∞`. The neutron's `|V̂_0| = 1.004 < q₀` is
   finite but **gigantic** (1.17×10⁶) — the Φ_q pole proximity amplifies a
   tiny p/n asymmetry into the −737 MeV mirror-nucleus pathology recorded
   in the canonical prop. **Candidate 1 fails (a), (b), and the structural
   justification is refuted.**

This re-confirms the 2026-05-16/17 history (`derive_m_p_hecke_full_tower`
docstring): the Φ_q "closure" was a **pole artefact at `|V̂_p| > q₀⁻¹`**.

---

## Candidate 2 — Analytic continuation of Li_2^q (DERIVED resolution)

**Structural justification.** `Li_2^q` is the proven tower kernel
(candidate 1 §1). Analytic continuation of a function past its **series
radius** is not a new functional or a fit — it is the **same function**,
uniquely determined by its values inside the radius (identity theorem).
The only choice is the branch (which side of the cut), fixed by the
standard `+i0` dilogarithm prescription. **Zero free parameters.**

**Finiteness:** YES — `z = q₀` is an integrable log branch point, not a
pole (see the core result above). Proton tower `= 4.97702`, neutron tower
`= 4.18629`, both finite.

**Overlap (c):** matches the series to 1e-30 inside `|z| < q₀`.

**p/n signal (d): PRESERVED, +18.89 %** — larger than the baseline
std-channel σ₀ split (+14.17 %), because the continued `Li_2^q` is steeper
just past the branch point, amplifying the p (`|V̂_0|=1.146`) vs n
(`|V̂_0|=1.004`) gap. The isospin signal flows.

**Open caveat (honest):** the continuation is complex
(`Im Li_2^q(1.146) = 0.6568`). Reality of the resulting MeV observable is
NOT established here (it requires checking that `Σ Im` cancels through the
m_e-normalisation / electron-tower ratio at the archimedean level). The
raw tower above uses `Re` only. This is the single thing to resolve before
any production wiring — flagged, not assumed.

---

## Candidate 3 — Bar-symmetrization (q ↔ q⁻¹) of the argument

**Structural justification under test.** The binding channel is
bar-symmetric (`Li_2^q = \overline{Φ_q}` under `q↦q⁻¹`,
`prop:li2q-phiq-bar-symmetrization`). Does the canonical binding functional
use a bar-symmetric combination of `|V̂_i|` and its bar image that stays
inside the radius?

**The bar image is genuine and inside the radius:** recomputing V̂ with
`q ↔ q⁻¹` (the Lusztig bar on the chain) gives `V̂_bar(proton σ₀) =
−0.1128` — well inside `|z| < q₀`. The geometric-mean bar-symmetric
argument `√(|V̂|·|V̂_bar|)` is `0.360` (proton σ₀), deep inside the radius.
So a bar-symmetric tower **converges** (proton 2.70772, neutron 2.70775).

**But it DESTROYS the p/n signal:** `p/n = −0.001 %` (versus +14 % in the
std channel). Bar-symmetrising the argument averages V̂ against its
`q→q⁻¹` image, and the proton/neutron asymmetry — which lives in the
bar-ASYMMETRIC part of V̂ — cancels almost exactly. **Fails requirement (d).
A bar-symmetric mass tower cannot carry isospin** — which is precisely why
the canonical sorting puts isospin/binding *differences* in the
bar-symmetric channel and absolute masses (where the signal must survive)
elsewhere. Candidate 3 is internally consistent with the framework but
answers the wrong question for the mass tower.

---

## Candidate 4 — Reciprocal / inversion V̂ ↦ 1/V̂ for |V̂| > 1

**Structural justification under test.** Is there a categorical map
`V̂ ↦ V̂⁻¹` (from Hecke `σ ↔ σ⁻¹` or the antipode) sending `|V̂_0| = 1.146`
to `0.873 < q₀`?

**Refuted: `1/V̂` is NOT the antipode/bar image.** The genuine bar
(`q↦q⁻¹`) image of V̂ is the recomputed Markov-trace scalar:

| | V̂ | 1/V̂ | genuine bar image V̂(q→q⁻¹) |
|---|---|---|---|
| proton σ₀ | 1.146101 | 0.872523 | **−0.112830** |
| neutron σ₀ | 1.003852 | 0.996163 | **−0.195089** |

`V̂ = z·a + b` is a **trace** (a Markov-invariant scalar), not a group
element; the antipode `S(σ_i) = σ_i⁻¹` acts on the *element*, and its
trace is NOT `1/(trace)`. The bar image is even sign-changed (negative),
nowhere near `1/V̂`. So mapping `|V̂_0| ↦ 1/|V̂_0|` has **no structural
backing** — it is selected purely because `0.873 < q₀` keeps the series
finite. **That is a FIT (RED)** by the production-vs-exploratory
discipline (chosen because it converges). The resulting tower happens to
be finite (proton 3.99736) and even keeps a small p/n signal (−3.89 %),
but the construction is illegitimate.

---

## What this audit does and does not claim

- **Does** establish, with a residue/order test at 60 dps, that `z = q₀`
  is an **integrable logarithmic branch point** of `Li_2^q`, NOT a pole —
  so the proton-σ₀ divergence is a **series-truncation artifact**, and the
  `+i0` analytic continuation is a **zero-free-parameter DERIVED
  resolution** that accepts the genuine V̂_i, converges, reduces to the
  series inside the radius (1e-30), and preserves the p/n signal (+18.9 %).
- **Does** refute candidates 1, 3, 4 on structural grounds (1: tower
  integral is provably `Li_2^q` not `Φ_q`, and `Φ_q` diverges identically;
  3: bar-symmetrising kills isospin; 4: `1/V̂` is not the antipode image →
  a fit).
- **Does NOT** wire the continued `Li_2^q` into production, tune any
  weight, or claim a MeV `m_p`. The raw dimensionless towers are reported;
  the MeV step and — critically — the **reality of the complex continued
  value at the archimedean level** are the gated next step, flagged for
  the owner, NOT assumed.
- **Does NOT** tune to m_p / B_AME. `{e⁻, p, n}` are the falsification
  test; the raw towers are reported finite-or-divergent, signal-preserved-
  or-not.

**Single most decision-relevant output:** the divergence is NOT
fundamental. `Li_2^q(|V̂_0|>q₀)` is finite by genuine analytic continuation
(branch point, not pole) — `Li_2^q(1.146) = 2.0809 + 0.6568 i`, zero free
parameters, p/n signal preserved. The remaining gate before production is
whether the imaginary part cancels to a real observable through the m_e
normalisation chain.
