# Does the GS jet-order valuation FORCE single-degree selection? (NO — degree-blindness, sharply bounded)

**Date:** 2026-08-02 · **Epic:** `qou-r2nh` · **Bean:** `qou-71ma` ·
**Branch:** `claude/deltalambda-jetorder-degree-selection-2026-08-01` · **PR #4574** ·
**Tier:** derivation / formalize-first (Lean, sorry-free) ·
**Scope:** (a) LIMITATIVE throughout; nothing fitted; nothing wired; no anchor inverted; L2 unchanged.

- Lean: [`QOU/BraidsAndKnots/DeltaLambdaJetOrderDegreeSelection.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaJetOrderDegreeSelection.lean) — sorry-free.
- Builds only on [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean) (`nStat`, `dim`, `deltaSign`, `deltaLambda`, `deltaSign_eq_nStat_parity`) — all on `main`.
- Companion (ungraded side): PR #4570 [`2026-08-02-deltalambda-sdp-topdegree-projection.md`](2026-08-02-deltalambda-sdp-topdegree-projection.md) (`qou-nmpr`).
- Direct parents: PR #4559 (`qou-ylot`, moduli under-determined); PR #4553 (single-degree `dtEuler` object).

## The crux (the sole remaining place a substrate-derivation could live)

Three independent directions converged on ONE question after two routes were proved dead:

- **#4553** (merged): `Δ_λ = (-1)^{n(λ)}·dim V_λ = DT(𝓑_λ)`. But the single-degree
  concentration `H^{top}(𝓑_λ) = V_λ` is **input by definition**
  (`gradedDim k := if k = nStat then dim else 0`), justified by the classical
  Springer correspondence — not forced from the drivers.
- **#4559** (`qou-ylot`): matching `Δ_λ` as a Behrend-signed DT **count**
  under-determines the Springer moduli (pins only parity mod 2 + count `dim V_λ`).
  **Count route dead.**
- **#4570** (`qou-nmpr`): the confinement SDP / canonical `T_w` / `tr_M` are
  functionals of the **ungraded** Wedderburn dim `dim V_λ` alone (they factor
  through `⊕_λ End(V_λ)`; no cohomological-degree variable), so they cannot force
  the top-degree object — `sdp_cannot_force_top_degree`. **SDP route dead.** Its
  audit named the precise next obstruction:

  > whether the a-function = GS jet-order valuation that already supplies the grade
  > VALUE `n(λ)` can be promoted to SELECT the single graded degree. That map, not
  > the SDP, is where a substrate-derivation must now be attempted.

**THE question (`qou-71ma`): does the GS jet-order valuation FORCE the single-degree
selection, or only supply the grade VALUE `n(λ)`?**

## Corpus / sibling state (grep + coordinate)

- **What the jet-order valuation IS (fixed by the corpus).** Per
  [`2026-07-11-deltalambda-grho-jet-order-derivation.md`](2026-07-11-deltalambda-grho-jet-order-derivation.md)
  and [`PrincipalGradingJetOrder.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PrincipalGradingJetOrder.lean),
  the GS jet-order valuation is the **classical fake-degree valuation**

  > `n(λ) = min_{T ∈ SYT(λ)} maj(T)` = the q-adic VALUATION (lowest term) of the
  > fake-degree polynomial `f_λ(q) = Σ_T q^{maj T}` (Macdonald I.5; Steinberg /
  > Lusztig),

  i.e. the **lowest jet-order at which `V_λ` enters** the length-graded regular
  representation. It is a **valuation** — a single bottom-grade number — and its
  parity `(-1)^{n(λ)}` is the (already-derived, sorry-free `deltaSign_eq_nStat_parity`)
  chirality sign. `deltaValueRing = (-1)^{n(λ)}·dim` in `PrincipalGradingJetOrder.lean`
  already **bakes in** the concentration (bottom-grade parity × full dim); the
  file's own note (line ~157) attributes the top-degree projection to the
  audit/witness (classical Springer input), NOT a machine-forced step.
- **No existing artifact claims the valuation FORCES concentration.** Corpus survey
  (Springer / fake-degree / coinvariant / jet-order / top-cohomology paths across
  `content/`, `docs/`, `computations/`): the single-degree concentration is
  everywhere imported as the **classical Springer fact** (`V_λ` = top cohomology of
  `𝓑_λ`, cited Springer 1978 in `DeltaLambdaDTIndex.lean`), never derived from the
  valuation. The explicit **negative** ("the valuation does not force it") is novel.
  Accepted precedent for the shape: `AtomicityJetIndependence.lean` (an
  "X is independent of the jet-order axioms" Lean-proved honest negative).
