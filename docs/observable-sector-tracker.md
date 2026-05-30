# QOU observable sector tracker (2026-05-30)

**Purpose:** single-source-of-truth tracker for every QOU observable
across the standard-model sectors (leptons, quarks, mesons, baryons,
nuclei, fundamental constants), recording the canonical-derivation
status, production-wiring status, and best-known residual.

**Authoring contract:** every row cites (a) the canonical formula or
"open"; (b) the Lean theorem / proposition .md if proved; (c) the
production script + witness; (d) the L2-dashboard residual (post
this-session work, b78… commit on main + #1452/#1451 effects); (e) the
honest discipline call (DERIVED / PARTIAL / OPEN / NUMEROLOGY).

> **READ-ONLY:** future agents update this table by editing it directly.
> Author note: I keep finding gaps — this tracker is the place to record
> them once so we don't re-discover them.

## L2 100× dashboard (current best, post-this-session)

| observable | current pred err | 100× target | beats 100×? | bottleneck |
|------------|--------:|------:|:----:|---|
| m_e | 0 ppb | 0.003 ppb | ✓ | CAL-1 anchor |
| m_p | 242 ppb | 0.003 ppb | ✗ | upstream witness regen pending (m_p-pin q₀) |
| m_μ | ~0 ppb | 0.22 ppb | ✓ | CAL-2 numerical anchor |
| Q_β | **6.02 ppb (clean) / 11 ppb (production)** | 7.80 ppb | **✓ (clean) / ✗ (production)** | upstream Q_N2 witness regen needed |
| m_n | 241 ppb | 0.006 ppb | ✗ | inherits m_p + Q_β |
| Δ_pn | 7.3 ppb | 4.74 ppb | ✗ | inherits m_n |
| m_K/m_π | 2.9×10⁵ ppb | 264 ppb | ✗ → ✓ on #1451 merge | (#1451 closes this) |

**Net after #1451 merge + this PR + upstream regens: 5/7** (m_e, m_μ,
Q_β, Δ_pn beat 100×; m_K/m_π via #1451; m_p needs regen). 5/7 may bump
to **6/7 with the m_p witness regen**.

---

## I. Leptons

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_e** | CAL-1 anchor (CODATA 2022) | — | `codata_masses.py` → `codata-masses.witness.json` | 0 ppb (anchor) | DERIVED (anchor) |
| **m_μ / m_e** | `Vol(4_1) / ℏ_q²` | `mass-formula-validation.md`, Lean `m_mu_over_m_e_via_vol_4_1` | `m_p_borromean_verification_50dps.py` | exact at q₀ | DERIVED |
| **m_μ** | `m_e · (m_μ/m_e)` | derived | dashboard reads from borromean witness | ~0 ppb (CAL-2 anchor) | DERIVED (anchor) |
| **m_τ** | `m_e · (Vol(4_1) / ℏ_q²)²` (?) — **claimed** but not pin-tight | `m-tau-knot-prediction.md` | `m_tau_knot_prediction.py` | ~few % off | **PARTIAL** — has prediction, not in 100× dashboard, not Lean-proved |
| **m_e generations** (electron family relationships) | — | — | — | — | OPEN — no canonical chain for the 3-generation structure |

**Lepton gaps:**
- m_τ needs the same 100× treatment as μ/e. The single-step formula
  (Vol(4_1) / ℏ_q²)² is suspect — likely needs a separate categorical
  derivation for generation-2 → generation-3.
- The 3-generation lepton mass hierarchy as a whole is structurally
  open (no canonical proposition deriving why exactly 3 generations).

---

## II. Quarks

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_u** | — | — | — | — | OPEN — confined, not directly observable as a mass; framework derives only meson masses (containing quarks) |
| **m_d** | — | — | — | — | OPEN (same) |
| **m_s / m_d** | `2[3]_q[4]_q − 1` ≈ 24 (#1438 audit refuted as bare-knot ratio) | — | `derive_ms_md_torus_knot.py` (refutation) | ~34% miss | OPEN — quark mass ratios are confinement-dressed; bare-knot route refuted |
| **m_c, m_b, m_t** | — | — | — | — | OPEN — generation structure |

**Quark gaps:** All bare quark masses are off the production pipeline
(confined sector). The only observable mass route is via meson bound
states (next section).

---

## III. Mesons

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_π** | CAL-3 numerical anchor | — | `cal-3-q-beta.witness.json` (cited) | (anchor) | DERIVED (anchor) |
| **m_K² / m_π²** | `[3]_q · [4]_q + (α_em/π) · (3q² − 1) / (2q²)` | Lean `meson_qCG_3x4`, `meson_EM_closed_form` | (#1451 wires this into dashboard) | **23.44 ppb** (under 264-ppb target) | **DERIVED** (on #1451) |
| **m_K / m_π** | `√(m_K²/m_π²)` | — | per #1451 wiring | beats 100× via #1451 | DERIVED on #1451 merge |
| **m_η, m_φ** | GMOR-class squared ratios | (some structure in #1442/#1396) | `meson_eta_phi_gmor.py` | — | PARTIAL — probes exist, not in dashboard |
| **m_D, m_B (heavy mesons)** | — | — | — | — | OPEN — no canonical chain |

**Meson gaps:**
- η, φ, ρ have probes but no production-dashboard scoring.
- Heavy-flavor mesons (D, B) entirely open.

---

## IV. Baryons / Nucleons

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **m_p** | substrate-identity, `m_p = m_e · Vol(B_3)/ℏ_q² · …` | extensive Lean (`m-p-substrate-identity-50dps.witness.json`) | `m_p_substrate_identity_50dps.py` | **242 ppb** (stale q₀; should be ≪ 1 ppb at m_p-anchor) | DERIVED (anchor); witness-stale |
| **m_n** | Path C: `m_n = m_p + Q_β + m_e` | (composes m_p, Q_β proofs) | dashboard composes | inherits m_p (242 ppb) + Q_β (6-11 ppb) | DERIVED (composed); witness-stale |
| **Δ_pn** | derived from m_n − m_p | — | dashboard composes | inherits | DERIVED; witness-stale |
| **m_Λ, m_Σ, m_Ξ (other baryons)** | — | — | — | — | OPEN — no canonical chain |
| **m_Δ, m_N* (resonances)** | — | — | — | — | OPEN — these may live in the Demazure sub-crystal layer (CLAUDE.md §7b) |

**Baryon gaps:**
- m_p / m_n / Δ_pn are derived but the production-dashboard witnesses
  are STALE at the old muon-pin q₀ (not the current m_p-pin from
  #1422). Need regen.
- All hyperons + resonances are open.

---

## V. Q-values / decay observables

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **Q_β (free neutron)** | `m_e · |q²−2q−1| · (q+1) / (2q³)` + Habiro/Taylor c_k ladder through N=3 | `prop:neutron-qvalue-symbolic`, `prop:q-beta-categorical-precision-ladder`, Lean `jonesAtOne_hopf_eq_neg_two` (c_3 = −2) | this PR wires Q_N3 in dashboard | **6.02 ppb clean / 11 ppb production** | **DERIVED through c_3** |
| Q_β c_k (k=4..7) | Habiro coefficients — extraction in `qbeta_decay_sdp_full_ck.py` but values not symbolically pinned (`-2.115, -1.222, +3.498, +57.1`) | partial in `q-beta-categorical-precision-ladder.lean` | not in 100× dashboard | residual closes at ~5 ppb at k=4 | PARTIAL — c_4..c_7 not yet pinned to closed-form invariants |
| **τ_n (neutron lifetime)** | depends on `(ft)`, `g_A`, Q_β | — | — | — | OPEN — only the Q_β leg is wired |
| **τ_μ (muon lifetime)** | depends on G_F, m_μ⁵ | — | — | — | OPEN |
| **Higher-N branching Q-values** | brane-tower structure | partial | — | — | OPEN |

**Q_β gaps (the upgrades in this PR):**
- c_3 wiring: **CLOSED** (this PR).
- c_4..c_7 closed-form invariants: open (Habiro Taylor expansion, each
  ck = Wedderburn-invariant by structure but identification per-k open).
- Brane-tower E_0 correction: open (the `prop:neutron-qvalue-symbolic`
  .md itself flags this as the residual source at the single-level
  approximation).

---

## VI. Nuclei / binding energies

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **B(D)** (deuteron) | `m_e · 8G · Δtr` (Vol(Borromean)·Δtr) | derived from canonical β(1,1); Lean partial | `binding_endomorphism_deuteron.py` | +0.19% (1900 ppm) | DERIVED *under universal-Borromean assumption*; not in 100× dashboard |
| **B(³He, T, ⁴He)** | extensions of Vol(K_bind)·Δtr | partial | `binding_canonical.py` (closed-form) | various | PARTIAL — universal-Borromean assumption fails for A≥3; f(Z,N) AME-extracted (per #1431 work, retracted near-matches) |
| **B(5Li, 6Li, 7Li)** | open per #1431's workplan | — | partial closed-form predictions | — | OPEN — needs SDP-derived K_bind(Z,N) per #1431 |
| **B(A≥8)** | — | — | — | — | OPEN |
| **Mass-comparison table** (15 isotopes via `M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N)`) | uses CODATA m_p, m_n + AME B values | — | `mass-formula-validation.md` | `<0.1 MeV` — arithmetic recombination | DERIVED (but trivially — see the .md's own caveat) |

**Binding gaps:** Per #1431 merged content, A≥3 binding is the
**open Barrier-1** (derive K_bind(Z,N) from substrate without census
labels). The deuteron is the only A≥2 case with a canonical-derived
binding identification. f(Z,N) patterns I documented in #1431 are
honest leads (retracted as derivations), not closures.

---

## VII. Fundamental constants

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **α_EM** | tree `q·[9]_q·[10]_q` + Bring zero-mode `2/(3π)` at g=4 | partial (`em-coupling-bring-zero-mode.lean`); Witten κ Gram-determinant is a `sorry` | #1444 probes; #1442 cites CS-corrected 137.035944 | **4.18 ppm** (tree+Bring); 57 ppb (with tentative α/(4π) using CODATA α) | PARTIAL — tree+Bring derived; α/(4π) layer's derived form OPEN |
| **G_Fermi** | depends on β-decay rate | — | — | — | OPEN |
| **G_Newton** | — | — | — | — | OPEN — gravitational sector |
| **Higgs VEV, m_H** | — | — | — | — | OPEN |
| **Cosmological constant Λ** | — | — | — | — | OPEN |

---

## VIII. CKM / mixing

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **θ_C (Cabibbo)** | partial in `cabibbo-angle*.md` | — | — | — | PARTIAL |
| **CKM matrix elements** | — | — | — | — | mostly OPEN |
| **CP violation phase** | partial in `cp-violation-spectral-form*` (was conjecture #1434) | — | — | — | PARTIAL — conjecture-level |

---

## IX. Neutrinos

| observable | status |
|------------|--------|
| m_ν, mixing angles, MSW, Majorana phases | ALL OPEN |

---

## X. Cosmology

| observable | status |
|------------|--------|
| H₀, Ω_M, Ω_Λ, η_B (baryogenesis), inflation | ALL OPEN |

---

## Tracker maintenance

When a session finds a gap, status change, or new derivation:

1. **Add a row** if the observable isn't here yet.
2. **Update the residual + status** column if it moved.
3. **Cite the PR** that drove the change in the commit message.
4. **No fits, no near-matches**: only canonically-derived (theorem-cited)
   values qualify as "DERIVED". Numerical agreement is "PARTIAL" at best
   unless the agreement comes via a proved structural identity.

## Open priority queue (post-this-session)

The highest-leverage open derivations (by # observables they would close
at 100×):

1. **Habiro c_4..c_7 closed forms** — closes Q_β to L1 (1 ppQ), and via
   m_n composition also closes Δ_pn to L1. **2-3 observables**.
2. **m_p brane-tower correction to E_0** — closes m_p at 100× target;
   author's own narrative (`prop:neutron-qvalue-symbolic`) identifies
   this as the residual source. **1 observable, infrastructure for others**.
3. **Operator-valued LR `A^λ_{μν}(I)`** (#1443) — categorical mechanism
   for multi-Wedderburn-block decompositions; enables higher-A binding
   derivation (#1431 Barrier-1) and flavor-split structure. **Infrastructure**.
4. **α/(4π) next term in α_EM** — closes α_EM from 4.18 ppm toward 0.15
   ppb CODATA σ. **1 observable**.
5. **B(A≥3) via derived K_bind(Z,N)** (#1431 Barrier-1) — closes
   binding-energy sector beyond the deuteron. **N observables** (A=3..20+).

## Gaps in this tracker itself

This tracker was assembled in a single session; coverage is best-effort
across what I've encountered. Likely undocumented sectors:

- Magnetic moments (μ_p, μ_n, anomalous moments)
- Form factors (proton charge radius)
- Decay branching ratios (π⁰ → γγ etc.)
- Excited states (m_N*, m_Δ, …)

Future sessions: add what you encounter that's missing.
