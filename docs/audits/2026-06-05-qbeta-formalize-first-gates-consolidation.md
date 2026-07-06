# Q_β `c_k` formalize-first gates — consolidation + Δ_λ pre-flight checklist

**Date:** 2026-06-05
**Branch:** `claude/qbeta-formalize-first-gates-2026-06-05`
**Predecessors:** PR #1875 (bar-even §4(b) gate), PR #1839 (`CFinite` engine), PR #1727 (u_substrate simple-pole), PR #1831 (1+2-factor saturated search), PR #1786 (c_2 = −1 structural seed), refuted-class map `2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`

> **Why this doc.** PR #1875 added the bar-even structural invariant as a proper proposition triple + sympy probe. PR #1839 ships the `CFinite.recurrence_step` engine. PR #1727 established that `g(u) = Σ_k c_k u^k` has a simple pole at u_substrate. **These three are converging structural infra** — but no single document codifies the *pre-flight checklist* a new probe must clear before launching. This doc fills that gap and consolidates the now-closed 1+2-factor saturated search (PR #1831, 1309 NEGATIVE candidates) as a refuted-class record.

---

## 1. The closed search spaces (do NOT re-run)

Two combinatorial sweeps have **saturated** at the proton-anchor real-q level and are now refuted classes (`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md` rows C1 + C2):

| sweep | scope | result | evidence |
|---|---|---|---|
| **1-factor** | 28 enumerated single forms `f(q)` (incl. `J−ℏ²`, `[3]_q/25`, q-rationals, knot invariants) | **all REFUTED** at proton+muon cross-anchor (rigidity `dc_3/dq ≈ 4.6×10⁶`) | PR #1831 (refuted-class C1) |
| **2-factor composite** | 1281 candidates `f₁(q) · f₂(q)` (Cartesian product over the 28 + auxiliary) | **all REFUTED** — best proton matcher (`q² + q⁻² − [4]_q`) misses muon by **14×** | PR #1831 (refuted-class C2) |

**Total:** 1309 candidates exhaustively scanned at the proton+muon cross-anchor; **NONE survive**.

**Standing rule:** Any new probe proposing a c_3 form of shape `f(q)` or `f₁(q) · f₂(q)` over real q is **already in a refuted class** — cite the corresponding row from the refuted-class map and DO NOT re-run. The exhaustive nature of the 1+2-factor sweep makes this unambiguous; the next productive search is fundamentally different (3+-factor composite, fibre-level cyclotomic / root-of-unity, or operator-level decomposition).

---

## 2. The four §4 invariants any new F(q) candidate must satisfy

Per the refuted-class map §4 (formalize-first gate), any candidate Habiro element `F(q)` for the Q_β precision ladder must clear **all four** structural invariants **before** the numerical anchor sweep runs:

