# OV base seminormal vector — column-superstandard polytabloid (numerical verification)

**Context.** `seminormalVector_base_exists`
([`JucysMurphy.lean:850`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/JucysMurphy.lean))
is the single remaining `sorry` in the Okounkov–Vershik seminormal cone: for one
standard tableau `T₀` of shape `μ`, exhibit a nonzero simultaneous Jucys–Murphy
eigenvector `v ∈ S^μ` whose `X_s`-eigenvalue is the content of the cell holding
label `s` in `T₀`. Everything downstream (swap-transport `seminormalVector_data_step`,
all-`T` connectivity, spanning, `dim S^μ = #SYT`) is already proved sorry-free; only
this base vector is open.

## Finding (formalize-first check, before writing any Lean)

The classical candidate for `v` is a **polytabloid** `e_{T₀}`. A plain polytabloid is
**not** a JM eigenvector in general (the seminormal basis vectors are specific
combinations of polytabloids). So *which* `T₀` — if any — has `e_{T₀}` itself an
eigenvector had to be checked before committing to a formalization target.

Direct computation over `M^μ` (free ℚ-module on tabloids, `S_n` acting by permuting
labels; `X_s = Σ_{i<s}(i\,s)`; `e_{T₀} = Σ_{π∈colStab(T₀)} sgn(π)·[πT₀]`), script
[`computations/ov_base_polytabloid_eigen_check.py`](../../computations/ov_base_polytabloid_eigen_check.py):

| shape `μ` | row-superstandard `e_{T₀}` | **column-superstandard** `e_{T₀}` |
|-----------|----------------------------|-----------------------------------|
| `[2,1]`   | ✗ not an eigenvector       | ✓ `X_s·e = c_s·e` for all `s`     |
| `[2,2]`   | ✗                          | ✓                                 |
| `[3,1]`   | ✗                          | ✓                                 |
| `[3,1,1]` | ✗                          | ✓                                 |

For the **column-superstandard** tableau (fill `0,1,2,…` down successive columns),
`e_{T₀}` is a simultaneous `X_s`-eigenvector and the eigenvalue is exactly
`content(cell of label s)` — verified for every `s` on all four shapes. The
column-superstandard tableau is itself standard (rows/columns strictly increasing —
checked for `[2,1],[2,2],[3,1],[3,1,1],[3,2,1],[4,1,1,1]`).

**The row-superstandard tableau (`SytRowSuperstandard.rowSuperstandardStd`) does NOT
work** — its polytabloid is not a JM eigenvector. This matters: the natural
"base tableau already in the repo" is the *row*-superstandard one, and building
`base_exists` toward it would be **proving a false statement**. The correct target
is the **column-superstandard** polytabloid (as the `base_exists` docstring already
states — now numerically confirmed).

## Consequence for the formalization

`base_exists` reduces to the single computation

  `(Mtab.rep μ).asAlgebraHom (jucysMurphy (nOf μ) s) (polytabloid T₀) = cellContent(cell_s) • polytabloid T₀`,

with `T₀ =` column-superstandard, plus the two cheap conjuncts `polytabloid T₀ ∈ S^μ`
(`polytabloid_mem_specht`) and `polytabloid T₀ ≠ 0` (standard-basis independence,
`T₀` standard). The eigen-equation is a self-contained polytabloid computation that
does **not** need the OV/Gelfand–Zetlin edifice or the famous Specht walls
(`specht_isSimple`, `specht_form_nondegenerate`, …). It remains a substantial Lean
proof (transposition action on tabloids modulo column antisymmetrization), but it is
now **de-risked and correctly targeted**.

**Bean:** `qou-kskn` (milestone) / `qou-mhx0` (base-vector machinery).

## Update — brick 3b fully mapped (the off-column Garnir collapse)

