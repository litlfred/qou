# S5/S3/S3↪S5 corpus review + the full-Hecke vs SU_q(3) question — resolved (2026-06-16)

**Branch:** `claude/atom-braid-bond-dimension-program-2026-06-16` (PR #2389)
**Follows:** the [bond-dimension verdict](2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md)
(χ_eff = p(3A), wall intrinsic). Owner asked: are there unexplored symmetries —
specifically **S5, S3, S3↪S5, Bring, Galois** — and is the full-Hecke vs SU_q(3)
trace choice justified? Both resolved here.

## A. The S5/S3 structure is central — but it is a *block functor*, not a sector truncation

Corpus review (paths below) — the symmetric-group structure is foundational to QOU:

- **S5 = Aut(Bring quintic surface) Σ₄**; `A5 ⊂ S5 ≅ icosahedral I ⊂ SO(3)` — the
  Klein icosahedral solution of the quintic (the **Galois** group of the generic
  quintic is S5; its solvability obstruction `A5` is the icosahedral symmetry). S5
  permutes the 5 Bring coordinates and **factors as S2 × S3** = spacetime × colour
  ([`brings-surface/fivefold-symmetry.md`](../../content/quantum-observable-universe/brings-surface/fivefold-symmetry.md),
  [`mass-endomorphism/color-spacetime-s5-factorization.md`](../../content/quantum-observable-universe/mass-endomorphism/color-spacetime-s5-factorization.md)).
- **S3 = colour** (the 3 colour coordinates) **= per-nucleon 3-strand braid** (H₃)
  **= Borromean 3-link** (S3-trivial subspace selects one octahedral cell).
- **S3↪S5 = the verified restriction functor `Res^{S5}_{S3}`** (123→345, fixing the
  spacetime frame): `(3,2)↓ = (3)⊕2(2,1)`, `(3,1,1)↓ = (1,1,1)⊕2(2,1)⊕(3)`,
  difference = sign rep. Generation `ℓ` is routed to an S5 block via `SO(3)↓A5`
  (V₁→T₁→(3,1,1) electron; V₂→H→(3,2) muon; V₃→T₂⊕G tau)
  ([`docs/audits/2026-06-16-s5so3-branching-backbone-verified.md`](2026-06-16-s5so3-branching-backbone-verified.md)).

**Decisive point for the wall:** `Res^{S5}_{S3}` maps **blocks → blocks** and grades
**generations**; it **re-weights amplitudes within all Wedderburn sectors**, it does
**not** select a small subset of partitions. There is **no corpus mechanism** by
which S5/S3/icosahedral structure truncates the `p(3A)` sector sum. The Wedderburn-
projector "shift" between generations (the open s5-so3 keystone) is an amplitude
re-weighting on all sectors, not a restriction.

## B. Full-Hecke vs SU_q(3) — the colour quotient is empirically invalid

The natural SU_q(3) "colour" trace would keep only **≤3-row** partitions
(polynomial in A: ¹⁶O ~192 sectors vs p(48)=147 273). Does it approximate the full
trace? **No** — measured contribution of the truncated (>row) tail to `tr_M`:

| atom | ≤2 rows missing | ≤3 rows (SU_q(3)) missing | ≤4 rows missing |
|---|---|---|---|
| D (n=6) | 5.42 % | **0.216 %** | 0.057 % |
| ³He (n=9) | 2.99 % | **1.15 %** | 0.129 % |
| ⁴He (n=12) | 7.34 % | **3.36 %** | 0.250 % |

The ≤3-row restriction misses by **0.2 → 1.1 → 3.4 %, growing with A** — orders of
magnitude above the 50-dps / 1-ppQ floor, and worse than the rejected active-set
10⁻³ truncation. **So QOU genuinely requires the full Hecke trace; the SU_q(3)
colour quotient is not a valid production approximation.** Combined with the corpus
(no derivation exists), the status is: the full-Hecke choice is *empirically forced*
but *not yet derived* — a documented gap, not a free optimization.

## C. Verdict on "unexplored symmetries"

The S5/S3/S3↪S5/Bring/Galois structure — though it *is* the substrate's defining
symmetry and the generation-grading mechanism — does **not** reduce the `p(3A)` wall.
It is a block-level functor, not a spectrum truncation, and the one quotient that
*would* be polynomial (SU_q(3), ≤3 rows) is empirically invalid (≥3 % at ⁴He). The
[bond-dimension verdict](2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md)
stands: exact `tr_M` is intrinsically `O(p(3A))`; heavy nuclei use the A→∞ q-CLT
extrapolation.

## D. The lead worth keeping (NOT a sector reduction — a physics observation)

The >3-row missing fraction **grows monotonically with A** (0.2 → 1.1 → 3.4 %) and is
percent-scale — the same order as **nuclear binding** (B/M ~ 0.1–1 %). This suggests
the **≤3-row (colour) sectors carry the free-nucleon-sum mass, and the >3-row
sectors carry the cooperative many-body content** (binding) — consistent with the
#2343/#2349 finding that B_sym is pairwise-chain-exact and the cooperative α-binding
lives *outside* the leading structure. This is a **derive-or-refute research lead**
on where binding lives in the Wedderburn decomposition, **not** a computational
shortcut (the >3-row sectors are needed, not prunable). Flagging for the binding
program; out of scope for the (now-closed) bond-dimension wall question.

## Files reviewed

- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md),
  [`docs/audits/2026-06-16-s5so3-branching-backbone-verified.md`](2026-06-16-s5so3-branching-backbone-verified.md),
  [`docs/audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md),
  [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md),
  `content/quantum-observable-universe/brings-surface/fivefold-symmetry.md`,
  `content/quantum-observable-universe/mass-endomorphism/color-spacetime-s5-factorization.md`.
- Compute: `computations/atom_bond_dimension_measure.py` (extended with the row-tail
  measurement).
