# Downstream propagation of the coulomb-decomposition correction

**Date:** 2026-08-08
**Branch:** `claude/coulomb-decomposition-downstream-2026-08-08`
**Upstream:** [`docs/audits/2026-08-08-convention-slip-class-sweep-force-channels.md`](2026-08-08-convention-slip-class-sweep-force-channels.md)
(defect 1 + defect 2), PR #4760, commit `a52e583c96` (cherry-picked here).

## What propagated

`climax-volume-mass/coulomb-charge.md` had the crossing-energy split's
multiplicities exchanged. Corrected upstream to

```
E_cross = n₊q − n₋q⁻¹  =  ½(n₊ − n₋)(q + q⁻¹)  +  ½(n₊ + n₋)(q − q⁻¹)
                            ↑ bar-even = Q         ↑ bar-odd = ½·total crossings
```

Three consequences carry downstream:

1. **`Q` scales the bar-even channel**, not the bar-odd one.
2. **The bar-odd coefficient is a crossing count**, hence non-negative, so it
   cannot change sign with chirality. Any claim that `Q`'s sign flips an
   attractive/repulsive contribution is unsupported.
3. **An unqualified `tanh(ln q) ≈ 0.104`** is the `n₋ = 0` case only.

## The discriminator that settles most verdicts

Most of the sweep's apparent breadth dissolves once two distinct ratios are
separated. They are numerically equal at `m = 0` and nowhere else, which is why
they were conflated:

| Ratio | Value | Needs the `m = 0` qualifier? |
|---|---|---|
| **Per-crossing** weight ratio `(q − q⁻¹)/(q + q⁻¹)` | `tanh(ln q) ≈ 0.104` | **No.** A single crossing has no multiplicity. |
| **Channel-total** ratio `E_asym/E_sym` | `((p + m)/(p − m))·tanh(ln q)` | **Yes.** |

A block quoting `0.104` is therefore only defective if it is quoting the
*channel-total* ratio. Three blocks that the `tanh` grep surfaced
(`skein-crossing-asymmetry-prop`, `hydrogen-knot-structure`,
`pair-creation-energy`) use the per-crossing ratio and are clean on this axis.

The canonical Lean matches: `emStrongRatio` is defined at
[`crossing-energy-decomposition.lean:115`](../../content/quantum-observable-universe/observations/crossing-energy-decomposition.lean),
*above* the composite section that begins at line 147 — i.e. it is the
per-crossing ratio, and `em_strong_ratio_tanh` is a correct identity. **No Lean
change was needed for the ratio.**

## Per-block verdicts

19 blocks triaged: **6 defective (fixed)**, **13 clean**, **4 needs-author items**
(raised as beans, spread over 3 of the blocks).

### Defective — fixed

| Block | Defect | Fix |
|---|---|---|
| [`observations/strangelet-crossing-energy`](../../content/quantum-observable-universe/observations/strangelet-crossing-energy.md) | `.md:17,19` gave `𝔈_cross = N·½(n₊+n₋)(q+q⁻¹)` and "the entire crossing energy lies in the symmetric (strong) channel". **Both the channel and the multiplicity are inverted:** `Q = ½(n₊−n₋)` is the bar-even coefficient, so `Q = 0` *annihilates* that channel and forces `n₊ = n₋`. | Now derives `𝔈_cross = N·½(n₊+n₋)(q−q⁻¹) = N·n₊(q−q⁻¹)`, purely bar-odd. Title "purely strong" → "purely bar-odd". **Lean sibling corrected too** (below). |
| [`climax-volume-mass/q-energy-terms-and-limits`](../../content/quantum-observable-universe/climax-volume-mass/q-energy-terms-and-limits.md) | *(upstream defect 2.)* `.md:35` gave the negative-crossing weight as `q⁻¹`, dropping the sign that `def:crossing-energy` carries (`−q⁻¹`) — the identical error one level down, at the per-crossing weights. Its stated sum reconstructed `n₊q + n₋q⁻¹`. Also reused `𝔈_×` for two quantities. | Signed weights restored per `def:crossing-energy`; `𝔈_× = ½(q−q⁻¹)` kept as the *sign-blind bar-odd* weight (its canonical corpus meaning); signed total named `𝔈_cross`. |
| [`observations/crossing-energy-interpretation`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md) | Asserted "the antisymmetric part distinguishes charges" **in the same paragraph** that noted the `sinh` weight is blind to the crossing sign — an internal contradiction. "Physical force" column assigned Strong / Coulomb to the two channels. | Force column replaced by the channel totals; row labels → Symmetric / Antisymmetric; identification flagged open; `m = 0` scope made explicit on the table. |
| [`observations/cp-violation-evidence`](../../content/quantum-observable-universe/observations/cp-violation-evidence.md) | `.md:27` quoted `tanh(ln q) ≈ 0.104` as *the* EM-to-strong ratio from the decomposition, unqualified. **Kaons are precisely the mixed-chirality case** the qualifier exists for. | Qualifier + the unevaluated `(p+m)/(p−m)` factor stated; channel identification withdrawn. The `δ_CP ~ 10⁻³` order-of-magnitude agreement is **retained as recorded**. |
| [`observations/strangelet-double-beta-interpretation`](../../content/quantum-observable-universe/observations/strangelet-double-beta-interpretation.md) | "This is not a coincidence: both measure the antisymmetric channel", citing the decomposition — while working in the `Q = 0` sector, i.e. `p = m`, where the channel-total ratio has a **zero denominator**. | Numerical coincidence retained and explicitly *recorded, not explained*; causal claim withdrawn; `Γ_2β ~ s⁴ ≈ 10⁻⁴` unchanged, now in terms of `s` itself. |
| [`observations/substrate-consistency-window-table2-data`](../../content/quantum-observable-universe/observations/substrate-consistency-window-table2-data.md) | Row 2 "EM/strong ratio \| `tanh(ln q)`" — unqualified channel ratio + the withdrawn label. | Relabelled "Bar-odd/bar-even weight ratio (per crossing)". **Value `0.104` unchanged.** |

