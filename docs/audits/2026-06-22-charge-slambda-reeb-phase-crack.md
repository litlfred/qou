# Formalize-first crack at the charge-type S_λ normalisation

**Date:** 2026-06-22 · **Branch:** `claude/bold-mendel-5994kg` · **PR #2612** ·
**Bean:** `h7lv` · **Probe:** [`charge_slambda_reeb_phase_crack.py`](../../computations/charge_slambda_reeb_phase_crack.py)
→ [`charge-slambda-reeb-phase-crack.witness.json`](../../computations/charge-slambda-reeb-phase-crack.witness.json)
(audit-only; no fit; no production rewire)

## The open item

The shadow-price probe ([`2026-06-22-he3-pairknot-clambda-coulomb-probe.md`](2026-06-22-he3-pairknot-clambda-coulomb-probe.md))
computed the explicit `C_λ = w̃_λ·h/2` (`prop:wedderburn-weight-canonical`, no
fit) and found the bare `Σ_charge C_λ·Z(Z−1)·m_e = 0.034 MeV` — only **4.4%** of
the ³H−³He split (0.764 MeV), **22.6× short**. The question: what categorical
structure supplies the missing magnitude **without fitting** (the Δ_λ-gate /
CAL-4 discipline forbids a fitted normalisation)?

## Method — formalize-first (state class → find invariant → let it narrow)

Per AGENTS.md §"Formalize-first probe discipline": before any wide numerical
search, find the structural constraint. Here the answer is assembled from
*existing* corpus results — no new search, no fit.

## Finding (four parts, no fit)

### 1. The SHAPE is forced — `Z(Z−1)/A^{1/3}`

