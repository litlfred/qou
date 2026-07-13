<!-- FILE_START: mba-sidecar-delta-lambda-closure.md -->
**Algorithm ($\Delta_\lambda$ closure — open gate).**
*Compute the per-partition binding density $\Delta_\lambda(K)$
for an isotope knot $K$, consumed by Step 9b
([`alg:per-isotope-binding`](#alg:per-isotope-binding)).*

### Input

- *Isotope knot $K$ + braid index $n_K$.*
- *Partition $\lambda \vdash n_K$.*

### Output

- *Per-partition density $\Delta_\lambda(K) \in \mathbb{R}$.*

### Closure obstructions

**Open gate.** Six closure ansätze have been refuted on the
deuteron:

| Ansatz | Source | Refuted on |
|--------|--------|------------|
| Frobenius co-Casimir | Track-A early proposals | deuteron |
| Demazure-fibre | symmetric-crystal early attempts | deuteron |
| LP-Plancherel | LP-based ansatz | deuteron |
| LP-Frobenius | LP-based ansatz | deuteron |
| crystal-graph naïve | KLR / Kashiwara level-0 | deuteron |
| augmented Markov | Markov-extension ansatz | deuteron |

The current direction is **Option E** (Kashiwara crystal, q-Reeb + isospin mirror — `option_e_v9.py`), with PROBE 4 cheap-pass refutation and the full-order $\theta_\lambda$ approach.

### Correctness conditions

*[`rem:term6-binding-density`](#rem:term6-binding-density)
fixes the binding sum's algebraic shape; the open piece is
identifying the categorical realisation of $\Delta_\lambda$.*

*[`conj:crystal-graph-realization`](#conj:crystal-graph-realization)
is the conjectural input under which Option E aims to close the
gate — its monotonicity property mirrors the cemetery-group
emergence pattern (Section: cemetery group).*

### Algorithm (current candidate — Option E v9)

```
1. Build the Kashiwara crystal for sl_{n_K} at the partition λ.
2. Apply q-Reeb deformation and isospin mirror.
3. Extract per-block volume + spectral data.
4. Combine into the Δ_λ candidate.
5. Cross-check against AME deuteron binding.
```

### Witness contract

*No verified witness yet — Option E v9 is candidate code, not
production. Cross-PR coordination tracked in
[`docs/coordination/2026-06-02-mba-appendix-maintenance-contract.md`](../../../docs/coordination/2026-06-02-mba-appendix-maintenance-contract.md).*

### Notes

*Per AGENTS.md \"$\\Delta_\\lambda$ gate (Track A blocker)\" rule: **do not propose a seventh fit-based ansatz**. The three-calibration discipline review will reject it. Productive directions include GAP-A-3, GAP-A-4 (categorical brane-tower level selection / $\\rho$ general rule) and Option E (Kashiwara crystal). Full context: [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../../../docs/audits/2026-05-18-delta-lambda-gating-context.md).*
<!-- FILE_END: mba-sidecar-delta-lambda-closure.md -->

<!-- FILE_START: mba-sidecar-mirror-cancellation.md -->
**Proposition (mirror-pair cancellation of the bar-even baseline).**
*Let $(Z, N)$ and $(N, Z)$ be a mirror pair at fixed mass number
$A = Z + N$, with crossing statistics of the atom braid word*
$$
\sigma + \sigma^{-1} = 10A - 2, \qquad \mathrm{avg} = 2A + 1, \qquad
w = \sigma - \sigma^{-1} = 4Z .
$$
*Then the two bar-even statistics are mirror-invariant,*
$(\sigma+\sigma^{-1})(Z,N) = (\sigma+\sigma^{-1})(N,Z)$ *and*
$\mathrm{avg}(Z,N) = \mathrm{avg}(N,Z)$, *while the writhe is the unique
distinguishing statistic,*
$$
w(Z,N) - w(N,Z) = 4(Z - N).
$$
*Consequently, for any binding-exponent deviation of the additive form
$f(Z,N) = \beta(A) + \zeta(Z-N)$ — an $A$-only baseline $\beta$ plus an
interface-imbalance term $\zeta$ — the mirror difference cancels the baseline
exactly:*
$$
f(Z,N) - f(N,Z) = \zeta(Z-N) - \zeta(N-Z).
$$

The two bar-even crossing invariants depend only on $A$ (the $Z$, $N$
coefficients cancel in $\sigma + \sigma^{-1}$ and in $\mathrm{avg}$), so they are
identical across a mirror pair; the bar-odd writhe $w = 4Z$ is the sole crossing
content that distinguishes the two members. The cancellation of $\beta(A)$ in the
mirror difference is therefore unconditional once the deviation is written in the
additive form $\beta(A) + \zeta(Z-N)$ — that separation is the only hypothesis,
justified by the mirror-invariance of the bar-even statistics and supplied (not
derived) as the additive-channel ansatz.

Thus, the observed mirror splits are clean numerical values ($\zeta(+1) - \zeta(-1) \approx -1.34$ for ${}^{3}\mathrm{He}/{}^{3}\mathrm{H}$, $\approx -1.77$ for ${}^{7}\mathrm{Be}/{}^{7}\mathrm{Li}$) even where absolute deviations are large and $A$-dependent. This holds even past the $A \le 4$ regime. The difference isolates the bar-odd $Z$-correction from the $A$-dependent baseline. The sign of $\zeta$ is fixed by the per-nucleon intra-$\mathcal{B}_3$ writhe asymmetry (proton $+3 >$ neutron $+1$); its magnitude is open and unfitted.
<!-- FILE_END: mba-sidecar-mirror-cancellation.md -->

<!-- FILE_START: mba-sidecar-isovector-chiral-residue.md -->
**Proposition (conditional on the keystone identification
`BWVacuumRowIsHecke`).**
*Let the binding residual's isovector (bar-odd) part be the chiral residue of the
$W_\lambda$ Plancherel measure $\mu(\lambda) = d_q(\lambda)^2/D^2$ — i.e. the
chiral part $\mathfrak{m}_{\mathrm{chiral}}$ of the categorical mass
([`chirality-residue-mass-term`](#prop:chirality-residue-mass-term)) carried by
the writhe's isovector content $2(Z-N)$ with chiral weight $\kappa$. Then the
isovector mirror difference is*
$$
b(Z,N) - b(N,Z) \;=\; 4\,\kappa\,(Z-N),
$$
*independent of the mass number $A = Z+N$; equivalently the per-isospin
coefficient $b = 4\kappa$ is fixed by the single keystone chiral weight $\kappa$.*

The bar-odd writhe $\sigma - \sigma^{-1} = 4Z = 2A + 2(Z-N)$ splits into an isoscalar part $2A$ and an isovector part $2(Z-N)$ with an $A$-independent slope ([`prop:mirror-baseline-cancellation`](#prop:mirror-baseline-cancellation)). The chiral residue is the Reeb-involution-odd ($\xi \mapsto -\xi$) content ([`archimedean-chirality`](#rem:archimedean-chirality)). The Bring surface supplies the chiral datum via the $A_5$ Galois twist $\sqrt{5} \mapsto -\sqrt{5}$ (keystone five-fold chirality). Therefore, the chiral weight $\kappa$ is the chiral part of the $W_\lambda$ Plancherel measure. Its value corresponds to the open keystone conjecture $\mathtt{BWVacuumRowIsHecke}$ ($\mathtt{bwS0}\,\lambda = d_q(\lambda)/D$).

**Consequence.** The binding-energy isovector closure is *not* an isolated problem. It derives from the **same** open conjecture as the $W_\lambda$ keystone. Once $\kappa$ is derived there, the binding coefficient $b = 4\kappa$ naturally follows. The empirical test then becomes the binding-side check that the isovector residual vanishes given the keystone chiral residue — a rigid, no-fit criterion. The value $\kappa$ emerges solely from the three calibrations and the keystone identification. It is never tuned to data (the measured $b \approx -1.75$ represents the *current error*, not a target).
<!-- FILE_END: mba-sidecar-isovector-chiral-residue.md -->

<!-- FILE_START: mba-sidecar-ck-truncation-ladder.md -->
**Algorithm ($c_k$ truncation ladder).**
*Compute the coefficients of the convergent $\mathfrak{Q}_\beta$ series
$\mathfrak{Q}_\beta = Q_{\mathrm{base}} \cdot \prod_{k = 2}^{N} (1 + c_k\, u^k)$
and report each $c_k$ with its **tiered classification**.*

### Input

- *Target precision $\varepsilon \in \mathbb{R}_{> 0}$.*
- *Substrate $q_0$ (CAL-2 anchor).*

### Output

- *Truncation order $N \geq \lceil \log_{10}(1/\varepsilon) / 2.07 \rceil - 1$.*
- *Tuple $\{(k, c_k, \mathrm{tier})\}_{k = 2}^{N}$ with tier one
  of `proved`, `near-match`, or `fitted`.*

### Tier classification (STRICT)

| $k$ | $c_k$ | Tier | Notes |
|---|---|---|---|
| 2 | $-1$ | **proved** | Taylor-exact, established |
| 3 | $-2 = J_{\mathrm{Hopf}}(q = 1)$ | **near-match** | swings $\leq 3.47\%$ at m_p-pin $q_0$ |
| $\geq 4$ | $q_0$-dependent | **near-match** | N=4→N=5 non-monotonicity is the experimental signature |
| any | empirical fit | **fitted** | flagged as discipline violation |

*Per AGENTS.md "$\mathfrak{Q}_\beta$ c_k is a TRUNCATION ORDER, not a wire/un-wire
gate", **never** report tiers as binary wired / dropped — always
tiered.*

### Algorithm

```
1. Choose N from target precision.
2. For k = 2:
   c_2 = -1   (proved).
3. For k = 3, …, N:
   compute c_k from the categorical-precision-ladder formula at q_0;
   classify as `near-match` if within 5% of a closed-form q=1
   limit, else as `fitted` and flag for discipline review.
```

### Correctness conditions

*[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
establishes the convergent ladder, the truncation-order
inequality, and the Taylor-exactness of $c_2$.*

### Python API entry point

*Canonical compute is the script
[`computations/q_beta_predicted.py`](../../../computations/q_beta_predicted.py),
which records each $c_k$ with its tier in the witness JSON.
Higher-precision regenerations use
[`build_cal_3_q_beta_witness.py`](../../../computations/build_cal_3_q_beta_witness.py).*

### Witness contract

*Canonical witness:
[`q-beta-predicted.witness.json`](../../../computations/q-beta-predicted.witness.json).
**Must** record each $c_k$ alongside its tier. The $\mathfrak{Q}_\beta$ subdir
ledger ([`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md))
maintains the flip-flop history table; any wire/un-wire decision
must update both.*

### Notes

*Permanent fix path is the $\mathfrak{Q}_\beta$ Habiro element parallel to
$\alpha_{\mathrm{EM}}$'s $[2]_q \cdot (1 - h^2 \alpha)$
(PR #1511). The $c_3$ flip-flop history (six entries as of
2026-05-31) is the canonical example of why tiered classification
is mandatory.*
<!-- FILE_END: mba-sidecar-ck-truncation-ladder.md -->

<!-- FILE_START: mba-sidecar-lp-sdp-dual-emission.md -->
**Algorithm (LP/SDP dual-emission contract).**
*Every LP / SDP / operator-selection compute must emit both
primal and dual variables in its witness JSON. This sidecar
documents the canonical contract enforced in CI.*

### Required witness fields

| Field | Meaning |
|-------|---------|
| `y0_star` | shadow price of the net constraint |
| `y_star` | shadow prices of Frobenius positivity constraints (≥ 0) |
| `active_set` (or `active_constraints` / `active_channels`) | indices $i$ with `y_star[i] > 0` |
| `primal_obj` | $\sum_i t_i x_i^*$ |
| `dual_obj` | $n_{\mathrm{target}} \cdot y_0^*$ (= `primal_obj` by strong duality) |
| `duality_gap` | $|\text{primal\_obj} - \text{dual\_obj}|$ |

### Canonical entry point

The shared solver helpers live at
[`tools/pyhecke/python/pyhecke/lp_dual_solver.py`](../../../tools/pyhecke/python/pyhecke/lp_dual_solver.py)
and expose `solve_operator_selection_lp(t, G, n_target)` and
`solve_psd_operator_selection_sdp(t, G, n_target)`. Both return a
result whose `.to_dict()` contains every required field. The
per-witness driver script is
[`confinement-operator-selection.py`](../../../computations/confinement-operator-selection.py).

### CI enforcement

[`computations/lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py)
runs in `witness-pipeline.yml`:

- warn-only by default;
- `--strict` fails CI;
- `--strict-wired` enforces the wired subset only.

The validator scans every `*.witness.json` whose name or
`description` / `computation` field signals an LP / SDP /
operator-selection compute and verifies the dual fields are
present.

### Why this is mandatory

*The dual variables **are** the binding-energy shadow prices. Active demand channels (`y_star[i] > 0`) name the receptive sub-braids, identifying the Wedderburn blocks saturated by the bound state. Solving only the primal drops this structural information, a historical flaw (58 of 58 LP/SDP witnesses on `main` lacked the dual when this rule was introduced).*

### Correctness conditions

*[`prop:operator-selection-lp`](#prop:operator-selection-lp) §
*dual program* establishes strong duality (`primal_obj = dual_obj`
to solver tolerance) and the interpretation of $y^*$ as the
binding-energy shadow prices.*

### Python API entry point

```python
from pyhecke.lp_dual_solver import (
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)

result = solve_operator_selection_lp(t, G, n_target)
witness = result.to_dict()   # primal + dual + active_set + gap
```

### Notes

*Cross-reference: AGENTS.md §"LP / SDP duals — first-class
infra". Active baseline of missing-dual witnesses: run the
validator for the current count — do not cite a dated baseline.*
<!-- FILE_END: mba-sidecar-lp-sdp-dual-emission.md -->

<!-- FILE_START: mba-sidecar-witness-json-pipeline.md -->
**Algorithm (Witness-JSON pipeline).**
*Cross-language interchange contract for `*.witness.json` files
emitted by canonical compute scripts via the `WitnessBuilder` API.
Maintained as a sidecar to the canonical chain because every
chain step's `computation.witness` field points to a file that
conforms to this contract (or, for **legacy witnesses**, is
scheduled to be migrated to it — see *Migration status* below).*

### Required JSON shape (`WitnessBuilder.build()` output)

```json
{
  "engine":           "python",
  "engineVersion":    "...",
  "computedAt":       "YYYY-MM-DDTHH:MM:SS+00:00",
  "commitSha":        "<git head sha>",
  "scriptFile":       "<script>.py",
  "scriptHash":       "<content sha256>",
  "scriptCommitSha":  "<git file sha>",
  "durationMs":       0,
  "assertions":       [{ "name": "...", "passed": true, "delta": "..." }],
  "allPassed":        true,
  "computation":      "<witness name>",
  "precisionMetadata": {
    "compute_dps":      65,
    "output_dps":       50,
    "guard_digits":     15,
    "truncation_bound": "1e-50"
  },
  "environment":      { ... },
  "parameters":       { ... },
  "data":             { ... },
  "caveats":          [ ... ]
}
```

### Precision discipline

- Default compute: **65 dps** mpmath
  (`qou_substrate.precision.COMPUTE_DPS`).
- Default serialisation: **50 dps**
  (`qou_substrate.precision.OUTPUT_DPS`).
- Cross-method assertion at $\leq 10^{-15}$ relative agreement
  (L1 — internal compute precision).
- The `precisionMetadata` block records the truncation bound so
  downstream consumers know the error floor of every serialised
  value.

### LP/SDP duals

*If the compute is LP / SDP / operator-selection, the witness
**must** additionally carry the fields specified in
[`alg:lp-sdp-dual-emission`](#alg:lp-sdp-dual-emission).*

### Wedderburn-respecting witnesses

*Every per-partition computation (Step 5 and downstream Step 9b)
must record the partition tag $\lambda$ alongside each value via
`builder.add_data(...)`, so the witness is partition-respecting
and reviewers can audit the isotypic structure.*

### Algorithm

```
1. Initialize WitnessBuilder(name, engine="python+mpmath").
2. builder.add_parameter(key, value) for each input parameter.
3. builder.add_data(key, value) for each computed output
   (per-partition tags included where relevant).
4. builder.add_assertion(name, condition_callable, description)
   for each correctness check.
5. builder.add_caveat(text) for any known limitation.
6. builder.add_upstream(path) for each upstream witness whose
   hash must be tracked for drift.
7. builder.save() emits the JSON to the canonical location.
```

### Correctness conditions

1. *The Wedderburn decomposition
   ([`prop:wedderburn-trace-identity`](#prop:wedderburn-trace-identity))
   defines the partition structure that `add_data` records.*
2. *The LP/SDP dual contract
   ([`prop:operator-selection-lp`](#prop:operator-selection-lp))
   defines the dual-emission fields used by Step 10.*

### Canonical entry point

```python
from qou_substrate.witness import WitnessBuilder

w = WitnessBuilder(name="my-result", engine="python+mpmath")
w.add_parameter("q0", q0_value)
w.add_data("tau_M", tau_M_value)
w.add_assertion(
    "1ppQ_cross_method",
    condition=lambda: abs(a - b) < mp.mpf("1e-15"),
    description="cross-method agreement at L1",
)
w.save()
```
### Witness contract (meta)

*Every `*.witness.json` is audited by:
[`lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py)
(LP/SDP duals), `q-usage-watcher` (q-regime declarations), and
the q₀ staleness detector. Stale or schema-violating witnesses
fail CI in `witness-pipeline.yml`.*

### Notes

*Cross-language sibling: the
[`witness-schema`](../../../tools/witness-schema/) PyPI + npm
package provides Zod / Pydantic / TypeScript types for every
canonical witness shape, so Pyodide / Node / TS callers see the
same contract.*
<!-- FILE_END: mba-sidecar-witness-json-pipeline.md -->

