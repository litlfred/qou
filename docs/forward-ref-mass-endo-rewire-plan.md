# Forward-ref cluster fix: mass-endomorphism → mass-theory (17 edges)

*Last updated: 2026-05-29 after paper-wide Tier-1 sweep.*

Tracks the disposition of the largest logical-defect cluster surfaced
by [`forward_ref_classifier.py`](../computations/forward_ref_classifier.py)
(see [`forward-ref-logical-analysis.md`](forward-ref-logical-analysis.md)).

## Triage result (read-only inspection)

| Finding | Evidence |
|---------|----------|
| 11 of 12 cluster **source** blocks are Lean-sorry-free | a sorry-free proof that declares a forward `uses[]` edge usually over-declares — the proof compiles without consuming the target ⇒ the edge is a narrative citation, not a logical dependency |
| `prop:mass-endomorphism` is a **genuine conjecture** mislabeled `prop:` | title "Mass endomorphism *conjecture*"; body "**Conjecture (explicit mass endomorphism)**"; Lean `class MassEndomorphism` with unproved `vol_eq` field |
| The conjecture is **not load-bearing** | the block's own prose (§"Scope: convenience target, not load-bearing") states the mass formula `thm:knot-mass-formula-unified` + `prop:mass-endomorphism-tower` "does **not** depend on the closed-form conjecture below" |
| §3b-cond already implemented in Lean | downstream results take `[M : MassEndomorphism R β]` and are proved sorry-free as conditional theorems |

## Disposition rule (per edge)

1. **Over-declared edge → rewire.** Source proof is sorry-free and does
   not actually consume the later target: drop the forward `uses[]`,
   repoint to the *proved* upstream result
   (`prop:mass-endomorphism-tower` / `thm:knot-mass-formula-unified`)
   or express as a narrative forward-pointer.
2. **Genuine conjecture → relabel** `prop:`→`conjecture` (only the
   irreducibly-open blocks — `prop:mass-endomorphism`,
   `prop:rho-k-pair-gen-canonical-form`).
3. **Conditional consumer → keep `prop:`, add §3b-cond banner.** A block
   downstream of a conjecture stays provable, proved modulo the named
   `[conj:C]` Lean class hypothesis + a "conditional on conj:C" banner.

## Edges (17)

Source blocks (sorry-free unless noted):
`prop:mass-endomorphism`, `prop:rho-k-pair-gen-canonical-form`,
`prop:markov-trace-axiomatic-closed-form`,
`prop:tau-M-asymptotic-rep-theory`, `prop:explicit-central-idempotent`,
`prop:homological-shell-condensation`,
`prop:categorical-chain-convergence-mechanisms`,
`prop:atomic-mass-gb-nf`, `prop:categorical-mass-markov`,
`prop:markov-trace-recursive-reducer`,
`prop:q-hecke-seminormal-character-closure`,
`def:qou-motivic-galois-instance` (2 Lean sorries).

## Tier 3 — irreducible foundational forward refs (option-b checked, fails)

Seven cluster edges have a target that the source **genuinely
invokes** (it appears in the source's `.md` derivation and/or `.lean`
proof). For these, dropping the `uses[]` would delete a real
dependency — wrong. The remaining levers are (b) promote the target
to an earlier chapter, or (c) document as irreducible.

**Option (b) was checked per edge and fails for all seven.** Each
`mass-theory` target carries its *own* `uses[]` dependency that also
lives in `mass-theory`, so promoting the target into the
`mass-endomorphism` opener does not remove the forward edge — it
relocates it. The transitive cost confirms this is structural, not
incidental:

| Tier 3 target | later-chapter blocks it drags if promoted |
|---|---:|
| `prop:habiro-residue-sum-equivalence` | 1 |
| `prop:jucys-murphy-central-elements-qou` | 1 |
| `prop:hecke-mass-trace` | 2 |
| `prop:q-beta-categorical-precision-ladder` | 112 |
| `prop:alpha-shift-torus-knot` | 153 |
| `prop:graded-trace-residue-split` | 226 |
| `prop:bring-figure-eight-depth-2-witness` | 282 |

The union is **327 of the 445 blocks** in `mass-theory` — promoting
the Tier 3 targets would dissolve the analysis chapter into the
opener, destroying the deliberate opener/analysis split. Even the two
"drags 1" cases leave a residual forward edge (their single blocker is
itself mid-`mass-theory`).

**Disposition: (c) document as irreducible.** These seven are genuine
foundational forward references — the chapter structure intentionally
*states* the opener/conjecture early and *develops* the trace / Habiro
/ central-idempotent machinery in the analysis chapter. The dependency
direction is real and the placement is by design. They remain counted
as logical defects but are explained here; the cluster's logical-defect
count does not reach zero, which is the correct accounting.

## Second cluster — particle-interactions → mass-theory (11 edges)

Same triage method (MD/LEAN/REV matrix + per-edge read). Disposition:

- **Tier 1 — over-declared (5 dropped):** target in neither prose nor
  Lean, no reverse edge.
  `atomic-braid → def:transfer-matrix-operator`,
  `wigner-su4-from-spin-isospin → atom-knot-mass-derivation`,
  `magic-shell-coupling-kappa → wedderburn-weight-canonical`,
  `t-from-trace-cyclicity → atom-knot-mass-derivation`,
  `universal-ilp-algorithm → q-integer-mass-formula`.
- **Tier 3 — irreducible (6 documented):** target genuinely invoked in
  the source derivation prose, and option-(b) promote is BLOCKED for
  each (every target carries its own `mass-theory` dependency, so a
  promote only relocates the edge).
  `wigner-su4-from-spin-isospin → isospin-from-canonical-bowtie`,
  `confinement-operator-selection → frobenius-gram-matrix`,
  `type-b-folding-cpt → p-from-braid-mirror`,
  `knot-particle-generation → skein-generation`,
  `cemetery-group-emergence → gs-spectral-sum-finite`,
  `geom-universality → geom-yekutieli-alignment`.

## Gate

Re-run the classifier after each disposition; the logical-defect count
must drop monotonically (baseline at branch open: 91; after clusters 1
+ 2 over-declared drops + §3b hygiene + paper-wide Tier-1 sweep: 56).
Regenerate `forward-ref-classification.witness.json`.

## Paper-wide Tier-1 sweep (22 dropped, 4 held back)

After the two mass clusters were dispositioned, a paper-wide sweep
identified 26 more Tier-1 candidates (target absent from source's
.md prose AND .lean proof). Verification flagged 4 as **orphan-risk**:
dropping their edge would leave the target with zero referrers (each
target is real, sorry-free, scholarly content — not abandoned).
Those 4 are held back and documented as Tier-3 (real-but-foundational
structural anchors):

| Source → Target | Why kept |
|---|---|
| `prop:habiro-precision-ladder-equivalence → prop:mass-endomorphism-tower` | only structural anchor for the tower; source builds on the equivalence |
| `def:q-angular-momentum → prop:nuclear-spin-parity` | source .md explicitly discusses spin / parity — implicit real dependency |
| `prop:tau-M-asymptotic-rep-theory → prop:hoefsmit-V21-cos-symmetrization` | source .md discusses Hoefsmit seminormal representation — implicit real dependency |
| `prop:borromean-quark → prop:bn-mtc-action` | only structural anchor for bn-mtc-action's role in quark assembly |

The remaining 22 candidates were dropped (each target retained 1-15
other referrers). Defect count 78→56.
