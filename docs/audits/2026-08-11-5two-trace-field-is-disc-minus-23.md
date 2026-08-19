# 5₂'s invariant trace field is the cubic of discriminant −23, not ℚ(√−7)

**Date:** 2026-08-11 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ · **Tier:** scope-(b)
structural exclusion on a proved invariant · **Discipline:** a field correction; no
action value claimed, none retracted, nothing wired, no tier change.

## The claim being corrected

[`2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md`](2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md)
opens:

> The 5₂ invariant trace field is **ℚ(√−7)** (`det(5₂)=7`), so the bar-odd action is
> expected as a **ℚ(√−7)** dilog constant.

The parenthetical is the error in miniature: it reads the **geometric** trace field off
the **determinant**, which is an Alexander-polynomial datum. The two live on different
layers of the knot, and conflating them sent an entire search into the wrong field.

## What is true

| Object | Field | Degree | Why |
|---|---|---|---|
| Geometric shapes / invariant trace field `K` | cubic, `disc = −23` | 3 | `θ³ − θ² + 1 = 0`; one real + one complex place |
| Quadratic attached to `K` | `ℚ(√−23)` | 2 | A₃-fixed subfield of the S₃ Galois closure |
| Alexander root field | `ℚ(√−7)` | 2 | `Δ(t) = 2t² − 3t + 2`, `disc = −7`, `det = |Δ(−1)| = 7` |

**ℚ(√−7) is genuinely attached to 5₂** — as the quadratic subfield of `ℚ(ζ₇)`, where the
abelian/metabelian data of the ℤ/7 double branched cover lives. It is simply not the
geometric SL₂(ℂ) datum, and it **cannot** be: a degree-3 field has no quadratic subfield.

## Certification

[`qbeta_5two_trace_field_disc23_not_qsqrt7.py`](../../computations/probes/qbeta_5two_trace_field_disc23_not_qsqrt7.py)
— five assertions, all passing, all driven from the corpus's **own** saddle solver
(`qbeta_5two_quantum_volume_probe.saddle`) rather than re-derived:

1. **The shapes satisfy monic integer cubics of discriminant −23.** `y` → `x³−2x²+3x−1`,
   `x` → `x³+x²−1`, `1/y` → `x³−3x²+2x−1`. Coefficients recovered by PSLQ, then the
   discriminant computed by **exact integer arithmetic** — residuals `0.0` at 60 dps.
   Three different polynomials, one field.

2. **ℚ(√−7) cannot embed in `K`.** `[ℚ(√−7):ℚ] = 2` does not divide `[K:ℚ] = 3`. This is
   a **scope-(b)** exclusion in the sense of AGENTS.md §"Before declaring refuted",
   resting on a proved invariant — the tower law. No precision improvement can rescue
   the containment; it is not a near-miss.

3. **The unique quadratic attached to `K` is ℚ(√−23).** A non-Galois cubic has Galois
   group S₃ with a unique index-2 subgroup A₃, whose fixed field is `ℚ(√disc)`; `−23` is
   squarefree.

4. **The 7 is the Alexander layer.** `disc(Δ) = −7`, `det = |Δ(−1)| = 7`, roots
   `(3 ± i√7)/4`.

5. **Paired control — the numerics positively select √−23.** Run against both lines at
   `tol = 1e-40`, degree ≤ 3: `Im(z₁)` and `Im(z₁)/√7` satisfy **no** integer cubic,
   while `Im(z₁)/√23` satisfies `−184x³ + 10x − 1` with `disc = −178112 = −23·88²` —
   squarefree part 23, i.e. **back in `K`**.

Point 5 is the one worth dwelling on. A bare negative ("√−7 finds nothing") is weak
evidence, because a null PSLQ result can mean the height bound was too low. Running the
identical test against the competing line converts it: the same search at the same
tolerance and the same degree finds a relation on the √−23 line whose discriminant lands
back in `K`. The numerics do not merely fail to support ℚ(√−7) — they select ℚ(√−23).

## Blast radius: narrow, and the live lane was right all along

**Nothing is wired to production; no witness value depends on the field claim; the paper
never carried it.** Checked against `content/`: no content block asserts ℚ(√−7) for 5₂.
[`references.ts`](../../content/schema/references.ts) describes the Hakimoglu-Brown paper
correctly and ties its use to **4₁ / ℚ(√5)**, never to 5₂.

