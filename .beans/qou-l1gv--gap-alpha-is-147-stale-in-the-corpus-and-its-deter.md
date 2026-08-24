---
# qou-l1gv
title: 'GAP: alpha* is 14.7% stale in the corpus and its determining producer cannot run'
status: todo
type: task
priority: normal
created_at: 2026-08-24T13:05:13Z
updated_at: 2026-08-24T13:18:11Z
---

Found while triaging the last convention-C sites (`qou-cds1`, PR #5622).
`computations/alpha/alpha_high_precision.py` was on my list only because it
carries a C-frame `z`; it turned out to have **three** independent defects, and
the convention is the least important of them.

## 1. The documented α* is stale by +14.7 % — in its OWN convention

    docs/canonicalization-review.md:21,136     alpha* ~= 0.305807
    measured now, convention C (unchanged)     alpha* == 0.350886411466
                                               +14.7411 %

Both numbers are convention C, so **this drift is not the excision**. Something
upstream moved — the q₀ re-pin and/or a mass constant are the obvious
candidates — and nobody noticed, because the producer stopped being able to
report it (see 3).

## 2. Under the canonical convention D it is different again

    convention C   alpha* = 0.350886411466
    convention D   alpha* = 0.283762164005      (-19.13 % vs C)
    corpus         alpha* ~ 0.305807            (stale C)

The corpus value sits **between** the two live roots, which is how the staleness
stayed invisible: it looks like a plausible number from either side.

## 3. The producer cannot run, and has not been able to for some time

    $ python3 computations/alpha/alpha_high_precision.py
      Bracket: err(0.3) = +1.074673%, err(0.32) = +0.649811%
      ERROR: no sign change in bracket            -> exit 1

`a_lo/a_hi` are hardcoded `0.3 / 0.32`, a window built around the stale
0.305807. **Both live roots are outside it, on opposite sides** — C's 0.3509 is
above `a_hi`, D's 0.2838 is below `a_lo`. So converting the convention does not
fix it and does not break it further; it flips the sign of the whole error curve
(all-positive over the window under C, all-negative under D) without ever
crossing zero inside it.

## 4. It is also muon-pinned, against the standing directive

The run prints `q_0 = 1.1099785955573347` — the **muon** pin. The 2026-08-07
owner directive (reaffirmed 2026-08-15 R2) says compute defaults to proton.
That is a third, separate defect, and fixing it will move α* again.

## What this contaminates

`docs/alpha-blend-derivation.md:772` records **`alpha* = G/3` as "falsified by
PSLQ"**, citing this producer, and §5 discusses a "0.16 % match between α* and
G/3". `G/3 = 0.30532`, which is 0.16 % from the stale **0.305807** — and 13 %
from the live C root. So the falsification's *verdict* survives (it is further
away, not nearer) but its *reasoning* was against the wrong target, and any
other closed-form search run against 0.305807 was searching for a number that
is not α*.

The docstring calls α* *"the BLOCKING input for formal derivation: we need to
know exactly what α* equals before we can prove it."* It has been emitting
nothing.

## Why this is filed rather than fixed

Three entangled defects, each of which moves the answer: convention, bracket,
pin. Fixing any subset produces a number that is neither the old frame nor a
correct new one, and it would land in a witness where a reader could take it as
the new α*. That is the "defined residual != derived" hazard: publish it only
once all three are right.

Suggested order: (i) proton pin, (ii) convention D, (iii) re-derive the bracket
from a scan rather than hardcoding a window — the hardcoded window is what let
a 14.7 % drift go unreported for months. Then re-run the closed-form/PSLQ
search against the new α* and correct `alpha-blend-derivation.md` §5 + line 772.

Blast radius is small: the only importers are two audit scanners
(`witness_environment_split_audit`, `canonical_script_input_audit`), neither of
which consumes the math.


## CORRECTION (same day): the pin is RULED OUT as the cause, and my §4 claim was wrong

§4 above says the producer is muon-pinned and adds *"fixing it will move α* again."*
**Measured, and that is false.** Re-ran with `QOU_Q0_ANCHOR=proton`:

    Q0 the module bound        1.1099785827513808076   (proton — the env var IS respected)
    alpha* (convention C)      0.350886411466
    vs corpus 0.305807         +14.7411 %

**Identical to 12 digits** to the muon-pinned run. So α* here is *invariant*
under the muon↔proton pin, and the 14.74 % drift is **not** the pin.

