
## 🔥 Scope assessment (2026-08-02) — R2 is a genuine Mathlib GAP, not a quick win

Honest finding (rule 14): **Mathlib has NO Schur–Weyl duality** — classical
or quantum. A grep finds only `SchurZassenhaus`, `CategoryTheory…Schur`
(Schur's lemma), and `Matrix.SchurComplement` — none is the
`GL(V) × S_n ↷ V^{⊗n}` double-centralizer, let alone the
`U_q(gl_N) × H_n(q)` quantum version. Full quantum Schur–Weyl for Hecke
algebras is a multi-week formalization; it CANNOT be landed sorry-free in a
session, and I will not fake it with a `sorry`-scaffold or trivial-true.

**What IS tractable (honest sub-lemmas, for a future push):**
1. **Trace additivity over a finite direct sum** — `tr` over `⊕_λ M_{d_λ}`
   equals `Σ_λ tr(block_λ)`. This is the *linear backbone* of
   "partition function = character sum" and is provable from Mathlib
   (`Matrix.trace`, `map_sum`). Non-trivial-enough only if stated over the
   Wedderburn decomposition, which needs (2).
2. **The Wedderburn iso `H_n(q) ≅ ⊕_λ M_{d_λ}(K)`** — this is the real gap.
   Mathlib has `WedderburnArtin` (existence of *a* decomposition for
   semisimple rings) but NOT the explicit partition-indexed one for the
   Hecke algebra with the Hoefsmit matrix units. This is the load-bearing
   missing piece.
3. **Character formula `tr_M = Σ_λ w_λ χ_λ`** then follows from (1)+(2).

**Recommended decomposition into child beans (future):**
- `R2a`: trace additivity over `⊕` (near-term, ~Mathlib one-lemma).
- `R2b`: `H_n(q)` semisimple + `WedderburnArtin` instance (medium).
- `R2c`: the explicit partition-indexed matrix-unit iso via Hoefsmit
  (the hard, multi-week gap — where quantum Schur–Weyl actually lives).

Status: R2 left as `todo` — flagged as a hard gap, deliberately NOT
attempted this session to avoid a dishonest scaffold. R1 (`qou-j6lf`)
correctly consumes `y_λ>0` as given precisely because R2 is the piece that
would *supply* those weights.
