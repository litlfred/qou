# Reeb-resonance probe — NO eigenvalue resonance realizes the dynamical spin–colour coupling

**Date:** 2026-06-16
**Branch:** `claude/s5so3-reeb-resonance-probe-2026-06-16`
**Status:** honest negative — the dynamical intertwining is **not** closed by a Reeb-eigenvalue match.
**Discipline:** formalize-first + strict numerology guard (a 2-point match is fittable; require
parameter-free + a 3rd anchor).

## Question

The spin–colour coupling of `conj:s5-so3-fiber-action` splits into a **static** part (Schur-forced, unique
isotypic projection — `s5so3_ingredient4_coupling_schur.py`) and a **dynamical** part: the coupling must
intertwine the spin Hopf Reeb flow ($S^3$) with the colour Sasakian Reeb flow ($S^5$). The natural form of that
condition is a **resonance** between the spin-$\ell$ Reeb eigenvalue and the colour-$\lambda$ Reeb eigenvalue.
Does such a resonance hold?

## Result (verified — `scripts/s5so3_ingredient4_reeb_resonance_probe.py`, exit 0): NO

Testing the natural eigenvalue invariants (SO(3) Casimir $\ell(\ell+1)$ on the spin side; content sum $c(\lambda)$
on the colour side) against the verified bridge:

| $\ell$ | spin $\ell(\ell{+}1)$ | colour block(s) | content sum(s) |
|---|---|---|---|
| 1 (e) | 2 | $(3,1,1)$ | $0$ |
| 2 (μ) | 6 | $(3,2)$ | $2$ |
| 3 (τ) | 12 | $(3,1,1)$ **and** $(4,1)$ | $0,\;5$ (**multi-block**) |

Two observations kill the resonance:

1. **The 2-point "matches" are non-unique.** At $\ell=1,2$ the colour content $\{0,2\}$ is fit *equally* by
   $\ell(\ell-1)$ **and** $2(\ell-1)$ (and infinitely many others). A 2-point coincidence with no discriminating
   third anchor is exactly what the numerology guard forbids reporting.
2. **Both fail at the discriminating $\ell=3$ anchor.** $\ell(\ell-1)=6$ and $2(\ell-1)=4$; the tau colour
   contents are $\{0,5\}$ — neither matches. And $\ell=3$ (tau) is **multi-block** ($T_2\subset(3,1,1)$,
   $G\subset(4,1)$), so a single colour Reeb eigenvalue is not even well-defined there.

**No exact, parameter-free, $\ge3$-anchor Reeb resonance exists** among the natural invariants. The dynamical
spin–colour intertwining is therefore **not** realized by a simple eigenvalue match.

## Why this is the useful outcome

- It **documents the resonance route as a dead end**, so a future agent does not fit the $\ell=1,2$ coincidence
  ($c(\lambda)=\ell(\ell-1)$ looks seductive in isolation) into a false "closure" — the same failure mode as the
  refuted GAP-A-4 210 ppb mechanism.
- It **re-confirms the open object is genuinely geometric**, not arithmetic: the dynamical intertwining (if it
  exists) must come from the actual contact structures' compatibility, not a numerical eigenvalue identity. The
  multi-block spreading of tau ($\ell=3$) further signals that the clean single-block $\ell\to\lambda$ picture
  is itself only an $\ell\le2$ approximation.

## Net for `conj:s5-so3-fiber-action`

- Static coupling: **forced** (Schur). Dynamical coupling: **open**, and now shown **not** closable by a
  Reeb-eigenvalue resonance (this probe). The remaining content is the genuine contact-geometric existence of
  the intertwining of two specific Sasakian flows — owner-gated, multi-session, and *not* reducible to a number
  match.

## Cross-references

- [`2026-06-16-s5so3-two-sasakian-construction-attempt.md`](2026-06-16-s5so3-two-sasakian-construction-attempt.md) — the two-Sasakian construction + the static/dynamical split
- `scripts/s5so3_ingredient4_coupling_schur.py` — static coupling Schur-forced (dim Hom = 1)
- `scripts/s5so3_ingredient4_reeb_resonance_probe.py` — this probe (negative, exit 0)