After bricks 1–3a + the column-split (`jm_polytabloid_split`, merged #4048/#4055),
the eigen-equation reduces to the **off-column sum**
`Σ_{j<s, cross-column} e_{(j s)·T₀} = col(s)·e_{T₀}`. This decomposes by column:

**Single-column relation.** For each earlier column `c < c_s`,
`Σ_{j ∈ column c} e_{(j s)·T₀} = e_{T₀}`. Summing over the `c_s` earlier columns
gives `col(s)·e_{T₀}`. **Verified numerically** for `[2,1]/[3,1,1]/[2,2]/[3,2,1]`,
including non-adjacent columns (script `ov_base_polytabloid_eig_check.py`).

**Proof mechanism (fully specified).** The single-column relation is the Garnir
annihilation `Σ_{g ∈ transversal(S_C, S_{C∪{s}})} sgn(g)·rep(g)·e_{T₀} = 0`, where
`C =` the column-`c` labels and the transversal is `{id} ∪ {(j\,s) : j ∈ C}`
(`sgn(id)=+1`, `sgn(j s)=−1`), which rearranges to `Σ_{j∈C} rep(j s) e = e`. The
lever is the **already-proved** `SpechtStandardBasisCore.sum_sign_rep_polytabloid_eq_zero_of_family`:
it reduces the polytabloid annihilation to a tabloid-level vanishing for every
`ρ ∈ colStab t`, discharged by a **row collision**. The collision is *guaranteed*
here: in `ρ·T₀`, `s` sits in column `c_s` at some row `< colLen(c_s) ≤ colLen(c) = |C|`
(columns weakly decrease and `c < c_s`), so `s` shares a row with the column-`c`
label at that row — the antisymmetrizer kills the tabloid.

**Remaining Lean work (brick 3b):** define the transversal `G`, apply
`sum_sign_rep_polytabloid_eq_zero_of_family` with `G`, prove the row-collision
`hfam` (mirroring `garnir_full_annihilation`'s proof but for this single-column
transversal and the `s`-row `< colLen(c)` collision), and rearrange to the
single-column relation; then sum over `c < c_s` and combine with the same-column
count `= row(s)` (brick 3a) to close `base_exists`.

## Correction (2026-07-19, second pass) — brick 3b is a multi-session build, not trivial assembly

The "fully de-risked — every ingredient a proved upstream lemma" wording above
was **over-optimistic** (the mirror of the "open" over-claim: do not over-claim
"de-risked" either). On reading the Garnir machinery in
[`SpechtStandardBasisCore`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtStandardBasisCore.lean):

1. **`garnirG t i j = S_{A∪B}` is the FULL symmetric group on `A∪B`**, and `garnirA/garnirB`
   are **hard-coded to adjacent columns** `j, j+1` at a fixed row `i`
   (`garnirA = col j, rows ≥ i`; `garnirB = col j+1, rows ≤ i`). The existing
   `garnir_full_annihilation` / `garnir_row_collision` therefore do **not** transfer to
   the single later-column cell `s` vs an entire earlier column `C` — that needs a
   **new** collision lemma (the `s`-row `< colLen(c) = |C|` argument is clean and
   direct — the `C`-labels fill rows `0…|C|−1`, `s` lands at a row `< colLen(c_s) ≤ |C|`
   — but it is not the adjacent-column pigeonhole `garnir_row_collision` proves).

2. **The single-column relation is the COSET-transversal sum, not the full-group sum.**
   The transversal `{id} ∪ {(j s) : j ∈ C}` is **not** closed under right-multiplication
   by the collision swap, so `mtab_sum_sign_smul_of_eq_zero` does not apply to it directly.
   The honest route is: prove the **full-group** annihilation `∑_{σ ∈ S_{C∪{s}}} sgn σ · σ·e_t = 0`
   (new collision, full group trivially swap-closed), then **decompose `S_{C∪{s}}` into the
   `|C|+1` left cosets of `S_C`** with reps `{(x s) : x ∈ C∪{s}}`, use column antisymmetry
   `∑_{π∈S_C} sgn π · π·e_t = |C|!·e_t` (now landed — `colStab_subset_sum_rep_polytabloid`
   + `rep_colStab_polytabloid`) on each coset's inner sum, and cancel `|C|! ≠ 0` (char 0)
   to reach `∑_{j∈C} e_{(j s)·t} = e_t`.

**Landed this pass (all sorry-free, `lean`-direct exit 0, in
[`OVBaseSeminormalVector.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/OVBaseSeminormalVector.lean)):**

- `colStab_subset_sum_rep_polytabloid` — the coset-inner-sum collapse
  `∑_{σ∈H} sgn σ · σ·e_t = |H|·e_t` for any `H ⊆ colStab t` (collision-independent).
- `starSum_rep_polytabloid` — the outer star-sum
  `∑_{x∈{s}∪C} sgn(x\,s)·(x\,s)·e_t = e_t − ∑_{j∈C} e_{(j\,s)·t}`.
- `permFixingOutside D` (= `S_D` as a `Finset`) + `mem_permFixingOutside`.
- **`colGarnir_fullgroup_sum`** — the coset-reindexing core (item (ii) below, done):
  `∑_{σ∈S_{C∪{s}}} sgn σ · σ·e_t = |S_C|·(e_t − ∑_{j∈C} e_{(j\,s)·t})`, via
  `Finset.sum_nbij'` (bijection `(x,π) ↦ (x\,s)·π`) + `Finset.sum_product'` + the two
  bricks above. Collision-independent, over generic `[CommRing k]`.
- **`colGarnir_single_column_of_annihilation`** `[Field k] [CharZero k]` — the
  conditional closer: **given** the annihilation `= 0`, divide by `|S_C| = |C|! ≠ 0`
  to get the single-column relation `∑_{j∈C} e_{(j\,s)·t} = e_t`.

**Net effect:** items (ii) [coset decomposition + `|C|!` cancellation] are **done**.
The single-column relation now reduces to the **single** remaining debt:

**Still open (the collision-dependent remainder):** (i) the full-group **annihilation**
`∑_{σ∈S_{C∪{s}}} sgn σ · σ·e_t = 0` — via `sum_sign_rep_polytabloid_eq_zero_of_family`
+ `mtab_sum_sign_smul_of_eq_zero`, needing a **new** row-collision for `(C,{s})`;
(iii) the column-superstandard geometry (`colLen` weakly decreasing ⇒ `s`-row `< |C|`)
that supplies the collision; (iv) summing the single-column relations over `c < c_s`
+ brick 3a to the eigen-equation; (v) the two side conjuncts (`polytabloid_mem_specht`,
`≠ 0`) and discharging `seminormalVector_base_exists`. The collision (i)+(iii) is the
substantive next chunk; (iv)+(v) are assembly.
