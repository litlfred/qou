**Algorithm (Witness-JSON pipeline).**
*Cross-language interchange contract for `*.witness.json` files
emitted by canonical compute scripts via the `WitnessBuilder` API.
Maintained as a sidecar to the canonical chain because every
chain step's `computation.witness` field points to a file that
conforms to this contract, apart from a residue of older witnesses
that do not yet conform.*

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

- Default compute: **70 dps** mpmath
  (`qou_substrate.precision.COMPUTE_DPS`).
- Default serialisation: **60 dps**
  (`qou_substrate.precision.OUTPUT_DPS`), with a guard of **10**
  (`PRECISION_GUARD`, the difference between the two).
- Cross-method assertion at $\leq 10^{-15}$ relative agreement
  (L1 — internal compute precision).
- The `precisionMetadata` block records the truncation bound so
  downstream consumers know the error floor of every serialised
  value.

### LP/SDP duals

*If the compute is LP / SDP / operator-selection, the witness
**must** additionally carry the fields specified in
[LP/SDP dual-emission contract](#alg:lp-sdp-dual-emission).*

### Wedderburn-respecting witnesses

*Every per-partition computation (Step 5 and downstream Step 9b)
must record the partition tag $\lambda$ alongside each value via
`builder.add_data(...)`, so the witness is partition-respecting
and reviewers can check the isotypic structure.*

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
   ([Markov-trace normalization for $H_n(q)$](#prop:wedderburn-trace-identity))
   defines the partition structure that `add_data` records.*
2. *The LP/SDP dual contract
   ([Knot operator selection as linear program with LP duality](#prop:operator-selection-lp))
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

*Every `*.witness.json` is checked on three counts: the LP/SDP dual fields
([`lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py)),
an explicit $q$-regime declaration, and staleness against the current $q_0$.
A stale or schema-violating witness is rejected, not consumed.*

### Notes

*Cross-language sibling: the
[`witness-schema`](../../../tools/witness-schema/) PyPI + npm
package provides Zod / Pydantic / TypeScript types for every
canonical witness shape, so Pyodide / Node / TS callers see the
same contract.*
