# Triage: qCLT wiring, q-Lommel→Δ_λ, and the low-isotope mass-table re-witness (2026-06-14)

**Context.** Session picked up a stalled work-plan whose menu offered three
items: (1) re-witness the low-isotope mass table, (2) resume q-Lommel→Δ_λ,
(3) resume qCLT `m_qCLT_approx` compute wiring. This doc records the
read-only triage verdicts so the next session does not re-investigate.
All three are governed by the corpus-grep / formalize-first disciplines:
**both research items are confirmed gated, so the verdict itself is the
deliverable — no compute was burned on them.**

## Item 3 — qCLT `m_qCLT_approx` compute wiring: **OPEN-AND-GATED**

The two-channel mass split in
[`mass-theory/q-clt-jsj-mass-scaling.md`](../../content/quantum-observable-universe/mass-theory/q-clt-jsj-mass-scaling.md)
(lines 7–15) announces:

- `m_symbolic` — exact Hecke-trace evaluation, light isotopes (A ≤ 8);
- `m_qCLT_approx` — asymptotic limit via JSJ volume additivity.

**Channel 2 is wired to nothing.**

- **No compute.** No script in `computations/` computes
  `m_qCLT_approx` or evaluates JSJ-volume-additivity → mass. The 23
  files matching `qclt|q_clt|jsj|blitvic` are exploratory probes
  (e.g. `delta_lambda_jsj_phase3.py`,
  `probes/difference_knot_jsj_classification_probe.py`), not a
  channel-2 producer. The mass-table scripts
  (`canonical_mass_table_extended.py`, `atomic_mass_via_rho_k.py`)
  compute **only the symbolic channel, A ≤ 8**.
- **No witness.** No `*.witness.json` carries an `m_qCLT_approx` column
  or any A > 8 prediction.
- **Lean is structural only.**
  - `QOU/Observations/hecke_satisfies_blitvic_hypothesis.lean` — `sorry`
    stub; comment says the stub exists only so the `lean.ref` resolves.
  - `QOU/Observations/QCltNonCommutative/QCltNonCommutative.lean` —
    conjecture class; the single `sorry` on the `noncomputable instance`
    **is** the conjecture (intended per AGENTS.md §3b), not a missing proof.
  - `QOU/BraidsKnots/LinearJSJVolume.lean` — `axiom JSJ_volume_additivity`
    (line 28) + structural theorem `atomic_volume_is_linear`; **no method
    to compute** Vol_p, Vol_n, or Vol(K).
