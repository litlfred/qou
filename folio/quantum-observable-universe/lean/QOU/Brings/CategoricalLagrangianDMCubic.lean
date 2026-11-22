import Mathlib.Tactic

/-!
# QOU.Brings.CategoricalLagrangianDMCubic — the Donagi–Markman cubic-condition route to an INDEPENDENT geometric origin for the binding kernel C1

**Scope (read this first).**  This file is a **FORMALIZE-FIRST STRUCTURAL
SCAFFOLD** for an *open research route*, not a proof of anything about the
keystone binding kernel.  It states — honestly, as content-bearing conjecture
carriers with **no instances** — the structural chain by which the
Donagi–Markman "cubic condition" (`[donagi-markman1996cubics]` §1;
`[donagi1997swintegrable]`) would give the keystone binding kernel **C1** an
**independent geometric origin**, de-tautologizing the QDM-3 result.

**Why de-tautologize.**  `QOU.Machinery.QProlongation.symbol_eq_recurrence_kernel`
proves `symbol D_q = recurrenceKernelLead κ` **by construction**: the recurrence
operator `D_q` is *defined from* the C1 recurrence and `recurrenceKernelLead` is
*defined as* the leading term of that same recurrence.  That is an honest
tautological re-encoding (its own file says so), **not** a geometric origin for
C1.  The genuine wall is to build the cubic / period datum *independently* from
the Bring hyperkähler geometry and only *then* match it to the kernel.  This
file scaffolds that independent side.

**The 4-form → 2-form correction (documented, load-bearing).**  The Bring cone
`C(𝓑) ⊂ ℂ⁵` is a **real-4-dimensional** manifold
(`def:bring-cone-tetraplectic-structure`;
`QOU.Tetraplectic.BringCone`).  A tetraplectic 4-form on a `4m`-manifold needs
`Ω^m` non-degenerate; at `m = 1` the 4-form degenerates to a mere volume form
and carries **no** Lagrangian-fibration data.  The structure that actually
supports a Donagi–Markman ACIHS / Lagrangian fibration is the **hyperkähler
holomorphic-symplectic 2-form** `Ω_ℂ` (signalled by the 3-Sasakian link + the
Reeb quaternionic twist `[M_i,M_j] = 2M_k`, proved sorry-free in
`QOU.Tetraplectic.BringCone`).  So the load-bearing object below is the
holomorphic-symplectic **2-form**, NOT the 4-form.

## The structural chain (each item stated honestly)

1. `QDonagiMarkmanCubicCondition` — **primary conjecture class** (§3b-tax).  The
   q-analogue of DM's cubic condition on a q-Lagrangian fibration: there is a
   *field of totally-symmetric cubics* `c ∈ Sym³ T*B` whose contraction is the
   differential of the (q-)period map.  Content-bearing: the field asserts the
   period differential is *totally* symmetric (the integrability that is
   equivalent to the fibration being Lagrangian / the period matrix being a
   Hessian), which is FALSE for a generic fibration.  No instance (open).

2. `BringHolomorphicSymplectic` — **primary conjecture class** (§3b-tax).  The
   Bring hyperkähler cone carries a non-degenerate holomorphic-symplectic 2-form
   `Ω_ℂ`, and the on-shell categorical-Lagrangian wavefront `𝒟_∇ψ = 0`
   (`def:categorical-lagrangian`, `rem:wavefront-propagation`) is **Lagrangian**
   (isotropic + half-dimensional) w.r.t. it.  Content-bearing; no instance.

3. `categorical_lagrangian_dm_cubic` — **conditional theorem** (§3b-cond),
   proved sorry-free *modulo* classes (1)+(2) taken as explicit `[Instance]`
   hypotheses (the binders ARE the dependency edges, §3b-tax).  It composes the
   two class fields: it extracts the DM q-cubic of the Bring fibration, *derives*
   its full `S₃`/3-cycle symmetry from the two transposition symmetries (a
   genuine composition, not a self-assuming projection), and carries through the
   Lagrangian isotropy of the wavefront from class (2).

