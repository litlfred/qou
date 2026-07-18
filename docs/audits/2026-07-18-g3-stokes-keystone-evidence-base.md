# G3 monodromy / Stokes-constant keystone — evidence base + formalize-first target

**Date:** 2026-07-18
**Bean:** `qou-vr3q` (deep-dive 1 of the alien-calculus ↔ Habiro review, milestone `qou-89f9`)
**Branch:** `claude/alien-calculus-habiro-50257v`
**Status:** AUDIT (evidence synthesis + framing correction). No derivation, no
number claimed, no wiring.

## 0. Framing correction (READ FIRST — recurring conflation)

There are **two distinct `A_ω` objects**; earlier chat in this session conflated
them:

| | EVEN face | ODD face = **the G3 keystone** |
|---|---|---|
| object | binding period `a_D` (mass) | Q_β / Φ_b decay ladder |
| `A_ω` | `4√2·e^{−3/8} ≈ 3.8884` **measured** | **un-measured** |
| regime | q=1, EGF `e^{x+x²/2}` **entire** ⇒ **co-equational** (coefficient-plane); bar-even, stationary at q=1 to O((q−1)²) | irregular q-difference connection; **categorical Stokes/monodromy datum**, not a resummation constant |
| source | `computations/lever1_bridge_alien_datum_probe.py` + `lever1-bridge-alien-datum.witness.json` | `docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md` §2 |

**The measured 3.8884 is NOT the keystone.** It only demonstrates the
derive-then-verify template and confirms the odd part vanishes at q=1 (bar-even).

## 1. Exact open statement of G3

From `2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md` §2:

> **G3 — the argument-identification / monodromy datum `z(q₀) → S`.** No
> `FaddeevPhi` argument has been exhibited whose archimedean evaluation
> reproduces the anchor targets `S(muon) = +0.00968298`,
> `S(proton) = −0.03945936`. The fibre→observable passage is **not analytic
> continuation** but a **categorical Stokes / monodromy datum** (an irregular
> q-difference connection) — a **monodromy** (Stokes automorphism), not a
> resummation *constant*.

