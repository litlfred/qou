# Workplan-0b/M_N — substrate derivation of the nucleon-mass anchor

**Date opened**: 2026-05-18
**Originating PR**: #696 (D3 — wire flavor-split-substrate)
**Status**: HANDOFF — ready for a fresh agent to pick up
**Estimated effort**: 2–4 days (one focused researcher PR + Lean
formalisation)
**Risk class**: MEDIUM — does not affect the splitting derivation
already wired by PR #696; only refines the M_N anchor's calibration
status from CLASS-A to derived.

## TL;DR for the new agent

PR #696 wired `prop:flavor-dressed-mass-from-substrate-split`,
which derives the n − p splitting `μ_d − μ_u = M_N · S(q)` from
the substrate parameter `q_0` and the universal nucleon-mass scale
`M_N`.  **`M_N` itself is still anchored on CODATA** (specifically,
`M_N = (m_p + m_n)/2` consumed via the `M_P_MEV_VALIDATION` /
`M_N_MEV_VALIDATION` constants in `computations/substrate/codata_constants.py`).

This leaves a **CLASS-A acknowledged-stub** at the M_N anchor: the
splitting is substrate-pure, but the scale isn't.  Your job is to
provide a substrate-pure derivation of `M_N` so the entire
flavor-splitting chain reduces from 3-CAL (m_e + q_0 + M_N) to
the canonical 2-CAL form (m_e + q_0; M_N derived, Q_β remains a
separate calibration).

## Reading order

1. **`prop:flavor-dressed-mass-from-substrate-split`** —
   [content/quantum-observable-universe/braids-and-knots/flavor-dressed-mass-from-substrate-split.md](../../content/quantum-observable-universe/braids-and-knots/flavor-dressed-mass-from-substrate-split.md).
   Statement of the splitting; M_N appears as an external scale.
2. **Phase 1 audit doc** —
   [docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md](2026-05-10-workplan-0b-script-rewire-handoff.md).
   The broader Workplan-0b context: m_p, m_n as CODATA inputs is a
   3 → 9 calibration over-count.  Your M_N derivation closes one
   slice of that.
3. **Three-calibration discipline** —
   [`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)
   states the framework target: every observable factors as
   $m_e^a \cdot Q_\beta^c \cdot \hat{\mathcal{O}}(q_0)$.  M_N must
   factor this way too.
4. **The probe** —
   [`computations/probe_flavor_dressed_mass_split.py`](../../computations/probe_flavor_dressed_mass_split.py).
   See lines 9–22 for the explicit Class-A banner you are tasked
   with retiring.

## Target form

You're looking for a substrate-pure formula

```
M_N(q_0, m_e, Q_β) = m_e^a · Q_β^c · M_N̂(q_0)
```

where `M_N̂(q_0) ∈ ℚ(q_0)` (Laurent in `q_0^{±1/2}` per
`prop:three-calibration-inputs`) and `(a, c) ∈ ℤ²_{≥0}` with
`a + c = 1` for dimensional homogeneity (M_N is a mass).

Equivalently: a categorical or topological expression for the
nucleon scale in terms of the substrate.

## Candidate routes (rank by tractability)

### Route A — proton mass via Borromean Skein (already partial)

The proton mass `m_p` already has structural pieces on main:
- [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md)
  — LO piece $\rho_K = Z m_p + N m_n + Z m_e$ via Markov
  multiplicativity (Wenzl 1988 Thm 5).
- [`prop:m-p-borromean-verification-50dps`](../../content/quantum-observable-universe/braids-and-knots/m-p-borromean-verification-50dps.md)
  — 50-dps Borromean cross-check.
- [`conj:lambda-scale-substrate-form`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.md)
  — $\lambda_{\mathrm{scale}} = 5/2 - h^2 G$ at 5.4 ppm
  (justification, not derivation per audit §13).

If `m_p` reaches substrate-pure form, then per the framework's
beta-decay relation (`Q_BETA_MEV = m_n − m_p − m_e` in
`computations/substrate/codata_constants.py`) the neutron
mass is `m_n = m_p + m_e + Q_β`, so

```
M_N = (m_p + m_n) / 2
    = (m_p + (m_p + m_e + Q_β)) / 2
    = m_p + (m_e + Q_β) / 2
```

is also substrate-pure (m_e is CAL-1, Q_β is CAL-3 — both are
already in the canonical 3-input scheme; no 4th calibration is
introduced).

**Open piece**: closing the Skein resolution of the Borromean
braid (the OPEN item in the existing `calibration-inputs.md`
docstring).  This is the same open piece tracked in
`docs/audits/2026-05-17-1ppb-workplan-v4.md`.

### Route B — categorical mass from Frobenius trace

The categorical-mass framework
([`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md))
expresses `m̃(X)` as a Frobenius trace on the categorical-action
algebra.  The nucleon mass scale is then the Frobenius trace of
the proton (or neutron) braid representation — a structural
quantity, not a calibration.

