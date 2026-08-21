# TL-arc Lean infrastructure ledger — proved / conditional / assumed / vacuous

**Status: stub — in progress on `claude/tl-arc-lean-infra-2026-08-21`.**

Scope: classify every declaration under
`content/quantum-observable-universe/lean/QOU/MathlibExt/` (and the
directly-adjacent `QOU/BraidsAndKnots/`, `QOU/Hecke*` trees) that the
Temperley–Lieb / Wenzl-level arc depends on, into

- **PROVED** — real theorem, sorry-free, no conditional class in the signature;
- **CONDITIONAL** — carries a `class` hypothesis (§3b-cond: an *assumption*);
- **ASSUMED** — the declaration IS a `class`/`axiom` with no instance;
- **VACUOUS** — concludes `True` / `X = X` / otherwise content-free (a defect).

Then: the gap list scoped to front 2 (all-`n` corank) and front 3 (discharge
Wenzl 1988 via `TL_n`), and whatever cheap gaps are filled on this branch.

`#print axioms` **cannot see a conditional class** (bean `qou-fpjy`) — an
axiom-clean report does not mean unconditional. Classification below is by
reading signatures.
