# Why the duality σ is complex conjugation — the derivation, step by step

**Bean `qou-qjhc`. Branch `claude/duality-sigma-hermitian-derivation-2026-09-14`.**

The measurement side is settled: on every exact point the corpus holds, the field
automorphism carrying the duality intertwiner is complex conjugation of `K`
(`ptolemy_duality_sigma_is_complex_conjugation.py`, merged in #7356). That probe
says so explicitly of itself: *"It says nothing about WHY duality should be
realised by conjugation."*

This is the why, as far as it goes — and §5 states precisely where it stops.

## 0. The request was to start from the categorical Lagrangian. It cannot be done yet, and that is a finding

The corpus's categorical Lagrangian is a closed, formula-pinned object:

```
ℒ_q(∇, ψ) = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ  ∈ End_𝐂(A),      ψ* = ∫_A ∘ S(ψ)
𝒟_∇ = q⁻¹∇ + (1 − q⁻¹)ι_ξ∇
𝔖_q = tr(ℒ_q)
```

(`def:categorical-lagrangian`, Lean `QOU.CategoricalLagrangian`, a `structure` whose
`lagrangian_formula` field pins the morphism; existence and uniqueness both proved
sorry-free.)

**Measured across all six corpus-grep paths on 2026-09-14: the corpus's
reality/conjugation arc and its Lagrangian arc do not touch anywhere.** A
co-occurrence scan of the reality cluster (1,575 files) against the Lagrangian/action
set over 18,639 tracked `content/` files returns nothing; a case-insensitive grep for
`agrangian`, `categorical action` and `action functional` over `QOU/Eightfold/` (where
the real-structure arc lives) and over `content/.../eightfold-way/` returns **zero
matches in both directions**.

Three specific gaps, each of which would have to be closed first:

1. **The only anti-structure inside `ℒ_q` is the antipode `S`**, via `ψ* = ∫_A ∘ S(ψ)`
   — and `def:frobenius-hopf-substrate` **nowhere asserts `S² = id`**. The QOU
   substrate's antipode is not known to be an involution. (The `S² = id` hits in the
   corpus are all the *Hecke* antipode, a different object.) So the involutivity
   hypothesis this derivation needs has no supplier upstream.
2. `ℒ_q` is **fibre-independent** — `alg:categorical-action` states it flatly:
   *"It depends strictly on the rigid-monoidal structure of 𝐂, independent of the
   fibre functor τ. Archimedean specialisation enters at Step 9."* But a signature
   (§4) is an archimedean invariant. So any Lagrangian route to conjugation must pass
   through the archimedean specialisation, not around it.
3. `prop:categorical-self-duality` — the one self-duality statement that *is* about
   the Lagrangian — is **unformalised**, and the block says so itself: *"The
   implication above is established in narrative here and is not formalised."*

Reporting this as a gap rather than bridging it is deliberate. A derivation that
started "assume `S` is a real structure" would be assuming the conclusion.

## 1. Step 1 — the intertwiner relation *is* an invariant form. Forced.

The duality datum is an invertible `A` over `K` with, for every generator `g`,

```
A · σ(ρ(g)) · A⁻¹ = ρ(g)^{-T}.                                    (*)
```

Multiply (*) on the right by `A`, then on the left by `ρ(g)ᵀ`:

```
A σ(ρ(g))           = ρ(g)^{-T} A
ρ(g)ᵀ A σ(ρ(g))     = A.                                          (**)
```

Define the σ-sesquilinear form on `K³`

```
H(v, w) := vᵀ A σ(w).
```

Then `H(ρ(g)v, ρ(g)w) = vᵀ ρ(g)ᵀ A σ(ρ(g)) σ(w) = vᵀ A σ(w) = H(v, w)` by (**).

**The duality intertwiner and a ρ-invariant sesquilinear form are the same object
written two ways.** No choice was made anywhere; this is one line of rearrangement.

Formalised: `QOU.Eightfold.invariantForm_of_intertwiner`. It needs no hypothesis on
`σ` at all — the whole content is `Mᵀ · Minv = 1`.

**Schur.** Solving (**) as a linear system over ℚ, the solution space has exactly
`[K:ℚ]` free ℚ-parameters in every case — one `K`-dimension. So `A` is canonical up
to a `K`-scalar. Measured: 4 (5_2 orbit 0), 4 (L6a4), 2 (m004), 6 (5_2 orbit 1).

## 2. Step 2 — it normalises Hermitian, constructively, by Hilbert 90

Write `A† := ᵗσ(A)`. Expanding the Hermitian condition `H(w,v) = σ(H(v,w))`:

```
wᵀ A σ(v) = σ(vᵀ A σ(w)) = σ(v)ᵀ σ(A) w = wᵀ ᵗσ(A) σ(v),
```

so **`H` is σ-Hermitian ⟺ `A = A†`**.

`A†` is also an invariant form, and by Schur `A` is unique up to a `K`-scalar, so

```
A† = c·A   for a unique c ∈ K.
```

Applying `†` twice: `A = (cA)† = σ(c) A† = σ(c) c A`, hence

```
N(c) := σ(c)·c = 1.
```

**Hilbert 90** for `K / Fix(σ)` makes such a `c` a ratio, and here explicitly: for any
`x`, set `d := x + c σ(x)`. Then

```
σ(d) = σ(x) + σ(c) x = σ(x) + x/c = d/c,   so   σ(d)·c = d,
```