**Open piece**: making the Frobenius trace categorically explicit
for the proton/neutron Borromean configurations.  The trace's
value at `q_0` should match `m_p(q_0)` to whatever precision the
substrate parameter is known.

### Route C — Bring zero-mode / Euler-class anchor

The Bring-surface zero-mode derivation
([`prop:em-coupling-bring-zero-mode`](../../content/quantum-observable-universe/descartes-universe/em-coupling-bring-zero-mode.md))
fixes α_EM additively from the Euler characteristic.  An analogous
Euler-class anchor for the nucleon mass would fix M_N from the
substrate parameter alone.

**Open piece**: identifying the right characteristic class
(probably the secondary characteristic for the nucleon braid
group, not the Bring surface's primary class).

## Test plan for the resulting derivation

Whatever route lands, the derivation must satisfy:

1. **Numerical match at q_0**: `M_N(q_0) ≈ 938.918 MeV`
   (current value from `(m_p + m_n)/2`); residual ≤ 1% or
   explicitly conditional on a known correction.
2. **Substrate-pure**: no CODATA mass appears as an INPUT.  M_N
   may appear in `_VALIDATION` form as a comparison target.
3. **Lean formalisation**: a `theorem nucleon_scale_substrate :
   M_N = m_e^a * Q_β^c * <expression in q>` in
   `content/quantum-observable-universe/lean/QOU/...` with at
   most a `sorry` for the calibration-
   independent Skein resolution (or whichever upstream piece is
   itself still open).
4. **Probe witness**: a `probe_M_N_substrate.py` script under
   `computations/` emitting
   `M-N-substrate.witness.json` with three assertions:
   - `substrate_closure_vs_codata_within_X_pct` (X depends on
     route; aim for ≤ 1%)
   - `derivation_uses_no_4th_calibration` (boolean predicate
     auditing the production-side absence of fourth CAL input)
   - `dimensional_homogeneity` (boolean — confirms (a, c) ∈ ℤ²
     with a + c = 1)
5. **canonical-script-input-audit re-classification**: after
   wiring, the audit (per PR #733) should reclassify the
   substrate-splitting consumers from
   `3-input-canonical-with-substrate-splitting` (CLASS-A M_N) to
   `2-input-canonical` (m_e + q_0; Q_β tracked separately).

## What NOT to do

- **Do not** introduce a 4th calibration (e.g. PDG nucleon-scale
  value, AME proton mass, hyperbolic-volume fit, magic-number
  pinning).  That defeats the purpose.
- **Do not** delete the existing `_VALIDATION` constants in
  `codata_constants.py`.  They stay as comparison targets even
  after the substrate derivation lands.
- **Do not** bundle this with downstream wiring.  Land the
  substrate-pure derivation first; the production-side rewire
  (consumer scripts replacing `M_N_MEV_VALIDATION` with the
  substrate witness) is a separate Phase 5 follow-up.

## Branch + PR conventions

- Branch name: `claude/iw-compute-m-n-substrate-derivation` per
  the `claude/iw-<TYPE>-<STUB>` convention from PR #722.
- One PR per route attempt (don't pre-bundle attempted-and-failed
  routes).  Falsified attempts become `rem:*-falsified` blocks
  per AGENTS.md §3a/§3b.
- Coordinate with PR #696 author (this session) on the M_N
  CLASS-A banner retirement; the probe docstring at lines 9–22
  is updated once the substrate derivation lands.

## Acceptance criteria

Workplan-0b/M_N is **closed** when:

1. A `prop:nucleon-scale-substrate-form` (or equivalent label)
   exists with substrate-pure derivation + Lean formalisation.
2. `probe_M_N_substrate.py` emits a witness gating closure vs
   CODATA within 1%.
3. `probe_flavor_dressed_mass_split.py`'s docstring CLASS-A
   banner is retired (replaced by an `interprets:` link to the
   new M_N derivation).
4. `canonical_script_input_audit.py` reclassifies consumers to
   `2-input-canonical`.
5. PR #696's Phase plan table is updated: "Phase 5 — M_N
   substrate derivation — landed".

## Coordination

- Subscribe to PR #696's discussion if reopening that PR's audit.
- Open coordination comment on any in-flight `derive_m_p_*` /
  `atomic_mass_via_rho_k.py` PR — your route A overlap will need
  cherry-pick coordination per AGENTS.md `local/coordinate` §3.
- Use the integration-watcher branch convention
  (`claude/iw-compute-...`) for any spawned sub-PRs (Lean stub,
  probe wiring) so they're discoverable via the
  `claude/iw-` infix.
