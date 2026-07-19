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
count `= row(s)` (brick 3a) to close `base_exists`. Substantial but fully
de-risked — every ingredient is a proved upstream lemma or a specified collision.