### Clean

| Block | What was checked |
|---|---|
| [`observations/crossing-energy-decomposition`](../../content/quantum-observable-universe/observations/crossing-energy-decomposition.md) | The canonical source. Claim 1 has the correct `(p−m)cosh + (p+m)sinh`; claim 4 gives **both** the `m = 0` ratio and the general multiplicity factor. Reference standard for this sweep. |
| [`observations/crossing-energy-pair-cancellation`](../../content/quantum-observable-universe/observations/crossing-energy-pair-cancellation.md) | `.md:14` uses the correct `(p−m)cosh λ + (p+m)sinh λ`; the mirror argument turns on sign-blindness, consistent with the correction. Attributes the Coulomb reading to `rem:pair-creation-energy` rather than asserting it. |
| [`observations/breit-wheeler-observation`](../../content/quantum-observable-universe/observations/breit-wheeler-observation.md) | Cites `prop:crossing-energy-decomposition` in `uses[]` but uses **no** split, ratio, or `Q`. Its `h_A = q − q⁻¹ ≈ 0.209` is a raw `q`-quantity. |
| [`observations/w-boson-mass-discrepancy`](../../content/quantum-observable-universe/observations/w-boson-mass-discrepancy.md) | Same: cites the decomposition, uses only the vertex `δq` formula. No split, ratio, or `Q`. |
| [`observations/substrate-consistency-window`](../../content/quantum-observable-universe/observations/substrate-consistency-window.md) | Prose block; all numerics live in its table-data siblings. Table 2 was the defective one (fixed above). |
| [`knots-particles-confinement/electroweak-higgs-torus-link-triplet`](../../content/quantum-observable-universe/knots-particles-confinement/electroweak-higgs-torus-link-triplet.md) | Uses only `Q = ½·writhe` on `σ₁^{2k}` (`.md:48`), correct and untouched by the fix. Its bar-even/bar-odd is the **σ-involution grading on the Hecke sym/alt block** (eigenvalue swap `q^{2k} ↔ q^{−2k}`), a *distinct object* from the `q ↔ q⁻¹` grading of the crossing-energy split — attributes do not transfer between them. Notably it already declines to use `Q` for the charge assignment ("it cannot single out the neutral slot"). |
| [`knots-particles-confinement/electroweak-triplet-charge-spin-from-involution`](../../content/quantum-observable-universe/knots-particles-confinement/electroweak-triplet-charge-spin-from-involution.md) | No split, no ratio, no `Q` in the statement. Cites `def:coulomb-charge` only in a `.ts` note recording the free-label finding. |
| [`index-of-definitions/definition-index`](../../content/quantum-observable-universe/index-of-definitions/definition-index.md) | Pure index row (`:85`), name + chapter + Lean decl. `Q`'s definition and its Lean name are unchanged by the fix. |
| [`climax-volume-mass/skein-crossing-asymmetry-prop`](../../content/quantum-observable-universe/climax-volume-mass/skein-crossing-asymmetry-prop.md) | Per-crossing ratio ⇒ no qualifier needed. `δ_Coulomb = q − ½(q+q⁻¹) = ½(q−q⁻¹)` is *exactly consistent* with the corrected split, `½(q+q⁻¹)` being the signed bar-even weight of a positive crossing. **One adjacent sign gloss fixed** (`weight of q⁻¹` → `−q⁻¹`, matching the relation displayed directly below it). |
| [`observations/pair-creation-energy`](../../content/quantum-observable-universe/observations/pair-creation-energy.md) | Ratio is stated **for the electron**, which is `T_{2,3}` all-positive (`m = 0`) — correct in its stated scope. Inherits only the channel label. |
| [`observations/hydrogen-knot-structure`](../../content/quantum-observable-universe/observations/hydrogen-knot-structure.md) | `α = tanh(ln q)/C_geom` uses the per-crossing ratio, and `C_geom` is *defined* by consistency with the primary `α_EM = q⁻¹/([9]_q[10]_q)`. No split restated. |
| [`observations/building-block-knots-table6-data`](../../content/quantum-observable-universe/observations/building-block-knots-table6-data.md), [`appendix-knot-periodic-table/knot-periodic-table`](../../content/quantum-observable-universe/appendix-knot-periodic-table/knot-periodic-table.md) | `𝔈_× = ½(q−q⁻¹) ≈ 0.1045` is exactly the per-crossing bar-odd weight `sinh(ln q)`. Correct; these fix the canonical meaning of `𝔈_×` that `q-energy-terms-and-limits` was made to respect. |

