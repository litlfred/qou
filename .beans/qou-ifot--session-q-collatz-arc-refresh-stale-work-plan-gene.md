---
# qou-ifot
title: 'Session: q-Collatz arc — refresh stale work plan, general-word cycle forcing'
status: completed
type: milestone
priority: normal
created_at: 2026-08-29T16:28:38Z
updated_at: 2026-09-08T07:45:46Z
---

TURN 1 (2026-08-29). Reviewed the arc against main -- main's collatz substance is IDENTICAL to the working tree (only .qa.json sidecar churn differs on those paths), so 'lots landed on main' is true corpus-wide but did not move this arc. What HAD moved is the arc's own record: six beans listed as open work that had already landed. Refreshed all six (commit 4c8d75a98a) and opened + landed the successor chip qou-rcgi (commit 13d3d51bbb, PR #6042).

LIVE q-COLLATZ GAPS after this turn, in the order I would attack them:
1. C12 (largest unformalized): rem:collatz-three-forms states the Markov-trace convergence tr_M(C_q^k(h)) -> 1 over H_n(q) in PROSE and its .ts carries NO lean ref at all. Tractable to at least state.
2. qou-4atn: does v_[2] descend on D_infty? Blocker cleared. Honest ceiling: a global descent measure there CLOSES q-Collatz-on-a-QOU via reaches_cycle_of_descent_domainStable, so expect a wall, and the useful move is a D_infty counterexample rather than a proof.
3. C11 residual: the contact-boundary iff stays conditional on the kappa_0 = chi(A) trace-gap input inherited from QouObstructionReductionContext -- now a named, single, finite target rather than a diffuse 'conditional'.
4. Multi-window generalisation of qou-rcgi (see that bean).
5. The general word / q-Steiner. Open, and open classically; do not expect to close it.

TURN 3. Two more items landed. qcz15 C12: rem:collatz-three-forms now has a Lean carrier (commit d09d3357e7), and it surfaced a live overclaim -- QOU.Substrate.contact_threshold_lt_two announced '1 < v* < 2' while proving only the upper half, with the lower half absent corpus-wide; both fixed (876f70faa3). qou-4atn: SETTLED NEGATIVE (105465b558) -- v_[2] does not descend on D_inf, structurally, and the general obstruction (any N-valued descent measure is positive off the target) is the reusable part.

REVISED live gap order for the arc:
1. Find a descent measure for D_inf that is NOT a valuation. qou-4atn's descent_measure_pos_off_target now constrains the search: mu must be strictly positive at every non-attractor point, which kills every [k]_q-adic valuation at once. A height (degree, L1 coefficient norm) is the natural next family. NOTE the honest ceiling is unchanged: a working mu CLOSES q-Collatz-on-a-QOU, so this is not expected to close cheaply.
2. C11 residual: the kappa_0 = chi(A) trace-gap input inherited from QouObstructionReductionContext -- a single named finite target.
3. Multi-window generalisation of the general-word forcing (qou-rcgi).
4. Wire the arc's library .lean files to content blocks as a class -- needs the folio-assistant pipeline, absent in this container.
5. The general word / q-Steiner. Open, and open classically.

TURN 6-7. Landed: orbit-level compositions (qou-rcgi follow-on list now empty), and then the arc's most useful negative -- qou-n3xf, which MEASURES the height criterion's coverage over all 2^k words (k<=18) and then PROVES the criterion is empty at the critical ratio. That bounds the entire height approach: no extension of it can reach cycle candidates.

ARC STATUS. Nothing bounded remains. The three open items are all research and all now sharply stated:
1. An invariant surviving at 2^k ~ 3^m (the cycle question). qou-n3xf says the q=1 height is not it, and says why.
2. A non-valuation descent measure on D_inf (the convergence question). qou-4atn says no valuation is it, and says why -- descent_measure_pos_off_target forces strict positivity off the attractor.
3. The Connes / Hattori-Stallings computation for C11 (qou-7kfp localised it to one equation).
Each of the three now has a proved statement of what will NOT work, which is the durable product of this session.

TURN 8 -- verification debt CLOSED, and a self-correction. Twice in this PR I wrote that a docstring edit was 'an argument, not a machine check' because the QOU cone had no oleans. Both files are now machine-verified (commit 11613e241c).

SELF-CORRECTION: collatz_contact_boundary.lean does NOT import 'the QOU cone' as I claimed. It imports exactly ONE module (qou_obstruction_reduction) whose olean I had already built for C11. It was verifiable the entire time -- I inferred the difficulty from the file's location instead of reading its imports. That is the same class of error this session has been correcting in the corpus, made by me, in this PR's own commit messages.

For the genuinely deep file (QOU/QCollatz.lean -- cone reaches QOU.Mass.*, Glossary, BraidKnot) I restored lake-cache/qou-v4-24-0 (3407 mathlib + 2275 QOU oleans) into a SEPARATE directory rather than over the working .lake, so a bad tarball could not cost the Mathlib oleans the session depends on. No lake build at any point, so nothing evicted (the AGENTS.md eviction footgun avoided by construction). Exit 0.

NEW RESULT enabled by having the real cone: collatz_three_forms_bridge.lean proves the correspondence collatz_three_forms.lean had only ASSERTED -- contactThreshold_eq_qInt (the 7c-generic form IS the library's qInt form), qInt_contactThreshold_mem_Ioo (the two-sided 1 < v* < 2 in the library's own terms), agrees_with_landed (the landed one-sided theorem is recovered, so the developments are consistent rather than parallel). All exit 0 against the real cone, axioms clean.

OPERATIONAL NOTE for the next agent: the AGENTS.md LEAN_PATH overlay trap is real and bit here. Lean resolves a module by the FIRST LEAN_PATH root owning the namespace and does NOT fall through, so a freshly-built QOU olean placed in a second root is invisible -- it must be copied into the restored root itself. Cost me one 5-minute cycle.

Session complete. PR litlfred/qou#6042 MERGED 2026-08-30T09:18:32Z (head c669b225e3, 36 files, +4236/-13, 33 commits, twelve tranches).

Durable results:
- v=0 for the backward TREE is CLOSED (tranche 11, beans qou-btil + qou-ky5e). The Eisenstein norm is the invariant: N(w+1)=1 so the even branch-inverse preserves it; an odd-preimage forces P(w)=-w of norm 1; every k>=1 branch sits at N = 1+6k+12k^2 >= 19. Each branch is a bare even chain, so no two odd-preimages ever chain. This also EXPLAINS the observed mod-6 congruence: alpha = w+1 is a unit of order 6.
- Four routes settled NEGATIVELY, which is the more useful half: no valuation can be a descent measure (tranche 3; block descent does not rescue it, tranche 8); the q=1 height criterion is provably empty at the critical ratio (tranche 6); C11 needs a real Hochschild computation and the two literature inputs provably cannot reach it (tranche 4).
- A live overclaim fixed: contact_threshold_lt_two was titled '1 < v* < 2' but proved only the upper half; the lower half existed nowhere in the corpus and is now proved.
- scripts/lean-olean-staleness-check.py (tranche 12, bean qou-ruo1).

STILL OPEN: v=0 across all of D_inf, which is equivalent to the convergence conjecture (qcz7 A1). No bounded chip remains in this arc.

## 2026-09-08: twin qou-wxg1 (identical title, duplicate session milestone, completed) cross-referenced; this bean is the record. Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 6 / §7.3 C7.
