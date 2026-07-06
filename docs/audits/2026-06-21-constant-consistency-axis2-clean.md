# Constant-consistency audit — coverage record (2026-06-21, axis-2: CLEAN)

Second pass of the constant-consistency sweep (after the q₀ census #2569 and the
cluster-D/vol(4₁) fixes #2576). This axis came back **clean in live compute** —
recorded so future agents don't re-scan these.

## Axes verified consistent

| Quantity | Canonical | Verdict |
|---|---|---|
| **m_μ/m_e** | `206.7682830` (CODATA) | ✅ canonical in all compute; the only variants (`206.7683`, `206.768`) are **display/docstring strings** (`canonical_script_input_audit.py`, `kaon_pion_ratio_7_8_probe.py` print lines), not inputs |
| **m_μ (MeV)** | `105.6583755` | ✅ consistent |
| **Vol(Hopf)** | `0` (non-hyperbolic) | ✅ not hard-coded anywhere — computed/asserted, no nonzero literal |
| **q-bracket `[n]_q`** | balanced `(qⁿ−q⁻ⁿ)/(q−q⁻¹)` | ✅ every `q_int`/`qint` def uses the balanced form — **no** balanced-vs-unbalanced mixing |
| **Vol(Borromean) = 8·G** | `7.327724753417752120…` | ✅ live compute uses the full-precision value; `7.327724753846269` survives only as a *comment* in `experimental_constants.py:136` ("previous f64 value", already centralised), wrong-tail variants only in `_deprecated/` |
| **Catalan G** | `0.9159655941772190150…` | ✅ consistent to the precision tier each consumer needs (sub-floor tail differences only) |

## Standing item (unchanged)

The one real systemic inconsistency remains the **q₀ hardcode staleness** —
**cluster A** (61 live files on the stale pre-re-pin `1.1099785827513808…`),
documented in [`2026-06-21-q0-hardcoded-constant-census.md`](2026-06-21-q0-hardcoded-constant-census.md).
That is the owner-sequenced, witness-regenerating sweep (route q₀ through
`q_parameter.Q`); it is **not** a quick fix and would collide with the active
binding/qbeta work, so it stays deferred.

## Conclusion

Outside the known q₀ cluster-A staleness, the framework's hardcoded constants
are **consistent**. The genuine divergence bugs found this sweep —
`hoefsmit_b` (bar-parity, #2558), cluster-D q₀ in 5 qbeta probes (#2576), and
the 1e-16-wrong vol(4₁) in `t6_tau_h5_embedding_probe.py` (#2576) — are fixed.
The consistency-scan well is dry pending the cluster-A migration.