- **Distinct from the open `DeltaLambdaDTRealization` conjecture.** That primary
  conjecture (content-bearing, no instance;
  [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md))
  asks whether the substrate forces the DT **moduli `𝓑_λ`** (its dimension + Behrend
  count) rather than reading `(n(λ), dim V_λ)` off after the fact — a *different*
  leg. This audit answers a sharper, orthogonal sub-question: even granting `n(λ)`
  as the jet-order valuation, that valuation does not force the single-degree
  *concentration*.
- **Sibling coordination.** Distinct-angle intent posted on **#4570** (companion,
  `qou-nmpr`) and **#4559** (parent, `qou-ylot`), each naming this valuation angle.
  **#4554** (`A_ω=3`, `qou-qnnq`) is merged and independently reached
  "structurally-open"; this converges by a fourth direction. Forward extension:
  #4558 (general-`n` DT lift).

## The test — result: NO, sharply bounded (formalize-first, sorry-free)

A valuation reads only the **bottom** grade; it is manifestly degree-blind above
it. Formalize the obstruction at the `n = 5` anchor by exhibiting, for every block,
two graded objects that AGREE on everything the jet-order valuation + Wedderburn
data can read, yet differ in signed Euler characteristic:

- `G_λ = singleCoeffs` — `dim V_λ` concentrated in the single degree `n(λ)`;
- `H_λ = fakeCoeffs`   — the honest jet-order / coinvariant graded object (graded
  dims = coefficients of `f_λ(q)`).

| lemma | statement |
|---|---|
| `single_valuation_eq_nStat` / `fake_valuation_eq_nStat` | both objects share the jet-order VALUATION `n(λ)` |
| `singleTotalDim_eq_dim` / `fakeTotalDim_eq_dim` | both share the ungraded Wedderburn dim `dim V_λ` (`= f_λ(1)`) |
| `fakeCoeff_at_valuation_eq_one` | **THE SHARP MECHANISM** — at grade `n(λ)`, `H_λ` carries coefficient **1** (monic leading term of `f_λ(q)`), NOT `dim V_λ` |
| `singleCoeff_at_valuation_eq_dim` | `G_λ` carries `dim V_λ` at grade `n(λ)` |
| `single_gradedEuler_eq_deltaLambda` | `χ(G_λ) = (-1)^{n(λ)}·dim V_λ = Δ_λ` |
| `fake_gradedEuler_ne_deltaLambda` | `χ(H_λ) = f_λ(-1) ≠ Δ_λ` for every `dim V_λ > 1` block |
| **`jetorder_valuation_cannot_force_single_degree`** | **THE CRUX** — `G_λ`, `H_λ` share BOTH the valuation `n(λ)` AND the ungraded dim, yet differ in signed Euler char; only `G_λ = Δ_λ` |
| `valuation_and_totalDim_do_not_determine_gradedEuler` | degree-blindness is **generic** (`[d+2]` vs `[d+1,1]`: same valuation, same total, different Euler char) — not an `n=5` artifact |

### Fake-degree data at `n = 5` (coefficient at the valuation grade is always `1`)

`f_λ(q) = q^{n(λ)}·[5]_q!/∏_{cell}[h]_q`; its leading term at `q^{n(λ)}` is monic.

| λ | `n(λ)` | `dim V_λ` | `f_λ(q)` | coeff of `H_λ` at `n(λ)` | `dim V_λ` (`G_λ` at `n(λ)`) | `χ(H_λ)=f_λ(-1)` | `Δ_λ` |
|---|---|---|---|---|---|---|---|
| `(5)` | 0 | 1 | `1` | 1 | 1 | `+1` | `+1` |
| `(4,1)` | 1 | 4 | `q[4]_q` | **1** | **4** | `0` | `-4` |
| `(3,2)` | 2 | 5 | `q²[5]_q` | **1** | **5** | `1` | `+5` |
| `(3,1,1)` | 3 | 6 | `q³[3]_q(1+q²)` | **1** | **6** | `-2` | `-6` |
| `(2,2,1)` | 4 | 5 | `q⁴[5]_q` | **1** | **5** | `1` | `+5` |
| `(2,1,1,1)` | 6 | 4 | `q⁶[4]_q` | **1** | **4** | `0` | `+4` |
| `(1⁵)` | 10 | 1 | `q^{10}` | 1 | 1 | `+1` | `+1` |

Every non-`dim`-1 block: the honest graded object reads **1** at the a-function
grade, while concentration demands **`dim V_λ`** there. The missing `dim − 1` sits
spread across higher grades — exactly the shape a valuation is blind to.