Bridge equation defining it: `Δ_ω f̃ = A_ω · ∂f̃/∂z`; leading singularity at
`ω ≈ Vol(4₁)/π ≈ 0.646` (same Borel action as the even-face κ-tower, PR #3683).

## 2. The derivation target (not a fit): the exact integer 3

The anti-fit route requires `A_ω` to **emerge as an integer count**
(Donaldson–Thomas / 3d-index), not be inverted from the anchors. Already in
hand, exact:

- `computations/probes/qbeta_g3_ggm_stokes_41.py` — implements the GGM (2012.00062)
  4₁ Stokes data: `S⁰ = [[1,0],[−3,1]]`, singularity at `ι = ±Vol(4₁)/π`, integer
  Stokes constant **3**, descendant tower `S⁺₁₁ = 1 − 8q − 9q² + …`. Internally
  certified exact (det W_m = 2; q-difference eq 49; eq-59a sandwich). The
  identification of this integer with the corpus `A_ω` normalization
  (`Im 𝔙 → N_odd`) is the **explicitly-not-claimed** remaining bridge.
- Trace-field hypothesis (bean `qou-t3jv`,
  `computations/qbeta/qbeta_aomega_stokes3_tracefield_probe.py`): Stokes `−3`
  = `disc(ℚ(√−3)) = −3`, unifying even (ℚ(√3)) and odd (ℚ(√−3)) channels via
  `√−3 = i√3 ∈ ℚ(ζ₁₂)`. **H1 hypothesis, NOT verified** — "matching two −3's is
  not a derivation."

Literature already cited (`content/schema/references.ts`):
`garoufalidis-gu-marino2021/2023peacock` (Stokes constants = DT integers),
`dimofte-gaiotto-gukov2013` + `garoufalidis-hodgson-rubinstein-segerman2015`
(3d-index / m004 flux-sum), `fantini-rella2024` (modular resurgent ⇒ Stokes =
L-function coefficients).

**One prior probe already tested the L-function/integer comparison numerically**
(`qbeta_modular_resurgence_stokes_probe.py`, Option D): action consistent within
spread with Vol(4₁)/π (5.2%, not identified); β=3/2 modular weight **fails**;
Stokes not identifiable at 7 rungs (below the 1/210 entropy bar); L-tower
**blocked**. Verdict: the derivation route is the **exact GGM state-integral /
3d-index algebra**, not float extraction from finitely many rungs.

## 3. Formalize-first target (the cleanest prune)

The corpus already carries the rigidity scaffold, sorry-free, with **one** honest
open input:

- `QOU/QBeta/CyclicDilogPentagon.lean:192` `faddeevPhi_unique_of_pentagon`
  (sorry-free) and `QOU/QBeta/MonodromyDatumRigidity.lean:80`
  `monodromy_datum_rigidity` (sorry-free): **every scale-invariant readout of any
  FaddeevPhi solution is the same** ⇒ `A_ω` "carries no fitting freedom."
- The **single open input** is `PentagonRigidity.uniqueUpToScalar`
  (`CyclicDilogPentagon.lean:174–181`, **no instance**): the Faddeev–Volkov
  "doubly-periodic ⇒ constant" **Liouville step, not in Mathlib**.

> **Formalize-first target:** prove `PentagonRigidity` (the Liouville step). This
> discharges the uniqueness leg and converts G3 from "find a function `z(q₀)→S`"
> to "**verify the pentagon pins** the already-proved inversion / unitarity /
> self-duality bundle." It is the structural prune: it does not compute `A_ω`,
> but it proves `A_ω` is *forced* (zero fitting freedom), so the only remaining
> content is the integer identification of §2 — turning a search over functions
> into a check of one integer.

This is the honest division: the Liouville step is a genuine multi-week Mathlib
gap (do **not** axiomatize it to "close" G3 — that is the §Axiomatization-is-not-
a-proof trap); the integer-3 identification is the physics content and stays a
falsifiable open step.

## 4. Status corrections captured (for currency)

- `2026-07-13-alien-calculus-surreal-integration-review.md` §2 calls
  `BorelWatsonUniqueness.lean` "1 sorry" — **stale**; current file is sorry-free
  (`watson_uniqueness_rhp:97`), residual is the `z↦1/z` sector-transport assembly,
  not a `sorry`. The only live `sorry` in the QBeta tree is
  `ToroidalHarmonicsBasis.lean:114` (unrelated to G3).
- "k=21 singularity unresolved" is now **k=31 confirmed structurally unresolvable
  by fixed-order Borel–Leroy** (`qbeta-dladder-extension-singularity.witness.json`,
  2026-07-17: dlog-Padé vs root-test gap persists at 0.172; q-Gevrey drift, no
  single Gevrey index) — needs the Φ_b state-integral / GGM route, consistent
  with §2/§3.

## 5. Discipline

Corpus-grep: this synthesizes existing audits (`phib…gap-audit`,
`alien-calculus-surreal-integration-review` Option D, `dladder-*`) — no new
open-item declaration, no refutation. The even/odd `A_ω` correction (§0) is the
one durable fix. Anti-laundering: the §3 target proves *rigidity*, not the datum;
the integer-3 identification (§2) stays explicitly open and falsifiable.

## 6. Update (same day) — dual period LANDED; open input sharpened (NOT closed)

Formalize-first advance on the §3 target, honest scope. The rigidity scaffold
proved only *one* period of the inter-solution ambiguity (`ratio_ib_periodic`,
shift `ib`). Landed the **second** period, `lean`-direct **exit 0**:
- `QOU/QBeta/CyclicDilogPentagon.lean` — new `phi_binv_quasiperiod` (full `i/b`
  shift from `shift_binv`, guarded off the dual pole lattice) and
  `ratio_ibinv_periodic` (the ratio `Φ₁/Φ₂` is `i/b`-invariant). With
  `ratio_ib_periodic` this **proves the ambiguity is doubly periodic** for the
  lattice `⟨ib, i/b⟩`.

**What this does NOT do (anti-laundering, explicit).** It does **not** prove
`PentagonRigidity.uniqueUpToScalar`. The remaining gap is now *precisely* named:
"doubly-periodic ⇒ constant" (Liouville for elliptic functions), which in
addition needs **holomorphicity/continuity of the ratio** — NOT carried by the
`FaddeevPhi` conjecture-class (it axiomatizes only the two difference equations;
the contour-integral `Φ_b` and its analyticity are the open input) — and
Mathlib's absent elliptic-function boundedness API. `uniqueUpToScalar` stays an
honest open hypothesis with **no instance**. The advance is that the search
around it is now closed: the only missing piece is one classical theorem plus a
holomorphicity endowment, not a vague "Faddeev–Volkov rigidity."

## 7. Update — the elliptic-Liouville step FORMALIZED (standalone), sorry-free

The classical theorem named in §6 as the remaining gap is now landed and
machine-checked, `lean`-direct **exit 0**:
[`QOU/Common/EllipticLiouville.lean`](../../content/quantum-observable-universe/lean/QOU/Common/EllipticLiouville.lean)
— `doublyPeriodic_entire_const`: an entire `f : ℂ → ℂ` with two ℝ-spanning
periods is constant (fundamental-box compactness ⇒ bounded via lattice
periodicity ⇒ Mathlib Liouville). Standalone complex analysis, **no** `FaddeevPhi`
dependency.

**Still open (anti-laundering, explicit):** this does NOT discharge
`uniqueUpToScalar`. Two hypotheses remain, both open input: (i) endow `FaddeevPhi`
with holomorphicity of `Φ_b` (the class axiomatizes only the difference
equations); (ii) prove the ratio `Φ₁/Φ₂` of two solutions is entire (poles
cancel). Given (i)+(ii), `ratio_ib_periodic` + `ratio_ibinv_periodic` +
`doublyPeriodic_entire_const` compose to force the ratio constant. The elliptic-
Liouville *excuse* is removed; the holomorphicity endowment is the surviving gap.

## 8. Update — the endowment SCOPED and machine-checked (reduction landed)

`QOU/QBeta/FaddeevRigidityReduction.lean` — `uniqueUpToScalar_of_ratio_entire`,
`lean`-direct **exit 0**. It proves `∃ c, Ψ = c·Φ` from **exactly three explicit
hypotheses**, deriving the `ib`-periodicity from nowhere-zero. So the entire G3
rigidity leg now rests on three named, ranked inputs:

| input | what it is | difficulty |
|---|---|---|
| `hratio` — `Ψ/Φ` entire | **THE endowment.** NOT "`Φ_b` entire" (false — `Φ_b` is meromorphic, poles on the `1/b`-lattice). Decomposes into (i) `Φ_b` holomorphic/meromorphic (open — `FaddeevPhi` axiomatizes only the difference equations) + (ii) **divisor cancellation**: two solutions share zeros+poles ⇒ ratio has only removable singularities ⇒ entire, nowhere-zero. | hard (real math) |
| `hspan` — `⟨ib, i/b⟩` ℝ-spans `ℂ` | non-degeneracy `b² ∉ ℝ`; the substrate branch `arg b = π/4`. **Fails for real `b`** (both periods imaginary ⇒ lattice collapses) — a genuine constraint, not a nuisance. | easy (algebraic; provable/citable) |
| `hibinv` — `i/b`-periodicity everywhere | derivable off the dual pole lattice from `ratio_ibinv_periodic`; extending across that discrete set needs the identity theorem. | medium |

**Net:** the endowment scope is `hratio`, and its hard half is (ii) divisor
cancellation of two `Φ_b` solutions — a meromorphic-divisor argument (Mathlib's
meromorphic API is thin). `hspan` and `hibinv` are lighter and separable. Nothing
is axiomatized; the reduction is a proved implication, so any future proof of the
three inputs closes `uniqueUpToScalar` by direct application.

## 9. Update (prepare-merge integration) — converged with upstream elliptic-Liouville

The reuse-and-simplify pass against the 42 upstream commits caught a **parallel
duplicate**: `origin/main` landed `QOU/MathlibExt/DoublyPeriodicLiouville.lean`
(`const_of_doublyPeriodic` + `ratio_const_of_doublyPeriodic`, sorry-free) — the
same elliptic-Liouville step this branch proved as `EllipticLiouville.lean`.
Per the discipline, the branch's duplicate was **deleted** and its work
re-pointed to the upstream lemma; two independent proofs of the same Liouville
step are a confirmation, not waste (supersedes §7's `EllipticLiouville.lean`
reference).

Net after convergence: `QOU/QBeta/FaddeevRigidityReduction.lean`
(`uniqueUpToScalar_of_entire`, `lean`-direct exit 0) now **consumes** upstream
`ratio_const_of_doublyPeriodic`, retaining only the branch's novel
FaddeevPhi-specific content — the compact `ib`-period of the ratio is **derived**
from nowhere-zero (via `phi_b_quasiperiod`), not assumed, so a caller supplies
only the dual `i/b`-period, entireness, and the basis. The §8 open-input table
is unchanged (hratio / hspan / hibinv).

## 10. Update — `hspan` CLOSED (the easy input of §8), rigidity now on 2 inputs

The §8 `hspan` input (lattice `⟨ib, i/b⟩` ℝ-spans ℂ) is now proved, `lean`-direct
**exit 0**: `QOU/QBeta/PeriodLatticeBasis.lean` — `exists_period_basis`:
`(b^2).im ≠ 0 ⇒ ∃` basis with entries `I·b, I/b` (via `periods_linearIndependent`
+ `finrank ℝ ℂ = 2`). `FaddeevRigidityReduction.uniqueUpToScalar_of_entire_of_sq_not_real`
now consumes it, so Faddeev–Volkov rigidity reduces to **two** open inputs:

| input | status |
|---|---|
| `hspan` — lattice non-degenerate | **CLOSED** (`exists_period_basis`, exit 0); needs only the scalar `b² ∉ ℝ` (substrate `arg b = π/4`; fails real `b`) |
| `hibinv` — `i/b`-period everywhere | open (identity theorem off dual lattice; bean `qou-q95i`) |
| `hratio`/entireness | open — the endowment: `Φ_b` holomorphic + divisor cancellation (bean `qou-2cvs`) |

Physical content preserved: the non-degeneracy `b² ∉ ℝ` is exactly the substrate
branch requirement — rigidity provably **fails** for real `b`, where both periods
are imaginary and the lattice collapses.
