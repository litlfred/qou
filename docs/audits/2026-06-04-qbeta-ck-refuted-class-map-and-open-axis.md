# Q_β c_k derivation — refuted structural-class map + the one open axis

**Date:** 2026-06-04
**Status:** SEARCH-SPACE MAP (method/hypothesis-class status). Complements —
does **not** supersede — the per-rung
[`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md),
which stays authoritative for each rung's canonical-vs-empirical *tier*.
This doc records which **derivation approaches** have been eliminated, so the
next session narrows its probe instead of re-running a refuted class.

> **Why this doc, distinct from the registry.** The registry answers *"what is
> the status of rung c_k?"* (value-level). This doc answers *"which method of
> deriving the c_k / the ladder element is still alive?"* (method-level). Both
> are needed: the registry stops re-deriving a refuted *value*; this map stops
> re-running a refuted *method*. It is the backward-pruning corpus-grep
> discipline (CLAUDE.md §"Before declaring open") applied to the **search
> space**, and the forward-pruning formalize-first discipline
> (CLAUDE.md §"Formalize-first probe discipline") applied to **what to run
> next**.

---

## 1. What the open keystone actually is (read before proposing any probe)

Per registry §3/§5, the open object is **not a c_k value**. It is the
fibre-level pair:

- the **Habiro element** `F(q)` whose Habiro / Taylor coefficients **are** the
  ladder `c_k` (`Q_β = Q_base · ∏_{k≥2} (1 + c_k u^k)`, `u = b·ℏ_q² ≈ 0.00852`), and
- the **kernel** `R(q,ξ)` of the proved (sorry-free) *conditional* recursion
  `F(qξ) = R(q,ξ)·F(ξ) ⟹ c_{k+1} = Σ_j a_j(q₀) c_{k+1−j}`.

Only **c_2 = −1** is canonical (Taylor-exact, anchor-stable). Every c_k≥3 is
**empirical** until `F(q)` is constructed. Two hard constraints on any candidate
`F(q)`, both already established, kill most naive attempts up front:

1. **Fibre-level, not real-q.** `c_3`'s best real-q forms reproduce the
   empirical value at the **proton anchor only** and are **rigid**
   (`dc_3/dq ≈ 4.6×10⁶`; swing 4.7M× smaller than the empirical c_3) — so a
   genuine `F(q)`, if it exists, is **complex-analytic / root-of-unity** at the
   fibre level, **never** a real-q formula in `q₀`
   (CLAUDE.md §"Im(q) at fibre vs observable level"; registry §3 c_3 row;
   falsification audit
   [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)).
2. **Anchor-stability is the canonicity gate.** Registry §8: a coefficient is
   `canonical` only if it passes a proton+muon cross-anchor swing `< 1%`. A
   small proton residual alone is `empirical`, always.

These two facts are the **invariants the surviving hypothesis class must
respect**. A probe that proposes a real-q `c_3 = f(q₀)` or validates against the
proton anchor only is **dead on arrival** — it is already in the refuted map
below.

---

## 2. Refuted structural-class map

Each row is a **class** of derivation attempt, the verdict, and the load-bearing
evidence. **Before running a new c_k probe, check this table; if your idea is a
member of a `REFUTED` class, do not re-run it.**

| # | hypothesis class | verdict | evidence |
|---|---|---|---|
| C1 | **Real-q single-formula c_3** (`J−ℏ²`, `[3]_q/25`, and 28 enumerated single forms) | **REFUTED** — proton-only match, cross-anchor rigid | 28 NEGATIVE single-formula scan (PR #1831); rigidity falsification `dc_3/dq≈4.6×10⁶` (registry §3) |
| C2 | **Real-q 2-factor composite c_3** (`f₁(q)·f₂(q)` over 1281 candidates) | **REFUTED** — best proton matcher (`q²+q⁻²−[4]_q`) misses muon 14× | cross-anchor 2-factor sweep, 1281 cands, NEGATIVE (PR #1831) |
| C3 | **Torus-knot family `T(2,n)`** as the rung-1 `/25` source | **REFUTED** — cubic Taylor `= deg-3 poly in n`; none equals the target `1` | 9-knot extended scan T(2,3..11)+twists (PR #1822) |
| C4 | **Cinquefoil `T(2,5)` knot-assignment** for c_3 | **REFUTED** — T(2,5) is the muon particle-knot, not c_3; `/25` is the coincident fibre constant `[5]_q²\|_{q=1}` | knot-assignment verification (PR #1811) |
| C5 | **Constant-kernel recursion** `R(q,ξ) = const` (depth ≤ 4) | **REFUTED through depth 4** → kernel, if any, is non-constant q-rational | commit `eca145ca` (registry §5) |
| C6 | **Pell-Lucas σ-action pattern extended into the free rungs** (`c_8 = 4b⁴`, …) | **BREAKS at first free rung c_8** — closed `+2.27` vs bias-corrected `−0.215` (wrong sign) | c6–c10 cross-anchor bias-corrected probe (PR #1842, merged `160a3a6d`) |
| C7 | **SDP extraction of c_k≥4** | **noise-dominated / biased** — `+1.7%` bias on the *proved* c_2, ratios 10³–10⁷× at k≥8 | SDP-zero probe (PR #1839); extraction docstring (registry §3) |
| C8 | **Algebra-tower box-adding** (`H₃ ⊂ H₄` Bratteli induction) to derive the Family-A `linking_weight` | **REFUTED B1/B2/B3** — uniform residual q-dependent; y_λ-weighted 60.1% error; per-source λ all q-dependent | Bratteli probe, 3× REFUTED (PR #1841) |
| C9 | **Per-knot `Vol(β_K)` flip for the light series** (production swap) | **NOT VIABLE as a flip** — per-block undershoot grows `−57%`(p) → `−95%`(T); diagnostic-only | Option-A per-knot Vol diagnostic (PR #1816) |
| C10 | **Khovanov–Rozansky `sl_N`** import for the H₃→H₄ `+1` | **REFUTES (wrong axis)** — its `+1` is gauge rank N, the transverse axis; importing it misleads | literature import (PR #1808) |
| C11 | **Volume conjecture** as the strand-count limit | **SILENT** — limit parameter is color N / root-of-unity order, not strand count | literature import (PR #1808) |
| C12 | **Trace-level Markov-stabilization** (`Ind_{H₃}^{H₄}` under `tr_M`; M1 identity-trace + M2 `z^{±k}` renormalised; mass-side axis) | **REFUTED** — `z(q₀)=0.4993 < 1 < linking_weight=2.5328` (direction obstruction); `tr_M(1_{H₄}) = Σ_{λ⊢4} y_λ f^λ = 1` exactly, not 2.53 (M1); no exact `z^{±k}·(clean H₃)` coincidence (M2); `z⁻¹ = q^½+q^{-½}` irrational | sibling probe — PR #1850 (merged `e43d071d`), formalize-first prediction confirmed |
| C13 | **#1622 mode→ladder bridge with a `Δtr_M`-seeded *linear/bar-even* `f`** (change of variable `u=√q ↦ u_L=b·ℏ_q²`, seed `1+N·Σ_{k≥2}(a_{2k}/b^k)u_L^k`, scale `N` fixing `c_2=−1`) | **REFUTED** — both seeds give a *constant* (anchor-stable) `c_3` far from `−2`: raw even-in-ℏ `c_3=−100/(77b)≈−1.497` (25% off), #1602 bar-even `c_3=−175/(144b)≈−1.401` (30% off); `c_4` off 65–87%. `c_2=−1` only as a scale-fix, not independently derived. The bridge IS now executed; the surviving `f` is **non-linear** in `Δtr_M`. | PR #2465 — `habiro_mode_to_ladder_bridge.py` + `habiro-mode-to-ladder-bridge.witness.json`; formalize-first gate (the bridge had to be formal/anchor-independent, and is) |

**Reading.** The real-q axis (C1–C4), the constant-kernel axis (C5), the
Pell-Lucas-into-free-rungs axis (C6), the SDP-extraction axis (C7), the
algebra-tower box-adding axis (C8), and **the trace-level Markov-stabilization
axis (C12)** are all closed. C9 is closed as a *production flip* (it remains a
legitimate diagnostic). C10–C11 are literature dead-ends for the H₃→H₄ jump.
**Both surviving mass-side mechanisms (algebra-tower C8, trace-level C12) are
now refuted**; per #1850's synthesis, the production `linking_weight =
(1/4)·Σ_{λ⊢4} dim_q ≈ 2.53` is best read as a **CODATA-implied near-match**
(landing near `λ = m_p/(m_e·Vol/ℏ²) ≈ 2.46`), not a derived categorical count.

**C13 (2026-06-18)** closes the *decay-side* bridge method at its simplest
seedings: the #1622 mode→ladder change of variable is now **executed**, and a
`Δtr_M`-seeded **linear / bar-even** `f` does **not** reproduce `c_3` (gives a
constant `≈ −1.4…−1.5`, not `−2`). The bridge itself is sound and the exact
even-in-ℏ data is now pinned (§3 forward constraint); what survives is a
**non-linear** `f`, still fibre-level and open.

---

## 3. The remaining open axis — fibre-level Habiro element F(q) (decay-side only)

> **Update 2026-06-04 (post-#1850).** The original §3 listed **two facets** of
> the open axis (mass-side `Ind_{H₃}^{H₄}` under `tr_M` + decay-side fibre
> Habiro). The mass-side facet has now been **REFUTED at the canonical
> trace-stabilization level** by PR #1850 (table row C12). The §4
> formalize-first gate predicted exactly this — that the trace-level identity
> would fail the invariant check — and the canonical probe confirmed it. **The
> remaining open axis is decay-side only**: the fibre-level complex-analytic
> Habiro element F(q) of §1, never a real-q mass-side trace identity.

- **Mass-side `linking_weight ≈ 2.53` (refuted):** the algebra-tower box-adding
  (C8, PR #1841) and the trace-level Markov-stabilization (C12, PR #1850) both
  fail. The 2.53 multiplier is **CODATA-implied near-match** territory, not a
  derived categorical count — full provenance in #1850's synthesis and
  the [`vol_density_borromean()`](../../computations/_li_2_q_util.py)
  docstring in `_li_2_q_util.py` (the "2.53 is a CODATA-implied-λ near-match"
  paragraph).
- **Decay-side fibre Habiro element F(q) (open):** the keystone of §1, whose
  kernel `R(q,ξ)` is non-constant q-rational (C5 ruled out constants) and whose
  evaluation is root-of-unity / complex-analytic (C1–C4 ruled out real-q). This
  is **not** a trace identity over real q at a real anchor; it is a
  fibre-level (formal/cyclotomic) q-series object per CLAUDE.md
  §"Im(q) at fibre vs observable level". **The previous framing that called the
  mass-side trace identity and the decay-side fibre element "two facets of one
  question" is too strong** — they were two candidate mechanisms; only one
  survived.

The §1 invariants for any F(q) candidate (fibre-level, anchor-stable,
bar-even, integer `q=1` shadow) stand unchanged.

> **New forward constraint (2026-06-18, PR #2465 / C13).** The #1622 bridge
> is now **executed**, yielding the **exact, anchor-independent ℏ_q-Taylor
> series of `Δtr_M`** (about `q=1`):
> `a_n = [ℏ^n]Δtr_M = −5/4, −13/8, −33/16, −77/32, −177/64, −25/8,
> −891/256, −3923/1024, −4277/1024, …` Because `u_L = b·ℏ_q²`, the
> **even-in-ℏ** coefficients `a_4, a_6, a_8` are the *only* `Δtr_M` data
> feeding the integer rungs `c_2, c_3, c_4`; the **odd-in-ℏ** `a_1, a_3, …`
> are the half-integer bar-odd remainder `f` must cancel (the √u→u² lift;
> makes PR #1602's `−√3/12·u¹` class exact). Any surviving `f` must map this
> fixed even-in-ℏ data onto the empirical `c_k` **non-linearly** — the
> linear and bar-even-projection seedings are refuted (C13). Note
> `bar-even (u↦1/u) ≠ even-in-ℏ` parity: two independent constraints, both
> binding.

---

## 4. Formalize-first gate for the next probe (narrow before you run)

> **Update 2026-06-04.** PR #1850 ran a textbook execution of this gate against
> the (now-refuted) trace-level axis: the `z(q₀) = 1/(q^½+q^{-½}) < 1` direction
> obstruction was identified **before** any anchor scan, narrowing the probe
> from "scan all trace constructions" to "test M1 (identity trace) + M2 (`z^{±k}`
> renormalised) only" — and both fell. This is the discipline working as
> intended; the gate killed the class on the structural invariant, not on a
> wide numeric search. Apply the same shape to any future F(q) candidate.

Per CLAUDE.md §"Formalize-first probe discipline", state the invariant the
surviving class must satisfy **before** launching a probe, so a refuted
sub-case is killed on paper rather than by an expensive scan:

1. **Hypothesis class.** A fibre-level (formal-q / cyclotomic) Habiro element
   `F(q)` whose Habiro / Taylor coefficients reproduce the ladder `c_k`, with a
   non-constant q-rational kernel `R(q,ξ)` satisfying
   `F(qξ) = R(q,ξ)·F(ξ)`. **Not** a real-q mass-side trace identity (refuted by
   C8 + C12).
2. **Invariant the whole class must satisfy.** (a) **Anchor-stability** — any
   coefficient produced must pass proton+muon swing `< 1%` (registry §8);
   (b) **bar-evenness** / `q↦q⁻¹` symmetry of any `F(q)` (the c_2 = −1 rung is
   bar-even, Kashiwara `f̃₁²`); (c) **q=1 classical-limit shadow** must
   reproduce the known integer (`c_3 → J_Hopf(1) = −2`) without fitting; (d)
   **direction sanity** — `|F(q₀)|` and any scaling factor must respect the
   target observable's magnitude (the lesson of #1850: `z<1` cannot multiply up
   to `linking_weight > 1`).
3. **Formalize it.** A Lean lemma (even conditional `class` + `-- Ref:` per
   §3b-cond) stating the q-difference equation for `F(q)`, or a rigorous
   symbolic q-difference argument for `R(q,ξ)`. The proved-sorry-free recursion
   *engine* already exists (registry §5); what is missing is the **kernel**, so
   the formalization target is `R(q,ξ)` (non-constant q-rational, ζ₄ residue,
   √u→u² lift), not another value.
4. **Let the result narrow the probe.** If a candidate `F(q)` fails the `q=1`
   shadow, the bar-evenness invariant, or the direction sanity check
   symbolically, **do not** run the numerical anchor sweep — add a new row to
   §2 and stop.

---

## 5. Standing rule (discipline)

- **Before any new c_k / ladder-element derivation probe, consult §2.** If the
  idea is a member of a `REFUTED` class, it is already eliminated — do not
  re-run it; cite the row instead.
- **A new class that is run gets a new §2 row** with its verdict (so the map
  stays the single method-level record, mirroring how the registry is the
  single rung-level record).
- **Per-rung status changes still go to the registry**, never here. This doc
  records *methods*, the registry records *tiers*. Do not duplicate a rung tier
  into this file.
- The decay-side fibre-Habiro axis (§3) is **owner-gated multi-session
  research**, not a foreground discharge — coordinate with the active Phase-2 /
  1762-roadmap siblings (PRs #1808, #1816, #1841, #1850, #1811) via
  `coordinate.md` before opening a probe branch; overlap at the Hecke `tr_M` /
  fibre-Habiro machinery is near-certain.
- **Mass-side `linking_weight` is now CODATA-implied near-match territory** —
  not "open keystone." Probes that propose a mass-side trace identity for
  `2.53` are members of refuted classes C8 (algebra-tower) or C12 (trace-level);
  cite those rows and do not re-run.

---

## 6. Cross-references

- **Authoritative rung status:** [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
- **1ppQ Q_β master ledger (open probes):** [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- **Truncation-order framing (N is a precision knob):** [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- **Shared root cause (Q_β / m_n / Δ_pn):** [`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)
- **H₃→H₄ literature import (named the trace-level lead):** [PR #1808](https://github.com/litlfred/qou/pull/1808) (doc `2026-06-04-h3-h4-jump-literature-import.md` lands when #1808 merges)
- **H₃→H₄ jump consolidated negative (paper-topic deep-dive complement to this map):** [`2026-06-04-h3-h4-jump-both-axes-refuted.md`](2026-06-04-h3-h4-jump-both-axes-refuted.md) — closes 2 of the 5 #1762 attack options at the paper-topic level (mass-side `linking_weight_family_a` ≈ 2.53 is CODATA-implied near-match), while this map records the same outcome at the method-registry level (C8 + C12).
- **Trace-level axis scope + refutation (C12):** [`2026-06-04-markov-stab-trace-axis-scope.md`](2026-06-04-markov-stab-trace-axis-scope.md), [`markov_stab_trace_axis_probe.py`](../../computations/probes/markov_stab_trace_axis_probe.py), `markov-stab-trace-axis-probe.witness.json` (all merged via PR #1850)
- **Refuted-class source PRs:** #1811, #1816, #1822, #1831, #1839, #1841, #1842, #1850 (all merged)
