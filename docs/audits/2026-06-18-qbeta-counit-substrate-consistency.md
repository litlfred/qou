# Q_β counit/trace consistency at the live substrate q₀ — ground truth + a block-numeric reconciliation (2026-06-18)

**Scope.** Advances the one open item of the merged counit/transition
framing — the *convergence / consistency leg* of
[`conj:qbeta-trace-counit-convergence`](../../content/quantum-observable-universe/particle-interactions/qbeta-trace-counit-convergence.md)
(merged on `main`; Lean class
`QOU.Interactions.QBetaConvergence.QBetaTraceCounitConvergence`) — by pinning
the **archimedean substrate evaluation** at the *live, proton-anchored* `q₀`.
The merged generic-field Lean
([`qbeta_counit_vs_trace.lean`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_counit_vs_trace.lean),
[`qbeta_energy_scale.lean`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_energy_scale.lean))
left the Markov loop value `z` symbolic; this audit instantiates it at the
physical substrate and characterises the `N=0` truncation remainder.

No fit, no scan, no production wiring. Witness:
[`qbeta-counit-substrate-consistency.witness.json`](../../computations/qbeta/qbeta-counit-substrate-consistency.witness.json)
(`computations/qbeta/qbeta_counit_substrate_consistency.py`, 50 dps, 4/4 green).

## Ground truth at the live anchor (`q₀ = 1.10997859…`, proton-pinned)

The `N=0` neutron−proton normal-form difference `(n−p)` carries reduction
content `h²/2 − h·z` under the Markov trace (loop value `z`) and `h²/2 − h`
under the Frobenius counit (`z=1`), with `h = q − q⁻¹`. Multiplying the
dimensionless content by the per-Hecke-step energy
`𝔈₀ = m_e/(q(q−1)) = 4.18598 MeV`:

| quantity | value | residual vs CODATA `0.78233341` |
|---|---|---|
| `h = q − q⁻¹` | `0.2090603` | — |
| `ℏ_q² = (1−q⁻¹)²` | `0.0098172` | — |
| `z_sub = √q/(q+1) = 1/(√q+1/√q)` | `0.4993203` | — |
| `ε(Δ) = h²/2 − h` (counit content) | `−0.1872072` | — |
| `tr_M(Δ)|_{z_sub} = h²/2 − h·z_sub` | `−0.0825350` | — |
| **counit** `Q_β = \|ε(Δ)·𝔈₀\|` | **`0.7836458` MeV** | **`+0.168 %`** (right tool) |
| **trace** `Q_β = \|tr_M(Δ)\|_{z_sub}·𝔈₀\|` | **`0.3454898` MeV** | **`−55.84 %`** (wrong tool) |

The counit value matches the closed form `m_e(q+1)(q²−2q−1)/(2q³)`
(Lean `Qbeta_closed`) to `< 10⁻⁴⁰`. Reproducing **both** signatures at the
*live* anchor (a) validates the substrate loop value `z_sub`, and
(b) **confirms the +0.17 % counit value is current, not stale** — the anchor
re-pin was 2026-05-28, and CLAUDE.md flags Habiro-exact Q_β witnesses as
potentially stale post-re-pin.

## The convergence-leg invariant (formalize-first)

The `+0.17 %` counit residual is the **`N=0` truncation remainder**: the
counit `ε(Δ)·𝔈₀` is built from the `N=0` normal-form difference alone, so its
deviation from CODATA is the leading-order truncation error, not a fit. The
falsifiable structural bound is

```
|remainder|  ≤  O( ℏ_q² / (1 − ℏ_q²) )  =  0.9915 %   at q₀,
```

and the observed counit residual `0.168 % ⊂ 0.99 %` ✓. This is the same
order as the `0.74 %` `𝔈₀` derived-vs-calibration gap (`4.186` vs `4.155`
MeV, [`energy-scale-planck.md`](../../content/quantum-observable-universe/particle-interactions/energy-scale-planck.md)).
The bound is the invariant the open leg must respect: the higher-`N`
brane-tower corrections must carry the `N=0` counit value into CODATA while
staying within `~1 %`.

**What closing the conjecture requires (unchanged from the block):** a *closed
evaluation of the tower-summed* Markov-trace difference
`𝔪(n)−𝔪(p)−m_e`, shown to reorganise onto the counit form. A perturbative
expansion about the `N=0` trace term does **not** suffice — the trace term is
the *wrong functional* (it misses by −56 %, below), so the identity is
functional-consistency, not a small-correction limit. This audit pins the
target's invariant; it does not close it.

## Block-numeric reconciliation (corrected on this PR)

The merged `conj:qbeta-trace-counit-convergence` `.md` and `.lean` quote the
`N=0` Markov-trace term as `|tr_M(Δ)|·𝔈₀ ≈ 0.49 MeV` with a "~259 %" deficit.
That figure does not reconcile with the canonical functional definitions
(merged `trMNP h z = h²/2 − h·z`): at **no** standard loop value — and in
particular at the substrate `z_sub = √q/(q+1)` the block itself names — does
`|tr_M(Δ)|·𝔈₀` equal `0.49`. The exact value is

```
|tr_M(Δ)|_{z_sub}·𝔈₀ = 0.3454898 MeV   (−55.84 % vs CODATA; ~2.27× low),
```

which **agrees with the canonical #2363 result** ("`tr_M` gives `Q_β` ~2× low,
−56 %", `docs/coordination/1ppq-qbeta.md` cont. row for PR #2363) and with the
witness here. The block's `0.49 MeV / 259 %` is therefore an internal numeric
slip (it also contradicts the block's own cited "~2× low"). This PR corrects
the block prose + docstring to `0.345 MeV / −56 %`; the conjecture statement,
the Lean class, and the conditional corollary are unchanged (the error was in
illustrative prose only).

## Discipline

- The counit value is already RESOLVED + merged (#2363, cross-validated to
  `2·10⁻¹⁶` vs #2346's `Im 𝔙`). This is **not** a new c_k near-match and does
  not touch the flip-flop guard.
- Orthogonal to the active c_k-extraction frontier: #2106 (Hoefsmit Stage B
  operator-level c_k), #1839 (residue kernel), #2453/#2460 (Jacobi–Anger /
  Φ_q). Those are the *static-mass* tower; this is the *transition* counit.
- Audit-only witness; no production wiring; the Δ_λ gate is untouched.