- **Ledger.** [`docs/coordination/cfs-q-clt.md`](../coordination/cfs-q-clt.md)
  is about the Chapter-7 CFS/q-CLT *structural formalization* (PR #653,
  Issue #649) — GNS embedding, Plancherel skeleton, non-comm probability
  dictionary. **No** mention of an `m_qCLT_approx` compute channel.

**Blocker (original triage).** A full SnapPy-grade hyperbolic-volume
solver is research-scope. **But** the *leading* term does not need it.

**Update (this PR): channel 2 is now wired.** The JSJ-additive leading
term `m_qCLT_leading(Z,N) = Z·m_p + N·m_n` needs only the framework's
existing predicted nucleon masses — no volume solver — and the binding
correction `B(Z,N)` is exactly the Δ_λ term (Item 2). Wired in
[`m_qclt_approx.py`](../../computations/m_qclt_approx.py)
→ witness `m-qclt-approx.witness.json` (3 assertions, all pass):

- The binding-corrected channel `Z·m_p + N·m_n − B` reproduces the CODATA
  atomic mass of D/T/³He to **within the nucleon-mass gap**, *uniformly*
  across isotopes — the JSJ-additive **structure is sound**. The gap is the
  proved-pipeline **+2.89 %** (2.892–2.906 %, spread 0.014 %); the derived,
  no-fit spectral-phase correction θ/(8ℏ²)≈0.9711 reduces it **34.9×** to
  **~−819 ppm** but is *exploratory/unwired* (per
  `docs/audits/2026-05-28-spectral-phase-correction-derived.md`). The
  witness reports **both** regimes, so the residual is transparently the
  nucleon-mass-gap status, not a floor of the channel.
- The leading term alone carries an extra, A-growing **binding-fraction**
  error (3.01→3.20 %) — so the remark's "exact asymptotic limit" is
  **false** and was corrected to "asymptotically linear structure;
  ~1 % absolute estimator". The Lean
  [`LinearJSJVolume.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsKnots/LinearJSJVolume.lean)
  was also fixed (removed-keyword `constant`→`axiom`; the vacuous
  self-`exact` theorem replaced by three genuine derivations:
  cluster-additivity + proton/neutron increments; lean-direct exit 0).

What remains gated is only the **absolute** accuracy: the nucleon-mass
gap (Subgoal-2, declined) and the binding model `B` for A > 8 (= Item 2).

## Item 2 — q-Lommel → Δ_λ: **OPEN-AND-GATED**

> **Update (2026-06-14): reduced to a derived-`b` near-match.** The
> *second-kind* order recurrence (not the argument recurrence this section's
> original NO was based on) gives a DERIVED coefficient
> `b = q₀¹⁰+q₀⁻¹⁰ = 2cosh(10η₀)` from the `q₀^(10A−5)` residual; two seeds then
> predict ⁴He to −3.5% with no fit (gate-respecting). Full synthesis +
> open keystone (derive `10A−5` from Bring's-surface crossings):
> [`2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md`](2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md).
> The paragraphs below record the *original* data-limited precheck framing.

The precheck **already ran**:
[`delta_lambda_qlommel_recurrence_precheck.py`](../../computations/delta_lambda_qlommel_recurrence_precheck.py)
→ witness
[`delta_lambda_qlommel_recurrence_precheck.witness.json`](../../computations/delta_lambda_qlommel_recurrence_precheck.witness.json).

- Verdict: *"INCONCLUSIVE / DATA-LIMITED (no fit attempted, per the Δ_λ
  gate)… DECISIVE TEST GATED on extending the same-shape Δ_λ tower to
  ⁶Li, ⁷Li, ⁸Be, …"*; `discipline: "… nothing wired"`.
- Concretely: current Δ_λ data is only 4 atoms / 3 A-levels (D, T, ³He,
  ⁴He). A three-term recurrence needs ≥ 4 same-shape levels to test the
  coefficient `b_ν`; with one interior point per single-isospin chain,
  nothing is falsified.
- Gate: AGENTS.md §"Δ_λ gate" — six ansätze have failed on the deuteron;
  **do not propose a seventh fit-based ansatz**. Productive directions
  are GAP-A-3 / GAP-A-4 / Option E, not a q-Lommel fit.

**Blocker.** Data-insufficiency, not a fixable algebra bug. The missing
input is the Subgoal-1 Borromean-tower per-isotope extension (⁶Li, ⁷Li,
⁸Be, …), a separate research workline. Any closure built now would be a
fit and violate the gate. **No bounded compute step** other than
confirming (by reading the tower lead PR) that the tower is the *only*
blocker.

## Item 1 — low-isotope mass-table re-witness: **canonical is timeout-degraded**

[`low_isotope_mass_table.py`](../../computations/low_isotope_mass_table.py)
is a thin wrapper: it **projects** `A ≤ 3` rows out of the shared
`canonical-mass-table-extended.witness.json`. The table should carry 5
atoms — `LOW_ISOTOPE_ATOMS = ["p", "n", "D", "T", "3He"]`.

Staleness check (this session):

| Field | Wrapper witness (on `main`) | Current canonical | Verdict |
|-------|------------------------------|-------------------|---------|
| `computedAt` | 2026-05-24 | 2026-06-13 | wrapper stale |
| `derived_from.scriptCommitSha` | `4f6074e9` (05-24 canonical) | `91114040` (06-13) | pointer drifted |
| `scriptHash` | `31a7877…` | current script `aba55d1…` | wrapper script changed |
| row count | **5** (p, n, D, T, ³He) | **2** (D + one A=3) | canonical regressed |

The wrapper witness *is* stale. **But** the canonical it projects from
has only 2 rows — and the canonical's own description says *"the actual
rows reflect what completed within the per-atom timeout."* So the 2-row
state is a **timeout artifact**, confirmed (not intended qCLT thinning —
Item 3 shows the symbolic channel is the only mass producer, A ≤ 8).

**Consequence.** A light reproject (`--no-rerun-canonical`) faithfully
copies the degraded canonical → a 2-atom witness that **drops the proton
and neutron rows** — not a valid "refresh the table." A faithful 5-atom
refresh requires **regenerating the shared canonical** for the 5 light
atoms, which (a) cascade-re-stales the canonical's downstream derived
witnesses and (b) raises a method-label question (the canonical was last
built with `--method branching`; the wrapper's default is `laurent_q`).
This is an architecturally significant change to shared state — recorded
here for an explicit decision rather than done unilaterally. The 05-24
witness retains the correct 5-atom physics in the meantime.

## Net

| Item | Verdict | Tractable now? |
|------|---------|----------------|
| 3 — qCLT `m_qCLT_approx` | **leading term WIRED** this PR (structure validated, "exact" overclaim corrected); only absolute accuracy gated | partial — leading done; binding correction `B` = Item 2 |
| 2 — q-Lommel → Δ_λ | **near-match via DERIVED b** (2026-06-14): second-kind order recurrence, `b = q₀¹⁰+q₀⁻¹⁰ = 2cosh(10η₀)` from `q₀^(10A−5)`; two-seed predicts ⁴He −3.5%, no fit; Lean `two_root_geometric` | partial — structure + derived `b` done; open keystone = derive `10A−5 = 5(2A−1)` from Bring-surface crossings + the Z-correction. See [`2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md`](2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md) |
| 1 — low-isotope re-witness | canonical timeout-degraded to 2 rows | yes, but requires regenerating the shared canonical (decision pending) |