4. `QCubicEqBindingKernel` — **THE TARGET, dependent conjecture class** (§3b-tax;
   depends on class (1) via an `[Instance]` binder).  It asserts the open
   identity: the DM q-cubic of the Bring fibration equals the binding kernel
   **C1** — concretely, the q-cubic's leading self-contraction is the nonzero
   recurrence-kernel weight κ = `QOU.Machinery.QProlongation.recurrenceKernelLead`
   (the leading term of the depth-2 C1 kernel
   `[n+2]_q b_{n+2} = b_{n+1} + b_n`,
   `QOU.Mass.QDifferenceConfluentObstruction`).  **This is the genuine open
   wall.**  It has **no instance**.  Deriving it (NOT fitting it) is what would
   give C1 an independent geometric origin and de-tautologize QDM-3; it is **NOT
   proved here.**

## Honesty (STRICT — the whole point; AGENTS.md §3b / §Axiomatization is NOT a Proof)

* Content-bearing classes only — no empty `: Prop`, no `: True` field.  Each
  field is a parameter-quantified statement in the SHAPE of the claim
  (`proof-no-empty-prop-carrier` / `proof-claims-unencoded` would flag a bare
  marker).
* **No fake instances** to "close" a primary/target conjecture; **no
  `native_decide`**; **no relabelling** a conjecture as a theorem.  The one
  theorem here is genuinely conditional (§3b-cond) and derives its conclusion
  from the class fields.
