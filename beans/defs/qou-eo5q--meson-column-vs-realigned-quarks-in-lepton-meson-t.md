---
# qou-eo5q
title: 'Meson column vs realigned quarks in lepton-meson-torus-knot-dictionary: phi = s-sbar carries generation-2 flavour content while sitting in the generation-3 row. Left unharmonised deliberately in the 2026-08-01 realignment; resolve or document.'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-decide
created_at: 2026-08-01T22:05:55Z
updated_at: 2026-10-10T18:14:38Z
parent: qou-8lxd
---

## Body written 2026-10-10 — this bean was TITLE-ONLY from 2026-08-01

The title already states the finding; this adds the measurement, the two
*further* defects found in the same block while checking it, and options.

## Defect 1 — the one in the title, and it is an INDEXING shift, not one bad cell

`prop:lepton-meson-torus-knot-dictionary`
(`folio/quantum-observable-universe/knots-particles-confinement/lepton-meson-torus-knot-dictionary.md`)
tabulates generations against `T(2, 2k+1)`:

| Generation | `n` | Lepton (`H₂`) | Quark flavour (`H₃`) | Meson (`qq̄`) |
|---|---|---|---|---|
| 1st | 3 | `e` | `u, d` | `π` |
| 2nd | 5 | `μ` | `c, s` | `K` |
| 3rd | 7 | `τ` | `t, b` | `η, φ` |

Its `-proof` sibling gives each meson's constituent content and crossing count:

```
π : ū d  = 3 + 3 = 6     <- gen1 + gen1   (pure generation 1)
K : ū s  = 3 + 5 = 8     <- gen1 + gen2   (MIXED)
η, φ: s s̄ = 5 + 5 = 10   <- gen2 + gen2   (pure generation 2, in the gen-3 row)
```

So the meson column is not "the meson built from this row's quarks" — it is
**the next rung of the total-crossing ladder 6, 8, 10**, which runs in step 2
exactly as `n = 3, 5, 7` does and therefore looks aligned while being offset.
Only row 1 is self-consistent. Row 2 is a mixed gen-1/gen-2 state and row 3 is a
pure gen-2 state. The title's `φ = s s̄` is the extreme case, not the only one.

**The physical reason there is no clean row 3** is worth stating, because it
constrains the options: the generation-3 quarkonia are `b b̄` (the `Υ`, which
exists, `7 + 7 = 14` crossings under this scheme) and `t t̄` (**toponium, which
does not exist as a bound state** — the top decays first). So the table cannot
be "harmonised" by substitution alone without committing to `Υ` and leaving the
`t` row's meson slot empty.

## Defect 2 — "(odd primes)" is an exclusion the corpus performs differently

Line 1 reads *"indexed by torus knots `T(2, n)` for `n = 3, 5, 7, …` **(odd
primes)**"*. This is a `proposition`, so the parenthesis is a claim.

Measured: the phrase "odd prime" occurs in **exactly this one block**,
corpus-wide in `.md`. And it conflicts with the corpus's own allowed-knot list:
`beta-stability-interpretation.md` derives the embeddability bound
`(m−1)(n−1)/2 ≤ g = 4`, i.e. `(m−1)(n−1) ≤ 8`, and lists the survivors as
**`T(2,3), T(2,5), T(2,7), T(2,9), T(3,4), T(3,5)`** — `T(2,9)` **included**
(`1 · 8 = 8 ≤ 8`). So primality is excluding `T(2,9)` here while the chapter's
stated mechanism admits it. What actually excludes `T(2,9)` is an open question
on this arc's own `8f-gen` front ("what excludes `T(2,9)`"), so the parenthesis
is asserting a resolution of it in passing.

## Defect 3 — `η` is not `s s̄`

Minor and separable. `φ(1020)` is predominantly `s s̄` (PDG), so that half is
fine. `η` is an `SU(3)`-octet mix of `uū, dd̄, ss̄`, not `s s̄`. Grouping them as
"`η, φ : s s̄`" is loose at `η`.

## Options

1. **Relabel the column, do not re-populate it** — "Meson at crossing count
   `2n`" or "crossing-ladder meson", and say in prose that the meson index is
   the total-crossing rung and is therefore offset from the generation index.
   Cost: one header + one sentence. Risk: lowest; it makes the table say what it
   measurably is. **Recommended (agent judgement).**
2. **Re-populate for genuine generation-3**: `Υ (b b̄)`, `14` crossings, and
   state that the `t t̄` slot is empty because toponium is not bound. Cost:
   table cell + the proof's crossing list + a sentence. Risk: commits the
   framework to a `14`-crossing prediction nothing currently computes.
3. **Document the mismatch and leave the table** — the disposition the
   2026-08-01 realignment chose ("left unharmonised deliberately"). Cost: one
   `authorNotes` entry or one prose sentence. Honest, and keeps a table whose
   rows do not mean what their header says.
4. **Nothing.**

Defects 2 and 3 are independent of the choice above and are one-token each:
drop "(odd primes)" (or replace with the embeddability bound the corpus
actually uses), and write "`φ : s s̄`; `η` an octet mix" instead of grouping.

**Default if unanswered: (4).** The table keeps a meson column offset by one
generation, a primality claim the chapter's own bound contradicts, and a loose
`η`. Nothing numerical moves — no witness, no Lean, no compute reads this block.

