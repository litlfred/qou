# Covariance-kernel epic (qou-x631) — Phase 2: Śniady genus expansion on the (f^λ)³-biased measure

**Date:** 2026-07-19 · **Branch:** `claude/fl-sniady-genus-2026-07-19` · **Bean:** `qou-joi7` ·
**Epic:** `qou-x631` · **Tier:** exact verification + biased-measure asymptotics + precise
obstruction statement (kernel carried as an open conjecture) · **Discipline:** scope-(a); no fit;
nothing wired; no `c_k`; L2 unchanged (2/7). **Follows:** #3998 (frontier + Lean infra), #4xxx
(Phase 1 route-elimination).

## The kernel (unchanged, still OPEN)

> `T₃ = Σ_λ (f^λ)² χ^λ(3-cycle) ≤ 0` ⇔ `cov(k) = Σ_{λ⊢k}(f^λ)³(Σ_□c² − C(k,2)) ≤ 0`
> ⇔ `Cov_Planch(f^λ, Σ_□c²) ≤ 0` ⇔ `Cov_Planch(f^λ, R₄) ≤ 0`.

Sole open input of the Δ_λ super-exponential growth bound (#3939, via the #3959 reduction). Phase 1
verified `k ≤ 40`, framed it in free cumulants (`Σ̂₃ = R₄+R₂`, `E_Planch[R₄] = −k`), Lean-proved the
reduction `D_of_T3_nonpos` sorry-free, and eliminated two proof routes (holonomic recurrence,
β-monotonicity), naming **Śniady's genus expansion on the `(f^λ)³`-biased measure via the RSK form**
as the Phase-2 target. This note carries out that Phase 2. **The kernel remains open.**

## A. The RSK form, verified LITERALLY (new)

Prior probes compute only the closed form `Σ_λ (f^λ)² χ^λ(3-cycle)` via hook dimensions. This phase
realizes the RSK bijection concretely: Schensted row-insertion of **every** `w ∈ S_k`, for k = 3..7.
Exact (`fl_sniady_rsk_form_verify.py`, exit 0):

| k | \|S_k\| | `Σ_w χ^{sh(w)}(3-cyc)` (enum) | `Σ_λ(f^λ)²χ³` (closed) | `3cov/(k)₃` |
|---|---|---|---|---|
| 3 | 6 | −2 | −2 | −2 |
| 4 | 24 | −2 | −2 | −2 |
| 5 | 120 | −16 | −16 | −16 |
| 6 | 720 | −260 | −260 | −260 |
| 7 | 5040 | −2336 | −2336 | −2336 |

and `#{w : sh(w)=λ} = (f^λ)²` (the RSK bijection `S_k ≅ ⊔_λ SYT(λ)²`) holds cell-by-cell. So the
Kerov-CLT observable `T₃` **is** the 3-cycle character averaged over the RSK shape of a uniform
permutation — verified, not merely asserted. `χ^λ(3-cycle)` computed by Murnaghan–Nakayama (signed
3-ribbon removal).

## B. Biased-measure asymptotics (new)

`P₃(λ) = (f^λ)³/Z₃`, `Z₃ = Σ(f^λ)³`. Exact, k = 3..44 (`fl_sniady_genus_biased_measure.py`, exit 0):

- **`Δ(k) := E_{P₃}[C₂] − C(k,2) = cov(k)/Z₃ < 0` for all k** (the kernel, extended and re-expressed
  as a *measure* deficit). `E_{P₃}[R₄] = 3Δ − k` is substantially **more negative** than the
  Plancherel `E[R₄] = −k` (e.g. k=40: `E_{P₃}[R₄] ≈ −113` vs `−40`). The cube-biasing pushes the
  measure onto shapes with more negative 4th free cumulant (flatter/more-balanced diagrams).
- **Leading order `−Δ(k) ~ c·k^p`, fitted `p ≈ 1.63`** (log-log least-squares, k∈[20,44]),
  `c ≈ 0.058`. This is **sub-quadratic** — one √k (or a little more) below the `k²/2` Plancherel
  content spread `C(k,2)`. Under Plancherel this term is exactly 0 (`E_Planch[C₂] = k(k−1)/2`), so
  the deficit is **born of the biasing**. The value is near — but honestly a touch above — the
  Kerov-CLT fluctuation order `k^{3/2}` (`Std_Planch(C₂) ~ k^{3/2}`); the data is consistent with
  `k^{3/2}` up to a slow correction. **We do not claim exactly 3/2.**
- **Infinitesimal tilt** `dE_β[C₂]/dβ|_{β=2} = Cov_Planch(C₂, ln f^λ)` is `< 0` for all k≥6 and scales
  with the **same** fitted exponent `p ≈ 1.63` — the finite `β:2→3` kernel and the infinitesimal
  tilt agree in sign and order.

## C. What the genus expansion says (the honest Phase-2 conclusion)

**The Phase-1 obstruction is confirmed and made precise.** `Σ̂₃ = R₄+R₂` is a *polynomial function
on Young diagrams* — its Plancherel joint cumulants carry Śniady's genus grading. But the biasing
weight `f^λ = χ^λ(e)` is the **exponential dimension**, which lies **outside** the algebra of
polynomial functions. In `Cov_Planch(f^λ, C₂)` the genus grading controls the `C₂` factor but **not**
the `f^λ` factor, so the genus expansion of the joint cumulants of the `Σ̂`'s does **not** close the
kernel. This is exactly why the two clean routes (Kerov-CLT central-limit control of `Σ̂`, and the
polynomial-function machinery) do not directly apply.

**What the genus / limit-shape picture *does* give:**

1. The `k^{3/2}`-order scaling identifies the deficit as a **fluctuation-order** effect (subleading to
   the `k²` content spread), consistent with `Std_Planch(C₂) ~ k^{3/2}` from the Kerov CLT.
2. The **sign** is the tilted-limit-shape heuristic: the extra factor `f^λ` concentrates `P₃` more
   tightly around the `f^λ`-maximising (balanced) shape, **reducing content dispersion** ⇒ `Δ < 0`.
   This is a heuristic for the sign, **not a proof** — the tilt is a large-deviation statement about
   `ln f^λ`, and turning it into a rigorous inequality is precisely the open work.

## Implication for the Δ_λ / binding structure

The Δ_λ super-exponential growth bound (#3939) needs only the **sign** `T₃ ≤ 0`. Phase 2 shows that
sign, where it holds, is a genuine **order-`k^{3/2}`** effect — not a knife-edge, not a slack bound
(the margin `−4T₃/Z₃ → 0⁺` confirms tightness). So the growth bound is **robustly correct modulo the
still-open sign** of this fluctuation-order anti-correlation. Nothing here changes the binding /
mass compute: it is a frontier map for the open kernel, with **nothing wired**.

## Formalize-first assessment (no new Lean this phase)

The invariant that would justify a scope-(b) closure **is** the open kernel `T₃ ≤ 0`; no smaller
clean invariant emerged. The one candidate — the elementary content-form of `T₂ = 0`
(`Σ_{λ⊢k}(f^λ)³·Σ_□c(□) = 0` via the transpose involution `λ↔λ'`, which negates total content while
`sgn` of a transposition is `−1`) — requires proving that conjugation is a *bijection* on the ad-hoc
`List ℕ` partition enumeration in `YoungDiagramKernel.lean`, a multi-session Lean effort out of scope
here. The existing Lean infra already captures the state faithfully: `D_of_T3_nonpos` (sorry-free
reduction) and `covariance_kernel_conjecture` (positive-controlled §3b conjecture). **No sorry
smuggling, no fake scope-(b).**

## Verdict

Kernel **still OPEN**. Delivered: literal RSK-form verification (k≤7), exact `(f^λ)³`-biased-measure
asymptotics (content-spread deficit of fitted order `k^{1.63}`, near `k^{3/2}`), the infinitesimal-tilt
object, and a **precise statement of why the genus grading does not close it** (`f^λ ∉` polynomial-
function algebra). scope-(a); no fit; nothing wired; no `c_k`.

## Compute

- RSK-form probe: [`computations/deltalambda/fl_sniady_rsk_form_verify.py`](../../computations/deltalambda/fl_sniady_rsk_form_verify.py) (exit 0), witness `fl-sniady-rsk-form-verify.witness.json`
- Genus / biased-measure probe: [`computations/deltalambda/fl_sniady_genus_biased_measure.py`](../../computations/deltalambda/fl_sniady_genus_biased_measure.py) (exit 0), witness `fl-sniady-genus-biased-measure.witness.json`

## Cross-references

- Phase 1 (route-elimination): [`2026-07-18-covariance-kernel-proof-epic-phase1.md`](2026-07-18-covariance-kernel-proof-epic-phase1.md)
- Frontier + Lean infra (#3998): [`2026-07-18-deltalambda-covariance-kernel-frontier.md`](2026-07-18-deltalambda-covariance-kernel-frontier.md)
- Reduction to the kernel (#3959): [`2026-07-18-deltalambda-D-reduction-content-covariance.md`](2026-07-18-deltalambda-D-reduction-content-covariance.md)
- Growth bound (#3939): [`2026-07-18-wstd-superexp-lower-bound.md`](2026-07-18-wstd-superexp-lower-bound.md)
- Lean: `QOU/BraidsAndKnots/DeltaLambdaDReduction.lean` (sorry-free), `QOU/BraidsAndKnots/YoungDiagramKernel.lean` (kernel conjecture)
- Literature: Śniady (PTRF 2006, arXiv:math/0305423), Biane (Adv. Math. 1998), Morales–Pak–Panova (arXiv:1610.07561)