* Nothing here is wired to production; C1 gets no geometric origin from this
  file — the scaffold *narrows the search*, it does not close the keystone.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]` throughout.  No `ℝ`, no ordering, no
`Real.*`, no archimedean construct: the cubics, the period differential, the
2-form and the kernel weight are pure `CommRing` algebra.  Any archimedean
Seiberg–Witten-period specialisation lives downstream, past the
substrate→archimedean wall.

## References

- [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 (§1 "The
  cubic condition": a family of abelian varieties admits a Lagrangian ACIHS
  structure iff there is a field of cubics on `TB` such that `dPeriod = ⟨c,·⟩`).
- [donagi1997swintegrable] https://arxiv.org/abs/alg-geom/9705010 (SW
  specialisation: `c_{ijk} = ∂³F`, `τ_{ij} = ∂²F`).
- [grassi-gu-marino2019qsw] https://doi.org/10.1007/JHEP07(2020)106 (quantum SW
  curve as a difference operator — the difference-kernel touch-point).
- [braden-marshakov2006wdvv] https://arxiv.org/abs/hep-th/0205308 (CAVEAT: the
  SW base is generally **not** a Frobenius manifold — do not claim it is; the
  genuine fact used is "cubic = 3-jet of the prepotential").
- [leitner2026] `def:categorical-lagrangian`, `rem:wavefront-propagation`,
  `def:bring-cone-tetraplectic-structure`,
  `lem:bring-cone-reeb-quaternionic-twist`,
  `conj:categorical-lagrangian-dm-cubic`;
  QDM-3 tautology audit
  `docs/audits/2026-07-20-qprolongation-definitional-sharpening.md`.
-/

noncomputable section

namespace QOU.Brings.CategoricalLagrangianDMCubic

/-! ### Geometric data carriers (data structures — NOT conjectures)

These are the geometric objects the conjectures are stated *about*, analogous to
`QOU.AlgebraicSubstrate.ReebEpsilon`.  Naming data does not assert anything; the
logical content lives entirely in the conjecture classes below.
-/

/-- **q-Lagrangian fibration data.**  A base of dimension `dim` together with the
    *differential of the (q-)period map* `dPeriod i j k = ∂_k τ_{ij}`, where
    `τ_{ij}` is the (symmetric) q-period matrix.  We record only the symmetry the
    period matrix carries a priori — symmetry in the first two slots
    (`τ_{ij} = τ_{ji}`).  The *third-slot* symmetry is exactly the Donagi–Markman
    cubic condition and is therefore NOT recorded here — it is the content of the
    conjecture class `QDonagiMarkmanCubicCondition`. -/
structure QLagrangianFibration (R : Type*) [CommRing R] where
  /-- Complex dimension of the fibration base `B`. -/
  dim : ℕ
  /-- Differential of the q-period map: `dPeriod i j k = ∂_k τ_{ij}`. -/
  dPeriod : Fin dim → Fin dim → Fin dim → R
  /-- The q-period matrix is symmetric: `∂_k τ_{ij} = ∂_k τ_{ji}`. -/
  dPeriod_symm_ij : ∀ i j k, dPeriod i j k = dPeriod j i k

/-- **Bring hyperkähler / holomorphic-symplectic data.**  The tangent model of
    the Bring cone carries an antisymmetric 2-form `omega = Ω_ℂ` (the
    holomorphic-symplectic form — the load-bearing structure after the
    4-form → 2-form correction) and a predicate `onShell` selecting the on-shell
    categorical-Lagrangian wavefront directions `𝒟_∇ψ = 0`.  Non-degeneracy and
    the Lagrangian property of `onShell` are the *conjectural* content and live
    in `BringHolomorphicSymplectic`, not here. -/
structure BringHKData (R : Type*) [CommRing R] where
  /-- Real dimension of the tangent model (even, for a symplectic form). -/
  dim : ℕ
  /-- The holomorphic-symplectic 2-form `Ω_ℂ` (a bilinear form on the tangent
      model). -/
  omega : Fin dim → Fin dim → R
  /-- `Ω_ℂ` is antisymmetric. -/
  omega_antisymm : ∀ i j, omega i j = - omega j i
  /-- The on-shell categorical-Lagrangian wavefront `𝒟_∇ψ = 0`, as a family of
      tangent directions. -/
  onShell : Fin dim → Prop

/-! ### (1) Primary conjecture — the q-analogue Donagi–Markman cubic condition -/

/-- **§3b primary conjecture class — the q-Donagi–Markman cubic condition.**

    `@conjecture: primary`

    The q-analogue of the Donagi–Markman cubic condition
    (`[donagi-markman1996cubics]` §1): for the q-Lagrangian fibration `F`, there
    is a **field of totally-symmetric cubics** `c ∈ Sym³ T*B` — symmetric under
    every transposition of its three slots — whose contraction reproduces the
    differential of the q-period map, `dPeriod = ⟨c, ·⟩` (i.e. `∂_k τ_{ij} =
    c_{ijk}`).

    **Content (not a marker).**  `F` records only that `dPeriod` is symmetric in
    its first two slots (the period matrix is symmetric).  The class asserts the
    STRONGER, non-automatic fact that `dPeriod` is *totally* symmetric — the
    integrability equivalent to `τ` being a Hessian `∂²F` and the fibration being
    Lagrangian (an ACIHS).  This is FALSE for a generic `dPeriod`, so the class
    genuinely constrains `F`; it is not dischargeable for an arbitrary fibration.

    No instance is supplied — the honest open state of the cubic-condition
    conjecture. -/
-- Ref: [donagi-markman1994] https://arxiv.org/abs/alg-geom/9408004 §1
-- Ref: [donagi1997] https://arxiv.org/abs/alg-geom/9705010
-- Ref: [leitner2026] conj:categorical-lagrangian-dm-cubic
class QDonagiMarkmanCubicCondition {R : Type*} [CommRing R]
    (F : QLagrangianFibration R) : Prop where
  /-- There is a totally-symmetric cubic `c` realising the period differential:
      `c` is symmetric under the (1 2) and (2 3) transpositions (which generate
      `S₃`), and `∂_k τ_{ij} = c_{ijk}`. -/
  exists_cubic :
    ∃ c : Fin F.dim → Fin F.dim → Fin F.dim → R,
      (∀ i j k, c i j k = c j i k) ∧
      (∀ i j k, c i j k = c i k j) ∧
      (∀ i j k, F.dPeriod i j k = c i j k)

/-! ### (2) Primary conjecture — the Bring holomorphic-symplectic 2-form -/

/-- **§3b primary conjecture class — the Bring holomorphic-symplectic 2-form and
    the Lagrangian wavefront.**

    `@conjecture: primary`

    The Bring hyperkähler cone carries a **non-degenerate** holomorphic-symplectic
    2-form `Ω_ℂ` (the `omega` of `D`), and the on-shell categorical-Lagrangian
    wavefront `𝒟_∇ψ = 0` (`D.onShell`) is **Lagrangian** with respect to it:
    isotropic (`Ω_ℂ` restricts to `0`) and half-dimensional.

    **The 4-form → 2-form correction is the reason this class exists.**  On the
    real-4-dim Bring cone the tetraplectic 4-form degenerates to a volume form and
    carries no fibration data; the holomorphic-symplectic 2-form `Ω_ℂ` (signalled
    by the 3-Sasakian link + the Reeb twist `[M_i,M_j] = 2M_k`,
    `QOU.Tetraplectic.BringCone`) is the load-bearing structure.

    **Content (not a marker).**  Three parameter-quantified fields: global
    non-degeneracy, isotropy of the wavefront, and half-dimensionality — together
    exactly "the wavefront is a Lagrangian submanifold of `(·, Ω_ℂ)`".  No
    instance is supplied — the honest open state. -/
-- Ref: [leitner2026] def:categorical-lagrangian, rem:wavefront-propagation,
--      def:bring-cone-tetraplectic-structure,
--      lem:bring-cone-reeb-quaternionic-twist
-- Ref: [leitner2026] conj:categorical-lagrangian-dm-cubic
class BringHolomorphicSymplectic {R : Type*} [CommRing R]
    (D : BringHKData R) : Prop where
  /-- `Ω_ℂ` is non-degenerate: every tangent direction pairs non-trivially. -/
  omega_nondegenerate : ∀ i : Fin D.dim, ∃ j : Fin D.dim, D.omega i j ≠ 0
  /-- The on-shell wavefront is isotropic: `Ω_ℂ` restricts to `0` on it (the
      defining half of "Lagrangian"). -/
  wavefront_isotropic :
    ∀ i j : Fin D.dim, D.onShell i → D.onShell j → D.omega i j = 0
  /-- The on-shell wavefront is half-dimensional: it carries exactly `dim/2`
      independent directions (the completing half of "Lagrangian"). -/
  wavefront_half_dim :
    ∃ S : Finset (Fin D.dim), (∀ i ∈ S, D.onShell i) ∧ 2 * S.card = D.dim

/-! ### (3) Conditional theorem (§3b-cond) — the DM cubic of the Bring fibration -/

/-- **Conditional on `QDonagiMarkmanCubicCondition F` and
    `BringHolomorphicSymplectic D`** (both taken as explicit `[Instance]`
    hypotheses — the binders ARE the dependency edges, §3b-tax): applying the
    Donagi–Markman cubic condition to the Bring q-Lagrangian fibration `F`
    (whose base is Lagrangian for `Ω_ℂ` by `D`) yields a q-cubic `c` on the base
    that

    * reproduces the period differential (`∂_k τ_{ij} = c_{ijk}`), and
    * is fully `S₃`-symmetric — here witnessed by the 3-cycle symmetry
      `c_{ijk} = c_{jki}`, **derived** by composing the two transposition
      symmetries of the class (a genuine composition of the class fields, not a
      self-assuming projection), and

    while the wavefront stays isotropic for `Ω_ℂ` (carried through from `D`).

    This is a §3b-cond *rigorous conditional result*: fully verified by Lean
    modulo the two named, class-axiomatised conjectural inputs.  It does **NOT**
    identify `c` with the binding kernel — that is the separate open target
    `QCubicEqBindingKernel` below. -/
-- Ref: [donagi-markman1994] https://arxiv.org/abs/alg-geom/9408004 §1
-- Ref: [leitner2026] conj:categorical-lagrangian-dm-cubic
theorem categorical_lagrangian_dm_cubic {R : Type*} [CommRing R]
    (F : QLagrangianFibration R) (D : BringHKData R)
    [QDonagiMarkmanCubicCondition F] [BringHolomorphicSymplectic D] :
    ∃ c : Fin F.dim → Fin F.dim → Fin F.dim → R,
      (∀ i j k, F.dPeriod i j k = c i j k) ∧
      (∀ i j k, c i j k = c j k i) ∧
      (∀ i j : Fin D.dim, D.onShell i → D.onShell j → D.omega i j = 0) := by
  obtain ⟨c, hswap12, hswap23, hcond⟩ :=
    QDonagiMarkmanCubicCondition.exists_cubic (F := F)
  refine ⟨c, hcond, ?_, ?_⟩
  · -- 3-cycle symmetry `c i j k = c j k i`, derived from the two transpositions:
    -- `c i j k = c j i k` (swap 1↔2) `= c j k i` (swap 2↔3).
    intro i j k
    rw [hswap12 i j k, hswap23 j i k]
  · -- Lagrangian isotropy of the wavefront carried through from `D`.
    exact BringHolomorphicSymplectic.wavefront_isotropic

/-! ### (4) THE TARGET — the open keystone identity `q-cubic = binding kernel C1` -/

/-- **§3b dependent target conjecture class — the q-cubic equals the binding
    kernel C1.**

    `@conjecture: dependent` (depends on `QDonagiMarkmanCubicCondition F` via the
    `[Instance]` binder — the dependency edge, §3b-tax).

    **THIS IS THE GENUINE OPEN WALL.**  It asserts the identity that would give
    the keystone binding kernel **C1** an *independent geometric origin*: the
    Donagi–Markman q-cubic `c` of the Bring q-Lagrangian fibration `F` (which
    exists by `[QDonagiMarkmanCubicCondition F]`) equals the binding kernel C1 —
    concretely, `c` has a distinguished base direction `d` whose self-contraction
    `c_{ddd}` is the **nonzero** leading recurrence-kernel weight
    `κ = QOU.Machinery.QProlongation.recurrenceKernelLead` (the top-shift term of
    the proved depth-2 C1 kernel `[n+2]_q b_{n+2} = b_{n+1} + b_n`,
    `QOU.Mass.QDifferenceConfluentObstruction`).

    **Honesty.**  `κ` is carried abstractly (documented contract, mirroring
    `QOU.Mathlib.QJetBundle`'s light-import discipline) rather than importing the
    heavy `QuantumTorus` cone; the class names the exact decls it stands for.
    The field is content-bearing (a nonzero leading identification in the shape of
    the claim), NOT a marker.  **No instance is supplied.**  If this identity were
    *derived* (not fitted) it would de-tautologize QDM-3 — but it is NOT proved
    here.  The earlier `symbol D_q = recurrenceKernelLead κ` is a tautological
    re-encoding of the recurrence; nothing above supplies the independent
    geometric side, and this class must NOT be discharged by a fit. -/
-- Ref: [donagi1997] https://arxiv.org/abs/alg-geom/9705010
-- Ref: [grassi-gu-marino2019qsw] https://doi.org/10.1007/JHEP07(2020)106
-- Ref: [leitner2026] conj:categorical-lagrangian-dm-cubic;
--      QOU.Machinery.QProlongation.recurrenceKernelLead;
--      QOU.Mass.QDifferenceConfluentObstruction;
--      docs/audits/2026-07-20-qprolongation-definitional-sharpening.md
class QCubicEqBindingKernel {R : Type*} [CommRing R]
    (F : QLagrangianFibration R) (κ : R) [QDonagiMarkmanCubicCondition F] : Prop where
  /-- For any DM q-cubic `c` of `F` (any cubic realising the period differential),
      there is a distinguished base direction `d` whose self-contraction is the
      **nonzero** binding-kernel leading weight: `c_{ddd} = κ ≠ 0`.  The open
      identification of the geometric q-cubic with the C1 kernel. -/
  cubic_lead_eq_kernel :
    ∀ c : Fin F.dim → Fin F.dim → Fin F.dim → R,
      (∀ i j k, F.dPeriod i j k = c i j k) →
      ∃ d : Fin F.dim, c d d d = κ ∧ κ ≠ 0

end QOU.Brings.CategoricalLagrangianDMCubic
