# α_EM Front-3 ↔ W_λ keystone: the shared Bring period matrix `τ` (cross-link)

**Date:** 2026-07-17 · **Tier:** cross-link note + Lean formalization ·
**Scope:** (a); nothing wired.

> **Status of 1 ppQ is NOT reassessed here — see the canonical doc.**
> A same-day, same-request program reassessment already landed on main:
> [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)
> (L1 CLOSED ⁴He 6/6; L2 still 2/7; each miss reduced to one *named*
> computation). This note does **not** fork a parallel status doc. It records
> only **one structural observation** those front-by-front docs do not make —
> that two of the "separate" fronts share a single upstream geometric object —
> plus the machine-verified rep-theory core underneath it.

## The observation: Front 3 and the keystone share `τ`

The two live geometric attacks are treated as independent:

- **α_EM Front 3** — the photon 1-loop determinant normalization `1/(πb₁)=1/(8π)`
  on the genus-4 Bring **Jacobian** `J(𝓑_Br)=H¹/H¹(ℤ)`. The `b₁`-count is now
  *derived area-free* — [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
  shows `ζ_{Δ₁}(0)=−b₁` because the Epstein zeta `E_Λ(0)=−1` for *every* lattice
  independent of covolume (the residual open piece is the `π`/normalization, not
  the `b₁`).
- **W_λ keystone** — the McKay `2I↔Ê₈` value map `d_q(λ)=[mark]_q` (exact, no
  fit) + framing-is-phase; the one open piece is the *colored Lawrence–Rozansky
  modulus* `|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)`.

**Both are readings of one object:** `H¹(𝓑_Br)` with its S₅ action. The photon
threads through the `b₁=2g=8` one-cycles = the abelian Jacobian; the keystone's
LR amplitude lives on the same genus-4 surface via `A₅⊂S₅`. Concretely, from
[`x5-bring-prym-jacobian.md`](../../content/quantum-observable-universe/particle-interactions/x5-bring-prym-jacobian.md),
the ℤ₅-nontrivial part is `H¹(𝓑_Br,ℚ)_{≠0}=χ₁⊕χ₂⊕χ₃⊕χ₄` (`χ_k:\sigma\mapsto ζ₅^{-k}`)
plus a weight-0 S₅-standard summand; and [`s5_bring_hodge_depth.py`](../../computations/substrate/s5_bring_hodge_depth.py)
fixes `H⁰(Ω)≅W` (irreducible 4-dim S₅ standard rep, Riera–Rodríguez 1992) so
`H¹=2W`.

**Consequence for the plan:** computing the genus-4 Bring **period matrix `τ`**
once feeds *both* fronts —
- Front 3 needs `√det(Im τ)` (the Jacobian covolume) to finish the `1/(8π)`
  normalization now that `ζ_{Δ₁}(0)=−b₁` supplies the bare count;
- the keystone modulus `|S_{0λ}|` is built from the same S₅-isotypical periods.

So the currently-**unowned** "compute the Bring `τ`" is a shared sub-step, not two
separate ones. **Caveat (do not over-claim):** the photon is *abelian* (U(1) →
the Jacobian torus); the LR amplitude is *non-abelian* (SU(2)_q colored). They
share the S₅-equivariant Hodge structure and `τ`, **not** the moduli space; and
whether the four `ζ₅` channels map onto the four E₈ marks is exactly the
*unverified* geometric leg (`d_q(λ)=[mark]_q` is proved on the Hecke side, assumed
on the geometric side).

## Formalized here (machine-verified)

[`QOU/ArchimedeanUniverse/s5_bring_hodge_depth.lean`](../../content/quantum-observable-universe/lean/QOU/ArchimedeanUniverse/s5_bring_hodge_depth.lean)
— `lean`-direct v4.24.0, **sorry-free** — the S₅ character core that both fronts
sit on: `W=(4,1)` irreducible, sign-twist `(2,1,1,1)` irreducible and distinct,
and **`⟨χ_{H¹},χ_W⟩=2`** (mult 2 ⇒ Gauss–Manin recurrence depth ≤ 2 by Schur).
Honest scope, stated in the file: the geometric identification `H⁰(Ω)≅W` and
*depth = 2* (Griffiths transversality) are **cited, not proved**. `τ` itself is
**not** in-corpus — `s5_bring_hodge_depth.py` takes it as the Riera–Rodríguez
input; computing it numerically remains the unowned shared sub-step above.
