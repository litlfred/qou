# Borromean AJ stage 1 + trefoil annihilation assembly (PR #3279)

**Date:** 2026-07-04
**Beans:** `moqg` (Borromean tower), `ds4b` (literature), `6q9g` + `rz8b`
(trefoil), follow-up `6zub`.
**Lineage:** the 4₁ program (PR #3263: division-free certificate telescope,
`StrongAJFigureEight` sorry-free) — this tranche extends the machinery to
the second corpus knot (trefoil) and opens the Borromean (𝓑₃) program.

## Trefoil: annihilation assembled, sorry narrowed to two evaluation cores

[`AJTrefoilAnnihilation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/AJTrefoilAnnihilation.lean)
(lean-direct, exactly 2 cited-sorry warnings). No qZeilberger certificate
is needed at order 1: the Rosso–Jones tower extends by one term per color,
so with `P(n) = Σ_{j≤n} (−1)^j w^{6j(j+1)} [2j+1]_{w²}` the annihilation
reduces to two rational identities in `(w, Y = (w²)^N)` — [C1] coefficient
cancellation and [C2] boundary — pre-verified exactly in
[`aj_trefoil_telescope_assembly_check.py`](../../computations/aj_trefoil_telescope_assembly_check.py)
and proved in the generic case.

**The finding worth reading first:** `coloredJonesTrefoil` divides by
`qInt (w²) N`, which vanishes exactly at `x = (w⁴)^N = 1`, where the Lean
value is the division-by-zero junk `0`, not the analytic value. The merged
class field quantifies over ALL `w ≠ 0` — and it remains *true* there only
because of a three-way conspiracy: the operator's own coefficients vanish
at the junk slots (`a₀ ∝ (x−1)`, `a₁ ∝ (xq−1)`), and the surviving term
then requires the **root-of-unity evaluation** `J = 1` at the neighboring
color (RJ-sum periodicity; verified numerically to 40 dps for both slots).
The case split (`w⁴ = 1` collapse / generic / two degenerate slots) is
fully proved; the two evaluation lemmas
(`trefoil_eval_at_root_prev`/`_next`) are the remaining cited cores —
strictly smaller than the superseded broad general-`N` sorry (removed
from `AJTrefoil.lean`; instance moved, per the 4₁ restructure pattern).
The induction through the singular slot breaks (`[N]_v = 0` kills the
generic step at exactly the color the chain needs), so the cores need a
genuine sum evaluation — queued as bean `6zub`.

Contrast with 4₁: there the division-free telescope avoided ALL
denominators (divisions only by powers and the clearing product), so the
proof needed no case split and no root-of-unity lemmas. The trefoil's
tower *definition* carries the `1/[N]_v` normalization, so the degeneracy
is intrinsic to the statement, not the proof method.

## Borromean stage 1: R-matrix ground truth, fit-then-verify cyclotomics

arXiv is proxy-403 in this sandbox (Masbaum, *Skein-theoretical derivation
of some formulas of Habiro*, math/0306345, unreachable; OpenAlex empty
through the same proxy), so the epistemics are flipped: rather than
transcribing a half-remembered literature formula,
[`aj_borromean_colored_jones_tower.py`](../../computations/aj_borromean_colored_jones_tower.py)
builds ground truth **directly from the U_q(sl₂) R-matrix** —

- exact symbolic (variable `t`, `q = t⁴`), colors independent per strand
  (the Borromean braid `(σ₁σ₂⁻¹)³` is pure);
- conventions PINNED by machine checks, not chosen: `Ř·Ř⁻¹ = 1` and the
  Yang–Baxter equation (the first run's inverse check caught a real
  structure bug — `(τ∘R)⁻¹ = R⁻¹∘τ ≠ τ∘R⁻¹`, and the diagonal/nilpotent
  order of `R = D·N` swaps under inversion);
- the remaining convention risk collapses structurally: writhe 0 (framing
  factors cancel) and amphichirality (mirror-blind);
- anchors asserted: unlink reductions `J(1,·,·) = 1`, bar symmetry,
  Laurent-in-q integrality;
- then the diagonal Habiro cyclotomic form `J = Σ_k c_k ∏ᵢ σ_k(mᵢ)` — in
  the SAME basis `σ_k(m) = ∏_{j≤k}(Λ_m − λ_j)` as the Lean 4₁ ladder — is
  FIT on the diagonal and VERIFIED exactly on every mixed-color triple
  (mᵢ ≤ 4): Habiro's diagonality established by over-determined
  verification on the computed range, with the `c_k` closed form
  identified against candidates.

Results (run `aj-borromean-colored-jones-tower.witness.json`): see the
witness for the pinned convention, the exact `J(m₁,m₂,m₃)` values, the
cyclotomic `c_k`, and the identified closed form.

## Literature status (bean ds4b, bounded search)

Web search (arXiv full-text blocked; titles/abstracts reachable): strong
AJ is published for torus knots and cables
([Tran, AGT 13 (2013)](https://projecteuclid.org/journals/algebraic-and-geometric-topology/volume-13/issue-1/Proof-of-a-stronger-version-of-the-AJ-Conjecture-for/10.2140/agt.2013.13.609.full),
[cables](https://arxiv.org/pdf/1404.0331)) and for the figure-eight
([arXiv:2006.02042](https://arxiv.org/pdf/2006.02042) — the corpus's
`[nguyen-tran-2021]`); the AJ conjecture is known for two-bridge classes
([Lê–Tran](https://utd-ir.tdl.org/bitstreams/4cf5b871-ba07-44c7-8e7f-744947169315/download),
[diagrammatic approach](https://arxiv.org/abs/1903.01732)). **No published
proof of an AJ statement for the Borromean rings (or a multivariable
link version) surfaced in this search** — so the Borromean stages 2–3
(diagonal recurrence reconstruction + A-ideal specialization) target a
statement with no literature theorem to cite; any Lean class must carry
it as a §3b conjecture-grade input, not a cited theorem, and corpus-side
verification will be evidence-level. (Scoped claim: bounded search from a
firewalled sandbox, not a corpus-grep-style exhaustive sweep.)

## Status

- Trefoil: assembled; `6zub` queued (the two evaluation cores).
- Borromean: stage 1 running; stage 2 (diagonal recurrence via mod-p
  window reconstruction, as for 4₁/trefoil) is the next tranche.
