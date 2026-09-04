# lean-verifier — session log

One entry per session: **what you verified, by what method, and any entry you
confirmed or corrected.** Newest last.

**Prune the log, never the TRAPs.** A lesson worth keeping belongs in
`MEMORY.md` or a sibling as a TRAP; the log is only the trail. When an entry's
lesson has been promoted, collapse the entry to one line.

> Pruned 2026-09-03 (08-29 → 09-03 collapsed) and **de-duplicated 2026-09-04** —
> the log had grown to ~120 lines with five sessions recorded twice in long and
> short form, which is how a 200-line budget gets spent on nothing.

**std-3** below means `#print axioms` returned exactly
`[propext, Classical.choice, Quot.sound]` — the clean result, no `sorryAx`.

---

- **2026-08-29 (cool-johnson)** — Orphan-branch restore WORKS; the blocked host
  is Azure blob `lakecache.blob.core.windows.net`, which the restore never uses.
  Confirmed the cold-cache and sidecar TRAPs.

- **2026-08-30 (torus-knots)** — `QOU/Interactions/EmCouplingBarParity.lean`
  lean-direct exit 0, std-3 axioms. Restored `lake-cache/qou-v4-24-0` fresh:
  **3407** mathlib oleans this seed vs 6990 in the baseline; the cone sufficed.
  One fix: a `/-!` docstring preceded the imports, which Lean rejects.

- **2026-08-30** — `QOU/StandardModel/BrunnianIsotypeExclusion.lean` authored +
  verified, exit 0, std-3, no sorryAx. Restore ran out at ~2.2 G free (QOU lib
  files cut off); mathlib's 3407 sufficed for a Mathlib-only cone.
  `omit [inst] in` must precede the docstring.

- **2026-08-30 (PR #6097)** — Found `QOU/Hecke/WedderburnRankDegeneracy.lean`
  red on `main` for **six days** behind a FALSE GREEN: my own #5710 removed a
  field its instance discharged. Rebuilt the 8-module reverse-import cone,
  all-green after repair; found a second red file the same way
  (`QOU/Mass/QIntegerBarParity.lean`, one stale `open`). Wrote
  `verification-harness.md` with all three traps measured.

- **2026-08-31 (milnor-tl-brick2)** — New `QOU/MassTheory/QuantumTraceTower.lean`
  (Mathlib-only). One fix, not a tactic or statement change:
  `Data.Matrix.Kronecker` → `LinearAlgebra.Matrix.Kronecker`. Exit 0, std-3 on
  all three theorems. Cold-cache TRAP again: 1m16s wall, **5.7s user**.

- **2026-09-02 (qtr-kron-consolidation)** — `QuantumTraceTower.lean` gained its
  first QOU import, so it needed the QOU cone.
  `MarkovTraceMultiplicative.olean` was absent from the restore: built it
  lean-direct first, then rebuilt the target **from current source** to avoid a
  false green, then `#print axioms` against the fresh cone. Exit 0, std-3.
  `/usr/bin/time` is not installed here — use the bash `time` builtin.

- **2026-09-02 (magnus-o6ov)** — `QOU/MassTheory/MagnusHookExteriorPower.lean`
  as-written FAILS: `Finset.sum_powerset_card` does not exist in v4.24.0, and an
  `rw [esymm]` under a binder cannot fire. Both fixed mechanically (see
  `v4-24-0-renames.md`). Aggregator `Mathlib.olean` absent from this partial
  restore, so the literal `import Mathlib` errors — verified via a
  byte-identical-tactics temp copy with narrowed imports. Exit 0, std-3.

- **2026-09-02 (RowCap)** — `QOU/Hecke/RowCap.lean`, 10 theorems.
  `lake build` from ROOT green (3087 jobs), axioms clean on all ten
  (`alt_channel_empty_iff` needs only `propext`). The restore **survived** this
  build — 3470 mathlib oleans still present after — so the eviction TRAP did not
  fire that time; do not read that as a licence. Hit the ROOT-vs-per-paper TRAP
  anyway by not reading this memory first: built in `content/…/lean/`, which
  recompiled Aesop from source while the restored root cache sat unused.
  **Read the memory before touching the build, not after.** Added the `>= 2000`
  skip TRAP.

- **2026-09-03 (magnus gauge-hook)** — `MagnusGaugeCurvatureHookColumn.lean`
  verified AS AUTHORED (no fix), exit 0, zero diagnostics, std-3. All four
  imports have both olean and source in v4.24.0. Cache present in root `.lake`
  (3470 oleans) **without** the `RESTORED-NO-TRACES` marker — absence of the
  marker is not absence of the restore. Disk 2.1 G free: too little for a
  re-restore tarball, so a "restore first" reflex would have failed.

- **2026-09-03 (braid-twist-flip)** — Two content-block `.lean` realising
  trefoil monodromy `S₃ ≅ D₃`, both exit 0, no sorryAx.
  `lean/QOU/BraidTwistFlip.lean`: all 6 decls depend on **no** axioms.
  `braids-and-knots/braid-twist-flip.lean` imports `QOU.Basic`, so I built
  `QOU.Basic.olean` lean-direct first (5 s); 5 decls std-3, `rotation_ne_id`
  (via `decide`) = `[propext, Quot.sound]`. Found the `/tmp` → `ELAN_TOOLCHAIN`
  trap.

- **2026-09-03 (two-nucleon-sign-defect)** — New
  `QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean`. As authored exit 1; four
  mechanical fixes, no statement touched, no sorry (see `v4-24-0-renames.md`
  §4×4 complex matrices). Final exit 0, 8/8 std-3, 0 sorryAx. Cold 3m29s wall /
  **25s user**; warm 8s.

- **2026-09-04 (binding-law extensivity)** — New
  `QOU/Hecke/BindingExtensivity.lean`, 6 decls, exit 0, all std-3. One fix:
  `pow_le_pow_left` → `gcongr`. Cold 1m32s wall / **7.0s user**, warm 4.6s.
  Restored from a **leaked `/tmp/tmp.*`** rather than fetching — see
  `cache-restore-and-disk.md`. Re-derived the ROOT-vs-subproject olean trap from
  scratch because it sat at line 313 of a 498-line memory, outside the injected
  window; that is what prompted this split.