| # | invariant | source | formalised in |
|---|---|---|---|
| **(a)** | **Anchor-stable** — cross-anchor `u_substrate` swing < 1 ppm (10⁻⁶ relative; 210 ppb observed proton/muon at PR #1727 fibre-level tolerance) | refuted-class §4(a), PR #1727 | **this PR (Track 2)** ✓ ([`prop:q-beta-radius-of-convergence-gate`](../../content/quantum-observable-universe/mass-theory/q-beta-radius-of-convergence-gate.md)) |
| **(b)** | **Bar-even** under `q ↦ q⁻¹` (equivalently, even in `t = q − 1` Taylor) | refuted-class §4(b) | **PR #1875** ✓ ([`prop:q-beta-bar-even-kernel-invariant`](../../content/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-invariant.md)) |
| **(c)** | **q = 1 shadow** reproduces the known integer (e.g. `c_3 → J_Hopf(1) = −2`) without fitting | refuted-class §4(c) | TODO |
| **(d)** | **Direction sanity** — `\|F(q_0)\|` and any scaling factor must respect the target's magnitude | refuted-class §4(d), PR #1850 | TODO |

**This PR adds invariant (a)** via Track 2 (radius-of-convergence gate, see [`prop:q-beta-radius-of-convergence-gate`](../../content/quantum-observable-universe/mass-theory/q-beta-radius-of-convergence-gate.md)): the simple-pole-at-u_substrate condition from PR #1727 IS a sharp anchor-stability invariant (210 ppb cross-anchor shift). A candidate `F(q)` whose `g(u) := Σ c_k u^k` has its nearest singularity elsewhere than `u_substrate` fails the radius-of-convergence ratio test `c_{k+1}/c_k → 1/u_substrate` and must be REJECTED.

**Future PRs** are expected to add (c) (q=1 classical-limit shadow check) and (d) (direction-sanity invariant per #1850's `z(q₀) < 1` obstruction).

---

## 3. The Δ_λ pre-flight checklist (canonical workflow for new probes)

Before running any new probe attempting to derive a c_k, a kernel `R(q,ξ)`, or a Habiro element `F(q)`, walk this checklist **in order**:

### Step 1 — Corpus-grep (backward pruning)

Per AGENTS.md §"Before declaring open math", check:

```bash
grep -rln <topic> docs/audits/        # owner-authorised resolutions
grep -rln <topic> content/            # whole tree, cross-chapter
grep -rln <topic> computations/  # implemented Python
```

If any of these hit, the work may already exist. Cite the prior result instead of re-deriving.

### Step 2 — Refuted-class check

Open [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) §2. Walk the C1–C12 rows. If the proposed approach matches a refuted class (or the saturated 1+2-factor search above), STOP — add a new §2 row if the proposal is a genuine new variant; do NOT re-run.

### Step 3 — Bar-even check (§4(b), PR #1875)

State the candidate as a power series in `t = q − 1` or as `f(q, q⁻¹)`. Apply the bar-involution `q ↦ q⁻¹`. If `Δ := F(q, q⁻¹) − F(q⁻¹, q)` is non-zero identically (as an element of the ring), the candidate has odd-in-`t` content and **cannot** produce a clean integer-`u` ladder.

**Tooling:** [`qbeta_bar_even_kernel_invariant_probe.py`](../../computations/qbeta/qbeta_bar_even_kernel_invariant_probe.py) is the working template; copy + parameterize for new candidates.

### Step 4 — Radius-of-convergence check (§4(a), this PR Track 2)

Compute the nearest pole of `g(u) = Σ c_k u^k` (the log-correction generating function). If `|u_pole − u_substrate| / u_substrate > 1e−6` (the established fibre-level tolerance from PR #1727), REJECT the candidate.

**Tooling:** [`qbeta_radius_of_convergence_gate_probe.py`](../../computations/qbeta/qbeta_radius_of_convergence_gate_probe.py) is the rational-function singularity locator with mpmath verification.

### Step 5 — q = 1 classical-limit shadow (§4(c), TODO)

Evaluate the candidate at `q = 1` (or compute the limit if there's a removable singularity). Check that integer-valued shadows reproduce the known anchors (`c_2 → −1`, `c_3 → −2 = J_Hopf(1)`). A candidate failing this is structurally inconsistent with the [registry §3](../coordination/ck-dk-canonical-registry.md) seeds.

### Step 6 — Direction sanity (§4(d), TODO)

Verify `|F(q_0)|` is in the same order of magnitude as the target observable. Per PR #1850's `z(q_0) = 0.4993 < 1` obstruction: a scaling factor that cannot multiply up to the target's magnitude (`linking_weight > 1` in that case) is automatically refuted.

### Step 7 — Only now: run the numerical anchor sweep

If all six prior steps pass, the candidate IS in the surviving hypothesis class and the numerical sweep at proton + muon anchors is informative. If any prior step fails, add a new row to the refuted-class map §2 and STOP.

---

## 4. What this PR ships

1. **Track 3 (this doc)** — consolidation of refuted-class status (1+2-factor saturated) + the 7-step Δ_λ pre-flight checklist.
2. **Track 2 (sibling commits)** — the radius-of-convergence gate as a proper proposition triple + sympy probe, formalising §4(a).
   - `prop:q-beta-radius-of-convergence-gate`
   - `qbeta_radius_of_convergence_gate_probe.py`

Together with PR #1875's bar-even gate and PR #1839's `CFinite` engine, this completes **two of the four §4 invariants** as formalized Lean lemmas. The remaining two (q=1 shadow, direction sanity) are flagged as TODOs for future PRs and live in `docs/coordination/1ppq-qbeta.md` as queue items.

---

## 5. Standing rules (discipline)

- **Run the 7-step checklist before every new probe.** Sub-skips waste compute; sub-runs into refuted classes waste reviewer attention.
- **Add a new refuted-class row** when a new probe surfaces a structurally new obstruction (do NOT silently note it in the witness JSON; the refuted-class map is the canonical record).
- **Per-rung status changes go to the registry**, never here. This doc records *checklist steps* and *invariant scaffolding*; the registry records *tiers*.
- The actual `F(q)` kernel construction (the open keystone) remains **owner-gated multi-session research** per refuted-class map §5. The pre-flight checklist + the four §4 invariants make any future kernel proposal *easy to evaluate*; they do NOT construct the kernel itself.

---

## 6. Cross-references

- **Refuted-class map:** [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
- **c_k/d_k canonical registry:** [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
- **u_substrate simple-pole proof:** [`2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`](2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md) (PR #1727)
- **Bar-even gate (PR #1875):** [`prop:q-beta-bar-even-kernel-invariant`](../../content/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-invariant.md)
- **CFinite recurrence engine (PR #1839):** [`RationalCoeffRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/RationalCoeffRecurrence.lean)
- **c_2 = −1 structural seed (PR #1786):** [`prop:q-beta-c-2-eq-neg-one-structural`](../../content/quantum-observable-universe/mass-theory/q-beta-c-2-eq-neg-one-structural.md)
- **Master 1ppQ ledger:** [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
