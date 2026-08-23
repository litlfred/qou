---
# qou-8fl1
title: 'Eightfold chapter: Lean + QA coverage gap after the honesty pass'
status: todo
type: task
priority: normal
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-23T07:44:35Z
---

## Context

Honesty pass landed (see the `content(eightfold)` commit). Overclaims withdrawn,
four wrong meson weight rows fixed, corner-label error fixed, invalid Hurwitz
inference withdrawn. What remains is coverage, not accuracy.

## Open items

1. **QA sidecars.** 11 `.qa.json` files carrying `"criteria": {}` were removed —
   zero criteria had ever been evaluated, but populated `source_hashes` made the
   staleness check report them current, so they actively suppressed QA. The
   chapter now has **no** sidecar coverage. Needs a real `qa-sweep` run, which
   needs the `folio-assistant` pipeline
   (`scripts/setup-folio-assistant.sh`) — not available in the sandbox this pass.
   Same defect still live in `appendix-standard-model/strand-twist-datum.qa.json`
   and 6 `section-title-audit.qa.json` files across 5 papers.

2. **Lean coverage.** Three `proposition` blocks have no Lean backing:
   `prop:schur-weyl-eightfold` (ref removed — pointed at a module proving a
   different statement), `prop:meson-octet-decomposition`,
   `prop:borromean-decuplet`. Under AGENTS.md these warn rather than fail, but a
   proposition chapter with 1 real Lean module is thin.

3. **`Sym2Gate.lean` is vacuous.** Its declarations reduce to
   `6 = 6 ∧ 0 = 0` and `1 + 5 = 6 ∧ 1 > 0` — arithmetic tautologies whose
   representation-theoretic content lives in the *statement names*, not the
   proofs. Under "Strict Lean Discipline" item 5 this is a review failure. The
   prose now says "not excluded by the Sym² gate" rather than "passed", but the
   file should either encode a real decomposition claim or be demoted.

4. **`WeylInvarianceQDeformation.lean` hygiene.** Now that the `lean:` refs
   resolve (they were bare strings, so the schema rejected them and the §7c
   checker never ran), `qa-sweep` reports `wall-base-ring-minimal` **warn** on
   `prop:a2-from-three-strands` and `rem:q-deformation-weight-lattice`. The ℚ in
   `root_angle_ratio_A2` is defensible — an exact rational ratio, and notably
   *not* ℝ — but two declarations close with `native_decide`
   (`cartan_A2_offdiag`, `serre_exponent_A2`, `root_angle_ratio_A2`) on goals
   that are concrete finite matrix lookups. `decide`/`norm_num`/`rfl` would do,
   and AGENTS.md "Strict Lean Discipline" item 6 discourages `native_decide`.
   Low risk, but it is kernel-evaluator use where none is needed.

5. **No `def:octonion-algebra` anywhere in the corpus.** §5 uses the octonions
   and `G_2 = Aut(𝕆)` throughout but neither is defined as a content block. The
   dangling `uses: ["def:octonion-algebra"]` on `color-su3-from-g2.ts` was
   removed (it never resolved) and the gap recorded in the §8 ledger. Either
   author the definition or keep citing the literature explicitly.

6. **Chapter `.ts` TODOs** (3, all research-gated): `a2-root-system-proof` +
   `hexagonal-weight-lattice` (§1), `color-tube-coords-intro` (§5),
   `thurston-relaxation` (§6).

7. **New open problems added to §8** and needing owners: the
   spin–flavour–colour selection rule (the decuplet identification currently
   matches dimensions and weights only), and Gell-Mann–Okubo (asserted as a
   consequence, not derived; the one cross-check gives ≈6% vs ≈3.3%).

---

