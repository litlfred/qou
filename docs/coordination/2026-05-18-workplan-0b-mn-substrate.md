# Coordination ledger — workplan-0b/M_N substrate derivation

**Goal:** Upgrade the nucleon mass anchor `M_N` from CLASS-A acknowledged stub to a substrate-derived quantity by reconciling the three candidate routes (A: C2 inflection, B: operator-valued Frobenius, C: Bring Euler-class) with PR #690's C2 inflection mechanism.

**Owner branch:** `claude/workplan-0b-mn-substrate` (PR [#751](https://github.com/litlfred/qou/pull/751))

**Date opened:** 2026-05-18

**Predecessor ledger:** [`2026-05-18-lambda-scale-falsification.md`](./2026-05-18-lambda-scale-falsification.md) — PR #701 falsification of `λ_scale = 5/2 − h²·G` as a natural Wedderburn-block sum.

## Scope map

| PR | Status | Classification | Relationship |
|----|--------|----------------|--------------|
| [#751](https://github.com/litlfred/qou/pull/751) | open | **own** | Routes A/B/C concrete + cross-PR finding (PR #690 C2 inflection implicitly computes `5/2 − h²·G`) |
| [#690](https://github.com/litlfred/qou/pull/690) | merged | predecessor | Substrate-pure m_p via C2 inflection (`d²A/da² = 0` on categorical action A(a)) |
| [#701](https://github.com/litlfred/qou/pull/701) | merged | predecessor | Family A theorem `(1/4) Σ_λ dim_q V_λ = 5/2 + (3/4)h²` + 5-route falsification |
| [#735](https://github.com/litlfred/qou/pull/735) | merged | predecessor | Workplan-0b spec |
| [#772](https://github.com/litlfred/qou/pull/772) | open | **overlap (constructive)** | Audit doc: clarifies that `ρ_K · m_e` (per-atom categorical density × m_e) is distinct from substrate Planck-tick `E_0^(N=0)`; the 210× ratio between them is structural, not a missing normalization |
| [#761](https://github.com/litlfred/qou/pull/761) | open | dependency-check | Hoefsmit/GP combined stack; #751 Route B probe consumes the Python symbolic-q `hoefsmit_matrices_symbolic(shape, Q)` entry — needs API stability |
| [#736](https://github.com/litlfred/qou/pull/736) | open | text-conflict | Both PRs edit `folio/schema/references.ts`; #751 adds 1 entry (`lang2002algebra`), #736 adds 29. Additive, semantically clean |
| [#776](https://github.com/litlfred/qou/pull/776) | open | tangent | Demonstrates canonical pattern for co-located `.lean` → Lake-tree migration; #751's new block uses the co-located pattern with `validation: "stub"`; eventual Lake-tree lift can be a separate follow-up |
| [#763](https://github.com/litlfred/qou/pull/763) | merged | parallel | Bucket D sample: substrate-derived E_0 for proton/neutron predictions. No file conflict; same workplan-0b scope |
| [#758](https://github.com/litlfred/qou/pull/758) | merged | parallel | Bucket B batch 2: scripts migrated off direct M_P/M_N symbols. My probes already use the `experimental_constants` registry |

## Findings

### PR #751 headline (this branch)

**The required multiplicative factor for `M_N = m_e · Vol(B_3)/ℏ_q² · X` is `X = 2.4616`** at q_0. Equivalently, `Vol(K_p) = X · Vol(B_3) ≈ 18.04`.

| Form | Value at q_0 | Δ vs required |
|------|---------------|---------------|
| `5/2 − h²·G` (PR #701 empirical, falsified-as-derivation) | 2.4599666 | **−0.068 %** |
| PR #690 C2 inflection output `A(a_C2)` | 2.4615 | 0.000 % (target by construction) |
| Family A `5/2 + (3/4)h²` (PROVED on PR #701) | 2.5328 | +2.9 % |
| `[2]_q · 5/4` | 2.5136 | +2.1 % |

The 0.068 % agreement between `5/2 − h²·G` and `A(a_C2)` (PR #690's inflection-criterion output) is the structural fact this branch's three routes attempt to derive.

**Route-by-route status:**
- **Route A** (C2 inflection structural): `a_post_hoc = (4−q)/(4q+3)` is rational in q (not Laurent in `q^{±1/2}`); fails `prop:three-calibration-inputs` canonical form. **Open structural question:** why does `d²A/da² = 0` produce `5/2 − h²·G`? Candidates: entropy extremum / Picard-Lefschetz saddle / Yang-Baxter critical point.
- **Route B** (operator-valued Frobenius at H_4): scalar invariants of `ρ_λ(β_Bor_stab)` all miss `M_N` by ±50-120 %. Requires non-scalar invariant — matches PR #690's inflection-on-operator-valued framework.
- **Route C** (Bring Euler-class adaptation): `Vol(K_p) ≈ 18.04` admits no clean additive secondary-class match. Multiplicative form reduces to Route A.

**New content block on this branch:** `prop:sw-3root-rational-integrand` — the Schur-Weyl 3-root product is the exact rational function `−P(z)/D(z)` with `D = res_c(F, F_c) = −disc_c(F)` palindromic. Gives a closed-form algebraic foundation for `A(a)` integration via partial fractions.

### PR #772 (sibling)

What gets called `E_0` in some Bucket-D round-2 scripts is structurally `ρ_K · m_e`, NOT the substrate Planck-tick `E_0^(N=0) = m_e/(q_0·(q_0−1)) ≈ 4.186 MeV`. The 210× gap between `m_p / |tr_M(p)|` ≈ 880.8 MeV and `E_0^(N=0)` is by-design, not a missing normalization. Bucket-D rewires should use `predict_mass(Z, N, |tr_M|)` with `ρ_K` surfaced explicitly.

**Reading the two PRs together:** my factor `X ≈ 2.46` is the proton-specific `Vol(K_p) / Vol(B_3)`, parallel to `ρ_K^{LO}(1, 0)` structure. The C2-inflection criterion in Route A is a candidate categorical mechanism that produces `ρ_K^{LO}` for the proton via `M_N = Vol(B_3)/ℏ_q² · X · m_e = (Vol(B_3)/ℏ_q²) · (ρ_K^{LO}/m_e term).`

## Posted coordination comments

| Sibling | Comment | Topic |
|---------|---------|-------|
| [#772](https://github.com/litlfred/qou/pull/772#issuecomment-4482103701) | posted | Unify naming for the `2.46` factor; reference #772 framing in #751 audit doc once #772 lands |
| [#761](https://github.com/litlfred/qou/pull/761#issuecomment-4482105926) | posted | Cross-dependency check on Python `hoefsmit_matrices_symbolic(shape, Q)` signature + Hecke convention |
| [#736](https://github.com/litlfred/qou/pull/736#issuecomment-4482107917) | posted | `references.ts` text conflict (additive, clean). `lang2002algebra` not duplicated against #736's 22 paper entries |
| [#776](https://github.com/litlfred/qou/pull/776#issuecomment-4482109089) | posted | Defer Lake-tree migration of `sw-3root-rational-integrand.lean` to a follow-up (don't expand #751 scope mid-review) |

## Escalations

None at this time. No inconsistent findings across siblings — PR #772's `ρ_K vs E_0` framing is constructive context for #751's `X ≈ 2.46`; PR #690's C2-inflection output is consistent with the empirical `5/2 − h²·G`.

## Next concrete task (non-overlapping)

**Wait for review-round resolution on #751 before further work on this branch.** The two existing Copilot review batches (commits `8197914d` and `76d8f432`) are addressed in `fa01be4f` + `79cefddd`. Next CI cycle / sibling event will surface any follow-up.

If the user wants substantive progress on the open structural question in Route A ("why does inflection point of A(a) produce `5/2 − h²·G`?") that work belongs on a **fresh** branch — not in this PR — since #751's scope is "routes concrete + cross-PR finding", not "derive the inflection-point semantics".

---

## 2026-05-22 update — post-merge audit + #879 coordination

PR #751 was merged. A critical re-analysis on the merged tip
(`docs/audits/2026-05-22-pr751-critical-reanalysis.md`,
commit `42deac024` on `claude/workplan-0b-mn-substrate`)
triple-checked the merged work for CAL-4 leakage. Findings:

**One solid positive:** `prop:sw-3root-rational-integrand` is
correct — `integrand_baryon = -P(z)/D(z)` via Vieta-resultant,
machine-precision verified.

**One sneak CAL-4 (curve-fit face):** `(4-q)/(4q+3)` as
integration limit produces `A(a(q)) ≈ CODATA m_p` at q_0, but the
color-tube cubic `F(z,c)` has coefficients in z only (no q
anywhere). So A(a) is q-independent and the q-dependence enters
exclusively through the integration-limit choice — exactly what
fitting a curve through CODATA m_p over the q-range looks like.

**Main has partly fixed this (2026-05-18):**
- `f86ea9d7a` demotes `def:picard-lefschetz-thimble → rem:`
- `3a4a85f48` / `c5e3894fa` / `7dba7772b` reframe
  `prop:sw-period-thimble-equivalence` as algebraic residue on
  the principal Galois orbit over `ℤ[q^{±1/2}, ζ_5]`
- New `mobius-limit-from-thimble.md` explicitly states PL is
  "not numerically supported" (witness shows descent crossing
  at z ≈ 3.86, 10× larger than `a(q_0)`)
- Witness `derive-a-thimble-intersection.witness.json` labels
  the (4-q)/(4q+3) entry as **"← post-hoc"** in its own output

**Main has NOT fixed:** the replacement "algebraic-Galois" Step 1
in the new `mobius-limit-from-thimble.md` sources the **constants**
{4, 3} from the cubic's c²-coefficient and degree, but does not
source the **variable q** in either `4-q` or `4q+3`. Re-narration
without elimination.

### Sibling discovery — PR #879 (open, 2026-05-22)

[`audit: 210× scale-gap third pass — identifies CAL-4 in λ_scale (corrects PR #772 + interim v2)`](https://github.com/litlfred/qou/pull/879)
independently catches the **literal** face of the same CAL-4:
`LAMBDA_PROTON_DOC = 2.4599527869` hardcoded in
`m_p_borromean_verification_50dps.py`. The cheat sheet
[`docs/canonical-derivation-cheat-sheet.md`](https://github.com/litlfred/qou/blob/claude/210x-scale-gap-root-cause-v2/docs/canonical-derivation-cheat-sheet.md)
§5 Migration Backlog #1 + §8 Pitfalls track this as a known
3-calibration discipline violation with proposed replacement
`prop:lambda-scale-bring-bloch-identity` (open R&D).

| Audit | Face of the CAL-4 | Manifestation |
|---|---|---|
| **PR #879** | Literal | `LAMBDA_PROTON_DOC = 2.4599527869` hardcoded |
| **PR #751 critical re-analysis** (this branch) | Curve-fit | `a(q) = (4-q)/(4q+3)` → `A(a(q)) ≈ 2.4599` at q_0 |

Both reduce to the same observable: `λ_scale` has no substrate
derivation. The two-faces framing should help downstream readers
not "fix" one face without the other.

**Classification of #879 vs #751:**

| Axis | Value |
|---|---|
| Overlap | **additive** (same finding, two surfaces — literal vs curve-fit) |
| Dependency | **independent** (different files, both doc-only) |
| Cherry-pick opportunity | none in either direction; cross-link is sufficient |

### Posted coordination comments (round 2)

| Sibling | Action | Topic |
|---|---|---|
| #879 | post `add_issue_comment` (this update) | Two-faces of same CAL-4; link my audit; agree the named replacement `prop:lambda-scale-bring-bloch-identity` covers both |

### Escalations

None. PR #879's framing (literal CAL-4 in production scripts) and
this branch's framing (curve-fit CAL-4 in narrative blocks) are
**consistent, complementary findings**, not inconsistent. Both
point at the same Migration Backlog #1 resolution
(`prop:lambda-scale-bring-bloch-identity` or equivalent).

### Next concrete task (non-overlapping)

Subject to user direction (see end-of-turn options): either
(a) audit `prop:lambda-scale-bring-bloch-identity` + the 5
`bring_bloch_tier{1..5}_search_m_p.py` scripts for whether THAT
candidate replacement is itself a substrate derivation or a
Bring-volume PSLQ fit to CODATA, or (b) open a follow-up PR
adding the explicit "q is not sourced" banner from §3.5 of the
audit to `prop:mobius-limit-from-thimble` and demoting it to
`conj:mobius-limit-from-thimble`.
