# W1 arrow (A): the S₃-equivariance invariant + the DGG value-map build plan

> **⚠ CORRECTED (2026-08-01) — Part 1 below is WRONG.** The 3D-index function is
> S₃-**invariant** (trivial isotypic only); the `84·sign + 240·std` are the
> decomposition of the representation *space*, **not** the index vector. So
> `I_tot_meridian` discards no standard content (there is none), S₃ is *vacuous*
> for arrow (A), and there is no "graded standard component" to build from. See
> [`2026-08-01-arrow-a-s3-index-invariance-correction.md`](2026-08-01-arrow-a-s3-index-invariance-correction.md).
> Part 2 (the build plan, steps 2–5) stands; step 1 is corrected there.

**Date:** 2026-08-01
**Tier:** audit-only; scope-(a); no fit; nothing wired; L2 unchanged.
**Epic:** W1 binding-mass bridge `I_𝓑₃ → tr_M(β_Bor)`. Builds on the invariant
list ([`2026-07-24-borromean-index-bridge-invariant.md`](2026-07-24-borromean-index-bridge-invariant.md))
and the saddle-route result
([`2026-08-01-arrow-a-stateintegral-saddle-not-index-series.md`](2026-08-01-arrow-a-stateintegral-saddle-not-index-series.md)).

## Part 1 — the S₃-equivariance invariant (a decisive sharpening)

Invariant §1(a): a derived arrow (A) must factor through the cusp symmetry (S₃
permuting the three Borromean components) — a map of S₃-representations.
Made concrete
([`arrow_a_s3_equivariance.py`](../../computations/probes/arrow_a_s3_equivariance.py)):

The 3D-index is graded over the `{−1,0,1}⁶ = 729` peripheral classes, S₃
permuting the three `(p_h,q_h)` blocks. Exactly:

`Fix(e)=729, Fix(transposition)=81, Fix(3-cycle)=9` ⟹

$$\text{graded index} \;=\; 165\cdot\mathbf{triv}\;\oplus\;84\cdot\mathbf{sign}\;\oplus\;240\cdot\mathbf{std}$$

(`mult(triv)=165 = #orbits`, cross-checked against the committed graded-index
witness). On the `tr_M` side, `β_Bor ∈ H₃(q)` whose Wedderburn blocks are the
partitions of 3 = the S₃-irreps: `[3]→triv, [1,1,1]→sign, [2,1]→std`, with the
Borromean content in the `[2,1]` (standard) block.

**The finding.** `I_tot_meridian` — the corpus series `[1,6,129,−510,−1205,4004,
15898]` that arrow (A) has been trying to reproduce — is the **S₃-invariant sum**
over the cusp-symmetric meridian sublattice, i.e. the projection onto the
`165·triv` part. **It discards all 240 standard copies**, exactly the
S₃-non-trivial geometric content. Consequences:

- `I_tot_meridian → tr_M(β_Bor)` is a **trivial → trivial** map: the S₃ invariant
  gives it **no constraint**, and `I_tot_meridian` is the **under-constrained**
  object to bridge from.
- The real S₃ constraint lives at the **graded (pre-sum) level**: a derived (A)
  carries the `240·std` copies onto the single Hecke `[2,1]` block — a massive
  but S₃-typed projection.

**Build implication:** construct (A) from the graded index's **standard-isotypic
component**, not from the summed `I_tot_meridian`. This is a necessary-condition
sharpening of arrow (A), not a derivation.

## Part 2 — the DGG value-map build plan (for a dedicated future session)

Arrow (A) — the actual non-perturbative map `I_𝓑₃ → tr_M(β_Bor)`'s **values** — is
the DGG 3d-3d / quantum-modularity correspondence; a multi-session build. What
this session established narrows it to a concrete program. **Established anchors
(do not re-derive):**

- **Shared volume:** `Vol(𝓑₃)=8G` on the Jones side (#4208) and via the
  state-integral saddle = Bloch–Wigner dilog at the octahedron shapes (#4494).
- **Shared 1-loop:** the NZ-Jacobian torsion `|det J_NZ|=64` = the saddle Hessian
  (#4253, DGG 1-loop conjecture); the `exp(2c₀)=1/|det|` dictionary validated on
  4₁ to 2e-11 (#4238) and the `2^(c−1)` cusp-normalization law (#4261 + Whitehead).
- **Resummation route:** the volume-route goes through the state-integral
  **saddle**, NOT the index q-series (#4494 ruled out two series routes).
- **S₃ target:** build from the graded standard component → Hecke `[2,1]` (Part 1).

### Concrete sub-steps

1. **Object selection (from Part 1).** Extract the graded index's `standard`-
   isotypic component `I^std_𝓑₃` (240 copies over the 729 classes) — the
   S₃-typed object; drop `I_tot_meridian`.
2. **State integral for 𝓑₃.** Build the Andersen–Kashaev state integral
   `Z_𝓑₃(ℏ)` (a 2–3-dim Faddeev-Φ_b oscillatory integral over the 8-tetrahedron
   / 2-octahedron gluing). Reuse the corpus Faddeev/FKV Φ_b infrastructure
   (`_phi_q_util`, the FKV strip-growth work). Validate on 4₁ first
   (1-dim integral; saddle = `Vol(4₁)`, 1-loop = `1/√3`, matching #4238/#4253).
3. **State-integral ↔ total-index bridge.** Realise GHRS Rmk 1.13
   (`I^tot ≈` state integral) at the graded level: the state integral's
   cusp-variable dependence carries the S₃-standard structure; match it to
   `I^std_𝓑₃` from step 1.
4. **State integral ↔ tr_M.** The state integral is the analytic continuation of
   the colored Jones (volume conjecture); `tr_M(β_Bor)=J_{B,2}` is a colored-Jones
   value. Establish the continuation map value-by-value (the perturbative series
   `c₀,κ₁,κ₂,…` on the Jones side = the state-integral's asymptotic series), fixing
   the nome dictionary `Q ↔ h/q` by the correspondence (invariant §1(c)), not tuned.
5. **Anti-fit gate (invariant §1(f), STRICT).** The 2.89% `Vol(𝓑₃)·ρ` gap must NOT
   enter (A); no constant chosen by proximity to `F_Bor≈4.469`; every rational
   arises from arrow (B) `[3]_q!/q³` only. A `conj:`-tier statement until the
   correspondence map is Lean-checkable, per §Axiomatization-is-NOT-a-Proof.

### Go/no-go for the plan

The plan is **feasible but research-scale** (steps 2–4 are each a real numerical
build with the state-integral machinery). It is **not** a fit: every step matches
a computed invariant against an independent one, with the nome dictionary fixed by
the correspondence. The honest open core is step 4 (the value-by-value
continuation) — the DGG correspondence itself.

## Discipline

scope-(a); the S₃ decomposition is exact integer enumeration cross-checked
against the committed witness; the plan re-uses established anchors and does not
re-derive them; nothing wired; L2 unchanged.

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
