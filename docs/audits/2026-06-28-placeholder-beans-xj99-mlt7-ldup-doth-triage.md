# Placeholder beans `xj99` / `mlt7` / `ldup` / `doth` — verified triage (2026-06-28)

**Beans:** `xj99`, `mlt7`, `ldup`, `doth` (the remaining
"Resolve N placeholders/TODOs in `<dir>`" cluster).
**Follow-on to:** [`2026-06-26-lean-placeholder-bean-grep-inflation.md`](2026-06-26-lean-placeholder-bean-grep-inflation.md)
and [`2026-06-28-zslh-mass-theory-placeholder-rescope.md`](2026-06-28-zslh-mass-theory-placeholder-rescope.md).

## Finding — counts are grep-inflated, but (unlike `zslh`) the residual is genuine

The four beans' naive counts are inflated by the same four non-actionable
string classes documented in the 2026-06-26 audit. **But the distinction that
matters here:** after refining, the residual `sorry`s are **genuine cited open
proof-gaps** (`-- Ref: [manuscript]`, AGENTS.md §1) — *not* `zslh`-style §3b
conjecture-instances. They are real backlog (each needs new Mathlib infra or a
manuscript-level proof), just **far smaller** than the naive count and **not a
mechanical drain**. `doth` is a different work-type entirely (bibliography).

| bean | dir (files) | bean-claimed | naive grep | refined | hand-read truth |
|------|-------------|--------------|-----------|---------|-----------------|
| `xj99` | `quantum-observable-universes` (123 `.lean`) | 7 | 22 | **2** | 2 **cited §1 infra-gap** sorries — genuine open |
| `mlt7` | `mass-endomorphism` (40 `.lean`) | 15 | 34 | **6** | 6 **cited** sorries — genuine open |
| `ldup` | `unital-groebner-bases` (UGB) | 29 | 24 | **7** | 7 **cited §1 manuscript** proof-gaps — genuine open (different paper) |
| `doth` | `schema` (`references.ts`) | 25 | 3 | n/a | **bibliography placeholders** (unverified DOIs/editions) — *not* a sorry/grep class |

## Per-bean detail

### `xj99` — 2 genuine cited infra-gap sorries
- `fiber-adjoint-involution.lean:87` — `-- Ref: [manuscript] prop:fiber-adjoint-involution`;
  needs a coadjoint-orbit embedding + antipode-induced involution **not yet in
  `QOU.Basic`**.
- `q-resolvent.lean:67` — explicitly *"queued as a sorry per AGENTS.md §1 rather
  than hidden behind a vacuous `: True`"*; needs `s + δ_q` invertibility /
  coproduct-mate infra **not yet in Mathlib**.

### `mlt7` — 6 genuine cited sorries
Conjectural closed-forms (`conj-qbeta-c-k-closed-forms.lean`), the symbolic
11-matrix Hoefsmit trace evaluation (`chi-v21-hoefsmit-matrix-derivation.lean`,
backed by `probe_per_wedderburn_block_ck.py`), the central-idempotent
cross-checks (`explicit-central-idempotent.lean`, Lagrange interpolation in
`J_1…J_n`), and `qbeta-per-block-chi-closed-forms.lean`. Each is cited; each is
a real proof, not a placeholder.

### `ldup` — 7 genuine cited UGB proof-gaps
All the **termination / existence halves** of the Gröbner–Shirshov and PBW
normal-form theorems (`unital_groebner_decomposition`, `pbw_corollary`,
`s_polynomial_decomposition`, `ugb_pbw_corollary`, `AlgOps`,
`main_theorem_statement`), each `-- Ref: [manuscript] unital-groebner-bases`.
Genuine open manuscript steps in a **separate paper**.

### `doth` — genuine bibliography placeholders (separate work-type)
The `references.ts` `PLACEHOLDER` notes are unverified bibliographic
DOIs/editions (Wenzl 1988a/c, Drinfeld 1985, Habiro 2000, James–Kerber edition),
**already tracked** in
[`2026-06-23-bibliography-doi-verification-doth.md`](2026-06-23-bibliography-doi-verification-doth.md).
This is citation-verification work, not Lean `sorry`/placeholder resolution; the
"25 placeholders/TODOs" grep conflates it with the Lean class.

## Recommendation (owner closes/re-scopes beans per AGENTS.md §4a)

- **Re-scope the *counts*** of `xj99` (→2), `mlt7` (→6), `ldup` (→7) — the naive
  7/15/29 overstate by 3–10×.
- **Do NOT close them** — unlike `zslh` (whose residual was sanctioned §3b
  "do-not-discharge" markers), these residuals are **genuine open proof-gaps**
  that should eventually be proved. Re-characterize them as *"N cited §1
  open proof-gaps requiring new Mathlib/manuscript infra — real backlog, not a
  mechanical drain."*
- **`doth`**: re-scope as **bibliography-verification** work, point it at the
  existing `2026-06-23-bibliography-doi-verification-doth.md` ledger, and drop
  the misleading "placeholders/TODOs" framing.

## Why this matters

The mirror of the `zslh` lesson: a naive placeholder-bean count over-states the
backlog, but the correction is **not** uniformly "noise." Here the residual is
real — so the honest move is *re-scope the count + keep the bean*, not close it.
Distinguishing inflation-of-count from genuineness-of-residual is exactly the
calibration AGENTS.md §"Before declaring open/refuted" demands.
