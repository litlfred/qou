---
# qou-f7je
title: 'NOTATION: rename the non-Q_beta c_i cluster coefficients to an unused symbol'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T09:25:15Z
updated_at: 2026-10-04T15:21:42Z
parent: qou-mub3
---


## The problem

`c_k` denotes at least **three distinct objects**, and only one is governed by the
symbol registry:

| `c₃` | value | units | in registry §2? |
|---|---|---|---|
| Q_β **precision ladder** `Q_β = Q_base·∏(1+c_k u^k)` | ≈ −2 | dimensionless | **YES** (§3) |
| μ₃ **door / cluster** `c₃ = −E₀·Δ²g` | −1.7688 (T) / −1.4054 (³He) | MeV | **no** |
| Borromean **H9 magnitude lift** (#4364) | +0.297 | MeV | **no** |

The registry's §2 disambiguation table exists precisely to stop this — it already lists
the cyclotomic `c_k(n)`, the eigenvalue pair `(c_k,d_k)`, and the two distinct `a₁`s.
It does **not** list either μ₃-side sense.

**Why it is dangerous, not merely untidy:** the Q_β ladder value (−2) sits within 12 %
of the μ₃ door value (−1.77). A reader who greps `c₃` and finds "≈ −2" in one place and
"−1.77" in another has **no signal** they are unrelated objects. AGENTS.md
§"Conditional-proved ≠ premise-established" item 4 names exactly this failure —
*"distinct objects sharing a glyph is a recurring root cause"* — and cites the a₁
parity-shadow incident as precedent.

## Owner directive (2026-08-07)

Rename the **non-Q_β** `c_i` to an unused symbol. Q_β keeps `c_k` (it is the
registry-governed sense with the most downstream wiring and the most history — the
four-session wire/un-wire flip-flop, PRs #1452/#1479/#1580).

## Symbol selection — candidates the owner suggested are all TAKEN

- **`f_i`** — `f^λ` is the Frame–Robinson–Thrall dimension (number of SYT), used in
  *this very context*: `Z = Σ_λ f^λ s_λ` (`schur_principal_mpmath._f_lambda`,
  `YLambdaNormalizationSign.lean`). Also `f_bond`, the `f`-map, `f(Z,N)`.
- **`m_i`** — mass, everywhere (`m_e`, `m_p`, `m_π`, `m_μ`).
- **`p_i`** — `p` is the *brane point* per the notation-collision rules, and `p₁` is the
  power sum used in the `sign(Z)` proof (#4665).

Also unavailable: `y_λ` (Jones–Markov), `w_λ` (Plancherel), `u_λ` (LP shadow price) and
`u` (the Q_β ladder variable `b·ℏ_q²`), `z` (`z_markov`), `b`, `t_i` (LP objective),
`g` (the block-trace itself), `v_p`/`v_n` (block-multiplicative binding), `d_k` (brane
tower + homological differential), `κ` (heat coefficient).

**A survey of genuinely-free symbols still needs running** — my first attempt timed out
(5 min) grepping the corpus. Do it with the indexed search, not `grep -rc`.

Suggested starting candidates (verify unused before adopting): `ϰ_k`, `ξ_k`, `ζ_k`,
`η_k`, `ϑ_k`. A cluster-expansion coefficient conventionally takes a Greek letter, and
these keep it visually distinct from the Latin `c_k` at a glance — which is the whole
point.

## Definition of done

1. Survey free symbols with the indexed search; pick one; record it in
   `notation/notation-register.md` **and** `notation/notation-collisions.md`.
2. Add **all three** `c_k` senses to `ck-dk-canonical-registry.md` §2 — including the
   two μ₃-side ones — so the disambiguation table is complete even for the renamed
   symbol.
3. Rename across `computations/deltalambda/*`, the μ₃ audit docs, and any Lean
   docstrings that carry the cluster sense. **Do not touch the Q_β ladder `c_k`.**
4. Update `docs/audits/2026-08-07-mu3-door-status-consolidated.md`, which currently
   uses bare `c₃` for the cluster sense throughout.

## Related

- Convention question on the same objects: bean `qou-8jq2` (non-cyclic perblock vs
  canonical signed trace). These are independent — do not let one block the other.


## RESOLVED: the symbol is `cl_k` (owner pick, 2026-08-07)

Full alphabet surveyed. **No single Roman letter is collision-free** — every one is either
register-claimed or produces a same-domain case-collision:

| letter | uses | why it fails |
|---|---|---|
| `Y` | 4 | `y_λ` Jones–Markov weight — same domain, case-collision |
| `o`/`O` | 3 / 30 | little-o; confusable with zero |
| `Z` | 64 | proton number — reserved, and isotopes *are* this domain |
| `X` | 66 | `X_K` = knot object, `End_𝐂(X_K)`, 14 uses in mass-endomorphism |
| `j` | 66 | `J_K(q)` Jones polynomial |
| `U` | 89 | `U_q(𝔰𝔩₂)` |
| `W` | 90 | `W_λ` geometric weight — used in Δ_λ work |
| `Q` | 92 | `Q_β` |
| `r,s,t,u,v,b` | 150–340 | all live inside the cluster domain (damping ratio, Schur, LP objective, ladder `u = b·ℏ_q²`, binding block factors) |

Chosen: **`cl_k`** (`\mathrm{cl}_k`) — roman, self-documenting, zero collision, greppable.
Follows the repo's own precedent: `\mathrm{Sk}` (Skein module, moved off `\mathcal{S}`) and
`h_\mathrm{A}` (Hecke amplitude, canonized off bare `H_A`).

## DONE

1. `notation-collisions.md` — new `$c_k$ vs $\mathrm{cl}_k$` entry with the rationale.
2. `ck-dk-canonical-registry.md` §2 — `cl_k` row added; the disambiguation table now covers
   the cluster sense that was missing.
3. `2026-08-07-mu3-door-status-consolidated.md` — prose renamed to `cl₃` + a notation banner.
4. Docstrings of `mu3_frechet_perblock_probe.py` / `mu3_abs_choice_robustness_probe.py` state
   which sense their `c3` variable carries. Both re-run exit 0.

## DEFERRED — and why this is not foot-dragging

Compute-layer **variable names and witness keys still read `c3`**. That is deliberate:
`c3_MeV` is a **cross-probe data contract**, not a private local.

- `mu4_rhoF_cluster_derivation_probe.py:119-120` reads
  `JT["T"]["correlation_c3_MeV"]` out of *another probe's* committed witness.
- **15 committed witnesses** carry `c3` / `c3_MeV` keys.
- Renaming keys without migrating every consumer breaks the reads **silently** — a wrong
  number, not an exception.

The reader-facing ambiguity (which was the actual danger: two coefficient families ~12 %
apart sharing a glyph) is now **fully resolved** in the register, the registry, and the prose.
The compute rename is hygiene with real breakage risk and no remaining reader benefit.

### Sweep plan for the compute layer

1. Enumerate every producer emitting a `c3*` key and every consumer reading one (start from
   the 15 witnesses + the `correlation_c3_MeV` cross-read).
2. Rename producer + consumer **in the same commit**, per producer.
3. Re-run each producer; diff the witness to confirm only the key changed, not the value.
4. Batch ≤ 49 files per PR (Gemini review limit).

Do **not** sed the tree.
