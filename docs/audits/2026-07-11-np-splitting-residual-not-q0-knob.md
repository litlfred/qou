# Neutron–proton splitting: L1 precision reached; the 0.63% residual is missing physics, not a q₀ knob

**Date:** 2026-07-11
**Depends on:** the exact traced-volume closed form for the quark Φ-volumes
([`2026-07-11-quark-volume-provenance.md`](2026-07-11-quark-volume-provenance.md)).
**Probe:** [`computations/probes/np_splitting_residual_probe.py`](../../computations/probes/np_splitting_residual_probe.py).

`Δm = α·|ΔΦ|`, `α = m_e·8G`, `Φ(K) = Σᵢ log|V̂ᵢ(K)|` (Hecke traced-volume).

## (a) L1 (compute precision) — reached

Replacing the 6-digit `quarkPhi` literals with the exact closed form removes the
`~10⁻⁶` truncation floor:

| `|ΔΦ|` | value |
|--------|-------|
| engine (exact-`Fraction` `traced_volume`) | `0.34760410008476405947923551228…` |
| sympy closed form (same `q`) | `0.34760410008476405947923551228…` |
| **engine vs closed form** | **`0.0` — identical to 40+ digits** |
| closed form @ canonical 50-dps `q₀` | `0.34760402781524654755…` |
| old 6-digit literal | `0.347593` (floor `~10⁻⁶`) |

The closed form **equals** the engine to every digit (the symbolic derivation is
exact) and evaluates stably to 50 dps, so Δ_pn now clears the literal floor and
can participate in the L1 `≤ 1 ppQ` cross-method check. **This is an L1 enabler,
not an L2 (accuracy) change.**

### Side finding — a q₀-pin inconsistency (fixed)

Methods diverge at `~7×10⁻⁸` purely because of the `q₀` pin used
(`d|ΔΦ|/dq ≈ +4.19`, so `10⁻⁸` in `q` → `10⁻⁷` in `Φ`). Two pins differ at
`10⁻⁸` in the corpus: the canonical `q_parameter.Q_50_DIGIT_STR =
1.10997858275…` (`q_parameter.Q` is its f64 view) vs
`two_quark_volume…Q0 = 1.10997859555…`. The `q0` constant in
`neutron-proton-mass-splitting.lean` had been set to the *latter*; corrected to
the canonical full-precision `Q_50_DIGIT_STR` value (matching
`QOU.LiftingDescent.H3BraneTowerScaffold.q0`) in this change.

## (b) L2 (accuracy) — the 0.63% residual is structural

`Δm_pred = 1.301589` vs `Δm_CODATA = 1.293334` → **+0.638%**, correction factor
`r − 1 = −0.006343`.

- **Not a q₀ artifact.** Absorbing the residual by shifting `q₀` (holding `α`)
  needs **`Δq/q ≈ 474 ppm`**. The `q₀` pin is at the **ppb** level (proton
  0.06 ppb, muon 22 ppb) — so a q₀ re-pin is `~10⁵×` too large and would destroy
  `m_p`/`m_μ`. The residual cannot be a mis-pin.
- **Not a single clean Habiro term.** `(r−1)/ℏ_q² = −0.646` (near `−2/3 = −0.667`
  but **3% off** — *near-match tier*, not exact); `/h² = −0.145`; `/h = −0.030`.
  No tidy `(1 + c·ℏ_q²)` correction at this anchor.

**Verdict (scope-limited, per AGENTS.md §"declaring refuted").** The traced-volume
Φ is the **exact, permanent leading piece** (a proved/exact factor stays valid
even while the total is inaccurate); the 0.63% is a genuine **additive**
higher-order term — EM self-energy / d−u quark-mass split / higher brane-tower —
that adds to it. It is *not* a q₀ knob and *not* a one-parameter fit. The
formalize-first next step is to prove the invariant that the missing term must
satisfy (parity/sign/magnitude bound) before scanning candidate closures.

Δ_pn is one of the three failing L2 observables (the `Q_β`/`m_n`/`Δ_pn`
shared-root trio, [`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md));
this pins down which leg (L1 vs L2) the traced-volume closed form actually moves.
