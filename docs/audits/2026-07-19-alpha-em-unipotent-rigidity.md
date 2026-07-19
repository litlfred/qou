# α_EM — unipotent rigidity: R1 closed in full (2026-07-19)

**Context:** owner-directed follow-up to R1/N3
([#4072](https://github.com/litlfred/qou/pull/4072)): *work on the only
invisible piece — the unipotent part of the T2 monodromy.*

**Probe:** [`computations/alpha_em/alpha_em_unipotent_rigidity_probe.py`](../../computations/alpha_em/alpha_em_unipotent_rigidity_probe.py)
→ [`alpha-em-unipotent-rigidity.witness.json`](../../computations/alpha_em/alpha-em-unipotent-rigidity.witness.json)
— 4/4 PASS, sympy-exact (constructive rigidity on the full parameter
family).

**Scope guard (STRICT):** R2 not asserted; no fit; nothing wired; `1/(8π)`
stays phase-4.

## The result — the invisible piece carries no freedom

- **U1 — the algebra side is intrinsically non-semisimple.** The
  framework's own `H₂(i) = ℂ[σ]/((σ−i)²)` has regular representation equal
  to the Jordan block (explicit basis-swap conjugation). The unipotent part
  is not imported from geometry — the framework's algebra carries it
  already.
- **U2 — the geometric unipotent is Picard–Lefschetz.** The full twist
  (Dehn twist about the two branch points, = the T2 half-twist squared)
  acts as the transvection `1 + 2N` (N rank-1 nilpotent, exact) — standard
  vanishing-cycle monodromy, at the same integral point as the
  Gambaudo–Ghys signature jump.
- **U3 — rigidity.** The 2-dim module with `(σ−i)² = 0`, `σ ≠ i·1` is
  **unique up to isomorphism**: every nonzero 2×2 nilpotent
  `[[p,q],[r,−p]]` (p²+qr = 0) is explicitly conjugate to `[[0,1],[0,0]]`
  on both parameter branches, with nonzero determinants. So any τ matching
  the semisimplified data — which R1/N3 closed — matches the unipotent part
  **automatically**. There is no second invariant to transport.
- **U4 — skein consistency.** On the Jordan module `σ⁻¹ = σ − 2i` exactly:
  the §7a skein relation holds identically; the Hecke relation at q=i has
  exactly two module classes (scalar, Jordan) and the monodromy selects
  Jordan. No residual freedom anywhere.

## Final wall state

```
R1: CLOSED IN FULL — semisimplified level (#4072) + unipotent level (this).
R2: the wall's ENTIRE surviving open content — the loop-weight provenance
    (the tower's one-loop insertion is F(b_s/[2]_q at q=1) weighted by
    a₀·α): a pure physics identification with ZERO functorial residue.
    Phase-4, owner-gated.
```

Every functorial question raised by the τ-correspondence program — from the
first obstruction (`a6d522e0a`) through the B-plan, the numerical
exclusions, and the F-construction — is now answered and machine-verified.
What remains is exactly the statement only the owner can canonize.
