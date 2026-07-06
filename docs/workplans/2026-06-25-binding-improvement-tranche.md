# Binding-improvement tranche — workplan (2026-06-25)

**Branch:** `claude/jolly-wright-6kc4d2` (post-#2734 merge; at `main` tip).
**Origin:** after PR #2734 (tau-M `c_k` ladder proof) merged, the author
selected **three** binding-improvement fronts to pursue in parallel:

1. **A=4 interface operator scaffolding** — Option E PROBE 2 (beans `ae42`/`ae43`/`ae4b`).
2. **Lever-1 fibre kernel `R(q,x)`** — beans `z2bn`/`830y`.
3. **s5-so3 keystone pre-work** — `Jac(Bring)` CM/isogeny + color `E_q`
   Picard–Fuchs rapidity test (target θ ≈ 0.7815); beans `s5bb`/keystone ledger.

This doc is the living anchor for the tranche. It is **exploratory** work
(per `production-vs-exploratory-discipline.md`): probe files carry the
`EXPLORATORY` banner, every wide search is gated by formalize-first +
q-locality, and the Δ_λ "no 7th fit-ansatz" rule stands.

## Deconfliction (the three fronts are not independent)

| Front | Actionable now? | Status |
|---|---|---|
| **1. A=4 interface operator** | **Yes — independent forward step** | Sanctioned Δ_λ PROBE-2 direction; extends the A=3 mirror-pair. Primary focus. |
| **2. Lever-1 `R(q,x)`** | **Mostly banked** | Algebraic kernel resolved in **PR #2718** (2026-06-24): depth-2 `R=x²−τx+1`, det=1; τ **algebraically fixed** (no fit) `τ=3(3q⁴+8q²+3)/(4q(q+1)²)`, τ(q₀)=2.6423863133015 (reproduced this session); λ₊≈2.1846>1 Lean-proved sorry-free (`BindingRecurrenceSpectral.lean`). **Open remainder = keystone** (geometric origin of τ) **+ `a_D^(n)=lw(n−1)`** geometric↔algebraic ID (conj #1765). |
| **3. Keystone pre-work** | **Partly — tool-gated** | The non-owner-gated remainder of front 2. Sub-direction B (CM/isogeny of `Jac(Bring)`, color `E_q` identified j≈129.86) is "mostly done"; color `E_q` Picard–Fuchs rapidity θ≈0.7815 test pending tooling (Sage?). |

**Consequence:** front 2's *open* part **is** front 3 (both gate on the
owner-reserved Gauss–Manin monodromy `tr B`). New search on the `R(q,x)`
kernel class is **not** warranted (formalize-first already pruned it — the
spectral invariant λ₊(τ)>1 is Lean-proved and the kernel satisfies it).
So the live, non-redundant work is **front 1 (A=4)** + **front 3 pre-work**.

## Outcome (2026-06-25)

Full synthesis: [`docs/audits/2026-06-25-binding-frontier-three-front-convergence.md`](../audits/2026-06-25-binding-frontier-three-front-convergence.md).

**All actionable, non-owner-gated work across the three fronts is already
banked / recorded / pruned in the corpus; the three converge on one
owner-gated object** — the abelianised λ_SW holonomy on color `E_q`
(`θ=0.7815`, `τ=2.6424`).

- **Front 1 (A=4):** interface operator exists + evaluated — under-binds ⁴He
  **−70.8%**, deficit **saturates** (⁴He/D = 2.70 vs AME 12.72). Bounded piece;
  cannot supply the extensive term (scope-(a), not exclusion). Fresh re-run
  native-gated (clarabel fork dep unfetchable here). Witness-emission hygiene
  gap in `a4_interface_trace_integration_all.py` filed as follow-up.
- **Front 2 (Lever-1):** banked (#2718); τ(q₀)=2.6423863133015 reproduced.
- **Front 3 (keystone):** curve identified (color E_q, j≈129.86); Picard–Fuchs
  route formalize-first-pruned (integer-trace obstruction). Open step
  owner-gated.

**No non-gated, non-fitting forward step remains on binding *magnitude*.** The
unlock is the owner-gated keystone holonomy. ρ-free *ratios* (Lever 3 `thb7`)
remain the parameter-free falsifiable-prediction avenue.

## Plan (status)

### Front 1 — A=4 interface operator scaffolding (PRIMARY)
- [ ] Map existing A=3 interface-operator / Option-E v9 mirror-pair code (agent running).
- [ ] Scaffold an A=4 interface-operator module (exploratory; `EXPLORATORY` banner).
- [ ] Evaluate the A=4 binding closure against AME2020 (⁴He); report honest residual.
- Discipline: this is the sanctioned PROBE-2 direction, **not** a 7th fit-ansatz.

### Front 3 — keystone pre-work (SECONDARY; partly tool-gated)
**Tooling reality (this sandbox):** Sage / PARI-gp / Magma **absent**; sympy
1.14.0 + mpmath present. So Riemann-surface integration (numeric j via periods)
and the owner-gated DG holonomy are blocked; pure symbolic algebra is fine.

Banked (do not redo): `Jac(Bring) ~ E⁴` isotypic, H¹(Bring)=std A₅-irreducible
(#2701); color `E_q` = descartes `E_q`, j(q₀)≈129.86; `tr B = 2.6424 ∉ ℤ` ⇒
B is the abelianised λ_SW holonomy (`SL₂(ℝ)`, τ=2cosh θ, θ≈0.78145), **not** the
topological Picard–Fuchs monodromy.

Actionable (non-gated, symbolic):
- [ ] **(b-3)** Derive the symbolic Picard–Fuchs q-difference operator for color
  `E_q: y²=x³+p(q)x+r(q)` (reuse `lever1_color_eq_monodromy_integrality.py:38–89`
  + `bring_picard_fuchs_kernel.py:36–61`). Report the actual period-monodromy
  trace (expected integer `SL₂(ℤ)`); confirm it ≠ 2.6424, re-isolating τ to the
  owner-gated holonomy. *Confirmatory, bounded.*
- [ ] **(a-2)** Document the S₄-invariant fixed-field structure of K(Bring)
  (symbolic) to unblock an algebraic `j(Bring/S₄)` — lower priority.

Owner-gated (record, do not attempt): (a-4) q-family `E(q)` `tr M(q₀)`;
(b-4) abelianised λ_SW connection holonomy reproducing θ≈0.7815.

### Front 2 — Lever-1 (record, do not re-search)
- [x] Reproduced τ(q₀)=2.6423863133015 against the banked witness (toolchain check).
- [ ] Record the deconfliction (this doc); no new kernel-class search.

## Discipline gates (standing)
- Exploratory probes only; no production promotion without q-locality (<10² ppm/q) + 13-driver cite + Rule-14 escalation.
- Formalize-first before any wide numerical search.
- Δ_λ: no 7th fit-based ansatz (six failed; A=4 interface operator + s5-so3 fibre action are the sanctioned directions).
- Owner-gated: the geometric `tr B` / Gauss–Manin monodromy build (narrow Subgoal-2 reversal covers only the s5-so3 keystone DG construction).
