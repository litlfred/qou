# Lepton T(2,n) torus tower: group-action map (exploratory)

**Date:** 2026-06-02
**Branch:** `claude/lepton-t2n-torus-tower-2026-06-02` (PR #1682)
**Scope:** Author 2026-06-02 — map the group actions on the **lepton
2-strand `T(2,n)` torus-knot tower** (electron=`T(2,3)`, muon=`T(2,5)`,
tau=`T(2,7)`, `T(2,9)` saturation) that the merged census
([`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md),
PR #1677) identified as the lepton sector. Tabulate the tower group
structure; verify the `S₅`-equivariance selection `n∈{3,5}`; compare the
mass ratios RAW (falsification only); assess the `U(1)`-framing ladder.
**Compute:**
[`lepton_t2n_torus_tower.py`](../../computations/lepton_t2n_torus_tower.py),
witness
[`lepton-t2n-torus-tower.witness.json`](../../computations/lepton-t2n-torus-tower.witness.json)
(audit-only, RAW @ 60 dps + symbolic-in-q, 21 assertions pass). **No
tuning to any lepton mass ratio, electric charge, hypercharge, spin, or
any h^k.** The `H₂(q)` Wenzl Markov-trace machinery is reused verbatim
from the inter-nucleon linked-channel audit
([`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md),
PR #1678).

---

## VERDICT (one line)

**The lepton `T(2,n)` tower is a clean, fully RAW group-action ladder: a
single-generator `B₂ = ℤ → H₂(q) → S₂` chain whose `σ₁ⁿ` powers give
writhe `=n`, genus `=(n−1)/2`, and an intrinsic cyclic `ℤ_n`, with every
lepton odd-`n` (knot, fermion) by `gcd(2,n)=1`. The `S₅`-equivariance
selection `n∈{3,5}` (electron + muon) is a verified GROUP-THEORETIC FACT
— `S₅` has element orders `{1,2,3,4,5,6}`, and the odd-`n≥3` subset is
exactly `{3,5}`; tau (`n=7`) embeds topologically (genus 3 ≤ 4) but its
`ℤ₇` has no order-7 element in `S₅`, so the framework predicts a `2+1`
generation split (symmetry-preserving e,μ + symmetry-broken τ) which is a
genuine structural distinction, not a fit. The mass ratios fail RAW
honestly: the direct operator-level `|tr_M|` ratio gives m_μ/m_e off by
**152×** and m_τ/m_e off by **1954×** — confirming NO covert fit, and
that the production lepton-mass map is the calibrated Skein/Kashaev
`Vol(4₁)/ℏ_q²` identity (a `q→1` LIMIT, CAL-2-anchored), NOT this
operator ratio. The `U(1)`-framing ladder `q^{n·c}` is monotone in `n` (a
genuine ladder) but the lepton electric charge is CONSTANT (−1) across
generations — a category mismatch, so writhe does NOT encode electric
charge; the ladder instead tracks the generation index = the cyclic
symmetry `ℤ_n`. The single most promising DERIVED lead is the
`S₅`-equivariance `2+1` split, the only entry that is a theorem rather
than a near-match.**

---

## 1. The tower group-action table (RAW)

For each `T(2,n) = σ₁ⁿ` in `H₂(q)` (all values RAW; trace @ q₀ = 60 dps,
`q₀ = 1.10997858275…` the canonical proton-pinned 4₁-volume-derived
anchor, imported from `q_parameter.Q_MP`):

| `n` | Particle | `tr_M(σ₁ⁿ)(q₀)` `=J_{T(2,n)}(q₀)` | writhe `w` | genus `g` | cyclic | `B_n→H_n→S_n` | components `gcd(2,n)` | statistics |
|---|---|---:|---:|---:|---|---|---:|---|
| 3 | electron | 0.730204 | +3 | 1 | `ℤ₃` | `ℤ → H₂ → ℤ₂` | 1 (knot) | fermion |
| 5 | muon | 0.993002 | +5 | 2 | `ℤ₅` | `ℤ → H₂ → ℤ₂` | 1 (knot) | fermion |
| 7 | tau | 1.299201 | +7 | 3 | `ℤ₇` | `ℤ → H₂ → ℤ₂` | 1 (knot) | fermion |
| 9 | (ghost) | 1.662182 | +9 | 4 | `ℤ₉` | `ℤ → H₂ → ℤ₂` | 1 (knot) | fermion |
| 11 | (ghost) | 2.097812 | +11 | 5 | `ℤ₁₁` | `ℤ → H₂ → ℤ₂` | 1 (knot) | fermion |

Note `|tr_M(σ₁³)| = 0.7302` matches the conv-A trefoil value in
[`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md)
(Phase-3 table, `0.7302 conv A`) — the Wenzl trace reproduces the
corpus value exactly.

**The group structure, RAW (derived, not chosen):**

- **Braid group `B₂ = ℤ`.** Single generator `σ₁`; the tower is the
  power map `n ↦ σ₁ⁿ`. The braid relation is vacuous (only one
  generator) — the whole tower lives inside the abelian `ℤ`.
- **Hecke quotient `H₂(q)`.** Two 1-dim Wedderburn blocks `(2)`
  [`σ₁ ↦ q`] and `(1,1)` [`σ₁ ↦ −q⁻¹`]. The Markov trace decomposes as
  `tr_M(σ₁ⁿ) = W_(2) qⁿ + W_(1,1)(−q⁻¹)ⁿ` with the Wenzl weights fixed
  by the two Markov axioms (`tr_M(1)=1`, `tr_M(β·σ)=z·tr_M(β)`,
  `z = 1/(q^{1/2}+q^{-1/2})`). Both blocks carry weight at every `n`.
- **Symmetric quotient `S₂ = ℤ₂`.** The sign quotient `H₂ → ℤ₂` IS the
  fermion/boson statistics axis: `gcd(2,n)` components, odd `n` = knot =
  fermion, even `n` = 2-component link = boson
  ([`fermion-boson-knot-link.md`](../../content/quantum-observable-universe/particle-interactions/fermion-boson-knot-link.md)).
  **Every charged lepton is odd `n` ⇒ knot ⇒ fermion** — the tower is
  entirely fermionic, as required.
- **Cyclic knot-type symmetry `ℤ_n`.** Each `T(2,n)` carries an intrinsic
  `ℤ_n` rotation (the torus-knot rotational symmetry). This is the
  continuous-symmetry entry that feeds the `S₅` fiber group (§2).
- **Writhe `w = n`, genus `g = (n−1)/2`.** Both derived RAW from the
  all-positive braid word `σ₁ⁿ` (`n` positive crossings ⇒ writhe `n`;
  Seifert genus of `T(2,n)` is `(n−1)/2`).

**Closed-form trace and cross-checks (RAW):**

- **Symbolic in q.** `tr_M(σ₁³)` and `tr_M(σ₁⁵)` computed symbolically
  (sympy) from the Wenzl weights; the `T(2,3)` symbolic value evaluated
  at q₀ matches the mpmath value to 1e-45 (asserted
  `trM_T2_3_symbolic_eq_numeric`).
- **Census Hopf cross-check.** The Wenzl `tr_M(σ₁²)(q₀) = 1.1043880583…`
  matches the census's Hopf closed form `1 + (q−1)/√q` to **1e-50**
  (asserted `trM_hopf_wenzl_eq_census`). This validates the Wenzl trace
  against the merged census's independent Hopf computation — the same
  exact agreement the linked-channel audit found.

---

## 2. The `S₅`-equivariance selection `n∈{3,5}` (VERIFIED group-theoretically)

The census claims `T(2,n)` is `S₅`-equivariantly embeddable into Bring's
surface (`Aut(Σ₄) = S₅`) iff `ℤ_n ↪ S₅`, i.e. iff `S₅` has an order-`n`
element. Verified RAW:

- **Element orders of `S₅`.** Computed as the lcm of the parts over every
  partition of 5: `{1,2,3,4,5,6}` (asserted `S5_orders_eq_1_to_6`). The
  order-6 element is the `(2,3)` cycle type `lcm(2,3)=6`; there is **no**
  order-7, order-9, or order-11 element.
- **Odd `n≥3` admissible subset.** `{n ∈ {3,5,7,9,11} : n ∈ orders(S₅)}
  = {3,5}` (asserted `S5_equivariant_selection_eq_3_5`). Exactly the
  electron (`ℤ₃`, a 3-cycle) and the muon (`ℤ₅`, a 5-cycle).
- **Tau (`n=7`) is NOT `S₅`-equivariant** (asserted
  `tau_n7_not_S5_equivariant`): no order-7 element exists in `S₅`. But
  `genus(T(2,7)) = 3 ≤ 4`, so tau DOES embed topologically (Seifert-genus
  filter). The two criteria diverge precisely here.

**Is this a structural distinction the framework predicts? — YES.**

This reproduces
[`prop:s5-equivariant-torus-knots`](../../content/quantum-observable-universe/observations/s5-equivariant-torus-knots.md)
and its interpretation
[`rem:symmetry-preserving-leptons`](../../content/quantum-observable-universe/observations/symmetry-preserving-leptons.md):
the three-generation structure is **`2 + 1`, not `3 + 0`** — the electron
and muon are *symmetry-preserving* (their cyclic `ℤ_n` is realised by a
genuine `S₅` element), while the tau is *symmetry-broken* (it carries its
mass via a Seifert surface, not a new `S₅`-compatible cyclic structure).
The corpus is explicit that this is the framework's prediction; the three
observed generations match the *topological* (genus) criterion, and the
equivariant criterion *sharpens* — it does not contradict — the
three-generation count. **This is a theorem (group-theoretic fact), not a
fit; it is the cleanest entry in this audit.**

---

## 3. Mass-ratio RAW comparison (falsification references — fit-flagged)

The framework's PRODUCTION lepton-mass map is **NOT** the direct
operator-level trace ratio. It is the Skein/Kashaev-volume identity
([`skein-mass-relation.md`](../../content/quantum-observable-universe/observations/skein-mass-relation.md),
[`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md)):

```
m_μ/m_e  =(LO)=  Vol(4₁)/ℏ_q²   ≈ 206.7683  (matches CODATA — CALIBRATED via CAL-2)
```

This uses the **hyperbolic volume `Vol(4₁) ≈ 2.0299`** (the Kashaev
`q→1` LIMIT of `|tr_M(4₁)|`) divided by the substrate density `1/ℏ_q²`.
It is a **limit identity calibrated to CODATA**, not a q₀ operator ratio.
This audit does NOT reproduce or wire that path; it reports the RAW direct
operator ratio so the gap is visible:

| Ratio | Direct `|tr_M(T(2,n))| / |tr_M(T(2,3))|` (q₀, RAW) | CODATA | Miss factor | Fit flag |
|---|---:|---:|---:|---|
| m_μ/m_e (`T(2,5)`/`T(2,3)`) | 1.359897 | 206.7683 | **152.0×** | NONE |
| m_τ/m_e (`T(2,7)`/`T(2,3)`) | 1.779230 | 3477.23 | **1954.3×** | NONE |

- **The direct operator ratio misses CODATA by ~10²–10³×** (asserted
  `direct_mu_e_ratio_misses_codata_by_gt_100x`). This is consistent with
  the corpus Phase-3 finding (the figure-eight muon ID gives 0.27, a
  ~750× miss; the `T(2,5)` muon candidate used here gives 1.36, a 152×
  miss) — both are RAW, both fail, and the failure CONFIRMS there is no
  covert fit in the direct-trace path.
- **Fit-flag: NONE.** No coupling is tuned. A coupling chosen to close
  the 152×/1954× gap would be exactly the fit the discipline review
  catches. The honest RAW miss is reported as the falsification result.
- **Latent-fit check on the production path.** The Skein identity DOES
  match CODATA — but only because `ℏ_q²` is itself **fixed by CAL-2**
  (`ℏ_q² = Vol(4₁)/(m_μ/m_e)_CODATA`), i.e. the muon ratio is the
  *calibration input*, not a prediction. The OPEN piece is whether the
  same formal `ξ_ℓ(q)` predicts m_τ/m_e = 3477.23 without re-calibration
  ([`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md)
  property 4, "OPEN"). That is the genuine derivation target, and it is
  unresolved — flagged, not closed here.

---

## 4. Where the `U(1)` sits — the framing ladder `q^{n·c}` (assessed RAW)

`writhe(T(2,n)) = n ≠ 0` for every lepton ⇒ a **live** Reidemeister-I
framing factor `q^{n·c}` throughout the tower (unlike the writhe-0
Borromean baryon). At the observable level `Im(q₀)=0` (AGENTS.md), so
`q^{n·c}` is a real factor. With `c=1` SET (not fitted):

| `n` | Particle | writhe | `q^{n}` (q₀, c=1) | electric charge |
|---|---|---:|---:|---:|
| 3 | electron | +3 | 1.368 | −1 |
| 5 | muon | +5 | 1.685 | −1 |
| 7 | tau | +7 | 2.076 | −1 |
| 9 | (ghost) | +9 | 2.558 | −1 |

**Verdict: the framing factor is a genuine LADDER (monotone in `n`), but
it is NOT electric charge — it tracks the GENERATION index.**

- `q^{n·c}` is **strictly increasing** in `n` (3,5,7,9), so it is a
  per-lepton ladder, not a constant.
- The lepton **electric charge is CONSTANT (−1)** across all three
  generations. A monotone ladder cannot reproduce a constant ⇒ **category
  mismatch**: writhe does NOT encode electric charge.
- What the ladder DOES track is the **generation number** (`n = 2k+1` for
  generation `k`), i.e. the cyclic-symmetry index `ℤ_n` — a topological
  generation label, NOT a gauge charge.
- **`writhe → Y` (hypercharge) remains UNDEFINED**, consistent with the
  inter-nucleon linked-channel audit (which found the pp/nn framing
  difference misses the PDG mass split by ~305× at `c=1`). No coupling
  `c` is tuned here; `c=1` is set as the natural per-crossing value.

This is the writhe-nonzero counterpart to the census's writhe-0 Borromean
baryon: the lepton tower is exactly where the framing `U(1)` is *live*,
but "live framing" ≠ "gauge charge". The 2-strand `U(1)` that the
linked-channel audit identified is the same object; this audit shows that
on the lepton tower it indexes generation, not charge.

> **Coordination.** A sibling probe
> `claude/u1-hypercharge-assignment-2026-06-02` was named at task-open as
> the parallel `U(1)`-hypercharge derivation (it was not yet visible on
> remote when this branch opened). This audit deliberately does NOT
> attempt a `writhe → Y` map — that is the sibling's scope. The finding
> here (framing ladder = generation index, NOT charge) is the
> lepton-tower-specific complement: if the sibling derives a `U(1)`
> hypercharge, it must reconcile with the fact that on the lepton tower
> the framing tracks generation while electric charge is constant.

---

## 5. Most promising DERIVED lead for follow-up

**Lead: the `S₅`-equivariance `2+1` generation split — the only entry in
this audit that is a theorem, not a near-match.**

Every numerical entry (mass ratios, framing factors) is a RAW
falsification reference that *fails* by design (no fit). The one entry
that is a clean derived result is the group-theoretic selection
`{3,5} = odd n≥3 with ℤ_n ↪ S₅`. The productive follow-up is to ask
**what the symmetry-broken tau's Seifert-surface mechanism predicts that
the symmetry-preserving e,μ do not** — i.e. whether the `2+1` split
leaves a *derivable* signature (e.g. in the tau's mass-tower correction
relative to e,μ, or in a CP/chirality property tied to the broken `ℤ₇`).
This is a derivation task (compare the `S₅`-equivariant `T(2,3)/T(2,5)`
fiber decoration to the non-equivariant `T(2,7)`), NOT a fit. It is the
natural next deep-dive because it is anchored to a theorem rather than a
near-match, and it does not require the still-OPEN `ξ_ℓ(q)` dimensional
factor to make progress.

A secondary (lower-priority) lead: the OPEN `ξ_ℓ(q)` in
[`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md)
property 4 — whether one formal `ξ_ℓ` predicts m_τ/m_e without
re-calibration. This is the genuine mass-derivation target, but it is a
known multi-session open item, not newly surfaced here.

---

## What this audit does and does not claim

- **Does** tabulate the lepton `T(2,n)` tower group structure (trace,
  writhe=n, genus=(n−1)/2, `ℤ_n`, `B₂=ℤ→H₂→ℤ₂` statistics) RAW @ 60 dps
  + symbolic-in-q, with the Wenzl trace cross-checked against the census
  Hopf closed form to 1e-50.
- **Does** verify the `S₅`-equivariance selection `n∈{3,5}`
  group-theoretically (S₅ element orders `{1,2,3,4,5,6}`; tau n=7 not
  equivariant) and confirm the framework's `2+1` generation-split
  prediction.
- **Does** report the direct operator-level mass ratios RAW (152×
  muon, 1954× tau miss) with the fit-flag NONE, and identify the
  production path as the CAL-2-calibrated Skein/Kashaev `Vol(4₁)/ℏ_q²`
  LIMIT identity (not the operator ratio).
- **Does** assess the `U(1)`-framing ladder: monotone in `n` (generation
  index = cyclic `ℤ_n`), NOT electric charge (constant −1); `writhe → Y`
  undefined.
- **Does NOT** propose, fit, or tune any coupling, normalization,
  hypercharge, or h^k. Lepton mass ratios and electric charge are
  falsification references only.
- **Does NOT** wire to production, advance L2 numerically, or discharge
  any Lean `sorry`. No LP/SDP solve appears (no dual emission required).

## Cross-references

- The census (this audit's starting point):
  [`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md)
  (PR #1677).
- The H₂(q) Wenzl trace machinery (reused) + the 2-strand U(1):
  [`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md)
  (PR #1678).
- `S₅`-equivariant torus knots (`ℤ_n ↪ S₅`):
  [`s5-equivariant-torus-knots.md`](../../content/quantum-observable-universe/observations/s5-equivariant-torus-knots.md),
  [`symmetry-preserving-leptons.md`](../../content/quantum-observable-universe/observations/symmetry-preserving-leptons.md).
- Fermion/boson = knot/link, `gcd(2,n)`:
  [`fermion-boson-knot-link.md`](../../content/quantum-observable-universe/particle-interactions/fermion-boson-knot-link.md).
- Lepton–meson torus-knot dictionary:
  [`lepton-meson-torus-knot-dictionary.md`](../../content/quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md).
- Production lepton-mass map (Skein/Kashaev limit + OPEN ξ_ℓ):
  [`skein-mass-relation.md`](../../content/quantum-observable-universe/observations/skein-mass-relation.md),
  [`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md).
- Existing lepton braid-word compute (per-braid mass tower, crude V̂):
  [`canonical_lepton_braid_words.py`](../../computations/canonical_lepton_braid_words.py).
- The s5-so3 fiber audit (U(1)=writhe, spin=ribbon-twist):
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md).
