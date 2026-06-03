# A≥3 binding honesty — per-λ overclaim + shell review

**Created:** 2026-05-29
**Owner branch:** `claude/binding-log-scale-2026-05-28` → **PR #1417**
**Context:** Shell review ("shell is extractable in canonical braid-word
witness data; review paper on shells") surfaced that the per-λ Δ_λ
binding formula does **not** close the deuteron and a merged doc
overclaims closure via a fitted `C_knot`. Coordinated against the
in-flight binding-scale sibling so the two angles don't collide or
duplicate.

## Scope map

| PR | Branch | Angle | Relationship |
|----|--------|-------|--------------|
| **#1417** (mine) | `binding-log-scale-2026-05-28` | per-λ overclaim retraction + shell review + log-κ probe | — |
| **#1416** | `binding-habiro-dashboard-2026-05-28` | scalar binding-scale de-fit (E₀ probe, transfer-matrix unfold, dashboard) | **high overlap, complementary** |
| #1396 | `meson-tower-derivation-2026-05-28` | meson m_K/m_π is fitted (audit) | thematic only (same derived-vs-fitted rigor; different files) |

**No file overlap** between #1417 and #1416 (checked against #1416's 14
files). The per-λ files (gating doc, `deuteron-binding-interface-closure`,
`binding_energy_categorical_deuteron.py`) are mine; the scalar-scale files
(`shell_binding_transfer_matrix.py`, `binding-energy-scale-probe`,
`per_observable_100x_status.py`) are #1416's.

## Scope split posted on #1416
[comment](https://github.com/litlfred/qou/pull/1416#issuecomment-4575497037):
I take the per-λ overclaim correction; I will **not** duplicate #1416's
`shell_binding_transfer_matrix.py` / `binding-energy-scale-probe`. Offered
to fold #1417 into #1416 if a single de-fit PR is preferred (awaiting
response).

## Findings (this branch)

1. **Per-λ Δ_λ formula does NOT close binding.** Live 50 dps:
   `B = m_e·|Σ_λ y_λ·χ^λ·sgn·f^λ|` gives D −82.9 / T −77.5 / ³He −69.6 /
   ⁴He −89.3 %. The "Δ_λ CLOSURE ACHIEVED, zero free params" doc update
   (2026-05-26) is retracted; closure relied on `C_knot = 5.852 =
   B_AME/(m_e·|sum|)` — a fit.
2. **Shell is per-λ, not missing.** Recoverable from `atom-chi-rust-*`,
   `chi-lambda-he4-full-partition-table`, self-conjugate/magic labels,
   staircase λ_shell, torus-knot q^{2n_s} gap. The scalar Δtr / log-ratio
   collapses it.
3. **Two ~4 MeV scales close the deuteron only:** `m_e·Vol(𝓑₃)` (+0.19%,
   mine) and #1416's `E₀ = m_e/(q₀(q₀−1))` (+12%). Neither extends to A≥3.
   C_knot 5.85 (per-λ deficit) ≈ #1416's E₀/Q_β 5.34.

## Review comments addressed (#1417)
- Gemini HIGH (float64 `complex()` in `_real`): **accept-with-modification**
  (07efba0e2) — literal `mp.mpc(s)` ValueErrors on `a±bj`; used a
  float64-free real-part parse. Thread resolved.

## Update (2026-05-29 PM) — sibling state + derivation result

**Sibling state.** #1416 **confirmed the scope split** (keep separate, no
file overlap; my finding corroborates its de-fit). New overlapping siblings,
intent posted: **#1420** (meson 290 ppm → "EM is the lead"; ruled out
`R=1+4u²` as a fit, c=4.03≠4 — I heed this, won't wire it) and **#1421**
(low-mass sweep → D/T/³He census-knots = AME fit + "no derived atom→knot
rule" — same root cause as my `mass-volume-factorization` caveat). #1422
(q₀ re-pin −11.5 ppb) negligible for my %-level binding numbers.

**Derivation result (the open problem, advanced).** The A≥3 deficit is the
**linear truncation** `tr ~ exp(Vol)` ⇒ `Δtr` is the linearisation. The
extensive structure is the **complex-q / q-Reeb rotation** (per-rep:
rotation on (2,1), growth on outer). The **Markov-weighted q-Reeb phase**
closes the **A=3 mirror pair (³H, ³He) to 2% with no fit** (ρ≈18.5
MeV/rad); D (2-body) and ⁴He (doubly-magic + Coulomb=sinh channel) are the
special cases. Full write-up in
[`2026-05-28-binding-endomorphism-analogy.md`](../audits/2026-05-28-binding-endomorphism-analogy.md)
§"A≥3 derivation campaign".

## Next concrete task
- `/prepare-merge` #1417 in progress (rebased onto main, witness drift
  refreshed, docs added). Then reviews + merge per owner.
- Open lead (derive-or-refute, no fit): tighten the rotation-phase ρ by
  isolating the (2,1)-only Reeb phase and removing the ⁴He Coulomb (sinh)
  term; check whether D's 2-body case unifies. **#1416's scalar-scale lane
  is complementary — do not duplicate.**