**Reading.** The promoted a-function supplies precisely the pair `(valuation, ungraded
dim)`; `G_λ` and `H_λ` share BOTH, yet only `G_λ = Δ_λ`. So no functional of that
data — in particular the GS jet-order valuation — can distinguish, hence cannot
FORCE, the single-degree (top-cohomology) concentration. The valuation fixes WHERE
the bottom is; it is silent about the shape above. Concentrating the full `dim V_λ`
at `n(λ)` is an **ad-hoc collapse the valuation never performs**.

## Proved / open split

- **PROVED (sorry-free, this file):** the GS jet-order valuation — even added to the
  ungraded Wedderburn data ruled out in #4570 — does NOT force the single-degree
  concentration (two graded objects, same valuation `n(λ)` and same ungraded dim,
  different signed Euler characteristics; only the concentrated one is `Δ_λ`; sharp
  mechanism: coefficient `1 ≠ dim` at the valuation grade). Degree-blindness proved
  generic.
- **OPEN (unchanged, now precisely bounded):** whether ANY driver-level structure
  richer than a valuation — a genuine graded Springer / coinvariant object forced by
  the drivers (the open primary conjecture `DeltaLambdaDTRealization`, a *different*
  leg) — can supply the single-degree concentration. The three candidate forcing
  mechanisms that were on the table (DT count / confinement SDP / jet-order
  valuation) have now all fallen; a genuine graded substrate structure, not any of
  these, is the remaining route.

## Verdict

**NO — the GS jet-order valuation does not force single-degree selection**, proved as
a scope-(a) LIMITATIVE negative with a structural backbone: a valuation reads only
the bottom grade (`n(λ)`), with monic weight `1` there; the concentration puts the
full `dim V_λ` at that grade, which the valuation cannot supply. This is **not** a
claim that top-degree concentration is excluded from every closure — a genuine graded
substrate structure (the open `DeltaLambdaDTRealization`) remains a live route. It
IS the precise NEGATIVE answer to `qou-71ma`, and — crucially — it does **not** reopen
`Δ_λ`'s VALUE: `Δ_λ = (-1)^{n(λ)}·dim V_λ` is a function of two substrate SCALARS
(jet-order valuation parity + Wedderburn dim), needing no graded/geometric object;
only the DT/Springer geometric categorification carries the independent concentration
input. Fourth-direction convergence with #4554 / #4559 / #4570.

## Anti-fit / honesty ledger

- **0 free parameters**; `Δ_λ`, AME, CODATA, `q₀` never inverted; the fake-degree
  polynomials `f_λ(q)` are standard coinvariant graded dimensions (hook-length;
  `f_λ(1) = dim V_λ` machine-checked).
- Formalize-first honoured: the limitative claim is a sorry-free Lean statement. No
  `sorry`, no `True`-conclusion, no `native_decide`/`decide`-laundering (the
  `decide`s discharge genuinely-finite concrete integer computations at `n = 5`);
  base ring `ℤ`/`ℕ` (§7c).
- **No instance of the open conjecture fabricated.** The proved content is a
  *limitative* fact (the valuation does not force the concentration) — it does NOT
  close the open leg and does not launder it. "Axiomatization is NOT a proof",
  "sorry-free ≠ derived", "conditional-proved ≠ premise-established" respected.
- corpus-grep run before the "does-not-force" / "open" declarations (Springer /
  fake-degree / coinvariant / jet-order / top-cohomology paths walked; the
  valuation's classical meaning confirmed from
  `2026-07-11-deltalambda-grho-jet-order-derivation.md` + `PrincipalGradingJetOrder.lean`).

## Cross-references

- Companion (ungraded side): PR #4570, [`2026-08-02-deltalambda-sdp-topdegree-projection.md`](2026-08-02-deltalambda-sdp-topdegree-projection.md).
- Parent (moduli under-determined): PR #4559 (`qou-ylot`).
- Single-degree DT object: PR #4553, [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md).
- `A_ω=3` structurally-open: PR #4554 (`qou-qnnq`).
- jet-order valuation = fake-degree valuation derivation: [`2026-07-11-deltalambda-grho-jet-order-derivation.md`](2026-07-11-deltalambda-grho-jet-order-derivation.md); [`PrincipalGradingJetOrder.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PrincipalGradingJetOrder.lean).
- Open realization conjecture (different leg): `DeltaLambdaDTRealization`.
- Primary sources: Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., OUP 1995, §I.5 ; Springer, *A construction of representations of Weyl groups*, Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165 ; James, `[james1984representation]`.
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring open/refuted"; §"Strict Lean Discipline".
