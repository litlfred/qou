# The keystone's infinite-dim full-Hecke realization — three faces; the Habiro ring unifies it with Q_β

**Date:** 2026-06-16
**Branch:** `claude/keystone-infinite-dim-full-hecke-realization-2026-06-16`
**Status:** identifies the infinite-dim arena (verified weight + McKay) and unifies it with the corpus Q_β
Habiro element; **not** a closure. No fit.
**Discipline:** formalize-first + critical-distance.

## Context

#2406 ruled out any finite colour-SU(3) arena: the production trace is the **full Hecke / Wenzl principal
specialization** (all rows), so the keystone's geometric leg targets an **infinite-dimensional** object. That is
not exotic — the full-Hecke Markov trace has well-known infinite-dim homes. Here I identify them, verify the two
load-bearing identities, and — answering the author's "and Habiro?" — show the Habiro ring is the QOU-relevant
face that unifies the keystone with the established Q_β Habiro work.

## Verified (`scripts/keystone_infinite_dim_full_hecke_realization.py`, exit 0)

1. **The full-Hecke Markov weight = principal Schur specialization**
   $$s_\lambda(1,q,q^2,\dots) \;=\; \frac{q^{\,n(\lambda)}}{\prod_{c\in\lambda}\bigl(1-q^{h(c)}\bigr)}$$
   (Stanley EC2 7.21.2) — the canonical Markov trace weight (sibling #2389's production `y_λ`). Checked
   **stably** via the SSYT generating function (the bialternant determinant is numerically ill-conditioned;
   SSYT is exact): `(2,1),(3,1,1),(3,2),(2,2)` all match.
2. **McKay:** the binary icosahedral `2I` (the spacetime spin lift, #2364/keystone) has irrep dimensions
   `{1,2,2,3,3,4,4,5,6}` = the **marks of the affine E₈ Dynkin diagram** (Σdim²=120=|2I|); `S³/2I` = the
   Poincaré homology sphere = the link of the E₈ surface singularity.

## Three faces of the realization

- **Colour (type A).** The principal specialization is the character of the **gl_∞ / infinite-wedge basic
  representation** (boson–fermion correspondence); operator-algebraically the **Jones II₁ subfactor** (GNS from
  the *unique* Markov trace, Jones 1983). Infinite-variable — the canonical home of the full-Hecke trace.
- **Spacetime.** `2I ↔ affine E₈` (McKay) ↔ the **affine-E₈ basic representation**; `S³/2I` (Poincaré sphere) is
  the E₈ link. This is the spin/spacetime side's infinite-dim object — **distinct** from the colour (type-A) one,
  consistent with spacetime ⊥ colour (#2398, corpus `S5=S2×S3`).
- **Arithmetic / analytic — the Habiro ring (the QOU-relevant face).** The full-Hecke trace, to be evaluated
  consistently at the substrate `q₀` *and across all roots of unity*, lives in the **Habiro ring** (the
  cyclotomic completion `\widehat{\mathbb{Z}[q]}` at `(1-q),(1-q²),…` — the home of unified WRT / Kashaev quantum
  invariants). **This is the same ring as the corpus's Q_β Habiro element** (`α_EM = [2]_q(1-h²α)`; the permanent
  fix for the `c_k` truncation). So the keystone full-Hecke trace and the Q_β Habiro element are objects of the
  *same ring* — the infinite-dim full-Hecke realization is, arithmetically, a **Habiro-ring element evaluated at
  `q₀`**, unifying the keystone with the established Q_β Habiro framing.

## What this is, and is not

- **Is:** a verified identification of the infinite-dim arena (principal-spec weight + 2I↔E₈ McKay), with the
  Habiro ring tying it to Q_β. The colour and spacetime infinite-dim objects are distinct (spacetime ⊥ colour).
- **Is not:** a closure. The **spacetime⊥colour coupling** — how the colour full-Hecke (gl_∞/type-A, Habiro at
  `q₀`) trace couples to the spacetime affine-E₈ (`2I`) structure to produce the generation shift — remains the
  open keystone. Identifying the homes does not derive the physics (still open at the ingredient-5 level).

## Net

"Trying the infinite-dim full-Hecke realization" lands it: colour = Jones II₁ / gl_∞ principal specialization,
spacetime = affine-E₈/`2I`, arithmetic = the **Habiro ring at `q₀`** (= the Q_β Habiro element's ring). The
keystone is thus a **Habiro-ring** problem, unified with Q_β — a sharper aim than "build a Sasakian", and a real
bridge between the two open goals. The coupling is the residual open object; no fit introduced.

## Cross-references

- `docs/audits/2026-06-16-keystone-arena-is-full-hecke-not-su3.md` (#2406) — why finite SU(3) is ruled out
- `docs/audits/2026-06-16-keystone-wu-manifold-reeb-obstruction.md` (#2398) — spacetime ⊥ colour
- `docs/coordination/s5-so3-keystone.md` — keystone ledger
- `docs/coordination/1ppq-qbeta.md` + the Q_β Habiro element (`α_EM [2]_q(1-h²α)`, PR #1511) — the same Habiro ring
- `scripts/keystone_infinite_dim_full_hecke_realization.py` — verified weight + McKay (exit 0)