---

## 2026-05-31 update — magic-A wireup (PR #1543)

**Continuation of this thread.** User question "why does heavy-nucleus binding miss by 2-5×?" + my honest audit ([`2026-05-31-binding-alpha-shift-a4-status.md`](../audits/2026-05-31-binding-alpha-shift-a4-status.md)) revealed:

1. The framework already carries **two distinct binding paths** in disjoint Python files:
   - `binding-alpha-shift-extension` (per-rep Reeb phase at force-carrier torus knot) — exact for D, misses ⁴He by −79%.
   - `magic_A_formula` (ρ_F · m_e · A · 8G) — doubly-magic regime; gets ⁴He to +5.9%.
2. The §3b-cond `BindingForceCarrierKnot` class only knew the first path — wireup gap, not new math.
3. PR #1543 ships the wireup as a Lean content-block triple [`prop:magic-A-binding-formula`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md) (sorry-free §3b-cond) + extended witness emitter + audit doc.

**Gap closure factor:** 13.5× for ⁴He (|rel_err| 0.7904 → 0.0587). (The audit doc initially claimed 80×; Copilot review caught the math error, corrected in commit `68176332`.)

### Scope map (2026-05-31)

| PR | Branch | Angle | Relationship to #1543 |
|---|---|---|---|
| **#1543** (mine) | `binding-magic-A-wireup-2026-05-31` | magic-A formula wired in as §3b-cond Lean + content block + canonical-dispatch witness | — |
| #1507 | `canonical-fit-pattern-triage-2026-05-30` | Class-A banners on fit-pattern scripts | **scope-adjacent**: ρ_F = 2 risks fit-pattern misclassification; intent comment posted [#1507](https://github.com/litlfred/qou/pull/1507) |
| #1535 | `q0-regen-batch-cont-2026-05-31` | Witness regen sweep for ~370 stale | **no overlap** — new `binding-alpha-shift-witness.witness.json` is post-q₀-repin |
| #1537 | `nucleus-empty-sdp-refactor-2026-05-30` | Empty-SDP uniqueness for 7 nuclei | **tangent** — different mechanism (SDP vs. magic-A formula); both target the same A≥3 problem from different sides |
| #1475 | `qbeta-ck-interpretations-2026-05-30` | Q_β c_k Taylor interpretation | **tangent** — same `mass-theory/` chapter, different observable |

### Carry-forward

Both items framed initially as "Open Math A" and "Open Math B" turned out (2026-05-31 reanalysis, commit `f4614a09`) to be **structurally already answered** in the framework: ρ_F = ν_SDP per [`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md) (RESOLVED 2026-05-24); p/n asymmetry via Bring color-tube weighting in [`closed_form_tau_M.py`](../../folio-assistant/computations/closed_form_tau_M.py) `pn_convention="bring_color_weighted"` (PROVED PR #690/#942). Remaining is verification/formalisation: Lean class for [`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md); re-run of `binding_shell_enhancement_derivation.py` with Bring weighting; joint-tower SDP extension to ν_SDP(⁴He). **Pattern post-mortem** of why the existing resolution was missed (third such miss in this session) recorded in audit `## Why was the resolution missed?` section + corrective discipline (grep audits/ + corpus before declaring open).

## 2026-06-03 — PR #1748 bar-pairing extension (cross-PR coord)

PR #1748 (intra-partition rayon for the MPFR character kernel) carries
a downstream bar-pairing extension of PR #1742 that landed full
χ_λ data for the light series at q_0 AND q_0^{-1}.  Results below
are added to the A=3 honesty ledger as **independent confirming
evidence** for the "per-block formula does not extend past D"
finding — same conclusion as PR #1754's canonical Jones-Markov
underprediction and PR #1756's per-knot RED verdict.

### Bar-pairing extension table (PR #1742 formula)

| atom | n | B_arch (MeV) | err vs AME | growth_free / atom |
|---|---|---|---|---|
| D   | 6  | 2.3043 | +3.6 % | 4/5 |
| T   | 9  | 3.2525 | **−61.7 %** | 16/16 |
| ³He | 9  | 3.4667 | **−55.1 %** | 16/12 |
| ⁴He | 12 | 3.8043 | **−86.6 %** | 32/29 |

Three independent per-block formulations now agree the formula fails
past D:

- PR #1742 `Σ_λ y_λ (|χ^λ_free| − |χ^λ_atom|)` — err D +3.6 % → ⁴He −86.6 %
- PR #1754 canonical Jones-Markov — uniformly underpredicts ~0.4-0.7 MeV
- PR #1756 per-knot `m_e · Geom_full(K)` — err −50 % to −97 % across 6 atoms

### Durable artifacts

On PR #1748's branch (`claude/hecke-mpfr-intra-partition-rayon-2026-06-03`):

- χ_λ MPFR-50dps caches at q_0 AND q_0^{-1} for D / T / ³He / ⁴He
  (free + atom braids)
