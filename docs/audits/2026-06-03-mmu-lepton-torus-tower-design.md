# m_μ lepton torus-tower — design + feasibility (DESIGN-FIRST)

**Branch:** `claude/mmu-lepton-torus-tower-2026-06-03`
**PR:** #1753
**Date:** 2026-06-03
**Scope:** Design-first scoping of a "lepton torus-tower" to *reduce*
the m_μ prediction error (currently ≈ 209.8 ppb). NOT an implementation
of a fit; NO CAL-4; NO claim that the formal 100× gate is met.

## Governance flag (read first)

m_μ's 100× target is **0.22 ppb**, **below the ~780 ppb CAL-2 floor**.
Per [`docs/precision-goals.md`](../precision-goals.md) §"Two subgoals
(L2 split)", any target below the CAL-2 floor is **Subgoal-2
(research-grade)**, which **requires substrate-derivation of q₀** and was
**explicitly owner-declined on 2026-05-08** (coordination ledger:
*"Q_β derivation? No (explicit) — 780 ppb floor stands"*; q₀
substrate-derivation declined by extension).

**Therefore: passing the formal m_μ 100× gate (0.22 ppb) is OUT OF
SCOPE.** This work targets only the legitimate, in-scope deliverable:
*reducing* the 209.8 ppb prediction error via better lepton-sector
categorical structure — WITHOUT claiming the sub-floor target is met.

A second, subtler governance point falls out of the feasibility
analysis below (§(e)): because the 209.8 ppb residual is **entirely the
q₀ re-pin shift propagated through the `Vol(4_1)/ℏ_q²` lever**, reducing
it past ~210 ppb is *also* Subgoal-2-blocked unless a genuinely new,
**proved** (non-fitted) categorical term enters the muon evaluation.
The two governance flags compound.

---

## (a) Where the m_μ prediction error comes from