### Out of scope — a numerology collision worth flagging

Three *different* quantities all sit at `≈ 0.104` at `q₀` and are easy to
conflate; none is a defect, but the coincidence is a standing hazard:

- `tanh(ln q₀) ≈ 0.10399` — the per-crossing channel weight ratio.
- `½(q₀ − q₀⁻¹) ≈ 0.10450` — the per-crossing bar-odd weight `𝔈_×`.
- `ln q₀ ≈ 0.10437` — the meridian rapidity
  ([`braids-and-knots/meridian-exceptional-divisor-note.md:1`](../../content/quantum-observable-universe/braids-and-knots/meridian-exceptional-divisor-note.md),
  [`information-theory/q-heat-kernel-computational-fallback.md:17`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-computational-fallback.md)).

The `strangelet-double-beta-interpretation` defect is an instance of exactly
this: a numerical match at three digits was read as a structural identity.

## Lean

One Lean file changed:
[`lean/QOU/Observations/strangelet_crossing_energy.lean`](../../content/quantum-observable-universe/lean/QOU/Observations/strangelet_crossing_energy.lean).
It carried the inverted claim as a **class field**:

```lean
claim_ii_purely_strong_crossing :
  ctx.E_cross = N * ((n₊ + n₋ : ℕ) : ℝ) / 2 * (ctx.q_real + ctx.q_real⁻¹)
```

Because the field is a *hypothesis*, the theorem was not false — it proved the
implication. But the premise it carried was the defective statement, and the
field name asserted "purely strong crossing", so leaving it would put the Lean
in direct conflict with the corrected `.md` (a `proof-statement-integrity`
failure). Renamed to `claim_ii_bar_odd_crossing_energy` with `(q − q⁻¹)`, and
the matching conjunct + projection in the theorem updated.

> **✅ MACHINE-VALIDATED (parent session, 2026-08-08 — supersedes the caveat
> below).** `scripts/lean-verify.sh` on
> `QOU/Observations/strangelet_crossing_energy.lean` → **exit 0, 0 errors**, run
> from the main checkout where the `lake-cache/qou-v4-24-0` oleans were already
> resident (mathlib 6990, Batteries present). Sorry-free on **both** greps —
> naive `grep -c sorry` = 0 and word-bounded
> `grep -cE '(^|[^[:alnum:]_-])sorry([^[:alnum:]_-]|$)'` = 0 — and
> `sorryAx|admit|native_decide` = 0. **`lake build` never run.**
>
> The structural argument below stands and is now corroborated rather than
> load-bearing. Retained because it is the reasoning that made the edit
> defensible before a toolchain was available, and because the failure mode it
> records is real:
>
> **⚠ Original caveat — this Lean edit was NOT machine-validated in the agent's
> worktree.** `lean`-direct was attempted and could not be run: Lean 4.24.0 is
> installed but the worktree had 0 Mathlib oleans, and restoring
> `lake-cache/qou-v4-24-0` **exhausted the disk** (`/` hit 0 MB free) after
> extracting only the `mathlib` package — `Batteries`, `aesop` and the QOU build
> were never written, so `lean` failed at `unknown module prefix 'Batteries'`. A
> complete re-extract needs ~6 GB against 5.5 GB available. CI cannot substitute
> (auto-triggers are disabled repo-wide). **Lesson: a worktree does not inherit
> the main checkout's gitignored `.lake`, and restoring a second copy per
> worktree does not fit on this disk — verify Lean from the main checkout.**
>
> The change is nevertheless safe **by inspection**, and the argument is
> structural rather than a judgement call: the conjunct's proof is the bare
> projection `hc.claim_ii_bar_odd_crossing_energy`, whose type is *syntactically
> identical* to the rewritten conjunct — the same expression was substituted on
> both sides. No tactic reasoning touches it (`refine ⟨_, _, ?_⟩` discharges it
> by projection and leaves only the third conjunct, whose `linarith` proof
> mentions neither `E_cross` nor `q ± q⁻¹`). Elaboration therefore cannot change.
> **A reviewer with a working toolchain should still confirm.**

