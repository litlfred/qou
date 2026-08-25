# PROBE C4 — Bring adjoint torsion as a candidate non-algebraic `HH₁` pairing

**Date:** 2026-08-07 · **Branch:** `claude/pneqnp-residue-hh1-torsion-probes-2026-08-07`
(PR #4687) · **Status:** scoped + coordinated + **gated** (no Lean yet — honestly
deferred, see §Gate). Companion to PROBE A (`OuterDerivationResidue.lean` +
`hh1_hecke_outer_derivations.py`, same PR).

## What C4 targets

The P≠NP wall's open link is `res ≠ 0`, where `res` is a fibre-level `HH₁`
cocycle over Bring that must be **(a) a non-trace** [proved:
`not_trace_of_separates_commutator`, merged #4511], **(b) non-algebraic**
[algebrization barrier], **(c) beyond every finite Vassiliev order** [#4511 doc].

PROBE A addresses the *home* of clause (a): the residue is an **outer**
derivation, and outer derivations exist exactly at the root-of-unity/fibre level
(confirmed `dim HH¹(H₃(ζ)) = 1` at `[2]_q=0`, `[3]_q=0`; `= 0` generic).

**C4 addresses clause (b): the *non-algebraic* witness.** The concrete proposal:
the **adjoint Reidemeister torsion** of the Bring surface `Σ₄` (genus 4, `S₅`
symmetry) furnishes a linear pairing on `H¹(Σ₄) = ℂ⁸`, and its value is a
**transcendental** period/regulator — hence not an algebraic (poly-time /
finite-Vassiliev) invariant. A transcendental torsion pairing that also separates
a commutator (non-trace) would satisfy clauses (a)+(b) simultaneously.

## Why torsion is the right object

Reidemeister/adjoint torsion is the canonical *non-algebraic* invariant attached
to a hyperbolic/flat-connection geometry: it is a regulator (a ratio of periods),
and for hyperbolic pieces it lands on values like `Cl₂(θ)` (Clausen), `4G`
(Catalan), `2^{k/2}`, etc. — transcendental (or conjecturally so) numbers, not
elements of an algebraic weight-system tower. This is exactly the "beyond every
finite Vassiliev order" altitude clause (c) demands: the Kontsevich-integral tail
/ non-Lie-type invariants live here, not in the finite-type filtration.

## The merged inputs C4 consumes (already on `main`)

The adjoint-torsion compute needed to *evaluate* the pairing landed this week:

- `qou-pn5j` — `|τ(L5a1)| = 2^{5/2}` derived from the octahedral NZ data.
- `qou-k00d` — the unified multi-cusp 1-loop torsion law `exp(2c₀) = 2^{c−1}/|det|`
  (3-cusp Borromean cross-check).
- The Whitehead `c_σ = 2^{−3/4}` adjoint-torsion template (20-digit mpmath).

C4 does **not** re-derive these; it asks whether the *Bring* Σ₄ instance of the
same torsion law produces a **transcendental** value on the `H¹` pairing.

## The gate (why no Lean this session — honest deferral, not laziness)

C4's Lean formalization is blocked on two genuine dependencies, **not** on
effort:

1. **Clausen / transcendental-value infra** is mid-flight in PR #4532 (Whitehead
   Volume Conjecture: `QOU.Knot.Clausen`, `catalanG_eq_clausen_pi_div_two`). C4's
   clause-(b) statement (`Transcendental ℚ (torsion-pairing value)`) should
   consume that module rather than re-derive it. Coordination note posted on
   #4532.
2. **No corpus definition of "adjoint Reidemeister torsion of Σ₄"** exists yet;
   writing one from scratch as an axiomatized input would be **anti-laundering
   forbidden** (a `class` carrying the transcendence conclusion as a field, with a
   projection "theorem", is a vacuous self-assuming stub per §3b-cond
   non-degeneracy). The honest path is to build the torsion *definition* from the
   merged NZ-data compute first, then state the transcendence as a falsifiable
   claim over it.

**Therefore C4's next honest step is a *computation*, not a premature Lean class**:
extend the merged 1-loop torsion law to the Bring Σ₄ NZ data and read off the
candidate pairing value; only once a concrete value (e.g. a Clausen/Catalan-type
number) is in hand does the Lean transcendence statement become non-vacuous.

## Honest scope

- C4 is a **localization of clause (b)**, not a wall crossing. Even a proved
  transcendental torsion pairing is *necessary*, not *sufficient*: it must also be
  the *same* cocycle that carries the decision content (the non-trace clause (a)
  outer derivation from PROBE A). Tying (a) and (b) to one object is the whole
  difficulty and remains open.
- Per the anti-fit / anti-laundering discipline: a torsion value obtained by
  fitting the AME/observable anchors would be a fit, not a derivation, and could
  not be wired as the residue. Only a value *derived* from the Σ₄ geometry counts.
- No `res ≠ 0` instance is asserted anywhere in this branch.
