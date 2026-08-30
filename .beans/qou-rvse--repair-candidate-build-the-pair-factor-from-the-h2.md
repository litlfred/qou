---
# qou-rvse
title: 'Repair candidate: build the pair factor from the H2 Wedderburn split (isospin 2x2 = 3+1), not from crossing signs'
status: scrapped
type: task
priority: normal
created_at: 2026-08-30T10:32:43Z
updated_at: 2026-08-30T10:51:40Z
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



---

# 🛑 REFUTED, and by the corpus's own charge conjugation (2026-08-30)

Owner: *"derive the irrep-isospin assignment"*. It cannot be derived, because
**it cannot exist**. Lean, sorry-free, lean-direct exit 0:
`QOU/MassTheory/PairIsospinAssignment.lean`.

## The argument

`shell-schur-weyl-self-duality-proof.md` **step 4** fixes what charge
conjugation IS on the Hecke side, in the corpus's own words:

> *"On the Hecke side, the corresponding involution is tensoring with the sign
> representation V_{H_n}(1^n), which maps V_lambda -> V_{lambda*}."*

At **n = 2** the partitions of 2 are `(2)` and `(1,1)`, and `(2)* = (1,1)`.
**So C SWAPS the two blocks.**

Total isospin `T` is **C-invariant** — charge conjugation carries `|T,T3>` to
`|T,-T3>`, fixing `T`.

A C-invariant labelling of a two-element set whose C is the swap is
**constant** (`isospin_const_of_conj_invariant`). Hence
`no_conj_invariant_separating_label`: no C-invariant `T` gives the blocks
different values, so **none assigns (2) the triplet and (1,1) the singlet.**

The assignment is not merely underived. It **contradicts the corpus's own C.**

## The swap, concretely — and it exposes the real defect

Writing the H_2 relation inverse-free as `sigma^2 = h*sigma + 1` (`h = q - 1/q`),
the block swap is the algebra automorphism

    Phi(sigma) = h - sigma

(`heckeConj_isHecke` — it preserves the relation; `heckeConj_involutive`;
`eigen_swap` — it exchanges the eigenvalues `q` and `-1/q`). Verified
numerically: `h - q = -0.90091828395574149216 = -1/q` and `h + 1/q = q`, both
exact.

Push it through the Markov trace, where the corpus has `f_pp = tr(sigma) = z`
and `f_nn = z - h`:

    tr(Phi(sigma)) = h - z = -0.40362773835082593616 = **-f_nn**

**So C(f_pp) = -f_nn, not +f_nn.** Residual exactly 0.0. That missing sign is
the whole of the pair layer's parity defect measured in qou-1pig.

And `charge_symmetric_iff`: `f_pp = f_nn` **iff h = 0**, i.e. iff `q = 1/q`.
**The framework buys its q-deformation and its charge asymmetry with the same
parameter and cannot have one without the other.**

## Why there was never an isospin SU(2) at this level

Corpus-grepped. The corpus's `T_3` is defined in `spin-involution.md` as a
**Z/2 grading**: `T_3(a) = (1/2) sgn_sigma(a)`, `2 T_3 = sgn_sigma`. There is
no total-`T`, no Casimir, no `2 (x) 2 = 3 (+) 1` at the pair level.

And the corpus says so itself, in
`shell-schur-weyl-self-duality-interpretation.md`:

> *"Isospin doubling. Proton-neutron interchange symmetry emerges **at closed
> shells** via isospin SU(2) doubling."*
> *"Parity-violating phenomena arise at **level 3 (the inter-nucleon pair)**,
> where conjugate symmetry breaks via **skein asymmetry**. They do not appear at
> level 4 (the shell), where Schur-Weyl self-duality is exact."*

So isospin SU(2) is an emergent **level-4** structure; the pair is **level 3**,
where the corpus deliberately has only the Z/2. `prop:skein-crossing-asymmetry`
is the corpus's own name for the mechanism.

**Nothing here refutes that proposition.** It prices it: the level-3 charge
asymmetry it introduces is `h/2` in the bond factor, 1454x the isoscalar
splitting, and 2.29x the observed A=3 mirror splitting in energy.

## Status

**Scrapped as a repair route.** Scope-(b) exclusion with a named invariant
(C-invariance of total isospin) plus the corpus's own C. Do not re-propose
keying the pair factor on the H_2 block label.

The -7.8% 2H number recorded above is now **numerology** and must not be quoted
as support: its premise is refuted, and the three cautions listed with it
(underived assignment, one anchor, cheap re-assignment) were the right instinct.

## What survives, as the real question

The defect is not the pn averaging rule and not the block labelling. It is
`p |-> sigma, n |-> sigma^{-1}` — the identification of the nucleon's identity
with a **crossing sign**. Under the corpus's own C that map is not covariant:
C sends `sigma |-> h - sigma`, whose trace is `-f_nn`, not `f_nn`.

A repair has to change that identification, and the corpus's architecture says
where the isospin SU(2) actually lives: **level 4**. Whether a level-3 quantity
can inherit charge symmetry from a level-4 structure is the open question, and
it is qou-brng's neighbour, not its duplicate.



## Strengthened: the refutation now lives INSIDE the corpus's own carrier

Corpus-grepped my own new file and found `QOU/BraidKnot/ShellSchurWeylSelfDuality.lean`
already formalises the proof I was arguing from -- a `structure` with
`Partition`, `conj` (the transpose) and `conj_conj` (involutivity), plus
`SelfDual lam := conj lam = lam` and `selfDual_iff_fixed`.

So `PairIsospinAssignment` now **instantiates** it at n = 2 rather than
building a parallel construction beside it:

    def shellDuality : QOU.BraidKnot.ShellSchurWeylSelfDuality where
      Partition := Block ; conj := conj ; conj_conj := conj_involutive

    theorem no_selfDual (b : Block) : not (shellDuality.SelfDual b) := conj_ne b

**At n = 2 no block is self-dual.** The carrier defines a self-dual shell as a
fixed point of the transpose; at n = 2 the transpose has none. That is the sharp
form of the interpretation block's own claim that Schur-Weyl self-duality is
*exact at level 4* and broken at level 3 -- the pair has no self-conjugate
partition to carry it, and the corpus's own Lean now says so.

lean-direct exit 0 (72 s with the ShellSchurWeylSelfDuality cone, which pulls
Mathlib.Tactic); 0 sorry, 0 axiom. run-validate exit 0, 14 pre-existing issues.