## Compute

**No compute changed, and none needed to.**
[`computations/coulomb_energy.py`](../../computations/coulomb_energy.py) — the
likeliest carrier — encodes no channel split; it computes charge-symmetric-core
and mirror-binding quantities. A grep of `computations/` for the split and for
the ratio found **no producer or witness encoding the inverted pairing or the
unqualified channel ratio**, so there is nothing to report as a stale witness
and nothing to re-run. No production numerical value changed anywhere in this
branch.

## Open — needs author (beans)

| # | Item | Why it is not an agent call |
|---|---|---|
| 1 | **Relabel the two channels.** Is either the "electromagnetic" one? | The upstream fix explicitly left relabelling to the author. Affects the surviving labels in `crossing-energy-interpretation`, `pair-creation-energy`, `hydrogen-knot-structure`, `skein-crossing-asymmetry-prop` (its title says "Coulomb correction"), and the Lean name `QOU.Braiding.emStrongRatio`. |
| 2 | **`strangelet-crossing-energy` claim 1** derives `Q = 0` by summing quark electric charges in thirds (`+2/3 − 1/3 − 1/3`), but `def:coulomb-charge` gives `Q = ½(n₊ − n₋) ∈ ½ℤ`. Which `Q` is meant? | Both routes reach `0`, so nothing is numerically wrong; but they are different objects and only the author knows which the claim intends. |
| 3 | **`strangelet-crossing-energy` claim 3** writes `𝔈_bind = 8q⁻¹ > 6q⁻¹`, treating negative-crossing contributions as positive binding (`def:crossing-energy` gives `−q⁻¹` each) and not mentioning `n₊`. | The magnitude comparison reaches the right conclusion; the sign/normalisation convention for a "binding component" is an author call. Left untouched. |
| 4 | **`strangelet-double-beta-interpretation`** places the genus-2 sector at `Q = 0` while writing its knots as mirrors (`T_{2,5}^σ` etc., all-negative ⇒ `Q ≠ 0`). | Reconciling the sector charge with the mirror superscripts is physics assignment, not arithmetic. |

## Pre-existing issues noted, deliberately not touched

- `strangelet_crossing_energy.lean` is a **self-assuming projection**: the
  theorem merely projects its class fields (`§3b-cond` item 5). Correcting
  claim ii does not fix that. The honest fix is to carry `Q = ½(n₊−n₋)` and the
  split as *hypotheses* and **derive** the bar-odd form from `Q = 0` — which
  would also make the block genuinely conditional rather than tautological.
  Bean-worthy; out of scope here, and unverifiable without a toolchain.
- `q-energy-terms-and-limits` asserts both `𝔖_q = tr_M(ρ(β))` and
  `𝔖_q = Σ` per-crossing weights. These are different objects. Pre-existing;
  the structure of the block was preserved rather than amplified.

## Verification

| Gate | Result |
|---|---|
| `convention_slip_validate.py --strict` | **RC 0** — 6 pass / 3 fail (all pre-existing known-defect fixtures) / **0 surprises**. Was 4/3/0; the 2 new R1 entries pass. |
| New registry entries | `R1-em-strangelet-q-zero-bar-odd`, `R1-em-qenergy-signed-per-crossing-weights` — both **residual 0**. |
| `run-validate` | 29 issues, **byte-identical to the pre-edit baseline**. No issue added. |
| `check-sidecars.sh` | No un-sidecar'd §7c flags; all 6 listed blocks swept. |
| `qa-sweep` (7 blocks, 96 criteria each) | **0 critical, 0 major, 0 minor** on every block. |
| Render-QA grep battery | Clean on all 7 touched `.md`; battery self-tested against the `-`-in-`$$` hijack, brace imbalance, and `\operatorname`. |
| `lean`-direct | **Not run** — see the Lean section. Disk exhaustion, not a skipped step. |
| Compute | Unchanged; no witness encodes the split. |
