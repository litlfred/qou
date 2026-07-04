# Borromean AJ stage 1 — R-matrix ground truth, BLOCKED on an inverse bug at color ≥ 3

> **✅ RESOLVED 2026-07-04 — see the superseding audit
> [`2026-07-04-borromean-aj-stage1-rmatrix-fixed.md`](2026-07-04-borromean-aj-stage1-rmatrix-fixed.md)
> (bean `1iqq`). The R-matrix is fixed and the tower is established (exactly
> diagonal). NOTE: this doc's diagnosis was itself incomplete — it claimed the
> *forward* action was always correct and only the inverse was wrong. In fact
> the forward nilpotent q-power `t^{2n(n-1)}` was ALSO wrong at color ≥ 3 (YBE
> failed on V₃⊗V₃⊗V₃); the inverse failure was a downstream symptom. Both were
> fixed (`t^{n(n-1)}` forward + exact matrix inverse). Kept for the diagnostic
> history; read the FIXED audit for the current state.**

**Date:** 2026-07-04
**Beans:** `moqg` (Borromean stage 1, blocked), `ds4b` (AJ-for-links
literature), `1iqq` (R-matrix fix — the unblock), `n920` (cyclotomic
cross-check vs Habiro [H1]).
**Split from** the trefoil-annihilation PR (#3279); this is the Borromean
follow-up. The trefoil + Masbaum cross-check work is finished there.
**Lineage:** the 4₁ / trefoil programs (PRs #3263, #3279) — those knots'
towers are Lean-proved and literature-anchored; this opens the Borromean
(𝓑₃) program.

## Status: BLOCKED (do not use the values)

The stage-1 build does **not** yield a usable ground truth yet. The
hand-rolled U_q(sl₂) R-matrix in
[`aj_borromean_colored_jones_tower.py`](../../computations/aj_borromean_colored_jones_tower.py)
has a **correct forward action** — inverse *and* Yang–Baxter both verify on
V₂⊗V₂ and V₂⊗V₃ — but its **inverse is wrong at color ≥ 3**: `R·R⁻¹ ≠ id`
on **V₃⊗V₃** (self-check in the script + witness field
`BLOCKER_V3xV3_inverse_ok=false`; 1 basis vector fails). The V₂⊗V₂
convention-pin caps the nilpotent sum at n = 1, so it never exercises the
n ≥ 2 terms where the naive termwise inverse
`(-1)^n q^{-n(n-1)/2}…E^n⊗F^n` breaks down — the E/F operators from the two
tensor factors interleave through the K-weights, and the universal-R inverse
is not simply the termwise sign/power flip once n ≥ 2.

Everything downstream is therefore unreliable and **must not be read as a
finding**: the bar-symmetry "failure" at J(2,3,3) (the first triple where
σ₂⁻¹ acts on two color-3 strands — all lower triples ARE bar-symmetric, as
the amphichiral link requires) and the diagonal-cyclotomic fit failure are
both artifacts of the R⁻¹ bug. Scoped per the "before declaring refuted"
discipline: this is a **(a) scope-limited** blocker on *my construction*, not
a structural claim about Borromean diagonality either way — the diagonal
Habiro form is neither confirmed nor refuted here.

## Unblock path (bean `1iqq`)

Replace `r_apply` with a verified R-matrix: build the full R on V_m⊗V_m' as
an explicit matrix and invert it **symbolically**, gated on `R·R⁻¹=id` AND
YBE at *every* color used (not just V₂⊗V₂); or route through a trusted
quantum-group library. Only the forward-action layer + the anchor/fit
scaffolding are reusable. The script is kept as the diagnostic of record.

## Original design (forward layer correct; keep as scaffolding)

Build the multi-colored Jones tower J_B(m₁,m₂,m₃) of the Borromean rings
(closure of the pure 3-braid `(σ₁σ₂⁻¹)³`) from the R-matrix, then
fit-then-verify the diagonal Habiro cyclotomic form
`J = Σ_k c_k ∏ᵢ σ_k(mᵢ)` in the **same σ_k basis as the Lean 4₁ ladder**
(`σ_k(m) = ∏_{j≤k}(Λ_m − λ_j)`, `QOU.BraidKnot.HabiroNewtonLadder`). Anchors:
unlink reductions `J(1,·,·)=1` (holds), bar symmetry (amphichirality),
q-integrality (the reduced 3-component-link value is a *rational function* of
q — denominators are quantum integers `[m]`; only the *knot* case gives a
Laurent polynomial — so the anchor tests numerator-integrality, not
Laurent-ness). Convention pinned by inverse + YBE — which is exactly where
the color-≥3 blocker was caught.

## Literature status (bean `ds4b`, bounded search)

Web search (arXiv full-text blocked in the sandbox; titles/abstracts
reachable): strong AJ is published for torus knots and cables
([Tran, AGT 13 (2013)](https://projecteuclid.org/journals/algebraic-and-geometric-topology/volume-13/issue-1/Proof-of-a-stronger-version-of-the-AJ-Conjecture-for/10.2140/agt.2013.13.609.full),
[cables](https://arxiv.org/pdf/1404.0331)) and for the figure-eight
([arXiv:2006.02042](https://arxiv.org/pdf/2006.02042) — the corpus's
`[nguyen-tran-2021]`); the AJ conjecture is known for two-bridge classes
([Lê–Tran](https://utd-ir.tdl.org/bitstreams/4cf5b871-ba07-44c7-8e7f-744947169315/download)).
**No published proof of an AJ statement for the Borromean rings (or a
multivariable link version) surfaced** — so the Borromean stages 2–3
(diagonal recurrence reconstruction + A-ideal specialization) target a
statement with no literature theorem to cite; any Lean class must carry it as
a §3b conjecture-grade input. (Scoped claim: bounded search from a firewalled
sandbox, not a corpus-grep-style exhaustive sweep.)

The Borromean colored-Jones *formula* (as opposed to the AJ *statement*) is in
Habiro [H1] (*simple links*, RIMS Kokyuroku 1172) — cited by Masbaum but not
on arXiv. **Provenance note:** Masbaum math/0306345 is a *twist-knot* paper
(K₁ = trefoil, K₋₁ = fig-8); it does **not** contain a Borromean formula (that
mis-attribution was corrected in #3279). The cyclotomic cross-check (bean
`n920`) is re-pointed at Habiro [H1], not Masbaum.