The muon default remains a real directive violation (2026-08-07, reaffirmed
2026-08-15 R2) and should still be fixed — but it is a provenance defect with
**zero** effect on this number, so it does not belong in the "three entangled
defects, each of which moves the answer" framing. Only **two** move it: the
convention (C→D, −19.13 %) and whatever caused the 14.74 %.

**So the cause of the 14.74 % is still unidentified**, and the two obvious
candidates are now both eliminated: it is not the convention (both figures are
convention C) and it is not the pin (measured here). Remaining candidates, in
rough order of likelihood: a change in the CODATA mass constants
`M_p`/`M_n` the error functional targets, or a change in `nucleon_chains` /
`_std_vhat` / the `hQ` definition feeding the blend. Bisecting
`docs/canonicalization-review.md`'s commit against the producer's history would
localise it.

Recording the negative because it is the more useful half: an agent picking this
up would otherwise spend the first hour re-pinning the producer and find the
number unmoved.


## CAUSE IDENTIFIED — both conventions are live inside this one producer

The previous note said the cause was unidentified with the two obvious
candidates eliminated. Found it, and it is neither: **the producer computes with
convention C and convention D simultaneously.**

    line 44   from hecke_core import (..., h as H_A_F, z as Z_MARKOV)
    line 49   z_m = mp.mpf(str(float(Z_MARKOV)))       -> 0.6126880371464652   = z_D
    line 88   zv  = mp.mpf(1)/(mp.sqrt(Q0)+mp.sqrt(QI)) -> 0.499320334183694452 = z_C

    for reference at the proton pin:
        z_C = sqrt(q)/(q+1) = 0.499320334183694452
        z_D = q^3/(q^2+1)   = 0.612688037146465252

Both feed the same error functional whose root is α*: `z_m` at line 126
(`z_m**(2*span) * Phi_q(pv)`) and `zv` inside `std_za_b`.

**Mechanism of the drift.** The producer has exactly ONE commit in its history
(`f9ad94d750`) — it has not changed since α* ≈ 0.305807 was recorded. Its
*import cone* changed: `hecke_core` / `pyhecke.gram` were migrated to convention
D (`5046347e53` "pyhecke's mpmath path to convention D", `fcf09d2ff6` "enable
native dispatch on convention D + flip trace_weights binding"). That flipped
`Z_MARKOV` by +22.70 % while the locally-computed `zv` stayed C, and α* moved
+14.74 %. Nothing in this file was edited; the number changed underneath it.

This is the **import-cone drift** class AGENTS.md calls "the one that actually
bites" — a file-local `git diff` shows nothing.

**So the earlier measurements re-read as:**

| | z_m | zv | α* |
|---|---|---|---|
| as committed today | D | C | 0.350886411466 — **incoherent, a straddle** |
| with zv converted | D | D | **0.283762164005 — the coherent convention-D value** |
| corpus 0.305807 | C | C | the coherent convention-C value, now unreachable |

So 0.350886 is not "α* in convention C" as I labelled it — it is α* in **no
convention at all**. Correcting that: the C-vs-D framing in the table further up
this bean overstates how meaningful the 0.350886 figure is.

## A second defect in the same two lines: float64 laundering

    z_m = mp.mpf(str(float(Z_MARKOV)))

`Z_MARKOV` is an mpf; `float()` truncates it to binary64 and `mpf(str(...))`
re-inflates it. Measured: **16 significant digits retained of 50.** This is the
exact pattern AGENTS.md's NO-FLOAT64 section names, and the sibling file
`delta_lambda_v_hat_z_transfer_phase5d_4.py` carries a comment warning against
it verbatim ("the f64 constant carries ~16 significant digits, so mpf(str(...))
LAUNDERS it — read the high-precision name instead"). Use `Z_MARKOV` directly.

## Revised fix list (was three items, is four — and the order changes)

1. **Remove the straddle**: `zv` -> `Q0**3/(Q0**2+1)`, so both z's are D.
2. **Stop laundering**: `z_m = Z_MARKOV`, no float() round-trip.
3. **Re-derive the bracket** from a scan; the hardcoded [0.3, 0.32] is what hid
   a 14.74 % drift.
4. **Proton pin** — real directive violation, but measured α*-invariant, so it
   is provenance-only and goes last.

Then re-run the closed-form / PSLQ search against the coherent α* and correct
`docs/alpha-blend-derivation.md` §5 + line 772 and
`docs/canonicalization-review.md` lines 21 / 136 / 155.
