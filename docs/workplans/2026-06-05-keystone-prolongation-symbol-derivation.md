# Deriving the keystone — `R` = the jet-prolongation symbol

**Goal:** discharge the single remaining open input of the step-9b binding
closure ([`conj:qdifference-kernel-prolongation-symbol`], merged #1871) — derive
the q-difference kernel `R` of the binding generating function as the **symbol of
the jet-prolongation operator** of the Seiberg–Witten connection, *structurally*
(not by fitting term data — forbidden by the #1839 precision floor).

**Status:** derivation setup + falsifiable consistency test; gated on the
per-knot residue weights `a_D⁽ⁿ⁾` at `n = 2, 3` (owned by #1765).

---

## 0. Result (2026-06-05): the EXISTENCE half is now PROVED

`prop:prolonged-periods-fixed-depth` (Lean `prolongation_fixed_depth_recurrence`,
sorry-free): the prolonged periods are orbits of the prolongation operator `M`
on the finite-rank Gauss–Manin space, so by Cayley–Hamilton they satisfy a
**fixed-depth recurrence with `n`-independent kernel**, depth `≤ rank V ≤ 2g = 8`.
So the keystone splits cleanly: **existence proved**; only **identification**
(that the kernel is the Bring Picard–Fuchs operator) remains — the content of
§2–§5 below.

## 1. What is already proved (merged on main)

- (D) `a_D⁽ⁿ⁾ = Σ_p Res_p λ_SW⁽ⁿ⁾` — residue form (`prop:sw-period-residue-sum`).
- (C) body order `n` = jet vertical degree `n` (`lem:bond-order-eq-jet-degree`).
- (L3) if `G(qx)=R(q,x)G(x)` (depth `d`) then `B_{n+d}=Σ_{j<d} a_j B_{n+j}`
  (`prop:binding-genfun-qdifference`).
- conditional closure (`thm:binding-closure-conditional`): given the per-term
  identity (B), `B(K)=mₑ·Σ_n a_D⁽ⁿ⁾`.

So the binding closes the moment `R` is fixed. `R` fixed ⇒ the recurrence
determines every `a_D⁽ⁿ⁾` from the deuteron base ⇒ (B) ⇒ unconditional.

## 2. The structural claim to derive

The prolongation `J^n E → J^{n+1} E` of the abelianised SW connection
(`prop:mi-sw-abelianisation`) is a **single fibre-level operator**; its symbol,
read off the connection 1-form's Laurent expansion at the branch-point poles on
`S_c ≅ P¹`, is `R`. Concretely the successive prolonged periods are related by
the covariant derivative,

```
a_D⁽ⁿ⁺¹⁾ = (prolongation) · a_D⁽ⁿ⁾,
```

so the kernel coefficients `{a_j}` of `R` are the same at every `n` — a **fixed
depth-`d` recurrence**, not an `n`-dependent fit. This is the falsifiable
content.

## 3. The falsifiable consistency test (this branch)

Given the residue-weight sequence `a_D⁽ⁿ⁾`, `n = 2, 3, 4, …`, ask:

> Does a **single** depth-`d` linear recurrence `a_D⁽ⁿ⁺ᵈ⁾ = Σ_{j<d} c_j a_D⁽ⁿ⁺ʲ⁾`
> with **`n`-independent** `c_j` reproduce the sequence?

- **Yes** (small `d`, stable `c_j`) ⇒ evidence the prolongation symbol exists;
  the `c_j` ARE `R`'s kernel — check against the connection's local data.
- **No** (`c_j` drift with `n`, or `d` grows) ⇒ the prolongation-symbol
  conjecture is **refuted** for the binding `G`.

This is a *structural existence test*, not a parameter fit: a fixed-depth
recurrence either holds or it does not. `sw_prolongation_symbol.py` implements
it by solving the depth-`d` Hankel linear system (`mp.lu_solve`, scanning start
windows for a non-singular block) and **verifying the candidate kernel on every
out-of-sample window** at `q₀` — with the depth capped at `(N−1)//2` so a
verification window always exists (a pure fit can never pass).

## 4. The gating input — coordinate with #1765

The test needs `a_D⁽ⁿ⁾` at `n = 2, 3` (only `n = 4` = Family-A is wired here,
via `sw_period_residue.py`). These are exactly #1765's per-knot
`λ(L) = (1/(c+1)) Σ_{λ⊢c+1} dim_q(λ)` at `c = 1, 2` and its A-polynomial saddle
for ³He/⁴He. **Do not reimplement #1765's rule** (corpus-grep / no-duplicate
discipline) — consume its outputs. Coordination posted on #1765.

### 4a. How to run `sw_prolongation_symbol.py`

```bash
cd computations/substrate && python3 -u sw_prolongation_symbol.py
```

- **Input:** a sequence `seq = [a_D⁽²⁾, a_D⁽³⁾, a_D⁽⁴⁾, …]` of residue weights
  (mpmath `mpf` at `q₀`), passed to `minimal_recurrence(seq)`. The module
  currently feeds the self-validation sequence (torus `P_m`, `m = 1..7`); swap
  in the binding `a_D⁽ⁿ⁾` once #1765 supplies `n = 2, 3`.
- **Output / artifact:** `minimal_recurrence` returns `(d, [c_0,…,c_{d-1}])` —
  the minimal recurrence depth `d` and constant kernel — or `None` (no
  fixed-depth recurrence ⇒ keystone refuted at that order). The run emits
  `sw-prolongation-symbol.witness.json` (audit-only) recording the recovered
  `(d, c_j)` and the self-validation assertion.
- **Self-validation:** the torus sequence must return `d = 2`,
  `c = [−1, 2 cosh(2η₀)]` (Chebyshev) — this certifies the machinery before the
  binding inputs are consumed.

## 5. Next steps

1. `sw_prolongation_symbol.py` — the depth-`d` consistency tester (this branch).
2. Obtain `a_D⁽²⁾`, `a_D⁽³⁾` from #1765; run the test on `n = 2, 3, 4`.
3. If a fixed-depth recurrence holds, derive `R`'s kernel from the SW
   connection's branch-point Laurent data and check it matches the empirical
   `c_j` (closing the loop structurally).
4. On success: instantiate `QDifferenceKernelIsProlongationSymbol` ⇒
   `thm:binding-closure-conditional` becomes unconditional ⇒ P1 proved.
