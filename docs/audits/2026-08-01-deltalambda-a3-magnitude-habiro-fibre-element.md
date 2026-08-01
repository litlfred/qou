# GAP-A-3 ROUTE 4: a Habiro-ring fibre element does NOT supply the A=3 magnitude factor r* ≈ 1.585

**Date:** 2026-08-01
**Branch:** `claude/a3-magnitude-habiro-fibre-element-2026-08-01`
**Axis:** per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the A=3 (triton) 3-body **magnitude**.
**Tier:** derivation probe (EXPLORATORY / SPECULATIVE route, as tasked). **Verdict: two-part honest
negative — REFUTE(scope-b) + WALL(scope-a). 0 fit; nothing wired.**
**Gate:** Δ_λ open-for-all for derivation routes (owner reversal 2026-07-13); Subgoal-2 open-for-all
(2026-07-11). Anti-fit / anti-laundering discipline is orthogonal and STILL STANDS.

- Lean: [`QOU/MassTheory/HabiroMagnitudeA3.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/HabiroMagnitudeA3.lean)
  — sorry-free, `lean`-direct exit 0; no trivial-true / native_decide / axiom.
- Probe: [`computations/deltalambda/habiro_magnitude_a3_probe.py`](../../computations/deltalambda/habiro_magnitude_a3_probe.py)
  · witness `habiro-magnitude-a3.witness.json`.
- Bean: `qou-2ybf`.

## The gap and the route

The A=3 3-body magnitude factor `r* = μ₃/c₃ ≈ 1.585` is the ratio between the target additive-residual
moment `μ₃ = +0.4708` (`AdditiveResidualSimplex` #4320) and the Hecke-level near-miss `c₃ = +0.297`
(#4364 `BorromeanMagnitudeLift`). It is already bracketed out of **every Hecke-level ingredient** and out
of the **finite-type / Vassiliev filtration** of the single Borromean deficit:

- not a derived tower LEVEL (three-walls 2026-07-26, #4364/#4376);
- not a geometric `W_λ` (#4392, `S⁴ = 1`);
- not a coordination-EDGE factor (#4472, `K₃` breaks Brunnian order);
- not the exact-order Milnor μ̄_A coefficient (#4480, ratio exactly `−2`);
- not a Vassiliev weight-system correction (2026-08-01, `VassilievMagnitudeA3.lean`: every finite-type
  weight is `≤` the Hecke value; the integer Milnor weight is `−2`).

That last audit named the remaining candidate explicitly: "structure genuinely OUTSIDE the finite-type
filtration … e.g. a per-isotope operator-valued combiner, or a cross-cluster interface term." **ROUTE 4
tests the most speculative such candidate: a fibre-level Habiro-ring element**
`F(q) = Σ_n a_n(q)·(q;q)_n` in the cyclotomic completion, parallel to the proved α_EM element
`[2]_q·(1 − h²α)` (PR #1511) and the Q_β Habiro element. Per the AGENTS.md "Im(q) at fibre vs observable
level" banner, the magnitude coefficients live in the FIBRE, and each q₀ anchor is a distinct archimedean
evaluation of the SAME fibre object; a REAL closed form `r* = f(q₀)` for smooth real f is already known
to fail (`dc₃/dq` impossible, PR #1821). The disciplined Habiro question is whether a
**structurally-forced (0-fit)** cyclotomic-completion element evaluates to `r*` at the substrate.

## The decisive obstruction: the substrate anchor is `q₀ > 1`

The Habiro ring `ℤ[q]^ = lim_n ℤ[q]/((q;q)_n)` has canonical evaluations at ROOTS OF UNITY (where
`(q;q)_n` vanishes for `n ≥ ord`, truncating the sum to a finite polynomial) and, more generally, INSIDE
the unit disk `|q| < 1` (where `(q;q)_n → (q;q)_∞` and integer-coefficient series can converge). The QOU
substrate modulus is `q₀ ≈ 1.10998 > 1` — **OUTSIDE both loci.**

**Proved (sorry-free Lean).** For real `q > 1` the cyclotomic basis magnitude
`|(q;q)_n| = ∏_{k=1}^n (q^k − 1)` is UNBOUNDED (`pochAbs_unbounded`): the successive factor
`q^{n+1} − 1 → ∞`, so from some index on the partial products at least double each step (geometric
doubling, `pochAbs_ge_geometric`). Consequently a genuine (infinite) integer-coefficient Habiro element
`Σ a_n (q;q)_n` with `|a_n| ≥ 1` has terms that do NOT tend to `0` (`habiro_terms_not_tendsto_zero`) —
the series is **not summable at `q > 1`**. A genuine cyclotomic-completion element therefore has **no
canonical archimedean value at the substrate**; it cannot supply a well-defined magnitude factor there.

Numerically (muon-canonical `q₀ = 1.10997859…`, `computations/` layer): `|(q;q)_n|` first dips
(`n=1…~7`, factors `< 1`) then grows without bound — `|(q;q)_40| ≈ 1.8·10³¹`. The completion series
diverges.

## The finite (Laurent) sub-case is bracketed

The ONLY Habiro-shape elements with a well-defined evaluation at `q₀ > 1` are the FINITE
(Laurent-polynomial / rational) ones — exactly the α_EM shape `[k]_q·(1 − h²X)`, which is a genuine
Laurent object (its "Habiro" framing is the leading part of a cyclotomic expansion, but the WIRED object
is finite). Those are governed by the already-established finite-type bracketing:

| element at `q₀` | value | vs `r* = 1.5852` |
|---|---|---|
| `[1]_q` | `1.0000` | below (`1 < 3/2 < r*`) |
| `[2]_q = q₀ + q₀⁻¹` | `2.0108` | above (`r* < 2 ≤ [2]_q`) |
| correction `(1 − h²·X_deficit)` | `1 − 6·10⁻⁵` | negligible |
| best 0-fit quantum-integer scan `[6]_q/[4]_q` | `1.554` | `−1.9 %` (fit-scan near-miss, not forced) |

`rStar_strictly_between_q1_q2` (sorry-free): `r* ∈ (3/2, 2)` lies STRICTLY between `[1]_q = 1` and
`[2]_q = q + q⁻¹` for any `q > 1` with `q + q⁻¹ ≥ 2`. The α_EM-shape element evaluates (to leading order)
to a quantum integer `[k]_q`; no integer `k` — and no 0-fit categorical `X` — lands on `r*`. A value
hitting `1.585` requires a NON-forced (fit) coefficient, which the anti-fit discipline declines.

## Verdict — two-part honest negative

1. **REFUTE(scope-b)** of "an infinite cyclotomic-completion Habiro element evaluates to `r*` at the
   substrate." Cited proved invariant: `pochAbs_unbounded` (the basis magnitude grows without bound for
   `q > 1`), giving `habiro_terms_not_tendsto_zero` (divergence). No well-defined archimedean value exists
   at `q₀ > 1`, so none can equal `r*`. This is a genuine structural exclusion (a proved growth /
   non-summability fact), NOT a scope-(a) numerical near-miss — but it is narrow: it excludes the *bare
   infinite completion evaluated at the substrate*, not Habiro/quantum-modular structure in a *larger*
   closure (e.g. a resummed / analytically-continued object, or an operator-valued combiner). Per the
   "before declaring refuted" discipline, the (b) is on the well-definedness of the naive evaluation only.

2. **WALL(scope-a)** for the finite (Laurent) α_EM-shape sub-case. It reduces to the quantum integers
   `[k]_q`; `r*` lies strictly between `[1]_q` and `[2]_q` (`rStar_strictly_between_q1_q2`), and no derived
   (0-fit) element lands on it. Selecting a coefficient to hit `1.585` is a FIT, declined.

**Net.** No DERIVED (not fitted) Habiro-ring fibre element reproduces `r*`. The genuinely-new infinite
completion diverges at `q₀ > 1`; the well-defined finite part is the already-bracketed quantum-integer
object. This is consistent with the α_EM (`[2]_q·(1−h²α)`) and Q_β Habiro elements being FINITE Laurent
objects — the Habiro framing there does not smuggle in an infinite tail at `q₀ > 1`. The A=3 Δ_λ exact
magnitude closure remains **open** (scope-a), now with the cyclotomic-completion route closed too.

## Anti-fit / honesty ledger

- **0 free parameters** throughout; `μ₃`, `c₃`, AME, CODATA, `q₀` never inverted. No coefficient was
  chosen to hit `1.585` — the quantum-integer scan is reported precisely to show that any "match" would
  be a fit-scan, not a forced value.
- Verdicts classified: **REFUTE(scope-b)** (infinite-completion divergence, cited invariant
  `pochAbs_unbounded`) + **WALL(scope-a)** (finite-Laurent bracket). No unclassified "refuted"; the (b)
  is explicitly narrowed to the naive-evaluation well-definedness.
- **Not a fit, not wired.** "No seventh fit-based ansatz" + PROBE-4 KL-prune stand. Formalize-first
  honoured: every claim is a sorry-free Lean statement (lean-direct exit 0) written before the probe; no
  trivial-true / native_decide / axiom laundering.

## Cross-references

- Four/five prior A=3-magnitude walls:
  [`2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md),
  [`2026-08-01-deltalambda-a3-beyond-hecke-vassiliev-magnitude.md`](2026-08-01-deltalambda-a3-beyond-hecke-vassiliev-magnitude.md).
- Target moment: `AdditiveResidualSimplex.lean` (#4320) — `μ₂=0, μ₃=+0.4708, μ₄=−4.591`.
- Hecke near-miss lifted: `BorromeanMagnitudeLift.lean` (#4364).
- α_EM Habiro element (finite Laurent): PR #1511 (`[2]_q·(1−h²α)`).
- Option-E ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md).
- Fibre-vs-observable framing: AGENTS.md "Im(q) at fibre vs observable level (2026-06-01)".
