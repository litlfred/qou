---
# qou-5d6k
title: 'GAP-1 (cheapest): 2H per-bond defect - derived colour weight gives t=0.4997, target needs t=0.1195'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T16:43:39Z
updated_at: 2026-10-04T15:19:34Z
parent: qou-10v9
---

## 2026-08-25 (PR #5765) — REACHABLE is not DERIVABLE. Downgrading my own recommendation.

I proposed this as "the cheapest genuine derivation item in the corpus". That was
**too optimistic** and I am correcting it. The reachability result is real; the
conclusion I drew from it was not.

### What IS confirmed (reproduced independently, 50 dps)

Bean `qou-kj4v`'s convention-D reachability numbers reproduce to 9 digits:

    required mu = 0.587715064111    (bean: 0.5877150637)
    required d  = -0.0249729730357  (bean: -0.02497297346)
    d_req / h   = -0.119453446      (bean: -0.119453)
    admissible d in [-h, 0] = [-0.2090603, 0]   -> INSIDE

against the derived `d_der/h = -t_der = -0.499656072298`. Under convention C the
whole band sat below the target and this was impossible; under D it is not.
That is a genuine convention-D gain and it stands.

### What FORBIDS closing it by choosing d

Three results, all already in the corpus, that I did not weigh when I recommended
this:

1. **`content_keyed_interface_refuted`** (`InterfaceScalar.lean:507`). Nature has
   **FOUR** two-nucleon channels, not three:

       pn 3S1 deuteron  S=1 T=0  B = +2.224566  BOUND
       pn 1S0 virtual   S=0 T=1  B = -0.066     unbound
       pp 1S0           S=0 T=1  B ~ -0.1       unbound
       nn 1S0           S=0 T=1  B ~ -0.1       unbound

   The two `pn` rows have the **same nucleon content and opposite boundness**. Any
   `m_pp/m_pn/m_nn` assignment is a function of content, so it necessarily gives
   them the same energy. **No choice of the weights can work** — the defect is in
   what the multiplicities are allowed to depend on, not in their values.

2. **The exact flavour-only degeneracy.** In S-wave, Pauli locks spin to isospin
   (space symmetric => spin and isospin symmetry opposite): S=1 <=> T=0,
   S=0 <=> T=1. A Pauli-consistent interface carries a projector in EACH SU(2), and
   I verified at 50 dps:

       mu(3S1) = mu+^spin * mu-^iso = 0.18614164195799085217
       mu(1S0) = mu-^spin * mu+^iso = 0.18614164195799085217
       difference                   = 0.0   EXACTLY

   because multiplication commutes. **A flavour-only interface cannot split 3S1
   from 1S0 at all, whatever the functional.** In the SM that split is the tensor
   force (3S1-3D1 mixing), a spin-SPACE coupling; the Hecke interface has one index
   (the strand) and no space index to carry it.

3. **Both channels necessarily bind.** `mu+ + mu- = 1` exactly (verified), so
   projection only REMOVES trace weight => `mu_T < 1` => `B_T > 0` for both T. The
   projector decomposition can never produce an unbound channel. Unbinding needs
   `mu > 1`, i.e. leaving the convex decomposition (`stacked_crossing_gt_one`:
   sigma^2 gives mu = h*z+1 = 1.12809).

The bean states the consequence plainly: *"m_pp/m_pn/m_nn left at 1. Nothing here
licenses changing them, **and the refutation says nothing ever will**."*

### Corrected status

Tuning `d_pn` from 0.4997 to 0.1195 to land the deuteron **would be a fit**, and one
the corpus has already refuted structurally rather than merely left unfitted. It is
barred by the anti-fit discipline and by `content_keyed_interface_refuted`.

So GAP-1 is **not** a cheap tuning item. It is: *the target is now inside the band
(D gain), and there is a proved obstruction to reaching it for the right reason with
a flavour-only interface.*

`qou-kj4v` also records that nature's T=1 sits at -0.066 MeV from an unnaturally
large scattering length (a_s ~ -23.7 fm) — a near-critical fixed point, i.e.
fine-tuning rather than symmetry. **Both halves of the residual are dynamical, not
representational.**

### The actual open lever
A **SPACE index on the interface** — something carrying L, so 3S1-3D1 mixing has
somewhere to live. Until then the NN sector is sign-correct and magnitude-wrong
**by construction**, not by accident.

(Sign-correctness is itself derived and worth keeping: `2z - h = (q^4+1)/(q(q^2+1))`
is positive for all q>0, so `mu- < mu+` => the isospin singlet is always the more
bound channel — the deuteron-vs-pp/nn ordering, forced, no crossing count, no tuning.
`two_z_sub_h_conventionD`, `mu_singlet_lt_mu_triplet`, `singlet_binds_more`.)

### Scope
Item 1 is scope-**(b)** — a structural exclusion with the invariant cited (content is
constant across the two pn channels while boundness is not). Item 2 is scope-**(b)**
with the invariant being commutativity of the two projector scalars. Item 3 is
scope-**(b)** on `mu+ + mu- = 1`. These exclude the *flavour-only content-keyed route*,
not the deuteron.

Note: `InterfaceScalar.lean` carries 1 `sorry`; I did not check whether it is on this
chain. Lean compilation UNVERIFIED (no build in this container; the QOU target's last
recorded status is FAIL, 79 days old).

## Progress Update (PR litlfred/qou#8238)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8238 (`dcfad8a84dddbefde9a4efb59eba72ba663b1d84`, scriptCommitSha `2b4b5612016793df004e2f2990d7681285f78653`)
- **Summary**: Added `mu_singlet_closed_form_conventionD`, `mu_triplet_closed_form_conventionD`, and `stacked_crossing_trace_conventionD` in `QOU/QBeta/InterfaceScalar.lean`, verified by 80-dps mpmath probe `interface_kappa_geodesic_em_connsum_probe.py` (`scriptHash: 5c337ec3fbc3`).
