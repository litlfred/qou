# α_EM R2 decomposition — the unproven core shrinks to a QFT convention (2026-07-19)

**Context:** owner: *"work on r2"*, under the standing ruling
([`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)):
R2 is not Lean/derived-proved. This tranche does **not** prove R2 — it
decomposes it, derives three of its four legs from corpus results, and
names the residue at its sharpest.

**Probe:** [`computations/alpha_em/alpha_em_r2_decomposition_probe.py`](../../computations/alpha_em/alpha_em_r2_decomposition_probe.py)
→ [`alpha-em-r2-decomposition.witness.json`](../../computations/alpha_em/alpha-em-r2-decomposition.witness.json)
— 4/4 PASS.

**Scope guard (STRICT):** R2 remains unproven; R2b is a coherence argument
(not a theorem); the core is open; no fit; nothing wired; `1/(8π)` stays
phase-4.

## The decomposition

| Leg | Statement | Status |
|---|---|---|
| **R2a** | one loop = one KL insertion (`b_s`, eigenvalue `[2]_q`) | **derived** — it is inside the derived Habiro element `[2]_q(1−h²α)` (#1511, binomial-exact) + B4a |
| **R2b** | the n=2 term's home is `H¹(Bring)` | **coherence** from the *canonical* n=1 identification (#2114/#3920): one self-energy expansion, one home; zero-retuning evidence (one (b₁, Area, a₀) vocabulary, exact ratio 16/3) |
| **R2c** | the weight is `½·a₀` | **squeezed** by three derived results: #1511's geometry-independent coefficients (x carries no Bring moduli ⟹ universal), #3909's derived π-origin (heat kernel is the unique candidate giving π-power −1 ⟹ x = rational·a₀), B4b's proved ρ-split (rational = ½ given the pair premise) — no rational freedom remains |
| **R2-core** | *"the loop expansion weighs proper time by the standard Schwinger measure with unit normalization — one per-mode unit on the doubled pair"* | **OPEN** — the residue |

## What changed

R2's unproven content is no longer a statement about Bring, Hecke, or the
functor F — all of those legs are derived or canonized. The residue is a
**QFT-dictionary normalization convention** of textbook species (which
proper-time measure the framework's loop expansion uses). Smaller,
sharper, still open, still owner-gated — exactly as the ruling requires.

## Honest caveats

- R2b's "one expansion, one home" is a coherence principle applied to an
  *accepted identification*, not a theorem; a skeptic can decline it.
- R2c's universality squeeze narrows the candidate space to `rational·a₀`
  via #3909's *adjudicated candidate list* — a fourth, never-considered
  origin for the π would reopen it (the adjudication was exhaustive over
  the named candidates, not over all conceivable ones).
- Nothing here upgrades any tier; the program-outcome statement is
  unchanged: *derived conditional on R2; R2 open.*
