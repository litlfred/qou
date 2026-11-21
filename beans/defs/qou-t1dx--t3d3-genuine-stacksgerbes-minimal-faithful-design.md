---
# qou-t1dx
title: 'T3/D3: genuine stacks/gerbes, minimal faithful design + first milestone'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T20:38:55Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-533l
---

Owner: try all T3 designs. Front D3: genuine stacks/gerbes. Mathlib has none at f897ebc.

Scope a minimal faithful design: a prestack as a pseudofunctor C^op -> Grpd with descent data on covers; a gerbe as locally nonempty, locally connected, with band A.

Attempt a first sorry-free milestone, e.g. the torsor prestack Tors(G) of a presheaf of groups, and that it is a prestack. Report feasibility and a cost estimate.

## 2026-10-12 — first milestone landed (branch `t3-d3-stacks`)

- Model: target is (a) pseudofunctor `LocallyDiscrete Cᵒᵖ ⥤ Cat` with groupoid fibres (Yekutieli §2 verbatim). Strict `Cᵒᵖ ⥤ Grpd` rejected as unfaithful for `Tors(G)`.
- Proved, sorry-free (exit 0, axioms propext/choice/Quot.sound): `QOU.MathlibExt.StackGerbe.isSheaf_equivariantHom`. The presheaf of `A`-equivariant morphisms `P|_{C/X} ⟶ Q|_{C/X}` is a sheaf when `Q` is. This is the descent-of-morphisms (prestack) axiom for `A`-sheaves, hence for `Tors(G)`.
- NOT proved: Hom = Iso on torsors; effective descent of objects; any gerbe statement.
- Cost estimate for full Thm 4.17 under D3: ~10–20 sessions. Critical risks: pseudofunctor Hom-presheaf coherence (S1), and nonabelian/Čech `H²` (S5). Details in `docs/audits/2026-10-12-t3-d3-stacks.md`.
- Bean stays in-progress: the stack/gerbe definitions remain open.

## 2026-11-15 — Milestones 2 & 3 landed (PR #7985, commit `c9b5c7d59272bea9b0afd42852a09253e27ad54c`)

Per owner ruling `Q-VO9T-1 = 3` (session `session_012EE90758AE4945AC814D43`), extended `QOU/MathlibExt/StackGerbe.lean` with Milestones 2 and 3 (sorry-free, 0 warnings, standard axioms `[propext, Classical.choice, Quot.sound]`):
- **Milestone 2 (`Hom = Iso` on `A`-torsors, fibre groupoid, band isomorphism):**
  - `PresheafAction.IsPseudoTorsor`, `localNonemptySieve`, `LocallyNonempty`, `SheafTorsor J A P`
  - `equivariantHom_injective`, `equivariantHom_surjective_of_nonempty`, `equivariantHom_surjective` (gluing unique local preimages along `localNonemptySieve P Y.left ∈ J Y.left` via `IsSheafFor.amalgamate` and `IsSeparatedFor.ext`)
  - `isIso_of_equivariantHom_torsor`, `id_mem_equivariantHom`, `comp_mem_equivariantHom`, `inv_mem_equivariantHom`
  - `IsPresheafOfGroups`, `PresheafAction.IsMulAction`, `regularAction`, `isMulAction_regularAction`, `isPseudoTorsor_regularAction`, `locallyNonempty_of_nonempty`, `trivialSheafTorsor`
  - `trivialTorsorEndEquiv : (equivariantHom (regularAction A hA) (regularAction A hA)).obj (op X) ≃ A.obj (op X)` (band isomorphism)
  - `MulSheafTorsor`, `TorsorFibre J A X`, `torsorFibreCategory`, `torsorFibreGroupoid`, `torsorPullback`, `torsorPullback_id`, `torsorPullback_comp`
- **Milestone 3 (genuine `SiteGerbeData` over `(C, J)` and `Tors(A)` instantiation):**
  - `equivariantHom_of_sections`, `localIsoSieve`, `torsor_locallyConnected`
  - `SiteGerbeData J A` and `torsorSiteGerbe J A hA hAsheaf`
- **Remaining open (bean stays `in-progress`):** effective descent of objects (gluing torsors from 1-cocycles on a `J`-sieve) and nonabelian/gerbe lifting obstruction comparison (S5).

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
State on main unchanged since 2026-11-15: StackGerbe.lean Milestones 1–3 (PR #7985). Open: effective descent of objects (gluing torsors from 1-cocycles on a J-sieve) and the comparison with the Čech obstruction. Not attempted in this pass; estimate from the 2026-10-12 audit still applies (multi-session).
