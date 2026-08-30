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
| **Vol(Borromean) = 8·G** | `7.327724753417752120…` | ⚠ **SEE CORRECTION BELOW — this ✅ was wrong.** live compute uses the full-precision value; `7.327724753846269` survives only as a *comment* in `experimental_constants.py:136` ("previous f64 value", already centralised), wrong-tail variants only in `_deprecated/` |
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


---

## ⚠ CORRECTION 2026-08-30 — the Vol(Borromean) row's ✅ was FALSE

Bean `qou-f8lit`.

This document certifies `Vol(Borromean) = 8·G` as consistent, on the ground that the bad
value `7.327724753846269` *"survives only as a comment in `experimental_constants.py:136`
… wrong-tail variants only in `_deprecated/`"*.

**It was live in executable Lean.**
`content/quantum-observable-universe/mass-theory/nuclear-knot-classification.lean`
lines 28 and 30 carried

    bindingScale .satellite = m_e * 7.327724753846269
    bindingScale .borromean = m_e * 7.327724753846269

inside a **mass formula** — wrong from digit 11, abs err `4.3e-10` against
`8·G = 7.327724753417752120…`. Every other Lean carrier
(`building-block-knots.vol_borromean`, `categorical-neutron`, `categorical-proton`)
already used `7.32772475341775`, so that file was the outlier rather than an alternative
convention. Corrected on 2026-08-30.

### Why the miss, and what to change about audits like this one

This audit's evidence is entirely about `computations/` — `experimental_constants.py`,
`_deprecated/`. It appears never to have walked `content/**/*.lean`, and **it does not
say which surface it searched**. A reader takes the ✅ as a statement about the corpus;
it was a statement about one directory.

**A "clean" verdict is only as wide as the surface the detector walked.** An audit that
does not record its search surface cannot be re-checked, and its ✅ silently widens over
time into a claim it never made. Future consistency audits should state the globs they
ran, verbatim.

Found by [`scripts/known-constant-literal-audit.py`](../../scripts/known-constant-literal-audit.py),
which compares literals to **computed** constants by value instead of grepping for
known-bad digit strings — the relevant property here being that the same wrong number is
spelled several different ways across the corpus, so a grep for any one of them misses
the others.

**Not re-verified by this correction:** the other five ✅ rows in the table above. They
were audited with the same `computations/`-scoped method and carry the same blind spot;
none has been re-run against `content/`.
