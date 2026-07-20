# Q_β `c_3` — Habiro-element / fibre-level route: growth-class exclusion

**Date:** 2026-07-20
**Branch:** `claude/argument-principle-residue-sum-2026-07-20`
**Bean:** `qou-1dnr` (parallel independent attack; owner directive 2026-07-17)
**Verdict:** **NEGATIVE — the *formal*-Habiro-element route to `c_3` is REFUTED
AS A CLASS (scope-(b) structural exclusion).** No anchor-invariant `c_3`
derived; the near-match remains a fit.

---

## 1. Route and how it differs from the sibling

AGENTS.md flags the **Q_β Habiro element** as the intended permanent fix for the
`c_k` ladder (parallel to α_EM's `[2]_q·(1−h²α)`), living at the **fibre**
level. This branch attacked that route — *find a formal Habiro-ring element
`F(q)` whose Taylor / Ohtsuki (`q=1`) coefficients ARE the `c_k`* — **independently
of** the sibling on `qou-1dnr` (q-lift recursion / DM-cubic / Berezinian
even-odd cross-term). The two contexts converge on the same conclusion from
different directions (see §5).

## 2. The collision (the honest finding)

Two established corpus facts are mutually exclusive:

| object | growth | radius | source |
|---|---|---|---|
| **Q_β ladder** `g(u)=Σ c_k u^k` | **geometric** (`c_{k+1}/c_k → 1/u_sub ≈ 117.409`) | **finite** `= u_sub` | KC8 = `prop:q-beta-radius-of-convergence-gate`, PR #1713/#1727 (simple pole at `u_sub`) |
| **formal Habiro element** (`q=1` Ohtsuki expansion) | **Gevrey-1** (`\|c_k\| ~ k!`, super-geometric) | **zero** | Habiro 2008; Garoufalidis–Zagier; the class the *binding* `D(ũ)` lives in — registry **KC22** |

Geometric growth (finite radius) and Gevrey-1 growth (zero radius) are
**disjoint** sequence classes. Therefore the Q_β `c_k` **cannot** be the `q=1`
coefficients of any formal Habiro-ring element. The "Q_β Habiro element" the
corpus has hunted for does **not exist as a *formal* object**; the correct
object is the **analytic simple-pole residue** (the argument-principle /
residue-sum picture of this branch).

This upgrades two prior *numerical* results to a *proved structural* exclusion:
the C16 integrality-kill (ladder not Habiro-integral under natural
normalisations, PR #3536) and the empirical KC8 radius gate.

## 3. Formalize-first deliverable (Lean, sorry-free)

[`QOU/Mass/QbetaC3Habiro.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/QbetaC3Habiro.lean)
(verified `lean`-direct, exit 0, sorry-free):

* `GeometricGrowth` / `SuperGeometricGrowth` — the two growth classes over `ℝ`.
* **`geometric_not_superGeometric`** — the disjointness, **proved outright**
  (apply super-geometry at rate `L+1`; `((L+1)/L)^k` bounded contradicts
  `pow_unbounded_of_one_lt`; the `L=0` corner degenerates to `1 ≤ 0`).
* `QbetaLadderGeometric` / `FormalHabiroQOneExpansion` — the two cited corpus
  inputs as §3b-cond **class hypotheses** (KC8; Gevrey-1 literature), NOT
  re-derived.
* **`qbeta_ck_not_formal_habiro`** — the conditional exclusion: the two
  hypotheses on the same `c` yield `False` (scope-(b), AGENTS.md §"Before
  declaring refuted": a proved growth invariant forbids the ingredient).
* **`simplePole_coeff_geometric`** — the *surviving* analytic side: a simple
  pole's Laurent coefficients are geometric (consistent with KC8, **not** a
  formal Habiro element).

Base ring `ℝ` (§7c): the dichotomy uses ordering + the archimedean property.

## 4. Falsifiable-honesty test (two-anchor) — FAIL (fit, not derivation)

Probe
[`computations/probes/qbeta_c3_habiro_growth_dichotomy.py`](../../computations/probes/qbeta_c3_habiro_growth_dichotomy.py)
(two-anchor, no fitting):

| anchor | `q₀` | `u_substrate` | rate `1/u` |
|---|---|---|---|
| proton | 1.10997858275 | 0.008517234550 | 117.40900 |
| muon | 1.10997859555 | 0.008517236340 | 117.40898 |

* `u_substrate` cross-anchor drift **210 ppb** — the pole is at the *same*
  fibre-level location (PR #1727), and `1/u_sub = 117.409` reproduces PR #1713's
  `c_{k+1}/c_k → 117.409` to 4 s.f.
* Ratio-test dichotomy (in-range discriminator): geometric ratio **constant
  117.409**; Gevrey ratio `k+1` **unbounded**. Disjoint.
* **`c_3` itself is NOT anchor-invariant** — the near-match swings ~2.9%
  proton↔muon (`−2.0693` / `−2.0097`, registry `c_3` row). By the shared
  falsifiable test, swing ⇒ **fit**, not a derivation. This route derives **no**
  new `c_3`.

**Q_β residual:** unchanged. The `N=3` near-match already lands `+6.0 ppb`
(< the `7.8 ppb` 100× target), but `c_3` stays a **near-match**; because this
route produces no *derived* `c_3`, it does **not** bring Q_β under the target as
a derivation. The surviving analytic residue `A ≈ 1.804×10⁻¹⁵` has no real
`q₀`-rational closed form (PR #1727: 38 candidates, best −0.28%, ~2.9% swing
floor).

## 5. Convergence with the sibling (not waste)

The sibling's q-lift/DM-cubic route works the **binding** ladder `D(ũ)`, which
IS Gevrey/resurgent (KC22, radius → 0) — the *opposite* growth class from Q_β's
`g(u)`. This branch's result explains **why** every formal-Habiro attack on Q_β
(C14 forced-knot, C15 Borromean, C16 integrality, C17 raw-operator) failed:
they sought a zero-radius object where a **finite-radius analytic** one lives.
The two routes converge — the Q_β `c_3` closure, if any, is an **analytic**
(argument-principle / residue) statement at real `q₀`, the surviving Φ_b axis
(sibling `qou-9lot`, PR #3540), **not** a formal Habiro element.

## 6. What this does and does NOT claim

* **Proves** (scope-(b), Lean sorry-free): geometric and Gevrey-1 growth are
  disjoint ⇒ the Q_β `c_k` are not formal-Habiro/Ohtsuki coefficients.
* **Does NOT** derive `c_3`, wire anything to production, or refute the
  *analytic* residue route (that survives, open).
* **Does NOT** touch the near-match's tiered status (`c_3` stays
  EMPIRICAL/near-match in the registry).

## Cross-references

- Radius/simple-pole: [`2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md`](2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md), [`2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`](2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md)
- Refuted-class map (C14–C18): [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
- Registry (KC8, KC22, `c_3` row): [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
- Truncation-order framing: [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- α_EM Habiro precedent (bar-even) + Q_β residue-dual (bar-odd): `alpha-em-habiro-bar-involution`, [`QBetaResidueHabiroDual.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaResidueHabiroDual.lean)