- `bar_pairing_binding_observable.py` cache-aware consumer
- Roadmap doc:
  [`docs/audits/2026-06-03-bar-pairing-extension-tritium-he4-roadmap.md`](../audits/2026-06-03-bar-pairing-extension-tritium-he4-roadmap.md)

### Coord cross-links

- PR #1742 (parent observation): two coord comments posted with sanity
  check + final table
- PR #1754 (A=3 binding tranche): intent comment posted with cross-isotope data
- PR #1756 (per-knot 6-atom RED): intent comment posted noting parallel evidence

This entry closes the §3 sibling-intent step of the coordinate sweep
for the binding-observable scope on 2026-06-03.

## 2026-06-03 — per-knot λ(K): Habiro refuted, component selection rule found (PR #1765)

`/coordinate` sweep for the Geom_full-bridge work (PR #1765, branch
`claude/habiro-per-knot-lambda-derivation-2026-06-03`).

**Scope map:**

| PR | relation | classification |
|----|----------|----------------|
| #1762 (my parent) | 1ppQ roadmap §6.8 — this PR executed its top recommendation | dependency (posted result) |
| #1742 (bar-pairing) | same linking_weight / per-block scope | overlap (prior coord) |
| #1768 / #1772 (Kashiwara crystal, Q_β) | crystal-basis object, different application (Q_β not mass) | adjacent (ledger-only, not spammed) |
| #1521 (Habiro [2]_q·(1−h²α) fermion loop) | Habiro element, α_EM application | adjacent (different element) |

**Findings landed:**
1. Habiro hook **refuted** against the owner-uploaded G-Z paper
   (`uploads/2111.06645v3.pdf`): the figure-eight Kashaev element is
   root-of-unity-bound (terminates at ζ_N, diverges at real q₀);
   `Φ^(4_1)` leads with 3^(−1/4)≈0.76 (not 1), complex Q(√−3) coeffs,
   ℏ=2πi/N. The −1.05% real-q₀ coincidence was a resummation artefact.
2. **Zero-parameter component selection rule found** (the productive
   redirect): `lw(L) = (1/(c+1)) Σ_{λ⊢(c+1)} dim_q V_λ`, reproducing
   muon (c=1, exact ∀q) and proton (c=3, = Family-A) exactly. A finite
   quantum-dimension (Gelfand-model) Laurent polynomial — crystal-basis
   compatible, NOT a Habiro series.
3. **Gelfand ≠ regular**: the 6 knot-operator basis = Σ_{λ⊢3}(dim)²=6
   (regular rep); the linking_weight = Σ_{λ⊢3}dim=4 (Gelfand). Even/odd
   rank dichotomy: both anchors at even rank (poly in h²); c=2,4 odd
   rank carry √(h²+4).

**Coord comments posted:** PR #1762 (result of §6.8); PR #1765 (own
review triage, 11 Copilot threads resolved).

**Open / next:** (a) decisive c=2 test — find a 2-component-link
particle, check lw vs (q+1)²/(3q)=1.337 at q₀; (b) derive why rank
= c+1 (lepton-fibre hypothesis). Both gated on owner direction.

## 2026-06-03 (sweep 2) — c=2 investigation + PR #1777 EM-linking overlap

Second `/coordinate` sweep on PR #1765 branch.

**New since first sweep:**
- 5 new main commits (lean extractor, qa-sweep, canonical-axis WIP, copilot
  review on #1774, skills idle-time discipline) — all infrastructure, no
  file overlap with PR #1765's branch.
- **NEW SIBLING:** PR #1777 "Derive the two-like-charge EM-linking
  invariant (pp-Coulomb T−³He gate)" — genuinely overlapping methodology
  (per-interface 2-link scalar with the same "no fit / no CAL-4"
  discipline). Posted intent with the c=2 candidate
  `(q+1)²/(3q) = 1.337` as a concrete derived candidate for their
  EM-linking slot.

**Internal c=2 investigation (read-only, NOT committed to PR #1765):**
- Framework knot-particle table: gluon = Hopf link L2a1 (c=2), with Higgs
  = 4_1, muon = 5_1 (cinquefoil) — all c=1 knots so the c=1 lw=1 anchor
  still holds for all of them.
- `tr_M(σ₁²) = 1 + (q−1)/√q ≈ 1.104` at q₀ — the Markov trace of the Hopf
  link is NOT the same object as `(1/3)Σ_{λ⊢3} dim_q = 1.337` (Markov
  trace vs Wedderburn channel sum; different layers).
- Conclusion: the framework currently exposes NO observable that IS the
  gluon's c=2 linking_weight; PR #1777's "EM-linking invariant" slot is
  the most natural exposure point (now flagged via the intent comment).

**Own review threads:** all 11 still resolved (no new review activity on
PR #1765 since sweep 1).

**Comments posted:** PR #1777 (c=2 candidate).

**Open / next:** awaiting PR #1777 author triage. PR #1765 itself stands
complete as-is (selection rule + Habiro refutation + STEP-4 Gelfand-vs-
regular-rep analysis + 11 review fixes).
