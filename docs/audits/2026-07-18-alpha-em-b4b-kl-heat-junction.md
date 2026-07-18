# α_EM bean B4, brick b — the KL↔heat junction: the ½ is ρ-forced (2026-07-18)

**Bean:** `qou-1p06` (B4) of the τ-correspondence proof plan (milestone
`qou-b5qg`). Upstream: B1 merged
([#3955](https://github.com/litlfred/qou/pull/3955)), B2 shadow merged
([#3960](https://github.com/litlfred/qou/pull/3960) — `q=i↦H^{1,0}` FORCED),
B3 merged ([#3969](https://github.com/litlfred/qou/pull/3969) — Clause A =
B2-lift + B4), B4a merged
([#3973](https://github.com/litlfred/qou/pull/3973) — the ½ is a
decategorification-point constant with KL carrier `b_s/[2]_q`).

**Probe:** [`computations/alpha_em/alpha_em_b4b_kl_heat_junction_probe.py`](../../computations/alpha_em/alpha_em_b4b_kl_heat_junction_probe.py)
→ [`alpha-em-b4b-kl-heat-junction.witness.json`](../../computations/alpha_em/alpha-em-b4b-kl-heat-junction.witness.json)
— 4/4 assertions PASS (sympy-exact + exact-bijection numerics).

**Scope guard (STRICT):** scope-(a); derives nothing unconditionally; no
fit; nothing wired; `1/(8π)` stays phase-4.

## The junction claim (conditional on the B2 lift)

The heat unit `a₀·α` carried by one loop lives on the conjugate-**doubled**
space `H^{1,0}⊕H^{0,1}` (the #3920 doubling read through τ); the physical
channel is **one** member of the pair (the FORCED B2-shadow assignment); and
**reality of the Laplacian forces the unit to split equally** across the
conjugate pair. Hence the per-channel weight is `½·a₀·α` — the ½ is not a
convention and not a fit: it is the ρ-forced equal split.

## What was verified (V1–V4)

**V1 — one loop = one KL insertion (exact).** The KL element `b_s = σ + q⁻¹`
has channel spectrum `([2]_q, 0)`: the one-loop coefficient `−[2]_q·x` is
`−(KL eigenvalue on e₊)·x` **exactly**. The q-dependence of the one-loop term
*is* the KL eigenvalue — and its q=1 value 2 is the conjugate-pair count.

**V2 — ρ-forced equal split, abstract (exact).** If an antilinear involution
intertwines the component Laplacians (`Δ|_{H^{0,1}} = conj∘Δ|_{H^{1,0}}∘conj`)
and Δ is self-adjoint (real spectrum), then every spectral trace splits
equally: `Tr((conj A)^m) = conj(Tr A^m) = Tr(A^m)` for hermitian A. Verified
sympy-exact on a concrete complex-rational 3×3 hermitian matrix, m = 1…5.
**Reality is the mechanism.**

**V3 — ρ-forced equal split, geometric model (exact bijection).** On the
flat-torus H¹, conjugation maps the (1,0) k-mode to the (0,1) (−k)-mode; the
component heat traces are term-by-term equal under k↦−k (machine-0 at
t=10⁻², 10⁻³; the bijection makes the equality exact, not asymptotic).

**V4 — assembly arithmetic + disambiguation (exact).**
`½·a₀ = 1/(8π)` exactly; per-channel `x = a₀α/2` restores the full doubled
unit at q=1 (`[2]_1·x = a₀α` — V1's KL eigenvalue = the pair count); and the
½ is the **conjugate-pair share** (count 2, #3920's Hodge doubling), **not**
`1/b₁` (`b₁(Bring) = 2g = 8`; `1/(π·b₁) = 1/(8π)` is numerically coincident
but a different decomposition — this resolves the "three readings of the 2"),
and **not** the resolvent equal-weight (that lives at `q² = −1`, excluded as
Clause B by merged F2).

## Net effect: the wall reduces to ONE open statement

Given the B2 functorial lift (with its premise that one loop's mode space is
carried to the conjugate pair `H^{1,0}⊕H^{0,1}`):

- the **a₀** factor is inherited (B3: conformal class ⟹ universal heat unit);
- the **½** factor is forced (this brick: ρ-reality equal split + the FORCED
  B2-shadow channel assignment);
- the tower's own `[2]_q` (= the KL eigenvalue, B4a+V1) restores the doubled
  total at q=1 — `q→1 one-loop = [2]_1·x = a₀·α`, which is exactly B4's
  target statement.

**Everything in `½·a₀` now has a conditional derivation route; the single
remaining open statement is the B2 lift itself** (bean `qou-tq20`,
Mathlib-gated), i.e. that the categorical τ-functor carries ρ to the Hodge
conjugation of `H¹(Bring)` with the loop mode space landing on the conjugate
pair. B4b does **not** derive the lift.

## Position in the proof plan

```
B1 (ρ reality structure)      MERGED #3955
B2 (functorial statement)     shadow MERGED #3960; LIFT = the single remaining open wall
B3 (conformal inheritance)    MERGED #3969
B4 (classical-limit norm)     B4a MERGED #3973; B4b THIS — ½ ρ-forced conditionally
B5 (assembly)                 now = write the conditional theorem "B2-lift ⟹ measure = ½·a₀"
                              (all bricks in place)
```

Next: **B5 assembly** — state the full conditional theorem with every merged
brick cited, and formalize the assembly skeleton in core Lean where statable
(the ρ-split trace equality and the [2]_q-restoration identity are
finite/decidable; the lift stays an honest named hypothesis, never an axiom —
per §"Axiomatization is NOT a Proof").
