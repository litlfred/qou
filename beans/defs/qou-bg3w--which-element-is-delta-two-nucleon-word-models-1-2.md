---
# qou-bg3w
title: Which element is Delta? Two nucleon-word models (1-/2-crossing vs 11-crossing) both carry the name, and a possible third in pyhecke
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T15:47:38Z
updated_at: 2026-10-04T15:15:08Z
parent: qou-5vkl
---

Parent: `qou-cds1`. Surfaced by
`computations/qbeta/qbeta_delta_element_fork_pricing_probe.py` (15/15, exact
symbolic Q(q)) and
`docs/audits/2026-08-28-cds1-two-nucleon-word-models.md`.

## The question

`qbeta-counit-closed-form.md` names ONE object -- *"Delta = NF(n) - NF(p), the
single-wrap normal-form difference of the neutron and proton typed-crossing
elements in H_3(q)"* -- and asserts two closed forms for it,

    eps(Delta) = h^2/2 - h        tr_M(Delta) = h^2/2 - h*z .

TWO different elements of H_3(q) answer to that description, and BOTH closed
forms hold for the smaller and FAIL for the larger. Nobody has chosen.

| | Delta_S | Delta_L |
|---|---|---|
| source | `deuteron-binding-dressing-proton-net.md` net coefficients | `hecke_core._PROTON_G0/_G1` etc. |
| crossings | 1 (p), 2 (n) -- DERIVED, see below | 11 each |
| net(Delta) | h^2/2 - h = epsNPq = -0.187207 | -0.233198 |
| tr_M^z | h^2/2 - h z (AFFINE in z) | QUADRATIC in z |
| chi^(2,1) | 0 identically | -0.106814 |

Delta_S's crossing count is derived, not assumed: a typed crossing (sigma+d)
has net = 1+d and net is multiplicative across DISTINCT generators, so
net(n) = 1 - 3h/2 + h^2/2 = (1 - h/2)(1 - h) exactly. Delta_L's 11 matches
`q-beta-c3-hopf-three-fold-markov.md`'s *"both 11 typed crossings"*.

Mechanism: net is NOT multiplicative WITHIN one generator, because
T_0^2 = h T_0 + 1 reduces -- net(T_0^2) = 1+h vs net(T_0)^2 = 1. So an
11-crossing word cannot carry a 1-crossing coefficient. Structural, not a slip.

## Why it is load-bearing for qou-cds1

1. The D-frame trace baseline (`-15.451 %`, `92.1x the entire five-rung
   ladder`) takes its counit from Delta_S and its Markov trace from Delta_L.
   Priced consistently on Delta_S it is **257.26x** -- the published figure
   UNDERSTATES by 2.793x. (Calibrated: the probe reproduces the committed
   92.1058... exactly, which is what proves the attribution.)
2. qou-cds1's **(D1)** -- `2*alpha = net(Delta) - tr_M^z(Delta)`, the ONLY
   derivation of the ladder phase the corpus has -- is AFFINE in z only because
   Delta_S is supported on {gamma, sigma0, sigma1}. On Delta_L it is quadratic,
   so alpha = (z-1)h/2 is not the counit-minus-trace gap there at all.
   **If Delta_L is canonical, (D1) is unavailable** and branch 3
   (KZ / Kohno-Drinfeld holonomy) is the only remaining home for a derivation
   of alpha.

## A possible THIRD model -- FLAGGED, NOT CLAIMED

`pyhecke.atom.PROTON_NF` / `NEUTRON_NF` have coordinate sums 0.999125 and
0.810835, difference **-0.188291** -- within 0.58 % of epsNPq, matching neither
Delta_S (-0.187207 exactly) nor Delta_L (-0.233198).

Those constants are stored **float64** and I did **not** verify that pyhecke
uses the same basis ordering, so the coordinate sum may not be `net`. Check the
basis convention FIRST; do not treat -0.188291 as a measurement until then.

## Not the same question as qou-avt6 / qou-goc9

