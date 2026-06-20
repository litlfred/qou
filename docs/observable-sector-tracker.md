# QOU observable sector tracker (updated 2026-05-31)

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

> ## ⚠ c_k / d_k saga RESOLVED (2026-05-31) — read before editing precision rows
>
> The recurring "flip-flop" on the Q_β c_k and m_p d_k coefficients is
> **closed with a discipline verdict**: they are **stale-q₀
> near-matches, not derivations.** Two decisive tests settle it:
>
> - **c_k (item 1, `qbeta-delta-tr-vs-formA.witness.json`):** the Habiro
>   Δtr_M is NOT Form A's net-winding slot (leading Taylor orders differ,
>   −5/4 vs −2; substituting it misses CODATA by −240000 ppm). The bridge
>   `Q_β = m_e·f(Δtr_M, q)` is a genuine OPEN derivation.
> - **d_k (item 2, `mp-dk-decisive-test.witness.json`):** d_4 = 46 drifts
>   **100%** between the muon-pin and m_p-pin q₀; at canonical q₀ the bare
>   m_p formula is already 0.0092 ppb, so the "242 ppb gap" the d_k closed
>   was itself a stale-pin artifact.
>
> **Only `c_2 = -1` is Taylor-exact and wired.** All N≥3 c_k / d_k forms
> (J_Hopf, J−ℏ², c_3·b⁴, d_4=46, …) are structural near-matches locked
> behind §3b-cond conditional classes (`QbetaC3StructuralFormClass`,
> `QbetaHabiroTaylorBridgeClass`), NOT production derivations. Earlier
> "6.02 ppb clean Q_β / 5-of-7" claims in this file were stale-q₀
> artifacts and are corrected below. Authoritative ledger:
> `docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md` (read the
> ADDENDUM, not the body).

## L2 100× dashboard (authoritative, from per-observable-100x-status.witness.json @ 2026-05-30T21:01)

| observable | role | pred err | σ_exp (=100×/100) | beats 100×? | beats 1×? |
|------------|------|--------:|------:|:----:|:----:|
| m_e | CAL-1 anchor | 0 ppb | 0.2935 ppb | ✓ | ✓ |
| m_p | CAL-2 anchor | 0.0004 ppb | 0.3091 ppb | ✓ | ✓ |
| m_μ | validation | ~0 ppb | 21.77 ppb | ✓ | ✓ |
| m_K/m_π | validation (meson) | 23.44 ppb | 2.64×10⁴ ppb | ✓ | ✓ |
| Q_β | CAL-3 anchor | **1279 ppb** | 779.7 ppb | ✗ | ✗ |
| m_n | validation | 1.066 ppb | 0.5747 ppb | ✗ | ✗ |
| Δ_pn | validation | 773.9 ppb | 473.9 ppb | ✗ | ✗ |

