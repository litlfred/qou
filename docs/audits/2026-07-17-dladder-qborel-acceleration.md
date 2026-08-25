# Jackson q-Borel / Écalle acceleration of the bar-odd D-ladder

> **🛑 PREMISE CORRECTED 2026-08-09 — the D-ladder is CONVERGENT; there is no
> acceleration to perform.** This document's framing (Jackson q-Borel / Écalle
> acceleration of a *divergent* bar-odd ladder) rests on a divergence the ladder
> does not have. `D(ũ)` is convergent with radius
> `ρ = ũ(q*_ρ) = 0.142799996644689…`, the image of a **`Q_b` zero**
> (`q*_ρ ≈ 1.48989`, the real root > 1 of an irreducible degree-12 factor of the
> `Δ_net` numerator) that the 2026-07-12 singularity search omitted; `κ = 0`.
> See [`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md)
> and registry row **KC22**. Consequently there is **no instanton action, no
> Borel-plane singularity to locate, no Stokes constant to extract, and no
> Écalle resummation to perform**.
>
> **What survives.** The K1 measurement stands as data — and is now *explained*:
> a divergence-class estimator cannot converge on a convergent series, so
> "the gate fails at every Borel–Leroy and Jackson setting" is the expected
> reading of `κ = 0`, not a finite-`k` shadow. The large-order law is fixed with
> no free parameters by the single logarithmic branch point:
> `d_k = −(1/(2h*_ρ))·ρ^{−k}/k·(1 + O(1/k))`, `h*_ρ = q*_ρ − 1/q*_ρ = 0.818706471352`.
>
> **What is withdrawn.** The reading of the gate failure as a finite-`k` shadow
> resolvable by longer ladders or by a genuine multi-level acceleration kernel,
> and any implication that such a kernel exists to be found. Nothing here was
> wired; no `c_k` tier changes.

> **Independent replication:** a second implementation
> ([`2026-07-17-dladder-ecalle-acceleration.md`](2026-07-17-dladder-ecalle-acceleration.md),
> `qbeta_dladder_ecalle_acceleration_probe.py`) reproduces this document's K1
> headline — the estimator gate fails at every Borel–Leroy AND exponent-order
> Jackson setting at k = 21, so the finite-k shadow is double-confirmed.
> **Open discrepancy (ADJUDICATED 2026-07-17, bean qou-ffxw):** on the parity
> split this document reports the branches unresolved, while the replication
> finds each parity subseries individually gate-passing at its own per-parity
> slope-zero order in the w = ζ² plane (odd ρ_ζ ≈ 0.152, even ≈ 0.254).
> **Verdict: undecidable-at-k21** — probe
> [`qbeta_dladder_parity_adjudication_probe.py`](../../computations/qbeta/qbeta_dladder_parity_adjudication_probe.py)
> (witness [`qbeta-dladder-parity-adjudication.witness.json`](../../computations/qbeta/qbeta-dladder-parity-adjudication.witness.json))
> ran both methods on the same exact d_k. **This document's "unresolved" is the
> RAW dlog-Padé low bias, not a real absence of structure:** the flip localizes
> to the conformal map — raw dlog-Padé at the *replication's own* per-parity s\*
> still fails (raw Padé ≈ 2× below the root-test radius, this document's ARM-2
> "branch-cut-biased-low" signature), while the conformal-mapped estimator
> passes (C4b). The replication's gate is **not** self-referential (seed-invariant
> to ~1e-13, C4a) and its radii are stable (C3). BUT neither reading is
> established: on same-length convergent synthetics the short-series conformal
> estimator is biased ~30% high (C1a) and mis-recovers planted distinct-parity
> singularities (C2), so the 40%-split cannot be certified as ℤ/2 structure at
> k = 21. Deferred to the ORD-63 / k ≈ 31 extension. See §5 ARM 3 and the
> 1ppq-qbeta ledger. Neither reading is wired anywhere.

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

## §4. Results — 2-adic transport (exact; all 6 witness assertions pass)

Probe run at k = 1…21
([`qbeta-dladder-qborel-2adic-transport.witness.json`](../../computations/qbeta/qbeta-dladder-qborel-2adic-transport.witness.json)):

1. **Gap invariance — Lean-proved sorry-free.** The signed component gap
   `g_k = v₂(a_k) − v₂(b_k)` is exactly invariant under **every** scalar
   transform tested (classical `k!`, `[k]_2!`, `[k]_3!`, `[k]_{1/3}!`,
   `[k]_{1/2}!`, `(3;3)_k`) — and provably under the whole family:
   `QOU.QBeta.DLadderTwoAdicGrading.gap_invariant_under_scalar_transform`
   (`padicValRat.div` twice + `ring`; `lean`-direct exit 0 after lake-cache
   restore). The grading in gap form (`sign(g_k)` alternates with parity —
   verified exactly, `g_k` = −3, 4, −10, 9, −14, 15, …, −61) survives into
   every accelerated plane. **The invariant is PERMISSIVE: the 2-adic grading
   obstructs no q-Borel resummation shape** — the audit's kill criterion 2
   does not fire.
2. **The absolute law transports by `−v₂(f_k)`, computed exactly and matched
   to the LTE closed form.** It is preserved *verbatim* exactly by 2-adically
   **unit** bases — notably the **Jackson base-2 q-factorial** (`[j]_2 = 2^j − 1`
   odd for all `j`): the base matching the unique graded prime is the one
   whose q-Borel transform carries the absolute grading law unchanged. It is
   destroyed from `k = 2` on by classical `÷k!` (Legendre `v₂(k!) = k − s₂(k)`)
   and by base-3 factorials (`v₂([k]_3!) = Σ_{even j ≤ k}(1 + v₂(j))`).

## §5. Results — acceleration scan (k ≤ 21; witness all-pass)

Probe
([`qbeta-dladder-jackson-qborel-acceleration.witness.json`](../../computations/qbeta/qbeta-dladder-jackson-qborel-acceleration.witness.json)),
four arms:

- **ARM 1 — fixed-base class mismatch.** Transform-side growth is exact:
  `log [k]_Q! = (log Q)k²/2 + O(k)` for `Q > 1` (q-factorial), geometric
  `~ A^k` for `Q < 1`, `s·k·log k + O(k)` on the Leroy boundary `Q = 1`. The
  ladder grows like `exp(Bk + C·k·log k)` with small drifting `C` (KC22) —
  strictly between geometric and q-factorial. Numerically confirmed: every
  `Q > 1` (substrate q₀, 2, 3) over-accelerates (root-test slope < 0, tails
  falling — entire transform, **no singularity left to locate**); every
  `Q < 1` (1/2, 1/3) leaves the divergence untouched (slope rescaled by the
  geometric factor but strictly positive). **Only the Q → 1 Leroy boundary can
  match** — the "no single q-Gevrey index" of the 07-13 audit is mirrored by
  "no fixed Jackson base". Scope-(a): transform growth exact; ladder class is
  the triple-confirmed empirical finding, so this is a class-mismatch
  conditional on it, not a (b) exclusion.
- **ARM 2 — Borel–Leroy estimator gate: FAILS at every scanned `s ∈ [0, 0.40]`**
  (pre-registered 15% dlog-Padé/root-test consistency + Padé-window spread).
  The k = 21 inconsistency (ρ_Padé ≈ 0.15 vs ρ_root ≈ 0.26 at s\* ≈ 0.20)
  persists under the formalized gate — **the singularity is not resolved at
  k = 21; blocked on the ORD-63 extension terms** (sibling arm, three-front
  specs §1). *Observation (not a gate, not promoted post-hoc):* the merged
  conformal-mapped core (#3713) at s\* converges across [4/4]/[5/5] windows to
  **A ≈ 0.236 with 0.3% window spread**, within 9.5% of the root-test radius
  while raw dlog-Padé stays low — suggestive that raw Padé is the
  branch-cut-biased outlier; recorded for the extension arm to test.
- **ARM 3 — parity-split acceleration** (the 2-adic-grading-motivated
  decomposition, exact and commuting with every scalar `f_k`): gate 0/9 on the
  odd branch (11 terms), 0/9 on the even branch (10 terms) — unresolved at
  this depth too. **Adjudication (bean qou-ffxw, 2026-07-17):** this 0/9 is the
  **raw dlog-Padé low bias**, not an absence of structure — the sibling probe's
  conformal-mapped estimator passes both parities at their per-parity s\*, and
  the flip localizes to the conformal map (C4b). Verdict is
  *undecidable-at-k21* (the 40%-split is neither certified nor refuted at ~10–11
  coeffs/parity); see the top-of-doc adjudication blockquote and
  [`qbeta-dladder-parity-adjudication.witness.json`](../../computations/qbeta/qbeta-dladder-parity-adjudication.witness.json).
- **ARM 4 — back-transform self-check + A2.** The `Γ(1+sk)` Borel–Leroy
  back-transform reproduces the direct partial sums at the meridian to
  **2.5 × 10⁻²⁶** at both the muon-q₀ and the q\* (A2) points — machinery
  validated (kill criterion 3 clean). `D(ũ)` is **smooth and nonzero through
  q\*** (`D(ũ(q*)) ≈ D(ũ(μ)) ≈ −0.01667`): the S = 0 structural zero lives in
  the `h·D → S` bridge (the ord17 measured bridge ratio), not in the
  accelerated ladder — consistent with KC21's smooth-zero,
  ladder-inversion-amplified reading.

## §6. Tiered verdicts

| # | Finding | Tier |
|---|---|---|
| 1 | Gap form of the 2-adic bar-parity grading is invariant under the entire scalar acceleration family (`gap_invariant_under_scalar_transform`, sorry-free) | **proved-lean** |
| 2 | Absolute grading law preserved verbatim by 2-adically-unit bases (Jackson base 2), destroyed by `÷k!` / base-3; `v₂([k]_Q!)` matches LTE closed form | **structural-exact** (k ≤ 21 machine-checked; closed form verified) |
| 3 | The grading does **not** obstruct the q-Borel resummation (kill criterion 2 does not fire) | **structural-exact** (consequence of 1) |
| 4 | Fixed-base Jackson q-Borel (`Q ≠ 1` fixed) cannot resolve the D-ladder singularity: `Q > 1` entire / `Q < 1` no-op; only the Leroy boundary matches the `exp(Bk + Ck log k)` class | **scope-(a)** class-mismatch, conditional on the (triple-confirmed, empirical) divergence class; transform-side growth exact |
| 5 | Singularity not resolved at k = 21 under the pre-registered estimator gate (fails at every `s`); conformal core gives A ≈ 0.236 (0.3% window spread, 9.5% from root-test) as an **observation only** | **consistent-not-identified** / blocked on extension terms |
| 6 | Back-transform = direct partial sums to 2.5e-26 at both anchors; `D` smooth through q\* — the S = 0 zero is bridge-borne (A2 cross-check) | **measurement** (self-check clean) |

**No instanton action identified. No candidate value produced. No c₃ proposed.
Nothing wired.** The productive next step is mechanical: re-run ARM 2/3 (one
command, `argv[1] = 63`) on the extended `d_k` when the sibling ORD-63 arm
lands, with the conformal-vs-root observation as the specific thing the new
terms must confirm or kill.

## Cross-references

- Reassessment: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md);
  specs: [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md) §1.
- Exact ladder + grading: [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md)
  (incl. the §Resummation-note plain-Borel negative and the Borel–Leroy order scan).
- Registry rows: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) KC21/KC22.
- Divergence class: [`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md);
  Écalle framing: [`2026-07-13-alien-calculus-surreal-integration-review.md`](2026-07-13-alien-calculus-surreal-integration-review.md).
- Q_β ledger: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