**Is m_μ computed by the framework, or just taken as m_e × ratio?**
**It is computed** — there are two conventions, and they must not be
conflated (this is the live dispute on sibling PR #1556):

| Convention | Formula | Residual vs CODATA | Is it a genuine prediction? |
|---|---|---:|---|
| **Bare-categorical** | `m_μ = m_e · Vol(4_1)/ℏ_q²` | **209.8 ppb** (ratio) / 211.16 ppb (mass) | **YES** — q₀ + Vol(4_1) only, no CODATA m_μ input |
| **Ratio-anchored** | `m_μ = m_e × (m_μ/m_e)_CODATA` | ~3.4e-43 ("meets") | **NO** — CODATA m_μ fed back in; trivial round-trip |

The **bare-categorical** value is the genuine prediction (it is the one
`precision-goals.md` line 186 reports as the 963.6× miss, and the one
the `m_p_borromean_verification_50dps.py` `muon_check` section emits as
`muon_check.m_mu_pred_MeV`). The dashboard reader
`per_observable_100x_status.py` (lines 259–264) pulls m_μ from this
Borromean witness.

**Where the 209.8 ppb lives.** Confirmed by the existing 100-dps audit
[`mu_substrate_tension_audit_100dps.py`](../../computations/mu_substrate_tension_audit_100dps.py)
(witness verdict: **H1 SUPPORTED**) and reproduced independently by this
branch's probe:

1. The muon formula is a **single categorical term**, shell order
   **S = 0**: `m_μ = m_e · Vol(4_1)/ℏ_q²`, ℏ_q = 1 − 1/q.
2. q₀ was re-pinned from m_p/m_e on 2026-05-28 (#1422). The new q₀
   differs from the old μ-anchored q₀ by **Δq₀ = −11.61 ppb**.
3. The muon lever `∂ln(m_μ)/∂q = −2/(ℏ_q·q²) = −16.38`, i.e.
   `|∂ln m_μ / ∂ln q| = 18.19`. So the −11.61 ppb q₀ shift is amplified
   ~18× to **211.16 ppb** — matching the observed residual to
   8.7e-6 ppb.

**Conclusion (a):** the residual is **NOT a missing categorical term**
(no "12·m_e"-style correction is absent, unlike the proton). It is the
q₀ re-pin shift mechanically amplified by the figure-eight volume lever.
The substrate is over-determined: a single q₀ cannot simultaneously pin
m_p (to sub-ppb) *and* m_μ (to sub-ppb).

## (b) The categorical object for the muon

Per [`canonical_lepton_braid_words.py`](../../computations/canonical_lepton_braid_words.py)
and [`skein-mass-relation.md`]:

- **Muon = figure-eight 4_1 = (σ₁ σ₂⁻¹)² in H_3** (2 generators).
- 4_1 is **hyperbolic**, with `Vol(4_1) = 2·Cl₂(π/3) = 4·Λ(π/6) ≈
  2.0298832128…` (Clausen function; the older "2·Λ(π/3)" comment in
  several scripts is off by a factor 3 — see the corrected docstring in
  `mu_substrate_tension_audit_100dps.py::vol_4_1_mathlib`).
- The mass enters as `m_μ/m_e = Vol(4_1)/ℏ_q²` — the hyperbolic volume
  is the categorical invariant; ℏ_q² is the substrate normalisation.

There is a **structural tension in the name "torus-tower"**: 4_1 is
*not* a torus knot. The lepton dictionary in
[`lepton-meson-parallel-intro.md`] nominally assigns leptons to T(2,k)
*torus* braids (e = T(2,3) = 3_1 trefoil, τ = T(2,7) = 7_1 septafoil),
but the muon slot is filled by the **hyperbolic** 4_1, not the torus
T(2,5) = 5_1 cinquefoil. This matters because **torus knots have
hyperbolic volume 0** (they are not hyperbolic), so any "torus tower"
built on the Vol invariant degenerates at every torus level (e, τ, and
the T(2,5) muon candidate all give Vol = 0). See §(d).

## (c) Proposed tower structure for e/μ/τ generations

Two candidate towers, distinguished by which categorical invariant
indexes the generation:

**Tower I — hyperbolic-volume tower (current de-facto).**
The muon already uses `Vol/ℏ_q²`. The electron uses `m_e/m_e = 1`
(the anchor), and the tau uses a *separate* knot-volume search
([`m_tau_knot_prediction.py`](../../computations/m_tau_knot_prediction.py),
target m_τ/m_e = 3477.23). This is **not a uniform tower** — only the
muon level uses Vol(4_1); e and τ are handled differently. A genuine
tower would make `m_ℓ/m_e = Vol(K_ℓ)/ℏ_q²^{n_ℓ}` uniform across
generations, which immediately fails because Vol(3_1) = 0 (electron
anchor would predict m_e/m_e = 0, not 1).

**Tower II — generation-degree tower (cohomological).**
[`archimedean-leptons.md`](../../content/quantum-observable-universe/brings-surface/archimedean-leptons.md)
assigns generations by the **degree of the Bring's-surface form**:
deg α_V = 1 → electron, deg α_V = 2 → muon, with χ(𝒮) = −6 bounding
the count to three generations
([`generation-completeness.md`]). Here the tower index is the form
degree, and the knot (3_1 / 4_1 / 7_1) is the *realisation* of each
degree under the genus-≤4 spectral filter, not the mass lever itself.

**What a "torus-tower" would actually be.** The phrase is best read as
**Tower II indexed by torus-bundle level over the Bring's surface** —
i.e. the lepton generations are sections of a tower of torus bundles
(the form-degree filtration), and each generation's *representative*
knot is selected by the genus filter. Under this reading the muon's
4_1 is the genus-1-form representative; the "tower" is the bundle
filtration, not a tower of torus *knots*.

## (d) What a torus-tower would change in the m_μ evaluation

Concretely, three things a tower could change, with the probe's verdict
on each:

1. **Replace 4_1 by a torus knot T(2,5).** Fails the Vol lever:
   Vol(5_1) = 0 (probe §[4]). A torus tower cannot reuse
   `Vol(K)/ℏ_q²` — it would need a **non-Vol** categorical invariant
   (e.g. the Markov trace tr_M of the T(2,5) braid, or a q-quantum
   dimension / Jones-polynomial evaluation), which is a different
   construction entirely and not yet derived.

2. **Add a shell correction `m_μ = m_e·Vol(4_1)/ℏ_q²·(1 + c·u^k)`**
   (Habiro-style, analogous to the proton/Q_β ladder). This is the
   *only* route that could reduce the residual within the current
   knot assignment. But §(a) shows the residual is the **q₀ re-pin
   shift**, not a convergent shell — so any `c` chosen to close it
   would be **fitting the q₀-tension as signal**, exactly the
   antipattern that `precision-goals.md` flags (the μ-p 240 ppb floor
   is "derivable-below, not fittable-below"). **Forbidden.**

3. **Promote the tower index to operator-valued branching** (the
   GAP-A-4 direction). If the generation tower were operator-valued
   (a tower of Wedderburn projectors selecting the muon channel),
   the muon mass would acquire structure beyond the scalar
   `Vol(4_1)/ℏ_q²`. This is the *only* legitimate (non-fit) route and
   is genuinely open R&D — same family as the Δ_λ closure gate.

## (e) HONEST feasibility verdict

**Can the 209.8 ppb be reduced, and to what floor?**

- **The q₀ uncertainty does NOT cancel in m_μ/m_e.** This is the
  decisive structural fact (probe §[2]): m_e is the **external CAL-1
  anchor (CODATA, q₀-independent)**, so the entire q₀ dependence sits
  in `Vol(4_1)/ℏ_q²`. The ratio `m_μ/m_e = Vol(4_1)/ℏ_q²` is a *pure
  function of q₀*; the ratio residual (209.75 ppb) equals the mass
  residual (211.16 ppb) up to CODATA rounding. There is no cancellation
  to exploit — one might have hoped m_μ/m_e evades the q₀ floor, but it
  does not, precisely because m_e carries no compensating q₀ term.

- **The residual is the q₀ re-pin shift (H1).** 211 ppb = −11.61 ppb
  Δq₀ × 18.19 amplification. This is a **substrate over-determination**
  floor: q₀ cannot pin both m_p and m_μ at once. Reducing below it
  requires either (i) a better q₀ (substrate-derivation — **Subgoal-2,
  owner-declined**), or (ii) a new **proved** categorical term in the
  muon evaluation (operator-valued branching, GAP-A-4 — open R&D).

- **What is NOT a path:** a fitted shell correction `c·u^k` tuned to
  close 209.8 ppb (it would model the q₀-tension as signal — forbidden
  by the three-calibration discipline), or a torus-knot swap on the Vol
  lever (Vol = 0 for all torus knots).

**Verdict table:**

| Route | Reduces 209.8 ppb? | Floor reached | In scope? |
|---|---|---|---|
| Fitted `c·u^k` shell | yes (artificially) | any (fit) | **NO** — fits q₀-tension as signal |
| Torus-knot swap on Vol lever | no | n/a (Vol = 0) | n/a — degenerate |
| Better q₀ (substrate derivation) | yes | < CAL-2 floor | **NO** — Subgoal-2, owner-declined |
| Operator-valued branching (GAP-A-4) | **plausibly** | unknown, open R&D | **YES** — only legitimate route |
| Accept 211 ppb as the substrate floor | — | 211 ppb | **YES** — honest current state |

**Bottom line.** The 209.8 ppb is **mostly a hard substrate
over-determination floor**, not a missing-term gap. The *only*
in-scope, discipline-compliant way to reduce it is the GAP-A-4
operator-valued branching tower (the same open R&D that gates the
Δ_λ binding-energy program), which would give the muon mass genuine
categorical structure beyond the scalar `Vol(4_1)/ℏ_q²`. A "lepton
torus-tower" built on hyperbolic volume cannot deliver this (torus
levels are Vol-degenerate); a tower built on **operator-valued
generation branching** (Tower II / GAP-A-4) is the design that could.
Absent that derivation, the honest reporting is: **m_μ bare-categorical
= 211 ppb, q₀-limited, Subgoal-2-blocked below the CAL-2 floor.**

## Discipline labels

- This design doc + the feasibility probe are **EXPLORATORY**
  (audit-only). No production wiring; no dashboard changes.
- The probe contains **NO fit** to CODATA m_μ (the CODATA value appears
  only as a comparison target, never as an input determining a free
  parameter). NO CAL-4.
- Canonical-chain touchpoint: the muon evaluation is Step 10
  (Archimedean functor at q₀). No production compute changed, so no
  `appendix-mass-binding-algorithms/` `alg:`-block sync is required by
  this PR. If a future PR wires an operator-valued muon tower into
  production, that PR must sync the appendix.

## Cross-references

- [`mu_substrate_tension_audit_100dps.py`](../../computations/mu_substrate_tension_audit_100dps.py)
  — prior H1 audit (this design extends it with the ratio-cancellation
  and torus-degeneracy analysis).
- [`mmu_lepton_torus_tower_feasibility_probe.py`](../../computations/mmu_lepton_torus_tower_feasibility_probe.py)
  — this branch's probe + witness.
- [`canonical_lepton_braid_words.py`](../../computations/canonical_lepton_braid_words.py)
  — canonical lepton braid words (e/μ/τ).
- PR #1556 — m_μ convention reconciliation (ratio-anchored vs
  bare-categorical); this design uses the bare-categorical convention.
- [`docs/precision-goals.md`](../precision-goals.md) §"Two subgoals",
  §"Discipline note" (q₀-tension is derivable-below, not fittable-below).
- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
  — GAP-A-4 operator-valued branching (the legitimate reduction route).