Those are about the **augmentation** (sigma -> q, an algebra map). This is
about the **coordinate sum** `net` (T_w -> 1), which is what epsNPq actually is
(qou-99qc) and what Q_A is computed from. Under `net` the element DOES exist --
it is Delta_S. Neither result implies the other; do not merge them.

## What would close this

An owner/corpus call on which element the decay channel is about, or a
derivation that selects one. Until then the D-frame re-derivation cannot be
posed, because the phase leg's status depends on the answer.


## 2026-08-29 — the "possible THIRD model" is RESOLVED, and there is a FOURTH

Probe: computations/qbeta/qbeta_d1_eleven_crossing_exclusion_probe.py (14/14).

**The basis-convention check this bean asked for is done.** It said: *"Those
constants are stored float64 and I did not verify that pyhecke uses the same
basis ordering... Check the basis convention FIRST; do not treat -0.188291 as a
measurement."*

Checked. PROTON_NF/NEUTRON_NF are the output of pyhecke.atom.build_nucleon_nf,
a **9-crossing** builder (3x(sigma_0, sigma_1^-1) = 6, plus 3 quark pairs; it
omits the gluon dressing deliberately — "No separate gluon dressing — B_3 IS
the gluon structure"). Its **exact** net is **-0.1883216147**. The stored
float64 coordinate-sum difference is -0.188290601. **The coordinate sum IS net**
and the residual is float64 h versus exact _H_FRAC. So the third model is real,
it is the 9-crossing one, and -0.188291 is its net. The flag can come off.

**A FOURTH construction exists and this bean conflates two of them.** There are
three long models in pyhecke.atom, not one:

     build_nucleon_nf     ( 9 crossings)      net = -0.1883216147
     build_atom_nf_exact  (11, interleaved)   net = -0.2272041420
     nucleon_gen_chains   (11, gen-grouped)   net = -0.2332458961

The two 11-crossing builders carry the SAME multiset of typed crossings and
differ only in ORDER — build_atom_nf_exact interleaves gen-0 and gen-1 within
the B_3 block, nucleon_gen_chains emits all gen-0 then all gen-1. H_3(q) is not
commutative across generators, so these are DIFFERENT ELEMENTS, and their nets
differ by 2.6 %. This bean's Delta_L (-0.233198) is the **gen-grouped** one, via
_PROTON_G0/_G1; the exact atom/mass pipeline uses the **interleaved** one.

So the question this bean asks — *which element is Delta?* — has **four**
candidates, not three, and two of them are 11-crossing.

**What this does NOT change:** (D1) is unavailable for all three long models.
The z^2 coefficient of tr_M is nonzero for each, with h = 0 as its only real
root, against a substrate at h ~ 0.209. Details in the cds1 tail. Note in
particular that **L+ vanishes exactly for this bean's Delta_L** — the exclusion
there rides on L-, not L+.

**Still open, and still the block on qou-cds1:** which element the decay channel
is about. The candidate set is now measured and priced, but nothing here selects
one.


## 2026-08-29 (LATER) — every decimal in the entry above was at q = 111/100

Caught by a SIBLING's numbers, not by re-reading my own. PR #5958 independently
measured the same elements and reported the gen-grouped net as -0.2331977;
mine said -0.2332458961. Agreement to 4 digits, which I would have called
confirmation — but a 2.1e-4 relative gap is ~18000x the 11.54 ppb mu-p
tension, so it had to be something else.

**`pyhecke.gram._H_FRAC` derives from `_Q_FRAC = Fraction(111, 100)`** — q =
1.11 exactly, a deliberate exactness device ("H_3(q) at q = 111/100 is exact in
Q"). It is **185 ppm** off the substrate pin.

Contained, and checked before calling it anything: `_H_FRAC` / `_Q_FRAC` /
`hm_exact` / `build_atom_nf_exact` have 12 importers and the ONLY one emitting
a witness is under `_deprecated/`; `computations/lint_q_approximation.py`
already guards the class. Not a production leak — the defect was mine, reading
it as the substrate.

### Corrected table, and it makes every identification STRONGER

                       quoted at 111/100    at the substrate pin   vs recorded
  Delta_S               -0.187237882         -0.187207194529        -0.187207     4 -> 6 digits
  9-crossing            -0.188321615         -0.188290601471        -0.188290601  4 -> NINE
  11 interleaved        -0.227204142         -0.227159711766        (no record)
  11 gen-grouped        -0.233245896         -0.233197711316        -0.233198     4 -> 6
                                                                    (#5958: -0.2331977, 9 digits)

**The 9-crossing row settles this bean's open question.** The entry above
explained its residual as "float64 h vs exact _H_FRAC". That was wrong and
there was no residual: at the substrate pin the exact net matches the stored
float64 PROTON_NF/NEUTRON_NF coordinate-sum difference to NINE significant
figures. **The coordinate sum IS net** — conclusion unchanged, stated reason
replaced.

The symbolic exclusions are untouched: they are polynomial identities in h and
never depended on a pin.

### The candidate set is larger than either of us had

#5958's candidates come from CONTENT BLOCKS, mine from PYHECKE CODE PATHS, and
only the two endpoints overlap. Union:

  Delta_S (short model)                        -0.187207194529
  build_nucleon_nf (9 crossings)               -0.188290601471
  categorical-* as STATED                      -0.2089        (#5958)
  categorical-* recipe as CONSTRUCTED k=1      -0.2137638     (#5958)
  build_atom_nf_exact (11, interleaved)        -0.227159711766
  hecke_core / nucleon_gen_chains (11, grouped) -0.233197711316

**Six**, not four, and not two. Still unadjudicated; still an owner call.


## 2026-08-29 (LATER STILL) — L+ and L- were reported SWAPPED

PR #5958 caught it, by the strongest evidence available: they transcribed the
SAME element independently and published all six NF components. Every value
agrees — with slots 3 and 4 exchanged.

`gram.py` is the canonical owner:

    NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]
    NF_NAMES = ["gamma","sigma_0","sigma_1","L+","L-","e^-"]

so canonical L+ = sigma_0 sigma_1 at index 3. But `hm_sym` puts sigma_0 sigma_1
in slot **4** and sigma_1 sigma_0 in slot **3**. My probe reused NF_NAMES
positionally and printed them backwards. Now pinned by `_assert_slots()`, which
builds both words and asserts where they land.

**Corrected claim.** The entries above say "L+ is exactly 0 for Delta_L, so the
exclusion rides on L-". In canonical naming it is the REVERSE: **L- (sigma_1
sigma_0) vanishes; the exclusion rides on L+.**

**The exclusion is untouched.** The z^2 coefficient is d[L+] + d[L-] + h*d[e^-],
SYMMETRIC in the two slots because TR weights both with z^2. A 3<->4 swap cannot
move it. Every verdict and every polynomial stands.

**Confirmed independently, and worth keeping:** e^- is identically 0 for BOTH
nucleons in the gen-grouped model — I get this, and #5958 reports the same from
the other side. So the whole z(hz+1) term drops out of tr_M(Delta_L); the L
coordinates alone carry the z^2 there.

### Four corrections to one probe in one day

nine-crossing element called eleven; the wrong invariant; decimals at
q = 111/100; swapped basis labels. Each caught by evidence rather than
re-reading, three of four by measuring against something external, and NONE of
them moved the conclusion. That is not luck: the verdict rests on a symmetric
sum over the two L slots plus a degree argument in h, and no error of this
class can reach either.


## 2026-08-29 — the last two candidates are priced; the fork IS binary

`computations/qbeta/qbeta_d1_categorical_candidates_probe.py` (5/5). This bean
listed six candidates with (D1) measured for four. The two `categorical-*` ones
are now done, and the two are not the same kind of object:

* **"as STATED" (-0.2089) is not an element.** It is the difference of two
  QUOTED NUMBERS — net(p) = 1.0065 and net(n) = 0.7976, at 5 and 4 significant
  figures. There is no word, so no NF vector, so no tr_M. **(D1) is not
  ill-behaved for it; it is NOT WELL-POSED.** A stated net is a target the
  content blocks assert, not something one can trace. It should be struck from
  the candidate list as a category error rather than carried as a sixth option.

* **"as CONSTRUCTED (k=1)" (-0.2137638) is an element, and is EXCLUDED:**

      [z^2] tr_M = -(q-1)^3 (q+1)^3 (3q^8 - 5q^6 + 5q^4 - 5q^2 + 3) / (4 q^7)

  The octic has **no real root** (exact Sturm count 0), so the only real roots
  are q = ±1, both h = 0, against a substrate h ~ 0.209. Scope-(b), invariant
  cited — the same degree argument that excludes the three pyhecke models.

**Consequence for the decision.** Five of six are priced and the sixth is a
category error, so the candidate set collapses: **Delta_S is the only element
carrying (D1)**. The fork is binary after all — Delta_S, or no (D1) at all and
branch 3 (KZ / Kohno-Drinfeld holonomy) as the only remaining home for a
derivation of alpha. Nothing here selects between those two; that is still the
owner call this bean exists for. What is gone is the possibility that a third
route was hiding in the unmeasured candidates.

Method note: exact symbolic in h/q, no float64, and **no q0 substitution** —
the verdict is a statement about a polynomial, not about a pin. That is what
makes it immune to all four correction classes in this bean's history (a
9-crossing element called eleven; the wrong invariant; decimals silently at
q = 111/100; swapped basis labels).

Caught in this probe before it shipped: the root check first read
`solve(c1, h)` while the coefficient comes back in **q**, so it returned `[]`
and **passed vacuously**. Now solves in q and maps through h = q - 1/q, with an
exact Sturm count on the octic where a nonzero-h root could have hidden.



## 2026-09-03 — the 92.1058x is BRACKETED by the two consistent ratios, not understated

`computations/qbeta/qbeta_d_frame_baseline_element_consistency_probe.py` (5/5,
sympy exact at the 50-digit q_0 as a Rational, no float64).

This bean records the straddle as *"priced consistently on Delta_S it is
257.26x -- the published figure UNDERSTATES by 2.793x"*. Both halves reproduce
exactly (257.26025 and 2.79309x). **But the understatement figure is itself
Delta_S-conditional, and the bean does not say so.** Priced on Delta_L the same
published number OVERSTATES by 147.688x:

    element     counit (net)              trace at z_D            ratio
    Delta_S     -0.1872071945   +0.1678 % -0.1062356398  -43.157 %  257.260
    published   -0.1872071945   +0.1678 % -0.1580160043  -15.451 %   92.106
    Delta_L     -0.2331977113  +24.776 %  -0.1580160043  -15.451 %    0.6237

The two consistent ratios BRACKET the published one, strictly. So it is not an
approximation to either with a correction factor -- a cross-element ratio does
not have one, and quoting "2.793x" silently fixes the element. Same shape as
the four corrections this bean already collects: a quantity true relative to
one choice, reported as though the choice were not being made.

Two things established on the way, both checked rather than assumed:

* **The two trace routes are ONE functional.** The baseline probe's Frobenius
  pairing `sum_lambda y_lambda(q, N=2) chi^lambda` and the Markov trace at
  `z_D` agree on Delta_L to better than 1e-40 (-0.158016004341491298 both). That
  is what licenses pricing Delta_S's trace from its recorded closed form
  `h^2/2 - h z` instead of guessing a word for it.
* **The straddle took the flattering half of each element** -- Delta_S carries
  the corpus's best counit (+0.168 % against Delta_L's +24.8 %) and Delta_L the
  better of the two traces (-15.5 % against -43.2 %). No intent alleged: the
  counit is a hardcoded closed form and the trace is built from an imported
  word, so the two halves were never in one place to be compared. That is why
  it survived review.

**Not fixed, deliberately:** the 92.1058 in `qbeta_d_frame_trace_baseline_probe`
is left intact, because it is what `qbeta_delta_element_fork_pricing_probe`
calibrates against. The producer now carries a docstring banner naming which
element each half is on. The fix for a straddle is to say which element, not to
move a number consumers key on.

## 2026-09-03 — and (D1) on Delta_S derives the form that is already excluded

Not stated in this bean or in qou-cds1, and it changes what the fork decides.

From this bean's own recorded closed forms, `net(Delta_S) = h^2/2 - h` and
`tr_M^z(Delta_S) = h^2/2 - h z`, the (D1) relation gives

    2 alpha = net - tr_M^z  =>  alpha = h(z-1)/2 = (z-1)h/2

**identically** -- which is exactly the single-wrap eigenphase axiomatised at
`q-beta-cos-resummation.ts:48`, and exactly the functional form PR #6264
excluded EXHAUSTIVELY over the admissible set `{q, z_D}` (z_D misses by 1087
windows; z = q is excluded structurally, since alpha < 0 forces z < 1 while
q > 1 always).

So the fork's two arms are not "a derivation of alpha" versus "none":

* **Delta_S canonical** -> (D1) available -> it derives the refuted form, and
  the axiom becomes a *derived-and-refuted* claim rather than an unsupported
  one.
* **any long model canonical** -> (D1) unavailable (quadratic in z, only real
  root h = 0) -> the axiom stays unsupported, and qou-cds1's terminus already
  records that no route to alpha is known to be open.

Either way alpha is undetermined in that form. What the owner call decides is
which of those two the corpus records -- which is a smaller decision than this
bean was carrying, and worth knowing before spending it.

Recorded on `prop:qbeta-counit-closed-form` as an authorNote, together with a
caveat that `Delta = NF(n) - NF(p)` as written there does not name a unique
element (six constructions answer to it; five priced, one struck as a category
error). Consumers must name their builder.

Scope-(a) throughout. No observable moves -- not Q_beta, not a mass, not a
binding, not L2.



## 🛑 CORRECTION 2026-09-12 (from PR #7212) — the "exact vs float64" attribution in this bean is REFUTED

This bean states: *"Its **exact** net is **-0.1883216147**. The stored float64
coordinate-sum difference is -0.188290601. The coordinate sum IS net and the
residual is float64 h versus exact _H_FRAC. So the third model is real, it is
the 9-crossing one, and -0.188291 is its net. The flag can come off."*

The CONCLUSION is right — the third model is real, it is the 9-crossing one,
and the coordinate sum IS net. **The stated REASON is wrong, and so is the
figure called "exact".**

BOTH of those numbers are exact. They are at DIFFERENT q:

  -0.18832161472187   at q = 111/100      <- what this bean calls "exact"
  -0.18829060147138   at the proton pin   <- what this bean calls "float64"

Float64 rounding shows at ~1e-16, not the 1.6e-4 seen here. The gap is the
185 ppm `_Q_FRAC` device in `pyhecke.gram` (q = 111/100, an exactness choice
that is ~16000x the 11.54 ppb mu-p tension), NOT float64 arithmetic.

This was already diagnosed on 2026-09-04 in
`docs/audits/2026-09-04-delta-net-canon-and-crossing-count-analysis.md` §(ii),
which names it "the same 185 ppm `_Q_FRAC` trap", and is asserted in
`qbeta_delta_candidate_census_probe`'s check
`bg3w_nuc9_residual_is_the_pin_not_float64`. The correction never reached this
bean.

THE TABLE IN THIS BEAN IS AT q = 111/100. All three figures:

  model                                quoted (q=111/100)   substrate proton
  build_nucleon_nf     ( 9 crossings)  -0.1883216147        -0.1882906015
  build_atom_nf_exact  (11, interl.)   -0.2272041420        -0.2271597118
  nucleon_gen_chains   (11, gen-grp)   -0.2332458961        -0.2331977113

Cross-check that fixes them: the gen-grouped substrate figure is the
calibration constant `qbeta_option_e_order_dof_range_probe` (merged) asserts at
1e-30, -0.23319771131565870204...

Also corrected 2026-09-12 in `qbeta_d1_eleven_crossing_exclusion_probe`'s
docstring table (commit 4694165f19), which carried the same three 1.11 figures
while its own runtime assertion printed the substrate value — the earlier fix
had reached that probe's code and not its prose.

NOT closing this bean; only recording the correction. Status left as the owning
agent set it.

In-progress in Round 101 PR litlfred/qou#8450.
