---
# qou-ubsl
title: 'A3: symmetry energy = isospin/SU(4) Casimir on the Wedderburn partition'
status: completed
type: task
priority: normal
created_at: 2026-08-07T08:37:50Z
updated_at: 2026-08-31T03:14:19Z
parent: qou-kemt
---

Read the Casimir eigenvalue off lambda (C_2 = sum lambda_i(lambda_i+n+1-2i)); SU4SupermultipletGate.lean stopped at 4He locality. **ROAST (three, one serious):** (i) the Casimir gives (N-Z)^2, NOT (N-Z)^2/A -- the 1/A is Fermi-gas level density, a SEPARATE dynamical input; my memo wrongly claimed the Casimir supplies the shape. (ii) Descartes forces dim V=2, so Schur-Weyl gives GL(2) NOT GL(4) -- the SU(4) reading may be structurally FORBIDDEN. Resolve (ii) before any work. (iii) Wigner SU(4) is badly broken by spin-orbit above A~40.

## 2026-08-31 — objection (ii) RESOLVED: the SU(4) reading is structurally forbidden. A3 closed.

The ROAST said *"Descartes forces dim V=2, so Schur–Weyl gives GL(2) NOT GL(4) — the
SU(4) reading may be structurally FORBIDDEN. Resolve (ii) before any work."* Resolved,
and not by tracing the Descartes argument — by measuring the corpus's own weights.

**1. The trace annihilates every partition with more than two rows.** At convention D
(Wenzl level `r = 2`), `y_λ = 0` whenever `ℓ(λ) > 2`. Verified directly against
`markov_weights_symbolic.y_lambda_symbolic` for `n = 3…6`:

| n | surviving shapes | annihilated |
|---|---|---|
| 3 | (3), (2,1) | (1,1,1) |
| 4 | (4), (3,1), (2,2) | (2,1,1), (1⁴) |
| 5 | (5), (4,1), (3,2) | (2,2,1), (3,1,1), (2,1³), (1⁵) |
| 6 | (6), (5,1), (4,2), (3,3) | all seven with ℓ ≥ 3 |

Max surviving row count is **2, at every n**. SU(4)/Wigner supermultiplet labels need
partitions with up to **four** rows — precisely the ones the observable cannot see.

**2. On the shapes that do survive, the SU(4) Casimir carries no new information.**
With `C₂ = Σᵢ λᵢ(λᵢ + m + 1 − 2i)`, on a two-row `λ = (λ₁, λ₂)`:

    C₂^{GL(4)} − C₂^{GL(2)} = 2(λ₁ + λ₂) = 2n     — a CONSTANT at fixed strand number.

So the two Casimirs differ by an additive constant and are informationally identical.
At fixed `n` both reduce to functions of `(λ₁ − λ₂)` alone: one degree of freedom, which
is just SU(2) isospin `T = (λ₁−λ₂)/2`.

**Verdict: forbidden, not "may be".** Twice over — the SU(4)-distinguishing shapes have
zero weight, and on the surviving shapes the SU(4) label collapses to the SU(2) one the
trace already carries. A3 offers no new object.

Objection (i) was already conceded in this bean's own text (the Casimir gives `(N−Z)²`,
not `(N−Z)²/A`; the `1/A` is Fermi-gas level density, a separate dynamical input), and
(iii) — Wigner SU(4) broken by spin-orbit above A ≈ 40 — is untouched and now moot.

## 2026-09-04 — promoted to the top lead, with a number

Correlation of the additive law's residual `B_exp/(E_0.S)` against the three SEMF
shapes, 2548 measured AME nuclides
(`computations/qbeta/qbeta_tower_log_z_and_roast_probe.py`):

    (N-Z)^2/A^2   [asymmetry]   **-0.804**
    A^(-1/3)      [surface]       -0.178
    Z^2/A^(4/3)   [Coulomb]       -0.044

`docs/audits/2026-09-04-binding-law-options-decision-frame.md` named the SURFACE
term / edge set (`qou-h7mh`) as "the strongest lead". Wrong by 4x in correlation
— corrected there. **The dominant missing physics is the symmetry energy, which
is this bean.**

Sharpening it: the derived law already HAS an `(N-Z)` term, at first order
`+2(q0-1)(N-Z)`, and it has the **wrong sign** — the data wants `~-0.15(N-Z)`
(`qou-q7ga`). So the target is not "add a symmetry term" but "explain why the
isospin Casimir enters with the opposite sign to the q-deformation's own
splitting of `b_pp` and `b_nn` about `z`".