and therefore `(dA)† = σ(d) A† = σ(d) c A = d·A`. **`A_herm := d·A` is Hermitian.**
The witness is produced, not asserted to exist.

Measured `c`, per case — note it is *not* always `−1`, so the normalisation is doing
real work:

| case | `c` | Hilbert-90 witness `d` |
|---|---|---|
| `5_2-c1-orbit0` | `−1` | `(81t³ − 657t² + 64559t − 6247)/29197` |
| `m004-c1` | `t + 5` | `t + 6` |
| `L6a4-c1` | `256t³/113642578125 + 9298/11637` | `256t³/113642578125 + 20935/11637` |
| `5_2-c1-orbit1` | `1` | `2` |

`N(c) = 1` verified exactly in all four; `A_herm† = A_herm` verified exactly in all
four.

Formalised: `QOU.Eightfold.hilbert90_witness`,
`QOU.Eightfold.hermitian_of_hilbert90_witness`, assembled as
`QOU.Eightfold.hermitian_representative`. All sorry-free, over a general `CommRing`
with an arbitrary ring endomorphism.

## 3. Steps 1–2 do NOT single out conjugation

This is the load-bearing caveat and it is easy to miss. Everything above holds for
**any** involution `σ`. If the argument stopped here it would prove that *every*
non-identity involution carries an invariant Hermitian form — which is false, and
measured to be false: on `5_2` orbit 0 the other two involutions give nullspace
dimension **0**, no invariant form at all.

So Steps 1–2 explain what a duality `σ` *gives you*; they do not explain *which* `σ`.

## 4. Step 3 — the signature, which is what conjugation supplies

Embed `K ↪ ℂ`. If `σ` acts as complex conjugation at that embedding, then `†` is the
ordinary conjugate transpose, `A_herm` is a Hermitian **matrix**, its eigenvalues are
real, and it has a **signature** `(p,q)`, `p+q=3`. Then `ρ` lands in `U(p,q)`.

For an abstract involution none of this exists. **A signature is an archimedean
invariant, and that is the whole of what complex conjugation contributes.**

Read two independent exact ways, required to agree or the probe aborts:

- **Jacobi** on leading principal minors. For a σ-Hermitian matrix every leading
  principal minor is σ-**fixed**, hence lies in `Fix(σ)`; when `K` is CM that subfield
  is totally real, so each minor is a real algebraic number with an unambiguous sign,
  and the signature is the count of sign agreements/changes in `(1, D₁, D₂, D₃)`. No
  eigenvalue solver.
- the **roots of the characteristic polynomial** at 50 dps, asserted real.

| case | signature | at how many embeddings |
|---|---|---|
| `5_2-c1-orbit0` | (2,1) | 4 of 4 |
| `L6a4-c1` | (1,2) | 4 of 4 |
| `m004-c1` | (1,2) | 2 of 2 |
| `5_2-c1-orbit1` | (2,1) | 2 of 6, then the assertion fires — see §5 |

`(p,q)` and `(q,p)` are the same statement: `A_herm` is defined only up to a **real**
scalar and negating it swaps them. The projective group is **`PU(2,1)`** in every case.

**`PU(2,1)` is the isometry group of complex hyperbolic 2-space `ℂH²`, whose boundary
is the strictly pseudoconvex CR 3-sphere.** So these are **spherical CR
representations**, and the conjugation is the Hermitian structure of the CR geometry.

An incidental corroboration, noticed because it broke Jacobi: `A_herm[0,0] = 0` in
every case — `e₀` is a **null vector** of the form. A definite form has none, so the
indefiniteness was visible before the signature was computed.

**This converges with the corpus from the other side.** `brings-surface-unit-circle`
is *"the CR structure `M_S` carrying the archimedean QOU"*;
`observability-independent-motivation.md` records that Bring's surface is *strictly
pseudoconvex*; the Levi form is a Hermitian form (`QOU/Glossary.lean:186`); and
`simplicity-from-category.md` opens *"The ∗-involution enforces self-duality on the
2-forms … The geometric input reduces entirely to the CR structure."* Signature (2,1)
on `ℂ³` is exactly what makes the null cone a strictly pseudoconvex CR 3-sphere, so
the two pictures are consistent. **They are not yet connected** — no block states it.

## 5. What this does NOT establish

1. **Not a Lagrangian derivation.** §0. The chain runs from the intertwiner, not from
   `ℒ_q`, and the corpus supplies no edge between them.
2. **Not an explanation of WHY these reps are `PU(2,1)`.** Steps 1–3 show
   *conjugation ⟺ invariant Hermitian form*, and measure the signature. That the
   representations preserve such a form at all is the input, not the output.
3. **The converse is open.** Nothing here shows a duality `σ` *must* be conjugation.
4. **Orbit 1 is weaker than the table suggests, and the code enforces it.** Its `K` is
   totally imaginary but **not CM**: `Fix(σ)` has degree 3 and is not totally real, so
   the minors are not real at every embedding and no signature is defined at 4 of the
   6. The probe asserts and aborts rather than reporting one. `|Aut| = 2` there, so it
   could not have selected anything anyway.

## Artifacts

- `computations/ptolemy/ptolemy_duality_hermitian_form.py` — the three-step probe.
- `content/quantum-observable-universe/lean/QOU/Eightfold/DualityIntertwinerIsHermitianForm.lean`
  — Steps 1–2, lean-direct exit 0, `#print axioms` clean on all four declarations.
- `computations/ptolemy/ptolemy_duality_sigma_is_complex_conjugation.py` — the
  measurement this explains (merged #7356).
