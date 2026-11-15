# Q_β nucleon words: no symmetry maps n ↔ p, and where the bar involution breaks

Bean `qou-hlx8` (epic `qou-qs0e`, tracker #7735), **scoped to the element-level symmetry
tests only**, on the coordinator's instruction.

The rest of route 3 is stream 12's, in draft PR #7860 (session
`session_01Qmmkt8pE46F2YNM5QTVpHa`, branch `claude/bar-parity-split-close-gap-2026-11-15`):
* the trace/bar intertwining, holding iff z(q) − z(1/q) = h (`zD_bar_shift`);
* the decomposition f = h·g;
* the f_odd value.

None of that is recomputed here. This audit also answers stream 12's gap bean `qou-z08b`,
which asks which part of the word makes g fail to be bar-even.

* Probe, analysis only: `computations/qbeta/qbeta_bar_odd_sinh_role_probe.py`. It runs
  5/5 checks, exact in sympy. It writes **no** witness, computes **no** Q_β value, and
  touches no dashboard.

## Words (census letters, `nuc11_interleaved`)

```
n: u0 d1 u0 d1 u0 d1 | ud0 ud0 d1 | u0 u0
p: u0 d1 u0 d1 u0 d1 | u0  ud0 ud1 | u0 u0
     core (σ₀σ₁⁻¹)³     quark tail    gluon
```

Letters: u = σ, d = σ⁻¹ = σ − h, ud = σ − h/2. The suffix is the generator.

## 1. Result: composites of {bar, rev, swap, χ}, up to length 4

All composites were tested exactly at the NF element level:

| symmetry | action |
|---|---|
| bar | σ ↦ σ⁻¹ = σ − h, scalars h ↦ −h |
| rev | word reversal |
| swap | σ₀ ↔ σ₁ |
| χ | σ ↦ −σ⁻¹, same q (`qou-hlx6`); added for completeness |

| question | answer |
|---|---|
| S(n) = p or S(n) = −p, for any composite S? | **No.** |
| S(Δ) = −Δ? | **Only for bar∘χ and χ∘bar.** These are σ ↦ −σ with h ↦ −h, i.e. q ↦ −q. Every census letter is odd under it, so S(n) = −n and S(p) = −p. This is a word-length parity, **not** an n ↔ p map. |
| S(Δ) = +Δ? | **No.** |
| Within {bar, rev, swap} alone | **No** n ↔ p map, and **no** Δ ↦ ±Δ. |

**Scope (a).** This excludes the composites of these four maps on these two words. It does
not exclude a symmetry outside the set. The consequence for route 3: no tested algebra
symmetry makes Δ bar-odd, so the bar-odd projection of the trace has no structural
motivation from Δ. Whether it carries the sinh role is a separate question for stream 12.

## 2. Where it breaks (for `qou-z08b`)

The comparison is letter by letter, between S(n) and p, at positions 0–5 (core), 6–8 (quark
tail) and 9–10 (gluon):

| S | S(n) | mismatched positions | segments |
|---|---|---|---|
| bar | d0 u1 d0 u1 d0 u1 ud0 ud0 u1 d0 d0 | 0–5, 6, 8, 9, 10 | core, tail, gluon |
| rev | u0 u0 d1 ud0 ud0 d1 u0 d1 u0 d1 u0 | 1–4, 7, 8, 9 | core, tail, gluon |
| swap | u1 d0 … | all | all |
| bar∘rev∘swap | d1 d1 u0 ud1 ud1 u0 d1 u0 d1 u0 d1 | 0, 3–8, 10 | core, tail, gluon |

Bar applied segment by segment, at the letter level:

| segment | bar image | bar-fixed? |
|---|---|---|
| core (σ₀σ₁⁻¹)³ = u0 d1 ×3 | d0 u1 ×3 = (σ₀⁻¹σ₁)³ | no |
| gluon σ₀σ₀ = u0 u0 | d0 d0 = σ₀⁻²  | no |
| p tail u0 ud0 ud1 | d0 ud0 ud1 | no |
| n tail ud0 ud0 d1 | ud0 ud0 u1 | no |

**Reading for `qou-z08b`.** The failure is **not** confined to the quark tail. Bar is the
letter-level flavour flip: it exchanges u ↔ d and fixes ud. It therefore also flips the
**flavour-neutral** core and gluon, which are written in oriented letters: the core is
u0 d1 alternating and the gluon is u0 u0. Even if the tail were made bar-compatible, the
core alone sends (σ₀σ₁⁻¹)³ to (σ₀⁻¹σ₁)³, and the gluon sends σ₀² to σ₀⁻². Within the tail,
bar sends p's (u0, ud0, ud1) to (d0, ud0, ud1). That is the same letter multiset as n's tail
(ud0, ud0, d1), but at different positions and generators: the d sits on σ₀ at position 6
in bar(p), and on σ₁ at position 8 in n.

So the bar-oddness of g fails for three independent reasons:
1. the oriented core;
2. the oriented gluon;
3. tail placement.

Each is enough on its own. Fixing only the quark letters cannot restore bar-evenness.

This is the agent's reading of the letter-level table. The NF tests in §1 are what is
established.

## 3. Owner decision

### D-H8: is route 3 (Q_β reads the bar-odd part) closed as unmotivated?

* **(A) Close it, scope (a).**
  * *Means:* record §1 as the answer for route 3. Stream 12 keeps its computed value as a
    recorded function, not as a candidate.
  * *Costs:* none.
  * *Risks:* a symmetry outside {bar, rev, swap, χ} could exist.
  * *Commits to:* route 3 needs an exhibited n ↔ p symmetry before it is reopened.
* **(B) Keep it open and search wider.**
  * *Means:* look for word-dependent maps, e.g. flipping only the tail while keeping the
    core and gluon.
  * *Costs:* hours.
  * *Risks:* a map built to send this n to this p is selection against the target unless
    it is defined independently first.
  * *Commits to:* defining the map before testing it.

**Default if nothing is said: (A).** **Recommendation (judgement): (A).** §2 shows the
obstruction sits in the flavour-neutral core and gluon as much as in the tail. A map fixing
it would have to treat those segments differently from the quarks, which is a modelling
choice rather than a symmetry.
