# Workplan: canonical braid-word notation migration

**Date**: 2026-05-23
**Trigger**: owner directive — *"NO MORE: referring to nucleotide
and particles and such w/ using the full description. including
things like `⋈_knot`."*

## Problem

The codebase uses informal nucleon labels (`'p'`, `'n'`,
"proton", "neutron") as shorthand for the canonical braid
representations `𝓑_p`, `𝓑_n ∈ H_3(q)`.  This:

1. **Loses the knot-operator structure** — the string `'p'` carries
   no algebraic information; the actual object is a specific Hecke
   element in `H_3(q)` with a known σ-word decomposition.
2. **Makes Lean formalization incomplete** — `AtomicMass.lean` has
   `protonMass : ℝ` as a literal, not derived from `tr_M(𝓑_p, q_0)`.
3. **Obscures the interface knot** `⋈_K` — inter-nucleon crossings
   are just `(c, d)` tuples in Python, not named algebraic objects.
4. **Conflates physical intuition with mathematical structure** —
   "proton" is a physics label; `𝓑_p` is a precise Hecke element.

## Canonical objects (the "full description")

| informal | canonical | definition |
|----------|-----------|------------|
| proton | `𝓑_p` | confined H_3(q) braid: `σ_0^7 σ_1^4` (or per `_PROTON_G0/_G1` in `hecke_core.py`) |
| neutron | `𝓑_n` | confined H_3(q) braid: `σ_0^6 σ_1^4 σ_0^{-1}` (or per `_NEUTRON_G0/_G1`) |
| pp crossing | `⋈_K^{pp}` | `σ_{3k+2}` (positive crossing) |
| nn crossing | `⋈_K^{nn}` | `σ_{3k+2}^{-1}` (negative crossing) |
| pn crossing | `⋈_K^{pn}` | `(σ_{3k+2} + σ_{3k+2}^{-1})/2` (averaged) |
| atomic braid | `𝓑_K` | `∏_{k=0}^{A-1} 𝓑_{nuc_k} · ∏_i ⋈_K^{type_i}` |

## Scope assessment

### Python compute (87 scripts)

- `mass_at_3A_proper.py:267` — `ordering = ['p'] * Z + ['n'] * N`
  is the root of the informal pattern. All 87 callers of
  `atom_braid_word_3A` inherit the string-label convention.
- `hecke_core.py` — defines `_PROTON_G0`, `_NEUTRON_G0` etc. as
  the actual braid-word patterns. These ARE the canonical objects,
  just named with informal English labels.

**Fix**: rename `_PROTON_G0` → `_BRAID_P_G0` (or
`CONFINED_BRAID_PROTON_G0`) and add a module-level docstring
mapping to the canonical notation `𝓑_p`. The `ordering` list
can stay as `['p'] * Z + ['n'] * N` internally (it's a dispatch
key, not a mathematical object), but the DOCUMENTATION at every
use site should reference `𝓑_p` / `𝓑_n` / `⋈_K^{type}`.

### Content (.md + .ts) — 339 files

- 136 files already use `𝓑_p` / `𝓑_n` notation ✓
- ~200 files use "proton" / "neutron" without braid backing
- Many of these are in remarks, examples, and prose blocks where
  the braid structure isn't the primary topic

**Fix phases**:
1. **Phase A** (high-value): definitions, theorems, propositions
   that state results ABOUT proton/neutron mass — must reference
   `𝓑_p` / `𝓑_n` explicitly.  ~30-50 blocks.
2. **Phase B** (medium): remarks and examples that discuss
   nucleon-specific structure.  ~100 blocks.
3. **Phase C** (low): prose transitions and motivational text
   where "proton" is used in a non-mathematical context.  ~100
   blocks. These may be acceptable with a `\refterm{proton}{#proton}`
   link to the glossary term.

### Lean formalization — 10+ files

Currently:
- `AtomicMass.lean` has `protonMass : ℝ` as a pinned literal
- `Interactions.lean` has `ProtonTrefoilSign` (sign analysis)
- No `def protonBraid : HeckeElement H_3` exists
- No `def interfaceKnot : HeckeElement H_{3A}` exists

**Fix**:
1. Define `protonBraid : HeckeElement (H 3 q)` (or equivalent
   algebraic structure) from the σ-word decomposition.
2. Define `neutronBraid : HeckeElement (H 3 q)`.
3. Define `interfaceKnot : Species → Species → HeckeElement`
   parametrized by the species pair.
4. Derive `atomicBraid : (Z : ℕ) → (N : ℕ) → HeckeElement
   (H (3*(Z+N)) q)` from the composition.
5. `protonMass` becomes
   `|tr_M(protonBraid, q_0)| · E_0 · ρ · Vol(𝓑_3) / ℏ_q²`
   (the full categorical chain, not a literal).

**Effort**: ~2-4 weeks for steps 1-5. Step 5 depends on the
full `tr_M` formalization (currently has `sorry`s).

## Proposed execution order

| phase | scope | effort | priority |
|-------|-------|--------|----------|
| **0** | Rename `_PROTON_G0` → `_BRAID_P_G0` + docstring `𝓑_p` everywhere in `hecke_core.py` + `mass_at_3A_proper.py` | 2 hr | immediate |
| **A** | Content blocks: provable-kind blocks that state nucleon-mass results must reference `𝓑_p`/`𝓑_n` | 1-2 days | high |
| **B** | Content blocks: remarks + examples | 2-3 days | medium |
| **C** | Lean: define `protonBraid`, `neutronBraid`, `interfaceKnot` | 1-2 weeks | high (structural) |
| **D** | Lean: derive `protonMass` from the categorical chain | 2-4 weeks | research-grade |
| **E** | Content prose: `\refterm` links for informal "proton"/"neutron" | 1 day | low |

## Open questions for the owner

1. **Scope of "NO MORE"**: does this apply to ALL 339 .md files,
   or just provable-kind blocks (definitions/theorems/etc.)?
   Prose like "the proton is a baryon" may be acceptable without
   `𝓑_p` backing.
2. **Rename vs alias**: should `_PROTON_G0` be renamed outright
   (breaking 87 callers) or aliased (`_BRAID_P_G0 = _PROTON_G0`)?
3. **Lean priority**: should the Lean formalization of `protonBraid`
   block Phase A/B content work, or proceed in parallel?

## Cross-references

- `computations/mass_at_3A_proper.py:267` — root
  of the informal pattern
- `computations/substrate/hecke_core.py` — canonical braid
  word definitions (`_PROTON_G0`, etc.)
- `computations/closed_form_tau_M.py` — Phase 5q
  closed form (already uses `𝓑_p` / `𝓑_n` notation)
- `content/quantum-observable-universe/lean/QOU/AtomicMass.lean` —
  current Lean nucleon typing
- `docs/canonical-derivation-cheat-sheet.md §2` — canonical chain
