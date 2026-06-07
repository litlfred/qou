# Binding-link assignment is heuristic/survey, not SDP-derived

**Status:** GAP AUDIT (discipline). The per-isotope binding-link assignment
(²H→Hopf, ³H→8₁₁, ³He/⁴He→L6a4/Borromean) is a **hidden input** — chosen by
the Borromean-nuclei ↔ Borromean-rings topological analogy and labelled
"heuristic" in the code — **not** an output of the operator-selection SDP/LP,
despite "SDP" appearing in the file/registry names. This records it so the
choice is auditable.

## Evidence

- **`binding_k_solver.py`** hardcodes the link + braid word per atom:
  `"knot_name": "L6a4"`, `"atom_braid_word": [-1,2,-1,2,-1,2]` (L6a4 via
  SnapPy, line 130). The link is an **input**.
- Its own docstring (line 8): *"Earlier drafts called this an 'SDP solver';
  per Copilot's PR #614 [renamed]"* — explicitly **de-labelled as an SDP**
  because it does not select the link.
- Lines 414–431 label the binding-K words **"heuristic"** repeatedly:
  *"³He: K = σ₃σ₆ (two Hopf bindings … — heuristic)"*, *"³H … 8₁₁-class —
  heuristic, deferred"*, *"heuristic word approximations"*,
  `"K_word": [3, 6]  # heuristic: 2 Hopfs`.
- **`binding_k_enumerator.py`** calls them `"binding_link_known"` /
  `"… (heuristic)"`.
- The AME binding (`B_AME_MeV`) sits **in the solver input dicts** alongside
  the assumed link.

## What the SDP/LP actually does

PSD-feasibility of the per-block linking matrix `ρ_λ(K)` + per-block
operator-selection (Wedderburn-channel shadow prices, the `lp_dual_solver`)
**within** the pre-assigned link — not selection **of** the link. The "SDP
registry" label in `binding_link_volumes.py` is historical; the registry
holds hand-assigned links validated by PSD-feasibility + SnapPy volume.

## Classification

- **Not** a continuous CAL-4 fit (no constant tuned to AME).
- **Is** a discrete topological hidden input: *which* knot/link per isotope,
  currently fixed by physical analogy + topological matching, not derived
  from the substrate.
- This is the **"atom→knot assignment"** gate — listed as the open input of
  Path C (Kashaev volume law) in
  [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
  (alongside ρ_F). Same obstruction family as Δ_λ and the EM-linking length
  scale.

## Consequence

Any result that scales with `Vol(K_bind)` or the link's cusp geometry
inherits this gap. In particular the proposed **EM-linking Coulomb factor
`3/4 = L6a4 cusp-geometry ratio`**
([`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md),
PR #1777) only pushes the question back to *"why L6a4 for ³He?"* — which is
itself a heuristic. So that derivation is not clean until the atom→knot
assignment is derived from the substrate (the productive direction: derive
the binding link as the SDP-selected link from a candidate census **without**
AME in the selection objective — currently the link is assumed, not selected).

## Internal inconsistency (why this matters)

The heuristic isn't even self-consistent for ³He:

- The **canonical atomic braid** (`atom_braid_word_3A`) is a **CHAIN** — A−1
  *adjacent* interfaces (1-2, 2-3), no 1-3 — so its closure is a **chain of
  two Hopf links**, not a Borromean link (Borromean requires *all-pairs*
  mutual linking, which a chain lacks).
- `binding_k_solver.py` agrees with the chain: `"K_word": [3, 6]` =
  *"two Hopf bindings (3-4 and 6-7) — heuristic"* (line 414, 431).
- But `binding_link_volumes.py` assigns ³He → **L6a4 = Borromean**
  (`Vol = 8G`), and `binding_k_solver` also carries an L6a4 braid
  `[-1,2,-1,2,-1,2]` (the Borromean 3-braid).

So the *braid* says **two Hopfs (chain)**, the *volume registry* says
**Borromean** — two different links for the same nucleus, both labelled
heuristic. The Borromean choice is the physically-apt analogy (Borromean
nuclei); the chain is what the canonical braid actually closes to. They are
**not the same link** (`Vol(2 Hopfs) = 0` vs `Vol(Borromean) = 8G`), so this
is load-bearing — the +5.87 % magic-A / per-isotope binding leans on the 8G
volume, which the canonical chain braid does **not** produce.

## Recommendation

- Relabel the "SDP registry" / "SDP solver" naming to "heuristic link
  registry (PSD-validated)" to stop implying a derivation that isn't there
  (the rename was begun in PR #614 but the witness/registry names persist).
- File the atom→knot assignment as an explicit open gate in the binding
  status, at the same tier as Δ_λ.
