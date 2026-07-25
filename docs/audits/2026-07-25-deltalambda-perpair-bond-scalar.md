# Δ_λ per-pair bond scalar — the graded-dimension two-anchor NO-GO (formalize-first)

**Date:** 2026-07-25 · **Branch:** `claude/deltalambda-perpair-bond-scalar-2026-07-25`
· **PR:** #4300 · **Bean:** (new milestone this session) · **Axis:** per-isotope
binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the ≥4-body magnitude scalar ·
**Tier:** formalize-first structural NO-GO (scope-(b) proved invariant + scope-(a)
comparison). **No fit; no AME inversion; nothing wired.**

Probe: [`computations/deltalambda/deltalambda_graded_two_anchor_nogo_probe.py`](../../computations/deltalambda/deltalambda_graded_two_anchor_nogo_probe.py)
(exit 0, 6/6 assertions, mpmath 60 dps) · Witness:
`deltalambda-graded-two-anchor-nogo.witness.json` · Lean:
[`QOU/MassTheory/JetFiltrationTwoAnchorNoGo.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationTwoAnchorNoGo.lean)
(sorry-free, `lean`-direct exit 0).

## 0. Scout — where the single scalar sits (coordinate, don't duplicate)

The Δ_λ magnitude wall (after the sign front closed via the jet-order valuation,
`PrincipalGradingJetOrder.lean`) is reduced to **one magnitude object**, bracketed
two-sidedly (jet-filtration audit,
[`2026-07-18-deltalambda-jet-filtration-magnitude.md`](2026-07-18-deltalambda-jet-filtration-magnitude.md) §4):

```
sub-extensive  −ln det(I + m(J−I))   ρ_A ≤ C(A,2)   (Lean-capped; too FLAT)
        <   true binding magnitude   <
super-extensive graded dim  W_A(q) = [A]_q! = ∏[k]_q  (Lean-escapes cap; too STEEP)
```

- **Lower side — CLOSED (Lean).** The whole exchange-**determinant**-cumulant family
  is machine-excluded: `SaturationRhoCap.saturation_rho_cap_{three,four}` (`ρ₃ ≤ 3`,
  `ρ₄ ≤ 6`), `IsospinMirrorInvariance` (signed graph wrong-mirror), `B4CumulantBarEven`
  (A=4 det even in `m`, bar-symmetrization a no-op). Strong targets `ρ_strong(3) ≈ 3.81`,
  `ρ_strong(4) ≈ 13.03` exceed the caps for **all** `m` — sorry-free scope-(b) exclusion.
- **Upper side — ESCAPES the cap (Lean).** The **non-determinant** coinvariant graded
  dimension `W_A(q) = ∏_{k=1}^{A}[k]_q` (Poincaré polynomial of the `S_A` coinvariant
  algebra / jet-order filtration) grows factorially:
  `JetFiltrationGradedDimEscape.jet_graded_rho4_ge_twelve` proves
  `ρ_grad(4) = [3]_q·[4]_q ≥ 12 > 6` — the first non-determinant object that can *reach*
  `ρ_4 = 13.03`. But at the fixed substrate `q₀` it **undershoots A=3** (`3.342` vs
  `3.813`, −12.3 %) and **overshoots A=4** (`15.740` vs `13.032`, +20.8 %).

**Sibling coordination.** The covariance-kernel epic **`qou-x631`** is actively on the
Δ_λ front, but on a **different leg**: the super-exponential **partition-index growth
bound** `k(A) = O(log A)` via `Cov_Planch(f^λ, R₄) ≤ 0` (a Kerov-CLT / Biane–Śniady
character-ratio anti-correlation; recent work: A2 polynomial-positivity reduction, even
hook-power moment positivity, A2 pointwise reduction falsified for `n ≥ 29`). That is the
growth of `Δ_λ` **over partitions `λ`**; **this** audit is the per-**isotope** magnitude
`ρ_grad(A) = W_A(q)/W_2(q)` **over nucleon number `A`** — a genuinely distinct object.
No overlap with x631's covariance kernel. The six failed closure ansätze (Frobenius
co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov)
are **not** re-run here; the KL-positivity PROBE-4 prune stays pruned.

**The gap this audit closes.** The workplan W5
([`2026-07-24-binding-mass-workplan-refresh.md`](../coordination/2026-07-24-binding-mass-workplan-refresh.md) §4 item 5,
bean `qou-j5rx`, **todo**) asks: *"Lean-state the invariant any graded-dimension family
must satisfy (escape det cap at A=4 AND amplify at A=3)."* The jet-filtration probe
recorded "one knob cannot do both" only as **Python assertions**. This audit **formalizes
that no-go in Lean**, sorry-free — the distinct-angle deliverable.

## 1. Distinct angle — the single-knob two-anchor rigidity, formalize-first

The graded-dimension object has exactly **one knob**: the substrate value `q`. The
A=3 anchor is under-shot (needs the knob turned up); the A=4 anchor is over-shot (needs
it turned down). The formalizable question: *can the single knob do both?* Three proved
facts say **no**.

### (S) step-lock — `[4]_q ≥ 4` for every `q ≥ 1` (`q`-/AME-independent)

`gradedStep4_ge_four`: `[4]_q − 4 = (q−1)(q² + 2q + 3) ≥ 0` on `q ≥ 1`. The multiplicative
A=3→A=4 graded step is bounded below by its classical value `4` at **every** admissible
substrate value. The isospin/Coulomb-corrected **data** step is
`ρ_strong(4)/ρ_strong(3) = 13.0316/3.8128 ≈ 3.418 < 4`, so
`gradedStep4_gt_data_step` gives `[4]_q > 3.418` for all `q ≥ 1`: **the graded step
overshoots the observed growth at every `q`** — no `q` flattens it. (A `q < 1` would be
needed to hit the data step, and `q < 1` is forbidden — the archimedean substrate has
`q₀ > 1`.)

### (M) single-knob monotonicity — both anchors move the SAME way

`gradedRatio3_mono` and `gradedRatio4_mono`: both `q ↦ [3]_q` and
`q ↦ ρ_grad(4) = [3]_q·[4]_q` are monotone increasing on `[1,∞)`. Turning the knob up to
raise the under-shot A=3 ratio **necessarily raises** the already-over-shot A=4 ratio.
The knob cannot push one up and the other down — the crisp statement of "one knob cannot
do both."

### (N) the two-anchor no-go — reaching A=3 FORCES an A=4 overshoot

`graded_two_anchor_nogo`: for every `q ≥ 1`,

> `[3]_q ≥ ρ_strong(3) = 3.8128  ⟹  ρ_grad(4) = [3]_q·[4]_q > ρ_strong(4) = 13.0316`,

because `[4]_q ≥ 4` (step-lock) gives `[3]_q·[4]_q ≥ 3.8128 · 4 = 15.2512 > 13.0316`.
The no-go margin is a strictly positive `15.2512 − 13.0316 = 2.2196` (dimensionless
ρ-ratio). So **no single parameter-free `q` lands both light-nucleus anchors**. Forward
check at the forced solve: reaching `ρ_grad(3) = 3.8128` needs `q ≈ 1.25`, at which
`ρ_grad(4) ≈ 22.0` (+68.7 %) — the solve is shown only to exhibit the impossibility; it
is **not** wired (selecting `q` from the ratios would be the forbidden 7th fit).

## 2. A second scope-(b) elimination — the SU(4) row-restriction damping is vacuous

The natural physical damping candidate is the **SU(4) supermultiplet** row bound
`ℓ(λ) ≤ 4` (the `[1⁴]`-locality that makes ⁴He doubly-magic). The probe verifies by
enumeration that **every partition of `A ≤ 4` already has `≤ 4` parts**, so the row
restriction removes **no** partition for the light nuclei. Hence the SU(4) locality
**cannot** be the A=3→A=4 damping — it is inert exactly where the damping is needed. A
proved (combinatorial) elimination of one candidate from the W5 survivor list.

## 3. Verdict — HONEST WALL (single-knob graded family cannot close), tighter than before

| item | verdict |
|---|---|
| `[4]_q ≥ 4` step-lock for all `q ≥ 1` | **PROVED** (Lean, scope-(b), AME-independent) |
| both ρ_grad(3), ρ_grad(4) monotone ↑ in `q` (one knob, same direction) | **PROVED** (Lean, scope-(b)) |
| reaching ρ_strong(3) ⇒ overshoot ρ_strong(4) (two-anchor no-go) | **PROVED** (Lean; margin 2.2196) |
| SU(4) row-restriction `ℓ(λ)≤4` as the damping | **ELIMINATED** (vacuous for A≤4) |
| the true Δ_λ magnitude scalar | **STILL OPEN** — needs an `A`-dependent (non-single-knob) damping |

**This is a wall, not a derivation and not a fit.** The single-parameter `q`-scaled
coinvariant graded dimension `[A]_q!` — the upper side of the two-sided bracket — is
**proved unable** to close the two light-nucleus anchors: its per-step growth is q-locked
above the data step, and its single knob moves both anchors the same way. The bracket
does **not** collapse to a point via the `q`-knob. **Consequence for the search (W5):**
any closure must supply a genuinely **`A`-dependent damping** `d(A)` with `d(4)/d(3) < 1`
(damp A=4) while not falling back below the determinant cap (`ρ_A > C(A,2)`), and it must
**not** be a `q`-reparametrization of `[A]_q!` (proved insufficient here) nor the SU(4)
row-restriction (proved vacuous here). Candidate survivor classes to probe next
(formalize-first, per W5): **parabolic / skew quotients of `[A]_q!` whose truncation
level is `A`-locked by a stated principle** (not a fitted knob), or the **Demazure
sub-crystal** damping (workplan: "brackets A=4 but A=3 needs amplification" — now
consistent with (M): a genuinely two-parameter object).

**Anti-fit / anti-laundering (STRICT).** `ρ_strong(3)=3.8128`, `ρ_strong(4)=13.0316` are
DERIVED-ELSEWHERE comparison constants (isospin/Coulomb-corrected AME, #3986/#3990; the
committed jet-filtration witness); they appear only as **bounds** in (N), never inverted
to define a wired quantity. Invariants (S) and (M) are AME-independent. Nothing is wired;
no content block, no tier change, no production edit; nothing canonical. The result
**narrows** the search (scope-(b) exclusion of the single-knob graded family) — it does
not claim a closure.

## 4. Cross-references

- Two-sided bracket + escape (upper side): [`2026-07-18-deltalambda-jet-filtration-magnitude.md`](2026-07-18-deltalambda-jet-filtration-magnitude.md);
  `JetFiltrationGradedDimEscape.lean` (escape, sorry-free).
- Determinant-family cap (lower side): [`2026-07-18-deltalambda-saturation-det-ceiling.md`](2026-07-18-deltalambda-saturation-det-ceiling.md),
  [`2026-07-18-deltalambda-exchange-determinant-family-nogo.md`](2026-07-18-deltalambda-exchange-determinant-family-nogo.md);
  `SaturationRhoCap.lean`, `IsospinMirrorInvariance.lean`, `B4CumulantBarEven.lean`.
- Attack-vector map (per-pair magnitude context): [`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md).
- W5 workplan item + bean: [`2026-07-24-binding-mass-workplan-refresh.md`](../coordination/2026-07-24-binding-mass-workplan-refresh.md) §4.5; bean `qou-j5rx`.
- Sibling epic (distinct leg — partition-index growth): covariance kernel `qou-x631`,
  [`2026-07-18-deltalambda-covariance-kernel-frontier.md`](2026-07-18-deltalambda-covariance-kernel-frontier.md).
- Gate reversal (open for all, derivation routes): [`2026-07-13-delta-lambda-gate-open-for-all.md`](2026-07-13-delta-lambda-gate-open-for-all.md).

**Render-QA note.** The `folio-assistant` pipeline was not invoked in this session; the
manual preflight grep battery was run (balanced `$`/`$$`/braces, no `\operatorname`, no
list-marker lines inside display math, align-family fenced) — clean, but this doc was
**not machine-render-validated**.