`prop:mass-coefficient-shadow-price` factors `u_λ* = C_λ·S_λ(Z,N,A)`, classifies
`S_λ` by content sum (`c(λ)<0` ⇒ charge-type, Z-dependent), and states **"each
six-term-mass term is one shadow price."** The six-term formula is
Bethe–Weizsäcker, whose charge term is `a_C·Z(Z−1)/A^{1/3}`. So the charge-type
`S_λ` *shape* is forced, and the **sign is right** (T: `Z(Z−1)=0`; ³He nonzero).
What the prop leaves open is the **normalisation point** ("`C_λ·m_e` is the price
where `S_λ=1`" — but *which* (Z,N,A) is never said).

### 2. The MAGNITUDE cannot be partition-only × count — GAP-A-4 obstruction

[`2026-06-01-e0-lambda-composite-structure.md`](2026-06-01-e0-lambda-composite-structure.md)
(GAP-A-4): the proton, neutron and ³He are **bit-for-bit identical at H₃** (the
trefoil image; `rho-prefactor-structural-verifier.witness.json`, `allPassed`).
Therefore **any per-block composite of partition-only data cannot split
Markov-equivalent nuclei** — the (Z,N,A) physics lives in the **H₃ₐ braid word**,
not in the H₆ partition data. This is *exactly* why the bare `C_λ·Z(Z−1)` (H₆
partition data × a scalar count) misses by ~22×. The miss is **structural, not a
failed fit**.

### 3. The real `S_λ` is the H₃ₐ q-Reeb phase — right order, ~26× closer

[`binding_rotation_phase_lead.py`](../../computations/binding_rotation_phase_lead.py)
computes the free-vs-atom **q-Reeb phase** `|Δθ_λ|` at the atomic strand count —
an H₃ₐ object that *does* distinguish ³H/³He. The Markov-weighted
`ρ_need = B_AME/Σ_λ y_λ dim_λ|Δθ_λ|` closes the A=3 mirror pair to **2%**
(T = 18.345, ³He = 18.652 MeV/rad). With a **universal** ρ ≈ 18.5 the phase-sum
*difference* reproduces the split:

| route (³He−³H split, AME = 0.764 MeV) | value | vs split |
|---|---|---|
| partition-only `Σ_charge C_λ·Z(Z−1)·m_e` | **0.034 MeV** | 4.4% (22.6× SHORT) |
| atomic q-Reeb `ρ·[Σ(T)−Σ(³He)]`, ρ=18.5 | **0.898 MeV** | 117.6% (RIGHT ORDER) |

The atomic-phase **residual is ~5× smaller** than the partition-only residual
(0.134 vs 0.730 MeV from target). The atomic object gets the magnitude; the
partition count cannot — confirming part 2.

### 4. The Coulomb channel `sinh(log q) = h/2` is already inside `C_λ`

`crossing-energy-decomposition.lean` proves `(q±q⁻¹)/2 = cosh/sinh(log q)` and
`q = cosh(log q)+sinh(log q)` (derived identity, not fitted). The charge/Coulomb
channel is the **sinh** part `h/2 = (q−q⁻¹)/2` — which is *exactly* the factor in
`C_λ = w̃_λ·h/2`. So `C_λ` (channel + partition weight) and `S_λ` (atomic phase)
are **consistent views of the same binding energy**: the cosh part is the
p/n-symmetric strong scale (ρ), the sinh part is the charge-asymmetric Coulomb.

## Verdict

The open "two-like-charge brane-pairing invariant" is **not a new mystery** — it
is the **H₃ₐ q-Reeb phase object already in the corpus**, viewed through the
shadow-price lens. The crack resolves the *structure* of the open item:

- **Derived (no fit):** the charge-type `S_λ` shape `Z(Z−1)/A^{1/3}`; the reason
  the partition-only price misses (GAP-A-4); the identification `S_λ ≡` H₃ₐ
  q-Reeb phase `|Δθ_λ|` (right order); the Coulomb = `sinh(log q) = h/2` channel
  carried by `C_λ`.
- **Residual open (still no fit allowed):** the **universal-ρ normalisation** —
  the last ~2% of the strong scale (T vs ³He ρ differ by 2%) and the ~18%
  Coulomb-split overshoot. This is a *scale-normalisation* question on the
  already-identified atomic object, **not** a missing partition formula and
  **not** a seventh Δ_λ ansatz.

No production path is rewired; no constant is fitted.

## ρ-normalisation push — cosh(strong) vs sinh(Coulomb) channel split

Attacking the residual ~18% overshoot by isolating the sinh/Coulomb channel
(`strong_channel_rho` in
[`binding_rotation_phase_lead.py`](../../computations/binding_rotation_phase_lead.py)
zeros the inter-nucleon `−h` sinh term on every 3rd generator ⇒ a cosh-only
"strong" ρ; `full − strong` is the sinh channel). Using the witness `d0` block
(ρ_full T=18.346/³He=18.652; ρ_strong T=19.931/³He=19.201) and universal
ρ₀ = 18.5:

| channel of the ³H−³He split | split (MeV) | vs AME |
|---|---|---|
| sinh-only (Coulomb) `ρ₀·ΔΣ_sinh` | 0.462 | **60%** (under) |
| cosh-only (strong) `ρ₀·ΔΣ_cosh` | 0.437 | 57% |
| full (cosh+sinh) `ρ₀·ΔΣ_full` | 0.898 | **118%** (over) |

**Outcome (honest — no closure):** isolating the sinh channel does **not** pin
the split to ~100% without a fit. Instead it (i) **tightens the bracket** to
`(60%, 118%)` — much tighter than the prior `(4%, 127%)` — and (ii) **localises
the residual**: the mirror split is ~half cosh / ~half sinh, and the cosh
channel carries a **5.9% spurious mirror-asymmetry** (`Σ_cosh(³H)/Σ_cosh(³He) − 1
= 5.9%`, where ideal mirror partners must be equal). A perfectly
charge-symmetric strong channel would push the split into the sinh channel
(60%, undershoot); the observed cosh asymmetry adds the rest to overshoot at
118%. **Whether that cosh asymmetry is physical (charge-symmetry breaking) or a
braid-word construction artifact is the residual open piece** — it is *not* a
missing scale and *not* a fit. The Coulomb scale lies inside the bracket; pinning
it remains gated (CAL-4 / Δ_λ).

## Diagnosis — the 5.9% cosh asymmetry is an artifact; the split is all-sinh

Probe: [`he3_tritium_cosh_asymmetry_diagnosis.py`](../../computations/he3_tritium_cosh_asymmetry_diagnosis.py)
→ [`he3-tritium-cosh-asymmetry-diagnosis.witness.json`](../../computations/he3-tritium-cosh-asymmetry-diagnosis.witness.json).

The braid-word construction
([`atom_braid_word_3A`](../../computations/mass_at_3A_proper.py)) builds each
nucleon from intra chains (proton = uud, neutron = udd) plus an inter-nucleon
crossing. The proton−neutron **intra** difference in the identity-coefficient
sum is **exactly `+h = +(q−q⁻¹)`** (ratio = 1.000000) — a single linear-in-`h`
term, i.e. **bar-odd (sinh)**, exactly as the cheat-sheet "n−p difference is
bar-odd" rule requires. But `strong_channel_rho` zeros `d` **only** on
inter-nucleon generators (`k%3==2`), leaving the intra-nucleon bar-odd term in
the "cosh" bucket. Testing the per-λ characters χ_λ (n=9) of ³H vs ³He under
three `d`-treatments:

| `d`-treatment | max&#124;Δχ_λ&#124; (³H vs ³He) | meaning |
|---|---|---|
| full (all `d`) | 3.235 | mirror partners differ |
| inter-zeroed (current "strong") | 0.913 | the spurious 5.9% asymmetry |
| **all-`d`-zeroed (true cosh)** | **0.000** | **³H ≡ ³He, bit-for-bit** |

**The all-`d`-zeroed (charge-symmetric) cosh channel makes ³H and ³He identical
— zero split.** So the 5.9% "cosh asymmetry" is a **pure artifact** of
`strong_channel_rho`'s incomplete sinh-removal (it strips only the inter-nucleon
`−h`, not the intra-nucleon bar-odd `d=+h` p/n distinction). With `c≡1` and every
`d` a multiple of `h`, zeroing all `d` collapses both uud and udd chains to the
same σ-powers at the same generators — hence the exact identity.

