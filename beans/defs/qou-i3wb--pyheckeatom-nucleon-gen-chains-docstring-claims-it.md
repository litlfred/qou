---
# qou-i3wb
title: 'pyhecke.atom: nucleon_gen_chains'' docstring claims it matches build_nucleon_nf, and it does not'
status: in-progress
pr: 8290
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T18:28:14Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---

Sibling of `qou-bg3w` (which element is Delta) but NOT the same question, and
this one does not wait on the owner. `bg3w` decides which nucleon element is
canonical physics. This is a defect in the code that is true whichever way
`bg3w` goes: one builder's docstring asserts agreement with a builder it
demonstrably disagrees with.

## The contradiction, measured

`computations/qbeta/nucleon_builder_dressing_contradiction_probe.py` (7/7,
structural — counts crossings and compares templates, no arithmetic on q):

| builder | crossings | dressing |
|---|---|---|
| `build_nucleon_nf(['u','u','d'])` | **9** (B3 = 3x(sigma_0, sigma_1^-1) = 6, + 3 quark pairs) | none |
| `nucleon_gen_chains(['u','u','d'])` | **11** (g0 7 + g1 4) | +2 sigma_0 |

The two extra are appended literally, at `tools/pyhecke/python/pyhecke/atom.py`
(end of `nucleon_gen_chains`):

    # Gluon self-coupling: 2 sigma_0 per nucleon (ILP-derived)
    g0.append((1, 0))
    g0.append((1, 0))

And the two docstrings assert opposite things about exactly that:

* `nucleon_gen_chains`: "Derives chains from the quark content, **matching
  build_nucleon_nf**".
* `build_nucleon_nf`: "**No separate gluon dressing** -- B_3 IS the gluon
  structure."

Both cannot hold. They are different elements of H_3(q), and H_3 is not
commutative across generators, so this is not a re-ordering.

## Why it is not cosmetic — consumers split on it

"The nucleon" resolves to one of two inequivalent elements depending on which
name a caller reached for, while the docstring tells the reader the choice does
not matter:

* **9-crossing, undressed** via `PROTON_NF` / `NEUTRON_NF`:
  `computations/hecke_core_legacy.py`, `computations/atom_mass_derived.py`,
  `computations/substrate/hecke_core.py`, `pyhecke/__init__.py`, plus four
  `computations/qbeta/*` probes.
* **11-crossing, dressed** via `_PROTON_G0` / `_PROTON_G1` /
  `nucleon_gen_chains`: `computations/binding_canonical.py`,
  `computations/closed_form_tau_M.py` (mirrored into `qou-mass/_internal/`),
  `computations/tr_m_algebraic_q.py`,
  `computations/binding_threebody_joint_trace.py`,
  `computations/terms_2_3_atom_per_gen_mpfr_50dps.py`, `pyhecke/tower.py`,
  `pyhecke/undo.py`.

Both lists contain load-bearing producers, on both sides.

## What this bean does NOT claim

It does not say which builder is right. The dressing is annotated
"ILP-derived", so it may well be the intended physics and `build_nucleon_nf`
the stale one. That is `bg3w`'s question and an owner decision. **The docstring
claim is wrong either way**, and it is what makes the divergence invisible to a
reader checking whether two call sites agree.

## Fix

Cheapest correct move is documentation, not code: strike "matching
build_nucleon_nf" from `nucleon_gen_chains` and say what it actually does
(B3 + quark pairs + 2 sigma_0 ILP gluon self-coupling, 11 crossings), and have
`build_nucleon_nf`'s docstring name the other builder as the dressed variant.
Do NOT "fix" either builder to match the other before `bg3w` is decided --
that would silently move numbers in every producer listed above.

## Progress 2026-11-17 (PR #8290)

Updated `nucleon_gen_chains` and `build_nucleon_nf` docstrings in `tools/pyhecke/python/pyhecke/atom.py` on PR #8290 (`1c907342f24ac048c99eb24f30832b0b87b024b0`) to state the ordering distinction between `nucleon_gen_chains` (per-generator partitioned `(g0_chain, g1_chain)` of lengths `(7, 4)`, matching `grouped_word_from_chains`) and `build_nucleon_nf` / `nucleon_braid_word` (alternating `(sigma_0 sigma_1^-1)^3` Borromean braid order).

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

Still open on main: `tools/pyhecke/python/pyhecke/atom.py` `nucleon_gen_chains` docstring at `2ae54ab401` still says "matching build_nucleon_nf". The docstring fix is on open PR #8290 (not merged). Not duplicated here.
