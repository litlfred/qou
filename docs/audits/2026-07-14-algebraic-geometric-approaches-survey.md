# Algebraic-geometric approaches to the 1 ppQ walls — survey and ranking

**Date:** 2026-07-14 · **Branch:** `claude/canonical-derivation-c-k-n00n2h` ·
**Tier:** survey / context (no new compute; grounds the AG frontier for the two
open 1 ppQ derivations) · **Scope:** (a); nothing wired. Milestone bean `qou-hauo`.

Owner question: *what are the approaches on the algebraic-geometric side?* This
surveys the AG routes to the two isolated 1 ppQ walls — (W-α) the α_EM per-loop
measure `1/(π·b₁)` ([derivability map](2026-07-14-alpha-em-2loop-derivability-map.md))
and (W-q₀) the substrate `q₀` / `W_λ` keystone
([ledger](../coordination/s5-so3-keystone.md)) — and ranks them by tractability.
Both walls live on the **same object**: the Hodge/period structure of **Bring's
curve** `M₄` and its Jacobian.

## The shared AG substrate (established in corpus)

Bring's curve is the genus-4 curve of **maximal symmetry** `Aut = S₅` (order
120), the Bring–Jerrard quintic normal form. Corpus facts this survey builds on:

- **Hodge:** `H¹(M₄;ℂ) = H^{1,0} ⊕ H^{0,1}`, each `dim = g = 4`, so `b₁ = 2g = 8`
  (`cohomological-embedding.md`).
- **Symmetry tower:** `A₅ ≅ I ⊂ SO(3)`, double cover `2I ⊂ SU(2)`;
  `ℙ(V)/A₅ = S²(2,3,5)` = base of the Seifert fibration `S³/2I → S²(2,3,5)`
  (Poincaré sphere) (`klein-bring-icosahedral-bridge.md`).
- **Parity split (load-bearing for α_EM):** the **weak/colour** sector is the
  even `A₅` (the ζ₅ pentad + colour trefoil, parity-even); the **EM** sector is
  the **odd coset** `S₅∖A₅` — the involution `z ↦ 1/z` (parity-odd). *The photon
  lives in the odd coset.*
- **A colour-elliptic fibration exists** (`descartes-elliptic-curve.md`,
  `color-elliptic.md`) — a genuine elliptic curve inside the geometry.

## AG-1 + AG-4 first step DONE (this session, exact)

[`bring_s5_hodge_em_prym_probe.py`](../../computations/probes/bring_s5_hodge_em_prym_probe.py)
(+ witness, S₅ character table built from S₅ and verified orthonormal) settles
the cheap steps exactly:

- **AG-1:** `H^{1,0}(Bring) = (4,1)` standard rep ⇒ `b₁ = 2·dim V_{(4,1)} = 8`,
  so the loop measure `1/(π·b₁) = 1/(2π·dim V_{(4,1)})` is the reciprocal
  **categorical dimension** of the standard S₅ rep — the same rep the
  Hecke/Wedderburn machinery uses — **not** the area.
- **AG-4:** the EM involution `z↦1/z` is the odd-coset **transposition**;
  `χ_{(4,1)}(transp) = 2` ⇒ eigenvalues `(+1)³(−1)¹` on `V_{(4,1)}`, so the
  EM-anti-invariant **Prym has dim_C = 1: an elliptic curve**. The photon sees
  the odd-coset Prym (dim 1), not the whole surface — a *geometric* reason the
  loop measure differs from the zero-mode's full-surface `1/Area`, and a
  concrete tie to the corpus **color-elliptic curve**.

This turns AG-2 into the sharp next test: **is that EM Prym elliptic curve a CM
curve?** If yes, its period is a Chowla–Selberg `Γ`-value and the bare `π` in the
loop measure is exactly that period — the closed-form route opens.

## The five approaches, ranked

### AG-1 — S₅-equivariant Hodge decomposition (most illuminating; partial)

`H^{1,0}(M₄)` is a **4-dimensional irrep of `S₅`** (dim = g = 4; the standard
`(4,1)` or its sign-twist `(2,1,1,1)` — *to be pinned*). So

`b₁ = dim H¹ = 2·dim(4-dim S₅ irrep)`,

and the α_EM loop measure is `1/(π·b₁) = 1/(2π·dim V₄)`. This is a real,
unfitted structural identity: the loop normalization is governed by the
**same S₅ representation** whose Wedderburn blocks the framework already uses
throughout the Hecke/Markov machinery. It reframes "why `b₁` in the loop
measure" as "why `2·dim(standard rep)`" — a categorical-dimension statement,
not an area. **What it buys:** the photon determinant is `S₅`-equivariant, so
it factors through the isotypic decomposition; on the odd-coset (EM) piece the
normalization is the reciprocal categorical dimension. **What it does not do:**
supply the bare `π` (that is an archimedean period, → AG-2/AG-5) or the global
sign. Verdict: **the cleanest conceptual bridge; makes the wall a
representation-dimension statement, but not yet the full number.** First step:
pin the exact irrep (`(4,1)` vs `(2,1,1,1)`) of `H^{1,0}` and check whether the
EM odd-coset acts on it by the sign character (which would tie the loop sign to
the parity split).

### AG-2 — Periods / CM / Chowla–Selberg (the exact-closed-form route; hard)