**Lean already proves the correct answer** — `disc_eq_neg_23` in
[`FiveTwoSumRuleIntegrand.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSumRuleIntegrand.lean).
So do the live probes: `qbeta_5two_gswz_saddle_arithmeticity_probe.py` ("trace field
K = ℚ[ξ], ξ a root of x³−2x²+3x−1 (disc −23)") and `probes/rhoF_vs_adjoint_torsion.py`.

The error was confined to the 2026-07-18 audit branch and what cited it:

| Site | Disposition |
|---|---|
| `2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md` | retraction banner; document retained |
| `2026-07-18-5two-theorem3-shape-u-archimedean-negative.md` | inherited-premise banner; **its negative stands** |
| `qbeta_5two_dilog_qsqrt7_closed_form_probe.py` | retraction header; assertions are field-agnostic |
| `docs/coordination/keystone-multivector-attack.md` §V2 | corrected in place |
| beans `qou-7lim`, `qou-dq2q`, `qou-ized` | titles corrected |

## Two further claims in the retracted audit that do not survive review

Neither is load-bearing, but both would mislead a reader who took the audit at face value.

**"Vol(5₂) = 3·|D(z₁)| exactly — the two distinct shapes carry equal Bloch–Wigner"** is
presented as a discovery. It is forced. At `m = 1` the gluing equation `x − y = xy` gives
`1 − z₁ = y`, hence `z₂ = 1/y = 1/(1−z₁)` — a standard six-fold Bloch–Wigner symmetry
partner, for which `D(z₂) = D(z₁)` is the textbook identity. With shape multiset
`(z₁, z₂, z₂)` the `= 3D` follows trivially, and it carries no field information.

**"Theorem 3 IS the 5₂ dilog closed form"** was argued by solving `L(u) = Li₂(z₁) +
2Li₂(z₂)` numerically for `u` — one equation in one unknown, in an analytic function,
which essentially always has solutions. Matching a sum's *value* is not matching the
*triple*: Theorem 3's two non-free arguments are the branches of a `√(4−3u)`, equal only
at `u = 4/3`, whereas 5₂'s triple has a genuinely repeated shape.

## What this does and does not change for the bar-odd programme

**Does not change:** no bar-odd action *value* was ever claimed by the retracted audit —
its own anti-laundering note was correct — and none is claimed or retracted here. The
`q₀`-derivation gate (owner ruling 2026-08-02, bean `qou-eic1`) is untouched: nothing
here bears on it, and any route whose success condition is reproducing the c₃ swing's
value remains forbidden regardless of which field it runs in.

**Does change:** the field a search should run in. The corpus already has the correct
answer to the question the retracted audit was asking — the A6 GSWZ probe records the
exact **bar-odd σ-pair tower**, `P_k^{σ1} − P_k^{σ2} ∈ √−23·ℝ-axis of K ⊗ ℂ`, with the
denominator's 23-adic growth law recorded (probe §4, every order `k ≤ OMAX`).
**√−23, not √−7**, is the structural analogue of 4₁'s ℚ(√−3) bar-odd line: for both knots,
"bar-odd" is the imaginary direction separating the complex-conjugate embedding pair of
the trace field. That the corpus derived this independently, in the live lane, while an
audit doc asserted a field that cannot exist, is the useful lesson here.

## Why it happened, in one line

A quantity genuinely attached to the knot (`det = 7`) was promoted to a quantity it is
not (the geometric trace field), and the coincidence that an available paper had ℚ(√−7)
identities supplied the confirmation.

> **🛑 The guard this section originally gave was itself an over-claim — corrected
> 2026-08-18.** It read: *"the trace field of an `n`-tetrahedron hyperbolic knot is
> generically degree `n`, and a quadratic cannot sit inside an odd degree."* The
> **second** clause is the tower law and is rigorous — it is what excludes ℚ(√−7)
> from the 5₂ cubic, so **everything above stands.** The **first** clause is
> **false**: the Whitehead link (4 tetrahedra = one regular ideal octahedron) and the
> Borromean rings (8 = two octahedra) both have trace field **ℚ(i), degree 2**. The
> count does not bound the degree from below, and "generically" does not rescue it —
> these are two of the most-cited links in the subject, and the Whitehead is
> [a corpus worked case](2026-08-02-whitehead-c-sigma-closed-form-2-pow-minus-3-4.md)
> that already states ℚ(i) here.
>
> The heuristic held for exactly the two knots this audit was looking at, 4₁ and 5₂ —
> **a coincidence promoted to a rule, inside the correction written to fix a
> coincidence promoted to a rule.** Certification:
> [`knot_trace_field_degree_guard_counterexample.py`](../../computations/probes/knot_trace_field_degree_guard_counterexample.py)
> (5/5). Bean `qou-5gh6`.

**The usable guard.** A field claim about a hyperbolic knot needs a degree check, and
the degree must be **computed, not inferred**: solve the gluing equations, recover a
shape's minimal polynomial, take its degree — which is what the certification probe
above actually does, and why the 5₂ result holds independently of the bad heuristic.
Then apply the tower law: a quadratic cannot sit inside an odd degree.

## Cross-references

- Certification: [`qbeta_5two_trace_field_disc23_not_qsqrt7.py`](../../computations/probes/qbeta_5two_trace_field_disc23_not_qsqrt7.py)
  · witness `qbeta-5two-trace-field-disc23-not-qsqrt7.witness.json`
- Retracted: [`2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md`](2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md)
- Lean (already correct): `QOU.QBeta.disc_eq_neg_23`
- σ-pair tower (the √−23 bar-odd line): [`qbeta_5two_gswz_saddle_arithmeticity_probe.py`](../../computations/probes/qbeta_5two_gswz_saddle_arithmeticity_probe.py)
  §4 — *"Bar-odd projection: `P_k^{σ1} − P_k^{σ2} = b_k(ξ₁−ξ̄₁) + c_k(ξ₁²−ξ̄₁²) ∈ √−23·ℝ-axis
  of K ⊗ ℂ` — the exact odd-channel tower"*. Its §1 also states the trace field as
  `ℚ[ξ]`, `ξ` a root of `x³−2x²+3x−1` (disc −23) — i.e. the live lane had it right.
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Bean: `qou-ynff`
