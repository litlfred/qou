# Devil's-advocate audit — Wave 12 (predicted-spectra Mathlib-gap + information-theory)

**Watcher:** [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
**Date:** 2026-06-24 · **Model:** claude-opus-4-8 · L1–L4 lenses + adjudicator.

> ## ✅ Resolution status (2026-06-30) — this doc is now a historical record
>
> **Every wave-12 finding below was independently confirmed and fixed on `main`**
> by other agents (the `2ti7` content-sibling-orphan swarm + the "legit-bucket
> re-verification" pass) in the days after this audit. Two of the fixes landed
> *identically* to the fixes this session prototyped — the strongest possible
> confirmation the findings were real:
>
> | Block | Fixed on main by | Note |
> |-------|------------------|------|
> | `bring-residue-resolvent` | `4905b74c` decide→norm_num | identical to the audit's prototype fix |
> | `binding-alpha-shift-extension` | `d918f34f` Prop→data class + doc-comment + subtype coercion | same 3 fixes |
> | `bloch-group-quotient-construction` | `5b9c312f` 6 errors → GREEN sorry-free | the exact 6 errors found here |
> | `cl2-pentagon-and-faddeev-partial` | `3decb9b5` "13 mislabeled defects" | fixed |
> | `upstream-mathlib-additions` | `3decb9b5` | fixed |
>
> This PR therefore carries **only this audit record** — the corresponding
> compile-fixes and `da-*` sidecar splices were dropped as superseded by main.

---

Wave 12 audited the remaining proposition-kind Bucket-C1 blocks in `predicted-spectra/`
(the "upstream-Mathlib-gap-closure" cluster) plus `information-theory/`. **Every agent did
live `lean`-direct compilation** (oleans restored, Mathlib `ring` control confirmed EXIT 0
first), which is what the C1 token-grep checkers cannot do — and it changed three verdicts.

## Results (5 blocks)

| Block | Verdict | Strongest objection (as found 2026-06-24) |
|-------|---------|---------------------|
| `upstream-mathlib-additions` | 🔴 open | **Non-compiling — `sorry` via compile-recovery.** Tactic-grep clean, but `Complex.abs` (:63), `pow_le_one` (:202, renamed `pow_le_one₀` in v4.24.0), `Real.summable_one_div_nat_rpow` (:166) are unknown → error-recovery **injects `sorry`**, surfaced only by `#print axioms` (`sorryAx` on `blochWigner_zero` + `complexLiTwo_summable_on_unit_disk`). Labeled "three additions, each sorry-free". Plus two `: True := trivial` decls. |
| `bloch-group-quotient-construction` | 🔴 open | **Non-compiling** (EXIT 1, 6 errors): broken `Eq.symm` (:119), `ring failed` (:194), missing `noncomputable` (:289/:293), `unsolved goals`+`introN failed` in the headline `quot_universal_property` (:317/:321). `validation:not_checked`. "Closes gap (1)" vacuous at the class level (`HasBlochGroup` fields all `:True`, `:= trivial`). |
| `cl2-pentagon-and-faddeev-partial` | 🔴 open | **Non-compiling** (EXIT 1): the ref target + the whole Faddeev half fail (`partialProductLocal`/`LiTwo`/`faddeev_limit_at_zero` unresolved). Labeled "Lean theorems (sorry-free)"; plus a `def … : True := trivial` at :86. |
| `vdw-pskew-isolation` | 🔴 open | **Cross-block definitional contradiction** (compiles clean): `.md:18` asserts vdW **is** the bar-odd *discarded antisymmetric* channel, but its own cited `def:van-der-waals-hopf-channel.md:9` defines vdW as the *symmetric e₊ retained* block. No corpus reconciliation; the Lean proves only an inert free-variable identity. |
| `torus-knot-delta-q-writhe` | 🟢 clean | False-positive C1: compiles EXIT 0, clean axioms (no `sorryAx`); a 2-line `rw` proof. The flag traced to **hallucinated `qa-agent-drain` rows**. |

## Integrity re-verification (the wave's most important check)

The two compile-failures merged in #2688 (`binding-alpha-shift`, `bring-residue`) and the two
new ones (`cl2`, `bloch`) were **re-compiled against current main** at audit time — all 4
still failed with identical defects, confirming the "open / non-compiling" findings were not
stale-wrong. (All have since been fixed — see the resolution banner.)

## Highlights

- **A coherent defect class** — Lean files mislabeled `proved`/`sorry-free` that did not
  compile, concentrated in the **"Mathlib-gap-closure" blocks**, all **orphan siblings
  outside the QOU import graph** (`proof-build-green:n/a`), so `lake build QOU` never surfaced
  them. This is exactly the class the `2ti7` swarm later swept corpus-wide.

- **`qa-agent-drain` (2026-06-22) is unreliable in BOTH directions** — the wave's key infra
  finding. On `torus-knot`/`cl2`/`bloch`/`vdw-pskew` it **invented false** `sorryAx`/"sorry-stub"
  rows (false positives, the source of those C1 flags); on `upstream-mathlib` (qa.json:1163) it
  **falsely "refreshed" a correct sorry-flag to sorry-free** (false negative). A checker
  trusting these rows mis-triages either way; only per-block lens adjudication with real
  compilation is reliable on the C1 axis.

- **A new sorry-detection-evading variant**: `upstream-mathlib` had **no tactic `sorry`
  token** yet was `sorryAx`-backed because Lean inserts `sorry` when recovering from
  `unknownIdentifier`. Token-grep `proof-no-bare-sorries` returns `pass`; only `#print axioms`
  exposes it.

- **`vdw-pskew` is the wave's only non-mechanical open** — a genuine *scientific-content*
  contradiction (which Wedderburn channel "van der Waals" denotes), correctly scoped `limited`
  (the algebra and the `no-fit` label are both sound; only the physical identification
  conflicts across three mutually-citing blocks).

## Running tally (waves 1–12, 59 blocks)

**30 open · 18 survivable · 11 clean.** (Waves 1–11: 26/18/10 over 54 — merged in #2688;
wave 12: 4/0/1 over 5.) The audit's central deliverable — surfacing the non-compiling
mislabeled-Lean cluster — was realised: the other-agent swarms confirmed and fixed every
compile-failure on main, with two fixes landing identically to this session's prototypes.