**Net: 4/7 beat 100×, 4/7 beat 1× experimental** (m_e, m_p, m_μ,
m_K/m_π). Q_β / m_n / Δ_pn miss BOTH — this is the **μ-p substrate
tension floor**, the framework's irreducible self-consistency limit at
the single-substrate level (see `docs/precision-goals.md` Subgoal-2).
Note: m_p is NOT 242 ppb (that was the stale muon-pin); at the canonical
m_p-pin q₀ it is the 0.0004 ppb anchor. Closing Q_β below the floor
requires a genuine Taylor-exact c_3 derivation (the open bridge `f`),
NOT a structural near-match.

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
| **m_p** | CAL-2 numerical anchor; substrate-identity `m_p = m_e · 2Vol/ℏ_q² · F_Bor − 12` | extensive Lean (`m-p-substrate-identity-50dps.witness.json`) | `m_p_substrate_identity_50dps.py` | **0.0004 ppb** (anchor, at canonical m_p-pin q₀) | DERIVED (anchor) |
| **m_n** | Path C: `m_n = m_p + Q_β + m_e` | (composes m_p, Q_β proofs) | dashboard composes | **1.066 ppb** (inherits Q_β floor) — ✗ 100× | DERIVED (composed); limited by Q_β floor |
| **Δ_pn** | derived from m_n − m_p | — | dashboard composes | **773.9 ppb** (inherits Q_β floor) — ✗ 100× | DERIVED; limited by Q_β floor |
| **m_p brane-tower d_k** | claimed d_4 = J²·11+2 = 46, d_5 = 4, d_6 = −29 | — | `proton_brane_tower_correction_probe.py` (witness at stale q₀) | **stale-q₀ artifact** (item 2: d_4 drifts 100% between pins; d_5/d_6 don't match claims) | **NOT a derivation** — see `mp-dk-decisive-test.witness.json` |
| **m_Λ, m_Σ, m_Ξ (other baryons)** | — | — | — | — | OPEN — no canonical chain |
| **m_Δ, m_N* (resonances)** | — | — | — | — | OPEN — these may live in the Demazure sub-crystal layer (AGENTS.md §7b) |

**Baryon gaps:**
- m_p is the CAL-2 anchor (0.0004 ppb, exact by construction at the
  canonical m_p-pin q₀). The old "242 ppb / witness-stale" framing was
  itself the muon-pin artifact — corrected 2026-05-31 (item 2).
- m_n / Δ_pn are derived but limited by the Q_β substrate floor
  (1.066 / 773.9 ppb), not by m_p. Closing them at 100× requires
  closing Q_β (the open bridge), not regenerating m_p.
- The m_p brane-tower d_k are NOT categorical derivations (item 2).
- All hyperons + resonances are open.

---

## V. Q-values / decay observables

| observable | canonical formula | Lean proof | production | residual | status |
|---|---|---|---|---|---|
| **Q_β (free neutron)** | Form A `m_e · |q²−2q−1| · (q+1) / (2q³)` × c_k ladder; **only c_2 = −1 Taylor-exact** | `prop:q-beta-categorical-precision-ladder` (c_2 via Kashiwara N2_factor, PROVED); c_3 §3b-cond conditional `QbetaC3StructuralFormClass` | `per_observable_100x_status.py` wires **Q_N2 only** | **1279 ppb (Q_N2)** — ✗ 100×, ✗ 1× | **DERIVED through c_2 only**; at μ-p floor |
| Q_β c_k (k≥3) | structural forms (J_Hopf, J−ℏ², c_3·b⁴) — **stale-q₀ near-matches, NOT Taylor-exact** | §3b-cond `QbetaC3StructuralFormClass`, `QbetaHabiroTaylorBridgeClass` (conditional, no instance) | NOT wired | item-1: 3.35% off at canonical q₀, q₀-drifting | **NOT derivations** — `qbeta-delta-tr-vs-formA.witness.json` |
| **bridge `f`: Q_β = m_e·f(Δtr_M, q)** | — | — | — | item-1 bounds what it is NOT (not the Form-A slot) | **OPEN** — the genuine derivation target (multi-block Habiro q-difference) |
| **τ_n (neutron lifetime)** | depends on `(ft)`, `g_A`, Q_β | — | — | — | OPEN — only the Q_β leg is wired |
| **τ_μ (muon lifetime)** | depends on G_F, m_μ⁵ | — | — | — | OPEN |
| **Higher-N branching Q-values** | brane-tower structure | partial | — | — | OPEN |

**Q_β gaps (corrected 2026-05-31 after items 1+2):**
- c_3+ wiring: **NOT a derivation** (reversed earlier "CLOSED" claim).
  The c_3 = J_Hopf / J−ℏ² forms are stale-q₀ near-matches (3.35% / 2.6%
  off at canonical q₀); locked behind §3b-cond conditional classes.
- The open derivation step is the bridge `f` with `Q_β = m_e·f(Δtr_M, q)`
  — item 1 showed it is NOT the canonical Form-A-slot substitution; the
  multi-Wedderburn-block Habiro q-difference solution is the research
  target (`docs/audits/2026-05-30-qbeta-habiro-derivation-gap-plan.md`).
- Q_β at the μ-p substrate tension floor (1279 ppb); this is the honest
  production state, not a wiring gap.

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

1. **The Q_β bridge `f`: `Q_β = m_e · f(Δtr_M, q)`** — the genuine open
   derivation. Item 1 (2026-05-31) bounded what it is NOT (not the
   Form-A net-winding slot; Δtr_M's leading Taylor order is −5/4 vs Form
   A's −2). The target is the multi-Wedderburn-block Habiro q-difference
   solution. Closing it (Taylor-exact at canonical q₀, NOT a structural
   near-match) closes Q_β → m_n → Δ_pn at L1. **3 observables**.
   (Supersedes the earlier "Habiro c_4..c_7 closed forms" item — those
   were stale-q₀ near-matches, not the closure path.)
2. ~~m_p brane-tower correction to E_0~~ — **NOT a gap** (item 2): m_p is
   the 0.0004 ppb CAL-2 anchor at canonical q₀; the brane-tower d_k were
   a stale-pin artifact. Removed from the queue.
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
