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
colour quotient is not a valid production approximation.**

### Gap FILLED — the full-Hecke choice is principled, not arbitrary

The `y_λ` are the **Wenzl principal Schur specialization** `s_λ(1, q, q², …)`
(`wedderburn_jones_markov.py:7,63` → `schur_principal_symbolic`) — the **canonical
Jones–Markov trace** on the Hecke tower `H_n(q)` (the unique Markov trace, Wenzl
1988). The *principal* (infinite-variable) specialization is **nonzero for every λ
by construction** — there is no row cutoff. The SU_q(3) "colour" trace would be the
**finite 3-variable** specialization `s_λ(1, q, q²)`, which *is* zero for >3-row λ —
but that is a **structurally different trace functional**, not a truncation or
approximation of the canonical one. So the question "why full Hecke not SU_q(3)" is
resolved: QOU uses *the* canonical Markov trace; restricting to ≤3 rows would change
the functional (a different physical theory), not optimize this one. The `p(3A)`
wall is therefore intrinsic to the canonical Jones–Markov trace itself.

## C. Verdict on "unexplored symmetries"

The S5/S3/S3↪S5/Bring/Galois structure — though it *is* the substrate's defining
symmetry and the generation-grading mechanism — does **not** reduce the `p(3A)` wall.
It is a block-level functor, not a spectrum truncation, and the one quotient that
*would* be polynomial (SU_q(3), ≤3 rows) is empirically invalid (≥3 % at ⁴He). The
[bond-dimension verdict](2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md)
stands: exact `tr_M` is intrinsically `O(p(3A))`; heavy nuclei use the A→∞ q-CLT
extrapolation.

## D. The binding lead — tested and REFUTED

The >3-row missing fraction grows with A (0.2 → 1.1 → 3.4 %), percent-scale like
nuclear binding, suggesting the >3-row sectors might *be* the cooperative many-body
binding (≤3-row = free-nucleon mass, >3-row = binding). **Tested directly and
refuted:** row-decomposing the **free** nucleon reference (atom braid with
`include_inter=False`, i.e. no inter-nucleon coupling = no binding) shows the free
product carries **as much or more** >3-row content than the bound atom:

| atom | atom >3-row frac | free >3-row frac |
|---|---|---|
| D | 0.216 % | 0.081 % |
| ³He | 1.15 % | 1.82 % |
| ⁴He | 3.36 % | **7.47 %** |

The free reference (zero binding) already populates >3-row sectors — more than the
bound atom at ⁴He. So the >3-row content is **not** a binding signature; it is
intrinsic to the per-nucleon braid representation (each H₃ block fused into H_{3A}
generates >3-row partitions regardless of inter-nucleon coupling). The "binding
lives in >colour sectors" hypothesis is **false**. (This also independently
re-confirms §B: even a free nucleon needs the full-row trace — SU_q(3) restriction
fails for the free mass too, consistent with the canonical-Markov-trace resolution.)

## Files reviewed

- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md),
  [`docs/audits/2026-06-16-s5so3-branching-backbone-verified.md`](2026-06-16-s5so3-branching-backbone-verified.md),
  [`docs/audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md),
  [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md),
  `content/quantum-observable-universe/brings-surface/fivefold-symmetry.md`,
  `content/quantum-observable-universe/mass-endomorphism/color-spacetime-s5-factorization.md`.
- Compute: `computations/atom_bond_dimension_measure.py` (extended with the row-tail
  measurement).
