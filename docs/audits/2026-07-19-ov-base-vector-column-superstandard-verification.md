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