**Blast radius:** `prop:lepton-meson-torus-knot-dictionary` + its `-proof`
sibling + `lepton-meson-torus-knot-dictionary.lean`. Defect 2 touches the
`8f-gen` front's open `T(2,9)` question — do not resolve it here.


## ENACTED 2026-10-10 — owner said "do it correct"; read as option 1, and here is why

All three defects in this bean are fixed. The column question got the
**relabel**, not the Υ repopulation, and the reasoning is on the record so it
can be overruled cheaply.

**Defect 1 — the indexing shift.** `prop:lepton-meson-torus-knot-dictionary`'s
meson column header is now *"Meson at $2n$ crossings ($q\bar q$)"*, the closing
sentence says the meson is the pair whose **total** crossing number is $2n$ and
that the column is indexed by that total rather than by the row's quark
generation, and a new paragraph spells out the offset: $\pi = \bar u d$ is $3+3$
(pure gen-1), $K = \bar u s$ is $3+5$ (**mixed** gen-1/gen-2), $\phi = s\bar s$
is $5+5$ (pure gen-**2**, in the gen-3 row).

**Why option 1 and not option 2.** "Do it correct" admits two readings — make
the label match the content, or make the content match the label. Populating the
row with $\Upsilon$ at $7+7 = 14$ crossings would commit the framework to a
prediction **nothing in the corpus computes**, which under §NO FITTING is worse
than an honest label: a route is ranked by derivational cleanliness, not by
looking complete. So the block now states the *factual* position without
claiming either as a framework row — the third-generation quarkonia are
$\Upsilon = \mathfrak{b}\bar{\mathfrak{b}}$, which would sit at 14 crossings and
is not computed here, and $\mathfrak{t}\bar{\mathfrak{t}}$, which is not a bound
state. If the stronger version was wanted, it is a one-line change from here.

**Defect 2 — "(odd primes)" is gone**, replaced by *"odd $n = 3, 5, 7, \ldots$"*,
which is what $2k+1$ is and claims nothing more. The parenthesis had been
resolving the `8f-gen` front's open *"what excludes $T(2,9)$"* question in
passing, against the chapter's own embeddability bound $(m-1)(n-1) \le 8$, which
**admits** $T(2,9)$.

**Defect 3 — $\eta$ split from $\phi$** in the `-proof` sibling: $\phi$ is
$s\bar s$ at $5+5$; $\eta$ sits at the same rung but is an
$\mathrm{SU}(3)_{\mathrm{f}}$-octet mixture of $u\bar u$, $d\bar d$, $s\bar s$.

**Verification.** `qa-sweep` on both blocks after the edits: **0 critical, 0
major, 0 minor**. One transient to record rather than hide: the first batch run
reported `[major] detangler-no-forward-ref` at
`lepton-meson-torus-knot-dictionary.ts:0` — and that `.ts` is **unchanged from
`origin/main`**, whose baseline for the same block is 0/0/0. Three subsequent
runs, including one repeating the batch's exact ordering, report 0; the
attestation store holds no `detangler` criterion, so it is not
cache-suppression. Unreproducible, on a file this branch does not touch; not
claimed clean, not claimed broken.


## 2026-10-10 (later) — owner ruled 3a + "try compute 14"; Υ computed, scope-(a) negative

Owner (ofri): keep the relabel, do not put Υ in the table, but try the
14-crossing Υ entry with the same construction. Done in
`computations/eightfold/upsilon_14_crossing_probe.py` (witness 5/5, proton pin,
70 dps). Audit: `docs/audits/2026-10-10-upsilon-14-crossing-probe.md`.

- **Construction:** `m_X/m_π = χ^(2,1)(σ₁ⁿ)·(V_S(T(2,n))/V_S(T(2,3)))²`, the
  formula of `prop:meson-kaon-pion-hecke-seifert` / `prop:gen3-meson-phi-hecke-seifert`.
  `n` is the row's torus knot, not the crossing total. Controls reproduce:
  K −290 ppm, φ +0.22 %.
- **n = 7 (generation index, zero new choices):** 7.32011 against PDG
  `m_Υ/m_π = 67.7816(19)`, which is **−89.2 %**. The value is identical to the φ slot,
  because the construction cannot separate φ from Υ.
- **n = 14 (crossing count):** χ(σ¹⁴) = q¹⁴+q⁻¹⁴ is defined. **Missing choice:**
  V_S of the 2-component LINK T(2,14); the corpus defines V_S only for odd-n
  knots. The diagnostics are not adopted: literal π(n−2)/n gives −55.7 %, and the link-base
  orbifold Euler number gives +77.2 %.
- **New finding, deliberately not edited (owner said keep the relabel):** the
  header "Meson at 2n crossings" holds only in row 1. K is 8 crossings, not 10;
  φ is 10, not 14. The column follows n+3. Taken literally, the header's rule would put Υ
  in row 7. Options: (i) say "the next rung of the 6, 8, 10 ladder"
  instead of "2n", a one-phrase edit; (ii) leave as is (the default). Agent
  judgement: (i), because the header currently states a rule its own rows break.

Status left `completed`: the bean's task (the column disposition) is done. The
open question raised here is the header wording, which is an owner call and is
recorded above, not opened as a conjecture.
