# Adjoint Reidemeister torsion vs ν_SDP — falsifiable probe on `conj:kashaev-density-equals-sdp-multiplicity`

**Date:** 2026-08-02
**Bean:** `qou-r307` (salvaged from the PR #4573 Gemini-brainstorm review)
**Branch/PR:** `claude/r307-torsion-nu-sdp-probe-2026-08-02` / #4576
**Probe:** [`computations/probes/torsion_nu_sdp_probe.py`](../../computations/probes/torsion_nu_sdp_probe.py)
**Witness:** [`computations/probes/torsion-vs-nu-sdp.witness.json`](../../computations/probes/torsion-vs-nu-sdp.witness.json)

## Question

The open conjecture
[`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md)
proposes `ρ_F = ν_SDP` — the topological density selecting the geometric
connection (the constant / 1-loop term of the Kashaev asymptotics) equals
the SDP confinement multiplicity `ν_SDP ∈ {1,2}`.

Garoufalidis–Yoon 2024 (arXiv:2411.03801) **prove** that the NZ 1-loop
invariant **equals the adjoint Reidemeister torsion** for two-bridge knots.
This makes the literal reading testable: is `adjoint_torsion(K) = ν_SDP` for
`6_2` (ν_SDP = 1) and `8_11` (ν_SDP = 2)?

## Prediction (locked before compute — anti-fit)

Adjoint torsion lies in the trace field (ℚ(√−3) for `4_1`; cubic for
`6_2`/`8_11`) — a generically **complex, non-integer** number — so the literal
`torsion = ν_SDP ∈ {1,2}` reading was expected to **FAIL (scope-(a) category
mismatch)**: a normalization-free positive integer cannot equal a complex
trace-field algebraic number.

## Method + validation

Adjoint (3-dim) twisted Reidemeister torsion via Fox calculus on the SnapPy
numeric SL(2,ℂ) holonomy; Porti meridian torsion `𝕋_μ = −W'(1)` (Yamaguchi
simple-zero slope). **No ad-hoc rescaling** — the raw normalization already
reproduces the known rational value:

- **`4_1` validation:** `𝕋_μ = −3.00003` (known `−3`, trace field ℚ(√−3)) ✓

## Result — scope-(a) refutation of the literal reading

| knot | `𝕋_μ` (adjoint torsion) | \|𝕋_μ\| | ν_SDP | non-real? | = ν_SDP? |
|------|------------------------|--------|-------|-----------|----------|
| `6_2` | `+6.650 + 15.469i` | 16.838 | 1 | yes | **NO** |
| `8_11` | `−27.724 − 1.313i` | 27.755 | 2 | yes | **NO** |

Both `𝕋_μ` are complex trace-field numbers of modulus **≫ {1,2}** and are
non-real (⇒ `∉ ℤ`). The literal *"topological density = ν_SDP integer"*
reading is **refuted (scope-(a))**: the adjoint Reidemeister torsion (= NZ
1-loop) is **not** `ν_SDP` for `6_2`, `8_11`. `ν_SDP ∈ {1,2}` is a distinct,
normalization-free object.

## Scope + discipline (STRICT)

- **Scope-(a), not scope-(b).** This constrains the *identification* `ρ_F =
  torsion = ν_SDP` as written; it does **not** structurally exclude a
  relationship between the Kashaev density and `ν_SDP` under a different
  normalization (e.g. a phase/modulus reduction, or `ρ_F` being a *derived*
  functional of the torsion rather than the torsion itself). No proved
  invariant forbids such a route, so no scope-(b) claim is made.
- **Evidence, not derivation.** A *match* would have been evidence, never a
  proof; a *mismatch* likewise refutes only the literal equality. This does
  **not** close the Lean class-instance `sorry` of
  `conj:kashaev-density-equals-sdp-multiplicity`, and **nothing is wired** to
  any dashboard or the `Q_β` ladder.
- No fit, no `c_k` wired, no axiomatization.

## Follow-up

The surviving open question (bean `qou-r307`): is there a *reduced* functional
of the adjoint torsion — a phase, a modulus-class, or a normalized real part —
that recovers `ν_SDP ∈ {1,2}`? The raw `𝕋_μ` does not; a derived one is not
excluded and would be the honest next probe.