**2026-08-08 update (PR #4727).** Item 4 is **discharged**, and it was the
smallest of four defects in that file. Opening it to fix the `native_decide`
found three more that this bean did not catch:

- **The file did not compile.** Two `error: No goals to be solved` (dead `ring`
  and dead `native_decide` after a closing `simp`) — red on `main` since it
  landed.
- **`cartanMatrix_A2_q_independent` was `cartanMatrix_A2 = cartanMatrix_A2 :=
  rfl`** — a tautology with unused `R, q₁, q₂` binders, cited in three `.md`
  places as proving q-independence. AGENTS.md §"Strict Lean Discipline" item 5.
- **`qSerre_neq_cartan_diag` assumed its conclusion** — hypothesis `q² + 1 ≠ 2q`
  is definitionally the conclusion.

All four repaired: `lean`-direct **exit 0**, sorry-free, axioms
`{propext, Quot.sound, Classical.choice}`. The contentful half of the
separation (`qSerre_not_constant`, witnessed at q = 2) was added, since
constancy of the Cartan datum is true by construction and carries nothing
alone. The `.md`/`.ts` over-claims were corrected to say the q-independence is
**standard** (Lusztig/Kashiwara), cited and not formalised here. Audit:
`docs/audits/2026-08-08-weyl-invariance-file-repair.md`.

Item 3 (`Sym2Gate.lean` vacuous) still stands — it compiles, and the chapter
prose already labels it honestly, so it is correctly-labelled rather than
misleading. The generalised sweep is bean `qou-k448`.



## Item 3 detail (added 2026-08-22, folded from redundant qou-v4ns)

WHY Sym2Gate.lean item 3 stays a gap rather than 'just not done': the real
claim (SU(3) fundamental 𝟑 is complex type, 𝟑̄≠𝟑 ⇒ Sym²(𝟑)=𝟔 irreducible ⇒
passes the gate) is currently UNSTATABLE faithfully — Mathlib has no
SU(3)/Frobenius-Schur-indicator/complex-type machinery to phrase it over
genuine rep objects. So su3_sym2_irreducible : True is not laziness; it is a
Mathlib gap. The SU(2) side IS formalized next door (Sym2GateParity.lean:
zero_mem_sym2Indices_iff, adjoint_fails_gate) and carries the load-bearing
physics; Sym2Gate's decls are the SU(3) complement.

Resolution options: (a) build minimal SU(3)-fundamental + FS-indicator infra to
state+prove Sym²(𝟑) irreducible; or (b) if never needed downstream, remove the
content-free axiom su3_sym2_irreducible and restate octonion_3_passes_sym2_gate
(6=6∧0=0) to a real dim claim tied to sym2_dim_3. Ref: [fulton-harris1991] §11;
FS indicator (-1)^{2j}. (Both decls are advisory in the vacuity ledger; the
file docstring already documents the vacuity honestly.)



## ═══ TIERED WORKPLAN (2026-08-23) ═══

The 7 open items, ordered by tractability. (Item 4 already discharged, PR #4727.)

**T1 — Lean coverage for the 3 backing-free props [item 2, tractable-first].**
  prop:meson-octet-decomposition, prop:borromean-decuplet, prop:schur-weyl-eightfold.
  ASSESS each: if the claim is dimension-count arithmetic (like sym2_dim_3:
  3·4/2=6), it is a real decidable lemma — author it. If it needs genuine SU(3)
  rep decomposition (Clebsch-Gordan 3⊗3̄=8⊕1, 3⊗3⊗3=10⊕8⊕8⊕1), that part is a
  Mathlib gap → state the dimension shadow + bean the rep-level claim. Do NOT
  fake a decomposition proof.

**T2 — Sym2Gate SU(3)/Frobenius-Schur [item 3, hard Mathlib gap].**
  su3_sym2_irreducible : True + octonion_3_passes (6=6∧0=0). Needs SU(3)
  fundamental + FS-indicator (-1)^{2j} / complex-type infra, thin in Mathlib.
  Options: (a) build minimal SU(3)+FS infra (large); (b) if unused downstream,
  remove the content-free axiom + restate octonion_3_passes to a real dim claim
  tied to sym2_dim_3. Ref [fulton-harris1991] §11. Sub-bean candidate.

**T3 — def:octonion-algebra [item 5, definition].**
  §5 uses 𝕆 and G_2=Aut(𝕆) with no content block. Either author the definition
  (a genuine algebraic structure — Mathlib has no octonions; sizeable) or keep
  explicit literature citation. Lower priority; decide author-vs-cite.

**T4 — QA sidecars [item 1, pipeline-gated].**
  11 empty-criteria .qa.json removed ⇒ chapter has no sidecar coverage. Needs
  qa-sweep via folio-assistant pipeline (scripts/setup-folio-assistant.sh) —
  run when the pipeline is available; also the same defect in
  appendix-standard-model/strand-twist-datum.qa.json + 6 section-title-audit
  sidecars across 5 papers.

**Research-gated [items 6, 7 — NOT session-closeable].**
  §1/§5/§6 .ts TODOs (a2-root-system-proof, hexagonal-weight-lattice,
  color-tube-coords-intro, thurston-relaxation); spin-flavour-colour selection
  rule; Gell-Mann-Okubo (asserted not derived; ≈6% vs ≈3.3% cross-check). These
  are open physics/math, not formalization bookkeeping — leave beaned.
