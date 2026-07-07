# Fibre-side spec for the z→c_k evaluation map: the c_3 swing is phase-channel

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (fibre side) ·
**Hands to:** [PR #3458](https://github.com/litlfred/qou/pull/3458)
(`claude/z-c-k-f-map-keystone-ub5yix`, the active u-side session) ·
**Tier:** structural (sorry-free Lean + validated-evaluator witness) ·
**Verdict:** channel classification (scope-(a)) — **not** a c_3 construction

## One-line

The observed cross-anchor `c_3` swing is a **phase-channel** (bar-odd)
quantity; PR #1821's `dc_3/dq ≈ 4.66×10⁶` impossibility is a **magnitude-channel**
bound and does **not** constrain it. So the evaluation-map search should look
for a phase (argument of the pure-phase fibre `Φ_b`), not a smooth real
function of `q` with a near-singularity.

## The constraint being classified

From the merged cross-anchor probe
([`qbeta-c3-complex-habiro-cross-anchor-probe.witness.json`](../../computations/qbeta/qbeta-c3-complex-habiro-cross-anchor-probe.witness.json)):

| quantity | value |
|---|---|
| `c_3` at proton anchor | `−2.0693` |
| `c_3` at muon anchor | `−2.0097` |
| `Δq` (proton→muon) | `1.28×10⁻⁸` |
| `Δc_3` | `0.0596` |
| **required `dc_3/dq`** | **`4.66×10⁶`** |
| near-singularity radius for a smooth real `f` | `≈ 4.4×10⁻⁷` |

That probe tested four complex-analytic forms; all fail without a **fitted**
pole (candidate A: pole at radius `4.3×10⁻⁷`, "categorical meaning NONE";
B/C/D: derivatives `−20`, `0.90`, `−189` — orders of magnitude short). This
is the PR #1821 result: **no smooth real function of `q` reproduces `c_3`
across both anchors without a categorically-unmotivated near-singularity.**

Crucially, **none of those candidates was the validated Faddeev `Φ_b`** —
candidate C was a `log(−q)` control, D a cyclotomic partial-fraction proxy.

## The classification

PR #1821's bound is a statement about a **smooth real function of `q`** — i.e.
the **magnitude channel**. The fibre-saddle object is not that. On the fibre
saddle (real `b`, root-of-unity `q = e^{2πib²}`) the validated `Φ_b` is a
**pure phase**, `|Φ_b| ≡ 1`
([`qbeta-fmap-phi-b-root-of-unity-reference.witness.json`](../../computations/qbeta/qbeta-fmap-phi-b-root-of-unity-reference.witness.json)).
A pure phase has **identically zero magnitude derivative** and carries **all**
its variation in the phase. New probe
([`qbeta_fmap_phi_b_channel_separation_probe.py`](../../computations/qbeta/qbeta_fmap_phi_b_channel_separation_probe.py),
4/4, C14 anti-fitting) confirms this on the evaluator:

| gate | finding |
|---|---|
| **G1** magnitude flat | `|Φ_b| = 1`, `d|Φ_b|/dz ≤ 1.15×10⁻³⁵` — magnitude channel carries no variation |
| **G2** phase varies | `|d arg Φ_b/dz| ≈ 1.8–2.4` — the phase channel carries the variation |
| **G3** cross-factor σ-unitary | `|Φ_b(z₂)·\overline{Φ_b(z₁)}| = 1` exactly — the connecting factor is a pure phase |

### Lean anchor (sorry-free)

The algebraic reason G3 holds in general is
[`QOU.QBeta.IsSigmaUnitary.crossFactor`](../../content/quantum-observable-universe/lean/QOU/QBeta/FaddeevModularDouble.lean)
(FaddeevModularDouble.lean, `lean`-direct exit 0): for two σ-unitaries
`u₁, u₂` (the fibre-saddle `Φ_b` at two anchors), the connecting factor
`w = σ(u₁)·u₂` is itself σ-unitary and `u₁·w = u₂`. Hence **all** cross-anchor
variation between σ-unitaries is a pure-phase factor — the magnitude channel
is flat by construction, so the `Δc_3` swing is a **phase-channel** quantity.
(σ = the bar involution; archimedean instance: complex conjugation.)

## Scope and discipline (STRICT)

- **This is scope-(a), not (b).** It does **not** claim to construct `c_3`,
  and does **not** refute anything. It re-scopes PR #1821's negative from an
  implicit "no fibre source" reading to its correct statement: *the smooth-real
  **magnitude** family is excluded.* The **phase** channel — where the bar-odd
  carrier `Φ_b` lives — is untouched by that bound and remains open.
- **No fitting (C14).** The probe compares nothing to `c_3`, `Φ₁`, the residue
  `A`, `dc_3/dq`, or any physical constant. The `4.66×10⁶` observable-`q` slope
  is a **separate** (magnitude) channel and is deliberately **not** reproduced.
- **Consistent with the "Im(q) at fibre vs observable level" wall** (AGENTS.md):
  parity is a fibre notion; the `c_k` are archimedean evaluations. This spec
  says the bridge is an **argument extraction** of a pure-phase fibre object,
  not a real-analytic continuation of a magnitude.
- **Complements #3458's u-side obstruction.** #3458 (B3-U) showed the fibre
  parity does not descend to `c_k` by re-expansion in `u` (the odd channel
  enters through the archimedean evaluation map, not the `u`-grading). This
  spec sharpens *which* fibre datum that map consumes: the **phase** of the
  pure-phase `Φ_b`, with the near-singularity to be sought as a root-of-unity
  accumulation on `|q| = 1`, not a fitted real-`q` pole.

## What #3458's evaluation map should target (the handoff)

1. The map extracts a real projection (`Re` / `cos`) of the **phase** of the
   fibre-saddle `Φ_b` — consistent with the `Q_β/Q_A = cos Φ(u)` reframe
   ([`prop:phi-b-unitary-bar-odd`](../../content/quantum-observable-universe/mass-theory/phi-b-unitary-bar-odd.md)).
2. Its target is `c_2 = −1` (bar-even, anchor-independent) **and** the
   `c_3 → −2` shadow (bar-odd, anchor-dependent), per the merged registry.
3. The near-singularity that a magnitude reading needed (`4.4×10⁻⁷`) should
   correspond to a **root-of-unity accumulation** of the fibre `q̃` on `|q|=1`
   near the archimedean `q_0`, **not** a categorically-unmotivated real-`q`
   pole (which is why candidate A was a fit).

## Cross-references

- Lean: `QOU.QBeta.IsSigmaUnitary.{crossFactor, inv, mul_bar_self}`
  (FaddeevModularDouble.lean)
- Witness: `qbeta-fmap-phi-b-channel-separation.witness.json`
- Content: [`prop:phi-b-unitary-bar-odd`](../../content/quantum-observable-universe/mass-theory/phi-b-unitary-bar-odd.md)
- Sibling: PR #3458 B3-U obstruction audit
  (`docs/audits/2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md`)
- AGENTS.md §"Im(q) at fibre vs observable level"; §"Critical framing — Q_β c_3
  truncation order"; §"Before declaring refuted (a)/(b) scope"
