---
# qou-u5z0
title: 'AUDIT: a convention-C dependency can survive as a derived IDENTITY — invisible to every detector class'
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:24:15Z
updated_at: 2026-08-24T17:28:24Z
---

Found while sweeping for convention-C spellings during the `qou-cds1` excision.
**The instance is low-stakes; the class is not.**

## The instance

[`computations/qbeta/toroidal_harmonics.py:48-52`](../computations/qbeta/toroidal_harmonics.py):

    # The Markov parameter is z = sqrt(q)/(1+q). Let q = e^(-eta).
    # Then z = 1 / (2 cosh(eta/2)).
    # w = z^2 = 1 / (4 cosh^2(eta/2)) = 1 / (2 (cosh(eta) + 1))
    # Therefore, x = cosh(eta) maps to:
    x_w = 1/(2*w) - 1

The live line is `x_w = 1/(2*w) - 1`. That identity is **exact under convention
C and simply wrong under D** — measured at the proton pin, with `eta = -ln q`:

    C:  z = 0.49932033418369   w = z^2   1/(2w)-1 = 1.005448433353561 == cosh(eta)   TRUE
    D:  z = 0.61268803714647   w = z^2   1/(2w)-1 = 0.331960061687155  vs 1.005448…  FALSE

Off by a factor of 3, not a perturbation. The derivation is
`cosh(η) = 2cosh²(η/2) − 1` composed with `z_C = 1/(2cosh(η/2))`; neither step
survives `z_D = q³/(q²+1)`.

**Scope, stated honestly: LOW.** The module emits **no witness**, and its
apparent importer (`qbeta_toroidal_harmonics_basis_probe.py`) only names it in
its own docstring — it does not import it, and carries no `cosh`, no
`sqrt(q)` and no `z` of its own. So this is exploratory/standalone code, not
feeding production. Fix it when the file is next touched; it does not gate the
excision.

## The class — this is why it is filed

**A convention-C dependency can survive as a *derived identity*: no z
expression, no z literal, no witness edge.** Every detector deployed on this
campaign is blind to it:

| detector | keys on | sees this? |
|---|---|---|
| expression scan (mine) | `1/(sqrt q + …)`, `sqrt(q)/(q+1)`, return forms | **no** — no z expression in the code |
| value-literal scan (mine, `486178eb26`) | the decimal `0.49932…` | **no** — no literal |
| witness-layer intersection (sibling) | witnesses carrying the C fingerprint | **no** — emits no witness |
| consumer read-edge (sibling, #5669) | who *reads* a C-frame witness | **no** — no read edge |

The C-ness lives entirely in a **comment plus an arithmetic identity**. Only
re-deriving the mathematics finds it.

## How it was found, and the cheap generalisation

By enumerating **mathematically equivalent spellings of z_C** and grepping for
each, rather than grepping for the spellings already known. Seven forms all
evaluate to `0.499320334183694452` at the proton pin:

    1/(sqrt q + 1/sqrt q)      sqrt(q)/(q+1)        q**0.5/(1+q)
    (q**0.5 + q**-0.5)**-1     1/(2*cosh(ln q/2))   0.5/cosh(0.5*log q)
    Re 1/(2*cos(-i*ln q/2))

The **hyperbolic** family is the one that pays: `z_C = 1/(2 cosh(η/2))` with
`η = ln q`. Nothing in the campaign greps `cosh`.

Two notes for whoever automates this:

- **Narrow to the reciprocal shape.** Bare `cosh(` is **873** hits corpus-wide
  (toroidal harmonics, Ohtsuki ladders); `1/(2 cosh(…))` is 17, of which 15 are
  the harmonic normaliser `1/(2 cosh η)` — **no half-argument**, a different
  quantity. `z_C` needs `η/2`. The half is the discriminator.
- **Selftest with a negative case.** My first cut of the regex failed its own
  positive selftest (`mp.mpf(1) / (…)` is not a bare `1`), and would have
  reported a clean surface. Include the negative `two_cosh_u = 2 * mp.cosh(u)`
  so a widened pattern cannot silently swallow the normaliser.


## Second sweep round — three more equivalence classes, all CLEAN

Continued the method. Verified numerically that these also equal
`z_C = 0.499320334183694452` at the proton pin, then greped each with
selftests:

| spelling | corpus hits | verdict |
|---|---|---|
| `1/sqrt([2]_q + 2)` (also `1/sqrt(q + 1/q + 2)`, `1/sqrt((q+1)^2/q)`) | **0** | clean |
| `0.5*sech(ln q / 2)` | **0** | clean |
| `1/[2]_{sqrt q}` — reciprocal of `sqrt(q) + 1/sqrt(q)` | 2 files define it, **0 invert it** | clean |

The third needs the detail, because it is the near miss:

    qbeta_cosh_q_sinh_q_candidate_scan.py:72   two_q_half = mp.sqrt(q) + 1/mp.sqrt(q)
    qbeta_sym_part_hecke_natural_form.py:97    two_q_half = sp.sqrt(q) + 1/sp.sqrt(q)   # [2]_{q^(1/2)}

`1/two_q_half` **is** z_C exactly. Neither file takes that reciprocal — the
first only records it as witness data, the second **multiplies**
(`form_2 = -two_q_half * h_tilde**2 / 2`). So `[2]_{q^(1/2)}` is a quantity in
its own right here, a Hecke natural form, and both are legitimate.

**They are one reciprocal away, though.** A future edit that divides by
`two_q_half` becomes a convention-C site under a name containing no `z`, no
`sqrt(q)/(q+1)`, and no `0.49932`. Worth a watch pattern rather than a fix:
flag `/\s*two_q_half` or `two_q_half\s*\*\*\s*-1`.

**Net across both rounds:** ten equivalence classes enumerated, one live site
found (the hyperbolic identity above), one near-miss class recorded, the rest
clean. Recording the negatives so the next agent does not re-sweep them — the
value of the method is knowing which forms are *excluded*, not only which hit.
