# Jackson q-Borel / Écalle acceleration of the bar-odd D-ladder

**Date:** 2026-07-17 · **Branch:** `claude/dladder-qborel-acceleration-2026-07-17` ·
**Tier:** exact-arithmetic (2-adic transport) + high-precision measurement
(acceleration numerics) · **Scope:** (a) throughout — no `c_k` wired, no fit to
QOU observables, no tier change, nothing to production.

Takes up the single named odd-channel problem of the
[1ppQ path reassessment](2026-07-17-1ppq-path-reassessment.md) §"Non-duplicative
next-work options" item 1: the **Jackson q-Borel / Écalle acceleration of the
exact D-ladder** `D(ũ) = Σ_k d_k ũ^k`, `d_k = a_k + b_k√3 ∈ ℚ(√3)` (KC21/KC22,
[registry](../coordination/ck-dk-canonical-registry.md)). KC22 closed the entire
(q-)holonomic search class (none of it is re-run here); the
[07-13 finding](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md)
is that the ladder is **q-Gevrey with no single classical Gevrey index**, so the
correct machinery is the q-Borel / acceleration family, not plain Borel (the
plain `÷k!` negative is already recorded there).

## §1. Hypothesis class, closure, and refutation criteria (pre-registered)

**Object accelerated.** The exact bar-odd D-ladder coefficients `d_k ∈ ℚ(√3)`
(k = 1…21 from the ORD-43 build in
[`qbeta_dladder_generating_function_structure_probe.py`](../../computations/qbeta/qbeta_dladder_generating_function_structure_probe.py);
the ORD-63 extension arm of the
[three-front specs](2026-07-17-three-front-attack-specs.md) §1 targets k ≈ 31).
Equivalently the odd carrier of `S = h·D(ũ)` (KC21) — the Φ_b state-integral
odd face.

**Hypothesis class.** There exists a member of the two-parameter
q-Borel/Borel–Leroy acceleration family

$$\mathcal{B}_{Q,s} : d_k \;\longmapsto\; b_k = \frac{d_k}{([k]_Q!)^{\,s}},\qquad
[k]_Q! = \prod_{j=1}^{k} \frac{Q^j - 1}{Q - 1},$$

(with the classical Borel–Leroy `(k!)^s` as the `Q → 1` boundary and the Jackson
`÷(Q;Q)_k` transform equal to `÷[k]_Q!` up to the geometric factor `(Q−1)^k`,
which only rescales the Borel variable) such that the transformed series has a
**finite, estimator-consistent radius** — i.e. the dlog-Padé singularity and the
root-test radius agree — making the singularity location (the would-be instanton
action / Stokes datum) measurable, and the q-Laplace back-transform
reproduces the meridian data.

**What closure would mean.** A convergent q-Borel-resummed value for the odd
channel at the substrate meridian reproducing the `S(q)` data at the c₃ level,
with the singularity structure identified (a derived action, feeding the GGM
Stokes-integer route on #3805) — as a **candidate** with cross-anchor swing
measured, never a wired constant.

**What refutes (scope-(a), pre-registered).**

1. If **no `(Q, s)` in the scanned family** yields estimator-consistent
   summability at accessible k, the finding is "the acceleration family at
   k ≤ K_max does not resolve the singularity" — a scope-(a) negative on the
   *family at this order*, not on the resurgent reading.
2. If the **2-adic bar-parity grading** (anchor A1,
   `QOU.QBeta.DLadderTwoAdicGrading.bDen_two_adic_graded`) is transported by
   the transform in a way that *forbids* the resummation shape, that is a
   structural finding classified per the (a)/(b) rubric with the invariant
   named (§2).
3. If the back-transform at the meridian **disagrees** with the direct partial
   sums (which converge there — the divergence is asymptotic, far from optimal
   truncation at ũ(q₀) ≈ 0.0095), the implementation is wrong, not the math —
   a mandatory self-check, not a physics refutation.

**Anchors used as cross-checks (both exact, both in hand).**

- **A1 — 2-adic bar-parity grading:** `v₂(den b_k) = 0 ⟺ k` odd, Lean-anchored
  window `K = 5` (`bDen_two_adic_graded`;
  [`DLadderTwoAdicGrading.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DLadderTwoAdicGrading.lean)),
  exact to k = 21, `p = 2` the unique graded prime.
- **A2 — q\* (the S = 0 point):** `q* = 1.10997859303152…`, the third
  decay-sector determination of q₀
  ([`qbeta-c3-imq-qstar-ladder-amplification.witness.json`](../../computations/qbeta/qbeta-c3-imq-qstar-ladder-amplification.witness.json));
  `S′(q*) = 2.37 × (1/u³)` — smooth zero, ladder-inversion amplified (KC21).

## §2. Structural invariant before wide compute — 2-adic transport (STATUS: see results)

Formalize-first step: any member of the scalar acceleration family acts
**diagonally** on the ℚ(√3) components — `a_k ↦ a_k/f_k`, `b_k ↦ b_k/f_k` with
the *same* scalar `f_k ∈ ℚ^×` (`f_k = ([k]_Q!)^s`, `s ∈ ℤ` for exactness). Hence
for the 2-adic valuation `v₂` on ℚ:

$$v_2(a_k/f_k) - v_2(b_k/f_k) \;=\; v_2(a_k) - v_2(b_k)\qquad\text{(exactly, for every scalar } f_k).$$

The **signed component gap** `g_k = v₂(a_k) − v₂(b_k)` is therefore invariant
under the *entire* scalar q-Borel/Borel–Leroy/acceleration family — the ℤ/2
grading, in gap form, survives into every accelerated plane. The **absolute**
law (`v₂(den b_k) = 0` on odd k) transforms by `−v₂(f_k)` and survives only for
2-adically unit bases. Probe:
[`qbeta_dladder_qborel_2adic_transport_probe.py`](../../computations/qbeta/qbeta_dladder_qborel_2adic_transport_probe.py)
(exact; results §4).

## §3. The acceleration numerics (results §5)

Probe:
[`qbeta_dladder_jackson_qborel_acceleration_probe.py`](../../computations/qbeta/qbeta_dladder_jackson_qborel_acceleration_probe.py)
— the `(Q, s)` summability surface, dlog-Padé vs root-test consistency across
the locus, q-Laplace back-transform meridian self-check, and the A2 cross-check.

## §4. Results — 2-adic transport (exact)

*(pending run)*

## §5. Results — acceleration scan

*(pending run)*

## §6. Tiered verdicts

*(pending)*

## Cross-references

- Reassessment: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md);
  specs: [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md) §1.
- Exact ladder + grading: [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md)
  (incl. the §Resummation-note plain-Borel negative and the Borel–Leroy order scan).
- Registry rows: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) KC21/KC22.
- Divergence class: [`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md);
  Écalle framing: [`2026-07-13-alien-calculus-surreal-integration-review.md`](2026-07-13-alien-calculus-surreal-integration-review.md).
- Q_β ledger: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
