# Super/graded formalism — object-role map + honest simplification verdict

**Date:** 2026-07-20. **Scope:** resolves beans `qou-bf8r` (object-role map) and
records the **provisional** verdict for `qou-lzpr` (proof-simplification /
exposition review). Full audit deferred until the Lean layers land (`qou-83nk`
super/Berezinian, `qou-bj20` Lie-superalgebra). **Goal: shorten + clarify, NOT
tell a pretty story** — negatives are reported plainly.

## Candidate superalgebra

`U_q(osp(1|2))` — the quantum orthosymplectic superalgebra. Chosen because its
**even part is `U_q(sl₂)`**, which already underlies the framework's Hecke /
braid algebra `H_n(q)` (generator σ_i). The odd (fermionic) generators are the
new piece. Its **supertrace** reproduces the `(−1)^m` grading and its
**super-quantum-dimension** is the Berezinian — i.e. the super structure is not
bolted on, it sits on top of the existing `U_q(sl₂)`/Hecke spine.

## Object-role map

| Super role | QOU object | Status |
|---|---|---|
| Even (bosonic) generators | su(2) Reeb triad `M_i,M_j,M_k`, `[M_i,M_j]=2M_k`; `U_q(sl₂) ⊂ σ_i` (Hecke) | Reeb bracket proved sorry-free (`BringCone.lean`) |
| Odd (fermionic) generators | state section `ψ` / the `ψ*⊗𝒟_∇ψ` term of `ℒ_q` (`def:categorical-lagrangian`) | exists; not yet super-typed |
| Grading operator `(−1)^F` | the `(−1)^m` bar-parity (Door-v residual) | measured (Door-v probe) |
| Even (bar-even) sector | cosh face = **mass** = C1 binding kernel | C1 proved (q-lift) |
| Odd (bar-odd) sector | sinh face = **decay** = GGM / Q_β | GGM = colored-Jones face |
| ordinary trace `tr_M` → | **supertrace** `str = tr₊ − tr₋` where grading present | corpus uses `tr_M` (implicit str only in Bring Euler char) |
| ordinary determinant → | **Berezinian** (super quantum dim) at even/odd-mixing orders | corpus uses none (`qou-83nk` adds it) |

## Honest verdict (provisional)

**Where it plausibly clarifies (real):**
- The bar-even/bar-odd split collapses into **one grading operator** instead of
  two parallel channels — a genuine unification, one object not two.
- Door-v's `(−1)^m` residual stops being a separately-discovered fact and
  becomes the **definition** of `str`.
- The Q_β `c_k` cross-terms get a principled home (Berezinian expansion) — the
  one place it might close a real gap (see `2026-07-20-super-berezinian-dm-cubic-narrowing.md`).

**Where it does NOT help (honest negatives — do not oversell):**
- It **shortens no existing sorry-free proof.** The Hecke / Markov-trace proofs
  are already tight; super-typing them is *new content*, not a proof-shortener.
  This mirrors the §7b KLR-audit precedent (`2026-05-30-klr-dialog-assessment.md`:
  0/6 candidate proofs shortened by a crystal/KLR layer).
- It adds import/typeclass weight (super vector spaces, `ZMod 2` grading).
- Absent a **derived** gap-closure, it is exposition-additive — i.e. a "pretty
  story" — and should then be **dropped**, not kept for elegance.

**Net:** worth it **only as a gap-closer** (the Q_β `c_k` Berezinian derivation,
`qou-83nk`/`qou-jqof`). As a proof-simplification retrofit it does not pay for
itself. Re-run the full `qou-lzpr` audit once `qou-83nk` + `qou-bj20` land, with
the concrete test: *did any pre-existing proof get shorter, or any observable
get a derived (not fitted) term?* If neither, the honest disposition is to keep
only the minimal grading operator + `str` (which unify Door-v) and drop the rest.
