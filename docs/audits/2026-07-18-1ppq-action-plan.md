# 1ppQ action plan (2026-07-18) — the misses are measurement-limited; three named moves

**Date:** 2026-07-18 · **Axis:** program-level (L1/L2 + keystone) · **Tier:**
action plan (synthesis of ~248 origin/main commits 07-17→07-18; no new result;
no fit; no c_k wired; no tier change). **Supersedes**
[`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md).

## The reframe (two new sorry-free theorems)

The window's most important results are two Lean-proved structural facts that
together change *what the L2 misses are gated on*:

1. **A_ω anchor-invariance prune** — `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
   ([`SRigidityPrune.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean),
   sorry-free): any *anchor-invariant* datum cannot equal the c₃ carrier `S`,
   which swings 2.44 % between the proton and muon q₀ anchors at Δq₀ ~ 1e−8. This
   **excludes** deformed median resummation (computed anchor-blind) *and* classical
   CS(5₂) (anchor-invariant) as c₃ realisations.
2. **μ–p pin-sensitivity map** — `PinRobustnessOfRatios.lean` (sorry-free, #3847):
   the μ–p tension lives entirely in the absolute anchor `ℏ_q⁻²`; every **ratio**
   observable (W_λ, m_p/m_μ, m_n/m_p, the whole McKay keystone) has `ν_ℏ = 0` and
   is structurally **blind** to the 11.5 ppb split.

**Consequence.** c₃/S is intrinsically the *anchor-dependent* quantum `𝔙_q` at q₀
(the `1/u³` inversion of a smooth zero-crossing numerator), precision-limited by
the **experimental neutron Q_β measurement** (`dq*/dQ_β ≈ −0.54`), *not* by
resummation method or knot choice. And m_p/m_μ can only be closed by an
**anchor-free absolute q₀** — no ratio/geometric-W_λ route can move them. Net:
**4 of the 5 L2 misses (Q_β, m_n, Δ_pn via c₃; m_p, m_μ via q₀) are provably
measurement-limited absent a substrate-q₀ derivation.** L2 stays **2/7**
(m_e, m_K/m_π); nothing wired this window.

## The five L2 misses + α_EM — each as one named open computation

| Miss (factor) | Root cause | Single named open computation | Owner |
|---|---|---|---|
| **Q_β 160×, m_n 416×, Δ_pn 159×** | c₃ = bar-**odd** `𝔙_q` at q₀ | geometric `Im 𝔙_q → N_odd` normalization capstone on the **deformed (u≠0)** leg (u=0 Stokes integer **3** *derived* + GHHR-validated but excluded: 4₁ amphichiral ⇒ CS=0 at u=0) | #3898 (deformed leg), #3818 (Écalle), #3805/#3872 (u=0 Stokes, done) |
| **m_p 437×, m_μ 964×** | substrate q₀ (μ–p pin) | **anchor-free absolute q₀** via Murakami deformed-VC categorical N-selection (no fit) | uncontended (#2503 is the *pin-blind* geometric W_λ route) |
| **α_EM** (headline) | photon per-loop measure `1/(8π)` | **(a)** reciprocal-form + `8π = 2·4π` multiplicity joint (**unowned**); **(b)** polarized-Jacobian genus-4 theta-factor magnitude leg | (a) ledger-owned; (b) #3911 |
| **L1** | — | **CLOSED** — 6/6 atoms 1ppQ, now a **third** independent method (color-weighted seminormal tr_M, worst 7.28e−49) | done |

## What is settled / newly excluded (so effort isn't wasted)

- **α_EM:** count `1/b₁ = 8` **settled** (plain homological index `−ζ_{Δ₁}(0)=2g`,
  area-free, #3896); the bare π-power **settled to the 2-D heat-kernel** `1/(4π)`
  (#3909 merged; dilog and (2π)-Gaussian excluded). Jac = **E_{5τ₀}³ × E_{τ₀}**,
  *not* E⁴ (paper-confirmed, 2208.13692). The polarized determinant `det(M)=125`,
  `spec{1,5,5,5}` differs from the naive product **only** through the genus-4
  theta-factor of the integer M-lattice — that is leg (b).
- **My merged front-3 "continuum → state-sum" redirect is FALSIFIED** (the
  S-matrix quantum-dimension never equals `8/8π`); and the `ζ_Λ(0)=−b₁` lead was
  refuted by me (it is −1). The α_EM wall is now **two orthogonal arithmetic
  pieces**, not "one computation for all loop orders."
- **c₃ resummation forks are proved-futile:** fixed-base Jackson q-Borel pruned
  (only Q→1 matches the growth class); the parity-split softened to a single
  common order at k=31 with ρ_odd 95 % off Vol(4₁)/2π (my #3861); Φ_b 2-loop A₁
  = 1/3 + (17√3/108)i is Lean-exact but **≠ κ₁** (mis-identified). More
  fixed-order/anchor-invariant D-ladder resummation is duplication.
- **Binding (not a dashboard miss; m_n/Δ_pn ride on Q_β, not binding):** R11-a
  3-factor closure refuted; **R11-b Farkas certificate (proved-lean)** — the
  missing channel is **non-monotone/resonant in k**; the entire
  *additive-cumulant-of-raw-traces* family is ruled out (raw `tr_M(K)` is itself
  bar-odd ⇒ a **bar-even symmetrized** trace basis must come first).

## Three highest-leverage, non-duplicative next moves

1. **α_EM reciprocal-form / `8π = 2·4π` multiplicity joint (UNOWNED).** With the
   π-power settled to `1/(4π)` and `b₁=8` settled, this is the *last unowned*
   arithmetic piece of the α_EM headline: derive why the measure is `1/b₁`
   (reciprocal) and where the factor-of-2 (`1/(4π) → 1/(8π)`) comes from.
   Formalize-first; the polarized magnitude leg is already on #3911. *(Also close
   the currency gap: cross-link `bring_polarized_jacobian_determinant_probe.py`
   into `docs/coordination/alpha-em.md`.)*
2. **Substrate-first absolute q₀ via Murakami deformed-VC categorical N-selection.**
   The pin map proves this is the **only** route to an anchor-free q₀ < 11.5 ppb —
   the only thing that can close **both** m_p (437×) and m_μ (964×). Formalize-
   first (categorical N-selection, no fit; the winding carrier `|u| ≥ 2π` already
   landed), targets the largest single L2 miss, uncontended. Subgoal-2 is open.
3. **Stand down redundant c₃ resummation; record the measurement-limited ceiling.**
   `SRigidityPrune` proves the c₃ swing is anchor-dependent and experimental-Q_β-
   limited, so more fixed-order/anchor-invariant resummation is proved-futile.
   Route capacity to the *one* open c₃ target (the geometric `Im 𝔙_q → N_odd`
   capstone on the u≠0 leg, #3898), and **record in `precision-goals.md`** that
   Q_β/m_n/Δ_pn (and m_p/m_μ) closure is now gated on a next-gen neutron Q_β
   measurement (σ ≈ 0.024 eV) unless a substrate-q₀ derivation lands. No compute
   sibling is doing this ledger update — it is the single most important
   action-plan change.

## Cross-references

- Superseded reassessment: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)
- New theorems: [`SRigidityPrune.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean), [`2026-07-17-mu-p-pin-sensitivity-map.md`](2026-07-17-mu-p-pin-sensitivity-map.md)
- α_EM: [`2026-07-18-alpha-em-pi-origin-adjudication.md`](2026-07-18-alpha-em-pi-origin-adjudication.md), [`2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md`](2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md), [`docs/coordination/alpha-em.md`](../coordination/alpha-em.md)
- c₃/A_ω: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md), [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) (KC22)
- My parity finding: [`2026-07-17-dladder-odd-singularity-even-order.md`](2026-07-17-dladder-odd-singularity-even-order.md) (PR #3861)
- L1 third method: [`2026-07-18-l1-third-method-cw-seminormal.md`](2026-07-18-l1-third-method-cw-seminormal.md)
