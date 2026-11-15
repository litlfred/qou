---
# qou-voa6
title: 'qou-swiso: the bare Schur-Weyl iso is a surjection at N=2 -- three sites, one in the notation register'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T09:39:58Z
updated_at: 2026-10-04T15:13:39Z
parent: qou-mub3
---

## 2026-09-05 — three `≅` sites fixed, one docstring un-contradicted, and a systemic QA blind spot found by accident

Follow-on from `qou-oots` / PR #6806, which reported these defects and did not fix them.

### Fixed: the bare Schur–Weyl isomorphism (3 sites)

`q`-Schur–Weyl `H_n(q) → End_{U_q sl_N}(V^{⊗n})` is an isomorphism **only when `N ≥ n`**. Below that it is a surjection whose kernel is the span of the `> N`-row blocks. This framework runs at `N = 2` with `n = 3A`, where the image is `TL_n(q)` of dimension `Catalan(n)` against `dim H_n = n!` — kernel `n! − C_n` = 1, 10, 78, 588, 4611, 38890 at n = 3…8. An element of that kernel maps to the **zero** endomorphism, so the identification is not faithful.

| site | change |
|---|---|
| `notation/notation-collisions.md` | `\cong` → `\twoheadrightarrow`, plus the `N ≥ n` caveat and the kernel dimensions; the left-regular map is now marked as the one that is faithful unconditionally |
| `lean/QOU/MassEndomorphism/MassLeftMulEndomorphism.lean` | docstring: the Schur–Weyl sense is **weaker, not sharper**; *"literally an endomorphism"* removed |
| `mass-theory/wenzl-bridge-applicability-qou.lean` | docstring: *"centraliser isomorphism"* → **surjection**, with a note that the inhabitedness witness is unaffected so nothing below the line changes |

All three are **docstring/prose only** — no Lean proof term, no Python code path. The corpus already contradicted them two files away: `TraceBlindSector.lean:11` (`TL_n(q) = End_{U_q(sl₂)}(V^{⊗n})`) and `QSchurWeyl.lean:11` (*"the **image of** the Iwahori–Hecke algebra"*).

### Fixed: `wedderburn_jones_markov.py` contradicting itself inside one function

`:355-359` gave the >2-row vanishing of the 2-variable Schur form as the **reason** to prefer `y_λ` — which only makes sense if `y_λ` does not vanish there. `:385-395`, in the same function, states `y_λ` is *"EXACTLY zero for every λ with ≥ 3 rows"*. The docstring was convention-C-era; the body is D. Corrected, and the live reason to prefer `y_λ` stated instead (it is the Ocneanu weight, normalised `Σ y_λ f^λ = 1`; the 2-variable form is not a Markov weight at all).

Recorded rather than fixed: the `(1^p)` sign-rep contribution that `prop:alpha-shift-torus-knot` calls the pole-order maximizer is **not reachable through this sum under D** — it lies in `ker(H_n ↠ TL_n)` and is zero on the `N = 2` physical space. That is a live question about that proposition.

The producer diff is **provably docstring-only**: `ast.unparse` after stripping docstrings is byte-identical old vs new, so no witness re-run — per AGENTS.md's own rule that a comment-only edit drifts `scriptHash` while the payload cannot move.

### 🛑 Found by accident: 63 unlabelled blocks whose sidecars can never be refreshed

Trying to refresh the one sidecar my prose edit made stale, and failing, exposed this. **`qa-sweep` enumerates blocks by label**; a block whose `.ts` declares no `label:` is silently skipped and its `.qa.json` can never be refreshed by any chapter sweep.

Measured on `folio/quantum-observable-universe`: **3527** labelled blocks, **63** unlabelled, **all 63** carrying a sidecar that cannot be refreshed, **23 already stale**.

The mechanism is measured, not inferred — the notation chapter registers 13 blocks, 11 are labelled, and the sweep reports `blocks: 11`, the two skipped being exactly the two unlabelled.

**And those two are `notation-register` and `notation-collisions`** — the two files AGENTS.md names *authoritative for every mathematical symbol used in the paper*. They have **no QA coverage at all**: no voice sweep, no trap detectors, no `wall-side-correct`, and no `render-math-mode-envelope` — the criterion AGENTS.md introduces as **critical** precisely because the hand-grep for it matches the thing it should catch, with the instruction *"run `qa-sweep … --only render-math-mode-envelope` rather than grepping by hand"*. On these two blocks that instruction cannot be followed.

**Honest cost:** this PR knowingly ships `notation-collisions.qa.json` stale. Verified against `main` that its recorded `md` hash matched before my edit and does not after — so it was current, my edit made it stale, and there is no way to refresh it. It joins the 23.

**Two near-misses, both caught before they became claims.** The first `qa-sweep` invocation returned `criteria: 96, blocks: 0, findings: 0` — **a false green**, 0 findings over 0 blocks, which reads exactly like a pass. And the first diagnosis was *"the block is not registered in its chapter manifest"*, which was **wrong**: it is registered, in its own second section, and the earlier grep output was truncated at the first section's block list. The cause is the missing label.

**Not established:** that adding 63 labels is the right fix. A label emits `\label{}` into the LaTeX and makes the block cross-referenceable, so it is a rendering change and a judgement about authoring convention — the author's call, not a measurement. Most of the 63 are `intro-*`/`outro-*`, for which being unlabelled may be deliberate; arguably the defect is that a sidecar is written at all for a block the sweep cannot reach.

Audit: `docs/audits/2026-09-05-unlabelled-blocks-are-invisible-to-qa.md`.

## 2026-09-07 — the fixes MERGED (#6817); the bean stays open, and here is what is still open

PR #6817 merged onto `main` (rebase, per-commit). All three `≅` sites and the
`wedderburn_jones_markov.py` self-contradiction are fixed and on `main`.

**Strengthened at merge time.** Reviewing what landed on `main` since this
branch's merge base found that a sibling on `qou-cds1` has since PROVED the
surjection, sorry-free, at general index type:

* `heckeToTL_surjective` — `H_n(v^2) ↠ TL_n(δ)` (`f1c3a7603`)
* `heckeTLEquiv` — `TL_n(δ) = H_n(v^2)/⟨U_i U_j U_i − v^2 U_i⟩` (`52be85770`)

both in `QOU/MathlibExt/HeckeToTemperleyLieb.lean`. Both docstrings now cite it,
**with the scope stated** (`b53eff395`): what is proved is the PRESENTATION leg
`H ↠ TL`. The second leg `TL_n(q) = End_{U_q 𝔰𝔩₂}(V^{⊗n})` is *stated* in
`TraceBlindSector.lean:11` and is proved nowhere — verified by grep, not assumed.
**So the Schur–Weyl surjection is NOT closed end to end in Lean.** That gap is
the mathematical remainder of this bean and is why it is not `completed`.

**Also still open — an author decision, not an agent one.** The 63 unlabelled
blocks whose sidecars can never be refreshed. Adding a `label:` emits a
`\label{}` into the LaTeX and makes the block cross-referenceable, so it is a
rendering change and an authoring-convention judgement. Most of the 63 are
`intro-*`/`outro-*`, for which being unlabelled may well be deliberate — in
which case the defect is the opposite one, that a sidecar is written at all for
a block no sweep can reach. Both `notation-register` and `notation-collisions`
are in the 63, so the two blocks AGENTS.md §7aa calls authoritative for every
symbol in the paper have **no QA coverage at all**.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
