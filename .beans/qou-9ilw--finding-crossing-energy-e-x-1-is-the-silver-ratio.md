---
# qou-9ilw
title: 'FINDING: crossing energy E_x = 1 IS the silver-ratio beta-decay null (h=2 branch); E_x=0 is the h=0 branch'
status: in-progress
type: task
created_at: 2026-08-30T14:01:38Z
updated_at: 2026-08-30T14:01:38Z
---


## The identity

The corpus defines crossing energy per crossing as
`𝔈_×(q) = ½(q − q⁻¹)` (`binding-knots-visual-inventory.md`), and the Hecke
parameter as `h = q − 1/q`. So **`𝔈_× = h/2`**, and therefore

    𝔈_× = 0  ⟺  h = 0  ⟺  q = 1
    𝔈_× = 1  ⟺  h = 2  ⟺  q = 1 + √2   (silver ratio, q² = 2q + 1)

`prop:silver-ratio-beta-decay-null` is carried in Lean as
`QOU.ParticleInteractions.beta_decay_null_iff_h_zero_or_two`. Its two roots
`h ∈ {0, 2}` are therefore **exactly the two crossing energies 0 and 1**.

The corpus already treats the silver ratio as distinguished — `c_8, c_9, c_10`
become rational there (`prop:qbeta-c8-c10-silver-rationals`), `c_5` is a
Pell–Lucas outlier there and *not* at the golden ratio, and the σ-eigenvalues
are `1 ± √2` (self-referential fixed point). What is **not** recorded anywhere
is that this is the unit-crossing-energy point. Corpus-grep: every file
mentioning "silver ratio" and every file mentioning "crossing energy", zero
overlap outside the definition index.

## Why it is worth recording

The β-decay null is stated as a condition on `h`, which reads as an algebraic
accident. Restated as `𝔈_× ∈ {0, 1}` it reads as a physical statement: the
null occurs exactly when each crossing carries zero or unit energy. Same
theorem, and the second phrasing is the one a reader can interpret. That is a
naming/exposition fix, not new mathematics — but the corpus is a folio, and an
uninterpretable statement of a true theorem is a defect it cares about.

## What it does NOT do — do not overclaim

It does **not** connect to the volume conjecture, and the question it arose
from ("is there a limit where crossing energy = 1 and we recover the VC?")
answers **no**:

* VC lives at `|q| = 1`, `q = exp(2πi/N)`, `N → ∞` — approaching 1
  *tangentially along the unit circle*.
* `𝔈_× = 1` is `q = 1 + √2 ≈ 2.414`, real, modulus 2.414. Not on the circle;
  setting `𝔈_× = 1` moves **away** from the VC regime, not toward it.
* Worse, both β-decay-null roots are degenerate for the mass formula. At
  `q = 1`, `ℏ_q² → 0` so `Vol/ℏ_q² → ∞` (the mass term diverges). At the
  silver ratio the theorem's own content is that proton and neutron
  Markov-traces become *categorically indistinguishable* — a trace degeneracy,
  i.e. the point where the formula stops separating what it must separate.

## The limit that DOES recover the bare volume

`q → ∞`: `ℏ_q = 1 − 1/q → 1`, so `Vol/ℏ_q² → Vol` exactly. Measured:

| q | 𝔈_× | ℏ_q² | 1/ℏ_q² |
|---|---|---|---|
| q₀ ≈ 1.10998 | 0.10453 | 0.0098171 | 101.86 |
| 1+√2 | 1 | 0.34315 | 2.9142 |
| 10 | 4.95 | 0.81 | 1.2346 |
| 1000 | 499.9995 | 0.998001 | 1.0020 |
| → 1⁺ | → 0 | → 0 | → ∞ |

So the mass formula's volume term degenerates to the bare hyperbolic volume in
the large-`q` limit and diverges in the `q → 1` limit — and the VC regime sits
at the divergent end, approached along a direction the real-`q` axis never
takes.

## The real content: two non-commuting limits

This is the standard radial-vs-tangential dichotomy, and it is worth stating in
the corpus because the mass formula and the VC live on opposite sides of it:

* **radial** `q → 1` (real axis, the substrate direction) — Melvin–Morton–
  Rozansky: the colored Jones degenerates to the **Alexander** polynomial.
  Abelian/torsion data. No volume.
* **tangential** `q → 1` along roots of unity — Kashaev/VC: **hyperbolic
  volume**.

The object where both live is the **Habiro ring** (cyclotomic completion), which
is precisely what the corpus's whole `qbeta`/Habiro cluster is built on. So the
framework for asking "does the substrate ray see the volume?" already exists
in-repo; what is missing is anyone having pointed it at this question.

## Next

- [ ] Restate `prop:silver-ratio-beta-decay-null` in terms of `𝔈_× ∈ {0,1}` in
      the content block (exposition fix, same theorem).
- [ ] Record the `q → ∞ ⇒ Vol/ℏ_q² → Vol` limit somewhere a reader of the mass
      formula will meet it.
- [ ] Decide whether the radial/tangential non-commutation deserves its own
      block. It bears directly on whether the substrate pin can ever see VC.
