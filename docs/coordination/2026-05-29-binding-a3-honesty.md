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

Both items framed initially as "Open Math A" and "Open Math B" turned out (2026-05-31 reanalysis, commit `f4614a09`) to be **structurally already answered** in the framework: ρ_F = ν_SDP per [`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md) (RESOLVED 2026-05-24); p/n asymmetry via Bring color-tube weighting in [`closed_form_tau_M.py`](../../computations/closed_form_tau_M.py) `pn_convention="bring_color_weighted"` (PROVED PR #690/#942). Remaining is verification/formalisation: Lean class for [`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md); re-run of `binding_shell_enhancement_derivation.py` with Bring weighting; joint-tower SDP extension to ν_SDP(⁴He). **Pattern post-mortem** of why the existing resolution was missed (third such miss in this session) recorded in audit `## Why was the resolution missed?` section + corrective discipline (grep audits/ + corpus before declaring open).

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
- PR #1756 per-knot `m_e · VolDensity(K)` — err −50 % to −97 % across 6 atoms

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
