# Is the A=3 amplitude `E` a gauge-invariant of the Birkhoff connection matrix? A WELL-POSEDNESS result

**Date:** 2026-08-08 · **Bean:** `qou-wiub` (A=3 magnitude keystone), `qou-jqof` ·
**Branch:** `claude/deltalambda-birkhoff-wellposed-2026-08-08` ·
**Tier:** formalize-first (Lean, sorry-free, `lean`-direct exit 0) ·
**Scope:** well-posedness — MIXED verdict (a)-gauge-invariant-functional + (b)-single-entry-ill-posed; nothing fitted, nothing wired, `q₀`-derivation not routed through.
**Lean:** [`QOU/QBeta/BirkhoffAmplitudeWellPosed.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BirkhoffAmplitudeWellPosed.lean).

## The question

Two merged results this week pinned the A=3 anti-self-adjoint amplitude `E := C + σ B` — the
single free real DOF carrying the observed lift `r* = μ₃/c₃ ≈ 1.585`
(`A3AntiSelfAdjointLift`, `amplitude_surjective`/`amplitude_injective`/`amplitude_nonzero`) —
to the GLOBAL `0↔∞` Birkhoff connection matrix `P = (X^∞)⁻¹ X^0` of C1, the DM q-cubic carrier
(`StokesAmplitudeE` #4811 walled the *local* Stokes route; `E`'s value lives in the *global*
matrix). This is the red-team / well-posedness mirror of the μ₃-target-robustness audits
(`2026-08-01-mu3-target-frame-robustness.md`): **before anyone reads a value off `P`, is `E` a
single entry of `P`, or does the amplitude require the FULL monodromy representation — a
gauge-dependent combination?**

## The residual gauge (cited, not a fit)

By `QOU.MathlibExt.QCharacter`, the canonical local solutions are built from q-characters
`e_{q,c}`, and a q-character is unique **only up to a `q`-invariant (elliptic / theta) unit**
(`IsQChar.ratio_qInvariant`). Normalising the two local solution bases is therefore a residual
**gauge freedom**: `X^{(0)} ↦ X^{(0)} D_0`, `X^{(∞)} ↦ X^{(∞)} D_∞` with `D_0, D_∞` q-invariant
diagonal, under which

  `P ↦ D_∞⁻¹ P D_0`,   entrywise   `P_{ij} ↦ (d_∞,i)⁻¹ P_{ij} (d_0,j)`.

C1 is rank 2 (exponents `λ₊, λ₋`), so `P` is `2×2`.

## Verdict — MIXED, both branches proved sorry-free

| Assertion | Lean | Disposition |
|---|---|---|
| The cross-ratio `crossRatio P := P₀₁·P₁₀/(P₀₀·P₁₁)` is gauge-invariant (frame-free) | `crossRatio_gauge_invariant` | **proved (a)** |
| A single off-diagonal entry carries a full elliptic-unit gauge freedom (any `u·P₀₁` reachable) | `entry_gauge_orbit_surjective` | **proved (b)** |
| A nontrivial gauge genuinely moves a single entry (so it is NOT invariant) | `entry_not_gauge_invariant` | **proved (b)** |
| The gauge fixes all four entries iff it is a global scale ⇒ stabiliser `≅ K^×`, so `4−3=1` invariant | `gauge_fixes_all_iff` | **proved (dimension count)** |
| `E` = the gauge-invariant cross-ratio of the (open) global `P`, `E ≠ 0` | `AmplitudeIsGaugeInvariantCrossRatio` | **OPEN — §3b carrier, NO instance** |

**(a) There IS a specific frame-free functional — the cross-ratio.** `crossRatio P` is invariant
under the full residual gauge (`crossRatio_gauge_invariant`: the four gauge units cancel between
numerator and denominator). It is essentially the **unique** invariant: the gauge group `(K^×)⁴`
fixes a generic `P` only on its 1-parameter global-scale subgroup (`gauge_fixes_all_iff` ⇒
stabiliser `≅ K^×`), leaving `4 − 3 = 1` independent invariant on the four entries. **This is the
well-posed target the sibling must compute.**

**(b) A single entry is NOT gauge-invariant.** Any entry `P₀₁` is defined only up to
multiplication by an arbitrary `q`-invariant (elliptic) unit `u = (d_∞,0)⁻¹ d_0,1`
(`entry_gauge_orbit_surjective`: every `u·P₀₁` reachable; `entry_not_gauge_invariant`: a
nontrivial gauge changes it). So reading `E` off a single entry is **ill-posed** — it needs an
extra normalisation datum to pin the gauge. The residual freedom is the full multiplicative group
of q-invariant units (the two diagonal gauges `D_0, D_∞` modulo their common scale: `2·2 − 1 = 3`
scalar gauges, of which a single entry sees the quotient `1`-parameter elliptic unit as pure
ambiguity).

## Consequence for the sibling's construction

`E` is a physical amplitude: the A=3 mass lift `r*` is a frame-free observable
(`A3AntiSelfAdjointLift.amplitude_injective` makes it a well-defined function of the even-face
factor). So whatever functional of `P` supplies `E` must be gauge-invariant. By (b) it **cannot**
be a single entry; by (a) + the uniqueness count it must be the **cross-ratio**. The sibling
building `BirkhoffAmplitudeE.lean` should therefore target `crossRatio(P)`, not a matrix element.
This is recorded as the open §3b dependent conjecture `AmplitudeIsGaugeInvariantCrossRatio`
(`E = crossRatio P ∧ E ≠ 0`), **no instance** — building `P` and evaluating its cross-ratio is
the open successor; *choosing* the cross-ratio to hit `r*` (`amplitude_surjective`) would be the
forbidden fit and is not done.

**Consistency check for the sibling (not proved here).** `E` is bar-odd
(`DTIndexAmplitudeE.amplitude_barOdd`); therefore the concrete `crossRatio(P)` the sibling builds
must be bar-odd under `σ: q ↦ q⁻¹`. This constrains which entry-pairing realises the cross-ratio.
Not proved here — no concrete `σ` acts on `P`'s entries until `P` is constructed.

## Anti-laundering / honesty ledger

- **No fit.** `E` is never solved from `r*`/`μ₃`/`c₃`; the surjectivity witness (b) is exhibited
  precisely to show that *pinning* a single entry is the forbidden gauge-choice.
- **No axiomatized conclusion.** `AmplitudeIsGaugeInvariantCrossRatio` carries genuine content
  (`E` = a specific frame-free functional of the open `P` + `E ≠ 0`) and has **no instance**.
- **`q₀`-derivation not routed through** (the permanent gate respected).
- **Formalize-first, machine-verified** (`lean`-direct exit 0; sorry-free; deps only
  `Mathlib.Tactic`).
- **Distinct angle from the sibling.** They own `BirkhoffAmplitudeE.lean` (construct `P`); this
  file owns `BirkhoffAmplitudeWellPosed.lean` (what of `P` is frame-free) — parallel, no file
  overlap.

## Cross-references

- Lean (new): [`BirkhoffAmplitudeWellPosed.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BirkhoffAmplitudeWellPosed.lean).
- Amplitude bracket: [`A3AntiSelfAdjointLift.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3AntiSelfAdjointLift.lean); local-Stokes wall [`StokesAmplitudeE.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesAmplitudeE.lean).
- Gauge structure: [`QCharacter.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QCharacter.lean) (`IsQChar.ratio_qInvariant`).
- Birkhoff recipe: [`2026-08-01-branch-selection-birkhoff-connection-matrix.md`](2026-08-01-branch-selection-birkhoff-connection-matrix.md).
- Frame-free discipline mirrored: [`2026-08-01-mu3-target-frame-robustness.md`](2026-08-01-mu3-target-frame-robustness.md).
- Ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md).
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Strict Lean Discipline"; §"Before declaring refuted".

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (Birkhoff connection matrix, q-invariant normalisation gauge)
