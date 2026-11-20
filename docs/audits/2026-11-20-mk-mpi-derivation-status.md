# m_K/m_π: what is derived, what is selected, and what the row waits on

**Date:** 2026-11-20 · **Branch:** `claude/mk-mpi-derivation-2026-11-20` (PR #8529)
**Scope:** the STRONG core `[3]_q[4]_q` and the FORM of the EM term. The α_em half
(the Witten-κ Gram `sorry`, the two rival α_em derivations, bean `qou-aemx`) is
being worked on a sibling branch (`claude/alpha-em-witten-kappa-2026-11-20`) and is
not touched here.

Prior assessments this builds on, not re-derives:
[`2026-08-22-mK-mpi-l2-red-team.md`](2026-08-22-mK-mpi-l2-red-team.md) (bean `qou-dhck`,
completed), [`2026-05-28-meson-mass-ratio-derived-vs-fitted.md`](2026-05-28-meson-mass-ratio-derived-vs-fitted.md),
`24156dd479` (the Molien ruling does not reach this row).

---

## 1. The row, recomputed by component (measured this session)

`computations/meson/mk_mpi_derivation_status_probe.py`, 70 dps, proton q₀ =
`1.1099785827513808076…`, α_em⁻¹ from the same call the dashboard makes
(`meson_em_sinh_closed_form.alpha_em_inv_derived`) = `137.035935093976`.
Witness `computations/meson/mk-mpi-derivation-status.witness.json`, 4/4 assertions.

| component | value | err vs PDG 3.53711843895 | vs 263.6 ppb target |
|---|---|---:|---|
| core √([3]_q[4]_q) | 3.5367592327 | **−101 553.36 ppb** | misses **385.26×** |
| EM term on the ratio², (α_em/π)(1+log(1+ℏ_q)) | 0.002542269086 (factor 1.094475028) | — | — |
| total √(core² + EM) | **3.53711862102** | **+51.4754 ppb** | meets, miss_factor 0.1953 |

The total reproduces the committed dashboard row (`pred 3.53711862102`,
`err_ppb 51.48`) to every printed digit; this is asserted in the witness.

## 2. Corpus-grep (six paths) — what exists

| path | what it holds on this question |
|---|---|
| audits | red-team 2026-08-22 (tiers: core scan-selected, truncation fitted, α_em conditional); 2026-05-28 derived-vs-fitted (the term-by-term EM hunt, lines ~200–235; the "why 3 and 4 reduces to m_s/m_d" reframing, lines ~143–186); 2026-05-29 residual-derivation attempt (Seifert route, no derivation); 2026-08-02 roast (EM full-log fits worse). |
| content | `braids-and-knots/meson-qcg-fusion-identity.{md,lean}` (the identity only); `braids-and-knots/meson-em-sinh-closed-form.{md,lean}` — its `.md` already states it "does not identify that quantity with any physical correction"; `braids-and-knots/meson-em-sinh-ratio-reading.md` — already says the pair "was found by scanning products of q-integers, and the derivation of that pair from the braid content is open"; `knots-particles-confinement/lepton-meson-torus-knot-dictionary.{md,lean}` — pion = quarks (3,3), kaon = (3,5), totals 6/8/10; `mass-theory/meson-kaon-pion-hecke-seifert.md` — a different, retired route `χ^{(2,1)}(σ₁⁵)·(V_S ratio)²`. |
| computations | `meson_3x4_structural_origin.py` (witness description: *"Spin assignment post-hoc; first-principles braid derivation open"*); `meson_fusion_why34_em_residual.py`; `derive_ms_md_torus_knot.py` (no bare-knot ratio within 34 % of `2[3][4]−1`). |
| coordination | `sm-26-parameter-chip-away.md`, `2026-07-17-1ppq-program-ownership-map.md` — status mentions only. |
| library | `kaon` appears only in physics sources (GMOR/SU(3) breaking, lattice: `arxiv-1206.3156v2`, `arxiv-0811.1338v1`, `arxiv-0710.4405v1`, the SU(3)×SU(3) current-divergence OCR). None proposes a q-integer form. (`ocr/` tier included.) |
| beans | `qou-dhck` (red-team, completed), `qou-v6oz` (truncation, completed), `qou-5ipv` (roast, in-progress), `qou-3l2l` (α_em + meson leg epic). **No bean carries "derive the pair (3,4)" or "derive the EM factor's form".** |

**Derived vs selected, as the corpus itself records it:**

- `[3]_q[4]_q = [2]_q+[4]_q+[6]_q` — **proved** (`QOU.BraidKnot.meson_qCG_3x4`), but
  as an identity of q-integers. Its identification with m_K²/m_π² is **selected**:
  "candidate found by scanning q-integer products" (2026-05-28 audit; content block
  `meson-em-sinh-ratio-reading.md`, "The ratio is not, however, parameter-free").
- Squaring (GMOR / 2-body mass²) — **motivated** argument, 0 free parameters.
- EM term **magnitude scale** `(α/π)·m_π²` — **selected** from four candidates by
  closeness to the residual (2026-05-28 table: LO 0.92×, α f_π² 1.25×, …).
- EM **factor** `1+log(1+ℏ_q)` — **selected**: `(1+ℏ_q)` chosen because it closed
  to 0.46 %, `−ℏ_q²/2` because it closed further, then the log named as the series
  with that jet. The 2026-08-22 de-fit removed the *truncation* knob; it did not
  derive the *form*.
- α_em — derived conditional on the Witten-κ `sorry` (sibling's front).

## 3. Formalize-first on the selection — `QOU.BraidKnot.MesonFusionIndexSelection`

File: `folio/quantum-observable-universe/lean/QOU/BraidKnot/MesonFusionIndexSelection.lean`
(generic `CommRing`, `q·qi = 1`, §7c; wired into `QOU.lean`).

| declaration | statement | what it settles |
|---|---|---|
| `qCG_unnormalised_general` | `(q^m−qi^m)(q^{m+d}−qi^{m+d}) = (q−qi)·Σ_{k<m}(q^{d+1+2k}−qi^{d+1+2k})` for **all** m, d | the fusion identity is a family-wide fact |
| `meson_qCG_3x4_is_family_instance` | the credited `meson_qCG_3x4` statement, verbatim, as the m=3, d=1 instance | **the Lean credit on the core carries zero selection information** — it is equally true of every scan pair |
| `qCG_2x6` | `[2]_q[6]_q = [5]_q+[7]_q` | the runner-up (2,6) has an identity of identical standing |
| `scanPair_four_not_dictionary_index` | ∀g, quark torus index ≠ 4 (all odd, `quarkTorusIndex_odd`); ∀g, meson total crossing ≠ 4; kaon constituents (3,5) ≠ (3,4) | **scope (b) for the index reading only**: against the corpus's lepton–meson dictionary, `[4]_q` cannot be `[n]_q` of any quark or meson index — invariant: parity / the finite table. It does not exclude a reading the corpus has not defined (e.g. a spin-3/2 dimension, which `meson_3x4_structural_origin` calls "post-hoc"). |
| `sqrt_jet_agrees_to_order_two` | `(1+h−h²/2+h³/2)² = 1+2h+h⁴(…)` | the order-2 jet matched to data is also √(1+2h)'s |
| `pade_jet_agrees_to_order_two` | `(1+h/2)(1+h−h²/2+h³/4) = 1+3h/2+h⁴/8` | … and the [1/1] Padé's |

**Verification.** `lean -DautoImplicit=false -s 65536 QOU/BraidKnot/MesonFusionIndexSelection.lean`
→ exit 0, against restored dependency oleans (batteries, aesop, Qq, plausible,
proofwidgets, importGraph, LeanSearchClient from `cat/folio-assistant-sci/lake-cache/qou-v4-24-0`
head `a792c46d01b`) plus Mathlib oleans. `#print axioms` on all six:
`[propext, Classical.choice, Quot.sound]` — no `sorryAx`. Negative control (`(2:ℕ)=3 := rfl`
appended) → exit 1, so the check is live. Not run: the library sweep
(`scripts/lean-library-sweep.py`); the file imports Mathlib only, so its cone has no QOU
dirty closure.

**Honest negative, stated in its scope.** No corpus definition forces `(3,4)`.
The corpus's own meson objects (pion quarks `(3,3)`, kaon `(3,5)`, totals `6, 8`) are
proved not to contain `4`; the natural dictionary-indexed readings miss badly
(probe: `[5]/[3]` −86 %, `[8]/[6]` −89 %, `[3][5]` +27 %, GMOR with `m(n)=[n]_q` −89 %
on the ratio²). This is "not forced by anything the corpus defines", **not** "cannot be
derived": a future definition of the kaon as a Hecke/Wedderburn object could force it.

## 4. Look-elsewhere: how much did selecting (3,4) buy? (measured)

Scan family `{[a]_q[b]_q : 1 ≤ a ≤ b ≤ 12}` (78 members) at q₀:

| rank | pair | rel. dev. on m_K²/m_π² |
|---|---|---:|
| 1 | (3,4) | **203.10 ppm** |
| 2 | (2,6) | 26 742 ppm |
| 3 | (1,10) | 49 310 ppm |

The nearest family members bracketing the target are 7.61 % apart, so a target placed
at random in that gap lands within ±203 ppm of a member with probability
≈ 2·203e-6 / 0.0761 ≈ **0.53 %**. Read with care: the actual scan's family (which also
tried other closed forms — the retired `(q⁵−q⁻⁵)(9/5)²` route, Seifert powers) was larger
than this one, which raises the look-elsewhere chance; and one 1-in-190 coincidence is
not a derivation. It does say the 203 ppm agreement is not *cheap* within this family,
which is the honest reason the pair is worth deriving rather than discarding.

## 5. The EM term's form — derived or chosen?

**Chosen.** No content block or Lean declaration derives `1+log(1+ℏ_q)` (or the
`(α/π)·m_π²` scale) from a corpus object. `meson_EM_closed_form` proves only that the
retired order-2 truncation equals `(3q²−1)/(2q²)`, and its own content block says so.
The probe measures what that choice is worth across resummations that share the
matched jet:

| EM factor | err on m_K/m_π |
|---|---:|
| 1+log(1+h) (shipped) | 51.48 ppb |
| √(1+2h) | 63.68 ppb |
| Padé [1/1] 1+h/(1+h/2) | 44.96 ppb |
| 1+h−h²/2 (retired truncation) | 23.45 ppb |
| 1 (no substrate factor) | −8 718.6 ppb |

**Implication.** Within the order-2-jet class the verdict does not move (all inside
263.6 ppb; spread ≈ 19 ppb). What carries the row across the line is the *presence and
scale* of `(α_em/π)·(1+O(ℏ_q))` — dropping the substrate factor misses 33×. So the EM
form question is real but secondary; the scale question is not settled by any corpus
object.

**Critical-distance observation (assessment, not a corpus claim).** The term is called
"EM", but its size on the kaon scale, ≈ 49.5 MeV², is ~4 % of the measured π± EM
self-energy splitting (m_π±² − m_π⁰² ≈ 1261 MeV²) — the 2026-05-28 audit records this
itself. Under Dashen's theorem the leading EM shifts of K± and π± are equal, which acts
on the ratio² with the opposite sign structure to a pure `+(α/π)` addend. So the term is
best described as *a residual-sized addend with an α_em-proportional scale*, not as the
leading electromagnetic correction of chiral perturbation theory. A derivation would
have to say which object it is.

## 6. Can the row become unconditional? What it waits on

The strong core alone misses by 385×, so the row meets L2 **only** with the EM addend.
Unconditional status needs all three:

1. **α_em unconditional** — the Witten-κ Gram `sorry` (`em-coupling-chern-simons.lean`)
   and the reconciliation of the two α_em derivations: bean `qou-aemx` / epic `qou-3l2l`,
   on the sibling branch `claude/alpha-em-witten-kappa-2026-11-20`.
2. **The pair (3,4) derived** — a definition of K and π as Hecke/Wedderburn objects
   from which `[3]_q[4]_q` follows. Not derived; no corpus definition forces it (§3).
   New bean (GAP, this PR).
3. **The EM addend derived** — its scale `(α/π)·m_π²` and its factor. Chosen (§5).
   New bean (GAP, this PR).

Discharging (1) alone does **not** make the row unconditional: it removes the
`sorry`-condition and leaves two selection knobs. The honest count stays
**0/6 unconditional** until (2) and (3) close.

## 7. One stale sentence corrected

`docs/precision-goals.md:55` said of `m_K/m_π`: *"the `[3]_q[4]_q` core (99.98 %) is
exact/Lean-proved and α_em is derived, so the ratio itself is parameter-free"*. That
contradicted three corpus artifacts that already decide it — the red-team
(2026-08-22), the dashboard row's own note in `per_observable_100x_status.py`
("NOT parameter-free … the (3,4) pair is scan-selected") and the content block
`meson-em-sinh-ratio-reading.md` ("The ratio is not, however, parameter-free"). Corrected
in place (ask-first exemption 2: derived from the corpus), with the old wording quoted.
No number changed.
