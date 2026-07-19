# The c₃ swing is the `1/u³` ladder artifact, not a self-dual-locus pole — PR #4064 reinterpretation refuted (scope-(a))

**Date:** 2026-07-19 · **Branch:** `claude/agent-pickup-stalled-rtugin` ·
**Axis:** c₃ / Q_β bar-odd swing / q₀ unification · **Tier:** scope-(a)
consistency check / refutation of a reinterpretation · **Discipline:** no fit
(nothing tuned to CODATA), no `c_k` wired, nothing to production, no tier change;
`conj:im-q-physical-role` stays a conjecture.
**Probe:** [`computations/qbeta/qbeta_c3_swing_selfdual_pole_vs_ladder_probe.py`](../../computations/qbeta/qbeta_c3_swing_selfdual_pole_vs_ladder_probe.py)
· **Witness:** `computations/qbeta/qbeta-c3-swing-selfdual-pole-vs-ladder.witness.json`

## Context — reconciling the PR #4064 synthesis with the merged capstone

The PR #4064 c₃⟺q₀ unification synthesis proposed a **reinterpretation** of the
famous bar-odd swing `dc₃/dq ≈ 4.66×10⁶` (self-dual lens): the swing is a
**rigidity divergence at the self-dual / Chern–Simons-degeneration locus** — as
`u → ` the self-dual point, `Φ_odd → 0`, so `dΦ_odd/dq → ∞` — with a pole-form
`swing ≈ 1/|u²−1|`, and q₀ sitting "anomalously near" that locus.

That reinterpretation is in **direct tension** with the already-**merged** wall-
resolution capstone (PRs #3600/#3636/#3654,
[`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md);
[`2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md`](2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md)),
whose result 3+5 are: the swing is a **`1/u³` ladder-inversion representation
artifact over smooth geometry** (`u = b·ℏ_q² ≈ 0.00852` the truncation small-
parameter), and the Φ_b state integral is **smooth and anchor-blind** — *"there
was no singularity to break."*

Two competing functional forms for the same slope; this probe discriminates them
with the deterministic extractor `S(q) = c3_target_at(q, Q_β, m_e) + Vol(4₁)` at
full precision. This is exactly the critical-distance check the synthesis invites
— testing its most exciting claim adversarially before it hardens into corpus.

## Findings (all measured in the probe; deterministic extractor reused)

**q\* reproduced.** `S(q*) ≈ −8×10⁻⁵⁶` at `q* = 1.10997859303152328840…`
(80.30 % muon-ward), anchors reproduced (`S(proton)=−0.0394594`,
`S(muon)=+0.0096830`) — the genuine opposite-sign crossing, unchanged.

1. **q\* is a SIMPLE zero — no pole.** `S'(q*) = 3.84×10⁶` and
   `S''(q*) = −3.70×10⁸` are **both finite**. An analytic simple zero has no pole
   and no branch point, so `S` — hence any `Φ_odd ∝ S` — does **not** diverge at
   `q*`, and no derivative ratio blows up there. The "rigidity divergence at the
   self-dual locus" mechanism has **no numerical support at q\***.

2. **The pole form `1/|u²−1|` is ~6 orders of magnitude too small.** At q₀ the
   ladder parameter is tiny (`u ≈ 0.00852`, `u² ≈ 7.25×10⁻⁵`), so
   `1/|u²−1| ≈ 1.00007` — an **O(1)** number, against a measured swing of
   `≈ 3.84×10⁶`. The scale gap `(1/u³)/(1/|u²−1|) ≈ 1.62×10⁶` is exactly `1/u³`
   up to O(1). q₀ is **not** near a `u² → 1` self-dual locus — `u` there is
   small, nowhere near 1. Matching the pole form would need an un-derived
   prefactor `≈ 3.8×10⁶`.

3. **The swing IS `1/u³` (capstone reproduced).** `S'(q*) = 2.372 × (1/u³)`,
   a smooth O(1) prefactor. The magnitude is the extractor's `/u³` division of a
   smooth numerator zero — the merged form.

## Conclusion (scope-(a))

The self-dual-pole reinterpretation of the swing **conflates the ladder small-
parameter `u = b·ℏ_q²`** (which drives the `1/u³` amplification) **with the
Chern–Simons meridian variable**, and mistakes the **simple zero** of `S` at
`q*` for a **pole**. The merged capstone stands: the swing is a `1/u³`
representation artifact over smooth geometry, not a divergence at a self-dual
locus.

This is a **scope-(a)** negative — a *functional form* (`1/|u²−1|`) does not
reproduce the swing — supported by the computed simple-zero fact (`S'`, `S''`
finite). It is **not** a structural exclusion of the c₃⟺q₀ unification: `q*`
remains the shared target. What it removes is the **swing as evidence for a pole
at `q*`**.

## What survives and is sharpened

The **non-circular core is unchanged**: `q*` is a fixed **simple** zero of the
deterministic bar-odd extractor — the CS→0 / ε=0 point — a third, decay-sector
determination of q₀ (per capstone result 4; the μ-p tension becomes a μ-p-Q_β
trio). The swing and `q*` are **separate facts that merely coincide at `q*`**:
the swing is the extractor's `1/u³` artifact, `q*` is where its smooth numerator
crosses zero. The synthesis's shared-target claim (c₃ and q₀ both point at `q*`)
is untouched; only the "swing = signature of a pole" sub-claim is retired.

**Actionable follow-up.** The remaining live routes from the PR #4064 synthesis
are unaffected: the F-construction / R1 naturality on Bring/S₅ (the unified q₀=c₃
derivation target) and the Hilbert–Schmidt matrix-O probe. This probe simply
ensures neither is pursued under the mistaken belief that the swing magnitude is
independent geometric evidence for a self-dual pole.
