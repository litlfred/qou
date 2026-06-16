# Markov-trace weighting — the last open piece of `conj:s5-so3-fiber-action`, and the handoff to differential geometry

**Date:** 2026-06-16
**Branch:** `claude/s5so3-markov-weighting-sasakian-2026-06-16`
**Status:** scope — forced target + verifiable compatibility recorded; the geometric construction is the
handoff to differential geometry (not done in-session).
**Discipline:** formalize-first + critical-distance — state the forced target, record what is verifiable, mark
honestly where in-session methods bottom out. No fit, no fabricated construction.

## Where the keystone stands

Across this session's merged PRs the geometric leg of `conj:s5-so3-fiber-action` was reduced step by step:

- generation **selection** $\ell\mapsto\lambda$ is **realized** by the Hopf moment map $\mu$ (spatial
  $\mathrm{SO}(3)$-equivariance) + the Schur-forced static coupling;
- the strand fibre is forced to **colour $\mathbb{C}^3$** (Schur–Weyl);
- the round-$S^5$ colour Reeb (phase) is transverse to $\mu$, but that is the *contact* circle, not the
  generation direction (the spin Hopf Reeb is $\mathrm{Ad}$-trivial).

**The single remaining open piece is the Markov-trace WEIGHTING** $y_\lambda$ — the geometric origin of the
Ocneanu/Plancherel weights of $H_n(q)$.

## Forced target (verified — `scripts/s5so3_ingredient4_markov_weighting_facts.py`, exit 0)

The weighting is **not** free: it is the Ocneanu/Plancherel measure $W_\lambda = d_q(\lambda)^2/[n]_q!$. At $q_0$
for $n=5$:

| block $\lambda$ | $d_q(\lambda)$ | $W_\lambda = d_q^2/[5]_q!$ |
|---|---|---|
| $(3,1,1)$ — electron | $6.2204$ | $0.29467$ |
| $(3,2)$ — muon | $5.2204$ | $0.20754$ |
| $(2,2,1)$ | $5.2204$ | $0.20754$ |

($[5]_q!=131.313$ at $q_0$.) These are exactly the weights the A≥3 operator-branching compute
(siblings #2371/#2369/#2372) produces via the Markov trace — so the *algebraic* weighting is in hand; the open
question is its *geometric* origin.

## Candidate arena + verifiable compatibility

From the round-$S^5$ transversality obstruction, the colour Reeb must sit in the **spatial
$\mathrm{SO}(3)_{\mathrm{colour}}\subset\mathrm{SU}(3)$** — i.e. an $\mathrm{SU}(3)/\mathrm{SO}(3)$-homogeneous
Sasakian (the **Wu manifold**), not the round $S^5$. Compatibility facts that are **verifiable** (and met):

- $\dim \mathrm{SU}(3)/\mathrm{SO}(3) = 8-3 = 5$ — **odd**, so Sasakian-dimension-compatible. ✓
- Regular Sasakian ⟺ (Boothby–Wang) an $S^1$-bundle over a Kähler–Einstein 4-base; **necessary** condition
  $\chi=0$. The Wu manifold has $\chi=0$ (known) — so it is **not obstructed** at this level.

## The two OPEN geometric sub-questions (the handoff)

1. **(Q1) Sasakian existence.** Does $\mathrm{SU}(3)/\mathrm{SO}(3)$ admit a regular Sasakian structure whose
   Reeb is the spatial $\mathrm{SO}(3)_{\mathrm{colour}}$ circle (equivalently: is the $\mathrm{SO}(2)$-quotient a
   Kähler–Einstein 4-manifold)? The known torsion $H^2(\text{Wu};\mathbb{Z})=\mathbb{Z}/2$ is a feature to
   exploit/obstruct here.
2. **(Q2) Weight = equivariant index.** Does that Reeb's $S^1$-equivariant index / contact volume reproduce the
   forced $W_\lambda$ above (the geometric origin of the Ocneanu measure)?

**Neither is settled in-session.** These require genuine differential geometry (Sasakian existence on the Wu
manifold + an equivariant-index computation) — the point at which the formalize-first toolkit used throughout
this session bottoms out. Recording the forced target + the met necessary-conditions + the precise sub-questions
is the deliverable; the construction is the owner-gated, geometer-grade next step.

## Honest net

The keystone is now reduced to a **single, sharply-posed differential-geometry problem**: build the
$\mathrm{SU}(3)/\mathrm{SO}(3)$ (Wu-manifold) Sasakian with spatial-$\mathrm{SO}(3)$ Reeb and show its equivariant
index gives the Ocneanu weights $W_\lambda$. Everything else (selection, fibre, parity, the refuted shortcuts) is
done. No fit was introduced anywhere in the arc.

## Cross-references

- [`2026-06-16-s5so3-hopf-coupling-and-reeb-obstruction.md`](2026-06-16-s5so3-hopf-coupling-and-reeb-obstruction.md) — selection realized by μ; phase-Reeb obstruction; reframe
- [`2026-06-16-s5so3-two-sasakian-construction-attempt.md`](2026-06-16-s5so3-two-sasakian-construction-attempt.md) — the two Sasakian sides
- siblings #2371 / #2369 / #2372 — the A≥3 operator-branching compute that produces the $W_\lambda$ algebraically
- `scripts/s5so3_ingredient4_markov_weighting_facts.py` — forced target + compatibility (exit 0)
