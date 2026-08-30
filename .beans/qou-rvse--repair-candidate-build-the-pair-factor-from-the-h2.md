---
# qou-rvse
title: 'Repair candidate: build the pair factor from the H2 Wedderburn split (isospin 2x2 = 3+1), not from crossing signs'
status: todo
type: task
priority: normal
created_at: 2026-08-30T10:32:43Z
updated_at: 2026-08-30T10:33:37Z
---

## Why the current pair factor cannot be repaired by convention

From `qou-1pig`: the isovector term `f_pp - f_nn = h` is forced EXACTLY by the
Hecke skein relation `sigma - sigma^-1 = q - 1/q` under the identification
`p |-> positive crossing, n |-> negative crossing`. No `pn_convention` touches
it. So the thing to revisit is the identification itself.

## The diagnosis

A crossing sign is a **Z/2 grading**. It can only produce a +/- (odd) structure.
Isospin is an **SU(2) doublet**, and pair states decompose as

    2 (x) 2  =  3 (+) 1        T=1 triplet (pp, nn, and the T=1 part of pn)
                                T=0 singlet (pn only)

The triplet members are DEGENERATE under isospin symmetry -- that is what makes
`f_pp = f_nn` -- and the singlet is the distinguished channel. A Z/2 grading
cannot produce a triplet/singlet decomposition; it produces exactly the wrong
parity, which is what qou-1pig measures (isovector / isoscalar = 1454).

## The machinery is already in the file, one function above the bug

`closed_form_tau_M.wenzl_weights_h2` gives the H_2(q) Wedderburn decomposition
`2 (x) 2 = (2) (+) (1,1)` -- literally the isospin `3 (+) 1`:

    y_(2)   = 0.75270211325196540159        sigma eigenvalue  q    = +1.1099785828
    y_(1,1) = 0.24729788674803459841        sigma eigenvalue -1/q  = -0.9009182840
    and y_2*q - y_11/q = z                  (verified to full precision)

A pair factor keyed on WHICH IRREP the pair sits in is automatically
charge-symmetric (pp and nn are both pure T=1, hence identical) while
distinguishing pn (which carries the T=0 admixture). Correct parity by
construction, no new input.

## EXPLORATORY -- one data point, and it lands the right way

Reading `(2)` (symmetric) as T=1 and `(1,1)` as T=0, with the Sec.10a log map
`B = -alpha ln f`, `alpha = 4.18598 MeV`:

    channel              f                        B (MeV)      vs AME 2H
    pure T=1 (pp, nn)    q = 1.10997858    > 1    -0.4368      UNBOUND  <- correct!
    y-weighted mix (pn)  z = 0.61268804    < 1    +2.0507      ratio 0.9218  (-7.8%)

    current model (bring_color_weighted):          +2.8332      ratio 1.2736  (+27.4%)

So it gets the QUALITATIVE structure right -- the diproton and dineutron come out
unbound, the deuteron bound -- and the 2H accuracy improves 3.5x, parameter-free.

## Three reasons NOT to believe this yet

1. **The irrep-to-isospin assignment is not derived.** Reading `lambda = (2)` as
   T=1 is natural but I have not proved it here; the other assignment could
   easily reverse the sign of the improvement.
2. **One data point.** 2H only. No A >= 3 check, and the A >= 3 assembly is where
   every previous candidate died.
3. **It is a re-assignment, not a new formula.** `z` is *already* `f_pp` in the
   current model; the proposal makes it `f_pn`. That is cheap, and cheapness is
   exactly when to suspect a coincidence. -7.8% on a single anchor is not
   evidence.

## Next

Derive the irrep-to-isospin assignment before computing anything else with it.
Then A=3 and A=4 with the AME targets held out until the assignment is fixed --
tuning the assignment against the anchors would be a fit, and the three-calibration
discipline review will catch it.

Parent: qou-1pig (the parity defect), qou-brng (the extensive term).