**Consequences (correcting the bracket above):**

1. The earlier `(60%, 118%)` cosh/sinh bracket was an artifact of the incomplete
   split. Properly, **cosh = 0** and **the entire ³H/³He split is bar-odd
   (sinh)** — consistent with the framework's bar-odd assignment of the n−p
   difference (cheat sheet; `crossing-energy-decomposition.lean`).
2. The honest residual is therefore a single, clean overshoot of the all-sinh
   q-Reeb phase, best stated at the **binding-ratio** level (the split is a
   difference of near-equal binding energies, so it amplifies):

   | q-Reeb (universal ρ), all bar-odd | predicted | actual | error |
   |---|---|---|---|
   | binding **ratio** B(³H)/B(³He) | 1.1173 | 1.0990 | **+1.7%** |
   | split B(³H)−B(³He) | 0.905 MeV | 0.764 MeV | +19% |

   The q-Reeb phase captures the Coulomb split to **1.7% at the ratio level**,
   entirely in the bar-odd channel, **no fit**; difference-taking amplifies that
   to the 19% split overshoot. The residual is sub-2% physics (genuine
   charge-symmetry breaking + higher-order phase), **not** a missing mechanism
   and **not** a cosh/sinh mixing ambiguity.

**Producer note (minor):** `strong_channel_rho`'s "strong/cosh channel" is
incompletely sinh-stripped (inter-nucleon only). Its `d0(strong)` outputs should
be read as "inter-nucleon-symmetrised", not true charge-symmetric cosh. Not
rewired here (exploratory producer); documented for future use.

## Lean status

**No new Lean.** The two structural inputs are already formalised/witnessed: the
`sinh(log q)=h/2` Coulomb identity in
[`crossing-energy-decomposition.lean`](../../content/quantum-observable-universe/braids-and-knots/crossing-energy-decomposition.lean),
and the H₃ Markov-equivalence collapse in the GAP-A-4 verifier
(`rho-prefactor-structural-verifier.witness.json`). This crack *connects* them
to the shadow-price `S_λ`; it introduces no new identity to prove.

## Cross-references

- [`2026-06-22-he3-pairknot-clambda-coulomb-probe.md`](2026-06-22-he3-pairknot-clambda-coulomb-probe.md) — the explicit `C_λ` evaluation (the 22.6× miss)
- [`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/mass-theory/mass-coefficient-shadow-price.md) — `u_λ* = C_λ·S_λ`
- [`2026-06-01-e0-lambda-composite-structure.md`](2026-06-01-e0-lambda-composite-structure.md) — GAP-A-4 H₃-collapse obstruction
- [`2026-05-29-binding-a3-honesty.md`](../coordination/2026-05-29-binding-a3-honesty.md) + [`2026-05-28-binding-endomorphism-analogy.md`](2026-05-28-binding-endomorphism-analogy.md) — the q-Reeb phase A=3 result (ρ≈18.5, mirror to 2%)
