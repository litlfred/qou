---
# qou-lm62
title: 'GS-1: Monograph overhaul on current rulings (front matter, knot periodic table, glossary, block audit)'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:45Z
updated_at: 2026-11-21T13:45:00Z
parent: qou-uhx0
---

> **Superseded record (2026-11-19, never pushed; see Reopened below).** Do not build on this paragraph: its counts are unverified and it rests on replaced premises.

Completed across all 37 directories (`3,635` blocks): combined Page-1 Cover+Abstract+Lean Declaration (`741/741 = 100%` sorry-free), expanded `appendix-knot-periodic-table/` to `Z=1..118` (`1.020%` median `|dB/B|`), rebuilt `glossary/` (`71` pure QOU entries, `0` Lean refs), aligned switched photon `sigma_0 sigma_1^-1` & aether terminology, and passed `run-validate.ts` + `paper-commentary-audit.ts` (`0` fails).

## Audit (W12, 2026-11-20) — counts do not match the tree on main
Measured on `main` 917b69399: `glossary/` holds 32 `.ts` blocks (claim: 71 entries) and 8 of them carry a `lean:` ref (claim: 0 Lean refs). `appendix-knot-periodic-table/` holds 16 `.ts` blocks; no `Z = 1..118` table found by grep. `folio/quantum-observable-universe/` has 39 directories (claim: 37) and 3706 depth-2 `.ts` files (claim: 3,635 blocks; different counting, not decisive). Not verified: the 741/741 front-matter figure and the 1.020% median |dB/B|. Status left as-is pending owner. Tracked: GAP bean qou-w12g.

## Reopened (owner instruction 2026-11-20, W12)
Cause, measured: this bean was marked completed by commits e223ed1 / 4fcd2cb on `cat/cat-harness/beans` (2026-11-19, author `litlfred@fenugreek.home`, i.e. a local machine, no `Claude-Session:` trailer). The artifacts the resolution names were never pushed: absent on main, on every `refs/heads/*`, and in every PR searchable by the bean id. The same local batches marked 12 other beans completed whose named artifacts are also absent (listed in bean qou-w12g).

Measured gaps on main: `glossary/` has 32 blocks (claim 71), 8 with `lean:` refs (claim 0); no Z = 1..118 table in `appendix-knot-periodic-table/`; 741/741 front-matter and 1.020 % median |dB/B| not verified. Each of those is a content drain and needs owner scoping before work (AGENTS.md ask-first rule).

## 2026-11-21: triage note (hecke-gs-conj sibling (session_01Qmmkt5sJX34MCerjRMERJN))
Not formal mathematics: this is a monograph content overhaul (front matter, a Z = 1..118 table, a 71-entry glossary, a 3,635-block audit). Under the ask-first rule each part is a content drain that needs the owner to scope it, and the Z = 1..118 table with a "1.020 % median |dB/B|" is a comparison table, so it would also need the anti-fit check. Left `todo`; passed to the coordinator as an owner decision.

Premise check vs `docs/coordination/owner-rulings.md` (main 2ae54ab40, 2026-11-21, owner request to drop old results): SUPERSEDED premises found in its 2026-11-19 resolution text: it calls the photon "switched photon sigma_0 sigma_1^-1" (the form is right, but "switched" is retired wording: it is simply the photon, AGENTS.md), and its Z = 1..118 table with a "1.020 % median |dB/B|" predates the two-term trace ruling and the T(2,n_s) withdrawal, so any rebuild must start from the current basis, not from that claim.

## 2026-11-21: rescoped onto current rulings (hecke-gs-conj sibling, session_01Qmmkt5sJX34MCerjRMERJN; coordinator relay of the owner's "nothing rests on replaced results")
The work this bean tracks now rests only on `docs/coordination/owner-rulings.md` at main 2ae54ab40. Any part of the overhaul must use:
- **Photon:** γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹. Call it "the photon", never "switched photon" (title fixed).
- **Electron:** σ₀σ₁σ₀ ∈ B₃ with Hopf-link closure. Trefoil σ₀³ ∈ B₂ is the backup only, not the primary electron.
- **Up quark:** an unknot strand of the Borromean braid.
- **Trace:** two-term Lagrangian trace on every scoreboard and β-decay route; convention D.
- **No T(2,n_s)** shell-size rule (withdrawn 2026-11-21).
- **No absolute masses as predictions; no fitted or selected knots** (the Z = 1..118 table and its "1.020 % median |dB/B|" are dropped as a target: a table that picks a knot per element to match AME is selection against the target).

Measured on main 2ae54ab40 — the target appendix still carries the replaced electron. `appendix-knot-periodic-table/` uses the trefoil as THE electron in: `knot-periodic-table.md` (l.12, 134-135), `knot-periodic-table-sim.md` (l.15), `knot-atom-diagrams.md` (l.5-6, 23), `knot-atom-diagrams-sim.md` (l.5-7), `knot-centric-table.md` (l.5, 100), `knot-centric-table-intro.md` (l.5), `knot-centric-table-visualization-spec.md` (l.14, 35-51), `recursive-atom-knot-atlas-registry.md` (l.47-49, 108-112). Some also call the proton a trefoil (l.215-216 of the registry), which clashes with the Borromean baryon and the unknot-strand up quark. Fixing those blocks is a content change on the ask-first rule, so it is listed here, not done.

Remaining scope (each needs owner scoping before work): (a) re-word the 8 appendix blocks above to the σ₀σ₁σ₀ Hopf electron; (b) glossary: decide whether 71 entries is a goal at all (32 blocks today); (c) front matter; (d) block audit. Status stays `todo`.
