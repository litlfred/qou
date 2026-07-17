# W_λ realization — the observable-side unitarity/normalization gate (formalize-first reduction)

**Date:** 2026-07-17 · **Axis:** Subgoal-2 q₀ / s5-so3 keystone (geometric W_λ wall) ·
**Tier:** symbolic-exact (q-symbolic identity + RSK/Burnside q=1 anchor) ·
**No q₀ derivation, no fit, nothing wired, no tier change.** A *reduction* of one wall.

Complements — from the **observable (real q₀)** side — the sibling's **fibre-ζ** Lawrence–Rozansky
modulus spec ([`2026-07-17-three-front-attack-specs.md` §2](2026-07-17-three-front-attack-specs.md)),
which targets `|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)` at roots of unity. This audit does not compute
that amplitude; it pins the *normalization* any realization must satisfy at the observable q₀.

Probe [`keystone_wlambda_unitarity_normalization_gate_probe.py`](scripts/keystone_wlambda_unitarity_normalization_gate_probe.py)
→ [witness](scripts/keystone-wlambda-unitarity-normalization-gate.witness.json) (4/4).

## The reduction

The full-Hecke q-Plancherel weight is `W_λ = d_q(λ)²/[n]_q!`. Summed over `λ⊢n`:

`Σ_{λ⊢n} W_λ = Z(q) := (Σ_{λ⊢n} d_q(λ)²) / [n]_q!`,  with (verified n=2..5, q-symbolic):

- **`Z(1) = 1`** exactly — this is the **RSK/Burnside** identity `Σ_λ (f^λ)² = n!`; W_λ is a
  normalized measure **only** at q=1.
- **`Z(q₀) < 1`** for the substrate q₀: `n=2: 0.99458, n=3: 0.98744, n=4: 0.98216, n=5: 0.98222`.
  The `n=5` value **is** the ledger's P1 "sub-normalized `Z = 0.98222`" number — this audit supplies
  its S-matrix-unitarity *framing*.

**The gate.** A **unitary** modular S-matrix vacuum row satisfies `Σ_λ |S_{0λ}|² = 1` (unitarity),
i.e. it induces a *normalized* probability measure. Since `Σ_λ W_λ = Z(q) < 1` for `q ≠ 1`,

> **W_λ is not the vacuum-row probability measure of any unitary modular category at real q ≠ 1.**

So a compact/unitary S-matrix realization is excluded **not only** because it is q₀-*independent*
(the ledger's existing reason — rational sines) **but by an exact normalization (completeness)
obstruction**: any unitary row is normalized, W_λ is sub-normalized by exactly `Z(q)`. The geometric
object hosting W_λ at the observable q₀ must therefore be **non-unitary**, carrying completeness
defect exactly `Z(q)` — which **reinforces the redirect to the non-compact Hahn–Exton q-Bessel**
vacuum row (q₀-dependent, non-unitary), the corpus's current geometric target.

## Why this sharpens the wall

- **It pins a q-symbolic, machine-checkable gate:** `Σ_λ d_q(λ)² = Z(q)·[n]_q!`, `Z(q) < 1` for
  `q ≠ 1`. Any proposed geometric realization is testable against it *before* the (deferred) colored-LR
  compute: if the candidate is unitary, it fails this gate.
- **It identifies the "mass defect" `1 − Z(q)` as a failure of completeness/unitarity** of the
  untruncated q-dimension family at real q — a structural statement, distinct from (and complementary
  to) the defect-cubic *n*-scaling `1 − Z ≈ C(n)h² + …` (which characterizes *how* it grows, not *what*
  it is). The two together: the defect is the non-unitarity, and it grows as the proved cubic.
- **It bridges to the fibre spec:** the sibling's `|S_{0λ}(ζ)| = d_ζ/D` lives at the fibre (where a
  level-truncated modular category *is* unitary over its admissible λ); this gate lives at the
  observable q₀ (full, untruncated λ, non-unitary). The two are the two faces of the fibre→archimedean
  passage — the realization must be unitary-at-ζ **and** carry the `Z(q₀)` defect at q₀.

## Corollary — the "continuation wall" is not separate; it *is* the amplitude

The other named wall of C is the **fibre→archimedean continuation** (passing the object from the
fibre roots of unity ζ to the observable q₀). This audit's normalization decomposes it cleanly:

- **The normalization leg continues trivially.** `Z(q) = Σ_λ d_q(λ)²/[n]_q!` is a **rational
  function of q** (verified n=2..5; e.g. `n=2: 2q/(q²+1)`). A rational function continues to *any*
  real q₀ (bar poles) — there is **nothing to derive** in continuing the normalization from ζ to q₀.
- **The amplitude leg is the whole difficulty.** What does *not* continue trivially is the
  non-rational Lawrence–Rozansky / WRT q-series (the vacuum-row *amplitude*) — which is exactly the
  **LR-modulus front** (the sibling's fibre-ζ spec).

So "the fibre→archimedean continuation" is **not an independent wall**: its normalization part is
trivial (rational `Z`), and its amplitude part *is* the LR-modulus wall. C's genuinely-remaining
pieces are therefore (i) the colored-LR amplitude compute (fibre spec, deferred) and (ii) a
**q₀-fixing categorical condition** (the Bring-Jacobian `E⁴` W-plane modulus route — **numerology-
gated**: the ledger's STRICT rule is *formalize the monodromy operator, never fit `τ(q₀)=2.6424`*).
There is no distinct "continuation" problem to solve.

## Scope guard (STRICT)

- **Not a q₀ derivation.** This constrains the *normalization* of the geometric object; it says nothing
  about q₀'s *value* (still CAL-2 calibrated).
- **Not a closure.** It reduces/sharpens the wall (pins the gate, identifies the non-unitarity); the
  colored-LR Σ(2,3,5) amplitude compute (fibre spec) and the fibre→archimedean continuation remain the
  open pieces.
- **No fit, nothing wired, no tier change.** The `Z = 0.98222` value is the ledger's existing P1
  number, reframed — no new number is claimed.

## Cross-references

- Fibre-ζ modulus spec (complement): [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md) §2
- Keystone ledger (P1 sub-normalization, non-compact q-Bessel redirect): [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- Defect cubic (the `1−Z` n-scaling): `WLambdaDefectClosedForm.lean`, `2026-06-24-wlambda-defect-cn-closedform-crosscheck.md`
- RSK/Burnside `Σ(f^λ)²=n!` (the q=1 anchor / Identity-I): the on-main RSK brick program