`J(M₄)` is a highly special abelian 4-fold with `S₅`-action; the corpus's
colour-elliptic curve suggests `J(M₄)` may be **isogenous to a power of a CM
elliptic curve** (or carry CM). If so, its periods are **exact** via the
**Chowla–Selberg formula** (values of `Γ` at rational arguments) — and the bare
`π` in `1/(π·b₁)` would emerge as a **period integral**, giving a closed form
rather than a numerical `π`. This is the only route that could turn the loop
measure into an *exact* algebraic-times-period expression. Verdict: **highest
payoff, highest difficulty.** Concrete first step: determine the isogeny type of
`J(Bring)` (is it `E⁴`? `E²×A₂`? simple with CM?) — a finite computation
(class-group / endomorphism-algebra of the S₅-decomposition), decisive for
whether Chowla–Selberg applies.

### AG-3 — S³/2I WRT localization, unified with the keystone (best leverage; active)

The `W_λ` keystone's live frontier (#2524) is **Beasley–Witten non-abelian
Chern–Simons localization on `S³/2I`** (Reeb = Seifert `S¹`), giving
`W_λ = d_q²/D²` as an `S¹`-equivariant index. **The α_EM loop measure and the
keystone `W_λ` plausibly share this single source:** the photon 1-loop
determinant on the same Seifert geometry is normalized by the same localization
measure. If true, **one S³/2I localization computation certifies both walls at
once** — the biggest structural economy available. Verdict: **best
leverage-per-effort *because the machinery is already being built*** for the
keystone; the new content is only checking whether the abelian (photon) sector's
1-loop normalization falls out of the same non-abelian localization. Coordinate
with the s5-so3 keystone thread (do not duplicate).

### AG-4 — EM odd-coset Prym variety (structurally targeted; medium)

Because EM = the odd coset (the `z↦1/z` involution `ι`), the photon sector is
the **anti-invariant part** of `H¹` under `ι`. The double cover associated to
`ι` has a **Prym variety** `P = (1−ι)J(M₄)` that isolates exactly the
EM-relevant sub-Jacobian. The loop measure would then be a period/volume of `P`,
not of the full `J` — which could explain why the loop factor differs from the
zero-mode's full-surface `1/Area`. Verdict: **the most physically-targeted AG
route** (it uses the EM/parity split directly), medium difficulty. First step:
compute `dim P` (the anti-invariant `H¹`-dimension under `ι`) and check it
against the `b₁`-in-the-denominator structure — if `dim P` relates to the loop
`b₁` while `Area` is the whole surface, the numerator/denominator split of the
two IR measures becomes geometric, not coincidental.

### AG-5 — Higher regulators (explains the π-powers; exploratory)

The **zero-mode** `2/(3π)` is a **dilogarithm/Bloch regulator** value (the
framework's `conj:dilogarithm-archimedean-limit`, Suslin pentagon). The loop
measures carry successively higher `π`-powers (`1/π` per loop). This is the
signature of a **regulator tower**: Bloch–Wigner (`π¹`, zero-mode) → Beilinson
/ higher Chow / height pairing (`π²`, one loop) → …. If the per-loop `1/π`
is the **Beilinson regulator on the next motivic weight** of `M₄`, the whole
ladder is a regulator hierarchy and the `π`-powers are *derived*, not inserted.
Verdict: **the most speculative but the only one that explains the `π`-power
pattern across all loop orders in one stroke**; connects to L-values. First
step: check whether `1/(π·b₁)` equals a known second-regulator value (e.g. the
Beilinson regulator of `K₃(M₄)` or the height on `J(M₄)`) numerically to the
~10⁻⁴ the 1-loop term fixes it to.

## Ranking summary

| approach | payoff | difficulty | status | first concrete step |
|---|---|---|---|---|
| **AG-3** S³/2I localization (unify w/ keystone) | high (2 walls, 1 compute) | med (machinery active) | **best leverage** | check photon abelian 1-loop norm in the #2524 localization |
| **AG-1** S₅-equivariant Hodge | med (concept bridge) | low | **start here** | pin `(4,1)` vs `(2,1,1,1)` of `H^{1,0}`; EM-coset sign action |
| **AG-4** EM odd-coset Prym | med (targeted) | med | promising | compute `dim` anti-invariant `H¹` under `ι` |
| **AG-2** periods / CM / Chowla–Selberg | **highest** (exact form) | high | decisive test | isogeny type of `J(Bring)` |
| **AG-5** higher regulators | high (π-tower) | high (speculative) | exploratory | match `1/(πb₁)` to a 2nd-regulator value |

## Recommended sequence

1. **AG-1 first** (cheap, ~1 session): pin the `S₅`-irrep of `H^{1,0}` and the
   odd-coset action — turns the α_EM wall into a representation-dimension +
   sign-character statement, and either connects the loop sign to the EM parity
   split or refutes that connection.
2. **AG-2 isogeny test** (cheap-ish, decisive): determine whether `J(Bring)` is
   CM / `E⁴`-isogenous — this gates the entire exact-closed-form route.
3. **AG-3 coordination** (leverage): with the keystone thread, test whether the
   abelian photon 1-loop normalization drops out of the S³/2I localization the
   keystone is already computing.

Only after 1–3 does the choice between the Prym (AG-4) and regulator (AG-5)
deep routes become well-posed. None is a fit; all are derivations-or-refutations
on the same Bring-Jacobian object that already underlies the whole framework.

## Cross-references

- α_EM wall: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md), θ-graph [`…-theta-graph-two-loop-candidate.md`](2026-07-14-alpha-em-theta-graph-two-loop-candidate.md)
- q₀/W_λ keystone: [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- AG substrate blocks: `brings-surface/cohomological-embedding.md`, `klein-bring-icosahedral-bridge.md`, `descartes-elliptic-curve.md`
